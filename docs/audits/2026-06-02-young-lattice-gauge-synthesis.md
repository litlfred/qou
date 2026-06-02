# Young's-lattice synthesis: gauge structure, the 5↔3 keystone, and the vertical obstruction

**Date:** 2026-06-02
**Trigger:** Author framing during the group-actions exploration:
*"what does repn theory say? all needs to be compatible on Wedderburn
decomposition / partitions"* — followed by *"what about SU(2) spinors
for the eigenvalues / spaces / basis?"*
**Status:** Synthesis / coordination doc. Ties together eight merged
audits into a single representation-theoretic statement on Young's
lattice. No new compute; cross-references the merged probes.

## Headline

Reading the session's eight group-action audits against the
Wedderburn/partition decomposition of $H_n(q)$ collapses them into
**one** statement with a clean split:

> **Horizontal** (fixed strand-count $n$, across blocks $\lambda \vdash
> n$) is *settled*: the gauge charges are **central characters**, hence
> per-partition scalars (the content statistic), automatically
> compatible with the Wedderburn decomposition.
> **Vertical** (across $n$: connecting strand-counts by branching) is
> the *single remaining obstruction*: the only canonical maps are
> branching (add/remove a box), and between non-adjacent levels these
> are **multivalued**. The keystone "missing functor" and hypercharge's
> "missing second charge" are the **same** vertical obstruction.

The SU(2)-spinor refinement sharpens — but does not remove — the
vertical obstruction: a canonical **eigenbasis** of the multiplicity
space exists (Okounkov–Vershik / Jucys–Murphy), so the missing object
is a canonical **section**, not a canonical basis.

## Setup: everything is data on Young's lattice

$H_n(q)$ is semisimple at the substrate (real $q_0$), so Wedderburn
gives
$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} M_{d_\lambda}(\mathbb{C}(q)),
  \qquad d_\lambda = \#\,\mathrm{SYT}(\lambda).
$$
Blocks are indexed by **partitions** $\lambda \vdash n$; the Markov
trace is the per-partition Schur-weighted sum $\mathrm{tr}_M =
\sum_\lambda w_\lambda \chi^\lambda$. Every object in the framework —
observables, gauge charges, knot operators — is a **function on the
set of partitions**, with two structural directions.

## Horizontal direction (fixed $n$): the gauge sector is settled

The gauge correspondences established this session:

| Group | Corresponds to | Per-partition realization |
|-------|----------------|---------------------------|
| **U(1)** | writhe / ribbon **framing** | central → scalar $q^{w\cdot c}$ per block |
| **SU(2)** | **spinor** rotation (half-integer) | ribbon twist $\theta_\lambda = q^{\,2c(\lambda)}$, $\theta_j = q^{j(j+1)}$ |
| **SO(3)** | **orbital** rotation of the 3 color sheets (integer $\ell$) | spherical-harmonic level $\ell$; finite subgroups $S_3$ (pipeline), $I\cong A_5$ (fiber) |

The decisive representation-theory fact: the ribbon twist and the
framing/writhe phase are **central** elements, so by Schur's lemma they
act as **scalars on each block** $\lambda$. The
[u1-hypercharge audit](2026-06-02-u1-hypercharge-assignment.md)
computed exactly this — the twist eigenvalues came out as $\theta_j =
q^{j(j+1)}$ per block, the **Casimir/content ladder**, with no free
parameter. Therefore:

- **U(1) and SU(2) are diagonal on the Wedderburn decomposition** —
  they are compatible with the partition structure *by construction*,
  because central characters cannot be anything else.
- The per-crossing coupling is **fixed** ($c = 1/2$, pinned by
  [`def:coulomb-charge`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.lean):
  $Q = \tfrac12(n_+ - n_-) = \mathrm{writhe}/2$), not free — see the
  u1-hypercharge audit. Tuning $c$ is structurally foreclosed.
- The writhe matches **$I_3$** (isospin), not $Y$ or $Q$: the $p/n$
  same-$Y$ test falsifies writhe$\to Y$; the sign+ratio pattern
  $(+\tfrac12, -\tfrac12)$ matches $I_3$, consistent with the
  $u\leftrightarrow d$ swap being the $\sigma\leftrightarrow\sigma^{-1}$
  crossing-sign flip.

The horizontal gauge sector raises no Wedderburn-compatibility
problem.

## Vertical direction (across $n$): the single obstruction

The only canonical maps between strand counts are restriction and
induction — i.e. **branching**, the edges of Young's lattice
(add/remove a box). The
[5↔3 keystone audit](2026-06-02-h5-h3-functor-keystone.md) computed
these exactly:

- $\mathrm{Res}^{H_5}_{H_3}$ sends the $(2,1)$ baryon block across 5 of
  7 partitions $\lambda \vdash 5$ with multiplicity vector
  $[0,1,2,2,2,1,0]$ — multiplicities in $\{1,2\}$. (Note: $(4,1)$ and
  $(2,1,1,1)$ *do* restrict with multiplicity exactly 1; the obstruction
  is not "multiplicity $\neq 1$" but the absence of a canonical *single
  channel*.)
- Induction, the Markov tower $H_3\subset H_4\subset H_5$, and the
  icosahedral $\mathrm{Res}^{A_5}_{S_3}(H_{\ell=2}) = \mathrm{triv}
  \oplus 2\cdot(2,1)$ all send $(2,1)$ with the same multivalued
  structure.

**Theorem (keystone nonexistence).** There is no canonical map sending
the $\ell=2$ fiber amplitude to *the* $h^4 = -3/4$ baryon coefficient,
because $\mathrm{Hom}(\text{fiber}, (2,1))$ is a multiplicity space of
dimension $\geq 1$ with no canonical distinguished basis vector — any
choice is an element of a $\geq 1$-dimensional Hom-space, i.e. a fit.

This is the vertical obstruction. It is **not** that the representation
rings differ (restriction/induction are perfectly good functors
*between* them) — it is that the correspondence is **multivalued**.

### The leptons evade it by living at fixed $n=2$

The [lepton T(2,n) tower audit](2026-06-02-lepton-t2n-torus-tower.md)
showed the charged leptons are the 2-strand torus knots $T(2,n)$
($e=T(2,3)$, $\mu=T(2,5)$, $\tau=T(2,7)$), entirely inside $H_2$ (two
blocks). They have **no vertical problem** — their tower is the
writhe/generation index *within* one strand count, with the
S$_5$-equivariance selection $n\in\{3,5\}$ giving a **2+1 generation
split theorem**. This is why the lepton sector produced clean theorems
while baryon binding did not: **leptons are horizontal-only; baryon
binding is inherently vertical.**

## The SU(2)-spinor refinement (the author's follow-up)

Does the spinor structure resolve the multiplicity? The
[spinor-resolution audit](2026-06-02-su2-spinor-multiplicity-resolution.md)
answers precisely — **verdict (ii): #1684 sharpened, not overturned.**

- **Separation — YES.** The Okounkov–Vershik / Jucys–Murphy content
  eigenbasis exists: the JM $q$-content tuple $(c_4, c_5)$ separates the
  two $(2,1)$ copies in every multiplicity-2 case (the two orderings of
  a symmetric pair, e.g. $(2,0)$ vs $(0,2)$). So "no canonical *basis*"
  is **refuted** — the multiplicity space carries the canonical OV
  content-eigenbasis that $\mathrm{tr}_M$ already uses.
- **Selection — NO.** The baryon's *final-block* spin (the "$(2,1)$ is
  spin-$\tfrac12$") is **constant** across copies. Only the
  *intermediate*-$H_4$ spin differs — $(3,2)\to\{1,0\}$,
  $(3,1,1)\to\{1,\tfrac12\}$, $(2,2,1)\to\{0,\tfrac12\}$ — and these
  have empty global intersection $\{0,1\}\cap\{\tfrac12,1\}\cap
  \{0,\tfrac12\}=\varnothing$. No single spin value selects a copy
  consistently across $\lambda\vdash 5$; doing so would be a fit *and*
  ill-defined.

**Upgrade:** the obstruction moves from "no canonical **basis**" → "no
canonical **section**." The basis provably exists; the missing object
is a *forced nominator* of the physical copy. $h^4=-3/4$ is a block
invariant (not per-copy), so spin/JM choose *which copy embeds*, not
the $h^4$ value — no closure, no fit.

## The unification: one obstruction, two symptoms

Within a fixed $n$, the central characters give finitely many
per-partition scalars (content, Casimir) — **one** charge
(writhe$\to I_3$). Gell-Mann–Nishijima $Y = 2(Q - I_3)$ needs $Q$ and
$I_3$ *independently*, but here $Q=\mathrm{writhe}/2$ and the
writhe-derived $I_3$ are the **same datum**. The missing second charge
is **baryon number**, which *counts strands* — an inherently
**vertical** quantum number. Therefore:

> Hypercharge $Y$ is incomplete because its missing second charge is
> vertical (baryon number); the 5↔3 binding is blocked because the
> vertical map is multivalued. **These are the same vertical
> obstruction on Young's lattice.**

## Non-fit escapes (the productive frontier)

Representation theory leaves exactly two non-fit ways past the vertical
obstruction (both already named across the audits, now unified):

1. **Non-functorial / geometric section.** The canonical nominator
   comes from *extra* structure beyond Hecke rep theory — the
   icosahedral holonomy / color-tube cross-ratio on Bring's quintic
   surface ([flavor-cusp audit](2026-06-01-flavor-dependent-cusp-shape.md),
   [complex-fibre cross-ratio](2026-06-01-complex-fibre-cross-ratio.md)),
   which can pick a distinguished vector that branching alone cannot.
2. **Native-5-strand baryon.** The 3-strand Borromean is a
   Markov-shadow and $h^4$ lives natively at $n=5$, so there is no
   vertical map to construct
   ([fiber-action audit](2026-06-01-s5-so3-su2-u1-fiber-action.md),
   [knot-operator census](2026-06-01-knot-operator-census-group-actions.md)).

A third, narrower lead from the linked-channel work: a **second
independent crossing/trace invariant** carrying baryon number
([inter-nucleon linked channel](2026-06-01-inter-nucleon-linked-channel.md)).

## Action items

- [ ] Both escapes are *derivations to attempt*, not fits — any section
      must be forced by the geometric/holonomy structure or by the
      native-5-strand reframe, never chosen to produce $h^4=-3/4$.
- [ ] The baryon-number (vertical) charge is the joint missing object
      for *both* $Y$ and the 5↔3 section — a single derivation target.
- [ ] No production wiring: this synthesis records structure, changes no
      observable. L1/L2 dashboards unaffected.

## References (all merged on main)

- [`2026-06-01-complex-fibre-cross-ratio.md`](2026-06-01-complex-fibre-cross-ratio.md)
- [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
- [`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md)
- [`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md)
- [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md)
- [`2026-06-02-lepton-t2n-torus-tower.md`](2026-06-02-lepton-t2n-torus-tower.md)
- [`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md)
- [`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md)
- [`2026-06-02-su2-spinor-multiplicity-resolution.md`](2026-06-02-su2-spinor-multiplicity-resolution.md)
