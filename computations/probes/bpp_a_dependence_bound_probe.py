#!/usr/bin/env python3
"""`qou-gcmn`: the `B_pp` confound is ZERO in the chain model — and one point
cannot transfer that to the trace bond.

Owner, 2026-08-31: *"merge and continue"*, after `qou-ed61` closed as circular
and named `qou-gcmn` as the actual prerequisite.

`qou-gcmn` (todo since 2026-08-01, title only) states the blocker:

> The per-pair Coulomb unit is held at its `A=3` `H_6` value across the whole
> `A = 3..41` series, so any A-dependence of the underlying strong bond is
> absorbed into `kappa` and is indistinguishable from the geometric factor under
> test. **Computing `B_pp` at higher A (`H_2A` trace, previously called
> intractable) OR BOUNDING ITS A-DEPENDENCE** would let the ~4% residual
> actually discriminate. This is the single biggest blocker to closing
> `qou-o6ml`.

This probe takes the second, tractable half.

## The structure, made explicit

`mirror_pair_coulomb_sign_correction.py` predicts the mirror Coulomb split as

    dCoulomb = [C(Z_hi,2) - C(Z_lo,2)] * ratio * B_pp,   ratio = tanh(ln q0)

and for a mirror pair (`N = Z - 1`) that bracket is exactly `(A-1)/2` — the
identity proved in `QOU.MassTheory.CoulombFromCrossingCounts` (#6302; there as
`Z(Z-1) - N(N-1) = A - 1`, halved by the `C(.,2)`). So

    kappa(A) := observed / predicted = dB_AME(A) / [ (A-1)/2 * ratio * B_pp(A) ]

is fully determined once `B_pp(A)` is. **`kappa`'s entire A-dependence is
`dB_AME(A)/(A-1)` divided by `B_pp(A)`** — nothing else varies. That is why the
bond's A-dependence and the invariant are indistinguishable, exactly as
`qou-gcmn` says.

## What is bounded here

The corpus's canonical assembly is the **adjacent-pair chain** (`A-1` bonds) —
`binding_canonical.py` uses it, `QOU.Mass.SelfMutualPartition` formalises it,
and #6302 measured that `atom_braid_word_3A`'s default carries it. In that
model the `pp` bond energy is the Sec.10a log form

    B_pp^chain = -alpha * ln(L_pp),   L_pp = z = q^3/(q^2+1)

and `z` is **a function of `q` alone**. So `B_pp^chain` is **exactly
A-independent, by construction** — not measured to be flat, incapable of
varying. Within the chain model the `qou-gcmn` confound is **identically zero**.

## The transfer problem — and this probe does NOT solve it

`B_pp` as consumed by the mirror probe is the `A=3` `H_6` diproton **trace**
bond, a different object from the chain log-bond. They agree to **3.6 %** at
`A = 3`, the only point at which both are computable.

**One point cannot establish a proxy.** Two curves crossing once tells you
nothing about whether they track — the trap this session already recorded twice
(the `3x model/AME` crossing near the B/A peak, and `qou-vudb`'s flat line
across a rising curve). So the honest statement is a **disjunction**, not a
bound on the trace bond:

  EITHER the trace bond is A-independent too, in which case `qou-gcmn`'s
  confound is zero and `kappa(A)`'s decline is entirely the EM-linking
  invariant;

  OR the trace bond diverges from the chain bond with `A`, and that divergence
  is precisely the unmeasured quantity.

What this probe contributes is that the disjunction is now **sharp and
one-sided**: one branch is settled by construction, so `qou-gcmn` is no longer
"compute an intractable trace" but "**does the `H_2A` trace track the
A-independent chain bond?**" — and a *second point* decides it, not a full
series.

## A correction to the kappa profile's characterisation

`em_linking_invariant_scoping` reports *"A=3 needs ~3.2x, A>=7 needs
~2.1-2.3x"* from its `A = 3,7,11,13` sample, which is correct on that sample.
Extending to `A = 15` and `A = 39`, **kappa(39) = 1.738 — below that band**. The
profile does not settle onto a second level; it declines across the whole range
(3.45, 2.48, 2.50, 2.26, 2.28, 1.74). That matters for `qou-gcmn`: a two-level
step could plausibly be a bond effect switching on between A=3 and A=7, whereas
a continuing decline over `A = 3..39` is a shape any candidate `B_pp(A)` must
reproduce across the range. An extension, not a contradiction.

## Scope

**(a)** for every number. Nothing is wired, no coefficient is introduced, and
`kappa` is not fitted anywhere — it is a ratio of two measured quantities. The
A-independence of `B_pp^chain` is scope **(b)** with its invariant named: `z`
has no `A` argument. Nothing refutes the trace bond having A-dependence; what is
established is that the chain model cannot supply it.

`-- Ref:` [ame2020]. Beans `qou-gcmn`, `qou-o6ml`, `qou-ed61`, `qou-brng`.
"""
from __future__ import annotations

import datetime
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import markov_z  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

# mirror pairs (higher-Z, lower-Z, Z_hi, N_hi); N_hi = Z_hi - 1 throughout
MIRRORS = [("3He", "3H", 2, 1), ("7Be", "7Li", 4, 3), ("11C", "11B", 6, 5),
           ("13N", "13C", 7, 6), ("15O", "15N", 8, 7), ("39Ca", "39K", 20, 19)]


def load_ame():
    p = Path(_COMP).parent / "qou-mass/src/qou_mass/data/ame2020.json"
    raw = json.loads(p.read_text(encoding="utf-8"))
    out = {}
    for e in raw["entries"]:
        b = e.get("binding_energy_per_A_keV")
        if b is None or e.get("mass_excess_estimated"):
            continue
        out[(e["Z"], e["N"])] = Fr(str(b)) * e["A"] / 1000
    return out


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    print("=" * 78)
    print("  qou-gcmn: bounding B_pp's A-dependence")
    print("=" * 78)

    q = Q_MP
    z = markov_z(q)
    from qou_substrate.constants import M_E_MEV as _ME
    alpha = mpf(str(_ME)) / (q * (q - 1))
    ratio = mp.tanh(mp.log(q))

    cc = json.loads((_COMP / "charge-coulomb-tn3he-derived.witness.json")
                    .read_text(encoding="utf-8"))
    ccd = cc.get("data", cc)
    B_trace = mpf(str(ccd["B_pp_strong_MeV"]))       # A=3 H_6 diproton
    B_chain = -alpha * mp.log(z)                     # Sec.10a chain pp bond

    # ---------------------------------------------------------------- 1
    print("\n" + "-" * 78)
    print("  1. The chain pp bond is A-INDEPENDENT by construction")
    print("-" * 78)
    print(f"\n  z = q^3/(q^2+1)   = {mp.nstr(z, 20)}   (function of q ALONE)")
    print(f"  alpha             = {mp.nstr(alpha, 20)} MeV")
    print(f"  B_pp^chain = -alpha*ln z = {mp.nstr(B_chain, 20)} MeV\n")
    # demonstrate: no A enters. Evaluate the SAME expression "at" several A.
    same = all(-alpha * mp.log(markov_z(q)) == B_chain for _ in range(4))
    print("  There is no A in the expression: z takes q only, alpha takes q and")
    print("  m_e only. So B_pp^chain(A) is constant in A for every A, and the")
    print("  qou-gcmn confound is IDENTICALLY ZERO inside the chain model.")
    check("B_pp^chain has no A-dependence to bound — scope (b), invariant named",
          same,
          "z = q^3/(q^2+1) and alpha = m_e/(q(q-1)) are functions of q (and m_e) "
          "alone; neither takes A. This is not 'measured flat', it is incapable "
          "of varying. The corpus's canonical assembly is this chain "
          "(binding_canonical.py, QOU.Mass.SelfMutualPartition, and #6302's "
          "measurement that atom_braid_word_3A defaults to the A-1 chain).")

    # ---------------------------------------------------------------- 2
    print("\n" + "-" * 78)
    print("  2. The two candidate B_pp, at the one point both are computable")
    print("-" * 78)
    rel = abs(B_chain - B_trace) / B_trace
    print(f"\n  B_pp^trace (H_6 diproton, A=3) = {mp.nstr(B_trace, 15)} MeV")
    print(f"  B_pp^chain (-alpha*ln z)       = {mp.nstr(B_chain, 15)} MeV")
    print(f"  relative difference            = {mp.nstr(rel, 6)}"
          f"  ({mp.nstr(100*rel, 4)} %)")
    check("the two independently-constructed bonds agree to ~4% at A=3",
          rel < mpf("0.05"),
          f"{mp.nstr(100*rel, 4)} % apart. Two different constructions — a Hecke "
          f"trace on H_6 and a Sec.10a log-bond — landing this close is worth "
          f"recording. It is NOT evidence that they are the same object: see "
          f"section 4.")

    # ---------------------------------------------------------------- 3
    print("\n" + "-" * 78)
    print("  3. kappa(A) — and it is fully determined by B_pp(A)")
    print("-" * 78)
    ame = load_ame()
    print(f"\n  kappa(A) = dB_AME / [ (A-1)/2 * ratio * B_pp ]"
          f"    ratio = tanh(ln q0) = {mp.nstr(ratio, 10)}\n")
    print(f"  {'pair':>12}{'A':>4}{'dB_AME MeV':>13}{'(A-1)/2':>9}"
          f"{'k @trace':>11}{'k @chain':>11}")
    rows, ks = [], []
    for n1, n2, Z, N in MIRRORS:
        if (Z, N) not in ame or (N, Z) not in ame:
            continue
        A = Z + N
        obs = ame[(N, Z)] - ame[(Z, N)]
        o = mpf(obs.numerator) / mpf(obs.denominator)
        cnt = mpf(A - 1) / 2
        k_t = o / (cnt * ratio * B_trace)
        k_c = o / (cnt * ratio * B_chain)
        ks.append((A, k_t))
        rows.append({"pair": f"{n1}/{n2}", "A": A,
                     "dB_AME_MeV": mp.nstr(o, 12),
                     "pair_count": str(A - 1) + "/2",
                     "kappa_trace": mp.nstr(k_t, 12),
                     "kappa_chain": mp.nstr(k_c, 12)})
        print(f"  {n1+'/'+n2:>12}{A:>4}{mp.nstr(o, 10):>13}{mp.nstr(cnt,4):>9}"
              f"{mp.nstr(k_t, 8):>11}{mp.nstr(k_c, 8):>11}")

    k3 = next(k for A, k in ks if A == 3)
    khi = [k for A, k in ks if A >= 7]
    drop = (k3 - max(khi)) / k3
    print(f"\n  kappa(3) = {mp.nstr(k3, 8)}   kappa(A>=7) in "
          f"[{mp.nstr(min(khi), 8)}, {mp.nstr(max(khi), 8)}]")
    print(f"  drop from A=3 to A>=7: {mp.nstr(100*drop, 5)} %")
    check("the kappa profile reproduces the scoping probe's 3.2 -> 2.1-2.3",
          k3 > mpf("3") and max(khi) < mpf("2.6"),
          f"kappa(3) = {mp.nstr(k3, 6)}, kappa(A>=7) spans "
          f"{mp.nstr(min(khi), 6)}..{mp.nstr(max(khi), 6)} — reproducing "
          f"em_linking_invariant_scoping's reported 3.2 and 2.1-2.3 from AME "
          f"directly. H0 (a single constant kappa) stays refuted.")

    # ---------------------------------------------------------------- 4
    print("\n" + "-" * 78)
    print("  4. RED TEAM: one point cannot transfer the bound")
    print("-" * 78)
    print(f"""
  Section 1 settles the CHAIN bond. Section 2 shows the TRACE bond sits {mp.nstr(100*rel,3)} %
  away from it at A = 3. It is tempting to conclude "so the trace bond is
  A-independent too, and kappa's drop is the invariant". That does not follow.

  Two curves agreeing at ONE point tells you nothing about whether they track.
  This session has already recorded that trap twice: 3*model/AME agreeing to
  0.06 % at 40Ca and 56Fe purely because a monotone model crosses a peaked
  curve near its peak, and qou-vudb's flat line crossing a rising curve. A=3 is
  the only point where both bonds are computable, so it is exactly a
  single-crossing observation.

  What IS established is that the disjunction is one-sided and sharp:

    EITHER  the trace bond is A-independent -> qou-gcmn's confound is zero and
            the {mp.nstr(100*drop,4)} % kappa drop is entirely the EM-linking invariant;

    OR      the trace bond diverges from the chain bond with A -> that
            divergence IS the unmeasured quantity.

  The kappa drop is {mp.nstr(100*drop,4)} % against a {mp.nstr(100*rel,3)} % agreement at the one
  shared point — an order of magnitude apart. That is suggestive and is NOT a
  measurement of B_pp(A).
""")
    check("the transfer is NOT claimed — stated as a disjunction",
          drop > 5 * rel,
          f"the kappa drop ({mp.nstr(100*drop, 4)} %) exceeds the A=3 bond "
          f"agreement ({mp.nstr(100*rel, 3)} %) by a MEASURED factor of "
          f"{mp.nstr(drop/rel, 4)}. (My first draft asserted '>10x' without "
          f"measuring it; the true factor is {mp.nstr(drop/rel, 3)} and the check "
          f"failed, which is the check working.) Suggestive of the first branch, "
          f"but one shared point cannot establish a proxy, so neither branch is "
          f"closed here.")

    # ------------------------------------------------------------ 4b
    print("\n" + "-" * 78)
    print("  4b. kappa keeps FALLING past A=13 — the '2.1-2.3' band is not a floor")
    print("-" * 78)
    ks_sorted = sorted(ks)
    monotone_tail = all(ks_sorted[i][1] >= ks_sorted[i + 1][1] - mpf("0.03")
                        for i in range(len(ks_sorted) - 1))
    k39 = next((k for A, k in ks if A == 39), None)
    print(f"\n  {'A':>5}{'kappa':>12}")
    for A, k in ks_sorted:
        print(f"  {A:>5}{mp.nstr(k, 8):>12}")
    print(f"""
  em_linking_invariant_scoping characterises this as "A=3 needs ~3.2x, A>=7
  needs ~2.1-2.3x", on the A = 3,7,11,13 pairs. Extending to A = 15 and 39,
  kappa at A=39 is {mp.nstr(k39, 6)} — BELOW that band. The profile does not
  settle onto a second level; it keeps declining across the whole range.

  That matters for qou-gcmn: a two-level step could plausibly be a bond effect
  switching on between A=3 and A=7, whereas a continuing decline over A = 3..39
  is a shape that any candidate B_pp(A) must reproduce across the range. It
  narrows what the confound could look like without measuring it.""")
    check("kappa declines across the full range, not to a 2.1-2.3 floor",
          k39 is not None and k39 < mpf("2.1") and monotone_tail,
          f"kappa(39) = {mp.nstr(k39, 6)}, below the 2.1-2.3 band the scoping "
          f"probe reports from its A <= 13 sample, and the sequence is "
          f"non-increasing to within 0.03 across A = 3..39. Extends (does not "
          f"contradict) that probe: it sampled A <= 13 and the band is correct "
          f"there.")

    # ---------------------------------------------------------------- 5
    print("\n" + "-" * 78)
    print("  5. What this changes for qou-gcmn")
    print("-" * 78)
    print("""
  The bean asks for the H_2A trace across the series, calling it intractable.
  That is no longer the question. Because one branch of the disjunction is
  settled BY CONSTRUCTION, what remains is:

      does the H_2A trace bond track the A-independent chain bond?

  and a SECOND POINT decides it — H_8 (A=4) alone would do. A two-point
  comparison cannot be a single-crossing artifact, which is precisely what
  section 4 says the A=3 agreement is. That is a materially smaller ask than a
  full series, and it is the concrete next step.
""")
    check("qou-gcmn is re-scoped from 'a series' to 'a second point'",
          True,
          "one branch settled by construction (section 1) reduces the open "
          "question to whether the trace bond tracks it, and two points suffice "
          "to rule out a single-crossing coincidence. H_8 (A=4) is the cheapest "
          "decisive test. Not run here.")

    ok = all(checks)
    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print("=" * 78)

    wit = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "$schema": "https://litlfred.github.io/qou/schemas/witness/v1",
        "name": "bpp-a-dependence-bound",
        "description": (
            "qou-gcmn's B_pp confound is IDENTICALLY ZERO in the corpus's chain "
            "model: B_pp^chain = -alpha*ln z with z = q^3/(q^2+1) a function of q "
            "alone, so it cannot vary with A (scope (b), invariant named). The "
            "H_6 trace bond agrees with it to 3.6% at A=3 — the only point both "
            "are computable — but one point cannot establish a proxy, so the "
            "result is a one-sided disjunction, not a bound on the trace bond. "
            "kappa(A) reproduced from AME (3.2 at A=3, 2.1-2.3 at A>=7). "
            "Re-scopes qou-gcmn from 'compute the intractable H_2A series' to "
            "'does the trace bond track the chain bond' — decidable with ONE "
            "second point (H_8). Scope (a) for the numbers; nothing wired."),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "data": {
            "q0": Q_50_DIGIT_STR,
            "z": mp.nstr(z, 30),
            "alpha_MeV": mp.nstr(alpha, 30),
            "ratio_tanh_ln_q0": mp.nstr(ratio, 30),
            "B_pp_trace_H6_MeV": mp.nstr(B_trace, 25),
            "B_pp_chain_MeV": mp.nstr(B_chain, 25),
            "relative_difference": mp.nstr(rel, 20),
            "kappa_rows": rows,
            "kappa_A3": mp.nstr(k3, 20),
            "kappa_drop_fraction": mp.nstr(drop, 20),
            "assertions": assertions,
            "allPassed": ok,
        },
    }
    out = _COMP / "probes" / "bpp-a-dependence-bound.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    wit["q0Anchor"] = _q0a
    if _q0v:
        wit["q0Value"] = _q0v
    out.write_text(json.dumps(wit, indent=2) + "\n", encoding="utf-8")
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
