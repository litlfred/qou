**Proposition.**
At $q = q_0$, the beta-stability formula
([beta-stability](#prop:beta-stability))

$$
  p^*(A) =  \frac{A}{2 + c \cdot A^{2/3}},
  \qquad c = \frac{a_C}{2a_A} = 0.01497,
$$

predicts a stable neutron number $n_{\mathrm{pred}}(p)$ for each proton
number $p$. We compare this prediction against the observed most stable
isotope (AME2020/NUBASE2020) across all 103 elements:

See [Table](#tbl:neutron-prediction-comparison-table-data).

The mean discrepancy is $\overline{|\Delta n|} = 1.7$ neutrons across all
103 elements. The maximum discrepancy $|\Delta n| = 8$ occurs at $p = 102$
(nobelium) and $p = 103$ (lawrencium). Both are transuranic elements whose
most stable isotopes are poorly determined.

**Formal witness.**
The predicted and observed neutron numbers for all 103 elements reside in
the Lean witness data `integer-stability.lean`. The theorem
`stable_neutron_max_error` formally verifies that $|\Delta n| \leq 8$
for every element.
