## Tool for running startup shell scripts on Xmonad 
### How to use:
Every file under "scripts" folder will be read as a script.
Add the following to your xmonad.hs:
```haskell
import XMonad.Util.SpawnOnce ( spawnOnce )
myStartupHook :: X ()
myStartupHook = do
  spawnOnce "cd FOLDER_DIR;python3 main.py"
```
but remember to replace FOLDER_DIR to the actual folder path.

### Scripts
For making scripts, create simple text files(the extension doesn't matter) and right the shell commands on each line. Example:
```shell
cd /home
mkdir test
touch test.txt
```

If you want your script not to be read, but don't want to delete it, simply attach "dont" at it's first line. Example:
```shell
dont
cd /home
mkdir test
touch test.txt
```
this script won't be read, even if it's located on /scripts folder.

#### There are some files on the /scripts folder, but you can just delete it all.