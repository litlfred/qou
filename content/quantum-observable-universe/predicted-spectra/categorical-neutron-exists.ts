import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "status", date: "2026-06-26", body: "The Lean formalization currently provides a `sorry`-free weak proxy proof (`CategoricalNeutron.exists`) by instantiating a structure without stability or positivity field constraints (using free real fields). While the text describes a highly constrained LP-stable Borromean object, closing the gap to formalize the full constraint satisfaction is plausible because it strictly requires building out the Hecke normal form (NF) and linear programming infrastructure. The underlying construction is physically and mathematically consistent; the gap is entirely an artifact of missing computational algebra libraries in the formal environment rather than an unresolved theoretical doubt." },
  ],
  label: "prop:categorical-neutron-exists",
  title: "Existence of the categorical neutron",
  lean: { ref: "qou:QOU.CategoricalNeutron.exists",
    validation: "not_checked",
  },
  uses: ["prop:categorical-proton-exists"],
  proofs: ["prf:categorical-neutron-exists"],
  tags: ["existence", "neutron", "baryon"],
});
