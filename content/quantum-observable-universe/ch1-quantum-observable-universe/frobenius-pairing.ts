import { definition } from "../../schema/builders";

export default definition({
  label: "def:frobenius-pairing",
  title: "Frobenius pairing",
  tags: ["category-theory", "frobenius", "hopf-algebra"],
  lean: {
    decl: "QOU.FrobeniusHopfData.frobeniusForm",
    validation: "not_checked",
  },
  uses: ["def:quantum-universe"],
  examples: ["ex:frobenius-su2"],
});
