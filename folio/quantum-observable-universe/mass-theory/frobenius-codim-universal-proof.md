**Proof.**
*Since $p_\lambda$ is central and primitive in $Z(A)$, and each
$p_\lambda$ is $\tau$-dual to itself up to the scalar
$\tau(p_\lambda)$, linearity of $\tau$ gives*

$$
  \tau(C_{\dim_q})
  \;=\;
  \sum_\lambda \frac{1}{\dim_q(\lambda) \cdot \tau(p_\lambda)}
    \cdot \tau(p_\lambda)
  \;=\;
  \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$

*$\square$*

**$C_{\dim_q}$ is not forced by its trace.**
*An earlier version claimed that $C_{\dim_q}$ is the unique central element with trace $\sum_\lambda 1/\dim_q(\lambda)$. That is false whenever $A$ has at least two blocks: $\tau$ is one linear functional on $Z(A)$, which has dimension $|\widehat{A}| = p(n) \geq 2$ for $n \geq 2$, so every $z = \sum_\lambda c_\lambda p_\lambda$ with $\sum_\lambda c_\lambda\,\tau(p_\lambda) = \sum_\lambda 1/\dim_q(\lambda)$ has the same trace. The coefficients $c_\lambda = 1/(\dim_q(\lambda)\,\tau(p_\lambda))$ are a choice, not a consequence.*

*$C_{\dim_q}$ is categorical in three distinct senses:*

1. *The Frobenius pairing $\tau \colon A \otimes A \to \mathbb{C}$
   is a morphism in the :refterm[monoidal category]{#monoidal-category} of $A$-bimodules;
   $C_{\dim_q}$ is built from it by universal constructions
   (central idempotents + duality).*
2. *The $q$-dimension $\dim_q(\lambda)$ is the categorical
   **quantum trace** of the identity on the simple module
   $V_\lambda$ — intrinsic to a ribbon-category / rigid-monoidal
   structure.*
3. *In the equivalence between Frobenius algebras and 2D TQFTs
   (Atiyah–Segal / Abrams 1996 / Kock 2004 §2), every element of
   $A$ corresponds to a decorated 2-cobordism.  The standard
   Casimir $\Omega = \sum e_i \cdot e^i$ corresponds to the
   **torus with puncture**; $C_{\dim_q}$ corresponds to the torus
   with a **$\dim_q$-labelled puncture**, i.e., the torus twisted
   by the ribbon-category structure.*

**TQFT / handle-element interpretation.**
*For a 2-dimensional TQFT with state-space $A$, the
**handle element** of the torus-with-one-puncture is
$\mathrm{HE}_A := \sum_\lambda p_\lambda / \tau(p_\lambda)$
and its trace $\tau(\mathrm{HE}_A) = \sum_\lambda d_\lambda$
(classical-dimension sum, e.g., the number of involutions for
$A = H_n(R, q)$).  The element $C_{\dim_q}$ is the **quantum
refinement** of the handle: an additional factor $1/\dim_q(\lambda)$
per block rescales by the block's quantum dimension rather than
its classical one.*

*In Reshetikhin–Turaev language: if the MTC associated with $A$
has $S$-matrix $S_{\lambda\mu}$, then
$\tau(C_{\dim_q}) = S_{\mathbf{1}, \mathbf{0}}^{-1}
\cdot \sum_\lambda \dim_q(\lambda)^{-1}$ (modulo normalisation),
which is a reciprocal of the global dimension weighted by
self-duality.*

**Specialisations.**

1. *$A = H_n(R, q)$ with Markov trace $\tau = \mathrm{tr}_M$,
   $\dim_q = q$-hook-length dimension.
   $\widehat{A} = \{\lambda \vdash n\}$.  Then
   $\mathrm{tr}_M(C_{\dim_q}) = \sum_{\lambda \vdash n}
   1/\dim_q(\lambda)$.
   At $n = 3$: $= 2 + 1/[2]_q$.*
2. *$A = $ Temperley–Lieb $\mathrm{TL}_n(q)$ with Markov trace.
   $\widehat{A} = \{\text{Jones–Wenzl idempotents}\}$.  The
   co-Casimir trace is a $q$-weighted sum over Jones–Wenzl
   blocks.*
3. *$A = $ group algebra $\mathbb{C}[G]$ with $\tau = $ uniform
   (Haar) trace.  $\dim_q = \dim$ (classical). Then
   $\tau(C_{\dim_q}) = \sum_\lambda 1/\dim(\lambda)$, the
   **reciprocal-dimension character sum** — a known group-theoretic
   invariant related to the number of conjugacy classes via the
   first-orthogonality identity.*

**GB-filtration (confinement) decomposition.**
*When $A = H_n(R, q)$ is filtered by the confinement filtration
$J^\bullet(q)$
([confinement level](#def:confinement-level)), the partitions
$\lambda$ sort by level
$\ell(\lambda) = \mathrm{height}(\lambda) - 1$.  The Frobenius
co-Casimir trace decomposes*

$$
  \tau(C_{\dim_q})
  \;=\;
  \sum_{\ell = 0}^{n-1} \;
    \sum_{\lambda :\; \ell(\lambda) = \ell}
      \frac{1}{\dim_q(\lambda)},
$$

*with the self-dual pairing under Young-diagram transpose
($\lambda \leftrightarrow \lambda'$) identifying level $\ell$
with level $n - 1 - \ell$.  Each self-dual pair contributes an
**equal** $1/\dim_q$ value (since $\dim_q(\lambda) = \dim_q(\lambda')$
for any $q$).  At the extremes $\ell = 0$ and $\ell = n-1$:*

$$
  \dim_q\bigl((n)\bigr) \;=\; 1 \;=\; \dim_q\bigl((1^n)\bigr),
$$

*so, when both blocks are included, levels $0$ and $n-1$ contribute exactly $1$ each, giving
the bound*

$$
  \tau(C_{\dim_q}) \;\geq\; 2 \qquad \text{for all } n \geq 1.
$$

*Middle levels carry all the $q$-dependence.  For $n = 3$ only
one middle level exists (level $1$, $\lambda = (2,1)$), giving
$\tau(C_{\dim_q}) = 2 + 1/[2]_q$ when every block is included.
Under convention D the block $(1^n)$ has $\tau(p_{(1^n)}) = 0$ for $n \geq 3$
and must be dropped, so the bound $\geq 2$ does not hold there; at $n = 3$
the sum over $\widehat{A}^{\circ} = \{(3), (2,1)\}$ is $1 + 1/[2]_q$.*

**Independence of the vortex $\varrho$.**
*$\tau(C_{\dim_q}^{(A)})$ is **independent of the
specific vortex $\varrho$** — it depends only on the algebra
$A$ (equivalently on $n$ and $q$), not on the braid word
$\sigma_w$ representing $\varrho$.  This is both a **feature** and a
**limitation**:*

* *Feature (universality):* *Every vortex on $H_3(R, q)$ —
  proton $(uud)$, neutron $(udd)$, any nucleon-like trefoil —
  inherits the same additive offset, $(2 + 1/[2]_q) \cdot m_e$ with
  every block included (not available under convention D, see above).  Mass differences between nucleons come entirely
  from the descended $|\mathrm{tr}_M|$ and brane-tower pieces,
  not from the Frobenius correction.*
* *Limitation (vortex-blind):* *The Frobenius correction cannot
  by itself distinguish $\varrho_{\mathfrak{p}}$ from
  $\varrho_{\mathfrak{n}}$ or any other trefoil-like vortex.
  Vortex-dependent corrections — e.g. chirality factors
  $\{1+h, 1-h^2, (1-h^2)^2\}$ per
  ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
  or knot-factor Frobenius pairings per
  ([knot-factor Frobenius pairing](#conj:knot-factor-frobenius-pairing))
  — are separate structural terms beyond $\tau(C_{\dim_q})$.*

*The unified mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) therefore has
three tiers:*

1. *Vortex-specific: descended $|\mathrm{tr}_M(\sigma_w)|$ and brane
   tower $\sum \Phi_q$.*
2. *Algebra-specific (but vortex-independent): Frobenius
   co-Casimir $\tau(C_{\dim_q}^{(A)})$.*
3. *Isotope-specific (vortex-dependent but structural):
   chirality / knot-factor coefficients from
   the six-term mass formula
   ([six-term mass formula](#thm:six-term-mass-formula-complete)).*

**Consistency.**

1. *At $q = 1$ (classical limit): $\dim_q \to d_\lambda$ and
   $\tau(p_\lambda) \to d_\lambda^2/|G|$ (normalised group-algebra trace), so
   $C_{\dim_q}$ reduces to $\sum_\lambda |G|/d_\lambda^3 \cdot p_\lambda$
   and its trace is $\sum_\lambda 1/d_\lambda$ — the classical
   reciprocal-dimension sum.*
2. *In the "single-vortex" case $A = H_3(R, q)$, three blocks
   $\{(3), (2,1), (1,1,1)\}$ with $q$-dims $\{1, [2]_q, 1\}$
   give $\tau(C_{\dim_q}) = 2 + 1/[2]_q$ when all three blocks are
   included. Under convention D, $\tau(p_{(1,1,1)}) = 0$, so the
   $(1,1,1)$ term is undefined and the sum over the surviving blocks
   is $1 + 1/[2]_q$.*
3. *The self-duality $\lambda \leftrightarrow \lambda'$ is the
   **categorical shadow** of the Young-diagram transpose
   symmetry of the Hecke algebra, which in turn descends from
   the Hecke relation $\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$ admitting
   two eigenvalues $(q, -q^{-1})$ — the source of all
   $q$-deformation structure in the paper.*

## Explicit closed forms by partition count $n$

For each $n$, the Frobenius co-Casimir trace
$\tau(C_{\dim_q}^{(n)}) = \sum_{\lambda \vdash n} 1/\dim_q(\lambda)$
admits an explicit closed form by enumerating the $p(n)$ partitions
once $\dim_q(\lambda)$ is written out for each partition. The convention used throughout is the **quantum
hook-length formula** $\dim_q(\lambda) = [n]_q!\,/\,\prod_{x \in \lambda} [h_x]_q$,
which reduces to the classical $S_n$-irrep dimension at $q = 1$.

The closed forms established so far:

| $n$ | $p(n)$ | conj. pairs | self-conj. | nucleus covered |
|----:|-------:|------------:|-----------:|-------------------|
| $3$ | $3$ | $1$ | $1$ ((2,1)) | $\mathfrak{p}, \mathfrak{n}$ (single-vortex) |
| $6$ | $11$ | $5$ | $1$ ((3,2,1)) | ${}^{4}$He (H_{12} block; ) |
| $7$ | $15$ | $7$ | $1$ ((4,2,1)) | A $\ge$ 5 nuclei |
| $8$ | $22$ | $10$ | $2$ ((4,2,1,1), (3,3,2)) | ${}^4$He / ${}^{16}$O / ${}^{20}$Ne |

Each closed form follows the same scheme: (i) the sum over the
$p(n)$ partitions is split into its summands; (ii) each
$\dim_q(\lambda)$ is unfolded to its product-of-$q$-integers form;
(iii) the trace identity is verified by direct algebraic
simplification after the conjugate-pair grouping.

The $n = 8$ closed form involves partitions whose hook-product
cancellation against $[8]_q!$ leaves residual $/[2]_q$ factors
(specifically (5,1,1,1), (4,4), (4,1,1,1,1), (2,2,2,2)). These
appear as factors $(q + q^{-1})^{-1}$ in the explicit $\dim_q$
expressions. Self-conjugates at $n = 8$ are (4,2,1,1) and (3,3,2).

Beyond $n = 8$, the same scheme extends to $n = 9$
(partitions of $9$, $p(9) = 30$, needed for triton and ${}^{3}$He at
$H_9$) and $n = 12$ ($p(12) = 77$, needed for ${}^{4}$He's $H_{12}$
substrate when not yet decomposed). The bottleneck above $n = 8$
is the size of the explicit $\dim_q$ table rather than the proof
scheme.
