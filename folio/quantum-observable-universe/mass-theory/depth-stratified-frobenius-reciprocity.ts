import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Owner ruling 2026-09-05, re-affirmed 2026-09-08 and 2026-11-15: the canonical Phi_k weight is Molien $f^\\lambda q^{-\\kappa_\\lambda}\\dim_q(\\lambda)/[n]_q!$; $d_q^2/D^2$ is a labelled comparison arm (bean qou-oots). Prose previously called the choice open.",
    },
    {
      kind: "note",
      date: "2026-09-05",
      body: "Weight-family dependence of the K_3* ranking added 2026-09-05 (bean qou-oots). Measurements: docs/audits/2026-09-05-phi-k-weight-family.md; labelling sweep: docs/audits/2026-09-05-k3-weight-family-labelling.md.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note — deliberate two-sided placement.** The " +
        "mathematical core of the Lean sibling is **already generic**: " +
        "`uniformWedderburnWeight` and `frPulledBackWeight` are stated over " +
        "`{R : Type*} [Field R]` and closed by `field_simp`. The only `ℝ` are " +
        "the two **empirical falsification records** — " +
        "`(1.82 : ℝ) < 2.30 ∧ (1.82 : ℝ) < 5.94` and " +
        "`(3.96 : ℝ) > 2.31 ∧ (2.31 : ℝ) > 1.82 ∧ (1.82 : ℝ) < 5.47` — which " +
        "the module docstring itself introduces as \"empirical falsification " +
        "records as direct theorems\". Decimal measurements compared by `<` " +
        "are `ℝ` by §7c. So the generic construction and its numerical " +
        "realisation legitimately coexist in one file; the mixed-signal flag " +
        "is the criterion observing that coexistence, not a misplacement.",
    },
  ],
  label: "conj:depth-stratified-frobenius-reciprocity",
  title:
    "Frobenius-reciprocity ideal restriction at low curvature-rank",
  lean: {
    ref: "qou:QOU.BraidKnot.DepthStratifiedFrobeniusReciprocity",
    validation: "not_checked",
  },
  uses: [
    "cor:lr-tensor-character-bridge",
    "prop:chirality-from-frobenius-self-pairing",
  ],
  cites: ["frobenius1898", "macdonald1995", "lewin1981"],
  computation: {
    engine: "python",
    script:
      "computations/binding_depth_stratified_knot_weighted.py",
    witness:
      "computations/binding-depth-stratified-knot-weighted.witness.json",
    status: "experimental",
  },
  tags: [
    "tier:S",
    "frobenius-reciprocity",
    "curvature-rank",
    "knot-ideal",
    "chirality-channel",
    "binding-energy",
    "research-open",
    "drum-shape",
  ],
});
