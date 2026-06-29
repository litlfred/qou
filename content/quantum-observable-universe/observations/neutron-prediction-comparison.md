*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
At $q = q_0$, the beta-stability formula
([beta-stability](#prop:beta-stability))

$$
  p^*(A) =  \frac{A}{2 + c \cdot A^{2/3}},
  \qquad c = \frac{a_C}{2a_A} = 0.01497,
$$

predicts a stable neutron number $n_{\mathrm{pred}}(p)$ for
each proton number $p$.  Comparing with the observed most
stable isotope (AME2020/NUBASE2020) for all $103$ elements:

See [Table](#tbl:neutron-prediction-comparison-table-data).

The mean discrepancy is $\overline{|\Delta n|} = 1.7$ neutrons
across all $103$ elements.  The maximum discrepancy
$|\Delta n| = 8$ occurs at $p = 102$ (nobelium) and $p = 103$
(lawrencium), both transuranic elements with poorly determined
stable isotopes.

**Formal witness.**
The predicted and observed neutron numbers for all $103$
elements are recorded as Lean witness data in
`integer-stability.lean`, with the theorem
`stable_neutron_max_error` asserting $|\Delta n| \leq 8$
for every element.
