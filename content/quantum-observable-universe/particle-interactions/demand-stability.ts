import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:demand-stability",
  title: "Demand profile determines nuclear and atomic stability",
  tags: [
    "stability",
    "demand",
    "normal-form",
    "beta-decay",
    "shell-closure",
    "magic-numbers",
  ],
  uses: [
    "def:derived-atom",
    "prop:confinement-operator-selection",
    "descartes-universe:def:stable-nucleus",
    "descartes-universe:prop:beta-stability",
  ],
});
