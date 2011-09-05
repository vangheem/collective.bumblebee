

def getHost(request):
    base1 = request.get('BASE1')
    _, base1 = base1.split('://', 1)
    host = base1.lower()
    return host, request.get('SERVER_PORT')


def isThemeEnabled(request, settings):
    """Determine if a theme is enabled for the given request
    """

    # Disable theming if the response sets a header
    if request.response.getHeader('X-Theme-Disabled'):
        return False

    # Check for diazo.off request parameter
    if request.get('b.off', '').lower() in ('1', 'y', 'yes', 't', 'true'):
        return False

    if not settings.enabled or not settings.rules:
        return False

    host, port = getHost(request)

    for hostname in settings.hostnameBlacklist or ():
        if host == hostname or host == "%s:%s" % (hostname, port):
            return False

    return True
