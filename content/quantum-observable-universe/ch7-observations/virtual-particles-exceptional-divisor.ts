import { remark } from "../../schema/builders";

export default remark({
  label: "rem:virtual-particles-exceptional-divisor",
  title: "Virtual particles as excitations of the exceptional divisor",
  interprets: "def:recursive-brane-tower",
  uses: [
    "def:jet-prolongation",
    "rem:time-reversal-energy-barrier",
    "rem:reidemeister-mass-invariance",
  ],
  tags: [
    "virtual-particles", "exceptional-divisor", "brane-tower",
    "propagator", "off-shell", "interpretation",
  ],
});
