#!/usr/bin/env python3
"""Four-strand left doublet: does a flavour label survive the one gamma-gamma rule?

Bean qou-wkcd, the n >= 4 lead. Lean side:
QOU/QuarkState/FlavourDoubletFourStrands.lean (explicit (3,1) representation of H_4(q),
two flavour labels on sigma_1's left line, both proved for all q).

Pre-registered (2026-11-15, before any run):
  chirality = sigma_1 eigenline (left = q-line);
  label A   = sigma_3 eigenline on the left line (u = q-line, d = -q^{-1}-line);
  pass      = gamma-gamma words that pass reading 3 act differently on the two flavour
              states, and a gamma-gamma vertex flips flavour while vanishing on the right line.
Added after the label-A run (owner choice "both, side by side"):
  label B   = J_4 eigenline on the left line, J_4 = s3 s2 s1 s1 s2 s3 (Jucys-Murphy).
  Chosen because J_4 commutes with every 3-strand word, not because of its numbers.

Words tested: the gamma-gamma vertices V_s = sigma_s sigma_{s+1}^{-1}, Vb_s its mirror,
sites s in {0, 1} (0-indexed), and the reading-3 PASSING site patterns for m = 3, 4
reported by the SM thread (claude/gg-four-strand-2026-11-15, 1d8f88a737c):
m = 3: 000, 111; m = 4: 0101, 1010; every V/Vb orientation of each.

Exact: sympy rational functions in symbolic q. No floats, no witness, nothing fitted
(no free parameters). The generic-q nonvanishing is checked as "not identically zero".
"""
import itertools
import sys

import sympy as sp

q = sp.symbols("q", nonzero=True)
I3 = sp.eye(3)
n = q**2 + 1
D = q**4 + q**2 + 1

s1 = sp.diag(q, q, -1 / q)
s3 = sp.diag(q, -1 / q, q)
s2 = sp.Matrix([[q**2 - 1, -(q**4 + 1), q**2 * (q**4 + 1)],
                [-q**2, q**4, q**4],
                [1, 1, q**4]]) / (q * n)
S = [s1, s2, s3]
Si = [sp.simplify(s - (q - 1 / q) * I3) for s in S]

ok = True


def check(name, cond):
    global ok
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    ok &= bool(cond)


def zero(M):
    return all(sp.simplify(x) == 0 for x in M)


print("1. H_4 relations")
for i, s in enumerate(S):
    check(f"quadratic s{i+1}", zero((s - q * I3) * (s + I3 / q)))
check("braid s1 s2 s1", zero(s1 * s2 * s1 - s2 * s1 * s2))
check("braid s2 s3 s2", zero(s2 * s3 * s2 - s3 * s2 * s3))
check("s1 s3 = s3 s1", zero(s1 * s3 - s3 * s1))

PL = sp.diag(1, 1, 0)
PR = sp.diag(0, 0, 1)
labels = {
    "A (sigma_3)": (sp.diag(1, 0, 0), sp.diag(0, 1, 0)),
}
J4 = sp.simplify(s3 * s2 * s1 * s1 * s2 * s3)
Ja = sp.simplify(PL * (J4 - q**4 * I3) / (q**-2 - q**4))
Jb = sp.simplify(PL * (J4 - q**-2 * I3) / (q**4 - q**-2))
labels["B (J_4)"] = (Ja, Jb)
print("2. J_4 commutes with s1, s2; Ja + Jb = PL")
check("J4 s1 = s1 J4", zero(J4 * s1 - s1 * J4))
check("J4 s2 = s2 J4", zero(J4 * s2 - s2 * J4))
check("Ja + Jb = PL", zero(Ja + Jb - PL))


def vertex(site, mirror):
    a, b = site, site + 1
    return Si[a] * S[b] if mirror else S[a] * Si[b]


patterns = {3: ["000", "111"], 4: ["0101", "1010"]}
print("3. reading-3 passing words: flavour amplitudes on the left doublet")
rows = []
for m, pats in patterns.items():
    for pat in pats:
        for orient in itertools.product([0, 1], repeat=m):
            w = I3
            for c, o in zip(pat, orient):
                w = w * vertex(int(c), o)
            name = ".".join(("Vb" if o else "V") + c for c, o in zip(pat, orient))
            for lab, (X, Y) in labels.items():
                xx = sp.factor(sp.simplify((X * w * X).trace()))
                yy = sp.factor(sp.simplify((Y * w * Y).trace()))
                mix = sp.factor(sp.simplify((X * w * Y * w * X).trace()))
                rows.append((name, lab, xx, yy, mix))
for name, lab, xx, yy, mix in rows:
    print(f"  {name:22s} {lab:12s} diag differ: {sp.simplify(xx - yy) != 0}   "
          f"flavour flip (XwY.YwX): {'0' if mix == 0 else 'nonzero'}")

print("4. structural checks (pre-registered pass criteria)")
three = [r for r in rows if set(r[0].replace("Vb", "").replace("V", "").split(".")) == {"0"}]
check("label B: no 3-strand passing word flips flavour",
      all(r[4] == 0 for r in three if r[1] == "B (J_4)"))
check("label A: 3-strand passing words DO flip flavour (sigma_2 moves sigma_3's line)",
      all(r[4] != 0 for r in three if r[1] == "A (sigma_3)"))
check("both labels: 3-strand passing words act differently on the two states (p != n)",
      all(sp.simplify(r[2] - r[3]) != 0 for r in three))
e = Ja * vertex(1, 0) * Jb
check("label B: strand-4 vertex V1 flips flavour (Ja V1 Jb != 0)", not zero(e))
check("label B: Ja V1 Jb vanishes on the right line", zero(e * PR) and zero(PR * e))
check("label B: strand-4 passing word 111 flips flavour",
      any(r[4] != 0 for r in rows if r[1] == "B (J_4)" and r[0].count("1") == 3
          and "0" not in r[0].replace("Vb", "").replace("V", "").replace(".", "")))

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
