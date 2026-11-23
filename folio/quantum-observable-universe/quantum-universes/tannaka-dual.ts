import { definition } from "../../schema/builders";

export default definition({
  label: "def:tannaka-dual",
  title: "Tannaka dual (emergent gauge group)",
  lean: { ref: "qou:QOU.TannakaDual", validation: "not_checked" },
  uses: ["def:quantum-universe"],
  cites: ["saavedra-rivano1972", "deligne1990"],
  tags: [
    "category-theory",
    "tannaka-krein",
    "gauge-group",
    "fibre-functor",
  ],
});
