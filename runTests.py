'''
Entry point to call OpTest.
'''
import nose2


if __name__ == '__main__':
    from optoolbox import OpLog
    OpLog.configureLogging()
    nose2.discover()
