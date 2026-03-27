import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:jet-prolongation",
  label: "rem:jet-planck-steps",
  title:
    "Planck steps as jet orders: Taylor approximation of $E$ at the Big Bang",
  tags: [
    "jet-bundle",
    "planck-time",
    "discrete-time",
    "big-bang",
    "taylor-polynomial",
    "chiral-cubic",
    "golden-ratio",
    "brane-tower",
    "information-theory",
    "finite-field",
  ],
  uses: [
    "prop:jet-prolongation",
    "def:recursive-brane-tower",
    "rem:discrete-planck-step",
    "prop:chiral-elliptic",
    "rem:golden-ratio-degeneration",
    "def:categorical-q-connection",
    "def:quantum-planck-constant",
    "ex:q-reeb-flow",
    "rem:j1e-local-states",
    "def:bundle-initial-conditions",
    "ex:finite-field-realisation",
  ],
});
