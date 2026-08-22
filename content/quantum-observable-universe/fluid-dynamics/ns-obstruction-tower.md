**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"NS obstruction tower").**

Let $(\mathbf{C}, A, \tau)$ define a QOU carrying Euler characteristic $\chi(A)$ and [obstruction classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$. Let $\Sigma \subset \mathcal{S}$ denote the precise collision locus of two anti-parallel vortex filaments.

The [boundary observability](#def:ns-regular-qou) $\mathrm{Obs}_\partial(A)$ derives directly from the restriction of the obstruction classes down to the collision locus:

$$
  \mathrm{Obs}_\partial(A)
  = 
  \ker\!\left(
    \bigoplus_{n \geq 0}
    H^2(\mathcal{S}, \mathcal{B})
    \xrightarrow{ \mathrm{res}_\Sigma}
    \bigoplus_{n \geq 0}
    H^2(\Sigma, \mathcal{B}|_\Sigma)
  \right).
$$

The QOU is [NS-singular](#def:ns-regular-qou) (mandating blowup) if and only if $\mathrm{res}_\Sigma(\kappa_n) \neq 0$ for at least one $n$. It is NS-regular if and only if $\mathrm{res}_\Sigma(\kappa_n) = 0$ for all $n$.

**Proof.**

**(a) Where the obstruction sits.**

Following the [QU-to-QOU theorem](#thm:qu-to-qou), the base obstruction is exactly $\kappa_0 = e(\xi)$, the Euler class of the Reeb bundle, carrying $\mathrm{tr}(\kappa_0) = \chi(A)$. The obstruction at arbitrary level $n$ takes the form

$$
  \kappa_n
  = 
  \kappa_0
  + 
  \delta_n,
  \qquad
  \delta_n \in \mathrm{im}\!\bigl(
    H^2(\mathcal{S}, \mathcal{O}_\mathcal{S})
    \to H^2(\mathcal{S}, \mathcal{B})
  \bigr),
$$

where $\delta_n$ applies the explicit jet correction at level $n$. Due to the perpetual obstruction ([QU-to-QOU](#thm:qu-to-qou) item 3, rigidly strengthened by the [motivic perpetual obstruction theorem](#conj:motivic-perpetual-obstruction) evaluating the substrate's motivic Galois character place-by-place), $\kappa_0$ and $\delta_n$ strictly occupy complementary subgroups whenever $\kappa_0$ avoids torsion. Consequently, $\kappa_n \neq 0$ unconditionally for all $n$.

**(b) Restriction to the collision locus.**

The collision locus $\Sigma$ forms a strict 1-dimensional submanifold (a line segment). $H^2(\Sigma, \mathcal{B}|_\Sigma)$ derives from the long exact sequence applied to the pair $(\mathcal{S}, \mathcal{S} \setminus \Sigma)$:

$$
  \cdots \to
  H^1(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \xrightarrow{\partial}
  H^2_\Sigma(\mathcal{S}, \mathcal{B})
   \to 
  H^2(\mathcal{S}, \mathcal{B})
  \xrightarrow{ \mathrm{res}}
  H^2(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \to \cdots
$$

The obstruction transfers nontrivially to $\Sigma$ if and only if $\kappa_n$ strictly evades the image of the restriction map descending from $\mathcal{S} \setminus \Sigma$. Equivalently, the connecting homomorphism $\partial$ isolates it: $\kappa_n|_\Sigma \neq 0$ if and only if $\kappa_n$ maintains nontrivial **local cohomology** support anchored precisely at $\Sigma$.

**(c) Local cohomology computation.**

Evaluating the [local cohomology](#def:local-cohomology-group) at any collision point $p \in \Sigma$ gives

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  R^1\Gamma_{\mathfrak{m}_p}(A).
$$

For the anti-parallel pair, each vortex filament naturally hosts the fundamental representation $V_{1/2}$ of $\mathrm{SU}_q(2)$. At the intersection point $p$, both filaments stack their contributions onto the local cohomology:

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  V_{1/2}^{(1)} \oplus V_{1/2}^{(2)}.
$$

This constructs a rigid 4-dimensional space. It remains **nonzero** if and only if both individual filaments successfully provide nontrivial local sections at $p$ — that is, when the discrete vortex cores have not dissolved into a continuous sheet.

**(d) Connection to core aspect ratio.**

Relying on [core-Levi equivalence](#prop:core-levi-form), the local cohomology holds a nonzero value if and only if the Levi form maintains strict non-degeneracy at $p$. Algebraically:

$$
  H^1_{\mathfrak{m}_p}(A) \neq 0
  \quad\Longleftrightarrow\quad
  \lambda_\parallel(p) > 0
   \text{ and }
  \lambda_\perp(p) > 0
  \quad\Longleftrightarrow\quad
  \kappa(p) = a_\perp/a_\parallel \in (0, \infty).
$$

If the core flattens completely ($\kappa \to 0$ or $\kappa \to \infty$), one Levi eigenvalue collapses. The local cohomology subsequently degenerates from $V_{1/2}^{\oplus 2}$ down to a quotient, forcing the obstruction class $\kappa_n|_\Sigma$ to deform safely toward zero.

**(e) The NS obstruction as an Euler-class residue.**

Synthesising (a)--(d), the exact NS obstruction at level $n$, forcibly restricted to the collision locus, yields

$$
  \kappa_n\big|_\Sigma
  = 
  \mathrm{lk}(\varrho_1, \varrho_2)
  \cdot e(\xi)\big|_\Sigma
  +  \delta_n\big|_\Sigma,
$$

where $\mathrm{lk}(\varrho_1, \varrho_2)$ tracks the explicit linking number separating the two filaments, and $e(\xi)|_\Sigma$ evaluates the Euler class of the Reeb bundle precisely on $\Sigma$.

Mapped onto the Descartes universe ($\chi(A) = -6$, anchored on Bring's surface): $e(\xi) = -6 \cdot [\Sigma_4]$ evaluated inside $H^2(\Sigma_4, \mathbb{Z})$. The local restriction $e(\xi)|_\Sigma$ registers as nonzero strictly when $\Sigma$ behaves homologically nontrivially inside $\Sigma_4$. The anti-parallel pair (carrying linking number 1) satisfies this identically.
