# Social Login With Django

The Social Login feature has been implemented using [*dj-rest-auth*](https://dj-rest-auth.readthedocs.io/) library.

By using [*dj-rest-auth*](https://dj-rest-auth.readthedocs.io/) library, we can have a social login system suitable for *REST API* based projects.

You have to have a Client ID and Secret Key to be able to use this feature.

### HOW TO BUILD THIS PROJECT?

The project is Dockerized which makes it easy to run locally and deploy to a server.


The Main requirement is you need to have [Docker](https://www.docker.com/) installed on your machine.


**Steps to follow:**

1. **GENERATE** keys. You need to generate social app keys for GitHub and Google.
2. **RENAME** the .env files.
   - Rename *.env.developer* file to *.env*
   - Rename *.env-react.developer* file to *.env-react*
3. **PLACE** the keys to correct spots in both .env and .env-react files.
4. **RUN** `docker compose up`.
5. **VISIT** http://localhost:5173 to view and test the project!

### HOW TO GENERATE SOCIAL APP KEYS?
To be able to use the social login features of the providers(like GitHub, Google, FaceBook...), you need to create a social/OAuth app using your account with each provider.


Unfortunately, creating these apps is provider-specific which makes the process a bit hard for beginners.


Here are some tutorials you can use:
- [Tutorial](https://docs.ultimatemember.com/article/1532-social-login-github-app-setup) for GitHub social app creation.
- Google social app [tutorial](https://docs.ultimatemember.com/article/141-social-login-google-app-setup).

  
  *** DO NOT FORGET to set **callback urls** correctly:
  - Google: http://127.0.0.1:8000/accounts/google/login/callback/
  - Github: http://localhost:8000/accounts/github/login/callback/ *

  *Somehow *127.0.0.1* doesn't work for GitHub, try using *localhost* instead.

Don't forget to have fun! :)
