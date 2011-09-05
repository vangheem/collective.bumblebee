from bumblebee.conditions import BaseIf


class IfPath(BaseIf):

    def __init__(self, path, extras={}):
        super(IfPath, self).__init__(extras)
        self.path = path

    def __call__(self, root):
        req = self.extras['request']
        path = req['PATH_INFO']
        if self.path.startswith('/'):
            return path.startswith(self.path)
        else:
            return self.path in path
