#!/usr/bin/env python3
"""Multiplicity-refined `n_⋆` probe + Type-B-folded-crystal-depth
candidate for `conj:brane-tower-z-habiro`.

Both scalar-eigenvalue and per-eigenvalue operator-valued forms of
the level-selection rule have been refuted under uniform `k` (commit
`00292059`).  The remaining open branch is whether a **substrate-
derived per-atom rule** `n_⋆(𝔥)` — built from the per-generator
near-pole multiplicity profile `m(𝔥)` and/or the Type-B-folded-
crystal structure of `H_{3A}(q_0)` — closes the AME light-isotope
binding gap uniformly across `{D, T, ³He}`.

Per the conjecture's falsifiability §, a *substrate-derived* per-atom
`n_⋆` (without empirical retuning) is permitted; ad-hoc per-atom
selection is not.  This probe tests four candidate rules constructed
from substrate data alone:

  (R1) **Multiplicity-shifted Hecke grade**
       `n_⋆(𝔥) = max(1, k_Hecke(𝔥) - m_max(𝔥) + 1)`
       where `m_max(𝔥)` counts per-generator scalar volumes
       `|V̂_i(q_0)|` within ε of the pole at `q_0`.

  (R2) **Multiplicity-truncated Hecke grade**
       `n_⋆(𝔥) = floor(k_Hecke(𝔥) / m_max(𝔥))`
       (alternative simple shift).

  (R3) **Type-B-folded-crystal depth** (AGENTS.md §7b)
       `n_⋆(𝔥) = depth_of_dominant_self_dual_partition(𝔥)`
       where `λ_⋆(𝔥) = argmax_{λ = λ^T} |y_λ(q_0) · χ^λ_q(β_𝔥)|`
       and `depth(λ) = #{cells of λ above the main diagonal}`.
       Self-conjugate partitions are the fixed points of the
       Type-B-folding involution `λ ↔ λ^T`; stable matter
       (D, T, ³He are stable) is the fixed-point locus.

  (R4) **Type-B-folded-crystal depth · multiplicity correction**
       `n_⋆(𝔥) = max(1, depth(λ_⋆) - m_max(𝔥) + 1)`
       — combines (R1) and (R3).

The per-eigenvalue spectra persisted in
`probe-phiq-operator-valued.witness.json` (commit `00292059`) supply
the Wedderburn-block contributions; no new heavy compute required.

Output: `probe-phiq-multiplicity-refined.witness.json`
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder
from hecke_core import atom_per_generator_volumes, partition_is_self_conjugate

AME = {"deuteron": 2.224566, "tritium": 8.481798, "he3": 7.71806}
Z_N = {"deuteron": (1, 1), "tritium": (1, 2), "he3": (2, 1)}
RHO_MAP = {"deuteron": 1, "tritium": 2, "he3": 2}
# k_Hecke per atom from joint-tower-sdp-h6-h9.witness.json conventions.
K_HECKE = {"deuteron": 2, "tritium": 9, "he3": 2}
# Near-pole band width: |V̂_i| within ε of q_0 counts as a pole-driver.
NEAR_POLE_EPSILON = 0.15
THRESHOLD_PCT = 10.0


class PhiQPoleHit(Exception):
    pass


def phi_q_truncated(z, k_max, q=float(Q0)):
    qi = 1.0 / q
    product = 1.0
    qi_pow = qi
    for k in range(1, k_max + 1):
        factor = 1.0 - qi_pow * z
        if abs(factor) < 1e-14:
            raise PhiQPoleHit(f"j={k}, q^-j·z={qi_pow * z:.4g}")
        product /= factor
        qi_pow *= qi
    return product


def phi_q_truncated_complex(mu, k_max, q=float(Q0)):
    qi = 1.0 / q
    product = 1.0 + 0j
    qi_pow = qi
    for j in range(1, k_max + 1):
        factor = 1.0 - qi_pow * mu
        if abs(factor) < 1e-14:
            raise PhiQPoleHit(f"j={j}")
        product /= factor
        qi_pow *= qi
    return product


def tower_op_at_n_star(per_atom_row, n_star):
    """Per-eigenvalue operator-valued tower at given n_⋆.

    tower_op = |Σ_λ y_λ · Σ_a Φ_q^{[≤n_⋆]}(μ_a^(λ))|
    """
    total = 0.0 + 0j
    for row in per_atom_row["rows"]:
        y = float(row["y_at_q0"])
        evs = [complex(r, i) for r, i in zip(
            row["eigenvalues_real"], row["eigenvalues_imag"]
        )]
        per_irrep = sum(
            phi_q_truncated_complex(mu, n_star) for mu in evs
        )
        total += y * per_irrep
    return abs(total)


def near_pole_multiplicity_profile(Z, N, *, epsilon=NEAR_POLE_EPSILON,
                                     q=float(Q0)):
    """Per-generator near-pole multiplicity m_max(𝔥).

    Returns (m_max, per_generator_magnitudes, near_pole_indices)
    where m_max = #{i : |V̂_i(q_0)| ≥ q_0 - epsilon}.
    """
    vols_dict = atom_per_generator_volumes(Z, N, include_inter=True)
    mags = [abs(v["full"]) if isinstance(v, dict) else abs(v)
            for v in vols_dict]
    threshold = q - epsilon
    near_pole = [i for i, m in enumerate(mags) if m >= threshold]
    return len(near_pole), mags, near_pole


def partition_diagonal_depth(partition):
    """`depth(λ)` = #{cells of λ strictly above the main diagonal}.

    For self-conjugate λ, equals #{cells strictly below diagonal}
    (the Young diagram is symmetric across the diagonal).  For a
    general λ, this is the "upper-triangular" cell count.  Used as
    a proxy for Kashiwara crystal depth on the Type-B-folded
    subcrystal.
    """
    rows = list(partition)
    depth = 0
    for i, row_len in enumerate(rows):
        # Cells (i, j) with j > i are above-diagonal.
        depth += max(0, row_len - (i + 1))
    return depth


def dominant_self_dual_partition(per_atom_row):
    """Identify λ_⋆ = argmax_{λ = λ^T} |y_λ · χ^λ_q(β)| from the
    persisted per-irrep rows.

    Returns (λ_⋆, depth(λ_⋆), |y_λ_⋆ · χ^λ_⋆|).  If no self-conjugate
    partition appears in the rows, returns (None, 0, 0.0).
    """
    best = None
    best_mag = -1.0
    for row in per_atom_row["rows"]:
        partition = tuple(row["partition"])
        if not partition_is_self_conjugate(partition):
            continue
        y = float(row["y_at_q0"])
        chi = float(row["chi_q_at_q0"])
        mag = abs(y * chi)
        if mag > best_mag:
            best_mag = mag
            best = partition
    if best is None:
        return None, 0, 0.0
    return best, partition_diagonal_depth(best), best_mag


def main():
    HERE = Path(__file__).parent
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]
    def sigma_3A(A):
        return float(sigma_3A_witness[f"n={3 * A}"])

    tr_M_witness = json.loads(
        (HERE / "probe-phiq-operator-valued.witness.json").read_text()
    )

    q0_val = float(Q0)

    w = (
        WitnessBuilder("probe-phiq-multiplicity-refined", engine="python")
        .set_description(
            "Multiplicity-refined and Type-B-folded-crystal-depth `n_⋆` "
            "candidates for conj:brane-tower-z-habiro.  Tests four "
            "substrate-derived per-atom rules (R1 multiplicity-shifted "
            "Hecke; R2 multiplicity-truncated Hecke; R3 Type-B-folded "
            "self-dual partition diagonal depth; R4 combination) using "
            "the per-generator scalar volumes (hecke_core."
            "atom_per_generator_volumes) and the per-irrep Wedderburn "
            "rows persisted in probe-phiq-operator-valued.witness.json "
            "(commit 00292059).  Substrate-derived per-atom n_⋆ is "
            "permitted by the conjecture's falsifiability criterion; "
            "ad-hoc retuning is not.  This is the remaining open "
            "branch of the n_⋆ existence claim after both scalar-"
            "eigenvalue and operator-valued (per-eigenvalue) uniform-k "
            "forms have been refuted."
        )
        .set_content_block("conj:brane-tower-z-habiro")
        .add_parameter("q_0", q0_val)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("near_pole_epsilon", NEAR_POLE_EPSILON)
        .add_parameter("threshold_pct", THRESHOLD_PCT)
        .add_parameter("rules_tested",
                        ["R1_mult_shifted", "R2_mult_truncated",
                         "R3_type_b_depth", "R4_combined"])
    )

    print("=" * 88)
    print("Multiplicity-refined + Type-B-folded-crystal `n_⋆` probe")
    print("=" * 88)
    print(f"  q_0 = {q0_val}, near-pole ε = {NEAR_POLE_EPSILON}")
    print(f"  Threshold for closure: {THRESHOLD_PCT}% across all atoms")
    print()

    # Per-atom substrate data: m_max, λ_⋆, depth(λ_⋆), volumes
    print("  Substrate data per atom:")
    print(f"  {'atom':>10} {'A':>3} {'n':>3} {'k_Hecke':>9}"
          f" {'m_max':>6} {'λ_⋆':>14} {'depth(λ_⋆)':>11}"
          f" {'|y·χ|_max':>11}")
    print("  " + "-" * 76)
    per_atom_data = {}
    for name, (Z, N) in Z_N.items():
        A = Z + N
        n = 3 * A
        k_hecke = K_HECKE[name]
        m_max, mags, near_pole_indices = near_pole_multiplicity_profile(
            Z, N
        )
        row = tr_M_witness["data"]["per_atom"][name]
        lambda_star, depth_lambda_star, mag_lambda_star = (
            dominant_self_dual_partition(row)
        )
        tr_M = float(row["tr_M"])
        per_atom_data[name] = {
            "Z": Z, "N": N, "A": A, "n": n,
            "k_Hecke": k_hecke,
            "m_max": int(m_max),
            "near_pole_generator_indices": near_pole_indices,
            "per_generator_magnitudes": mags,
            "lambda_star": list(lambda_star) if lambda_star else None,
            "depth_lambda_star": int(depth_lambda_star),
            "lambda_star_yχ_magnitude": float(mag_lambda_star),
            "tr_M": tr_M,
        }
        lambda_str = str(list(lambda_star)) if lambda_star else "(none)"
        print(f"  {name:>10} {A:>3} {n:>3} {k_hecke:>9} {m_max:>6}"
              f" {lambda_str:>14} {depth_lambda_star:>11}"
              f" {mag_lambda_star:>11.5f}")
    print()

    # Compute n_⋆(𝔥) per rule per atom; evaluate scalar tower.
    rules = {
        "R1_mult_shifted":  lambda d: max(1, d["k_Hecke"] - d["m_max"] + 1),
        "R2_mult_truncated": lambda d: max(1, d["k_Hecke"] // max(d["m_max"], 1)),
        "R3_type_b_depth":  lambda d: max(1, d["depth_lambda_star"]),
        "R4_combined":      lambda d: max(
            1, d["depth_lambda_star"] - d["m_max"] + 1
        ),
    }

    print("  Candidate-rule sweep — n_⋆(𝔥) per atom, scalar AND")
    print("  operator-valued (per-eigenvalue) tower forms vs AME:")
    print()
    print(f"  {'rule':<22} {'form':<4} {'atom':>10} {'n_⋆':>4} "
          f"{'tower':>11}  {'B_abs':>9}  {'AME':>7}  {'err_pct':>11}")
    print("  " + "-" * 88)

    results = {}
    for rule_name, rule_fn in rules.items():
        results[rule_name] = {}
        for name, d in per_atom_data.items():
            n_star = int(rule_fn(d))
            Z, N, A = d["Z"], d["N"], d["A"]
            mags = d["per_generator_magnitudes"]
            rho = RHO_MAP[name]
            tr_M_abs = abs(d["tr_M"])
            sigma_val = sigma_3A(A)
            results[rule_name][name] = {"n_star": n_star}
            # Scalar form
            try:
                tower_scalar = sum(phi_q_truncated(m, n_star) for m in mags)
                B_scalar = M_E_MEV * rho * (
                    tr_M_abs + tower_scalar + sigma_val
                )
                err_scalar = 100.0 * (B_scalar - AME[name]) / AME[name]
                results[rule_name][name].update({
                    "tower_scalar": float(tower_scalar),
                    "B_scalar_MeV": float(B_scalar),
                    "err_scalar_pct": float(err_scalar),
                })
                print(f"  {rule_name:<22} scl {name:>10} {n_star:>4} "
                      f"{tower_scalar:>11.3f}  {B_scalar:>9.4f}"
                      f"  {AME[name]:>7.4f}  {err_scalar:>+10.2f}%")
            except PhiQPoleHit as e:
                results[rule_name][name]["scalar_pole_hit"] = str(e)
                print(f"  {rule_name:<22} scl {name:>10} {n_star:>4} "
                      f"-- pole ({e})")
            # Operator-valued (per-eigenvalue) form
            try:
                op_row = tr_M_witness["data"]["per_atom"][name]
                tower_op = tower_op_at_n_star(op_row, n_star)
                B_op = M_E_MEV * rho * (tr_M_abs + tower_op + sigma_val)
                err_op = 100.0 * (B_op - AME[name]) / AME[name]
                results[rule_name][name].update({
                    "tower_op": float(tower_op),
                    "B_op_MeV": float(B_op),
                    "err_op_pct": float(err_op),
                    "ame_close_op_within_threshold": abs(err_op) < THRESHOLD_PCT,
                })
                print(f"  {rule_name:<22} op  {name:>10} {n_star:>4} "
                      f"{tower_op:>11.3f}  {B_op:>9.4f}"
                      f"  {AME[name]:>7.4f}  {err_op:>+10.2f}%")
            except (PhiQPoleHit, OverflowError) as e:
                results[rule_name][name]["op_error"] = str(e)
                print(f"  {rule_name:<22} op  {name:>10} {n_star:>4} "
                      f"-- {e}")
        print()

    # Verdict per rule × form
    print(f"  Verdict per (rule, form) (closure within {THRESHOLD_PCT}% "
          f"across all atoms?):")
    closing_rules = []
    for rule_name, per in results.items():
        for form_key, label in [("err_scalar_pct", "scl"),
                                  ("err_op_pct", "op")]:
            errs = []
            ok = True
            for a in AME:
                v = per[a]
                if form_key not in v:
                    ok = False
                    break
                errs.append(abs(v[form_key]))
            if not ok:
                print(f"    {rule_name:<22} {label}: SKIPPED")
                continue
            max_err = max(errs)
            verdict = "YES" if max_err < THRESHOLD_PCT else f"NO ({max_err:.1f}%)"
            if max_err < THRESHOLD_PCT:
                closing_rules.append(f"{rule_name}/{label}")
            print(f"    {rule_name:<22} {label}: {verdict}")
    print()
    if closing_rules:
        print(f"  CLOSURE achieved by rule(s): {closing_rules}")
        print("  This would refute the n_⋆ refutation chain and support")
        print("  the conjecture's substrate-derived per-atom existence claim.")
    else:
        print("  No rule closes uniformly.  All four substrate-derived")
        print("  multiplicity / Type-B-fold candidates fail the AME")
        print("  light-isotope falsifiability threshold.")
        print("  The conjecture's n_⋆ existence claim is now refuted")
        print("  across every probed family (scalar-eigenvalue uniform-k,")
        print("  scalar ℓ·n_0+k, per-eigenvalue operator-valued uniform-k,")
        print("  and substrate-derived multiplicity / Type-B-fold rules).")

    w = (
        w
        .add_data("per_atom", per_atom_data)
        .add_data("results", results)
        .add_data("closing_rules", closing_rules)
        .add_assertion(
            "no_substrate_rule_closes_within_threshold",
            computed=0 if closing_rules else 1,
            expected=1,
        )
        .add_caveat(
            "depth(λ) = number of cells strictly above the diagonal "
            "is a proxy for full Kashiwara crystal depth on the "
            "Type-B-folded sub-crystal; the rigorous crystal depth "
            "(via BFS on the canonical-basis graph) would refine the "
            "(R3) / (R4) candidates but is heavier compute."
        )
        .add_caveat(
            "Near-pole multiplicity uses scalar |V̂_i(q_0)| from "
            "atom_per_generator_volumes; an alternative formulation "
            "would use per-irrep eigenvalue near-pole counts from "
            "probe-phiq-operator-valued.witness.json."
        )
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
