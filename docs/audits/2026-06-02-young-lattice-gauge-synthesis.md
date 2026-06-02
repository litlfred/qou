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

## Non-fit escapes — both attempted, both CLOSED (2026-06-02)

Representation theory left exactly two non-fit ways past the vertical
obstruction (both named across the audits, then unified). **Both were
computed; both fail — by the same mechanism (separation, not
selection).** The keystone stands.

1. **Native-5-strand baryon (Escape 2) — FALSIFIED**
   ([`2026-06-02-native-5-strand-baryon.md`](2026-06-02-native-5-strand-baryon.md),
   PR #1694). The hypothesis that the 3-strand Borromean $B_3$ is a
   Markov-shadow of a canonical native-5-strand object fails decisively:
   a Brunnian-5 link's proper sublinks are *trivial* (deletion → unlink
   $\neq B_3$), so $B_3$ is not a shadow of any Brunnian-5 object; the
   forced $S_5$-symmetric 5-braid's RAW Markov trace misses
   $z^2\,\mathrm{tr}_M(B_3)$ by **96.5%**; and no $\lambda\vdash 5$ block
   carries $h^4=-3/4$. The obstruction relocates ("no canonical 5-strand
   pre-image of $B_3$") rather than dissolving.

2. **Geometric / icosahedral-holonomy section (Escape 1) — FAILS**
   ([`2026-06-02-escape1-geometric-holonomy-section.md`](2026-06-02-escape1-geometric-holonomy-section.md),
   PR #1699). The mult-2 Hom-space $V=\mathrm{Hom}_{S_3}((2,1),
   \mathrm{Res}^{A_5}_{S_3}(H))\cong\mathbb{C}^2$ was realized
   *explicitly*. A canonical operator on $V$ must come from an $A_5$
   element commuting with / normalizing the $S_3$ color-sheet
   stabilizer, but **$C_{A_5}(S_3)=\{e\}$** (trivial centralizer) and
   **$N_{A_5}(S_3)=S_3$** (self-normalizing). Hence the only forced
   operator is the scalar identity — spectrum $\{1,1\}$, every line
   invariant, **none distinguished**. Geometry *separates* (it produces
   $V=\mathbb{C}^2$ with the OV/JM basis) but does **not select** a
   canonical line; the Bring cross-ratio is a *free modulus* (several
   icosahedral special values), so "the cross-ratio that gives $h^4$"
   would be a fit.

**The delimitation (the result of this arc) — TRIPLE-CONFIRMED.** Three
independent structural selectors were tested on the same $\mathbb{C}^2$
multiplicity space; **all three SEPARATE but do not SELECT** a canonical
line:

| Selector | Result | PR |
|----------|--------|-----|
| **SU(2) spin / ribbon twist** | separates (OV/JM eigenbasis) but the two copies share final spin; no global selector | #1687 |
| **Icosahedral $A_5$ geometry / Bring cross-ratio** | separates but $C_{A_5}(S_3)=\{e\}$, $N=S_3$ ⟹ only forced operator is scalar identity | #1699 |
| **Kashiwara / Option-E crystal (bar-involution)** | separates (per-copy HW vectors) but bar *swaps* the copies (no bar-fixed line); selection lives at the irreducible level, not the multiplicity index | #1703 |

The missing object — the canonical section / vertical baryon-number
charge — is therefore **not derivable from existing categorical
structure** (Hecke branching, OV/JM content-eigenbasis, ribbon-twist
spin, Kashiwara crystal/bar) **nor from existing geometric structure**
(icosahedral $A_5$ holonomy, Bring cross-ratio). It is a **genuine new
physical input**. The keystone obstruction is now fully characterized:
nonexistence (#1684) → sharpened to "no canonical section" (#1687) →
both non-fit *escapes* ruled out (#1694, #1699) → **all three structural
*selectors* ruled out** (#1687, #1699, #1703).

A residual narrower lead (not a structural selector — a candidate
*identity* for the new input itself) is the linked-channel **second
independent crossing/trace invariant** carrying baryon number
([inter-nucleon linked channel](2026-06-01-inter-nucleon-linked-channel.md)).
The Option-E crystal *machinery* still has a live role on a **different**
object — the $\Delta_\lambda$ binding-energy Gram closure (PR #1697) —
which is unaffected by this keystone-selector negative.

## Action items

- [x] Escape 2 (native-5-strand) attempted — **falsified** (#1694).
- [x] Escape 1 (geometric/holonomy section) attempted — **fails**
      (#1699); no forced non-scalar operator on the $\mathbb{C}^2$
      multiplicity space.
- [ ] The baryon-number (vertical) charge is the joint missing object
      for *both* $Y$ and the 5↔3 section — and is now established to be a
      **genuine new physical input**, not derivable from existing
      categorical or geometric structure. Any future closure must
      introduce that input explicitly (e.g. an additional substrate
      datum), never fit a selector to produce $h^4=-3/4$.
- [x] Crystal selector (Kashiwara / Option-E bar-involution) tested —
      **separates but does not select** (#1703); the bar swaps the two
      copies with no fixed line. Third and final structural selector;
      all three (spin, geometry, crystal) now ruled out. (The Option-E
      crystal *machinery* remains live for the separate $\Delta_\lambda$
      Gram closure, PR #1697 — a different object.)
- [x] No production wiring: this synthesis records structure, changes no
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
