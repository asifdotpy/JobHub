from django.apps import AppConfig

class JobsConfig(AppConfig):
    """
    A Django app configuration class for the 'jobs' app.

    This class is used to configure the 'jobs' app by specifying its name and providing any custom behavior that 
    should be executed when the app is ready to be used.

    Attributes:
        name (str): The name of the app, which must be unique across all installed apps.
    """
    name = 'jobs'

    def ready(self):
        """
        This method is called by Django when the app is ready to be used.

        It imports the 'JobOpening' model from the 'models.py' file to ensure that it is available to be used 
        elsewhere in the project. This ensures that any Django operations that use the model, such as database 
        migrations or creating administrative interfaces, are performed correctly.
    """
        from .models import JobOpening

