#!/usr/bin/env python3
"""Nothing destroys entanglement: the sign is forced, so the committed probe
is not measuring entanglement.

Bean qou-6tcn. Raised by the author against the result I relayed from
`binding_von_neumann_entropy_probe.py` -- that binding "destroys" block
entanglement (dS < 0 at 2H and 3H). The objection is right, and it is stronger
than a complaint about a sign.

TWO REASONS THAT NUMBER CANNOT BE AN ENTANGLEMENT ENTROPY
=========================================================
1. **Unitarity.** For a closed process in which the same particles come back --
   virtual production and annihilation being the clean case -- the global state
   stays pure, so its von Neumann entropy is identically 0 and CANNOT change.
   Any quantity that moves under such a process is not the global entropy.
2. **Positivity across a cut.** Entanglement entropy is only defined once a
   bipartition is named. Across any cut, a product state has S_A = 0 and every
   state has S_A >= 0. So for binding -- free nucleons are a product across the
   proton|neutron cut -- dS = S_bound - 0 >= 0 IDENTICALLY. It is a theorem,
   not a measurement.

WHAT THE COMMITTED PROBE ACTUALLY COMPUTES
==========================================
`block_entropy` is `-sum_lambda p_lambda ln p_lambda` with
`p_lambda ~ W_lambda ||rho_lambda(beta)||_F^2`. There is no bipartition, no
partial trace and no reduced density matrix anywhere in it: it is the SHANNON
entropy of a classical distribution over the Wedderburn blocks of the WHOLE
algebra -- a measure of how spread a braid's character is across irreps. That
is a real quantity and its numbers are not in dispute. It is simply not an
entanglement entropy, and the label "von Neumann entanglement entropy" on it is
wrong. Its dS < 0 is the proof: no bipartite entanglement measure can do that.

I relayed that label without checking it. This probe does not re-run the
committed probe or dispute its arithmetic; it establishes the sign theorem the
committed number violates, and identifies the object that does satisfy it.

THE RIGHT CUT IS ALREADY IN THE CORPUS
======================================
The natural bipartition for binding is proton strands | neutron strands, i.e.
the subalgebra `H_3 (x) H_3 subset H_6`. Restriction along it is Frobenius
reciprocity and its multiplicities are Littlewood-Richardson -- and
`sublemma-2-1-deuteron-branching.witness.json` already carries them, per
`lambda`, as `lr_breakdown_per_lambda`. That witness also records
`max_relative_diff_no_interface = 1.98e-70`: the DISJOINT (free) character
matches the LR prediction to seventy digits, so the free state is exactly the
induced product across this cut -- which is what makes its cut entropy zero and
the sign theorem bite.

MEASURED (exact integer arithmetic; no q, no float64)
=====================================================
For a state maximally mixed in H_6 block `lambda`, the reduced weights on the
cut are `p^lambda_{mu,nu} = c^lambda_{mu,nu} f^mu f^nu / f^lambda`:

    lambda            f^lam   S_cut (nats)
    (6)                   1     0.000000     <- restricts to ONE (mu,nu): product
    (5,1)                 5     1.054920
    (4,2)                 9     1.273028
    (4,1,1)              10     1.470808     <- max
    (3,3)                 5     0.500402
    (3,2,1)              16     1.386294
    (3,1,1,1)            10     1.470808
    (2,2,2)               5     0.500402
    (2,2,1,1)             9     1.273028
    (2,1,1,1,1)           5     1.054920
    (1^6)                 1     0.000000     <- the other product block

Non-negative on all eleven, exactly zero on exactly the two one-dimensional
blocks, and invariant under conjugation `lambda -> lambda'` on all eleven.

SCOPE -- (a) throughout
=======================
MEASURED: the cut entropies above and their non-negativity; the dimension
identity `sum c^lambda_{mu,nu} f^mu f^nu = f^lambda` as a control; the
conjugation symmetry; that the committed probe reports dS < 0 for two of three
isotopes.

NOT claimed: that `E_0 * S_cut` is the binding energy, or that this cut entropy
appears in any binding formula. In particular the value AME would require of it
lies INSIDE the measured range, and that is NOT evidence -- a weighting over
eleven blocks spanning [0, 1.4708] can be made to hit almost anything in that
interval, so "it is in range" is a genericity observation, not a result. No
weighting is chosen here and no binding contribution is computed. Nor is
entanglement cost claimed to be excluded as an ingredient: the earlier probe
refutes ONE prescription, and this one refutes that prescription's LABEL.
"""

from __future__ import annotations

import json
import pathlib
import sys
from fractions import Fraction
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)

HERE = pathlib.Path(__file__).resolve().parent
BRANCH = HERE.parent / "sublemma-2-1-deuteron-branching.witness.json"
VN = HERE.parent / "probes" / "binding-von-neumann-entropy-test.witness.json"


def hook_dim(lam):
    lam = tuple(lam)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def conjugate(lam):
    lam = tuple(lam)
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0]))


def main() -> int:
    wb = WitnessBuilder("binding-cut-entropy-sign-is-forced",
                        engine="python-exact")
    wb.set_description(
        "Across the proton|neutron cut H_3 (x) H_3 < H_6 the free state is a "
        "product (S=0) and every state has S >= 0, so dS >= 0 is a THEOREM. "
        "Measured exactly: the per-block cut entropy is non-negative on all 11 "
        "blocks, zero on exactly the two one-dimensional ones, and conjugation "
        "invariant. The committed binding_von_neumann_entropy_probe reports "
        "dS < 0 for 2 of 3 isotopes, so its quantity -- a Shannon entropy over "
        "Wedderburn blocks of the whole algebra, with no bipartition, no "
        "partial trace and no reduced density matrix -- is not an entanglement "
        "entropy and its 'von Neumann entanglement' label is wrong.")

    br = json.loads(BRANCH.read_text())
    lr = br["lr_breakdown_per_lambda"]

    rows, dim_ok = {}, 0
    for lam_s, terms in lr.items():
        lam = eval(lam_s)  # noqa: S307 -- our own witness's key format
        f_lam = hook_dim(lam)
        wts = [t["c"] * hook_dim(t["mu"]) * hook_dim(t["nu"]) for t in terms]
        tot = sum(wts)
        dim_ok += (tot == f_lam)
        S = -mp.fsum(mp.mpf(x) / tot * mp.log(mp.mpf(x) / tot)
                     for x in wts if x)
        rows[lam_s] = {"f_lambda": f_lam, "n_cut_terms": len(terms),
                       "sum_c_f_f": tot, "S_cut": mp.nstr(S, 24)}

    S = {k: mp.mpf(v["S_cut"]) for k, v in rows.items()}
    ZERO = mp.mpf("1e-30")
    nonneg = sum(1 for v in S.values() if v >= -ZERO)
    exact_zero = [k for k, v in S.items() if abs(v) <= ZERO]
    strictly_pos = [k for k, v in S.items() if v > ZERO]
    conj_ok = sum(1 for k in S
                  if abs(S[k] - S[str(conjugate(eval(k)))]) <= ZERO)  # noqa: S307
    s_max = max(S.values())

    vn = json.loads(VN.read_text())["data"]["rows"]
    neg_dS = sum(1 for r in vn if r["dS"] < 0)

    print(f"{'lambda':<20}{'f^lam':>6}{'terms':>7}{'S_cut (nats)':>15}")
    for k, v in rows.items():
        print(f"{k:<20}{v['f_lambda']:>6}{v['n_cut_terms']:>7}"
              f"{float(mp.mpf(v['S_cut'])):>15.6f}")
    print(f"\nnon-negative: {nonneg}/11   exactly zero: {exact_zero}")
    print(f"conjugation-symmetric: {conj_ok}/11   max S_cut = "
          f"{mp.nstr(s_max, 10)}")
    print(f"committed probe rows with dS < 0: {neg_dS}/3")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE SIGN THEOREM, block by block.
    wb.add_assertion(
        name="cut_entropy_nonnegative_on_every_block",
        computed=str(nonneg), expected="11", tolerance="0", unit="count",
        source="S_cut(lambda) over the H_3 (x) H_3 < H_6 bipartition")

    # A2 — CONTROL. The LR weights really are the restriction: dimensions match.
    wb.add_assertion(
        name="control_restriction_preserves_dimension",
        computed=str(dim_ok), expected="11", tolerance="0", unit="count",
        source="sum_{mu,nu} c^lambda_{mu,nu} f^mu f^nu = f^lambda")

    # A3 — zero exactly where the block restricts to a single (mu,nu).
    wb.add_assertion(
        name="product_blocks_have_exactly_zero_cut_entropy",
        computed=str(len(exact_zero)), expected="2", tolerance="0",
        unit="count",
        source="the one-dimensional blocks (6) and (1^6)")

    # A4 — CONTROL against the vacuous reading "the cut entropy is just zero".
    wb.add_assertion(
        name="control_cut_entropy_strictly_positive_elsewhere",
        computed=str(len(strictly_pos)), expected="9", tolerance="0",
        unit="count",
        source="the other nine blocks of H_6")

    # A5 — CONTROL that the table is not degenerate: a specific max value.
    wb.add_assertion(
        name="control_max_cut_entropy_value",
        computed=mp.nstr(s_max, 20), expected="1.4708084763",
        tolerance="1e-8", unit="nats",
        source="attained at (4,1,1) and its conjugate (3,1,1,1)")

    # A6 — conjugation is a symmetry of the cut, on all eleven.
    wb.add_assertion(
        name="cut_entropy_invariant_under_conjugation",
        computed=str(conj_ok), expected="11", tolerance="0", unit="count",
        source="S_cut(lambda) = S_cut(lambda') block by block")

    # A7 — THE REFUTATION OF THE LABEL. A bipartite measure cannot do this.
    wb.add_assertion(
        name="committed_probe_reports_negative_delta_S",
        computed=str(neg_dS), expected="2", tolerance="0", unit="count",
        source="binding-von-neumann-entropy-test rows with dS < 0 (2H, 3H)")

    # A8 — CONTROL for A7's premise: the free state IS the product across this
    #      cut, so its cut entropy is zero and dS >= 0 genuinely applies.
    wb.add_assertion(
        name="control_free_state_is_the_induced_product",
        computed=mp.nstr(mp.mpf(br["max_relative_diff_no_interface"]), 20),
        expected="0", tolerance="1e-60", unit="dimensionless",
        source="disjoint character vs LR prediction, "
               "sublemma-2-1-deuteron-branching")

    wb.add_data("cut", "H_3 (x) H_3 < H_6 (proton strands | neutron strands)")
    wb.add_data("per_block", rows)
    wb.add_data("zero_cut_entropy_blocks", exact_zero)
    wb.add_data("max_cut_entropy", mp.nstr(s_max, 30))
    wb.add_caveat(
        "Scope (a). Establishes that dS >= 0 is forced across any bipartition, "
        "hence that the committed probe's quantity is not an entanglement "
        "entropy -- it is a Shannon entropy over Wedderburn blocks of the whole "
        "algebra. That probe's arithmetic is not disputed and is not re-run; "
        "only its LABEL is refuted, and I relayed that label without checking "
        "it.")
    wb.add_caveat(
        "NOT claimed: that E_0 * S_cut is the binding energy, or that this cut "
        "entropy appears in any binding formula. The value AME would require "
        "lies inside the measured range [0, 1.4708], and that is a GENERICITY "
        "observation rather than evidence -- a weighting over eleven blocks "
        "spanning that interval can be made to hit almost anything in it. No "
        "weighting is chosen and no binding contribution is computed.")
    wb.add_caveat(
        "Entanglement cost is NOT excluded as an ingredient. The earlier probe "
        "refutes one prescription; this one refutes that prescription's label. "
        "Neither bears on whether a correctly-defined cut entropy plays a role.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
