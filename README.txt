Introduction
============

collective.bumblebee is a very simple integration package 
of the bumblebee output transformation framework.

To configure your rules, edit the IThemeSettings.rules settings
in the configuration registry.

Read the bumblebee documentation at https://github.com/vangheem/Bumblebee
on how to create your rule xml.


It also add an extra condition if-path::

    <drop src="#foo" if-path="/foo/bar" />

or::

    <drop src="#foo" if-not-path="/foo/bar" />


Development Tips
----------------

Turn bumblebee off
    Append "?b.off=1" onto any url to not apply rules.

Reload rules(for production)
    Append "?b.reload=1" onto any url and be logged in as admin.