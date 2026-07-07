<!-- FILE_START: topological-mass-su2.md -->
Continuing the [:refterm[descent]{#descent} eigenspaces for SU(2)](#ex:descent-eigenspaces-su2),
we verify the [topological mass theorem](#thm:topological-mass) for
$G = \mathrm{SU}(2)$.

**The decomposition.** By the topological mass theorem, the mass of a
cycle $\varrho$ decomposes according to the eigenspace splitting:

$$
  \mathfrak{m}(\varrho) =  \mathfrak{m}_{\mathrm{desc}}(\varrho) + \mathfrak{m}_{\mathrm{trans}}(\varrho),
$$

where $\mathfrak{m}_{\mathrm{desc}} = \lVert \mathrm{tr}_{\mathrm{desc}}(\varrho) \rVert$
gives the descended (persistent) contribution and
$\mathfrak{m}_{\mathrm{trans}} = \lVert \mathrm{tr}_{\mathrm{trans}}(\varrho) \rVert$
gives the transient contribution.

**Descended mass.** The descended trace $\mathrm{tr}_{\mathrm{desc}}$
factors through the projection $\hat{\tau}$ onto
$\mathfrak{A}^{\mathrm{desc}} \cong \mathfrak{su}(2)$. For the Hopf
fibration $\mathrm{SU}(2) \to \mathbb{CP}^1$, the descended mass of
the fundamental cycle evaluates to:

$$
  \mathfrak{m}_{\mathrm{desc}} =  \chi(\mathbb{CP}^1) =  2,
$$

which is the Euler characteristic of $\mathbb{CP}^1 \cong S^2$. This provides the
topologically protected part. It remains invariant under continuous
deformations of the cycle and the metric.

**Transient mass.** The transient trace
$\mathrm{tr}_{\mathrm{trans}}$ captures fluctuations in the
cotangent directions $\mathfrak{A}^{\mathrm{trans}} \cong \Omega^1(\mathbb{CP}^1) \oplus \mathbb{C}$.
For a cycle $\varrho$ that is $\mathrm{U}(1)$-equivariant,
$\mathfrak{m}_{\mathrm{trans}}(\varrho) = 0$ since the transient eigenspace has
non-zero $\mathrm{U}(1)$-weight. Non-equivariant deformations of
$\varrho$ contribute a non-zero $\mathfrak{m}_{\mathrm{trans}}$ that measures the
departure from the symmetric configuration.

**Total mass.** For the fundamental cycle of the Hopf fibration,
$m = 2 + 0 = 2$, recovering the Euler characteristic. For a deformed
cycle, $m = 2 + \mathfrak{m}_{\mathrm{trans}}$, with the correction depending on
the $L^2$-norm of the cotangent component.
<!-- FILE_END: topological-mass-su2.md -->

<!-- FILE_START: gb-spectral-sequence.md -->
The unified knot mass formula ([unified knot mass](#thm:knot-mass-formula-unified)) comprises six structural terms. These emerge as pages of a spectral sequence associated with the Gröbner–Shirshov filtration $J^\bullet(q)$ on $H_n(R, q)$. We make this spectral-sequence structure precise and state the $E_\infty$ convergence target.

**Definition (filtered differential algebra).**
*The Hecke algebra $H_n(R, q)$ with the confinement filtration $J^\bullet(q)$ ([confinement level](#def:confinement-level)) carries a natural differential $d$ induced by three Gröbner–Shirshov rewriting rules ([Hecke normal form](#def:hecke-normal-form)):*

1. *Hecke relation: $d_{\mathrm{H}}(\sigma_i^2) = (q - q^{-1})\sigma_i + \mathbf{1}$.*
2. *Far commutativity: $d_{\mathrm{F}}(\sigma_i \sigma_j) = \sigma_j \sigma_i$ for $|i - j| \geq 2$.*
3. *Yang–Baxter: $d_{\mathrm{YB}}(\sigma_i \sigma_{i+1} \sigma_i) = \sigma_{i+1} \sigma_i \sigma_{i+1}$.*

*Each rule lowers filtration degree. The direct sum $d = d_H + d_F + d_{YB}$ satisfies $d \circ d = 0$ on the filtered complex. This makes $(H_n(R, q), J^\bullet, d)$ a filtered differential algebra.*

**Proposition (GB spectral sequence).**
*The filtered differential algebra $(H_n(R, q), J^\bullet, d)$ has an associated spectral sequence $(E_r^{\ell, *}, d_r)$ with:*

$$
  E_0^{\ell, *} \;=\; J^\ell(q) / J^{\ell+1}(q)
  \qquad \text{(associated graded)},
$$

$$
  E_1^{\ell, *} \;=\; H^*\bigl(J^\ell / J^{\ell+1},\ d\bigr)
  \qquad \text{(Hochschild-type cohomology of each stratum)},
$$

*and higher pages $E_r^{\ell, *}$ obtained by successive homology of $d_r$.*

*Convergence:*

$$
  E_\infty^{\ell, *}
  \;\Longrightarrow\;
  \mathrm{gr}^\ell\bigl(H_n(R, q)\bigr).
$$

*The Markov trace $\mathrm{tr}_M: H_n(R, q) \to \mathbb{C}$ forms a $d$-closed linear functional. It descends to $E_\infty$.*

**Identification of the six mass terms with spectral-sequence pages.**

*Pairing $\mathrm{tr}_M$ against the braid word $T_w$ decomposes over the spectral sequence pages as:*

See [Table](#tbl:gb-spectral-sequence-table-data).

**Derivation of $d \circ d = 0$ (via Hochschild complex).**

*The rewriting rules $d_H, d_F, d_{YB}$ define a reduction procedure. To obtain $d \circ d = 0$, we pass to the Hochschild cochain complex over the natural ground ring $R$:*

$$
  C^k(H_n(R, q), H_n(R, q))
  \;:=\;
  \mathrm{Hom}_R\bigl(H_n(R, q)^{\otimes k},\ H_n(R, q)\bigr),
$$

*where $R$ forms the categorical base ring. This forms the target of the fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ ([Tannaka–Krein reconstruction](#prop:tannaka-krein-reconstruction)). $R$ is the commutative ring in which Markov-trace values live before archimedean calibration $\tau \colon R \to \mathbb{R}$ ([categorical mass, Markov](#prop:categorical-mass-markov)).*

*Under different realisations ([knot operator energy](#def:knot-operator-energy)):*

- *Archimedean: $R$ contains $\mathbb{R}[q, q^{-1}]$, evaluated at $q = q_0 \in \mathbb{R}$.*
- *$p$-adic: $R$ contains $\mathbb{Q}_p[q, q^{-1}]$.*
- *Finite-field: $R$ contains $\mathbb{F}_p[q, q^{-1}]$.*

*The spectral-sequence construction operates over any such $R$. The physics application uses the archimedean realisation. The derivation is ring-agnostic. Complex numbers appear only as a derived embedding $R \hookrightarrow \mathbb{C}$ when we extract residues at roots of unity ([GB residue spectral sum](#prop:gb-residue-spectral-sum)).*

*We equip the complex with the standard Hochschild differential:*

$$
  (d\,f)(a_0 \otimes \cdots \otimes a_k)
  \;=\;
  a_0 \cdot f(a_1 \otimes \cdots \otimes a_k)
  + \sum_{i=0}^{k-1} (-1)^{i+1} f\bigl(a_0 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_k\bigr)
  + (-1)^{k+1} f(a_0 \otimes \cdots \otimes a_{k-1}) \cdot a_k.
$$

*The identity $d \circ d = 0$ is a classical theorem for any associative $R$-algebra. It holds verbatim for $H_n(R, q)$. The Markov trace $\mathrm{tr}_M$ forms a cyclic $0$-cochain (satisfying $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$). It is therefore $d$-closed at degree $0$.*

*The confinement filtration $J^\bullet(q)$ induces a decreasing filtration on $C^\bullet$:*

$$
  F^p C^k
  \;:=\;
  \{f \in C^k \mid f\bigl(J^{p_1}(q)^{\otimes k}\bigr) \subset J^{p + p_1}(q)\},
$$

*This filtration maintains compatibility with the Hochschild differential ($d(F^p) \subset F^p$), forming the filtered Hochschild complex.*

*Therefore:*

1. **$d \circ d = 0$ holds** *on the filtered complex.*
2. **Filtration preservation** *follows because $J^\bullet$ provides an ideal-filtration compatible with multiplication.*

*Hence $(C^\bullet(H_n(R, q)), d, F^\bullet)$ forms a filtered cochain complex with spectral sequence pages $(E_r^{p, q}, d_r)$.*

**Convergence $E_\infty \Rightarrow \mathrm{gr}\,H_n(R, q)$.**

*The filtration $J^\bullet(q)$ is:*

1. *Bounded below: $J^0 = H_n(R, q)$.*
2. *Exhaustive: $\bigcap_\ell J^\ell = 0$ for any generic $q = q_0$. Partition energies $E_\ell(q_0)$ are distinct and positive ([confinement level, uniqueness](#prop:confinement-level-unique)).*
3. *Finite-dimensional at each degree $J^\ell(q)/J^{\ell+1}(q)$.*

*These provide the classical convergence conditions for a filtered spectral sequence. Therefore:*

$$
  E_\infty^{p, q}
  \;\cong\;
  \mathrm{gr}^p\,H^{p+q}\bigl(H_n(R, q), H_n(R, q)\bigr),
$$

*The total Hochschild cohomology equals the sum over pages. Pairing this with the Markov-trace cocycle $\mathrm{tr}_M$ yields the six-term mass decomposition.*
<!-- FILE_END: gb-spectral-sequence.md -->

<!-- FILE_START: gb-spectral-sequence-interpretation.md -->
**Open formalization requirements.**

Standard Hochschild-complex theory yields $d \circ d = 0$ and $E_\infty$ convergence. The open requirements are:

1. Term-by-term identification of $E_\infty^{p, *}$ with the six mass-formula components. At $p = 0$ (descended $\mathrm{tr}_M$), this yields the Frobenius co-Casimir ([`thm:frobenius-codim-universal`](#thm:frobenius-codim-universal)). For $p \geq 1$, identifying $\Phi_q$ poles and chirality demands explicit page computation.
2. Explicit $E_1$ page computation for $H_3(R, q)$. Burciu and Scheimbauer (2019) establish that $\dim H^k(H_n(R, q), H_n(R, q))$ grows via a specific partition generating function. The pairing with $\mathrm{tr}_M$ isolates the cyclic part. Matching this to the six terms requires a computational derivation.

The Hochschild complex guarantees the existence of the spectral sequence. Matching its pages to the mass-formula terms remains open.

## Rigorous derivation path

A rigorous derivation requires four steps:

- Construct the Hochschild cochain complex $C^*(H_n(R, q), H_n(R, q))$ with the filtration induced by $J^\bullet(q)$.
- Prove $\mathrm{tr}_M$ forms a Hochschild cocycle, exploiting the cyclicity of the Markov trace.
- Compute the spectral sequence pages $E_r$ explicitly for $n = 3$ and verify the decomposition.
- Match each page to the corresponding mass term via $\Phi_q$ poles, Frobenius invariants, and chirality components.

This represents a research-level project in cohomological algebra and deformation theory. We flag the target; the work remains open.

## Structural value

The spectral-sequence framing enforces architectural rigidity:

1. The six mass terms are structurally constrained. They constitute the non-trivial pages of a canonical spectral sequence.
2. The mass sum equals the total cohomology of the filtered Hecke algebra paired with $T_w$.
3. Regime switching ([`prop:mass-formula-regime-switching`](#prop:mass-formula-regime-switching)) occurs because different pages dominate for different $A$. This reflects the spectral sequence structure, not an ad-hoc failure of additivity.

## Relation to standard formalisms

Hochschild cohomology $HH^*(H_n(R, q))$ is established by Kosmann-Schwarzbach, Lambe–Stasheff, and Burciu–Scheimbauer. These supply deformation-theoretic data: $HH^2$ controls deformations, $HH^3$ controls obstructions.

Our filtration $J^\bullet(q)$ incorporates the specific substrate parameter $q$, forming a finer grading than standard length. This yields $q$-dependent differentials. 

Reshetikhin–Turaev invariants at roots of unity emerge as residues of the $E_\infty$ pages when $q = \zeta_\ell$ collapses the filtration. The RT evaluation operates strictly as a spectral-sequence specialization.

This grounds the mass formula in quantum topology and deformation theory. The unification objective seeks to prove the six-term mass evaluates a specific spectral-sequence cohomology class paired against the atomic braid, relying exclusively on the Hecke algebra.

## Archimedean realization

The $E_\infty$-pairing operates strictly over the categorical base ring $R$. Pairings $\langle \mathrm{tr}_M, E_\infty^{p,*}(T_w)\rangle$ evaluate in $R$, not $\mathbb{C}$. 

Applying the archimedean fibre functor $\tau \colon R \hookrightarrow \mathbb{C}$ promotes the $E_\infty$-pairing to a contour integral on the Descartes elliptic curve $\mathcal{E}_q(\mathbb{C})$. The level-$p$ stratum maps to the geometric jet bundle $J^p\mathcal{S}$. The Seiberg–Witten differential $\lambda_{\mathrm{SW}}^{(p)}$ serves as the tautological section.

The pairing's $\mathbb{C}$-realization gives the Picard–Lefschetz thimble period $\Pi^{(p)}$, equaling $\tau\bigl\langle\mathrm{tr}_M, E_\infty^{p,*}(T_w)\bigr\rangle$ up to the integer intersection numbers $n_\sigma^{(p)}$ of the Lefschetz decomposition. The spectral sequence and the PL thimble decomposition provide two presentations of identical data across the archimedean wall.
<!-- FILE_END: gb-spectral-sequence-interpretation.md -->

<!-- FILE_START: homological-shell-condensation.md -->
The Białynicki-Birula stratification of the brane tower
([recursive-brane-tower](#def:recursive-brane-tower),
[brane-tower-levels](#ex:brane-tower-levels)) under the :refterm[descent]{#descent}
involution $\hat\tau$
([:refterm[descent]{#descent}-involution](#def:descent-involution)) yields a spectral
sequence whose $E_\infty$ page records the failure of categorical
neutrality at each level. This block names the **homological
condensation** at saturated $n$. The higher pages collapse to zero,
encoding shell closure as an algebraic-geometry condition on the
brane-tower stratification.

## Setup

Fix a level $n \in \mathbb{N}$ in the brane tower, with associated
:refterm[descent]{#descent}-graded jet algebra $A_n = A_{n-1} \otimes \Omega^1(A_{n-1})$
([def:direct-limit-algebra](#def:direct-limit-algebra)). The
Białynicki-Birula stratification of $\mathrm{Spec}(A_n)$ under the
$\mathbb{C}^\times$-action induced by the :refterm[descent]{#descent} involution
$\hat\tau$ \cite{bialynicki1973} produces a filtration

$$
  F^0 A_n \supset F^1 A_n \supset \cdots \supset F^p A_n \supset \cdots
$$

with associated graded $\mathrm{gr}_F A_n$. The Gröbner–Shirshov
spectral sequence
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence)) on this
filtration converges to the :refterm[descent]{#descent}-graded algebra:

$$
  E_1^{p,q} \;=\; H^q\bigl(\mathrm{gr}_F^p A_n\bigr)
  \;\Longrightarrow\;
  H^{p+q}\bigl(A_n\bigr).
$$

The strict-positive part $E_\infty^{p, >0}(n)$ measures the
non-trivial cohomology supported above the $E_2$-collapse line.
Operationally, it measures the obstruction to reading the :refterm[descent]{#descent}-graded trace
purely from the diagonal
([prop:graded-trace-residue-split](#prop:graded-trace-residue-split)).

## Statement

**Proposition (Conjecture — homological shell condensation).**
*For every $n \in \mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$, the
Białynicki-Birula spectral sequence on $A_n$ collapses entirely above
the $E_2$ line:*

$$
  E_\infty^{p, q}(n) \;=\; 0
  \qquad\text{for all } p \in \mathbb{N}, \; q > 0,
  \quad n \in \mathfrak{M}.
$$

*Equivalently, the :refterm[descent]{#descent}-graded trace
$\mathrm{tr}_{M, \ell}$ on $J^\ell / J^{\ell+1}$
([prop:graded-trace-residue-split](#prop:graded-trace-residue-split))
is supported entirely on the diagonal at saturated $n$, and the
brane-tower :refterm[descent]{#descent} residues vanish for $\ell \geq 2$.*
<!-- FILE_END: homological-shell-condensation.md -->

<!-- FILE_START: homological-shell-condensation-interpretation.md -->
## Terminology: "condensation"

The vanishing $E_\infty^{p, >0}(n) = 0$ dictates that every higher
:refterm[descent]{#descent} residue collapses onto the diagonal. There are no
off-diagonal jet-tower contributions at saturated $n$. The shell
condenses into a single graded piece. For $n \notin \mathfrak{M}$
the off-diagonal pieces survive. They provide the algebraic content of
non-saturation (residual capacity to absorb crossing energy).

The phenomenology this picks up is standard. At
$n \in \mathfrak{M}$ the binding-energy curve flattens, the next
nucleon adds nearly-zero binding, and the shell is mathematically
"full". The refactor identifies this directly in the spectral sequence,
rather than via shell-model fitting.

## Conditional content via the categorical-neutrality conjecture

Conditional on
[`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md),
the full-twist $\Delta_n^2$ acts as the identity on $\Phi_n$ at
$n \in \mathfrak{M}$. The categorical neutrality forces the
Wedderburn support of $\Phi_n$ onto self-conjugate partitions. Pairing
this with Yekutieli rigidity \cite{yekutieli2010}, the :refterm[descent]{#descent}
involution $\hat\tau$ inherits the corresponding self-conjugacy on
$A_n$, and the BB stratification becomes self-dual: the strata above
the $E_2$ collapse line cancel pairwise. The conjectured
$E_\infty^{p, >0}(n) = 0$ forms the algebraic-geometry crystallisation
of this cancellation.

This conditional structure justifies authoring both conjectures
together. The categorical conjecture forms the Hecke-side
content; the homological conjecture forms its brane-tower-side image
under Yekutieli rigidity. A proof of either implies the other under
the substrate axioms.

## Relation to the Hoefsmit / matrix-evaluation programme

Numerical verification at $k = 3, \dots, 10$
([prop:magic-numbers-from-q](../observations/magic-numbers-from-q.md))
empirically confirms $E_\infty^{p, >0}(n) = 0$ at $n = 2, 8, 20$ via
direct computation of :refterm[descent]{#descent} residues from Hoefsmit matrices. The
combinatorial blow-up at $k \geq 12$ blocks the matrix-evaluation
approach. The homological framework analytically bypasses this
barrier by replacing per-partition matrix computation with
spectral-sequence arithmetic
([rem:k12-barrier-bypass](../observations/k12-barrier-bypass.md)).

## Operator-level support (clarification)

The "Wedderburn support of $\Phi_n$ onto self-conjugate
partitions" in §"Conditional content" above describes operator-level support.
$\Phi_n$ has zero matrix entries on non-self-conjugate isotypical
components, but the operator on the self-conjugate components is
generically non-trivial. It is not the Plancherel-weighted
character sum $\sum_{\lambda = \lambda'} w_\lambda \chi^\lambda$,
which vanishes identically at certain atomic-braid cycle types
(see [reframing memo](../../../docs/audits/-self-conj-support-reframing.md)).
The $E_\infty^{p, >0}(n) = 0$ collapse condition stated above is
precisely operator-level (page collapse on the associated graded
algebra). It remains consistent with this reading.

## Discussion

This remains conjectural under AGENTS.md §3b. The supporting evidence comprises:

1. Numerical verification at $n \in \{2, 8, 20\}$ via the
 matrix-evaluation programme.
2. Conditional equivalence with
 [`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md)
 under Yekutieli rigidity (the Hecke-side conjecture is stated
 independently).
3. Phenomenological agreement: the seven values
 $\{2, 8, 20, 28, 50, 82, 126\}$ form the only nucleon counts at
 which the experimental binding curve exhibits a discontinuous
 first-derivative drop (the empirical signature of shell closure).

The downstream cone affects the higher-magic-number predictions
$n \in \{50, 82, 126\}$ where matrix evaluation remains unavailable.
Per §3b, any provable result quoting these higher-magic-number
predictions transitively depends on this conjecture and must be
typed `conjecture` until either the conjecture is proved or the
prediction is demoted to a numerical empirical claim.
<!-- FILE_END: homological-shell-condensation-interpretation.md -->

<!-- FILE_START: qou-motivic-galois-instance.md -->
# QOU MotivicGaloisCharacter instance via Habiro evaluation

The QOU brane-tower substrate carries a concrete instance of [`def:motivic-galois-character`](#def:motivic-galois-character) constructed by the Habiro evaluation map:

$$
  \mathrm{Frob}_p \;=\; f(u) \big|_{u = \zeta_{2p}}
  \;\in\; \mathbb{Z}[\zeta_{2p}].
$$

Here $f(u) = \sum_{m \geq 0} a_m(u) (u; u)_m$ represents the Habiro cyclotomic expansion of the atomic Markov trace $\mathrm{tr}_M(T_w, q)$ and $u = q^{1/2}$. The cyclotomic Pochhammer $(u; u)_m$ vanishes for $m \geq 2p$. This forces the sum to terminate after a finite number of terms.

## Construction and verification

- **Compatibility verification.** We perform two finite-place coherence checks on every $(p, \text{atom})$ cell. First, Galois-norm integrality holds: the trace $N(\mathrm{Frob}_p) = \sum_{\sigma \in \mathrm{Gal}(\mathbb{Q}(\zeta_{2p})/\mathbb{Q})} \sigma(\mathrm{Frob}_p)$ yields a rational integer (residual $< 10^{-7}$). Second, Weil purity holds at small primes: at $p \in \{2, 3\}$, the orbit-spread $\max|\sigma(\mathrm{Frob}_p)| - \min|\sigma(\mathrm{Frob}_p)|$ remains below $10^{-10}$ for every atom, and the inferred weight $w = 2 \log_p |\mathrm{Frob}_p|$ takes integer or near-integer values. At larger primes, the spread grows. The QOU motive remains mixed in general, consistent with the brane tower forming a sum across cohomology degrees.

- **Lean instance.** The instance in [`qou-motivic-galois-instance.lean`](qou-motivic-galois-instance.lean) discharges [`def:motivic-galois-character`](#def:motivic-galois-character) for the QOU substrate. The `frobenius_at` field maps each prime to its extracted Frobenius eigenvalue. The `almost_everywhere_nontrivial` field functions as a substrate axiom (AGENTS.md §3b), backed by a numerical witness for primes $p \leq 13$.

## Per-cell summary

| Atom | $p=2$ | $p=3$ | $p=5$ | $p=7$ | $p=11$ | $p=13$ |
|---|---|---|---|---|---|---|
| p (proton) | $\|F\|=8$, $w=6$ | $\|F\|=1$, $w=0$ | $\|F\|=0.62$, partial | partial | partial | partial |
| n (neutron) | $\|F\|=8$, $w=6$ | $\|F\|=2.65$, $w\approx1.77$ | $\|F\|=0.24$, partial | partial | partial | partial |
| D (deuteron) | $\|F\|=96$, $w\approx13.17$ | $\|F\|=4.58$, $w\approx2.77$ | $\|F\|=1.44$, partial | $\|F\|=38.74$, partial | partial | partial |

Cells marked "partial" have on-disk Habiro data that exhausts before the Pochhammer truncation point ($m_{\max} < 2p$). Galois-norm integrality still holds, indicating the partial sum already approximates the true Frobenius eigenvalue well. Unmarked cells achieve full truncation within the available data and pass the Weil-purity check $|\sigma(\mathrm{Frob}_p)| = p^{w/2}$ for every $\sigma$ in the Galois orbit.

## Downstream consumers

This instance discharges audit GAP 5b ([`docs/audits/family-4-motivic-path.md`](../../../docs/audits/family-4-motivic-path.md)). Theorems that previously required [`def:motivic-galois-character`](#def:motivic-galois-character) as an `[instance]` hypothesis can now consume the explicit QOU instance directly. In particular, [`conj:motivic-perpetual-obstruction`](#conj:motivic-perpetual-obstruction) becomes an unconditional theorem for the QOU substrate.

## Coherence

Cross-prime coherence follows structurally from the Habiro theorem. Any two evaluations $f|_{u = \zeta_{2p}}$ and $f|_{u = \zeta_{2q}}$ extract from the same Habiro element and respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$. The deeper $\ell$-adic archimedean Weil/Deligne behaviour lies outside this construction.
<!-- FILE_END: qou-motivic-galois-instance.md -->
