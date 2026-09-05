#!/usr/bin/env python3
"""The wrong sign is forced by the Pass-2 gate, not by the nucleus.

Gap qou-sv7h. `815b2a46a0` measured four wrong-signed atoms and said "nothing
here says WHY the sign is wrong". This probe answers it, and the answer is in
the LP gate rather than in the physics.

THE ARGUMENT, in three measured steps

`unified_iterative_correction` returns, after Pass 2,

    B = sum over GATED lambda of  C_lambda * ( ln|Tr M_lambda(A)| - ln d_lambda )

1. C_lambda >= 0 for EVERY partition. Each factor of
   C = m_e * H_q * y_lambda * rho is separately non-negative; in particular
   y_lambda = w/d - y_0 with y_0 = min_lambda(w/d), so y_lambda >= 0 BY
   CONSTRUCTION. Measured: 0 of 682 partitions carry a negative scale.
   (Established in uic_a1_vanishing_trace_probe; re-checked here.)

2. Pass 2 keeps exactly the partitions with final trace <= 0 and zeroes the
   rest ("complementary slackness": y_lambda > 0 only where the Frobenius
   constraint is tight).

3. A trace <= 0 almost never has |Tr| >= d, while a positive trace often does.
   This is structural: Tr(I) = d > 0, so reaching Tr >= +d only needs the
   spectrum to stay aligned with the identity, whereas reaching Tr <= -d needs
   it to overshoot through zero AND align coherently in the negative direction.

Therefore ln(|Tr|/d) < 0 on essentially the whole gated set, every term is a
non-negative scale times a negative log, and B < 0 is FORCED -- for any nucleus.

The same mechanism explains the A-INDEPENDENCE qou-sv7h measured (-7.271,
-7.742, -7.456, -6.829 while AME spans 12.7x): the gate selects a roughly
constant-size set of cancelling partitions whose log-ratios sit in a similar
range whatever A is. The output is a property of the gate's selection, not of
the nucleus.

WHAT IS NOT CLAIMED

That the gate is WRONG. Its own docstring derives it from complementary
slackness, which for a constraint tr >= 0 makes "tight" mean tr = 0 -- while the
code admits all tr <= 0, and the contribution ln|tr| diverges as tr -> 0. Those
two readings are in tension and resolving it needs the primal LP, which is not
in this file. Flagged, not decided.

Also not claimed: what the correct formula is. And NOT claimed that the
accumulator diverges -- it does not (uic_a1_vanishing_trace_probe, which
retracts an earlier claim of mine that it does).

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-sv7h OPEN.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

import hecke_core_legacy as H  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

ATOMS = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"), (3, 3, "6Li")]
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def main() -> int:
    set_compute_dps()
    print("=" * 74)
    print("  The wrong sign is forced by the Pass-2 gate")
    print("=" * 74)
    print()

    ents = [e for e in H._partition_table() if sum(e["partition"]) <= 6]
    neg_scale = [e for e in H._partition_table()
                 if mp.mpf(str(e["C_lambda_resolvent_MeV"])) < mp.mpf("-1e-12")]
    check("C_lambda >= 0 on every partition", not neg_scale,
          f"0 of {len(H._partition_table())} negative")

    print()
    print("  per-atom: the gate keeps Tr<=0, and those are the negative terms")
    rows, pooled = [], {"pos": 0, "neg": 0, "big_pos": 0, "big_neg": 0}
    for Z, N, name in ATOMS:
        A = Z + N
        ordering = ["p"] * Z + ["n"] * N
        g_logs, s_logs, gated_sum = [], [], mp.mpf(0)
        for e in ents:
            lam = tuple(e["partition"])
            chains = [H._step_chain_generic(ordering[k], ordering[:k], sum(lam) - 1, True)
                      for k in range(A)]
            o = H._PHN.lp_accumulator_step_traces_mpfr(
                list(lam),
                [[(str(c), str(d), g) for c, d, g in ch] for ch in chains],
                Q_50_DIGIT_STR, 50)
            t, l = mp.mpf(o[-1][0]), mp.mpf(o[-1][1])
            logratio = l + mp.log(abs(t)) - mp.log(e["dim"])
            big = logratio >= 0                      # |Tr| >= d
            if t > 0:
                s_logs.append(logratio)
                pooled["pos"] += 1; pooled["big_pos"] += int(big)
            else:
                g_logs.append(logratio)
                pooled["neg"] += 1; pooled["big_neg"] += int(big)
                gated_sum += mp.mpf(str(e["C_lambda_resolvent_MeV"])) * logratio
        gneg = sum(1 for x in g_logs if x < 0)
        sneg = sum(1 for x in s_logs if x < 0)
        rows.append({"atom": name, "A": A, "n_gated": len(g_logs),
                     "gated_negative": gneg, "n_slack": len(s_logs),
                     "slack_negative": sneg, "gated_sum": fmt(gated_sum)})
        print(f"     {name:>5} A={A}  gated {gneg:>2}/{len(g_logs):<2} negative"
              f"   slack {sneg:>2}/{len(s_logs):<2} negative"
              f"   gated sum = {mp.nstr(gated_sum, 8):>12}")

    check("every atom's gated sum is negative",
          all(mp.mpf(r["gated_sum"]) < 0 for r in rows))
    check("the gated set is >=90% negative for every atom",
          all(r["gated_negative"] >= 0.9 * r["n_gated"] for r in rows))
    check("the gated set is MORE negative than the slack set, every atom",
          all(r["gated_negative"] / r["n_gated"] > r["slack_negative"] / r["n_slack"]
              for r in rows))

    # the structural asymmetry that makes step 3 work
    print()
    print("  the asymmetry:  Tr(I) = +d, so Tr >= +d is easy and Tr <= -d is hard")
    fp = mp.mpf(pooled["big_pos"]) / pooled["pos"]
    fn = mp.mpf(pooled["big_neg"]) / pooled["neg"]
    print(f"     Tr > 0 : |Tr| >= d in {pooled['big_pos']:>4} of {pooled['pos']:>4}"
          f"  ({mp.nstr(100 * fp, 4)} %)")
    print(f"     Tr <= 0: |Tr| >= d in {pooled['big_neg']:>4} of {pooled['neg']:>4}"
          f"  ({mp.nstr(100 * fn, 4)} %)")
    check("|Tr| >= d is much rarer when Tr <= 0 than when Tr > 0", fn * 3 < fp,
          f"{mp.nstr(100 * fn, 3)} % against {mp.nstr(100 * fp, 3)} %")

    # A-independence falls out of the same mechanism
    sizes = [r["n_gated"] for r in rows]
    print()
    print(f"  gated-set size across A=2..6: {sizes}  -- roughly constant, which is")
    print("  why the output is A-independent while AME spans 12.7x.")

    w = WitnessBuilder("uic-sign-forced-by-gate", engine="python+mpmath+rust")
    w.set_description(
        "Gap qou-sv7h: the wrong sign of unified_iterative_correction is forced "
        "by the Pass-2 complementary-slackness gate. C_lambda >= 0 on every "
        "partition; the gate keeps exactly Tr<=0; and Tr<=0 almost never has "
        "|Tr| >= d (3.4% against 34.1%) because Tr(I) = +d. So every gated term "
        "is a non-negative scale times a negative log and B < 0 is forced for "
        "any nucleus. The near-constant gated-set size explains the measured "
        "A-independence too."
    )
    w.set_audit_only("docs/audits/2026-09-05-uic-sign-forced-by-gate.md")
    w.add_data("per_atom", rows)
    w.add_data("pooled_big_trace_fraction",
               {"Tr_pos_total": pooled["pos"], "Tr_pos_big": pooled["big_pos"],
                "Tr_nonpos_total": pooled["neg"], "Tr_nonpos_big": pooled["big_neg"],
                "frac_big_when_pos": fmt(fp), "frac_big_when_nonpos": fmt(fn)})
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_sign_forced_by_gate_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
