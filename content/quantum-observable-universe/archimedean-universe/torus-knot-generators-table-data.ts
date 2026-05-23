import { table } from "../../schema/builders";

export default table({
  label: "tbl:torus-knot-generators-table-data",
  title: "Torus-knot generators admitted by the $\\chi(A) = -6$ constraint",
  caption:
    "Six coprime pairs $(m, n)$ with $m \\geq 2$ satisfying the genus " +
    "bound $(m-1)(n-1) \\leq 8$ from $\\chi(\\mathrm{Bring}) = -6$. " +
    "Together with $T_{1,0} = 0_1$ (unknot, genus 0), the generator set " +
    "has $|\\mathcal{G}| = 7$.",
  uses: ["prop:torus-knot-generators"],
  tags: ["torus-knot", "generator", "genus-bound", "summary-table"],
});
