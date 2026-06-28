import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:c5-involution-leibniz-decomposition",
  label: "rem:c5-involution-leibniz-falsifiable-prediction",
  title:
    "The $c_5$ falsifiable prediction: averaging-resonance $1/2$ fingerprints at $k = 8, 11, \\ldots$",
  uses: [
    "prop:c5-involution-leibniz-decomposition",
    "def:bar-involution",
  ],
  tags: [
    "qbeta",
    "falsifiable-prediction",
    "averaging-resonance",
    "ck-ladder",
  ],
});
