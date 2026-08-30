#!/usr/bin/env python3
"""
lever1_saddle_action_jet_residue_probe.py — (A) per-pair saddle actions on the color cubic;
(B) the z=∞ jet-residue tower and the EXACTNESS (b)-exclusion of classical-jet periods.
(lever-1 / z2bn; owner-picked follow-ups to the Borel(1/2) datum of PR #3694.)

(A) Saddle actions. In exact-WKB the Borel-plane singularities of a period series sit at
SADDLE ACTIONS ω_ij = ∫_{z_i}^{z_j} (X_a − X_b) dz between branch points (the trajectory /
BPS dictionary) — NOT at the branch-point positions z_k themselves (a conflation in the
reviewed external dialog). The color cubic
    P = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)
is q-free, so its pair actions are pure numbers, comparable (report-only, numerology guard)
with the measured level-1/2 Borel datum ξ = 1/√2 of the q=1 binding period. This part
computes the three reciprocal-pair actions by continuity-tracked quadrature.

(B) Jet-residue tower at z=∞ + exactness. The corpus jet rule (sw_period_growth_probe.py)
is λ_SW^(n) = X^(n)(z)dz with X^(n) the n-th TOTAL z-derivative on the curve. But then
    λ_SW^(n) = d(X^(n−1))   for every n ≥ 1
is an EXACT meromorphic differential on Σ, so ALL its residues (at every point, including
the branch-point poles and z=∞) and ALL its closed-cycle periods vanish identically —
Stokes/exactness, a proved invariant. Hence the identification a_D^(n) = ∮λ_SW^(n) =
lw(n−1) ≠ 0 CANNOT hold with the classical d/dz jet rule on any closed cycle:
a scope-(b) exclusion of the classical-jet-period reading, INDEPENDENT of and consistent
with PR #2768's q-freeness (b)-exclusion. It does NOT touch the q-difference prolongation
(the live route) nor the algebraic residue-sum identity `prop:sw-period-residue-sum`
(dim_q weights). This part verifies the exactness statement exactly (sympy): sheet
expansions at ∞ (X ~ c·z, c ∈ {−1, ±i}), n=0 residues {0, ±5i/16} (reproducing the
Step-1 probe), and identically-zero 1/z-coefficients of X^(n) for n = 1…4 on every sheet.

Anti-fit: actions are geometry (no target matched); part-B is an exact structural check;
comparisons to 1/√2 are REPORTED, not asserted. No wiring. EXPLORATORY, scope-(a) for the
action values, scope-(b) (exactness invariant) for the jet-period exclusion.

Audit: docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md (addendum)
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Xs, zs = sp.symbols('X z')
PXZ = Xs ** 3 + (zs + 1) * Xs ** 2 + (zs ** 2 + zs + 1) * Xs + (zs ** 3 + zs ** 2 + zs + 1)


def cubic_roots(z):
    return mp.polyroots([1, z + 1, z ** 2 + z + 1, z ** 3 + z ** 2 + z + 1],
                        maxsteps=120, extraprec=60)


def branch_points():
    b = lambda z: z + 1
    c = lambda z: z ** 2 + z + 1
    d = lambda z: z ** 3 + z ** 2 + z + 1
    disc = lambda z: (18 * b(z) * c(z) * d(z) - 4 * b(z) ** 3 * d(z)
                      + b(z) ** 2 * c(z) ** 2 - 4 * c(z) ** 3 - 27 * d(z) ** 2)
    nodes = [mp.mpf(k) - 3 for k in range(7)]
    V = mp.matrix(7, 7)
    rhs = mp.matrix(7, 1)
    for i, zn in enumerate(nodes):
        for j in range(7):
            V[i, j] = zn ** j
        rhs[i, 0] = disc(zn)
    coef = mp.lu_solve(V, rhs)
    return mp.polyroots([coef[6 - k, 0] for k in range(7)], maxsteps=200, extraprec=80)


def track(za, zb, T):
    """Continuity-track the 3 sheets along the straight path za→zb (Chebyshev-clustered)."""
    pts, sheets = [], []
    prev = None
    for k in range(T + 1):
        s = mp.mpf(k) / T
        t = (1 - mp.cos(mp.pi * s)) / 2
        z = za + t * (zb - za)
        roots = list(cubic_roots(z))
        if prev is None:
            order = roots
        else:
            order = []
            pool = roots[:]
            for pr in prev:
                jbest = min(range(len(pool)), key=lambda j: abs(pool[j] - pr))
                order.append(pool.pop(jbest))
        pts.append(z)
        sheets.append(order)
        prev = order
    return pts, sheets


def colliding_pair(sheets, idx):
    tri = sheets[idx]
    pairs = [(0, 1), (0, 2), (1, 2)]
    return min(pairs, key=lambda ab: abs(tri[ab[0]] - tri[ab[1]]))


def pair_action(za, zb, T):
    pts, sheets = track(za, zb, T)
    pa = colliding_pair(sheets, 1)          # pair colliding near za
    pb = colliding_pair(sheets, len(sheets) - 2)  # pair colliding near zb
    # trapezoid in s of (X_a − X_b)·dz/ds  with z = za + t(s)(zb−za), dt/ds = (π/2)sin(πs)
    total = mp.mpc(0)
    Tn = len(pts) - 1
    vals = []
    for k in range(Tn + 1):
        s = mp.mpf(k) / Tn
        dz_ds = (zb - za) * (mp.pi / 2) * mp.sin(mp.pi * s)
        f = (sheets[k][pa[0]] - sheets[k][pa[1]]) * dz_ds
        vals.append(f)
    for k in range(Tn):
        total += (vals[k] + vals[k + 1]) / 2 / Tn
    return total, pa, pb


def main() -> int:
    print("=== lever-1: (A) per-pair saddle actions; (B) z=∞ jet residues + exactness ===\n")

    # ---------- (A) ----------
    bps = list(branch_points())
    used = [False] * 6
    pairs = []
    for i in range(6):
        if used[i]:
            continue
        j = min((j for j in range(6) if j != i and not used[j]),
                key=lambda j: abs(bps[i] * bps[j] - 1))
        used[i] = used[j] = True
        pairs.append((bps[i], bps[j]))
    recip_ok = all(abs(a * b - 1) < 1e-8 for a, b in pairs)
    print(f"branch points: 3 reciprocal pairs (z·z' = 1): {'PASS' if recip_ok else 'FAIL'}")

    actions = []
    conv_ok = True
    same_pair_ok = True
    for (za, zb) in pairs:
        A1, pa1, pb1 = pair_action(za, zb, 800)
        A2, pa2, pb2 = pair_action(za, zb, 1600)
        conv = abs(A1 - A2) / max(abs(A2), mp.mpf('1e-30'))
        conv_ok &= conv < 1e-3
        same_pair_ok &= (pa2 == pb2)
        actions.append(A2)
        print(f"  pair |z|={float(abs(za)):.4f}↔{float(abs(zb)):.4f}: "
              f"A = {mp.nstr(A2, 8):>24}  |A| = {float(abs(A2)):.6f}  "
              f"(conv {float(conv):.1e}; colliding sheets {pa2}"
              f"{' = both ends' if pa2 == pb2 else f' vs {pb2} — DIFFER'})")
    inv_sqrt2 = 1 / mp.sqrt(2)
    print(f"\n  report-only comparison (numerology guard — no identification asserted):")
    print(f"    measured Borel(1/2) datum ξ = 1/√2 ≈ {float(inv_sqrt2):.6f}; "
          f"|A| values: {[f'{float(abs(A)):.5f}' for A in actions]}")
    print(f"    |A|/(1/√2): {[f'{float(abs(A)/inv_sqrt2):.4f}' for A in actions]}")

    # ---------- (B) ----------
    print("\n(B) z=∞ sheet expansions, n=0 residues, and jet exactness (exact sympy):")
    w = sp.symbols('w')  # w = 1/z
    K = 8
    res0 = []
    jets_zero = True
    for cval in (sp.Integer(-1), sp.I, -sp.I):
        # X = c/w + Σ_{k≥0} a_k w^k ; solve P=0 order by order in w
        aks = []
        Xser = cval / w
        for k in range(0, K + 1):
            ak = sp.symbols(f'a{k}')
            trial = Xser + ak * w ** k
            expr = sp.expand(PXZ.subs({Xs: trial, zs: 1 / w}) * w ** 3)
            # δ(P·w³) from a_k enters at order w^{k+1} (P_X ~ z²); lower orders already vanish
            ser = sp.expand(sp.series(expr, w, 0, k + 2).removeO())
            lead = ser.coeff(w, k + 1)
            sol = sp.solve(sp.Eq(lead, 0), ak)
            assert sol, f"no solution at sheet {cval}, order {k}"
            aval = sol[0]
            aks.append(aval)
            Xser = Xser + aval * w ** k
        # n=0: Res_∞(X dz) = −a_1  (dz = −dw/w²; standard: Res_∞ = −coeff of 1/z)
        res0.append(sp.simplify(-aks[1]))
        # jets n=1..4: X^(n) = d^n X/dz^n; the 1/z coefficient must vanish identically.
        Xz = Xser.subs(w, 1 / zs)
        for n in range(1, 5):
            Xz = sp.diff(Xz, zs)
            c_m1 = sp.simplify(sp.expand(Xz).coeff(zs, -1))
            jets_zero &= (c_m1 == 0)
    res_set = sorted([str(r) for r in res0])
    step1_match = sorted(['0', '-5*I/16', '5*I/16']) == res_set or \
        sorted(['0', '5*I/16', '-5*I/16']) == res_set
    sheet_sum_zero = sp.simplify(sum(res0)) == 0
    print(f"  n=0 residues at ∞ per sheet: {res_set} (sheet-sum 0: "
          f"{'PASS' if sheet_sum_zero else 'FAIL'}; matches Step-1 {{0, ±5i/16}}: "
          f"{'PASS' if step1_match else 'FAIL'})")
    print(f"  jets n=1..4: 1/z-coefficient of X^(n) ≡ 0 on every sheet: "
          f"{'PASS' if jets_zero else 'FAIL'}")
    print("  structural reason (the (b)-invariant): λ_SW^(n) = X^(n)dz = d(X^(n−1)) is an")
    print("  EXACT differential for n ≥ 1 ⇒ all residues and all closed-cycle periods vanish")
    print("  identically ⇒ the classical-jet rule cannot carry a_D^(n) = lw(n−1) ≠ 0 on any")
    print("  cycle. Independent of, and consistent with, PR #2768's q-freeness (b)-exclusion.")
    print("  The q-difference prolongation and prop:sw-period-residue-sum are untouched.")

    ok = recip_ok and conv_ok and sheet_sum_zero and step1_match and jets_zero
    print(f"\n### Verdict: {'ALL CHECKS PASS' if ok else 'CHECK FAILED'}")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-saddle-action-jet-residue", engine="mpmath+sympy")
        wb.set_description(
            "Lever-1 (z2bn): (A) the three reciprocal-pair saddle actions of the q-free color "
            "cubic, continuity-tracked quadrature (conv <1e-3): the exact-WKB dictionary puts "
            "Borel singularities at ACTIONS between branch points, not at branch positions "
            "(corrects the external dialog's conflation); values reported against the measured "
            "level-1/2 datum 1/sqrt2 with NO identification asserted (numerology guard). "
            "(B) exact sympy: sheet expansions at infinity reproduce the Step-1 n=0 residues "
            "{0, +-5i/16} (sheet-sum 0), and the 1/z coefficient of X^(n) vanishes identically "
            "for n=1..4 on every sheet — the finite face of the EXACTNESS (b)-exclusion: "
            "lambda_SW^(n)=X^(n)dz=d(X^(n-1)) is exact for n>=1, so all residues and all "
            "closed-cycle periods vanish; the classical-jet rule cannot carry "
            "a_D^(n)=lw(n-1)!=0 (invariant: Stokes/exactness; independent of #2768's "
            "q-freeness exclusion; q-difference route and prop:sw-period-residue-sum "
            "untouched). No fit; no wiring.")
        wb.add_data("branch_pairs", [[str(a), str(b)] for a, b in pairs])
        wb.add_data("pair_actions", [str(A) for A in actions])
        wb.add_data("pair_action_abs", [float(abs(A)) for A in actions])
        wb.add_data("abs_over_inv_sqrt2", [float(abs(A) / inv_sqrt2) for A in actions])
        wb.add_data("colliding_pair_same_both_ends", bool(same_pair_ok))
        wb.add_data("res_infinity_n0", res_set)
        wb.add_data("jet_residues_n1_4_zero", bool(jets_zero))
        wb.add_assertion(
            name="saddle_actions_computed_and_jet_exactness_exclusion",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("3 reciprocal pairs; quadrature converged; n=0 residues reproduce Step-1 "
                    "{0, ±5i/16}; jets n=1..4 have identically zero residues on every sheet — "
                    "the exactness (b)-invariant: d(X^(n−1)) has no periods/residues, so the "
                    "classical-jet rule cannot yield the nonzero lw tower."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
