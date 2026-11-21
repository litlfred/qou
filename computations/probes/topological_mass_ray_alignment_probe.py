#!/usr/bin/env python3
"""Probe: do the corpus's mass-tower pieces lie on a common ray?

Context. `conj:topological-mass` asserts ‖t‖ = ‖d‖ + Σ‖τ_i‖ where t = d + Σ τ_i.
`QOU.Torsion.mass_decomposition_eq_iff` (sorry-free) proves this holds iff the
pieces lie pairwise on a common ray; for real pieces, iff they share a sign.

The only corpus producer that evaluates descended and transient pieces
separately is `computations/mass_endomorphism.py::mass_from_tower_mp`:

    desc   = |Π_i V̂_full,i|                     (descended, Markov-trace product)
    single = Σ_i Φ_q(V̂_full,i)                  (one blow-up centre per generator)
    cross  = Σ_{i<j} z² Φ_q(|V̂_full,i V̂_full,j|) (pair blow-up centres)
    mass   = desc + single + cross

That producer DEFINES the mass as a sum of norms, i.e. it assumes the
conjecture; it has no independently computed total trace value to compare
against. What it does carry are the SIGNED pieces before the norm is taken.
This probe reports their signs. It chooses nothing: the crossing tables are
the producer's, rebuilt on the mp layer with HA = q - q^-1 in mpf (the
producer's own mp mirror reads the float64 table, which caps precision).

The identification "signed descended piece = Π V̂_full" is the producer's.
Whether the signed TRANSIENT trace value equals Φ_q(V̂) (rather than only its
norm, which is all `conj:topological-mass-dilogarithm` asserts) is NOT fixed by
the corpus; it is reported as a reading, not as a finding.

No witness is written (probe). mpmath only.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import _path_bridge  # noqa: F401, E402
from mpmath import mp  # noqa: E402

mp.dps = 60

import mass_endomorphism as me  # noqa: E402  (module import does not run __main__)

q = mp.mpf(me.q0_mp)
HA = q - 1 / q
z = q ** 3 / (q ** 2 + 1)
w_sym, w_std, w_alt = (mp.mpf(me.w_sym_mp), mp.mpf(me.w_std_mp), mp.mpf(me.w_alt_mp))
ONE, ZERO = mp.mpf(1), mp.mpf(0)

# Crossing tables: the producer's, entry for entry, with (c, d) in mpf.
SIG, SIGINV, HALF = (ONE, ZERO), (ONE, -HA), (ONE, -HA / 2)
TABLES = {
    "electron": (2, {0: [SIG] * 3}),
    "proton": (3, {0: [SIG] * 3 + [SIG] + [HALF] + [SIG] * 2,
                   1: [SIGINV] * 3 + [HALF]}),
    "neutron": (3, {0: [SIG] * 3 + [SIGINV] + [HALF] + [SIG] * 2,
                    1: [SIGINV] * 3 + [HALF]}),
}


def vols(n_strands, cross):
    out = []
    for gen in range(n_strands - 1):
        a, b, sp, ap = ZERO, ONE, ONE, ONE
        for c, d in cross.get(gen, []):
            a, b = a * c * HA + a * d + b * c, a * c + b * d
            sp *= c * q + d
            ap *= -c / q + d
        vs = z * a + b
        out.append(w_sym * sp + w_std * vs + w_alt * ap)
    return out


def phi(x):
    x = mp.mpf(x)
    if abs(x) >= q:
        return mp.inf
    prod, qp = ONE, 1 / q
    tiny = mp.mpf(10) ** (-(mp.dps + 5))
    for _ in range(100000):
        t = qp * x
        prod /= 1 - t
        if abs(t) < tiny:
            break
        qp /= q
    return prod


def sgn(x):
    return "+" if x > 0 else ("-" if x < 0 else "0")


print(f"q0 = {mp.nstr(q, 25)}   (q_parameter.Q_MP, manifest-selected pin)")
print(f"z_D = q^3/(q^2+1) = {mp.nstr(z, 25)}")
allok = True
for name, (n, tab) in TABLES.items():
    V = vols(n, tab)
    desc_signed = mp.fprod(V)
    singles = [phi(v) for v in V]
    crosses = [z ** 2 * phi(abs(V[i] * V[j]))
               for i in range(len(V)) for j in range(i + 1, len(V))]
    pieces = [desc_signed] + singles + crosses
    sum_norms = mp.fsum(abs(p) for p in pieces)
    norm_sum = abs(mp.fsum(pieces))
    signs = "".join(sgn(p) for p in pieces)
    aligned = all(p >= 0 for p in pieces) or all(p <= 0 for p in pieces)
    print(f"\n{name}: V_full = {[mp.nstr(v, 20) for v in V]}")
    print(f"  signed descended  Π V_full = {mp.nstr(desc_signed, 25)}")
    print(f"  transient singles Φ_q(V)   = {[mp.nstr(s, 20) for s in singles]}")
    print(f"  transient pairs   z²Φ_q    = {[mp.nstr(c, 20) for c in crosses]}")
    print(f"  piece signs (desc, singles, pairs) = {signs}   common ray: {aligned}")
    print(f"  Σ‖piece‖ (producer's mass)        = {mp.nstr(sum_norms, 30)}")
    print(f"  ‖Σ piece‖                          = {mp.nstr(norm_sum, 30)}")
    print(f"  gap Σ‖·‖ − ‖Σ·‖                    = {mp.nstr(sum_norms - norm_sum, 30)}")
    # Self-check against the theorem: gap == 0 iff aligned.
    gap_zero = abs(sum_norms - norm_sum) < mp.mpf(10) ** (-(mp.dps - 10))
    if gap_zero != aligned:
        allok = False
        print("  CHECK FAILED: gap-zero and ray-alignment disagree")
print("\nself-check (gap = 0  <=>  common ray, per mass_decomposition_eq_iff):",
      "PASS" if allok else "FAIL")
sys.exit(0 if allok else 1)
