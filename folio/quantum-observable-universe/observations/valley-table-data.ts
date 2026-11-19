import { table } from "../../schema/builders";

export default table({
  label: "tbl:valley-table-data",
  title: "Representative stable isotopes: Coulomb ratio and Diophantine error",
  caption:
    "Representative elements spanning the periodic table, comparing the continuous beta-stability prediction $p^*(A)$ with the observed stable proton number, the neutron-to-proton ratio, and the Diophantine error $\\varepsilon = |p_{\\mathrm{stab}} - p^*|$. $\\diamond\\star$ marks doubly-stable nuclei with both low Diophantine error and closed Skein shell structure.",
  uses: ["rem:valley-table"],
  tags: ["valley-of-stability", "diophantine", "codata", "neutron-proton-ratio"],
});
