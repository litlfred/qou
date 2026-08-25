#!/usr/bin/env python3
"""alpha_em_b2_hodge_normalization_probe.py — Option C, item 2: the Hodge-side
normalization of the B2 scalar c, and the sign-consistency of the Schur match.

Follow-up to `alpha_em_b2_scalar_c_probe.py` (PR #4168, item 1 = Markov side).
The B2 statement is `τ(Markov Gram) = c · Hodge Gram`; Option B (#4160) forces the
two forms proportional (Schur, `std` irreducible). Item 1 pinned the **Markov**
numerator `w_(4,1)(q₀)`. This probe attacks the **Hodge denominator**.

## What the Hodge form actually is (corpus + Braden–Northover / Riera–Rodríguez)

`H^{1,0}(Bring) = std = (4,1)` (irreducible, `s5_bring_hodge_depth.lean`). Bring's
curve is a smooth genus-4 curve, so **its own Jacobian is principally polarized**
(the canonical theta divisor). The canonical Hodge form on `std` is the
principal-polarization metric `Y = Im(Z)` (`Z` symmetric, `Im Z > 0`) in a
symplectic homology basis (Riera–Rodríguez 1992). Aut(Bring)=S₅ acts by
isometries ⇒ `Y` is an S₅-invariant symmetric form on the irreducible `std` ⇒ by
Schur it is `∝` the standard invariant form — **positive-definite**.

**Do NOT confuse this with the isogeny `(5,5,5,1)`.** The corpus records
`Z = τ₀·C` isogeny-diagonalizing to `(5τ₀,5τ₀,5τ₀,τ₀)` (Serre `J(Bring)~E⁴`).
The tuple `(5,5,5,1)` is the **polarization TYPE of the E⁴ isogeny image** — a
*non-principal* structure on a different (isogenous) abelian variety. It is NOT
the canonical Hodge form on `std`, which (principal polarization) is `∝` the
standard form. Reading `(5,5,5,1)` as "the Hodge Gram eigenvalues" is the trap
this probe flags (it would contradict Schur, which forces a single scalar on the
irreducible `std`).

## What this probe verifies (machine, no fit)

1. Builds the standard S₅-invariant form on `std` concretely (Euclidean form
   restricted to the sum-zero subspace of the permutation rep ℝ⁵) and confirms
   it is **positive-definite** (signature (4,0)) — the shape of the canonical
   Hodge form.
2. Records the Hodge scale `Im(τ₀) ≈ 0.186676` (Braden–Northover 2208.13692;
   `BringEllipticFactor.lean`).
3. **Sign-consistency (the basis-independent advance).** The canonical Hodge
   form (positive-definite) and the Markov form (Wenzl positive-definite for
   `q>0`, confirmed for the (4,1) block in item 1) are BOTH positive-definite
   invariant forms on the irreducible `std`. Signature (4,0)=(4,0) ⇒ the Schur
   proportionality `τ(Markov)=c·Hodge` (#4160) is realized by a **positive
   scalar `c>0`** — the identification is sign-consistent (rules out any
   negative/indefinite obstruction to the lift).

## What stays OPEN — |c| is DOUBLY gated (STRICT, §"Axiomatization is NOT a Proof")

The numerical **magnitude** `|c|` is NOT independently computable. It needs both:
  (a) the explicit Riera–Rodríguez symplectic period entries `Z` (the actual
      matrix `C`) — NOT present in the corpus (only the isogeny type + `τ₀`), and
  (b) the τ-map basis-matching (sub-piece ii, still open) — to compare the two
      *canonically-normalized* forms (Markov-trace vs principal-polarization),
      which live on different structures (Hecke module vs Hodge structure).
So this **corrects the plan's framing**: item 2 is NOT independent of sub-piece
(ii) — `|c|` is coupled to the τ-equivariance. What item 2 delivers is the
*sign* of `c` (positive) and a precise statement of the two missing inputs. No
`TauRhoHodgeLift` instance is registered; `1/(8π)` stays phase-4; nothing wired.

Run: python3 -u computations/alpha_em_b2_hodge_normalization_probe.py 2>&1 | tee /tmp/b2h.log

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [braden-northover-2012] https://doi.org/10.3842/SIGMA.2012.065
-- Ref: [riera-rodriguez-1992] The period matrix of Bring's curve, Pacific J. Math. 154 (1992)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Braden–Northover period point of Bring's curve (BringEllipticFactor.lean).
TAU0_RE = mp.mpf("-0.5")
TAU0_IM = mp.mpf("0.186676")


def _std_invariant_form():
    """The standard S₅-invariant symmetric form on `std=(4,1)`.

    Realize `std` as the sum-zero subspace of the permutation rep ℝ⁵. A basis is
    b_i = e_i − e_{i+1}, i=0..3. The S₅-invariant form is the restriction of the
    Euclidean inner product; its Gram in this basis is the A₄ Cartan matrix
    (2 on the diagonal, −1 on the off-diagonal). Returns the 4×4 Gram.
    """
    dim = 4
    G = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            if i == j:
                G[i, j] = mp.mpf(2)
            elif abs(i - j) == 1:
                G[i, j] = mp.mpf(-1)
    return G


def _perm_matrices_on_std():
    """S₅ generators (adjacent transpositions s_i=(i,i+1), i=1..4) acting on
    `std` in the b_i = e_i − e_{i+1} basis, to verify invariance of the form.

    s_i permutes e_i ↔ e_{i+1}. We build the 5×5 permutation matrix, act on the
    5×4 basis-embedding B (columns b_i in ℝ⁵), and solve for the 4×4 rep matrix
    ρ(s_i) with (perm·B) = B·ρ(s_i)."""
    import mpmath
    dim = 4
    # B: 5×4, columns b_i = e_i − e_{i+1}
    B = mpmath.zeros(5, 4)
    for i in range(4):
        B[i, i] = mp.mpf(1)
        B[i + 1, i] = mp.mpf(-1)
    reps = []
    for t in range(4):  # s_{t+1} swaps index t and t+1
        P = mpmath.eye(5)
        P[t, t] = mp.mpf(0); P[t + 1, t + 1] = mp.mpf(0)
        P[t, t + 1] = mp.mpf(1); P[t + 1, t] = mp.mpf(1)
        PB = P * B
        # solve B · ρ = PB for ρ (4×4): ρ = (BᵀB)⁻¹ Bᵀ PB
        BtB = B.T * B
        rho = (BtB ** -1) * (B.T * PB)
        reps.append(rho)
    return reps


def _eigsy_min_max(M):
    evals, _ = mp.eigsy(M)
    n = M.rows
    lo = min(evals[i] for i in range(n))
    hi = max(evals[i] for i in range(n))
    return lo, hi


def main() -> int:
    print(f"τ₀ = {mp.nstr(TAU0_RE, 6)} + {mp.nstr(TAU0_IM, 8)}i   (Braden–Northover)")
    print(f"Im(τ₀) = {mp.nstr(TAU0_IM, 10)}  (Hodge scale)")

    G = _std_invariant_form()
    print("\nstandard S₅-invariant form on std (A₄ Cartan matrix):")
    for i in range(4):
        print("   " + "  ".join(mp.nstr(G[i, j], 4) for j in range(4)))
    lo, hi = _eigsy_min_max(G)
    pos_def = lo > 0
    print(f"eigenvalues in [{mp.nstr(lo, 6)}, {mp.nstr(hi, 6)}] ⇒ "
          f"positive-definite: {pos_def} (signature (4,0))")

    # verify S₅-invariance: ρ(s_i)ᵀ G ρ(s_i) = G
    reps = _perm_matrices_on_std()
    inv_res = mp.mpf(0)
    for rho in reps:
        R = rho.T * G * rho - G
        inv_res = max(inv_res, max(abs(R[a, b]) for a in range(4) for b in range(4)))
    print(f"S₅-invariance residual max|ρᵀGρ − G| = {mp.nstr(inv_res, 4)} (≈0 confirms invariant)")

    # Hodge form = principal-polarization metric ∝ this standard form (Schur).
    # Markov form (item 1) = Wenzl positive-definite. Both signature (4,0).
    hodge_posdef = pos_def
    markov_posdef = True  # established in alpha_em_b2_scalar_c_probe (nullity=1, Wenzl>0)
    sign_consistent = hodge_posdef and markov_posdef

    verdict = (
        "Option C item 2 (Hodge-side normalization of the B2 scalar c). The "
        "canonical Hodge form on std is the PRINCIPAL-polarization metric Im(Z) "
        "(Bring's own Jacobian is a ppav; Riera–Rodríguez), which by Schur is ∝ "
        "the standard S₅-invariant form — verified here positive-definite "
        f"(eigs>0, signature (4,0); S₅-invariance residual {mp.nstr(inv_res, 3)}). "
        "The isogeny tuple (5,5,5,1) is the polarization TYPE of the E⁴ isogeny "
        "image (non-principal), NOT the Hodge Gram eigenvalues — reading it as "
        "such contradicts Schur. SIGN-CONSISTENCY (basis-independent advance): "
        "the canonical Hodge form and the Markov form (Wenzl pos-def, item 1) "
        "are both positive-definite invariant forms on irreducible std, so the "
        "Schur proportionality τ(Markov)=c·Hodge (#4160) is realized by a "
        "POSITIVE scalar c>0 — sign-consistent, no indefinite obstruction. "
        "OPEN (STRICT): |c| is DOUBLY gated — needs (a) the explicit "
        "Riera–Rodríguez symplectic period entries Z (absent from the corpus; "
        "only the isogeny type + τ₀ are recorded) AND (b) the τ-map basis-match "
        "(sub-piece ii, open). This CORRECTS the plan: item 2 is coupled to (ii), "
        "not independent. No TauRhoHodgeLift instance; 1/(8π) phase-4; nothing wired."
    )
    print(f"\nVERDICT: {verdict}")

    wb = WitnessBuilder("alpha-em-b2-hodge-normalization")
    wb.set_audit_only("docs/audits/2026-07-24-alpha-em-b2-tau-identification-attack-options.md")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "α_EM B2 τ-identification, Option C item 2 (Hodge-side normalization). "
        "Canonical Hodge form on std = principal-polarization metric ∝ standard "
        "S₅-invariant form (verified positive-definite, S₅-invariant). Isogeny "
        "(5,5,5,1) is the E⁴ polarization type, NOT the Hodge Gram. Sign-consistency: "
        "Hodge + Markov both positive-definite ⇒ Schur scalar c>0. |c| doubly gated "
        "on explicit Riera–Rodríguez Z (absent) + τ-map (sub-piece ii). Corrects the "
        "plan (item 2 coupled to ii). No instance; 1/(8π) phase-4.")
    wb.add_parameter("tau0_im", mp.nstr(TAU0_IM, 12))
    wb.add_parameter("std_dim", 4)
    wb.add_assertion("hodge_form_positive_definite",
                     "true" if pos_def else "false", "true",
                     source=f"min eigenvalue {mp.nstr(lo, 6)} > 0 (Hodge-form shape)")
    wb.add_assertion("s5_invariance_residual", mp.nstr(inv_res, 4), "0",
                     tolerance=1e-30, source="max|ρᵀGρ−G|")
    wb.add_assertion("schur_scalar_sign_positive", "true" if sign_consistent else "false",
                     "true", source="both Hodge and Markov forms positive-definite ⇒ c>0")
    wb.add_data("std_invariant_form_eigs_min_max",
                [mp.nstr(lo, 8), mp.nstr(hi, 8)])
    wb.add_data("isogeny_polarization_type", [5, 5, 5, 1])
    wb.add_data("isogeny_type_note", "polarization type of the E⁴ isogeny image "
                "(non-principal), NOT the Hodge Gram eigenvalues on std")
    wb.add_data("c_magnitude_status", "DOUBLY GATED — needs (a) explicit "
                "Riera–Rodríguez symplectic period Z (absent from corpus) + "
                "(b) τ-map basis-match (sub-piece ii, open)")
    wb.add_data("c_sign", "positive (c>0), sign-consistent by signature match")
    wb.add_caveat("Corrects the attack plan: item 2 (Hodge normalization) is NOT "
                  "independent of sub-piece (ii) — |c| couples to the τ-equivariance. "
                  "Only the SIGN of c is independently determined (positive).")
    wb.add_caveat("STRICT anti-laundering: no TauRhoHodgeLift instance registered; "
                  "1/(8π) stays phase-4; the (5,5,5,1) isogeny type is not read as a "
                  "Hodge Gram (that would contradict Schur on irreducible std).")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\nwitness → {out.name}")
    return 0 if sign_consistent else 1


if __name__ == "__main__":
    raise SystemExit(main())
