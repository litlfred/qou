**Proposition (per-block character closed forms, antipode pairing,
vanishing at $q = 1$).**
*For all $q > 0$,*

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

*Each block vanishes at $q = 1$ (the classical point), and the
antipode pairing*

$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; q^{-4} \cdot \chi_{(3)}(\Delta_{T_\beta})(q)
$$

*holds for all $q > 0$.*

**Proof.** Each closed form is a definitional rational expression
in $q$; the vanishing at $q = 1$ follows from the $(q^2 - 1)$
factor present in all three; the antipode pairing is the rational
identity $-(q^2-1)(q^2+1)^2/(4q^5) = q^{-4} \cdot [-(q^2-1)(q^2+1)^2/(4q)]$,
which simplifies to $1/q^5 = q^{-4} \cdot 1/q$, true. All three
parts are discharged in Lean by `field_simp; ring` after positivity
witnesses for the denominators ($q > 0$). $\square$

## Scope and discipline notes

This proposition establishes the **per-block source data** that
feeds the Q$_\beta$ precision-ladder derivation. Each per-block
character is an exact rational function of $q$, pre-archimedean,
sorry-free.

**What this proposition does NOT establish.**

- A closed form for $\Delta\tau_M(q) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(q)$.
  Why: the canonical Wenzl–Markov weights $y_\lambda(q)$ from
  `markov_weights_symbolic.solve_y_lambda(3)` involve $\sqrt q$ (via
  the Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$) and are NOT
  rational in $q$. A first version of this file attempted to prove
  a closed form for $\Delta\tau_M$ using an incorrect rational guess
  for $y_\lambda$; that version was retracted. The companion probe
  `qbeta_c3_multiblock_recursion_attack.py` does emit a Δτ_M closed
  form, but using a **non-canonical rational surrogate** for $y_\lambda$
  (clearly marked in the script's docstring and witness JSON) — it is
  a NEAR-MATCH diagnostic, not a derivation. Proving the actual
  $\Delta\tau_M$ identity requires square-root handling beyond the
  `ring` tactic and is open.
- The empirical $c_3 \approx -2$ identity. Per the 1ppQ-Q$_\beta$
  ledger ([`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md)),
  $c_3 = -2$ is settled as a NEAR-MATCH with non-zero cross-anchor
  swing, NOT a Taylor-exact closure.
- The f-map identification. The Habiro element scaling map
  $f : \Delta\tau_M(\sqrt u) \mapsto Q_\beta(c_3 \text{ at } u^3)$
  remains the keystone of the 1ppQ closure.

**Structural insight from the vanishing-at-1 theorem.** All three
blocks have a $(q^2 - 1)$ factor, so each contributes at order $w$
or higher in the Taylor expansion around $q = 1$, where $w = q - 1$.
The per-block ε¹-order coefficients (from the witness's
`taylor_coefficients_per_block_ε_order` field) are
$\{(3): -2, (2,1): -1, (1,1,1): -2\}$. The shared $-2$ at order $w$
between the $(3)$ and $(1,1,1)$ blocks is the algebraic signature
of the antipode pairing — under $q \mapsto 1/q$, the order-$w$
expansion picks up the same leading coefficient up to the $q^{-4}$
framing weight.

## Cross-references

- The probe computation:
  [`folio-assistant/computations/qbeta/qbeta_c3_multiblock_recursion_attack.py`](../../../folio-assistant/computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
  (witness `qbeta-c3-multiblock-recursion-attack.witness.json`).
- The pre-archimedean recursion for $z$: 
  [`folio-assistant/computations/qbeta/qbeta_prearchimedean_z_recursion.py`](../../../folio-assistant/computations/qbeta/qbeta_prearchimedean_z_recursion.py).
- The downstream c$_k$ conjectures:
  [`conj:qbeta-c-k-closed-forms`](#conj:qbeta-c-k-closed-forms)
  (axiomatised; conditional on the Habiro element identification).
- The 1ppQ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
