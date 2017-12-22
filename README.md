# MaxMatch
This is a simple implementation of the maxmatch algorithm for word segmentation

I initially wrote this based on the template in in the first chapter of Jurafsky and Martin's "Speech and Language Processing" for
the MaxMatch algorithm.

I tested this on a few trending hashtags from Twitter, but wasn't happy with the performance. Part of the problem was that the 
English dictionary I found online was a little too broad (containing word mispellings and weird acronyms/text speak) and that the
standard MaxMatch will recursively parse based on the first segment that is found in the unsegmented word. The solution to this is
twofold: use a simplified dictionary and use a heuristic.

The former is too difficult for my taste (I couldn't find another on in json format, which I prefer for super fast lookups), so I
wrote a modified version of MaxMatch. This simply allowed the greedy algorithm to continuously run on the unsegmented word, such 
that all valid segmentations could be found. From here, it simply computed the the segmentation with the highest character per word
ratio.

