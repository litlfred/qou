**Conjecture (GS-depth $\leftrightarrow$ Goncharov period-depth correspondence).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)) and let
$G(\mathcal{H}_q)$ be its sub-Hopf-algebra of grouplikes. Filter
$G(\mathcal{H}_q)$ by **iterated-integral depth**:*

$$
  G^{(0)} \;\subseteq\; G^{(1)} \;\subseteq\; G^{(2)} \;\subseteq\; \cdots,
  \qquad
  G^{(n)} \;:=\; \langle\, \exp_q,\, \log_q,\, \mathrm{Li}_2^q,\, \ldots,\, \mathrm{Li}_n^q \,\rangle.
$$

*Let $\tau_{\mathrm{arch}}$ be the archimedean realization functor
([archimedean realization](#def:archimedean-realization-functor)) and
let $\mathcal{P}_\bullet \subset \mathbb{R}$ be Goncharov's period
filtration on the algebra of (real) periods. Then:*

$$
  \boxed{\;\tau_{\mathrm{arch}}\!\left( G^{(n)}(\mathcal{H}_q) \right)
         \;\subseteq\; \mathcal{P}_n,\;}
$$

*and the inclusion is sharp at every depth — for each $n \geq 1$
there exists a grouplike $g \in G^{(n)} \setminus G^{(n-1)}$ whose
$\tau_{\mathrm{arch}}$-image generates a non-trivial class in
$\mathcal{P}_n / \mathcal{P}_{n-1}$.*

### Stratification dictionary

| Depth $n$ | Grouplike at depth $n$ | Goncharov class |
|---|---|---|
| 0 | $\exp_q$, scalars | algebraic numbers |
| 1 | $\log_q$ | $\log\alpha$, $\alpha \in \overline{\mathbb{Q}}$ (Baker class) |
| 2 | $\mathrm{Li}_2^q$ | hyperbolic 3-mfld volumes (Bloch–Wigner regulator) |
| $n$ | $\mathrm{Li}_n^q$ | weight-$n$ multiple polylogs (Goncharov motivic) |

### Structural content of the statement

The classical Mikusiński operational calculus on $C[0,\infty)$ takes
$f * g \mapsto \tilde f \cdot \tilde g$ under Laplace, turning ODEs
into algebra. The categorical analog already in this paper —
[`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique),
[`q-resolvent`](#def:q-resolvent) — does exactly this for $\mathcal{H}_q$.
What it does *not* yet pin down is **which algebraic relations on
$\mathcal{H}_q$ survive $\tau_{\mathrm{arch}}$ and which do not**. The
present conjecture supplies the structural answer:

- A relation $R(g_1,\dots,g_m) = 0$ among grouplikes survives
  $\tau_{\mathrm{arch}}$ iff *all $g_i$ live in the same depth $G^{(n)}$
  and the relation is an algebraic identity in the cellular structure of
  $H_n(q)$* (provable over $\mathbb{Z}[q^{\pm 1}]$).
- A relation that crosses depth or invokes a transcendental
  identity among periods (e.g. the Bloch–Wigner 5-term relation,
  hyperbolic gluing equations) is an **archimedean accident** — it
  holds only in $\mathbb{R}$, not over $\mathcal{H}_q$ generically.

This is the wall-crossing criterion: depth determines what survives.

### Surreal envelope

Lift the standard-part map $\mathrm{std} \colon \mathbf{No} \to \mathbb{R}$
to the level of grouplikes. The depth filtration extends:

$$
  G^{(n)}(\mathcal{H}_q^{\,\mathbf{No}})
  \;\xrightarrow{\;\mathrm{std}\;}\;
  \mathcal{P}_n.
$$

Surreal infinitesimals $1/\omega^k$ sit at depth $k$ as *literal*
infinitesimal scaling factors — there is no recourse to distributions
or limits. The "delta at depth $n$" of graded Mikusiński is the
surreal element $1/\omega^n$, and $\mathrm{std}$ collapses each layer
to its archimedean image. This makes the *algebraic core survives*
mechanism ([algebraic core survives](#rem:algebraic-core-survives))
into a quantitative statement: it survives **at the depth at which it
lives**.

### Existing depth-2 evidence

The paper already records a depth-2 instance in
[`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration):
the figure-8 knot, embedded in Bring's surface, has hyperbolic
volume $2\,\mathrm{Cl}_2(\pi/3) = 2\,\mathrm{Im}\,\mathrm{Li}_2(e^{i\pi/3})$.
One $\mathrm{Li}_2$ factor $\Rightarrow$ iterated-integral depth $2$,
matching the Bloch-regulator class of the archimedean image. See the
explicit canonical witness in
[`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness).

### Discharge targets

**Open.** The conjecture is structural (no concrete computation
suffices to discharge it), but admits a clean reduction to known
period theory:

1. **Inclusion $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$:**
   reduces to showing $\tau_{\mathrm{arch}}$ commutes with iterated
   integration; for the categorical Laplace transform this is the
   monoidality result already proved
   ([`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique)).
2. **Sharpness ($\mathcal{P}_n / \mathcal{P}_{n-1}$ non-trivial in
   image):** depth-2 case is the Bloch–Wigner regulator
   ([bloch2000], [suslin1991]) realised by hyperbolic 3-manifolds.
   Higher depths reduce to Goncharov's motivic-Galois action on
   multiple polylogs ([kontsevich1995], Goncharov 2001).

**Two related open questions:**

- *Cellular vs iterated-integral depth.* The cellular GB-depth on
  $Z(H_n(q))$ — attributed here to
  [`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification),
  though **that proposition stratifies by the curvature rank of *words* and
  mentions no partition**; the max-hook statistic is
  `QOU.BraidKnot.gbDepth`, a definition, and the step joining them is
  unestablished (see
  [`docs/audits/2026-08-16-three-gb-filtrations-one-name.md`](../../../docs/audits/2026-08-16-three-gb-filtrations-one-name.md))
  — (max hook of partition) is a **separate** filtration from the
  iterated-integral depth used here. Their precise relationship —
  e.g. whether amphichiral self-conjugate cells correspond to
  *even* iterated-integral depths — is open.
- *Graded Titchmarsh.* At which iterated-integral depth does the
  $*_q$-product on $\mathcal{H}_q$ first acquire zero divisors?
  This bounds where the graded field-of-fractions tower
  $\mathcal{M}_q^{(0)} \hookrightarrow \mathcal{M}_q^{(1)} \hookrightarrow \cdots$
  is well-defined, and feeds the operational-calculus mechanism
  per the Mikusiński (1959) construction.
