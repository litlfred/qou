#!/usr/bin/env python3
"""The a-dependence of the closed form, tested against SnapPy — bean qou-vdvT.

`qou-vdvS` derived, for van der Veen's `b = 1` Whitehead chains,

    |tau_DG|(W_{a,1,c,d}) = 2^{2n-2} sqrt(n^2 + m^2),   n = c+d,  m = 4a-c+d

and confirmed it at five manifolds — but every one of them had `a = 0`. The
`a`-dependence was pure prediction, and it is the half that matters most,
because `a` enters van der Veen's Lemma 1 ONLY through the phase
`chi^{4a-c+d}`. Nothing in the modulus of the summand knows about `a`; the
`a`-dependence of `|tau_DG|` is manufactured entirely by interference in the
`n`-sum. If the closed form is right for the wrong reason, this is where it
shows.

WHY THE CHEAP TEST FAILED FIRST. `Vol(W_{a,b,c,d}) = 8(c+d) Lambda(pi/4)` is
independent of `a`, so by Thurston-Jorgensen the chains `{W_{a,1,c,d} : a in Z}`
cannot be infinitely many distinct manifolds — they are the SAME complement with
different peripheral framings. Scanning `OrientableCuspedCensus(cusps=2)` at
octahedral volume returns only `m129` (the Whitehead link, `|tau| = sqrt2`) and
`m125` (`|tau| = sqrt8`, and `8 = 1 + m^2` has no integer solution, so it is not
in the family at all). There is no alternative manifold carrying the `a != 0`
values. So the prediction is a statement about the CHANGE-OF-CURVE LAW, and
testing it needs peripheral curves `p*meridian + q*longitude`, which
`one_loop_torsion.one_loop` did not support.

WHAT WAS ADDED. `_curve_row` in `computations/one_loop_torsion.py`. The log-form
gluing equation of a peripheral curve is LINEAR in its homology class, so the
row of `p*mu + q*lambda` is the integer combination `p*mer + q*lon` of the two
rows SnapPy already returns, and `nz_pair` stays valid because it is linear too.
No new geometry, no new normalisation. The legacy `0`/`1` spelling still works
and is checked to agree.

THE RESULT. Writing the framing as `mu - a*lambda` on one cusp:

    Whitehead  W_{a,1,1,0}   n=1, m=4a-1   tau^2 = 1 + (4a-1)^2
        a =  0  1  -1   2  -2   ->   2, 10, 26, 50, 82        all exact
    Borromean  W_{a,1,1,1}   n=2, m=4a     tau^2 = 64 (1 + 4a^2)
        a =  0  1  -1   2  -2   ->   64, 320, 320, 1088, 1088  all exact

and the Borromean values are identical on all three cusps and symmetric under
`a -> -a`, both of which the closed form requires (`m = 4a` enters only through
`m^2`) and neither of which was put in.

So the phase-driven half of the closed form is confirmed, at two cusp numbers,
against machinery that knows nothing about the colored Jones polynomial.

Nothing is fitted. The predicted values are computed from the closed form first
and printed before the SnapPy numbers.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf, sqrt, fabs  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent

# (base manifold, c, d, cusps) — the a = 0 member, whose complement carries the
# whole family under reframing.
FAMILIES = {
    "L5a1": dict(c=1, d=0, cusps=2, label="W_{a,1,1,0} (Whitehead)"),
    "L6a4": dict(c=1, d=1, cusps=3, label="W_{a,1,1,1} (Borromean)"),
}
TWISTS = (0, 1, -1, 2, -2)


def tau_predicted(a: int, c: int, d: int):
    """|tau_DG| = 2^{2n-2} sqrt(n^2 + m^2),  n = c+d,  m = 4a-c+d."""
    n, m = c + d, 4 * a - c + d
    return mpf(2) ** (2 * n - 2) * sqrt(mpf(n) ** 2 + mpf(m) ** 2)


def main() -> int:  # noqa: C901
    set_compute_dps()
    try:
        import warnings
        warnings.filterwarnings("ignore")
        import snappy
        sys.path.insert(0, str(COMP))
        from one_loop_torsion import one_loop
    except Exception as exc:                            # pragma: no cover
        print(f"snappy/one_loop_torsion unavailable ({type(exc).__name__}); "
              "cannot run")
        return 1

    print("=" * 76)
    print(" The a-dependence of |tau_DG| = 2^{2n-2} sqrt(n^2+m^2), by reframing")
    print("=" * 76)

    # -- backwards compatibility of the extended `curves` argument --------
    M = snappy.Manifold("L5a1")
    compat = [
        (fabs(one_loop(M)), fabs(one_loop(M, curves=[(1, 0), (1, 0)]))),
        (fabs(one_loop(M, curves=[1, 0])), fabs(one_loop(M, curves=[(0, 1), (1, 0)]))),
    ]
    compat_ok = all(a == b for a, b in compat)
    print(f"\n  legacy 0/1 spelling agrees with the (p,q) spelling: {compat_ok}")
    print(f"    default        vs (1,0),(1,0) : {mp.nstr(compat[0][0], 18)}"
          f"  {mp.nstr(compat[0][1], 18)}")
    print(f"    [1,0]          vs (0,1),(1,0) : {mp.nstr(compat[1][0], 18)}"
          f"  {mp.nstr(compat[1][1], 18)}")

    # -- the prediction, printed BEFORE the measurement -------------------
    print("\n  PREDICTED tau^2, from the closed form (a enters only via a PHASE):\n")
    pred = {}
    for name, f in FAMILIES.items():
        row = {a: tau_predicted(a, f["c"], f["d"]) ** 2 for a in TWISTS}
        pred[name] = row
        cells = "  ".join(f"a={a:+d}: {mp.nstr(v, 12)}" for a, v in row.items())
        print(f"    {f['label']:26s} {cells}")

    # -- measured, by reframing the a = 0 complement ----------------------
    print("\n  MEASURED, framing mu - a*lambda on one cusp:\n")
    rows, n_bad, n_tested = {}, 0, 0
    for name, f in FAMILIES.items():
        M = snappy.Manifold(name)
        cusps = f["cusps"]
        rows[name] = {"label": f["label"], "cusps": cusps, "framings": {}}
        print(f"    {name} ({f['label']}, {cusps} cusps)")
        for cusp in range(cusps):
            got = {}
            for a in TWISTS:
                cur = [0] * cusps
                cur[cusp] = (1, -a)          # meridian - a*longitude
                t2 = fabs(one_loop(M, curves=cur)) ** 2
                ok = fabs(t2 / pred[name][a] - 1) < mpf("1e-18")
                n_tested += 1
                n_bad += (not ok)
                got[a] = {"tau_sq": mp.nstr(t2, 22), "matches": bool(ok)}
            cells = "  ".join(f"a={a:+d}: {mp.nstr(fabs(one_loop(M, curves=[(1,-a) if i==cusp else 0 for i in range(cusps)]))**2, 12)}"
                              for a in TWISTS)
            print(f"      cusp {cusp}: {cells}")
            rows[name]["framings"][f"cusp_{cusp}"] = got

    all_ok = compat_ok and n_bad == 0
    print(f"\n  framings tested: {n_tested};  mismatches: {n_bad}")

    verdict = (
        "THE a-DEPENDENCE IS CONFIRMED, at two cusp numbers. |tau_DG| = "
        "2^{2n-2} sqrt(n^2+m^2) with m = 4a-c+d reproduces the SnapPy 1-loop "
        "invariant exactly on every framing tested: Whitehead tau^2 = "
        "2, 10, 26, 50, 82 and Borromean tau^2 = 64, 320, 320, 1088, 1088, for "
        "a = 0, 1, -1, 2, -2. This is the half of the closed form that was pure "
        "prediction, and it is the half that matters, because `a` enters van "
        "der Veen's Lemma 1 ONLY through the phase chi^{4a-c+d} — the modulus "
        "of the summand does not know about it, and the whole a-dependence of "
        "|tau_DG| is manufactured by interference in the n-sum. The Borromean "
        "values come out identical on all three cusps and symmetric under "
        "a -> -a, both required by m = 4a entering as m^2, neither put in. "
        "It also settles what the twisted chains ARE: the same complement with "
        "meridian mu - a*lambda, which is what the a-independence of "
        "Vol(W_{a,b,c,d}) forced and what the census scan (only m129 and m125 "
        "at octahedral volume, neither carrying sqrt10) confirmed."
        if all_ok else
        "A CHECK FAILED — inspect before citing.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("one-loop-twisted-framing", engine="mpmath")
    wb.set_description(
        "Confirms the a-dependence of |tau_DG| = 2^{2n-2} sqrt(n^2+m^2) "
        "(m = 4a-c+d) by reframing the a=0 complement with meridian "
        "mu - a*lambda, at two cusp numbers and every framing tested. This is "
        "the phase-driven half of the closed form derived in qou-vdvS, which "
        "had only ever been checked at a = 0. Required extending "
        "one_loop_torsion.one_loop to general (p,q) peripheral curves; the "
        "legacy 0/1 spelling is checked to agree and the module self-test "
        "stays green. Nothing fitted — predictions printed before measurement.")
    wb.set_audit_only(
        "docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md")
    wb.add_data("what_was_extended", {
        "function": "computations/one_loop_torsion.py::_curve_row",
        "why_it_is_sound": ("the log-form gluing equation of a peripheral curve "
                            "is LINEAR in its homology class, so the row of "
                            "p*mu + q*lambda is p*mer + q*lon of the two rows "
                            "SnapPy returns; nz_pair is linear too"),
        "legacy_spelling_agrees": bool(compat_ok),
        "self_test_still_green": "checked by running one_loop_torsion.py directly",
    })
    wb.add_data("why_reframing_is_the_only_access", {
        "volume_is_a_independent": "Vol(W_{a,b,c,d}) = 8(c+d) Lambda(pi/4)",
        "consequence": ("by Thurston-Jorgensen the chains cannot be infinitely "
                        "many distinct manifolds — they are one complement "
                        "reframed"),
        "census_scan": ("OrientableCuspedCensus(cusps=2) at octahedral volume "
                        "returns only m129 (|tau| = sqrt2) and m125 "
                        "(|tau| = sqrt8; 8 = 1+m^2 has no integer solution, so "
                        "m125 is not in the family). No manifold carries the "
                        "a != 0 values"),
    })
    wb.add_data("families", rows)
    wb.add_data("predicted", {
        name: {f"a_{a}": mp.nstr(v, 22) for a, v in row.items()}
        for name, row in pred.items()})
    wb.add_assertion(
        "twisted_framings_match_closed_form",
        computed=str(n_tested - n_bad), expected=str(n_tested), tolerance="0.5",
        source=("|tau_DG| under mu - a*lambda against 2^{2n-2} sqrt(n^2+m^2), "
                "a in {0,1,-1,2,-2}, on every cusp of L5a1 and L6a4"))
    wb.add_assertion(
        "legacy_curve_spelling_unchanged",
        computed="1" if compat_ok else "0", expected="1", tolerance="0.5",
        source="curves=[0,0] vs [(1,0),(1,0)] and [1,0] vs [(0,1),(1,0)]")
    out = wb.save()
    print(f"\n  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
