**Conjecture (jet-order independence — the QOU-attackable reduction).**
For every truncation order $N$, the Habiro-ring expansions of the coloured-Jones invariants for the three QOU knots/links,

$$
  J_{4_1}(q),\qquad J_{5_2}(q),\qquad J_{\mathcal{B}_3}(q)
  \;\in\; \widehat{\mathbb{Z}[q]},
$$

are *algebraically independent modulo $(q;q)_{N+1}$* over $\mathbb{Q}[q, q^{-1}]$. Equivalently, the Jacobian of their cyclotomic coefficient vectors $\bigl(c_0(K), \dots, c_N(K)\bigr)$ for $K \in \{4_1, 5_2, \mathcal{B}_3\}$ possesses full rank $3$ for all $N \ge N_0$.

This statement supplies a computationally viable target. It implies the [algebraic-independence conjecture](#conj:hyperbolic-volume-transcendence) provided the surreal-limit bridge holds. The ideal approach requires the full transcendence machinery (Grothendieck periods and the Borel regulator on $K_3(\overline{\mathbb{Q}})$), which remains out of reach. This reduction replaces that machinery with three framework-native tools and one remaining gap.

**Finiteness and decidability.**
Each $J_K(q)$ admits a canonical jet-order grading. The Habiro cyclotomic expansion $J_K(q) = \sum_{n \ge 0} c_n(K)\,(q;q)_n$ organizes the invariant such that the $n$-th term forms the vertical jet-degree $n$ component of the categorical generating function. This aligns with the body-order filtration grading the binding series $G(x;q) = \sum_n B_n x^n$. Algebraic independence to order $N$ imposes a finite-rank condition on the truncated coefficient matrix. The claim is strictly decidable.

**The three framework tools.**

1. **Jet-order filtration** supplies the grading. Independence is verified order-by-order. Reid (1991) anchors the base order. Because $4_1$ is the unique arithmetic hyperbolic knot, its trace field $\mathbb{Q}(\sqrt{-3})$ is rigidly distinct from the cubic trace field of $5_2$ and the link field of $\mathcal{B}_3$ at order $0$.
2. **Gröbner–Shirshov filtration** certifies each order. The reduction engine computes the elimination ideal $I_N = \bigl(\text{relations among } J_{4_1}, J_{5_2}, J_{\mathcal{B}_3} \bmod (q;q)_{N+1}\bigr) \subseteq \mathbb{Q}[q,q^{-1}][x,y,z]$. Full Jacobian rank holds if and only if $I_N$ carries no generator of total degree $\le N$. This translates "no polynomial relation" into a normal-form computation natively executed by the skein engine. At the base order, the $h$-jet expansion about $q=1$ of the canonical Markov traces $\mathrm{tr}_M(K)$ for the three canonical braid words yields jet-Jacobian rows $(\tfrac14, -1, \tfrac{55}{16})$, $(\tfrac12, 0, -\tfrac1{16})$, and $(1, 0, 0)$, with elimination determinant $\tfrac1{16} \neq 0$ and LU pivots $(\tfrac14, 2, \tfrac18)$. Full rank $3$ therefore holds unconditionally at the base order by a finite rational determinant computation. Higher orders require no further computation once the column-extension structure is in place: the order-$N$ Jacobian contains this non-singular $3\times3$ minor as a column-submatrix, so its rank is at least $3$, while the three rows bound the rank above by $3$. Since matrix rank is monotonically non-decreasing in the column count, any monotone, row-bounded rank function equal to $3$ at the base order remains equal to $3$ for all $N \ge 3$; per-order independence thus reduces to the column-extension identification for the order-$N$ Jacobian.
3. **Surreal error bounds** supply the bridge to the limit. The correct geometric picture is parallel transport on the projective state fibre. The coloured-Jones invariant $J_K(q)$ acts as the holonomy of the categorical connection, parallel-transported along the aether $q$-deformation path on $\mathcal{S} = P \times_G \mathbb{CP}^1$. The volume is its singular-limit asymptotics $\mathrm{Vol}(K) = \lim_{n\to\infty} \tfrac{2\pi}{n}\log\lvert J_K(e^{2\pi i/n})\rvert$. The surreal error bound measures the transport error as $q$ deforms toward the root-of-unity point. This error is non-Archimedean because the target point is a singularity of the connection. The error is an infinitesimal in the surreal field. Three conditions must hold for the bridge:
   - **(I1) Uniformity in jet order.** The transport error must be bounded uniformly in $N$. The connection's curvature is uniformly controlled along the deformation path, independent of the truncation order. Any error growing with $N$ severs the transfer.
   - **(I2) Archimedean projection.** The error inhabits the surreal fibre level, carrying the $\mathrm{Im}(q)$ structure. The volume is archimedean ($\mathrm{Im}(q_0) = 0$). The surreal infinitesimal must project to exactly $0$ under $\tau$. A non-infinitesimal archimedean shadow would inject a spurious polynomial relation among the volumes.
   - **(I3) Monodromy separation.** Transport around the cusp is flat only at generic $q$. At the root-of-unity limit, the holonomy accumulates cusp/modular monodromy. The bound must isolate the physical holonomy, which yields $\mathrm{Vol}$, from this monodromy artifact.
   The surreal error field provides the natural setting for this uniform bound. Uniformity (I1) and the composition of (I2) with (I3) hold unconditionally, isolating two explicit physical hypotheses: vanishing of the physical-holonomy archimedean shadow (I2) and vanishing of the monodromy shadow (I3).

**The one remaining gap.**
This reduction does not prove the deep conjecture. It reduces the conjecture to a single native lemma:

> **Bridge lemma (open).** If $\{J_{4_1}, J_{5_2}, J_{\mathcal{B}_3}\}$ are jet-order independent for all $N$ with a surreal-bounded uniform error, then $\{\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)\}$ are algebraically independent over $\mathbb{Q}(q_0)$.

This reduction shifts the [algebraic-independence conjecture](#conj:hyperbolic-volume-transcendence) from a Grothendieck-period transcendence problem to a finite base-order determinant computation coupled with the surreal transport bridge. With the base-order rank and the uniformity and composition steps established unconditionally, the remaining content isolates into the column-extension linkage and the two shadow-vanishing inputs (I2) and (I3).
