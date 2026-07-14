**Proposition (conditional on [`conj:tower-geometric-lower-bound`](tower-geometric-lower-bound.md)).**
*Assume the geometric tower lower bound $c\,r^{k} \leq w(k)$ with $r > 1$, $c > 0$. If the binding is extensive — $w(A) \leq M \cdot A$ for every $A \geq 1$ — then a contradiction follows. Consequently no **linear** level-selection rule $k(A) = A$ (nor bond-count $k(A) = A(A-1)/2$, a fortiori) is consistent with extensive binding: the selected jet level grows at most **logarithmically** in $A$.*

**Proof idea.** The tower bound gives $c\,r^{A} \leq w(A) \leq M\cdot A$ for all $A \geq 1$. But a geometric $c\,r^{A}$ with $r > 1$ eventually outgrows any linear $M\cdot A$ — formally $(A) = o(r^{A})$ as $A \to \infty$ — so the inequality cannot hold for all $A$. Dividing the surviving bound by $c$ and taking $\log_r$ shows $k(A) \leq \log_r\!\big((M/c)\,A\big)$, i.e. at most logarithmic growth.

**Why the hypothesis is restricted to $A \geq 1$.** Extensivity is imposed only for $A \geq 1$, the physical regime. The $A = 0$ case is a boundary artifact — the tower bound forces $w(0) \geq c > 0$ while $M \cdot 0 = 0$, an immediate contradiction that has nothing to do with the exponential-versus-linear mechanism. Excluding it ensures the exclusion is the genuine growth argument rather than a degenerate boundary coincidence.

## Lean structure

[`QOU.Mass.LevelSelection.no_linear_selection`](../lean/QOU/Mass/LevelSelectionLogarithmic.lean) proves the contradiction outright, **sorry-free**, taking the tower bound as the class hypothesis `[TowerGeometricLowerBound w r c]` (§3b-cond). The exponential-beats-linear step is Mathlib's `isLittleO_coe_const_pow_of_one_lt` ($(A:\mathbb{R}) = o[\mathrm{atTop}]\, r^{A}$); `#print axioms` reports only `propext / Classical.choice / Quot.sound`. The companion inequality `linear_selection_bound` ($c\,r^{A} \leq M\cdot A$) is the un-contradicted form; this proposition is the exclusion it entails.
