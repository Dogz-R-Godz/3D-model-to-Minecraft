import mcschematic
import math
def round_point(point):
    """Rounds each coordinate of a point to the nearest integer."""
    return (round(point[0]), round(point[1]), round(point[2]))

def points_along_line(point1, point2):
    """Returns a list of rounded points along the line between two 3D points."""
    # Calculate the difference between the two points
    diff = (point2[0]-point1[0], point2[1]-point1[1], point2[2]-point1[2])
    # Calculate the distance between the two points
    distance = math.sqrt(diff[0]**2 + diff[1]**2 + diff[2]**2)
    # Calculate the number of intermediate points to generate (10 in this example)
    num_points = max(diff[0],diff[1],diff[2],0-diff[0],0-diff[1],0-diff[2],1)
    # Calculate the step size for each coordinate
    step = (diff[0]/num_points, diff[1]/num_points, diff[2]/num_points)
    # Generate the list of points along the line
    points = []
    for i in range(num_points+1):
        x = point1[0] + i*step[0]
        y = point1[1] + i*step[1]
        z = point1[2] + i*step[2]
        points.append(round_point((x, y, z)))
    return points
schem = mcschematic.MCSchematic()
v={}
vt={}
vn={}
f={}

model_size=[0,0]
schematic={}

fileToOpen=input("Input the name of the file you want to put into minecraft here -> ")
size_x=input("Input the X size of your creation")
size_y=input("Input the Y size of your creation")
size_z=input("Input the Z size of your creation")

size=(size_x,size_y,size_z)
with open(f"{fileToOpen}.obj") as file:
    for line in file:
        if line[0]=="v":
            if line[1]=="n":
                line2=line.split()
                for thing in line2:
                    if thing!="vn":
                        if float(thing)>=0 and float(thing)>model_size[0]:
                            model_size[0]=float(thing)
                        if float(thing)<0 and float(thing)<model_size[1]:
                            model_size[1]=float(thing)
                line2_2=""
                for letter in line2[3]:
                    if letter!='"\"' and letter!='"n':
                        line2_2+=letter
                #for x in range(len(line2)-1):
                    #E_found=False
                    #num=""
                    #num2=1
                    #for y in line2[x+1]:
                        #if y!="E":
                            #if E_found==False:
                                #num+=y
                        #else:
                            #E_found=True
                            #num2=int(float(f"{line2[x+1][len(line2[x+1])-2]}{line2[x+1][len(line2[x+1])-1]}"))
                            #num='{:.100f}'.format(float(line2[x+1]))
                           #x=x
                    #line3[x]='{:.100f}'.format(float(num))
                vn[len(vn)+1]=[float(line2[1]),float(line2[2]),float(line2_2)]
            elif line[1]=="t":
                x=0
                #line2=line.split()
                #line2_2=""
                #for letter in line2[3]:
                    #if letter!='"\"' and letter!='"n':
                        #line2_2+=letter
                #for thing in line2:
                    #if thing!="vt":
                        #if float(thing)>=0 and float(thing)>model_size[0]:
                            #model_size[0]=float(thing)
                        #if float(thing)<0 and float(thing)<model_size[1]:
                            #model_size[1]=float(thing)
                #vt[len(vt)+1]=[float(line2[1]),float(line2[2]),float(line2_2)]
            else:
                line2=line.split()
                line2_2=""
                for letter in line2[3]:
                    if letter!='"\"' and letter!='n':
                        line2_2+=letter
                for thing in line2:
                    if thing!="v":
                        if float(thing)>=0 and float(thing)>model_size[0]:
                            model_size[0]=float(thing)
                        if float(thing)<0 and float(thing)<model_size[1]:
                            model_size[1]=float(thing)

                #for x in range(len(line2)-1):
                    #E_found=False
                    #num=""
                    #num2=1
                    #for y in line2[x+1]:
                        #if y!="E":
                            #if E_found==False:
                                #num+=y
                        #else:
                            #E_found=True
                            #num2=int(float(f"{line2[x+1][len(line2[x+1])-2]}{line2[x+1][len(line2[x+1])-1]}"))
                            #num='{:.100f}'.format(float(line2[x+1]))
                           #x=x
                    #line3[x]='{:.100f}'.format(float(num))
                v[len(v)+1]=[float(line2[1]),float(line2[2]),float(line2_2)]
        elif line[0]=="f":
            line2=""
            diffCoords=[]
            for x in line:
                if x!="f":
                    line2+=x
            line2=line2.split()
            lines=[]
            lines2={}
            coord=""
            for x in range(len(line2)):
                if "//" in line2:
                    lines.append(line2[x].replace("//",",0,"))
                else:
                    lines.append(line2[x].replace("/",",0"))
            for x in range(len(lines)):
                tuple1=tuple(map(int, lines[x].split(',')))
                if x!=len(lines)-1:
                    tuple2=tuple(map(int, lines[x+1].split(',')))
                    lines2[tuple1[0]]=tuple2[0]
                else:
                    tuple2=tuple(map(int, lines[0].split(',')))
                    lines2[tuple1[0]]=tuple2[0]
                


            f[len(f)+1]=lines2
print("All faces and verticies found")
points3=[]
line=[]
x=x
model_width=model_size[0]+(0-model_size[1])
multiplyer=size[0]/model_width
connections={}
counter=0
for x in f:
    counter+=1
    points3.append(f[x]) #f={1: {1: 2, 2: 4, 4: 3, 3: 1}, 2: {3: 4, 4: 8, 8: 7, 7: 3}, 3: {7: 8, 8: 6, 6: 5, 5: 7}}
        #point1=v[y[0]]
        #point1=(round((point1[0]*multiplyer)+multiplyer),round((point1[1]*multiplyer)+multiplyer),round((point1[2]*multiplyer)+multiplyer))
        #point2=vn[y[1]]
        #point2=(round((point2[0]*multiplyer)+multiplyer),round((point2[1]*multiplyer)+multiplyer),round((point2[2]*multiplyer)+multiplyer))
        #points=points_along_line(point1, point2)
        #for z in points:
            #if z not in schematic.keys():
                #schematic[z]="minecraft:stone"
    line_numbers={}
    for n in points3[0]:
        y,z=v[n],v[points3[0][n]]
        y2=(round((y[0]*multiplyer)+multiplyer),round((y[1]*multiplyer)+multiplyer),round((y[2]*multiplyer)+multiplyer))
        z2=(round((z[0]*multiplyer)+multiplyer),round((z[1]*multiplyer)+multiplyer),round((z[2]*multiplyer)+multiplyer))
        points2=points_along_line(y2, z2)
        line_numbers[n]=points2
            #line.append(points_along_line(y2,z2))
        for z2 in points2:
            if z2 not in schematic.keys():
                schematic[z2]="minecraft:stone"
    for y in line_numbers:
        line_numbers[y].pop(0)
        line_numbers[y].pop()
    for y in line_numbers:
        for z in line_numbers[y]:
            for y2 in line_numbers:
                if y2!=y:
                    for z2 in line_numbers[y2]:
                        if z not in connections.keys():
                            if z2 not in connections.keys():
                                connections[z]=[z2]
                                blocks=points_along_line(z, z2)
                                for block in blocks:
                                    if block not in schematic.keys():
                                        schematic[block]="minecraft:stone"
                            elif z not in connections[z2]:
                                connections[z2].append(z)
                                blocks=points_along_line(z, z2)
                                for block in blocks:
                                    if block not in schematic.keys():
                                        schematic[block]="minecraft:stone"
                        elif z2 not in connections[z]:
                            connections[z].append(z2)
                            blocks=points_along_line(z, z2)
                            for block in blocks:
                                if block not in schematic.keys():
                                    schematic[block]="minecraft:stone"

    points2=[]
    connections={}
    points3=[]
    print(f"Another face done. {counter}/{len(f)} done.")
print("All faces filled in")
#for x in v:
    #if (round(v[x][0]*multiplyer),round(v[x][1]*multiplyer),round(v[x][2]*multiplyer)) not in schematic.keys():
        #schematic[(round(v[x][0]*multiplyer),round(v[x][1]*multiplyer),round(v[x][2]*multiplyer))]="minecraft:stone"
#for x in f:
for x in schematic:
    schem.setBlock(x, schematic[x])
schem.save("Schems", fileToOpen, mcschematic.Version.JE_1_19_2)
print(f"Schematic Finished, you can find it in Schems/{fileToOpen}. This schematic is for Java Edition 1.19.2. You need a mod like worldedit or litematica to run this file. ")