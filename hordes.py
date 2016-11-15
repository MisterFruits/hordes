# coding: utf-8

class Ville(object):
    """docstring for Ville"""
    def __init__(self, scie=False, manufacture=False):
        super(Ville, self).__init__()
        self.scie = scie
        self.manufacture = manufacture
        self.chantiers = {}
