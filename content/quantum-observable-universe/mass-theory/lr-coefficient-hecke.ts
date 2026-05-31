import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lr-coefficient-hecke",
  title:
    "Littlewood-Richardson coefficient $c^\\lambda_{\\mu\\nu}$ for Iwahori-Hecke branching",
  chapter: "mass-theory",
  cites: ["wenzl1988", "ariki1996", "ram1991"],
  uses: [],
  defines: [],
  tags: [
    "littlewood-richardson",
    "branching",
    "hecke-algebra",
    "wedderburn",
    "non-negative-integer",
  ],
  lean: { ref: "qou:QOU.BraidKnot.LRCoefficientHecke" },
});
