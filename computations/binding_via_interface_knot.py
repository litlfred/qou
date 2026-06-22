"""
binding_via_interface_knot.py — categorical binding energy via the
interface-knot Δ_I^K + Hecke-product constituent vacuum, both braids
living in the *same* H_{3A}(q) algebra.

Per the structural finding in PR #801: the tensor-product baseline
$Z·m(β_p) + N·m(β_n)$ (independent H_3 algebras) is categorically
wrong.  The correct composite is

    β_K = (β_p^(1) … β_n^(N))  ·  Δ_I^K   ∈ H_{3A}(q)
          ───────── disjoint Hecke product on
                    disjoint strand blocks ─────────  ──── interface knot ─

Per `def:ew-interface-knot` and `prop:atomic-mass-gb-nf` (deuteron's
Δ_I^D = σ_3 contributes the `+1` in u_shift = 18Z + 21N + 1).  The
existing canonical generator `atom_braid_word_3A(Z, N, include_inter=
True/False)` provides exactly the toggle: `True` yields β_K, `False`
yields T_constit^K (disjoint Hecke product, no interface crossings).

Mass-endomorphism conditions (`prop:mass-endomorphism-tower`)
satisfied by construction for the same-Hecke-algebra subtraction:

  - Markov-invariance term-by-term (Li_2^q tower preserves it)
  - |S| ≤ 2 R-side bound (descended + single + pair only)
  - Symmetric Li_2^q (NOT Faddeev Φ_q — Faddeev gives −737 MeV
    mirror-nucleus pathology per SUPERSEDED banner)
  - Three blow-up types: descended, single-gen, pair (weighted by z²)
  - Three-calibration discipline (m_e, q_0; Q_β only for absolute
    scale — variance test uses dimensionless B_dim)
  - B(p) = B(n) = 0 by construction (no interface for single nucleon)

CONVERGENCE FINDING — pair Li_2^q diverges at H_{3A>3}.
For atoms beyond the proton/neutron (H_3 case), some per-generator
V̂_i exceed 1 (V̂ ≈ 1.05–1.09 — within the H_{3A} Wedderburn-character
spectrum), and pair products |V̂_i V̂_j| ≈ 1.15 exceed the Li_2^q
convergence radius |z| < q_0 ≈ 1.1097.  The first-order tower
T1 + T2 (descended + single-generator) is FINITE; T3 (pair) requires
regularization.  This script:

  1. Computes T1 + T2 (first-order, FINITE) and reports
     B_dim^(1) = (T1+T2)_free − (T1+T2)_atom — categorical
     prediction at |S| ≤ 1.
  2. Diagnoses T3 by counting pair-product over-radius events;
     reports `T3_divergent_pairs` and `max_pair_product` per atom.
  3. T3 regularization (next iteration): options include (a) re-
     deriving V̂ under a Wedderburn-weight scheme that bounds |V̂|
     < q^{1/2}, (b) analytic continuation of Li_2^q via
     reflection formula at |z| ≥ q, (c) restriction to non-
     divergent pairs with a structural justification.

Ref: prop:unified-curvature-rank-mass-formula
Ref: prop:mass-endomorphism-tower
Ref: def:ew-interface-knot
Ref: prop:atomic-mass-gb-nf
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from codata_constants import M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION
from mass_at_3A_proper import per_generator_V_hat_3A, E_0_CALIBRATION_MEV
from _li_2_q_util import load_q_50dps, li_2_q
# Pentagon-reduced Li_2^q (with POST-τ Rogers log² correction).
# Per docs/audits/2026-05-19-pentagon-reduction-li2q.md: bare pentagon
# (P) holds pre-τ as the Hopf-algebraic characterisation; post-τ
# series form picks up the log² correction term. The pentagon
# reduction routes pair-product arguments |V_i V_j| > q_0 (outside
# the Li_2^q series radius) through a recursive identity using
# convergent sub-arguments.
from pentagon_reduction_li2q import li_2_q_pentagon


B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def mass_tower_first_order(
    vols: list[dict], q: mp.mpf, q_inv: mp.mpf, z: mp.mpf,
) -> dict:
    """First-order |S| ≤ 1 mass tower (descended + single-generator)
    plus T3 (pair-Li_2^q via pentagon reduction).

    T1 = |∏ V̂_i|
    T2 = − Σ_i Li_2^q(−|V̂_i|)
    T3 = − z² · Σ_{i<j} Li_2^q(−|V̂_i V̂_j|)

    Each Li_2^q(−|V̂_i|) in T2 is finite at q_0 ≈ 1.1097 since
    |V̂_i| < q_0. For T3 the pair products |V̂_i V̂_j| can exceed q_0;
    the algebraic pentagon identity reorganises these into convergent
    sub-arguments (see `pentagon_reduction_li2q.li_2_q_pentagon` +
    `docs/audits/2026-05-19-pentagon-reduction-li2q.md`).
    """
    flat = [mp.mpf(str(vd["full"])) for vd in vols]
    n = len(flat)

    desc = mp.mpf(1)
    for v in flat:
        desc *= v
    t1 = mp.fabs(desc)

    # T2: -Σ Li_2^q(-|V_i|)
    t2 = mp.mpf(0)
    for v in flat:
        t2 += li_2_q(-v, q, q_inv)
    t2 = -t2

    # T3: -z² · Σ_{i<j} Li_2^q(-|V_i V_j|) via pentagon reduction.
    # For pair products |V_i V_j| ≥ q_0 the pentagon factors the
    # divergent target into convergent sub-arguments (post-τ Rogers
    # log² correction is included in li_2_q_pentagon).
    t3 = mp.mpc(0)
    max_pair = mp.mpf(0)
    div_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            vi = mp.fabs(flat[i])
            vj = mp.fabs(flat[j])
            p = vi * vj
            if p > max_pair:
                max_pair = p
            if p >= q:
                div_pairs += 1
            # Argument to Li_2^q is -|V_i V_j| (negative real).
            arg = -p
            li = li_2_q_pentagon(arg, q, q_inv)
            t3 += li
    t3 = -z ** 2 * t3
    # Pentagon factorisation introduces complex intermediates whose
    # imaginary parts cancel structurally; keep the real part (with
    # tracking of residual for diagnostic).
    # Copilot review #2 on PR #822: keep imag residue as mp.mpf string
    # to preserve high-precision (don't truncate to ~53 bits).
    t3_imag_residue = str(mp.im(t3))
    t3 = mp.re(t3)

    return {
        "t1": t1, "t2": t2, "t3": t3,
        "m_first_order": t1 + t2,       # T1+T2 only — backward compat
        "m_with_t3": t1 + t2 + t3,       # T1+T2+T3 — new full first-order
        "max_pair_product": max_pair,
        "t3_divergent_pairs": div_pairs,
        "t3_imag_residue": t3_imag_residue,
        "n_generators": n,
        "vols_full": [str(v) for v in flat],
    }


def main() -> int:
    mp.mp.dps = 50
    builder = WitnessBuilder("binding-via-interface-knot")
    builder.set_description(
        "Categorical binding energy via interface-knot Δ_I^K + Hecke-"
        "product constituent vacuum (both in same H_{3A}(q)). "
        "First-order (T1+T2) computation with Li_2^q tower; T3 "
        "convergence diagnosed but deferred (pair products exceed "
        "q_0 ≈ 1.1097 for some H_{3A>3} pairs)."
    )
    builder.add_parameter("Q_beta_CAL3_MeV", str(E_0_CALIBRATION_MEV))
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    # MeV-scale provenance (Copilot review #5 on PR #822): the
    # per-atom B_MeV_first_order / B_MeV_with_t3 fields below use
    # E_0 = Q_β as the dimensionful conversion (binding-energy
    # scale, per PR #801 convention). pentagon-reduction-li2q's
    # witness uses m_e (CAL-1) for B_MeV^(1+T3) on the same
    # dimensionless number, so the two MeV columns differ by
    # ~ m_e / E_0 ≈ 0.654× by design. Compare the dimensionless
    # B_dim_* fields directly across the two witnesses for an
    # apples-to-apples check.
    builder.add_parameter("MeV_scale_factor", "E_0=Q_beta_CAL3")
    builder.add_parameter(
        "MeV_scale_note",
        "B_MeV_* fields use Q_beta as the dimensionful scale; "
        "pentagon-reduction-li2q.witness.json uses m_e. Same B_dim_* "
        "values, different MeV multipliers by ~m_e/E_0 ≈ 0.654×.",
    )

    q, q_inv, z = load_q_50dps()
    builder.add_parameter("q0_50dps", str(q))
    builder.add_parameter("z_markov_50dps", str(z))
    print(f"q_0 = {float(q):.6f},  z_M = {float(z):.6f}")
    print(f"{'atom':<6} {'A':>2} {'T1_a':>10} {'T2_a':>10} {'m_a':>10} "
          f"{'T1_f':>10} {'T2_f':>10} {'m_f':>10} {'B_dim^(1)':>10} "
          f"{'B_MeV^(1)':>10} {'B_AME':>8} {'ratio':>8} "
          f"{'max|VV|_a':>10} {'div_a':>6}")

    # 4He H_12 character sum requires > 12 GB RAM and ~5 min CPU; skip
    # by default. Override with INCLUDE_4HE=1 on a larger host.
    include_4he = os.environ.get("INCLUDE_4HE") == "1"
    atom_list = ("D", "T", "3He", "4He") if include_4he else ("D", "T", "3He")

    results = {}
    for atom in atom_list:
        Z, N = ZN[atom]
        try:
            vols_atom = per_generator_V_hat_3A(
                Z, N, include_inter=True,
                weight_scheme="normalized_plancherel")
            vols_free = per_generator_V_hat_3A(
                Z, N, include_inter=False,
                weight_scheme="normalized_plancherel")
        except (MemoryError, RuntimeError) as exc:
            results[atom] = {
                "Z": Z, "N": N, "A": Z + N, "n_strands": 3 * (Z + N),
                "compute_failed": True,
                "failure_reason": f"{type(exc).__name__}: {exc}",
                "canonical_status": "canonical-with-empirical-assignment",
                "T3_deferred": True,
                "T3_deferral_reason": (
                    "Compute failed before T3; H_12 character on this "
                    "host insufficient RAM. Retry on larger host or "
                    "use Rust geck_pfeiffer kernel (cherry-pick from PR #761)."
                ),
            }
            print(f"  {atom:<6} {Z+N:>2}  COMPUTE FAILED: "
                  f"{type(exc).__name__}: {exc}")
            continue

        ra = mass_tower_first_order(vols_atom, q, q_inv, z)
        rf = mass_tower_first_order(vols_free, q, q_inv, z)

        # T1+T2 binding (PR #801 baseline, kept for diff)
        B_dim1 = rf["m_first_order"] - ra["m_first_order"]
        B_MeV1 = mp.mpf(str(E_0_CALIBRATION_MEV)) * B_dim1
        # T1+T2+T3 binding (with pentagon-reduced pair Li_2^q)
        B_dim_full = rf["m_with_t3"] - ra["m_with_t3"]
        B_MeV_full = mp.mpf(str(E_0_CALIBRATION_MEV)) * B_dim_full
        B_emp = B_AME[atom]
        ratio_old = B_MeV1 / B_emp
        ratio_full = B_MeV_full / B_emp

        results[atom] = {
            "Z": Z, "N": N, "A": Z + N, "n_strands": 3 * (Z + N),
            "atom_config": ra, "free_config": rf,
            # Backward-compat: T1+T2-only fields kept for downstream
            # consumers that diff'd against PR #801 baseline.
            "B_dim_first_order": str(B_dim1),
            "B_MeV_first_order": str(B_MeV1),
            "ratio_pred_over_AME": float(ratio_old),
            # New: T1+T2+T3 with pentagon-reduced T3 (post-τ
            # Rogers log² correction). Per
            # docs/audits/2026-05-19-pentagon-reduction-li2q.md the
            # T3 contribution closes most of the magnitude gap on D
            # and substantially improves T, ³He.
            "B_dim_with_t3": str(B_dim_full),
            "B_MeV_with_t3": str(B_MeV_full),
            "ratio_with_t3_over_AME": float(ratio_full),
            "T3_atom_contribution": str(ra["t3"]),
            "T3_free_contribution": str(rf["t3"]),
            "T3_imag_residue_atom": ra.get("t3_imag_residue"),
            "T3_imag_residue_free": rf.get("t3_imag_residue"),
            "B_AME_MeV": str(B_emp),
            "B_pred_sign": "+" if B_MeV_full > 0 else "-",
            "canonical_status": "canonical-with-empirical-assignment",
            "T3_deferred": False,
            "T3_method": "pentagon-reduction-with-log2-correction",
        }
        # mpf→str→repr for the diagnostics fields
        for k in ("t1", "t2", "m_first_order", "max_pair_product"):
            for sub in (ra, rf):
                sub[k] = str(sub[k])
        print(f"  {atom:<6} {Z+N:>2} "
              f"T1+T2 atom={float(ra['m_first_order']):>8.4f} "
              f"T3={float(ra['t3']):>+8.4f} "
              f"| free={float(rf['m_first_order']):>8.4f} "
              f"T3={float(rf['t3']):>+8.4f} "
              f"| B(T1+T2)={float(B_MeV1):>6.3f} MeV (r={float(ratio_old):.3f}) "
              f"B(+T3)={float(B_MeV_full):>6.3f} MeV (r={float(ratio_full):.3f}) "
              f"AME={float(B_emp):>6.3f}")

    builder.add_data("per_atom", results)

    # Cross-atom variance (only successfully-computed atoms)
    computed = {k: r for k, r in results.items() if not r.get("compute_failed")}
    ratios = [r["ratio_pred_over_AME"] for r in computed.values()]
    abs_ratios = [abs(x) for x in ratios]
    rmin, rmax = (min(abs_ratios), max(abs_ratios)) if abs_ratios else (0, 0)
    mom = rmax / rmin if rmin > 0 else float("inf")
    signs_correct = all(r["B_pred_sign"] == "+" for r in computed.values())
    builder.add_data("atoms_computed", list(computed.keys()))
    builder.add_data("atoms_failed",
                      [k for k, r in results.items() if r.get("compute_failed")])
    if not include_4he:
        builder.add_data("atoms_deferred", ["4He"])
        builder.add_data("deferral_note", (
            "4He H_12 character sum requires > 12 GB RAM. Run with "
            "INCLUDE_4HE=1 on a larger host, or cherry-pick the "
            "geck_pfeiffer Rust kernel from PR #761 for a faster path."
        ))

    builder.add_data("max_over_min_abs_first_order", float(mom))
    builder.add_data("all_signs_correct_first_order", signs_correct)

    # Categorical-derivation comparison
    builder.add_data("compared_to_tensor_product_baseline", {
        "tensor_product_max_over_min": 3.96,
        "tensor_product_sign_correct": False,
        "tensor_product_failure_modes": [
            "T/³He predicted UNBOUND (wrong sign)",
            "Wrong Hecke algebra (independent H_3 instead of common H_{3A})",
            "No interface knot in baseline (tensor → no inter-block crossing)",
        ],
        "this_first_order_max_over_min": float(mom),
        "this_first_order_sign_correct": signs_correct,
    })

    if mom < 1.05 and signs_correct:
        verdict = (f"PASS — max/min^(1) = {mom:.3f} < 1.05; all signs correct. "
                   "First-order interface-knot tower closes the variance.")
    elif mom < 1.5 and signs_correct:
        verdict = (f"STRONG — max/min^(1) = {mom:.3f} < 1.5×, signs correct. "
                   "Major improvement over tensor-product 3.96× variance + "
                   "sign-wrong.")
    elif signs_correct and mom < 3.96:
        verdict = (f"IMPROVES — max/min^(1) = {mom:.3f}, signs correct. "
                   "T3 now computed via pentagon-reduction "
                   "(`pentagon_reduction_li2q.li_2_q_pentagon`); "
                   "higher-order tower terms beyond T3 still pending.")
    elif signs_correct:
        verdict = (f"SIGN-FIX — max/min^(1) = {mom:.3f}; signs correct "
                   "(tensor-product was wrong-sign). T3 computed via "
                   "pentagon-reduction; higher-order tower pending.")
    else:
        verdict = (f"NO IMPROVEMENT — max/min^(1) = {mom:.3f}, "
                   f"signs_correct = {signs_correct}")
    builder.add_data("verdict", verdict)
    print(f"\n  max/min |ratio|^(1) = {mom:.4f}  (was 3.96× under tensor-product)")
    print(f"  All B_pred^(1) > 0:   {signs_correct}  "
          "(was False — T/³He were UNBOUND under tensor-product)")
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
