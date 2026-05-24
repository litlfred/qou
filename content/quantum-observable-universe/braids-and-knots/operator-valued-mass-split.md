The HOMFLYPT polynomial of the Borromean proton braid
$(\sigma_1 \sigma_2^{-1})^3$ equals the HOMFLYPT of the mirror
neutron braid $(\sigma_1^{-1} \sigma_2)^3$ at every SU($N$)
specialisation ($N = 2, 3, \ldots$). This is not a numerical
accident: the Borromean rings are *amphicheiral* — the link
type is topologically equivalent to its mirror image.

The proton/neutron mass split therefore **cannot** come from any
topological invariant (HOMFLYPT, Jones, Alexander, Khovanov, or
any other knot/link polynomial). It must come from the
**operator-valued crossing convention** — the averaged crossings
$I = \sigma - (h/2) \cdot 1$ in the canonical pipeline braids,
whose coefficients encode quark-flavour content (uud vs udd).

This separates the mass-formula derivation into two structural
layers:

| Layer | Source | Invariant type | What it determines |
|---|---|---|---|
| **Topological** | Braid closure / link type | HOMFLYPT $P(K; a, z)$ | Particle *family* (all baryons share Borromean topology) |
| **Operator-valued** | Averaged crossings $I_{\mathrm{flavour}}$ | Markov trace $\operatorname{tr}_M(\beta_{\mathrm{op}})$ | Individual *particle* within the family (proton vs neutron) |

The mass split $\Delta m = m_n - m_p$ lives entirely in the
operator-valued layer. The topological layer contributes a
common baseline (the Borromean-link HOMFLYPT value at each SU($N$)
channel) that is identical for proton and neutron.

## Precedents in the literature

Three independent lines of work provide relevant precedent.
**Note on proof status**: this paper distinguishes sharply between
*mathematical theorems* (rigorous, Lean-formalizable) and
*physical proposals* (models, analogies, numerical fits). The
precedents below are classified accordingly.

### 1. Bilson-Thompson helon model \cite{bilsonthompson2005} — *physical proposal, not a proof*

Bilson-Thompson proposed (without rigorous proof) that Standard
Model fermions are braided ribbons in which the **twist** on each
strand (not the braid topology) encodes electric charge. In this
model, proton and neutron share the same 3-strand braid topology
but differ by the twist assignment on individual strands. The
extension to loop
quantum gravity \cite{bilsonthompson2007} showed that these braids
can be embedded as spin-network edges, with twist corresponding
to a local holonomy.

**Connection to QOU:** the QOU averaged crossing
$I = \sigma - (h/2) \cdot 1$ plays the role of
Bilson-Thompson's twist — it is the operator-valued decoration
that breaks the amphicheirality and distinguishes particles within
a family. The QOU construction is more algebraically precise
(the decoration is a specific element of the Hecke algebra $H_n(q)$,
not an ad-hoc twist), and the mass formula
$\mathfrak{m}_K = m_e \cdot \rho_K \cdot |\operatorname{tr}_M(\beta_K)|$
gives quantitative predictions where the helon model gives only
qualitative charge assignments.

**Precision-gap insight from this precedent:** Bilson-Thompson's
model does not predict *masses* (only charge/generation quantum
numbers). The QOU framework's advantage is that the Hecke algebra
provides a COMPUTABLE mass formula. However, the helon model's
insight that the decoration should respect a local symmetry
(twist = local holonomy) suggests that the QOU averaged-crossing
coefficients should be derivable from a local gauge principle —
this is the content of
[`conj:canonical-knot-id-sdp`](#conj:canonical-knot-id-sdp) (the
SDP uniqueness conjecture). Closing this conjecture would promote
the averaged-crossing convention from empirical to derived.

### 2. Reshetikhin-Turaev colored invariants \cite{reshetikhin1991} — *rigorous mathematics*

Reshetikhin and Turaev gave a mathematically rigorous construction
of link invariants from representations of quantum groups
$U_q(\mathfrak{g})$ (this IS a theorem, not a physical claim). In the
colored Jones polynomial, each strand carries a *representation*
(color) $V_i$, and the invariant $J_K^{(V_1, \ldots, V_n)}(q)$
depends on the color assignment. Different colors on different
strands give different invariants for the same braid topology.

**Connection to QOU:** the mass endomorphism tower
([`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower))
decomposes the Markov trace through the Wedderburn structure
$\operatorname{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$.
Each partition $\lambda \vdash n$ labels an irreducible
representation of $H_n(q) \cong \bigoplus_\lambda \mathrm{End}(V_\lambda)$.
The per-partition contribution $y_\lambda \cdot \chi_\lambda(\beta)$
IS a colored invariant in the Reshetikhin-Turaev sense — it
is the trace of the braid's image in the irrep $V_\lambda$,
weighted by the Markov weight $y_\lambda$.

The HOMFLYPT polynomial at SU($N$) computes a DIFFERENT coloring:
$P(\hat\beta; \mathrm{SU}(N)) = \sum_\lambda s_\lambda(\mathrm{SU}(N))
\cdot \chi_\lambda(\beta) / \dim V_\lambda$ where $s_\lambda$
is the quantum Schur function. So each SU($N$) channel is a
*weighted sum* over the same Wedderburn blocks, with
$N$-dependent weights.

**Precision-gap insight:** the Reshetikhin-Turaev framework
predicts that finer invariants (higher-rank colorings, multi-
colored links) should carry more structural information than the
Jones polynomial alone. In the QOU context, this means:

- **SU(3) evaluation** ($N = 3$, color channel) of the
  operator-valued proton/neutron braids may give a tighter
  $Q_\beta$ predictor than the SU(2)-only Markov trace.
- **Colored Jones at representation $V_\lambda$** for specific
  partitions (e.g. $\lambda = (2,1)$ — the 2-dimensional
  irrep of $H_3$) may isolate the mass-split signal from the
  topological baseline.

Both require implementing the operator-valued HOMFLYPT (averaged
crossings in the Hecke algebra engine) — a follow-up to the
pure-braid engine built in PR #999.

### 3. Quandle invariants \cite{joyce1982}, \cite{matveev1982} — *rigorous mathematics*

A **quandle** $(Q, \triangleright)$ is a set $Q$ with a binary
operation $\triangleright$ satisfying three axioms (Joyce's theorem
that the knot quandle is a complete invariant of oriented prime knots
IS a mathematical theorem with a rigorous proof):

1. $a \triangleright a = a$ for all $a \in Q$ (idempotency).
2. For each $a, b \in Q$ there is a unique $c$ with
   $c \triangleright a = b$ (right-invertibility).
3. $(a \triangleright b) \triangleright c =
   (a \triangleright c) \triangleright (b \triangleright c)$
   (self-distributivity).

These axioms mirror the three Reidemeister moves — a quandle
is precisely the algebraic structure that encodes "crossing
rules" modulo topological equivalence. The **knot quandle**
$Q(K)$ is a complete invariant of oriented prime knots
(Joyce's theorem): two prime knots are ambient isotopic if
and only if their knot quandles are isomorphic.

**Connection to QOU:** the Hecke algebra's quadratic relation
$\sigma_i^2 = (q - 1)\sigma_i + q$ defines a *deformed crossing
rule*. The QOU averaged crossing
$I = \sigma - (h/2) \cdot 1$ is a further deformation that depends
on the quark flavour at the crossing. In the quandle language,
the QOU framework uses a **parameterised quandle** — the
crossing operation $\triangleright$ depends on the strand labels
(quark types), making it a quandle over the flavour group. This
is analogous to the **Alexander quandle** (where
$a \triangleright b = ta + (1-t)b$ for a parameter $t$), but
with the parameter varying per crossing.

**Precision-gap insight:** the quandle framework provides
**counting invariants** (the number of quandle colorings of a
knot diagram) that are strictly finer than the knot polynomial.
For the QOU mass formula, the relevant quandle is the
flavour-parameterised Hecke quandle, and the quandle-coloring
count may encode the number of physically distinct baryonic
states within a given topological class. This has not been
explored — it represents a genuinely new direction for the
mass-tower structure.

## Novelty outside the LQG/physics world

The amphicheirality separation (topology vs operator) has
precedents in **pure mathematics** independent of any physical
application:

- **Vassiliev (finite-type) invariants** decompose knot
  invariants into a graded series where each grade detects a
  different "level" of topological complexity. The QOU operator-
  valued layer is analogous to the **lowest-order Vassiliev
  correction** — it is the first term that distinguishes knots
  that share the same polynomial invariants.

- **Khovanov homology** (2000) categorifies the Jones polynomial
  into a bigraded chain complex. The extra grading (the
  *homological* degree) carries torsion information invisible to
  the Jones polynomial. The QOU operator-valued crossing is a
  DIFFERENT kind of extra data — it lives at the *algebra* level
  (Hecke algebra element), not at the *homological* level. Both
  are examples of "enriching a knot invariant with non-topological
  structure."

- **Knot contact homology** (Ekholm-Etnyre-Sullivan 2005, Ng 2008)
  associates a differential graded algebra (DGA) to a knot, whose
  augmentation variety is a strictly finer invariant than the
  Alexander polynomial. The DGA's differential is an *operator* on
  the algebra — the non-topological enrichment is in the
  differential, not in the braid word.

In all cases, the pattern is the same: a topological invariant
(polynomial, homology group, quandle) captures the *family*, and
an algebraic enrichment (operator, differential, grading, coloring)
captures the *individual*. The QOU contribution is to connect this
algebraic enrichment to a **computable mass formula** — making
the abstract mathematical distinction physically measurable.
