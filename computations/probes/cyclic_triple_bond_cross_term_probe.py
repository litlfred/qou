#!/usr/bin/env python3
"""
Probe — the non-monotone word class, measured on the production atom words.

FORMALIZE-FIRST CONTEXT (read the Lean before the numbers):

  QOU/MathlibExt/MonotoneWordTraceFactorizes.lean  — a monotone (ascending, one
      run per generator) word has Markov trace = product of its run traces.
  QOU/MathlibExt/RevisitClassCrossTerm.lean        — which departures from
      monotonicity carry a cross term:
        one-step revisit  x g_m g_{m+1} g_m          : NONE (cyclicity alone)
        skip revisit      x g_m g_{m+2} g_m          : NONE (far commutation)
        climb-2-and-back  x g_m g_{m+1} g_{m+2} g_m  : NONE
        cyclic square     x g_m g_{m+1} g_m g_{m+1}  : z^2 - h z - 1   (per tr x)
      So a bond re-crossing after its neighbour changes nothing; the ONLY source
      of a cross term is the cyclic square (g_m g_{m+1})^2 — three adjacent
      strands braided cyclically, closure T(3,2) instead of the Hopf chain.

This probe therefore measures exactly one class, with NO free count: at each
inter-nucleon bond (the single letter B at generator 3k+2) the bond is made a
CYCLIC TRIPLE — its two crossings alternate with the last two crossings of
nucleon k's adjacent intra run at 3k+1:

    production   ...  L1 L2 L3 L4 · B      · suffix        (monotone)
    hopf-clasp   ...  L1 L2 L3 L4 · B B    · suffix        (monotone, bond doubled)
    cyclic       ...  L1 L2 L3 · B · L4 · B · suffix       ((g_{3k+1} g_{3k+2})^2)

Predicted by the Lean + multilinearity in the affine letters (a·1 + b·g):

    tr(cyclic) - tr(hopf-clasp) = b(L1 L2 L3) · (z^2 - h z - 1) · tr(prefix) · Π tr(suffix runs)

where b(L1 L2 L3) is the g-coefficient of the collapsed run product and every
production letter has b = 1. The probe checks this closed form against the
Rust mpfr kernel (`pyhecke_native.chi_lambda_all_partitions_mpfr`, the general-
word kernel; the production transfer kernel REFUSES non-monotone words) on the
explicit modified words, then converts to MeV with the production binding law
`B = Q_beta(n) · (tr_M(free) - tr_M(atom))` (binding_canonical) and sets the
shift beside the production residual against AME 2020.

A second variant — the bond alternating with nucleon (k+1)'s FIRST two intra
crossings at 3k+3 — is measured numerically only (the trailing letters at
3k+3 put it outside the Lean statement); it is reported, not derived.

LAW SUPERSEDED THE SAME DAY (2026-09-04, qou-rp9i): the MeV conversion below
uses `B = Q_beta·(tr_free − tr_atom)`, which #6611 refutes at every scale; the
surviving law is `B = E_0·ln(tr_free/tr_atom)`. The trace-level checks here are
law-independent; the MeV column is superseded by
`cyclic_triple_under_log_law_probe.py` (same closed forms, log law, 20/20).

Nothing here is wired or fitted. One cyclic triple per bond is the minimal
member of the class; making every bond cyclic is reported as a total, not as
a model. Arithmetic: mpmath 50 dps throughout; kernel results are decimal
strings loaded into mpf; no float64 anywhere. ⁴He kernel checks cost ~8 min
per word and are behind `--full`; its closed forms are always printed.
"""
from __future__ import annotations

import argparse
import os
import sys
import time

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402

mp.mp.dps = 50
Q = Q_MP
H = Q - 1 / Q
Z_D = Q ** 3 / (Q ** 2 + 1)
DEFECT = Z_D ** 2 - H * Z_D - 1          # the convention-D Markov defect
Q_BETA = mp.mpf(str(Q_NEUTRON_MEV))
TOL = mp.mpf("1e-40")

NUCLEI = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]


# ── affine-letter algebra (a·1 + b·g at one generator) ─────────────────────
def letter(c, d):
    """(a, b) with the production triple (c, d, g) meaning c·σ_g + d·1."""
    return (mp.mpf(str(d)) if not isinstance(d, mp.mpf) else d,
            mp.mpf(str(c)) if not isinstance(c, mp.mpf) else c)


def aff_mul(x, y):
    """(a+bg)(a'+b'g) = (aa'+bb') + (ab'+a'b+h bb') g   under g² = h g + 1."""
    a, b = x
    a2, b2 = y
    return (a * a2 + b * b2, a * b2 + a2 * b + H * b * b2)


def aff_prod(letters):
    out = (mp.mpf(1), mp.mpf(0))
    for L in letters:
        out = aff_mul(out, L)
    return out


def aff_tr(x):
    return x[0] + x[1] * Z_D


def runs_of(word):
    """[(gen, [letters])] in order; asserts the word is monotone."""
    runs, last = [], -1
    for c, d, g in word:
        if g < last:
            raise ValueError(f"non-monotone production word: gen {g} after {last}")
        if g != last:
            runs.append((g, []))
            last = g
        runs[-1][1].append(letter(c, d))
    return runs


def tr_monotone_closed(word):
    """Π over runs of tr(run product) — MonotoneWordTraceFactorizes.tr_affineWord."""
    out = mp.mpf(1)
    for _g, Ls in runs_of(word):
        out *= aff_tr(aff_prod(Ls))
    return out


# ── the general-word kernel ────────────────────────────────────────────────
def encode(word):
    """(c,d,g) triples → the kernel's (sign, g+1) with per-position avg_shifts.
    Validated: reproduces tr_m_atom_zn byte-for-byte on 2H/3H/3He/4He."""
    signed, shifts = [], []
    for c, d, g in word:
        cm = mp.mpf(str(c)) if not isinstance(c, mp.mpf) else c
        assert abs(cm - 1) < TOL, f"c={c} != 1 unsupported by the sign encoding"
        dm = mp.mpf(str(d)) if not isinstance(d, mp.mpf) else d
        g1 = int(g) + 1
        if abs(dm) < mp.mpf("1e-30"):
            signed.append((1, g1)); shifts.append("")
        elif abs(dm + H) < mp.mpf("1e-30"):
            signed.append((-1, g1)); shifts.append("")
        elif abs(dm + H / 2) < mp.mpf("1e-30"):
            signed.append((0, g1)); shifts.append("")
        else:                                   # colour-weighted p–n letter
            signed.append((0, g1)); shifts.append(mp.nstr(-dm, 60))
    return signed, shifts


_Y = {}


def tr_kernel(word, n):
    import pyhecke_native as pn
    if n not in _Y:
        _Y[n] = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q).items()}
    signed, shifts = encode(word)
    out = pn.chi_lambda_all_partitions_mpfr(n, signed, Q_50_DIGIT_STR, 50, shifts)
    return sum(_Y[n][tuple(lam)] * mp.mpf(s) for lam, s in out)


# ── the modified words ─────────────────────────────────────────────────────
def bond_positions(word, A):
    """index of the single bond letter at generator 3k+2, k = 0..A-2."""
    pos = {}
    for i, (_c, _d, g) in enumerate(word):
        if g % 3 == 2:
            assert g not in pos, "production bond is a single letter"
            pos[g] = i
    return [pos[3 * k + 2] for k in range(A - 1)]


def words_left(word, i):
    """cyclic triple with nucleon k's last two intra crossings (Lean-covered)."""
    B = word[i]
    assert word[i - 1][2] == word[i][2] - 1
    hopf = word[:i] + [B, B] + word[i + 1:]
    cyc = word[:i - 1] + [B, word[i - 1], B] + word[i + 1:]
    return hopf, cyc


def words_right(word, i):
    """cyclic triple with nucleon (k+1)'s first two intra crossings (numeric only)."""
    B = word[i]
    assert word[i + 1][2] == word[i][2] + 1
    hopf = word[:i] + [B, B] + word[i + 1:]
    cyc = word[:i] + [B, word[i + 1], B] + word[i + 2:]
    return hopf, cyc


def cross_left_closed(word, i):
    """b(L1 L2 L3) · defect · tr(prefix) · Π tr(suffix runs)."""
    runs = runs_of(word)
    g_run = word[i - 1][2]
    prefix = mp.mpf(1)
    for g, Ls in runs:
        if g < g_run:
            prefix *= aff_tr(aff_prod(Ls))
    Ls_run = [L for g, Ls in runs if g == g_run for L in Ls]
    b_collapsed = aff_prod(Ls_run[:-1])[1]
    suffix = mp.mpf(1)
    for g, Ls in runs:
        if g > g_run + 1:
            suffix *= aff_tr(aff_prod(Ls))
    return b_collapsed * DEFECT * prefix * suffix


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="also run the ~8-min ⁴He kernel checks")
    args = ap.parse_args()
    checks: list[tuple[str, bool]] = []
    print(f"  q0 (proton pin) = {mp.nstr(Q, 20)}   z_D = {mp.nstr(Z_D, 15)}   "
          f"h = {mp.nstr(H, 15)}   z²−hz−1 = {mp.nstr(DEFECT, 15)}")
    print(f"  Q_beta(n) = {mp.nstr(Q_BETA, 12)} MeV   binding law: B = Q_beta·(tr_free − tr_atom)\n")

    for name, Z, N in NUCLEI:
        A, n = Z + N, 3 * (Z + N)
        kernel_ok = (A <= 3) or args.full
        W = atom_braid_word_3A(Z, N)
        W_free = atom_braid_word_3A(Z, N, include_inter=False)
        tr_prod_closed = tr_monotone_closed(W)
        tr_free_closed = tr_monotone_closed(W_free)
        ta, tf, _, _ = tr_m_atom_zn(Z, N)
        checks.append((f"{name}: closed-form product of run traces = production tr_M(atom)",
                       abs(tr_prod_closed - ta) < TOL))
        checks.append((f"{name}: closed-form product of run traces = production tr_M(free)",
                       abs(tr_free_closed - tf) < TOL))
        B_prod = Q_BETA * (tf - ta)
        B_ame = ame_binding_mev(Z, A)
        resid = B_ame - B_prod
        print(f"  ── {name}  (n = {n}, |W| = {len(W)})")
        print(f"     tr_M(atom) = {mp.nstr(ta, 18)}   tr_M(free) = {mp.nstr(tf, 18)}")
        print(f"     B_prod = {mp.nstr(B_prod, 10)} MeV   B_AME = {mp.nstr(B_ame, 10)} MeV   "
              f"residual (AME − prod) = {mp.nstr(resid, 10)} MeV")
        total_left = mp.mpf(0)
        for k, i in enumerate(bond_positions(W, A)):
            hopf, cyc = words_left(W, i)
            tr_hopf_closed = tr_monotone_closed(hopf)
            cross_closed = cross_left_closed(W, i)
            tr_cyc_closed = tr_hopf_closed + cross_closed
            if kernel_ok:
                t0 = time.time()
                tr_hopf_k, tr_cyc_k = tr_kernel(hopf, n), tr_kernel(cyc, n)
                wall = time.time() - t0
                checks.append((f"{name} bond {k}: kernel tr(hopf-clasp word) = closed form",
                               abs(tr_hopf_k - tr_hopf_closed) < TOL))
                checks.append((f"{name} bond {k}: kernel tr(cyclic) − tr(hopf) = b·(z²−hz−1)·tr(prefix)·Πsuffix",
                               abs((tr_cyc_k - tr_hopf_k) - cross_closed) < TOL))
                checks.append((f"{name} bond {k}: cyclic trace < hopf-clasp trace (extra binding)",
                               tr_cyc_k < tr_hopf_k))
                kern = f"kernel {wall:.1f}s"
            else:
                kern = "kernel skipped (--full)"
            dB_hopf = Q_BETA * (ta - tr_hopf_closed)        # doubling the bond alone
            dB_cross = -Q_BETA * cross_closed               # the pure interleaving effect
            total_left += dB_cross
            print(f"     bond {k} (gen {3*k+2}) [{kern}]")
            print(f"        tr(hopf-clasp) = {mp.nstr(tr_hopf_closed, 15)}   "
                  f"tr(cyclic) = {mp.nstr(tr_cyc_closed, 15)}   cross = {mp.nstr(cross_closed, 15)}")
            print(f"        ΔB(double the bond)   = {mp.nstr(dB_hopf, 10)} MeV")
            print(f"        ΔB(interleave, pure)  = {mp.nstr(dB_cross, 10)} MeV   "
                  f"= {mp.nstr(dB_cross / resid * 100, 6)} % of the residual")
            if kernel_ok:
                hopf_r, cyc_r = words_right(W, i)
                tr_hopf_r, tr_cyc_r = tr_kernel(hopf_r, n), tr_kernel(cyc_r, n)
                cross_r = tr_cyc_r - tr_hopf_r
                checks.append((f"{name} bond {k}: right-variant hopf word = closed form (monotone)",
                               abs(tr_hopf_r - tr_monotone_closed(hopf_r)) < TOL))
                print(f"        right variant (numeric): cross = {mp.nstr(cross_r, 15)}   "
                      f"ΔB(interleave) = {mp.nstr(-Q_BETA * cross_r, 10)} MeV   "
                      f"ratio to left = {mp.nstr(cross_r / cross_closed, 12)}")
        print(f"     all {A-1} bonds cyclic (left variant): ΣΔB(interleave) = {mp.nstr(total_left, 10)} MeV"
              f"   vs residual {mp.nstr(resid, 10)} MeV   ({mp.nstr(total_left / resid * 100, 6)} %)\n")

    # ── the n = 3 minimal instance, kernel vs Lean closed form ───────────────
    import pyhecke_native as pn
    y3 = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(3, Q).items()}

    def tr3(w):
        return sum(y3[tuple(l)] * mp.mpf(s) for l, s in pn.chi_lambda_all_partitions_mpfr(3, w, Q_50_DIGIT_STR, 50))
    cyc3 = tr3([(1, 1), (1, 2), (1, 1), (1, 2)])
    hopf3 = tr3([(1, 1), (1, 1), (1, 2), (1, 2)])
    checks.append(("n=3: tr((g0 g1)²) − tr(g0² g1²) = z²−hz−1 exactly (RevisitClass.cyclicSquare_cross_term)",
                   abs((cyc3 - hopf3) - DEFECT) < TOL))
    checks.append(("n=3: one-step revisit tr(g0 g1 g0) = tr(g0² g1) (RevisitClass.oneStepRevisit_eq_monotone)",
                   abs(tr3([(1, 1), (1, 2), (1, 1)]) - tr3([(1, 1), (1, 1), (1, 2)])) < TOL))
    y4 = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(4, Q).items()}

    def tr4(w):
        return sum(y4[tuple(l)] * mp.mpf(s) for l, s in pn.chi_lambda_all_partitions_mpfr(4, w, Q_50_DIGIT_STR, 50))
    checks.append(("n=4: climb-2-and-back tr(g0 g1 g2 g0) = tr(g0² g1 g2) (RevisitClass.twoStepClimbRevisit_eq_monotone)",
                   abs(tr4([(1, 1), (1, 2), (1, 3), (1, 1)]) - tr4([(1, 1), (1, 1), (1, 2), (1, 3)])) < TOL))
    checks.append(("n=4: interleaved word = z · cyclic square (RevisitClass.interleaved_eq_stab_cyclicSquare)",
                   abs(tr4([(1, 1), (1, 2), (1, 1), (1, 3), (1, 2)]) - Z_D * cyc3) < TOL))

    ok = 0
    print()
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
