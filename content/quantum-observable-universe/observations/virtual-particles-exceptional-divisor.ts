import { remark } from "../../schema/builders";

export default remark({
  label: "rem:virtual-particles-exceptional-divisor",
  title: "Virtual particles as excitations of the exceptional divisor",
  interprets: "def:recursive-brane-tower",
  uses: [
    "def:exceptional-divisor",
    "def:recursive-brane-tower",
    "prop:vertex-is-exceptional-divisor",
    "prop:jet-prolongation",
    "rem:heisenberg-commutator",
  ],
  tags: [
    "virtual-particles", "exceptional-divisor", "brane-tower",
    "propagator", "off-shell", "interpretation",
  ],
});
