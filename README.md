# blender-tips
blender-tips

# Bake fluid on commandline:

```
/Applications/Blender.app/Contents/MacOS/Blender --background ~/BlenderFiles/test_render1.blend --python bake.py
```
(`bake.py` is in this repo)

# Render frame on commandline:

```
/Applications/Blender.app/Contents/MacOS/Blender --background ~/BlenderFiles/test_render1.blend -o './feb08a####.png' -f 2
```
(Note that `-o` MUST precede the `-f` ...)

# Render animation on commandline:

```
/Applications/Blender.app/Contents/MacOS/Blender --background ~/BlenderFiles/test_render1.blend -o './feb08a####.png' -s 1 -e 5 -a
```
Where:
- `-s` is start frame
- `-e` is end frame (inclusive)
- `-a` says to render animation
