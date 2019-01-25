class Position:
    def __init__(self, py):
        self.py = py
        self.data = self.to_array(py)

    def to_array(self, py):
        data = []
        for i in range(len(py.plateau)):
            for j in range(len(py.plateau[i].etageArray)):
                for k in range(len(py.plateau[i].etageArray[j])):
                    data.append
