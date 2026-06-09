import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:em-coupling-projection",
  title:
    "Electromagnetic coupling from the antisymmetric braiding and force-carrier crossings",
  tags: [
    "electromagnetic",
    "fine-structure-constant",
    "coupling",
    "braiding",
    "q-integer",
    "crossing",
    "involution",
    "fibre-functor",
    "chern-simons",
    "descent-decomposition",
    "exceptional-divisor",
  ],
  lean: { ref: "qou:QOU.Archimedean.isEmCoupling_iff",
    validation: "not_checked",
  },
  uses: ["thm:em-spectral-completeness"],
});
