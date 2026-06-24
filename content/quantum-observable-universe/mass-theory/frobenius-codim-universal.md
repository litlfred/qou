*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Preliminaries.**

* **$\widehat{A}$**: the **isomorphism-class index set of simple
  $A$-modules** — equivalently, the indexing set of Wedderburn
  blocks of a finite-dim semisimple algebra $A$.  Standard
  representation-theory notation (analogous to $\widehat{G}$ for
  the unitary dual of a group).  For $A = H_n(R, q)$,
  $\widehat{A} = \{\lambda \vdash n\}$ (partitions of $n$).

* **Vortex**: a morphism $\varrho \colon \mathbf{1} \to A$ in the
  rigid :refterm[monoidal category]{#monoidal-category} of the quantum observable universe —
  i.e., a closed element of $A$ arising as the closure of a braid
  $\beta \in B_n$
  ([Hecke mass element](#def\:hecke-mass-element)).  Each vortex has
  a Hecke-algebra representative $\sigma_w \in H_n(R, q)$ whose Markov
  trace is the categorical mass
  ([categorical mass, Markov](#prop\:categorical-mass-markov)).
  In physics: particles (quarks, nucleons, nuclei) are vortices.

* **$C_{\dim_q}$**: the "C" stands for **Casimir** (Lie-algebra /
  TQFT terminology); "co-" because it is the Frobenius-pairing
  dual of the unit $1 = \sum_\lambda p_\lambda$, **not** the
  standard quadratic Casimir $\Omega = \sum_i e_i \otimes e^i$.
  See §"Why $C_{\dim_q}$ and not something else?" below.

**Setup.**
Let $(A, \tau)$ be a finite-dimensional semisimple self-dual
Frobenius algebra over $\mathbb{C}$ with non-degenerate symmetric
bilinear form $\tau \colon A \to \mathbb{C}$ and Wedderburn
decomposition

$$
  A \;=\; \bigoplus_{\lambda \in \widehat{A}}
          \mathrm{Mat}_{d_\lambda}(\mathbb{C}),
$$

where $d_\lambda$ is the classical dimension of block $B_\lambda$.
Let $p_\lambda \in A$ be the central idempotent of block $\lambda$,
and let $\dim_q(\lambda) \in \mathbb{C}^\times$ denote any
non-vanishing "quantum dimension" function on blocks (e.g., for
$A = H_n(R, q)$ with Markov trace, $\dim_q$ is the $q$-hook-length
dimension giving $\tau(p_\lambda) = \dim_q(\lambda) \, d_\lambda
/ [n]_q!$).

**Theorem (Frobenius quantum-co-dimension trace).**
\*The **quantum-co-dimension element**

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

*

**Why $C_{\dim_q}$ and not some other element? (categorical + unique)**

*Two answers.  **Uniqueness**: the map
$Z(A) \ni z \mapsto \tau(z) \in \mathbb{C}$ is a linear functional
on the centre.  By non-degeneracy of $\tau$ on $Z(A)$ (which
holds iff the Frobenius form restricts non-degenerately to the
centre — true for any semisimple Frobenius algebra), the element
$z \in Z(A)$ with $\tau(z) = \sum_\lambda 1/\dim_q(\lambda)$ is
**unique**.  Writing $z = \sum_\lambda c_\lambda p_\lambda$ and
matching $\tau(z) = \sum c_\lambda \cdot \tau(p_\lambda)$ to
$\sum 1/\dim_q$ forces $c_\lambda = 1/(\dim_q(\lambda)\,\tau(p_\lambda))$
— this **is** the definition of $C_{\dim_q}$.  The element is
therefore **forced by the structure**, not ad-hoc.*

*$C_{\dim_q}$ is categorical in three distinct senses:*

1. *The Frobenius pairing $\tau \colon A \otimes A \to \mathbb{C}$
   is a morphism in the :refterm[monoidal category]{#monoidal-category} of $A$-bimodules;
   $C_{\dim_q}$ is built from it by universal constructions
   (central idempotents + duality).*
2. *The $q$-dimension $\dim_q(\lambda)$ is the categorical
   **quantum trace** of the identity on the simple module
   $V_\lambda$ — intrinsic to a ribbon-category / rigid-monoidal
   structure, not a choice.*
3. *In the equivalence between Frobenius algebras and 2D TQFTs
   (Atiyah–Segal / Abrams 1996 / Kock 2004 §2), every element of
   $A$ corresponds to a decorated 2-cobordism.  The standard
   Casimir $\Omega = \sum e_i \cdot e^i$ corresponds to the
   **torus with puncture**; $C_{\dim_q}$ corresponds to the torus
   with a **$\dim_q$-labelled puncture**, i.e., the torus twisted
   by the ribbon-category structure.*

*So the element is required (unique) and its construction is
purely categorical — no arbitrary choices.*

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
([confinement level](#def\:confinement-level)), the partitions
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
$(A, \tau)$ — whether a single nucleon $(A = H_3(R, q))$, an
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
([proton residual](#prop\:partition-sum-proton-residual)) and its
extensions to nuclear bindings.  The specific value
$\tau(C_{\dim_q})$ depends on the algebra $A$ (hence on the
vortex content), but the **structural form** — trace of the
Frobenius co-dimension element — is universal.*

**Independence of the vortex $\varrho$.**
*Critically, $\tau(C_{\dim_q}^{(A)})$ is **independent of the
specific vortex $\varrho$** — it depends only on the algebra
$A$ (equivalently on $n$ and $q$), not on the braid word
$\sigma_w$ representing $\varrho$.  This is both a **feature** and a
**limitation**:*

* *Feature (universality):* *Every vortex on $H_3(R, q)$ —
  proton $(uud)$, neutron $(udd)$, any nucleon-like trefoil —
  inherits the same $(2 + 1/[2]_q) \cdot m_e$ additive
  offset.  Mass differences between nucleons come entirely
  from the descended $|\mathrm{tr}_M|$ and brane-tower pieces,
  not from the Frobenius correction.*
* *Limitation (vortex-blind):* *The Frobenius correction cannot
  by itself distinguish $\varrho_{\mathfrak{p}}$ from
  $\varrho_{\mathfrak{n}}$ or any other trefoil-like vortex.
  Vortex-dependent corrections (e.g. chirality factors
  $\{1+h, 1-h^2, (1-h^2)^2\}$ per
  ([figure-eight BW coefficients](#prop\:six-term-mass-formula-complete))
  or knot-factor Frobenius pairings per
  ([knot-factor Frobenius pairing](#conj\:knot-factor-frobenius-pairing))
  — are separate structural terms beyond $\tau(C_{\dim_q})$.*

*The unified mass formula
([unified knot mass](#thm\:knot-mass-formula-unified)) therefore has
three tiers:*

1. *Vortex-specific: descended $|\mathrm{tr}_M(\sigma_w)|$ and brane
   tower $\sum \Phi_q$.*
2. *Algebra-specific (but vortex-independent): Frobenius
   co-Casimir $\tau(C_{\dim_q}^{(A)})$.*
3. *Isotope-specific (vortex-dependent but structural):
   chirality / knot-factor coefficients from
   `thm:six-term-mass-formula-complete`.*

**Consistency.**

1. *At $q = 1$ (classical limit): $\dim_q \to d_\lambda$ and
   $\tau(p_\lambda) \to d_\lambda/|G|$ (group-algebra trace), so
   $C_{\dim_q}$ reduces to $\sum_\lambda |G|/d_\lambda^2 \cdot p_\lambda$
   and its trace is $\sum_\lambda 1/d_\lambda$ — the classical
   reciprocal-dimension sum.*
2. *In the "single-vortex" case $A = H_3(R, q)$, three blocks
   $\{(3), (2,1), (1,1,1)\}$ with $q$-dims $\{1, [2]_q, 1\}$
   give $\tau(C_{\dim_q}) = 2 + 1/[2]_q$ matching proton
   residual to $0.14\%$ at $q_0 \approx 1.11$.*
3. *The self-duality $\lambda \leftrightarrow \lambda'$ is the
   **categorical shadow** of the Young-diagram transpose
   symmetry of the Hecke algebra, which in turn descends from
   the Hecke relation $\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$ admitting
   two eigenvalues $(q, -q^{-1})$ — the source of all
   $q$-deformation structure in the paper.*

## Explicit Lean closures by partition count $n$

For each $n$, the Frobenius co-Casimir trace
$\tau(C_{\dim_q}^{(n)}) = \sum_{\lambda \vdash n} 1/\dim_q(\lambda)$
admits an explicit closed form via $\mathrm{Fin}\,p(n)$ enumeration
once a Lean definition of $\dim_q(\lambda)$ for each partition is
available. The convention used throughout is the **quantum
hook-length formula** $\dim_q(\lambda) = [n]_q!\,/\,\prod_{x \in \lambda} [h_x]_q$,
which reduces to the classical $S_n$-irrep dimension at $q = 1$.

The status table:

| $n$ | $p(n)$ | conj. pairs | self-conj. | Lean theorem | nucleus unblocked |
|----:|-------:|------------:|-----------:|-------------|-------------------|
| $3$ | $3$ | $1$ | $1$ ((2,1)) | inline at $\sigma_w$-trace | $\mathfrak{p}, \mathfrak{n}$ (single-vortex) |
| $6$ | $11$ | $5$ | $1$ ((3,2,1)) | `hecke_n6_frobenius_codim` | ${}^{4}$He (H_{12} block; ) |
| $7$ | $15$ | $7$ | $1$ ((4,2,1)) | `hecke_n7_frobenius_codim` | A $\ge$ 5 nuclei |
| $8$ | $22$ | $10$ | $2$ ((4,2,1,1), (3,3,2)) | `hecke_n8_frobenius_codim` | ${}^4$He / ${}^{16}$O / ${}^{20}$Ne |

Each closure follows the same proof scheme: (i) a `Fin.sum_univ_*`
decomposition lemma extending Mathlib's `Fin.sum_univ_eight` to
$p(n)$ summands via a sequence of `Fin.sum_univ_castSucc` peels;
(ii) per-partition `@[simp]` lemmas unfolding $\dim_q(\lambda)$ to
its product-of-$q$-integers form; (iii) the trace identity itself,
discharged by `simp + ring` after the conjugate-pair grouping.

The $n = 8$ closure introduces partitions whose hook-product
cancellation against $[8]_q!$ leaves residual $/[2]_q$ factors
(specifically (5,1,1,1), (4,4), (4,1,1,1,1), (2,2,2,2)). These are
encoded as $(q + q^{-1})^{-1}$ in the explicit `dim_q` expressions;
the `ring` discharge handles them via real-arithmetic field
identities. Self-conjugates at $n = 8$ are (4,2,1,1) and (3,3,2).
The complete index map and the conjugate-symmetric `Fin 22`
ordering are documented in
[`frobenius-codim-universal.lean`](frobenius-codim-universal.lean).

The generator that produces the per-partition $\dim_q$ table and
the Lean source is
[`computations/phase5/phase5_n8_dim_q_table.py`](https://github.com/litlfred/qou/blob/claude/wire-applied-uniqueness-mass-table/computations/phase5/phase5_n8_dim_q_table.py);
the JSON output and per-partition factor signatures are committed
under `phase5-n8-dim-q-table.json`.

Beyond $n = 8$, the same scheme extends mechanically to $n = 9$
(partitions of $9$, $p(9) = 30$, needed for triton and ${}^{3}$He at
$H_9$) and $n = 12$ ($p(12) = 77$, needed for ${}^{4}$He's $H_{12}$
substrate when not yet decomposed). The bottleneck above $n = 8$
is the size of the explicit $\dim_q$ table rather than the proof
scheme; both can be machine-generated by extending the
`phase5_n8_dim_q_table.py` script.
