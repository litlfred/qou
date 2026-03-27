import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-planck-constant",
  label: "rem:discrete-planck-step",
  title: "Discrete time at the Big Bang: one Planck step of Reeb flow",
  tags: [
    "planck-time",
    "discrete-time",
    "big-bang",
    "reeb-flow",
    "information-theory",
    "dynamical-flow",
    "primordial-vortex",
  ],
  uses: [
    "def:quantum-planck-constant",
    "ex:q-reeb-flow",
    "def:substrate-parameter",
    "rem:reeb-exceptional-divisor",
    "rem:golden-ratio-degeneration",
    "rem:golden-ratio-transport",
    "rem:julia-set-reeb",
    "def:bundle-initial-conditions",
    "rem:substrate-radial-coordinate",
  ],
});
