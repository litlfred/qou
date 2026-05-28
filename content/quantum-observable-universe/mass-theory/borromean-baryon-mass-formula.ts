import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borromean-baryon-mass-formula",
  title:
    "Borromean baryon mass formula with common scale $\\lambda_{\\mathrm{scale}}$",
  lean: {
    ref: "qou:QOU.Borromean.MassFormula",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script:
      "folio-assistant/computations/derive_m_baryon_volume_form.py",
    witness:
      "folio-assistant/computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
  uses: [
    "def:borromean-baryon",
    "def:quantum-planck-constant",
    "def:algebraic-quantum-volume",
    "def:typed-crossing-operator",
    "prop:three-calibration-inputs",
    "thm:topological-mass",
    "prop:graded-hecke-energy-truncation-bound",
  ],
  cites: [
    "thurston1978",
    "kashaev1997",
    "murakami-murakami2001",
    "codata2022",
  ],
  tags: [
    "borromean",
    "baryon",
    "mass-formula",
    "topological-mass",
    "lambda-scale",
    "common-scale",
    "open-problem",
    "substrate-only",
    "vol-form",
  ],
});
