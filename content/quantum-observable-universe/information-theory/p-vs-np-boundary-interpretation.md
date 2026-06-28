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
