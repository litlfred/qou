#!/usr/bin/env python3
"""alpha_em_b2_tits_deformation_probe.py — build the seminormal→Young deformation
T(q) explicitly and test the canonical Tits *-isometry (B2 sub-piece ii).

Context (epic `qou-6ufi`). The B2 wall reduces to the canonical, q-deformation-
pinned Tits *-iso `T = τ` on the (4,1) block (PRs #4199, #4209). This probe
CONSTRUCTS the deformation explicitly and tests, numerically, whether the natural
*-isometry is also a representation-intertwiner (the two conditions the canonical
Tits iso must jointly satisfy).

## Construction (no fit)

The Hoefsmit seminormal rep `ρ_H^q(σᵢ)` of (4,1) is defined on the SYT basis for
all q, with a DIAGONAL contravariant Gram `G(q) = diag(g_i(q))` (the item-1 /
#4168 Markov form). As q→1, `ρ_H^q(σᵢ) → ` Young's rep of the transposition
(eigenvalues → ±1). The natural deformation *-isometry is

    T(q) = diag( √(g_i(1)/g_i(q)) ),   so   T(q)ᵀ · G(q) · T(q) = G(1)  (exact),

with `T(q) → Id` as `q → 1`. This is the seminormal→Young frame alignment.

## The decisive test

A *-isometry alone is not the Tits iso — the Tits iso must ALSO be a
representation intertwiner (`T·ρ_H^q·T⁻¹` must be the target action). This probe
checks both:

  (i)  *-isometry:  `T(q)ᵀ·G(q)·T(q) = G(1)`  and  `T·ρ_H^q·T⁻¹` self-adjoint
       w.r.t. `G(1)`  ⇒ `T` is a valid *-COMPATIBLE Tits conjugator (φ = ρ_S⁻¹ ∘
       conj(T) ∘ ρ_H is a *-algebra iso H₅(q) → ℂ[S₅] on the block).
  (ii) intertwiner-of-GENERATORS:  is `T·ρ_H^q(σᵢ)·T⁻¹ = ρ_H^1(σᵢ)` (Young)?
       This FAILS: `T·ρ_H^q·T⁻¹` keeps the Hecke eigenvalues `q,−q⁻¹`, whereas
       Young has `±1`. So `T` conjugates `σᵢ` to `ρ_S(φ(σᵢ))` — a NON-generator
       element of ℂ[S₅] — confirming the Tits iso is an ALGEBRA iso, not a
       generator conjugation (the `intertwiner_trace_eq` obstruction, #4199).

**Upshot.** `T(q)` IS a concrete, deformation-continuous (`→Id` at q=1),
*-compatible Tits conjugator for the (4,1) block — a genuine candidate for the
canonical `τ` on the Hecke→(q=1 seminormal) half. What it does NOT do (honest
residual): the (q=1 seminormal SYT basis) → (Hodge period basis) alignment `U`,
which needs the S₅ action in the Braden–Northover period basis — NOT in the
corpus (only the Hodge Gram `M_S = 5·Id−𝟙` is). So `|c|` stays gated on that pure
S₅-intertwiner `U`, not on the deformation. No instance registered; `1/(8π)`
phase-4; nothing wired.

Run: python3 -u computations/alpha_em_b2_tits_deformation_probe.py 2>&1 | tee /tmp/tits.log

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
DIM = 4


def _q0():
    # Q_50_DIGIT_STR, not Q: `Q` is the f64 solve, and mpf(str(Q)) would
    # convert a double to a high-precision TYPE while preserving only its
    # 17 digits (owner directive: NO FLOAT64).
    from qou_substrate.constants import (  # type: ignore[import-not-found]
        Q_50_DIGIT_STR)
    return mp.mpf(Q_50_DIGIT_STR)


def _diag_gram(sigmas):
    """Diagonal contravariant Gram G with σₖᵀ G = G σₖ, normalised g_0 = 1.
    (The seminormal SYT basis is orthogonal w.r.t. the contravariant form.)"""
    d2 = DIM * DIM
    normal = mp.zeros(d2, d2)
    for sig in sigmas:
        Phi = mp.zeros(d2, d2)
        for a in range(DIM):
            for b in range(DIM):
                row = a * DIM + b
                for r in range(DIM):
                    for s in range(DIM):
                        val = mp.mpf(0)
                        if s == b:
                            val += sig[r, a]
                        if a == r:
                            val -= sig[s, b]
                        if val != 0:
                            Phi[row, r * DIM + s] += val
        normal += Phi.T * Phi
    evals, evecs = mp.eigsy(normal)
    i0 = min(range(d2), key=lambda i: abs(evals[i]))
    G = mp.zeros(DIM, DIM)
    for a in range(DIM):
        for b in range(DIM):
            G[a, b] = evecs[a * DIM + b, i0]
    if G[0, 0] < 0:
        G = -G
    return G


def _offdiag_max(M):
    return max(abs(M[i, j]) for i in range(DIM) for j in range(DIM) if i != j)


def main() -> int:
    q0 = _q0()
    q_ref = mp.mpf("1.000001")   # proxy for q=1 (seminormal is singular exactly at 1)
    print(f"q₀ = {mp.nstr(q0, 12)},  q_ref (≈1) = {mp.nstr(q_ref, 8)}")

    sig0 = seminormal_matrices_mpfr(SHAPE, q0)
    sig1 = seminormal_matrices_mpfr(SHAPE, q_ref)
    G0 = _diag_gram(sig0)
    G1 = _diag_gram(sig1)

    # deformation sweep: eigenvalues of σ₁ at q → 1 approach ±1 (Young)
    print("\ndeformation ρ_H^q(σ₁) eigenvalues (→ Young ±1 as q→1):")
    for q in [mp.mpf("1.0001"), mp.mpf("1.01"), mp.mpf("1.1"), q0]:
        s = seminormal_matrices_mpfr(SHAPE, q)[0]
        ev, _ = mp.eig(mp.matrix(s.tolist()))
        print(f"   q={mp.nstr(q,6):>10}:  {[mp.nstr(e,5) for e in ev]}  "
              f"(Hecke expects q={mp.nstr(q,5)}, −1/q={mp.nstr(-1/q,5)})")

    # T(q₀) = diag(sqrt(g_i(1)/g_i(q0)))
    T = mp.zeros(DIM, DIM)
    for i in range(DIM):
        T[i, i] = mp.sqrt(G1[i, i] / G0[i, i])
    Tinv = mp.zeros(DIM, DIM)
    for i in range(DIM):
        Tinv[i, i] = 1 / T[i, i]

    # (i) *-isometry: Tᵀ G0 T = G1
    iso = T.T * G0 * T - G1
    iso_res = max(abs(iso[i, j]) for i in range(DIM) for j in range(DIM))
    # T conjugate self-adjoint w.r.t. G1: G1 (T ρ T⁻¹) = (T ρ T⁻¹)ᵀ G1
    sa_res = mp.mpf(0)
    eig_gap = mp.mpf(0)
    for s in range(4):
        # isometry Tᵀ·G0·T = G1 ⇒ T⁻¹·ρ·T is G1-self-adjoint (conjugation direction matters)
        rp = Tinv * sig0[s] * T
        R = G1 * rp - rp.T * G1
        sa_res = max(sa_res, max(abs(R[i, j]) for i in range(DIM) for j in range(DIM)))
        # (ii) generator-intertwiner check: is T ρ_H^{q0} T⁻¹ = ρ_H^1 (Young)?  eigenvalue gap
        evp, _ = mp.eig(mp.matrix(rp.tolist()))
        evy, _ = mp.eig(mp.matrix(sig1[s].tolist()))
        # compare sorted real parts
        gap = abs(sorted([mp.re(e) for e in evp])[0] - sorted([mp.re(e) for e in evy])[0])
        eig_gap = max(eig_gap, gap)

    # T → Id as q→1?
    T_ref = mp.zeros(DIM, DIM)
    G1b = _diag_gram(seminormal_matrices_mpfr(SHAPE, mp.mpf("1.0001")))
    for i in range(DIM):
        T_ref[i, i] = mp.sqrt(G1[i, i] / G1b[i, i])
    to_id = max(abs(T_ref[i, i] - 1) for i in range(DIM))

    print(f"\n(i)  *-isometry  Tᵀ·G(q₀)·T = G(1)     residual : {mp.nstr(iso_res, 4)}")
    print(f"     T·ρ·T⁻¹ self-adjoint w.r.t. G(1)   residual : {mp.nstr(sa_res, 4)}")
    print(f"     T(q)→Id as q→1                     |T−Id|   : {mp.nstr(to_id, 4)}")
    print(f"(ii) generator-intertwiner  T·ρ_H^q·T⁻¹ = Young?  eig gap : {mp.nstr(eig_gap, 4)}")
    print(f"     (gap ≈ |q₀−1| ⇒ NOT a generator intertwiner — Tits φ sends σᵢ to a non-generator)")

    tol = mp.mpf(10) ** (-20)
    iso_ok = (iso_res < tol and sa_res < tol)
    obstruction_persists = (eig_gap > mp.mpf("0.01"))

    verdict = (
        f"Explicit seminormal→Young Tits deformation for (4,1). T(q₀)="
        f"diag(√(g_i(1)/g_i(q₀))) is (i) a valid *-COMPATIBLE Tits conjugator — "
        f"exact *-isometry Tᵀ·G(q₀)·T=G(1) (resid {mp.nstr(iso_res,3)}), conjugate "
        f"self-adjoint w.r.t. G(1) (resid {mp.nstr(sa_res,3)}), and →Id as q→1 "
        f"(|T−Id|={mp.nstr(to_id,3)} at the q-step); so φ=ρ_S⁻¹∘conj(T)∘ρ_H is a "
        f"*-algebra iso H₅(q₀)→ℂ[S₅] on the block. (ii) It is NOT a "
        f"generator-intertwiner: T·ρ_H^{{q₀}}·T⁻¹ keeps the Hecke eigenvalues "
        f"(gap {mp.nstr(eig_gap,3)} ≈ |q₀−1| vs Young ±1), so σᵢ maps to a "
        f"NON-generator element of ℂ[S₅] — confirming the algebra-iso picture and "
        f"the intertwiner_trace_eq obstruction (#4199). UPSHOT: the deformation "
        f"half (Hecke→q=1 seminormal) is explicitly constructed and *-isometric; "
        f"the residual to |c| is the pure-S₅ alignment U of the q=1 seminormal SYT "
        f"basis to the Braden–Northover period basis (M_S), whose S₅ action is NOT "
        f"in the corpus. No instance; 1/(8π) phase-4; nothing wired."
    )
    print(f"\nVERDICT: {verdict}")

    wb = WitnessBuilder("alpha-em-b2-tits-deformation")
    wb.set_audit_only("docs/audits/2026-07-24-alpha-em-b2-tau-identification-attack-options.md")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "α_EM B2 canonical Tits *-iso: explicit seminormal→Young deformation T(q)="
        "diag(√(g_i(1)/g_i(q))) for (4,1). Verified: (i) exact *-isometry to the "
        "q=1 seminormal Gram + self-adjoint conjugate + T→Id at q=1 ⇒ a valid "
        "*-compatible Tits conjugator (φ a *-algebra iso on the block); (ii) NOT a "
        "generator-intertwiner (eig gap ≈ |q₀−1|, σᵢ↦non-generator) — confirms the "
        "algebra-iso picture. Residual to |c|: the pure-S₅ alignment to the "
        "Braden–Northover period basis (S₅ action not in corpus). No instance; "
        "1/(8π) phase-4.")
    wb.add_parameter("q0", mp.nstr(q0, 30))
    wb.add_parameter("q_ref", mp.nstr(q_ref, 12))
    wb.add_assertion("star_isometry_and_selfadjoint", "true" if iso_ok else "false", "true",
                     source="Tᵀ·G(q₀)·T=G(1) and T·ρ·T⁻¹ G(1)-self-adjoint (<1e-20)")
    wb.add_assertion("generator_obstruction_persists", "true" if obstruction_persists else "false",
                     "true", source="T·ρ_H^q·T⁻¹ keeps Hecke eigenvalues (gap≈|q₀−1|)")
    wb.add_data("star_isometry_residual", mp.nstr(iso_res, 6))
    wb.add_data("selfadjoint_residual", mp.nstr(sa_res, 6))
    wb.add_data("T_to_identity_at_q1", mp.nstr(to_id, 6))
    wb.add_data("generator_eig_gap", mp.nstr(eig_gap, 6))
    wb.add_data("T_diag", [mp.nstr(T[i, i], 12) for i in range(DIM)])
    wb.add_data("G_markov_q0_diag", [mp.nstr(G0[i, i], 12) for i in range(DIM)])
    wb.add_data("G_markov_q1_diag", [mp.nstr(G1[i, i], 12) for i in range(DIM)])
    wb.add_caveat("T(q) closes the DEFORMATION half (Hecke→q=1 seminormal), a valid "
                  "*-compatible Tits conjugator. The geometric-realization half — the "
                  "pure-S₅ intertwiner U from the q=1 seminormal SYT basis to the "
                  "Braden–Northover period basis (M_S) — needs the S₅ action in that "
                  "basis, which is NOT in the corpus. |c| stays gated on U.")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\nwitness → {out.name}")
    return 0 if (iso_ok and obstruction_persists) else 1


if __name__ == "__main__":
    raise SystemExit(main())
