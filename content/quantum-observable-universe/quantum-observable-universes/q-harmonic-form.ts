import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-harmonic-form",
  title: "Particle ($q$-harmonic form)",
  tags: ["particle", "harmonic"],
  lean: {
    decl: "QOU.QHarmonicForm",
    validation: "leanok",
  },
  uses: ["def:categorical-q-ext-deriv"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/q-harmonic-form-0.svg", blockIndex: 0, hash: "4b36efb57e86" },
  ],

});
