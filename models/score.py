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

    def get_scores(self, id=None):
        """Method to get all scores

        Returns:
            list: the list of all scores
        """
        scores = []

        if id is None:
            for score in self.score_list:
                scores.append(score)
        else:
            for score in self.score_list:
                if score["id"] == id:
                    scores.append(score)

        return scores

    def find_user(self, user, password):
        """Method to find a user

        Args:
            user (str): the username to find

        Raises:
            ValueError: if user is not str

        Returns:
            boolean: true if user is found
        """
        if type(user) is not str:
            raise ValueError
        if type(password) is not str:
            raise ValueError

        if user == "" or password == "":
            raise ValueError

        for score in self.score_list:
            if score["username"] == user and score["password"] == password:
                return score

        return False

    def delete_score(self, id):
        """Method to delete a score

        Args:
            id (str): id of the score

        Raises:
            ValueError: if id is not str

        Returns:
            boolean: true if score is deleted
        """
        if type(id) is not str:
            raise ValueError

        for score in self.score_list:
            if score["id"] == id:
                self.score_list.remove(score)
                return True

        return False

    def save(self):
        """Method to save and write into the json file
        """
        with open(self.filename, "w") as fp:
            json.dump(self.score_list, fp)

    def add_score(self, id, username, password, score, date):
        """Method to add a score

        Args:
            id (str): id of the score
            username (str): username of the player
            password (str): password of the player
            score (int): the score integer
            date (str): the date of the score

        Raises:
            ValueError: if username, password, or date are not str
            ValueError: if score is not int
            valueError: if date, username, or password are empty str

        Returns:
            boolean: true when score added successfully
        """

        if type(id) is not str:
            raise ValueError
        if type(username) is not str or type(score) is not int:
            raise ValueError
        if type(date) is not str or type(password) is not str:
            raise ValueError
        if username == "" or password == "" or date == "" or id == "":
            raise ValueError

        score_dict = {
            "id": id,
            "username": username,
            "password": password,
            "score": score,
            "date": date
        }

        self.score_list.append(score_dict)
        return True