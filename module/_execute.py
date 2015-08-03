"""
Valmor F. de Almeida dealmeidav@ornl.gov; vfda

Cortix: a program for system-level modules
        coupling, execution, and analysis.

Tue Dec 10 11:21:30 EDT 2013
"""
#*********************************************************************************
import os, sys, io
from cortix.launcher.interface import Launcher
#*********************************************************************************

#---------------------------------------------------------------------------------
# Execute module            

def _Execute(self, slotId, runtimeCortixParamFile, runtimeCortixCommFile ):

#  print('module:',self.__name)
#  print('module executable: ',self.__executableName)
#  print('module path      : ',self.__executablePath)
#  print('input file       : ',self.__inputFilePath+self.__inputFileName)
#  print('param file       : ',runtimeCortixParamFile)
#  print('comm  file       : ',runtimeCortixCommFile)
 
#  guestExec = self.executablePath + self.executableName

  input     = self.inputFilePath + self.inputFileName
  param     = runtimeCortixParamFile
  comm      = runtimeCortixCommFile

  fullPathCommDir = comm[:comm.rfind('/')]+'/'
  runtimeModuleStatusFile = fullPathCommDir + 'runtime-status.xml'

  status = runtimeModuleStatusFile

  modLibParentDir = self.modLibParentDir
  modLibName      = self.modLibName
  modName         = self.modName 
  modType         = self.modType

  # run module on its own thread using file IO communication
  t = Launcher( modLibName, modLibParentDir, 
                modName, slotId, input, param, comm, status )
  t.start()

  return runtimeModuleStatusFile

#*********************************************************************************
