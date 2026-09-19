#!/usr/bin/env python3
"""deuteron_block_measure_entangled_support_probe.py — the q-distribution the picture presupposes
already exists, and the deuteron's entangled block set is the convention-D two-row support.

Bean `qou-jfx8` / session `qou-0nrt` (owner, 2026-09-16): *"we should [put] a q-distribution on
phase space according to the weights of the LP-dual shadow [prices]"*. Before any new object is
built, measure what the corpus already carries on **committed data only**:

  1. The Markov block measure `P(λ) := y_λ(q₀) · f^λ` on `Λ₆ = {λ ⊢ 6}`, with `y_λ` the
     convention-D Frobenius-pairing weight at the proton pin (`y-lambda-at-q0.witness.json`) and
     `f^λ` the classical dimension (hook-length formula, exact integer). `∑_λ P(λ) = 1` is Markov
     axiom M1 read through the pairing (`QOU.MassTheory.BlockMeasure.blockMass_sum_eq_one`,
     sorry-free); this probe checks the committed numbers satisfy it, and that every non-zero
     mass is positive (positivity is a *hypothesis* in the Lean, `IsProbability`).
  2. The deuteron's **entangled support** `{λ : χ_λ(atom) ≠ χ_λ(free)}` from
     `atom-chi-rust-d.witness.json` (`χ_λ` of the bound word and of the free constituent product,
     both in `H_6`, MPFR 50 dps), and its convention-D-weighted restriction
     `{λ : y_λ ≠ 0 ∧ χ_λ(atom) ≠ χ_λ(free)}`. The Lean `trM_eq_of_entangledSupp_empty` says an
     empty weighted set forces `tr_M(atom) = tr_M(free)` and hence zero logarithmic binding; this
     measures that the set is **not** empty, and by how much per block.
  3. The LP-dual `y*` of `deuteron-real-sdp.witness.json` per block, beside `P(λ)`: the two
     candidate "weightings of the directions" are compared by **rank**, not fitted.

What is and is not shown. Shown: the normalisation and positivity of `P` on committed data; the
weighted entangled support is exactly the four two-row blocks `(6), (5,1), (4,2), (3,3)`; the
free→bound displacement `y_λ(χ_λ(atom) − χ_λ(free))` is dominated by `(5,1)`; the LP-dual `y*`
and `P` rank the four two-row blocks in nearly opposite order. Not shown: that either weighting
is *the* q-distribution of the owner's picture, any binding number, any selection of `K`.

No fit, no `B_AME`, no q₀ arithmetic (q₀ enters only through the committed `y_λ(q₀)` strings).
Arithmetic: `mpmath` at 60 dps on the witnesses' own 50-dps decimal strings; `f^λ` exact in ℤ.
The LP-dual `y*` values are float64 **in the source witness** (Clarabel output) and are used
only for a rank comparison, never in arithmetic.

-- Ref: [manuscript] prop:frobenius-pairing; def:markov-axioms-primitive;
   QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean; bean qou-jfx8
"""
from __future__ import annotations

import json
import sys
from math import factorial  # float64-ok: exact arbitrary-precision int (hook-length count f^λ, lines below use // and %), never a float
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(REPO / "computations"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60

Y_WITNESS = REPO / "computations" / "y-lambda-at-q0.witness.json"
CHI_WITNESS = REPO / "computations" / "atom-chi-rust-d.witness.json"
LP_WITNESS = REPO / "computations" / "deuteron-real-sdp.witness.json"


def hook_dim(lam: tuple[int, ...]) -> int:
    """Number of standard Young tableaux of shape `lam` (hook-length formula), exact."""
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j - 1) + (conj[j] - i - 1) + 1
    assert factorial(n) % prod == 0
    return factorial(n) // prod


def parse_partition(p: str) -> tuple[int, ...]:
    return tuple(int(x) for x in p.strip("()").rstrip(",").split(",") if x.strip())


def main() -> int:
    Y = json.loads(Y_WITNESS.read_text(encoding="utf-8"))
    C = json.loads(CHI_WITNESS.read_text(encoding="utf-8"))
    D = json.loads(LP_WITNESS.read_text(encoding="utf-8"))
    assert Y["q0Anchor"] == "proton", "the y_λ cache must be the proton-pinned one"

    y = {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"]) for e in Y["data"]["by_n"]["6"]}
    chi_atom = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in C["data"]["atom"]["by_partition"]}
    chi_free = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in C["data"]["free"]["by_partition"]}
    parts = [parse_partition(p) for p in D["data"]["partitions"]]
    ystar = {parts[i]: str(D["data"]["lp"]["y_star"][i]) for i in range(len(parts))}
    assert set(parts) == set(y) == set(chi_atom) == set(chi_free), "the three witnesses index the same blocks"

    rows = []
    total = mp.mpf(0)
    tr_atom = mp.mpf(0)
    tr_free = mp.mpf(0)
    print(f"{'λ':<16}{'f^λ':>4}{'y_λ (D, proton)':>18}{'P = y·f':>14}{'χ_atom':>12}{'χ_free':>12}{'y(χA−χF)':>14}{'LP y*':>9}")
    for lam in parts:
        f = hook_dim(lam)
        P = y[lam] * f
        total += P
        disp = y[lam] * (chi_atom[lam] - chi_free[lam])
        tr_atom += y[lam] * chi_atom[lam]
        tr_free += y[lam] * chi_free[lam]
        rows.append({
            "partition": list(lam), "f_lambda": f,
            "y_lambda": mp.nstr(y[lam], 50), "P": mp.nstr(P, 50),
            "chi_atom": mp.nstr(chi_atom[lam], 50), "chi_free": mp.nstr(chi_free[lam], 50),
            "displacement_y_times_chi_diff": mp.nstr(disp, 50),
            "chi_differs": bool(chi_atom[lam] != chi_free[lam]),
            "in_weighted_entangled_support": bool(y[lam] != 0 and chi_atom[lam] != chi_free[lam]),
            "lp_dual_y_star_float64_source": ystar[lam],
            "weight_family": "markov_y_lambda_convention_D",
        })
        print(f"{str(lam):<16}{f:>4}{mp.nstr(y[lam], 10):>18}{mp.nstr(P, 10):>14}{mp.nstr(chi_atom[lam], 8):>12}"
              f"{mp.nstr(chi_free[lam], 8):>12}{mp.nstr(disp, 8):>14}{ystar[lam][:7]:>9}")

    two_row = [r for r in rows if len(r["partition"]) <= 2]
    weighted_support = [tuple(r["partition"]) for r in rows if r["in_weighted_entangled_support"]]
    raw_support_count = sum(1 for r in rows if r["chi_differs"])
    disp_abs = {tuple(r["partition"]): abs(mp.mpf(r["displacement_y_times_chi_diff"])) for r in rows}
    dominant = max(disp_abs, key=disp_abs.get)
    rank_P = sorted((tuple(r["partition"]) for r in two_row), key=lambda l: -mp.mpf(next(x["P"] for x in rows if tuple(x["partition"]) == l)))
    rank_ystar = sorted((tuple(r["partition"]) for r in two_row), key=lambda l: -mp.mpf(ystar[l]))
    print()
    print("Σ_λ P(λ)            =", mp.nstr(total, 40))
    print("weighted entangled support:", weighted_support, f"(raw χ-differs: {raw_support_count}/{len(rows)})")
    print("dominant displacement block:", dominant, "=", mp.nstr(disp_abs[dominant], 12))
    print("rank by P            :", rank_P)
    print("rank by LP-dual y*   :", rank_ystar)
    print("tr_M(atom) = Σ yχ    =", mp.nstr(tr_atom, 25), "| tr_M(free) =", mp.nstr(tr_free, 25),
          "| ratio", mp.nstr(tr_atom / tr_free, 20))
    print("deuteron-real-sdp tr_M_beta_D (as recorded):", D["data"].get("tr_M_beta_D"))

    checks = [
        ("block_measure_sums_to_one_to_50dps", abs(total - 1) < mp.mpf("1e-48"),
         "Σ_λ y_λ f^λ over λ ⊢ 6 from y-lambda-at-q0.witness.json (Lean: blockMass_sum_eq_one)"),
        ("nonzero_masses_are_positive", all(mp.mpf(r["P"]) > 0 for r in two_row) and all(mp.mpf(r["P"]) == 0 for r in rows if len(r["partition"]) > 2),
         "convention D: two-row masses > 0, ≥3-row masses = 0 (TwoRowCapDerived)"),
        ("weighted_entangled_support_is_two_row_support", set(weighted_support) == {(6,), (5, 1), (4, 2), (3, 3)},
         "atom-chi-rust-d.witness.json: χ differs on all 11 blocks; weighted by y_λ only the four two-row blocks survive"),
        ("entangled_support_nonempty_so_binding_form_nonzero_is_permitted", len(weighted_support) > 0,
         "contrapositive of trM_eq_of_entangledSupp_empty"),
        ("displacement_dominated_by_5_1", dominant == (5, 1),
         "|y_λ(χ_atom − χ_free)| is largest on (5,1)"),
        ("lp_dual_and_block_measure_rank_two_row_blocks_differently", rank_P != rank_ystar,
         "P ranks (4,2) > (5,1) > (6) > (3,3); deuteron-real-sdp y* ranks (6) > (3,3) > (5,1) > (4,2)"),
    ]
    ok_all = True
    w = WitnessBuilder("deuteron-block-measure-entangled-support", engine="mpmath")
    for name, ok, src in checks:
        ok_all &= bool(ok)
        print(f"  [{'ok' if ok else 'FAIL'}] {name}")
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save(
        {
            "q0Anchor": "proton",
            "q0_anchor_reason": "y_λ read from the proton-pinned y-lambda-at-q0 cache; no q₀ arithmetic here",
            "description": (
                "PROBE (bean qou-jfx8): the convention-D Markov block measure P(λ)=y_λ f^λ on H_6 at the "
                "proton pin sums to 1 and is positive on the two-row blocks; the deuteron's y-weighted "
                "entangled support {λ: y_λ≠0, χ_λ(atom)≠χ_λ(free)} is exactly the four two-row blocks, "
                "dominated by (5,1); the LP-dual y* of deuteron-real-sdp ranks those blocks in nearly the "
                "opposite order to P. Committed inputs only; nothing fitted; nothing wired."
            ),
            "inputs": {
                "y_lambda": str(Y_WITNESS.name), "chi": str(CHI_WITNESS.name), "lp_dual": str(LP_WITNESS.name),
                "chi_witness_q0Anchor_recorded": C.get("q0Anchor"),
                "chi_witness_computedAt": C.get("computedAt"),
            },
            "weight_family": "markov_y_lambda_convention_D",
            "rows": rows,
            "sum_P": mp.nstr(total, 50),
            "weighted_entangled_support": [list(l) for l in weighted_support],
            "raw_chi_differs_count": raw_support_count,
            "dominant_displacement_block": list(dominant),
            "rank_by_P": [list(l) for l in rank_P],
            "rank_by_lp_dual_y_star": [list(l) for l in rank_ystar],
            "tr_M_atom_from_pairing": mp.nstr(tr_atom, 50),
            "tr_M_free_from_pairing": mp.nstr(tr_free, 50),
            # quoted, not computed: the LP witness stores this as float64; kept as its own repr string
            "deuteron_real_sdp_tr_M_beta_D_as_recorded_float64_source_str": repr(D["data"].get("tr_M_beta_D")),
            "caveats": [
                "atom-chi-rust-d.witness.json records no q0Anchor field. Its y-weighted trace 0.15197 differs from "
                "deuteron-real-sdp's recorded tr_M_beta_D 0.57517; BOTH witnesses were last regenerated in the same "
                "commit 870c65d84b (2026-09-15), so this is NOT an element-generation dating artifact. Which element "
                "or normalisation deuteron_real_sdp traces is NOT adjudicated here.",
                "LP-dual y* is float64 in its source witness; used for rank only.",
            ],
        }
    )
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
