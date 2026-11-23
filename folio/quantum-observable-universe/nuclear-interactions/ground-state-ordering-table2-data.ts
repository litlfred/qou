import { table } from "../../schema/builders";
export default table({
  label: "tbl:ground-state-ordering-table2-data",
  title: "Nucleon-ordering ansatz sequences vs. $\\Phi_q$ minimality status",
  caption: "Comparison of legacy sorted and interleaved/tail-packed nucleon-ordering sequences against exhaustive $\\Phi_q$ evaluation (prop:ground-state-ordering): sorted minimises $\\Phi_q$ at $A = 3$, whereas for $A \\geq 4$ the interleaved tail-packed rule fails to minimise $\\Phi_q$ in general and strictly maximises it in counterexamples such as $(A, Z) = (5, 1)$ and $(7, 3)$.",
  uses: ["prop:ground-state-ordering"],
  tags: ["extracted-table", "nucleon-ordering"],
});
