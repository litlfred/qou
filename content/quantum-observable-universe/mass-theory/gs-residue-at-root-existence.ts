import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-residue-at-root-existence",
  title:
    "Existence of the cyclotomic residue at each filtration level",
  lean: {
    ref: "qou:QOU.BraidKnot.GBResidueSpectralSum.residue",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:gb-residue-spectral-sum",
    "prop:residue-at-root",
    "conj:gs-graded-markov-trace-existence",
    "def:habiro-ring",
  ],
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/term6_full_pole_sum.py",
    witness: [
      "folio-assistant/computations/term6-full-pole-sum.witness.json",
      "folio-assistant/computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "residue",
    "cyclotomic",
    "quantum-dilogarithm",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
