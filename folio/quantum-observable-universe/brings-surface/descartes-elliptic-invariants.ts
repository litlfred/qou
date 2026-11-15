import { remark } from "../../schema/builders";

export default remark({
  label: "rem:descartes-elliptic-invariants",
  title: "Invariants and classical limit of $\\mathcal{E}_q$",
  interprets: "prop:descartes-elliptic-curve",
  tags: [
    "elliptic-curve",
    "descartes",
    "j-invariant",
    "classical-limit",
    "weierstrass",
  ],
  uses: ["prop:descartes-elliptic-curve"],
});
