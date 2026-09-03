"""probe_alpha — series of alpha = (z - 1)h/2 and cos(alpha) around q = 1.

Convention **D**: z = q^3/(q^2 + 1). This read `z = sp.sqrt(q)/(1 + q)` —
convention C, excised by the 2026-08-09 owner ruling and reaffirmed
2026-08-15 R1 — until 2026-08-25. The convention is not cosmetic, and where it bites is worth
recording: both give z(1) = 1/2, so the two series AGREE at first order
(alpha = -w/2 + ...) and diverge from second order on —

    C:  alpha = -w/2 +   w^2/4 - 5w^3/16 + ...
    D:  alpha = -w/2 + 5*w^2/4 -  w^3/2  + ...

A check that looked only at the classical limit would not have separated them.

The series is written in w = q - 1 so the expansion is about the classical
point. Nothing consumes this file and it emits no witness; it is kept as a
scratch expansion, now in the canonical convention.
"""
import sympy as sp

w = sp.Symbol('w')
q = 1 + w
z = q**3 / (q**2 + 1)          # convention D
h = q - 1 / q
alpha = (z - 1) * h / 2

print("alpha:", alpha.series(w, 0, 6))
print("cos(alpha):", sp.cos(alpha).series(w, 0, 6))
