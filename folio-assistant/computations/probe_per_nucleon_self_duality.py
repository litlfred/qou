#!/usr/bin/env python3
"""Probe — categorical magic via shell-self-duality at PER-NUCLEON level.

Earlier `probe_atom_shell_self_duality.py` falsified the conjecture
that Z=N atoms are shell-self-dual at the FULL atom level (H_{3A}).
This probe restricts the test to the per-nucleon sub-tower (H_3),
testing whether each nucleon's intra braid is shell-self-dual.

For each nucleon flavor (proton uud, neutron udd):

  1. Build the intra braid (per `nucleon_gen_chains` in `hecke_core.py`)
  2. For every partition pair (λ, λ*) of H_3:
     (3), (1,1,1) — extreme pair
     (2,1) — self-conjugate
  3. Compute χ_λ and χ_{λ*} via Hoefsmit at q_0
  4. Test x_λ = x_{λ*} (categorical magic at sub-tower level)

If proton or neutron is shell-self-dual at H_3, that supplies the
categorical condition for "magic" — at the sub-tower level rather
than the atom level. Atoms inheriting this self-duality through
their intra structure would then be magic in a derived sense.

NO Vol_hyp.  NO knot identification.  NO census search.

Output: probe-per-nucleon-self-duality.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np

from experimental_constants import M_E_MEV
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1, partitions_of, q_factorial, q_int
from light_isotope_sweep import chi_lambda_numeric, dim_q
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder


def transpose_partition(shape):
    if not shape:
        return ()
    n_cols = max(shape)
    return tuple(
        sum(1 for part in shape if part > col)
        for col in range(n_cols)
    )


def nucleon_crossings_h3(g0_chain, g1_chain):
    """Build a (gen_idx, cross_type) sequence for H_3 from per-gen chains.

    `_PROTON_G0`/`_NEUTRON_G0` etc. are lists of (c, d) tuples.
    The Hoefsmit pipeline `chi_lambda_numeric` takes (gen_idx, type) where
    type ∈ {"sigma", "sigma_inv", "averaged"} for (c, d) ∈ {(1,0), (1,-h), (1,-h/2)}.
    """
    h_val = Q_0 - 1.0 / Q_0
    crossings = []
    for c, d in g0_chain:
        if abs(d) < 1e-12:
            crossings.append((0, "sigma"))
        elif abs(d - (-h_val)) < 1e-12:
            crossings.append((0, "sigma_inv"))
        elif abs(d - (-h_val / 2)) < 1e-12:
            crossings.append((0, "averaged"))
        else:
            return None
    for c, d in g1_chain:
        if abs(d) < 1e-12:
            crossings.append((1, "sigma"))
        elif abs(d - (-h_val)) < 1e-12:
            crossings.append((1, "sigma_inv"))
        elif abs(d - (-h_val / 2)) < 1e-12:
            crossings.append((1, "averaged"))
        else:
            return None
    return crossings


def test_nucleon_self_duality(name, crossings):
    """Test x_λ(β) = x_{λ*}(β) for all (λ, λ*) of H_3."""
    if crossings is None:
        return None, None
    rows = []
    seen = set()
    nfac = q_factorial(3)
    tr_M = 0.0
    self_conj = 0
    pair_dual = 0
    not_dual = 0
    for shape in partitions_of(3):
        shape_star = transpose_partition(shape)
        try:
            chi, d = chi_lambda_numeric(shape, crossings)
        except Exception:
            continue
        if d == 0:
            continue
        d_q = float(dim_q(shape))
        y_lambda = float(d_q ** 2 / nfac)
        tr_M += y_lambda * chi / d
        is_self_conj = (shape == shape_star)
        if is_self_conj:
            chi_star = chi
        else:
            try:
                chi_star, _ = chi_lambda_numeric(shape_star, crossings)
            except Exception:
                continue
        sorted_pair = tuple(sorted([shape, shape_star]))
        if sorted_pair in seen:
            continue
        seen.add(sorted_pair)
        equal = abs(chi - chi_star) < 1e-9
        ratio = chi / chi_star if chi_star != 0 else None
        if is_self_conj:
            self_conj += 1
        elif equal:
            pair_dual += 1
        else:
            not_dual += 1
        rows.append({
            "shape": list(shape), "shape_star": list(shape_star),
            "is_self_conjugate": is_self_conj, "dim": d,
            "chi_lambda": chi, "chi_lambda_star": chi_star,
            "y_lambda": y_lambda, "equal_within_1e-9": equal,
            "ratio_chi_to_chi_star": ratio,
        })
    summary = {
        "n_strands": 3,
        "n_pairs_examined": len(rows),
        "self_conjugate_count": self_conj,
        "pair_dual_count": pair_dual,
        "not_dual_count": not_dual,
        "all_dual": (not_dual == 0),
        "tr_M_at_q0": tr_M,
    }
    return rows, summary


def main():
    print("=" * 78)
    print("Probe — per-nucleon shell-self-duality (H_3 sub-tower)")
    print("=" * 78)
    print(f"q_0 = {Q_0}")
    print()

    nucleons = [
        ("proton (uud)", _PROTON_G0, _PROTON_G1),
        ("neutron (udd)", _NEUTRON_G0, _NEUTRON_G1),
    ]
    out_nucleons = []
    for name, g0, g1 in nucleons:
        print(f"━━ {name}")
        crossings = nucleon_crossings_h3(g0, g1)
        if crossings is None:
            print("    SKIP: chain has unrecognised (c, d)")
            continue
        rows, summary = test_nucleon_self_duality(name, crossings)
        print(f"    {summary['n_pairs_examined']} (λ, λ*) pairs examined")
        print(f"    self-conjugate (λ = λ*):  {summary['self_conjugate_count']}")
        print(f"    dual-pair (χ_λ = χ_{{λ*}}): {summary['pair_dual_count']}")
        print(f"    NOT dual:                  {summary['not_dual_count']}")
        print(f"    all-dual (= categorically magic at H_3): {summary['all_dual']}")
        print(f"    tr_M(β) at q_0 = {summary['tr_M_at_q0']:+.6f}")
        for r in rows:
            sym_marker = "*" if r["is_self_conjugate"] else " "
            equal_marker = "✓" if r["equal_within_1e-9"] else "✗"
            shape_str = str(r['shape'])
            shape_star_str = str(r['shape_star'])
            print(f"      {sym_marker} λ={shape_str:<12} λ*={shape_star_str:<12} "
                  f"d={r['dim']} χ={r['chi_lambda']:>+.4f} χ*={r['chi_lambda_star']:>+.4f} "
                  f"{equal_marker}")
        print()
        out_nucleons.append({
            "name": name, "summary": summary, "rows": rows,
        })

    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for n in out_nucleons:
        verdict = "✓ MAGIC at H_3" if n["summary"]["all_dual"] else "✗ not magic at H_3"
        print(f"  {n['name']}: {verdict}")
    print()

    # Witness
    w = (
        WitnessBuilder("probe-per-nucleon-self-duality", engine="python")
        .set_description(
            "Per-nucleon shell-self-duality probe at H_3. Tests whether "
            "proton (uud) and neutron (udd) intra braids satisfy "
            "χ_λ(β) = χ_{λ*}(β) on every Wedderburn pair of H_3. "
            "Sub-tower complement to probe-atom-shell-self-duality (which "
            "tested at H_{3A} and falsified the atom-level conjecture). "
            "If individual nucleons are self-dual at H_3, this gives "
            "the categorical magic condition at the sub-tower level."
        )
        .set_content_block("prop:shell-schur-weyl-self-duality")
        .add_parameter("q_0", Q_0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("nucleons", out_nucleons)
        .add_caveat(
            "H_3 has only 3 partitions: (3), (2,1), (1,1,1). The "
            "self-conjugate one is (2,1); the extreme pair is "
            "((3), (1,1,1)). Pass criterion: the extreme pair "
            "satisfies χ_(3) = χ_(1,1,1). Per the chi-sym-alt theorem "
            "their PRODUCT is closed-form, but EQUALITY is a stronger "
            "(non-theorem) condition tested empirically here."
        )
    )
    out_path = w.save()
    print(f"Witness: {out_path.name}")


if __name__ == "__main__":
    main()
