# notifictinary-backend
backend for notifictionary application

## Instruction to run on PyCharm
- In pycham run configuration select Edit Configurations...
- In Envitonment Variables add a new variable named `DJANGO_SETTINGS_MODULE` and set its value to `notifictionary_backend.settings`
- Create another run Configuration and name it to 'migrate' and do the same for environment variable section
- Remove port.
- Check 'Custom run command' and enter 'migrate' in the field.
- Create another run Configuration and name it to 'makemigrations' and do the same for environment variable section.
- Remove port.
- Check 'Custom run command' and enter 'makemigrations' in the field.
- run `migrate` configuration.
- run `notifictionary_backend` configuration.
