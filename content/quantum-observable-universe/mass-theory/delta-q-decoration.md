**Definition (q-dimension decoration of the NF basis).**
*Let $H_n(q)$ be the Iwahori–Hecke algebra over
$R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, with normal-form
basis $\{b_w\}_{w \in S_n}$ indexed by reduced expressions of
permutations $w \in S_n$.  The
**$\delta_q$-decoration** is the map*

$$
  \delta_q : H_n(q) \;\longrightarrow\; R^{|\,\mathrm{Par}(n)\,|}
$$

*— the **:defterm[$\delta_q$-decoration]{#delta-q-decoration}** —
sending an algebra element $b \in H_n(q)$ to the tuple of its
$q$-characters in each irreducible representation
$V_\lambda$ (for $\lambda \vdash n$):*

$$
  \delta_q(b)
  \;:=\;
  \bigl(\chi_\lambda(b)\bigr)_{\lambda \vdash n}
  \;\in\;
  R^{|\,\mathrm{Par}(n)\,|},
$$

*where $\chi_\lambda(b) = \mathrm{tr}_{V_\lambda}(\rho_\lambda(b))$
is the trace of $b$ acting in the seminormal-basis representation
$\rho_\lambda : H_n(q) \to \mathrm{End}(V_\lambda)$.*

### Why the :defterm[q-dimension layer]{#q-dimension-layer} matters

The Markov trace $\mathrm{tr}_M : H_n(q) \to R$ is the
characteristic invariant used in operator-selection LP
([`prop:operator-selection-lp`](#prop:operator-selection-lp))
and in the Φ$_q$ tower. It corresponds to a single weighted sum
over irreps:

$$
  \mathrm{tr}_M(b) \;=\; \sum_{\lambda \vdash n}
  w_\lambda \cdot \frac{\chi_\lambda(b)}{f^\lambda},
$$

where $w_\lambda = \dim_q(V_\lambda)^2 / [n]_q!$ and
$f^\lambda = \dim V_\lambda$ is the classical irrep dimension
(number of standard Young tableaux of shape $\lambda$).

The $\delta_q$-decoration **preserves the per-irrep structure**
that the Markov trace collapses by summing.  This refinement is
necessary to identify how $\alpha_{EM}$ — which lives in the
q-dimension layer
([`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation),
round 11) — projects onto specific Wedderburn components of
the molecular bound-state operator
([`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)).

### Wedderburn structure

Recall the Wedderburn decomposition for semisimple $H_n(q)$:

$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n}
  \mathrm{End}(V_\lambda).
$$

Under this isomorphism, $\delta_q(b)$ records exactly the per-block
trace:

$$
  \delta_q(b)_\lambda \;=\; \mathrm{tr}_{V_\lambda}\bigl(\rho_\lambda(b)\bigr).
$$

The **Markov trace contribution from each block** is then

$$
  \mathrm{tr}_M^\lambda(b)
  \;=\;
  \frac{w_\lambda}{f^\lambda}\,\delta_q(b)_\lambda.
$$

Summing over $\lambda$ recovers the standard Markov trace.

### Computation

A reusable Python implementation is available in
[`computations/delta_q_decoration.py`](computations/delta_q_decoration.py),
using the seminormal Hoefsmit representation matrices from
[`hecke_characters.py`](computations/hecke/hecke_characters.py).
The witness data
[`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json)
caches the per-irrep characters for $H_2, H_3, H_4$ NF bases and
the force-carrier knots $T_{2,9}, T_{3,5}$.

**Computational complexity.** For partition $\lambda \vdash n$
with $f^\lambda$ standard Young tableaux, $\rho_\lambda(\sigma_i)$
is an $f^\lambda \times f^\lambda$ matrix.  Computing
$\delta_q(\beta)$ for a braid $\beta$ of length $\ell$ costs
$O(\ell \cdot \sum_\lambda (f^\lambda)^3)$ in matrix
multiplications.  For $n = 4$:
$\sum_\lambda (f^\lambda)^3 = 1 + 27 + 8 + 27 + 1 = 64$.

### Force-carrier examples

For the Bring force-carrier torus knots
([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness))
the $\delta_q$-decoration produces the q-dimensions appearing in
the bare formula
$1/\alpha_{EM} = q\,[9]_q\,[10]_q$
([`prop:em-coupling-projection`](#prop:em-coupling-projection)):

$$
  \delta_q(T_{2,9})
  \;=\;
  q^{9} - q^{-9}
  \;=\;
  h\,[9]_q,
$$

(in the $H_2(q)$ representation, summed over the two irreps
$V_{(2)}, V_{(1,1)}$ with eigenvalues $q^9, -q^{-9}$ respectively).

The companion identity
([`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio))
expresses $\alpha_{EM}$ as a categorical-trace ratio:

$$
  \alpha_{EM}
  \;=\;
  \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}.
$$

### Reusability

The $\delta_q$-decoration is the **single new infrastructure layer**
identified in
[`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation)
round 11 as the missing piece for fully categorical derivation of
the Hartree energy.  It is reusable across:

- Operator-selection LP (refines the Markov-trace cost into
  per-irrep contributions, useful for symbolic-$q$ analysis of LP
  optima).
- Bound-state projection analysis (rounds 17–18 of the
  $E_h$ investigation: identifies which irrep channels carry
  force-carrier content via the
  [`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)).
- Cache-and-reuse for downstream binding-energy computations
  (the witness JSON enables $O(1)$ lookup of per-irrep characters
  rather than re-multiplying matrices).
