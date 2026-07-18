**Catalogue (Taylor coefficients of the surrogate $\Delta\mathrm{tr}_M$).**
*The Taylor coefficients $c_n$ of*
[`delta_tau_M_surrogate`](qbeta-per-block-chi-closed-forms.md)
*expanded around the classical point $q = 1$ in the variable
$w = q - 1$, to order 7, are read off the closed form*

$$
  \Delta\mathrm{tr}_M^{\text{surr}}(q) = \frac{-q^{11} + q^{10} - 2q^9 + q^8 + q^6 - q^5 - q^3 + 2q^2 - q + 1}{4 q^5 (q^2 + q + 1)}
$$

*by substituting $q = 1 + w$ and extracting the coefficient of $w^n$:*

| Order $n$ | Coefficient $c_n$ | Status in Lean |
|---|---|---|
| 0 | $0$ | proved sorry-free (`delta_tau_M_surrogate_vanish_at_one`) |
| 1 | $-5/6$ | proved sorry-free (`delta_tau_M_surrogate_hasDerivAt_one`) |
| 2 | $5/6$ | catalogued from witness; formal proof deferred |
| 3 | $-41/9$ | catalogued from witness; formal proof deferred |
| 4 | $149/18$ | catalogued from witness; formal proof deferred |
| 5 | $-1729/108$ | catalogued from witness; formal proof deferred |
| 6 | $111/4$ | catalogued from witness; formal proof deferred |
| 7 | $-3665/81$ | catalogued from witness; formal proof deferred |

The witness records both the closed form and per-order coefficients;
orders 0 and 1 are independently verified by the sorry-free Lean
theorems named in the table.

## Cross-references

- Parent block:
  [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
  (`delta_tau_M_surrogate` definition + order-0/order-1 proofs).
- Witness JSON:
  [`qbeta-c3-multiblock-recursion-attack.witness.json`](../../../computations/qbeta/qbeta-c3-multiblock-recursion-attack.witness.json).
- 1ppQ-Q$_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
