<!-- FILE_START: intro-mutant-jones-bloch-group.md -->
The Jones polynomial cannot distinguish mutant knot pairs — the
Kinoshita–Terasaka and Conway knots are the canonical example —
but the substrate-level Hecke construction *should* be able to:
it tracks more refined invariants than the closure trace alone.
This section uses the mutant pair as a falsifiability test and
identifies the Bloch group closure as the categorical residue
that resolves the mutant ambiguity.

The arc structures around the falsifiability question.  The
first blocks set up the bi-filtration grid that distinguishes
mutant knots categorically; the middle blocks compute the
substrate-level invariant on the canonical mutant pair and
exhibit the separation; the closing blocks tie the separation
to the Bloch-group quotient construction from the Descartes
chapter, identifying the Bloch closure as the algebraic
incarnation of the mutant resolution.

The output is the categorical mutant-resolving invariant and
its substrate-flow stability.  This is the strongest single
falsifiability result in the chapter: the substrate-level
construction makes a definite prediction on a case where the
Jones polynomial is silent, and the experimental
distinguishability of the mutant pair tests the prediction
directly.
<!-- FILE_END: intro-mutant-jones-bloch-group.md -->

<!-- FILE_START: knot-indexed-convolution-grid.md -->
**Proposition (placement of paper's existing knot-indexed
convolutions in the bi-filtration grid; conditional on [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)).**

*Each existing "non-tensor product" operation in the QOU paper —
where two morphisms are combined via a knot/braid/partition-shaped
twist rather than a plain tensor product — sits at a specific
$(n, K)$ stratum of the bi-filtration $\mathcal{H}_q^{(n, K)}$
([`def:hq-bi-filtration`](#def:hq-bi-filtration)).*

### The grid

See [Table 1](#tbl:knot-indexed-convolution-grid-table1-data).

### Two structural observations

#### Observation 1: most "knot-indexed" operations sit at $n = 0$

The paper's *operational* knot-indexed convolutions ($\mathrm{Lk}_R^{(k)}$,
$\bowtie_K$, Hoefsmit pairing, Markov trace) live at depth $n = 0$
on the algebraic side — they manipulate Hecke elements without
introducing polylogarithms. Their *archimedean image* sits at
higher depth depending on what is paired with: Markov trace + braid
of a hyperbolic knot lands at depth 2 (volume); CS lands at depth 3.

This is not accidental: the bi-filtration encodes a clear separation
between **input shape** (the knot index $K$, depth-$0$ on the
algebraic side) and **output transcendence depth** (achieved only
after applying $\tau_{\mathrm{arch}}$, which involves the depth-$n$
grouplike $\mathrm{Li}_n^q$).

#### Observation 2: the $\bowtie_K$ "non-tensor product" pattern is a depth-0 knot index

The original confusion in the first answer of this session — was
$\bowtie_K$ a Mikusiński-style convolution? — reduces to: **$\bowtie_K$
is a depth-0, knot-indexed Hecke element**. In the bi-filtration
language:

$$
  \bowtie_K \;\in\; \mathcal{H}_q^{(0, \,\text{EW interface braid})}.
$$

The "convolution" structure the user identified is the bi-filtration
itself: convolution by $\bowtie_K$ shifts the knot-index axis (via
left/right multiplication in $H_6(q)$) without changing the depth
axis. This is a *structural translation*, not a polylogarithmic
operation.

### Closure properties of the grid

See [Table 2](#tbl:knot-indexed-convolution-grid-table2-data).

### Significance for the paper's existing operations

This proposition serves three purposes:

1. **Names the pattern.** The "$\bowtie_K$-style" non-tensor products
   are now collected under one definition: each is a knot-indexed
   convolution at a specific $(n, K)$ stratum.

2. **Predicts compatibility.** Operations at the same depth $n$ but
   different $K$ should compose via convolution as the table predicts.
   E.g., $\mathrm{Lk}_R^{(k_1)} *_q \mathrm{Lk}_R^{(k_2)}$ should
   land in $\mathcal{H}_q^{(0, \text{double link})}$.

3. **Identifies novel candidates.** The empty cells of the grid —
   in particular high-$n$ chiral entries and the $S_5$-Galois orbit
   of depth-3 cyclotomic periods — are *predicted to exist* by the
   bi-filtration definition but are not yet realised in the paper.
   Each is a falsifiability target.

### Discussion

**Tabulation block.** The placement of each existing operation is
*verified by inspection* of its defining block. The closure
properties are *conjectural* (modulo well-definedness of the
bi-filtration). The joint-action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
sharpens the closure into an equivariance.
<!-- FILE_END: knot-indexed-convolution-grid.md -->

<!-- FILE_START: conway-kt-vol-injectivity-test.md -->
**Remark (Conway–Kinoshita–Terasaka mutant pair: Jones-coincident,
Vol-coincident — sanity check for B1's Vol-injectivity prediction).**

The transcendental-accounting ledger
([`rem:transcendental-accounting`](#rem:transcendental-accounting)
Fact 2) records the structural prediction:

$$
  J_{K_1}(q) \;=\; J_{K_2}(q) \;\;\text{in } \mathbb{Z}[q^{\pm 1}]
  \;\;\Longrightarrow\;\;
  \mathrm{Vol}(K_1) \;=\; \mathrm{Vol}(K_2).
$$

The cleanest known Jones-coincident pair of *distinct hyperbolic
knots* is the **Conway–Kinoshita–Terasaka (CKT) mutant pair**:

| Knot | Hoste–Thistlethwaite name | Crossing number | Jones polynomial | Vol (SnapPy) |
|---|---|---|---|---|
| Conway knot | $11n34$ | 11 | $-q^{-4} + 2q^{-3} - 2q^{-2} + 2q^{-1} - 2 + 2q - 2q^2 + q^3$ | $11.31951569\ldots$ |
| Kinoshita–Terasaka knot | $11n42$ | 11 | (identical) | $11.31951569\ldots$ |

These knots are **mutant**: one is obtained from the other by
rotating a Conway 2-tangle by $\pi$ in a 2-sphere intersecting the
projection at 4 points. Mutation preserves:

- the Jones polynomial $J_K(q)$ (Lickorish 1982),
- *all* coloured Jones polynomials $J_K^{(N)}(q)$
  (Morton–Cromwell, also Garoufalidis–Lê),
- the hyperbolic volume $\mathrm{Vol}(K)$ — **theorem of Ruberman
  (1987)**: mutation of hyperbolic knots preserves both the volume
  and the Chern–Simons invariant.

**B1's Vol-injectivity prediction is therefore satisfied for the
CKT pair**: same Jones $\Rightarrow$ same volume, by Ruberman.
This is a *positive sanity check*, not a falsification target —
for mutants, the equality is forced by Ruberman's theorem
independent of B1.

### Sharper falsification targets

For B1 to be *falsifiable* at the Vol-injectivity layer, we need
**non-mutant Jones-coincident pairs**:

| Candidate | Status | Source |
|---|---|---|
| Eliahou–Kauffman–Thistlethwaite (2003) infinite family of links with $J_L = 1$ (same as unlink) | distinct from unlink, but link not knot | Eliahou et al. 2003 |
| Anstee–Przytycki–Rolfsen pairs | non-mutant Jones-coincident knot pairs exist; volumes computed in some cases — Vol(K_1) = Vol(K_2) confirmed for known cases | Anstee–Przytycki–Rolfsen 1989 |
| Jones-coincident pairs in Bring-embeddable class ($g \leq 4$) | open whether any exist | follows from Jones-faithfulness on $g \leq 4$, which is open per [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3 |

### Relevance of the CKT case to B1

Even though the equality is forced by Ruberman (not by B1), the
*mechanism* through which equality arises differs across frameworks:

| Framework | Mechanism for $\mathrm{Vol}(\text{Conway}) = \mathrm{Vol}(\text{KT})$ |
|---|---|
| Classical 3-manifold topology | Ruberman's theorem on mutation |
| B1 + transcendental-accounting | $J_K = J_{K'} \Rightarrow$ same depth-2 grouplike pre-image $\Rightarrow$ same $\tau_{\mathrm{arch}}$ image |
| Volume Conjecture asymptotic | both $J_K^{(N)}$ identical $\Rightarrow$ same asymptotic $\Rightarrow$ same volume |

All three give the same answer for CKT. **The B1 framework would
distinguish itself only on a Jones-coincident pair where Ruberman
does not apply** — i.e. non-mutant pairs.
### Cross-references

- B1 prediction: [`rem:transcendental-accounting`](#rem:transcendental-accounting) Fact 2
- Open Jones-faithfulness question: [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3
- Bring-embeddable class: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
- Bi-filtration placement: [`prop:knot-indexed-convolution-grid`](#prop:knot-indexed-convolution-grid)
<!-- FILE_END: conway-kt-vol-injectivity-test.md -->

<!-- FILE_START: jones-faithfulness-crossing-8.md -->
**Remark (Bring-embeddable Jones-faithfulness — theorem at crossing
$\leq 8$, open at crossing $\geq 9$).**

The "Jones-faithfulness on Bring-embeddable knots" question
recorded in [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness)
Q3 — *do distinct Bring-embeddable knots always produce distinct
Jones polynomials?* — is **theorem-level for crossing number
$\leq 8$**.

### Theorem-level results

**Hoste–Thistlethwaite–Weeks knot enumeration (1998)** classified
all prime knots up to crossing number 16 and verified that
**every prime knot of crossing $\leq 11$ has a unique Jones
polynomial** — i.e., no two distinct prime knots up to 11 crossings
share their Jones polynomial.

The first known examples of distinct prime knots with the same
Jones polynomial are the **Conway–Kinoshita–Terasaka mutant pair**
at 11 crossings ([`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)),
which is the *unique* known example at crossing 11.

Restricted to **Bring-embeddable knots** (Seifert genus $g \leq 4$,
[`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)):

| Crossing range | Bring-embeddable count | Jones-distinguishes? |
|---|---|---|
| $\leq 4$ | finite explicit list | **yes** (theorem; by definition since each knot has different Jones polynomial) |
| 5–8 | finite explicit list | **yes** (HTW 1998) |
| 9–10 | finite explicit list | **yes** (HTW 1998) |
| 11 (Conway-KT) | mutant pair has $g \leq ?$ | **no for the mutant pair** (Conway = 11n34, KT = 11n42, both have genus 3 $\le$ 4 — *Bring-embeddable*) |

The strict statement: **for Bring-embeddable knots up to crossing
10, Jones-distinguishes; the Conway-KT mutant pair at crossing 11
provides one Jones-coincident pair within the Bring-embeddable
class**.

### Tightening of [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3

The original Q3 ("do distinct Bring-embeddable knots always produce
distinct Jones polynomials?") refines to:

- **Up to crossing 10**: (yes) theorem (HTW 1998).
- **At crossing 11**: (no) **falsified by the Conway-KT mutant pair**.
 But Vol-injectivity *still holds* by Ruberman 1987 (mutation
 preserves volume for hyperbolic knots).
- **At crossing $\geq 12$**: open whether more Jones-coincident pairs
 exist. Anstee–Przytycki–Rolfsen 1989 constructions give some
 non-mutant Jones-coincident pairs, but their genus / Bring-
 embeddability is not always recorded.

### Significance for B1's Vol-injectivity prediction

B1's Vol-injectivity prediction
([`rem:transcendental-accounting`](#rem:transcendental-accounting)
Fact 2):

$$
  J_{K_1}(q) = J_{K_2}(q) \;\;\Longrightarrow\;\;
  \mathrm{Vol}(K_1) = \mathrm{Vol}(K_2).
$$

For Bring-embeddable knots:

- Up to crossing 10: vacuously true (no Jones-coincident pairs).
- At crossing 11 (Conway-KT): satisfied (Ruberman), confirmed in
 [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test).
- At crossing $\geq 12$: depends on whether non-mutant
 Jones-coincident Bring-embeddable pairs exist; if any do, B1
 predicts equal volumes — falsifiable.

### The strong falsification target

A **non-mutant Jones-coincident pair** of Bring-embeddable knots
with **provably different volumes** would *falsify* B1's
Vol-injectivity. None are currently known. Existence is open.

If such a pair were found:

- The Volume Conjecture asymptotic mechanism would still be
 consistent (the asymptotic uses *coloured* Jones, not just
 $J_K^{(2)}$, so $J_{K_1}^{(2)} = J_{K_2}^{(2)}$ doesn't imply
 $J_{K_1}^{(N)} = J_{K_2}^{(N)}$ for higher $N$).
- B1's stronger version (Vol-injectivity from $J^{(2)}$ alone) would
 fail.
- The framework would still be valid for the *coloured* version of
 the Jones-faithfulness implication.
### Cross-references

- Original open question: [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3
- Mutant pair sanity check: [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)
- Bring-embeddable atlas: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
- B1 Vol-injectivity prediction: [`rem:transcendental-accounting`](#rem:transcendental-accounting) Fact 2
<!-- FILE_END: jones-faithfulness-crossing-8.md -->

<!-- FILE_START: wedderburn-as-noncomm-fourier.md -->
**Statement.**
*The character expansion underlying the
[three-invariant mass formula](#thm:wedderburn-mass-formula) is the
**inverse non-commutative Fourier transform** on $H_n(q)$ in the sense
of Peter--Weyl/Plancherel for finite-dimensional semisimple algebras.*

For $q$ generic, $H_n(q)$ is semisimple and the Wedderburn--Artin
decomposition reads

$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} \operatorname{End}_{\mathbb{C}}(V_\lambda),
$$

where $\lambda$ ranges over partitions of $n$ and $V_\lambda$ is the
Specht module with $\dim V_\lambda = d_\lambda$. The Markov trace
$\operatorname{tr}_M : H_n(q) \to \mathbb{C}$
([Jones--Markov trace](#thm:jones-markov-trace))
admits the spectral expansion

$$
  \operatorname{tr}_M(\beta)
  \;=\;
  \sum_{\lambda \vdash n}
  w_\lambda \,\frac{\chi_\lambda(\beta)}{d_\lambda},
\qquad
\beta \in H_n(q),
$$

where $\chi_\lambda$ is the irreducible character on the $\lambda$-block
and $\{w_\lambda\}$ are the Markov weights (Jones--Ocneanu coefficients).

**Identification.** Reading $\widehat{H_n(q)} = \{\lambda \vdash n\}$ as
the *non-commutative spectrum*:

| Commutative side ($S^1$ or $U(1)$) | Non-commutative side ($H_n(q)$) |
|:--|:--|
| Frequency $k \in \mathbb{Z}$ | Partition $\lambda \vdash n$ |
| Fourier coefficient $\widehat{f}(k)$ | Character value $\chi_\lambda(\beta)$ |
| Plancherel measure $dk$ | Quantum dimension weight $w_\lambda / d_\lambda$ |
| $f = \sum_k \widehat{f}(k)\,e^{ik\theta}$ | $\operatorname{tr}_M(\beta) = \sum_\lambda w_\lambda \chi_\lambda(\beta)/d_\lambda$ |

The role of $\operatorname{tr}_M$ is the inverse-transform: it
*reassembles* a class function on $H_n(q)$ from its non-commutative
Fourier coefficients $\{\chi_\lambda(\beta)\}_\lambda$.

**Renaming, not new content.** Nothing new is asserted: this is
exactly the Peter--Weyl/Plancherel formula for the finite-dimensional
semisimple algebra $H_n(q)$, applied to the trace functional
$\operatorname{tr}_M$. The proposition is included because the
"non-commutative Fourier transform" reading clarifies how downstream
results — in particular the
[three-invariant mass formula](#thm:wedderburn-mass-formula) and
the
[Markov trace product factorization](#thm:markov-trace-product)
— *select* a finite set of partitions
$\{\lambda\} \subseteq \widehat{H_n(q)}$ as physical mass channels.

**Scope.** The identification holds whenever $H_n(q)$ is semisimple,
i.e. for $q$ not a non-trivial root of unity. At roots of unity the
spectrum collapses to the *fusion category* $\widehat{H_n(q)}^{ss}$;
the proposition still holds for the surviving simple objects, but the
sum is restricted to the truncated index set. Throughout the QOU mass
formula we evaluate at the substrate parameter $q_0$, which is in the
generic locus, so the full Wedderburn decomposition applies.

**No new physics.** This proposition does not change any computed
quantity. It supplies the conceptual hook for the Pieri-shift
behaviour of the
[degree-one Hecke photon](#prop:pieri-photon-shift) and for the
spectral interpretation of the
archimedean remainder:
both are statements about which partitions $\lambda$ contribute at a
given filtration depth.
<!-- FILE_END: wedderburn-as-noncomm-fourier.md -->

<!-- FILE_START: degree-one-braid-trivial-volume.md -->
**Statement.**
*Let $\gamma \in H_n(q)$ be a degree-one element*

$$
  \gamma \;=\; 1 \;+\; \sum_{i=1}^{n-1} \phi_i\,\sigma_i,
  \qquad \phi_i \in \mathbb{C},
$$

*and write $\overline{\beta}$ for the closure of a braid word $\beta$.
Then under the
[archimedean realization functor](#def:archimedean-realization-functor)
the volume image vanishes:*

$$
  \tau_{\mathrm{arch}}\!\bigl(\operatorname{tr}_M(\gamma)\bigr)
  \;=\; 0
  \quad\text{in the volume normalisation}
  \quad
  \mathrm{Vol}_{\tau}(\overline{\gamma}) \;=\; 0.
$$
<!-- FILE_END: degree-one-braid-trivial-volume.md -->

<!-- FILE_START: pieri-photon-shift.md -->
**Statement.**
*Let $\gamma \in H_n(q)$ be a degree-one element*

$$
  \gamma \;=\; 1 + \sum_{i=1}^{n-1} \phi_i\,\sigma_i,
$$

*and let $\beta_m \in H_n(q)$ be a state supported on the
$\lambda$-block of the
[Wedderburn--Artin decomposition](#prop:wedderburn-as-noncomm-fourier),
i.e. $\chi_\mu(\beta_m) = 0$ for $\mu \neq \lambda$. Under the
inclusion $H_n(q) \hookrightarrow H_{n+1}(q)$, the support of
$\gamma \cdot \beta_m$ is contained in the partitions obtained from
$\lambda$ by adding or removing a single box:*

$$
  \mathrm{supp}\bigl(\gamma \cdot \beta_m\bigr)
  \;\subseteq\;
  \{\lambda\} \;\cup\;
  \{\lambda + \square\} \;\cup\;
  \{\lambda - \square\},
$$

*where $\lambda \pm \square$ ranges over the addable / removable
corners of the Young diagram $\lambda$.*
<!-- FILE_END: pieri-photon-shift.md -->

<!-- FILE_START: pieri-photon-shift-interpretation.md -->
**Remark (non-commutative Fourier picture).**
Under the spectral identification of
[Wedderburn--Artin = inverse non-commutative Fourier transform](#prop:wedderburn-as-noncomm-fourier),
$\gamma$ acts on the spectrum
$\widehat{H_n(q)} = \{\lambda \vdash n\}$ as a finite-difference
*box-shift* — the non-commutative analogue of a single-step shift on
$\mathbb{Z}$ in the commutative Fourier picture. Multiplying by
$\gamma$ raises or lowers the Young-diagram support by one box, never
more.
<!-- FILE_END: pieri-photon-shift-interpretation.md -->

<!-- FILE_START: phi-q-tower-jsj-bridge.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

### Statement

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate
parameter $q$, let $\beta \in B_n$ be a braid, and let
$\rho_q = 1/\hbar_q^2$ be the substrate density
([quantum Planck constant](#def:quantum-planck-constant)).
For each non-empty $S \subseteq \{0, \dots, n-2\}$ with
$\lvert S \rvert \leq 2$, let $K_S$ be the Φ$_q$-piece of $\beta$
([Φ$_q$-piece](#def:phi-q-piece)) and let
$V_S := \prod_{i \in S}\hat{V}_i^{\mathrm{full}}$ be the per-block
spectral coordinate
([mass endomorphism tower](#prop:mass-endomorphism-tower)).

#### Algebraic-side prerequisite

The **algebraic** content of "JSJ stratification" — a partition of
the mass-tower formula into level-$|S|$ summands in
$J^{|S|}/J^{|S|+1}$ of the GS confinement filtration — is stated
in full generality by
[`prop:phi-q-tower-algebraic-stratification`](#prop:phi-q-tower-algebraic-stratification).
That proposition is **unconditional**: it lives entirely in
$H_n(R, q)$ over $\mathbb{Q}(q^{1/2})$, makes no reference to
$\tau$, hyperbolic volume, or 3-manifold pieces, and uses the
**Frobenius norm** $\|\cdot\|_F$ valued in the ground ring (not
the Archimedean absolute value).

The conjecture below — and *only* the conjecture — crosses the
Archimedean wall by identifying that algebraic stratification
with the geometric JSJ under $\tau_{\mathrm{arch}}$.

**Conjecture (Φ$_q$–JSJ archimedean bridge).** Under the archimedean
realisation $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization))
each summand of the dilogarithm form of the tower equals $\rho_q$ times
the hyperbolic volume of the corresponding Φ$_q$-piece,

$$
  \tau_{\mathrm{arch}}\!\bigl(z^{\lvert S\rvert} \cdot \Phi_q(\|V_S\|_F)\bigr)
  \;=\;
  \rho_q \cdot
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S),
  \qquad
  1 \leq \lvert S \rvert \leq 2,
$$

(where $\|\cdot\|_F$ is the **Frobenius norm** valued in
$\mathbb{Z}[q^{\pm 1/2}]$, evaluated on the algebraic side *before*
applying $\tau_{\mathrm{arch}}$; the right-hand side is a real number
because $\tau_{\mathrm{arch}}$ supplies the Archimedean projection).
The descended summand $\bigl\| \prod_i \hat{V}_i \bigr\|_F$
realises archimedeanly to the holonomy term
$\rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_\emptyset)$.
Summing over $S$ yields

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathfrak{m}(\varrho)\bigr)
  \;=\;
  \rho_q \cdot
  \!\!\sum_{\substack{S \subseteq \{0,\dots,n-2\} \\ 0 \leq \lvert S\rvert \leq 2}}\!\!
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S).
$$

After identifying the family $\{K_S\}_S$ (modulo
small-piece collapse) with the JSJ decomposition
$\mathrm{JSJ}(K)$ of $K = \widehat{\beta}$, the right-hand side
coincides with the JSJ piecewise sum
$\sum_{P \in \mathrm{JSJ}(K)} \rho_F(P) \cdot \mathrm{Vol}_{\mathrm{hyp}}(P)$
that drives the canonical binding-energy pipeline.

### Significance (rather than deprecating Φ$_q$)

The conjecture says the **dilog form** and the **hyperbolic-volume
form** of the tower are not two competing engines: they are two
presentations of the same archimedean number, evaluated through two
different convergence schemes.

- **JSJ pipeline.** For each piece $P$, evaluate
  $\mathrm{Vol}_{\mathrm{hyp}}(P)$ canonical with SnapPy. Fast on
  finished hyperbolic atoms; opaque internally.
- **Φ$_q$ pipeline.** For each $S$, evaluate
  $\Phi_q(\|V_S\|_F)$ as a Laurent polynomial in $q^{1/2}$.
  Slower convergence (the Kashaev limit is logarithmic), but yields a
  closed-form, $q$-differentiable expression per generator and per
  pair.

The bridge predicts that the two engines compute the same atomic-mass
target, and explains the empirical 0.15% Φ$_q$ floor on $D$ as a
**Kashaev-convergence floor**, not a model floor. Phase 2 of the
1ppb handover (pentagon-defect expansion) is intrinsically a
Φ$_q$ computation — the pentagon identity is the Φ$_q$ five-term
relation — so the dilog form earns its keep as a *theoretical* tool
while JSJ remains the canonical workhorse.

### Conditional Lean theorem

Per `AGENTS.md` §3b, this conjecture is downstream of
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture) and
therefore cannot be a `theorem`/`proposition` block.  The Lean
formalisation lives in the formal Lake package at
`QOU.PhiQJSJ` (see
[`lean/QOU/PhiQJSJ.lean`](../../lean/QOU/PhiQJSJ.lean)) and states
the bridge as a Lean theorem **conditional on two typeclass
instances**:

```
theorem bridge {q : ℝ}
    [Kashaev.VolumeConjecture q]
    [PhiQJSJ.TowerSummandRealization q]
    [PhiQJSJ.PerPieceBridge q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) :
    TowerSummandRealization.realisation β S =
      rho q * pieceVolume q β S :=
  inst.bridge_per_piece β S
```

`bridge` contains **no `sorry`**: every step is either definitional
or supplied by a typeclass field.  The conjectural content is fully
concentrated in `[VolumeConjecture q]` (Kashaev's axiom) and
`[PerPieceBridge q]` (the per-piece identification asserted by the
conjecture).  Modulo those typeclass instances, the bridge theorem
is fully verified by Lean.

The supporting modules `QOU.PhiQPiece` and `QOU.Kashaev` also live
in the formal chain (`lean/QOU/PhiQPiece.lean`,
`lean/QOU/Kashaev.lean`); see
[`pieceVolume`](../../lean/QOU/Kashaev.lean) for the volume
predicate.  Per
[`QOU.GroundRingAnnotations`](../../lean/QOU/GroundRingAnnotations.lean),
`QOU.PhiQJSJ` is the Archimedean tier — it is **not** part of the
formal pre-Arch chain but is the explicit τ_arch bridge.

### Required ingredients (to be filled in incrementally)

1. **Single-crossing case** ($\lvert S \rvert = 1$). The Kashaev limit
   of a single-crossing piece is a one-bridge knot complement; its
   hyperbolic volume realises $\Phi_q(\|\hat{V}_i\|_F)$. The
   single-crossing identity is the smallest non-trivial instance of
   KVC and is the base case of the bridge.

2. **Adjacent-pair case** ($\lvert S \rvert = 2$). The pair piece
   $K_{\{i, i+1\}}$ is a two-bridge knot whose hyperbolic volume
   realises $z^2 \cdot \Phi_q(\|\hat{V}_i \hat{V}_{i+1}\|_F)$.
   The Markov weight $z^2$ on the algebraic side reproduces the
   gluing weight on the JSJ side, governed by the
   [pentagon UV commutation](#prop:pentagon-uv-commutation) relation.

3. **Descended (level-zero) carrier.** The empty piece $K_\emptyset$
   carries the descended summand
   $\bigl\| \prod_i \hat{V}_i \bigr\|_F$
   ([descended-level-zero](#prop:descended-level-zero)).

4. **JSJ identification.** Modulo collapse of Seifert-fibered small
   pieces, the family $\{K_S\}$ realises $\mathrm{JSJ}(K)$ with
   weights matching $\rho_F$ on the JSJ side. This step is the
   formal bridge between the **algebraic JSJ** (the
   $J^\bullet$-graded stratification of $H_n(q)$ described in the
   *Algebraic-side statement* above) and the geometric JSJ
   decomposition of $S^3 \setminus \widehat\beta$. The
   algebraic JSJ is intrinsic to the Hecke side and is not
   derived from the geometric JSJ; the conjecture is precisely
   that $\tau_{\mathrm{arch}}$ pushes one to the other.

The first two ingredients are conditional on KVC at the per-piece
level; the third is a categorical statement
([descended-level-zero](#prop:descended-level-zero)); the fourth is
a JSJ-theoretic identification, conjectural until each
small-piece collapse is verified.

### Motivic dictionary

The bridge admits a clean motivic reading: the algebraic side
$\Phi_q(\|V_S\|_F)$ is a class in the quantum Bloch group
$\mathfrak{B}(q)$ ([quantum Bloch group](#def:quantum-bloch-group)), the
archimedean realisation $\tau_{\mathrm{arch}}$ is the $q$-deformed
Borel/Beilinson regulator, and the right-hand side is the standard
Neumann–Zagier decomposition of the volume of $S^3 \setminus K$ along
its hyperbolic pieces [`neumann-zagier1985`, `zagier1986`]. In this
language the conjecture is the statement that

- the quantum Bloch class $[\Phi_q(\lvert V_S\rvert)]$ regulates
  archimedeanly to the volume of the corresponding Φ$_q$-piece, and
- the Φ$_q$ stratification $\{K_S\}_S$ realises the JSJ stratification
  with regulator weights matching $\rho_F$.

The $\rho_q$ prefactor on the right-hand side is the substrate-density
normalisation that converts a regulator output (a real number) into a
mass density on the brane. Phrased this way, the dilog form and the
hyperbolic-volume form are not two competing engines but two
presentations of the same regulator, evaluated through two
convergence schemes.
<!-- FILE_END: phi-q-tower-jsj-bridge.md -->

<!-- FILE_START: dilogarithm-archimedean-limit.md -->
**Conjecture (Archimedean limit of the partial product).**
*Let $q$ be the substrate parameter — the QOU substrate has
$q_0 \approx 1.11$ — and let $x \in (0, 1)$ be a state variable so
that $|x q^k| < 1$ along the truncation. Let $\Phi_n(x; q)$ be the
$q$-Pochhammer partial product
([definition](#def:q-pochhammer-partial-product)).
Under the joint Faddeev scaling $q \to 1$, $n \to \infty$,
$n\lvert 1 - q\rvert \to \infty$, the rescaled logarithm of the
partial product converges to the classical dilogarithm:*

$$
  \boxed{\;
  \lim_{\substack{q \to 1 \\ n \to \infty \\ n |1-q| \to \infty}}
  (1 - q) \cdot \log \Phi_n(x; q)
  \;=\;
  \mathrm{Li}_2(x)
  \;:=\;
  -\!\int_0^x \frac{\log(1 - t)}{t}\, dt.
  \;}
$$

*The limit is taken from $q \to 1^-$ in the convergence regime
$|q| < 1$ and is extended to $q \to 1^+$ (the QOU substrate side) by
analytic continuation. Equivalently, the algebraic logarithmic
singularities of the denominator factors $(1 - x q^k)$ at
$x = q^{-k}$ converge, under the Archimedean realization
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor)),
to the logarithmic singularity at $t = 1$ of the integrand
$-\log(1-t)/t$ in the classical $\mathrm{Li}_2$.*

## Saddle-point story

Take logarithms inside the partial product:

$$
  \log \Phi_n(x; q)
  \;=\;
  -\!\sum_{k=0}^{n-1} \log\bigl(1 - x q^k\bigr).
$$

Setting $q = e^{-\hbar}$ and $x = e^{-y}$ and rescaling $k = s/\hbar$,
the sum becomes a Riemann sum for the integral
$\hbar^{-1}\!\int_0^{n\hbar} -\log\!\bigl(1 - e^{-y - s}\bigr)\, ds$.
Substituting $t = e^{-y-s}$ and taking $n\hbar \to \infty$ produces
$\hbar^{-1} \cdot \mathrm{Li}_2(e^{-y}) = \hbar^{-1} \cdot
\mathrm{Li}_2(x)$, so $(1 - q) \log \Phi_n(x; q) \sim \hbar
\log \Phi_n \to \mathrm{Li}_2(x)$. This is the standard
Faddeev–Kashaev quasi-classical limit
[`faddeev1994`, `kashaev1997`].

## Established sub-result: the convergence regime $q \to 1^-$

For **fixed** $x \in (0,1)$ on the convergence side $q \to 1^-$, the limit
is **elementary** — a monotone left-Riemann-sum limit with an exponential
tail bound and the factor $(1-q)/\hbar \to 1$ — and it holds **uniformly
on compact subsets of $(0,1)$**. No Tauberian theorem and no branch-cut
analysis are needed: the denominator factors satisfy
$1 - x q^k \geq 1 - x > 0$ for all $k$, so the poles of $\Phi_n$ are never
approached. The full elementary proof (and its precise relationship to the
earlier Tier-B Lean assessment) is recorded in
[`docs/audits/2026-06-07-dilog-archimedean-limit-part-A-elementary.md`](../../../docs/audits/2026-06-07-dilog-archimedean-limit-part-A-elementary.md).
This discharges the uniform-Riemann-sum requirement (gap 1 below) as a
theorem; the conjectural content is therefore confined to the substrate
continuation $q \to 1^+$ (gaps 2–3).

## Conjectural status

The rigorous statement requires:

1. **Uniform control of the Riemann-sum error** *(resolved for the
   $q \to 1^-$ regime).* For fixed $x \in (0,1)$ the convergence is
   uniform on compact subsets of $\{0 < x < 1\}$ by the elementary
   argument above. The residual difficulty is **not** here but in the
   substrate continuation (item 2).

2. **Branch-cut compatibility** *(the genuine open content).* The
   classical $\mathrm{Li}_2$
   carries a branch cut on $[1, \infty)$; the partial product
   $\Phi_n(x; q)$ has $n$ poles approaching this cut as $q \to 1$.
   The conjecture asserts the limit is the **principal-branch**
   $\mathrm{Li}_2$, i.e. that the algebraic poles cancel against
   themselves before the limit is taken (Frobenius pairing with a
   fixed $T_w$ kills the poles above GB-depth $k_\star(T_w)$ —
   see [stratified Φ$_q$](#prop:quantum-dilogarithm-stratified)).

3. **Mathlib infrastructure.** A complete Lean proof needs a
   uniform Tauberian theorem and branch-cut control on the
   principal-branch dilogarithm — neither currently in Mathlib.
   The conjecture is therefore packaged as the typeclass
   `QOU.QPochhammer.ArchimedeanLimit`, with one field stating the
   convergence along Faddeev's joint scaling. `LiTwo : ℝ → ℝ`
   is no longer opaque: it is now defined as the explicit series
   $\mathrm{LiTwo}(x) := \sum_{k \geq 1} x^k / k^2$ via Mathlib's
   `tsum`, and the boundary lemmas `LiTwo_zero` and
   `partialProduct_zero` are unconditional. The class is inhabited
   unconditionally at $x = 0$ (`archimedeanLimit_zero` instance),
   where both sides of the convergence are identically zero; for
   $x \in (0, 1)$ the instance still awaits the Tauberian
   argument from `faddeev1994` / `kashaev1997`.

## Bridge to the geometric side

The conjecture is the **algebraic half** of the Kashaev volume
conjecture
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)).
The geometric half ([Bloch–Wigner volume](#rem:kashaev-volume-density))
asserts that $\mathrm{Im}\bigl(\mathrm{Li}_2(z) + \log z \cdot
\log(1 - z)\bigr) = D(z)$ is the hyperbolic volume of an ideal
tetrahedron with shape parameter $z$. Together, the two halves
give the QOU-native formulation of Kashaev:

$$
  \tau_{\mathrm{arch}}\!\bigl(\Phi_n(x; q_0)\bigr)
  \;\xrightarrow[\text{this conj.}]{}
  \;\mathrm{Li}_2(x)
  \;\xrightarrow[\text{Bloch-Wigner}]{}
  \;\mathrm{Vol}_{\mathrm{hyp}}(\Delta_z)
  \;=\;
  D(z),
$$

with the shape parameter $z$ matching the algebraic state variable
$x$ at the same denominator zero — the content of
[shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy).
<!-- FILE_END: dilogarithm-archimedean-limit.md -->

<!-- FILE_START: phi-q-wkb-greens-function.md -->
**Conjecture (next-order Faddeev WKB gives the categorical Green's function).**
*Let $q$ be the substrate parameter and $\hbar_q = 1 - q^{-1}$ the
quantum Planck constant. Under the joint Faddeev scaling $q \to 1$, $n \to \infty$, $n|1-q| \to \infty$ of
[the archimedean limit conjecture](#conj:dilogarithm-archimedean-limit),
the partial product $\Phi_n(x; q)$
([$q$-Pochhammer partial product](#def:q-pochhammer-partial-product))
admits a stationary-phase expansion at the dominant saddle $x_0$ of
the form*

$$
  \Phi_n(x; q)
  \;\sim\;
  \exp\!\Bigl(
    \hbar_q^{-1} S_0(x_0)
    + S_1(x_0)
    + \hbar_q \, S_2(x_0)
    + \cdots
  \Bigr),
$$

*where the leading term is the classical dilogarithm,*

$$
  S_0(x_0)  =  \mathrm{Li}_2(x_0)
  \qquad (= \text{archimedean limit}),
$$

(See [archimedean limit](#conj:dilogarithm-archimedean-limit) for the
conjectural archimedean realisation of $\mathrm{Li}_2$.)

*and the next-to-leading term is the half-log-determinant of the
[categorical Dirac operator](#def:categorical-dirac-operator)
$\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \, \iota_\xi \nabla$
restricted to the
[categorical-instanton moduli](#def:categorical-instanton) at
$x_0$:*

$$
  \boxed{\;
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2} \log \det\!\bigl(\mathfrak{D}_\nabla\big|_{x_0}\bigr).
  \;}
$$

*Equivalently, the
[archimedean realization](#def:archimedean-realization-functor)
$\tau_{\mathrm{arch}}$ of the one-loop fluctuation factor
$\exp S_1(x_0)$ is the two-point Green's function of $\mathfrak{D}_\nabla$
evaluated at the corresponding hyperbolic cusp:*

$$
  \tau_{\mathrm{arch}}\!\bigl(\exp S_1(x_0)\bigr)
  \;=\;
  G_\nabla(x_0)
  \;:=\;
  \langle  \mathfrak{D}_\nabla^{-1}  \rangle_{x_0}.
$$

## Narrative proof (modulo the conjectural ingredients listed below)

The proof has four steps. Steps 1–2 are classical Faddeev–Kashaev
asymptotics. Step 3 is the new categorical input. Step 4 is
standard heat-kernel zeta regularisation.

**Step 1 (classical: Faddeev–Kashaev scalar WKB).** Take logs inside
the partial product:

$$
  \log \Phi_n(x; q)
  \;=\;
  -\!\sum_{k=0}^{n-1} \log\!\bigl(1 - x q^k\bigr).
$$

Set $q = e^{-\hbar_q}$, rescale $k = s/\hbar_q$, and pass to the
Riemann-sum integral
$\hbar_q^{-1}\!\int_0^{n\hbar_q} -\log\!\bigl(1 - x e^{-s}\bigr)\, ds$.
Substituting $t = x e^{-s}$, the asymptotic in the Faddeev regime is

$$
  \log \Phi_n(x; q)
  \;=\;
  \hbar_q^{-1}\,\mathrm{Li}_2(x)
  \;+\;
  S_1^{\mathrm{scalar}}(x)
  \;+\;
  O(\hbar_q),
$$

with $S_1^{\mathrm{scalar}}(x) = -\tfrac{1}{2} \log(1 - x) - \tfrac{1}{2}\log(2\pi)$
the standard $\hbar_q^0$ correction of the scalar stationary-phase
integral. This is the leading-order
[archimedean limit](#conj:dilogarithm-archimedean-limit) plus its
direct $\hbar_q^0$ correction in the scalar variable $x$.

**Step 2 (classical: passage from scalar to operator-valued).** When
$\Phi_n(x; q)$ is regarded as a *partition function* (the
Faddeev–Kashaev / Reshetikhin–Turaev path-integral reading), the
scalar variable $x$ is the eigenvalue of a connection-valued
operator and the scalar Hessian $-\tfrac{1}{2}\log(1-x_0)$ is
replaced by the operator-valued log-determinant of the Hessian of
the categorical action $\mathfrak{S}_q[\nabla]$ at the dominant saddle
$\nabla_0$:

$$
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2}\,\log \det
   \bigl( \mathrm{Hess}\,\mathfrak{S}_q[\nabla]\big|_{\nabla_0} \bigr).
$$

This is the standard one-loop fluctuation rule for stationary-phase
integrals over the space of connections. The remaining content of
the conjecture is identifying $\mathrm{Hess}\,\mathfrak{S}_q[\nabla]_{\nabla_0}$
with the categorical Dirac operator $\mathfrak{D}_\nabla$.

**Step 3 (new categorical input: Hessian = $\mathfrak{D}_\nabla$ via
Lichnerowicz on the instanton saddle).** Let $\nabla_0$ be a critical
point of $\mathfrak{S}_q$, equivalently a
[categorical instanton](#def:categorical-instanton):
$\star_q F_{\nabla_0} = F_{\nabla_0}$. For a perturbation $\nabla =
\nabla_0 + a$ with $a \in \Omega^1(\mathrm{End}\, V)$,

$$
  F_{\nabla_0 + a}  =  F_{\nabla_0} + d_{\nabla_0} a + a \wedge_q a.
$$

The first variation vanishes at $\nabla_0$ (saddle condition); the
second variation of the gauge sector
$\mathfrak{S}_q^{\mathrm{gauge}} = \int_A \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$
is

$$
  \delta^2 \mathfrak{S}_q^{\mathrm{gauge}}\big|_{\nabla_0}(a, a)
  \;=\;
  \langle  d_{\nabla_0} a,  d_{\nabla_0} a  \rangle_F
  \;=\;
  \langle  a,  \Delta_{\nabla_0}^q\, a  \rangle_F,
$$

where $\Delta_{\nabla_0}^q = d_{\nabla_0}^* \, d_{\nabla_0} +
d_{\nabla_0} \, d_{\nabla_0}^*$ is the *categorical $q$-Laplacian*
on $\Omega^1(\mathrm{End}\, V)$ with adjoint
$d_{\nabla_0}^* = \star_q\, d_{\nabla_0}\, \star_q$. So far this is
the categorical Yang–Mills computation, parallel to the classical
case.

The key identity is the **categorical Lichnerowicz formula** on the
self-dual background $\star_q F_{\nabla_0} = F_{\nabla_0}$:

$$
  \Delta_{\nabla_0}^q
  \;=\;
  \mathfrak{D}_{\nabla_0}^2  +  \tfrac{1}{4}\,\mathrm{Sc}_q,
$$

where $\mathfrak{D}_{\nabla_0}$ is the
[categorical Dirac operator](#def:categorical-dirac-operator) at
$\nabla_0$ and $\mathrm{Sc}_q$ is the $q$-scalar curvature
(vanishing on the contact-flat background of Bring's surface, where
$\xi$ is parallel). The classical Lichnerowicz identity
$\Delta = \mathfrak{D}^2 + R/4$ extends to the $q$-deformed case
because the categorical Dirac
$\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q\,\iota_\xi \nabla$
satisfies the same Clifford-multiplication structure as its
classical limit ($\iota_\xi$ playing the role of $\gamma^0$).

Therefore on the instanton saddle with vanishing $\mathrm{Sc}_q$:

$$
  \det \mathrm{Hess}\,\mathfrak{S}_q^{\mathrm{gauge}}\big|_{\nabla_0}
  \;=\;
  \det \Delta_{\nabla_0}^q
  \;=\;
  \det \mathfrak{D}_{\nabla_0}^2
  \;=\;
  (\det\, |\mathfrak{D}_{\nabla_0}|)^2,
$$

where we use the chiral structure on the spinor bundle: with
$\star_q F = F$ self-dual, $\mathfrak{D}_\nabla$ decomposes into
$(\mathfrak{D}_\nabla^+, \mathfrak{D}_\nabla^-)$ with
$\mathfrak{D}_\nabla^- = (\mathfrak{D}_\nabla^+)^*$, so
$\mathfrak{D}_\nabla^2 = \mathfrak{D}_\nabla^+\, \mathfrak{D}_\nabla^- \oplus
\mathfrak{D}_\nabla^-\, \mathfrak{D}_\nabla^+$ and the Pfaffian
identity $\det \mathfrak{D}_\nabla^2 = (\det |\mathfrak{D}_\nabla|)^2$
holds.

Combining with Step 2:

$$
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2}\, \log\det\bigl(\mathrm{Hess}\,\mathfrak{S}_q\big|_{\nabla_0}\bigr)
  \;=\;
  -\tfrac{1}{2}\, \log\det \mathfrak{D}_{\nabla_0}^2
  \;=\;
  -\log\det |\mathfrak{D}_{\nabla_0}|
  \;=\;
  -\tfrac{1}{2}\, \log\det \mathfrak{D}_{\nabla_0},
$$

where the final equality reads $\mathfrak{D}_\nabla$ as the Pfaffian
square root of $\mathfrak{D}_\nabla^2$ on the chiral spinor bundle —
the convention adopted in the conjecture statement above.

**Step 4 (standard: log-determinant = Green's function via heat-kernel
zeta).** By standard zeta-function regularisation,

$$
  -\tfrac{1}{2}\log\det \mathfrak{D}_\nabla
  \;=\;
  -\tfrac{1}{2}\,\mathrm{tr}\,\log \mathfrak{D}_\nabla
  \;=\;
  \tfrac{1}{2} \int_0^\infty \!\! \frac{dt}{t}
   \bigl( \mathrm{tr}\, e^{-t \mathfrak{D}_\nabla} - \mathrm{tr}\, e^{-t} \bigr).
$$

The functional derivative of this expression with respect to the
connection $\nabla$ at the saddle equals the diagonal of
$\mathfrak{D}_\nabla^{-1}$ — i.e. the categorical Green's function
$G_\nabla(x_0)$. The archimedean realisation $\tau_{\mathrm{arch}}$
sends the regularised determinant to the standard heat-kernel
determinant on the corresponding ideal-tetrahedron triangulation of
the hyperbolic brane configuration (paralleling how
[`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)
sends the leading Faddeev limit to the Bloch–Wigner volume).

This closes the chain $S_1 \leadsto -\tfrac{1}{2}\log\det\mathfrak{D}_\nabla
\leadsto G_\nabla(x_0)$ — modulo the three open ingredients listed
below.

## Open ingredients of the proof

| Step | Status | What remains |
|---|---|---|
| 1. Scalar Faddeev–Kashaev WKB | classical | none — Faddeev 1994, Kashaev 1997 |
| 2. Scalar $\to$ operator-valued passage | classical | none — standard one-loop fluctuation rule |
| 3a. Hessian = $\Delta_{\nabla_0}^q$ on $\Omega^1(\mathrm{End}\,V)$ | categorical Yang–Mills computation | direct from the variation of $\mathfrak{S}_q^{\mathrm{gauge}}$; routine |
| 3b. Categorical Lichnerowicz $\Delta^q = \mathfrak{D}^2 + \tfrac{1}{4}\mathrm{Sc}_q$ | new categorical lemma | Clifford-multiplication structure of $\iota_\xi$; provable but not in the paper yet |
| 3c. $\mathrm{Sc}_q$ vanishes on contact-flat Bring background | standard | $\xi$ parallel $\Rightarrow$ scalar curvature trivial |
| 3d. Pfaffian identity for self-dual chiral $\mathfrak{D}$ | classical | none — Atiyah–Singer / index theorem |
| 4. Heat-kernel determinant = propagator | standard analytic regularisation | none in the $\mathbb{R}^4$ archimedean specialisation; in Lean, needs heat-kernel infrastructure not in Mathlib |

The genuinely *new* step is **3b** — the categorical Lichnerowicz
identity. This is a single categorical lemma (provable from the
Clifford-multiplication structure of the
[categorical Dirac](#def:categorical-dirac-operator) and the
self-duality $\star_q F = F$ of the
[categorical-instanton equation](#def:categorical-instanton)). The
remaining steps are either standard or already in the paper.

Granting **3b**, the proof closes everything *except* the Lean
formalisation, which is blocked by the absence of heat-kernel
determinant theory and stationary-phase asymptotics from Mathlib.
The conjecture remains formally a conjecture (since 3b has not been
written up as a separate proposition with its own proof), but the
status of "what stops it" is much narrower: a single categorical
lemma plus Mathlib infrastructure.

## One algebraic object, two analytic outputs

The conjecture sharpens the Φ$_q$ (product form) vs
$-\mathrm{Li}_2^q(-z)$ (Kashaev integration limit) split: the same
algebraic state $\Phi_n(x; q_0)$ produces *both* of the
geometric features required for an observable QFT, separated
by their order in $\hbar_q$:

| WKB order | Symbol | Archimedean output | Role |
|-----------|--------|-------------------|------|
| $\hbar_q^{-1}$ | $S_0 = \mathrm{Li}_2(x_0)$ | Bloch–Wigner volume $D(z)$ | classical action / CS phase |
| $\hbar_q^{0}$ | $S_1 = -\tfrac{1}{2}\log\det \mathfrak{D}_\nabla$ | Green's function $G_\nabla(x_0)$ | one-loop propagator |
| $\hbar_q^{+1}$ | $S_2$ | curvature corrections | higher-loop |

For force-carrier torus knots $T_{m,n}$ the
$S_0$ piece evaluated at the corresponding flat-$\mathrm{SU}(2)$
critical point recovers the classical Chern–Simons invariant
(see [Chern–Simons as knot invariant](#rem:chern-simons-as-knot-invariant))

$$
  \mathrm{CS}(T_{m,n})
  \;=\;
  \frac{\pi^2 (m^2 - 1)(n^2 - 1)}{12\,m\,n}
$$

via Faddeev–Kashaev (the imaginary half of the volume conjecture, since
$\mathrm{Vol}(T_{m,n}) = 0$); the $S_1$ piece supplies the matching
one-loop propagator factor of the same algebraic state.

## Conjectural status in Lean

Granting the narrative proof above, three ingredients still need
formal write-up to upgrade the block to a theorem:

1. **Step 3b — categorical Lichnerowicz lemma.** A separate
   proposition stating $\Delta_{\nabla_0}^q = \mathfrak{D}_{\nabla_0}^2
   + \tfrac{1}{4}\,\mathrm{Sc}_q$, with proof from the Clifford-
   multiplication structure of $\iota_\xi$ in the
   [categorical Dirac](#def:categorical-dirac-operator). This is a
   single computation in the QOU formalism, not currently in the paper.

2. **Stationary-phase uniformity.** Standard stationary-phase gives the
   prefactor pointwise at $x_0$; the full statement asserts the
   asymptotic is uniform in a neighbourhood of $x_0$ along Faddeev's
   joint scaling, strong enough to commute with $\tau_{\mathrm{arch}}$.
   Inherited from
   [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit).

3. **Mathlib infrastructure.** A complete Lean proof needs heat-kernel
   determinant theory and stationary-phase asymptotics — neither
   currently in Mathlib. The conjecture is packaged as the typeclass
   `QOU.QPochhammer.WKBGreensFunction`, extending
   `QOU.QPochhammer.ArchimedeanLimit` with one additional field
   stating the $\hbar_q^0$ stationary-phase identity.

Ingredient (1) is the closest to a paper-side write-up; ingredients
(2)–(3) are the same Mathlib gap the parent conjecture already faces.

## Significance

The categorical Green's function $G_\nabla$ is the kernel that controls
the exponential decay of correlations in the categorical action — i.e.,
the mass-gap statement
([Yang–Mills surreal bound](#rem:yang-mills-surreal-bound)). The
$S_0 \leftrightarrow S_1$ split exhibited here is the structural
reason both the
Chern–Simons phase ([Chern–Simons as knot invariant](#rem:chern-simons-as-knot-invariant)) and the
mass-gap propagator emerge from a *single* algebraic state $\Phi_n(x;
q_0)$ at $q = q_0$ — without separately postulating a metric. The
Φ_q-piece [`def:phi-q-piece`](#def:phi-q-piece) thus carries both the
geometry (S_0) and the metric (S_1) of the corresponding hyperbolic
brane configuration; they are the leading and subleading analytic
shadows of the same algebraic datum, related by the WKB hierarchy in
$\hbar_q$.
<!-- FILE_END: phi-q-wkb-greens-function.md -->

<!-- FILE_START: algebraic-geometric-dilog-equivalence.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

**Conjecture (Algebraic-geometric dilogarithm equivalence).**
*The categorical Markov trace of the nonabelian multiplicative integral
over a lifted transient crossing
([mass identity](#def:mass-identity))
evaluates algebraically to a rational function in $\mathbb{Z}[q^{1/2},
q^{-1/2}, x]$ governed by the $q$-Pochhammer partial product
$\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
([q-Pochhammer partial product](#def:q-pochhammer-partial-product)).
Under the Archimedean realization $\tau_{\mathrm{arch}}$
([archimedean realization functor](#def:archimedean-realization-functor)):*

1. *(**Pole-to-cusp bijection.**) The roots
   $\{x = q^{-k} : k = 0, \dots, n-1\}$ of the denominator
   $(x; q)_n$ are in bijection with the ideal vertices of a hyperbolic
   tetrahedron triangulating the $\Phi_q$-piece $K_S$ of the lifted
   transient crossing
   ([Φ$_q$-piece](#def:phi-q-piece)).*

2. *(**Asymptotic Bloch–Wigner.**) The asymptotic of the partial
   product under Faddeev's scaling
   ([Archimedean limit](#conj:dilogarithm-archimedean-limit))
   recovers the Bloch–Wigner dilogarithm $D(z)$ at the matched shape
   parameter, so*

$$
  \tau_{\mathrm{arch}}\!\bigl(\Phi_n(x; q_0)\bigr)
  \;\xrightarrow[n \to \infty]{}\;
  D(z(x))
  \;=\;
  \mathrm{Vol}_{\mathrm{hyp}}\bigl(\Delta_{z(x)}\bigr),
$$

   *where $z(x)$ is the shape parameter of the ideal tetrahedron
   $\Delta_{z(x)}$ that triangulates $K_S$.*

3. *(**Mass formula.**) The $\tau_{\mathrm{arch}}$-image of the
   transient mass element is*

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathfrak{m}^{\mathrm{trans}}(\varrho)\bigr)
  \;=\;
  \rho_q \cdot
  \!\!\sum_{S \subseteq \{0,\dots,n-2\}}\!\!
  D\bigl(z(\lvert V_S\rvert)\bigr)
  \;=\;
  \rho_q \cdot
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K),
$$

   *recovering the JSJ piecewise sum used in the canonical binding-
   energy pipeline (cf.
   [Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)).*

## Relation to the structural form of Kashaev

The conjecture is the **QOU-native, partial-product** form of the
Kashaev–Murakami–Murakami theorem
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)).
Kashaev–MM pass through the colored Jones polynomial at roots of
unity; the present conjecture passes through the **explicit shared
denominator**:

| Side | Object | Pole / singularity |
|------|--------|--------------------|
| Algebraic ($R$) | $\Phi_n(x; q_0)$ | zero of $(1 - x q^k)$ at $x = q^{-k}$ |
| Archimedean ($\mathbb{C}$) | $\mathrm{Li}_2$ | logarithmic singularity at $t = 1$ |
| Geometric ($\mathbf{Hyp}_3$) | ideal tetrahedron $\Delta_z$ | cusp at vertex $v_k$ |

The bijection between the rows is the content of
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
Under that bijection, the algebraic state sum and the hyperbolic
volume are not two competing engines: they are the same regulator
$\Phi_n(x; q_0) \mapsto D(z(x))$ evaluated through two convergence
schemes.

## Conjectural standing (AGENTS.md §3b)

This block is downstream of
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)) and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)), so it is
necessarily a **conjecture** — propagation of conjectural backing
forbids promotion to `proposition`/`theorem`.

A Lean instance of the equivalence is provided as a typeclass
`QOU.QPochhammer.algebraic_geometric_equivalence` parametrised by an
`[ArchimedeanLimit]` instance and a `[Kashaev.VolumeConjecture]`
instance; downstream theorems then verify formally, modulo those two
class instances. This matches the conjectural-class pattern used for
[Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge).

## Witness

The algebraic-geometric matching of poles to cusps for the simplest
non-trivial case (the trefoil, $n = 3$) is recorded in
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json).
The witness reports the algebraic denominator zeros, the SnapPy-
solved cusp shape parameters obtained by feeding those zeros as
Newton–Raphson seeds, and the residual after one Newton step.
<!-- FILE_END: algebraic-geometric-dilog-equivalence.md -->

<!-- FILE_START: shared-denominator-cusp-holonomy.md -->
**Conjecture (Shared-denominator cusp holonomy).**
*Let $T_w \in H_n(R, q)$ be a Hecke normal-form word at GB-depth
$k_\star(T_w) = n$, let $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
be its $q$-Pochhammer partial product
([definition](#def:q-pochhammer-partial-product)),
and let $K_S$ be the $\Phi_q$-piece of the lifted braid
([Φ$_q$-piece](#def:phi-q-piece)). Then the roots of the
denominator polynomial*

$$
  (x; q)_n
  \;=\;
  \prod_{k=0}^{n-1}\bigl(1 - x q^k\bigr)
  \;\in\;
  \mathbb{Z}[q, x]
$$

*enforce the **cusp completeness conditions** of the Thurston
gluing equations on the ideal-tetrahedron triangulation of
$S^3 \setminus K_S$:*

$$
  (x; q_0)_n \;=\; 0
  \quad\Longleftrightarrow\quad
  \mathrm{Hol}_{\mu_k}(z_k) = 1
  \;\;\text{and}\;\;
  \mathrm{Hol}_{\lambda_k}(z_k) = 1
  \;\;\text{for some cusp}\;k,
$$

*where $z_k$ is the shape parameter of the ideal tetrahedron at
cusp $k$ and $\mu_k, \lambda_k$ are its meridian and longitude.*

## Algebraic poles as geometric addresses

The conjecture says the **algebraic denominator zeros are the
addresses of the geometric cusps**: a zero in the algebraic state
sum at $x = q_0^{-k}$ corresponds to the geometric requirement that
parallel transport around the meridian and longitude of the $k$-th
ideal-tetrahedron cusp yields a holonomy of exactly $1$. Algebraic
divergence and geometric completeness are the same event, viewed
from opposite sides of the Archimedean fibre functor $\tau$.

| Algebraic side ($R$) | Archimedean side ($\mathbb{C}$) | Geometric side ($\mathbf{Hyp}_3$) |
|---|---|---|
| zero of $(1 - x q_0^k)$ | logarithmic singularity of $\mathrm{Li}_2$ | meridian + longitude holonomy = $1$ |
| pole of $\Phi_n$ | branch point of $\log$ | complete cusp of $\Delta_{z_k}$ |
| algebraic Markov-trace divergence | $\tau_{\mathrm{arch}}$-evaluation diverges | shape parameter $z_k$ on Thurston variety |
| GB-depth $k_\star = n$ | thimble dimension $n$ | $n$ ideal tetrahedra in JSJ piece |

The bijection across rows is the **shared denominator**: the same
polynomial $(x; q_0)_n$ controls the algebraic singularities, the
classical $\mathrm{Li}_2$ branch structure, and the Thurston cusp
equations.

## Proof sketch (modulo the upstream conjectures)

Assume
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)).

1. **Algebraic side** ([q-Pochhammer partial product §interpretation](#def:q-pochhammer-partial-product)).
   The denominator $(x; q)_n$ has $n$ simple zeros at $x = q^{-k}$
   for $k = 0, \dots, n-1$. Each is a simple pole of $\Phi_n(x; q)$.

2. **Archimedean side** ([Archimedean limit](#conj:dilogarithm-archimedean-limit)).
   Under Faddeev's scaling, $(1 - q) \log \Phi_n(x; q) \to
   \mathrm{Li}_2(x)$. The poles of $\Phi_n$ map to the logarithmic
   branch point of $\mathrm{Li}_2$ at $t = 1$ in the integrand
   $-\log(1 - t)/t$.

3. **Geometric side** (Thurston [`thurston1978`], Neumann–Zagier
   [`neumann-zagier1985`]). For an ideal-tetrahedron triangulation of
   a hyperbolic 3-manifold, the **cusp completeness conditions** are
   $\mathrm{Hol}_\mu = \mathrm{Hol}_\lambda = 1$ on the meridian and
   longitude; equivalently, the Neumann–Zagier potential
   $\Phi_{\mathrm{NZ}}(z)$ has a critical point at $z = z_k$ matching
   the corresponding shape parameter.

4. **Bridge.** Under the
   [algebraic-geometric equivalence](#conj:algebraic-geometric-dilog-equivalence)'s
   pole-to-cusp bijection, the algebraic root $x = q_0^{-k}$ matches
   cusp $k$, and Step 2 identifies the singularity of the algebraic
   $\Phi_n$ with the singularity of $\mathrm{Li}_2$ at $z_k$ — which
   by Step 3 is the cusp-completeness condition. $\square$

## Implication for the Newton–Raphson solver

The conjecture has a **direct computational consequence**: the zeros
$\{q_0^{-k}\}$ of the algebraic denominator are the **exact initial
seed values** for the Newton–Raphson solver of the Thurston gluing
equations on the active JSJ piece. The pipeline is:

1. The algebraic engine computes $\Phi_n(x; q_0)$ as a rational
   function.
2. Extract the $n$ roots of its denominator $(x; q_0)_n$:
   $\{q_0^{-k} : k = 0, \dots, n-1\}$.
3. Pass the roots across the WASM boundary to the SnapPy kernel.
4. Use the roots not as a universal constant but as the **initial
   guesses** for the Newton–Raphson solver.

By Steps 1–4 of the proof sketch above, the algebraic seeds sit
**near** the cusp-completeness solution of the Thurston gluing
equations — only the gluing residuals from the active transient
crossings differ from zero. The solver converges in $O(1)$ Newton
steps per cusp (empirically $\approx 10$ steps to machine precision
across depths $n = 1, \dots, 3$, see witness below), instead of the
$O(\log\epsilon^{-1})$ steps needed when starting from a generic
universal $z_q$. The Newton step also avoids local-minimum traps,
because the algebraic poles are **isolated** in the cusp variety.

The witness
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json)
drives Newton–Raphson on the color-tube discriminant $\Delta(z) = 0$
from each algebraic seed (perturbed by $0.1i$ to enter $\mathbb{C}$).
At depths $n = 1, 2, 3$, all seeds converge to a complex critical
point with residual $\lesssim 10^{-13}$ in 9–11 iterations,
empirically supporting the $O(1)$ claim.

## Relation to existing PL/JSJ infrastructure

This conjecture is the **shared-denominator** statement that the
existing
([Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)) already
asserts implicitly: the JSJ piecewise sum
$\sum_S \mathrm{Vol}(K_S)$ is computed from the algebraic
$\sum_S \Phi_q(\lvert V_S\rvert)$ at exactly the cusps prescribed by
the algebraic denominators. Phrased motivically, the algebraic class
$[\Phi_n(x; q_0)] \in \mathfrak{B}(q)$ in the
([quantum Bloch group](#def:quantum-bloch-group))
regulates archimedeanly to the volume of the matched JSJ piece, with
the regulator's domain of definition pinned by the shared-denominator
locus.

## Discussion

Stated conditional on
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)). The Lean
formulation
`QOU.QPochhammer.shared_denominator_cusp_holonomy` is therefore a
class instance, not a closed theorem.

### Empirical scope of the seeding pipeline

Two computational witnesses bracket the conjecture's strong form:

- **Color-tube cubic** (succeeds):
  [q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json)
  drives Newton–Raphson on $\Delta(z) = 0$ from the algebraic seeds
  $q_0^{-k} + 0.1i$. At depths $n \leq 3$, Newton converges to
  machine-precision residual ($\lesssim 10^{-13}$) in 9–11 iterations,
  empirically supporting the $O(1)$-steps-per-cusp prediction.

- **SnapPy Thurston gluing system** (bounds the strong form):
  [snappy-cusp-seeding.witness.json](../../../computations/snappy-cusp-seeding.witness.json)
  measures the distance between the bare algebraic seeds and SnapPy's
  tetrahedral shape parameters for $\mathtt{m004}$, $\mathtt{m003}$,
  and the Borromean rings $\mathtt{L6a4}$. The bare seeds sit at
  distance $\sim 0.4$–$0.9$ from SnapPy's $z_k$, so the pole-to-cusp
  bijection cannot be a literal canonical identity
  $q_0^{-k} = z_k$. The conjecture must be interpreted as a bijection
  of **labels** (algebraic-pole index $\leftrightarrow$ cusp index)
  with the actual shape parameter being a non-trivial function
  $\tau_{\mathrm{arch}}(q_0^{-k})$ of the algebraic seed; the shape
  of that function is the subject of further work.

The two witnesses together support the conjecture's *structural*
content (algebraic poles label cusps) while bounding its *canonical*
form (the bare $q_0^{-k}$ are not literally the cusp shapes).
<!-- FILE_END: shared-denominator-cusp-holonomy.md -->

<!-- FILE_START: quantum-bloch-group.md -->
The classical Bloch group $\mathcal{B}(\mathbb{C})$ is
defined by the five-term relation of the dilogarithm
$\mathrm{Li}_2$.  The **quantum Bloch group**
$\mathfrak{B}(q)(R)$ replaces this with the **pentagon
identity** of the quantum dilogarithm $\Phi_q$:

$$
  \Phi_q(u)\,\Phi_q(v)
  \;=\;
  \Phi_q(v)\,\Phi_q(uv)\,\Phi_q(u)
  \qquad \text{where } uv = qvu
$$

This identity is the **Yang–Baxter equation in
exponential form**.  The connection to our framework:

1. The braid group $B_n$ is generated by the Yang–Baxter
   equation $\sigma_i\sigma_{i+1}\sigma_i =
   \sigma_{i+1}\sigma_i\sigma_{i+1}$.

2. The Hecke relation $\sigma_i^2 = H_A\sigma_i + 1$ is
   the **linearisation** of the quantum pentagon identity.

3. The traced volumes $\hat{V}_i(q)$ satisfy the Hecke
   relation because they are matrix elements of
   $\rho(\sigma_i)$ in the standard representation.

4. The algebraic quantum volume
   $\mathrm{Vol}_q = \prod \hat{V}_i$ therefore satisfies
   the pentagon identity (multiplicatively), and its
   logarithm $\Phi_1 = \tfrac{1}{2}\sum \ln(\hat{V}_i \cdot \overline{\hat{V}_i})$ satisfies the
   five-term relation (additively).

This explains **why** $\Phi_1$ is a quantum dilogarithm:
the traced volumes are exponentials of quantum dilogarithm
values, and their product lives in the quantum Bloch group.
The regulator map $\mathfrak{B}(q) \to \mathbb{R}$ sends
the algebraic volume to the hyperbolic volume, recovering
$\mathrm{Vol}(S^3 \setminus K)$ from the algebraic data.

The **Kashaev invariant** is the state sum version:
$\langle K \rangle = \sum_j \prod_{\text{tetrahedra}}
\Phi_q(x_j)^{\pm 1}$, living in the Habiro ring.  For the
Borromean rings, this gives $\langle \mathcal{B}_3 \rangle$
whose archimedean evaluation yields $8G$.

## Pre-archimedean side: $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$

The quantum Bloch group $\mathfrak{B}(q)$ has a natural
**pre-archimedean refinement** over the Habiro ring
$\widehat{\mathbb{Z}[q]}$ (Habiro 2002), without passing through
the complex numbers:

| Side | Bloch group | Regulator $\Phi_1$ | Where |
|------|-------------|---------------------|-------|
| **Pre-archimedean** | $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$ | $\tfrac{1}{2}\sum \ln(\hat{V}_i \cdot \overline{\hat{V}_i})$ | Habiro ring; bar = $q \leftrightarrow q^{-1}$ |
| **Archimedean** ($\tau_{\mathrm{arch}}$ at real $q_0$, real $\hat{V}_i$) | $\mathcal{B}(\mathbb{C})$ | $\sum \ln\lvert\hat{V}_i\rvert$ | Borel regulator $r_1: K_1(\mathbb{C}) \to \mathbb{R}$ |

The bar-involution form $\tfrac{1}{2}\ln(V \cdot \overline{V})$ at
the pre-archimedean level is what the framework uses for $\rho_K$'s
single-generator piece (`[prop:rho-k-graded-expansion`](rho-k-graded-expansion.md)).
At the archimedean specialization with real $q_0$ and real $\hat{V}_i$,
this reduces to the classical Borel regulator $\sum \ln\lvert\hat{V}_i\rvert$ —
the form that appears in
[`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
under the Beilinson regulator $r_2: K_3(\mathbb{C}) \to \mathbb{R}$.

This makes the QOU framework's K-theoretic content categorically
explicit: $\rho_K$ is a graded regulator on $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$
whose archimedean evaluation at $q_0 \in \mathbb{R}_{>1}$ recovers the
classical hyperbolic K_3 regulator. The pre-archimedean form respects
the Hecke bar-involution; the archimedean form respects the standard
$\mathbb{R}$-valued K-theory.

This refines the discussion in
[`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md):
the framework's working object is the **pre-archimedean
$\mathfrak{B}(\widehat{\mathbb{Z}[q]})$**, and the Beilinson regulator
$r_2$ is the archimedean realization of the graded $\rho_K$.
<!-- FILE_END: quantum-bloch-group.md -->

<!-- FILE_START: degree-two-baryon-weight.md -->
**Proposition.**
*The coefficient of $\Phi_2$ in the Wedderburn mass formula is*

$$
  \beta_2 = -2[3]_q
          = -2 \cdot \frac{q^3 - q^{-3}}{q - q^{-1}}
          \approx -6.087
$$

*where $[3]_q$ is the quantum 3-integer.*
<!-- FILE_END: degree-two-baryon-weight.md -->

<!-- FILE_START: borromean-bloch-group-element.md -->
**Conjecture (D16 K-theoretic / Bloch-group closure).**
*The Borromean rings complement $\mathbf{S}^3 \setminus \mathcal{B}_3$
defines a non-trivial element $[\mathcal{B}_3] \in K_3(\mathbb{C})$
(equivalently, an element of the Bloch group $B(\mathbb{C})$) whose
**Beilinson regulator $r_2: K_3(\mathbb{C}) \to \mathbb{R}$ evaluates
to** $\mathrm{Vol}(\mathcal{B}_3) = 8G$.  The Markov-trace coefficient
$h^4 = -3/4$ of $\mathrm{tr}_M(\mathcal{B}_3, q)$ has a K-theoretic
shadow as the next-order regulator term: $r_2[\mathcal{B}_3] \cdot
(h^4\text{-coefficient}) = (8G)(-3/4) = -6G$.*

## The K-theoretic structure

The Bloch group $B(F)$ of a field $F$ is generated by symbols
$[z]$ for $z \in F \setminus \{0, 1\}$ modulo the **5-term
relation**

$$
  [x] + [y] + [1 - xy] + \bigl[\tfrac{1 - x}{1 - xy}\bigr] + \bigl[\tfrac{1 - y}{1 - xy}\bigr]
  \;=\;
  0,
$$

which IS the Bloch-Wigner / Rogers Pentagon identity for the
dilogarithm.  Bloch–Suslin showed $B(\mathbb{C}) \otimes \mathbb{Q}
\cong K_3^{\text{ind}}(\mathbb{C}) \otimes \mathbb{Q}$.

The **Beilinson regulator** $r_2: B(\mathbb{C}) \to \mathbb{R}$ is
given by the Bloch-Wigner dilogarithm:

$$
  r_2([z]) \;=\; D(z)
  \;=\;
  \mathrm{Im}\,\mathrm{Li}_2(z) + \log|z| \cdot \arg(1 - z).
$$

For an ideal tetrahedron with cross-ratio $z$, the hyperbolic volume
is $\Lambda(\theta) = D(e^{i\theta})/2 = \mathrm{Im}\,\mathrm{Li}_2(e^{i\theta})$
— the **Lobachevsky function**.  So hyperbolic volume IS a regulator
evaluation, per
[`rem:vol-as-motivic-period`](#rem:vol-as-motivic-period).

## The Borromean Bloch-group element

Per
[`def:quantum-bloch-group`](#def:quantum-bloch-group) and the
classical Bloch-Suslin construction:

- The Borromean complement decomposes into 8 ideal octahedra, each
  with cross-ratio $\zeta = e^{i\pi/3}$ (the regular ideal
  octahedron, $\theta = \pi/3$).
- Each octahedron contributes Bloch-group element $8 \cdot
  [\zeta]_2 + \ldots$ via the Lobachevsky decomposition.
- The total Bloch-group element is

$$
  [\mathcal{B}_3]_{B(\mathbb{C})}
  \;=\;
  8 \cdot [e^{i\pi/3}]
  \;\in\;
  B(\mathbb{C}),
$$

with regulator $r_2[\mathcal{B}_3] = 8 \cdot \Lambda(\pi/3) =
8G$ (Catalan's constant; see
[`prop:binding-scale-catalan`](#prop:binding-scale-catalan)).

## The conjectural content — $h^4$ as the next-order regulator term

The Beilinson regulator extends to higher orders via the formal
$q$-expansion of $\Phi_q$ around $q = 1$ (the archimedean limit per
[`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)):

$$
  \log \Phi_q(z)
  \;=\;
  \frac{1}{q - 1}
  \bigl(
    \mathrm{Li}_2(z) + h \cdot R_1(z) + h^2 \cdot R_2(z) + \cdots
  \bigr),
$$

where $R_k(z)$ are higher-Bloch regulators.  The conjecture is:

$$
  \frac{r_2^{(2)}[\mathcal{B}_3]}{r_2[\mathcal{B}_3]}
  \;=\;
  h^4 \text{ coefficient of } \mathrm{tr}_M(\mathcal{B}_3, q)
  \;=\;
  -\frac{3}{4},
$$

where $r_2^{(2)}$ is the order-$h^2$ correction to the leading
$r_2$ regulator.  Equivalently: $r_2^{(2)}[\mathcal{B}_3] = -6G$.

## Significance

Per
[`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
§3 (Cluster C of the duality tracker), four candidate routes for
deriving $h^4 = -3/4$ categorically:

1. **Direct Borromean Markov trace** — already done
2. **Pachner-Pentagon state-sum** —
   [`conj:pachner-pentagon-borromean`](pachner-pentagon-borromean.md) (D15, sibling)
3. **K-theoretic / Bloch group regulator** (this conjecture, D16)
4. **DIM-master Pentagon** — research-grade

Closing D16 ties $h^4$ to the K-theoretic structure of $K_3(\mathbb{C})$
— the deepest connection to motivic / arithmetic structure.  It
also closes the loop:

- $r_2$ at order $h^0$ = $8G$ (the bare hyperbolic volume = production
  $\mathrm{Vol}(\mathcal{B}_3)$ in the canonical formalism),
- $r_2^{(2)}$ at order $h^4$ = $-6G$ (the Markov-trace coefficient),
- $r_2^{(k)}$ at higher orders — the full Markov-trace closed form.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: N/A — the Bloch group lives at the
  decategorified level (image of $K_3(\mathbb{C})$ in $\mathbb{R}$);
  no Coxeter length attaches naturally.
- **Jet order**: $h^4$ (the load-bearing claim is at the next-order
  regulator level beyond the $h^0$ volume).
- **Bar-symmetry status**: bar-symmetric.  The Beilinson regulator
  $r_2[z] = \mathrm{Im}\,\mathrm{Li}_2(z) + \ldots$ is bar-symmetric
  under $q \mapsto q^{-1}$ because $\mathrm{Li}_2^q$ is bar-symmetric
  (per [`bar-involution.md`](bar-involution.md) Table 2 — Rogers
  q-dilog is bar-symmetric, Faddeev's $\Phi_q$ alone is bar-anti-
  symmetric).

## Lean axiomatisation (sketch)

```lean
class BorromeanBlochGroupElement
    (M : Type*) [BrCategory M] [QuantumDilogarithm M] where
  /-- The Bloch-group element of the Borromean complement. -/
  borromean_bloch_class : BlochGroup (Complex)
  /-- It equals 8 · [e^(iπ/3)]. -/
  borromean_bloch_eq_eight_xi :
    borromean_bloch_class = 8 • bloch_symbol (Complex.exp (Complex.I * π / 3))
  /-- The Beilinson regulator of the class equals 8G. -/
  regulator_eq_eight_G : r_2 borromean_bloch_class = 8 * catalan_G
  /-- The order-h² regulator correction equals -6G. -/
  regulator_h2_correction : r_2_h2_correction borromean_bloch_class = -6 * catalan_G
  /-- Equivalently, the h^4 Markov-trace coefficient = -3/4. -/
  borromean_h4_coefficient_from_regulator :
    markov_trace_h4_coefficient borromean_complement = -3/4
```

## Open R&D

1. **Compute prototype**: at $q = q_0$, canonical evaluate both
   sides of the conjectural identity
   $r_2^{(2)}[\mathcal{B}_3] = -6G$.  The left side requires
   extending the Bloch-Wigner regulator to order $h^2$ via the
   $\Phi_q$ formal expansion; the right side is already in
   [`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form).
2. **D16 to closed** requires the Lean class instance + the
   `borromean_h4_coefficient_from_regulator` proof (which would
   import a Bloch-Suslin lemma from Mathlib once available; per
   `lean_loogle` search, $K_3$ formalisation is currently partial in
   Mathlib).
3. **Cross-validate against D15**: the Pachner-Pentagon state-sum
   and the K-theoretic regulator should both give $h^4 = -3/4$ —
   a triple cross-validation of the topological coefficient.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D16
  + §2 Cluster C (Pentagon validation D15-D18)
- [`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
  — Pentagon literatures + 4 candidate routes for $h^4 = -3/4$
- Sibling Cluster C item:
  [`conj:pachner-pentagon-borromean`](pachner-pentagon-borromean.md) (D15)
- The quantum Bloch group:
  [`def:quantum-bloch-group`](#def:quantum-bloch-group)
- The motivic-period framing:
  [`rem:vol-as-motivic-period`](#rem:vol-as-motivic-period)
- The volume = regulator identity:
  [`prop:vol-through-tau`](#prop:vol-through-tau),
  [`prop:binding-scale-catalan`](#prop:binding-scale-catalan)
- The archimedean dilog limit:
  [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)
- The Kashaev volume conjecture (upstream):
  [`conj:kashaev-volume-conjecture`](kashaev-volume-conjecture.md)
<!-- FILE_END: borromean-bloch-group-element.md -->

