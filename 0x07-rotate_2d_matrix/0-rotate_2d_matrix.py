#!/usr/bin/python3
""" Module that implements a rotation of a matrix """


def rotate_2d_matrix(matrix):
    """ Rotates a two dimensional matrix by 90 degree"""
    temp = matrix[:]
    for i in range(len(matrix)):
        column = [row[i] for row in temp]
        matrix[i] = column[::-1]
