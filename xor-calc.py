#!/usr/bin/python

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))


a = "30167b0eb4eef511ec82272b4b47a2d71471"
b = "1319057cb23c1dcbf616876372617fff8b48"

binary_a = a.decode("hex")
binary_b = b.decode("hex")

xored = xor_strings(binary_a, binary_b).encode("hex")

print xored