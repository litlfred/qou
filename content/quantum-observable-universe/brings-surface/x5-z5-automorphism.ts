import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:x5-z5-automorphism",
  proofs: ["prf:x5-z5-automorphism"],
  lean: { ref: "qou:QOU.HyperellipticQuintic.z5_automorphism", validation: "not_checked" },
  title: "$\\mathbb{Z}_5$ automorphism of the hyperelliptic quintic",
  tags: ["automorphism", "z5", "roots-of-unity", "hyperelliptic"],
  uses: [
    "def:hyperelliptic-quintic",
    "rem:lagrange-resolvents",
  ],
});
