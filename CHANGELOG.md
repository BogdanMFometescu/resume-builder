# resume-builder

Changelog for the resume-builder-app

[11.12.2023]

Version 0.3.2
-
- fixed the html links for all the views from users
- added back button to all forms 



[11.12.2023]

Version 0.3.1
-
- added signals
- modified the views.py from resume app
- fixed the urls links 
- added the html templates


[10.12.2023]

Version 0.3.0
- 
- added user app 
- created Profile model
- created forms for User and Profile
- refactored the README.md


[10.12.2023]

Version 0.2.5
- 
- MODERN TEMPLATE HTML 
  - added methods in views.py form adding new education, skills,projects,experience
  - added the urls for the above views
  - added the functionality for each model to be edited and deleted 
  - added the functionality to add experience directly from the html (+ button) 
  - added the functionality to add education directly from the html (+ button) 
  - added the functionality to add projects directly from the html (+ button) 
  - added the functionality to add skills directly from the html (+ button)   
  - added the functionality to add skills directly from the html (+ button) 

- EXPORT-PDF TEMPLATE HTML

  - refactored the fields from both templates (simple and modern html)   

- modified the README.MD file

[fixed]  - redirect in views.py to the actual resume_id.



[09.12.2023]

Version 0.2.4
-
- SIMPLE TEMPLATE HTML 
  - added methods in views.py form adding new education, skills,projects,experience
  - added the urls for the above views
  - added the functionality for each model to be edited and deleted 
  - added the functionality to add experience directly from the html (+ button) 
  - added the functionality to add education directly from the html (+ button) 
  - added the functionality to add projects directly from the html (+ button) 
  - added the functionality to add skills directly from the html (+ button)   
  - added the functionality to add skills directly from the html (+ button) 



[08.12.2023]

Version 0.2.3
-

- implemented the edit/delete functionality for the resume
- added views and url paths for updating/deleting experience, skills, education,projects
- fixed templates for simple resume, added functionality for edit/delete

[01.12.2023]

Version 0.2.2
-

- refactored the changelog
- refactored the resumes.html (removed redundant code)
- refactored the home.html (removed the redundant code)
- refactored the resume-template-01.html
- refactored the resume-template-02.html

[29.11.2023]

Version 0.2.1
-
-fixed the html templates for export-pdf and single-resume


Version 0.2.0
-

- implemented the pdf export option
- refactored the html templates

[23.11.2023]

Version 0.1.6
-

- refactored the models.py module
- added poetry environment

Version 0.1.5
-

- added new model for testing formset
- added section fields in form-resume.html

[22.11.2023]

Version 0.1.4
-

- renamed the fields from models.py
- made migrations and cleaned database

[21.11.2023]


Version 0.1.3
-

- modified the form-resume.html

Version 0.1.2
-

- Added new field in models.py (resume_template)
- Added new resume template in static/resume_templates
- Removed unused templates and refactored the resume/templates folder
- Removed templates methods from views.py
- Added home() method in views.py

Version 0.1.1
-

- Added whitenoise
- Added Uikit
- Created 2 new methods for Update and Delete Resume in views.py
- Modified settings.py (added STATIC_ROOT)










