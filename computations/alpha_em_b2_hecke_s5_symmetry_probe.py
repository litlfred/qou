#!/usr/bin/env python3
"""alpha_em_b2_hecke_s5_symmetry_probe.py — the corrected sub-piece (ii) premise
is SATISFIABLE (non-vacuity guard for markovGram_transports_to_hodge).

Context (epic `qou-6ufi`, B2 τ-identification). PR #4199 corrected the (ii)
framing: the *generator*-intertwiner `ρH s·P = P·ρS s` between the Hecke and S₅
actions is UNSATISFIABLE at q₀≠1 (trace σ₁ ≈ 2.43 ≠ 2 = trace transposition;
Lean `intertwiner_trace_eq`). The correct object is `HeckeSideS5Symmetry`: an S₅
action `ρS'` **on the Hecke module space** under which the Markov Gram is
invariant, conjugate (via `T`) to the geometric S₅ action `ρS`.

This probe DEMONSTRATES that premise is genuinely satisfiable for the actual
std=(4,1) block — guarding against re-introducing a vacuous conditional (the
mistake #4199 fixes). Construction (no fit):

  1. `G_Markov` — the seminormal contravariant Gram of H₅(q₀) on (4,1)
     (positive-definite; the item-1 form, PR #4168).
  2. geometric `ρS` — the S₅ standard rep on `std` (permutation rep, sum-zero),
     invariant form `G_std` = A₄ Cartan matrix.
  3. congruence `T` with `Tᵀ · G_Markov · T = G_std` (Cholesky), and
     `ρS'(s) := T · ρS(s) · T⁻¹`. Then `G_Markov` is `ρS'`-invariant and
     `ρS'(s)·T = T·ρS(s)` — the two `HeckeSideS5Symmetry` fields — and
     `trace ρS'(s) = trace ρS(s)` (character match: NO trace obstruction, unlike
     the generator route).

**Honest scope (STRICT).** This exhibits *a* Hecke-side S₅ symmetry, proving the
structure is inhabitable (the key contrast with the obstructed generator route).
It is NOT the canonical Tits `*`-iso: `T` here is an arbitrary congruence, whereas
the canonical one is pinned by the q-deformation (continuity to q=1). So the
induced scalar is convention-dependent — `|c|` still needs the canonical τ
(sub-piece ii proper). No `HeckeSideS5Symmetry` instance for the actual τ is
registered; `1/(8π)` stays phase-4; nothing wired.

Run: python3 -u computations/alpha_em_b2_hecke_s5_symmetry_probe.py 2>&1 | tee /tmp/b2sym.log

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [braden-northover-2012] https://doi.org/10.3842/SIGMA.2012.065
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
SHAPE = (4, 1)


def _q0():
    # Q_50_DIGIT_STR, not Q: `Q` is the f64 solve, and mpf(str(Q)) would
    # convert a double to a high-precision TYPE while preserving only its
    # 17 digits (owner directive: NO FLOAT64).
    from qou_substrate.constants import (  # type: ignore[import-not-found]
        Q_50_DIGIT_STR)
    return mp.mpf(Q_50_DIGIT_STR)


def _markov_gram(sigmas, dim):
    """Seminormal contravariant Gram: the (unique, 1-dim) G with σₖᵀ G = G σₖ.
    Returns the positive-definite representative (diagonal seminormal form)."""
    d2 = dim * dim
    normal = mp.zeros(d2, d2)
    for sig in sigmas:
        Phi = mp.zeros(d2, d2)
        for a in range(dim):
            for b in range(dim):
                row = a * dim + b
                for r in range(dim):
                    for s in range(dim):
                        val = mp.mpf(0)
                        if s == b:
                            val += sig[r, a]
                        if a == r:
                            val -= sig[s, b]
                        if val != 0:
                            Phi[row, r * dim + s] += val
        normal += Phi.T * Phi
    evals, evecs = mp.eigsy(normal)
    i0 = min(range(d2), key=lambda i: abs(evals[i]))
    G = mp.zeros(dim, dim)
    for a in range(dim):
        for b in range(dim):
            G[a, b] = evecs[a * dim + b, i0]
    # make positive-definite (sign/scale): normalise so diagonal is positive
    if G[0, 0] < 0:
        G = -G
    return G


def _s5_std_perm(dim=4):
    """Geometric S₅ std rep: adjacent transpositions on b_i=e_i−e_{i+1} basis."""
    B = mp.zeros(5, 4)
    for i in range(4):
        B[i, i] = mp.mpf(1); B[i + 1, i] = mp.mpf(-1)
    BtB = B.T * B
    reps = []
    for t in range(4):
        P = mp.eye(5)
        P[t, t] = mp.mpf(0); P[t + 1, t + 1] = mp.mpf(0)
        P[t, t + 1] = mp.mpf(1); P[t + 1, t] = mp.mpf(1)
        reps.append((BtB ** -1) * (B.T * (P * B)))
    return reps


def _cartan_a4():
    G = mp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            if i == j:
                G[i, j] = mp.mpf(2)
            elif abs(i - j) == 1:
                G[i, j] = mp.mpf(-1)
    return G


def main() -> int:
    q0 = _q0(); dim = 4
    print(f"q₀ = {mp.nstr(q0, 12)}, shape {SHAPE}")
    sig = seminormal_matrices_mpfr(SHAPE, q0)
    G_M = _markov_gram(sig, dim)
    rhoS = _s5_std_perm()
    G_std = _cartan_a4()

    # Cholesky congruence: T with Tᵀ G_M T = G_std.  G_M = LMᵀ LM, G_std = LSᵀ LS,
    # T = LM⁻¹ LS  ⇒  Tᵀ G_M T = LSᵀ LM⁻ᵀ (LMᵀ LM) LM⁻¹ LS = LSᵀ LS = G_std.
    LM = mp.cholesky(G_M)      # lower: LM LMᵀ = G_M  (mpmath convention)
    LS = mp.cholesky(G_std)
    # mpmath cholesky: A = L Lᵀ.  We need Tᵀ G_M T = G_std.
    # With G_M = LM LMᵀ, set T = LM⁻ᵀ LS?  Check: Tᵀ G_M T = LSᵀ LM⁻¹ (LM LMᵀ) LM⁻ᵀ LS
    #   = LSᵀ (LMᵀ LM⁻ᵀ) LS ... not identity.  Use the symmetric-square-root free route:
    # Solve directly:  G_M = LM LMᵀ ⇒ LM⁻¹ G_M LM⁻ᵀ = I.  Want Tᵀ G_M T = G_std = LS LSᵀ.
    # Set T = LM⁻ᵀ LS: Tᵀ G_M T = LSᵀ LM⁻¹ (LM LMᵀ) LM⁻ᵀ LS = LSᵀ (LMᵀ LM⁻ᵀ) LS.
    # LMᵀ LM⁻ᵀ = (LM⁻¹ LM)ᵀ = I. So Tᵀ G_M T = LSᵀ LS.  But G_std = LS LSᵀ ≠ LSᵀ LS.
    # Cleanest: use T = LM⁻ᵀ · LSᵀ  won't square either.  Do it via eigen: G_M^{-1/2}.
    # Robust: T = G_M^{-1/2} · G_std^{1/2}  (symmetric sqrt) ⇒ Tᵀ G_M T = G_std.
    def sym_sqrt(A, inv=False):
        ev, Q = mp.eigsy(A)
        D = mp.zeros(A.rows, A.rows)
        for i in range(A.rows):
            r = mp.sqrt(ev[i]); D[i, i] = (1 / r) if inv else r
        return Q * D * Q.T
    GM_inv_sqrt = sym_sqrt(G_M, inv=True)
    Gstd_sqrt = sym_sqrt(G_std)
    T = GM_inv_sqrt * Gstd_sqrt
    # verify Tᵀ G_M T = G_std
    cong = T.T * G_M * T - G_std
    cong_res = max(abs(cong[i, j]) for i in range(4) for j in range(4))

    # ρS'(s) = T ρS(s) T⁻¹ ; verify markov_inv and intertwines and character match
    Tinv = T ** -1
    markov_res = mp.mpf(0); inter_res = mp.mpf(0); char_res = mp.mpf(0)
    for s in range(4):
        rhoSp = T * rhoS[s] * Tinv
        # markov_inv: ρS'(s)ᵀ G_M ρS'(s) = G_M
        R1 = rhoSp.T * G_M * rhoSp - G_M
        markov_res = max(markov_res, max(abs(R1[i, j]) for i in range(4) for j in range(4)))
        # intertwines: ρS'(s) T = T ρS(s)
        R2 = rhoSp * T - T * rhoS[s]
        inter_res = max(inter_res, max(abs(R2[i, j]) for i in range(4) for j in range(4)))
        # character: trace ρS'(s) = trace ρS(s)
        tr_p = sum(rhoSp[i, i] for i in range(4))
        tr_s = sum(rhoS[s][i, i] for i in range(4))
        char_res = max(char_res, abs(tr_p - tr_s))

    print(f"congruence Tᵀ·G_M·T = G_std residual : {mp.nstr(cong_res, 4)}")
    print(f"markov_inv  ρS'ᵀ·G_M·ρS' = G_M resid  : {mp.nstr(markov_res, 4)}")
    print(f"intertwines ρS'·T = T·ρS resid        : {mp.nstr(inter_res, 4)}")
    print(f"character   trace ρS' = trace ρS resid : {mp.nstr(char_res, 4)}  (0 ⇒ no trace obstruction)")
    print(f"trace ρS(s₁) = {mp.nstr(sum(rhoS[0][i,i] for i in range(4)), 6)} (S₅), "
          f"vs Hecke trace σ₁ = {mp.nstr(sum(sig[0][i,i] for i in range(4)), 6)} (≈2.43, the obstruction)")

    tol = mp.mpf(10) ** (-25)
    ok = (cong_res < tol and markov_res < tol and inter_res < tol and char_res < tol)

    verdict = (
        f"HeckeSideS5Symmetry premise is SATISFIABLE for the actual (4,1) block: "
        f"an S₅ action ρS' on the Hecke space (ρS'(s)=T·ρS(s)·T⁻¹, T the "
        f"G_M↦G_std congruence) leaves the Markov Gram invariant "
        f"(resid {mp.nstr(markov_res,3)}), conjugates to the geometric S₅ "
        f"(resid {mp.nstr(inter_res,3)}), and MATCHES characters "
        f"(trace ρS'=trace ρS, resid {mp.nstr(char_res,3)}) — so the "
        f"intertwiner_trace_eq obstruction that KILLS the generator route "
        f"(Hecke trace 2.43 ≠ 2) does NOT apply here. This confirms "
        f"markovGram_transports_to_hodge (#4199) is a genuine, NON-vacuous "
        f"reduction. STRICT: T is AN arbitrary congruence, not the canonical Tits "
        f"*-iso (which the q-deformation pins); so |c| still needs the canonical τ. "
        f"No instance registered; 1/(8π) phase-4; nothing wired."
    )
    print(f"\nVERDICT: {verdict}")

    wb = WitnessBuilder("alpha-em-b2-hecke-s5-symmetry")
    wb.set_audit_only("docs/audits/2026-07-24-alpha-em-b2-tau-identification-attack-options.md")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "α_EM B2 sub-piece (ii): the corrected HeckeSideS5Symmetry premise "
        "(markovGram_transports_to_hodge, #4199) is SATISFIABLE for the actual "
        "(4,1) block — exhibits ρS' on the Hecke space leaving the Markov Gram "
        "invariant, conjugate to the geometric S₅, with matching characters (no "
        "trace obstruction, unlike the generator route). Non-vacuity guard. T is "
        "an arbitrary congruence, not the canonical Tits *-iso; |c| still τ-gated. "
        "No instance; 1/(8π) phase-4.")
    wb.add_parameter("q0", mp.nstr(q0, 30))
    wb.add_parameter("shape", list(SHAPE))
    wb.add_assertion("premise_satisfiable", "true" if ok else "false", "true",
                     source="all four HeckeSideS5Symmetry residuals < 1e-25")
    wb.add_assertion("no_trace_obstruction", mp.nstr(char_res, 4), "0", tolerance=1e-25,
                     source="trace ρS' = trace ρS (character match)")
    wb.add_data("congruence_residual", mp.nstr(cong_res, 6))
    wb.add_data("markov_invariance_residual", mp.nstr(markov_res, 6))
    wb.add_data("intertwines_residual", mp.nstr(inter_res, 6))
    wb.add_data("character_match_residual", mp.nstr(char_res, 6))
    wb.add_data("hecke_sigma1_trace", mp.nstr(sum(sig[0][i,i] for i in range(4)), 12))
    wb.add_data("s5_transposition_trace", mp.nstr(sum(rhoS[0][i,i] for i in range(4)), 12))
    wb.add_caveat("T is AN arbitrary G_M↦G_std congruence, NOT the canonical Tits "
                  "*-iso (pinned by the q-deformation). This proves the structure "
                  "is inhabitable (contrast: the generator-intertwiner is provably "
                  "not); it does NOT pin |c|, which still needs the canonical τ.")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\nwitness → {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
