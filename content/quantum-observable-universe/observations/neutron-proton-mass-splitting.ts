import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:neutron-proton-mass-splitting",
  title: "Neutron--proton mass splitting from quark crossing change",
  lean: { ref: "qou:QOU.NeutronProtonSplitting.splitting_value",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});
