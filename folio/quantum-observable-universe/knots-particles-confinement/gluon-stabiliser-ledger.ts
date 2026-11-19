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
        "`fsh-guts/deprecated/computations/integer-lp-gluon.py` ranges over " +
        "`{σ₀, σ₁, L₊, L₋}` words up to length three. Both reach `e⁻`.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Evidence for the `e⁻` claim. Re-running the retired producer's " +
        "enumeration in its own convention reproduces its witness exactly " +
        /* <!-- literal-source: scratch re-run of retired producer in retired z^3 convention (no witness minted, noted below) --> */
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
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**(1) above is settled, and it goes the way the caveat feared** " +
        "(bean `qou-jqjx`, closed). Rebuilt on the retired script's own typed " +
        "nucleon so only the convention varies, and reproduced the corpus's " +
        /* <!-- literal-source: scratch reproduction of retired z^3 weight values (-0.005936 / -0.132224) in qou-jqjx audit --> */
        "numbers exactly on the retired weight (`-0.005936` / `-0.132224` " +
        "against the quoted `-0.006` / `-0.132`). On live convention D — " +
        "`z = q^3/(q^2+1)` and `tr_M(e-) = h*z^2 + z`, which `pyhecke.gram` " +
        "exports and `computations/universal-ilp.py` consumes through " +
        "`hecke_core` — the same elements are `+0.544370` and `+0.408267`, " +
        "and every intermediate step of both typed builds is positive as " +
        "well. There is no instability at any point, so the gluon is not " +
        "required. The proton and neutron blocks now carry the withdrawal.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Two details worth keeping. First, the retired script prints " +
        "`Gram matrix: corrected (tr_M(e-) = z^3 ...)` — it calls the bug the " +
        "correction, which is why the defect survived being looked at. " +
        "Second, convention D's Gram is singular (`lambda_min ~ 3e-16`, " +
        "radical `(-1/q)^len(w)`), and `gram.py`'s header warns that fixing " +
        "the trace alone drops a singular Gram into a path with nothing to " +
        "handle it. That warning is about inverting `G` and does not reach " +
        "this verdict: `G(x - c*v) = G x` exactly when `G v = 0`, so " +
        "Frobenius positivity is already well defined on the quotient. " +
        "Measured, projecting the radical out moves `min(G x)` by 5.6e-17 " +
        "against margins of +0.339 and +0.218.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "This makes (2) sharper rather than moot. With bare feasible for " +
        "both nucleons the minimum-crossing objective returns 0 gluon " +
        "crossings each, and the `|tr_M|` tiebreak returns a single `sigma_0` " +
        "each — 1:1. So the two objectives no longer disagree about which " +
        "nucleon needs more; they agree there is no asymmetry. `qou-v5fp`'s " +
        "question (which objective the corpus means) still needs an answer, " +
        "but it can no longer rescue the 2-versus-4 split either way.",
    },
    {
      kind: "status",
      date: "2026-09-04",
      body:
        "**Prose swept to match.** The closing paragraph asserted *\"the " +
        "proton takes two gluon crossings and the neutron four, and that " +
        "difference is what makes the neutron heavier and so feeds " +
        "$\\mathfrak{Q}_\\beta$\"* for eleven days after that claim had been " +
        "withdrawn — and the withdrawal was already recorded **in this very " +
        "block's author notes**, one entry above, on 2026-08-24. The note " +
        "and the prose disagreed and the prose was the one a reader saw. " +
        "The neutron block was separately corrected 13 -> 11 crossings on " +
        "2026-08-29 (`qou-vtlj`, owner-authorised correction 1 of 4), which " +
        "makes the gluon count 2 for both nucleons. The sentence is now " +
        "struck with the count stated, and the four-statements tally " +
        "re-counted from three distinct answers to two ({1, 2, 2, 2}). " +
        "No number moves: this block emits no witness and computes nothing.",
      see: "docs/audits/2026-09-04-delta-net-canon-and-crossing-count-analysis.md",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/universal-ilp.py",
    witness: [
      "computations/universal-ilp.witness.json",
      "computations/qbeta/qbeta-delta-net-four-values.witness.json",
      "computations/qbeta/integer-lp-gluon-convention-d.witness.json",
      "computations/atomic-chirality-residue.witness.json",
    ],
    status: "verified",
  },
});
