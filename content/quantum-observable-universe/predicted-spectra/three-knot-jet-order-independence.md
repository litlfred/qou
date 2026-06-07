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
   skein engine already performs.
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
   for the uniform bound; the Lean reduction axiomatises (I1)+(I2)+(I3)
   as the single vanishing-shadow input of the bridge class.

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
statement (no path) to a finite per-order GB computation (QOU runs it)
plus the surreal bridge lemma above (QOU-native, still open).  What it
*gives up*: the bridge lemma is itself unproved, so this closes nothing
unconditionally — it converts an external dead end into an internal,
incremental research target on the framework's own filtration.
