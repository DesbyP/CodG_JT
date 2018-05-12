import re


class Equation(object):
    def __init__(self, seq_str):
        # check input
        assert re.fullmatch('[A-Za-z0-9+ ]+->[A-Za-z0-9+ ]+', seq_str), "Invalid equation: {}".format(seq_str)
        self.seq = seq_str

    def parse_seq(self):
        parse = self.seq.replace(" ", "").split("->", len(self.seq))
        print(parse)


class EquationSide(object):
    def __init__(self, half_seq_str):
        self.half_seq = half_seq_str

    def parse(self):
        pass


class Molecule(object):
    def __init__(self, molecule_str):
        self.molecule = molecule_str

    def parse(self):
        pass


class Atom(object):
    def __init__(self, atom_str):
        self.atom = atom_str

    def parse(self):
        pass
