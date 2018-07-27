from itertools import groupby

class newssearch(object):

    def __init__(self, content):
        self._idx = {
            # create dict pair word: set of references
            k: set([i for w, i in g]) for k, g in groupby(
                # the list has to be sorted by first element in the tuple,
                # i.e. the word
                # required by itertools.groupby implementation
                sorted(
                    # create a list of tuples (word, reference)
                    [ (word, ref) for ref,news in enumerate(content)
                        for word in news.split()],
                    key=lambda (w, i): w
                ),
                lambda (w,i): w
            )
        }

    def orquery(self, oqry):
        # reduce all the matching words' reference sets to union set
        return reduce(
            set.union,
            [self._idx[word]
                for word in oqry.split()
                if word in self._idx ]
        )

    def andquery(self, aqry):
        # reduce words' reference sets to intersection sets
        # if a word is not found in the index, the result is empty set 
        sr = set()
        try:
            sr = reduce(set.intersection, [self._idx[word] for word in aqry.split()])
        except KeyError, e:
            print 'keyword not found: '+str(e)
        return sr
