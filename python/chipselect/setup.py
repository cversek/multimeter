"""   
desc:  Setup script for 'automat' package.
auth:  Craig Wm. Versek (cversek@physics.umass.edu)
date:  2012-05-27
notes: install with "sudo python setup.py install"
"""
import platform, os, shutil

PACKAGE_METADATA = {
    'name'         : 'chipselect',
    'version'      : 'dev',
    'author'       : "Craig Versek",
    'author_email' : "cversek@physics.umass.edu",
}
    
PACKAGE_SOURCE_DIR = 'src'
MAIN_PACKAGE_DIR   = 'chipselect'
MAIN_PACKAGE_PATH  = os.path.abspath(os.sep.join((PACKAGE_SOURCE_DIR,MAIN_PACKAGE_DIR)))

INSTALL_REQUIRES = []


def ask_yesno(prompt, default='y'):
    while True:
        full_prompt = prompt + "([y]/n): "
        val = raw_input(full_prompt)
        if val == "":
            val = default
        if val in ['y','Y']:
            return True
        elif val in ['n','N']:
            return False


###############################################################################
# MAIN
###############################################################################
if __name__ == "__main__":
    #the rest is controlled by setuptools
    from ez_setup import use_setuptools
    use_setuptools()

    from setuptools import setup, find_packages

    # run the setup script
    setup(
        
          #packages to install
          package_dir  = {'':'src'},
          packages     = find_packages('src'),
          
          #non-code files
          package_data     =   {'': ['*.dat']},

          #dependencies
          install_requires = INSTALL_REQUIRES,
          extras_require = {
                           },
          dependency_links = [
                              #'http://sourceforge.net/project/showfiles.php?group_id=80706', #matplotlib
                             ],
          #scripts and plugins
          entry_points = {
                          #'console_scripts': ['automat_decode_nispy = automat.scripts.decode_nispy:main']
                         },
          **PACKAGE_METADATA 
    )
