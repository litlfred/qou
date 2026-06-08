import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mobius-surreal-renormalization",
  title: "Möbius energy as a difference of infinite surreals",
  interprets: "prop:mobius-energy",
  uses: [
    "prop:mobius-energy",
    "def:surreal-blowup-calculus",
    "rem:conway-normal-form",
  ],
  cites: ["ohara1991", "freedman-he-wang1994"],
});
