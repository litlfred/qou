import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:planck-time",
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
    "finite-field",
    "p-adic",
    "algebraic-dynamics",
  ],
  uses: [
    "rem:julia-set-reeb",
    "def:bundle-initial-conditions",
    "prop:substrate-radial-coordinate",
    "rem:witt-lift-qou",
  ],
  cites: ["thooft2016"],
});
