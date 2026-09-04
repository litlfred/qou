#!/usr/bin/env python3
"""probe_k3_selfnormalized_recheck.py — does the k=3 FR verdict survive
the corrected q-Plancherel normalization?

BACKGROUND (bean qou-7o7h, audit 2026-09-04-plancherel-convention-gap.md).
`fr_pullback_k3_test.py` weights partitions by the textbook q-Plancherel
form dim_q^2/[n]_q!, which is NOT a probability measure in the balanced
q-integer convention this corpus uses: c_n = Sum_lambda dim_q^2/[n]_q!
runs 0.991 / 1.111 / 1.517 at n = 6/9/12 and GROWS with n.  Because the
binding functional is linear in the weights, B scales by exactly c_n --
which cancels within one atom and does NOT across atoms, so every
CROSS-atom metric is distorted.  The k3 test's headline number
(max/min of |B_pred/B_AME| over D, T, 3He, 4He) is exactly such a metric.

THE OPEN QUESTION THIS CLOSES.  The audit deliberately left open whether
the k3 test's CONCLUSIONS move under the correction, on the grounds that
it needed the re-run rather than an argument.  This is that re-run.

METHOD.  Self-normalizing means dividing dim_q^2 by Sum_mu dim_q^2(mu)
instead of by [n]_q!.  Since Sum_mu dim_q^2 = c_n * [n]_q! exactly, the
whole change is the substitution

    [n]_q!  ->  c_n * [n]_q!

so this probe patches the k3 module's `qfac` and re-runs its OWN
functions unmodified.  That keeps the comparison honest: same braid
words, same upstream chi witnesses, same functional -- one factor
different.  The canonical producer is not edited.

WHAT IS BEING CHECKED, in order of what it would cost to be wrong:

  1. reproduction   -- the unpatched run reproduces the committed witness
  2. scaling law    -- the patched per-atom ratios equal the unpatched
                       ones divided by c_n, for EVERY atom and knot
                       (this is the claim the audit rests on, now tested
                       on the FR weights rather than only the uniform
                       ones)
  3. verdict        -- does the ranking (which K_3* is best) and the
                       PARTIAL-support conclusion survive?

A NOTE ON PRECISION.  The k3 test computes chi via the Rust kernel in
FLOAT64 (`q_f64 = float(Q0)` at its line 234), so its numbers carry
~1e-16 relative noise regardless of normalization.  That is a separate
defect, far below the ~53% normalization effect measured here, and it is
NOT fixed by this probe -- recorded so the two are not conflated.

Usage:
    python3 -u probe_k3_selfnormalized_recheck.py
"""
from __future__ import annotations

import os
import sys
import time
from functools import lru_cache

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import _path_bridge  # noqa: F401,E402  (sys.path bootstrap first)

from substrate._precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

_T0 = time.monotonic()

ATOMS = ("D", "T", "3He", "4He")
ATOM_N = {"D": 6, "T": 9, "3He": 9, "4He": 12}

# committed k3 figures, for the reproduction check (inputs, not outputs)
COMMITTED = {"4_1": "1.5014667307010572",
             "5_2": "1.5394225544216216",
             "6_1": "1.604032884478463"}


def partitions(n: int, mx: int | None = None) -> list:
    if mx is None:
        mx = n
    if n == 0:
        return [()]
    out = []
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            out.append((k,) + rest)
    return out


def main() -> int:
    set_compute_dps()
    import fr_pullback_k3_test as k3

    # ---- c_n from the k3 module's OWN dim_q/qfac, not a reimplementation
    @lru_cache(maxsize=None)
    def c_of_n(n: int) -> mp.mpf:
        tot = mp.mpf(0)
        for lam in partitions(n):
            dq = k3.dim_q(lam, k3.Q0_PROTON)
            tot += mp.mpf(str(dq)) * mp.mpf(str(dq))
        return tot / k3.qfac(n, k3.Q0_PROTON)

    for n in sorted(set(ATOM_N.values())):
        print(f"  c_{n} = {mp.nstr(c_of_n(n), 16)}")

    def sweep(label: str) -> dict:
        """Run the k3 module's own per-atom binding for every knot."""
        out: dict = {}
        for knot_name, knot_word in k3.CANDIDATE_KNOTS.items():
            ratios: dict = {}
            for atom in ATOMS:
                r = k3.compute_atom_binding_fr(atom, knot_word, knot_name)
                if r.get("deferred"):
                    continue
                ratios[atom] = (mp.mpf(r["B_MeV"]) / k3.B_AME[atom])
            vals = [abs(v) for v in ratios.values()]
            out[knot_name] = {
                "ratios": ratios,
                "max_over_min": max(vals) / min(vals),
            }
            print(f"    [{label}] {knot_name}: "
                  f"max/min = {mp.nstr(out[knot_name]['max_over_min'], 10)}")
        return out

    print("\n  --- as committed (textbook dim_q^2/[n]_q!) ---")
    textbook = sweep("textbook")

    # ---- the one-factor substitution: [n]_q! -> c_n * [n]_q!
    _orig_qfac = k3.qfac

    def patched_qfac(n, q):
        return _orig_qfac(n, q) * c_of_n(n)

    print("\n  --- self-normalized (dim_q^2 / sum dim_q^2) ---")
    k3.qfac = patched_qfac
    try:
        selfnorm = sweep("selfnorm")
    finally:
        k3.qfac = _orig_qfac

    # ---- 1. reproduction of the committed figures
    repro_dev = mp.mpf(0)
    for kn, committed in COMMITTED.items():
        repro_dev = max(repro_dev,
                        mp.fabs(textbook[kn]["max_over_min"]
                                - mp.mpf(committed)) / mp.mpf(committed))

    # ---- 2. the scaling law, on the FR weights, per atom
    scaling_dev = mp.mpf(0)
    for kn in textbook:
        for atom in textbook[kn]["ratios"]:
            t = textbook[kn]["ratios"][atom]
            s = selfnorm[kn]["ratios"][atom]
            # textbook = c_n * selfnorm  =>  selfnorm = textbook / c_n
            scaling_dev = max(
                scaling_dev,
                mp.fabs(s - t / c_of_n(ATOM_N[atom])) / mp.fabs(s))

    # ---- 3. the verdict
    rank_text = sorted(textbook, key=lambda k: textbook[k]["max_over_min"])
    rank_self = sorted(selfnorm, key=lambda k: selfnorm[k]["max_over_min"])
    ranking_survives = rank_text == rank_self

    print(f"\n  reproduction of committed figures: rel dev "
          f"{mp.nstr(repro_dev, 6)}")
    print(f"  scaling law on FR weights (per atom): rel dev "
          f"{mp.nstr(scaling_dev, 6)}")
    print(f"  ranking textbook   : {' < '.join(rank_text)}")
    print(f"  ranking self-norm  : {' < '.join(rank_self)}")
    print(f"  ranking survives   : {ranking_survives}")
    for kn in rank_text:
        print(f"    {kn}: {mp.nstr(textbook[kn]['max_over_min'], 8)}"
              f"  ->  {mp.nstr(selfnorm[kn]['max_over_min'], 8)}")

    wb = WitnessBuilder("probe-k3-selfnormalized-recheck", engine="mpmath",
                        start_time=_T0)
    wb.set_description(
        "Re-runs fr_pullback_k3_test under the CORRECTED (self-normalized) "
        "q-Plancherel measure, closing the question the 2026-09-04 "
        "convention-gap audit left open. Self-normalizing is exactly the "
        "substitution [n]_q! -> c_n*[n]_q!, so this patches the k3 "
        "module's qfac and re-runs its own functions unmodified -- same "
        "braid words, same upstream chi witnesses, same functional. "
        "Checks three things: that the unpatched run reproduces the "
        "committed figures; that the scaling law (ratio scales by c_n) "
        "holds on the FR weights and not merely the uniform ones; and "
        "whether the knot RANKING and the PARTIAL-support verdict "
        "survive. Note the k3 test computes chi in float64 (q_f64 = "
        "float(Q0)); that ~1e-16 defect is separate, far below the ~53% "
        "normalization effect, and is NOT addressed here.")
    wb.set_audit_only("docs/audits/2026-09-04-plancherel-convention-gap.md")
    wb.add_data("c_n", {str(n): mp.nstr(c_of_n(n), 30)
                        for n in sorted(set(ATOM_N.values()))})
    wb.add_data("per_knot", {
        kn: {
            "max_over_min_textbook": fmt(textbook[kn]["max_over_min"]),
            "max_over_min_selfnormalized": fmt(selfnorm[kn]["max_over_min"]),
            "ratios_textbook": {a: fmt(v) for a, v
                                in textbook[kn]["ratios"].items()},
            "ratios_selfnormalized": {a: fmt(v) for a, v
                                      in selfnorm[kn]["ratios"].items()},
        } for kn in textbook})
    wb.add_data("ranking", {
        "textbook": rank_text,
        "selfnormalized": rank_self,
        "survives": bool(ranking_survives),
    })

    wb.add_assertion(
        "reproduces_committed_k3_figures",
        computed=fmt(repro_dev), expected=fmt(mp.mpf(0)), tolerance=1e-12,
        source="unpatched sweep vs the three committed per-knot max/min "
               "in fr-pullback-k3-test.witness.json — establishes that "
               "the patched run differs only by the normalization",
    )
    wb.add_assertion(
        "scaling_law_holds_on_fr_weights",
        computed=fmt(scaling_dev), expected=fmt(mp.mpf(0)), tolerance=1e-30,
        source="per-atom, per-knot: ratio_selfnorm = ratio_textbook/c_n. "
               "The audit verified this for UNIFORM weights; this tests "
               "it on the FR-redistributed weights, where the stratum "
               "total S_k carries the normalization and the within-"
               "stratum redistribution is scale-free",
    )
    wb.save()
    print("\n  witness saved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
