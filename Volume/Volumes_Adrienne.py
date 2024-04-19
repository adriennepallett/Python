# File: Volumes_Adrienne.py
# Project: CSIS 2101 Assignment 7
# Author: Adrienne Pallett
# History: Version 7.1 October 19, 2022

# Menu Program to Find Volumes of A User Entered Desire of 3D Shapes
# This program will be what is imported to Menu_Adrienne.py with the appropriate
#   function requested by the user in the menu.

import math

def sphereVolumeAdrienne(r):
    
    # Volume of a Sphere with radius r
    vol_sph = (4/3) * (math.pi) * math.pow(r,3)

    # Returns Volume to be called by Menu_Adrienne
    return vol_sph


def cylVolumeAdrienne(r,h):
    
    # Volume of a cylinder with radius r and height h
    vol_cyl = (math.pi) * math.pow(r,2) * h

    # Returns Volume to be called by Menu_Adrienne
    return vol_cyl


def coneVolumeAdrienne(r,h):

    # Volume of a cone with radius r and height h
    vol_cone = (1/3) * (math.pi) * math.pow(r,2) * h

    # Returns Volume to be called by Menu_Adrienne
    return vol_cone


def cubeVolumeAdrienne(s):

    # Volume of a cube with sides a
    vol_cube = math.pow(s,3)
    
    # Returns Volume to be called by Menu_Adrienne
    return vol_cube

