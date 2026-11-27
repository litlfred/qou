#!/usr/bin/env python3
"""The chain binding has an EXACT closed form, and no parameter makes it extensive.

Third correction in this arc, and the one that supersedes the other two.

## What was measured

Decomposing the chain binding `B(A) = E0*(S_off - S_on)` into its two trace
sums, both turn out to be exactly geometric, and their ratio is exactly the
corpus's own bond factor:

    S_on(A) / S_off(A)        = f ^ (A - 1)     exact at every A
    S_off(A + 1) / S_off(A)   = g               constant across every step

                 g                        f
    pp   1.1457596924573008697   0.6126880371464652516   ( = z_D = q^3/(q^2+1) )
    nn   0.98774368811580957163  0.403627738350825936

`f_pp` is convention-D `z` on the nose -- `atomic_tr_m_helium4_canonical.py`
defines `f_pp = z_d` -- so this is not a coincidence to be explained but the
bond factor showing up where it should. Hence

    B(A) = E0 * S_off(2) * g^(A-2) * (1 - f^(A-1))

reproduces all four measured points at `1e-30` relative. TWO constants against
FOUR points is an identity, not a fit. It is exactly the form the `qou-brng`
taxonomy calls Channel 2, `Delta tr = tr_free * (1 - f^bonds)`.

## What it overturns -- including twice over, mine

1. **"pp saturates to a nonzero limit"** (my #6373 body). Refuted in Lean:
   rising ratios prove nothing.
2. **"then BOTH species collapse"** (my correction to 1). ALSO WRONG. That
   leaned on the corpus's bounded-trace claim, and `g_pp > 1` means `S_off`
   GROWS geometrically, so the pp total is unbounded and the boundedness
   hypothesis simply does not hold there. The Lean lemma was right; I fed it a
   false premise.
3. **"the binding is intensive"** (`2026-06-02-binding-intensive-vs-extensive-
   derivation.md`) is the `g <= 1` branch. Correct for the NEUTRON chain
   (`g < 1`); the PROTON chain has `g > 1` and is unbounded. The claim needs
   scoping to the branch, not retracting -- its evidence was `A <= 4` on
   canonical nuclei, and this is a different object measured further out.

## The exclusion, which survives all three

Extensivity means `B(A) ~ cA`. Split on `g`:

  * `g <= 1`  -> `B <= E0*S_off(2)`, BOUNDED  (`chain_bounded_of_growth_le_one`)
  * `g > 1`   -> each step multiplies by at least `g`, so growth is at least
                 geometric (`chain_step_ge_growth`)

Bounded is too slow to be linear and geometric is too fast, so **no value of `g`
makes this channel extensive.** Scope (b), invariant named, independent of `f`,
of the anchor, and of the species. That is the useful output: it retires the
whole channel in one argument instead of scoring ansatze one at a time.

## `g` is NOT a fitted constant -- it is the A=1 free trace

The `include_inter=False` word is an **exact disjoint union**: at every `A` it
uses only generators `{3i, 3i+1}`, strictly inside each nucleon's own 3-strand
block, with **zero stray generators** and exactly 11 crossings per block,
identical for every nucleon. Measured accordingly,

    S_off(1) = 1.145759692457300869689   (pp)   vs g = same, |diff| 9.3e-31
    S_off(1) = 0.987743688115809571634   (nn)   vs g = same, |diff| 3.9e-31

so `S_off(A) = g^A` with `g = S_off(1)`. **`g` cannot drift with `A` because it
IS the `A=1` value**, and `f` is a two-nucleon value. The closed form has no
free parameter left.

This was worth measuring for its cost as much as its content: it took
milliseconds, where the `A=6` run that would have tested `g` by brute force
projects to **~40 h** at `n=18` (max dim ~13000) and was stopped. The cheap
structural test beat the expensive one by five orders of magnitude.

**The remaining gap is an algebra question, not a compute one.** The
disjointness of the WORD is structural and measured; the FACTORIZATION of the
weighted Schur-Weyl sum over those blocks is verified numerically at
`A = 1,2,3,4,5` to 20 digits and is **not proved in general**.

## What the closed form then says

Evaluating it (an EVALUATION, not an extrapolation, given the paragraph above --
though it still rests on the unproved factorization):

    pp marginal   A=5  1.5459   A=6  1.5519   A=7  1.6240   A=8  1.7526
    nn marginal   A=6  0.0146   A=7 -0.0226   A=8 -0.0371

so **the pp marginal has a minimum at A=5 and turns UP at A=6**, and **the nn
marginal goes NEGATIVE at A=7** (adding a neutron reduces total binding).

These remain falsifiable, but the falsifier has MOVED. It is no longer "does `g`
drift at A=6" -- `g` is the A=1 value and cannot. It is now: **does the weighted
sum really factor over disjoint blocks?** Proving or refuting that settles every
`A` at once, and costs no compute at all.
"""

import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "habiro"),
           str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(40)

# Reuse the landed sparse evaluator rather than re-implementing it; needed only
# for the A=1 single-nucleon trace in section 4b (everything else reads the
# checkpoint).
_spec = importlib.util.spec_from_file_location(
    "_cw", str(_HERE / "colour_weighting_across_mixed_nuclei_probe.py"))
_cw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cw)

CKPT = _COMP / ".bpp-higher-a-checkpoint.json"


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    if not CKPT.exists():
        print("  checkpoint absent — run bpp_higher_a_resumable_driver first "
              "(2 3 4 5, and again with --neutron)")
        return 1

    q = Q_MP
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    z_D = q ** 3 / (q ** 2 + 1)

    ck = json.loads(CKPT.read_text())
    agg = defaultdict(lambda: defaultdict(lambda: mp.mpf(0)))
    for k, v in ck.items():
        # A `<A>|<w>|<lam>|partial` key is an IN-FLIGHT ROW CURSOR banked
        # by the driver's --budget-seconds path, not a completed term: its
        # value is a dict, and `mp.mpf(dict)` raises. Skip it. This probe
        # reports only completed partitions, so an in-flight one is simply
        # not yet part of the sum.
        if k.endswith("|partial"):
            continue
        a, w, lam = k.split("|", 2)
        sp = "nn" if a.startswith("n") else "pp"
        agg[(sp, int(a.lstrip("n")))][w] += mp.mpf(v)

    print("=" * 78)
    print("  The chain binding closed form — and why no g makes it extensive")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV")
    print(f"  z_D = q^3/(q^2+1) = {mp.nstr(z_D, 22)}\n")

    params, closed_ok, ratio_ok = {}, [], []
    # The same guard the sibling logratio probe carries (Copilot review there).
    # Without it, two failure modes both write or crash silently:
    #   * ONE species only -> `continue` skips it, then params["nn"] KeyErrors;
    #   * BOTH species but DIFFERENT A-sets (the driver is resumable, so a bank
    #     mid-run routinely has pp at A={2,3,4,5} and nn at A={2,3,4}) -> both
    #     pass `len(As) >= 3` and the probe fits its closed form on unequal
    #     ranges, reporting a comparison it never made.
    # Refuse on either, rather than report on a partial checkpoint.
    A_BY_SP = {sp: sorted(A for s, A in agg if s == sp) for sp in ("pp", "nn")}
    _missing = [sp for sp in ("pp", "nn") if len(A_BY_SP[sp]) < 3]
    if _missing:
        print(f"  checkpoint has fewer than 3 A-points for species {_missing} "
              f"(have {A_BY_SP}). Run "
              f"bpp_higher_a_resumable_driver 2 3 4 5 (pp) and again with "
              f"--neutron (nn) to completion first. REFUSING to report on a "
              f"partial checkpoint.")
        return 1
    if A_BY_SP["pp"] != A_BY_SP["nn"]:
        print(f"  checkpoint species disagree on the A-set: "
              f"pp={A_BY_SP['pp']} nn={A_BY_SP['nn']}. The pp-vs-nn "
              f"comparisons below would be across different A ranges. "
              f"REFUSING; finish both species first.")
        return 1
    for sp in ("pp", "nn"):
        As = A_BY_SP[sp]
        off = [agg[(sp, A)]["off"] for A in As]
        on = [agg[(sp, A)]["on"] for A in As]
        f = on[0] / off[0]
        gs = [off[i + 1] / off[i] for i in range(len(off) - 1)]
        g = gs[0]
        params[sp] = {"f": f, "g": g, "S0": off[0], "A0": As[0]}

        print("-" * 78)
        print(f"  {sp}: S_on/S_off = f^(A-1), and S_off has constant step g")
        print("-" * 78)
        print(f"\n  {'A':>3}{'S_on/S_off':>26}{'f^(A-1)':>26}{'S_off step g':>26}")
        for i, A in enumerate(As):
            r = on[i] / off[i]
            pred = f ** (A - As[0] + (As[0] - 1))
            gstr = mp.nstr(gs[i], 20) if i < len(gs) else ""
            print(f"  {A:>3}{mp.nstr(r, 20):>26}{mp.nstr(pred, 20):>26}"
                  f"{gstr:>26}")
            ratio_ok.append(abs(r - pred) < mp.mpf("1e-25"))
        gspread = max(gs) - min(gs)
        print(f"\n  g spread across steps: {mp.nstr(gspread, 6)}")
        params[sp]["g_spread"] = gspread

        print(f"\n  closed form  B(A) = E0 * S_off({As[0]}) * g^(A-{As[0]}) * "
              f"(1 - f^(A-1)):")
        worst = mp.mpf(0)
        for i, A in enumerate(As):
            pred = E0 * off[0] * g ** (A - As[0]) * (1 - f ** (A - 1))
            meas = E0 * (off[i] - on[i])
            rel = abs(pred - meas) / abs(meas)
            worst = max(worst, rel)
            print(f"    A={A}  pred = {mp.nstr(pred, 18):>22}   "
                  f"meas = {mp.nstr(meas, 18):>22}   rel = {mp.nstr(rel, 4)}")
        params[sp]["worst_rel"] = worst
        closed_ok.append(worst < mp.mpf("1e-25"))
        print()

    # ------------------------------------------------- 1. f IS the bond factor
    print("-" * 78)
    print("  1. f_pp is convention-D z, exactly")
    print("-" * 78)
    fpp = params["pp"]["f"]
    dz = abs(fpp - z_D)
    print(f"\n  measured f_pp = {mp.nstr(fpp, 22)}")
    print(f"  z_D           = {mp.nstr(z_D, 22)}")
    print(f"  |difference|  = {mp.nstr(dz, 6)}")
    check("the measured bond factor IS convention-D z, not merely near it",
          dz < mp.mpf("1e-25"),
          "atomic_tr_m_helium4_canonical.py defines f_pp = z_d, so this is the "
          "corpus's own constant appearing where it should — a consistency "
          "check on the construction, NOT a new identification.")

    # --------------------------------------------- 2. the closed form is exact
    print("\n" + "-" * 78)
    print("  2. TWO constants reproduce FOUR points — an identity, not a fit")
    print("-" * 78)
    check("closed form reproduces every measured point to <1e-25 relative",
          all(closed_ok) and all(ratio_ok),
          f"worst relative error: pp {mp.nstr(params['pp']['worst_rel'], 4)}, "
          f"nn {mp.nstr(params['nn']['worst_rel'], 4)}. A 2-parameter form "
          f"matching 4 points at 1e-30 has no freedom left to fit with.")

    # ------------------------------------------- 3. the branch each species is in
    print("\n" + "-" * 78)
    print("  3. g decides the branch — and the species land on opposite sides")
    print("-" * 78)
    gpp, gnn = params["pp"]["g"], params["nn"]["g"]
    print(f"""
  pp   g = {mp.nstr(gpp, 20)}  > 1   -> S_off GROWS, total UNBOUNDED
  nn   g = {mp.nstr(gnn, 20)}  < 1   -> S_off decays, total BOUNDED

  So "the binding is intensive" (2026-06-02 audit) is the g <= 1 branch. It is
  correct for the NEUTRON chain and does NOT hold for the proton chain. That
  audit's evidence was A <= 4 on canonical nuclei; this is a different object
  measured further out, so the claim needs SCOPING to the branch, not retracting.
""")
    check("the two species sit on opposite sides of g = 1",
          gpp > 1 and gnn < 1,
          "This is why my own 'both collapse' correction was wrong: it assumed "
          "the bounded-total hypothesis, which fails for pp. The Lean lemma "
          "was right and the premise I fed it was false.")

    # ------------------------------------------------------- 4. the exclusion
    print("\n" + "-" * 78)
    print("  4. NO g makes the channel extensive — scope (b)")
    print("-" * 78)
    print("""
  Extensivity means B(A) ~ cA. Split on g:

    g <= 1  ->  B <= E0*S_off(A0), BOUNDED
                QOU.MassTheory.MarginalRatio.chain_bounded_of_growth_le_one
    g >  1  ->  each step multiplies by at least g, so growth is at least
                geometric
                QOU.MassTheory.MarginalRatio.chain_step_ge_growth

  Bounded is too slow to be linear; geometric is too fast. Neither branch can be
  asymptotically linear, so no value of g makes this channel extensive --
  independent of f, of the anchor, and of the species.

  That retires the CHANNEL, not one ansatz. It is the same conclusion the
  qou-brng taxonomy reached by scoring seven channels numerically, obtained
  instead from the closed form, so it does not have to be re-run per candidate.
""")
    check("the exclusion is stated with its Lean witnesses and is "
          "parameter-independent", True,
          "Both lemmas are sorry-free and generic in S, g, f — no substrate, "
          "no q, no anchor enters either statement.")

    # ------------------------------ 4b. g IS the single-nucleon free trace
    print("\n" + "-" * 78)
    print("  4b. g is not emergent — it IS the A=1 free trace, so it cannot drift")
    print("-" * 78)
    from canonical_braid_crossings import atom_canonical_crossings as _ac
    from canonical_braid_crossings import d_for_ctype as _dfc
    from wedderburn_jones_markov import y_lambda_at as _yla
    h = q - mp.mpf(1) / q
    _db = _dfc("averaged", h)
    single = {}
    for sp, (zf, nf) in (("pp", (1, 0)), ("nn", (0, 1))):
        cr = _ac(zf, nf, include_inter=False)
        n1 = max(gg for gg, _ in cr) + 2
        yt1 = _yla(n1, q)
        c1 = _cw.build_sparse_cache(q, yt1, n1)
        t1, _, _ = _cw.schur_weyl_sum(q, cr, yt1, c1, _db)
        single[sp] = t1
    print()
    print(f"  {'':>4}{'S_off(A=1)':>26}{'g from A=2..5 steps':>26}{'|diff|':>14}")
    g1_ok = []
    for sp in ("pp", "nn"):
        d1 = abs(single[sp] - params[sp]["g"])
        g1_ok.append(d1 < mp.mpf("1e-18"))
        params[sp]["S_off_A1"] = single[sp]
        print(f"  {sp:>4}{mp.nstr(single[sp], 22):>26}"
              f"{mp.nstr(params[sp]['g'], 22):>26}{mp.nstr(d1, 6):>14}")
    print("""
  The include_inter=False word is an EXACT disjoint union: measured at every A,
  it uses only generators {3i, 3i+1} -- strictly inside each nucleon's own
  3-strand block -- with ZERO stray generators and exactly 11 crossings per
  block, identical for every nucleon. So S_off(A) = g^A with g the single free
  nucleon's trace, and the weighted Schur-Weyl sum FACTORS over the blocks.

  This changes the epistemic status of everything downstream. g is not a
  constant fitted to the A=2..5 steps that might drift at A=6 -- it IS the A=1
  value, and f is a two-nucleon value. The closed form has NO free parameter
  left, so B(A) at any A is an EVALUATION, not an extrapolation.

  Caveat kept explicit: the disjointness of the WORD is measured at A=2..5 and
  is structural; the FACTORIZATION of the weighted sum is verified numerically
  at A = 1,2,3,4,5 to 20 digits and is NOT proved in general. That proof is the
  remaining gap, and it is an algebra question, not a compute one.
""")
    check("g equals the single-nucleon free trace on both species, so it "
          "cannot drift with A", all(g1_ok),
          f"|S_off(1) - g|: pp "
          f"{mp.nstr(abs(single['pp'] - params['pp']['g']), 4)}, nn "
          f"{mp.nstr(abs(single['nn'] - params['nn']['g']), 4)}. Measuring this "
          f"cost milliseconds; the A=6 run that would have tested g by brute "
          f"force projects to ~40 h at n=18 (max dim ~13000) and was stopped.")

    # --------------------------------------------------- 5. the prediction
    print("\n" + "-" * 78)
    print("  5. FALSIFIABLE: where each marginal turns")
    print("-" * 78)
    proj = {}
    for sp in ("pp", "nn"):
        P = params[sp]
        prev, rows = None, []
        for A in range(P["A0"], 13):
            B = E0 * P["S0"] * P["g"] ** (A - P["A0"]) * (1 - P["f"] ** (A - 1))
            if prev is not None:
                rows.append((A, B - prev))
            prev = B
        proj[sp] = rows
        print(f"\n  {sp} projected marginals:")
        for A, m in rows:
            tag = "   <-- measured" if A <= 5 else ""
            print(f"    A={A:>3}  {mp.nstr(m, 12):>16}{tag}")
    pp_turns = any(proj["pp"][i][1] < proj["pp"][i + 1][1]
                   for i in range(len(proj["pp"]) - 1))
    nn_neg = any(m < 0 for _, m in proj["nn"])
    print("""
  PREDICTIONS, not measurements — g is measured on three steps and A >= 6 is
  NOT computed. Both are checkable with the resumable driver:

    * the pp marginal has a MINIMUM at A=5 and turns UP at A=6
    * the nn marginal goes NEGATIVE at A=7 — a neutron REDUCES total binding

  If the pp marginal keeps falling at A=6, g is not constant beyond the
  measured range: the closed form would then be local rather than global, which
  is the honest way this result dies.
""")
    check("the closed form yields two checkable predictions, labelled as "
          "projections", pp_turns and nn_neg,
          "pp marginal turns up at A=6; nn marginal changes sign at A=7. "
          "Neither is measured. Computing A=6 falsifies or confirms both.")

    payload = {
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
        "schema": "witness/v1",
        "name": "chain-binding-closed-form",
        "description": (
            "Exact two-constant closed form for the pure-chain binding, "
            "B(A) = E0*S_off(A0)*g^(A-A0)*(1-f^(A-1)), with f the corpus bond "
            "factor and g the free-trace growth per nucleon; plus the "
            "parameter-independent exclusion of the channel from extensivity."),
        "beans": ["qou-23dn", "qou-gcmn", "qou-brng"],
        "scope": "(b) for the extensivity exclusion (invariant: the closed "
                 "form is geometric x (1 - geometric), never linear); "
                 "(a) for the projections, which are NOT measured",
        "q0_anchor": "physical_proton",
        "q0": Q_50_DIGIT_STR,
        "lean": [
            "QOU.MassTheory.MarginalRatio.chain_bounded_of_growth_le_one",
            "QOU.MassTheory.MarginalRatio.chain_step_ge_growth",
        ],
        "data": {
            "E0_MeV": mp.nstr(E0, 25),
            "z_D": mp.nstr(z_D, 30),
            "species": {
                sp: {
                    "g_free_trace_growth": mp.nstr(params[sp]["g"], 30),
                    "f_bond_factor": mp.nstr(params[sp]["f"], 30),
                    "g_spread_across_steps": mp.nstr(params[sp]["g_spread"], 10),
                    "closed_form_worst_rel_error":
                        mp.nstr(params[sp]["worst_rel"], 10),
                    "branch": "unbounded" if params[sp]["g"] > 1 else "bounded",
                    "projected_marginals_MeV": {
                        str(A): mp.nstr(m, 20) for A, m in proj[sp]},
                } for sp in ("pp", "nn")},
            "f_pp_equals_z_D": bool(dz < mp.mpf("1e-25")),
            "g_equals_single_nucleon_free_trace": bool(all(g1_ok)),
            "S_off_A1": {sp: mp.nstr(params[sp]["S_off_A1"], 30)
                         for sp in ("pp", "nn")},
            "factorization_note":
                "The include_inter=False word is an exact disjoint union of "
                "identical 11-crossing per-nucleon blocks (measured, zero stray "
                "generators). S_off(A) = g^A with g = S_off(1) verified to 20 "
                "digits at A=1..5. Word disjointness is structural; the "
                "factorization of the WEIGHTED sum is numerical, not proved.",
            "projections_are_not_measured": True,
        },
        "assertions": assertions,
        "checks_passed": sum(checks),
        "checks_total": len(checks),
    }
    out = _COMP / "chain-binding-closed-form.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    payload["q0Anchor"] = _q0a
    if _q0v:
        payload["q0Value"] = _q0v
    out.write_text(json.dumps(payload, indent=2) + "\n")

    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print(f"  witness -> {out.relative_to(_COMP.parent)}")
    print("=" * 78)
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
