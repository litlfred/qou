<!-- FILE_START: qbeta-per-block-delta-tau-intro.md -->
The previous section evaluated the Markov trace block by block. We now read these characters through the $T_\beta$ endomorphism. 

The per-block characters $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$ are written in closed form and vanish at the classical point $q = 1$ ([`prop:qbeta-per-block-chi-closed-forms`](#prop:qbeta-per-block-chi-closed-forms)). Once the Markov weights take their canonical values, this vanishing forces the trace difference $\Delta\tau_M$ to carry an explicit $(q^2-1)$ factor ([`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor`](#prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor)). This is a conditional statement formalised via a class hypothesis (§3b-cond), which we inhabit with an explicit $\sqrt{q}$-bearing instance ([`prop:qbeta-canonical-markov-weights-explicit-instance`](#prop:qbeta-canonical-markov-weights-explicit-instance)).

The low-order Taylor data of the surrogate $\Delta\tau_M$ ([`prop:qbeta-delta-tau-surrogate-taylor-coefficients`](#prop:qbeta-delta-tau-surrogate-taylor-coefficients)) provides the exact per-block input required by the downstream decay-side $c_k$ recursion. In contrast, the downstream extraction itself relies on calibration anchoring.
<!-- FILE_END: qbeta-per-block-delta-tau-intro.md -->

<!-- FILE_START: qbeta-per-block-chi-closed-forms.md -->
# Per-block character closed forms and antipode pairing

For all $q > 0$, the per-block characters over $H_3(q)$ take the exact rational forms:

$$
  \chi_{(3)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q},
$$
$$
  \chi_{(2,1)}(\Delta_{T_\beta})(q)
  \;=\; \frac{(q^2 - 1)(-q^4 - 1)}{4q^3},
$$
$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q^5}.
$$

Each block vanishes at the classical point $q = 1$. The antipode pairing relates the sign and trivial representations for all $q > 0$:

$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; q^{-4} \chi_{(3)}(\Delta_{T_\beta})(q).
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, physical observables, and numerical evaluation at the substrate parameter $q_0$. Generic categorical or $q$-deformation identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: qbeta-per-block-chi-closed-forms.md -->

<!-- FILE_START: qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md -->
# Canonical $(q^2 - 1)$ factor of the Markov trace difference

Assume a concrete instance of the canonical Wenzl–Markov weights class `CanonicalMarkovWeightsH3` exists. This instance supplies weights $y_{(3)}(q)$, $y_{(2,1)}(q)$, and $y_{(1,1,1)}(q)$ satisfying the dimension-normalisation axiom $y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q) = 1$ for $q > 0$. 

Define the canonical trace difference $\Delta\tau_M^{\text{can}}(q)$ as the weighted sum:

$$
  \Delta\tau_M^{\text{can}}(q) =
  y_{(3)}(q) \chi_{(3)}(q)
  + y_{(2,1)}(q) \chi_{(2,1)}(q)
  + y_{(1,1,1)}(q) \chi_{(1,1,1)}(q).
$$

Then for $q > 0$, the trace difference factors as:

$$
  \Delta\tau_M^{\text{can}}(q) = (q^2 - 1) P^{\text{can}}(q),
$$

where

$$
  P^{\text{can}}(q) = y_{(3)}(q) P_{(3)}(q) + y_{(2,1)}(q) P_{(2,1)}(q) + y_{(1,1,1)}(q) P_{(1,1,1)}(q).
$$

Here $P_\lambda(q)$ are the per-block witnesses from `chi_blocks_have_q2_minus_1_factor`. In particular, $\Delta\tau_M^{\text{can}}(1) = 0$.

## Cross-references

- Parent block: [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md) (establishes the per-block $\chi_\lambda$ closed forms and the `CanonicalMarkovWeightsH3` class).
- Sibling on main: [`prop:q-beta-over-e0-classical-vanishing`](../mass-theory/q-beta-over-e0-classical-vanishing.md) (shows the classical-point vanishing of the upstream object $S(q) = \mathfrak{Q}_\beta/E_0$).
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, physical observables, and numerical evaluation at the substrate parameter $q_0$. Generic categorical or $q$-deformation identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md -->

<!-- FILE_START: qbeta-delta-tau-surrogate-taylor-coefficients.md -->
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
<!-- FILE_END: qbeta-delta-tau-surrogate-taylor-coefficients.md -->

<!-- FILE_START: qbeta-canonical-markov-weights-explicit-instance.md -->
# Explicit instance of canonical Markov weights

The Lean class `CanonicalMarkovWeightsH3` (declared in [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md) §Extension #4) is inhabited. We construct an explicit $\sqrt q$-bearing instance:

$$
  y_{(3)}(q) = z(q), \qquad
  y_{(2,1)}(q) = \tfrac{1}{2} - z(q), \qquad
  y_{(1,1,1)}(q) = z(q),
$$

where $z(q) = \sqrt q / (1 + q)$ is the Markov parameter.

## Cross-references

- Class declaration: [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md) §Extension #4.
- Conditional theorems consuming this class: [`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor`](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md).
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
<!-- FILE_END: qbeta-canonical-markov-weights-explicit-instance.md -->

