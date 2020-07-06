#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:49:55 2020

@author: amogh
"""


import web
urls = (
'/input', 'index'
)
class index:
    def GET(self):
        i = web.input(name=None)
        return render.index(i.name)
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
render = web.template.render('templates/')