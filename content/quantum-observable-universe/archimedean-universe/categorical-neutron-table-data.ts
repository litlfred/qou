import { table } from "../../schema/builders";

export default table({
  label: "tbl:categorical-neutron-table-data",
  title: "Neutron Borromean braid: crossing pairs",
  caption:
    "Three crossing pairs in the Borromean neutron braid " +
    "$\\mathcal{B}_3(\\mathfrak{u},\\mathfrak{d},\\mathfrak{d})$: " +
    "one $\\mathfrak{d}$-$\\mathfrak{d}$ same-flavour pair and two " +
    "$\\mathfrak{u}$-$\\mathfrak{d}$ cross-flavour pairs, with their " +
    "Hecke crossing elements.",
  uses: ["def:categorical-neutron"],
  tags: ["neutron", "borromean", "crossing-pairs"],
});
