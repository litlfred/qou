import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-harmonic-form",
  title: "Particle",
  tags: ["particle", "harmonic"],
  lean: {
    decl: "QOU.QHarmonicForm",
    validation: "leanok",
  },
  status: "not_started",
  uses: ["def:categorical-q-ext-deriv"],
});
