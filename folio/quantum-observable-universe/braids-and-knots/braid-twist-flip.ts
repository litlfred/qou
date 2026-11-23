import { definition } from "../../schema/builders";

export default definition({
  label: "def:braid-twist-flip",
  lean: { ref: "qou:QOU.BraidTwistFlip", validation: "not_checked" },
  title: "Braid involutions: twist and flip",
  tags: ["braid-group", "involution", "s3", "dihedral"],
  uses: ["def:su2-generators"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The four spectral resolvents $w_1,\\dots,w_4$ carry this action through the conjugate pairs $(w_1,w_4)$ and $(w_2,w_3)$ and the projective ratios $\\eta_1=w_1/w_2$, $\\eta_2=w_3/w_4$ ([the braid-group action](#rem:braid-group-action)): the reflection swaps the conjugate pairs, and the rotation cycles the three branches. The action lives on the branches rather than on the resolvents because $S_3$ has no faithful action on four points ($4\\nmid 6$)." },
  ],
  examples: ["rem:holonomy-trefoil"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/braid-twist-flip-0.svg", blockIndex: 0, hash: "336b117e82c3" },
    { mime: "image/svg+xml", url: "rendered/braid-twist-flip-1.svg", blockIndex: 1, hash: "beaff1e729c8" },
  ],

});
