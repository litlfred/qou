import { remark } from "../../schema/builders";

export default remark({
  label: "rem:information-theoretic-time-properties",
  interprets: "def:information-theoretic-time",
  title: "Reeb time coordinate, three regimes, and the arrow of time",
  tags: [
    "information-theory",
    "planck-time",
    "discrete-time",
    "statistical-mechanics",
    "reeb-flow",
    "julia-set",
  ],
  uses: [
    "def:information-theoretic-time",
    "prop:reeb-operations-per-planck",
    "prop:ordering-jet-compatibility",
    "prop:local-substrate-q",
    "def:planck-time",
    "ex:q-reeb-flow",
  ],
});
