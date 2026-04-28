import { proof } from "../../schema/builders";

export default proof({
  label: "prf:shannon-jones-markov-no-go",
  title:
    "Proof of `prop:shannon-jones-markov-no-go` (independent computational validation)",
  of: "prop:shannon-jones-markov-no-go",
  lean: {
    ref: "qou:QOU.BraidKnot.shannon_jones_markov_no_go",
    validation: "not_checked",
  },
  computation: {
    script:
      "folio-assistant/computations/tau_codim_conjectures_validate.py",
    witness:
      "folio-assistant/computations/tau-codim-conjectures-validation.witness.json",
  },
  uses: ["prop:shannon-jones-markov-no-go"],
});
