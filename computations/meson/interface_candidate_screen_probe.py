#!/usr/bin/env python3
"""Interface candidates crossing the wall >= 2 times: a SCREEN, and no selection.

Bean qou-6tcn. Addendum 28 showed the atom word is a connected sum because each
block wall is crossed exactly once, and located the change in the interface `I`
of `conj:confinement-nf-structure-forcing`'s `beta = beta_1 * I * beta_2`. This
screens five candidate interfaces at the deuteron wall.

**It selects none of them, and the reason is the point of the probe.**

MEASURED (deuteron, wall sigma_3, interface slot at index 11 of 23)
==================================================================
    candidate                          xings  prov.#?  tr_M(atom)  vs sqrt(AME)
    I1  s3                (current)        1     True   0.693389      0.4649x
    I2  s3 s2 s4 s3       (2-block)        2    False   0.417642      0.2800x
    I3  s3 s3             (clasp)          2    False   1.276677      0.8560x
    I4  s2 s3 s4          (fan)            1     True   0.328149      0.2200x
    I5  (s3 s2 s4 s3)^2   (doubled)        4    False   1.860693      1.2475x

THREE FINDINGS, AND A REFUSAL
=============================
1. **The trace is NOT monotone in wall crossings.** `I2` crosses the wall twice
   and traces *lower* than `I1`, which crosses once. So "more threading gives a
   bigger trace" is false, and a crossing count cannot be used as a proxy for
   the objective.
2. **`I4` shows the two metrics are independent.** It touches two strands on
   each side of the wall yet crosses it once, and is still **provably** a
   connected sum. Strands *touched* is not strands *crossing*; only the latter
   bears on the connected-sum structure.
3. **One candidate clears the threshold** -- `I5`, at 1.2475x -- and it is the
   most elaborate of the five.
4. **REFUSAL: no candidate is selected.** Picking `I5` *because* it clears
   `sqrt(B_AME)` would be a fit, and precisely the kind this repository's
   anti-fit discipline exists to stop. Nothing here derives which interface is
   correct. What could: the colour-tube structure of
   `conj:inter-nucleon-channel-color-tube` via `conj:s5-so3-fiber-action`, or a
   derivation from the Bring geometry. The AME number may not do the selecting.

NECESSARY vs SUFFICIENT -- read `prov.#?` correctly
===================================================
`prov.#?` is the **single-crossing factorisation**: exactly one occurrence of the
wall generator, everything before it below the wall and everything after above.
That is a **sufficient** condition for a connected sum. So:

* `True`  -> the closure **IS** a connected sum. Provable, and `I1`/`I4` are.
* `False` -> **NOT DETECTED as one.** It does **not** follow that the complement
  contains an essential torus. Incompressibility is a geometric condition no
  probe here tests.

A COMPARISON NOTE THAT MATTERS
==============================
`I1` traces `0.693389`, not the committed atom value `0.575172`. That is not a
discrepancy: the canonical interface is the **colour-weighted averaged** letter
(two branches at that slot), while all five candidates are **pure** words. `I1`
is the pure single-crossing interface -- the closest like-for-like analogue --
not the canonical atom. All five are therefore comparable to each other, and
none of them is the committed object.

SCOPE -- (a)
============
NOT claimed: that any candidate produces an essential torus; that any is correct
or derivable; that `conj:jsj-decomposition-linearity` is true or false; that
binding follows. Nothing computes a binding contribution. Traces come through
`block_rep_braid_word` (float64); the spreads here are percent-level, far above
that.
"""

from __future__ import annotations

import itertools
import pathlib
import sys
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import binding_k_solver as bks  # noqa: E402
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from q_parameter import HA_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 40)

Q, H, TOL, WALL = Q_MP, HA_MP, mp.mpf("1e-9"), 3
CANDIDATES = [
    ("I1", "s3", "current: a single wall crossing", [3]),
    ("I2", "s3 s2 s4 s3", "2-block transposition (the cabling pattern)", [3, 2, 4, 3]),
    ("I3", "s3 s3", "clasp", [3, 3]),
    ("I4", "s2 s3 s4", "fan: touches 2 strands a side, crosses once", [2, 3, 4]),
    ("I5", "(s3 s2 s4 s3)^2", "doubled block transposition", [3, 2, 4, 3, 3, 2, 4, 3]),
]


def hook_dim(lam):
    lam = tuple(x for x in lam if x)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def two_row(n):
    return [(n,)] + [(n - k, k) for k in range(1, n // 2 + 1)]


def tr_M(word, n):
    y = {l: qint(n - 2 * (l[1] if len(l) > 1 else 0) + 1) / qint(2) ** n
         for l in two_row(n)}
    return mp.fsum(
        y[l] * mp.mpf(str(float(np.trace(
            bks.block_rep_braid_word(l, word, q=float(Q))))))
        for l in two_row(n))


def slots(word):
    out = []
    for (_c, d, g) in word:
        t = -mp.mpf(str(d)) / H
        if abs(t) < TOL:
            out.append([(g + 1, mp.mpf(1))])
        elif abs(t - 1) < TOL:
            out.append([(-(g + 1), mp.mpf(1))])
        else:
            out.append([(g + 1, 1 - t), (-(g + 1), t)])
    return out


def wall_crossings(word):
    return sum(1 for g in word if abs(g) == WALL)


def provably_connected_sum(gens):
    occ = [i for i, x in enumerate(gens) if abs(x) == WALL]
    if len(occ) != 1:
        return False
    p = occ[0]
    return (all(abs(x) < WALL for x in gens[:p])
            and all(abs(x) > WALL for x in gens[p + 1:]))


def main() -> int:
    wb = WitnessBuilder("interface-candidate-screen", engine="python-exact")
    wb.set_description(
        "Screens five interface words at the deuteron block wall. SELECTS NONE. "
        "The trace is NOT monotone in wall crossings (I2 crosses twice and "
        "traces below I1, which crosses once), strands touched is independent of "
        "strands crossing (I4 touches 2 a side, crosses once, is provably still "
        "a connected sum), and one candidate clears sqrt(B_AME) at 1.2475x -- "
        "but choosing it BECAUSE it clears would be a fit, so no candidate is "
        "chosen. prov.#? False means NOT DETECTED as a connected sum, which is "
        "necessary but NOT sufficient for an essential torus.")

    word = atom_braid_word_3A(1, 1)
    sl = slots(word)
    gens = [g + 1 for (_c, _d, g) in word]
    pos = gens.index(WALL)
    need = mp.sqrt(AME_B_DEUTERON_MEV_VALIDATION)

    rows = []
    for tag, expr, note, I in CANDIDATES:
        tot = mp.mpf(0)
        for combo in itertools.product(*sl):
            w = mp.mpf(1)
            for _, wt in combo:
                w *= wt
            b = [g for g, _ in combo]
            tot += w * tr_M(b[:pos] + I + b[pos + 1:], 6)
        rows.append({
            "tag": tag, "interface": expr, "note": note,
            "wall_crossings": wall_crossings(I),
            "provably_connected_sum":
                provably_connected_sum(gens[:pos] + I + gens[pos + 1:]),
            "tr_M": mp.nstr(tot, 20),
            "ratio_to_sqrt_AME": mp.nstr(tot / need, 20)})

    by = {r["tag"]: r for r in rows}
    t = {k: mp.mpf(by[k]["tr_M"]) for k in by}
    clears = [r["tag"] for r in rows
              if mp.mpf(r["ratio_to_sqrt_AME"]) >= 1]
    prov = [r["tag"] for r in rows if r["provably_connected_sum"]]

    print(f"{'cand':<5}{'interface':<20}{'xings':>6}{'prov.#?':>9}"
          f"{'tr_M':>13}{'vs sqrt(AME)':>14}")
    for r in rows:
        print(f"{r['tag']:<5}{r['interface']:<20}{r['wall_crossings']:>6}"
              f"{str(r['provably_connected_sum']):>9}"
              f"{float(mp.mpf(r['tr_M'])):>13.6f}"
              f"{float(mp.mpf(r['ratio_to_sqrt_AME'])):>13.4f}x")
    print(f"\nclears sqrt(AME): {clears}   provably connected sums: {prov}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — the trace is NOT monotone in wall crossings.
    wb.add_assertion(
        name="trace_is_not_monotone_in_wall_crossings",
        computed=repr(bool(t["I2"] < t["I1"])), expected="True",
        tolerance="0", unit="boolean",
        source="I2 crosses the wall twice and traces below I1, which crosses "
               "once; so a crossing count is no proxy for the objective")

    # A2 — strands TOUCHED is independent of strands CROSSING.
    wb.add_assertion(
        name="fan_touches_two_strands_but_is_still_a_connected_sum",
        computed=repr(bool(by["I4"]["provably_connected_sum"]
                           and by["I4"]["wall_crossings"] == 1)),
        expected="True", tolerance="0", unit="boolean",
        source="I4 = s2 s3 s4 touches strands 2,3 below and 4,5 above, yet "
               "crosses the wall once and factors")

    # A3 — CONTROL: the current interface is provably a connected sum, tying
    #      this screen to Addendum 28.
    wb.add_assertion(
        name="control_current_interface_is_provably_a_connected_sum",
        computed=repr(bool(by["I1"]["provably_connected_sum"])),
        expected="True", tolerance="0", unit="boolean",
        source="I1 = s3, the single wall crossing measured in Addendum 28")

    # A4 — exactly one candidate clears the threshold.
    wb.add_assertion(
        name="one_candidate_clears_the_threshold",
        computed=str(len(clears)), expected="1", tolerance="0", unit="count",
        source="candidates with tr_M >= sqrt(B_AME); it is I5")
    wb.add_assertion(
        name="clearing_candidate_ratio",
        computed=by["I5"]["ratio_to_sqrt_AME"], expected="1.247533",
        tolerance="1e-4", unit="ratio",
        source="I5 = (s3 s2 s4 s3)^2 -- reported, NOT selected")

    # A5 — CONTROL against the vacuous reading "they all clear": most do not.
    wb.add_assertion(
        name="control_most_candidates_fall_short",
        computed=str(len(CANDIDATES) - len(clears)), expected="4",
        tolerance="0", unit="count",
        source="four of five are below sqrt(B_AME)")

    # A6 — CONTROL on the comparison note: I1 is NOT the committed atom, since
    #      the canonical interface is averaged and all candidates are pure.
    wb.add_assertion(
        name="control_pure_I1_differs_from_the_committed_atom_trace",
        computed=repr(bool(abs(t["I1"] - mp.mpf("0.5751722457697739"))
                           > mp.mpf("0.1"))),
        expected="True", tolerance="0", unit="boolean",
        source="the canonical interface is the colour-weighted AVERAGED letter; "
               "I1 is its pure analogue, so the five are comparable to each "
               "other but none is the committed object")

    wb.add_data("wall", WALL)
    wb.add_data("interface_slot_index", pos)
    wb.add_data("candidates", rows)
    wb.add_data("required_trace", mp.nstr(need, 24))
    wb.add_data("selected_candidate", None)
    wb.add_caveat(
        "NO CANDIDATE IS SELECTED. I5 clears sqrt(B_AME) at 1.2475x; choosing it "
        "BECAUSE it clears would be a fit. Nothing here derives which interface "
        "is correct. What could: the colour-tube structure of "
        "conj:inter-nucleon-channel-color-tube via conj:s5-so3-fiber-action, or "
        "a derivation from the Bring geometry. The AME number may not do the "
        "selecting.")
    wb.add_caveat(
        "prov.#? is the single-crossing factorisation, a SUFFICIENT condition "
        "for a connected sum. True means the closure IS one; False means NOT "
        "DETECTED as one and does NOT imply an essential torus. "
        "Incompressibility is geometric and no probe here tests it.")
    wb.add_caveat(
        "Scope (a). Not claimed: that any candidate produces an essential torus, "
        "that any is correct or derivable, that "
        "conj:jsj-decomposition-linearity is true or false, or that binding "
        "follows. Nothing computes a binding contribution. float64 traces via "
        "block_rep_braid_word; the spreads are percent-level.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
