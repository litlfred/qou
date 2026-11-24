import { remark } from "../../schema/builders";

export default remark({
  label: "rem:kz-connection-sl2-remark",
  title: "Residues, flatness and monodromy of the KZ connection",
  interprets: "def:kz-connection-sl2",
  cites: ["kohno1987", "drinfeld1991"],
  uses: [
    "def:kz-connection-sl2",
    "prop:categorical-mass-markov",
  ],
});
