**Proposition.**
*Let $w = w_{\mathrm{std}}$ be the branched brane-tower weight, which by [Brane-tower growth above the containment threshold (GAP-A-3)](tower-geometric-lower-bound.md) satisfies $c\,r^{k} \leq w(k)$ for $k \geq 3$ with $r = \sqrt{2} > 1$ and $c = 1/30 > 0$. If the binding is extensive — $w(A) \leq M \cdot A$ for every $A \geq 1$ — then a contradiction follows. Consequently no **linear** level-selection rule $k(A) = A$ (nor bond-count $k(A) = A(A-1)/2$, a fortiori) is consistent with extensive binding: the selected jet level grows at most **logarithmically** in $A$.*

**Proof idea.** The tower bound gives $c\,r^{A} \leq w(A) \leq M\cdot A$ for all $A \geq 1$. But a geometric $c\,r^{A}$ with $r > 1$ eventually outgrows any linear $M\cdot A$ — formally $(A) = o(r^{A})$ as $A \to \infty$ — so the inequality cannot hold for all $A$. Dividing the surviving bound by $c$ and taking $\log_r$ shows $k(A) \leq \log_r\!\big((M/c)\,A\big)$, i.e. at most logarithmic growth.

**Restriction of the hypothesis to $A \geq 1$.** Extensivity is imposed only for $A \geq 1$, the physical regime. Excluding $A = 0$ ensures the exclusion is the genuine growth argument rather than a degenerate boundary coincidence: at $A = 0$ the linear side is $M \cdot 0 = 0$, so the inequality would fail or hold for reasons unrelated to the exponential-versus-linear mechanism.

The tower bound does not force $w(0) \geq c > 0$: $w_{\mathrm{std}}(0) = 0$, because no diagram of fewer than three cells contains $(2,1)$. Stated for every $k$, the growth hypothesis would be false at $k = 0$, so the $A = 0$ case is a falsity in the antecedent rather than a boundary effect in the conclusion. That is why [Brane-tower growth above the containment threshold (GAP-A-3)](tower-geometric-lower-bound.md) now carries a threshold, and why this proposition is unconditional rather than conditional.

## Status

The contradiction is proved outright from the tower-geometric lower bound, by the step "an exponential $r^A$ with $r > 1$ dominates any linear function of $A$" ($A = o(r^{A})$ as $A \to \infty$). The companion inequality $c\,r^{A} \leq M\cdot A$ is the un-contradicted form; this proposition is the exclusion it entails.

**The hypothesis is discharged, so the exclusion is not conditional.** The tower-geometric lower bound holds for the actual weight $w_{\mathrm{std}}$ at threshold $k_{0} = 3$, so the exclusion applies to $w_{\mathrm{std}}$ itself, as does its bond-count companion excluding superlinear selection. Before that bound was established neither exclusion applied to any concrete weight. The threshold costs the argument nothing, because both proofs choose $A$ arbitrarily large.
