#!/usr/bin/env python3
"""The 3x binding shortfall is NEITHER an extensivity failure NOR a coefficient.

Owner, 2026-08-30: *"investigate next qou-brng -- the 3x absolute shortfall is
now the only thing left standing between the model and the binding table, and
it's assembly-level, not bond-level."*

It is assembly-level. It is **not** the extensivity problem the corpus has been
calling it, and it is **not** repairable by any constant either -- and those are
three different diagnoses that this arc has been treating as one. The measured
answer is the third: a SHAPE mismatch whose missing piece is an object the
corpus has already proved the crossing counts cannot supply.

## Where the framing was wrong

`bond_rule_dashboard_comparison_probe` -- my own, merged earlier today --
reported "both rules are ~3x short for A >= 4" and attributed it to "the
extensivity problem (`qou-brng`)". **That attribution is wrong**, and the
numbers it printed already said so once read as a sequence in A:

    12C 0.348036   16O 0.342994   40Ca 0.333159   56Fe 0.333638

That converges; it does not decay. An extensivity deficit (model ~ A^p, p < 1,
against an extensive AME) sends the ratio to ZERO. This one is bounded below by
0.307 across the whole table and, past A ~ 62, RISES again.

The reason is structural and needs no measurement: the chain assembly lays down
exactly `A - 1` bonds, so

    B_model = -alpha * [ (Z-1) ln f_pp + ln f_pn + (N-1) ln f_nn ]

is **affine in (Z, N)** -- both second differences vanish identically -- and
`B_model / A` therefore tends to a constant. This assembly never had an
extensivity deficit to begin with.

## And it is not a coefficient either

The tempting next move is "then it is one missing constant near 3". Two
independent measurements refuse it:

1. **Monotone vs peaked (section 7, the decisive one).** `B_model/A` is
   strictly increasing in A along `N = Z` and bounded above by its limit, so it
   can never turn over. The AME `B/A` turns over at `62Ni`. Multiplying by any
   positive constant preserves monotonicity, so **no** constant reproduces the
   fall. This is a shape exclusion and it needs no fit.

2. **The deuteron (section 6).** The bare model already OVER-binds `2H` by
   1.27x. Tripling puts it at 3.82x. So whatever supplies ~3 at large A must
   vanish at A = 2; it is not a uniform per-bond multiplicity.

## The peak-matching trap, recorded as a negative

3x the model agrees with AME to **0.06% at 56Fe and 0.06% at 40Ca**, and
disagrees by 4% at 12C, 18% at 208Pb, 40% at 7Li. That is precisely what a
constant-`B/A` model does against a curve that rises, peaks and falls: it can
only CROSS, and it crosses near the peak. The agreement at A ~ 40-56 is
therefore **not evidence** for a factor 3, however sharp it looks. Same trap
AGENTS.md records for R3 of this very bean (the 0.954*hbar_q^2 "saturation"
that is a match to the empirical B/A peak, not to a fundamental coefficient)
and for `qou-vudb` (a flat line crossing a rising curve). Written down so the
next reader does not have to rediscover it -- I nearly quoted the 0.06% as a
result.

## What the missing piece is

The fall past `62Ni` is the Coulomb term, which counts proton PAIRS `Z(Z-1)`.
`QOU.MassTheory.CrossingCountAffine.no_crossing_combination_is_protonPairs`
(merged today, sorry-free) proves no linear functional of the crossing counts is
`Z(Z-1)` -- second difference 2 against 0. So the object missing from the
binding table is the SAME object that theorem excludes, reached from a different
side: that theorem was measured against mirror splittings, this is the absolute
table.

Scope **(a)** for every numerical statement here; the shape exclusion in section
7 is scope **(b)** with its invariant named (monotonicity of an affine-in-(Z,N)
functional divided by A). Nothing is wired, no coefficient is introduced.

`-- Ref:` [ame2020]. Beans `qou-brng`, `qou-0c19`, `qou-nial`.
"""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, interface_factor, markov_z  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

# The same 12 nuclei the dashboard probe uses, so the two are directly
# comparable, plus the heavy end where B/A has turned over.
NUCLEI = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
          ("6Li", 3, 3), ("7Li", 3, 4), ("7Be", 4, 3), ("9Be", 4, 5),
          ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20), ("56Fe", 26, 30),
          ("62Ni", 28, 34), ("90Zr", 40, 50), ("120Sn", 50, 70),
          ("208Pb", 82, 126), ("238U", 92, 146)]

# The isobaric symmetric line, where the closed form is exact. Even A only.
SYMMETRIC_A = [4, 8, 12, 16, 20, 40, 60, 100, 200, 1000, 10000]


def load_ame():
    p = Path(_COMP).parent / "qou-mass/src/qou_mass/data/ame2020.json"
    raw = json.loads(p.read_text(encoding="utf-8"))
    out = {}
    for e in raw["entries"]:
        b = e.get("binding_energy_per_A_keV")
        if b is None or e.get("mass_excess_estimated"):
            continue
        # exact decimal text -> mpf, never through float
        out[(e["Z"], e["N"])] = mpf(str(b)) * e["A"] / 1000
    return out


def main() -> int:
    q = Q_MP
    h = hecke_h(q)
    z = markov_z(q)
    d = flavor_split_leading(q)
    from qou_substrate.constants import M_E_MEV as _ME
    alpha = mpf(str(_ME)) / (q * (q - 1))

    f_pp = interface_factor("positive", q)
    f_pn = z - h * (mpf(1) / 2 - d / 4)
    f_nn = interface_factor("negative", q)
    F = {"pp": f_pp, "pn": f_pn, "nn": f_nn}

    def B(Z, N):
        """Sec.10a log form on the CHAIN p^Z n^N: Z-1 pp, one pn, N-1 nn."""
        tot = mpf(0)
        for cnt, key in ((Z - 1, "pp"), (1, "pn"), (N - 1, "nn")):
            if cnt > 0:
                tot += cnt * (-alpha * mp.log(F[key]))
        return tot

    ame = load_ame()
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    print("=" * 78)
    print("  The 3x shortfall: not extensivity, not a coefficient -- a SHAPE")
    print("=" * 78)
    print(f"\n  alpha  = {mp.nstr(alpha, 20)} MeV")
    print(f"  f_pp   = {mp.nstr(f_pp, 20)}")
    print(f"  f_pn   = {mp.nstr(f_pn, 20)}")
    print(f"  f_nn   = {mp.nstr(f_nn, 20)}")

    # ---------------------------------------------------------------- 1
    # The closed-form limit on the symmetric line.
    print("\n" + "-" * 78)
    print("  1. The model's B/A limit, in closed form")
    print("-" * 78)
    limit_BA = -(alpha / 2) * mp.log(f_pp * f_nn)
    print(f"\n  N = Z = A/2  =>  B_model/A -> -(alpha/2)*ln(f_pp*f_nn)")
    print(f"                                = {mp.nstr(limit_BA, 30)} MeV/nucleon\n")
    print(f"  {'A':>7}{'B_model/A':>26}{'|diff from limit|':>22}")
    prev = None
    monotone_to_limit = True
    for A in SYMMETRIC_A:
        Zs = A // 2
        ba = B(Zs, Zs) / A
        dif = abs(ba - limit_BA)
        print(f"  {A:>7}{mp.nstr(ba, 20):>26}{mp.nstr(dif, 6):>22}")
        if prev is not None and dif > prev:
            monotone_to_limit = False
        prev = dif
    tail = abs(B(5000, 5000) / 10000 - limit_BA)
    check("model B/A converges to the closed-form limit",
          monotone_to_limit and tail < mpf("1e-3"),
          f"|B/A - limit| falls monotonically to {mp.nstr(tail, 6)} at A=10^4; "
          f"limit = {mp.nstr(limit_BA, 25)} MeV/nucleon (exact closed form)")

    # ---------------------------------------------------------------- 2
    # The ratio against AME: converging, not decaying.
    print("\n" + "-" * 78)
    print("  2. model/AME across the table -- bounded away from 0, and NON-monotone")
    print("-" * 78)
    print(f"\n  {'nuc':>7}{'A':>5}{'AME B/A':>12}{'model B/A':>12}"
          f"{'model/AME':>12}{'AME/model':>11}")
    rows = []
    for nm, Z, N in NUCLEI:
        if (Z, N) not in ame:
            continue
        A = Z + N
        a_ = ame[(Z, N)]
        m_ = B(Z, N)
        r = m_ / a_
        rows.append({"nucleus": nm, "A": A, "Z": Z, "N": N,
                     "ame_B_MeV": mp.nstr(a_, 12),
                     "ame_B_per_A_MeV": mp.nstr(a_ / A, 12),
                     "model_B_MeV": mp.nstr(m_, 12),
                     "model_B_per_A_MeV": mp.nstr(m_ / A, 12),
                     "model_over_ame": mp.nstr(r, 12),
                     "ame_over_model": mp.nstr(1 / r, 12)})
        print(f"  {nm:>7}{A:>5}{mp.nstr(a_/A, 6):>12}{mp.nstr(m_/A, 6):>12}"
              f"{mp.nstr(r, 6):>12}{mp.nstr(1/r, 6):>11}")

    ratios = [(rw["nucleus"], rw["A"], mpf(rw["model_over_ame"])) for rw in rows]
    lo = min(ratios, key=lambda t: t[2])
    hi_heavy = max([t for t in ratios if t[1] >= 62], key=lambda t: t[2])
    # An extensivity deficit sends the ratio to 0. This one is bounded away from
    # zero and NON-MONOTONE: it bottoms out near the AME peak and RISES again.
    check("model/AME does NOT decay -- bounded away from 0, with an interior "
          "minimum near the AME peak",
          min(t[2] for t in ratios) > mpf("0.25")
          and hi_heavy[2] > lo[2] + mpf("0.05"),
          f"the ratio bottoms at {mp.nstr(lo[2], 8)} ({lo[0]}, A={lo[1]}) and "
          f"RISES to {mp.nstr(hi_heavy[2], 8)} ({hi_heavy[0]}, A={hi_heavy[1]}); "
          f"never below {mp.nstr(min(t[2] for t in ratios), 8)} anywhere. An "
          f"extensivity deficit would send it monotonically to 0. It does the "
          f"opposite past A~60 -- see section 7.")

    # ---------------------------------------------------------------- 3
    # The chain is extensive BY CONSTRUCTION -- state it as an identity.
    print("\n" + "-" * 78)
    print("  3. The chain assembly is extensive by construction")
    print("-" * 78)
    # B(Z,N) is affine in (Z,N): its second difference vanishes identically.
    sec = (B(20, 20) - 2 * B(19, 20) + B(18, 20))
    sec2 = (B(20, 20) - 2 * B(20, 19) + B(20, 18))
    print(f"\n  second difference in Z at N=20 : {mp.nstr(sec, 6)}")
    print(f"  second difference in N at Z=20 : {mp.nstr(sec2, 6)}")
    check("B_model is affine in (Z,N) -- exactly A-1 bonds, no curvature",
          abs(sec) < mpf("1e-40") and abs(sec2) < mpf("1e-40"),
          f"both second differences vanish ({mp.nstr(abs(sec), 4)}, "
          f"{mp.nstr(abs(sec2), 4)}) -- so B_model/A tends to a constant and "
          f"the model has the extensive A-scaling already")

    # ---------------------------------------------------------------- 4
    # Is the constant exactly 3? No -- and the AME side has no limit.
    print("\n" + "-" * 78)
    print("  4. Is it a clean factor 3?  NO -- and the agreement is a crossing")
    print("-" * 78)
    x3 = []
    print(f"\n  {'nuc':>7}{'A':>5}{'3*model/AME':>14}")
    for rw in rows:
        v = 3 * mpf(rw["model_over_ame"])
        x3.append((rw["nucleus"], rw["A"], v))
        print(f"  {rw['nucleus']:>7}{rw['A']:>5}{mp.nstr(v, 8):>14}")
    best = min(x3, key=lambda t: abs(t[2] - 1))
    worst_heavy = max([t for t in x3 if t[1] >= 4], key=lambda t: abs(t[2] - 1))
    # The AME B/A curve rises then falls: show it has no asymptote.
    ba = [(rw["nucleus"], rw["A"], mpf(rw["ame_B_per_A_MeV"])) for rw in rows]
    peak = max(ba, key=lambda t: t[2])
    last = ba[-1]
    print(f"\n  AME B/A peaks at {peak[0]} (A={peak[1]}) = {mp.nstr(peak[2], 8)} "
          f"MeV and FALLS to {mp.nstr(last[2], 8)} at {last[0]}")
    check("the AME side has NO asymptote -- B/A rises, peaks, falls",
          peak[1] < last[1] and last[2] < peak[2],
          f"peak at A={peak[1]} ({mp.nstr(peak[2],8)} MeV/nucleon), down to "
          f"{mp.nstr(last[2],8)} at A={last[1]}. So there is no constant to "
          f"divide by: '3' is a ratio to the PEAK, not to a limit.")
    check("3x agreement is a CROSSING, not a plateau -- not evidence for 3",
          abs(best[2] - 1) < mpf("0.01") and abs(worst_heavy[2] - 1) > mpf("0.02"),
          f"3*model/AME is {mp.nstr(best[2], 8)} at {best[0]} (A={best[1]}) but "
          f"{mp.nstr(worst_heavy[2], 8)} at {worst_heavy[0]} (A={worst_heavy[1]}). "
          f"A constant-B/A model can only CROSS a rising-peaking-falling curve; "
          f"it crosses near the peak. Same trap as R3 and qou-vudb.")

    # ---------------------------------------------------------------- 5
    # What the constant actually is, at the peak, reported honestly.
    print("\n" + "-" * 78)
    print("  5. The near-3 number, stated as exactly what it is")
    print("-" * 78)
    k_peak = peak[2] / limit_BA
    print(f"\n  (AME B/A at its peak) / (model B/A limit)")
    print(f"     = {mp.nstr(peak[2], 20)} / {mp.nstr(limit_BA, 20)}")
    print(f"     = {mp.nstr(k_peak, 20)}")
    print(f"\n  distance from the integer 3 : {mp.nstr(abs(k_peak - 3), 8)}")
    print(f"  relative                    : {mp.nstr(abs(k_peak - 3)/3, 8)}")
    check("the constant is NEAR 3 but is not measurably 3",
          abs(k_peak - 3) < mpf("0.1") and abs(k_peak - 3) > mpf("1e-6"),
          f"k = {mp.nstr(k_peak, 15)}, |k - 3| = {mp.nstr(abs(k_peak-3), 8)} "
          f"({mp.nstr(100*abs(k_peak-3)/3, 6)}%). Near 3, and the comparison "
          f"point (the empirical peak) is not a fundamental quantity, so this "
          f"cannot be sharpened by measuring harder.")

    # ---------------------------------------------------------------- 6
    # The deuteron: where x3 fails outright, which is the useful constraint.
    print("\n" + "-" * 78)
    print("  6. The deuteron kills a uniform factor 3 outright")
    print("-" * 78)
    d_model = B(1, 1)
    d_ame = ame[(1, 1)]
    print(f"\n  2H   model {mp.nstr(d_model, 12)}   AME {mp.nstr(d_ame, 12)}"
          f"   model/AME {mp.nstr(d_model/d_ame, 8)}")
    print(f"       3*model = {mp.nstr(3*d_model, 12)}  -> "
          f"{mp.nstr(3*d_model/d_ame, 8)}x AME")
    check("a UNIFORM factor 3 is refuted by the deuteron (scope (a))",
          3 * d_model / d_ame > mpf("3"),
          f"the single-bond nucleus is already OVER-bound by the bare model "
          f"({mp.nstr(d_model/d_ame, 8)}x); tripling puts it at "
          f"{mp.nstr(3*d_model/d_ame, 8)}x AME. So whatever supplies the factor "
          f"near 3 at large A must VANISH at A=2 -- it is not a uniform "
          f"per-bond multiplicity.")

    # ---------------------------------------------------------------- 7
    # The SHAPE exclusion: monotone model vs peaked data. No fit needed.
    print("\n" + "-" * 78)
    print("  7. A shape exclusion no coefficient can repair")
    print("-" * 78)
    sym = [(A, B(A // 2, A // 2) / A) for A in (4, 8, 12, 16, 20, 40, 60,
                                                100, 200, 1000)]
    strictly_up = all(sym[i][1] < sym[i + 1][1] for i in range(len(sym) - 1))
    under_limit = all(v < limit_BA for _, v in sym)
    print(f"\n  model B/A along N = Z:  " +
          "  ".join(f"A={A}:{mp.nstr(v, 6)}" for A, v in sym[:6]))
    print(f"  strictly increasing in A : {strictly_up}")
    print(f"  bounded above by limit   : {under_limit}  "
          f"(limit {mp.nstr(limit_BA, 12)})")
    print(f"\n  AME B/A: rises to {mp.nstr(peak[2], 8)} at {peak[0]} (A={peak[1]}), "
          f"then FALLS to {mp.nstr(last[2], 8)} at {last[0]} (A={last[1]})")
    check("the model's B/A is MONOTONE and the data's is PEAKED -- a shape "
          "mismatch, not a coefficient one",
          strictly_up and under_limit and peak[1] < last[1] and last[2] < peak[2],
          "B_model/A increases strictly in A along N=Z and is bounded above by "
          f"{mp.nstr(limit_BA, 12)}, so it can NEVER turn over. AME B/A turns "
          f"over at A={peak[1]}. Rescaling the model by ANY positive constant "
          "preserves monotonicity, so no choice of the constant in section 5 "
          "reproduces the fall -- which is why model/AME rises again past A~60 "
          "in section 2, instead of settling.")

    print(f"\n  What supplies the fall is the Coulomb term, which goes as the")
    print(f"  number of proton PAIRS. Z(Z-1) at the two ends of the table:")
    for nm in ("40Ca", "208Pb", "238U"):
        rw = next((r for r in rows if r["nucleus"] == nm), None)
        if rw:
            Zc = rw["Z"]
            print(f"    {nm:>7}  Z={Zc:<4} Z(Z-1) = {Zc*(Zc-1):>6}")
    print("  and QOU.MassTheory.CrossingCountAffine proves NO linear functional")
    print("  of the crossing counts is Z(Z-1) -- second difference 2 vs 0. So the")
    print("  missing piece here is the SAME object that theorem excludes, met from")
    print("  the binding-table side instead of the mirror-splitting side.")

    ok = all(checks)
    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print("=" * 78)
    print("""
  VERDICT -- three diagnoses separated, and the arc had merged them.

  NOT an extensivity failure. The chain assembly is affine in (Z,N) by
  construction (both second differences vanish exactly), so B/A converges to a
  closed-form limit and model/AME is bounded below by 0.307 across A=2..238.
  A real extensivity deficit sends that ratio to zero. My own merged probe
  attributed the shortfall to extensivity; that attribution is withdrawn here.

  NOT a coefficient either. B_model/A is strictly increasing along N=Z and
  bounded above by its limit, so it cannot turn over; AME B/A turns over at
  62Ni. Multiplying by a positive constant preserves monotonicity, so NO
  constant reproduces the fall. Independently, the deuteron refuses a uniform
  factor 3 outright -- the bare model already OVER-binds it 1.27x.

  A SHAPE mismatch, and the missing shape is already characterised. What makes
  AME B/A fall is the Coulomb term, counting proton pairs Z(Z-1);
  CrossingCountAffine.no_crossing_combination_is_protonPairs proves no linear
  functional of the crossing counts is Z(Z-1). Same object, met from the
  absolute-table side instead of the mirror-splitting side.

  DO NOT QUOTE the 3x agreement. 3*model/AME is 1.0009 at 56Fe and 0.9994 at
  40Ca -- and 1.40 at 7Li, 1.18 at 208Pb. A constant-B/A model crosses a peaked
  curve near its peak; that is arithmetic, not evidence. Same trap as R3 of this
  bean and as qou-vudb.
""")

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
        "name": "assembly-shortfall-shape",
        "description": (
            "The chain-assembly binding shortfall is NEITHER an extensivity failure "
            "NOR a coefficient. B_model is affine in (Z,N) (exactly A-1 bonds) so "
            "B/A converges to -(alpha/2)ln(f_pp*f_nn) and model/AME is bounded "
            "below by 0.307 across A=2..238 -- not extensivity. B_model/A is "
            "strictly increasing along N=Z and bounded by its limit while AME B/A "
            "peaks at 62Ni and falls, so no positive constant reproduces the "
            "fall, and the deuteron refuses a uniform factor 3 outright -- not a "
            "coefficient. The missing shape is the Z(Z-1) Coulomb multiplicity "
            "that CrossingCountAffine proves the crossing counts cannot supply. "
            "Scope (a) for the numbers, (b) for the monotonicity exclusion."),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "data": {
            "q0": Q_50_DIGIT_STR,
            "alpha_MeV": mp.nstr(alpha, 30),
            "bond_factors": {"f_pp": mp.nstr(f_pp, 30),
                             "f_pn": mp.nstr(f_pn, 30),
                             "f_nn": mp.nstr(f_nn, 30)},
            "model_B_per_A_limit_MeV": mp.nstr(limit_BA, 30),
            "ame_B_per_A_peak": {"nucleus": peak[0], "A": peak[1],
                                 "B_per_A_MeV": mp.nstr(peak[2], 20)},
            "constant_at_peak": mp.nstr(k_peak, 30),
            "distance_from_3": mp.nstr(abs(k_peak - 3), 20),
            "deuteron": {"model_MeV": mp.nstr(d_model, 20),
                         "ame_MeV": mp.nstr(d_ame, 20),
                         "model_over_ame": mp.nstr(d_model / d_ame, 20),
                         "three_x_over_ame": mp.nstr(3 * d_model / d_ame, 20)},
            "table": rows,
            "assertions": assertions,
            "allPassed": ok,
        },
    }
    out = _COMP / "probes" / "assembly-shortfall-shape.witness.json"
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
