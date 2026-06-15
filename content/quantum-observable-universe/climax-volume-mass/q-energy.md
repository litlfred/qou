*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The **$q$-energy** of a particle knot $K$ is the sum of three
terms, each derived from the categorical triple $(\mathbf{C}, A, \tau)$
and the substrate parameter $q$.

**Definition.**
Let $K = \hat{\beta}$ be a particle knot with braid representative
$\beta \in B_n$.  The **$q$-energy** is:

$$
  \mathfrak{E}_q(K) \;=\; \underbrace{J_q^2(K) \cdot \hbar_q}_{\text{rotational}}
  \;+\;
  \underbrace{p_q(\beta)^2 \cdot \hbar_q / (2\,[n]_q)}_{\text{translational}}
  \;+\;
  \underbrace{\mathfrak{S}_q(K)}_{\text{action (rest mass)}}
$$

where:

- $J_q^2(K) = [j]_q [j+1]_q$ is the $q$-angular momentum
  ([q-angular momentum](#def:q-angular-momentum)),
- $p_q(\beta)$ is the $q$-momentum (writhe)
  ([q-momentum](#def:q-momentum)),
- $\mathfrak{S}_q(K) = \mathrm{tr}_\tau(\rho(\beta))$ is the categorical
  action — the Markov trace of the braid in the Hecke
  algebra $H_n(R, q)$,
- $\hbar_q = 1 - q^{-1}$ is the quantum Planck constant,
- $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-number.

**The three terms.**

1. **Rotational term** $J_q^2 \cdot \hbar_q$:
   The $q$-deformed rotational energy.  For a spin-$\frac{1}{2}$
   particle at the substrate parameter $q$:
   $[1/2]_q [3/2]_q \cdot \hbar_q \approx 0.818 \times 0.0991 = 0.0811$.
   This vanishes at $q = 1$ (where $\hbar_q \to 0$).

2. **Translational term** $p_q^2 \cdot \hbar_q / (2[n]_q)$:
   The $q$-deformed kinetic energy from the writhe.
   The $[n]_q$ in the denominator is the $q$-deformed
   "number of strands" (inertia).

3. **Action term** $\mathfrak{S}_q(K)$: The categorical action
   $\mathfrak{S}_q = \mathrm{tr}(\mathscr{L}_q)$ evaluated on the knot.
   This is the **rest mass energy** — the categorical
   action (Markov trace of the braid representation):

$$
  \mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta))
$$

At a single brane level this equals $|\mathrm{tr}_M(\rho(\beta))|$
([categorical mass as Markov trace](#prop:categorical-mass-markov)).
The full mass including the brane tower evaluates to
$\mathrm{Vol}(K)/\hbar_q^2$ for hyperbolic knots
([topological mass formula](#prop:topological-mass-formula)).
For torus knots (including the trefoil / electron), the single-level
action is nonzero but the hyperbolic volume vanishes; the mass
arises from the quantum dilogarithm contributions across the tower
([mass endomorphism conjecture](#conj:mass-endomorphism)).

The action term dominates: for hadrons, $\mathfrak{S}_q \sim 10^3$ MeV
while the rotational and translational terms are $O(\hbar_q) \sim 0.1$.

**At rest** ($p_q = 0$, $J_q = 0$):

$$
  \mathfrak{E}_q(K)\big|_{\text{rest}} \;=\; \mathfrak{S}_q(K) \;=\; \mathfrak{m}(K) c^2
$$

recovering the topological mass formula.

**Limits.**

| Limit | $\mathfrak{E}_q$ |
|-------|-------|
| $q = 1$ (classical) | $j(j+1) \cdot 0 + w^2 \cdot 0 + \mathfrak{S}_1 = \mathfrak{S}_1$ |
| $q \to \infty$ (deep-quantum) | $J_q^2 \to q^{2j+1}, \; p_q \to w \cdot q, \; \mathfrak{S}_q \to \infty$ |
| Rest frame | $\mathfrak{S}_q(K)$ (mass) |

**Relation to crossing energy.**

Each crossing in the braid word contributes energy
$\mathfrak{E}_\times(q) = \frac{1}{2}(q - q^{-1}) = 0.1045$ (in units
of the mass scale $\mu_0$).  The total action is:

$$
  \mathfrak{S}_q(K) \;=\; \sum_{j=1}^{k} \mathfrak{E}_\times^{(\epsilon_j)}(q)
$$

where $\epsilon_j = \pm 1$ is the crossing sign.  For a
positive crossing: $\mathfrak{E}_\times^{(+)} = q$.  For a negative
crossing: $\mathfrak{E}_\times^{(-)} = q^{-1}$.  The asymmetry
$q \neq q^{-1}$ at the substrate parameter $q$ means positive crossings
carry more energy than negative ones — this is the energy
signature of parity violation.
