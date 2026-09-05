#!/usr/bin/env python3
"""Why binding_energy is negative: term 1 takes ln of a trace that is ZERO.

Gap qou-sv7h. `815b2a46a0` measured four wrong-signed atoms and said plainly
that "nothing here says WHY the sign is wrong -- that is the physics question
this measurement opens and does not answer." This probe answers it, and the
answer is arithmetic rather than physics.

THE STRUCTURE

`unified_iterative_correction` accumulates, per partition and per step,

    B_lambda = C_lambda * ( ln|Tr M_lambda^(0..A)| - ln d_lambda )
    C_lambda = m_e * H_q(lambda) * y_lambda * rho_lambda(s_*)

Each factor of C_lambda is separately non-negative, and this probe measures
that rather than asserting it:

  * m_e > 0;
  * H_q(lambda) = prod_x [h_x]_q > 0 at q0 > 1;
  * y_lambda = w_lambda/d_lambda - y_0 with y_0 = min_lambda(w/d), so
    y_lambda >= 0 BY CONSTRUCTION -- and the code's closed form 1/[k]_q!
    reproduces that minimum at every k;
  * rho_lambda(s_*) = 1/(mu_lambda + s_*), with mu_lambda = sum_x [c(x)]_q^2
    a sum of squares and s_* = (q-1)/q > 0, so rho > 0.

So the SIGN of every contribution is the sign of its log-trace factor, and the
magnitude is a non-negative multiple of it.

THE DEFECT

At A = 1 -- a single nucleon, no bond -- the Markov trace of the (2,1) block is
EXACTLY ZERO. `ln|Tr|` is therefore -infinity, and since C_(2,1) > 0 the
accumulated binding is -infinity too. Every finite value the function has ever
returned is an artefact of where the arithmetic underflowed:

    kernel dps   |Tr|          ln|Tr|      implied delta_(2,1)
        20       7.2e-16        -34.9          -4.38   <- the reported value
        50       2.7e-51       -116.4         -14.4
       100       7.3e-61       -141.4         -17.5
      exact           0           -inf          -inf

`log_norm` is 0.0 throughout, so there is no compensating rescale: the reported
`log_trace` IS `ln|Tr|`.

WHAT IS NOT CLAIMED. That the other traces are ill-conditioned -- they are not.
A census over every partition of k <= 5 across both deuterium steps finds
exactly ONE vanishing pair out of 34; all others are stable to <3 decades under
a 50 -> 100 dps change. This is a single identifiable term, not a general
breakdown, which is what makes it worth reporting: 84.7 % of the A=1 step comes
from it, the A=1 step is present for EVERY nucleus, and it is the term that
carries the sign.

That also explains, without any new physics, three things qou-sv7h measured and
could not account for: the sign is negative on BOTH matrix families (a
structural zero survives the braid-relation correction); the prediction is
nearly A-independent (a divergent A=1 term dominates and does not depend on the
nucleus); and neither a sign flip nor a constant rescale repairs it (a
divergence is not a mis-scaled binding).

Scope (a): this identifies why the computed number is negative. It does NOT say
what the correct binding formula is, and it does not touch the extensive-term
question (qou-brng), which concerns what should be ADDED once term 1 is
well-defined.

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
from hecke_core import (  # noqa: E402
    q_factorial, partitions_of, partition_dimension, wedderburn_weight,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def main() -> int:
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 74)
    print("  Why term 1 is negative: ln of a structurally-zero Markov trace")
    print("=" * 74)
    print()

    # ---- 1. the scale is non-negative, partition by partition -------------
    print("  1. C_lambda = m_e * H_q * y_lambda * rho  --  every factor >= 0")
    ents = H._partition_table()
    hook_bad = [e for e in ents if e["q_hook"] <= 0]
    scales = [(tuple(e["partition"]), mp.mpf(str(e["C_lambda_resolvent_MeV"])))
              for e in ents]
    # The only non-positive scales are the min-attaining (k) and (1^k)
    # partitions, whose y_lambda is exactly 0; they show up at ~1e-18 of
    # float64 noise rather than at 0, so compare against a noise floor rather
    # than against zero.
    noise = mp.mpf("1e-12")
    truly_neg = [(p, v) for p, v in scales if v < -noise]
    near_zero = [(p, v) for p, v in scales if abs(v) <= noise]
    print(f"     partitions: {len(ents)};  q_hook <= 0: {len(hook_bad)}")
    print(f"     C_lambda < -1e-12: {len(truly_neg)};  |C_lambda| <= 1e-12: {len(near_zero)}")
    check("q_hook is positive on every partition", not hook_bad,
          f"{len(ents)} partitions")
    check("no partition carries a genuinely negative scale", not truly_neg,
          f"{len(near_zero)} are exact zeros (the min-attaining (k)/(1^k))")

    # y_0 really is the minimum, so y_lambda >= 0 by construction
    minmatch = True
    for k in range(2, 12):
        parts = [tuple(p) for p in partitions_of(k)]
        ratios = [mp.mpf(wedderburn_weight(p)) / partition_dimension(p) for p in parts]
        true_min, claimed = min(ratios), mp.mpf(1) / q_factorial(k)
        if abs(true_min - claimed) / abs(true_min) > mp.mpf("1e-12"):
            minmatch = False
    check("y_0 = 1/[k]_q! IS min_lambda(w/d), so y_lambda >= 0 by construction",
          minmatch, "checked k = 2..11")

    # ---- 2. the (2,1) trace at A=1 vanishes -------------------------------
    print()
    print("  2. the (2,1) Markov trace at A=1 is a STRUCTURAL ZERO")
    lam = (2, 1)
    chain_a1 = H._step_chain_generic("p", [], sum(lam) - 1)
    rows = []
    for dps in (20, 50, 100):
        out = H._PHN.lp_accumulator_step_traces_mpfr(
            list(lam), [[(str(c), str(d), g) for c, d, g in chain_a1]],
            Q_50_DIGIT_STR, dps)
        tr, ln = mp.mpf(out[0][0]), mp.mpf(out[0][1])
        rows.append({"kernel_dps": dps, "abs_trace": fmt(abs(tr)),
                     "log_norm": fmt(ln),
                     "ln_abs_trace": fmt(mp.log(abs(tr))) if tr != 0 else "-inf"})
        print(f"     dps={dps:>4}  |Tr| = {mp.nstr(abs(tr), 8):>16}"
              f"   ln|Tr| = {mp.nstr(mp.log(abs(tr)), 8):>14}"
              f"   log_norm = {mp.nstr(ln, 4)}")
    t20 = mp.mpf(rows[0]["abs_trace"])
    t100 = mp.mpf(rows[2]["abs_trace"])
    decades = mp.log(t20 / t100, 10)
    check("the trace FALLS with precision, i.e. it is zero not small",
          decades > 20, f"{mp.nstr(decades, 4)} decades from dps 20 -> 100")
    check("log_norm is 0, so no rescale compensates the vanishing trace",
          all(mp.mpf(r["log_norm"]) == 0 for r in rows))

    # ---- 3. census: how many (partition, step) pairs vanish? --------------
    print()
    print("  3. census over k <= 5, both deuterium steps")
    lams = [tuple(e["partition"]) for e in ents if sum(e["partition"]) <= 5]
    vanishing = []
    for lm in lams:
        ng = sum(lm) - 1
        chains = [H._step_chain_generic(n, ["p"][:i], ng)
                  for i, n in enumerate(["p", "n"])]
        res = {}
        for dps in (50, 100):
            o = H._PHN.lp_accumulator_step_traces_mpfr(
                list(lm), [[(str(c), str(d), g) for c, d, g in ch] for ch in chains],
                Q_50_DIGIT_STR, dps)
            res[dps] = [abs(mp.mpf(t)) for t, _l in o]
        for st in range(2):
            a, b = res[50][st], res[100][st]
            drop = mp.mpf(99) if (a == 0 or b == 0) else mp.log(a / b, 10)
            if drop >= 3:
                vanishing.append({"partition": str(lm), "step_A": st + 1,
                                  "drop_decades": fmt(drop)})
    print(f"     vanishing pairs: {len(vanishing)} of {len(lams) * 2}")
    for v in vanishing:
        print(f"       {v['partition']:<16} A={v['step_A']}  drop {v['drop_decades'][:6]} decades")
    # A 3-decade threshold, not 10: the real drop here is 9.56 decades and a
    # first pass at >=10 reported ZERO vanishing pairs. The detector's own
    # threshold hid the finding it was written to catch.
    check("exactly one (partition, step) pair vanishes", len(vanishing) == 1,
          "(2,1) at A=1; all others stable")

    print()
    print("  CONSEQUENCE: C_(2,1) > 0 and ln|Tr| -> -inf, so term 1 -> -inf.")
    print("  The binding energy as computed is divergent; its reported value is")
    print("  set by the arithmetic precision, not by the nucleus.")

    w = WitnessBuilder("uic-a1-vanishing-trace", engine="python+mpmath+rust")
    w.set_description(
        "Gap qou-sv7h: unified_iterative_correction is negative because at A=1 "
        "the (2,1) Markov trace is exactly zero, so its ln is -infinity against "
        "a provably non-negative scale. Precision-tracked: |Tr| falls ~10 "
        "decades per 50 dps of added precision, log_norm stays 0, and a census "
        "over k<=5 finds exactly one such pair in 34."
    )
    w.set_audit_only("docs/audits/2026-09-05-uic-a1-vanishing-trace.md")
    w.add_parameter("q0", fmt(q))
    w.add_data("precision_scan_2_1_A1", rows)
    w.add_data("vanishing_pairs", vanishing)
    w.add_data("n_partitions_scanned", len(ents))
    for name, ok in CHECKS:
        w.add_assertion(name, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_a1_vanishing_trace_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
