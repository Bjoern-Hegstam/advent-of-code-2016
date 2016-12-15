#!/usr/bin/env python

import fileinput
import argparse
import re

class Disc:
    def __init__(self, h, p0, N):
        self.h = h
        self.p0 = p0
        self.N = N

    def get_pos(self, t):
        return (self.p0 + t) % self.N

    def __repr__(self):
        return 'Disc #{0} has {1} positions; at time=0, it is at position {2}.'.format(self.h, self.N, self.p0)

def main(part, files):
    discs = []
    lines = [line.strip() for line in fileinput.input(files)]

    for line in lines:
        vals = re.match(r'^Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)\.$', line)
        params = [int(v) for v in vals.groups()]
        discs.append(Disc(params[0], params[2], params[1]))

    print_equation_system(discs)

    #print('Drop time: {}'.format(find_drop_time(discs)))


def print_equation_system(discs):
    varibles = 'abcdefghiklmnopqstuvxyz'
    for disc in discs:
        print('0 = {0:2d} + t + {1:2d}{2}'.format(disc.h + disc.p0, disc.N, varibles[disc.h - 1]), end=', ')


def find_drop_time(discs):
    drop_time = 0
    t = 0
    ball_pos = 0

    while True:
        t += 1
        ball_pos += 1
        print('\nt({0}) - B({1})'.format(t, ball_pos))

        for disc in discs:
            print('D({0}) - {1}'.format(disc.h, disc.get_pos(t)))

        if discs[ball_pos - 1].get_pos(t) != 0:
            ball_pos = 0
            drop_time = t
            continue

        if ball_pos == len(discs):
            break

        ball_pos

    return drop_time

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default='1', type=int)
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    main(args.part, args.files)
