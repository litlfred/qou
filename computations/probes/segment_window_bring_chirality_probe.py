#!/usr/bin/env python3
"""segment_window_bring_chirality_probe.py — the two follow-ups to the segment-collision datum (bean `qou-jfx8`,
owner 2026-10-12: "widen the collision to k segments from each side; derive a chiral Bring term on UT(Σ₄)").
Companions: `QOU/MassTheory/SegmentCollisionDatum.lean` Part E (`window_factor`, `window_cannot_separate`) and
`QOU/Brings/BringConjugationChirality.lean`.

W  THE k-SEGMENT WINDOW. Particle a ∈ {T, ³He} (production words from `mass_at_3A_proper.atom_braid_word_3A`,
   include_inter=True, validated against the committed `atom-chi-rust-{t,3he}` characters on every two-row
   block). A window of k segments on a's side is the subalgebra on its top k strands, generators 9−k … 7
   (0-indexed). Its state is φ_a(x) = tr(a·x)/tr(a) on a basis of reduced words x. Lean Part E predicts
   φ_T = φ_He for k ≤ 3 (both chains end in the same neutron block above the bond at generator 5) and says
   nothing for k = 4, the first window that reaches the bond. Measured: the worst |φ_T − φ_He| per k.
   By Part A the other particle's side contributes a common factor, so a's side decides separation.
B  THE BRING C₅ ROTATIONS, an independent check of the Fourier argument in the Lean file. On Bring's curve
   Σx = Σx² = Σx³ = 0, the 5-cycle (g x)_k = x_{k−1} fixes p_j = (ζ^{jk}); the tangent line is computed as the
   kernel of the Jacobian (numerically, mpmath complex), and the rotation of g on it is compared with ζ^{−j}.
   Conjugate fixed points must carry conjugate rotations, and no rotation may be real.

mpmath throughout (60 dps; no float arithmetic). q₀ from the committed y-lambda witness (proton anchor).
Nothing fitted, selected or wired.
-- Ref: [manuscript] bean qou-jfx8, qou-rydq
"""
from __future__ import annotations

import json
import sys
from itertools import permutations
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
mp.mp.dps = 60
import composition_feasibility_a2_probe as cf  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
C = HERE.parent
TWO_ROW_9 = [(9,), (8, 1), (7, 2), (6, 3), (5, 4)]


def to_word(triples):
    return [(mp.mpf(c), mp.mpf(d), int(g)) for c, d, g in triples]


def reduced_words(gens):
    """One reduced word per permutation of the strands spanned by consecutive generators `gens`."""
    k = len(gens) + 1
    out = []
    for perm in permutations(range(k)):
        p, w = list(perm), []
        changed = True
        while changed:                                   # bubble sort records a reduced word
            changed = False
            for i in range(k - 1):
                if p[i] > p[i + 1]:
                    p[i], p[i + 1] = p[i + 1], p[i]
                    w.append(gens[i])
                    changed = True
        out.append(list(reversed(w)))
    return out


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    TOL = mp.mpf("1e-40")
    y9 = cf.load_y(9)
    supp = [l for l in cf.partitions_of(9) if y9[l] != 0]
    check("convention_D_support_at_n9_is_the_two_row_blocks", sorted(supp) == sorted(TWO_ROW_9), "y-lambda-at-q0 n=9")

    atoms = {}
    for tag, (Z, N) in (("t", (1, 2)), ("3he", (2, 1))):
        w = to_word(atom_braid_word_3A(Z, N, include_inter=True))
        com = json.loads((C / f"atom-chi-rust-{tag}.witness.json").read_text(encoding="utf-8"))["data"]["atom"]
        cmap = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in com["by_partition"]}
        chis = {l: cf.chi(l, w) for l in TWO_ROW_9}
        dev = max(abs(chis[l] - cmap[l]) for l in TWO_ROW_9)
        print(f"{tag}: validation worst |χ − χ_committed| on two-row blocks = {mp.nstr(dev, 5)}")
        check(f"{tag}_word_reproduces_committed_atom_characters_two_row", dev < TOL, f"atom-chi-rust-{tag}")
        atoms[tag] = (w, mp.fsum(y9[l] * chis[l] for l in TWO_ROW_9))

    # ── W: the k-segment window ──
    window = {}
    for k in (1, 2, 3, 4):
        gens = list(range(9 - k, 8))
        basis = reduced_words(gens) if gens else [[]]
        worst, rows = mp.mpf(0), []
        for x in basis:
            xw = [(mp.mpf(1), mp.mpf(0), g) for g in x]
            phi = {}
            for tag, (w, tr_a) in atoms.items():
                phi[tag] = mp.fsum(y9[l] * cf.chi(l, w + xw) for l in TWO_ROW_9) / tr_a
            sep = abs(phi["t"] - phi["3he"])
            worst = max(worst, sep)
            rows.append({"x": x, "phi_T": mp.nstr(phi["t"], 25), "phi_3He": mp.nstr(phi["3he"], 25), "sep": mp.nstr(sep, 8)})
        window[k] = (worst, rows)
        print(f"  k = {k}: window gens {gens}, {len(basis)} basis words, worst |φ_T − φ_He| = {mp.nstr(worst, 8)}")
    check("windows_k<=3_cannot_separate_T_from_3He", all(window[k][0] < TOL for k in (1, 2, 3)), "Lean window_cannot_separate")
    check("window_k=4_separates_T_from_3He", window[4][0] > mp.mpf("1e-6"), "first window reaching the bond at generator 5")

    # ── B: the Bring C₅ rotations, by direct Jacobian kernel ──
    zeta = mp.exp(2j * mp.pi / 5)
    rot = {}
    for j in (1, 2, 3, 4):
        p = [zeta ** (j * k) for k in range(5)]
        eqs = [sum(p), sum(x ** 2 for x in p), sum(x ** 3 for x in p)]
        on_curve = max(abs(e) for e in eqs) < TOL
        J = mp.matrix([[1] * 5, [2 * x for x in p], [3 * x ** 2 for x in p]])
        # kernel of J: complete J with two random-free rows by solving for vectors; use SVD-free nullspace via
        # Gaussian elimination on the 3×5 system with free variables x3, x4.
        A = mp.matrix([[J[r, c] for c in range(3)] for r in range(3)])
        ker = []
        for free in ((1, 0), (0, 1)):
            rhs = mp.matrix([-(J[r, 3] * free[0] + J[r, 4] * free[1]) for r in range(3)])
            sol = mp.lu_solve(A, rhs)
            ker.append([sol[0], sol[1], sol[2], mp.mpc(free[0]), mp.mpc(free[1])])
        g = lambda v: [v[(k - 1) % 5] for k in range(5)]   # noqa: E731  (g x)_k = x_{k−1}
        lam = g(p)[1] / p[1]
        v = ker[0]                                          # a kernel vector; tangent line = span(v, p) / p
        # write g(v) = μ v + c p in the 2-dim kernel span{v, p}; solve from two coordinates
        gv = g(v)
        M = mp.matrix([[v[0], p[0]], [v[1], p[1]]])
        mu, _c = mp.lu_solve(M, mp.matrix([gv[0], gv[1]]))
        resid = max(abs(gv[k] - mu * v[k] - _c * p[k]) for k in range(5))
        r = mu / lam
        rot[j] = r
        expect = zeta ** (-j)
        print(f"  p_{j}: on curve {on_curve}, g-rotation {mp.nstr(r, 12)}  vs ζ^(−j) {mp.nstr(expect, 12)}   resid {mp.nstr(resid, 3)}")
        check(f"bring_C5_rotation_at_p{j}_eq_zeta^(-{j})", on_curve and abs(r - expect) < TOL and resid < TOL,
              "Lean rotExp_eq_neg; tangent line = Jacobian kernel mod p")
    check("conjugate_fixed_points_carry_conjugate_rotations",
          all(abs(rot[j] - mp.conj(rot[5 - j])) < TOL for j in (1, 2)), "Lean rotExp_neg")
    check("no_C5_rotation_is_real_(chirality_never_neutral)", all(abs(mp.im(rot[j])) > mp.mpf("0.1") for j in rot),
          "Lean rotExp_ne_rotExp_neg")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("segment-window-bring-chirality", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0_anchor_reason": "q0 read from the committed y-lambda-at-q0 witness string; atom words validated against committed characters",
        "description": ("PROBE (bean qou-jfx8): (W) the k-segment collision window on the production T and 3He words — "
                        "k <= 3 cannot separate them, k = 4 (first window reaching the bond) does; (B) the C5 rotations at "
                        "the fixed points of a 5-cycle on Bring's curve are zeta^(-j), conjugate in conjugate pairs, never "
                        "real. Nothing fitted, selected or wired."),
        "weight_family": "markov_y_lambda_convention_D",
        "window": {str(k): {"worst_sep": mp.nstr(v[0], 20), "rows": v[1]} for k, v in window.items()},
        "bring_c5_rotations": {str(j): {"re": mp.nstr(mp.re(r), 30), "im": mp.nstr(mp.im(r), 30)} for j, r in rot.items()},
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
