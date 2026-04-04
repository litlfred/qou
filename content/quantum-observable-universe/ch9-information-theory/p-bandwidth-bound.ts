import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:p-bandwidth-bound",
  title: "Polynomial computation as sub-horizon bandwidth",
  tags: [
    "P-class",
    "bandwidth",
    "information-flow",
    "planck-step",
    "complexity",
    "polynomial-time",
  ],
  uses: [
    "def:computational-horizon",
    "def:information-speed-of-light",
    "def:operational-entropy",
    "rem:skein-turing-machine",
    "prop:reeb-operations-per-planck",
  ],
});
