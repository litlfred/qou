import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:coxeter-parabolic-transversal",
  lean: {
    ref: "qou:QOU.Machinery.CoxeterParabolic.braid_at_pair",
    validation: "not_checked",
  },
  title:
    "Parabolic transversals and the Hecke presentation laws at every rank",
  tags: [
    "coxeter",
    "hecke-algebra",
    "parabolic-subgroup",
    "braid-relation",
    "coset-decomposition",
  ],
  uses: ["prop:coxeter-strong-exchange", "def:hecke-normal-form"],
  cites: ["kassel1995", "jones1987"],
});
