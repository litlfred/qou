import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qou-is-ccc",
  proofs: ["prf:qou-is-ccc"],
  title: "A QOU with aeons is a conformal cyclic cosmology",
  tags: [
    "ccc", "aeon", "conformal-cyclic-cosmology",
    "penrose", "jet-horizon", "conformal-invariance",
  ],
  lean: { ref: "qou:QOU.qou_is_ccc",
    validation: "not_checked",
  },
  uses: ["prop:horizon-conformal-invariance"],
  cites: ["penrose2010"],
});
