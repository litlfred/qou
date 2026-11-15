import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lichnerowicz-wkb-corollary",
  interprets: "prop:categorical-lichnerowicz",
  title: "Lichnerowicz identity reduces the $\\Phi_q$-WKB conjecture",
  tags: ["lichnerowicz", "q-laplacian", "categorical-dirac", "wkb"],
  uses: [
    "prop:categorical-lichnerowicz",
    "def:categorical-instanton",
  ],
});
