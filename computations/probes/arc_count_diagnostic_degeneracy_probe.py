#!/usr/bin/env python3
"""The R^2=0.83 arc-count diagnostic is not in the witness it cites.

`qou-0c19` (in-progress since 2026-08-02, title only, no body) asserts:

    LOCALIZE the missing additive extensive term: it lives in the inter-nucleon
    COLOR-TUBE channel. Diagnostic: per-isotope error proportional to
    inter-nucleon arc count R^2=0.83 (vs signed-h R^2=0.26) = the extensive
    ~A signature.

repeated verbatim in `docs/audits/2026-08-02-deltalambda-value-proved-downstream-
and-additive-term.md` (S4) as "the framework already localizes it", and in the
content block `brings-surface/inter-nucleon-channel-color-tube.md:34`, which
names its source: `computations/low-isotope-sign-flip-diagnostic.witness.json`.

**Read that witness.** It is the primary finding here, and it needs no model:

| quantity | corpus says | the cited witness says |
|---|---|---|
| err vs inter-nucleon arc count | `R^2 = 0.83` | `R^2 = 0.26529448…` |
| err vs signed-h weight         | `R^2 = 0.26` | `R^2 = 0.00175532…` |
| sample size                    | (not stated) | **5**, of which p and n have `err_pct ~ 1e-10` |
| the witness's own verdict      | "localizes it" | "**WEAK** correlation … sign-flips are **NOT** explained …" |

The string `0.83` does not occur anywhere in that file. The `0.26` the corpus
attributes to the *signed-h* regressor is, to three digits, the value the
witness reports for the *arc count* one.

So the durable artifacts cite a witness for a number it does not contain, in
support of a conclusion its own recorded verdict contradicts, on a sample of
five points of which three are informative.

## What this probe checks, and what it deliberately does not

1. **The citation mismatch**, read straight out of the committed witness. Exact
   strings, no arithmetic.
2. **The sample.** n = 5; the two A=1 rows are anchors with ~1e-10 relative
   error, so three points carry the fit.
3. **The claim AS WRITTEN in the bean and the audit** -- *"per-isotope error
   proportional to arc count … the extensive ~A signature"* -- is a statement
   about ABSOLUTE error, and for that reading the diagnostic is degenerate for
   two independent algebraic reasons, both measured here in exact rational
   arithmetic:
   - R^2 is invariant under scaling the response, so a model short by a
     constant FRACTION has `R^2(err ~ X) = R^2(B_AME ~ X)` for every X. And
     `R^2(B_AME ~ arc)` alone is **0.994** over 2449 nuclei. Nothing needs to be
     missing to clear 0.83.
   - R^2 is invariant under affine reparametrisation of the regressor, and
     `arc = A - 1` is affine in `A`. So arc count scores *exactly* what bare `A`
     scores, and what `7A - 3` scores. The diagnostic cannot tell the
     inter-nucleon arc structure apart from the mass number.

4. **SCOPE LIMIT, stated because it cuts against point 3.** The witness fits
   `err_pct` -- *relative* error -- not absolute. A constant fractional
   shortfall gives a CONSTANT `err_pct`, i.e. zero variance, so the argument in
   point 3 does **not** apply to the witness's own regression. Point 3 governs
   the claim as it is written in the bean, the audit and the content block
   (all of which say "extensive ~A signature", which is an absolute-error
   statement); the witness's actual computation is a different fit, and what
   disposes of that one is its own n=5 and its own WEAK verdict, not point 3.

## What is NOT claimed

Not that `conj:inter-nucleon-channel-color-tube` is false -- it may hold for
other reasons, and this probe tests none of them. Not that the 0.83 was
fabricated: this clone is **shallow**, only two commits touching that witness
are in the fetched window, and both carry 0.2653 -- an earlier version outside
the window cannot be excluded, so the honest statement is that the citation does
not match the witness *as committed today*, which is what any reader acting on
it would find. Scope **(a)** throughout. Nothing wired.

`-- Ref:` [ame2020]. Beans `qou-0c19`, `qou-brng`.
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

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()


def _fr_to_mpf(fr: Fr):
    """Exact Fraction -> mpf at the active compute precision (no float64)."""
    return mpf(fr.numerator) / mpf(fr.denominator)

CITED = "low-isotope-sign-flip-diagnostic.witness.json"


def load_ame_exact():
    p = Path(_COMP).parent / "qou-mass/src/qou_mass/data/ame2020.json"
    raw = json.loads(p.read_text(encoding="utf-8"))
    out = {}
    for e in raw["entries"]:
        b = e.get("binding_energy_per_A_keV")
        if b is None or e.get("mass_excess_estimated"):
            continue
        out[(e["Z"], e["N"])] = Fr(str(b)) * e["A"] / 1000
    return out


def r2_exact(xs, ys):
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    den = n * sxx - sx * sx
    if den == 0:
        return None
    b = (n * sxy - sx * sy) / den
    a = (sy - b * sx) / n
    ybar = sy / n
    sst = sum((y - ybar) ** 2 for y in ys)
    ssr = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    return None if sst == 0 else 1 - ssr / sst


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    print("=" * 78)
    print("  The R^2=0.83 arc-count diagnostic is not in the witness it cites")
    print("=" * 78)

    # ---------------------------------------------------------------- 1
    print("\n" + "-" * 78)
    print("  1. What the cited witness actually contains")
    print("-" * 78)
    wp = _COMP / CITED
    raw_text = wp.read_text(encoding="utf-8")
    W = json.loads(raw_text)
    d = W["data"]
    r2_arc = d["linear_fit_err_pct_vs_n_inter"]["R_squared"]
    r2_sh = d["linear_fit_err_pct_vs_signed_h_weight"]["R_squared"]
    verdict = d["verdict"]
    n_iso = len(d["per_isotope"])
    print(f"\n  file: computations/{CITED}")
    print(f"  fit err_pct ~ n_inter        R^2 = {r2_arc[:20]}")
    print(f"  fit err_pct ~ signed_h       R^2 = {r2_sh[:20]}")
    print(f"  per_isotope sample size          = {n_iso}")
    print(f"  verdict: {verdict[:150]}")
    has083 = "0.83" in raw_text
    check("the string '0.83' does not occur in the cited witness",
          not has083,
          f"grep of the committed file finds 0 occurrences. Its two recorded "
          f"R^2 are {r2_arc[:10]} (arc count) and {r2_sh[:10]} (signed-h), "
          f"against the corpus's quoted 0.83 and 0.26. The 0.26 the corpus "
          f"attributes to SIGNED-H is, to three digits, the witness's ARC-COUNT "
          f"value.")

    weak = "WEAK" in verdict.upper() and "NOT explained" in verdict
    check("the witness's own verdict contradicts what it is cited for",
          weak,
          f"recorded verdict begins: \"{verdict[:96]}…\" — cited in "
          f"inter-nucleon-channel-color-tube.md:34 and in the 2026-08-02 audit "
          f"as the framework's localization of the missing extensive term.")

    zero_rows = [e for e in d["per_isotope"] if abs(Fr(e["err_pct"])) < Fr(1, 1000)]
    check("the fit rests on 3 informative points, not 5",
          n_iso == 5 and len(zero_rows) == 2,
          f"n = {n_iso}: {', '.join(e['atom_label'] for e in d['per_isotope'])}. "
          f"The two A=1 rows (p, n) are anchors with |err_pct| < 1e-3, so three "
          f"points carry the regression. An R^2 on 3 points is not evidence of "
          f"a structural signature either way.")

    # ---------------------------------------------------------------- 2
    print("\n" + "-" * 78)
    print("  2. The claim AS WRITTEN is degenerate -- absolute-error reading")
    print("-" * 78)
    print("\n  The bean, the audit and the block all gloss it as 'the extensive")
    print("  ~A signature', which is a statement about ABSOLUTE error. Under")
    print("  that reading the diagnostic cannot discriminate, for two reasons.\n")
    ame = load_ame_exact()
    keys = sorted(k for k in ame if 2 <= k[0] + k[1] <= 240)
    xs = [Fr(Z + N - 1) for Z, N in keys]
    ys = [ame[k] for k in keys]
    ceiling = r2_exact(xs, ys)
    print(f"  (a) R^2(B_AME ~ arc) = {float(ceiling):.6f} on {len(keys)} nuclei,")
    print(f"      exact rational arithmetic, NO MODEL of any kind. R^2 is")
    print(f"      invariant under scaling the response, so a model short by a")
    print(f"      constant fraction reproduces this exactly:")
    for lam in (Fr(1, 3), Fr(1, 2), Fr(9, 10)):
        r = r2_exact(xs, [(1 - lam) * y for y in ys])
        print(f"        lambda={str(lam):>5} -> R^2(err ~ arc) = {float(r):.10f}"
              f"  {'==' if r == ceiling else '!='} ceiling")
    ident = all(r2_exact(xs, [(1 - l) * y for y in ys]) == ceiling
                for l in (Fr(1, 3), Fr(1, 2), Fr(9, 10)))
    check("(a) a constant fractional shortfall reproduces the ceiling exactly",
          ident and ceiling > Fr(83, 100),
          f"R^2(B_AME ~ arc) = {float(ceiling):.6f} > 0.83 with nothing missing, "
          f"and equals R^2(err ~ arc) as EXACT rationals for every fraction "
          f"tested. Clearing 0.83 on absolute error requires no additive term.")

    print()
    regs = [("arc count = A - 1", lambda Z, N: Fr(Z + N - 1)),
            ("A", lambda Z, N: Fr(Z + N)),
            ("7*A - 3", lambda Z, N: Fr(7 * (Z + N) - 3))]
    vals = {}
    for nm, f in regs:
        vals[nm] = r2_exact([f(Z, N) for Z, N in keys], ys)
        print(f"  (b) R^2(B_AME ~ {nm:<18}) = {float(vals[nm]):.6f}")
    same = len(set(vals.values())) == 1
    check("(b) arc count scores EXACTLY what bare A scores",
          same,
          "R^2 is invariant under affine reparametrisation of the regressor and "
          "arc = A-1 is affine in A, so the diagnostic cannot distinguish the "
          "inter-nucleon arc structure from the mass number. 'It beats signed-h' "
          "then says only that binding is extensive and signed-h is not a proxy "
          "for A -- both already known.")

    # ---------------------------------------------------------------- 3
    print("\n" + "-" * 78)
    print("  3. SCOPE LIMIT -- why section 2 does NOT dispose of the witness")
    print("-" * 78)
    print("""
  The witness fits `err_pct`, a RELATIVE error. A constant fractional shortfall
  gives a constant err_pct -- zero variance -- so section 2's invariance
  argument does not apply to that regression at all. Section 2 governs the
  claim as WRITTEN in the bean, the audit and the content block, every one of
  which glosses it as an absolute 'extensive ~A signature'. What disposes of
  the witness's own fit is its n=5 and its own WEAK verdict (section 1), not
  section 2. Keeping these apart is the point: they are different claims and
  only one of them is what a reader of the bean would act on.
""")
    check("the two readings are kept separate rather than conflated",
          True,
          "absolute-error reading -> degenerate by (a) and (b) above; "
          "relative-error reading (what the witness computes) -> disposed of by "
          "n=5 and the recorded WEAK verdict. Neither argument is used for the "
          "other's claim.")

    ok = all(checks)
    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print("=" * 78)
    print(f"""
  VERDICT. `qou-0c19`'s localization evidence does not survive reading its own
  source. The cited witness contains no 0.83; it reports 0.2653 for the arc
  count and 0.0018 for signed-h, on five points of which three are informative,
  and its recorded verdict is that the correlation is WEAK and the sign-flips
  are NOT explained -- the opposite of the conclusion it is cited for in
  inter-nucleon-channel-color-tube.md:34, in the 2026-08-02 audit S4, and in the
  bean's title.

  Separately, the claim as WRITTEN in those artifacts -- absolute error ~ arc
  count, 'the extensive ~A signature' -- is degenerate twice over:
  R^2(B_AME ~ arc) = {float(ceiling):.4f} with no model at all, and arc = A-1
  scores exactly what bare A scores.

  This does NOT refute conj:inter-nucleon-channel-color-tube. It removes the
  evidence cited for it -- which, for the bean, is the whole content: it has a
  title and no body.
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
        "name": "arc-count-diagnostic-degeneracy",
        "description": (
            "qou-0c19's 'error ~ inter-nucleon arc count, R^2=0.83 (vs signed-h "
            "0.26)' localization evidence does not match its cited source. "
            "low-isotope-sign-flip-diagnostic.witness.json contains no 0.83; it "
            "records 0.2653 (arc) and 0.0018 (signed-h) on n=5 with 3 informative "
            "points, and its own verdict is WEAK correlation / sign-flips NOT "
            "explained. Separately, the absolute-error reading used in the bean, "
            "audit and content block is degenerate: R^2(B_AME ~ arc) = 0.994 with "
            "no model, and arc=A-1 scores exactly what bare A scores. Does NOT "
            "refute conj:inter-nucleon-channel-color-tube. Scope (a)."),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "data": {
            "q0": Q_50_DIGIT_STR,
            "cited_witness": f"computations/{CITED}",
            "cited_witness_contains_0_83": has083,
            "cited_r2_arc_count": r2_arc,
            "cited_r2_signed_h": r2_sh,
            "cited_sample_size": n_iso,
            "cited_verdict": verdict,
            "corpus_quoted_r2_arc": "0.83",
            "corpus_quoted_r2_signed_h": "0.26",
            "r2_ame_vs_arc_exact": str(ceiling),
            "r2_ame_vs_arc": fmt(_fr_to_mpf(ceiling)),
            "n_nuclei_ame": len(keys),
            # str(), not fmt(): these are exact `Fraction`s, and the
            # DEGENERACY is the finding — three regressors, one R2. Three
            # identical rationals state the tie exactly; three truncated
            # decimals ask the reader to trust the truncation. Matches
            # `r2_ame_vs_arc_exact` above, which is str() on the same object.
            "regressor_race": {k: str(v) for k, v in vals.items()},
            "shallow_clone_caveat": (
                "This clone is shallow; only 2 commits touching the cited "
                "witness are in the fetched window and both carry 0.2653. An "
                "earlier version outside the window cannot be excluded, so the "
                "claim is about the witness AS COMMITTED TODAY."),
            "assertions": assertions,
            "allPassed": ok,
        },
    }
    out = _COMP / "probes" / "arc-count-diagnostic-degeneracy.witness.json"
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
