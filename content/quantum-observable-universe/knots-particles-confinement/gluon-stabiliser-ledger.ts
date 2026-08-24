import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:derived-atom",
  label: "rem:gluon-stabiliser-ledger",
  title: "The gluon ledger: what step 4 enumerates, and why the trefoil loses",
  tags: [
    "gluon",
    "stabiliser",
    "ilp",
    "frobenius-positivity",
    "nucleon",
    "confinement",
    "lepton-number",
  ],
  uses: [
    "def:derived-atom",
    "def:universal-ilp-algorithm",
    "rem:ilp-solution-count-unwrap",
    "fundamental-knots-operator-basis",
    "def:lepton-number-categorical",
    "rem:lepton-number-categorical-properties",
    "rem:nucleon-from-photons-summary",
    "rem:categorical-proton-properties",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Closes bean `qou-1ngr`, which asked why the gluon stabiliser may " +
        "not be `e⁻ = σ₀σ₁σ₀` and proposed two reasons (lepton number; " +
        "double counting). Neither holds, and neither is needed: the " +
        "premise that the feasible set is restricted to `L±` is wrong. " +
        "`computations/universal-ilp.py` ranges over `{σ₀, σ₁, σ₀⁻¹, " +
        "σ₁⁻¹}` words up to six crossings; the retired " +
        "`computations/_deprecated/integer-lp-gluon.py` ranges over " +
        "`{σ₀, σ₁, L₊, L₋}` words up to length three. Both reach `e⁻`.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Evidence for the `e⁻` claim. Re-running the retired producer's " +
        "enumeration in its own convention reproduces its witness exactly " +
        "(proton 40 survivors, optimum `σ₀→σ₀` at |tr_M| = 0.0274; neutron " +
        "26 survivors, optimum `L₊→L₋` at 0.1120), and `e⁻` appears among " +
        "the survivors of both — as `σ₀→L₋` (proton, rank 35/40, |tr_M| = " +
        "1.173) and as `L₊→σ₀` (neutron, rank 21/26, |tr_M| = 1.105). So " +
        "`e⁻` is admissible and simply loses. The 84 of " +
        "`rem:ilp-solution-count-unwrap` is 4 + 4² + 4³, the *enumerated* " +
        "count, not the feasible count — that block calls it feasible and " +
        "should say candidate. Scratch re-run only; no witness was minted.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "The sibling `rem:antiquark-channel-ledger` closes the same shape of " +
        "gap at step 2 and would be the natural cross-link, but it and " +
        "`rem:pion-mass-hyperbolic-threshold` are both absent from " +
        "`knots-particles-confinement.ts`, so their labels do not resolve " +
        "and neither block renders. Linking either fails validation. " +
        "Registering them needs an ordering decision — the ledger uses the " +
        "pion remark, which sits in a later section — so it is left to bean " +
        "`qou-bzy0` rather than done here.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "Two things found while checking this that are larger than the bean " +
        "and are NOT fixed here. (1) The retired producer used `tr_M(e⁻) = " +
        "z³`, which the 2026-05-19 fix replaced with `h·z² + z` " +
        "(`tools/pyhecke/python/pyhecke/gram.py`). On the corrected weight " +
        "the bare 9-crossing nucleon is already Frobenius-positive, so " +
        "\"the gluon is strictly required by the LP dual\" and the quoted " +
        "tr_M = −0.006 / −0.132 do not survive the convention change — " +
        "bean `qou-jqjx`. (2) `computations/universal-ilp.witness.json` " +
        "records the gluon as `σ₁` at one crossing and confinement as " +
        "`σ₁` at one crossing, against B₃'s six; its assertions compare " +
        "the script to its own `expected` values, so `status: " +
        "\"verified\"` does not check the corpus's crossing counts — bean " +
        "`qou-v5fp`, which also has the per-crossing-shell numbers showing " +
        "min-cr and min-|tr_M| disagree. The 2-versus-4 split feeding " +
        "CAL-2 rests on the retired producer alone.",
    },
  ],
});
