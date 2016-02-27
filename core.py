class BlockMatrix:
    blocks = []

    def __init__(self, blocks):
        self.blocks = blocks

    def __mul__(self, other):
        """
        Matrix multiplication can be reduced to multiplication
        on the level of individual matrices.
        :param other:
        :return:
        """
        blocks = []
        if len(self) == len(other):
            for i, j in zip(self.blocks, other.blocks):
                blocks.append(i*j)
        return BlockMatrix(blocks)


    def __lshift__(self, other):
        """
        Direct product multiplication is implemented by <<, as we are basically
        pushing one matrix into another.
        :param other:
        :return:
        """
        return BlockMatrix(blocks=self.blocks + [other])

    def __len__(self):
        return len(self.blocks)

    def __str__(self):
        return ' \u2297 '.join([str(i) for i in self.blocks])

class Quaternion:
    """
    Here I use quaternions because they behave like the Pauli matrices,
    (1, i sigma_x, i sigma_y, i sigma_z)
    """
    def __init__(self, index, factor=1):
        self.index = index
        self.factor = factor

    def __mul__(self, other):
        if self.index == other.index:
            factor = -1 if self.index > 0 else 1
            factor *= self.factor * other.factor
            return Quaternion(0, factor)
        elif self.index == 0 or other.index == 0:
            return self if other.index == 0 else other
        else:
            raise NotImplementedError()

    def __str__(self):
        name = ['1', 'i', 'j', 'k']
        return '{}{}'.format(self.factor if self.factor != 1 else '', name[self.index])

unit = Quaternion(0)
i = Quaternion(1)
a = BlockMatrix([unit, Quaternion(3)])
print(a)
print(a*a)
b = a << i
print(b)