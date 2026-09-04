#!/usr/bin/env python3
"""magnus_hook_majorant_monotone_probe.py — is the hook-column bound DERIVED-decaying, closing the
chain from Σ|eig(M_λ)| to a monotone function of b? (qou-o6ov)

THE LAST GAP. The chain is now:
    Σ_i|eig_i(M_λ)|  ≤  √(dim_λ · tr_λ(X*X))                                  (B, #6573)
    tr_hook(X*X)      =  -c²·q^{T(1-j)}·Σ_{a,b}Σ_± ± e_j(μ(word)),  T = 2L+4   (#6556, derived)
Both are derived. What is still only MEASURED is that the right-hand side falls with b. This probe
closes that by applying the SAME sharp triangle inequality the hook bound #6520 used — and which is
already Lean-proved in MagnusHookDecayBound (`abs_esymm_le_esymm_abs`, `abs_sum_esymm_sub_le`):

    |tr_hook(X*X)|  ≤  c²·q^{T(1-j)}·Σ_{a,b} Σ_± e_j(|μ(word)|)  =:  B''_j          (SHARP)

(all signs +, eigenvalue MODULI), and then, via (B),

    Σ|eig(M_hook)| / dim  ≤  √( B''_j / dim ),   dim = C(n-1,j).                     (FINAL)

If B''_j / C(n-1,j) is monotone decreasing in j, then so is its square root, and the hook-column
decay becomes a DERIVED statement about the Burau moduli rather than a measurement of the trace.

CRUDE vs SHARP — and a prediction of mine that the probe REFUTED. The spectral radius of a
length-T word is ≈ q^T (measured: r/q^T = 0.80 at A=2), so the twist q^{T(1-j)} nearly cancels the
dominant eigenvalue and a crude |e_j| ≤ C(n-1,j)·r^j leaves ≈ q^T·C(n-1,j) — a growing binomial.
I therefore asserted here that the crude bound "will not do it" and that only the sharp form could
decay. **That was wrong, and reporting both is what caught it.** PER DIMENSION the binomial is
divided back out (dim = C(n-1,j) for a hook), so the crude bound IS monotone decreasing too, at
both A=2 and A=3. What separates them is tightness, not monotonicity: crude/dim exceeds sharp/dim
by 3x (j=1) to ~2000x (j=8). The #6520 precedent is about RAW monotonicity, a different quantity —
do not carry its conclusion across to the per-dim form.

CHECKS (A=2,3; exact mpf, dps 140):
  (1) B''_j really bounds |tr_hook(X*X)| (it must — triangle inequality);
  (2) is B''_j / C(n-1,j) monotone decreasing in j?  ← the deciding column
  (3) crude vs sharp, to show the crude one fails;
  (4) the composed FINAL per-dim bound vs the actual Σ|eig|/dim, with tightness.
scope-(a); NO-FLOAT64. No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_hook_exterior_power_probe import elem_sym_from_eigs  # noqa: E402
from magnus_gauge_hook_closed_form_probe import reflection_generators  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402


def word_moduli(gens, q, ngen, sV):
    """For every expanded word of X*X, its Burau eigenvalue MODULI. All words have length 2L+4."""
    rho = sV[gens[0]]
    for g in gens[1:]:
        rho = rho * sV[g]
    rho_star = sV[gens[-1]]
    for g in reversed(gens[:-1]):
        rho_star = rho_star * sV[g]
    Y = rho_star * rho
    out = []
    for a in range(ngen - 1):
        for Amat in (sV[a] * sV[a + 1], sV[a + 1] * sV[a]):
            for b in range(ngen - 1):
                for Bmat in (sV[b] * sV[b + 1], sV[b + 1] * sV[b]):
                    E, _ = mp.eig(Amat * Y * Bmat)
                    out.append(sorted((abs(e) for e in E), reverse=True))
    return out


def analyze(A):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    L = len(gens)
    T = 2 * L + 4
    c = 4 / (q + 1 / q) ** 2
    sV, dimV = reflection_generators(n, ngen, q)
    mods = word_moduli(gens, q, ngen, sV)
    r = max(m[0] for m in mods)

    print(f"[mono] A={A} (n={n}); T=2L+4={T}, {len(mods)} words, Burau dim {dimV}")
    print(f"[mono] r = max spectral radius = {mp.nstr(r,8)};  q^T = {mp.nstr(q**T,8)};  "
          f"r/q^T = {mp.nstr(r/q**T,6)}  (≈1 ⇒ twist cancels the dominant eigenvalue)\n")
    print("   j   hook             dim    |tr(X*X)|        B''_j (sharp)   B_j (crude)    "
          "B''/dim      FINAL/dim    actual Σ|eig|/dim")
    rows = []
    for j in range(0, n):
        k = n - j
        hook = tuple([k] + [1] * (n - k))
        X, Xstar, dim, _ = build(hook, gens, q, ngen)
        P = Xstar * X
        trXX = abs(mp.re(sum(P[i, i] for i in range(dim))))
        E, _ = mp.eig(X)
        s_abs = sum(abs(e) for e in E)
        twist = q ** (T * (1 - j))
        sharp = c ** 2 * twist * sum(elem_sym_from_eigs(m)[j] for m in mods)
        crude = c ** 2 * twist * len(mods) * mp.mpf(math.comb(dimV, j)) * r ** j
        final = mp.sqrt(sharp / dim) if sharp > 0 else mp.mpf(0)   # √(dim·sharp)/dim
        rows.append((j, dim, trXX, sharp, crude, s_abs))
        print(f"  {j:>2}   {str(hook):<15} {dim:>4}  {mp.nstr(trXX,8):>13}  {mp.nstr(sharp,8):>13}  "
              f"{mp.nstr(crude,7):>12}  {mp.nstr(sharp/dim,7):>11}  {mp.nstr(final,7):>11}  "
              f"{mp.nstr(s_abs/dim,7):>13}")

    print()
    holds = all(t <= s * (1 + mp.mpf(10) ** -60) for _, _, t, s, _, _ in rows)
    print(f"  (1) B''_j bounds |tr(X*X)| for every j?   {'YES ✓' if holds else 'NO ✗'}")
    inner = [(j, d, s) for j, d, _t, s, _c, _a in rows if s > 0]
    mono_sharp = all(inner[i + 1][2] / inner[i + 1][1] < inner[i][2] / inner[i][1]
                     for i in range(len(inner) - 1))
    crude_inner = [(j, d, cc) for j, d, _t, _s, cc, _a in rows if cc > 0]
    mono_crude = all(crude_inner[i + 1][2] / crude_inner[i + 1][1] < crude_inner[i][2] / crude_inner[i][1]
                     for i in range(len(crude_inner) - 1))
    print(f"  (2) SHARP B''_j/dim strictly decreasing in j?  {'YES ✓' if mono_sharp else 'NO'}")
    print(f"  (3) CRUDE B_j/dim strictly decreasing in j?    {'YES' if mono_crude else 'NO (as expected)'}")
    # tightness = (actual per dim) / (bound per dim) = (a/d) / √(s/d) = a/√(d·s).
    # Both sides MUST be per-dim; comparing the total a against the per-dim bound is a units
    # error that can print a ratio > 1 and read as a bound violation where there is none.
    tight = [(a / d) / mp.sqrt(s / d) for _j, d, _t, s, _c, a in rows if s > 0 and a > 0]
    if tight:
        print(f"  (4) FINAL per-dim bound tightness (actual/dim ÷ bound/dim): "
              f"{mp.nstr(min(tight),3)} … {mp.nstr(max(tight),3)}  "
              f"{'(all ≤ 1 ✓)' if max(tight) <= 1 else '(SOME > 1 — bound violated, investigate)'}")
    if holds and mono_sharp:
        print("\n  ⇒ CHAIN CLOSED ON THE HOOK COLUMN. Σ|eig(M_hook)|/dim ≤ √(B''_j/dim) with")
        print("    B''_j/dim strictly decreasing in j = b(λ) — every step derived: (B) by")
        print("    Cauchy–Schwarz+Schur (#6573), the closed form by the common twist (#6556), and")
        print("    B''_j by |e_j(μ)| ≤ e_j(|μ|), already Lean-proved in MagnusHookDecayBound.")
        print("    What remains INPUT, not theorem: the Burau moduli themselves (measured).")
    elif holds:
        print("\n  ⇒ B''_j holds but its per-dim form is NOT monotone — the sharp triangle bound is")
        print("    not enough to derive the decay here. Report that; do not present a non-monotone")
        print("    bound as closing the chain.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    args = ap.parse_args()
    for A in args.A:
        analyze(A)
        print()


if __name__ == "__main__":
    main()
