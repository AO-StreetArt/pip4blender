.. _addondeps:

Developing with Pip4Blender
===========================

Developers creating new Add-ons will benefit the most from pip4blender.  During
initial development, developers can install libraries as needed, one-by-one.  This
reduces the overall cost of development by promoting use of solid, well-tested,
third-party libraries instead of the same code re-written over and over again.

.. image:: _images/Install_Library.png

Once an add-on is complete (enough) to release to the public, a requirements.txt
file can be generated, which specifies the name and version of all dependent
packages.

.. image:: _images/Generate_ReqFile.png

This will write all 3rd party libraries currently installed from pip4blender to
a file specified in a file browser, which can then be packaged along with an add-on.

Users who have pip4blender installed can hit the 'Install Requirements File'
button, which will open a filebrowser to select the requirements file supplied
by the developer.

.. image:: _images/Install_ReqFile.png
