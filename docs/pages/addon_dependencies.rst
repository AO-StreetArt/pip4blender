.. _addondeps:

Developing with Pip4Blender
===========================

Developers creating new Add-ons will benefit the most from pip4blender.  During
initial development, developers can install libraries as needed, one-by-one.  This
reduces the overall cost of development by promoting use of solid, well-tested,
third-party libraries instead of the same code re-written over and over again.

Once a developer is complete (enough) to release the add-on to the public, they
can also distribute a requirements.txt file, which specifies the name and version
of all dependent packages.

Then, users can hit the 'Install Requirements File' button, which will open a
filebrowser to select the requirements.txt file supplied by the developer.

.. image:: _images/Install_ReqFile.png  
