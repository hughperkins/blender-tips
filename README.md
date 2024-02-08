# blender-tips
blender-tips

# Bake fluid on commandline:

```
/Applications/Blender.app/Contents/MacOS/Blender --background ~/BlenderFiles/test_render1.blend --python bake.py
```
(`bake.py` is in this repo)

# Render frame on commandline:

```
/Applications/Blender.app/Contents/MacOS/Blender --background ~/BlenderFiles/test_render1.blend -f 2 -o './feb08a####.png'
```
(Note that `-o` MUST precede the `-f` ...)
