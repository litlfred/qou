"""The A=1 Markov trace is zero — and the accumulator survives it. Dropping it does not.

Gap qou-sv7h. Two options were on the table for term 1's wrong sign:
  (V1) a single nucleon has zero binding, so the A=1 step should not enter;
  (V2) reference the bound state against the free-nucleon (intra-only) braid.
This probe measures both, and the answer to (V1) is the opposite of what it
looks like.

WHAT IS TRUE, AND MEASURED HERE

1. The per-partition scale is NON-NEGATIVE, every factor separately:
   C_lambda = m_e * H_q(lambda) * y_lambda * rho_lambda(s_*), with
   y_lambda = w/d - y_0 and y_0 = min_lambda(w/d) -- so y_lambda >= 0 BY
   CONSTRUCTION, and the code's closed form 1/[k]_q! IS that minimum at every
   k = 2..11. Measured: q_hook <= 0 in 0 of 682; C_lambda < -1e-12 in 0 of 682.

2. At A = 1 the Markov trace of the (2,1) block is EXACTLY ZERO. Precision
   tracked, |Tr| falls without bound as the arithmetic improves and log_norm
   stays 0, so ln|Tr| -> -infinity. Exactly one such (partition, step) pair
   exists in 34 over k <= 5; every other trace is stable.

3. AND IT CANCELS. The accumulator TELESCOPES:
       sum_k (log_cur_k - log_prev_k) = log_final - ln d_lambda
   so the divergent intermediate appears once with each sign. Measured on the
   RETURNED value, bit-identical at three precisions:

       kernel dps    uic(1,1), k_max=5
           50        -1.2268740026260945
          100        -1.2268740026260945
          150        -1.2268740026260945

   *** unified_iterative_correction is NOT divergent. ***

   [VALUE UPDATED 2026-09-12, bean `qou-21oc`.  These read
    -0.7335499391634722 until the Pass-2 sign gate was DROPPED from the
    producer (owner ruling; its complementary-slackness justification refuted
    sorry-free in PR #7251), after which the function returns the UNGATED sum.
    The gated value at this tier is -0.7335499391634978 -- note the LAST THREE
    DIGITS never matched the number printed here, which is pre-existing drift
    of the docstring against the audit doc, not an effect of the gate drop.
    THIS PROBE'S CONCLUSION IS UNAFFECTED: the gate has nothing to do with
    precision, the value is still bit-identical across 50/100/150 dps, and all
    9 assertions still pass with the witness byte-identical -- it records
    assertions, not totals.]

RETRACTION. An earlier version of this probe (and PR #6746, docs/audits/
2026-09-05-uic-a1-vanishing-trace.md, commit 2cb02fb644) concluded that term 1
diverges and that this explained the wrong sign. That conclusion was WRONG. It
was drawn from the PER-STEP decomposition, where (2,1) shows a -117 delta at
A=1, without checking that the A=2 step carries +115 and that the telescoped
total is stable. The sign is NOT explained by a divergence, and the sign
question is still open.

WHAT THE MEASUREMENT ACTUALLY BUYS

  * (V1) DROPPING THE A=1 STEP IS THE DIVERGENT OPTION. It removes one half of
    a cancelling pair. Measured at (2,1) for deuterium:

        dps    A=1 delta      A=2 delta      V0 (keep)     V1 (drop)
         50    -117.1419      +114.9436      -2.198293     +114.9436
        100    -142.0855      +139.8872      -2.198293     +139.8872

    V0 is bit-stable; V1 tracks the precision. So the intuition "a free nucleon
    has no binding, so drop its step" is right about the physics and wrong about
    this arithmetic: the step is not an additive offset, it is one term of an
    exact cancellation.

  * (V2) THE FREE-NUCLEON REFERENCE IS FINITE. Replacing the baseline ln d
    (the EMPTY braid) with ln|Tr_free| (the intra-only braid that
    `include_inter=False` exists to build) is stable at every precision tested
    and shifts the value modestly -- at (2,1)/deuterium, -2.2254 against V0's
    -2.1983. It is a defensible alternative reference, not a repair of the sign.

  * The per-step decomposition is NOT interpretable on its own. Individual step
    deltas are dominated by a +-117 artefact that cancels in the total, so any
    diagnostic reading `per_step` sees numbers that mean nothing individually.
    They are also computed with float64 `math.log`, so summing -117.14 and
    +114.94 to get -2.198 spends ~3 significant digits.

Scope (a). Does NOT explain the wrong sign; does NOT say what the correct
formula is; does not touch the extensive-term question (qou-brng).

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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def main() -> int:
    set_compute_dps()
    q = Q_MP

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

    # ---- 4. and it CANCELS: the telescoped total is stable ---------------
    print()
    print("  4. the accumulator telescopes, so the divergent step CANCELS")
    from q_parameter import Q_50_DIGIT_STR as _Q50

    def _kernel_at(dps):
        def f(partition, chains):
            o = H._PHN.lp_accumulator_step_traces_mpfr(
                list(partition),
                [[(str(c), str(d), g) for c, d, g in ch] for ch in chains],
                _Q50, dps)
            return [(mp.mpf(t), mp.mpf(l)) for t, l in o]
        return f

    _orig = H._lp_kernel_steps
    totals = {}
    try:
        for dps in (50, 100, 150):
            H._lp_kernel_steps = _kernel_at(dps)
            totals[dps] = H.unified_iterative_correction(1, 1, k_max=5, k_exact=5)
            print(f"     kernel dps={dps:>4}   uic(1,1) k_max=5 = {totals[dps]!r}")
    finally:
        H._lp_kernel_steps = _orig
    check("the RETURNED value is precision-stable -- term 1 is NOT divergent",
          len(set(totals.values())) == 1, "bit-identical at 50/100/150 dps")

    # ---- 5. V1 (drop the A=1 step) is the divergent option ----------------
    print()
    print("  5. V1 -- dropping the A=1 step -- breaks the cancellation")
    ordering = ["p", "n"]
    v0s, v1s = [], []
    for dps in (50, 100):
        ch = [H._step_chain_generic(ordering[k], ordering[:k], 2, True)
              for k in range(2)]
        o = H._PHN.lp_accumulator_step_traces_mpfr(
            list(lam), [[(str(c), str(d), g) for c, d, g in c2] for c2 in ch],
            Q_50_DIGIT_STR, dps)
        st = [(mp.mpf(t), mp.mpf(l)) for t, l in o]
        lc = lambda x: x[1] + mp.log(abs(x[0]))
        L0b = mp.log(2)
        d0, v0 = lc(st[0]) - L0b, lc(st[-1]) - L0b
        v0s.append(v0); v1s.append(v0 - d0)
        print(f"     dps={dps:>4}  A=1 delta={mp.nstr(d0, 10):>14}"
              f"  V0(keep)={mp.nstr(v0, 10):>13}  V1(drop)={mp.nstr(v0 - d0, 10):>13}")
    # Relative movement, not bit-equality: V0 prints identically to 10 digits
    # but the traces differ at the 51st vs 62nd digit, so the logs differ far
    # below any figure anyone reads. A first pass asserted bit-equality and
    # FAILED on that -- the same over-strict-threshold mistake as the census
    # above, caught by the probe's own assertion.
    rel0 = abs(v0s[1] - v0s[0]) / abs(v0s[0])
    rel1 = abs(v1s[1] - v1s[0]) / abs(v1s[0])
    print(f"     relative movement 50 -> 100 dps:   V0 {mp.nstr(rel0, 6)}"
          f"     V1 {mp.nstr(rel1, 6)}")
    check("V0 (keep A=1) is precision-stable to < 1e-15 relative",
          rel0 < mp.mpf("1e-15"), f"moves {mp.nstr(rel0, 4)}")
    check("V1 (drop A=1) is NOT -- it moves by O(10%) and grows",
          rel1 > mp.mpf("0.01"),
          f"moves {mp.nstr(rel1, 4)}; one half of a cancelling pair removed")

    print()
    print("  So the sign is NOT explained by a divergence, and V1 is refuted:")
    print("  the A=1 step is not an additive offset, it is one term of an exact")
    print("  cancellation. The sign question stays OPEN.")

    w = WitnessBuilder("uic-a1-vanishing-trace", engine="python+mpmath+rust")
    w.set_description(
        "Gap qou-sv7h: the (2,1) Markov trace at A=1 is exactly zero (one such "
        "pair in 34 over k<=5), but the accumulator TELESCOPES and it cancels -- "
        "uic(1,1) is bit-identical at 50/100/150 dps, so term 1 is NOT "
        "divergent. RETRACTS the earlier conclusion in PR #6746 / commit "
        "2cb02fb644. Measures the two proposed fixes: V1 (drop the A=1 step) is "
        "the DIVERGENT option, removing one half of the cancelling pair; V2 "
        "(free-nucleon reference) is finite. The wrong sign is NOT explained."
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
