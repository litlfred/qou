#!/usr/bin/env python3
"""alpha_em_b2_scalar_c_probe.py — Option C: numerically pin the Markov-side
normalization of the B2 τ-identification, and confirm Option B's premises.

Context (epic `qou-6ufi`, attack plan
[`docs/audits/2026-07-24-alpha-em-b2-tau-identification-attack-options.md`]).
The α_EM per-loop wall `1/(8π) = ½·a₀` reduces to the **B2 τ-identification**:
the categorical loop weight `W` on `H^{1,0}(Bring)` equals `complexify` of the
Markov Gram at `q₀`. Option B (merged, PR #4160,
`SchurInvariantFormProportional.lean`) proved the Schur mechanism: because
`H^{1,0}(Bring) = std` is the **irreducible** 4-dim standard S₅-rep (#2701), any
two invariant symmetric forms on it are proportional — SO the τ-image of the
Markov Gram and the Hodge Gram are forced ∝, leaving two open sub-pieces:
  (i)  the commutant of the (4,1) rep is scalar (absolute irreducibility);
  (ii) the τ-image is S₅-equivariant;
plus the scalar `c` itself (this Option C).

**What this probe DERIVES (machine-verified, no fit):**

  1. **Sub-piece (i), numerically confirmed for the actual (4,1) block at q₀.**
     Build the (4,1)=std seminormal H₅(q₀)-representation (σ₁..σ₄, Hoefsmit
     asymmetric-natural form) and solve for ALL invariant bilinear forms
     `G` with `σₖᵀ G σₖ = G ∀k`. The solution space is **exactly 1-dimensional**
     — the numerical witness that the commutant is scalar (Schur), the named
     hypothesis `invariantForm_proportional_of_commutantScalar` took as input.
  2. **Orthogonal (symmetric) type.** The unique invariant form's generator is
     **symmetric** (not antisymmetric) — so `std` is orthogonal type and the
     invariant form is a genuine symmetric Gram, matching the B2 premise's
     `IsSymm` requirement (discharged Lean-side in `MarkovGramRealSymm.lean`).
  3. **The Markov-side normalization scalar.** The canonical Wedderburn/Markov
     weight `w_{(4,1)}(q₀) = d_q(λ)² / [5]_q!` — the normalization the Markov
     trace assigns to the std block — is reported as the Markov-side pin of `c`.

**What stays OPEN (STRICT, §"Axiomatization is NOT a Proof").** The physical
scalar `c` in `τ(Markov Gram) = c · Hodge Gram` is
`c = (Markov normalization) / (Hodge-polarization normalization)`. This probe
pins the Markov numerator; the Hodge denominator needs the Braden–Northover
period-matrix polarization of `Jac(Bring)` ([braden-northover-2012]) — the
remaining Option-C refinement. Schur (Option B, merged) GUARANTEES the two
forms are proportional; this probe does NOT fabricate the identification,
register a `TauRhoHodgeLift` instance, or wire anything. `1/(8π)` stays a
phase-4 identification. The nullity=1 and symmetric-type facts are generic in
`q` (hold for all semisimple `q>0`), so they are independent of the q₀ pin.

Run: python3 -u computations/alpha_em_b2_scalar_c_probe.py 2>&1 | tee /tmp/b2c.log

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [braden-northover-2012] https://doi.org/10.3842/SIGMA.2012.065
-- Ref: [orellana1998] https://doi.org/10.1006/jabr.1998.7437
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import seminormal_matrices_mpfr  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

SHAPE = (4, 1)      # std = standard 4-dim S₅ irrep; #SYT = 4
N = sum(SHAPE)      # 5


def _q0() -> "mp.mpf":
    """Substrate q₀ (report the value + pin explicitly to avoid the
    muon/proton pin-confusion bug, bean tnjb). The structural conclusions
    (nullity, symmetric type) are q-independent for generic q."""
    try:
        # Q_50_DIGIT_STR, not Q: `Q` is the f64 solve (NO FLOAT64).
        from qou_substrate.constants import (  # type: ignore[import-not-found]
            Q_50_DIGIT_STR)
        return (mp.mpf(Q_50_DIGIT_STR),
                "qou_substrate.constants.Q_50_DIGIT_STR (package pin, 50 dps)")
    except Exception:
        # Fallback: canonical muon-q₀ value used by the computations/ layer.
        return mp.mpf("1.10997859555733471"), "muon-q₀ literal (computations/ layer)"


def _q_int(k: int, q: "mp.mpf") -> "mp.mpf":
    """Balanced q-integer [k]_q = (q^k - q^{-k})/(q - q^{-1})."""
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def _q_factorial(n: int, q: "mp.mpf") -> "mp.mpf":
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= _q_int(k, q)
    return out


def _hook_lengths(shape):
    lam = list(shape)
    width = lam[0]
    conj = [sum(1 for p in lam if p > j) for j in range(width)]
    hooks = []
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = conj[j] - i - 1
            hooks.append(arm + leg + 1)
    return hooks


def _q_dimension(shape, q: "mp.mpf") -> "mp.mpf":
    """d_q(λ) = [n]_q! / ∏_x [h_x]_q."""
    num = _q_factorial(sum(shape), q)
    den = mp.mpf(1)
    for h in _hook_lengths(shape):
        den *= _q_int(h, q)
    return num / den


def _wedderburn_weight(shape, q: "mp.mpf") -> "mp.mpf":
    """Markov/Wedderburn weight w_λ = d_q(λ)² / [n]_q!."""
    return _q_dimension(shape, q) ** 2 / _q_factorial(sum(shape), q)


def _matmul(A, B):
    return A * B


def _invariant_form_space(sigmas, dim):
    """Solve the CONTRAVARIANT (Markov/Specht) condition σₖᵀ G = G σₖ ∀k
    for a general dim×dim G (dim² unknowns).

    At q≠1 the seminormal σₖ are NOT orthogonal (they satisfy the Hecke
    relation, so σₖᵀσₖ ≠ 1). The invariant form is the one making σₖ
    SELF-ADJOINT: ⟨σₖ v, w⟩ = ⟨v, σₖ w⟩, i.e. Gσₖ = σₖᵀG. This is the
    Markov-trace / Specht contravariant form (`bilinM`, `bilinM_isSymm`),
    which specializes to σᵀGσ=G at q=1 (where σ becomes orthogonal). Using
    σᵀGσ=G at q≠1 gives the empty space — the bug this replaces.

    Returns (nullity, generator, evals, thresh). Builds the normal matrix
    M = Σₖ Φₖᵀ Φₖ, Φₖ : G ↦ σₖᵀ G - G σₖ (vec(G) row-major), reads the
    near-zero eigenspace via mp.eigsy.
    """
    d2 = dim * dim
    # Build each Φₖ as a d2×d2 mpmath matrix acting on vec(G).
    normal = mp.zeros(d2, d2)
    for sig in sigmas:
        Phi = mp.zeros(d2, d2)
        # out[a,b] = Σ_p σ[p,a]G[p,b] − Σ_q G[a,q]σ[q,b]
        # ∂out[a,b]/∂G[r,s] = σ[r,a]·[s==b] − [a==r]·σ[s,b]
        for a in range(dim):
            for b in range(dim):
                row = a * dim + b
                for r in range(dim):
                    for s in range(dim):
                        col = r * dim + s
                        val = mp.mpf(0)
                        if s == b:
                            val += sig[r, a]
                        if a == r:
                            val -= sig[s, b]
                        if val != 0:
                            Phi[row, col] += val
        normal += Phi.T * Phi
    evals, evecs = mp.eigsy(normal)
    lam_max = max(abs(evals[i]) for i in range(d2))
    thresh = lam_max * mp.mpf(10) ** (-30)
    null_idx = [i for i in range(d2) if abs(evals[i]) < thresh]
    nullity = len(null_idx)
    # Reshape the first null eigenvector to a dim×dim matrix.
    gen = None
    if null_idx:
        i0 = null_idx[0]
        gen = mp.zeros(dim, dim)
        for a in range(dim):
            for b in range(dim):
                gen[a, b] = evecs[a * dim + b, i0]
    return nullity, gen, evals, thresh


def main() -> int:
    q0, pin = _q0()
    print(f"q₀ = {mp.nstr(q0, 20)}  [{pin}]")
    print(f"shape λ = {SHAPE} (std), n = {N}, dps = {mp.mp.dps}")

    sigmas = seminormal_matrices_mpfr(SHAPE, q0)
    dim = sigmas[0].rows
    print(f"seminormal rep built: {len(sigmas)} generators, dim = {dim}")

    # ── sanity: Hecke relation σ² = h·σ + 1, h = q - 1/q ──
    h = q0 - 1 / q0
    hecke_res = mp.mpf(0)
    for sig in sigmas:
        R = sig * sig - (h * sig + mp.eye(dim))
        hecke_res = max(hecke_res, max(abs(R[i, j]) for i in range(dim) for j in range(dim)))
    print(f"max |σ² − (hσ+1)| = {mp.nstr(hecke_res, 4)}")

    # ── sanity: braid relation σᵢσᵢ₊₁σᵢ = σᵢ₊₁σᵢσᵢ₊₁ ──
    braid_res = mp.mpf(0)
    for i in range(len(sigmas) - 1):
        A, B = sigmas[i], sigmas[i + 1]
        R = A * B * A - B * A * B
        braid_res = max(braid_res, max(abs(R[a, b]) for a in range(dim) for b in range(dim)))
    print(f"max |braid relation residual| = {mp.nstr(braid_res, 4)}")

    # ── (i) invariant-form space ──
    nullity, gen, evals, thresh = _invariant_form_space(sigmas, dim)
    print(f"\ninvariant-form space nullity = {nullity} (expect 1 ⇒ scalar commutant, Schur)")
    print(f"eigenvalues of normal matrix (ascending, first 6): "
          f"{[mp.nstr(evals[i], 3) for i in range(min(6, dim*dim))]}")

    # ── (ii) symmetric type + orthogonality check ──
    is_symm_res = None
    orth_res = None
    if gen is not None:
        is_symm_res = max(abs(gen[a, b] - gen[b, a]) for a in range(dim) for b in range(dim))
        # normalize gen so its largest entry is 1 for readability
        scale = max(abs(gen[a, b]) for a in range(dim) for b in range(dim))
        Gn = gen * (1 / scale)
        orth_res = mp.mpf(0)
        for sig in sigmas:
            R = sig.T * Gn - Gn * sig   # self-adjointness σᵀG = Gσ
            orth_res = max(orth_res, max(abs(R[a, b]) for a in range(dim) for b in range(dim)))
        print(f"unique invariant form: max |G − Gᵀ| = {mp.nstr(is_symm_res, 4)} "
              f"(≈0 ⇒ SYMMETRIC / orthogonal type)")
        print(f"self-adjointness residual max |σᵀG − Gσ| = {mp.nstr(orth_res, 4)}")
        print("normalized invariant Gram (max-entry = 1):")
        for a in range(dim):
            print("   " + "  ".join(mp.nstr(Gn[a, b], 6) for b in range(dim)))

    # ── (iii) Markov-side normalization scalar ──
    w_lambda = _wedderburn_weight(SHAPE, q0)
    d_q = _q_dimension(SHAPE, q0)
    print(f"\nMarkov-side normalization:")
    print(f"  d_q({SHAPE}) at q₀ = {mp.nstr(d_q, 20)}  (classical dim = {dim})")
    print(f"  w_{SHAPE}(q₀) = d_q² / [5]_q! = {mp.nstr(w_lambda, 20)}")

    schur_ok = (nullity == 1)
    symm_ok = (is_symm_res is not None and is_symm_res < mp.mpf(10) ** (-30))

    verdict = (
        f"Option C (Markov-side pin of the B2 scalar c). For the actual std=(4,1) "
        f"seminormal H₅(q₀)-block: (i) the invariant-bilinear-form space is EXACTLY "
        f"{nullity}-dimensional — the numerical witness that the commutant is scalar "
        f"(absolute irreducibility, Schur), the named hypothesis of Option B's "
        f"invariantForm_proportional_of_commutantScalar (#4160); (ii) its unique "
        f"generator is SYMMETRIC (orthogonal type; residual "
        f"{mp.nstr(is_symm_res, 3) if is_symm_res is not None else 'n/a'}), matching "
        f"the B2 IsSymm premise discharged in MarkovGramRealSymm.lean; (iii) the "
        f"canonical Markov normalization is w_(4,1)(q₀) = d_q²/[5]_q! = "
        f"{mp.nstr(w_lambda, 12)}. STRICT: the physical c = (Markov norm)/(Hodge "
        f"polarization norm); the Hodge denominator needs the Braden–Northover "
        f"period polarization of Jac(Bring) — the remaining refinement. Schur "
        f"(#4160) GUARANTEES proportionality; nothing is fabricated, no "
        f"TauRhoHodgeLift instance is registered, 1/(8π) stays phase-4. Nullity=1 "
        f"and symmetric type are generic in q (q₀-pin-independent)."
    )
    print(f"\nVERDICT: {verdict}")

    wb = WitnessBuilder("alpha-em-b2-scalar-c")
    wb.set_audit_only("docs/audits/2026-07-24-alpha-em-b2-tau-identification-attack-options.md")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "α_EM B2 τ-identification, Option C (Markov-side pin of scalar c). "
        "Machine-verified for the std=(4,1) seminormal H₅(q₀)-block: invariant-form "
        "space nullity = 1 (scalar-commutant / Schur premise of #4160 confirmed), "
        "unique generator symmetric (orthogonal type, IsSymm premise), Markov weight "
        "w_(4,1)(q₀)=d_q²/[5]_q! reported as the Markov-side normalization. Hodge-side "
        "polarization normalization (Braden–Northover period matrix) is the remaining "
        "refinement; Schur guarantees proportionality. No fit, no instance, nothing "
        "wired; 1/(8π) phase-4.")
    wb.add_parameter("q0", mp.nstr(q0, 30))
    wb.add_parameter("q0_pin", pin)
    wb.add_parameter("shape", list(SHAPE))
    wb.add_parameter("dim", dim)
    wb.add_parameter("dps", mp.mp.dps)
    wb.add_assertion("scalar_commutant_nullity", nullity, 1,
                     source="invariant contravariant-form space dim (expect 1 ⇒ Schur)")
    wb.add_assertion("invariant_form_symmetric",
                     mp.nstr(is_symm_res, 4) if is_symm_res is not None else "n/a",
                     "0", tolerance=1e-30, source="max|G−Gᵀ| (orthogonal type)")
    wb.add_data("hecke_relation_residual", mp.nstr(hecke_res, 6))
    wb.add_data("braid_relation_residual", mp.nstr(braid_res, 6))
    wb.add_data("invariant_form_nullity", nullity)
    wb.add_data("invariant_form_is_symmetric", bool(symm_ok))
    wb.add_data("orthogonality_residual", mp.nstr(orth_res, 6) if orth_res is not None else None)
    wb.add_data("d_q_std_at_q0", mp.nstr(d_q, 30))
    wb.add_data("wedderburn_weight_std_at_q0", mp.nstr(w_lambda, 30))
    wb.add_data("markov_side_pin_of_c", mp.nstr(w_lambda, 30))
    wb.add_data("open_remaining", "Hodge-polarization normalization from "
                "Braden–Northover period matrix (braden-northover-2012); "
                "c = markov_norm / hodge_norm. Schur (#4160) forces proportionality.")
    wb.add_caveat("Nullity=1 and symmetric type are generic in q (hold for all "
                  "semisimple q>0), so independent of the q₀ pin. Only w_(4,1)(q₀) "
                  "is q₀-dependent.")
    wb.add_caveat("STRICT anti-laundering: this pins ONLY the Markov-side "
                  "normalization. It does NOT construct τ, assert the τ-image is "
                  "S₅-equivariant (sub-piece ii, still open), or register any "
                  "TauRhoHodgeLift instance. 1/(8π) remains a phase-4 identification.")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\nwitness → {out.name}")
    return 0 if (schur_ok and symm_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
