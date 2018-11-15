import scipy.stats
import scipy.spatial
from numpy.random import RandomState
import matplotlib.pyplot as plt
import sys

def generateRandomJsonData():
    randomValue = RandomState(100000)
    # coordinate of locations (locations=[[x,...],[y,...]])
    locations = randomValue.randint(0, 500, size=(2, 100))
    # values of locations (values=[0,0,...])
    values = randomValue.randint(0, 1000, size=(100))
    return locations, values

def getJsonData(jsonFile):
    if jsonFile:
        return None       
    else:
        return generateRandomJsonData() 

def calculationTriangles(locations):
    # triangulation
    triangulation = scipy.spatial.Delaunay(locations.T)
    triangles = triangulation.simplices.copy()
    return triangulation, triangles


def detectColor(triangulation, locations, values):
    ax = plt.figure().add_subplot(111)
    def assimVertex(index): return triangulation.points[index]
    triangleSet = map(assimVertex, triangulation.vertices)
    # triangle color
    index = 0
    for triangle in triangleSet:
        ax.add_patch(plt.Polygon(triangle,
                                 facecolor='0.3',
                                 alpha=0.5))
        index += 1
    return ax
        
def plotTriangles(locations, triangles, imageName):
    # liner
    plt.triplot(locations[0],
                locations[1],
                #triangles=triangleSet,
                triangles=triangles,
                color='black',
                linewidth=0.5)
    plt.savefig(imageName)

if __name__ == '__main__':
    
    args = sys.argv
    commandType = args[1]
    jsonFile = args[2]
    imageName = args[3]
    locations, values = getJsonData(False)
    triangulation, triangles = calculationTriangles(locations)
    ax = detectColor(triangulation, locations, values)
    plotTriangles(locations, triangles, imageName)
