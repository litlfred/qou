**Catalogue (Taylor coefficients of the surrogate $\Delta\tau_M$).**
*The Taylor coefficients $c_n$ of*
[`delta_tau_M_surrogate`](qbeta-per-block-chi-closed-forms.md)
*expanded around the classical point $q = 1$ in the variable
$w = q - 1$, to order 7:*

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

*Source: SymPy computation in
[`qbeta_c3_multiblock_recursion_attack.py`](../../../computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
(Step 2: Taylor expansion to 12 orders), serialised in
[`qbeta-c3-multiblock-recursion-attack.witness.json`](../../../computations/qbeta/qbeta-c3-multiblock-recursion-attack.witness.json)
under `taylor_coeffs_w_expansion`.*

## Honest scope

**This block establishes:**

- The named function `delta_tau_M_surrogate_taylor_witness : ℕ → ℚ`
  in Lean returning the witness-recorded coefficient at each order.
- Sorry-free reflexivity-level theorems
  `delta_tau_M_surrogate_taylor_witness_0 = 0` and
  `delta_tau_M_surrogate_taylor_witness_1 = -5/6` matching the
  formally-proved Lean theorems on the actual derivative-at-1.

**This block does NOT establish:**

- Sorry-free $n$-th derivative theorems for orders 2..7. Each would
  require a quotient-rule chain $n+1$ levels deep — mechanical but
  bulky (~30-50 Lean lines per order). Stated as Lean theorems with
  `sorry` and `-- Ref:` citations to the witness JSON.
- A closed-form recursion for the $c_n$ (the underlying rational
  function is a degree-11/degree-7 quotient, so a finite-order
  linear recursion on $c_n$ exists, but extracting it is open work).

**Why the witness values are reliable.** The SymPy script in
[`qbeta_c3_multiblock_recursion_attack.py`](../../../computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
applies `sp.series(... w, 0, 12)` to the closed form

$$
  \Delta\tau_M^{\text{surr}}(q) = \frac{-q^{11} + q^{10} - 2q^9 + q^8 + q^6 - q^5 - q^3 + 2q^2 - q + 1}{4 q^5 (q^2 + q + 1)}
$$

substituting $q = 1 + w$ and extracting coefficients of $w^n$. The
witness records both the closed form and per-order coefficients;
order-0 and order-1 are independently verified by the sorry-free
Lean theorems above (orders 0 and 1).

## Cross-references

- Parent block:
  [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
  (`delta_tau_M_surrogate` definition + order-0/order-1 proofs).
- Witness JSON:
  [`qbeta-c3-multiblock-recursion-attack.witness.json`](../../../computations/qbeta/qbeta-c3-multiblock-recursion-attack.witness.json).
- 1ppQ-Q$_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
