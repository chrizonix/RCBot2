# vim: set sts=2 ts=8 sw=2 tw=99 et:
import sys
try:
  from ambuild2 import run
except:
  try:
    import ambuild
    sys.stderr.write('It looks like you have AMBuild 1 installed, but this project uses AMBuild 2.\n')
    sys.stderr.write('Upgrade to the latest version of AMBuild to continue.\n')
  except:
    sys.stderr.write('AMBuild must be installed to build this project.\n')
    sys.stderr.write('http://www.alliedmods.net/ambuild\n')
  sys.exit(1)

run = run.PrepareBuild(sourcePath=sys.path[0])
run.default_build_folder = 'obj-' + run.target_platform
run.options.add_option('--hl2sdk-root', type=str, dest='hl2sdk_root', default=None,
                       help='Root search folder for HL2SDKs')
run.options.add_option('--enable-debug', action='store_const', const='1', dest='debug',
                       help='Enable debugging symbols')
run.options.add_option('--enable-optimize', action='store_const', const='1', dest='opt',
                       help='Enable optimization')
run.options.add_option('-s', '--sdks', default='all', dest='sdks',
                       help='Build against specified SDKs; valid args are "all", "present", or '
                            'comma-delimited list of engine names (default: %default)')
run.Configure()
