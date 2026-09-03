#!/usr/bin/env python3
"""magnus_gauge_invariant_curvature_probe.py — the gauge-invariant q-curvature that fixes the
germ's free off-diagonal (qou-o6ov).

#6434 pinned the germ A_i = q·∂_qσ_i·σ_i⁻¹ as UNDERDETERMINED: the differentiated-Hecke relation
fixes its σ-eigenbasis DIAGONAL to ±1 but leaves the OFF-DIAGONAL free, so the germ is
representation-specific (seminormal vs R-matrix differ on genuine blocks — the 6.5% two-row miss
of #6432). The owner's open question: is there a gauge-invariant (q-curvature) formulation in
which the free off-diagonal is FIXED by a naturality condition?

YES — the canonical choice is the SPECTRAL PROJECTOR germ. Fix the free off-diagonal by demanding
the germ be a function of σ alone (the only natural, realization-independent choice):
    P_i = (σ_i + q⁻¹·I)/[2]_q     (projector onto σ_i's q-eigenspace, [2]_q = q + q⁻¹)
    A_i^P = 2P_i − I = (2σ_i − h)/[2]_q     (h = q − q⁻¹; the channel-sign operator: +1 on q, −1 on −q⁻¹)
    Ω₂^P = Σ_a [A_a^P, A_{a+1}^P] = (4/[2]_q²)·Σ_a [σ_a, σ_{a+1}].
This has the SAME constraint-fixed diagonal (±1) as the true germ but off-diagonal linear in σ.
Crucially Ω₂^P is a genuine ELEMENT OF THE HECKE ALGEBRA (a polynomial in the σ's), unlike the
germ (a log-derivative of the rep matrix). So its trace is a CHARACTER — realization-independent
by construction. That is exactly "gauge-invariant q-curvature".

THIS PROBE MEASURES three things at A=2 (n=6, exact mpf):
 (1) GAUGE-INVARIANCE: Σ_k (n-2k+1)·tr_(n-k,k)(ρ·Ω₂^P)  ==?==  tr_(ℂ²)^⊗n(ρ·Ω₂^P)  [expect MATCH
     to ~1e-140, vs the germ's 6.5% miss] — confirms Ω₂^P is a true algebra element / gauge-invariant.
 (2) DOES IT PRESERVE THE ARC'S ANSWER? per irrep, tr(ρ·Ω₂^P) vs the seminormal germ tr(ρ·Ω₂)
     [expect NO — a different, cleaner object; the projector naturality changes the decay object].
 (3) DOES IT STILL DECAY with b(λ)=n−λ_1? per irrep |tr(ρ·Ω₂^P)| vs dim and b(λ) — is the
     gauge-invariant curvature ALSO row-decaying (the property the arc needs)?

scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_extreme_rep_endpoint_probe import omega2_trace  # noqa: E402
from magnus_two_row_rmatrix_probe import r_matrix, embed  # noqa: E402

# Pin precision EXPLICITLY here (do not rely on the base module setting mp.mp.dps as an import
# side effect): the ~1e-140 gauge-invariance agreement below is a genuine dps-floor match, so the
# claim degrades silently to the 15-dps default if that side effect ever changes.
mp.mp.dps = 140


def sigma_dense_list(shape, q):
    """Dense seminormal σ_g matrices for every generator g, in irrep `shape`."""
    per_gen, dim = base.block_structure(shape)
    sig = base.sigma_csr(per_gen, dim, q)
    return [base._dense_from_csr(sig[g], dim) for g in range(len(sig))], dim


def projector_curvature_trace(shape, gens, q):
    """tr(ρ·Ω₂^P) in irrep `shape`, where Ω₂^P = (4/[2]²)Σ_a[σ_a,σ_{a+1}] (projector germ).
    Built directly from the σ-commutators — a genuine Hecke-algebra element."""
    sig, dim = sigma_dense_list(shape, q)
    ngen = len(sig)
    # word ρ = ∏ σ_gens
    rho = sig[gens[0]]
    for g in gens[1:]:
        rho = rho * sig[g]
    two_q = q + 1 / q
    coef = 4 / two_q ** 2
    O = mp.zeros(dim, dim)
    for a in range(ngen - 1):
        O = O + (sig[a] * sig[a + 1] - sig[a + 1] * sig[a])
    O = coef * O
    M = rho * O
    return sum(M[i, i] for i in range(dim)), dim


def projector_curvature_trace_rmatrix(A, q):
    """tr_(ℂ²)^⊗n(ρ·Ω₂^P) via the 2-dim R-matrix, Ω₂^P = (4/[2]²)Σ_a[Ř_a,Ř_{a+1}]."""
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    R4 = r_matrix(q)
    ngen = max(gens) + 1
    sig = [embed(R4, i, n) for i in range(ngen)]
    rho = sig[gens[0]]
    for g in gens[1:]:
        rho = rho * sig[g]
    D = 1 << n
    two_q = q + 1 / q
    coef = 4 / two_q ** 2
    O = mp.zeros(D, D)
    for a in range(ngen - 1):
        O = O + (sig[a] * sig[a + 1] - sig[a + 1] * sig[a])
    O = coef * O
    M = rho * O
    return sum(M[i, i] for i in range(D)), n


def b_of(shape):
    return sum(shape) - shape[0]


def main():
    A = 2
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    print(f"[gauge] projector germ A^P = (2σ−h)/[2]_q; Ω₂^P = (4/[2]²)Σ[σ_a,σ_{{a+1}}]  "
          f"(a genuine Hecke element)")
    print(f"[gauge] q₀={mp.nstr(q,8)}, A={A}, n={n}, |word|={len(gens)}\n")

    # ------- per-irrep: projector curvature vs seminormal germ; decay in b(λ) -------
    print("  λ           b   dim    tr(ρ·Ω₂^P) [gauge-inv]      tr(ρ·Ω₂) [seminormal germ]   equal?")
    parts = list(base.partitions(n))  # materialize — reused by tests (2)/(3)
    two_row_rows = []  # (k, lam, dim, mult, trP, trgerm)
    for lam in parts:
        _pg, dim = base.block_structure(lam)
        trP, _ = projector_curvature_trace(lam, gens, q)
        trg, _ = omega2_trace(lam, gens)
        b = b_of(lam)
        eq = abs(trP - trg) < mp.mpf(10) ** -30
        print(f"  {str(lam):<11} {b:>1}  {dim:>4}   {mp.nstr(mp.re(trP),12):>20}   "
              f"{mp.nstr(mp.re(trg),12):>20}   {'YES' if eq else 'no'}")
        # collect two-row shapes for the gauge-invariance sum
        if len(lam) <= 2:
            k = lam[1] if len(lam) == 2 else 0
            mult = n - 2 * k + 1
            two_row_rows.append((k, lam, dim, mult, trP, trg))

    # ------- (1) GAUGE-INVARIANCE via Schur–Weyl two-row sum -------
    lhsP = mp.mpf(0)
    for k, lam, dim, mult, trP, _trg in sorted(two_row_rows):
        lhsP += mult * mp.re(trP)
    rhsP, _ = projector_curvature_trace_rmatrix(A, q)
    relP = abs(lhsP - rhsP) / (abs(lhsP) + mp.mpf(10) ** -80)
    print(f"\n  (1) GAUGE-INVARIANCE  Σ_k (n-2k+1)·tr_(n-k,k)(ρΩ₂^P)  vs  tr_(ℂ²)^⊗n(ρΩ₂^P):")
    print(f"      seminormal weighted sum = {mp.nstr(lhsP,14)}")
    print(f"      R-matrix tensor trace   = {mp.nstr(mp.re(rhsP),14)}")
    # Ω₂^P is an EXACT algebra element (no finite difference anywhere), so the two-gauge agreement
    # is a genuine dps-floor match (~1e-140 at 140 dps). Gate at 1e-100 — far below the true match
    # yet far above the germ's 6.5% miss — so a real regression cannot slip through a lax 1e-20.
    GAUGE_TOL = mp.mpf(10) ** -100
    gauge_ok = relP < GAUGE_TOL
    print(f"      |Δ_rel| = {mp.nstr(relP,4)}   "
          f"{'✓ GAUGE-INVARIANT (< 1e-100; measured ~1e-140)' if gauge_ok else '✗ differs — NOT gauge-invariant'}")
    print(f"      [contrast: the germ Ω₂ misses this same test by 6.5% (#6432) — it is NOT an algebra element]")

    # ------- (2) does Ω₂^P equal the seminormal-germ decay object? -------
    all_equal = True
    for lam in parts:
        trP, _ = projector_curvature_trace(lam, gens, q)
        trg, _ = omega2_trace(lam, gens)
        if abs(trP - trg) > mp.mpf(10) ** -30:
            all_equal = False
            break
    print(f"\n  (2) Ω₂^P == seminormal germ Ω₂ per irrep?  {'YES' if all_equal else 'NO — a different, cleaner object'}")

    # ------- (3) does the gauge-invariant curvature ALSO decay with b(λ)? -------
    print(f"\n  (3) row-decay of the GAUGE-INVARIANT curvature |tr(ρΩ₂^P)| by b(λ):")
    by_b = {}
    for lam in parts:
        _pg, dim = base.block_structure(lam)
        trP, _ = projector_curvature_trace(lam, gens, q)
        by_b.setdefault(b_of(lam), []).append((lam, dim, abs(mp.re(trP))))
    for b in sorted(by_b):
        for lam, dim, mag in by_b[b]:
            print(f"      b={b}  {str(lam):<11} dim={dim:>4}  |tr(ρΩ₂^P)|={mp.nstr(mag,8):>14}  "
                  f"|tr|/dim={mp.nstr(mag/dim,6)}")


if __name__ == "__main__":
    main()
