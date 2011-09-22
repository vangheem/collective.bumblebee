Introduction
============

collective.bumblebee is a very simple integration package 
of the bumblebee output transformation framework.

To configure your rules, edit the IThemeSettings.rules settings
in the configuration registry.

Read the bumblebee documentation at https://github.com/vangheem/Bumblebee
on how to create your rule xml.

Extra Selectors
---------------

pt
~~

Render a page template inline::

    <after src-pt="" dst="#foo">
        <h1 tal:content="context/Title" />
    </after>


Available attributes in page templates are: context, here, object, published, request


tal
~~~

    <after src-tal="context/Title" dst="#foo" />


Available attributes in tal expressions are: here, object, published, request, folder, portal


Extra Conditions
----------------

if-path
~~~~~~~

It also add an extra condition if-path::

    <drop src="#foo" if-path="/foo/bar" />

or::

    <drop src="#foo" if-not-path="/foo/bar" />


if-tal
~~~~~~

Use tal and python expressions for if statement::

    <drop src="#foo" if-tal="here/@@plone_context_state/is_portal_root" />

    <drop src="#foo" if-tal="python: 'foobar' in here.Title()" />

    <drop src="#foo" if-not-tal="python: 'foobar' in here.Title()" />


Available attributes in tal expressions are: here, object, published, request, folder, portal


Development Tips
----------------

Turn bumblebee off
    Append "?b.off=1" onto any url to not apply rules.

Reload rules(for production)
    Append "?b.reload=1" onto any url and be logged in as admin.
