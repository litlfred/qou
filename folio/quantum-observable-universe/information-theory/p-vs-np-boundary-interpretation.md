**Geometric meaning of each case.**

* **$\mathcal{H}_c = \varnothing$** (P = NP): The polynomial observable subcategory $\mathcal{R}^{\circ}$ is closed. Every degree-$0$ section existing in $\mathcal{R}$ already extends to polynomial depth. The computational horizon ideal vanishes: $\mathfrak{h}_c = (0)$. No information barrier separates the polynomial slice from the full tree. The resolution tree exhibits no genuine boundary; it harbors a removable singularity.
* **$\mathcal{H}_c \neq \varnothing$** (P $\neq$ NP): The polynomial observable subcategory $\mathcal{R}^{\circ}$ is not closed. A non-trivial computational boundary manifests as a codimension-$1$ locus where degree-$0$ sections vanish. The horizon ideal $\mathfrak{h}_c \neq (0)$ captures polynomial-time algorithms that reach the boundary and return $0$. The resolution tree exhibits a genuine event horizon, forming an essential singularity.

**Parallel with the jet horizon and NS obstruction.**
See [the horizon-boundary comparison table](#tbl:p-vs-np-boundary-table1-data).

**The three equivalent criteria for $\mathcal{H}_c \neq \varnothing$.**

1. **Ideal-theoretic.** The horizon ideal is non-trivial: $\mathfrak{h}_c \neq (0)$. Polynomial-time algorithms evaluate to $0$ on the boundary.
2. **Cohomological.** The Skein resolution obstruction class does not vanish: $\kappa_c^{\mathrm{comp}}(L, q) \neq 0$. This class obstructs the lift from polynomial depth to full resolution.
3. **Information-theoretic.** The effective tree size, after interference, strictly exceeds the polynomial bandwidth budget: $I(\mathrm{poly}(c)) < c \cdot \log 3$ $q$-bits.

**Connection to quantum computation.**
The descent involution $\hat{\tau}$ acts directly on the boundary. At a root of unity $q_k$:
$$
  \mathcal{H}_c(L, q_k) = \mathcal{H}_c^{\mathrm{desc}} \cup \mathcal{H}_c^{\mathrm{trans}}.
$$
The descended boundary $\mathcal{H}_c^{\mathrm{desc}}$ constitutes the classical horizon, remaining opaque at real $q$. The transient boundary $\mathcal{H}_c^{\mathrm{trans}}$ supplies the quantum correction. For BQP problems, exact cancellation occurs: $\mathcal{H}_c^{\mathrm{trans}} = -\mathcal{H}_c^{\mathrm{desc}}$. This yields $\mathcal{H}_c = \varnothing$ at the root of unity. The boundary completely dissolves under quantum interference.

The standard complexity hierarchy translates to:
See [the complexity-regime table](#tbl:p-vs-np-boundary-table2-data).
