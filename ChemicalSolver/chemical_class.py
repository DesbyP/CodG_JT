import re


class Equation(object):
    def __init__(self, seq_str):
        # check input
        assert re.fullmatch('[A-Za-z0-9+ ]+->[A-Za-z0-9+ ]+', seq_str), "Invalid equation: {}".format(seq_str)
        self.seq = seq_str
        self.left_eq = None
        self.right_eq = None

    def parse_seq(self):
        parse = self.seq.replace(" ", "").split("->", len(self.seq))
        self.left_eq = EquationSide(parse[0])
        self.right_eq = EquationSide(parse[1])
        self.left_eq.parse()
        self.right_eq.parse()


class EquationSide(object):
    def __init__(self, half_seq_str):
        self.half_seq = half_seq_str
        self.list_mol = []

    def parse(self):
        list_mol = self.half_seq.split("+", len(self.half_seq))
        for i in range(len(list_mol)):
            self.list_mol.append(Molecule(list_mol[i]))
            self.list_mol[i].parse()

        print(list_mol)

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
