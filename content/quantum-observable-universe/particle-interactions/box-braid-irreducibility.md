*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*The process $\gamma\gamma \to \nu\nu^{\sigma}$ requires the
$T_{3,5}$ torus knot topology (weak mediator,
[force–knot identification](#rem:force-knot-identification)).
The crossing number $c(T_{3,5}) = 10$ is a topological invariant:
no braid representation in any $B_n$ whose closure is $T_{3,5}$
has fewer than $10$ crossings.  Each crossing is one $R$-matrix
application — one Planck step.  Therefore:*

1. *The process cannot occur before Planck step $10$.*
2. *No simpler mediator exists: $T_{3,5}$ is the unique
   cross-family torus knot on the genus-$4$ Bring's surface.*
3. *The box is the minimum-crossing topology for any
   $\gamma$–$\nu$ interaction.*

**The box braid: crossing-by-crossing.**

The process $\gamma\gamma \to \nu\nu^{\sigma}$ has no tree-level
realisation because photons ($K = \mathbf{1}_{B_4}$ 4-strand id;
see [confined-particle](#def:confined-particle),
[photon](#ex:photon-wavefront)) carry no braid strands and
neutrinos ($K_{0_1}$, [neutrino](#def:neutrino-knot)) have zero
crossing chirality $Q(\nu) = 0$.  The minimal topology is a box
with four vertices and four internal propagators, all at brane
tower level $A_1$
([virtual particles](#rem:virtual-particles-exceptional-divisor)):

```tex
\[
\begin{tikzcd}[row sep=3em, column sep=4em]
  \gamma_1 \ar[r, "\text{EM}" {above}, "\dagger\text{-coupling}" {below}]
  & e^-_{\mathrm{virt}} \ar[d, "\text{Skein}_{T_{3,5}}" {right}]
  \\
  \gamma_2 \ar[u, "\text{EM}" {left}, "\dagger\text{-coupling}" {right}]
  & \nu\nu^{\sigma} \ar[l, phantom, "\text{output}" {below}]
\end{tikzcd}
\]
```

**Vertex structure.**

At each vertex, a specific braid operation occurs:

- **EM vertices** ($\gamma \leftrightarrow e^-e^+$): the
  photon's $\dagger$-involution couples to the trefoil's
  antisymmetric crossing energy
  ([force–knot identification](#rem:force-knot-identification),
  §I), creating virtual $e^-e^+$ pairs at the exceptional
  divisor $\mathcal{S}_p$.  Each pair is a trefoil + mirror trefoil
  ($T_{2,3} \sqcup T_{2,3}^{\sigma}$) at brane level $A_1$.

- **Weak vertices** ($e \to \nu$ via $T_{3,5}$): the Skein
  relation mediated by $T_{3,5}$
  ([force–knot identification](#rem:force-knot-identification),
  §III) converts the charged trefoil to the neutral unknot.

**The $T_{3,5}$ braid word.**

The torus knot $T_{3,5}$ has braid representation
$(\sigma_1\sigma_2)^5 \in B_3$ with $(3-1) \cdot 5 = 10$
crossings:

$$
  W_{3,5} = 
  \sigma_1\sigma_2\sigma_1\sigma_2\sigma_1\sigma_2
  \sigma_1\sigma_2\sigma_1\sigma_2
  \qquad\text{(10 crossings)}
$$

*Proof that $c(T_{3,5}) = 10$ is irreducible.*

The crossing number of a torus knot $T_{m,n}$ with
$\gcd(m,n) = 1$ and $2 \leq m < n$ is

$$
  c(T_{m,n}) =  \min\bigl((m-1)n, (n-1)m\bigr).
$$

For $T_{3,5}$: $\min(2 \cdot 5, 4 \cdot 3) = \min(10, 12) = 10$.
The minimum is achieved by the $B_3$ representation
$(\sigma_1\sigma_2)^5$, and the braid index of $T_{3,5}$ is
$\min(3, 5) = 3$ (Morton–Williams inequality), confirming that
$B_3$ is the minimum strand count.

**Why no reduction below 10 crossings is possible:**

**(i) Topological invariance.**  The crossing number $c(K)$
is a knot invariant: it is the minimum number of crossings
over **all** diagrams of $K$ (not just positive braids, but
all braid groups $B_n$ and all non-braid diagrams).  For
torus knots, this minimum is known exactly.  No isotopy,
Reidemeister move, or change of braid representation can
reduce $c(T_{3,5})$ below $10$.

**(ii) Distinction from the Iwahori--Hecke algebra normal form.**
In the Iwahori--Hecke algebra $H_3(q)$, which has dimension
$|S_3| = 6$, the word $(\sigma_1\sigma_2)^5$ reduces to a
polynomial in the standard basis $\{T_w : w \in S_3\}$ —
with maximum word length $3$ per basis element (since the
longest element of $S_3$ has length $3$).  This algebraic
reduction computes the **amplitude** of the process (the
Markov trace gives the Jones polynomial $J_{T_{3,5}}(q)$),
not the physical crossing count.  Each $\sigma_i$ in the
original braid word is one physical $R$-matrix application
— one Planck step.  The Iwahori--Hecke algebra computes **what
amplitude** results from $10$ $R$-matrix applications; it
does not reduce the **number** of applications.

**(iii) $T_{3,5}$ is the unique cross-family mediator.**
The only torus knots embeddable on the genus-$4$ Bring
surface with winding numbers from both the $m = 2$ (lepton)
and $m = 3$ (quark) families are $T_{3,4}$ and $T_{3,5}$
([unmapped torus knots](#rem:unmapped-torus-knots)).
Of these, $T_{3,4}$ connects $m = 3$ to $n = 4$ (force
carrier: Hopf${}^2$ color binding in $H^{0,1}$), while
$T_{3,5}$ connects $m = 3$ to $n = 5$
(second generation).  Only $T_{3,5}$ mediates flavor-changing
charged-to-neutral transitions.  No alternative mediator with
fewer crossings exists on the Bring's surface.

**(iv) No direct $\gamma$–$\nu$ coupling.**
A direct coupling would require connecting the photon (no
braid strands, $Q = 0$) to the neutrino ($Q = 0$) without
charged intermediaries.  But the photon's electromagnetic
interaction is the antisymmetric component of the crossing
energy under the $\dagger$-involution — it couples only to
objects with $Q \neq 0$.  The neutrino has $Q(\nu) = 0$.
The charge-neutrality gap between photon and neutrino can
only be bridged by passing through charged intermediaries
($e^{\pm}$, trefoils with $Q = \pm 1$) and then converting
via the weak mediator $T_{3,5}$.  $\square$

**Corollary: neutrino stability.**

The neutrino ($K_{0_1}$, mass $m_\nu \sim \mu_0(q-1)$,
[neutrino](#def:neutrino-knot)) is **stable** — it cannot decay
via any process.

1. **No beta decay.** The neutrino is an elementary knot (unknot)
   with no internal constituents, no crossing orientation partition,
   and no substructure to rearrange
   ([electron immortality](#rem:electron-immortality) applies
   *a fortiori*: the unknot is even simpler than the trefoil).

2. **No scattering decay.** Any decay channel
   $\nu \to \gamma + \cdots$ or $\nu \to \nu' + \cdots$ must
   pass through the $T_{3,5}$ topology (or something at least as
   complex).  The $T_{3,5}$ mediator requires $10$ $R$-matrix
   applications — $10$ Planck steps of braid computation.  Each
   application costs crossing energy $(q - q^{-1}) \cdot \mu_0$.
   The total energy barrier:

   $$
     E_{\mathrm{box}}  \geq 
     c(T_{3,5}) \cdot (q - q^{-1}) \cdot \mu_0
     = 
     10 \cdot (q - q^{-1}) \cdot \mu_0
     \gg
     m_\nu =  \mu_0(q - 1).
   $$

   The ratio $E_{\mathrm{box}} / m_\nu \geq 10 \cdot (q + 1) / q \approx 19$ at the substrate parameter $q$: the box
   energy barrier is $\sim 19$ times the neutrino mass.

3. **No simpler process.** $T_{3,5}$ is the unique cross-family
   mediator on the Bring's surface, and its crossing number $10$
   is a topological invariant.  No isotopy or alternative mediator
   reduces the barrier.

The neutrino is therefore the **most stable** particle in the
Descartes universe: it has no decay channels at any energy below
the $T_{3,5}$ crossing threshold.  Unlike the electron (which is
stable by topological invariance of the trefoil — it *could*
interact but cannot *decay*), the neutrino is stable by
**energetic inaccessibility of its only interaction channel**.
This is why neutrinos pass through matter virtually unimpeded:
every interaction requires the full box machinery, which is both
topologically irreducible and energetically suppressed.
