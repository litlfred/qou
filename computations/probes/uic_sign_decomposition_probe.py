#!/usr/bin/env python3
"""The ungated UIC sum decomposed by sign: at A = 2 the positive mass vanishes.

Bean `qou-21oc`.  The Pass-2 sign gate was dropped on 2026-09-12 (owner ruling;
its complementary-slackness justification refuted sorry-free in PR #7251), and
`unified_iterative_correction` now sums over every enumerated partition.  The
sum is still wrong-signed against AME2020, and THAT is what this probe is about.

WHAT IS SUMMED
==============
    S = sum_lambda  C_lambda * L_lambda,
    L_lambda = l_lambda + ln|t_lambda| - ln d_lambda

where `(t, l)` are the final trace and the ACCUMULATED log returned by
`lp_accumulator_step_traces_mpfr`, and `C_lambda = C_lambda_resolvent_MeV`.
Note the `l`: `L` is NOT simply `ln|tr| - ln d`, and an earlier framing of this
quantity that dropped `l` is wrong.  `C_lambda >= 0` on every partition
(re-checked here), so `sign(term) = sign(L)` and the question "why is S < 0" is
exactly "why does the negative-L mass outweigh the positive-L mass".

THE RESULT AT A = 2
===================
The positive mass is zero TO THE PRECISION OF THE ARITHMETIC, at every
truncation tested -- about 74 orders of magnitude below |S|:

    cap |lambda|    blocks with L > 0    all one-dim    all C ~ 0    P
    ------------    -----------------    -----------    ---------   ------------
         <= 6               5                yes           yes       0 (exact)
         <= 8               7                yes           yes      -6.3e-74
         <= 10              9                yes           yes      -9.6e-74

**Do not say "exactly zero".**  Of the 28 one-dimensional blocks in the table,
16 carry `C` exactly 0 and 12 carry a residue at ~1e-74, some of it NEGATIVE
(which is why P is a small negative number rather than a small positive one).
That is the signature of an EXACT cancellation evaluated at 70 dps: the corpus
states the subtrahend `1/[k]_q!` equals `min_lambda (w_lambda / d_lambda)`, and
a difference of two equal quantities computed to finite precision lands on the
floor, not on zero.  So `C_lambda >= 0` and `P = 0` are both true to working
precision and neither is established exactly by this computation.

Every block with `L > 0` at 2H is a one-dimensional ROW partition `(k)` -- and
those are exactly the blocks the weight annihilates.  The mechanism is already
in the corpus: `prop:unified-iterative-correction` states that the subtrahend
`1/[k]_q!` equals `min_lambda (w_lambda / d_lambda)`, so it kills the two
one-dimensional blocks `(k)` and `(1^k)` at every level and nothing else.  What
is new here is that at A = 2 the annihilated set and the positive-L set
COINCIDE, so `S < 0` is forced rather than observed.

SCOPE -- THIS IS (a), NOT (b), AND IT DOES NOT GENERALISE
=========================================================
Three limits, asserted rather than left implicit:

1. **Measured, not proved.**  Verified at caps 6, 8, 10; `L > 0 => lambda
   one-dimensional` is not established for all k.  Proving it would make the
   A = 2 exclusion scope-(b); until then this is a scope-(a) negative.
2. **FALSE at A >= 3.**  At 4He and 6Li the blocks `(2,1)` and `(2,2)` have
   `L > 0` AND `C > 0`, so P > 0 there -- just 21-68x too small.  This probe
   asserts that explicitly so the A = 2 headline cannot be read as general.
3. **This is the probe's own reconstruction**, over partitions with
   `|lambda| <= cap` and the ordering `["p"]*Z + ["n"]*N`, NOT the producer's
   return.  It is validated against the producer at the one point they agree:
   cap <= 6 gives -2.251132, against the producer's k=6 row
   -2.251131977321312.  Do NOT quote these sums as
   `unified_iterative_correction` values.

NOT AN ENTANGLEMENT RESULT.  `computations/meson/binding_cut_entropy_sign_is_forced_probe.py`
also concludes "the sign is forced", about a DIFFERENT quantity -- entanglement
entropy across the proton|neutron cut, where positivity is a theorem.  The two
have nothing to do with each other; they are cross-referenced here only so a
reader does not conflate them.

Precision: mpmath end to end at the repo compute dps; no float() anywhere on a
computed path, per AGENTS.md NO-FLOAT64 (which binds probes as hard as
producers).

-- Ref: [manuscript] content/quantum-observable-universe/mass-theory/unified-iterative-correction.md
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.dirname(_HERE)
for _p in (_COMP, os.path.join(_COMP, "..", "tools", "qou-substrate", "python"),
           os.path.join(_COMP, "..", "tools", "pyhecke", "python")):
    _a = os.path.abspath(_p)
    if _a not in sys.path:
        sys.path.insert(0, _a)

from mpmath import mp  # noqa: E402
import hecke_core_legacy as H  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

ATOMS = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"), (3, 3, "6Li")]
CAPS_2H = (6, 8, 10)
ZERO = mp.mpf("1e-40")
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def is_one_dimensional(lam: tuple[int, ...]) -> bool:
    """The row `(k)` and the column `(1^k)` -- the two blocks with dim 1."""
    return len(lam) == 1 or all(part == 1 for part in lam)


def block_L(entry: dict, ordering: list[str]) -> mp.mpf:
    """L_lambda = l + ln|t| - ln d, from the accumulator's final step."""
    lam = tuple(entry["partition"])
    chains = [H._step_chain_generic(ordering[k], ordering[:k], sum(lam) - 1, True)
              for k in range(len(ordering))]
    out = H._PHN.lp_accumulator_step_traces_mpfr(
        list(lam),
        [[(str(c), str(d), g) for c, d, g in ch] for ch in chains],
        Q_50_DIGIT_STR, 50)
    t, l = mp.mpf(out[-1][0]), mp.mpf(out[-1][1])
    return l + mp.log(abs(t)) - mp.log(entry["dim"])


def main() -> int:
    set_compute_dps()
    print("=" * 74)
    print("  The ungated UIC sum by sign: at A = 2 the positive mass vanishes")
    print("=" * 74)
    print()

    table = H._partition_table()
    negative_scale = [e for e in table
                      if mp.mpf(str(e["C_lambda_resolvent_MeV"])) < -ZERO]
    check(f"C_lambda >= 0 on every partition, to tolerance {mp.nstr(ZERO, 2)}",
          not negative_scale, f"0 of {len(table)} below -{mp.nstr(ZERO, 2)}")
    # The tolerance is load-bearing and is reported, not hidden: some weights are
    # a cancellation residue at ~1e-74 and a few of those are NEGATIVE. Exact
    # non-negativity is NOT established here.
    one_dim_all = [e for e in table if is_one_dimensional(tuple(e["partition"]))]
    od_exact = [e for e in one_dim_all
                if mp.mpf(str(e["C_lambda_resolvent_MeV"])) == 0]
    od_resid = [e for e in one_dim_all if e not in od_exact]
    od_max = max((abs(mp.mpf(str(e["C_lambda_resolvent_MeV"]))) for e in od_resid),
                 default=mp.mpf(0))
    print(f"    one-dimensional blocks: {len(one_dim_all)}  "
          f"(C exactly 0: {len(od_exact)}; C a residue: {len(od_resid)}, "
          f"max |C| = {mp.nstr(od_max, 4)})")
    check("the one-dimensional blocks' weights are zero to the compute floor "
          "(exact cancellation at finite precision, NOT proved exact)",
          od_max < mp.mpf("1e-70"), f"max |C| = {mp.nstr(od_max, 4)}")

    # ---- per-atom decomposition at the common cap -------------------------
    ents6 = [e for e in table if sum(e["partition"]) <= 6]
    print()
    print("  per-atom, cap |lambda| <= 6:")
    print(f"    {'atom':>5} {'P (pos)':>14} {'N (neg)':>14} {'S = P+N':>14}"
          f" {'|N|/P':>9} {'n+':>3} {'n-':>3} {'top1/|N|':>9}")
    rows = []
    for Z, N_, name in ATOMS:
        ordering = ["p"] * Z + ["n"] * N_
        P = mp.mpf(0); NEG = mp.mpf(0); npos = nneg = 0
        neg_mags = []
        for e in ents6:
            L = block_L(e, ordering)
            C = mp.mpf(str(e["C_lambda_resolvent_MeV"]))
            if L > 0:
                P += C * L; npos += 1
            elif L < 0:
                NEG += C * L; nneg += 1
                neg_mags.append(abs(C * L))
        S = P + NEG
        top1 = (max(neg_mags) / abs(NEG)) if neg_mags and NEG != 0 else mp.mpf(0)
        ratio = (abs(NEG) / P) if P > ZERO else None
        rows.append({
            "atom": name, "A": Z + N_, "P": fmt(P), "N": fmt(NEG), "S": fmt(S),
            "n_positive_L": npos, "n_negative_L": nneg,
            "abs_N_over_P": (fmt(ratio) if ratio is not None else "infinite (P = 0)"),
            "top1_share_of_abs_N": fmt(top1),
        })
        print(f"    {name:>5} {mp.nstr(P, 7):>14} {mp.nstr(NEG, 7):>14}"
              f" {mp.nstr(S, 7):>14}"
              f" {(mp.nstr(ratio, 5) if ratio is not None else 'inf'):>9}"
              f" {npos:>3} {nneg:>3} {mp.nstr(100 * top1, 3) + '%':>9}")

    d = {r["atom"]: r for r in rows}
    check("every atom's ungated sum is negative",
          all(mp.mpf(r["S"]) < 0 for r in rows))
    check("at 2H the positive mass P is zero to the compute floor",
          abs(mp.mpf(d["2H"]["P"])) < mp.mpf("1e-70"),
          f"P = {d['2H']['P']}")
    # The honest negative: the A=2 result does NOT generalise.
    heavier = [r for r in rows if r["A"] >= 3]
    check("at A >= 3 the positive mass is NONZERO -- the A=2 result does NOT "
          "generalise", all(mp.mpf(r["P"]) > ZERO for r in heavier),
          ", ".join(f"{r['atom']} P={mp.nstr(mp.mpf(r['P']), 4)}" for r in heavier))
    check("at A >= 3 the negative mass still outweighs the positive by > 20x",
          all(abs(mp.mpf(r["N"])) / mp.mpf(r["P"]) > 20 for r in heavier),
          ", ".join(f"{r['atom']} {mp.nstr(abs(mp.mpf(r['N'])) / mp.mpf(r['P']), 4)}x"
                    for r in heavier))
    check("no single block carries more than 25% of |N| -- the sign is not one "
          "outlier", all(mp.mpf(r["top1_share_of_abs_N"]) < mp.mpf("0.25")
                         for r in rows),
          "max " + mp.nstr(100 * max(mp.mpf(r["top1_share_of_abs_N"]) for r in rows), 3) + "%")

    # ---- the A = 2 structure, across truncations --------------------------
    print()
    print("  2H across truncations -- is P = 0 an artifact of the cap?")
    ordering_2h = ["p", "n"]
    sweep = []
    for cap in CAPS_2H:
        ents = [e for e in table if sum(e["partition"]) <= cap]
        P = mp.mpf(0); NEG = mp.mpf(0)
        pos_blocks = []
        for e in ents:
            L = block_L(e, ordering_2h)
            C = mp.mpf(str(e["C_lambda_resolvent_MeV"]))
            if L > 0:
                P += C * L
                pos_blocks.append((tuple(e["partition"]), C, e["dim"]))
            elif L < 0:
                NEG += C * L
        all_1d = all(is_one_dimensional(lam) for lam, _C, _dim in pos_blocks)
        all_annihilated = all(C <= ZERO for _lam, C, _dim in pos_blocks)
        sweep.append({
            "cap_abs_lambda": cap, "n_partitions": len(ents),
            "n_positive_L": len(pos_blocks),
            "positive_L_all_one_dimensional": all_1d,
            "positive_L_all_zero_weight": all_annihilated,
            "P": fmt(P), "S": fmt(P + NEG),
            "positive_L_blocks": [list(lam) for lam, _C, _dim in pos_blocks],
        })
        print(f"    cap<={cap:<3} n={len(ents):<4} L>0: {len(pos_blocks):<2}"
              f"  all 1-dim: {str(all_1d):<5}  all C=0: {str(all_annihilated):<5}"
              f"  P={mp.nstr(P, 5):>6}  S={mp.nstr(P + NEG, 8):>12}")

    check("at 2H every block with L > 0 is ONE-DIMENSIONAL, at every cap",
          all(s["positive_L_all_one_dimensional"] for s in sweep),
          f"caps {list(CAPS_2H)}")
    check("at 2H every block with L > 0 has C_lambda = 0 -- the positive set is "
          "exactly the annihilated set", all(s["positive_L_all_zero_weight"] for s in sweep))
    ratios = [abs(mp.mpf(s["P"])) / abs(mp.mpf(s["S"])) for s in sweep]
    check("at 2H |P| / |S| is at the compute floor at every cap, so S < 0 is "
          f"FORCED to that precision (scope-(a): measured to |lambda| <= "
          f"{max(CAPS_2H)}, not proved)",
          all(r < mp.mpf("1e-60") for r in ratios),
          "max |P|/|S| = " + mp.nstr(max(ratios), 4))

    # ---- validation against the producer ----------------------------------
    producer_k6 = mp.mpf("-2.251131977321312")
    mine_cap6 = mp.mpf(sweep[0]["S"])
    agree = abs(mine_cap6 - producer_k6) < mp.mpf("1e-6")
    check("the reconstruction matches the producer where they agree "
          "(2H, k = 6)", agree,
          f"{mp.nstr(mine_cap6, 10)} against {mp.nstr(producer_k6, 10)}")

    # ---- truncation growth -------------------------------------------------
    mags = [abs(mp.mpf(s["S"])) for s in sweep]
    monotone = all(b > a for a, b in zip(mags, mags[1:]))
    print()
    print("  |S| across caps: " + " -> ".join(mp.nstr(m, 7) for m in mags))
    check("|S| grows monotonically with the truncation over the measured range "
          "-- NO evidence of convergence (not a divergence claim)", monotone)

    w = WitnessBuilder("uic-sign-decomposition", engine="python+mpmath+rust")
    w.set_description(
        "Bean qou-21oc: the ungated unified_iterative_correction sum decomposed "
        "by sign. C_lambda >= 0 on every partition, so sign(term) = sign(L) with "
        "L = l + ln|t| - ln d (note the ACCUMULATED l: L is NOT ln|tr| - ln d). "
        "At A = 2 the positive mass is zero TO THE COMPUTE FLOOR at caps |lambda| <= 6, 8, 10 (|P|/|S| < 1e-70; NOT exactly zero -- 12 of 28 one-dimensional blocks carry a cancellation residue at ~1e-74, some negative): "
        "every block with L > 0 is a one-dimensional row partition (k), which is "
        "exactly the set the subtrahend 1/[k]_q! annihilates, so S < 0 is FORCED "
        "rather than observed. SCOPE-(a), NOT (b): measured to |lambda| <= 10, "
        "not proved for all k. It does NOT generalise -- at A >= 3 the blocks "
        "(2,1) and (2,2) carry L > 0 with C > 0, so P > 0, merely 21-68x too "
        "small. These sums are the PROBE'S OWN reconstruction, not the "
        "producer's return; validated against it at 2H k=6 only."
    )
    w.set_audit_only("docs/audits/2026-09-14-uic-sign-decomposition-at-a2.md")
    w.add_data("per_atom_cap6", rows)
    w.add_data("two_h_truncation_sweep", sweep)
    w.add_data("scope", {
        "classification": "scope-(a) negative -- measured, not proved",
        "proved_for_all_k": False,
        "generalises_beyond_A2": False,
        "what_would_make_it_scope_b":
            "A proof that L_lambda(A=2) > 0 implies lambda is one-dimensional. "
            "Then the positive set is contained in the annihilated set for all "
            "k and S < 0 at deuterium becomes a structural exclusion.",
        "reconstruction_not_producer":
            "Sums are over |lambda| <= cap with ordering ['p']*Z + ['n']*N and "
            "one kernel call per partition; the producer uses the alternating "
            "ground-state ordering and its own k_exact ladder. Agreement is "
            "checked at 2H k=6 only.",
        "not_the_entanglement_result":
            "computations/meson/binding_cut_entropy_sign_is_forced_probe.py "
            "concludes 'the sign is forced' about entanglement entropy across "
            "the proton|neutron cut, where positivity is a theorem. Unrelated.",
    })
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_sign_decomposition_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
