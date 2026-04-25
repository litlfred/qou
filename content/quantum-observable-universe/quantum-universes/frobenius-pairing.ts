import { definition } from "../../schema/builders";

export default definition({
  label: "def:frobenius-pairing",
  title: "Frobenius pairing",
  tags: ["category-theory", "frobenius", "hopf-algebra"],
  lean: { ref: "qou:QOU.FrobeniusHopfData.frobeniusForm",
    validation: "not_checked",
  },
  uses: ["def:quantum-universe"],
  examples: ["ex:frobenius-pairing-su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/frobenius-pairing-0.svg", blockIndex: 0, hash: "9097b644f678" },
  ],

});
