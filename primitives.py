
import pyglet
from pyglet.gl import *
from math import *
from config import *



def afficherRectangle(position=(0.0,0.0,0.0),angleX=0.0,angleY=0.0,angleZ=0.0,dimensions=(1.0,1.0),texture=None,couleur=(1.0,0.0,0.0)):
        x,y,z = position
        largeur, hauteur  = dimensions

        if texture == None:
                r,v,b = couleur
                glColor3f(r,v,b)
                glDisable(GL_TEXTURE_2D)
                glPushMatrix()
                glTranslatef(x,y,z)
                if angleX!=0.0:
                    glRotatef(angleX,1.0,0.0,0.0)
                if angleY!=0.0:
                    glRotatef(angleY,0.0,1.0,0.0)
                if angleZ!=0.0:
                    glRotatef(angleZ,0.0,0.0,1.0)
                glScalef(largeur,hauteur,1.0)
                glBegin(GL_QUADS)
                glVertex3f(-0.5,0.0,0.0)
                glVertex3f(0.5,0.0,0.0)
                glVertex3f(0.5,1.0,0.0)
                glVertex3f(-0.5,1.0,0.0)
                glEnd()
                glPopMatrix()
                glEnable(GL_TEXTURE_2D)
        else:
                glBindTexture(GL_TEXTURE_2D,texture.id)
                glPushMatrix()
                glTranslatef(x,y,z)
                if angleX!=0.0:
                    glRotatef(angleX,1.0,0.0,0.0)
                if angleY!=0.0:
                    glRotatef(angleY,0.0,1.0,0.0)
                if angleZ!=0.0:
                    glRotatef(angleZ,0.0,0.0,1.0)
                glScalef(largeur,hauteur,1.0)
                glBegin(GL_QUADS)
                glTexCoord2f(0.0,0.0)
                glVertex3f(-0.5,0.0,0.0)
                glTexCoord2f(1.0,0.0)
                glVertex3f(0.5,0.0,0.0)
                glTexCoord2f(1.0,1.0)
                glVertex3f(0.5,1.0,0.0)
                glTexCoord2f(0.0,1.0)
                glVertex3f(-0.5,1.0,0.0)
                glEnd()
                glPopMatrix()



def dessinerRectangle(p0, p1, p2, p3,texture=None, textureRepeat = True, color = (0,1,0)):

    """
    Affiche une forme selon les quatres point definis
    """
    
    
    if texture == None:
            r,v,b = color
            glDisable(GL_TEXTURE_2D)
            glColor3f(r,v,b)
            glBegin(GL_QUADS)
            glVertex3f(p0[0],p0[1],p0[2])
            glVertex3f(p1[0],p1[1],p1[2])
            glVertex3f(p2[0],p2[1],p2[2])
            glVertex3f(p3[0],p3[1],p3[2])
            glEnd()
            glEnable(GL_TEXTURE_2D)
    else:

        if textureRepeat:
                    a = fabs(p0[0] - p1[0])
                    b = fabs(p0[1] - p1[1])
                    c = fabs(p0[2] - p1[2])

                    if a >= b and a >= c:
                            d = a
                    elif b >= a and b >= c:
                            d = b
                    elif c >= a and c >= b:
                            d = c
                    else:
                            d = a

                    a = fabs(p1[0] - p2[0])
                    b = fabs(p1[1] - p2[1])
                    c = fabs(p1[2] - p2[2])

                    if a >= b and a >= c:
                            e = a
                    elif b >= a and b >= c:
                            e = b
                    elif c >= a and c >= b:
                            e = c
                    else:
                            e = a

                    del a
                    del b
                    del c

                    glColor4f(1,1,1,1)
                    glBindTexture(GL_TEXTURE_2D,texture.id)
                    glBegin(GL_QUADS)
                    glTexCoord2f(0.0,0.0)
                    glVertex3f(p0[0],p0[1],p0[2])
                    glTexCoord2f(d,0.0)
                    glVertex3f(p1[0],p1[1],p1[2])
                    glTexCoord2f(d,e)
                    glVertex3f(p2[0],p2[1],p2[2])
                    glTexCoord2f(0,e)
                    glVertex3f(p3[0],p3[1],p3[2])
                    glEnd()
        else:
                    glColor4f(1,1,1,1)
                    glBindTexture(GL_TEXTURE_2D,texture.id)
                    glBegin(GL_QUADS)
                    glTexCoord2f(0.0,0.0)
                    glVertex3f(p0[0],p0[1],p0[2])
                    glTexCoord2f(0.0,1.0)
                    glVertex3f(p1[0],p1[1],p1[2])
                    glTexCoord2f(1.0,1.0)
                    glVertex3f(p2[0],p2[1],p2[2])
                    glTexCoord2f(1.0,0.0)
                    glVertex3f(p3[0],p3[1],p3[2])
                    glEnd()

def dessinerTriangle(p0, p1, p2,texture=None):

    """
    Affiche une forme selon les trois point definis
    """
    
    
    if texture == None:
            r,v,b = 0,1,0
            glColor3f(r,v,b)
            glDisable(GL_TEXTURE_2D)
            glColor3f(1.0,0.0,0.0)
            glBegin(GL_TRIANGLES)
            glVertex3f(p0[0],p0[1],p0[2])
            glVertex3f(p1[0],p1[1],p1[2])
            glVertex3f(p2[0],p2[1],p2[2])
            glEnd()
            glEnable(GL_TEXTURE_2D)
    else:
            glBindTexture(GL_TEXTURE_2D,texture.id)
            glBegin(GL_TRIANGLES)
            glTexCoord2f(0.0,0.0)
            glVertex3f(p0[0],p0[1],p0[2])
            glTexCoord2f(0.0,0.0)
            glVertex3f(p1[0],p1[1],p1[2])
            glTexCoord2f(1,1)
            glVertex3f(p2[0],p2[1],p2[2])
            glEnd()
            

def dessinerBrique(p0,coteX,coteZ,hauteur,texture):

        p1 = (p0[0], p0[1], p0[2] + coteZ)
        p2 = (p0[0], p0[1] + hauteur, p0[2] + coteZ)
        p3 = (p0[0], p0[1] + hauteur, p0[2])
        p4 = (p0[0] + coteX, p0[1], p0[2])
        p5 = (p0[0] + coteX, p0[1], p0[2]+ coteZ)
        p6 = (p0[0] + coteX, p0[1] + hauteur, p0[2]+ coteZ)
        p7 = (p0[0] + coteX, p0[1] + hauteur, p0[2])

        if hauteur != 0:
                dessinerRectangle(p0, p1, p2, p3,texture)
                dessinerRectangle(p2, p1, p5, p6,texture)
                dessinerRectangle(p6, p5, p4, p7,texture)
                dessinerRectangle(p3, p7, p4, p0,texture)
                dessinerRectangle(p2, p3, p7, p6,texture)
                dessinerRectangle(p0, p4, p5, p1,texture)
        else:
                dessinerRectangle(p0, p4, p5, p1,texture)

def dessiner_BriquePredefinie(self, p0, p1, p2, p3, p4, p5, p6, p7, texture_lat=TEXTURE_TROTTOIR, texture_top=TEXTURE_PAVE):

        prims.dessinerRectangle(p0, p1, p5, p4, texture_lat)
        prims.dessinerRectangle(p1, p2, p6, p5, texture_lat)
        prims.dessinerRectangle(p2, p3, p7, p6, texture_lat)
        prims.dessinerRectangle(p3, p0, p4, p7, texture_lat)
        prims.dessinerRectangle(p4, p5, p6, p7, texture_top)

def makedisplaylist():
        """ test """
        display_list = glGenLists(1)
        glNewList(display_list, GL_COMPILE)
        glEndList()
        return display_list
        



def translate(x,y,z):
        glTranslatef(x,y,z)

def rotate(angle, x, y, z):
        glRotatef(angle, x, y, z)



        
