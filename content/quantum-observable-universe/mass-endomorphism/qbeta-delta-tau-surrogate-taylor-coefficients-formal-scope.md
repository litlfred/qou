## Formal scope

**What is established:**

- The named function `delta_tau_M_surrogate_taylor_witness : ℕ → ℚ`
  in Lean returning the witness-recorded coefficient at each order.
- Sorry-free reflexivity-level theorems
  `delta_tau_M_surrogate_taylor_witness_0 = 0` and
  `delta_tau_M_surrogate_taylor_witness_1 = -5/6` matching the
  formally-proved Lean theorems on the exact derivative-at-1.

**What is deferred:**

- Sorry-free $n$-th derivative theorems for orders 2..7. Each requires a quotient-rule chain $n+1$ levels deep. These remain stated as Lean theorems with
  `sorry` and `-- Ref:` citations to the witness JSON.
- A closed-form recursion for the $c_n$. The underlying rational
  function forms a degree-11/degree-7 quotient, so a finite-order
  linear recursion on $c_n$ exists, but extracting it remains open.
