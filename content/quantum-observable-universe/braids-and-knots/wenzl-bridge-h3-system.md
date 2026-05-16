**Wenzl-bridge $y_\lambda$ system for $H_3(q)$** as a $3 \times 3$ linear
algebra problem (Lean infrastructure).

The Markov-trace decomposition on $H_3(q)$ is

$$
  \tau_M(x) \;=\; y_{(3)} \chi_{(3)}(x) + y_{(2,1)} \chi_{(2,1)}(x) + y_{(1,1,1)} \chi_{(1,1,1)}(x) .
$$

Applying the Markov axioms M1 and M3 (from [`rem:markov-axioms-primitive`](#rem:markov-axioms-primitive))
on the test elements $\{1, \sigma_1, \sigma_1 \sigma_2\}$ gives a $3 \times 3$
linear system:

$$
  \underbrace{
    \begin{pmatrix} 1 & 2 & 1 \\ q & q - q^{-1} & -q^{-1} \\ q^2 & (q-q^{-1})^2 - 1 & q^{-2} \end{pmatrix}
  }_{A(q)}
  \cdot
  \begin{pmatrix} y_{(3)} \\ y_{(2,1)} \\ y_{(1,1,1)} \end{pmatrix}
  \;=\;
  \begin{pmatrix} 1 \\ z \\ z^2 \end{pmatrix}
$$

with $z = 1/(\sqrt q + 1/\sqrt q)$ the Markov-Jones parameter.

## Lean formalization

The companion file [`wenzl-bridge-h3-system.lean`](wenzl-bridge-h3-system.lean):

1. Defines `wenzlMatrix : Matrix (Fin 3) (Fin 3) ℝ` with the explicit
   character-table entries from Hoefsmit/Wenzl.
2. Proves `wenzlMatrix_explicit` — pinning down all 9 matrix entries.
3. States `wenzl_matrix_det_nonzero_at_q_zero_one_excluded` — the
   non-singularity condition.
4. States `wenzl_bridge_solution_exists` — existence and uniqueness via
   Cramer's rule.

## Open Lean steps

The current stub has TWO `sorry`s for the technically-tedious-but-
mechanical determinant evaluation:

- `wenzl_matrix_det_nonzero_at_q_zero_one_excluded`: the determinant of
  the explicit 3×3 matrix evaluates (via `Matrix.det_fin_three`) to a
  rational expression in $q$. Showing it's non-zero for $q \neq 0, \pm 1$
  requires `field_simp + ring + linarith` on the explicit form.
- `wenzl_bridge_solution_exists`: follows from `Matrix.mul_vec_eq_iff_unique`
  (or similar Mathlib API) given the non-vanishing determinant.

Both are mechanical Lean-engineering steps; the underlying mathematical
content is settled (Cramer's rule for non-singular 3×3 systems).

## Status

Lean stub: **2 sorries** — both are mechanical-but-tedious closures
deferred to follow-up Lean-engineering work. The mathematical content
is established (Wenzl 1988); the formalisation is at the "Mathlib
linear-algebra completion" stage.

This stub provides the **infrastructure** to plug into downstream
theorems requiring the explicit Wenzl-bridge solution; it doesn't
itself close them.
