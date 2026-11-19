The pentagon identity of the quantum dilogarithm
(quantum Bloch group)

$$
  \Phi_q(v)\,\Phi_q(u) \;=\; \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v)
$$

requires the quantum-torus relation $uv = q\,vu$ on its operator arguments. The analysis below establishes where that relation lives in the brane-tower formalism and how it drives the jet-tower mass ascension.

## Within a single jet level — trivial commutation

At a fixed jet level $n$, the traced volumes $\hat V_i^{(n)}
\in \mathbb{Z}[q^{\pm 1/2}, z]$ are **scalar Laurent polynomials**
([algebraic quantum volume](#def:algebraic-quantum-volume)).
Two scalars commute, so

$$
  \hat V_i^{(n)} \, \hat V_j^{(n)}
  \;=\;
  \hat V_j^{(n)} \, \hat V_i^{(n)}
$$

without any $q$-factor. This is the level-internal lemma
[traced-volume pair commutation](#lem:vhat-pair-commutation-trace); it
settles the level-internal half of the commutation question.

## Between adjacent jet levels — the pentagon q-factor

The brane tower
([recursive brane tower](../lifting-and-descent/recursive-brane-tower.md))
admits a non-commutative quantization in which the level-shift
operator $\hat\tau_n$ supplies the canonical pair $u, v$
satisfying $uv = q\,vu$. Specifically, let $\widehat U_i$ and
$\widehat V_j$ denote level-shift conjugates of $\hat V_i$ and
$\hat V_j$ at adjacent jet levels $n$ and $n+1$. Then

$$
  \widehat U_i \, \widehat V_j
  \;=\;
  q \, \widehat V_j \, \widehat U_i
$$

on the transient summand $\ker \hat\tau_n$ between the two
levels, where the :refterm[descent]{#descent} involution $\hat\tau_n$ separates the
descended part (where the residual $R_q$ lives) from the
transient part (where the pentagon $q$-factor is exact).

**Proposition.** The pentagon identity
$\Phi_q(v)\,\Phi_q(u) = \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v)$
applies to the operator lift $u = \widehat U_i$, $v = \widehat
V_j$ at adjacent jet levels $n, n+1$, and supplies the
*inter-level ascension rule* for the jet-tower mass formula
([jet-brane mass-tower formulation](#rem:mass-endomorphism-jet-tower)):

a triple product at jet level $n$ rewrites via pentagon as a
pair plus a singleton at level $n$, leaving a residual
$\Phi_q(uv)$ that ascends to level $n+1$.

## Proof

The pentagon q-factor is a feature of the brane tower's
$q$-graded jet stratification, not of the scalar $\hat V_i$'s:

1. **Hecke braid relation** at the operator level (before
   :refterm[descent]{#descent} to scalars): $\sigma_s \sigma_{s+1} \sigma_s =
   \sigma_{s+1} \sigma_s \sigma_{s+1}$ in $H_n(R, q)$.
2. **:refterm[Descent]{#descent} involution split**: $\hat\tau_n$ separates
   $H_n(R, q)$ into $\mathrm{im}\,\hat\tau_n$ (descended,
   level-$n$ contribution) and $\ker\,\hat\tau_n$ (transient,
   ascends to level $n+1$).
3. **Eigenvalue specialisation** on the $q$-block of $\sigma_s$
   reduces the descended part to scalar form, where commutation
   is trivial.
4. **Operator lift on the transient part**: the surviving
   non-trivial commutation is between level-$n$ and level-$(n+1)$
   operators, giving the quantum-torus relation $uv = q\,vu$.

The pentagon identity then governs how triple products at level
$n$ reorganise into pair + singleton at level $n$ plus a residual
ascending to level $n+1$ — the algebraic content of the jet-tower
ascension.

## Significance for the mass tower

The mass-tower jet form
([jet-brane mass-tower formulation](#rem:mass-endomorphism-jet-tower))

$$
  \mathfrak{m} \;=\; |\mathrm{tr}_M(W)|
  + \sum_{n=0}^{N}\!\Bigl(\sum_{\xi \in \mathcal{S}^{(n)}_1}\!\Phi_q(|\mathrm{tr}_M(\xi)|)
  + z^2\!\!\!\sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2}\!\!\!\Phi_q(|\mathrm{tr}_M(\xi\xi')|)\Bigr)
  + R_N
$$

contains only **singletons** ($\mathcal{S}_1$) and **pairs**
($\mathcal{S}_2$) at each level $n$, plus a tail bound $R_N$.
The pentagon's role is structural: it certifies that **no
triples** appear at any level — every triple at level $n$ is
absorbed into a pair plus singleton at level $n$ plus a
residual that lives at level $n+1$. Iterating gives the jet
ascension; the geometric tail bound from
[brane-tower geometric tail bound](#prop:jet-tower-convergence)
controls $R_N$.
