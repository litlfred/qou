<!-- FILE_START: lusztig-vs-hermitian-bar.md -->
**Proposition** (Lusztig bar vs Hermitian $\ast$).
*On the complex Iwahori–Hecke algebra $H_n(\mathbb{C}, q)$ with
$q \in \mathbb{C}^\times$, the two ring anti-involutions*

$$
\beta_L \colon q \mapsto q^{-1},\quad \sigma_i \mapsto \sigma_i^{-1}
\qquad\text{(Lusztig bar)},
$$

$$
\beta_H \colon q \mapsto \overline{q}^{\,-1},\quad \sigma_i \mapsto \sigma_i^{-1}
\qquad\text{(Hermitian $\ast$)}
$$

*coincide on the parameter $q$ if and only if
$\mathrm{Im}(q) = 0$, equivalently $q \in \mathbb{R}$.*

The Lean formalization specialises to $\mathbb{R}$ for the archimedean evaluation at the substrate $q_0$.
## Significance

The framework's existing bar-symmetric / bar-anti-symmetric decomposition is built around $\beta_L$ alone. On the real axis this is the only available involution structure. On general complex $q$ with $\lvert q \rvert > 1$ and $\mathrm{Im}(q) \neq 0$, the algebra admits a finer decomposition by simultaneous $\beta_L$- and $\beta_H$-eigenvalues, producing four channels:

| $\beta_L$-eigenvalue | $\beta_H$-eigenvalue | Existing name | Comment |
|---|---|---|---|
| $+1$ | $+1$ | bar-symmetric, Hermitian | retained (current) |
| $+1$ | $-1$ | bar-symmetric, anti-Hermitian | new (CP-odd, parity-even?) |
| $-1$ | $+1$ | bar-anti-symmetric, Hermitian | new (CP-even, parity-odd?) |
| $-1$ | $-1$ | bar-anti-symmetric, anti-Hermitian | projected away |

The interpretation of the two new channels remains open. This proposition only records the structural existence of the decomposition; it does not claim either new channel corresponds to physical structure.

## Non-claims of this proposition (CAL-4 caveat)

- It does not claim $\mathrm{Im}(q_0) \neq 0$.
- It does not claim the two new channels carry physical content.
- It does not introduce a further calibration input.

It claims only that on complex $q$ with $\mathrm{Im}(q) \neq 0$ the two anti-involutions split, and that the framework's current real-axis convention makes the split invisible.
<!-- FILE_END: lusztig-vs-hermitian-bar.md -->

<!-- FILE_START: q-zero-complex-extension.md -->
**Proposition** (q-zero complex extension).
*Let $R$ be a commutative ring and $q \in R^\times$ a unit. Every pre-Archimedean substrate identity—the Hecke quadratic $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, the bar involution $q \leftrightarrow q^{-1}$, $\sigma_i \leftrightarrow \sigma_i^{-1}$, the Frobenius pairing $\langle\cdot,\cdot\rangle_F$, and the Markov trace $\mathrm{tr}_M$—is stated polymorphically in $R$. The specialization $R = \mathbb{C}$ with $q_0 \in \mathbb{C}$ and $\lvert q_0 \rvert > 1$ is admissible. The substrate identities transfer verbatim, with $\lvert q \rvert > 1$ replacing the archimedean ordering $q > 1$ as the substrate-level non-degeneracy condition.*

## Significance

The proposition makes explicit that the framework's pre-Archimedean content is independent of the choice of $\mathrm{Im}(q)$. The current convention $q_0 \in \mathbb{R}$, $q_0 > 1$ is one valid specialization.

**CAL-4 caveat:** A complex $q_0$ with $\lvert q_0 \rvert > 1$ would require either a function expressing $\mathrm{Im}(q_0)$ in terms of the three existing calibrations, or a structural constraint fixing $\mathrm{Im}(q_0)$ from substrate data. Neither is currently supplied. The proposition provides infrastructure for the categorical lift without claiming the physical reality of $\mathrm{Im}(q_0)$.

The codebase evaluates one complex-$q$ regime: the unit circle $q = e^{i\Theta}$. Here the bar involution coincides with complex conjugation, and the pair $(\Phi_q, \mathrm{Li}_2^q)$ becomes a Hermitian-conjugate pair. This proposition extends the admissible regime to $\lvert q \rvert > 1$, where Lusztig bar and Hermitian $\ast$ split. The unit-circle case forms the boundary, the real-axis case forms the $\mathrm{Im}(q) = 0$ specialization, and the general complex case sits between them.
<!-- FILE_END: q-zero-complex-extension.md -->

<!-- FILE_START: two-filtration-bridge-general.md -->
**Proposition (two-filtration bridge map in full generality —
bar-class determines iterated-integral depth).**

[`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
verified the bridge map $d_{\mathrm{II}}$ at all partitions of $n \leq 4$.
*This proposition extends the verification to **all** partitions of
any $n$ via a structural bar-eigenspace argument.*

### Statement

For every partition $\lambda$ (of any $n \geq 1$), the iterated-
integral depth predicted by the two-filtration bridge conjecture
([`conj:two-filtration-bridge`](#conj:two-filtration-bridge))
depends only on the **bar-class** of $\lambda$:

$$
  \boxed{\;
    d_{\mathrm{II}}(\lambda)
    \;=\;
    \begin{cases}
      2 & \text{if } \lambda \text{ is self-conjugate } (\lambda = \lambda'), \\
      3 & \text{if } \{\lambda, \lambda'\} \text{ is a chiral pair } (\lambda \neq \lambda').
    \end{cases}
  \;}
$$
### Corollaries

**Generalises round 9**: the small-cases bridge verification
at $n \leq 4$ extends to all $n$ via the bar-eigenspace argument.

**Corollary for B1**:
- For each self-conjugate cell, B1's depth-2 row is theorem-level
 (combining Bloch–Suslin + per-knot VC where available).
- For each chiral pair, B1's depth-3 row is conditional on the CS
 computation per knot.

**Combined with
[`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
+
[`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)**:
the depth-3 content over $\mathbb{Q}(\zeta_N)$ for every prime $N$ is
controlled by $\lfloor (N - 1)/2 \rfloor - 1$ genuinely-new real
numbers, all pairing with chiral-pair cells in the appropriate
$H_n(q)$.

### Cross-references

- Bridge conjecture: [`conj:two-filtration-bridge`](#conj:two-filtration-bridge)
- Small-cases verification: [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
- Chirality structure: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)
- Joint action discharge: [`prop:joint-galois-braid-discharged`](#prop:joint-galois-braid-discharged)
- Hecke-Baer-* and bar action on $e_\lambda$:
 [`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic),
 [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
<!-- FILE_END: two-filtration-bridge-general.md -->

<!-- FILE_START: two-filtration-bridge.md -->
**Conjecture (two-filtration bridge: iterated-integral depth $\leftrightarrow$
partition-cellular GB-depth via central idempotents).**

*The substrate convolution Hopf algebra $\mathcal{H}_q$ carries
two distinct filtrations:*

- *the **iterated-integral depth** on grouplikes
  ([keystone correspondence](#conj:gb-depth-period-correspondence)),
  $G^{(0)} \subseteq G^{(1)} \subseteq \cdots$ with $G^{(n)}$
  generated by $\{\exp_q, \log_q, \mathrm{Li}_2^q, \ldots, \mathrm{Li}_n^q\}$;*
- *the **partition-cellular GB-depth** on the centre $Z(H_n(q))$
  ([curvature-rank GB stratification](#prop:curvature-rank-gb-stratification),
  [stratified $\Phi_q$](#prop:quantum-dilogarithm-stratified)),
  $Z^{(0)}(A) \subseteq Z^{(1)}(A) \subseteq \cdots$ where
  $\mathrm{depth}_{\mathrm{GB}}(\lambda) = \max_\square h(\square)$.*

*These are different numbers* — for the figure-8 self-conjugate cell
$\lambda = (2, 2)$, iterated-integral depth $= 2$ but partition
GB-depth $= 3$ (max hook length). *The conjecture: they are
related, and the bridge is via the central primitive idempotents
$e_\lambda$.*

### Statement

*For each $\lambda \vdash n$, the central idempotent $e_\lambda
\in Z(H_n(q))$ has a **canonical iterated-integral depth lift**
$\hat{e}_\lambda \in G^{(d_{\mathrm{II}}(\lambda))}(\mathcal{H}_q)$
where the depth $d_{\mathrm{II}}(\lambda)$ is given by:*

$$
  d_{\mathrm{II}}(\lambda) \;=\;
  \begin{cases}
    2 & \text{if } \lambda \text{ is self-conjugate (amphichiral cell)} \\
    3 & \text{if } \lambda, \lambda' \text{ form a chiral pair} \\
    \min(\mathrm{depth}_{\mathrm{GB}}(\lambda), 2\,\lceil n/2 \rceil) & \text{otherwise}
  \end{cases}
$$

*and the bridge map is given by the action of $e_\lambda$ on the
depth-$d_{\mathrm{II}}(\lambda)$ component of $\mathrm{Li}_n^q$ at
the canonical Bring shape parameter for cell $\lambda$.*

### Structural justification of the statement

The two filtrations have orthogonal information:

- **Iterated-integral depth** counts *how many polylogarithm
  factors* are needed to express a grouplike — equivalently, the
  Goncharov motivic-Galois weight.
- **Partition-cellular GB-depth** counts *how many braid generators*
  are needed to express a Hecke element — equivalently, the
  Bruhat-length/cellular complexity.

They cannot be equal in general (different units; one counts
"transcendental complexity," the other counts "algebraic combinatorial
complexity"). But they are *bridged* by the central idempotents,
which simultaneously:

- live in $Z(H_n(q))$ at a specific GB-depth (max hook), and
- pair under Markov trace with grouplikes at a specific iterated-
  integral depth.

The bridge map $\lambda \mapsto d_{\mathrm{II}}(\lambda)$ is what
the conjecture predicts.

### Concrete predictions

| $\lambda$ | $\mathrm{depth}_{\mathrm{GB}}$ | $d_{\mathrm{II}}$ | Period type witnessed |
|---|---|---|---|
| $(2,2)$ self-conj. | 3 | **2** | $\mathrm{Vol}(4_1) \in \mathcal{P}_2^+$ |
| $(3), (1,1,1)$ chiral pair | 3 | **3** | $\mathrm{CS}(3_1) \in \mathcal{P}_3^-$ |
| $(2, 1)$ self-conj. | 3 | **2** | hyperbolic vol if 3-mfd (not $T(2,3) = 3_1$) |
| $(4)$ totally symm | 4 | **2** | sym-channel vol (depends on shape) |
| $(2, 2, 1, \ldots)$ | depends | **2** if self-conj, **3** if pair | $\ldots$ |

The general pattern: **self-conjugacy under partition transpose
$\Rightarrow$ even iterated-integral depth (real period); chiral
pair $\Rightarrow$ odd depth (Tate-twisted period)**. Verifies
[`rem:chirality-period-pairing`](#rem:chirality-period-pairing).

### Reduction to known structure

At $n = 2, 3, 4$: the table above can be checked exhaustively against
the Hecke-cell structure. Self-conjugate partitions of small $n$ are
$(1)$, $(2,1)$ [no, $(2,1)$ is its own transpose], $(2,2)$, $(3,2,1)$,
$\ldots$ (these are the partitions equal to their transpose, called
*self-conjugate*). The bridge map gives them depth-$2$ witnesses;
chiral pairs split into depth-$3$ witnesses.

At $n \geq 5$: the partition combinatorics gets richer; Hoefsmit
seminormal form
([`prop:hoefsmit-seminormal-form`](#prop:hoefsmit-seminormal-form))
and the explicit $e_\lambda$ formula
([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent))
allow the bridge to be computed cell-by-cell.
<!-- FILE_END: two-filtration-bridge.md -->

<!-- FILE_START: hq-bi-filtration.md -->
**Definition (knot-indexed bi-filtration $\mathcal{H}_q^{(n, K)}$ on the substrate convolution algebra).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)),
filtered by iterated-integral depth
$G^{(0)} \subseteq G^{(1)} \subseteq \cdots$
([keystone correspondence](#conj:gb-depth-period-correspondence)).
For each Bring-embeddable knot/link $K$ ([Bring-embeddable
knots](#rem:bring-embeddable-knots)) with dominant cell
$\lambda_K \vdash n_K$ and central primitive idempotent
$e_{\lambda_K} \in Z(H_{n_K}(q))$
([explicit central idempotent](#prop:explicit-central-idempotent)),
the **knot-$K$-localised depth-$n$ stratum** is*

$$
  \mathcal{H}_q^{(n, K)}
  \;:=\;
  \bigl\{\, \alpha \;\in\; G^{(n)}(\mathcal{H}_q)
        \;:\; e_{\lambda_K} \cdot \alpha \cdot e_{\lambda_K} = \alpha \,\bigr\}.
$$

*The double-indexed family $\{\mathcal{H}_q^{(n, K)}\}_{n \geq 0,\;K}$
is the **bi-filtration**: a horizontal axis of iterated-integral
depth $n$ (Goncharov side) and a vertical axis of knot/braid class
$K$ (Hecke cell side).*

### Axes and refinements

**Depth axis $n$ (horizontal).** Inherited from
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence):
$G^{(0)}$ contains $\exp_q$ and scalars; $G^{(n)}$ adjoins the
grouplikes $\log_q, \mathrm{Li}_2^q, \ldots, \mathrm{Li}_n^q$.
Compatible with $\tau_{\mathrm{arch}}$ via
$\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$.

**Knot axis $K$ (vertical).** Refined by partition cell
$\lambda_K$. Two natural sub-axes inside the $K$-axis:

1. **Bar-class.** Self-conjugate $\lambda_K = \lambda_K'$ vs chiral
   pair $\lambda_K \neq \lambda_K'$ (cf. [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)).
2. **Genus.** $g(K) \leq 4$ for Bring-embeddable
   ([`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)).

### Compatibility with the Hopf and braid structures

The bi-filtration interacts with the existing structures on $\mathcal{H}_q$:

| Operation | Effect on $(n, K)$ |
|---|---|
| Convolution $*_q$ ($q$-shuffle) | $\mathcal{H}_q^{(n_1, K_1)} *_q \mathcal{H}_q^{(n_2, K_2)} \subseteq \bigoplus \mathcal{H}_q^{(n_1 + n_2, K')}$ where $K'$ ranges over cell-mergings |
| Coproduct $\Delta_q$ | $\Delta_q(\mathcal{H}_q^{(n, K)}) \subseteq \bigoplus_{n_1 + n_2 = n,\,K_1 \otimes K_2 = K} \mathcal{H}_q^{(n_1, K_1)} \otimes \mathcal{H}_q^{(n_2, K_2)}$ |
| Bar involution $* \colon q \mapsto q^{-1}$ | $* \colon \mathcal{H}_q^{(n, K)} \to \mathcal{H}_q^{(n, K^*)}$ where $K^*$ is the mirror knot |
| Markov trace $\mathrm{tr}_M$ | $\mathrm{tr}_M \colon \mathcal{H}_q^{(n, K)} \to \mathcal{P}_n / \mathcal{P}_{n-1}$ — depth-preserving, knot-evaluating |
| Braid action of $\beta \in B_{n_K}$ | $\beta \cdot \mathcal{H}_q^{(n, K)} \subseteq \mathcal{H}_q^{(n, \beta \cdot K)}$ where $\beta \cdot K$ is the conjugate braid closure |

### The grid: low-$(n, K)$ examples

| $K$ | $\lambda_K$ | Bar-class | $\mathcal{H}_q^{(0, K)}$ | $\mathcal{H}_q^{(2, K)}$ | $\mathcal{H}_q^{(3, K)}$ |
|---|---|---|---|---|---|
| trivial (unknot $0_1$) | $(1)$ | self-conj | scalars | $\mathrm{Li}_2^q(0) = 0$ | $\mathrm{Li}_3^q(0) = 0$ |
| trefoil $3_1$ | $(3)$ vs $(1,1,1)$ | chiral pair | $e_{(3)} \pm e_{(1,1,1)}$ | $\mathrm{Vol}(3_1) = 0$ (torus) | $\mathrm{CS}(3_1) = \pm \pi^2/6$ |
| figure-8 $4_1$ | $(2,2)$ | **self-conj** | $e_{(2,2)}$ | $2\,\mathrm{Cl}_2(\pi/3)$ (confirmed) | depth-3 partner (open) |
| Bring trilog input | abstract / virtual | (lifted from $\zeta_5$) | scalars | weight-2 extension | $\mathrm{Li}_3(\zeta_5)$ (confirmed) |

### The bi-filtration as a tooling unification

This block is the **definition layer** for the framework the
keystone implies but does not name. Three downstream conjectures
populate it:

- [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
  — the symmetry group acting on $\mathcal{H}_q^{(n, K)}$.
- [`prop:knot-indexed-convolution-grid`](#prop:knot-indexed-convolution-grid)
  — placement of paper's existing knot-indexed convolutions
  ($\mathrm{Lk}_R^{(k)}$, $\bowtie_K$, Markov trace, Hoefsmit pairing,
  Higgs-vev coupling) into the $(n, K)$-grid.
- [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
  — Beilinson regulator on $K_{2n-1}^{\mathrm{ind}}(\overline{\mathbb{Q}})$
  matches the depth-$n$ axis.
<!-- FILE_END: hq-bi-filtration.md -->

<!-- FILE_START: joint-galois-braid-action.md -->
**Conjecture (joint motivic-Galois $\times$ braid-group action on the
bi-filtration).**

*Let $\mathcal{H}_q^{(n, K)}$ be the knot-indexed bi-filtration
([`def:hq-bi-filtration`](#def:hq-bi-filtration)). Two groups act
on it by symmetry:*

- *the **motivic Galois group** $G_{\mathrm{mot}}$ acts on the
 depth axis, permuting Goncharov period classes
 $\mathcal{P}_n / \mathcal{P}_{n-1}$ under $\tau_{\mathrm{arch}}$
 (Kontsevich–Zagier 2001, Goncharov 2001);*
- *the **braid group** $B_{n_K}$ acts on the knot axis, permuting
 Wedderburn cells $e_{\lambda_K}$ via the standard
 representation on $H_{n_K}(q)$.*

*Conjectural joint structure: these two actions extend to a joint
action of a semi-direct product $G_{\mathrm{mot}} \rtimes B_{n_K}$
on $\mathcal{H}_q^{(n, K)}$, with the action on each axis being
**equivariant** with respect to the action on the other:*

$$
  \boxed{\;
    g_{\mathrm{mot}}(\beta \cdot \alpha)
    \;=\;
    \beta \cdot g_{\mathrm{mot}}(\alpha)
    \quad\text{for } \alpha \in \mathcal{H}_q^{(n, K)},\;
    g_{\mathrm{mot}} \in G_{\mathrm{mot}},\;
    \beta \in B_{n_K}.
  \;}
$$

*Equivalently: the motivic-Galois action commutes with the braid-
group action when restricted to the bi-filtration, and the joint
group $G_{\mathrm{mot}} \times B_{n_K}$ stabilises each
$\mathcal{H}_q^{(n, K)}$ stratum.*

### Structural motivation for the prediction

Three motivations:

1. **The depth axis is Galois-equivariant by construction.** Goncharov's
 motivic-Galois group acts accordingly on the period algebra
 $\mathcal{P}_*$, preserving the depth filtration. Pulled back via
 $\tau_{\mathrm{arch}}$, this gives an action on each $G^{(n)}(\mathcal{H}_q)$.

2. **The knot axis is braid-equivariant by construction.** The braid
 group $B_n$ acts on $H_n(q)$ via the standard half-twist generators
 $\sigma_i$, permuting Wedderburn cells via the Hoefsmit
 seminormal-form action. This descends to an action on
 $\mathcal{H}_q$ via Schur–Weyl.

3. **The two actions touch different parts of the structure.** Galois
 acts on $q$-coefficients (via $q \mapsto q^{-1}$ for the bar
 involution, or via cyclotomic Galois on $\zeta_n$); braid acts on
 the Hecke-element argument. These are **a priori orthogonal**,
 so commutativity is the natural conjecture.

### Equivalent statements

- The bi-filtration $\mathcal{H}_q^{(n, K)}$ is a **bi-graded
 $(G_{\mathrm{mot}} \times B_{n_K})$-module**.
- The composition map $\tau_{\mathrm{arch}} \circ (\beta \cdot -)$
 equals $(\beta \cdot -) \circ \tau_{\mathrm{arch}}$ on each
 stratum (with $\beta$ acting on the period side via its
 monodromy representation).
- The joint orbit of any $\alpha \in \mathcal{H}_q^{(n, K)}$ under
 $G_{\mathrm{mot}} \times B_{n_K}$ stays within $\mathcal{H}_q^{(n, K)}$.

### Concrete prediction at $(n, K) = (3, \zeta_5\text{-Bring})$

For the Bring depth-3 bi-filtration cell
([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)):

- $G_{\mathrm{mot}}$-action: cyclotomic Galois $\sigma_a \colon
  \zeta_5 \mapsto \zeta_5^a$ for $\gcd(a, 5) = 1$. Permutes
 $\{\mathrm{Li}_3(\zeta_5^k) : k = 1, 2, 3, 4\}$ as the
 $(\mathbb{Z}/5)^\times \cong \mathbb{Z}/4$ orbit.
- $B_n$-action (here $B_5$ via $S_5$ symmetry of Bring): permutes
 the same 4 values via the regular representation of $S_5$ on
 $\mathbb{Q}(\zeta_5)$.

**The conjecture predicts**: these two permutation actions
**commute**. canonical evidence: the orbit-sum
$\sum_{k=1}^4 \mathrm{Li}_3(\zeta_5^k) = -\frac{24}{25}\zeta(3)$
is *both* Galois-invariant (= cyclotomic Galois-trace) *and*
$S_5$-invariant (= regular-representation trace), so the joint-
invariant subspace contains $\zeta(3)$. Higher invariants would
test the joint commutativity sharply.

### Concrete prediction at $(n, K) = (2, 4_1)$

For the figure-8 ($\lambda_K = (2, 2)$ self-conjugate cell):

- $G_{\mathrm{mot}}$-action: bar involution $q \mapsto q^{-1}$.
 Fixes $e_{(2, 2)}$ since $(2, 2)$ is self-conjugate. acts as the identity
 on $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \in \mathcal{P}_2^+$.
- $B_3$-action (figure-8 is a 3-strand braid): the dihedral
 $D_3 = S_3$ symmetry of the braid acts on $e_{(2, 2)}$ by definition
 (since $(2, 2)$ is the unique self-conjugate cell of
 $H_3 \subset H_4$ structure).

Joint action stabilises the entire stratum by definition —
**consistent with the prediction** that the figure-8 is the
canonical fixed point for both groups in $\mathcal{H}_q^{(2, K)}$.
### Significance

If discharged, the joint action gives:

1. **Symmetry-organised period generation.** Periods at depth $n$
 for knot $K$ generate a $G_{\mathrm{mot}} \rtimes B_{n_K}$-module;
 the irreducible decomposition predicts which periods are
 independent vs forced by $q$-rational structure.
2. **Cross-axis dictionaries.** Galois orbits on $\mathcal{P}_n$
 correspond to braid orbits on cells: each pair $(g, \beta)$
 gives a relation among period values.
3. **B1 sharpness via representation theory.** The keystone's
 sharpness condition (image generates $\mathcal{P}_n / \mathcal{P}_{n-1}$
 non-by definition) reduces to non-vanishing of certain
 $G_{\mathrm{mot}} \rtimes B_n$-invariants — a representation-
 theoretic question, much more tractable than
 transcendence-theoretic ones.
<!-- FILE_END: joint-galois-braid-action.md -->

<!-- FILE_START: adelic-substrate.md -->
**Definition.**
*The **adelic substrate** of the QOU framework is the ring of adeles of $\mathbb{Q}$,*

$$
  \mathbb{A}
  \;=\;
  \mathbb{R} \;\times\; \prod_{p}{}^{\!\!\prime}\;\mathbb{Q}_p,
$$

*the restricted product of the archimedean completion $\mathbb{R}$ with all $p$-adic completions $\mathbb{Q}_p$ (restriction: almost all components lie in the maximal compact subring $\mathbb{Z}_p$).*

Each non-archimedean place $p$ corresponds to a localized quantum
geometric state of the substrate: a specific $q$-deformation
evaluated at a primitive root of unity, equivalently a Kummer level
in the Habiro / cyclotomic completion
([algebraic quantum volume](#def:algebraic-quantum-volume)).
The archimedean place $\infty$ — the $\mathbb{R}$ component — is
the laboratory continuum, accessible only through the
[classical limit functor](#def:classical-limit-functor) and the
[archimedean realization functor](#def:archimedean-realization-functor).

**Motivation for the adelic substrate.** Replacing $\mathbb{R}$ by $\mathbb{A}$ resolves a
structural tension already noted in
[classical limit (preamble)](#sec:classical-limit-preamble): the
local $q$-geometries at each prime do not assemble into a continuous
manifold, but they *do* assemble into a global adelic object. The
macroscopic universe is therefore not the real continuum
$\mathbb{R}$ alone but the simultaneous integration of all local
non-archimedean data weighted by their archimedean shadow.

**Adelic integration (Tate's thesis).** Global observables of the
substrate — the macroscopic mass functional, the global
$L$-function of Bring's coordinate ring, the partition functions of
the brane tower — are not Riemann integrals over $\mathbb{R}$. They
are Tate integrals over $\mathbb{A}$:

$$
  \mathcal{Z}(s)
  \;=\;
  \int_{\mathbb{A}^\times} \! f(x)\,|x|^s\, d^\times x
  \;=\;
  \zeta_\infty(s) \cdot \prod_{p} \zeta_p(s),
$$

a product of local zeta integrals, one per place. The classical
$\zeta(s)$ of [classical Riemann zeta](#def:classical-riemann-zeta)
is recovered as the global Tate integral of the standard adelic
Schwartz function. Local $q$-zeta data and macroscopic real-valued
observables are two faces of the same adelic object.

This is the global stitch: discrete quantum data at every prime,
glued by adelic restriction, projected to physical numbers by the
[archimedean realization functor](#def:archimedean-realization-functor).
<!-- FILE_END: adelic-substrate.md -->

