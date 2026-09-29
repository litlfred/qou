import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braiding-eigenvalue-extraction",
  label: "rem:sqrt-q-ribbon-structure",
  title: "The element $\\sqrt{q}$ and the ribbon structure",
  tags: [
    "ribbon",
    "twist",
    "sqrt-q",
    "tqft",
    "framed-links",
    "braiding",
    "eigenvalue",
  ],
  uses: [
    "prop:braiding-eigenvalue-extraction",
    "rem:tqft-context",
  ],
});
