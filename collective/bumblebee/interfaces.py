from zope.interface import Interface
from zope import schema

from zope.i18nmessageid import MessageFactory
_ = MessageFactory(u"plone")


class IThemingLayer(Interface):
    pass


class IThemeSettings(Interface):
    enabled = schema.Bool(
        title=_('enabled', u"Enabled"),
        required=True,
        default=False,
    )

    development_mode = schema.Bool(
        title=_('development_mode', 'Development Mode'),
        required=True,
        default=True
    )

    rules = schema.Text(
        title=_('rules', u'Rules'),
        description=_('rules_description', u'XML rules definition.'),
        required=True,
        default=u"""<xml>\n\n</xml>"""
    )

    hostnameBlacklist = schema.List(
        title=_('hostname_blacklist', u"Unthemed host names"),
        description=_('hostname_blacklist_description',
            u"If there are hostnames that you do not want to be themed, "
            u"you can list them here. This is useful during theme "
            u"development, so that you can compare the themed and unthemed "
            u"sites. In some cases, you may also want to provided an "
            u"unthemed host alias for content administrators to be able "
            u"to use 'plain' Plone."),
        value_type=schema.TextLine(),
        required=False,
        default=[u"127.0.0.1"],
    )
