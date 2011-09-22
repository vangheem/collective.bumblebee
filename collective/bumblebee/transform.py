from zope.interface import Interface, implements
from zope.component import adapts, queryUtility, getUtility

from plone.registry.interfaces import IRegistry
from plone.transformchain.interfaces import ITransform
from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

from repoze.xmliter.utils import getHTMLSerializer
from lxml import etree

from collective.bumblebee.interfaces import IThemingLayer, IThemeSettings
from collective.bumblebee.utils import isThemeEnabled, getHost
from bumblebee.xml import convertRules
from bumblebee import transform
from Acquisition import aq_parent

from collective.bumblebee.conditions import IfPath
from collective.bumblebee.conditions import IfTal
from collective.bumblebee.selectors import PageTemplateSelector
from collective.bumblebee.selectors import TalSelector

from bumblebee.xml import addCondition
from bumblebee.xml import addSelector

addCondition('path', IfPath)
addCondition('tal', IfTal)
addSelector('pt', PageTemplateSelector)
addSelector('tal', TalSelector)
_rule_cache = {}


class ThemeTransform(object):
    """Late stage in the 8000's transform chain. When plone.app.blocks is
    used, we can benefit from lxml parsing having taken place already.
    """

    implements(ITransform)
    adapts(Interface, IThemingLayer)

    order = 8851

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def getSettings(self):
        registry = queryUtility(IRegistry)
        if registry is None:
            return None

        try:
            settings = registry.forInterface(IThemeSettings, False)
        except KeyError:
            return None

        return settings

    def _getRules(self, settings, fromcache=True):
        if fromcache:
            key = "%s:%s" % getHost(self.request)
            if key in _rule_cache:
                rules = _rule_cache[key]
            else:
                rules = convertRules(settings.rules)
                _rule_cache[key] = rules
            return rules
        else:
            return convertRules(settings.rules)

    def getRules(self, settings):
        fromcache = True
        if settings.development_mode:
            fromcache = False
        elif 'b.reload' in self.request:
            key = "%s:%s" % getHost(self.request)
            if key in _rule_cache:
                portal = getSite()
                membership = getToolByName(portal, 'portal_membership')
                if membership.checkPermission('Manage portal', portal):
                    del _rule_cache[key]

        return self._getRules(settings, fromcache)

    def parseTree(self, result):
        contentType = self.request.response.getHeader('Content-Type')
        if contentType is None or not contentType.startswith('text/html'):
            return None

        contentEncoding = self.request.response.getHeader('Content-Encoding')
        if contentEncoding and \
                contentEncoding in ('zip', 'deflate', 'compress',):
            return None

        try:
            return getHTMLSerializer(result, pretty_print=False)
        except (TypeError, etree.ParseError):
            return None

    def transformString(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformUnicode(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformIterable(self, result, encoding):
        """Apply the transform if required
        """

        result = self.parseTree(result)
        if result is None:
            return None

        settings = self.getSettings()
        if not isThemeEnabled(self.request, settings):
            return result

        rules = self.getRules(settings)
        context = aq_parent(self.published)
        return transform(result, rules, extras={
            'request': self.request,
            'published': self.published,
            'context': context,
            'here': context,
            'object': context
        })
