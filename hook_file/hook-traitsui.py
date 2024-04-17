# (C) Copyright 2022 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE_Enthought.txt and may be redistributed only
# under the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!
import os

os.environ['ETS_TOOLKIT'] = 'qt4'
# os.system(" echo $ETS_TOOLKIT")


from PyInstaller.utils.hooks import collect_data_files, collect_entry_point, collect_submodules

data, hiddenimports = collect_entry_point("traitsui.toolkits")
data += collect_data_files("traitsui")
hiddenimports += collect_submodules("traitsui")
print(data)
print(hiddenimports)
