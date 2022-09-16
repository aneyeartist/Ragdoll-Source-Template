import bpy

#NB : The Basis Shape Key is ommited at every loop because it causes errors if it stays in the QC file

d = bpy.context.object.data
i = 1
n = 0

#Printing out the initial QC line to open the statement
print('\tflexfile "blank.vta"{')

print('\tdefaultflex frame 0')

#Defining the intial name of the Shape keys
for b in d.shape_keys.key_blocks:
    if b.name == 'basis shape key':
        print('', end='')
    else:
        print("\tflex \"%s\" frame %d" % (b.name, i))
        i+=1

#Closing the intial opening bracket from the QC
print("\t}")

#Setting up the range of each flex
for b in d.shape_keys.key_blocks:
    if b.name == 'basis shape key':
        print('', end='')
    else:
        print("\tflexcontroller {} range 0 1 \"{}\"".format(b.name,b.name))

#Creating controllers for eye control in SFM (not compulsary for Gmod, but good nonetheless)
print('\tflexcontroller eyes range -45 45 "eyes_updown"')
print('\tflexcontroller eyes range -45 45 "eyes_rightleft"')

#Creating a gap to allow for name definition
print(" ")

g = [b.name for b in d.shape_keys.key_blocks]

#Associating names in QC file
for b in g:
    if g[n] == 'basis shape key':
        print('', end='')
        n += 1
    else:
        print("\t%"+b, "=", b)
        n += 1