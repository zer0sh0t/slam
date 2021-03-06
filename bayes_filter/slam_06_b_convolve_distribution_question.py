# Instead of moving a distribution, move (and modify) it using a convolution.
# 06_b_convolve_distribution
# Claus Brenner, 26 NOV 2012
from pylab import plot, show, ylim
from distribution import *

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)

def convolve(a, b):
    """Convolve distribution a and b and return the resulting new distribution."""
   
    #print "a: ", a
    #print "b: ", b

    dist_lst = []
    # offs = (a.offset + b.offset) #- ((len(b.values)-1)/2) # og
    offs = a.offset + b.offset - (len(b.values) / 2) - 1
    for a_val in a.values:
        res = []
        for b_val in b.values:
            res.append(a_val*b_val)
        dist_lst.append(Distribution(offs, res))
        offs +=1
    c = Distribution.sum(dist_lst)
    
    return c  # Replace this by your own result.


if __name__ == '__main__':
    #arena = (0,100)
    arena = (0,250)

    # Move 3 times by 20.
    #moves = [20] * 3
    moves = [20] * 10

    # Start with a known position: probability 1.0 at position 10.
    position = Distribution.unit_pulse(10)
    plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         linestyle='steps')

    # Now move and plot.
    for m in moves:
        move_distribution = Distribution.triangle(m, 2)
        position = convolve(position, move_distribution)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             linestyle='steps')

    ylim(0.0, 1.1)
    show()
