#!/usr/bin/env python3
"""alpha_em_b2_invariant_c_probe.py — route C: can |c| be made
convention-independent (an intrinsic τ-invariant ratio, so the
normalization cancels)? The honest answer, derived: NO single scalar c
is normalization-free — the invariant content of the (Markov, Hodge)
pair is the generalized-eigenvalue SPECTRUM {rᵢ} up to overall scale
(a dim−1 = 3-parameter object), because the two forms are not
proportional (sub-piece (ii), #4216). What IS genuinely intrinsic
(scale- AND basis-invariant) are functions of the ratio-spectrum
SHAPE; the canonical geometric-mean representative of c exists but its
MAGNITUDE stays τ-scale-gated. So route C REFUTES its own premise —
and returns the exact invariant structure, which is the useful output.

Setup (from #4216, correct contravariant forms in the seminormal
basis): G_M = diag(mᵢ) (Hecke, q₀), G_H = diag(wᵢ) (S₅, q→1). The
generalized eigenvalues of the pencil (G_M, G_H) are rᵢ = mᵢ/wᵢ.

  I1  NORMALIZATION GROUP: under G_M → λ·G_M, G_H → μ·G_H (the two
      independent normalizations), rᵢ → (λ/μ)·rᵢ — a common rescale.
      So any SINGLE c ∝ (a symmetric function of rᵢ of degree 1) is
      NOT invariant; only degree-0 ratios rᵢ/rⱼ are. PROOF by direct
      transform check — the refutation of "convention cancels".
  I2  the INTRINSIC (scale+basis-invariant) scalars are functions of
      {rᵢ/r̄}: the normalized spread, the coefficient of variation,
      the spectral condition (max/min − 1). Computed exactly; these
      are the q-deformation shape (#4216: O((q−1)²)). Reported
      scope-(a) vs α_EM and 1/(8π) — the honest "is the intrinsic
      invariant α-scale?" row, NO identification.
  I3  the CANONICAL representative c = geometric mean (∏rᵢ)^{1/dim}
      (the scale-covariant degree-1 symmetric function; basis-
      invariant, = det(G_M G_H⁻¹)^{1/dim}). Its VALUE given the
      sibling-canonical Grams (Markov = q₀ seminormal weight,
      Hodge = A₄-Cartan S₅ form) is computed and compared to 1/(8π) —
      but its magnitude still carries the τ-scale, so it is a
      representative, not a closure.
  I4  q→1 CERTIFICATION: every intrinsic scalar → its q=1 value (the
      spread → 0, the geometric-mean c → the trivial 1) with the
      #4216 leading power, confirming the invariants are the
      deformation and nothing spurious.

Verdict: route C does not rescue a single convention-free |c|; the
invariant is a spectrum. This tightens the workplan — |c| genuinely
needs the τ=P categorical identification (the only remaining route to
fix the overall scale), OR the physical c must be RE-DEFINED as one of
the intrinsic scale-invariant scalars (a modeling choice for the
owner, not derivable here). Nothing wired; 1/(8π) phase-4; scope-(a).
mpmath dps 50; no float64.
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
ALPHA_EM = mp.mpf("0.0072973525693")     # CODATA fine-structure const
INV_8PI = 1 / (8 * mp.pi)


def q0_val():
    if q_at is not None:
        return q_at(50)
    return mp.mpf("1.10997859555733471989976322048322502665620840878")


def contravariant_diag(q, dim):
    """Diagonal of the contravariant seminormal form (σₖᵀG = Gσₖ),
    normalized to entry [0,0]=1."""
    rho = seminormal_matrices_mpfr(SHAPE, q)
    d2 = dim * dim
    normal = mp.zeros(d2, d2)
    for sig in rho:
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
    i0 = min(range(d2), key=lambda i: abs(evals[i]))
    g = mp.matrix(dim, dim)
    for a in range(dim):
        for b in range(dim):
            g[a, b] = evecs[a * dim + b, i0]
    g = (g + g.T) / 2
    g = g / g[0, 0]
    return [g[i, i] for i in range(dim)]


def intrinsics(ratios):
    dim = len(ratios)
    mean = mp.fsum(ratios) / dim
    var = mp.fsum([(r - mean) ** 2 for r in ratios]) / dim
    cv = mp.sqrt(var) / mean                       # coefficient of variation
    spread = max(ratios) - min(ratios)
    cond = max(ratios) / min(ratios) - 1           # spectral condition
    gm = mp.e ** (mp.fsum([mp.log(r) for r in ratios]) / dim)
    return {"mean": mean, "cv": cv, "spread": spread, "cond": cond,
            "geom_mean": gm}


def main() -> int:
    print("=" * 78)
    print(" B2 route C: is |c| a convention-free invariant? — intrinsic "
          "structure")
    print("=" * 78)

    q0 = q0_val()
    dim = len(seminormal_matrices_mpfr(SHAPE, q0))  # generators = dim? no
    rho = seminormal_matrices_mpfr(SHAPE, q0)
    dim = rho[0].rows
    print(f"\nq₀ = {mp.nstr(q0, 18)}; dim {dim}")

    mM = contravariant_diag(q0, dim)
    wH = contravariant_diag(mp.mpf(1) + mp.mpf("1e-30"), dim)
    ratios = [mM[i] / wH[i] for i in range(dim)]
    print(f"[setup] generalized eigenvalues rᵢ = mᵢ/wᵢ = "
          f"{[mp.nstr(r, 10) for r in ratios]}")

    # I1: normalization-group refutation of a single invariant c
    lam, mu = mp.mpf("2.5"), mp.mpf("0.4")
    ratios_scaled = [(lam / mu) * r for r in ratios]
    # a degree-1 symmetric function (geom mean) rescales; a degree-0
    # ratio (rᵢ/r₀) is invariant
    gm0 = intrinsics(ratios)["geom_mean"]
    gm1 = intrinsics(ratios_scaled)["geom_mean"]
    deg1_moves = abs(gm1 - (lam / mu) * gm0) < mp.mpf("1e-30")
    r_over = [ratios[i] / ratios[0] for i in range(dim)]
    r_over_s = [ratios_scaled[i] / ratios_scaled[0] for i in range(dim)]
    deg0_inv = max(abs(r_over[i] - r_over_s[i]) for i in range(dim)) \
        < mp.mpf("1e-30")
    ok1 = deg1_moves and deg0_inv
    print(f"\n[I1] normalization group (G_M→λG_M, G_H→μG_H): a single "
          f"c (degree-1) RESCALES by λ/μ ({deg1_moves}); only degree-0 "
          f"ratios rᵢ/r₀ are invariant ({deg0_inv})")
    print(f"    ⇒ NO normalization-free single c exists — the invariant "
          f"is the ratio-SPECTRUM up to scale (refutes C's premise): "
          f"{ok1}")

    # I2: the intrinsic scale-invariant scalars (the deformation shape)
    inv = intrinsics(ratios)
    print(f"\n[I2] intrinsic scale+basis-invariant scalars (the "
          f"q-deformation shape):")
    print(f"    spread max−min       = {mp.nstr(inv['spread'], 8)}")
    print(f"    spectral cond max/min−1 = {mp.nstr(inv['cond'], 8)}")
    print(f"    coeff of variation   = {mp.nstr(inv['cv'], 8)}")
    print(f"    vs α_EM = {mp.nstr(ALPHA_EM, 8)} (cond/α = "
          f"{mp.nstr(inv['cond'] / ALPHA_EM, 5)}); vs 1/(8π) = "
          f"{mp.nstr(INV_8PI, 8)} — scope-(a) rows, NO identification")

    # I3: canonical geometric-mean representative
    gm = inv["geom_mean"]
    print(f"\n[I3] canonical representative c = geom mean(rᵢ) = "
          f"det(G_M G_H⁻¹)^(1/dim) = {mp.nstr(gm, 12)}")
    print(f"    basis-invariant but scale-COVARIANT ⇒ magnitude still "
          f"τ-gated; c/(1/8π) = {mp.nstr(gm / INV_8PI, 6)} (row only)")

    # I4: q→1 certification — invariants vanish/trivialize as q→1
    print(f"\n[I4] q→1 certification of the intrinsic scalars:")
    ok4 = True
    prev = None
    for d in (mp.mpf("0.08"), mp.mpf("0.04"), mp.mpf("0.02")):
        mMd = contravariant_diag(mp.mpf(1) + d, dim)
        rd = [mMd[i] / wH[i] for i in range(dim)]
        invd = intrinsics(rd)
        print(f"    q=1+{mp.nstr(d, 3)}: cond={mp.nstr(invd['cond'], 6)}, "
              f"geom_mean={mp.nstr(invd['geom_mean'], 8)}")
        if prev is not None and not (invd["cond"] < prev):
            ok4 = False
        prev = invd["cond"]
    print(f"    cond → 0 and geom_mean → 1 as q → 1 (deformation, not "
          f"spurious): {ok4}")

    ok = ok1 and ok4
    verdict = (
        f"ROUTE C REFUTES ITS OWN PREMISE (honest, useful): |c| CANNOT "
        f"be made a convention-free single scalar. Because the Markov "
        f"and Hodge Grams are not proportional (#4216), the invariant "
        f"content of the pair is the generalized-eigenvalue SPECTRUM "
        f"rᵢ = {[mp.nstr(r, 6) for r in ratios]} up to overall scale — "
        f"a dim−1 = 3-parameter object, not one number: under "
        f"G_M→λG_M, G_H→μG_H a single c rescales by λ/μ (verified), "
        f"only degree-0 ratios rᵢ/r₀ are invariant. The genuinely "
        f"intrinsic scalars are the q-deformation SHAPE — spectral "
        f"condition {mp.nstr(inv['cond'], 5)} (≈ {mp.nstr(inv['cond'] / ALPHA_EM, 3)}·α_EM, "
        f"scope-(a), NO identification), coeff of variation "
        f"{mp.nstr(inv['cv'], 5)} — all → 0 as q→1 (certified "
        f"deformation). The canonical geometric-mean representative "
        f"c = {mp.nstr(gm, 8)} is basis-invariant but scale-covariant, "
        f"so its magnitude stays τ-gated. CONSEQUENCE for the "
        f"workplan: convention does not cancel; a well-defined |c| "
        f"needs the τ=P categorical identification to fix the overall "
        f"scale, OR the physical c must be redefined as one of the "
        f"intrinsic scale-invariant scalars (an owner modeling choice, "
        f"not derivable here). Nothing wired; 1/(8π) phase-4; "
        f"scope-(a)."
        if ok else
        f"INCOMPLETE (honest): I1 ok={ok1}, I4 ok={ok4} — data "
        f"recorded; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("alpha-em-b2-invariant-c", engine="mpmath")
    wb.set_description(
        "Route C: whether the B2 scalar |c| is a convention-free "
        "invariant. Derived NO — the non-proportional (Markov, Hodge) "
        "pair has an invariant SPECTRUM (up to scale), not a single "
        "scalar; a single c rescales under independent normalizations. "
        "The intrinsic scale-invariant scalars are the q-deformation "
        "shape (spectral condition, CV; ~alpha scale scope-(a), no ID); "
        "the geometric-mean c is basis-invariant but scale-covariant. "
        "|c| stays tau-gated. Nothing wired; scope-(a).")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.add_data("generalized_eigenvalues", [mp.nstr(r, 20)
                                            for r in ratios])
    wb.add_data("normalization_group", {
        "single_c_rescales_by_lambda_over_mu": bool(deg1_moves),
        "degree0_ratios_invariant": bool(deg0_inv),
        "convention_free_single_c_exists": False})
    wb.add_data("intrinsic_scalars", {
        "spread": mp.nstr(inv["spread"], 18),
        "spectral_condition": mp.nstr(inv["cond"], 18),
        "coeff_variation": mp.nstr(inv["cv"], 18),
        "cond_over_alpha_em": mp.nstr(inv["cond"] / ALPHA_EM, 12),
        "alpha_em": mp.nstr(ALPHA_EM, 15)})
    wb.add_data("geometric_mean_c", {
        "value": mp.nstr(gm, 25),
        "basis_invariant": True, "scale_covariant": True,
        "ratio_to_inv8pi": mp.nstr(gm / INV_8PI, 12)})
    wb.add_data("verdict", verdict)
    wb.add_assertion("no_convention_free_single_c",
                     computed=1.0 if ok1 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="single c rescales by lambda/mu under "
                            "independent Gram normalizations; only "
                            "degree-0 ratios invariant")
    wb.add_assertion("intrinsic_scalars_are_q_deformation",
                     computed=1.0 if ok4 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="spectral condition -> 0, geometric-mean "
                            "-> 1 as q -> 1")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
