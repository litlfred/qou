Let $(A, \tau)$ be a finite-dimensional semisimple self-dual
Frobenius algebra over $\mathbb{C}$ with non-degenerate symmetric
bilinear form $\tau \colon A \to \mathbb{C}$ and Wedderburn
decomposition

$$
  A \;=\; \bigoplus_{\lambda \in \widehat{A}}
          \mathrm{Mat}_{d_\lambda}(\mathbb{C}),
$$

where $\widehat{A}$ indexes simple blocks and $d_\lambda$ is the
classical dimension of block $B_\lambda$.  Let $p_\lambda \in A$
be the central idempotent of block $\lambda$, and let
$\dim_q(\lambda) \in \mathbb{C}^\times$ denote any non-vanishing
"quantum dimension" function on blocks (e.g., for $A = H_n(q)$
with Markov trace, $\dim_q$ is the $q$-hook-length dimension
giving $\tau(p_\lambda) = \dim_q(\lambda)\, d_\lambda / [n]_q!$).

**Theorem (Frobenius quantum-co-dimension trace).**
*The **quantum-co-dimension element**

$$
  C_{\dim_q}
  \;:=\;
  \sum_{\lambda \in \widehat{A}}
    \frac{1}{\dim_q(\lambda) \cdot \tau(p_\lambda)}
    \cdot p_\lambda
  \;\in\; Z(A)
$$

*lies in the centre of $A$ and satisfies*

$$
  \boxed{
    \tau\bigl(C_{\dim_q}\bigr)
    \;=\;
    \sum_{\lambda \in \widehat{A}} \frac{1}{\dim_q(\lambda)}.
  }
$$

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

**TQFT / handle-element interpretation.**
*For a 2-dimensional TQFT with state-space $A$, the
**handle element** of the torus-with-one-puncture is
$\mathrm{HE}_A := \sum_\lambda p_\lambda / \tau(p_\lambda)$
and its trace $\tau(\mathrm{HE}_A) = \sum_\lambda d_\lambda$
(classical-dimension sum, e.g., the number of involutions for
$A = H_n(q)$).  The element $C_{\dim_q}$ is the **quantum
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

1. *$A = H_n(q)$ with Markov trace $\tau = \mathrm{tr}_M$,
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
*When $A = H_n(q)$ is filtered by the confinement filtration
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

*so levels $0$ and $n-1$ contribute exactly $1$ each, giving
the universal bound*

$$
  \tau(C_{\dim_q}) \;\geq\; 2 \qquad \text{for all } n \geq 1.
$$

*Middle levels carry all the $q$-dependence.  For $n = 3$ only
one middle level exists (level $1$, $\lambda = (2,1)$), giving
$\tau(C_{\dim_q}) = 2 + 1/[2]_q$.*

**Physical content.**
*Any vortex represented on a self-dual Frobenius algebra
$(A, \tau)$ — whether a single nucleon $(A = H_3(q))$, an
isotope $(A = H_{3A}(q))$, or an abstract braid closure — has a
**tower residual** equal to $\tau(C_{\dim_q})$ weighted by the
fibre-functor calibration constant $m_e$:*

$$
  \Delta m_{\text{vortex}}
  \;=\;
  m_e \cdot \tau\bigl(C_{\dim_q}^{(A)}\bigr).
$$

*This is the **universal derivation** of the proton
$(5/2) \cdot m_e$ residual
([proton residual](#prop:partition-sum-proton-residual)) and its
extensions to nuclear bindings.  The specific value
$\tau(C_{\dim_q})$ depends on the algebra $A$ (hence on the
vortex content), but the **structural form** — trace of the
Frobenius co-dimension element — is universal.*

**Consistency.**

1. *At $q = 1$ (classical limit): $\dim_q \to d_\lambda$ and
   $\tau(p_\lambda) \to d_\lambda/|G|$ (group-algebra trace), so
   $C_{\dim_q}$ reduces to $\sum_\lambda |G|/d_\lambda^2 \cdot p_\lambda$
   and its trace is $\sum_\lambda 1/d_\lambda$ — the classical
   reciprocal-dimension sum.*
2. *In the "single-vortex" case $A = H_3(q)$, three blocks
   $\{(3), (2,1), (1,1,1)\}$ with $q$-dims $\{1, [2]_q, 1\}$
   give $\tau(C_{\dim_q}) = 2 + 1/[2]_q$ matching proton
   residual to $0.14\%$ at $q_0 \approx 1.11$.*
3. *The self-duality $\lambda \leftrightarrow \lambda'$ is the
   **categorical shadow** of the Young-diagram transpose
   symmetry of the Hecke algebra, which in turn descends from
   the Hecke relation $T_i^2 = (q - q^{-1}) T_i + 1$ admitting
   two eigenvalues $(q, -q^{-1})$ — the source of all
   $q$-deformation structure in the paper.*
