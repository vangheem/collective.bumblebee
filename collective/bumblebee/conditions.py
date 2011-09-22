from bumblebee.conditions import BaseIf
from Products.CMFCore.Expression import Expression, getExprContext


class IfPath(BaseIf):

    def __init__(self, path):
        self.path = path

    def __call__(self, root, extras={}):
        req = extras.get('request')
        if not req:
            return False
        path = req['PATH_INFO']
        if self.path.startswith('/'):
            return path.startswith(self.path)
        else:
            return self.path in path


class IfTal(BaseIf):

    def __init__(self, expression):
        self.expression = Expression(expression.strip())

    def __call__(self, root, extras={}):
        context = extras.get('context')
        expr_context = getExprContext(context, context)
        try:
            return bool(self.expression(expr_context))
        except:
            return False
