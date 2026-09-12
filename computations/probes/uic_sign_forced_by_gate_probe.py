#!/usr/bin/env python3
"""The wrong sign is BIASED by the Pass-2 gate -- but NOT forced by it.

RETRACTION 2026-09-12 (bean `qou-21oc`).  THE TITLE CLAIM OF THIS PROBE IS
REFUTED, by the experiment its own subject made available.

The Pass-2 gate was DROPPED from `unified_iterative_correction` on 2026-09-12
(owner ruling) after its complementary-slackness justification was refuted
sorry-free in `QOU.MassTheory.UICGateNotFromComplementarySlackness` (PR #7251).
If the wrong sign were FORCED BY the gate, removing the gate would have to be
able to change it.  Measured here, over the same terms with no sign filter:

    atom     gated sum      UNGATED sum
    2H      -1.3656848       -2.251132
    3H      -0.97040895      -1.8036172
    3He     -0.80794043      -1.7465929
    4He     -0.80209171      -1.3701187
    6Li     -1.0769706       -1.9696784

and independently, through the producer itself at k_exact = 4:

    2H      gated -0.0895596830589507  ->  ungated -0.412212192245027
    4He     gated -0.0805867484776914  ->  ungated -0.2742397716174

QUOTE THE TIER WITH EVERY ONE OF THESE.  The producer's return is strongly
`k_exact`-dependent: 2H ungated runs -0.412 / -1.227 / -2.251 / -17.691 at
`k_exact` = 4 / 5 / 6 / 11, a 43x spread, and 11 is the PRODUCTION DEFAULT.  The
two rows above are the `k_exact = 4` tier; at the default they are
`-9.14773623102088 -> -17.6908290020795` (2H) and
`-8.20155846836239 -> -15.9926510049258` (4He).

**These five are the PROBE'S OWN reconstruction, not the producer's return.** It
sums over partitions with `k <= 6` only, reading `C_lambda_resolvent_MeV` from
the partition table with one kernel call per partition and no per-step
accumulation, and it orders nucleons `["p"]*Z + ["n"]*N` where the producer uses
the alternating ground-state ordering. Cross-checked: at 2H (where the two
orderings coincide) the probe's `-2.251132` matches the producer's
`k_exact = 6` return `-2.251131977321312` to 8 significant figures; at 4He they
differ by 5.39 % (`-1.3701187` against `-1.448199112790757`) for exactly that
reason. Do NOT quote these five as `unified_iterative_correction` values.

Every ungated sum is negative, and LARGER in magnitude.  The AME2020 2H
binding is +2.2246 MeV, so dropping the gate moves the prediction AWAY from
the data, not toward it.

WHAT SURVIVES, unchanged and still measured below: step 1 (C_lambda >= 0 on
every partition, 0 of 682 negative) and step 3 (|Tr| >= d in 3.4 % of Tr <= 0
against 34.1 % of Tr > 0, because Tr(I) = +d).  Those two say the gated subset
is MORE negative than the slack one -- a BIAS, which the numbers confirm (the
gated sum is 0.61x the ungated one at 2H and 0.59x at 4He).  Step 2, the
inference from that bias to "B < 0 is FORCED", does not follow and is
withdrawn.  This is a scope-(a) retraction of an over-claim; the measurements
are untouched and every one of them still passes.

The A-independence paragraph below is likewise downgraded from explanation to
correlation.  The gated-set size is roughly constant across A -- but so is the
ungated sum, measured independently in `where_the_a_dependence_is_lost_probe`,
whose Layer 3 finds the RAW (pre-gate) ratio already flat at 1.25 / 1.16 / 1.09
for k = 5 / 7 / 9.  The gate is not the cause there either.

--- original text follows, kept because its steps 1 and 3 still stand ---

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

[2026-09-12: DECIDED, elsewhere.  The primal LP was hunted in PR #7251, and the
tension this paragraph flagged is mismatch 3 of four: on any feasible point of
`prop:operator-selection-lp`, `0 <= (Gx)_i` makes `<= 0` and `= 0` the same
predicate, so the code's `tr <= 0` IS the tightness gate and keeps only blocks
at exactly zero -- while the producer kept 4 of 10 at 2H.  So the gate IS
wrong, contrary to this paragraph's careful non-claim, and it is gone.]

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
    print("  The wrong sign is BIASED by the Pass-2 gate -- not FORCED by it")
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
        ungated_sum = mp.mpf(0)
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
            # The UNGATED sum: every partition contributes, no sign filter.
            # Added 2026-09-12 with the gate drop (bean `qou-21oc`) -- see the
            # RETRACTION in this file's docstring.  Same terms, no selection.
            ungated_sum += mp.mpf(str(e["C_lambda_resolvent_MeV"])) * logratio
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
                     "slack_negative": sneg, "gated_sum": fmt(gated_sum),
                     "ungated_sum": fmt(ungated_sum)})
        print(f"     {name:>5} A={A}  gated {gneg:>2}/{len(g_logs):<2} negative"
              f"   slack {sneg:>2}/{len(s_logs):<2} negative"
              f"   gated sum = {mp.nstr(gated_sum, 8):>12}"
              f"   UNGATED sum = {mp.nstr(ungated_sum, 8):>12}")

    check("every atom's gated sum is negative",
          all(mp.mpf(r["gated_sum"]) < 0 for r in rows))
    # THE CHECK THAT RETRACTS THIS PROBE'S TITLE.  If the sign were forced BY
    # the gate, removing the gate would have to be able to change it.  It does
    # not: the ungated sum is negative for every atom too.
    check("every atom's UNGATED sum is ALSO negative -- so the gate does NOT "
          "force the sign (retraction, 2026-09-12)",
          all(mp.mpf(r["ungated_sum"]) < 0 for r in rows),
          ", ".join(f"{r['atom']} {mp.nstr(mp.mpf(r['ungated_sum']), 6)}"
                    for r in rows))
    check("the ungated sum is LARGER in magnitude than the gated one, every "
          "atom -- dropping the gate moves AWAY from AME, not toward it",
          all(abs(mp.mpf(r["ungated_sum"])) > abs(mp.mpf(r["gated_sum"]))
              for r in rows))
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
        "Gap qou-sv7h: the wrong sign of unified_iterative_correction is BIASED "
        "by the Pass-2 complementary-slackness gate but NOT forced by it. "
        "C_lambda >= 0 on every partition; the gate kept exactly Tr<=0; and "
        "Tr<=0 almost never has |Tr| >= d (3.4% against 34.1%) because "
        "Tr(I) = +d, so the gated subset is more negative than the slack one. "
        "RETRACTED 2026-09-12 (bean qou-21oc): the earlier conclusion that "
        "B < 0 is FORCED by the gate is refuted. The gate was dropped (owner "
        "ruling; its CS justification refuted sorry-free in PR #7251) and every "
        "atom's UNGATED sum is negative too, and LARGER in magnitude, so "
        "dropping it moves away from AME. Steps 1 and 3 stand; the inference "
        "from bias to forcing does not."
    )
    w.set_audit_only("docs/audits/2026-09-05-uic-sign-forced-by-gate.md")
    w.add_data("per_atom", rows)
    w.add_data("retraction_2026_09_12",
               "The Pass-2 gate was DROPPED from the producer on 2026-09-12 "
               "(owner ruling, bean qou-21oc) after its complementary-slackness "
               "justification was refuted sorry-free (PR #7251). This probe's "
               "title claim -- that the wrong sign is FORCED BY the gate -- is "
               "thereby refuted: every atom's UNGATED sum is negative too, and "
               "larger in magnitude. What survives is steps 1 and 3 (C_lambda "
               ">= 0 everywhere; |Tr| >= d is ~10x rarer when Tr <= 0), i.e. "
               "the gate BIASED the sign, it did not create it.")
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
