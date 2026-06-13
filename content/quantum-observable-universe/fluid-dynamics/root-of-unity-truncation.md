**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Root-of-unity truncation").**

The [QOU axiom](#def:substrate-parameter) requires that $q$ is
**not** a root of unity. But the limit $q \to 1$ passes through
a dense set of roots of unity, and at each root the
representation theory undergoes a dramatic truncation that
**strengthens** regularity. The blowup at $q = 1$ is the
accumulation of infinitely many such truncations.

The truncation mechanism itself — the vanishing of the $q$-integer
$[\kappa]_q$ at $q = e^{i\pi/\kappa}$, collapsing the $q$-Laplacian
spectral tower $[k]_q^2$ to the finite Verlinde/ADE set — is
established in
[the $q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower).
Here we read off its fluid-dynamical consequence.

**Three regimes of $\mathrm{SU}_q(2)$ representations.**

1. **Generic $q > 1$ (QOU regime).**
 Infinitely many simple objects $V_j$, $j = 0, 1/2, 1, \ldots$
 Quantum dimensions $[2j+1]_q > 0$ for all $j$.
 Eigenvalues $[k]_q^2 \sim q^{2k}$ (exponential growth).
 The [well-posedness theorem](#thm:q-ns-wellposedness) gives
 global regularity.

2. **Root of unity $q = e^{i\pi/\kappa}$, $\kappa \in \mathbb{Z}_{\geq 2}$.**
 Only **finitely many** simple objects: $j = 0, 1/2, \ldots,
   (\kappa-2)/2$. The quantum dimension $[2j+1]_q$ vanishes at
 $j = (\kappa-1)/2$, truncating the representation category.
 The Verlinde formula governs fusion:

 $$
     N_{ij}^k
     = \int_0^1 \frac{S_{ik}S_{jk}}{S_{0k}}dk,
   $$

 where $S$ is the modular $S$-matrix. The representation
 category becomes a **modular tensor category** — the algebraic
 input for Chern--Simons TQFT at level $\kappa$.

3. **$q = 1$ (classical limit).**
 Infinite simple objects with $[k]_1 = k$ (polynomial).
 No truncation, no exponential damping. The
 [regularity breakdown](#conj:regularity-breakdown) regime.

**Root-of-unity regularity is stronger than generic.**

At $q = e^{i\pi/\kappa}$, the q-NS system has at most
$(\kappa-1)/2$ active vortex modes (the truncated representation
category has finitely many objects). This is a **hard cutoff**,
not the soft exponential damping of generic $q > 1$:

- Generic $q > 1$: modes with $[k]_q > \mathrm{Re}_q^{1/2}$
 are exponentially damped but nonzero.
- Root of unity: modes with $j > (\kappa-2)/2$ **do not exist**
 in the category. The Hilbert space is finite-dimensional.

A finite-dimensional ODE is by definition globally regular
(Picard--Lindelöf). So at every root of unity, the q-NS
system is not only well-posed but **finite-dimensional**.

**The $q = 1$ accumulation.**

As $\kappa \to \infty$, $q = e^{i\pi/\kappa} \to 1$. The
truncation level $j_{\max} = (\kappa-2)/2 \to \infty$: more
and more modes become available. The sequence of
finite-dimensional systems approaches the infinite-dimensional
classical system.

The blowup at $q = 1$ is the statement that this
infinite-dimensional limit is **singular**: no finite truncation
blows up, but the limit of all truncations can. This is
precisely the structure of a **phase transition at the
accumulation point**.

**Connection to the core aspect ratio.**

At a root of unity $q = e^{i\pi/\kappa}$, the vortex core
shape is controlled by the **modular tensor category** structure.
The fusion rules $N_{ij}^k$ determine which mode interactions
are allowed. The truncation $j \leq (\kappa-2)/2$ forbids
high-frequency core deformations: the core **cannot** develop
fine-scale structure beyond the cutoff. In particular:

- The core aspect ratio $\kappa(t) = a_\perp/a_\parallel$
 is controlled by the Fourier modes of the core boundary.
- At root of unity: only $(\kappa-1)/2$ modes exist, so
 $\kappa(t)$ is a trigonometric polynomial of bounded degree.
- A trigonometric polynomial of degree $N$ satisfies
 $|\kappa'(t)| \leq N\|\kappa\|_\infty$ (Bernstein
 inequality), preventing rapid oscillation.

This gives an **explicit bound** at each root of unity:

$$
  \sup_{t < T^*} \kappa(t)
   \leq 
  1 + C \cdot (\kappa - 1)
$$

for some universal constant $C$. The bound grows linearly
with the truncation level $\kappa$, and diverges as
$\kappa \to \infty$ ($q \to 1$).

**The refined gap.**

The original [vorticity lower bound](#prop:vorticity-lower-bound)
requires $\sup_t \kappa(t) \leq C$ with $C$ independent of $q$.
The root-of-unity analysis gives $\kappa(t) \leq 1 + C(\kappa-1)$,
which grows with $\kappa$. The question is the **rate of growth**:

- If $\kappa(t) \leq C_0$ uniformly (independent of $\kappa$):
 the core stays circular, the lower bound holds, and NS blows up.
 Counter-example established.

- If $\kappa(t) \sim \kappa$ (linear growth): the core flattens at
 the same rate as modes become available. The vorticity spreads
 into a sheet, and the lower bound $\omega \geq c/(T^*-t)$ may
 fail. NS might be regular.

- If $\kappa(t) \sim \kappa^\beta$ with $0 < \beta < 1$: an
 intermediate case. The lower bound holds if $\beta < 1/2$
 (the flattening is slower than the approach).

The [Levi form condition number](#def:levi-form-defect) at the
vortex core is $\lambda_{\max}/\lambda_{\min}$, which equals
$\kappa(t)^2$. The contact structure degenerates (becomes
integrable) iff $\lambda_{\min} \to 0$, i.e. $\kappa(t) \to
\infty$. So:

$$
  \boxed{
    \text{NS blows up}
    \iff
    \text{Levi form stays non-degenerate at collision}
    \iff
    \kappa(t) = O(1).
  }
$$

**This is the contact-geometric form of the millennium problem:**
does the contact structure of the brane remain non-degenerate
at the collision point of two vortex filaments?
