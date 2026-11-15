import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:molecular-bond-binding-from-trefoil-insertion",
  title: "Molecular bond binding energy from inverse-trefoil insertion",
  lean: {
    ref: "qou:QOU.BraidKnot.bondEnergy",
    validation: "not_checked",
  },
  uses: ["prop:confined-knot-binding"],
  cites: ["adams1985hyperbolic"],
  tags: [
    "binding-mechanism",
    "molecular-bond",
    "covalent-bond",
    "inverse-trefoil",
    "hartree-energy",
    "wedderburn",
  ],
});
