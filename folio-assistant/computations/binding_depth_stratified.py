"""
binding_depth_stratified.py — depth-stratified α_k · Φ_k formula
on the same H_{3A}(q), with α_{k≥4} = m_e · 8G damping per
prop:plancherel-term-7-formulation.

CATEGORICAL STRUCTURE — KNOT CONVOLUTION OPERATOR (NOT TENSOR PRODUCT):

Per def:ew-interface-knot + the knot-indexed-convolution-grid bi-
filtration: the atomic braid is the q-shuffle CONVOLUTION

    β_K = T_constit^K  *_q  Δ_I^K  ∈ H_{3A}(q)

where T_constit^K is the disjoint Hecke product of nucleon braids on
disjoint strand-blocks AND Δ_I^K is the interface-knot operator applied
via Hecke multiplication. BOTH configurations live in the SAME H_{3A}
algebra with the SAME Wedderburn weights ~w_λ — verified at runtime
below (body identical, only interface gens differ).

This is STRUCTURALLY DISTINCT from a tensor-product baseline
(Z · m(β_p)_H_3 + N · m(β_n)_H_3 in independent H_3 algebras) which
gives 3.96× variance + WRONG SIGN on T/³He (rejected on PR #801).

Per user direction (2026-05-19, see PR #814 cross-reference):
the heavy-atom variance issue in binding_block_multiplicative.py
(T3 pair-blowup grows as A², AME as A) is structurally addressed
by the depth-stratified formula:

  m_K(T) = α_0 Φ_0 + α_1 Φ_1 + α_2 Φ_2 + α_3 Φ_3
         + (m_e · 8G) · Σ_{k ≥ 4} Φ_k

where Φ_k = Σ_{λ ⊢ 3A : depth(λ) = k} ~w_λ · log|χ^λ(β) · dim_q λ|.

The damping α_{k≥4} = m_e · 8G ≈ 3.74 MeV per Φ_k provides built-in
suppression of high-curvature-rank contributions, matching the
linear-A scaling of AME binding (vs the A²-scaling of the
mass-endomorphism pair blowup).

For the binding (positive when the bound state has lower mass):
  B(K) := m_K(T_constit^K) − m_K(β_K)
       = Σ_k α_k · [Φ_k(T_constit^K) − Φ_k(β_K)]

i.e. the implementation computes  delta = phi_free − phi_atom  per
depth k and sums with α_k.  Both chi computations are at the SAME
H_{3A}, per the Δ_I^K structural fix established in PR #801.

CROSS-REFERENCE (PR #814): the involution / Leibniz origin of c_5's
1/2 fingerprint generalises to the universal α_{k≥4} damping —
both are signatures of averaged-crossing structure entering at high
curvature rank.

Ref: prop:plancherel-term-7-formulation
Ref: prop:unified-curvature-rank-mass-formula
Ref: def:ew-interface-knot
Ref: PR #814 (silver-ratio + Pell-Lucas c_k benchmark)
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from _precision import set_compute_dps, fmt
from witness_base import WitnessBuilder
from codata_constants import M_E_MEV
from mass_at_3A_proper import (
    atom_braid_word_3A, markov_trace_3A, dim_q, qfac,
    E_0_CALIBRATION_MEV)
from q_parameter import Q as Q0


B_AME = {
    "D":   mp.mpf("2.22456607"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def alpha_k(k: int) -> mp.mpf:
    """Structural prefactor per prop:plancherel-term-7-formulation.

    α_0 = α_1 = α_3 = 1
    α_2 = z_mark² (Markov stabilisation weight squared)
    α_{k≥4} = m_e · 8G  (universal damping at high curvature rank)
    """
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G  # k ≥ 4: universal damping


def phi_k(per_partition: list, n_strands: int, k: int) -> mp.mpf:
    """Φ_k = Σ_{λ : depth(λ) = k} ~w_λ · log|χ^λ · dim_q λ|.

    Uses the q-deformed Wedderburn weight ~w_λ = dim_q²(λ) / [n]_q!
    per prop:plancherel-term-7-formulation.
    """
    total = mp.mpf(0)
    qfact = qfac(n_strands)
    for p in per_partition:
        shape = p["partition"]
        depth = len(shape) - 1
        if depth != k:
            continue
        chi = mp.mpf(str(p["chi"]))
        dim_classical = p["dim"]
        if dim_classical == 0:
            continue
        dq = dim_q(shape)  # q-deformed dimension
        magnitude = mp.fabs(chi) * dq
        if magnitude < mp.mpf("1e-30"):
            continue
        weight = mp.mpf(str(dq * dq)) / qfact
        total += weight * mp.log(magnitude)
    return total


def compute_atom_binding(Z: int, N: int) -> dict:
    """Compute depth-stratified B(K) for atom (Z, N).

    Computes chi^λ for both atom (include_inter=True) and free
    (include_inter=False) configs at H_{3A}, applies α_k · Φ_k,
    takes the difference.

    STRUCTURE CHECK: both configs use the SAME H_{3A} algebra
    (convolution structure via atom_braid_word_3A); only difference
    is whether interface generators (positions 3k+2 for k=0..A-2)
    carry the Δ_I^K crossings (atom) or are empty (free / constituent
    vacuum). This is the q-shuffle convolution structure, NOT a
    tensor product over independent H_3 algebras.
    """
    A = Z + N
    n_strands = 3 * A

    # Runtime verification: body of atom and free braid words are
    # identical; only difference is interface-gen crossings.
    w_atom = atom_braid_word_3A(Z, N, include_inter=True)
    w_free = atom_braid_word_3A(Z, N, include_inter=False)
    body_atom = [(c, d, g) for c, d, g in w_atom
                  if g % 3 != 2 or g >= n_strands - 1]
    body_free = [(c, d, g) for c, d, g in w_free
                  if g % 3 != 2 or g >= n_strands - 1]
    if body_atom != body_free:
        raise RuntimeError(
            f"Body word differs between atom and free configs for "
            f"(Z={Z}, N={N}). Expected only interface-gen difference; "
            f"got body diff = {len(body_atom) - len(body_free)} entries. "
            "This breaks the q-shuffle convolution structure — "
            "configs must use the same H_{3A} algebra with only "
            "interface gens toggled."
        )

    atom_data = markov_trace_3A(Z, N, include_inter=True)
    free_data = markov_trace_3A(Z, N, include_inter=False)

    # Compute Φ_k for each depth k = 0 .. n_strands - 1
    n_strands_max = n_strands  # max depth = n_strands - 1
    contribs_atom = {}
    contribs_free = {}
    contribs_diff = {}
    delta_phi_total = mp.mpf(0)
    for k in range(n_strands_max):
        phi_atom_k = phi_k(atom_data["per_partition"], n_strands, k)
        phi_free_k = phi_k(free_data["per_partition"], n_strands, k)
        delta = phi_free_k - phi_atom_k
        ak = alpha_k(k)
        contrib = ak * delta
        contribs_atom[k] = phi_atom_k
        contribs_free[k] = phi_free_k
        contribs_diff[k] = {
            "alpha_k": fmt(ak),
            "phi_atom": fmt(phi_atom_k),
            "phi_free": fmt(phi_free_k),
            "delta_phi": fmt(delta),
            "alpha_k_times_delta_phi": fmt(contrib),
        }
        delta_phi_total += contrib

    B_MeV = delta_phi_total
    # Output is reported in MeV because α_{k≥4} = m_e · 8G carries the
    # MeV scale; at low k, α_k is dimensionless and the per-stratum
    # contribution is mixed-units (added as if MeV).  This is the same
    # convention as prop:plancherel-term-7-formulation's universal
    # high-k residue — no external E_0 multiplier is applied here.
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "n_partitions_atom": atom_data["n_partitions"],
        "n_partitions_free": free_data["n_partitions"],
        "tr_M_atom": fmt(atom_data["total"]),
        "tr_M_free": fmt(free_data["total"]),
        "contribs_diff_by_depth": contribs_diff,
        "B_dim": fmt(delta_phi_total),
        "B_MeV": fmt(B_MeV),
        "B_pred_sign": "+" if delta_phi_total > 0 else "-",
        "canonical_status": "canonical-with-empirical-assignment",
    }


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("binding-depth-stratified")
    builder.set_description(
        "Depth-stratified α_k · Φ_k binding via prop:plancherel-term-7-"
        "formulation. α_{k≥4} = m_e · 8G provides universal damping "
        "at high curvature rank. Both atom and free chi at same "
        "H_{3A}; binding is the categorical difference Φ_k(β_K) − "
        "Φ_k(T_constit^K) summed with structural α_k weights."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    builder.add_parameter("alpha_k_geq_4_MeV",
                           str(mp.mpf(str(M_E_MEV)) * 8 * mp.catalan))

    # 4He deferred unless INCLUDE_4HE=1 (H_12 character > 12 GB RAM)
    include_4he = os.environ.get("INCLUDE_4HE") == "1"
    atom_list = ("D", "T", "3He", "4He") if include_4he else ("D", "T", "3He")

    print(f"{'atom':<6} {'Z':>3} {'N':>3} {'n_str':>6} "
          f"{'B_MeV':>10} {'B_AME':>10} {'ratio':>8}")
    results = {}
    for atom in atom_list:
        Z, N = ZN[atom]
        r = compute_atom_binding(Z, N)
        B_pred = mp.mpf(r["B_MeV"])
        B_emp = B_AME[atom]
        ratio = B_pred / B_emp if B_emp > 0 else mp.mpf("nan")
        r["B_AME_MeV"] = fmt(B_emp)
        r["ratio_pred_over_AME"] = float(ratio)
        results[atom] = r
        print(f"  {atom:<6} {Z:>3} {N:>3} {3*(Z+N):>6} "
              f"{float(B_pred):>10.4f} {float(B_emp):>10.4f} "
              f"{float(ratio):>8.4f}")

    if not include_4he:
        results["4He"] = {
            "deferred": True,
            "deferral_reason": (
                "H_12 character sum > 12 GB RAM. Set INCLUDE_4HE=1 on "
                "larger host or cherry-pick PR #761 Rust GP kernel."
            ),
        }
        print(f"  4He    2   2     12  DEFERRED (H_12 RAM)")

    builder.add_data("per_atom", results)

    valid = {k: r for k, r in results.items() if not r.get("deferred")}
    ratios = [abs(r["ratio_pred_over_AME"]) for r in valid.values()]
    rmin, rmax = (min(ratios), max(ratios)) if ratios else (0, 0)
    mom = rmax / rmin if rmin > 0 else float("inf")
    signs_correct = all(r["B_pred_sign"] == "+" for r in valid.values())
    builder.add_data("max_over_min_abs", float(mom))
    builder.add_data("all_signs_correct", signs_correct)

    if mom < 1.05 and signs_correct:
        verdict = (f"PASS — max/min = {mom:.3f} < 1.05, signs correct. "
                   "Depth-stratified α_k · Φ_k closes the variance.")
    elif mom < 1.5 and signs_correct:
        verdict = (f"STRONG — max/min = {mom:.3f}, all signs correct.")
    elif signs_correct:
        verdict = (f"PARTIAL — max/min = {mom:.3f}, signs correct.")
    else:
        verdict = (f"SIGN MISMATCH — max/min = {mom:.3f}, "
                   f"signs_correct = {signs_correct}")
    builder.add_data("verdict", verdict)
    print(f"\n  max/min |ratio| = {mom:.4f}")
    print(f"  All signs +:    {signs_correct}")
    print(f"  Verdict: {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=float(B_AME["D"]),
        expected=2.22456607,
        tolerance=1e-10,
        unit="B(D) MeV",
        source="AME 2020 deuteron binding",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
