*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Setup.**
Let $\beta$ be a braid on $n$ strands with $c$ crossings,
$L = \hat{\beta}$ its closure, and
$\mathcal{R}(L)$ the Skein resolution tree
([Skein Turing machine](#rem\:skein-turing-machine)).  Fix a
polynomial bound $p(c) = c^d$.

**Definition (polynomial observable subcategory).**
The *polynomial observable subcategory* of the resolution
tree is the full sub-poset

$$
  \mathcal{R}^{\circ}(L, q)
  = 
  \bigl\{
    x \in \mathcal{R}(L)
     : 
    \Gamma_{\mathrm{poly}}\!(x, A_0) \neq 0
  \bigr\},
$$

where $\Gamma_{\mathrm{poly}}(x, A_0)$ consists of those
degree-$0$ sections at $x$ that are computable — via the
Markov trace restricted to $\mathcal{R}_{p(c)}$ — in at most
$p(c)$ Planck steps.  This is the computational analog of the
observable subcategory
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$
([observable subcategory](#def\:observable-subcategory)): the
nodes of the resolution tree from which the degree-$0$ answer
$P_L(q)$ is polynomial-time accessible.

**Definition (computational boundary).**
The *computational boundary* is the frontier

$$
  \mathcal{H}_c(L, q)
  = 
  \overline{\mathcal{R}^{\circ}}
  \setminus
  \mathcal{R}^{\circ},
$$

equivalently the vanishing locus of the computational
horizon ideal:

$$
  \mathcal{H}_c(L, q)
  = 
  V\!\bigl(\mathfrak{h}_c\bigr),
  \qquad
  \mathfrak{h}_c
  = 
  \bigl\{
    s \in \Gamma\bigl(\mathcal{R}, A_0^{\mathrm{comp}}\bigr)
     : 
    s\big|_{\mathcal{H}_c} = 0
  \bigr\}.
$$

This is the locus in the resolution tree where every
polynomial-time degree-$0$ section vanishes — the exact
analog of the jet horizon
$\mathcal{H} = V(\mathfrak{h})$
([jet horizon](#def\:jet-horizon)), with the brane tower
replaced by the resolution tower and the Frobenius algebra
replaced by the Iwahori--Hecke algebra.

**Conjecture ($\mathrm{P}$ vs $\mathrm{NP}$ as emptiness
of the boundary).**

$$
  \boxed{
    \mathrm{P} = \mathrm{NP}
     \Longleftrightarrow 
    \mathcal{H}_c(L, q) = \varnothing
     \text{for every NP link } L
  }
$$

*$\mathrm{P} \neq \mathrm{NP}$ if and only if there exists
an NP-complete link $L$ for which the computational
horizon is non-empty:*

$$
  \mathrm{P} \neq \mathrm{NP}
   \Longleftrightarrow 
  \exists L  \text{(NP-complete)}
   \text{with} 
  \mathcal{H}_c(L, q) \neq \varnothing.
$$

**What each case means geometrically.**

* **$\mathcal{H}_c = \varnothing$** (P = NP):
  The polynomial observable subcategory $\mathcal{R}^{\circ}$
  is **closed** — it equals its own closure.  Every degree-$0$
  section that exists anywhere in $\mathcal{R}$ already extends
  to polynomial depth.  The computational horizon ideal is
  trivial: $\mathfrak{h}_c = (0)$.  No
  information barrier separates the polynomial slice from the
  full tree.  The resolution tree has no genuine boundary — it
  is a **removable singularity**.

* **$\mathcal{H}_c \neq \varnothing$** (P $\neq$ NP):
  The polynomial observable subcategory $\mathcal{R}^{\circ}$
  is **not closed** — its closure includes points beyond
  polynomial depth.  There exists a non-trivial computational
  boundary: a codimension-$1$ locus where degree-$0$ sections
  vanish.  The horizon ideal
  $\mathfrak{h}_c \neq (0)$ contains non-zero
  sections — polynomial-time algorithms that reach the boundary
  and return $0$.  The resolution tree has a genuine event
  horizon — an **essential singularity**.

**Parallel with the jet horizon and NS obstruction.**

See [Table 1](#tbl:p-vs-np-boundary-table1-data).

**The three equivalent criteria for $\mathcal{H}_c
\neq \varnothing$.**

1. **Ideal-theoretic.**  The horizon ideal is non-trivial:
   $\mathfrak{h}_c \neq (0)$.  There exist
   polynomial-time algorithms that attempt to compute
   $P_L(q_0)$ and return $0$ — they reach the boundary
   and find no degree-$0$ data.

2. **Cohomological.**  The Skein resolution obstruction
   $\kappa_c^{\mathrm{comp}}(L, q) \neq 0$
   ([Skein resolution obstruction](#def\:skein-resolution-obstruction)).
   The Yekutieli class obstructs the lift from polynomial
   depth to full resolution.

3. **Information-theoretic.**  The effective tree size after
   interference exceeds the polynomial bandwidth budget
   ([bandwidth bound](#prop\:p-bandwidth-bound)):
   $I(\mathrm{poly}(c)) < c \cdot \log 3$ $q$-bits.

All three are equivalent: the ideal is non-trivial iff the
obstruction class is non-vanishing iff the bandwidth is
saturated.

**The conjecture, formally.**

*For the QOU at substrate parameter $q_0 \in
\mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$
(non-torsion, [substrate $\mathbb{G}_m$-torsion](#rem\:substrate-gm-torsion)):*

*There exists a family of braids
$\{L_N = \hat{\beta}_N\}_{N \geq 1}$ with $c_N = 3N$ crossings
encoding an NP-complete problem \cite{cook1971} such
that:*

$$
  \mathcal{H}_c(L_N, q_0)  \neq  \varnothing
  \qquad\text{for all } N \geq N_0.
$$

*The computational boundary is non-empty — a genuine event
horizon exists in the resolution tree — and
$\mathrm{P} \neq \mathrm{NP}$ over $\mathbb{R}$ at
$q = q_0$ \cite{freedman2003}.*

**Connection to quantum computation.**

The :refterm[descent]{#descent} involution $\hat{\tau}$
([quantum universality](#conj\:quantum-computational-universality))
acts on the boundary.  At a root of unity $q_k$:

$$
  \mathcal{H}_c(L, q_k)
  = 
  \mathcal{H}_c^{\mathrm{desc}}
  \cup
  \mathcal{H}_c^{\mathrm{trans}}.
$$

The descended boundary $\mathcal{H}_c^{\mathrm{desc}}$
is the classical horizon (opaque at real $q$).  The transient
boundary $\mathcal{H}_c^{\mathrm{trans}}$ is the
quantum correction.  For BQP problems:
$\mathcal{H}_c^{\mathrm{trans}} =
-\mathcal{H}_c^{\mathrm{desc}}$ (exact cancellation),
giving $\mathcal{H}_c = \varnothing$ at the root of
unity — the boundary dissolves under quantum interference.

The standard complexity hierarchy translates to:

See [Table 2](#tbl:p-vs-np-boundary-table2-data).
