.. _addondeps:

Known Limitations
=================

There are several known limitations to consider when using pip4blender.

Updating Bundled Libraries
--------------------------

Pip4Blender should not be used to update libraries that came bundled with Blender.
This has the potential to permanently damage your Blender installation.

Installing C Modules
--------------------

C Modules which include the 'Python.h' header will fail.  The bundled Python
installation does not include the source files for Python, making this rather
difficult.  Support for this is not planned at this time.
