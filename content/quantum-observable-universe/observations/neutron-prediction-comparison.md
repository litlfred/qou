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

**Interpretation.**
The beta-stability formula is the **smooth** (shell-free)
prediction from the stability cubic
([Diophantine valley](#rem:diophantine-valley)).  The
discrepancies $|\Delta n| \geq 2$ concentrate at:

1. **Stability pair closures** ($n = 20, 28, 50, 82, 126$):
   the observed neutron count clusters at these values while
   the smooth formula passes through them.  This accounts for
   the $|\Delta n| = 4$ at calcium ($n_{\mathrm{obs}} = 20$,
   $n_{\mathrm{pred}} = 24$) and barium ($n_{\mathrm{obs}} = 82$,
   $n_{\mathrm{pred}} = 78$).

2. **Transuranic elements** ($p > 92$): the observed isotopes
   are radioactive with half-lives too short for precise
   determination of the "most stable" $n$.

The smooth formula captures the **trend** (neutron excess
growing from $0\%$ to $60\%$) from the single parameter $q$.
The residuals encode the **shell structure** —
the stability pairs — which is the open question of the
[elliptic stability conjecture](#rem:elliptic-stability-locus).

**Formal witness.**
The predicted and observed neutron numbers for all $103$
elements are recorded as Lean witness data in
`integer-stability.lean`, with the theorem
`stable_neutron_max_error` asserting $|\Delta n| \leq 8$
for every element.
