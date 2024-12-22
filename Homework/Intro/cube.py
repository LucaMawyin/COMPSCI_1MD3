def cubeInfo(sideLength:int):
    print("Volume:", cubeVolume(sideLength))
    print("Surface Area:", cubeSufraceArea(sideLength))

def cubeVolume(sideLength:int):
    return (sideLength**3)

def cubeSufraceArea(sideLength:int):
    return 6*(sideLength**2)
