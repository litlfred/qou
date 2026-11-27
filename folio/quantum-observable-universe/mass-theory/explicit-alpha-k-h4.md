*For each $\lambda \,\vdash\, 4$, the Wedderburn-orthogonal representative $r_\lambda = \sum_C c_C \cdot T_{w_C}$ has coefficients $c_C(\lambda) \in \mathbb{Q}(q)$ defined as:*

| $\lambda$ | $c_e$ | $c_{(12)}$ | $c_{(12)(34)}$ | $c_{(123)}$ | $c_{(1234)}$ |
|--|--|--|--|--|--|
| $(4)$ | $\dfrac{1}{q^3 \Phi_{(4)}}$ | $\dfrac{q^4 + 2q^2 + 3}{q^2 \Phi_{(4)}}$ | $\dfrac{1}{q(q^2+1)}$ | $\dfrac{q^4 + q^2 + 2}{q (q^4 + q^2 + 1)}$ | $1$ |
| $(3,1)$ | $-\dfrac{1}{q(q^2+1)}$ | $\dfrac{1 - 2q^2 - q^4}{q^2 (q^2+1)}$ | $\dfrac{1}{q(q^2+1)}$ | $\dfrac{1 - q^2}{q}$ | $1$ |
| $(2,2)$ | $-\dfrac{q^2}{(q^2+1)^2}$ | $\dfrac{q(1-q^2)}{(q^2+1)^2}$ | $-\dfrac{q^4 + q^2 + 1}{(q^2+1)^2}$ | $1$ | $0$ |
| $(2,1,1)$ | $\dfrac{q^3}{q^2+1}$ | $\dfrac{q^4 - 2q^2 - 1}{q^2+1}$ | $-\dfrac{q^3}{q^2+1}$ | $\dfrac{1 - q^2}{q}$ | $1$ |
| $(1^4)$ | $-\dfrac{q^9}{\Phi_{(4)}}$ | $\dfrac{q^4(3q^4 + 2q^2 + 1)}{\Phi_{(4)}}$ | $-\dfrac{q^3}{q^2+1}$ | $\dfrac{q(-2q^4 - q^2 - 1)}{q^4 + q^2 + 1}$ | $1$ |

*where $\Phi_{(4)} = q^6 + 2q^4 + 2q^2 + 1$.*

*The table is a dual basis to the characters: $\chi_\mu(r_\lambda) = \delta_{\lambda\mu}\,\kappa_\lambda$, where each $\kappa_\lambda$ factors through $q$, $q^2+1$, $q^4+1$ and $q^4+q^2+1$ only, so $\kappa_\lambda \neq 0$ at generic $q$. For any trace $\mathrm{tr} = \sum_\mu y_\mu \chi_\mu$ this gives $\mathrm{tr}(r_\lambda) = y_\lambda \kappa_\lambda$.*

The characters $\chi_\mu$ are the characters of five explicit representations of $H_4$ with entries in $\mathbb{Z}[q^2]$: trivial, sign, the reflection representation $(3,1)$, its twist $T \mapsto (Q-1) - T$ for $(2,1,1)$, and the $H_3$ reflection representation pulled back along $T_1, T_2, T_3 \mapsto T_1, T_2, T_1$ for $(2,2)$. The Lean sibling checks the Hecke and braid relations for each of them and recomputes every entry of the character table. The statement holds over a generic commutative ring.
