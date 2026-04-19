import { remark } from "../../schema/builders";

export default remark({
  interprets: "unital-groebner-bases:prop:gs-cost-jones-recursion",
  label: "rem:hecke-energy-jones-recursion",
  title:
    "Hecke energy $\\kappa_c^{\\mathrm{comp}}$ as Jones-recursion cost",
  tags: [
    "hecke-algebra",
    "jones-polynomial",
    "hecke-energy",
    "skein-recursion",
    "kappa",
    "computational-cost",
  ],
  uses: [
    "def:skein-resolution-obstruction",
    "thm:jones-markov-trace",
    "unital-groebner-bases:prop:gs-cost-jones-recursion",
  ],
  cites: ["jones1987", "kassel1995"],
});
