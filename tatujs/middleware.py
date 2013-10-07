import json

from tatujs.extractor import extract


class ExtractorMiddleware(object):
    """ Middleware to extract specific contents from an HTML response.
    """

    def process_response(self, request, response):

        source = request.META.get('HTTP_X_SOURCE')

        if source:
            sources = json.loads(source)
            response.content = json.dumps(extract(response.content, sources))
            response.content_type = 'application/json'

        return response
