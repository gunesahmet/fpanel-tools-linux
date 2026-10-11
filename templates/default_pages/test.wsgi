def tag(t, **k):
    kk = ''.join(' %s=%r' % kv for kv in k.items())
    format = '<%s%s>%%s</%s>' % (t, kk, t)
    return lambda content: format % content

def table(d):
    from cgi import escape
    escq = lambda s: escape(s, quote=True)
    tr = tag('tr')
    th = tag('th')
    td_code = lambda content: tag('td')(tag('code')(content))
    return tag('table', border='1')(''.join((
        '\n\t' + tr(th('Key') + th('Value') + th('Repr')) + '\n',
        ''.join(('\t' + tr(td_code('%s') + td_code('%s') + td_code('%s')) + '\n') % (k, escq(str(v)), escq(repr(v))) for k, v in sorted(d.items())),
    ))) + '\n'

def application(environ, start_response):
    import os
    l = []
    from wsgiref.headers import Headers
    h = Headers(l)
    h.add_header('Content-Type', 'text/html')
    start_response('200 OK', l)
    yield '<html><head><title>my mod_wsgi test page</title></head><body>\n'
#    yield '<h3>General information</h3>\n'
#    yield table({})
    yield '<h3>Process info</h3>\n'
    yield table(dict(
        wd=os.getcwd(),
        pid=os.getpid(),
        ppid=os.getppid(),
        uid=os.getuid(),
        gid=os.getgid(),
    ))
    yield '<h3>Environment</h3>\n'
    yield table(environ)

