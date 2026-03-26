import { example } from "../../schema/builders";

export default example({
  label: "ex:hadron-half-life-verification",
  title: "Half-life predictions for selected beta emitters",
  tags: [
    "half-life",
    "beta-decay",
    "verification",
    "numerical",
    "tritium",
    "cobalt-60",
    "carbon-14",
  ],
  uses: [
    "prop:hadron-half-life",
    "rem:hadron-half-life-regimes",
    "prop:integer-stability",
    "def:substrate-parameter",
  ],
});
