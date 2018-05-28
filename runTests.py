'''
Entry point to call OpTest.
'''
from optoolbox import optest

modules = list()
modules.append(r"comm\testLoggedPopen.py")
modules.append(r"comm\testOpCommand.py")
modules.append(r"comm\testOpTelnet.py")
modules.append(r"environment\testCommonConfig.py")
modules.append(r"environment\testGlobalConfig.py")
modules.append(r"environment\testSharedConfig.py")
modules.append(r"environment\testTargets.py")
modules.append(r"opbuild\testBuild.py")
modules.append(r"system\testOpWin32.py")
modules.append(r"utils\testBaseConfig.py")
modules.append(r"utils\testOpFiles.py")
modules.append(r"utils\testOpMail.py")
modules.append(r"utils\testOpTime.py")
modules.append(r"utils\testOpUtil.py")
modules.append(r"utils\testRemoteExecution.py")
modules.append(r"utils\testSingleton.py")
modules.append(r"git\testSourceControlGIT.py")
modules.append(r"rtxsgtools\testGenerators.py")
modules.append(r"matlab\testMatlab.py")
modules.append(r"matlab\testMatlabHandler.py")
modules.append(r"matlab\testSimulink.py")
modules.append(r"executor\testExecutor.py")
modules.append(r"executor\test_testconfig.py")



if __name__ == '__main__':
    optest.main(modules, keepAlive=False)
    #optest.main(userTestModules=modules, keepAlive=False)