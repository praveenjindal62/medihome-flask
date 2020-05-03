from web.views.interfaces.ViewInterface import ViewInterface
from flask import render_template,abort

class AbortView404(ViewInterface):
    def process(self,request,session):
        return abort(404)

class AbortView500(ViewInterface):
    def process(self,request,session):
        return abort(500)