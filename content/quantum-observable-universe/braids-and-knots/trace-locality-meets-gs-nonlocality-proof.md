*Proof.*

**(1) Markov locality.** Part (1) of the proposition is the
definition of the Markov trace. By
[Jones–Markov trace](#thm:jones-markov-trace), the unique
$R$-linear trace
$\mathrm{tr}_M \colon \bigcup_n H_n(R, q) \to R\otimes\mathbb{Q}$
satisfying normalisation $\mathrm{tr}_M(1) = 1$, the trace property
$\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$, and the Markov property
$\mathrm{tr}_M(x \sigma_n) = z\, \mathrm{tr}_M(x)$
for all $x \in H_n(R, q)$, $n \geq 1$, $z = q^3/(q^2+1)$ (convention D — see
[`rem:markov-axioms-primitive`](#rem:markov-axioms-primitive));
the negative stabilisation
$\mathrm{tr}_M(x \sigma_n^{-1}) = z_{-}\, \mathrm{tr}_M(x)$,
$z_{-} = z - (q - q^{-1})$, follows from the Hecke quadratic
relation.
The Markov property *is* the locality statement. $\square$ for (1).

**(2) GS non-locality.** Part (2) is a structural observation about
the Gröbner–Shirshov reduction algorithm on the Hecke algebra. The algorithm
applies three rewriting rules:

- *Hecke quadratic relation:*
  $\sigma_i^2 \to (q - q^{-1}) \sigma_i + 1$ (eliminates squared
  generators).
- *Braid relation:*
  $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$
  (Yang–Baxter / commutation).
- *Far-commutativity:*
  $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $\lvert i - j \rvert
  \geq 2$.

The braid relation acts on a window of three consecutive generators,
and successive applications can propagate changes across the entire
braid word. Therefore the normal form depends non-locally on the
input — flipping a single generator in $\beta$ can require rewriting
many generators in $\mathrm{NF}_{\mathrm{GS}}(\beta)$. $\square$ for (2).

**(3) Product factorisation.** Part (3) is Wenzl 1988
[`wenzl1988`], Theorem 5.13.2 in the QOU manuscript. The argument:

By the Wedderburn structure of $H_n(R, q)$ at generic $q$,
$$
  H_n(R, q) \otimes_R \mathbb{Q}(q^{1/2})
  \;\cong\;
  \bigoplus_{\lambda \vdash n}
    \mathrm{End}_{\mathbb{Q}(q^{1/2})}(S^\lambda_q).
$$
The normal form $\mathrm{NF}_{\mathrm{GS}}(\beta)$ is an element of
this direct sum; in each Wedderburn block, it is a single matrix
unit times a scalar coefficient. The Markov trace on a matrix unit
in $\mathrm{End}(S^\lambda_q)$ is (by uniqueness up to scalar) a
fixed multiple of the standard trace, with proportionality constant
$w_\lambda(q)$. The product factorisation then follows from the
multiplicativity of the standard trace on products of matrix units
in distinct positions of the same block: at each normal-form
generator $e_{j_i}$, the local contribution is exactly the
$i$-th vertex volume $\widehat{V}_i(q)$, determined by the local
data of the GS coefficient $(a_i, b_i)$.

Specifically, Wenzl 1988 establishes:
- The Wedderburn-block weight
  $w_\lambda(q) = \prod_{x \in \lambda}
  \bigl(z\,q^{c(x)} - z_{-}\,q^{-c(x)}\bigr)/\bigl(q^{h(x)} - q^{-h(x)}\bigr)$
  is the canonical proportionality constant, where $c(x)$ and $h(x)$
  are the content and hook length of the cell $x$ and
  $z_{-} = z - (q - q^{-1})$
  ([witness](computations/markov-trace-weights-wenzl.witness.json);
  exact for every $\lambda \vdash n \leq 5$).
- Each vertex volume $\widehat{V}_i(q)$ depends only on the
  Bratteli-diagram path traced by the normal-form generator $e_{j_i}$
  through the inductive system $H_1 \subset H_2 \subset \cdots$.
- The product $\prod_i \widehat{V}_i(q)$ equals the Markov trace of
  the normal-form element.

This factorisation is *local in the normal-form word*: each
vertex volume depends on a single normal-form generator and its
Bratteli-path context, not on the global braid word $\beta$. $\square$
for (3).

**Reconciliation.** Parts (1)–(3) together establish that the
composite operation $\beta \mapsto \mathrm{tr}_M(\rho(\beta))$
factors as

$$
  \beta \;\xrightarrow{\;\text{GS (non-local)}\;}\;
  \mathrm{NF}_{\mathrm{GS}}(\beta)
  \;\xrightarrow{\;\prod \widehat{V}_i \text{ (local in NF)}\;}\;
  \mathrm{tr}_M(\rho(\beta)).
$$

The first arrow is non-local; the second is local. The composite is
the global expectation value, and the two operational stances in the
QOU manuscript correspond to the two arrows. $\square$
