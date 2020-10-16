class cell():
    def _init_(self, pos) :
        self.possibleAnswers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.answer = None
        self.position = pos
        self.solved = False
        