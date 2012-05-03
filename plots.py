from fSequencing import *
from ZeroOnePlotter import Plotter

f1 = lambda x: 2.2 * (x - x**2)
funcSequence = SequenceForFunction(f1, 0.0, 1.0, 200)
pfunc = Plotter(funcSequence)

sequence = SequenceForIteratedFunction(f1, 0.2, 200)
p = Plotter(sequence)


f2 = lambda x: 3.2 * (x - x**2)

sequence = SequenceForIteratedFunction(f2, 0.2, 200)
p = Plotter(sequence)

f3 = lambda x: 3.5 * (x - x**2)

sequence = SequenceForIteratedFunction(f3, 0.2, 200)
p = Plotter(sequence)

f4 = lambda x: 3.8 * (x - x**2)

sequence = SequenceForIteratedFunction(f4, 0.2, 200)
p = Plotter(sequence)

sequence = SequenceForIteratedFunction(f4, 0.21, 200)
p = Plotter(sequence)