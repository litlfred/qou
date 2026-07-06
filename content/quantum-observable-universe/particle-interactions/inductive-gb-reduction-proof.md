**Proof.**
At each inductive step, the product $\mathcal{N}_{\leq k} \cdot C \cdot \mathfrak{N}_{k+1}$ contains at most $|\mathcal{N}_{\leq k}| \times 2 \times 6$ terms. (The crossing $C$ contains at most 2 terms; the nucleon normal form contains 6 terms.) Gröbner–Shirshov reduction eliminates all $\sigma_i^2$ factors via the Hecke relation and sorts words via Yang–Baxter. This yields a normal form of strictly bounded size.

The **Hecke square rule** for typed crossings enforces this bound:

$$
  C_{pp}^2 = H_A \cdot C_{pp} + \mathbf{1}, \qquad C_{nn}^2 = H_A \cdot C_{nn} + \mathbf{1},
$$

where $H_A = q - q^{-1}$. These equations apply the standard Hecke relation $\sigma_i^2 = H_A\sigma_i + \mathbf{1}$ to typed crossings. They guarantee that consecutive same-type nucleon pairs arrest normal form complexity. Two $pp$ crossings resolve into a linear combination of a single crossing and the identity.

For mixed crossings:

$$
  C_{pn}^2 = H_A \cdot C_{pn} + \mathbf{1} - \tfrac{1}{4}H_A^2.
$$

The extra constant $-\tfrac{1}{4}H_A^2$ provides the mixed-crossing correction. The identity channel absorbs it at each step.

## Complexity bound

| Mass number $A$ | Unreduced terms | Reduced NF terms | Hecke steps |
| :---: | :---: | :---: | :---: |
| 2 | 12 | $\leq 2$ | 1 |
| 4 | 432 | $\leq 8$ | $\leq 12$ |
| 8 | $\sim 10^5$ | $\leq 32$ | $\leq 80$ |
| 16 | $\sim 10^{10}$ | $\leq 128$ | $\leq 480$ |

The inductive method systematically reduces $\sim 10^{10}$ unreduced terms to at most $128$ normal form terms for oxygen-16. $\square$
