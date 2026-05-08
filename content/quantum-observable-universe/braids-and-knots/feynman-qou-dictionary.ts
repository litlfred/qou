import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:feynman-categorical-trace",
  label: "rem:feynman-qou-dictionary",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.FeynmanQOUDictionary",
    validation: "not_checked",
  },
  title: "Dictionary: Feynman path integral $\\leftrightarrow$ QOU categorical trace",
  tags: ["path-integral", "feynman", "dictionary", "categorical-trace"],
  uses: [
    "def:categorical-transfer-matrix",
    "prop:feynman-classical-limit",
    "prop:photon-threading-mass",
  ],
});
