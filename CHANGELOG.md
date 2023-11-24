# resume-builder
Changelog for the resume-builder-app

[21.11.2023]

Version 0.1.1 
-
- Added whitenoise
- Added Uikit 
- Created 2 new methods for Update and Delete Resume in views.py
- Modified settings.py (added STATIC_ROOT)

Version 0.1.2 
-
- Added new field in models.py (resume_template)
- Added new resume template in static/resume_templates
- Removed unused templates and refactored the resume/templates folder
- Removed templates methods from views.py
- Added home() method in views.py
               
Version 0.1.3
-
- modified the form-resume.html 

[22.11.2023]

Version 0.1.4
-
- renamed the fields from models.py 
- made migrations and cleaned database


Version 0.1.5
-
- added new model for testing formset
- added section fields in form-resume.html 


[23.11.2023]

Version 0.1.6
-
- refactored the models.py module
- added poetry environment 


Version 0.2.0
-
- implemented the pdf export option
- refactored the html templates 
