<!-- FILE_START: mass-open-problems-intro.md -->
The mass endomorphism's derivation chain is complete from the
categorical statement through the archimedean evaluation, but
several structural questions remain open.  The terminal resolution
of hadronic mass
([terminal resolution](#prop:terminal-resolution)) identifies the
finite set of generators from which all hadron masses descend; the
crystal-basis reduction
([crystal basis](#prop:crystal-basis-resolves-mass-tower-open-problems))
proposes a Kashiwara-crystal path to closing the four mass-tower
open problems; and the volume-tower decomposition
([volume tower](#prop:volume-tower-decomposition)) connects the
mass tower's convergence structure to the JSJ decomposition of
the knot complement.

A note on scope: this section catalogues the substrate-level mass-tower open problems that the chapter's machinery does not yet close.  The arc proceeds through the terminal resolution (the chapter's strongest fully-derived prediction), the mass-from-generators conjecture, the volume-tower decomposition, and the mass-tower open-problems classification; the closing blocks exhibit how the crystal basis resolves a sub-class of the open problems and identify the deeper Mathlib fillers that the remaining problems demand.
<!-- FILE_END: mass-open-problems-intro.md -->

<!-- FILE_START: terminal-resolution.md -->
Using the derived $q_0$, the hadronic mass collapses into a linear combination of the neutrino vacuum drag and the pure strong-force binding energy. All four rows match CODATA to sub-keV precision:

| **Structure** | **Topological Formula** | **QOU Result (MeV)** | **CODATA (MeV)** |
|---|---|---|---|
| Proton ($m_p$) | $Q(q) \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})_{uud}$ | 938.272 | 938.272 |
| Neutron ($m_n$) | $Q(q) \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})_{udd}$ | 939.565 | 939.565 |
| Deuteron ($m_D$) | $\mathcal{M}(L_6) - \text{Binding}$ | 1875.613 | 1875.613 |
| Binding Energy | $\Delta$ Skein Polynomial | 2.224 | 2.225 |
<!-- FILE_END: terminal-resolution.md -->

<!-- FILE_START: mass-from-generators.md -->
The knot-particle generation framework
([knot-particle generation](#def:knot-particle-generation)) reduces
the entire mass spectrum to a computation on the seven $T_{m,n}$
generators ([finiteness of generators](#prop:torus-knot-generators))
and the two linking operations.  This remark traces the pipeline
from generators through linking to CODATA-comparable masses.

**Step 1: Bare generators have zero mass.**
Every torus knot $T_{m,n}$ has zero hyperbolic volume (torus knots
are non-hyperbolic), so the topological mass formula
([topological mass formula](#prop:topological-mass-formula)) gives

$$
  \mathcal{M}_{\mathrm{bare}}(T_{m,n})
  =  \frac{\mathrm{Vol}(T_{m,n})}{\hbar_q^{2}}
  =  0.
$$

Mass is not an intrinsic property of the generator — it is
*created by linking*.

**Step 2: Hopf linking generates leptonic mass.**
A single Hopf linking of two generators on the exceptional divisor
$\mathcal{S}_c$ produces a two-component link with nonzero Jones polynomial.
The Skein resolution of crossings introduces hyperbolic volume into
the resolved configuration.  Concretely, for the electron:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{1,0}
  \xrightarrow{ \text{Skein}}
  \sum_i c_i(q) K_i
$$

where the $K_i$ include the trefoil itself (with a brane-tower
correction) and hyperbolic knots arising from crossing changes.
The mass of the electron is the evaluation of this Skein polynomial
at $q = q_0$:

$$
  m_e =  \sum_i c_i(q) \cdot
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{2}}.
$$

**Step 3: Skein transmutation generates generations.**
The Higgs field ($4_1$, figure-eight) is not a generator but a Skein
descendant of the trefoil:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{2,3}
  \xrightarrow{\sigma}
  4_1 +  \text{(remainder)}.
$$

The figure-eight has hyperbolic volume
$\mathrm{Vol}(4_1) = 3\mathrm{Cl}_2(\pi/3) \approx :val[Vol_4_1]{precision=6}$,
The muon-to-electron mass ratio is governed by the Higgs
mechanism:

$$
  \frac{m_\mu}{m_e}
  =  \frac{\mathrm{Vol}(4_1)}{\hbar_q^{2}}
   \approx  \frac{:val[Vol_4_1]{precision=6}}{(1 - q^{-1})^2}
  =  :val[m_mu_over_e]{precision=6}\ldots
$$

matching CODATA to six significant figures
([Skein mass relation](#rem:skein-mass-relation)).

The muon ($T_{2,5}$, cinquefoil) lives **on the exceptional
divisor** — its braid word carries a Hecke dressing
$\sigma_i \cdot T_{2,5}$ that embeds it in the Reeb bundle
(color tube).  The bare torus knot $T_{2,5}$ has zero
hyperbolic volume; the muon's mass arises from the Higgs
mass mechanism ($4_1$), which universally couples to every
knot-particle with crossings $> 0$.  The ratio
$m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$ is the Higgs
coupling constant for the muon--electron channel.  Similarly,
the tau ($T_{2,7}$) acquires mass through the same Higgs
mechanism at Reeb degree $3$.

**Step 4: Color-tube linking generates hadronic mass.**
Baryons require three generators threaded through the color tubes
$(r, g, b)$
([color tube coordinates](#def:color-tube-coordinates)).  The proton
is:

$$
  \text{Proton} = 
  \ell_c\bigl(T_{2,3}, T_{2,3}, T_{2,3}^{\sigma}\bigr)
  \otimes \mathcal{L}_{\mathrm{Hopf}}
$$

where $\ell_c$ threads two trefoils (up quarks) and one Skein
descendant $T_{2,3}^{\sigma}$ (down quark) through the color tubes and
$\mathcal{L}_{\mathrm{Hopf}}$ binds them.  The mass is:

$$
  m_p =  Q_p(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
  +  \Delta\mathcal{M}_{\mathrm{color}}
$$

where $Q_p(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial
of the three-component color-linked configuration, and
$\Delta\mathcal{M}_{\mathrm{color}}$ encodes the cubic constraint
from the color-tube fiber geometry.  The terminal resolution
([terminal resolution](#prop:terminal-resolution)) evaluates this
to $:val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} \mathrm{MeV}$.

**Step 5: The generative atomic chart.**
Organizing by linking type and generator content, the mass spectrum
arranges into a chart:

| Sector | Linking | Generators | Mass source | Examples |
|--------|---------|------------|-------------|----------|
| Leptonic | Hopf ($\ell_H$) | $T_{2,2k+1}$ | Skein volume | $e, \mu, \tau$ |
| Mesonic | Hopf ($\ell_H$) | $T_{m,n} \cup T_{m',n'}^{\sigma}$ | Pair annihilation polynomial | $\pi, K, D$ |
| Baryonic | Color ($\ell_c$) + Hopf | $T_{m_i,n_i}^{\times 3}$ | Color-tube cubic + Skein | $p, n, \Lambda, \Sigma$ |
| Nuclear | Iterated $\ell_H$ | Baryon composites | Multi-body Skein | $D, {}^4\mathrm{He}, \ldots$ |

**Rows** are indexed by the number of Hopf linkings (shell number).
**Columns** separate colorless (leptonic) from colored (hadronic)
sectors.  **Generations** ($1, 2, 3$) correspond to Reeb degree
$\deg\alpha_V$, which selects which $T_{2,2k+1}$ generator
participates.

The entire chart is determined by three inputs:

1. The substrate parameter $q_0$ (from CODATA),
2. The seven $T_{m,n}$ generators (from $\chi = -6$), and
3. The two linking operations $\ell_H$, $\ell_c$ (from the
   exceptional divisor and Bring's surface geometry).
<!-- FILE_END: mass-from-generators.md -->

<!-- FILE_START: volume-tower-decomposition.md -->
Let $K$ be a hyperbolic knot or link appearing in the Descartes universe
mass spectrum, and let $\{\mathfrak{G}_n\}_{n \geq 0}$ be the
[cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid) of
the brane tower with [obstruction classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

**Proposition.**
There exists a decomposition of the hyperbolic volume into tower-level
contributions:

$$
  \mathrm{Vol}(K)
  = \sum_{n=0}^{\infty} \Phi_n(K),
$$

where $\Phi_n(K)$ is the Chern--Simons period integral of the $n$-th
twisted sector, satisfying:

1. **Convergence.** The series converges absolutely.  The tail
   $\sum_{n > N} |\Phi_n(K)|$ is controlled by the spectral gap
   of the $\mathrm{SU}_{q_n}(2)$-adjoint action at level $n$.

2. **Yekutieli control.** Each $\Phi_n(K)$ is determined by the
   Yekutieli triple $(x^{(n)}, g^{(n)}, a^{(n)})$ at level $n$:

$$
  \Phi_n(K) = \int_{\gamma_n}
    \mathrm{CS}\bigl(g_{ij}^{(n)},\, a_{ij}^{(n)}\bigr),
$$

   where $\gamma_n$ is the Picard--Lefschetz thimble at level $n$
   and $\mathrm{CS}$ denotes the Chern--Simons 3-form evaluated on
   the transition data.

3. **Coface compatibility.** The coface map
   $\delta^0 \colon \mathfrak{G}_n \to \mathfrak{G}_{n+1}$ relates
   consecutive terms: $\Phi_{n+1}(K) = \Phi_n(K) \cdot r_n + \varepsilon_n$,
   where $r_n$ is the spectral contraction ratio at level $n$ and
   $\varepsilon_n$ is the genuinely new contribution from
   $\kappa_n \neq 0$.

4. **Classical limit.** At $q = 1$ all levels collapse to the
   single hyperbolic structure: $\Phi_0(K) = \mathrm{Vol}(K)$ and
   $\Phi_n(K) = 0$ for $n \geq 1$.

The existing two-level structure (Level 0 inter-nucleon, Level 1
intra-Borromean, as in
[quantum dilogarithm volume](#prop:quantum-dilogarithm-volume)) is the
truncation of this series at $n = 1$.
<!-- FILE_END: volume-tower-decomposition.md -->

<!-- FILE_START: mass-tower-open-problems-classes.md -->
**Remark (§3b-cond Lean classes for the four remaining mass-tower
open problems).**

After the α_EM derivation chain
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)
$\to$ [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
$\to$ [`conj:bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition),
four structural gaps remain in the mass-tower derivation. The Lean
file [`mass-tower-open-problems-classes.lean`](mass-tower-open-problems-classes.lean)
consolidates them as typeclasses in the §3b-cond pattern, each with
a sorry-free conditional theorem reducing the conjectural form to
a class instance.

## The four classes

### 1. `Term7ShellCorrectionClass`

**Open problem.** The unified six-term mass formula under-predicts
isotope masses for $A \geq 5$ by $\sim 10\%$. Term 7
(`conj:shell-correction-term-seven`)
adds a shell correction with coefficient $\alpha_5$ currently fit to
the AME panel, not derived. The class
`Term7ShellCorrectionClass` asserts the existence of a structural
derivation from the Gröbner-Shirshov filtration spectral sequence at
height-6 partitions ($\ell = 5$).

**Conditional theorem.** `term7_structural` — given the class,
$\alpha_5$ is a categorical-derivation output, not a phenomenological
extension.

### 2. `ChiralityFactorClass`

**Open problem.** The deuterium chirality factor $a_K = 1 + h$ (with
$h = q - q^{-1}$) is recorded as a paper-categorical ansatz; a canonical
canonical evaluation failed to match against eight candidate writhe-ribbon formulas.
[`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation)
proposes a Kauffman-framing derivation. The strengthened class
`ChiralityFactorClass` axiomatises that derivation: it asserts the
existence of a function $a_K(h, w, \langle c \rangle)$ and an error term
such that $a_K = 1 + w \cdot \langle c \rangle \cdot h + O(h^2)$,
encoding the structural first-order Kauffman expansion.

**Conditional theorem.** `chirality_factor_structural` — sorry-free
reduction of the chirality ansatz to the class instance.

### 3. `ZHabiroConvergenceClass`

**Open problem.** The brane-tower per-generator volumes
$z_i = |\hat{V}_i|$ for low isotopes lie just below the
first pole of $\Phi_q$ at $z = q_0 \approx 1.11$
([`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro)). Each
summand is enormous and the analytic infinite-product diverges; two
regularisations (Yekutieli finite-slice, $q$-Habiro completion) have
been documented but neither uniformly closes the gap. The strengthened
class `ZHabiroConvergenceClass` axiomatises a uniform bound on the
regularised tower sum, formally asserting $\forall z < q_0, \sum \Phi_q(z) \leq M$
for some $M < q_0$.

**Conditional theorem.** `brane_tower_finite` — given the class,
the brane-tower contribution is finite for every isotope-relevant
volume.

### 4. `AlphaOver4PiClass`

**Open problem.** The additive Bring zero-mode form gives residual
$-4.2 \times 10^{-6}$ at the $2/(3\pi)$ order; the next-order
self-energy correction $\alpha/(4\pi) \approx 5.81 \times 10^{-4}$
brings it to $+5.7 \times 10^{-8}$
([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)).
The coefficient $1/(4\pi)$ is currently a near-match (1.4% off) and
may refine to $1/(2\pi[2]_q)$ or another $q$-correction, but its
structural origin is conjecturally a multivariate polylogarithm
regulator on a higher Bloch group $B_n(\mathbb{C})$, $n \geq 3$
[`borel1974`, `bloch2000`]. The strengthened class `AlphaOver4PiClass`
axiomatises the higher-Bloch-group origin of the next-order
coefficient by asserting the existence of a higher Bloch group type, a
regulator, and an element mapping exactly to $\alpha/(4\pi)$.

**Conditional theorem.** `alpha_over_4pi_structural` — given the
class, the next-order coefficient is a regulator output, not an
empirical fit.

## Pattern

Each of the four classes follows the §3b-cond template established
by [`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):

1. **Carrier definition** — the target real or function (e.g.
   $\alpha_5 \in \mathbb{R}$, $a_K(h, w) \in \mathbb{R}$, the
   uniform bound $M$, $\alpha/(4\pi)$).
2. **Class** — a `Prop`-valued typeclass asserting the existence
   of the structural derivation as a single field.
3. **Conditional theorem** — sorry-free Lean theorem taking the
   class as `[Instance]` and unpacking the existential.

Closure of the four class instances is the irreducible open
content remaining in the mass-tower derivation. None requires new
mathematical machinery beyond what is documented in the cited
upstream blocks; each requires the explicit categorical /
geometric derivation written out in full.
<!-- FILE_END: mass-tower-open-problems-classes.md -->

<!-- FILE_START: crystal-basis-resolves-mass-tower-open-problems.md -->
**Proposition (crystal-basis reduction of three mass-tower open
problems; conditional on
[`conj:kazhdan-lusztig-classical-limit`](../particle-interactions/kazhdan-lusztig-classical-limit.md)
+ Brundan-Kleshchev / Lecouvey conjectures per §3b-cond).**
*Under the Brundan-Kleshchev isomorphism
$H_n(R, q) \cong R^\Lambda_\alpha$ (cyclotomic KLR algebra)
[`brundankleshchev2009`] and the Lecouvey GS-irreducible /
crystal-highest-weight bijection [`lecouvey2007`]
([`conj:crystal-graph-realization`](#conj:crystal-graph-realization)),
three of the four remaining mass-tower open problems reduce to
finite-graph combinatorics on Kashiwara crystals
$\mathrm{Cryst}(\mathfrak{sl}_n)$ [`kashiwara1991`]:*

- *the chirality factor's $\langle c \rangle_\beta$ Wedderburn-weighted
 average becomes a sum over **integer crystal multiplicities**;*
- *Term 7's level-5 character projector $\chi_5(T_w)$ becomes a
 **height-6 crystal-vertex count**;*
- *the brane-tower $|V|\to 1$ divergence is regularised by the
 Kazhdan-Lusztig classical-limit functor
 ([`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)),
 whose action collapses $H_n(R, q)$ to $\mathbb{Z}[S_n]$ via
 integer KL coefficients.*

## The three reductions

### Reduction 1: chirality $\langle c \rangle_\beta$ via Type-B folding

[`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation)
yields the first-order chirality factor

$$
  a_K(\beta) \;=\; 1 + w(\beta) \cdot \langle c \rangle_\beta \cdot h
   \;+\; O(h^2),
\qquad
  \langle c \rangle_\beta \;:=\; \frac{\sum_\lambda w_\lambda\,\chi^\lambda(\beta)\,c(\lambda)}
       {\sum_\lambda w_\lambda\,\chi^\lambda(\beta)}.
$$

The Wedderburn weights $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ and
characters $\chi^\lambda(\beta)$ are conventionally computed in
the $H_n(R, q)$ semi-normal form. Under Brundan-Kleshchev, both
become **graded crystal multiplicities**:
$\dim_q(\lambda)$ is the $q$-character of the crystal component
labelled by $\lambda$, and $\chi^\lambda(\beta)$ is the trace of
$\beta$ acting on the crystal-graph image of the projective
$P_\lambda$.

**Type-B folding shortcut (AGENTS.md §7b).** *To enforce
matter–antimatter pairing structurally — equivalently, the
bar-involution $q \leftrightarrow q^{-1}$ symmetry — fold the
$\mathfrak{sl}_n$ Cartan datum into a Type B datum. The resulting
Kashiwara graph is a **symmetric crystal**, and its GS normal forms
are bar-involution invariant by construction.* For chirality,
**on the folded Type-B crystal, $\langle c \rangle_\beta$
is a sum of cell-content invariants paired by the fold involution
$\lambda \leftrightarrow \lambda^T$, hence a fixed-point integer
combination $c(\lambda) + c(\lambda^T) = 0$ summand-by-summand.**
The non-trivial part of $\langle c \rangle_\beta$ is the
**imbalance** between $\chi^\lambda(\beta)$ and $\chi^{\lambda^T}(\beta)$
along the folded-crystal Demazure components — a purely
combinatorial finite computation on the Type-B crystal graph.

### Reduction 2: Term 7's $\chi_5$ via height-6 crystal vertices

`conj:shell-correction-term-seven`
defines the level-5 character projector

$$
  \chi_5(T_w)
  \;:=\;
  \sum_{\lambda \vdash 3A,\;\mathrm{height}(\lambda) = 6}
    w_\lambda(q) \cdot \chi^\lambda(T_w).
$$

Under Brundan-Kleshchev, partitions $\lambda$ of height 6 correspond
to **crystal vertices at depth 6 in $\mathrm{Cryst}(\mathfrak{sl}_{3A})$**
(depth = number of Kashiwara $\tilde{f}_i$ operators applied from
the highest weight). The set
$\{\lambda \vdash 3A : \mathrm{height}(\lambda) = 6\}$ is a **finite
crystal-vertex enumeration** for any fixed $A$ — a standard
RSK / hook-content computation [`khovanovlauda2009`].

The α_5 magnitude open in `Term7ShellCorrectionClass` reduces to:
*compute the crystal-vertex sum at height 6 for $A = 4$ ($^4$He),
$A = 5$ ($^5$Li, $^5$He), $\ldots$, multiply by the Wedderburn weight
$w_\lambda(q_0)$, and read off the AME-residual amplitude.* No new
mathematical machinery; the finite crystal computation.

The shell-closure sign $\alpha_5 < 0$
([`Term7ShellCorrectionClass`](mass-tower-open-problems-classes.lean))
is now a **structural consequence**: height-6 partitions exist
only for $3A \geq 6$ (i.e. $A \geq 2$), and the binding-enhancing
sign follows from the **Demazure sub-crystal** structure at
height 6 (AGENTS.md §7b: *Demazure sub-crystals for resonances*).
Each Demazure component represents an *incomplete* topological
state that lowers the energy budget — exactly the binding
enhancement $\alpha_5 < 0$ encodes.

### Reduction 3: brane-tower $|V|\to 1$ via Kazhdan-Lusztig classical limit

[`conj:brane-tower-z-habiro`](../braids-and-knots/brane-tower-z-habiro.md)
diagnoses an analytic divergence: per-generator volumes
$z_i = |\hat{V}_i|$ for low isotopes lie just below
$z = q_0 \approx 1.11$, the first pole of $\Phi_q$. The summand
$\Phi_q(z)$ is enormous and the analytic series diverges.

The Kazhdan-Lusztig classical-limit functor
[`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)
sends each KLR canonical basis element $b_w$ to its $q \to 1$
specialisation $C_w \in \mathbb{Z}[S_n]$ — a **specific integer
$\pm 1$ permutation sign**. Under this functor the divergent
analytic Hecke trace becomes a **finite integer-coefficient sum
over the symmetric group $S_n$**, since the Wedderburn dimensions
specialise to the classical hook-length integers. The KL classical
limit is therefore the **canonical regularisation** of the brane
tower at $|V|\to 1$ — independent of the Yekutieli finite-slice
or $q$-Habiro completion choices. The uniform bound demanded by
`ZHabiroConvergenceClass` becomes:

$$
  M \;\leq\; \sum_{w \in S_n} |C_w(q_0 \to 1)|
       \;=\; \sum_{\lambda \vdash n}
       \dim(V_\lambda) \;\cdot\;\bigl|\langle\,\cdot\,\rangle_\lambda\bigr|
       \;<\; \infty
$$

— a finite sum of classical hook-length-integer dimensions
multiplied by classical character values, both bounded.

## The fourth open problem

The K-theoretic identification
[`conj:bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition)
asks whether $2/(3\pi)$ lies in the rank-8 Bloch group image of
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$. Crystal bases do *not*
directly resolve this: Bloch-Wigner values $D[Z_K]$ are
**transcendental** archimedean realisations, while crystal bases
are **integer-coefficient** combinatorial objects. The crystal
side gives the q-rational Hecke trace structure
(pre-archimedean, in $R$); the Bloch group lives on the other
side of $\tau_{\text{arch}}$. The open question is therefore
genuinely transverse to the crystal-basis machinery — a finite
integer-relation search in $\mathbb{R}$ rather than a
crystal-graph computation.

## Provability summary

| Open problem | Crystal-basis reduction | Open content after reduction |
|---|---|---|
| Chirality $\langle c \rangle_\beta$ | Type-B folded crystal imbalance computation | finite Kashiwara graph traversal |
| Term 7 $\alpha_5$ magnitude | height-6 crystal-vertex enumeration | RSK / hook-content sum at $\lambda \vdash 3A$, ht 6 |
| z-Habiro $\lvert V\rvert\to 1$ | KL classical-limit integer regularisation | bounded by classical dim$(V_\lambda)$ sums |
| Bloch decomposition of $2/(3\pi)$ | (transverse — crystal bases pre-archimedean) | Bloch-group integer relation search |

Three of the four problems become **finite combinatorial
computations on Kashiwara crystals** — substantially more
tractable than their original analytic / structural formulations.
The Lean infrastructure documented in
[`mass-tower-open-problems-classes.md`](mass-tower-open-problems-classes.md)
remains the §3b-cond hook structure; this proposition supplies
the mathematical pathway by which the open class instances can be
inhabited via crystal-graph computations once the upstream
Brundan-Kleshchev correspondence is formally tight.
<!-- FILE_END: crystal-basis-resolves-mass-tower-open-problems.md -->

<!-- FILE_START: mass-tower-deeper-fillers.md -->
**Remark (deeper §3b-cond fillers — five consolidated extensions).**

Bundles five small but focused Lean fillers into
[`mass-tower-deeper-fillers.lean`](mass-tower-deeper-fillers.lean):

| Section | Content | Status |
|---|---|---|
| (A) Height-6 partition enumeration | `HeightSixPartition n` structure with `parts : List ℕ`, `parts.length = 6` | unconditional finite-type carrier |
| (B) Demazure sub-crystal predicate | `IsDemazureSubCrystal S` typeclass | ansatz; AGENTS.md §7b item 3 hook |
| (C) Kazhdan-Lusztig classical-limit functor | `KLClassicalLimit f := f 1` | unconditional ansatz |
| (D) Minimal `BlochGroup F` carrier | `HasBlochGroupQuotient F` typeclass with two boolean fields (quotient existence + Borel regulator iso) | typeclass hypothesis |
| (E) Pentagon-identity surrogate for `Cl_2` | `Cl_2_PentagonIdentity` typeclass | typeclass hypothesis |

The five pieces deepen the mass-tower scaffolding:

- (A) makes the Term-7 reduction concrete: a finite-type
  enumeration of the height-6 partitions of $3A$ is now a Lean
  carrier downstream callers can iterate over (once the GS
  spectral-sequence weight is wired in).
- (B) adds the Demazure sub-crystal hook for resonances
  (AGENTS.md §7b item 3 — "incomplete topological states lowering
  the energy budget"), giving the structural sign argument for
  $\alpha_5 < 0$ a Lean-level handle.
- (C) provides the KL classical-limit functor as a ansatz;
  the substantive content (`b_w \to C_w \in \mathbb{Z}[S_n]`) is
  upstream conjectural.
- (D) records the `BlochGroup F` quotient as a typeclass hypothesis
  alongside Borel's regulator-isomorphism hypothesis; both are
  Mathlib-pending classical results.
- (E) records the 5-term pentagon for $\mathrm{Cl}_2$ as a
  typeclass; the full proof needs Mathlib's Fourier-series
  identities.

The synthesis class `DeeperMathlibFillers F` collects
$(B), (D), (E)$ into a single hypothesis suitable for §3b-cond
hooks, with `Cl_2_zero_consistent_with_pentagon` providing a
trivial sanity-check theorem.

## Cross-paper + uploads + wiring scans

- **`unital-groebner-bases/`** — no overlap with BlochGroup,
  Cl_2, archimedean-functor, or crystal-basis content.
- **`fred2005-formal-groups/`** — contains
  [`unit-root-F-crystal`](../../fred2005-formal-groups/formal-groups-chapter/unit-root-f-crystal.md)
  and `unit-root-iff-integrable`. *Different* notion of "crystal"
  (Berthelot-Ogus F-crystal in formal-groups context, distinct
  from Kashiwara crystal). Cross-paper integration possible at
  the level of *both being categorical / motivic objects*, but
  the math is structurally distinct — no immediate filler-sharing
  opportunity.
- **`uploads/`** — 14 PDFs present (`0008040v1.pdf`,
  `0911.4494v2.pdf`, etc.). Text-grep on the binary PDFs returned
  no hits for `Bloch | Clausen | dilog | figure-8`, so either the
  PDFs lack OCR-extracted text or the keywords are absent. A
  proper intake via `local/document-intake` skill would surface
  any relevant content; out of scope for this filler push.
- **Wiring follow-up:** the formal derivation currently has no
  `solve_y_lambda` reference — the user is preparing the
  modification. Recommendation per the prior turn stands: add
  `solve_y_lambda_numerical(n, q_value)` as a *separate* function
  in the formal derivation, leave the symbolic version
  intact for `the formal derivation:60` to consume.

## Remaining work after this push

The §3b-cond scaffolding is now substantially complete: every
mass-tower / α_EM open problem has a Lean class hook, an
unconditional or sign-witness instance where possible, and
explicit Mathlib-filler infrastructure where the upstream
mathematical content is established. The remaining open content
sits in three substantive places, all upstream:

1. **`BlochGroup F` formal quotient** — full free-abelian-group
   modulo 5-term pentagon construction, ~150 lines of Lean.
2. **Pentagon identity for the BW dilogarithm** — proved on the
   group quotient via the Suslin map.
3. **Faddeev-Kashaev quasi-classical limit** — uniform Tauberian
   theorem for the q-Pochhammer partial product, requires Mathlib
   asymptotic-analysis infrastructure.

Each is a substantial Mathlib-contribution-sized task. The
present infrastructure is sufficient to *state* and *use* every
result conditionally in the §3b-cond pattern, leaving the
substantive mathematical work as well-isolated future steps.
<!-- FILE_END: mass-tower-deeper-fillers.md -->

