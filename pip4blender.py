"""
The MIT License (MIT)

Copyright (c) 2015 Alex Barry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@author: AO Street Art
"""

bl_info = {
    "name": "Pip4Blender",
    "author": "AO Labs",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "description": "Blender Add-on to support installing Python Libraries via pip",
    "category": "Development",
}

import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty, CollectionProperty
import os, platform
from subprocess import call, STDOUT
import urllib.request
from pathlib import Path

def find_python_executable():
    # Find the location of the python executable
    os_install_location = Path(os.__file__)
    python_path = None
    base_path = (os_install_location.parents[0] / "..")
    if platform.system() == "Windows":
        full_path = (base_path / "bin" / "python.exe")
        python_path = '"%s"' % full_path
    else:
        python_path = (base_path / ".." / "bin" / "python3.5m")
    print("Found Python Executable: %s" % python_path)
    return python_path

# Install Pip for Blender's Python interpreter
class InstallPip(bpy.types.Operator):
    bl_idname = "object.install_pip"
    bl_label = "Install Pip in Blender"
    bl_options = {'REGISTER'}
    file_path = bpy.props.StringProperty(name="File Path", default="")

    # Called when operator is run
    def execute(self, context):
        print("Installing Pip in Blender")

        # Get the get-pip script
        get_pip_path = Path.home() / "get-pip.py"
        urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "%s" % get_pip_path)
        # Find the location of the python executable
        executable_location = find_python_executable()
        # Call get-pip with the blender python executable
        get_pip_command = "%s %s --user" % (executable_location, get_pip_path)
        call(get_pip_command, shell=True)

        # Let's blender know the operator is finished
        return {'FINISHED'}

# Install Python packages from Blender
class GenerateRequirementsFile(bpy.types.Operator):
    bl_idname = "object.generate_requirements_file"
    bl_label = "Generate Requirements File"
    bl_options = {'REGISTER'}
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    # Called when operator is run
    def execute(self, context):
        req_file = self.filepath
        print(req_file)
        if (req_file != ""):
            print("Generating Requirements file")

            # Find the location of the python executable
            executable_location = find_python_executable()

            # Call get-pip with the blender python executable
            pip_install_command = "%s -m pip freeze > %s" % (executable_location, req_file)
            call(pip_install_command, shell=True)

        # Let's blender know the operator is finished
        return {'FINISHED'}

    def invoke(self, context, event):

        context.window_manager.fileselect_add(self)
        #Open browser, take reference to 'self'
        #read the path to selected file,
        #put path in declared string type data structure self.filepath

        return {'RUNNING_MODAL'}
        # Tells Blender to hang on for the slow user input

# Install Python packages from Blender
class InstallRequirementsFile(bpy.types.Operator):
    bl_idname = "object.install_requirements_file"
    bl_label = "Install Requirements File"
    bl_options = {'REGISTER'}
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    # Called when operator is run
    def execute(self, context):
        req_file = self.filepath
        print(req_file)
        if (req_file != ""):
            print("Installing Python packages from requirements file")

            # Find the location of the python executable
            executable_location = find_python_executable()

            # Call get-pip with the blender python executable
            pip_install_command = "%s -m pip install -r %s" % (executable_location, req_file)
            call(pip_install_command, shell=True)

        # Let's blender know the operator is finished
        return {'FINISHED'}

    def invoke(self, context, event):

        context.window_manager.fileselect_add(self)
        #Open browser, take reference to 'self'
        #read the path to selected file,
        #put path in declared string type data structure self.filepath

        return {'RUNNING_MODAL'}
        # Tells Blender to hang on for the slow user input

# Install Python packages from Blender
class InstallPythonLibrary(bpy.types.Operator):
    bl_idname = "object.install_python_library"
    bl_label = "Install Python Library"
    bl_options = {'REGISTER'}

    # Called when operator is run
    def execute(self, context):
        addon_prefs = context.user_preferences.addons[__name__].preferences
        pkg_name = addon_prefs.package_name
        if (pkg_name != ""):
            print("Installing Python packages")

            # Find the location of the python executable
            executable_location = find_python_executable()

            # Call get-pip with the blender python executable
            pip_install_command = "%s -m pip install --user %s" % (executable_location, pkg_name)
            call(pip_install_command, shell=True)

        # Let's blender know the operator is finished
        return {'FINISHED'}

# Global Addon Properties
class Pip4BlenderPreferences(bpy.types.AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    package_name = StringProperty(
            name="Package Name",
            default=""
            )

    def draw(self, context):
        layout = self.layout
        layout.label("Install Pip in Blender")
        layout.label("This should be done once for your Blender installation, and will not be undone if you remove the addon")
        layout.operator("object.install_pip")
        layout.label(text="Install a Python Package")
        layout.prop(self, "package_name")
        layout.operator("object.install_python_library")
        layout.operator("object.generate_requirements_file")
        layout.operator("object.install_requirements_file")


def register():
    bpy.utils.register_class(InstallPip)
    bpy.utils.register_class(InstallPythonLibrary)
    bpy.utils.register_class(GenerateRequirementsFile)
    bpy.utils.register_class(InstallRequirementsFile)
    bpy.utils.register_class(Pip4BlenderPreferences)

def unregister():
    bpy.utils.unregister_class(Pip4BlenderPreferences)
    bpy.utils.unregister_class(InstallPip)
    bpy.utils.unregister_class(GenerateRequirementsFile)
    bpy.utils.unregister_class(InstallRequirementsFile)
    bpy.utils.unregister_class(InstallPythonLibrary)
