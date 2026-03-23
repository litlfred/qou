import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-harmonic-form",
  title: "$q$-harmonic form (particle)",
  tags: ["particle", "harmonic"],
  lean: {
    decl: "QOU.QHarmonicForm",
    validation: "leanok",
  },
  status: "stated",
  uses: ["def:categorical-q-ext-deriv"],
});
