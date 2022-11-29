import json

class Score:
    """Score class
    """
    def __init__(self, filename) -> None:
        """Constructor

        Args:
            filename (str): name of the json file to read
        """
        tmp_list = []
        self.filename = filename

        with open(self.filename, "r") as fp:
            json_data = json.load(fp)
            for score in json_data:
                tmp_list.append(score)

        self.score_list = sorted(tmp_list, key=lambda x: x["score"], reverse=True)
            
    def __len__(self):
        return len(self.score_list)

    def get_scores(self):
        """Method to get all scores

        Returns:
            list: the list of all scores
        """
        scores = []

        for score in self.score_list:
            scores.append(score)

        return scores

    def save(self):
        """Method to save and write into the json file
        """
        with open(self.filename, "w") as fp:
            json.dump(self.score_list, fp)

    def add_score(self, username, score):
        """Method to add a score

        Args:
            username (str): username of the player
            score (int): the score integer

        Raises:
            ValueError: if username is not str or score is not int
            ValueError: is username is empty str

        Returns:
            boolean: true when score added successfully
        """

        if (type(username) is not str or type(score) is not int):
            raise ValueError
        if username == "":
            raise ValueError

        score_dict = {
            "username": username,
            "score": score
        }

        self.score_list.append(score_dict)
        return True