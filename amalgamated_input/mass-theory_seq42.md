<!-- FILE_START: intro-parity-classification-discrepancy.md -->
The classical $m_n$ assignment is parity-blind — it cannot
distinguish a knot from its mirror image — and this blindness
shows up empirically as a small but systematic discrepancy
between the substrate-level mass prediction and the CODATA value.
This section diagnoses the discrepancy, exhibits the parity
classification that resolves it, and assembles the atomic-atlas
table that records the resolution per-element.

The arc starts with the parity-blind diagnosis, traces the
discrepancy to the categorical chirality pairing, and exhibits
the resolution via the augmented parity classification.  The
closing blocks tabulate the atomic atlas (the per-element
parity / chirality table) and identify the cases where the
discrepancy resolution is unambiguous versus those where the
substrate-flow ambiguity propagates.
<!-- FILE_END: intro-parity-classification-discrepancy.md -->

<!-- FILE_START: mn-classical-parity-blind.md -->
**Remark.**
*The classical Murnaghan–Nakayama recursion computes characters
$\chi^\lambda(\sigma)$ of the symmetric group $S_n$ on a permutation
$\sigma$ specified by its cycle type.  When applied to the
$S_{3A}$-projection $\pi(\mathcal{A})$ of the atomic braid word
$\mathcal{A}$, the classical Specht character $\chi^\lambda(\pi(\mathcal{A}))$
cannot distinguish a proton from a neutron, because the two
have identical permutation images.*

**Computational evidence.**
*Using the formal derivation:*

See [Table](#tbl:mn-classical-parity-blind-table-data).

*Proton and neutron collapse onto the same cycle type $(2, 1)$
because both atomic-braid words have an odd number of crossings at
generator $0$ and an even number at generator $1$ — so the
parity pattern is identical.  At the $S_n$ level, positive and
negative crossings $\sigma_i^{\pm 1}$ project to the same
transposition $(i, i+1)$.*

**Origin of the loss of information.**
*The Hecke algebra $H_n(R, q)$ has two eigenvalues for each Hecke
generator: $\sigma_i$ has spectrum $\{q, -q^{-1}\}$.  The q-deformed
character $\chi^\lambda_q(\sigma_w)$ distinguishes these eigenvalues
through q-weighted ribbon tableaux — a positive crossing and a
negative crossing contribute **different** q-factors to the same
ribbon removal.  In the classical limit $q \to 1$, the two
eigenvalues collide at $\{+1, -1\}$ but the character becomes the
plain $S_n$-character, which only sees the transposition
(parity-blind).*

*Consequence: the **classical Murnaghan–Nakayama is the wrong
character** for mass predictions.  It captures the correct
partition support $\{\lambda : \chi^\lambda(\pi(\mathcal{A})) \neq 0\}$
but the wrong weights for atoms that differ only in $\sigma^{\pm 1}$
content (like $\mathfrak{p}$ vs $\mathfrak{n}$).  Any $\beta$-decay
calibration $E_0 = 0.782\;\mathrm{MeV} / (|\mathrm{tr}_M(\mathfrak{n})|
- |\mathrm{tr}_M(\mathfrak{p})|)$ fails because the classical
difference is zero.*

**Structural value of the classical computation.**
*Even though the classical MN gives zero proton–neutron splitting,
the computation is valuable as a **structural diagnostic**:*

1. *It identifies exactly which partitions $\lambda \vdash 3A$
   carry nonzero Schur–Weyl weight for each atom.*
2. *The partition set is sparse: for $A = 4$ only $5$ of the
   $77$ partitions of $12$ contribute.*
3. *Because the q-deformed character $\chi^\lambda_q$ has the same
   support as $\chi^\lambda$ (ribbon removability is a shape
   property, not a q-weight property), the classical support
   list **is** the support list for the full Hecke character.*
4. *The full mass calculation therefore requires evaluating
   q-deformed $\chi^\lambda_q(\sigma_w)$ only on this pre-computed
   support — a substantial pruning of the partition sum.*

**Next step: q-deformed ribbon characters.**
*The full Hecke-algebra character is*

$$
  \chi^\lambda_q(\sigma_w)
  \;=\;
  \sum_{\text{ribbon tableau of shape } \lambda}
    q^{\operatorname{charge}(\text{tableau})}
    \cdot (\text{sign accounting for } \sigma^{\pm 1}),
$$

*a q-weighted version of the Murnaghan–Nakayama sum.  Ram and
Wenzl (1992) give explicit formulas for small cases, and the
general ribbon-q-weight recipe is in the Ram 1991 thesis.
Implementing this recipe over the Murnaghan–Nakayama support
identified here closes the proton–neutron splitting gap and is
the natural next iteration of the symbolic engine.*

**Reference implementation.**
*formalism: the formal derivation.
Uses the formal derivation (classical MN recursion) and
the formal derivation (global $H_{3A}$ sum with q symbolic).
Witness file: `schur-weyl-mn.witness.json`.  Evaluation time: 
a few seconds for $A \leq 3$, under a minute for $A = 4$ (77
partitions).*
<!-- FILE_END: mn-classical-parity-blind.md -->

<!-- FILE_START: q-character-closes-parity-gap.md -->
**Remark.**
*The parity-blindness of the classical Murnaghan–Nakayama character
([MN parity-blind](#rem:mn-classical-parity-blind)) is closed by
the $q$-deformed Hecke character $\chi^\lambda_q(\sigma_w)$.  Computed
symbolically via the Hoefsmit seminormal form, the $q$-character
distinguishes $\sigma$ from $\sigma^{-1}$ through the Hecke
eigenvalue gap $(q, -q^{-1})$ and therefore distinguishes proton
from neutron at every $q$.*

**Hoefsmit seminormal form (symbolic).**
*For a partition $\lambda \vdash n$ with standard Young tableaux
$T_1, \ldots, T_{f^\lambda}$ (indexing the Specht-module basis;
distinct from the Hecke generator $\sigma_i$), the Hecke generator
$\sigma_i$ acts on the Specht module $S^\lambda$ by:*

- *If $i$ and $i+1$ are in the same row of $T$ (axial distance
  $\rho = 1$): $\rho_\lambda(\sigma_i)\,T = q \cdot T$.*
- *If in the same column ($\rho = -1$): $\rho_\lambda(\sigma_i)\,T =
  -q^{-1}\,T$.*
- *Otherwise: $2 \times 2$ block on $\{T, T'\}$ with $T'$ the
  tableau obtained by swapping $i, i+1$, matrix
  $\begin{pmatrix} a & b \\ b & a' \end{pmatrix}$ where
  $a = (q - q^{-1})/(1 - q^{-2\rho})$,
  $a' = (q - q^{-1})/(1 - q^{2\rho})$,
  $b^2 = a a' + 1$, $\rho = \mathrm{content}(c_{i+1}) -
  \mathrm{content}(c_i)$.*

*Keeping $q$ as a sympy symbol,
$\chi^\lambda_q(\sigma_w) =
\operatorname{Tr}\bigl(\prod_{i \in w} \rho_\lambda(\sigma_i^{\,\varepsilon_i})\bigr)$,
where $\varepsilon_i = \pm 1$ is the sign of the $i$-th letter in $w$,
is an exact rational function of $q$.*

**canonical witness at $A = 1$ ($q_0 \approx 1.11$).**

| $\lambda \vdash 3$ | $\chi^\lambda_q(\sigma_w^{\mathfrak{p}})$ @ $q_0$ | $\chi^\lambda_q(\sigma_w^{\mathfrak{n}})$ @ $q_0$ | difference |
|---|---|---|---|
| $(3)$ | $+1.3825$ | $+1.1221$ | $+0.2604$ |
| $(2,1)$ | $+3.1902$ | $+2.3874$ | $+0.8028$ |
| $(1,1,1)$ | $+4.2587$ | $+2.7419$ | $+1.5167$ |

*All three partitions differ nontrivially between proton and
neutron — in sharp contrast to the classical MN case where all
characters were identical.*

**Schur–Weyl trace at $A = 1$:**

$$
  |\mathrm{tr}_M(\mathfrak{p})|_{q_0} = 3.036, \qquad
  |\mathrm{tr}_M(\mathfrak{n})|_{q_0} = 2.331, \qquad
  Q_{\mathrm{cat}} = -0.7052.
$$

*$\beta$-decay calibration now succeeds:
$E_0 = 0.782\,\mathrm{MeV} / |Q_{\mathrm{cat}}| = 1.109\,\mathrm{MeV}$/cat.unit.
The q-deformation restores the structural information lost in
the classical limit.*

**Mechanism by which the $q$-character sees the sign.**
*A positive crossing $\sigma_i$ and a negative crossing $\sigma_i^{-1}$
project to the same $S_n$ transposition (parity-blind at $q = 1$),
but as elements of $H_n(R, q)$ they are distinct: $\sigma_i$ has
eigenvalue $+q$ on the symmetric channel and $-q^{-1}$ on the
antisymmetric channel, while $\sigma_i^{-1}$ has $q^{-1}$ and $-q$.
The seminormal matrix for $\sigma_i$ and $\sigma_i^{-1}$ differ:*

$$
  \rho_\lambda(\sigma_i)
  \;=\;
  \begin{pmatrix} a & b \\ b & a' \end{pmatrix},
  \qquad
  \rho_\lambda(\sigma_i^{-1})
  \;=\;
  \begin{pmatrix} a' & b \\ b & a \end{pmatrix}
  \;=\;
  \rho_\lambda(\sigma_i) - (q - q^{-1}) \cdot I.
$$

*(The Hecke inverse identity
$\sigma_i^{-1} = \sigma_i - (q - q^{-1}) \cdot I$ gives the clean form
on the right.)  Tracing through a braid word with mixed
$\sigma^{\pm 1}$ crossings accumulates a net $q$-dependence that
distinguishes the proton word (majority $\sigma$) from the
neutron word (majority $\sigma^{-1}$).*

**Computational cost and scope.**
*Symbolic Hoefsmit matrix products are $O(d^3)$ per generator in
sympy, where $d = \dim S^\lambda = f^\lambda$:*

- *$A = 1$: $f^\lambda \in \{1, 2, 1\}$, fast; the values above
  are exact.*
- *$A \geq 2$: $f^\lambda$ up to $16$ (for $\lambda = (3,2,1)$
  at $A=2$) and up to $132$ at $A=4$; symbolic cost becomes
  prohibitive.  For $A \geq 2$ use the **canonical**
  Hoefsmit pipeline in
  the formal derivation
  (well-tested, handles 2$\times$2 block $b^2$ sign with
  `sqrt(abs(b^2))` where the symbolic expression can turn
  negative off the unitary locus).*

**Correction to an earlier claim.**
*An earlier draft asserted that the classical Murnaghan–Nakayama
character's support equals the Hecke $q$-character's support
(i.e., MN-support pruning is valid).  This is **false** for
general braid words.  It holds only when $\sigma_w$ is a pure
standard-basis element $T_v$ for some $v \in S_n$: then
$\chi^\lambda_q(T_v)$ is a $q$-deformation of $\chi^\lambda(v)$
and shares its support.  For a braid word $T_{i_1}T_{i_2}\cdots
T_{i_k}$ with mixed $\sigma^{\pm 1}$, the Hecke relations
$\sigma_i^2 = (q-q^{-1})\sigma_i + I$ expand the product into a linear
combination $\sum_v c_v(q)\,T_v$ over many $v$ with different
cycle types.  The $q$-character pulls in all of them, so the
effective support can be strictly larger than the
MN-support on any single $v$.  Pruning to the MN-support at
$A \geq 2$ produces a **biased** result and is not used.*

**Reference implementation.**
*formalism: the formal derivation.
Builds Hoefsmit matrices with `q` as sympy symbol, multiplies
through atomic braid word, traces to extract $\chi^\lambda_q(\sigma_w)$.
Witness: `hecke-character-symbolic.witness.json`.*

**Next step.**
*Apply the categorical derivation steps in
the formal derivation (full $H_{3A}$
Wedderburn sum) to $A = 2$ (deuteron) with all $11$ partitions of
$6$, weighted by the exact symbolic $w_\lambda(q_0)$.  The
canonical Hoefsmit handles the 2$\times$2 block $b^2$ sign robustly.
This is the final piece needed for deuteron binding energy from
first principles — the only inputs are $E_0$ ($\beta$-decay) and
$q_0$ (substrate).*
<!-- FILE_END: q-character-closes-parity-gap.md -->

<!-- FILE_START: frobenius-codim-universal.md -->
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
  ([Hecke mass element](#def:hecke-mass-element)).  Each vortex has
  a Hecke-algebra representative $\sigma_w \in H_n(R, q)$ whose Markov
  trace is the categorical mass
  ([categorical mass, Markov](#prop:categorical-mass-markov)).
  In physics: particles (quarks, nucleons, nuclei) are vortices.

* **$C_{\dim_q}$**: the "C" stands for **Casimir** (Lie-algebra /
  TQFT terminology); "co-" because it is the Frobenius-pairing
  dual of the unit $1 = \sum_\lambda p_\lambda$, **not** the
  standard quadratic Casimir $\Omega = \sum_i e_i \otimes e^i$.
  See §"Uniqueness of $C_{\dim_q}$" below.

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
<!-- FILE_END: frobenius-codim-universal.md -->

<!-- FILE_START: frobenius-codim-universal-interpretation.md -->
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
([proton residual](#prop:partition-sum-proton-residual)) and its
extensions to nuclear bindings.  The specific value
$\tau(C_{\dim_q})$ depends on the algebra $A$ (hence on the
vortex content), but the **structural form** — trace of the
Frobenius co-dimension element — is universal.*
<!-- FILE_END: frobenius-codim-universal-interpretation.md -->

<!-- FILE_START: frobenius-limits-substrate-cost.md -->
**Remark.**
*The Frobenius co-Casimir trace
([universal Frobenius co-dimension](#thm:frobenius-codim-universal))*

$$
  \tau(C_{\dim_q}^{H_n(R, q)}) \;=\; \sum_{\lambda \,\vdash\, n} \frac{1}{\dim_q(\lambda)}
$$

*has a regular limit structure across all $n$, with a clean
physical interpretation as the **substrate's fundamental cost
of information exchange** — independent of the specific vortex
being processed.*

**Limits (verified symbolically for $n = 3, 4, 5, 6$).**

| $n$ | $q \to 0^+$ | $q = 1$ (classical)     | $q_0 = 1.110$ | $q \to \infty$ |
| --- | ----------- | ----------------------- | ------------- | -------------- |
| $3$ | $2$         | $5/2 = 2.500$           | $2.497$       | $2$            |
| $4$ | $2$         | $19/6 \approx 3.167$    | $3.146$       | $2$            |
| $5$ | $2$         | $46/15 \approx 3.067$   | $3.031$       | $2$            |
| $6$ | $2$         | $473/144 \approx 3.285$ | $3.202$       | $2$            |

**Universal features:**

1. *$\lim_{q \to 0^+} \tau(C_{\dim_q}) = 2$ for all $n \geq 1$.*
2. *$\lim_{q \to \infty} \tau(C_{\dim_q}) = 2$ for all $n \geq 1$.*
3. *At $q = 1$ the value peaks at $\sum_\lambda 1/d_\lambda$
   (classical reciprocal-dimension sum).*
4. *The function is **symmetric under $q \leftrightarrow q^{-1}$**
   (a consequence of $[k]_q = [k]_{q^{-1}}$).*
5. *At $q_0 \approx 1.11$ (paper's canonical substrate) the value
   sits slightly below the classical peak — the substrate is
   $q$-deformed but close to classical.*

**Physical interpretation — SPECULATIVE.**

**Caveat.** *The following is interpretive, not derived.  The limit
structure (Proved: $\tau \to 2$ at $q \to 0, \infty$;
$\tau = \sum 1/d_\lambda$ at $q = 1$; $q \leftrightarrow q^{-1}$
symmetry) is rigorous.  The "substrate information cost" reading
below is a **plausible narrative** consistent with the limit
structure and the role of quantum dimensions in categorical
representation theory, but is not rigorously identified with any
physical information measure.*

*Narrative: the minimum value $2$ (in units of $m_e$) can be
read as the **two self-dual endpoints** of the Young lattice
— the fully symmetric $(n)$ and fully antisymmetric $(1^n)$
partitions with $\dim_q = 1$ at every $q$.  These are the
trivial and sign representations of $S_n$, in the language of
statistics bosonic and fermionic coherent channels.*

*One might try to interpret $1/\dim_q(\lambda)$ as a
**transmission resistance** of channel $\lambda$, with
$\tau(C_{\dim_q}) = \sum 1/\dim_q$ as a parallel-resistance
sum, and the total as a "substrate info-exchange cost":*

$$
  \Delta m_{\text{substrate}}(n, q)
  \;\stackrel{?}{=}\;
  m_e \cdot \sum_{\lambda \,\vdash\, n} \frac{1}{\dim_q(\lambda)}.
$$

*But this identification is **not proved**.  A rigorous
information-theoretic reading would require showing that
$\tau(C_{\dim_q})$ equals a specific entropy, channel capacity,
or thermodynamic quantity on the substrate — which has not been
done.  Candidates and what they would require:*

1. *Shannon-channel analog: would need the substrate to carry a
   probability measure on channels $\lambda$ with entropy
   $-\sum p_\lambda \log p_\lambda$ matching
   $\tau(C_{\dim_q})$ up to calibration.*
2. *Landauer-bound analog: would need a dissipation argument
   showing the substrate must radiate at least
   $m_e \cdot \tau(C_{\dim_q})$ to create any vortex.  No such
   argument has been constructed in this paper.*
3. *Entropic-gravity analog (following
   [entropic gravity](#rem:entropic-gravity)): would need
   a holographic boundary computation yielding
   $\tau(C_{\dim_q})$ from an area law.*

*Until one of these is rigorously established, the
"information cost" language is **analogy, not theorem**.  The
limit structure is real; the physical reading is a conjecture.*

**Brane tower = cost of the specific computation.**

*Where $\tau(C_{\dim_q})$ is vortex-independent substrate cost,
the **brane tower**
([mass endomorphism tower](#prop:mass-endomorphism-tower))*

$$
  \sum_i \Phi_q(|\hat V_i^{\mathrm{full}}|)
  + z^2 \sum_{i<j} \Phi_q(|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|)
$$

*is the **computational cost of processing the specific braid
word $T_w$**.  Each quantum dilogarithm $\Phi_q$ counts paths in
a cluster-algebra resolution — the "work" of passing a crossing
through the exceptional divisor.  Each factor in the tower
tracks a specific crossing or pair of crossings; the tower sum
is the total computational work for that vortex.*

*Contrast:*

| piece                                  | depends on           | physical role                         |
| -------------------------------------- | -------------------- | ------------------------------------- |
| descended $\|\mathrm{tr}_M(T_w)\|$     | $T_w$, $q$           | "output amplitude" of the computation |
| brane tower $\sum \Phi_q$              | $T_w$, $q$           | "processing cost" for that braid      |
| Frobenius $m_e \cdot \tau(C_{\dim_q})$ | only $n$, $q$, $m_e$ | "vacuum / substrate overhead"         |

*The Landauer analogy: Frobenius = minimum energy to erase a
bit ($k_B T \ln 2$); brane tower = energy to actually do the
computation.  The substrate gives the vacuum for free only
up to the Frobenius bound.*

**Calibration values in the brane tower.**

*No.  The brane tower is expressed entirely in terms of $q$ and
the Hecke-algebra transfer matrices: $\Phi_q$, $[k]_q$,
$z = 1/(q^{1/2} + q^{-1/2})$, and intermediate $\hat V_i$.  The
only calibration that enters the unified mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) is $m_e$
(equivalently $E_0$ via $\beta$-decay, or $m_\mu/m_e$ via
[local substrate](#prop:local-substrate-q)).*

*Derived substrate constants — $\hbar_q = (q-1)/q$, $c_q = 1/(q-1)$,
$G_q$, $\eta_q$, $\chi_q$ — are all **functions of $q$ alone**,
They never appear as independent calibrations in the mass
formula.  They parametrize the same substrate but are derived,
not additional.*

**Physics reading at $q_0 \approx 1.11$.**

*The substrate sits slightly $q$-deformed off classical.  At
$n = 3$ (nucleon), the substrate cost is*

$$
  m_e \cdot \left(2 + \frac{1}{[2]_q}\right) \approx 1.276\;\mathrm{MeV},
$$

*the classical $5/2 m_e$ reduced by $\sim 0.1\%$.
Interpretation: the substrate is "almost classical" at
$q_0 \approx 1.11$ — the quantum deformation accounts for only
a 0.1% reduction in the vacuum info-exchange cost, dictated by
the $q$-hook-length formula $\dim_q((2,1)) = [2]_q \neq 2$.*

**As $q$ moves:**

* *$q \to 1$: substrate "heats up" to classical; vacuum cost
  rises to $\sum 1/d_\lambda$.  All representation channels
  become equally accessible (no $q$-suppression of middle
  partitions).*
* \*$q \to 0$ or $q \to \infty$: substrate "freezes" to the
  self-dual endpoints; vacuum cost drops to $2 m_e$.  Middle
  representation channels are suppressed (their $1/\dim_q \to 0$
  because $\dim_q \to \infty$).  The substrate becomes "bosonic
  * fermionic only" — no mixed statistics.\*
* *$q = q_0 \approx 1.11$: substrate sits in the intermediate
  regime, with mixed statistics slightly reduced from classical.
  This is the :refterm[observed value]{#observed-value} where nucleons + nuclei actually
  exist.*

**Open: relation to Landauer / information-theoretic bounds.**

*The "info-exchange cost" language is suggestive but requires
rigor: $\tau(C_{\dim_q})$ might literally equal an entropy or
free-energy of the substrate's mixing measure on the Young
lattice, up to the fibre-functor scale.  Upstream
the formal derivation ruled out the simplest Kerov random-walk
interpretation; the correct information-theoretic frame is
open.  Candidates: heat-kernel regularisation of the Plancherel
trace, Kerov growth model with non-trivial feed, or a
categorical version of the Jarzynski equality.*
<!-- FILE_END: frobenius-limits-substrate-cost.md -->

<!-- FILE_START: knot-mass-formula-unified.md -->
Let $\varrho \colon \mathbf{1} \to A$ be a vortex with braid
representative $\beta \in B_n$ and Hecke mass element
$T_w \in H_n(R, q)$
([Hecke mass element](#def:hecke-mass-element)). Let
$\hat V_i^{\mathrm{full}}$ denote the additive-Wedderburn traced
volume at generator $i$ of the braid word. Let
$\Phi_q(z) = \prod_{k \geq 1} (1 - q^{-k} z)^{-1}$ be the quantum
dilogarithm and $z = 1/(q^{1/2} + q^{-1/2})$ the Markov parameter.

*The boxed theorem below is the **six-term spectral expansion** of
the Gröbner–Shirshov-NF mass identity
([atomic mass via GB-NF](#prop:atomic-mass-gb-nf))
$\mathfrak{m}(\varrho) = m_e \cdot \rho_K \cdot \lvert\!\operatorname{tr}_M\!(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))\!\rvert$.
The descended $\lvert\!\operatorname{tr}_M(T_w)\!\rvert$ piece supplies
the GB-NF normal-form trace; the brane tower and Frobenius co-Casimir
are the spectral decomposition of $\rho_K$ across Wedderburn blocks.
Empirically the six-term sum recovers $\rho_K^{\mathrm{CODATA}}$ to
$\sim 5\%$ for $A = 1$ but under-predicts by $22\%$–$31\%$ for $A \in \{2, 3\}$
(`rho-k-codata-vs-six-term.witness.json`), so the spectral closure of
$\rho_K$ from braid data alone remains open.*

**Theorem (unified knot mass formula; conditional on [`conj:knot-factor-frobenius-pairing`](#conj:knot-factor-frobenius-pairing)).**
*The categorical mass of the vortex $\varrho$ is*

$$
  \boxed{
    \mathfrak{m}(\varrho)
    \;=\;
    \underbrace{\bigl|\mathrm{tr}_M(T_w)\bigr|}_{\text{descended}}
    \;-\;
    \underbrace{\sum_{i=0}^{n-2} \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}}|\bigr)
               - z^2 \sum_{0 \leq i < j \leq n-2}
                  \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|\bigr)}_{\text{brane tower}}
    \;+\;
    \underbrace{m_e \cdot \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)}_{\text{Frobenius co-Casimir}}
  }
$$

*where $\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$
is the symmetric q-dilogarithm with
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$. Per
([mass endomorphism tower proof](#prop:mass-endomorphism-tower)), this
is the closed-form result of integrating the Briggs–Klein
expansion flow $\int_0^V (\ln_q(1+t)/t)\,dt = -\mathrm{Li}_2^q(-V)$
over each resolved defect $E_i \cong \mathbb{P}^1(\mathbb{C})$.*

**Brane-tower-evaluation note (added).**
*The boxed brane-tower form $\sum_i \Phi_q(|\hat V_i|) + z^2 \sum_{i<j}
\Phi_q(|\hat V_i \hat V_j|)$ is the **archimedean Kashaev specialisation**
of the algebraic R-side form
$\sum_i z\,\mathrm{Vol}_q^{(\{i\})}(\beta) + z^2\sum_{i<j}\mathrm{Vol}_q^{(\{i,j\})}(\beta)$
in `prop:mass-endomorphism-tower`. The Kashaev substitution
$\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q(|\hat V_i|)$ evaluates the
quantum dilogarithm on per-generator amplitudes, which are NOT
Markov-invariant. canonical at $q_0 \approx 1.110$ this
specialisation produces $\Phi_q(0.99) \approx 6.7 \times 10^5$ — i.e.
each per-generator term contributes $\sim 10^5$ Hecke-units, summing
to $\sim 10^6$ for atomic braids. Tiny p/n asymmetries between
mirror nuclei (T = 1p+2n vs $^3$He = 2p+1n) get amplified by
$\sim 10^5\times$, predicting T − $^3$He $\approx -737$ MeV against
CODATA $+0.019$ MeV. See
`brane-tower-isospin-diagnosis.witness.json` and
`paper-six-term-isotope-sweep.witness.json` (the four `tower_mode`
variants).*

*The R-side algebraic form, by contrast, gives
$\mathrm{tr}_M(\sigma_i) = z$ and $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$
(Markov axiom; `prop:markov-pair-z2`) for every braid
$\beta$, so $T_2 = (n-1)\cdot z^2$ and $T_3 = \binom{n-1}{2}\cdot z^4$
universally, depending only on the strand count $n$. These are
isospin-exact (T and $^3$He get identical T2+T3 since both have
$n=3A=9$) and $O(1)$ Hecke-units at $q_0$ — six orders of
magnitude smaller than the Kashaev-specialisation form. At
$q\to 1$ the closed-form trace value is $(1/2)^{2A-1}$, also
isospin-exact.*

*Implications. The boxed Kashaev specialisation in this theorem is
**Markov-invariance-broken at $q_0$** and produces hundreds-of-MeV
isospin pathologies at the atomic-braid scale. A complete proof
requires either:*

1. *replacing the boxed formula with the R-side algebraic form
 $\sum_S z^{|S|}\,\mathrm{Vol}_q^{(S)}(\beta)$ — Markov-invariant
 by construction; or*
2. *replacing the per-generator $\Phi_q(|\hat V_i|)$ with a
 q-deformed Wedderburn-weighted trace expansion $\sum_n c_n\,\mathrm{tr}_M(\sigma_i^n)$
 (Heine identity; `brane-tower-plancherel-scaffold.witness.json`)
 — converges to $\Phi_q(z)$ but each summand is a trace; or*
3. *using the Habiro-coefficient sum $\sum_m a_m(T_w)\,(u;u)_m / \mathrm{denom}(u)$
 per `prop:full-pole-structure-mass-trace` — single trace,
 absorbs T2+T3+T6 into one cyclotomic expansion.*

*Empirical: Path 3 (Habiro form) gives sub-1% atomic-mass errors
on $\{p, n, D, T, ^3\mathrm{He}\}$ via a single-prefactor binding
model (`path-b-habiro-mass-canonical evaluation.witness.json`). None of the
additive variants of paths 1, 2 reach this accuracy when forced
through the proton-calibration in the boxed theorem — suggesting
that the additive structure itself may need to be re-derived from
the categorical mass identity $\mathfrak{m}_{q,K} = m_e\cdot\rho\cdot|\mathrm{tr}_M(T_w)|$
([categorical mass, Markov](#prop:categorical-mass-markov)) rather
than treated as a sum of independent pieces.*

*This is **not a refutation of the theorem** — the algebraic form
$\sum_S z^{|S|}\mathrm{Vol}_q^{(S)}$ is correct as a Hochschild-page
decomposition (`prop:gb-spectral-sequence`). It is a flag that
the boxed Kashaev specialisation is the wrong evaluation step at
$q_0$, and the open derivation question is which of paths 1–3
(or another structural reformulation) gives the canonical canonical
value matching CODATA.*

*where*

$$
  C_{\dim_q}^{H_n(R, q)}
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    \frac{[n]_q!}{\dim_q(\lambda)^2 \cdot d_\lambda}
    \cdot e_\lambda
  \;\in\; Z\bigl(H_n(R, q)\bigr)
$$

*is the Frobenius co-Casimir element
([universal Frobenius co-dimension](#thm:frobenius-codim-universal))
with trace*

$$
  \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)
  \;=\;
  \sum_{\lambda \,\vdash\, n} \frac{1}{\dim_q(\lambda)}.
$$

**Three-part structure.**

| piece | algebraic origin | physical content |
|---|---|---|
| descended $\|\mathrm{tr}_M(T_w)\|$ | Markov trace of braid word | $E^0$ term of filtration |
| brane tower $\sum \Phi_q$ | quantum-dilogarithm resolution | single + pair blow-ups |
| Frobenius $m_e \cdot \mathrm{tr}_M(C_{\dim_q})$ | self-dual co-Casimir | universal fibre-functor residual |

*Each piece is computable from the braid word $T_w$ and the
quantum dimensions $\{\dim_q(\lambda) : \lambda \vdash n\}$ alone.
No empirical constant enters except the single fibre-functor
calibration $m_e$ (or equivalently $E_0$) that converts
categorical mass to MeV
([categorical mass, Markov](#prop:categorical-mass-markov)).*

**Specialisations by braid size $n$.**

*For a trefoil / single nucleon ($n = 3$):*

$$
  \mathfrak{m}_{\mathfrak{p}}
  \;=\;
  |\mathrm{tr}_M(T_w^{\mathfrak{p}})|
  + \text{brane-tower}(n{=}3)
  + m_e \cdot \left(2 + \frac{1}{[2]_q}\right).
$$

*The Frobenius piece $m_e \cdot (2 + 1/[2]_q) \approx 1.276\;\mathrm{MeV}$
matches the observed proton tower residual to $0.14\%$
([proton residual](#prop:partition-sum-proton-residual)).*

*For a general isotope braid ($n = 3A$):*

$$
  \mathfrak{m}_{\text{isotope}}
  \;=\;
  |\mathrm{tr}_M(T_w)|
  + \text{brane-tower}(n{=}3A)
  + m_e \cdot \sum_{\lambda \,\vdash\, 3A} \frac{1}{\dim_q(\lambda)}.
$$

*The right object is the $(3A)$-level Frobenius sum
$\tau\bigl(C_{\dim_q}^{H_{3A}(R, q)}\bigr) = \sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$,
not $A$ copies of the single-vortex $(n=3)$ value.*

*This is forced by the algebraic content of
[Frobenius co-Casimir universal](#thm:frobenius-codim-universal):
when the isotope's braid lives in $H_{3A}(R, q)$, the central
idempotents $p_\lambda$ are indexed by partitions $\lambda \vdash 3A$,
not by partitions of $3$. The per-A heuristic
$A \cdot \tau(C_{\dim_q}^{H_3})$ would correspond to a disconnected sum
of $A$ independent $H_3$-blocks, which is**not** the algebra
hosting an isotope braid.*

*exact algebraic values per
the canonical formalism:*

| atom | $A$ | per-vortex $1{\cdot}m_e\Sigma_3$ | per-A $A{\cdot}m_e\Sigma_3$ | **per-$3A$ $m_e\Sigma_{3A}$ (algebraic)** |
|---|---:|---:|---:|---:|
| D | 2 | 1.276 MeV | 2.552 MeV | **1.636 MeV** |
| T, ${}^{3}$He | 3 | 1.276 MeV | 3.828 MeV | **1.300 MeV** |
| ${}^{4}$He | 4 | 1.276 MeV | 5.105 MeV | **1.151 MeV** |

*The per-$3A$ values are close to the per-vortex value ($\sim
1.2$–$1.6$ MeV) because $\sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$
is dominated by the two extreme blocks $((3A))$ and $((1^{3A}))$
each contributing $1$, plus a $q$-dependent middle that grows
slowly in $A$. This explains why the per-vortex heuristic was
empirically a good approximation, but it is not the rigorous
statement.*

*Compute side: scripts that use $A \cdot m_e \cdot (2 + 1/[2]_q)$
(the canonical formalism,
the canonical formalism)
are using the per-A heuristic and need to be migrated to the
per-$3A$ algebraic form before any "best prediction" claim.*

**Specialisations by knot type.**

*For a single braid generator ($n = 2$, electron candidate):*
$\widehat{H_2(R, q)} = \{(2), (1,1)\}$ both with $\dim_q = 1$, so
$\sum 1/\dim_q = 2$, giving Frobenius residual $2 m_e \approx
1.022\;\mathrm{MeV}$.

*For Borromean-type braids ($n \geq 6$):*
the Frobenius sum grows with $n$; see table in
[Frobenius universal](#thm:frobenius-codim-universal).

**Classical limit ($q \to 1$).**
*The Hecke algebra reduces to $\mathbb{C}[S_n]$; $\dim_q \to d_\lambda$
and $[2]_q \to 2$. The Frobenius co-Casimir trace reduces to
$\sum_\lambda 1/d_\lambda$ (classical reciprocal-dimension sum).
For $n = 3$ this is exactly $5/2$ — recovering the upstream
classical discovery
(the formal derivation).*

**Rationale for the "unified" label:**
*The three pieces were previously distinct objects with separate
derivations:*

1. *Descended $|\mathrm{tr}_M|$ — `prop:categorical-mass-markov`,
 the mass-identity prescription.*
2. *Brane tower $\sum \Phi_q$ — `prop:mass-endomorphism-tower`,
 derived from the quantum-dilogarithm resolution of the
 exceptional divisor.*
3. *Frobenius correction — `thm:frobenius-codim-universal` (new),
 derived from self-dual Frobenius structure of $H_n(R, q)$.*

*This theorem combines them into a single three-term formula.
Each term is independently derived; the sum is the total mass.*

**Limitation: the Frobenius piece is vortex-blind.**

*The Frobenius correction $m_e \cdot \mathrm{tr}_M(C_{\dim_q})$
**does not depend on the specific vortex $\varrho$** — only on
the ambient Hecke algebra $H_n(R, q)$. All trefoil-like vortices
on $H_3(R, q)$ (proton, neutron, any quark configuration) get
the same additive offset $(2 + 1/[2]_q) \cdot m_e$. Mass
differences between such vortices therefore must come from
the first two pieces (descended + brane tower).*

**Isotope binding: chirality factors are a FOURTH tier.**

*For compound isotope bindings, the paper's full formula
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
adds a **vortex-dependent chirality factor**
$a_K \in \{1 + h,\; 1 - h^2,\; (1 - h^2)^2\}$ for $\{D, T, ^4\mathrm{He}\}$
respectively — reflecting the knot type (chiral+, amphichiral,
Borromean$\times$2). Upstream verification
(the formal derivation) gives
$T: 0.505\%$ and $^3\mathrm{He}: 0.856\%$ agreement with AME
using these factors.*

*The chirality factor is a fourth structural layer beyond the
three Frobenius-universal layers of this theorem. It is vortex-
dependent, like the descended and tower pieces, but algebra-
independent in form (depends only on the knot type of the
isotope braid, not on the specific $T_w$ expansion). A
complete mass formula is therefore:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  |\mathrm{tr}_M(T_w)|
  \;+\;
  \sum \Phi_q(\cdot)
  \;+\;
  m_e \cdot \mathrm{tr}_M(C_{\dim_q})
  \;+\;
  a_K \cdot B_{\mathrm{bulk}}
  \;+\;
  (\text{jet-level corrections}),
$$

*where $a_K$ is the chirality factor and the jet-level
corrections reflect the open-problem prefix-word structure
per upstream the formal derivation.*

**Consistency checks.**

1. *At $q = 1$: classical Hecke reduces to $\mathbb{C}[S_n]$, brane
 tower collapses ($\Phi_1$ singular — handled by a separate
 classical-limit argument), Frobenius term reduces to $\sum
   1/d_\lambda$ (number of conjugacy classes / involutions).*
2. *For the identity braid $T_e = 1 \in H_n(R, q)$:
 $|\mathrm{tr}_M(1)| = 1$; brane tower vanishes (no crossings);
 Frobenius term is pure $\sum 1/\dim_q$ — this is the
 **vacuum mass** of the trivial vortex, consistent with
 the unit object's fibre-functor value.*
3. *Under braid concatenation $T_{w_1 w_2} = T_{w_1} T_{w_2}$
 (Hecke multiplication): the descended piece is multiplicative
 in $|\mathrm{tr}_M|$; the brane tower is additive;
 the Frobenius piece is **vortex-count-additive** (per
 deuteron observation). Total mass is therefore not 
 additive or multiplicative — the three pieces compose by
 their own rules and the sum respects the expected
 thermodynamic behaviour of bound-state mass defects.*
<!-- FILE_END: knot-mass-formula-unified.md -->

<!-- FILE_START: nuclear-knot-classification.md -->
**Proposition.**
*The closure of the nuclear braid $\mathcal{N}(Z,N)$ in $H_3(R, q)$
determines a bulk modification factor $a(\mathcal{N})$ for the
BW binding energy.  This factor is a single product over
independent nucleon pairs:*

$$
  a(\mathcal{N})
  \;=\;
  \prod_{i=1}^{n_{\mathrm{pairs}}}
    (1 - \varepsilon_i)
$$

*where $\varepsilon_i$ is the Frobenius norm deviation of the
$i$-th nucleon pair from the identity braid:*

- *Amphicheiral pair (pp or nn in $\mathcal{B}_3$):
  $\varepsilon = h^2 = (q - q^{-1})^2$*
- *Chiral pair (pn):
  $\varepsilon = -h = -(q - q^{-1})$*

*The sign convention: amphicheiral pairs ($K = \bar{K}$) deviate
quadratically ($h^2 > 0$, reducing binding); chiral pairs deviate
linearly ($-h < 0$, increasing binding).*

| $A$ | Pairs | Deviations $\varepsilon_i$ | $a(\mathcal{N})$ |
|-----|-------|---------------------------|-------------------|
| $1$ | $0$ | — | free nucleon |
| $2$ | $1$ pn (chiral) | $-h$ | $1 + h \approx 1.209$ |
| $3$ | $1$ pp or nn (amphicheiral) | $h^2$ | $1 - h^2 \approx 0.956$ |
| $4$ | $2$ (pp + nn, amphicheiral) | $h^2, h^2$ | $(1 - h^2)^2 \approx 0.914$ |
| $\geq 5$ | many | $(1 - h^2)^n \to 1$ | $1$ |

*In the large-$A$ limit, $(1 - h^2)^n \to 1$ since
$h^2 \approx 0.044 \ll 1$, recovering the standard
BW formula for heavy nuclei.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: nuclear-knot-classification.md -->

<!-- FILE_START: geom-yekutieli-alignment.md -->
**Proposition (conditional on
[`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence)
and
`rem:baryon-period-ratio`).**
*The piecewise geometric invariant
$\mathrm{Geom}(K)$
([topological mass formula](#prop:topological-mass-formula))
is the evaluation of the Yekutieli rigid dualizing complex
$\omega_A^\bullet$ on the algebraic stratification of the braid
$\beta$ with closure $K = \widehat\beta$ (per
[algebraic stratification](#prop:phi-q-tower-algebraic-stratification);
the τ-image of this evaluation is the geometric reading on
$S^3 \setminus K$, classified by Thurston's geometrization at the
τ-side):*

$$
  \mathrm{Geom}(K) =
  \langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}
  =
  \begin{cases}
    \mathrm{Vol}(K) / \hbar_q^2
      & K \text{ hyperbolic} \\[4pt]
    \mathrm{CS}(K) \cdot \hbar_q^2
      & K \text{ torus} \\[4pt]
    0 & K = \bigcirc
  \end{cases}
$$

*where $\langle -, - \rangle_{\mathrm{Frob}}$ is the Frobenius
pairing induced by the rigid dualizing complex, and
$\hbar_q = 1 - 1/q$ is the quantum Planck constant.*

*Proof.*
The argument has three parts.

**Part 1: the rigid dualizing complex mediates duality.**
The Frobenius--Hopf algebra $A$ at the substrate parameter $q$
carries a rigid dualizing complex $\omega_A^\bullet$
(Yekutieli \cite{yekutieli2015}), which satisfies the rigidifying
isomorphism

$$
  \omega_A^\bullet
  \;\simeq\;
  R\mathrm{Hom}_{A^e}(A, A^e)
$$

in the derived category $D(A^e)$.  The Frobenius form
$\lambda\colon A \to \mathbf{1}$ makes $A$ self-dual with respect
to $\omega_A^\bullet$, inducing the non-degenerate pairing

$$
  \langle -, - \rangle_{\mathrm{Frob}}
  \colon
  H^\bullet(S^3 \setminus K; \omega_A^\bullet)
  \otimes
  H^{3-\bullet}(S^3 \setminus K; A)
  \;\longrightarrow\;
  \mathbb{C}.
$$

This is the categorical substitute for the canonical sheaf in the
non-commutative setting.

**Part 2: Geometric type selects the evaluation mode (algebraic
side).** The proof works in $\mathbb{Z}[q^{\pm 1/2}]$ throughout;
the geometric / 3-manifold reading appears only as the τ-image
discussed in Part 3. Algebraically, the rigid dualizing evaluation
$\langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}$
admits a single closed-form expression in terms of the
[algebraic quantum volume](#def:algebraic-quantum-volume)
$\mathrm{Vol}_q(\beta) \in \mathbb{Z}[q^{\pm 1/2}]$ and the
[Chern-Simons phase](#rem:chern-simons-as-knot-invariant) $\mathrm{CS}_q(\beta)$:

$$
  \mathrm{Geom}(K)
  \;=\;
  \frac{\mathrm{Vol}_q(\beta)}{\hbar_q^2}
  \;+\;
  \mathrm{CS}_q(\beta) \cdot \hbar_q^2
$$

with the $\hbar_q$ factors normalising the Frobenius pairing. For
the algebraic-side derivation no Thurston-geometrization input is
required; the Wedderburn-Artin block decomposition of $H_n(R, q)$
selects which of the two summands dominates for a given braid:

- *Algebraic-hyperbolic regime* ($\mathrm{Vol}_q(\beta) \ne 0$
  in $\mathbb{Z}[q^{\pm 1/2}]$): the first summand carries the
  contribution. The fundamental class pairs against the algebraic
  quantum volume, and the Frobenius normalisation introduces
  $1/\hbar_q^2$ as the mass scale.

- *Algebraic-torus regime* ($\mathrm{Vol}_q(\beta) = 0$ in
  $\mathbb{Z}[q^{\pm 1/2}]$, e.g. $\beta = \beta_{T_{m,n}}$): the
  algebraic quantum volume vanishes identically and the second
  summand carries the contribution. The dualising normalisation
  flips to $\hbar_q^2$ (multiplicative rather than divisive),
  reflecting the Frobenius duality between bulk and boundary:

$$
  \frac{\mathrm{Vol}_q(\beta)}{\hbar_q^2}
  \quad\longleftrightarrow\quad
  \mathrm{CS}_q(\beta) \cdot \hbar_q^2.
$$

- *Algebraic-trivial regime* ($\beta = 1$, the identity / unknot
  closure): both algebraic summands vanish (vacuum normalisation),
  reflecting the empty cohomology of the trivial element of
  $H_n(R, q)$ against $\omega_A^\bullet$.

**Part 3: the Frobenius self-pairing is unitary (algebraic).**
For any braid $\beta$ and its mirror $\beta^*$ (obtained by
reversing each $\sigma_i \mapsto \sigma_i^{-1}$), the Frobenius
pairing satisfies

$$
  \langle \beta, \beta^* \rangle_{\mathrm{Frob}}
  = \mathrm{Geom}(\beta) \cdot \mathrm{Geom}(\beta^*)^{-1}
  = 1,
$$

since $\mathrm{Vol}_q(\beta^*) = \mathrm{Vol}_q(\beta)$ in
$\mathbb{Z}[q^{\pm 1/2}]$ (algebraic quantum volume is invariant
under mirror image, by inspection of the Markov-trace product
formula) and $\mathrm{CS}_q(\beta^*) = -\mathrm{CS}_q(\beta)$
(the Chern-Simons phase changes sign on mirror — direct
consequence of the $q \mapsto q^{-1}$ involution on the relevant
braid representation).

For **amphicheiral** knots ($K = K^*$, e.g.\ the figure-eight
$4_1$), the self-pairing is manifestly real.  This explains why
the figure-eight BW modification factors
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
are both real algebraic expressions in $q$:
$1 - h^2 = 4 - [3]_q$ and $h[2]_q = q^2 - q^{-2}$.

**Connection to transcendence.**
The non-vanishing Yekutieli obstruction classes $\kappa_n \neq 0$
at every level of the brane tower — the content of
[motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)
applied to the substrate's motivic Galois character at every
finite place — ensure that the evaluation $\mathrm{Geom}(K)$ for
distinct hyperbolic knots produces algebraically independent
values. A polynomial relation among the
$\mathrm{Vol}(K_i)/\hbar_q^2$ would force the tower to collapse
at finite height, contradicting place-by-place non-vanishing of
the motivic Galois character
([hyperbolic volume transcendence](#conj:hyperbolic-volume-transcendence)).
$\square$
<!-- FILE_END: geom-yekutieli-alignment.md -->

<!-- FILE_START: content-scaling-correspondence.md -->
**Proposition.**
*By $q$-Schur--Weyl duality $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$,
the content $c = j - i$ of a box at position $(i,j)$ in a Young diagram
equals the magnetic quantum number $m_j$ of the corresponding
$\mathrm{SU}_q(2)$ weight space.*

*The content determines the BW scaling function:*

| Content $c$ | Isospin meaning | Scaling $f_c(Z,N)$ |
|:-----------:|:---------------:|:-------------------:|
| $+1$ | proton nearest-neighbor | $Z(Z{-}1)/A^{1/3}$ |
| $-1$ | neutron nearest-neighbor | $N(N{-}1)/A^{1/3}$ |
| $0$ | balanced (pn mixed) | $A^{2/3}$ or $\pm 1/\sqrt{A}$ |
| $\pm 2$ | next-nearest same-type | $Z^{4/3}/A^{1/3}$ |
| $\lvert c\rvert \geq 3$ | long-range | $T^p(T{+}1)^p/A^p$ |

*Each scaling function counts the number of nucleon pairs at
spin projection $c$ in the nuclear ground state.* $\square$
<!-- FILE_END: content-scaling-correspondence.md -->

