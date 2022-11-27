import json

class Score:
    def __init__(self, filename) -> None:
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
        scores = []

        for score in self.score_list:
            scores.append(score)

        return scores

    def save(self):
        with open(self.filename, "w") as fp:
            json.dump(self.score_list, fp)

    def add_score(self, id, score):

        if (type(id) is not str or type(score) is not int):
            raise ValueError
        if id == "":
            raise ValueError

        score_dict = {
            "id": id,
            "score": score
        }

        self.score_list.append(score_dict)
        return True