import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gs-cost-jones-recursion",
  title:
    "Gröbner--Shirshov reduction on $H_n(q)$ implements the Jones recursion",
  lean: {
    decl: "UGB.GrobnerShirshov.Hecke.gs_cost_jones_recursion",
    validation: "not_checked",
  },
  tags: [
    "hecke-algebra",
    "jones-polynomial",
    "skein-relation",
    "s-polynomial",
    "markov-trace",
  ],
  uses: [
    "def:jet-stratified-reduction",
    "thm:ugb-buchberger",
    "prop:ugb-s-poly-decomposition",
    "quantum-observable-universe:thm:jones-markov-trace",
  ],
  cites: ["jones1987", "kassel1995", "bergman1978", "bokut-shiao2001"],
});
