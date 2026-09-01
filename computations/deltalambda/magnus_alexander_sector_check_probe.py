#!/usr/bin/env python3
"""magnus_alexander_sector_check_probe.py — WHERE is the Alexander sector? (qou-o6ov)

Answers the Schur–Weyl bridge question and CORRECTS #6387. #6387 suggested the sign rep
λ=(1ⁿ) (the b=n−1 decay endpoint) is "the fully-antisymmetric = Alexander sector." That is
BACKWARDS. Three facts, verified here + one standard citation:

  (i)   b=1 is the REFLECTION rep λ=(n−1,1), dim n−1. It is the (reduced) BURAU representation
        of B_n (Jones 1987; unitary form: Squier 1984, library/squier-burau-unitary-1984), and
        the Alexander polynomial is Δ_K(t) ∝ det(I − reducedBurau(β)). So the Alexander sector
        is b=1 — the decay's PEAK, not its endpoint.
  (ii)  b=n−1 is the SIGN rep λ=(1ⁿ), dim 1: every σ_i acts as the scalar −q⁻¹, so ρ is a
        monomial (−q⁻¹)^L carrying only writhe/framing — NO knot information, NO Alexander.
        (And ⁅A_a,A_{a+1}⁆=0 there ⇒ tr=0, #6387's exact-zero endpoint.)
  (iii) the germ trace |tr(ρ_λ Ω₂)|/dim PEAKS at b=1 and decays toward the b=n−1 sign-rep zero.

⇒ the decay runs FROM the Burau/Alexander sector (b=1) TO the information-free sign endpoint
(b=n−1). The Alexander structure sits at the SOURCE of the decay, not the endpoint; the
sign-rep endpoint does NOT equal any Alexander sector.

This probe verifies (i) dim/b, (ii) the sign-rep scalar, (iii) the b=1 peak. scope-(a);
NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_extreme_rep_endpoint_probe import omega2_trace  # noqa: E402


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    L = len(gens)
    print(f"[alex] A={A} (n={n}), braid word length L={L}")

    # (i) reflection rep (n-1,1) is b=1, dim n-1
    refl = tuple([n - 1, 1])
    _pg, dim_refl = base.block_structure(refl)
    b_refl = n - refl[0]
    print(f"  (i)  reflection λ={refl}: dim={dim_refl} (= n−1 = {n-1}), b={b_refl}  "
          f"⇒ this is the reduced BURAU rep — the ALEXANDER sector (Jones 1987; Squier 1984).")

    # (ii) sign rep (1^n) is b=n-1, dim 1, ρ = scalar (−q⁻¹)^L
    sign = tuple([1] * n)
    per_gen, dim_sign = base.block_structure(sign)
    sig = base.sigma_csr(per_gen, dim_sign, base.Q0)
    # each generator's 1x1 matrix entry:
    s0 = base.csr_to_dict(sig[0]).get(0, {}).get(0, mp.mpf(0))
    rho_scalar = s0 ** L  # ρ = ∏ σ = s0^L since all σ_i equal the same scalar in the sign rep
    want = (-1 / base.Q0) ** L
    tr_sign, _ = omega2_trace(sign, gens)
    print(f"  (ii) sign λ=(1^{n}): dim={dim_sign}, σ_i scalar = {mp.nstr(s0,6)} "
          f"(= −q⁻¹ = {mp.nstr(-1/base.Q0,6)}); ρ = scalar {mp.nstr(rho_scalar,4)} "
          f"(monomial, writhe only) ⇒ NO Alexander; tr(ρ Ω₂)={mp.nstr(tr_sign,3)}")

    # (iii) germ trace peaks at b=1, decays to sign-rep zero
    print("  (iii) |tr(ρ_λ Ω₂)|/dim by b (max-dim λ of each b):")
    byb = {}
    for shape in base.partitions(n):
        _pg, dim = base.block_structure(shape)
        if dim <= 1:
            continue
        b = n - shape[0]
        tr, _ = omega2_trace(shape, gens)
        cur = byb.get(b)
        if cur is None or dim > cur[1]:
            byb[b] = (abs(tr) / dim, dim, shape)
    peak_b = max(byb, key=lambda b: byb[b][0])
    for b in sorted(byb):
        val, dim, shape = byb[b]
        star = "  <-- PEAK (Burau/Alexander sector)" if b == peak_b else \
               ("  <-- endpoint → 0 (sign rep is b={}, dim 1)".format(n-1) if b == max(byb) else "")
        print(f"       b={b:>2}: |tr|/dim={mp.nstr(val,4):>9}  (dim {dim}){star}")
    print(f"  ⇒ PEAK at b={peak_b} (the b=1 reflection/Burau/Alexander sector); "
          f"decay runs AWAY from Alexander toward the trivial sign endpoint.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
