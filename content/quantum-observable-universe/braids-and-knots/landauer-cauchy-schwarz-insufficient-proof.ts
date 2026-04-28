import { proof } from "../../schema/builders";

export default proof({
  label: "prf:landauer-cauchy-schwarz-insufficient",
  title:
    "Proof of `prop:landauer-cauchy-schwarz-insufficient` (balanced-family witness + computational validation)",
  of: "prop:landauer-cauchy-schwarz-insufficient",
  lean: {
    ref:
      "qou:QOU.BraidKnot.landauer_cauchy_schwarz_insufficient",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    status: "verified",
    script:
      "folio-assistant/computations/tau_codim_conjectures_validate.py",
    witness:
      "folio-assistant/computations/tau-codim-conjectures-validation.witness.json",
    requires: ["numpy", "scipy", "mpmath"],
  },
  uses: ["prop:landauer-cauchy-schwarz-insufficient"],
});
