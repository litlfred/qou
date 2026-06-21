*Lean sibling: a field $R$ carrying the $q$-data (AGENTS.md §7c); the identity is purely algebraic, pre-archimedean.*

**Proposition (q-dimension decoration of the basis knots).** *For the basis
torus knot $T_{2,k}$, the q-dimension decoration factors as the Hecke
deformation $h$ times the quantum integer $[k]_q$:*

$$
  \delta_q(T_{2,k}) \;:=\; q^{k} - q^{-k}
  \;=\; h\,[k]_q,
  \qquad
  h = q - q^{-1},\quad [k]_q = \frac{q^{k} - q^{-k}}{q - q^{-1}},
$$

*an exact identity in the substrate ring $R = \mathbb{Z}[q^{\pm 1/2}, h^{-1}]$ —
**pre-archimedean, no $\pi$** — needing only $q - q^{-1} \neq 0$ for the
division. Lean `deltaQ_eq_h_qbracket`, sorry-free.*

This is the q-data building block of the **$\alpha_{\text{basis-knot}}$ coupling
family**: the fine-structure constant is
[`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
$\alpha_{EM} = h^2/\bigl(q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})\bigr)$, the
antisymmetric $e_-$ (sinh) coupling of the Hopf 2-strand operation, with
$\alpha_{EM} := \alpha_{T_{2,3}}$. Each $\delta_q(T_{2,k})$ above is one such
$h\,[k]_q$ factor. Symbolic cross-check (basis-knot exponents $\{3,5,7,9,10\}$,
all exact):
[`delta_q_h_bracket_identity.py`](../../computations/delta_q_h_bracket_identity.py).
