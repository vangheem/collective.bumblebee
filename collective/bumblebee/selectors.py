from bumblebee.selectors import Base
from Products.CMFCore.Expression import Expression, getExprContext
from lxml.html import fromstring
from lxml.html import tostring
from lxml.html import HtmlElement
from zope.pagetemplate.pagetemplatefile import PageTemplate


class PT(PageTemplate):

    def pt_getContext(self, args=(), options={}, **kw):
        rval = PageTemplate.pt_getContext(self, args=args)
        options.update(rval)
        return options


class PageTemplateSelector(Base):

    def __init__(self, name, node):
        self.pt = PT()
        html = ''.join([tostring(n) for n in node.getchildren()])
        self.pt.write(html)

    def __call__(self, node, extras={}):
        try:
            result = fromstring(self.pt(**extras))
            if type(result) == HtmlElement:
                return [result]
            return result
        except:
            raise


class TalSelector(Base):

    def __init__(self, tal, node):
        self.expression = Expression(tal.strip())

    def __call__(self, node, extras={}):
        context = extras.get('context')
        expr_context = getExprContext(context, context)
        try:
            result = fromstring(self.expression(expr_context))
            if type(result) == HtmlElement:
                return [result]
            return result
        except:
            return []
