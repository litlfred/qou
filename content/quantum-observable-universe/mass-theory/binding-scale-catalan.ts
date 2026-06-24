import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-scale-catalan",
  proofs: ["prf:binding-scale-catalan"],
  title: "Binding energy scale $\\alpha = m_e \\times 8G$",
  lean: { ref: "qou:QOU.BindingScale.bindingScale_value",
    validation: "not_checked",
  },
  uses: ["def:borromean-baryon"],
  computation: {
    engine: "python",
    script: "computations/catalan_binding.py",
    witness: "computations/catalan-binding.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
});
