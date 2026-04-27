import { definition } from "../../schema/builders";

export default definition({
  label: "def:frobenius-hopf-substrate",
  title: "The quantum vacuum as a Frobenius--Hopf algebra",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate",
    validation: "not_checked",
  },
  uses: ["def:frobenius-pairing"],
  tags: ["frobenius", "hopf-algebra", "substrate", "vacuum"],
});
