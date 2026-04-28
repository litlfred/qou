import { definition } from "../../schema/builders";

export default definition({
  label: "def:cmb-boundary-datum",
  title: "CMB as boundary datum of a big bang state",
  tags: [
    "cmb", "boundary-datum", "jet-horizon",
    "big-bang-state", "aeon", "degree-one",
  ],
  lean: { ref: "qou:QOU.CMBBoundaryDatum",
    validation: "not_checked",
  },
  uses: ["def:aeon"],
});
