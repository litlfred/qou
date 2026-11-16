import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-error-amplification",
  title: "Binding-energy error amplification: $\\mathcal{A} = M_{\\mathrm{atom}}/B$",
  lean: {
    ref: "qou:QOU.MassTheory.BindingErrorAmplification.binding_rel_error",
    validation: "not_checked",
  },
  uses: ["conj:binding-scale-catalan"],
});
