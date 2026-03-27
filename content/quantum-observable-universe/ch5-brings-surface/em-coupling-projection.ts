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
  ],
  lean: {
    decl: "QOU.Descartes.em_coupling_projection",
    validation: "not_checked",
  },
  uses: [
    "rem:force-knot-identification",
    "rem:unmapped-torus-knots",
    "prop:antiparticle-crossing-reversal",
    "prop:torus-embeddable-complete",
    "prop:torus-knot-generators",
  ],
});
