"""Simple module designed to provide searching funcionalities for confidant app.

POC:
    The searching algorithm takes into account the "meta-data" of a diary record
    and it could be described as follows:

    1. Extract a score out of every diary record
        1.1 Count the number of occurancies of the keyword in the title
        1.2 Count the number of occurancies of the keyword in the content
        1.3 Add those numbers but give more weight to the title
    2. Create an ordered list of the most relevant diaries
        2.1 For a diary: the higher the score, the more relevant it is
        2.2 Ignore diaries with negative or zero score
        2.3 Sort the diaries list, most relevant first

Usage:
>>>     se = SearchEngine(list_of_diaries)
>>>     results = se.search(list_of_keywords)
>>>
>>>     # results will now contain an ordered list of most relevant diaries
"""


class SearchEngine():
    """Utility class that implements the searching algorithm.
    """

    def __init__(self, diaries, titleWeight=50):
        """`diaries` a list of Diary records to be searched and scored

        `titleWeight` the weight that is given to the title over the contents of
            a diary. It makes sense to calculate the importance of the
            title-occurance in words. E.g. If I assume that the word "beautiful"
            found in the title makes the Diary more relevant, like if I had found
            it 50 times in the content, then I should use titleWeight=50. In
            other words the concept is:
                occurance_in_title = titleWeight * occurance_in_content
        """

        self.diaries = diaries
        self.titleWeight = titleWeight

    def _scoreDiary(self, diary, keywords):
        """Scoring algorithm.

        See module's docstring for more details...
        """

        score = 0

        for key in keywords:

            # Normalize both key and strings to be searched
            # Everything should be lowercase in order for the tokens to be matched
            key = key.lower()
            title = diary.show_title().lower()
            content = diary.show_content().lower()

            # Score each part of the Diary depending on the number of occurancies
            titleScore = title.count(key)
            contentScore = content.count(key)

            # Give more weight to the keys found in title
            score += titleScore*self.titleWeight + contentScore

        return score

    def search(self, keywords):
        """Score the diaries against keywords list.

        `keywords` a list of strings
        """

        # For each Diary, append its score along with itself into the
        # relevanceList.
        # Each item in that list looks like:
        #    (score, Diary)

        relevanceList = [
            (self._scoreDiary(diary, keywords), diary)
            for diary in self.diaries
        ]

        # Sort: place more relevant (high-scored) Diaries first
        relevanceList.sort(key=lambda struct: struct[0], reverse=True)

        # Clean: remove irrelevant (zero-occurancies)
        # After that operation, that list will look like:
        #    [Diary1, Diary2, Diary3, ...]
        relevanceList = [x[1] for x in relevanceList if x[0] > 0]

        return relevanceList
