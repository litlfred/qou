import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:su2-emergence",
  lean: { ref: "qou:QOU.RankOneGaugeData", validation: "not_checked" },
  title: "Emergence of the gauge group",
  uses: ["def:quantum-observable-universe"],
  proofs: ["prf:su2-emergence"],
  examples: ["ex:su2-emergence"],
  tags: ["emergence", "gauge-group", "su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/su2-emergence-0.svg", blockIndex: 0, hash: "ff77986f66d2" },
    { mime: "image/svg+xml", url: "rendered/su2-emergence-1.svg", blockIndex: 1, hash: "e6bb15a051f3" },
  ],

});
