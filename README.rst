Pip4Blender
===========

Overview
--------

This is a Blender Add-on which enables support for using pip (the standard
Python Package Manager) from within Blender.

Blender utilizes a bundled Python implementation, which does not include pip.  Because
of this, it is actually quite difficult to install third-party libraries and packages
into the Blender Python Implementation.

This issue makes developing Blender Add-ons far more difficult, because developers
cannot use tried-and-true 3rd party libraries, and are forced to write the same code
over and over for each add-on that needs it.

Pip4Blender makes this just as easy as installing normal add-ons, and supports a
developer-centric workflow designed to make building and distributing add-ons with
dependencies as simple as possible.

Features
--------
* Install Pip into the Blender Python installation from the Blender UI
* Use pip to install specific libraries from the Blender UI
* Import requirements.txt files from the Blender UI
* Generate requirements.txt files from the Blender UI
* Compatible with all Blender versions using Python3 (ie. since Blender 2.5)
* Compatible with all major Operating Systems (Windows, Mac, Linux)

License
-------

PyAesel is licensed under the MIT license.
For further details, please refer to the LICENSE file.

Contact
-------

If you believe that you have found a bug in Pip4Blender, or have an enhancement request,
we encourage you to raise an issue on our `github page <https://github.com/AO-StreetArt/pip4blender>`__.
