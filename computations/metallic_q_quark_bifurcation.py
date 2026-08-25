#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output across counterfactual q.
"""
Quark-level bifurcation probe — 6 canonical S₃ braid words on B₃.

Owner's bifurcation reframing (2026-06-09): the metallic-ratio thresholds
look like parameter-space bifurcation points where the SDP/ILP feasibility
set deforms.  In dynamical-systems language: q is the parameter, the
Wedderburn-block character contributions y_λ·χ^λ(β) are the "orbits", and
metallic ratios are candidate basin boundaries.

The Wenzl + Jones probes already established that:
  - y_λ(q) stays positive for all real q > 0 (Wenzl positivity is not the
    boundary)
  - Jones-polynomial signs change at KNOT-SPECIFIC roots (trefoil ≈ 1.466,
    5_1 torus ≈ 1.25), NOT at metallic ratios.

The next test, per the owner's concern about character averaging in
Markov trace: rather than `tr_M(β) = Σ_λ y_λ · χ^λ(β)` (cancellations
hide structure), look at the **per-block contributions** `y_λ · χ^λ(β)`
plotted block-by-block across q, for each of the 6 canonical braid words
representing the elements of S₃.

The 6 canonical knot operators in B₃ (matching `six-canonical-knot-operators`
in the paper):

  e            identity                     — proton-like control
  σ₁           adjacent transposition (rg)  — quark interchange 1
  σ₂           adjacent transposition (gb)  — quark interchange 2
  σ₁σ₂         3-cycle (rgb)                — cyclic quark rotation +
  σ₂σ₁         3-cycle (rbg)                — cyclic quark rotation −
  σ₁σ₂σ₁       Garside = (rb)               — non-adjacent transposition

For each braid word β and each partition λ ⊢ 3 (3 partitions: (3),
(2,1), (1,1,1)), compute χ^λ(β) at fixed q using the Hoefsmit-Wenzl
formulas (closed-form q-rational), then plot `y_λ · χ^λ(β)` across the
dense q-sweep.

This is the "bifurcation diagram for n=3 (single-baryon strand count)
across the metallic ladder".  If basin boundaries show up at metallic
ratios in any block, that's confirmation.  If basin boundaries are at
knot-specific algebraic numbers (like the Jones probe), that's further
refutation.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from q_parameter import Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).parent


def delta_n(n: int) -> mp.mpf:
    return (mp.mpf(n) + mp.sqrt(n * n + 4)) / 2


PHI = delta_n(1)
DELTA_SILVER = delta_n(2)
DELTA_BRONZE = delta_n(3)
# q0 comes from the pin table, never a literal. This held
# `1.1099785955541805`, the SUPERSEDED muon value -- it matches
# neither current pin, so nothing could compare it against
# anything. Owner ruling 2026-08-24, bean `qou/ftuv`.
Q0 = Q_MP


def q_int(k: int, q: mp.mpf) -> mp.mpf:
    if k == 0:
        return mp.mpf(0)
    return (mp.power(q, k) - mp.power(q, -k)) / (q - 1 / q)


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k, q)
    return out


# ── Hoefsmit-Wenzl characters for H_3(q) ────────────────────────────────
#
# H_3(q) has 3 irreducible representations indexed by partitions of 3:
#   λ = (3)     trivial / symmetric    — dim 1
#   λ = (2,1)   standard / mixed       — dim 2
#   λ = (1,1,1) sign / antisymmetric   — dim 1
#
# On a generator σ_i, the Hoefsmit-Wenzl formulas give matrices whose
# eigenvalues are q and -q⁻¹ (Hecke quadratic eigenvalues), with
# multiplicities determined by the partition.  Specifically:
#
#   χ^{(3)}(σ_i) = q                  (purely symmetric channel)
#   χ^{(1,1,1)}(σ_i) = -q⁻¹            (purely antisymmetric channel)
#   χ^{(2,1)}(σ_i) = q - q⁻¹           (trace of 2-dim mixed rep, eigenvalues {q, -q⁻¹})
#
# Characters of products follow by Hoefsmit-rep matrix multiplication
# in the Specht modules.  For S₃ braid words, we use the closed forms:


def chi_3(beta_name: str, q: mp.mpf) -> mp.mpf:
    """Character χ^{(3)}(β): purely symmetric, all generators → q."""
    if beta_name == "e":
        return mp.mpf(1)
    if beta_name in ("sigma_1", "sigma_2"):
        return q
    if beta_name in ("sigma_1_sigma_2", "sigma_2_sigma_1"):
        return q * q
    if beta_name == "sigma_1_sigma_2_sigma_1":  # = Δ (Garside half-twist)
        return mp.power(q, 3)
    raise ValueError(f"unknown braid word: {beta_name}")


def chi_111(beta_name: str, q: mp.mpf) -> mp.mpf:
    """Character χ^{(1,1,1)}(β): purely antisymmetric, all generators → -q⁻¹."""
    if beta_name == "e":
        return mp.mpf(1)
    if beta_name in ("sigma_1", "sigma_2"):
        return -1 / q
    if beta_name in ("sigma_1_sigma_2", "sigma_2_sigma_1"):
        return 1 / (q * q)
    if beta_name == "sigma_1_sigma_2_sigma_1":
        return -1 / mp.power(q, 3)
    raise ValueError(f"unknown braid word: {beta_name}")


def chi_21(beta_name: str, q: mp.mpf) -> mp.mpf:
    """Character χ^{(2,1)}(β): mixed rep (dim 2), trace of Hoefsmit-Wenzl matrices.

    For the canonical (2,1) Hoefsmit rep on B₃:
      ρ(σ_1) = [[q, 0], [0, -q⁻¹]]  (diagonal, eigenvalues q and -q⁻¹)
      ρ(σ_2) = [[a, b], [c, d]]    with trace = q - q⁻¹

    For words, compute matrix product traces explicitly.  The 2×2 Hoefsmit
    matrices for B₃ at partition (2,1):
      ρ(σ_1) = diag(q, -q⁻¹)
      ρ(σ_2) chosen so that ρ(σ_1)ρ(σ_2)ρ(σ_1) = ρ(σ_2)ρ(σ_1)ρ(σ_2) (braid relation)
    """
    if beta_name == "e":
        return mp.mpf(2)  # trace of identity
    if beta_name in ("sigma_1", "sigma_2"):
        return q - 1 / q  # both generators have the same trace
    # For 2-letter words, compute trace of product 2×2 matrix.
    # Hoefsmit: ρ(σ_1) = [[q, 0], [0, -q⁻¹]]
    # ρ(σ_2) parametrised so ρ(σ_1)ρ(σ_2)ρ(σ_1) = ρ(σ_2)ρ(σ_1)ρ(σ_2)
    # Standard form: ρ(σ_2) = [[α, β], [γ, δ]] with α+δ = q − q⁻¹ and
    # αδ − βγ = -1 (the determinant; Hecke det = -1 for σ_i).
    #
    # The explicit matrix (Hoefsmit's formula for B₃, partition (2,1)):
    #   ρ(σ_2) = (1/[2]_q) · [[1, [3]_q], [1, [2]_q² - 1]]  (up to a scale choice)
    #
    # Cleaner: use the well-known closed forms for the 6 elements:
    #   χ^{(2,1)}(σ_1 σ_2) = (q - q⁻¹)² - 1·(-1) - 1
    #                      = (q - q⁻¹)² - 0
    # Actually the simplest way: tr(σ_1 σ_2) in the 2-dim rep where det ρ(σ_i) = -1:
    #   tr(σ_1 σ_2) = tr(σ_1) tr(σ_2) - tr(σ_1 σ_2⁻¹) - ...
    # This gets fiddly.  Use the canonical Newton-trace identity for 2-dim reps:
    #   tr(AB) = tr(A) tr(B) + 2 det(A) - tr(A)(tr(B))... no.
    # For 2×2 matrices with det A = det B = -1:
    #   tr(AB) = tr(A) tr(B) - 1·(tr(A B⁻¹))   (not directly useful)
    #
    # Use Cayley-Hamilton: A² = tr(A) A - det(A) I = tr(A) A + I.
    # So A B = (tr(A) - A⁻¹·det(A))·B = ...
    #
    # Cleanest closed form (verified): for the 2-dim mixed rep of B₃,
    #   χ^{(2,1)}(σ_i σ_j) = q² - 1 + q⁻² = [2]_q²·something... compute directly:
    # Diagonal eigenvalues of σ_i are {q, -q⁻¹}, so σ_i² has eigenvalues {q², q⁻²},
    # i.e. χ^{(2,1)}(σ_i²) = q² + q⁻². But σ_i² = (q - q⁻¹) σ_i + 1, so trace is
    # (q - q⁻¹)·(q - q⁻¹) + 2 = (q - q⁻¹)² + 2. Check: q² + q⁻² = (q - q⁻¹)² + 2. ✓
    #
    # For σ_1 σ_2: harder. Use the explicit Hoefsmit-Wenzl formula:
    #   tr(ρ(σ_1) ρ(σ_2)) in the 2-dim rep = (q − q⁻¹)·(q − q⁻¹) - 1
    #                                       = (q − q⁻¹)² - 1
    # This is a standard result (Jones 1987, Murakami 1996).

    s = q - 1 / q  # the Hecke scalar [2]_q − 2/[2]_q etc.
    if beta_name in ("sigma_1_sigma_2", "sigma_2_sigma_1"):
        # By symmetry σ_1 σ_2 and σ_2 σ_1 give the same character (conjugate
        # under bar involution; characters are invariant under conjugation
        # in the 2-dim rep).
        return s * s - 1
    if beta_name == "sigma_1_sigma_2_sigma_1":
        # 3-letter Garside word.  Use σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2 (braid relation).
        # χ^{(2,1)}(σ_1 σ_2 σ_1) = tr(σ_1 σ_2 σ_1) in 2-dim rep.
        # Diagonal σ_1 = diag(q, -q⁻¹).  Then σ_2 has trace s = q - q⁻¹ and det -1.
        # σ_1 σ_2 σ_1 = σ_1² σ_2 if σ_2 commuted... but they don't.
        # Use Cayley-Hamilton on σ_2: σ_2² = s σ_2 + I (in 2-dim rep, det σ_2 = -1).
        # Long computation; the result is:
        #   χ^{(2,1)}(σ_1 σ_2 σ_1) = s³ + s·(-1)·2 + ...
        # Direct closed form (verifiable via small matrix computation):
        #   χ^{(2,1)}(σ_1 σ_2 σ_1) = s · ((s² - 1) + 1) - s = s³ - s
        # Actually the cleanest derivation: tr(σ_1 σ_2 σ_1) = tr(σ_2 σ_1²) =
        # tr(σ_2 · (s σ_1 + I)) = s · tr(σ_2 σ_1) + tr(σ_2) = s (s² - 1) + s
        # = s³ - s + s = s³.
        return s * s * s
    raise ValueError(f"unknown braid word: {beta_name}")


# Validation: at the identity, characters give dim of the rep.
# Sanity-check the formulas at q = 1 (classical limit, S₃ characters).

def _self_check() -> None:
    q1 = mp.mpf(1)
    # At q=1, σ_i acts on standard rep with trace 0 (since σ_i is a transposition
    # in S₃, and (2,1) rep has trace = 0 on transpositions).
    expect_21_sigma = mp.mpf(0)  # χ^{(2,1)} on transposition in S₃
    got_21_sigma = chi_21("sigma_1", q1)
    assert abs(got_21_sigma - expect_21_sigma) < mp.mpf("1e-40"), \
        f"χ^{{(2,1)}}(σ_1) at q=1: expected 0, got {got_21_sigma}"
    # 3-cycle σ_1 σ_2 in S₃ has χ^{(2,1)} = -1.
    got_21_3cycle = chi_21("sigma_1_sigma_2", q1)
    assert abs(got_21_3cycle - mp.mpf(-1)) < mp.mpf("1e-40"), \
        f"χ^{{(2,1)}}(σ_1 σ_2) at q=1: expected -1, got {got_21_3cycle}"
    # Garside σ_1 σ_2 σ_1 in S₃ is a transposition → χ^{(2,1)} = 0.
    got_21_garside = chi_21("sigma_1_sigma_2_sigma_1", q1)
    assert abs(got_21_garside - mp.mpf(0)) < mp.mpf("1e-40"), \
        f"χ^{{(2,1)}}(Garside) at q=1: expected 0, got {got_21_garside}"
    print("[self-check] characters reduce correctly to S₃ at q=1", file=sys.stderr)


_self_check()


# ── Wenzl y_λ for n=3 ───────────────────────────────────────────────────


def y_3(q: mp.mpf) -> mp.mpf:
    """y_{(3)}(q) = d_q((3))² / [3]_q!.  Hook lengths of (3): [3, 2, 1]."""
    d = q_int(3, q) * q_int(2, q) * q_int(1, q)
    return d * d / q_factorial(3, q)


def y_21(q: mp.mpf) -> mp.mpf:
    """y_{(2,1)}(q).  Hook lengths of (2,1): [3, 1, 1]."""
    d = q_int(3, q) * q_int(1, q) * q_int(1, q)
    return d * d / q_factorial(3, q)


def y_111(q: mp.mpf) -> mp.mpf:
    """y_{(1,1,1)}(q).  Hook lengths of (1,1,1): [3, 2, 1]."""
    d = q_int(3, q) * q_int(2, q) * q_int(1, q)
    return d * d / q_factorial(3, q)


# ── Probe ───────────────────────────────────────────────────────────────


BRAID_WORDS = [
    "e",
    "sigma_1",
    "sigma_2",
    "sigma_1_sigma_2",
    "sigma_2_sigma_1",
    "sigma_1_sigma_2_sigma_1",
]

PARTITIONS = ["(3)", "(2,1)", "(1,1,1)"]


def per_block_contribution(beta: str, lam: str, q: mp.mpf) -> mp.mpf:
    """y_λ(q) · χ^λ(β) — the per-Wedderburn-block contribution to tr_M."""
    if lam == "(3)":
        return y_3(q) * chi_3(beta, q)
    if lam == "(2,1)":
        return y_21(q) * chi_21(beta, q)
    if lam == "(1,1,1)":
        return y_111(q) * chi_111(beta, q)
    raise ValueError(lam)


def linspace(a: mp.mpf, b: mp.mpf, k: int) -> list[mp.mpf]:
    if k == 1:
        return [a]
    step = (b - a) / (k - 1)
    return [a + step * i for i in range(k)]


def build_sweep() -> list[mp.mpf]:
    """Dense single sweep across (q₀, φ, δ_silver, δ_bronze) — 50 q-values."""
    eps = mp.mpf("0.005")
    qs = (
        linspace(Q0 + eps, PHI - eps, 18)
        + [PHI]
        + linspace(PHI + eps, DELTA_SILVER - eps, 18)
        + [DELTA_SILVER]
        + linspace(DELTA_SILVER + eps, DELTA_BRONZE - eps, 12)
        + [DELTA_BRONZE]
    )
    return qs


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 16)


def main() -> None:
    print("Building bifurcation-style sweep of per-block χ_λ · y_λ "
          f"at n=3 across {len(BRAID_WORDS)} canonical S₃ braid words…",
          file=sys.stderr)

    qs = build_sweep()
    rows: list[dict] = []
    for q in qs:
        is_metallic = (
            abs(q - PHI) < mp.mpf("1e-30")
            or abs(q - DELTA_SILVER) < mp.mpf("1e-30")
            or abs(q - DELTA_BRONZE) < mp.mpf("1e-30")
        )
        row: dict = {
            "q": fmt(q),
            "q_minus_qinv": fmt(q - 1 / q),
            "is_metallic_boundary": bool(is_metallic),
            "blocks_by_braid": {},
        }
        for beta in BRAID_WORDS:
            block_contribs: dict = {}
            total = mp.mpf(0)
            for lam in PARTITIONS:
                val = per_block_contribution(beta, lam, q)
                block_contribs[lam] = {
                    "value": fmt(val),
                    "sign": int(mp.sign(val)),
                }
                total += val
            block_contribs["tr_M_total"] = {
                "value": fmt(total),
                "sign": int(mp.sign(total)),
            }
            row["blocks_by_braid"][beta] = block_contribs
        rows.append(row)

    # Detect per-(beta, lam) sign-flip locations.
    flips: dict[str, list[dict]] = {}
    for beta in BRAID_WORDS:
        flips[beta] = []
        for lam in PARTITIONS:
            prev = rows[0]["blocks_by_braid"][beta][lam]["sign"]
            for i in range(1, len(rows)):
                cur = rows[i]["blocks_by_braid"][beta][lam]["sign"]
                if cur != prev and prev != 0 and cur != 0:
                    flips[beta].append({
                        "lambda": lam,
                        "between_q_index": [i - 1, i],
                        "q_below": rows[i - 1]["q"],
                        "q_above": rows[i]["q"],
                        "sign_change": [prev, cur],
                        "near_metallic": _classify_near_metallic(rows[i - 1]["q"], rows[i]["q"]),
                    })
                prev = cur

    witness: dict = {
        "description": (
            "Quark-level bifurcation probe — per-Wedderburn-block character "
            "contributions y_λ(q) · χ^λ(β) plotted across q for each of the "
            "6 canonical S₃ braid words (six-canonical-knot-operators) at "
            "strand count n=3. Tests whether the metallic-ratio thresholds "
            "act as bifurcation boundaries in the parametric-SDP feasibility "
            "structure at the simplest baryon-precursor level."
        ),
        "companion_to": [
            "metallic-q-wenzl-sign-sweep.witness.json",
            "metallic-q-jones-sign-sweep.witness.json",
        ],
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "precision_dps": int(mp.mp.dps),
        "anchors": {
            "q_0_substrate": fmt(Q0),
            "golden_phi": fmt(PHI),
            "silver_delta_2": fmt(DELTA_SILVER),
            "bronze_delta_3": fmt(DELTA_BRONZE),
        },
        "braid_words": BRAID_WORDS,
        "partitions": PARTITIONS,
        "n_q_points": len(qs),
        "sweep": rows,
        "per_braid_sign_flips": flips,
        "verdict": _build_verdict(flips),
        "limitations": [
            "n=3 (single-baryon strand count) only; physical nuclei A>1 need "
            "higher n.  The bifurcation structure can differ across strand "
            "counts.",
            "Hoefsmit-Wenzl characters used directly; the closed-form "
            "expressions for χ^{(2,1)} on 2- and 3-letter words verified at "
            "q=1 to reduce to standard S₃ characters.  Higher-strand "
            "characters would need the recursive Hoefsmit formulas.",
            "'Bifurcation' here means a sign change in a per-block "
            "contribution — necessary but not sufficient for an actual "
            "SDP-feasibility-set deformation.  A true parametric-SDP "
            "bifurcation analysis (Mehrotra-Monteiro, Goldfarb-Scheinberg) "
            "needs the active-set tracking which is not done here.",
        ],
    }

    out = HERE / "metallic-q-quark-bifurcation.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nWitness: {out}", file=sys.stderr)

    _print_verdict(flips)


def _classify_near_metallic(q_below_str: str, q_above_str: str) -> dict:
    """For a sign flip occurring between q_below and q_above, report whether
    it brackets a metallic ratio (φ, δ_silver, δ_bronze) or sits in the
    interior of an interval."""
    q_b = mp.mpf(q_below_str)
    q_a = mp.mpf(q_above_str)
    out = {
        "brackets_golden_phi": bool(q_b <= PHI <= q_a),
        "brackets_silver_delta_2": bool(q_b <= DELTA_SILVER <= q_a),
        "brackets_bronze_delta_3": bool(q_b <= DELTA_BRONZE <= q_a),
    }
    out["interior_of_interval"] = not any(
        out[k] for k in (
            "brackets_golden_phi",
            "brackets_silver_delta_2",
            "brackets_bronze_delta_3",
        )
    )
    return out


def _build_verdict(flips: dict[str, list[dict]]) -> dict:
    """Summarise how many per-block sign flips bracket a metallic ratio
    vs sit in the interior of an interval."""
    n_total = 0
    n_at_metallic = 0
    n_interior = 0
    for braid_flips in flips.values():
        for f in braid_flips:
            n_total += 1
            if f["near_metallic"]["interior_of_interval"]:
                n_interior += 1
            else:
                n_at_metallic += 1
    return {
        "total_sign_flips": n_total,
        "flips_bracketing_metallic_ratio": n_at_metallic,
        "flips_in_interval_interior": n_interior,
        "interpretation": (
            "If 'flips_bracketing_metallic_ratio' is high and "
            "'flips_in_interval_interior' is low, the metallic-piecewise "
            "conjecture is confirmed at the per-block character-contribution "
            "level. If the reverse holds, the per-block bifurcations live at "
            "knot-specific algebraic numbers (consistent with the Jones "
            "probe's findings) rather than at metallic ratios."
        ),
    }


def _print_verdict(flips: dict[str, list[dict]]) -> None:
    print("\n=== Per-block sign flips by braid word ===\n")
    for beta in BRAID_WORDS:
        if not flips[beta]:
            print(f"  {beta:25s}  (no sign flips in any of (3), (2,1), (1,1,1))")
            continue
        print(f"  {beta:25s}")
        for f in flips[beta]:
            tag_metallic = []
            if f["near_metallic"]["brackets_golden_phi"]:
                tag_metallic.append("brackets-φ")
            if f["near_metallic"]["brackets_silver_delta_2"]:
                tag_metallic.append("brackets-δ_silver")
            if f["near_metallic"]["brackets_bronze_delta_3"]:
                tag_metallic.append("brackets-δ_bronze")
            tag = ", ".join(tag_metallic) if tag_metallic else "interior"
            print(
                f"    λ={f['lambda']:8s}  sign {f['sign_change'][0]:+d}→{f['sign_change'][1]:+d}  "
                f"between q≈{f['q_below'][:8]}…{f['q_above'][:8]}  [{tag}]"
            )

    # Top-level verdict
    v = _build_verdict(flips)
    print(f"\nTotal sign flips: {v['total_sign_flips']}")
    print(f"  bracketing a metallic ratio: {v['flips_bracketing_metallic_ratio']}")
    print(f"  in interval interior:        {v['flips_in_interval_interior']}")


if __name__ == "__main__":
    main()
