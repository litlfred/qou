#!/usr/bin/env python3
"""The cut entropy is CONSTANT in A, so it cannot be the binding energy.

Bean qou-6tcn. Extension of `binding_cut_entropy_derived_weightings_probe.py`
from the deuteron to the isotope chain, at the author's request. The result is
decisive and it retires the line.

MEASURED -- one nucleon against the rest, cut `H_3 (x) H_{3(A-1)} < H_{3A}`,
Markov/Plancherel weighting `p = y_lambda f^lambda` (W1, the exact closed form):

    iso    A    n    S_vN        E_0*S_vN    B_AME      ratio
    2H     2    6    1.0359164   4.33633      2.22457   1.9493x
    3H     3    9    1.0359164   4.33633      8.48180   0.5113x
    3He    3    9    1.0359164   4.33633      7.71804   0.5618x
    4He    4   12    1.0359164   4.33633     28.29566   0.1533x
    6Li    6   18    1.0359164   4.33633     31.99399   0.1355x
    7Li    7   21    1.0359164   4.33633     39.24508   0.1105x

`S_vN` is **the same number at every A**, to better than 1e-50 out to n = 24.
`B_AME` is extensive and rises 17.6x across the same range. **A constant cannot
track an extensive quantity**, so the ratio drifts by 17.6x and the deuteron's
1.9493x was a coincidence of its being the smallest binding.

WHY IT IS CONSTANT -- and this is a STRUCTURAL argument, not a fit
=================================================================
The measured marginal is, exactly,

    A_(3)   = [4]_q / [2]_q^3        A_(2,1) = [2]_q / [2]_q^3

which are precisely `y_mu` at **n = 3** -- the closed form
`y_{(n-k,k)} = [n-2k+1]_q/[2]_q^n` evaluated at n = 3. So the one-nucleon
marginal of the n-strand Markov measure IS the 3-strand Markov measure, for
every n.

That is the **Markov property itself**. `prop:markov-trace-frobenius-selection`
defines a Markov trace as "a COMPATIBLE family of linear functionals
tau_n : H_n -> R" satisfying M1 and M3; compatibility is exactly the statement
that restricting `tau_n` to `H_k` gives `tau_k`. A trace with that property has
an n-independent k-strand marginal by construction, so **any** functional of
that marginal -- entropy included -- is n-independent too.

**SCOPE (b), a structural exclusion with a named invariant.** Per the repository
discipline this is not the usual scope-(a) "this construction alone does not
reproduce the numbers": the invariant is the Markov compatibility axiom, it is
definitional rather than fitted, and it forbids ANY closure in which a
fixed-width cut entropy of the Markov measure carries an extensive quantity. It
does NOT exclude entanglement cost as an ingredient of binding; it excludes this
specific object -- the fixed-width marginal's entropy -- from being extensive.

FORMALIZE-FIRST, MISSED
=======================
The one-line argument above predicts the entire table and needed no compute. I
ran the extension first and found the reason afterwards, which is precisely the
failure mode `AGENTS.md` §"Formalize-first probe discipline" exists to prevent:
state the invariant, let it narrow the probe. Recorded so the next agent reads
the invariant before spending the sweep. The Lean statement is
`folio/quantum-observable-universe/lean/QOU/MassTheory/MarkovMarginalConstant.lean`.

CONTROLS
========
This probe carries its own Littlewood-Richardson implementation, so it is only
as good as its controls:

* it reproduces the committed `lr_breakdown_per_lambda` of
  `sublemma-2-1-deuteron-branching.witness.json` exactly -- 35 coefficients,
  0 mismatches, and 0 extra nonzero terms the witness does not list;
* the dimension identity `sum_{mu,nu} c^lambda_{mu,nu} f^mu f^nu = f^lambda`
  holds at every n tested.

The second control **caught a real bug** in this routine during development: a
hard-coded row padding of 10 silently returned wrong coefficients for partitions
with more than 10 rows, which showed up as 2 failures out of 77 at n = 12 and
would not have been visible from the two-row blocks this probe actually uses.
"""

from __future__ import annotations

import json
import pathlib
import sys
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, ame_binding_mev  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)

HERE = pathlib.Path(__file__).resolve().parent
BRANCH = HERE.parent / "sublemma-2-1-deuteron-branching.witness.json"
ISOTOPES = [("2H", 1, 2), ("3H", 1, 3), ("3He", 2, 3),
            ("4He", 2, 4), ("6Li", 3, 6), ("7Li", 3, 7)]


def hook_dim(lam):
    lam = tuple(x for x in lam if x)
    if not lam:
        return 1
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def lr_coeff(lam, mu, nu):
    """c^lam_{mu,nu}: LR skew tableaux of shape lam/mu with content nu.

    Filled in REVERSE reading order (right-to-left, top-to-bottom) so the right
    neighbour and the cell above are already placed when a cell is filled.
    Width is derived, never hard-coded -- a fixed padding silently returns wrong
    coefficients for partitions with more rows than the pad.
    """
    width = max(len(lam), len(mu), sum(nu)) + 2
    L = list(lam) + [0] * width
    M = list(mu) + [0] * width
    nu = [x for x in nu if x]
    if any(M[i] > L[i] for i in range(width)):
        return 0
    cells = [(i, j) for i in range(width) for j in range(M[i], L[i])]
    if len(cells) != sum(nu):
        return 0
    cells.sort(key=lambda c: (c[0], -c[1]))
    k = len(nu)
    state = {"res": 0}
    fill, cnt = {}, [0] * k

    def rec(idx):
        if idx == len(cells):
            state["res"] += 1
            return
        i, j = cells[idx]
        for v in range(1, k + 1):
            if cnt[v - 1] >= nu[v - 1]:
                continue
            if (i, j + 1) in fill and v > fill[(i, j + 1)]:
                continue                                   # rows weakly increase
            if (i - 1, j) in fill and fill[(i - 1, j)] >= v:
                continue                                   # cols strictly increase
            if v > 1 and cnt[v - 2] <= cnt[v - 1]:
                continue                                   # lattice word
            cnt[v - 1] += 1
            fill[(i, j)] = v
            rec(idx + 1)
            del fill[(i, j)]
            cnt[v - 1] -= 1

    rec(0)
    return state["res"]


def two_row(m):
    return [(m,)] + [(m - k, k) for k in range(1, m // 2 + 1)]


def main() -> int:
    wb = WitnessBuilder("cut-entropy-is-A-independent", engine="python-exact")
    wb.set_description(
        "The one-nucleon cut entropy of the Markov/Plancherel measure is the "
        "SAME number at every A (1.0359164340, to <1e-50 out to n=24), because "
        "the one-nucleon marginal of the n-strand Markov measure IS the "
        "3-strand Markov measure -- A_(3) = [4]_q/[2]_q^3 and A_(2,1) = "
        "[2]_q/[2]_q^3 exactly. B_AME is extensive and rises 17.6x over the same "
        "range, so E_0*S_cut cannot be the binding energy and the deuteron's "
        "1.9493x was a coincidence. SCOPE (b): the invariant is the Markov "
        "compatibility axiom, definitional not fitted.")

    q0 = Q_MP
    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))

    def qint(m):
        return (q0 ** m - q0 ** (-m)) / (q0 - 1 / q0)

    # ── CONTROL 1: reproduce the committed deuteron LR breakdown exactly ───
    br = json.loads(BRANCH.read_text())["lr_breakdown_per_lambda"]
    P3_all = [(3,), (2, 1), (1, 1, 1)]
    match = mismatch = extra = 0
    for lam_s, terms in br.items():
        lam = eval(lam_s)                                    # noqa: S307
        seen = set()
        for t in terms:
            seen.add((tuple(t["mu"]), tuple(t["nu"])))
            if lr_coeff(lam, tuple(t["mu"]), tuple(t["nu"])) == t["c"]:
                match += 1
            else:
                mismatch += 1
        for mu in P3_all:
            for nu in P3_all:
                if lr_coeff(lam, mu, nu) and (mu, nu) not in seen:
                    extra += 1

    # ── the sweep ─────────────────────────────────────────────────────────
    rows, marg, dim_ok = [], {}, 0
    for name, Z, A in ISOTOPES:
        n = 3 * A
        blocks, P3, Prest = two_row(n), two_row(3), two_row(n - 3)
        dim_ok += all(
            sum(lr_coeff(l, m, v) * hook_dim(m) * hook_dim(v)
                for m in P3 for v in Prest) == hook_dim(l) for l in blocks)
        p = {l: qint(n - 2 * (l[1] if len(l) > 1 else 0) + 1)
             / qint(2) ** n * hook_dim(l) for l in blocks}
        A_mu = {}
        for l in blocks:
            fl = hook_dim(l)
            for m in P3:
                a = mp.fsum(mp.mpf(lr_coeff(l, m, v) * hook_dim(v)) / fl
                            for v in Prest)
                if a:
                    A_mu[m] = A_mu.get(m, mp.mpf(0)) + p[l] * a
        S = -mp.fsum(hook_dim(m) * A_mu[m] * mp.log(A_mu[m])
                     for m in A_mu if A_mu[m] > 0)
        B = ame_binding_mev(Z, A)
        marg[n] = A_mu
        rows.append({"isotope": name, "Z": Z, "A": A, "n": n,
                     "S_vN": mp.nstr(S, 24),
                     "E0_S_vN_MeV": mp.nstr(E0 * S, 24),
                     "B_AME_MeV": mp.nstr(B, 24),
                     "ratio": mp.nstr(E0 * S / B, 24)})

    S_all = [mp.mpf(r["S_vN"]) for r in rows]
    spread_S = max(S_all) - min(S_all)
    ratios = [mp.mpf(r["ratio"]) for r in rows]
    B_all = [mp.mpf(r["B_AME_MeV"]) for r in rows]
    drift = max(ratios) / min(ratios)
    b_span = max(B_all) / min(B_all)
    m0 = marg[6]
    d_closed = max(abs(m0[(3,)] - qint(4) / qint(2) ** 3),
                   abs(m0[(2, 1)] - qint(2) / qint(2) ** 3))
    d_across = max(max(abs(marg[n][m] - m0[m]) for m in m0) for n in marg)

    print(f"E0 = {mp.nstr(E0, 10)} MeV   cut = 3 | 3(A-1)\n")
    print(f"{'iso':<6}{'A':>2}{'n':>4}{'S_vN':>12}{'E0*S_vN':>10}"
          f"{'B_AME':>10}{'ratio':>9}")
    for r in rows:
        print(f"{r['isotope']:<6}{r['A']:>2}{r['n']:>4}"
              f"{float(mp.mpf(r['S_vN'])):>12.7f}"
              f"{float(mp.mpf(r['E0_S_vN_MeV'])):>10.5f}"
              f"{float(mp.mpf(r['B_AME_MeV'])):>10.5f}"
              f"{float(mp.mpf(r['ratio'])):>8.4f}x")
    print(f"\nS_vN spread across the chain : {mp.nstr(spread_S, 6)}")
    print(f"B_AME spans                  : {mp.nstr(b_span, 6)}x")
    print(f"ratio drifts                 : {mp.nstr(drift, 6)}x")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE RESULT. The entropy does not move at all.
    wb.add_assertion(
        name="cut_entropy_is_constant_across_the_chain",
        computed=mp.nstr(spread_S, 20), expected="0",
        tolerance="1e-40", unit="nats",
        source="max - min of S_vN over 2H, 3H, 3He, 4He, 6Li, 7Li")

    # A2 — THE REASON. The one-nucleon marginal IS the 3-strand Markov measure.
    wb.add_assertion(
        name="one_nucleon_marginal_is_the_three_strand_markov_measure",
        computed=mp.nstr(d_closed, 20), expected="0",
        tolerance="1e-40", unit="dimensionless",
        source="A_(3) vs [4]_q/[2]_q^3 and A_(2,1) vs [2]_q/[2]_q^3")

    # A3 — and it is the same marginal at every n, which is Markov compatibility.
    wb.add_assertion(
        name="marginal_independent_of_n",
        computed=mp.nstr(d_across, 20), expected="0",
        tolerance="1e-40", unit="dimensionless",
        source="max |A_mu(n) - A_mu(6)| over n = 6, 9, 12, 18, 21")

    # A4 — CONTROL against the vacuous reading "everything here is constant":
    #      the TARGET is emphatically not.
    wb.add_assertion(
        name="control_binding_is_extensive",
        computed=mp.nstr(b_span, 20), expected="17.6417",
        tolerance="1e-3", unit="ratio",
        source="B_AME(7Li) / B_AME(2H)")

    # A5 — so the ratio drifts, and the deuteron's near-2 does not survive.
    wb.add_assertion(
        name="ratio_drifts_across_the_chain",
        computed=mp.nstr(drift, 20), expected="17.6417",
        tolerance="1e-3", unit="ratio",
        source="max/min of E_0*S_vN / B_AME")

    # A6 — CONTROL on this probe's own LR implementation: exact agreement with
    #      the committed witness, with no coefficient invented and none missed.
    wb.add_assertion(
        name="control_lr_matches_committed_witness",
        computed=str(match), expected="35", tolerance="0", unit="count",
        source="lr_breakdown_per_lambda of sublemma-2-1-deuteron-branching")
    wb.add_assertion(
        name="control_lr_has_no_mismatch_or_extra_terms",
        computed=str(mismatch + extra), expected="0", tolerance="0",
        unit="count",
        source="mismatched coefficients plus nonzero terms the witness omits")

    # A7 — CONTROL: the dimension identity at every n in the sweep. This is the
    #      control that caught a real padding bug in lr_coeff during development.
    wb.add_assertion(
        name="control_dimension_identity_at_every_n",
        computed=str(dim_ok), expected=str(len(ISOTOPES)), tolerance="0",
        unit="count",
        source="sum c^lambda_{mu,nu} f^mu f^nu = f^lambda over the two-row blocks")

    wb.add_data("E0_MeV", mp.nstr(E0, 30))
    wb.add_data("q0_pin", "proton")
    wb.add_data("cut", "H_3 (x) H_{3(A-1)} < H_{3A}  (one nucleon vs the rest)")
    wb.add_data("weighting", "W1 Markov/Plancherel p = y_lambda f^lambda")
    wb.add_data("rows", rows)
    wb.add_data("constant_S_vN", mp.nstr(S_all[0], 30))
    wb.add_data("constant_E0_S_vN_MeV", mp.nstr(E0 * S_all[0], 30))
    wb.add_data("marginal_closed_form",
                {"A_(3)": mp.nstr(qint(4) / qint(2) ** 3, 30),
                 "A_(2,1)": mp.nstr(qint(2) / qint(2) ** 3, 30)})
    wb.add_caveat(
        "SCOPE (b) -- a structural exclusion with a named invariant, not the "
        "usual scope-(a) negative. The invariant is Markov compatibility (M1+M3 "
        "on the tower), which is definitional rather than fitted: a compatible "
        "family has an n-independent k-strand marginal by construction, so any "
        "functional of that marginal is n-independent. Lean: "
        "QOU.MassTheory.MarkovMarginalConstant.")
    wb.add_caveat(
        "What is excluded is THIS OBJECT -- the entropy of a fixed-width "
        "marginal of the Markov measure -- from carrying an extensive quantity. "
        "Entanglement cost is NOT excluded as an ingredient of binding, and a "
        "cut whose width GROWS with A is untouched by this argument.")
    wb.add_caveat(
        "FORMALIZE-FIRST, MISSED. The structural argument predicts the whole "
        "table and needed no compute; the sweep was run first and the reason "
        "found afterwards. Recorded per AGENTS.md so the next agent reads the "
        "invariant before spending the sweep.")
    wb.add_caveat(
        "This probe carries its own LR implementation. Its controls caught a "
        "real bug during development -- a hard-coded row padding of 10 returned "
        "wrong coefficients for partitions with >10 rows (2 of 77 failures at "
        "n=12), invisible from the two-row blocks actually used here.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
