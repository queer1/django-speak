==================
django-speak
==================

A fun (and bizarre) set of Django filters to convert a string into a 
different type of speech.

Available filters:

* ``pirate`` -- Returns text in "Pirate speak", like you hear in pirate movies.
* ``rasta`` -- Returns text in a Jamaican "Rastafari" speak, like in Reggae music.
* ``shakespeare`` -- Returns text in a Shakespearean format.
* ``ebonics`` -- Returns text in ebonics format, like Rap music. (*Coming soon!*)

Installation
============

1. To use the django-speak, you first need to add ``speak`` to
``INSTALLED_APPS`` in your settings file::

    INSTALLED_APPS = (
        ...
        'speak',
    )

2. Next, in your template, load the library and apply the filter to a variable 
you want to change::

    {% load speak %}
    {{ myvar|pirate }}
    
Example
=======

The best way to see how these filters work is to see it in action! I have set up
a site on Google App Engine that is running a small Django app that takes a string 
and then, depending on what language you choose, outputs your new, re-formatted 
text. Check it out:

http://django-speak.appspot.com/

If you were to use the ``pirate`` filter in your templates, and you pass it this
string for example::

    You are a beautiful woman, do you want to have a drink with me?

... you would get this in return::

    Ye be a fancy lass, doos ye wants to carouse wit me?

More...
=======

I'm going to continually add new words to each language, and hopefully some more 
languages as well.

If you find any bugs, have some feedback or have a new language requests, go here
http://github.com/danawoodman/django-speak/issues and create a case or get in 
touch with me. Any feedback is welcome!

If you use these filters in your project, send me an email so I can see what 
you did at:

dana (at) danawoodman.com

Enjoy!
