#!/usr/bin/env python3
"""Nahm data of the lepton bundles R^aL from their Neumann–Zagier rows (bean qou-35a8).

Companion to `QOU/MassTheory/LeptonBundleNahm.lean`. For each LR word (RL = 4₁ control,
RRL = μ word σ₀²σ₁⁻¹, RRRRL = τ word σ₀⁴σ₁⁻¹) this probe

1. builds the Floyd–Hatcher layered triangulation and its rect-form rows
   ∏ z^a (1−z)^b = ±1 with `nz_gluing_from_braid_monodromy_probe` (no SnapPy);
2. keeps all edge rows but the first, adds the first cusp row independent of the edges,
   and forms N = −B⁻¹A, the quadratic form of the Φ_b state integral of that
   triangulation (Dimofte–Garoufalidis 2013);
3. checks N is symmetric and integral;
4. checks, by EXACT reduction modulo the minimal polynomial, that the exact shapes solve
   1 − z_i = ∏_j z_j^{N_ij} with every sign +1, and that every gluing row holds;
5. reports Σ D(z_i) at 50 dps as an identification of the complete structure
   (Im z > 0). The volume is reported, never used as an input.

No measured value enters. Exit 1 on any failed check.
"""
from __future__ import annotations

import contextlib
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

import nz_gluing_from_braid_monodromy_probe as nz  # noqa: E402

set_compute_dps()
mp.dps = 50

y, s, w = sp.symbols("y s w")
# exact shapes, in the order of the probe's tetrahedra (generator, minimal polynomial, shapes)
EXACT = {
    "RL": (w, w**2 - w + 1, [w, w]),
    "RRL": (y, 2 * y**2 - 3 * y + 2, [y + sp.Rational(1, 2), y, y]),
    "RRRRL": (s, s**3 - 6 * s**2 + 8 * s - 4,
              [sp.Rational(1, 2) + s - s**2 / 4, 2 * s - s**2,
               sp.Rational(1, 2) + s - s**2 / 4, s, s]),
}
# the root with Im > 0 (complete structure) used only for the reported volume
ROOT = {
    "RL": "0.5+0.8660254j",
    "RRL": "0.75+0.6614378j",
    "RRRRL": "0.808512116+0.508851779j",
}

FAILS: list[str] = []


def check(name: str, ok: bool) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS.append(name)


def bloch_wigner(z):
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def rows(word):
    tets, maps = nz.layer(word)
    M = next(Mm for Mm in maps if Mm.trace() > 0)
    with contextlib.redirect_stdout(io.StringIO()):
        t, g, n, _cl, er, _cv, cy = nz.run_word(word, M, word)
    hr = nz.holonomy_rows(t, g, None, cy)
    nt = nz.nontrivial_cycles(er, hr)
    return n, er, hr[nt[0]][0], M


def reduce_mod(expr, gen, m):
    num, den = sp.fraction(sp.together(expr))
    inv = sp.invert(sp.rem(sp.expand(den), m, gen), m, gen)
    return sp.rem(sp.expand(num * inv), m, gen)


def main() -> int:
    for word, (gen, m, Z) in EXACT.items():
        n, er, cusp, M = rows(word)
        print(f"\n== {word}  (monodromy {M.tolist()}, trace {M.trace()}, {n} tetrahedra)")
        R = er[1:] + [cusp]
        A = sp.Matrix([r[0] for r in R])
        B = sp.Matrix([r[1] for r in R])
        check(f"{word}_B_invertible", B.det() != 0)
        N = -(B.inv() * A)
        print(f"  A = {A.tolist()}\n  B = {B.tolist()}\n  N = {N.tolist()}")
        check(f"{word}_N_symmetric", N == N.T)
        check(f"{word}_N_integral", all(x.is_integer for x in N))
        check(f"{word}_rect_identity_A_plus_BN_zero", A + B * N == sp.zeros(n, n))
        nahm_ok = all(
            reduce_mod(1 - Z[i] - sp.Mul(*[Z[j] ** int(N[i, j]) for j in range(n)]), gen, m) == 0
            for i in range(n))
        check(f"{word}_exact_nahm_equations_all_signs_plus", nahm_ok)
        rows_ok = all(
            reduce_mod(sp.Mul(*[Z[j] ** a[j] * (1 - Z[j]) ** b[j] for j in range(n)]) - sgn, gen, m) == 0
            for (a, b, sgn) in er + [cusp])
        check(f"{word}_all_gluing_rows_hold_exactly", rows_ok)
        r0 = mp.findroot(lambda x: sp.lambdify(gen, m, "mpmath")(x), mp.mpc(complex(ROOT[word])))
        zs = [mp.mpc(sp.lambdify(gen, z, "mpmath")(r0)) for z in Z]
        check(f"{word}_root_upper_half_plane", all(mp.im(z) > 0 for z in zs))
        print(f"  disc(minpoly) = {sp.discriminant(m, gen)}")
        print(f"  sum D(z_i) at the Im>0 root = {mp.nstr(sum(bloch_wigner(z) for z in zs), 30)}")
    print(f"\n{len(FAILS)} failed")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
