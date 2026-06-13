**Conjecture (jet-order independence — the QOU-attackable reduction).**
For every truncation order $N$, the Habiro-ring expansions of the
coloured-Jones invariants of the three QOU knots/links,

$$
  J_{4_1}(q),\qquad J_{5_2}(q),\qquad J_{\mathcal{B}_3}(q)
  \;\in\; \widehat{\mathbb{Z}[q]} ,
$$

are *algebraically independent modulo $(q;q)_{N+1}$* over
$\mathbb{Q}[q, q^{-1}]$: the Jacobian of their cyclotomic coefficient
vectors $\bigl(c_0(K), \dots, c_N(K)\bigr)$, $K \in \{4_1, 5_2,
\mathcal{B}_3\}$, has full rank $3$ for all $N \ge N_0$.

This is the statement QOU can actually attack, and it implies the deep
[algebraic-independence conjecture](#conj:hyperbolic-volume-transcendence)
*provided* the surreal-limit bridge below holds.  We state the partial
approach explicitly: the ideal would be the full transcendence machinery
(Grothendieck periods, the Borel regulator on $K_3(\overline{\mathbb{Q}})$),
which is out of reach; the reduction replaces that machinery with three
QOU-native tools and one remaining QOU-native gap.

**Why this is a finite, decidable claim.**  Each $J_K(q)$ has a
canonical *jet-order* grading — the Habiro (cyclotomic) expansion
$J_K(q) = \sum_{n \ge 0} c_n(K)\,(q;q)_n$, whose $n$-th term is the
vertical/jet degree-$n$ part of the categorical generating function (the
same body-order filtration that grades the binding series $G(x;q) =
\sum_n B_n x^n$).  Algebraic independence *to order $N$* is a finite-rank
condition on the truncated coefficient matrix, hence decidable.

**The three QOU tools.**

1. **Jet-order filtration** supplies the grading: independence is checked
   order-by-order in $n$, and the base order is anchored by Reid (1991) —
   $4_1$ is the unique *arithmetic* hyperbolic knot, so its trace field
   $\mathbb{Q}(\sqrt{-3})$ is rigidly distinct from the cubic trace field
   of $5_2$ and the link field of $\mathcal{B}_3$ at order $0$.
2. **Gröbner–Shirshov (GB) filtration** *certifies* each order: the
   elimination ideal $I_N = \bigl(\text{relations among } J_{4_1}, J_{5_2},
   J_{\mathcal{B}_3} \bmod (q;q)_{N+1}\bigr) \subseteq
   \mathbb{Q}[q,q^{-1}][x,y,z]$ is computed by the reduction engine; full
   Jacobian rank $\iff I_N$ carries no generator of total degree $\le N$.
   This turns "no polynomial relation" into a normal-form computation the
   skein engine already performs.  The **base-order certificate is
   Lean-formalized sorry-free *and witnessed by the framework's own
   computation***: the h-jet expansion about $q=1$ of the canonical Markov
   traces $\mathrm{tr}_M(K)$ for the three knots' canonical braid words
   gives jet-Jacobian rows $(\tfrac14, -1, \tfrac{55}{16})$,
   $(\tfrac12, 0, -\tfrac1{16})$, $(1, 0, 0)$ with elimination determinant
   $\tfrac1{16} \neq 0$ (LU pivots $(\tfrac14, 2, \tfrac18)$,
   `jetOrder3_certificate`) — so full rank $3$ holds at the Reid-1991 base
   order, a finite decidable determinant test on real data
   (`jet_order_pivots.py` $\to$ `jet-order-pivots.witness.json`).  Higher
   orders then need **no** further computation, by the following
   structural argument: the order-$N$ Jacobian ($3 \times (N+1)$) contains
   this non-singular $3\times3$ minor as a column-submatrix, so its rank is
   $\ge 3$, while the three rows bound it by $3$ — hence rank exactly $3$ at
   *every* $N$ from the base order onward, rank being monotone in the
   column count.  Lean formalizes the **two endpoints** of this argument:
   the base minor is full-rank (`jetJacobianBase_rank`, proved via
   invertibility) and the abstract monotonicity principle
   (`jacobianRank_eq_three_of_base`: any monotone, row-bounded rank
   function equal to $3$ at the base order is $3$ for all $N \ge 3$).  The
   column-extension linkage that discharges the principle's hypotheses for
   the *concrete* order-$N$ Jacobian remains a structural input — per-order
   independence reduces to it rather than to a separate determinant test at
   each truncation.
3. **Surreal error bounds** supply the *bridge* to the limit, and the
   right geometric picture is **parallel transport on the projective
   state fibre**.  The coloured-Jones invariant $J_K(q)$ is the holonomy
   of the categorical (Yekutieli non-abelian Stokes / KZ) connection
   parallel-transported along the substrate $q$-deformation path on
   $\mathcal{S} = P \times_G \mathbb{CP}^1$, and the volume is its
   singular-limit asymptotics
   $\mathrm{Vol}(K) = \lim_{n\to\infty} \tfrac{2\pi}{n}\log\lvert
   J_K(e^{2\pi i/n})\rvert$.  The surreal error bound measures the
   transport error as $q$ deforms toward the root-of-unity point; it is
   surreal (non-Archimedean) precisely because that point is a
   *singularity* of the connection, so the error is an infinitesimal in
   the surreal field rather than a real number.  Three issues must hold
   for the bridge:

   - **(I1) Uniformity in jet order.**  The transport error must be
     bounded *uniformly* in $N$ — equivalently, the connection's
     curvature is uniformly controlled along the deformation path
     independent of the truncation order.  Error growing with $N$ breaks
     the transfer.
   - **(I2) Archimedean projection (the fibre-vs-observable wall).**  The
     error lives at the *fibre* level (surreal, carrying the $\operatorname{Im}(q)$
     structure), while the volume is *archimedean* ($\operatorname{Im}(q_0) = 0$,
     real).  The surreal infinitesimal must project to *exactly* $0$
     under $\tau$; a non-infinitesimal archimedean shadow would inject a
     spurious polynomial relation among the volumes.
   - **(I3) Monodromy separation.**  Transport around the cusp is flat
     only at generic $q$; at the root-of-unity limit the holonomy picks
     up cusp/modular monodromy.  The bound must separate the physical
     holonomy ($\to \mathrm{Vol}$) from the monodromy artifact.

   The surreal-number error field of the framework is the natural home
   for the uniform bound.  The Lean reduction no longer assumes the three
   issues as one monolithic axiom: it splits them, and **(I1) uniformity
   and the (I2)∘(I3) composition are now proved** (`transport_uniform_bound`,
   `transport_shadow_vanishes`).  What remains conjectural is exactly the
   two *physical* inputs — the physical-holonomy shadow vanishes (I2) and
   the monodromy shadow vanishes (I3) — each a named hypothesis rather
   than an opaque single axiom.

**The one remaining gap (stated honestly).**  The reduction is *not* a
proof of the deep conjecture.  It is a reduction of it to a single
QOU-native lemma:

> **Bridge lemma (open).**  If $\{J_{4_1}, J_{5_2}, J_{\mathcal{B}_3}\}$
> are jet-order independent for all $N$ with a surreal-bounded uniform
> error, then $\{\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)\}$
> are algebraically independent over $\mathbb{Q}(q_0)$.

What QOU *buys*: the deep [algebraic-independence
conjecture](#conj:hyperbolic-volume-transcendence) — needed only for
well-definedness of the mass coefficient ring, never for RH/NS/$P\neq
\mathrm{NP}$ — is reduced from a Grothendieck-period transcendence
statement (no path) to a finite per-order GB computation (base order now
Lean-certified) plus the surreal bridge, which is itself split so that
only its two physical inputs (I2)+(I3) remain conjectural — (I1)
uniformity and the composition are proved.  What it *gives up*: those two
inputs are still unproved, so this closes nothing unconditionally — it
converts an external dead end into an internal, incremental research
target on the framework's own filtration, with the base order and the
bridge's structural half already discharged.
