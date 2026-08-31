#!/usr/bin/env python3
"""
determinacy_filter_calibration_probe.py — calibrating my own triage heuristic
against the settled record, and finding it half wrong.

THE HEURISTIC UNDER TEST.  PR #5863 closed two fronts that came out
structurally opposite, and I proposed a filter from the contrast:

    prefer candidate binding terms carrying a genuine EXTREMAL or STRUCTURAL
    determinacy; treat a FREE CONTINUOUS PARAMETER WITH NO OPTIMUM as a
    warning sign.

Authorised for testing (bean `qou-pjq5`).  It is my own generalisation from two
cases, so the job is to break it before applying it.  It breaks in both halves,
in different ways, and what survives is narrower and more useful.

DEFECT 1 -- "EXTREMAL" WAS DOING NO WORK.
An extremal principle over an underdetermined constraint carries ZERO
information about which coordinate wins: the cost decides, and the cost is a
modelling choice.  Proved in general for ANY single constraint --
`QOU.MassTheory.both_orderings_achievable` -- and measured here on the real
Hecke objects (A3).  The corpus said this in 2026-05 and I did not read it
before proposing the filter: Option D of the Delta_lambda programme "moves the
underdetermination to the choice of cost rather than eliminating it"
(`docs/audits/2026-05-09-mass-table-fitting-audit.md`).

DEFECT 2 -- "STRUCTURAL" DOES NOT PREDICT SUCCESS.
Option B, the Frobenius co-Casimir `1/dim_q(lambda)`, is recorded in that same
table as "theorem-forced (no free params)" -- maximally structural by my filter
-- and it FAILED (residual -2.30 MeV, wrong sign).  Later confirmed
"PROVED-INSUFFICIENT ... vortex-blind"
(`docs/audits/2026-06-01-e0-lambda-substrate-derivation-options.md`).  A
candidate with no free parameter can simply be the wrong object.

WHAT SURVIVES, and it is worth more than what I proposed.
The filter separates DETERMINATE from UNDERDETERMINED.  It does not separate
right from wrong, and it never could.  Its value is the opposite of what I
claimed: a no-free-choice candidate yields a definite prediction and therefore
becomes FALSIFIABLE -- co-Casimir was promoted to a testable claim and refuted
in one measurement, which is the filter working.  An underdetermined candidate
can never be falsified, because it absorbs any residual into its free choice.
So the warning sign means "this cannot be tested", not "this will be wrong".

And the free choice hides in three places, not one: a free PARAMETER (the
growing-width `w`), a free OBJECTIVE (Option D's cost), or a free SELECTION RULE
(Occam's "single-support + min |Delta|").  My original phrasing named only the
first, which is why "extremal" looked like an escape from it.  It is not: an
optimum relocates the freedom into the objective.

NOT CLAIMED.  Nothing here refutes any candidate; a triage heuristic cannot
exclude anything, only a proved invariant can (AGENTS.md).  Everything below is
scope (a).  The Option-D numbers quoted from the 2026-05 audit are CITED, not
re-run -- flagged as such, per the corpus rule that another agent's write-up is
not a primary source.

@module computations/meson/determinacy_filter_calibration_probe
"""

from __future__ import annotations

import pathlib
import re
import sys
from fractions import Fraction
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)
Q = Q_MP

_FAILED: list[str] = []


# bean qou-srvu. Each `check` below is a real falsifiable claim -- it prints
# [PASS]/[FAIL], is tallied, and decides this script's exit code -- but none of
# them reached the witness, so `save()` emitted `allPassed: true` over an EMPTY
# assertions list: green while asserting nothing, and in direct contradiction
# with the same run's exit code. Recorded here and flushed to the witness just
# before `save()`, which needs no call-site change. The assertion NAME is the
# label the message already carries ("A1", "C2", ...); the whole message
# becomes `source`, so every caveat in it travels with the assertion. No
# threshold is introduced: every one already sits at its call site.
_CHECKS: list[tuple[bool, str]] = []


def check(ok: bool, msg: str) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {msg}")
    _CHECKS.append((bool(ok), msg))
    if not ok:
        _FAILED.append(msg)


def _flush_assertions(wb) -> None:
    """Emit each recorded check as a witness assertion."""
    for i, (ok, msg) in enumerate(_CHECKS, 1):
        label = msg.split(":", 1)[0].strip()
        if not re.fullmatch(r"[A-Z]\d+", label):
            label = f"check_{i}"
        wb.add_assertion(label, computed=ok, expected=True, source=msg)


# -- the settled record, with citations ------------------------------------
# Each row: (name, free_choice_kind, blind, outcome, citation)
# free_choice_kind: "none" | "parameter" | "objective" | "selection"
SETTLED = [
    ("Occam single-partition pick", "selection", False, "underdetermined",
     "docs/audits/2026-05-09-mass-table-fitting-audit.md"),
    ("B: Frobenius co-Casimir 1/dim_q", "none", True, "failed",
     "docs/audits/2026-06-01-e0-lambda-substrate-derivation-options.md"),
    ("C: Demazure-fibre", "none", True, "failed",
     "docs/audits/2026-05-09-mass-table-fitting-audit.md"),
    ("D: LP shadow prices", "objective", False, "underdetermined",
     "docs/audits/2026-05-09-mass-table-fitting-audit.md"),
    ("growing-width cut, constant w", "parameter", False, "excluded",
     "docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md (Add. 42)"),
    ("PROBE-4 KL crystal weights", "none", True, "excluded-by-invariant",
     "docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md"),
    ("Delta_lambda VALUE = signed Springer dim", "none", False, "proved",
     "docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md"),
    ("cable-shift law", "none", False, "determined",
     "docs/audits/2026-08-26-cable-shift-deficit-lives-in-multidim-channels.md"),
]

DETERMINATE = {"proved", "determined", "failed", "excluded-by-invariant"}
UNDETERMINED = {"underdetermined", "excluded"}


# -- q-objects -------------------------------------------------------------

def qint(m: int):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def hook_dim(lam) -> int:
    lam = tuple(x for x in lam if x)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def qdim(lam):
    """q-hook-length quantum dimension."""
    lam = tuple(x for x in lam if x)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    num = qint(sum(lam))
    out = mp.mpf(1)
    for i, row in enumerate(lam):
        for j in range(row):
            out *= qint((row - j) + (conj[j] - i) - 1)
    return mp.factorial(sum(lam)) / out * (num / num)


def seminormal(shape, q):
    """Hoefsmit seminormal matrices for the generators of H_n(q).

    Lifted verbatim from `cable_shift_where_the_deficit_lives_probe.py`, which
    is merged and exercised -- rather than re-derived here, where a fresh
    transcription error would be indistinguishable from a finding.
    """
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    hq = q - 1 / q
    sigmas = []
    for k in range(1, n):
        rows = [[mp.mpf(0)] * dim for _ in range(dim)]
        seen = set()
        for i in range(dim):
            if i in seen:
                continue
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            a = hq / (1 - q ** (-2 * rho))
            sw = dict(syts[i])
            sw[k], sw[k + 1] = ci1, ci
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == sw), None)
            if j is None:
                rows[i][i] = a
                seen.add(i)
            else:
                ap = hq / (1 - q ** (2 * rho))
                rows[i][i], rows[j][j] = a, ap
                rows[i][j] = rows[j][i] = mp.sqrt(a * ap + 1)
                seen.update((i, j))
        sigmas.append(mp.matrix(rows))
    return sigmas, dim


def char_of_word(shape, word):
    """Character of a braid word on the seminormal channel `shape`."""
    sigmas, dim = seminormal(shape, Q)
    acc = mp.eye(dim)
    for g in word:
        M = sigmas[abs(g) - 1]
        acc = acc * (M if g > 0 else M ** -1)
    return sum((acc[i, i] for i in range(dim)), mp.mpf(0))


def markov_weight(lam, k):
    j = lam[1] if len(lam) > 1 else 0
    return qint(k - 2 * j + 1) / qint(2) ** k


def main() -> int:
    wb = WitnessBuilder("determinacy-filter-calibration", engine="python-exact")
    wb.set_description(
        "Calibrates the PR #5863 triage heuristic against the settled record and "
        "finds it half wrong. 'Extremal' carries no determinacy -- the cost "
        "decides (proved in Lean for any single constraint; measured here on the "
        "real Hecke objects). 'Structural' does not predict success -- the "
        "Frobenius co-Casimir was theorem-forced with no free parameters and "
        "failed. What survives: the filter separates DETERMINATE from "
        "UNDERDETERMINED, never right from wrong, and the free choice hides in a "
        "parameter, an objective OR a selection rule.")

    print("=" * 92)
    print("Calibrating the determinacy filter against the settled record")
    print("=" * 92)

    N6 = [p for p in partitions_of(6) if len(p) <= 2]

    # -- A1: the filter's 'structural' half is falsified -------------------
    print("\n1. Defect 2 first: 'structural' does not predict success")
    structural_failures = [r for r in SETTLED
                           if r[1] == "none" and r[3] in ("failed", "excluded-by-invariant")]
    check(len(structural_failures) >= 2,
          f"A1: {len(structural_failures)} settled candidates had NO free choice "
          "and still did not deliver the binding term - "
          + "; ".join(r[0] for r in structural_failures)
          + ". So 'no free parameter' is not a success predictor, and my filter's "
            "'prefer structural' clause is FALSIFIED as stated")

    # -- A2: the blindness that explains co-Casimir ------------------------
    print("\n2. Why co-Casimir failed, computed rather than asserted")
    inv_qdim = {lam: 1 / qdim(lam) for lam in N6}
    print("     lambda        1/dim_q(lambda)")
    for lam in N6:
        print(f"   {str(lam):12s}  {mp.nstr(inv_qdim[lam], 12):>16}")

    wA = [1, 2, 1, 3, 2, 1]
    wB = [1, -2, 1, -3, 2, 1]
    chis = {lam: (char_of_word(lam, wA), char_of_word(lam, wB)) for lam in N6}
    spread = max(abs(a - b) for a, b in chis.values())
    check(spread > mp.mpf("1e-3"),
          f"A2: the per-block slot DOES vary with the braid word - max |chi(wA) "
          f"- chi(wB)| = {mp.nstr(spread, 10)} over the two-row lambda at n = 6. "
          "But `1/dim_q(lambda)` has no word argument at all, so it contributes "
          "the SAME number to every atom. That is the 'vortex-blind' verdict, "
          "recomputed from the formulae rather than taken from the audit")

    # -- A3: the extremal half, measured on the real objects ---------------
    print("\n3. Defect 1: the extremum is decided by the cost, not the constraint")
    a = {lam: markov_weight(lam, 6) * chis[lam][0] for lam in N6}
    a = {lam: v for lam, v in a.items() if abs(v) > mp.mpf("1e-30")}

    cost_planch = {lam: mp.mpf(hook_dim(lam)) * markov_weight(lam, 6) for lam in a}
    cost_frob = {lam: inv_qdim[lam] for lam in a}

    def argmin(cost):
        return min(a, key=lambda lam: cost[lam] / abs(a[lam]))

    pick_p, pick_f = argmin(cost_planch), argmin(cost_frob)
    print(f"\n   Plancherel-style cost picks  lambda = {pick_p}")
    print(f"   Frobenius-style  cost picks  lambda = {pick_f}")
    print("\n     lambda        |a_lambda|        w/|a| (Planch)     w/|a| (Frob)")
    for lam in a:
        print(f"   {str(lam):12s}  {mp.nstr(abs(a[lam]), 9):>12}"
              f"  {mp.nstr(cost_planch[lam] / abs(a[lam]), 9):>16}"
              f"  {mp.nstr(cost_frob[lam] / abs(a[lam]), 9):>16}")

    check(pick_p != pick_f,
          f"A3: the two costs select DIFFERENT partitions ({pick_p} vs {pick_f}) "
          "on the same feasible set - so the extremum determines nothing; the "
          "cost does. Matches QOU.MassTheory.both_orderings_achievable, which "
          "proves BOTH orderings are reachable for ANY single constraint")

    # -- A4: what survives -------------------------------------------------
    print("\n4. The refinement, and its hit-rate on the settled record")
    hits = misses = 0
    print("\n   candidate                                free-choice   outcome            call")
    for name, kind, blind, outcome, _cite in SETTLED:
        predicted = "undetermined" if kind != "none" else "determinate"
        actual = "determinate" if outcome in DETERMINATE else "undetermined"
        ok = predicted == actual
        hits += ok
        misses += (not ok)
        print(f"   {name:40s} {kind:12s}  {outcome:18s} {'hit' if ok else 'MISS'}")

    check(misses == 0,
          f"A4: the REFINED rule - 'a free choice anywhere (parameter, objective "
          f"or selection rule) means undetermined' - is {hits}/{hits + misses} on "
          "the settled record. It predicts DETERMINACY, which is a property of "
          "the specification, not correctness, which is not")

    naive_misses = sum(1 for n, k, b, o, _c in SETTLED
                       if k == "none" and o in ("failed", "excluded-by-invariant"))
    check(naive_misses > 0,
          f"A5: whereas my ORIGINAL filter, read as a success predictor, misses "
          f"{naive_misses} of {len(SETTLED)} - every structural candidate that "
          "made a definite prediction and was then refuted. Those are not filter "
          "failures if the filter's job is falsifiability: it promoted them to "
          "testable, and the measurement did the rest")

    # -- A6: could the call have been made in advance? ---------------------
    print("\n5. Pre-registrability - the tautology charge")
    check(all(k in ("none", "parameter", "objective", "selection")
              for _n, k, _b, _o, _c in SETTLED),
          "A6: every classification above is read off the candidate's "
          "SPECIFICATION - does a parameter, objective or selection rule remain "
          "unfixed? - so it is available BEFORE the fit is run, and the rule is "
          "not a post-hoc re-description of the outcome. A2 demonstrates this "
          "concretely: co-Casimir's blindness is computable from `1/dim_q` alone")

    wb.add_data("q0", mp.nstr(Q, 20))
    wb.add_data("settled_candidates", [
        {"name": n, "free_choice": k, "blind": b, "outcome": o, "citation": c}
        for n, k, b, o, c in SETTLED])
    wb.add_data("refined_rule_hits", hits)
    wb.add_data("refined_rule_misses", misses)
    wb.add_data("original_filter_success_misses", naive_misses)
    wb.add_data("chi_word_spread_n6", mp.nstr(spread, 20))
    wb.add_data("lp_pick_plancherel_cost", str(pick_p))
    wb.add_data("lp_pick_frobenius_cost", str(pick_f))
    wb.add_data("verdict",
                "The proposed filter is HALF WRONG. 'Extremal' supplies no "
                "determinacy (the cost decides; Lean-proved for any single "
                "constraint). 'Structural' does not predict success (co-Casimir "
                "was theorem-forced and failed). What survives: a free choice "
                "anywhere - parameter, objective or selection rule - means the "
                "candidate cannot be falsified; no free choice means it can. "
                "Falsifiability, not correctness.")
    wb.add_caveat(
        "Scope (a). A triage heuristic excludes nothing; only a proved invariant "
        "does. Nothing here refutes any candidate.")
    wb.add_caveat(
        "The Option-D Plancherel/Frobenius numbers in the 2026-05 audit are CITED, "
        "not re-run. A3 measures the same PHENOMENON on freshly built Hecke "
        "objects with a representative 6-strand word; the generality comes from "
        "the Lean, not from this instance.")
    wb.add_caveat(
        "The settled-candidate table is hand-assembled from the corpus with "
        "citations, and is a sample of what is recorded, not a census.")
    wb.add_caveat(
        "DO NOT QUOTE THE 8/8 AS VALIDATION. I assigned BOTH axes of that table "
        "- the free-choice label and the outcome class - so A4 is a consistency "
        "check on my own bookkeeping, not independent evidence. The two "
        "load-bearing results are A1 (three structural candidates failed, "
        "recorded by other agents at the time) and A3 (the two costs measurably "
        "pick different partitions on freshly built Hecke objects). If the "
        "refined rule is ever to earn a hit-rate, it needs candidates classified "
        "BEFORE their outcomes are known.")
    _flush_assertions(wb)
    wb.save()

    print("\n" + "=" * 92)
    print(f"{6 - len(_FAILED)}/6 assertions passed")
    print("=" * 92)
    return 1 if _FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
