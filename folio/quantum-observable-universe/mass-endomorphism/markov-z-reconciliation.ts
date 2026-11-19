import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-z-reconciliation",
  title: "Reconciliation of the Markov parameter $z$",
  interprets: "prop:categorical-mass-markov",
  uses: ["prop:categorical-mass-markov"],
  tags: [
    "markov-trace",
    "normalization",
    "convention",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-03",
      body: "**Prior art, credited late (2026-09-03).** The classification above was already in Lean before this section was written, and the pull request that added it (#6370) did not cite any of it. `QOU.QBeta.WenzlWeight.wenzlLevel_conventionD` and `level_eq_two_of_conventionD` (PR #5242) prove that D is Wenzl level `r = 2`; `QOU.SchurWeyl.OcneanuWeight` (PR #5575) proves the `z_D` row cap from the general-`n` cell product and records that `z_D` is the `k = 2` member of `z = q^{2k+1}/(1 + q^2 + \\cdots + q^{2k})` — the family `z_N` above with `N = k`, the quantum integer written as its geometric sum — while C is in no member; `QOU.SchurWeyl.WenzlWeightLevelR.wenzlMarkovParam` is the family itself, of which the `markovZAt` theorems cited below are the Hecke-normalised copy `z_N = z_W/q`; and `QOU.SchurWeyl.OcneanuWeightWenzl.ocneanuWeight_conventionD_eq_schurPrincipal` is the hook-content identification at every partition. What this section adds beyond those is the framing-ratio *mechanism* — the monomial `a = q^N` collapsing each numerator into a quantum integer — and the log-derivative argument that C is in no member for any real exponent, not only for no integer one. The `n = 3` values are tied to the Markov-derived weights `HeckeMarkov3.markovWeight0/1/2` in `QOU.BraidKnot.QBetaCanonicalMarkovWeightsDerived`. Additional declarations in `QOU.Information`: `markovZNeg_eq`, `markov_loop_value_product`, `markov_framing_ratio_eq`, `markovZ_eq_qsq_div_qDimTwo`, `qDimTwo_sq_sub_hbar_sq`, `markovZAt_framing`, `markovZAt_two_eq_markovZ`, `ocneanu_numerator_collapse`, `qIntSym_two`; symbolic cross-check in `computations/probes/markov_loop_value_product_and_framing_ratio.py`.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/probes/interface-knot-markov-z-convention-d.witness.json",
      "computations/probes/graded_binding_sign_convention_probe.witness.json",
    ],
    status: "verified",
  },
});
