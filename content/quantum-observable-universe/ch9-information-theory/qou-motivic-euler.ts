import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qou-motivic-euler",
  title: "Motivic Euler characteristic of the QOU locus",
  uses: [
    "def:qou-motivic-measure",
    "def:qou-locus",
    "rem:axiom-independence",
    "rem:fibre-functor-rigidity",
  ],
  cites: ["denef2001", "yekutieli2010"],
  tags: ["motivic-integration", "euler-characteristic", "rigidity", "yekutieli"],
});
