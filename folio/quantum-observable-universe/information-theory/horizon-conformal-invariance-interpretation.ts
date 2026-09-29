import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:horizon-conformal-invariance",
  label: "rem:horizon-conformal-invariance-interpretation",
  title: "Conformal invariance at the horizon as a consequence of observability",
  uses: [
    "prop:horizon-conformal-invariance",
    "def:observation",
  ],
  cites: ["penrose2010"],
});
