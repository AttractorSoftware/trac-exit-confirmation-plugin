
from trac.core import Component, implements
from trac.web.chrome import add_script
from pkg_resources import resource_filename
from trac.web.chrome import ITemplateProvider
from trac.web.api import IRequestFilter

class ScriptLoading(Component):
    implements(IRequestFilter, ITemplateProvider)

    # IRequestFilter methods

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        add_script(req, 'exit_confirmation/confirmation_window.js')
        return template, data, content_type

    # ITemplateProvider methods

    def get_templates_dirs(self):
        return []

    def get_htdocs_dirs(self):
        return [('exit_confirmation', resource_filename(__name__, 'htdocs'))]

