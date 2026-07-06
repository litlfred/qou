The jet-tower mass formula
([rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower))
contains a "pentagon ascension" argument that non-rigorously invokes the
quantum-dilogarithm pentagon identity
$\Phi_q(v)\,\Phi_q(u) = \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v)$ —
which **as an operator identity requires
$uv = q\,vu$**. The audit
[`derivation-audit-.md` line 113](../../../docs/audits/derivation-audit-.md)
flagged this as "expected but unwritten" for traced volumes
$\hat V$ at generic jet level. This block closes the gap by
giving the precise algebraic statement and a one-paragraph proof.

The headline: **the traced volumes commute.** The pentagon
ascension argument is therefore **not load-bearing on the
operator pentagon identity**; the same conclusion (singletons

* pairs + jet ascension) follows from Markov-trace factorization
  without any q-commutation input.

## Statement

Let $\hat V_i(q) \in \mathbb{Z}[q^{\pm 1/2}, z]$ be the traced
volume of the $i$-th crossing of a closed braid, defined by

$$
  \hat V_i(q) \;=\; z(q)\,a_i(q) + b_i(q),
\qquad
  z(q) \;=\; \frac{1}{q^{1/2} + q^{-1/2}},
$$

with $a_i, b_i \in \mathbb{Z}[q^{\pm 1/2}]$ determined by the
braid word and the Hecke normal form
([def:algebraic-quantum-volume](#def:algebraic-quantum-volume)).

**Lemma (pair commutation at traced-volume level).**
*For any two indices $i, j$ — adjacent or non-adjacent —*

$$
  \hat V_i(q) \cdot \hat V_j(q)
  \;=\;
  \hat V_j(q) \cdot \hat V_i(q)
  \qquad
  \text{in } \mathbb{Z}[q^{\pm 1/2}, z].
$$

*Equivalently,*

$$
  \mathrm{tr}_M\!\bigl(\hat V_i \hat V_j\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\hat V_j \hat V_i\bigr)
  \;=\; z^2.
$$

*The pentagon q-factor* $q$ *appearing in the prerequisite
$uv = q\,vu$ does **not** apply to scalar traced volumes; it
applies only to operator-valued lifts of $\hat V_i$ in some
non-commutative quantization of the brane tower (see "Operator
lift" below).*
