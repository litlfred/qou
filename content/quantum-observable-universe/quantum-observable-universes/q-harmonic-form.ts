import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-harmonic-form",
  title: "Particle ($q$-harmonic form)",
  tags: ["particle", "harmonic"],
  lean: { ref: "qou:QOU.QHarmonicForm",
    validation: "leanok",
  },
  uses: ["def:categorical-q-ext-deriv"],
});
