The pentagon identity of the quantum dilogarithm
([quantum Bloch group](#rem:quantum-bloch-group)) applies to a
pair of operators $u, v$ satisfying the **quantum-torus
relation**

$$
  uv \;=\; q\,vu.
$$

The ascension argument in the
([jet-tower remark](#rem:mass-endomorphism-jet-tower)) uses
$u = \hat V_i^{(n)} \hat V_j^{(n)}$ and
$v = \hat V_k^{(n)}$ where $\hat V_\ell^{(n)}$ are the
additive Wedderburn traced-volume operators at jet level $n$.
This proposition verifies that the required commutation holds
on the physically relevant block.

**Proposition.**  Let $(i,j,k)$ with $i < j < k$ be a triple
of braid-generator indices at fixed jet level $n$, and let
$\hat V_\ell \equiv \hat V_\ell^{(n)}$ be the Markov-traced
generator volumes
([Markov trace factorization](#thm:markov-trace-factorization)).
Set $u = \hat V_i\hat V_j$ and $v = \hat V_k$.  In the
Wedderburn block $B_\lambda \subset H_n(R, q)$ on which the
standard-representation eigenvalue of the Hecke generator is
$q$, the operator pair satisfies

$$
  u\,v \;=\; q\,v\,u
  \qquad \text{on }B_\lambda^{\mathrm{trans}},
$$

where $B_\lambda^{\mathrm{trans}}$ is the transient summand of
$B_\lambda$ at jet level $n$.

## Derivation

*Step 1 — Reduce to a two-generator commutator.*  By
far-commutativity in the Hecke algebra
([Jones--Markov trace](#thm:jones-markov-trace)), for
$|p - r| \ge 2$ the generators $\sigma_p, \sigma_r$ commute
outright: $\sigma_p\sigma_r = \sigma_r\sigma_p$, hence
$\hat V_p\hat V_r = \hat V_r\hat V_p$ whenever they act on
disjoint strands.  The only non-trivial commutation is between
**adjacent** Hecke generators; after far-commuting the
non-adjacent factors of $u$ past $v$, the commutator
$[u,v]_q := uv - q\,vu$ reduces to a sum of commutators of the
form $[\hat V_s \hat V_{s+1}, \hat V_{s+1}]_q$ for $s \in \{j-1, j, k-1\}$
determined by the braid pattern of the triple.

*Step 2 — Eigenvalue specialization.*  On the $q$-eigenblock
$B_\lambda$ of $\sigma_s$ (the block where the Hecke relation
$\sigma_s^2 = (q - q^{-1})\sigma_s + 1$ specializes to the
eigenvalue $q$), the generator $\sigma_s$ acts as scalar
multiplication by $q$ in the standard representation.  By the
[generator volume decomposition](#prop:generator-volume-decomposition),
$\hat V_s = z\,a_s + b_s$ where $a_s, b_s$ are transfer-matrix
polynomials in $q$.  On $B_\lambda$, the traced-volume operator
$\hat V_s$ reduces to a scalar $\hat v_s \in \mathbb{Q}(q^{1/2})$
that commutes with every other block-diagonal operator.  The
non-trivial commutation survives **only** in the ladder between
blocks, carried by the Hecke braid relation
$\sigma_s\sigma_{s+1}\sigma_s = \sigma_{s+1}\sigma_s\sigma_{s+1}$.

*Step 3 — Braid relation at the pair level.*  Multiplying the
braid relation $\sigma_s\sigma_{s+1}\sigma_s = \sigma_{s+1}\sigma_s\sigma_{s+1}$
on the left by $\sigma_s^{-1}$ gives the pair-swap identity
$$
  \sigma_{s+1}\sigma_s
  \;=\;
  \sigma_s^{-1}\,\sigma_{s+1}\sigma_s\sigma_{s+1}.
$$
Using $\sigma_s^{-1} = \sigma_s - (q - q^{-1})$ from the Hecke
relation, and taking the Markov-traced volume at block-diagonal
eigenvalue $q$:

$$
  \hat V_s \hat V_{s+1}
  \;=\;
  q \cdot \hat V_{s+1} \hat V_s
  \;+\; R_q(\hat V_s, \hat V_{s+1}),
$$

where the residual $R_q$ is a sum of lower-order terms
proportional to $(q - q^{-1})$.  The residual $R_q$ is
**descended**: it factors through the image of
$\hat\tau_n \colon \mathcal{A}_{n+1} \to \mathcal{A}_{n+1}^{\mathrm{desc}}$
([descent involution](#def:descent-involution)).  Indeed, the
Hecke reduction $\sigma_s^2 = (q - q^{-1})\sigma_s + 1$
projects any power of $\sigma_s$ onto $\{1, \sigma_s\}$; the
constant-term contribution to $R_q$ is the descended part at
level $n$, and the $\sigma_s$-linear term lifts to a pair
generator at level $n{+}1$ — precisely the ascension pattern
encoded in the pentagon identity.

*Step 4 — Quantum-torus relation on the transient block.*
Restricting to the transient summand
$B_\lambda^{\mathrm{trans}} = \ker\hat\tau_n \cap B_\lambda$
([descent eigenspaces](#prop:descent-eigenspaces)), the
descended residual vanishes:
$R_q|_{B_\lambda^{\mathrm{trans}}} = 0$.  The remaining
identity is

$$
  \hat V_s \hat V_{s+1}
  \;=\; q\,\hat V_{s+1} \hat V_s
  \qquad \text{on }B_\lambda^{\mathrm{trans}}.
$$

Applying this pairwise rewrite to $u = \hat V_i \hat V_j$ and
$v = \hat V_k$, and using the far-commutativity of Step 1 to
move non-adjacent factors, yields
$u\,v = q\,v\,u$ on $B_\lambda^{\mathrm{trans}}$.
$\square$

## Why the transient block is the right domain

The pentagon identity of $\Phi_q$ in the form
$\Phi_q(v)\Phi_q(u) = \Phi_q(u)\Phi_q(uv)\Phi_q(v)$ with
$uv = qvu$ produces a **three-factor** right-hand side.
Interpreting the residual triple $\Phi_q(uv)$ as a new
blow-up centre, the ascension
([jet-tower remark](#rem:mass-endomorphism-jet-tower))
rewrites a level-$n$ triple $\Phi_q(|\hat V_i\hat V_j\hat V_k|)$
as level-$n$ pairs/singletons plus a residual that cannot be
absorbed at level $n$.  By Step 3, that residual lies in
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat\tau_n$ —
the transient (new-mode) algebra at the next jet level — where
the pentagon commutation $uv = qvu$ is exact.

The descent involution $\hat\tau_n$ therefore exactly separates
the two halves of the pentagon:

- **Descended part** ($\mathrm{im}\hat\tau_n$): carries
  $R_q$, the non-pentagon residual.  Contributes to the
  base-level mass only once
  ([descended level-0 only](#prop:descended-level-zero)).
- **Transient part** ($\ker\hat\tau_n$): satisfies
  $uv = qvu$ and admits the pentagon ascension.  Contributes
  a pair or singleton at level $n{+}1$.

This is the operator-level justification of the quadratic
closure of the mass tower per jet level.

## Limitation — what this proposition does *not* prove

The derivation above establishes the quantum-torus relation
$uv = q\,vu$ on the $q$-eigenblock $B_\lambda^{\mathrm{trans}}$
using the Hecke braid relation and descent splitting.  Two
points are deferred:

1. **Other Wedderburn blocks.**  At the eigenvalue $-q^{-1}$
   (alt block, $\mathrm{sign}$ representation), the analogous
   commutation is $uv = q^{-1}\,vu$, which reverses the sign
   of the quantum dilogarithm argument.  The net contribution
   at level $n{+}1$ is symmetric under $q \leftrightarrow q^{-1}$,
   consistent with the $\mathrm{sym} \leftrightarrow \mathrm{alt}$
   exchange in the three-Wedderburn formula
   ([Wedderburn mass formula](#thm:wedderburn-mass-formula)).
   A direct check on the std ($2\times 2$) block is open.

2. **Sharpness of the residual.**  Step 3 only shows
   $R_q \in \mathrm{im}\hat\tau_n$; it does not determine
   $R_q$ explicitly.  A sharp form would match $R_q$ to the
   base-level descended contribution and close the remaining
   open piece of the jet-tower decomposition
   ([jet-tower remark](#rem:mass-endomorphism-jet-tower),
   subconjecture 3).
