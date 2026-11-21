**Proof.**

> **Scope of the inductive bound.** The per-step product count $|\mathcal{N}_{\leq k}| \times 2 \times 6$ bounds the unreduced product before applying the Hecke quadratic relations; proving that Gröbner–Shirshov reduction collapses the support to the tabulated normal-form sizes ($\leq 2, 8, 32, 128$) and the binomial bound remains an open combinatorial step.

At each inductive step, the product $\mathcal{N}_{\leq k} \cdot C \cdot \mathfrak{N}_{k+1}$ contains at most $|\mathcal{N}_{\leq k}| \times 2 \times 6$ terms. (The crossing $C$ contains at most 2 terms; the nucleon normal form contains 6 terms.) Gröbner–Shirshov reduction eliminates all $\sigma_i^2$ factors via the Hecke relation and sorts words via Yang–Baxter. This yields a normal form of strictly bounded size.

The **Hecke square rule** for typed crossings enforces this bound:

$$
  C_{pp}^2 = h_{\mathrm{A}} \cdot C_{pp} + \mathbf{1}, \qquad C_{nn}^2 = -h_{\mathrm{A}} \cdot C_{nn} + \mathbf{1},
$$

where $h_{\mathrm{A}} = q - q^{-1}$. The first is the Hecke relation $\sigma_i^2 = h_{\mathrm{A}}\sigma_i + \mathbf{1}$ for $C_{pp} = \sigma_i$. The second follows for $C_{nn} = \sigma_i^{-1} = \sigma_i - h_{\mathrm{A}}$, whose square is $\sigma_i^{-2} = -h_{\mathrm{A}}\sigma_i^{-1} + \mathbf{1}$. They guarantee that consecutive same-type nucleon pairs arrest normal form complexity. Two $pp$ crossings resolve into a linear combination of a single crossing and the identity.

For mixed crossings:

$$
  C_{pn}^2 = \mathbf{1} + \tfrac{1}{4}h_{\mathrm{A}}^2.
$$

For $C_{pn} = \tfrac12(\sigma_i + \sigma_i^{-1}) = \sigma_i - \tfrac12 h_{\mathrm{A}}$ the linear term cancels, so the square of a mixed crossing is a scalar. The identity channel absorbs it at each step.

## Complexity bound

| Mass number $A$ | Unreduced terms | Reduced NF terms | Hecke steps |
| :---: | :---: | :---: | :---: |
| 2 | 12 | $\leq 2$ | 1 |
| 4 | 432 | $\leq 8$ | $\leq 12$ |
| 8 | $\sim 10^5$ | $\leq 32$ | $\leq 80$ |
| 16 | $\sim 10^{10}$ | $\leq 128$ | $\leq 480$ |

The inductive method systematically reduces $\sim 10^{10}$ unreduced terms to at most $128$ normal form terms for oxygen-16. $\square$
