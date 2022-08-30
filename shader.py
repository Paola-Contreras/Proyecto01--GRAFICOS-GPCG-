import random as rand
import math_lib as m


def flat(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    #Light model 
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]
    intensity = m.dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def rainbow (render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= rand.random()
        g *= rand.random()
        r *= rand.random()
        

    triangleNormal = ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]
    intensity = m.dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def zebra (render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs['normals']
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]
    
    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w
    
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]

    triangleNormal = (nx, ny, nz)

    #Light model 
    intensity = m.dotProduct(triangleNormal, dirLight)


    if intensity > 0.90:
        r, g, b =  (0,0,0)
    elif intensity > 0.80:
           r, g, b =  (1,1,1)
    elif intensity > 0.70:
           r, g, b =  (0,0,0)
    elif intensity > 0.60:
           r, g, b =  (1,1,1)
    elif intensity > 0.50:
           r, g, b =  (0,0,0)
    elif intensity > 0.40:
           r, g, b =  (1,1,1)
    elif intensity > 0.30:
           r, g, b =  (0,0,0)
    elif intensity > 0.20:
       r, g, b =  (1,1,1)
    elif intensity > 0.10:
        r, g, b = (0,0,0)
    elif intensity > 0.05:
        r, g, b = (1,1,1)
    elif intensity > 0.06:
        r, g, b = (0,0,0)
    elif intensity > 0.01:
        r, g, b = (1,1,1)

    b *= intensity 
    g *= intensity 
    r *= intensity 

    if b > 1: r =1
    if r > 1: g =1
    if g > 1: b =1
    
    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def degraded (render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs['normals']
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]
    
    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w
    
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]

    triangleNormal = (nx, ny, nz)
    intensity = m.dotProduct(triangleNormal, dirLight)
    
    if intensity < 0.2:
        intensity = 0.1
    elif intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.7:
        intensity = 0.6
    elif intensity < 0.9:
        intensity = 0.8
    elif intensity < 0.94:
        intensity = 0.9
    elif intensity <= 1:
        intensity = 1

    
    g += intensity * 0.5
    r += intensity * 0.5
    b += intensity * 0.3

    if b > 1: b=1
    if r > 1: r=1
    if g > 1: g=1
    
    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def gourad(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w
    
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]

    triangleNormal = (nx, ny, nz)


    intensity = m.dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def light(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    #Light model 
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]
    intensity = m.dotProduct(triangleNormal, dirLight)

    white = [1,1,1]
    b += intensity * white[0]
    g += intensity * white[1]
    r += intensity * white[2]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def normalMap(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    tangente = kwargs["tangente"]
    bitangente = kwargs["bitangente"]

    b /= 255
    g /= 255
    r /= 255

    # P = Au + Bv + Cw
    tU = tA[0] * u + tB[0] * v + tC[0] * w
    tV = tA[1] * u + tB[1] * v + tC[1] * w

    if render.active_texture:
        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w
    
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]

    triangleNormal = (nx, ny, nz)

    if render.normal_map:
        texNormal = render.normal_map.getColor(tU, tV)
        texNormal = [texNormal[0] * 2 - 1,
                        texNormal[1] * 2 - 1,
                        texNormal[2] * 2 - 1]

        texNormal2 =[]
        for i in range(len(texNormal)):
            norm = texNormal[i] / m.normalize(texNormal)
            texNormal2.append(norm)
        texNormal = texNormal2

        tanM = [tangente[0],bitangente[0],triangleNormal[0],tangente[1],bitangente[1],triangleNormal[1],tangente[2],bitangente[2],triangleNormal[2]]
        tangentMatrix = m.createMatrix(3,3,tanM)

        texNormal = m.multiplyMatrix(tangentMatrix,texNormal)

        texNormal1 =[]
        for i in range(len(texNormal)):
            norm = texNormal[i] / m.normalize(texNormal)
            texNormal1.append(norm)
        texNormal = texNormal1

        intensity = m.dotProduct(texNormal, dirLight)
    else:
        intensity = m.dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0