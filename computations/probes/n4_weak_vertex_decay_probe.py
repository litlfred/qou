#!/usr/bin/env python3
"""Can the weak vertex W turn one J_4 flavour state into the other on the n=4 left doublet?

Bean qou-wkcd, the n >= 4 lead, step "is neutron decay constructible". Inputs are all
already in the corpus; nothing is fitted and no measured number is used.
  * (3,1) rep of H_4(q) and the J_4 flavour projectors Ja (eigenvalue q^-2) and
    Jb (q^4) on sigma_1's left line: QOU/QuarkState/FlavourDoubletFourStrands.lean.
  * Weak vertex on a positive letter sigma: W(sigma) = sigma - h * P_L(sigma),
    h = q - 1/q, P_L(sigma) = (sigma + 1/q)/(q + 1/q) (the q-line, |q| > 1):
    QOU/QuarkState/WeakVertexLeftProjector.lean (weakVertex_sub_letter).

Pre-registered (2026-11-15, before any run):
  P1  W at site 1 or 2 commutes with J_4, so it never changes the J_4 flavour.
      (Expected from J_4 commuting with H_3; checked, not assumed.)
  P2  The insertion at site 3, P_L(sigma_3), connects Ja and Jb: Jb P_L(s3) Ja != 0.
  P3  For each reading-3 passing gamma-gamma word w of the probe
      n4_left_doublet_flavour_probe.py (m = 3: 000, 111; m = 4: 0101, 1010, all
      orientations), replace ONE positive sigma_3 letter by W(sigma_3). Record the
      change in the flavour-flip amplitude Jb w Ja, and whether that change stays on
      sigma_1's left line (no right-line component on either side).
  Outcome is reported whatever it is. Which of Ja/Jb is n and which is p is NOT
  decided here (owner call); amplitudes are reported for both directions.

Scope: only positive sigma_3 letters get a vertex. The corpus vertex is defined for a
letter of the Hecke quadratic s^2 = h s + 1; an inverse letter has its own left line
(the -q line), and how the vertex acts there is not ruled, so it is not tested.
Exact: sympy, symbolic q. "nonzero" means not identically zero as a rational function.
"""
import itertools
import sys

import sympy as sp

q = sp.symbols("q", nonzero=True)
I3 = sp.eye(3)
n = q**2 + 1
h = q - 1 / q

s1 = sp.diag(q, q, -1 / q)
s3 = sp.diag(q, -1 / q, q)
s2 = sp.Matrix([[q**2 - 1, -(q**4 + 1), q**2 * (q**4 + 1)],
                [-q**2, q**4, q**4],
                [1, 1, q**4]]) / (q * n)
S = [s1, s2, s3]
Si = [sp.simplify(s - h * I3) for s in S]
PLs = [sp.simplify((s + I3 / q) / (q + 1 / q)) for s in S]
W = [sp.simplify(S[i] - h * PLs[i]) for i in range(3)]

PL = sp.diag(1, 1, 0)
PR = sp.diag(0, 0, 1)
J4 = sp.simplify(s3 * s2 * s1 * s1 * s2 * s3)
Ja = sp.simplify(PL * (J4 - q**4 * I3) / (q**-2 - q**4))
Jb = sp.simplify(PL * (J4 - q**-2 * I3) / (q**4 - q**-2))

ok = True


def check(name, cond):
    global ok
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    ok &= bool(cond)


def zero(M):
    return all(sp.simplify(x) == 0 for x in M)


print("0. inputs")
for i in range(3):
    check(f"W(s{i+1}) = s{i+1}^-1 on its left line, s{i+1} on its right line",
          zero(W[i] * PLs[i] - Si[i] * PLs[i])
          and zero(W[i] * (I3 - PLs[i]) - S[i] * (I3 - PLs[i])))
check("Ja + Jb = PL", zero(Ja + Jb - PL))

print("1. P1: W at sites 1, 2 keeps the J_4 flavour")
for i in (0, 1):
    check(f"W(s{i+1}) J4 = J4 W(s{i+1})", zero(W[i] * J4 - J4 * W[i]))

print("2. P2: the site-3 insertion connects the two flavours")
ba = sp.simplify(Jb * PLs[2] * Ja)
ab = sp.simplify(Ja * PLs[2] * Jb)
print("  Jb P_L(s3) Ja =", sp.factor(ba))
print("  Ja P_L(s3) Jb =", sp.factor(ab))
check("Jb P_L(s3) Ja != 0", not zero(ba))
check("Ja P_L(s3) Jb != 0", not zero(ab))
check("both stay on sigma_1's left line",
      zero(PR * ba) and zero(ba * PR) and zero(PR * ab) and zero(ab * PR))


def vertex_letters(site, mirror):
    a, b = site, site + 1
    return [(a, -1), (b, 1)] if mirror else [(a, 1), (b, -1)]


def mat(letters):
    M = I3
    for i, e in letters:
        M = M * (S[i] if e == 1 else Si[i])
    return M


print("3. P3: one weak vertex on a positive sigma_3 letter of a passing word")
patterns = {3: ["000", "111"], 4: ["0101", "1010"]}
summary = []
for m, pats in patterns.items():
    for pat in pats:
        for orient in itertools.product([0, 1], repeat=m):
            letters = []
            for c, o in zip(pat, orient):
                letters += vertex_letters(int(c), o)
            name = ".".join(("Vb" if o else "V") + c for c, o in zip(pat, orient))
            free = mat(letters)
            free_ba = sp.simplify((Jb * free * Ja))
            free_ab = sp.simplify((Ja * free * Jb))
            slots = [k for k, (i, e) in enumerate(letters) if i == 2 and e == 1]
            if not slots:
                summary.append((name, None, None, None, None, None))
                continue
            for k in slots:
                delta = sp.simplify(-h * mat(letters[:k]) * PLs[2] * mat(letters[k + 1:]))
                d_ba = sp.simplify(Jb * delta * Ja)
                d_ab = sp.simplify(Ja * delta * Jb)
                leak = not (zero(PR * delta * Ja) and zero(PR * delta * Jb))
                summary.append((name, k, zero(free_ba) and zero(free_ab),
                                not zero(d_ba), not zero(d_ab), leak))
for name, k, free0, ba_, ab_, leak in summary:
    if k is None:
        print(f"  {name:22s} no positive sigma_3 letter: no vertex slot")
    else:
        print(f"  {name:22s} slot {k}: free flip=0? {free0}  "
              f"vertex Ja->Jb: {'nonzero' if ba_ else '0'}  Jb->Ja: {'nonzero' if ab_ else '0'}  "
              f"right-line leak: {leak}")
with_slot = [r for r in summary if r[1] is not None]
print(f"  words with a slot: {len({r[0] for r in with_slot})} of {len({r[0] for r in summary})}")
print(f"  slots where the vertex changes Ja->Jb: {sum(1 for r in with_slot if r[3])} of {len(with_slot)}")
print(f"  slots with a right-line leak: {sum(1 for r in with_slot if r[5])} of {len(with_slot)}")

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
