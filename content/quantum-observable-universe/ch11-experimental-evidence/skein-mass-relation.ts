import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-mass-relation",
  title: "$q$-Deformed Skein Relation",
  uses: ["rem:skein-decomposition", "def:substrate-parameter", "def:quantum-planck-constant"],
  proofs: ["prf:skein-mass-relation"],
  lean: {
    decl: "QOU.HadronicMass.SkeinMassRelation",
    validation: "leanok",
  },
  tags: ["mass", "skein"],
});
