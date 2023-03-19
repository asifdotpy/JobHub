from django.http import HttpResponse
from django.views.generic import TemplateView
import os

# Define a new class that extends TemplateView.
class PdfView(TemplateView):
    # Set the content type to 'application/pdf'.
    content_type = 'application/pdf'

    # Override the 'get' method to return a PDF response.
    def get(self, request, *args, **kwargs):
        # Get the name of the PDF file from the URL parameters.
        pdf_file = kwargs.get('pdf_file')

        # Construct the path to the PDF file by joining the 'pdf' directory and the file name.
        pdf_path = os.path.join('pdf', pdf_file)

        # Open the PDF file in binary mode.
        with open(pdf_path, 'rb') as f:
            # Create an HttpResponse object with the PDF file's contents and the correct content type.
            response = HttpResponse(f.read(), content_type=self.content_type)

            # Set the Content-Disposition header to 'inline' and include the file name in the response.
            response['Content-Disposition'] = 'inline; filename=' + pdf_file

            # Return the HttpResponse object.
            return response