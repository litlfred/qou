import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qou-is-ccc",
  title: "A QOU with aeons is a conformal cyclic cosmology",
  tags: [
    "ccc", "aeon", "conformal-cyclic-cosmology",
    "penrose", "jet-horizon", "conformal-invariance",
  ],
  lean: {
    decl: "QOU.qou_is_ccc",
    validation: "not_checked",
  },
  uses: [
    "def:aeon",
    "def:jet-horizon",
    "def:big-bang-state",
    "def:cmb-boundary-datum",
    "prop:horizon-conformal-invariance",
    "def:observation",
  ],
  cites: ["penrose2010"],
});
