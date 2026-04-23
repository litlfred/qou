import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-mass-relation",
  title: "Proof of $q$-Deformed Skein Relation",
  uses: ["rem:skein-mass-relation"],
  lean: { ref: "qou:QOU.HadronicMass.SkeinMassRelation",
    validation: "leanok",
  },
});
