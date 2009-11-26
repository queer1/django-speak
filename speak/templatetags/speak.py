import re

from django import template

register = template.Library()

@register.filter
def pirate(value):
    """
    This template filter allows you to make any string into 'Pirate speak'.
    
    Example::
        
        {% load speak %}
        {{ object.body|pirate }}
        
    """
    word_dict = {
        r'\b(you|your)\b': 'yar',
        r'\b(yours)\b': 'yars',
        r'\b(hello)\b': 'ahoy',
        r'\b(mad)\b': 'addled',
        r'\b(hey)\b': 'arr',
        r'\b(yes)\b': 'aye',
        r'\b(stop)\b': 'avast',
        r'\b(for)\b': 'far',
        r'\b(treasure)\b': 'booty',
        r'\b(will come)\b': 'be comin\'',
        r'\B(ing)\b': 'in\'', # Replaces "ing" endings with "in'"
        r'\b(in)\b': '\'n',
        r'\b(lady|woman|female)\b': 'lass',
        r'\b(friend)\b': 'bucko',
        r'\b(my)\b': 'me',
        r'\b(song)\b': 'chanty',
        r'\b(front)\b': 'fore',
        r'\b(coin)\b': 'doubloon',
        r'\b(have a drink|take a drink|get a drink)\b': 'carouse',
        r'\b(are)\b': 'is',
        r'\b(beautiful|pretty)\b': 'fancy',
        r'\b(want)\b': 'wants',
        r'\b(guy|man)\b': 'scallywag',
    }
    return replacer(value, word_dict)


@register.filter
def shakespeare(value):
    """
    This template filter turns a string into Shakespearean prose.

    Example::

        {% load speak %}
        {{ object.body|shakespeare }}

    """
    word_dict = {
        r'\b(you)\b': 'thou',
        r'\b(should|shall)\b': 'shalt',
    }
    return replacer(value, word_dict)   


@register.filter
def rasta(value):
    """
    This template filter turns a string into 'Rasta speak', like in Reggae.

    Example::

        {% load speak %}
        {{ object.body|rasta }}

    """
    word_dict = {
        r'\b(thou)\b': 'jah',
        r'\b(depression)\b': 'uppression',
        r'\b(depress)\b': 'uppress',
        r'\b(yes|yeah)\b': 'yah',
        r'\b(man)\b': 'mon',
        r'\b(good|great)\b': 'irie',
        r'\b(me|my|I)\b': 'I and I',
        r'\b(I)\b': 'I and I',
    }
    return replacer(value, word_dict)


def replacer(value, word_dict):
    """
    This function replace words in the ``value`` from the ``word_dict``.
    
    By passing a string and a dictionary of word matches, the function returns
    the string with all the words replaced.
    
    Example ``word_dict``::
    
        word_dict = {
            r'\b(foo)\b': 'bar',
            r'\b(hello)\b': 'world',
        }
     
    """
    for k, v in word_dict.iteritems():
        r = re.compile(k) #re.IGNORECASE
        value = r.sub(v, value)

    return value



# TODO: Rasta, Old English, Ebonics
