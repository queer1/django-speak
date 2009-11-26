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
        # Adjectives
        r'\b(beautiful|pretty)\b': 'fancy',
        r'\b(big)\b': 'grand',
        r'\b(front)\b': 'fore',
        r'\b(mad)\b': 'addled',
        r'\b(this)\b': 'tis',
        # Adverbs
        r'\b(there)\b': 'thar',
        r'\b(quickly)\b': 'handsomely',
        r'\b(yes)\b': 'aye',
        # Expressions, phrases, and commands
        r'\b(goodbye|good bye)\b': 'fair winds',
        r'\b(guy|man)\b': 'scallywag',
        r'\b(haha)\b': 'harhar',
        r'\b(hello)\b': 'ahoy',
        r'\b(hey)\b': 'arr',
        r'\b(stop)\b': 'avast',
        # Nouns
        r'\b(alcohol|beer)\b': 'grog',
        r'\b(boat)\b': 'ship',
        r'\b(boy|child)\b': 'lad',
        r'\b(coin)\b': 'doubloon',
        r'\b(crew|sailors)\b': 'hands',
        r'\b(eye)\b': 'deadlight',
        r'\b(eyes)\b': 'deadlights',
        r'\b(food)\b': 'grub',
        r'\b(friend)\b': 'bucko',
        r'\b(girl)\b': 'lassie',
        r'\b(hell|Hell)\b': 'El',
        r'\b(lady|woman|female)\b': 'lass',
        r'\b(money|cash)\b': 'loot',
        r'\b(prostitute)\b': 'wench',
        r'\b(rop)\b': 'cord',
        r'\b(song)\b': 'chanty',
        r'\b(toilet|bathroom)\b': 'head',
        r'\b(treasure)\b': 'booty',
        # Prepositions
        r'\b(about)\b': '\'bouts',
        r'\b(for)\b': 'far',
        r'\b(in)\b': 'n',
        r'\b(with)\b': 'wit',
        # Pronouns
        r'\b(my)\b': 'me',
        r'\b(My)\b': 'Me',
        r'\b(you)\b': 'ye',
        r'\b(You)\b': 'Ye',
        r'\b(your)\b': 'yar',
        r'\b(Your)\b': 'Yar',
        r'\b(yours)\b': 'yars',
        r'\b(Yours)\b': 'Yars',
        # Verbs
        r'\b(are)\b': 'be',
        r'\b(do)\b': 'doos',
        r'\b(have a drink|take a drink|get a drink)\b': 'carouse',
        r'\b(sleep)\b': 'lay',
        r'\b(like)\b': 'likes',
        r'\b(rob)\b': 'pillage',
        r'\b(steal)\b': 'plunder',
        r'\b(want)\b': 'wants',
        r'\b(will)\b': 'be',
        # Other
        r'\B(ing)\b': 'in', # Replaces "ing" endings with "in"
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
        # Adjectives
        
        # Adverbs
        
        # Expressions, phrases, and commands
        r'\b(it is)\b': 'tis',
        
        # Nouns
        
        # Prepositions
        
        # Pronouns
        r'\b(my)\b': 'mine',
        r'\b(you|your|yours)\b': 'thou',
        # Verbs
        r'\b(are)\b': 'art',
        r'\b(should|shall)\b': 'shalt',
        # Other
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
        # Adjectives
        r'\b(everlasting)\b': 'everliving',
        r'\b(good|great)\b': 'irie',
        r'\b(higher)\b': 'iya',
        r'\b(this)\b': 'dis',
        # Adverbs
        r'\b(continually)\b': 'itinually',
        r'\b(up)\b': 'op',
        r'\b(yes|yeah)\b': 'yah',
        # Expressions, phrases, and commands
        r'\b(isn\'t)\b': 'inna',
        # Nouns
        r'\b(Africa|Ethiopia|heaven|Heaven)\b': 'Zion',
        r'\b(brothers)\b': 'brethren',
        r'\b(cannibis)\b': 'ganja',
        r'\b(dedication)\b': 'livication',
        r'\b(depression)\b': 'uppression',
        r'\b(god|God)\b': 'jah',
        r'\b(government|society|institution)\b': 'Babylon',
        r'\b(creator)\b': 'irator',
        r'\b(invention)\b': 'outvention',
        r'\b(joy)\b': 'ites',
        r'\b(man)\b': 'mon',
        r'\b(oppression)\b': 'downpression',
        r'\b(politics)\b': 'politricks',
        r'\b(sister)\b': 'sista',
        r'\b(sisters)\b': 'sistren',
        r'\b(understanding)\b': 'overstanding',
        r'\b(unity)\b': 'inity',
        # Prepositions
        r'\b(about)\b': 'bout',
        r'\b(the)\b': 'da',
        # Pronouns
        r'\b(me|my|I)\b': 'I and I',
        r'\b(you)\b': 'ya',
        # Verbs
        r'\b(apreciate)\b': 'aprecilove',
        r'\b(depress)\b': 'uppress',
        # Other
        
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
