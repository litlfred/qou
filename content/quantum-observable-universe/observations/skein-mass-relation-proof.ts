import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-mass-relation",
  title: "Proof of $q$-Deformed Skein Relation",
  uses: ["rem:skein-mass-relation"],
  lean: { ref: "qou:QOU.HadronicMass.SkeinMassRelation",
    validation: "leanok",
  },
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
  ],
});
