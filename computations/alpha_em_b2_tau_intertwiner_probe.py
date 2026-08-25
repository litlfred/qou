#!/usr/bin/env python3
"""alpha_em_b2_tau_intertwiner_probe.py — B2 sub-piece (ii), the
binding constraint, done CORRECTLY: the Markov Gram (Hecke-invariant,
q₀) and the Hodge Gram (S₅-invariant, q=1) are BOTH diagonal in the
shared seminormal basis, and their diagonal RATIO is NOT constant — so
"τ(Markov Gram) = c·Hodge Gram" does NOT hold for the naive q→1
identification; the τ-functor must do genuine work, and its residual
IS sub-piece (ii). This SHARPENS the impact assessment: the obstacle
is not a ~20% normalization choice (period-matrix probe #4206) — it is
that WITHOUT the specific τ there is no single c AT ALL.

Correct invariance (per the sibling _invariant_form_space): at q≠1 the
asymmetric seminormal σₖ are NOT orthogonal; the invariant form is the
CONTRAVARIANT (Markov/Specht) form making σₖ self-adjoint,
  σₖᵀ G = G σₖ,
which specialises to σᵀGσ=G at q=1. In the seminormal basis this G is
DIAGONAL (the basis is contravariant-orthogonal by construction).

Pipeline (each gated):
  T1  G_M = contravariant form of ρ_H(q₀) — diagonal, 1-dim space
      (Schur); = the Markov Gram.
  T2  G_H = contravariant form of ρ_S(q→1) — diagonal, 1-dim space;
      = the Hodge/Specht form (∝ the A₄-Cartan S₅ invariant form).
  T3  the non-proportionality: normalise both to entry [0,0]=1 and
      measure the SPREAD of the diagonal ratio rᵢ = G_M[i]/G_H[i].
      rᵢ ≡ 1 ⇔ proportional (a single c exists via the identity map);
      spread > 0 ⇔ the forms differ and τ ≠ (q→1). Report the exact
      spread and each rᵢ.
  T4  q→1 scaling: recompute the spread at q = 1 + δ for a few δ and
      fit the leading power — CERTIFYING that the non-proportionality
      IS the q-deformation (spread → 0 as q → 1, leading order in
      (q−1)), i.e. τ must compensate exactly the q-deformation of the
      contravariant form. This LOCALISES what the open τ-functor does.
  T5  consequence for |c|: since rᵢ is non-constant, a single scalar c
      is DEFINED ONLY relative to a choice of τ; the period-matrix
      det/tr ambiguity (#4206) was a symptom of this deeper fact.
      Record the range of "effective c" = rᵢ·(Hodge scale) across
      tableaux as the honest c-band, and the 1/(8π) gap row.

Anti-laundering: the Grams are SOLVED (contravariant nullspace, Schur-
unique), not fitted; the non-proportionality is measured and its
q-deformation origin certified; NO c is claimed as closed — the
finding is that (ii) is essential, not cosmetic. Nothing wired;
1/(8π) phase-4; scope-(a). mpmath dps 50; no float64.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import (  # noqa: E402
    seminormal_matrices_mpfr)
from _precision import set_compute_dps  # noqa: E402

try:
    from qou_substrate.constants import q_at
except Exception:
    q_at = None

set_compute_dps()
SHAPE = (4, 1)


def q0_val():
    if q_at is not None:
        return q_at(50)
    return mp.mpf("1.10997859555733471989976322048322502665620840878")


def contravariant_form(sigmas, dim):
    """Diagonal-in-seminormal contravariant form G with σₖᵀG = Gσₖ ∀k.
    Returns (G, nullity, smallest_eig)."""
    d2 = dim * dim
    normal = mp.zeros(d2, d2)
    for sig in sigmas:
        Phi = mp.zeros(d2, d2)
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
    thresh = lam_max * mp.mpf(10) ** (-28)
    null_idx = [i for i in range(d2) if abs(evals[i]) < thresh]
    gen = None
    if null_idx:
        i0 = min(null_idx, key=lambda i: abs(evals[i]))
        gen = mp.zeros(dim, dim)
        for a in range(dim):
            for b in range(dim):
                gen[a, b] = evecs[a * dim + b, i0]
        gen = (gen + gen.T) / 2
    return gen, len(null_idx), min(abs(evals[i]) for i in range(d2))


def spread_at(q, dim):
    rho = seminormal_matrices_mpfr(SHAPE, q)
    G, nul, _ = contravariant_form(rho, dim)
    if G is None or abs(G[0, 0]) < mp.mpf("1e-40"):
        return None, None, nul
    Gn = G / G[0, 0]
    diag = [Gn[i, i] for i in range(dim)]
    off = max(abs(Gn[i, j]) for i in range(dim) for j in range(dim)
              if i != j)
    return diag, off, nul


def main() -> int:
    print("=" * 78)
    print(" B2 sub-piece (ii): Markov vs Hodge Gram — the (ii) "
          "obstruction, quantified")
    print("=" * 78)

    q0 = q0_val()
    rho0 = seminormal_matrices_mpfr(SHAPE, q0)
    dim = rho0[0].rows
    print(f"\nq₀ = {mp.nstr(q0, 18)}; shape {SHAPE}, dim {dim}")

    # T1: Markov Gram (Hecke, q₀)
    diagM, offM, nulM = spread_at(q0, dim)
    # T2: Hodge Gram (S₅, q→1)
    diagH, offH, nulH = spread_at(mp.mpf(1) + mp.mpf("1e-30"), dim)
    ok12 = nulM == 1 and nulH == 1 and offM < mp.mpf("1e-20") \
        and offH < mp.mpf("1e-20")
    print(f"\n[T1] Markov Gram (q₀): nullity {nulM}, off-diag "
          f"{mp.nstr(offM, 2)}; diag = {[mp.nstr(x, 8) for x in diagM]}")
    print(f"[T2] Hodge Gram (q→1): nullity {nulH}, off-diag "
          f"{mp.nstr(offH, 2)}; diag = {[mp.nstr(x, 8) for x in diagH]}")
    print(f"    both diagonal + Schur-unique (nullity 1): {ok12}")

    # T3: non-proportionality
    ratios = [diagM[i] / diagH[i] for i in range(dim)]
    spread = max(ratios) - min(ratios)
    ok3 = spread > mp.mpf("1e-6")     # genuinely non-proportional
    print(f"\n[T3] diagonal ratio rᵢ = G_M[i]/G_H[i] = "
          f"{[mp.nstr(r, 10) for r in ratios]}")
    print(f"    SPREAD = {mp.nstr(spread, 6)} — rᵢ NOT constant ⇒ "
          f"Markov Gram is NOT ∝ Hodge Gram under q→1 identity: {ok3}")
    print(f"    ⇒ a single scalar c does NOT exist for τ = (q→1); the "
          f"τ-functor MUST compensate this — sub-piece (ii) is "
          f"ESSENTIAL, not a normalization choice")

    # T4: q→1 scaling — certify the spread is the q-deformation
    print(f"\n[T4] q→1 scaling of the spread (certifies q-deformation "
          f"origin):")
    deltas = [mp.mpf("0.08"), mp.mpf("0.04"), mp.mpf("0.02")]
    sp = []
    for d in deltas:
        dg, _, _ = spread_at(mp.mpf(1) + d, dim)
        s = max(dg[i] / diagH[i] for i in range(dim)) \
            - min(dg[i] / diagH[i] for i in range(dim))
        sp.append(s)
        print(f"    q = 1+{mp.nstr(d, 3)}: spread = {mp.nstr(s, 8)}")
    # leading power p: spread ~ C·δ^p
    p1 = mp.log(sp[0] / sp[1]) / mp.log(deltas[0] / deltas[1])
    p2 = mp.log(sp[1] / sp[2]) / mp.log(deltas[1] / deltas[2])
    ok4 = abs(p1 - p2) < mp.mpf("0.1") and sp[2] < sp[0]
    print(f"    leading power p ≈ {mp.nstr(p1, 5)}, {mp.nstr(p2, 5)} "
          f"(spread → 0 as q → 1, order (q−1)^p): {ok4}")

    # T5: consequence for |c| — the honest c-band + 1/(8π) gap
    hodge_scale = diagH[0]      # normalization anchor (arbitrary here)
    c_eff = [ratios[i] for i in range(dim)]   # relative to G_H units
    inv8pi = 1 / (8 * mp.pi)
    print(f"\n[T5] there is no single c; the tableau-wise 'effective "
          f"ratio' spans {mp.nstr(min(c_eff), 8)}..{mp.nstr(max(c_eff), 8)} "
          f"(a {mp.nstr(spread / min(c_eff) * 100, 3)}% band)")
    print(f"    this is the DEEPER obstruction the #4206 det/tr ~20% "
          f"ambiguity was a symptom of; |c| stays τ-gated. 1/(8π) = "
          f"{mp.nstr(inv8pi, 10)} (gap row, no identification)")

    ok = ok12 and ok3 and ok4
    verdict = (
        f"SUB-PIECE (ii) IS ESSENTIAL, NOT COSMETIC — the binding "
        f"constraint QUANTIFIED: the Markov Gram (Hecke-invariant, q₀) "
        f"and the Hodge Gram (S₅-invariant, q→1) are BOTH diagonal in "
        f"the shared seminormal basis (Schur-unique, off-diag "
        f"< 1e-20) but their diagonal ratio rᵢ = "
        f"{[mp.nstr(r, 6) for r in ratios]} is NOT constant (spread "
        f"{mp.nstr(spread, 4)}), so the Markov Gram is NOT proportional "
        f"to the Hodge Gram under the naive q→1 identity — a SINGLE "
        f"scalar c does not exist for τ=(q→1). The spread vanishes as "
        f"q→1 with leading power ≈ {mp.nstr(p1, 3)} (certified "
        f"q-deformation origin), so the open τ-functor must compensate "
        f"exactly the q-deformation of the contravariant form — THAT "
        f"is the content of (ii), now localised. This SHARPENS the "
        f"assessment: the |c| obstacle is not the period-matrix det/tr "
        f"~20% normalization choice (#4206, a symptom) — it is that "
        f"without the specific τ there is no c at all. The forms' "
        f"tableau-wise ratio spans a "
        f"{mp.nstr(spread / min(c_eff) * 100, 2)}% band; |c| stays "
        f"τ-gated. A well-defined |c| therefore REQUIRES closing the "
        f"τ=P categorical identification (or route C: an intrinsic "
        f"τ-invariant ratio). Nothing wired; 1/(8π) phase-4; scope-(a)."
        if ok else
        f"INCOMPLETE (honest): T1/T2 ok={ok12} (nul {nulM},{nulH}), "
        f"T3 non-prop ok={ok3} (spread {mp.nstr(spread, 3)}), T4 "
        f"scaling ok={ok4} — data recorded; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("alpha-em-b2-tau-intertwiner", engine="mpmath")
    wb.set_description(
        "B2 sub-piece (ii) quantified: the Markov Gram (Hecke q0) and "
        "Hodge Gram (S5 q->1), both diagonal + Schur-unique in the "
        "seminormal basis, have a NON-CONSTANT diagonal ratio (spread "
        "measured, q-deformation origin certified by the q->1 power "
        "scaling) — so no single c exists under q->1; the tau-functor "
        "is essential. Sharpens the |c| obstacle beyond the #4206 "
        "det/tr ambiguity. Nothing wired; scope-(a).")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.add_data("markov_gram_diag", [mp.nstr(x, 20) for x in diagM])
    wb.add_data("hodge_gram_diag", [mp.nstr(x, 20) for x in diagH])
    wb.add_data("nonproportionality", {
        "ratios": [mp.nstr(r, 18) for r in ratios],
        "spread": mp.nstr(spread, 12),
        "percent_band": mp.nstr(spread / min(c_eff) * 100, 8),
        "single_c_exists_under_q_to_1": False})
    wb.add_data("q_deformation_scaling", {
        "deltas": [mp.nstr(d, 6) for d in deltas],
        "spreads": [mp.nstr(s, 12) for s in sp],
        "leading_power": [mp.nstr(p1, 8), mp.nstr(p2, 8)]})
    wb.add_data("inv_8pi", mp.nstr(inv8pi, 20))
    wb.add_data("verdict", verdict)
    wb.add_assertion("grams_diagonal_schur_unique",
                     computed=1.0 if ok12 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="both contravariant forms diagonal + "
                            "1-dim nullspace (Schur)")
    wb.add_assertion("markov_not_proportional_hodge",
                     computed=1.0 if ok3 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="diagonal ratio non-constant (spread > "
                            "1e-6) — no single c under q->1")
    wb.add_assertion("nonprop_is_q_deformation",
                     computed=1.0 if ok4 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="spread -> 0 as q -> 1 with a consistent "
                            "leading power (q-deformation certified)")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
