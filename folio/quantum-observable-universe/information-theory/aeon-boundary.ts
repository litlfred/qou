import { definition } from "../../schema/builders";

export default definition({
  label: "def:aeon-boundary",
  title: "Boundary of an aeon",
  tags: [
    "aeon", "jet-horizon", "boundary",
    "big-bang", "cyclic-cosmology",
  ],
  lean: { ref: "qou:QOU.aeonBoundary",
    validation: "not_checked",
  },
  uses: [
    "def:aeon",
    "def:big-bang-state",
    "def:cmb-boundary-datum",
  ],
  cites: ["penrose2010"],
});
