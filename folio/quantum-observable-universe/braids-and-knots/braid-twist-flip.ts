import { definition } from "../../schema/builders";

export default definition({
  label: "def:braid-twist-flip",
  lean: { ref: "qou:QOU.BraidTwistFlip", validation: "not_checked" },
  title: "Braid involutions: twist and flip",
  tags: ["braid-group", "involution", "s3", "dihedral"],
  uses: ["def:su2-generators"],
  examples: ["rem:holonomy-trefoil"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/braid-twist-flip-0.svg", blockIndex: 0, hash: "336b117e82c3" },
    { mime: "image/svg+xml", url: "rendered/braid-twist-flip-1.svg", blockIndex: 1, hash: "beaff1e729c8" },
  ],

});
