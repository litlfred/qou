<!-- FILE_START: mass-theory-orphan-reconnect-intro.md -->
Blocks in this section were reconnected during the Phase 7
orphan audit.  They address structural results at the boundary
of the mass theory: Borromean Bloch-group elements, categorical
Higgs mechanism, interface-knot Markov traces, isospin from
canonical bowtie, and spectral completeness conditions.  Each
awaits integration into a thematic section above as the mass
chapter's internal structure stabilises.

The arc proceeds through the Borromean-Bloch group element, the
categorical Higgs mechanism, the interface-knot Markov-Z block,
the isospin-from-canonical-bowtie derivation, and the supporting
refinement / projection / completeness blocks ($\rho_K H_{3a}$
refinement, $H_4 \otimes H_3$ half-symmetric projection, weak
spectral completeness).
<!-- FILE_END: mass-theory-orphan-reconnect-intro.md -->

<!-- FILE_START: categorical-higgs-mechanism.md -->
**Conjecture (categorical Higgs mechanism — skeleton).**
*The Higgs mechanism — the symmetry-breaking $SU(2)_L \times U(1)_Y
\to U(1)_{\rm em}$ in which three of the four electroweak gauge
bosons "eat" three Goldstone scalars to become massive — admits a
**categorical** formulation in $\mathbf{C}$ in which Goldstone-
eating is identified with **topological linking** of closed-braid
representatives.*

This is a **skeleton** (status: work-in-progress) for the open
gap flagged in
`conj:force-carrier-knot-vs-link-dichotomy`
§Status item 1.

### Setup

Let $A$ be the substrate algebra of a QOU $(\mathbf{C}, \varTheta,
G, \mathcal{S})$ over the categorical ring $R$, with $q \in R$
generic (not a root of unity, $q \neq 1$). Pre-EWSB, the
$SU(2)_L \times U(1)_Y$ gauge sector consists of four mediators
realised as **1-component knots** (single trace strand each),
images in $\mathrm{Hom}_R(\mathbf{1}, A)$:

- $W^1, W^2, W^3$ (the $\mathfrak{su}(2)_L$ triplet)
- $B$ (the $\mathfrak{u}(1)_Y$ singlet)

A Higgs doublet $\Phi$ provides four real scalar degrees of
freedom; choosing a vacuum aligned with $U(1)_{\rm em}$ gives:

- $\sigma$ (the surviving Higgs scalar, $H$ in PDG notation)
- $\pi^1, \pi^2, \pi^3$ (three Goldstone scalars, would-be massless)

### Categorical Higgs claim

Post-EWSB, the three broken gauge bosons each form a **2-component
link** with their associated Goldstone:

$$
  (W^+, \pi^+) \;\rightsquigarrow\; T(2, 4) \quad
  (W^-, \pi^-) \;\rightsquigarrow\; T(2, 4) \quad
  (Z, \pi^Z) \;\rightsquigarrow\; T(2, 6).
$$

The longitudinal mode of the gauge boson and the eaten Goldstone
fuse into the linked pair; the linking number $\mathrm{lk} = 1$
encodes the broken-generator multiplicity. The Higgs scalar
$\sigma$ remains a separate mediator, realised topologically as
$T(2, 8)$ (carrying the surviving Higgs degree of freedom).

The unbroken photon $\gamma = \cos\theta_W \, B + \sin\theta_W \, W^3$
remains a 1-component knot — image in $\mathrm{Hom}_R(\mathbf{1},
A)$ — and is identified with the saturating EM force-carrier
$T_{2,9}$ on Bring's surface
([`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace)).

### Categorical content (sketch)

**Step A — Goldstone scalars are knot objects pre-EWSB.**
Each of the four Higgs-doublet components is a 1-component knot
in $\mathrm{Hom}_R(\mathbf{1}, A)$ (since they are scalars in
$\mathbf{C}$, not endomorphisms). Three of them ($\pi^{\pm}, \pi^Z$)
will become "eaten."

**Step B — Linking is the categorical operation.**
Define the **categorical linking** of two 1-component knots
$\hat\beta_1, \hat\beta_2$ as the morphism

$$
  \mathrm{Lk}_R \colon \mathrm{Hom}_R(\mathbf{1}, A) \otimes
  \mathrm{Hom}_R(\mathbf{1}, A) \;\to\; \mathrm{End}_R(A)
$$

induced by the braid composition $\hat\beta_1 \cdot \hat\beta_2$
with non-trivial topological linking number $\mathrm{lk} \geq 1$
between the two strands. (The trivial linking $\mathrm{lk} = 0$
gives the disjoint tensor $\hat\beta_1 \otimes \hat\beta_2$,
remaining in $\mathrm{Hom}_R(\mathbf{1}, A^{\otimes 2})$.)

**Step C — Higgs mechanism is $\mathrm{Lk}_R(\text{boson},
\text{Goldstone})$.**
Pre-EWSB, the boson $W^a$ and the Goldstone $\pi^a$ each live in
$\mathrm{Hom}_R(\mathbf{1}, A)$ separately. Post-EWSB, the
Higgs-doublet vacuum-expectation-value $\langle \Phi \rangle \neq 0$
induces a specific $\mathrm{Lk}_R(W^a, \pi^a)$ braid topology
with $\mathrm{lk} = 1$, identifying the pair as a 2-component
link in $\mathrm{End}_R(A)$. The combined object now carries an
additional operator-strand (the Goldstone-strand), and its
Markov trace acquires the link-specific q-deformed Wedderburn weight
$\tilde w_\lambda = \dim_q^2/[n]_q!$.

**Step D — Mass via q-deformed Wedderburn weight.**
The mass of the post-EWSB boson is the Markov-trace eigenvalue of
its 2-component-link image, weighted by the Hoefsmit cell-content
projector
([`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)).
Specifically, the rest-mass energy is

$$
  m_X \;=\; \mathrm{tr}_M\bigl( e_X^{(\rm Hoefsmit)}
  \cdot \beta(T(2, 2k_X)) \cdot e_X^{(\rm Hoefsmit)} \bigr)
  \cdot E_\times \cdot \mu_0
$$

where $e_X^{(\rm Hoefsmit)}$ is the appropriate Hoefsmit-pattern
projector and $E_\times \cdot \mu_0$ is the unit-mass scale per
[`crossing-energy.md`](#def:crossing-energy).

### Requirements for completing the skeleton

1. **Rigorous definition of $\mathrm{Lk}_R$** as a categorical
   operation in a ribbon $\mathbf{C}$ —
   — now authored as
   [`conj:categorical-linking-operation`](#conj:categorical-linking-operation)
   (Tier A1, this branch). Five open structural properties
   (linearity, $k = 0$ reduction, multiplicativity, trace-cut
   symmetry, bar-involution compatibility) pending discharge.
2. **Derivation of $\theta_W$ (Weinberg angle)** as a categorical
   parameter of the linking, identifying $\cos\theta_W,
   \sin\theta_W$ as Hecke eigenvalues / Frobenius traces on
   specific projectors —
   — now authored as
   [`conj:weinberg-angle-categorical`](#conj:weinberg-angle-categorical)
   (Tier A2, this branch). Simple-multiplicity reading canonical
   fails; corrected version requires non-uniform Hoefsmit
   multiplicities + the Higgs-vev induced Hoefsmit-decomposition
   automorphism.
3. **Connection to U4** — the count of three broken generators is
   currently structural (from the four-generator $SU(2)_L \times
   U(1)_Y$ minus one surviving $U(1)_{\rm em}$). Categorical
   derivation requires
   `conj:electroweak-mass-eigenstate-count`.
4. **Mass formula** — Step D is currently a categorical
   *interpretation* of a Hoefsmit-projector trace; deriving
   absolute mass values (matching CODATA $m_W = 80.4$ GeV, $m_Z
   = 91.2$ GeV, $m_H = 125.3$ GeV) requires the constrained-
   PSLQ structurally derived from the Hoefsmit cell-content
   arithmetic + the per-pattern multiplicities $(2, 1, 3, 3, 1,
   2)$. Gated on (1) and (2) above.
### Audit-flag impact

If discharged, this conjecture supplies the categorical
**linking** operation that underlies path-α-Bring's
matter-knot/force-link distinction, closing the principal open
gap of
`conj:force-carrier-knot-vs-link-dichotomy`.
Combined with the Hoefsmit cell-content identification at
$n = 6$, it provides the structural-derivation pathway for the
EW boson masses ($W, Z, H$) — closing **NV-1** in the audit.
<!-- FILE_END: categorical-higgs-mechanism.md -->

<!-- FILE_START: interface-knot-markov-z.md -->
**Proposition (Interface-knot contribution to canonical-atom Markov trace).**

*Let $\mathcal{B}_K \in H_{3A}(q)$ be the canonical atomic braid for atom
$K = (Z, N)$ with $A = Z + N$, decomposed as*
$$
  \mathcal{B}_K \;=\; \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K
$$
*where $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)}$
is the disjoint Hecke product on disjoint 3-strand blocks (constituent
vacuum, `def:ew-interface-knot`) and
$\bowtie_K$ is the interface knot — a product of single-generator
crossings at the strand-block boundaries
$g \in \{3, 6, \ldots, 3(Z+N-1)\}$, each one either $\sigma_g$
(positive) or $\sigma_g^{-1}$ (negative).*

*Then the Markov trace ratio satisfies the **Markov-axiom interface
identity***
$$
  \boxed{\;
    \frac{\tau_M(\mathcal{B}_K)}{\tau_M(\mathcal{B}_K^{\mathrm{vac}})}
    \;=\; z(q)^{p_+(K)} \cdot \bigl(z(q) - h(q)\bigr)^{p_-(K)}
  \;}
  \tag{$\star$}
$$
*exactly, where $z(q) = 1/(q^{1/2}+q^{-1/2})$ is the Markov parameter,
$h(q) = q - q^{-1}$ is the Hecke skein parameter, and $p_+(K)$ /
$p_-(K)$ are the counts of positive / negative interface generators
in $\bowtie_K$.*
### Corollaries

1. **Atom-braid trace factorisation.** For any canonical atomic braid:
   $$
     \tau_M(\mathcal{B}_K) \;=\; z^{p_+(K)} \cdot (z-h)^{p_-(K)} \cdot \tau_M(\mathcal{B}_K^{\mathrm{vac}}).
   $$
   This iterated product is formalised sorry-free as the theorem
   `interface_knot_markov_z` (Lean), proved by induction over the interface
   list from the two single-step identities (`interface_knot_markov_z_single`
   for $z$, `interface_knot_markov_z_negative` for $z-h$).

2. **Per-Z step.** Adding a proton (Z+1) inserts one positive interface
   (p-* boundary): $\tau_M$ multiplies by $z$.

3. **Per-N step within a pair.** Adding a neutron after an existing
   neutron (n-n boundary) inserts one negative interface: $\tau_M$
   multiplies by $z - h$ (not by $z$).

4. **Per-N step crossing pair-flavor.** Adding a neutron after a proton
   (p-n boundary) inserts one positive interface: factor $z$.

5. **Phase 5b $\cosh(h)$ correction lives ELSEWHERE.** The per-Z step
   factor $\alpha \approx [3]_q^2 \cdot \cosh(h)$ identified in
   `conj:alpha-cosh-h-z-step-correction`
   is at the **single-block $|\Delta_\lambda^*|$ extraction level**,
   not the full $\tau_M$ ratio. The $\tau_M$-level identity is
   *exact* ($\star$); the single-block-level correction is *empirical*
   and structurally distinct.

### Proved structural corollaries (binding assembly)

Two correctly-scoped structural facts about the binding assembly
`B = E_0\,\tau_M(\mathcal{B}_K^{\mathrm{vac}})\,(1-\prod_i f_i)` are formalised
sorry-free alongside the interface identity (same `.lean` file):

1. **Interface-deficit saturation** (`QOU.BraidKnot.InterfaceDeficit`). For bond
   factors $f_i \in [0,1]$ the deficit $D = 1-\prod_i f_i$ satisfies
   $0 \le D \le 1$, is monotone in the bond list, and the marginal deficit of an
   added bond is $(1-f)\prod < 1-f$. This is the *proved* form of the 4-body
   assembly observation: the multiplicative deficit **saturates** (extra bonds
   contribute ever less) — it does **not** show the interface program is
   excluded, only that the bond *count/topology* cannot supply unbounded scaling.
2. **SU(4) shell closure** (`QOU.BraidKnot.SU4Supermultiplet`). The
   fully-antisymmetric Wigner supermultiplet $[1^A] = \Lambda^A(\mathbb{C}^4)$ has
   dimension $\binom{4}{A}$, so it vanishes for $A>4$: ${}^4\mathrm{He}$ (the SU(4)
   singlet) is the last s-shell supermultiplet. Theorem `su4_shell_closure`.

### Implementation reference

- formalism: the canonical formalism
- Witness: `computations/delta-lambda-fr-identity-phase5c.witness.json` (2 assertions; **Markov-axiom interface identity passes to $10^{-15}$ rel. err.**)
- Cross-reference: `def:ew-interface-knot` (the canonical interface-knot definition).
- Cross-reference: Phase 5c.1 audit doc covers the empirical extraction; this proposition is the categorical resolution.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: interface-knot-markov-z.md -->

<!-- FILE_START: rho-k-h3a-refinement.md -->
**Proposition (H_{3A} Wedderburn refinement of $\rho_K$ beyond leading-order; conditional on [`conj:hoefsmit-scattering-pipeline`](#conj:hoefsmit-scattering-pipeline)).**
*Let $K$ be an $A$-nucleon atom with braid word $\mathcal{B}_K \in B_{3A}$,
and let $\mathrm{tr}_M$ denote the canonical Markov trace on $H_{3A}(q)$
([gs-graded Markov trace existence](#conj:gs-graded-markov-trace-existence)).
Then the categorical density
$\rho_K = M(K) / (m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|)$
admits the **Wedderburn-Schur decomposition**

$$
  \rho_K(q)
  \;=\;
  \rho_K^{\mathrm{LO}}(Z, N)
  \;+\;
  \frac{1}{|\mathrm{tr}_M(\mathcal{B}_K)|}
  \sum_{\lambda \vdash 3A}
    y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\Delta_\lambda(K)
$$

*where:*

- *$\rho_K^{\mathrm{LO}}(Z, N) = (Z\cdot m_p + N\cdot m_n) /
  (m_e\cdot|\mathrm{tr}_M(\mathcal{B}_K)|)$ is the **constituent-mass leading-
  order ansatz** verified to $\le$ 0.1 % residual on $\{D, T, {}^3\mathrm{He}\}$
  (rho-k-leading-order verification);*
- *$y_\lambda(q)$ is the **Wenzl-bridge central coefficient** of
  the partition $\lambda \vdash 3A$
  ([Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge));*
- *$\chi^\lambda(\mathcal{B}_K)$ is the **Hoefsmit character** of $\mathcal{B}_K$
  in the irrep $\rho_\lambda$
  ([Hoefsmit scattering pipeline](#conj:hoefsmit-scattering-pipeline));*
- *$\Delta_\lambda(K) \in \mathbb{R}$ is the **block-binding correction**
  encoding how the per-$\lambda$ Wedderburn block contributes to the
  total mass beyond the constituent piece.*

**Statement of the refinement.**
*The mass formula in the $\rho_K$ assembly
(§T6 unit-convention resolution)*

$$
  M(K) \;=\; \rho_K(q) \cdot m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|
$$

*is **exact** modulo the values of $\Delta_\lambda(K)$.  The leading-
order ansatz amounts to setting $\Delta_\lambda(K) \equiv 0$, in which
case the $\sum_\lambda$ contribution collapses by the
Schur-Weyl identity
$\sum_\lambda y_\lambda \chi^\lambda(\mathcal{B}_K) = |\mathrm{tr}_M(\mathcal{B}_K)|$
to give exactly $\rho_K^{\mathrm{LO}}\cdot m_e \cdot |\mathrm{tr}_M|
= Z\cdot m_p + N\cdot m_n$ — the constituent mass.  The residual
binding-energy contribution lives entirely in the $\Delta_\lambda$
profile.*

**Status.**
*This proposition refines `prop:rho-k-scaling-structure`
([2026-04 witness `rho-k-scaling-structure.witness.json`](https://github.com/litlfred/qou/blob/main/computations/rho-k-scaling-structure.witness.json))
and complements
`prop:six-term-mass-formula-complete`
by giving the **exact** $\rho_K$ closed form rather than the
narrative six-term decomposition.  Compute is stubbed in
the canonical formalism;
full evaluation requires summing $p(3A)$ partitions
($p(3) = 3$, $p(6) = 11$, $p(9) = 30$, $p(12) = 77$,
$p(30) = 5604$, $p(60) = 966\,467$) with Hoefsmit characters
$\chi^\lambda$ and the closed-form $y_\lambda$ from
[`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge).*

**Derivation.**

*Step 1 — Wedderburn block decomposition.*
*By [`prop:wedderburn-as-noncomm-fourier`](#prop:wedderburn-as-noncomm-fourier),
$H_{3A}(q) \;\cong\; \bigoplus_{\lambda \vdash 3A} M_{f_\lambda}(K(q))$,
so any element $T \in H_{3A}(q)$ admits a unique decomposition
$T = \sum_{\lambda \vdash 3A} T_\lambda$ with $T_\lambda \in M_{f_\lambda}$.
Applying this to $T_{\mathcal{B}_K}$ (the Hecke representative of the
atomic braid word) and taking the Markov trace block-by-block:*

$$
  |\mathrm{tr}_M(\mathcal{B}_K)| \;=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K),
$$

*the **Schur-Weyl identity** for the canonical Markov trace
([prop:schur-weyl-mass-decomposition](#prop:schur-weyl-mass-decomposition)).
This identity is exact at any $q$ (no truncation).*

*Step 2 — Mass formula in Wedderburn coordinates.*
*By [`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf), the atomic
mass functor $M$ satisfies the GS-graded factorization*

$$
  M(K) \;=\; m_e \cdot \sum_{\lambda \vdash 3A}
    y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\bigl(1 + \Delta_\lambda(K)\bigr),
$$

*where the $1$ piece reproduces the Schur-Weyl identity in Step 1
(weighted by $m_e$ to convert cat-units to MeV at the constituent
level), and $\Delta_\lambda(K)$ encodes the deviation of the
block-by-block mass contribution from constituent sum.  Concretely,
$\Delta_\lambda(K)$ is the **per-block binding fraction**:*

$$
  \Delta_\lambda(K) \;=\;
  \frac{M_\lambda(K) - m_e\cdot y_\lambda\,\chi^\lambda(\mathcal{B}_K)}
       {m_e \cdot y_\lambda \chi^\lambda(\mathcal{B}_K)},
$$

*with $M_\lambda(K)$ the mass-functor's $\lambda$-block component.*

*Step 3 — Recover $\rho_K^{\mathrm{LO}}$ at $\Delta \equiv 0$.*
*Setting $\Delta_\lambda \equiv 0$ in Step 2 and dividing by
$m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|$:*

$$
  \rho_K\Big|_{\Delta = 0}
  \;=\;
  \frac{m_e \cdot \sum_\lambda y_\lambda \chi^\lambda(\mathcal{B}_K)}
       {m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|}
  \;=\; 1,
$$

*so $\rho_K^{(0)} \cdot m_e \cdot |\mathrm{tr}_M| = m_e \cdot
|\mathrm{tr}_M|$, **not** the constituent mass.  The constituent
mass enters via the $A=1$ instances ($K = p, n$) which fix
$y_{(1)}\chi^{(1)}(\mathcal{B}_p) = m_p / m_e$ and analogously for the
neutron.  Substituting back:*

$$
  \rho_K^{\mathrm{LO}} \;=\; \frac{Z\cdot m_p + N\cdot m_n}
                                  {m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|}
$$

*as stated.*

*Step 4 — Refinement formula.*
*Subtracting Step 3 from Step 2 and dividing by $m_e \cdot |\mathrm{tr}_M|$:*

$$
  \rho_K - \rho_K^{\mathrm{LO}}
  \;=\;
  \frac{1}{|\mathrm{tr}_M(\mathcal{B}_K)|}
  \sum_\lambda y_\lambda \chi^\lambda(\mathcal{B}_K) \Delta_\lambda(K),
$$

*which is the refinement claim.  $\blacksquare$*

**Connection to the six-term narrative.**

*The narrative six-term decomposition (T1+T2+T3+T4+T5+T6) is a
**partial-fraction split** of $\rho_K \cdot m_e \cdot |\mathrm{tr}_M|$
along principal-part boundaries (Mittag-Leffler complementarity, see
T6 mittag-leffler decomposition);
the Wedderburn-Schur decomposition above is a **partition-indexed
split** along irreducible blocks.  Both are exact; they correspond
to different choices of basis for the same $|\mathrm{tr}_M|$.  The
$\rho_K$ assembly is a single multiplicative factor (one number per
atom) while the six-term narrative is six conceptually distinct
contributions; the user-facing predictions are **identical**.*

*This proposition is the math content behind P3 in
[`AUDIT-DEEP-2026-05.md`](../../../AUDIT-DEEP-2026-05.md) §7.
Compute follow-up: full $\Delta_\lambda$ extraction at $A \ge 2$.*
<!-- FILE_END: rho-k-h3a-refinement.md -->

<!-- FILE_START: rho-k-h3a-refinement-interpretation.md -->
**Remark (interpretation).**

- *The leading-order ansatz $(Z\cdot m_p + N\cdot m_n)/(m_e\cdot|\mathrm{tr}_M|)$
  is the **$\Delta \equiv 0$ truncation** of the full Wedderburn-Schur
  decomposition.  Its 0.1 %-level residuals on $D, T, {}^3\mathrm{He}$
  are precisely the binding energies and reflect non-vanishing
  $\Delta_\lambda$.*
- *The block-binding correction $\Delta_\lambda$ is **block-local**:
  different partitions $\lambda$ contribute independently.  This is
  the categorical analogue of the **shell structure** picked up by
  the SEMF asymmetry / pairing terms.*
- *To reach 1 ppb mass-prediction accuracy, one must compute
  $\Delta_\lambda(K)$ for every $\lambda \vdash 3A$ in the
  Plancherel-dominant cone (per
  [`conj:hoefsmit-scattering-pipeline`](#conj:hoefsmit-scattering-pipeline) §142 –
  bound MAE$(k) \le C_0 \cdot [2]_q^{-2(k-3)}$).  At the substrate
  $q_0 = 1.109978595554181\ldots$ (50 dps), $[2]_{q_0}^2 \approx 4.04$, so each level
  reduces residual by $\sim 4\times$; nine levels suffice to drop
  $0.3 \%$ to $0.3 \% / 4^9 \approx 1$ ppb.*
<!-- FILE_END: rho-k-h3a-refinement-interpretation.md -->

<!-- FILE_START: s4-s3-half-symmetric-projection.md -->
**Proposition (conditional on
[`conj:borromean-baryon-mass-formula`](#conj:borromean-baryon-mass-formula)
— half-symmetric $H_4$ projection extracts one octahedral cell via
$S_4 \downarrow S_3$ branching).**
*The half-symmetric Wedderburn projection on $H_4(q)$, further
restricted to the $S_3$-trivial subspace (where $S_3$ acts by permuting
the three components of the Borromean rings $\mathcal{B}_3$), extracts
the curvature contribution of exactly **one** of the 8 ideal octahedral
cells in the $\mathcal{B}_3$-complement tessellation.*
## Structural role in $\mathrm{VolDensity}(\mathcal{B}_3)$ refinement

> ** reframing.** This section originally proposed a
> Yekutieli per-cell additive form
> $\lambda_{\text{scale}}^{\text{Yekutieli}} = \tfrac{5}{2} + (\tfrac{3}{4} - G)\,h^2$.
> That form was **purged from production** on (commit
> `71d674da1`) as non-canonical:  found the natural-reading
> bijection gives the per-cell curvature $\kappa = +0.5$, not $-G$,
> and no categorical derivation supplies a $-G \cdot h^2$ term.
> Per , the
> canonical mass formula is
> $$m(K) = m_e \cdot \mathrm{VolDensity}(K, q_0),$$
> with no separate $\lambda_{\text{scale}}$ constant.

The bijection $\tfrac{5}{2} \times \tfrac{2}{5} = 1$ established
above is a **structural input** that constrains how
$\mathrm{VolDensity}(\mathcal{B}_3, q_0)$ should evaluate at $h^2$
order on the half-symmetric Wedderburn subspace: exactly one of the
eight ideal octahedra of $S^3 \setminus \mathcal{B}_3$ is selected
by the combined H_4 half-symmetric projection and $S_3$-trivial
restriction. The bijection is sound combinatorics regardless of
any per-cell curvature value; it speaks to *which* cell contributes,
not *how much* it contributes.

The "how much" question — the per-cell curvature value — remains
open. The framework's current production prediction
$m_p \approx 965\;\text{MeV}$ ($+2.89\%$ vs CODATA) is the
$\mathrm{VolDensity}(\mathcal{B}_3)$ value at the framework's
current categorical-exactness order; refining that exactness at
higher $h^2$ orders is the open frontier (see the Family A gap
audit [`docs/audits/-family-a-gap-audit.md`](https://github.com/litlfred/qou/blob/claude/family-a-gap-audit-/docs/audits/-family-a-gap-audit.md),
currently in ;
relative path resolves once that PR merges).
This bijection is one of two structural inputs needed for the
refinement (the other being the $S_5 \leftrightarrow SO(3)$ fiber
action on Bring's surface).
<!-- FILE_END: s4-s3-half-symmetric-projection.md -->

<!-- FILE_START: weak-symmetric-normalization.md -->
**Proposition (weak-sector symmetric-channel normalization
$\mathcal{N}_{\rm sym}(q)$).**

*Let $R$ be the categorical coefficient ring with $q \in R$ generic
(not a root of unity in $R$, $q \neq 1$). The
[weak-sector spectral completeness](#conj:weak-spectral-completeness)
identity*

$$
  e_W^{+} + e_W^{-} + e_Z^{+} + e_Z^{-} + e_H^{+} + e_H^{-}
  \;=\; \mathbf{1}_{H_2(q)}
$$

*assigns each EW projector $e_X^\pm$ ($X \in \{W, Z, H\}$) a
Plancherel weight $w_X^\pm = (\dim_q \mathrm{im}\, e_X^\pm)^2 /
[2]_q! \in R$. The **symmetric-channel normalization**
$\mathcal{N}_{\rm sym}(q) \in R$ is defined as the Frobenius-trace
ratio*

$$
  \mathcal{N}_{\rm sym}(q)
  \;:=\;
  \frac{\sum_{X \in \{W, Z, H\}} \tau\!\left( e_X^{+} \cdot
        \beta(T(2, 2k_X)) \cdot e_X^{+} \right)}
       {\sum_{X \in \{W, Z, H\}} w_X^{+}}
  \;\in\; R,
$$

*where $k_W = 2, k_Z = 3, k_H = 4$ are the even-twist parameters.
Equivalently, $\mathcal{N}_{\rm sym}(q)$ is the Plancherel-weighted
character product over the EW symmetric channel — exactly the analog
for the EW sector of [`prop:gram-determinant-plancherel-ratio`](#prop:gram-determinant-plancherel-ratio)
$\delta_{CS}(q)$ for the EM sector.*

### Statement (formal)

The Hecke algebra $H_2(q)$ over $R$ has Wedderburn decomposition
$H_2(q) \cong R e_+ \oplus R e_-$ with sym/alt block projectors

$$
  e_+ \;=\; \frac{\sigma_0 + q^{-1}}{q + q^{-1}},
  \qquad
  e_- \;=\; \frac{q - \sigma_0}{q + q^{-1}}.
$$

Per `prop:even-twist-torus-link-psd-feasibility`,
$\sigma_0^{2k}$ acts as $q^{2k}$ on $e_+ H_2(q) e_+$ and as
$q^{-2k}$ on $e_- H_2(q) e_-$. The Frobenius trace satisfies

$$
  \tau(e_+) \;=\; \tau(e_-) \;=\; \frac{1}{[2]_q},
$$

(uniform across blocks since both are 1-dimensional). The
**symmetric channel** is the direct sum $e_W^+ \oplus e_Z^+ \oplus
e_H^+$ across the three even-twist parameters, and

$$
  \mathcal{N}_{\rm sym}(q)
  \;=\;
  \frac{\frac{1}{[2]_q}\,(q^4 + q^6 + q^8)}{\frac{3}{[2]_q}}
  \;=\;
  \frac{q^4 + q^6 + q^8}{3}
  \;=\;
  \frac{q^4 (1 + q^2 + q^4)}{3}.
$$

(One can equally express this as $q^6 \cdot [3]_{q^2} / 3$ where
$[3]_{q^2} = 1 + q^2 + q^4$ is the $q^2$-integer.) This is a
**closed-form $R$-element** with no free parameters once
`conj:electroweak-higgs-torus-link-triplet`
fixes $k \in \{2, 3, 4\}$.

### canonical evaluation (for cross-checks)

At $q_0 \approx :val[q_0]{precision=6, witness=computations/q-pinning-50-digit.witness.json}$ (50 dps):
- $q^4 \approx 1.5170$
- $q^6 \approx 1.8694$
- $q^8 \approx 2.3035$
- $\mathcal{N}_{\rm sym}(q_0) \approx (1.5170 + 1.8694 + 2.3035)/3 \approx 1.8966$

This is the **structural input** that the constrained-basis PSLQ
search for $N_v$ requires (Phase D of
`docs/audits/-path-alpha-bring-refinement.md`).

### Superseding structural input — direct cell-content trace

The proper structural input for the $N_v$ closed form is the
**bar-self-dual cell-content trace**

$$
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  4\bigl(q^{18} + q^{-18}\bigr)
  + 2\bigl(q^{10} + q^{-10}\bigr)
  + 1\bigl(q^{6} + q^{-6}\bigr)
  + 3\bigl(q^{2} + q^{-2}\bigr)
$$

derived in
[`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)
**without** invoking Plancherel weights. The corresponding
constrained-PSLQ basis for $N_v$ should use this trace as the
structural input — not the Plancherel-weighted form below.

### Connection to the closed-form $N_v$ ansatz (legacy framing)

Per the parallel pipeline with [`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace),
an earlier-proposed closed form for $N_v$ was

$$
  N_v \;\stackrel{?}{=}\;
  \frac{[4]_q \cdot [6]_q \cdot [8]_q}{[2]_q^{\,a}}
  \cdot \mathcal{N}_{\rm sym}(q)^{\,b}
  \cdot (1 + \delta_{\rm EW}(q)),
$$

with $\delta_{\rm EW}(q)$ a small Plancherel correction (analog of
$\delta_{CS}$). **This ansatz was based on the Plancherel-weight
framing now demoted.** A revised ansatz using
$\mathrm{tr}_{\rm pure}$ as the structural input is the operative
direction; concrete exponents are determined by the LP/SDP solve
on the EW sector + PSLQ uniqueness on the
$\{[4]_q, [6]_q, [8]_q, [2]_q, \mathrm{tr}_{\rm pure}\}$ basis,
**not** the Plancherel basis.
### Audit-flag impact

If $\mathcal{N}_{\rm sym}(q)$ is the right structural input,
**NV-1** closes:
$G_F = 1/(\sqrt{2} v^2)$ becomes a closed-form $R$-rational
expression in $\{q, [k]_q\}$ alone, with $v = N_v \cdot E_\times
\cdot \mu_0$ derived from the categorical EW spectral data.

**Audit doc.** [`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md).
<!-- FILE_END: weak-symmetric-normalization.md -->

<!-- FILE_START: z-eq-n-rho-correction.md -->
For light atoms on the **doubly-symmetric line $Z = N = k$**, the
canonical Kashaev binding-energy law

$$
  B_{\rm Kashaev} \;=\; \rho_{\rm struct} \cdot m_e \cdot
  \mathrm{Vol}_{\rm hyp}(K_A)
$$

acquires a **substrate-q correction** at finite $q$ that we
conjecture takes the form

$$
  B(Z\!=\!N\!=\!k,\;q)
  \;=\;
  m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A) \cdot
  \bigl(\rho_{\rm struct} + A - [A]_q\bigr),
  \qquad A = 2k.
$$

At $q = 1$: $[A]_q = A$, recovering the classical integer Kashaev
law.

### Empirical support

canonical exact match at $q_0 = 1.10998\ldots$ for the four atoms in the table
([per-atom δρ canonical evaluation](../../../computations/per-atom-rho-deviation.witness.json)):

| atom | err (Kashaev) | err (corrected) | improvement |
|------|--------------:|----------------:|------------:|
| ${}^2$H   | $+1.090\,\%$  | $+0.011\,\%$    | $\times 99$ |
| ${}^4$He  | $+5.867\,\%$  | $+0.057\,\%$    | $\times 103$ |
| ${}^{12}$C  | $+5.410\,\%$  | $+0.063\,\%$    | $\times 86$ |
| ${}^{16}$O  | $+5.301\,\%$  | $+0.152\,\%$    | $\times 35$ |

${}^{12}$C and ${}^{16}$O close *via propagation* through the existing α-cluster
formula: their predicted binding energies are derived from
$B(\!^4\!\mathrm{He})$ as
$B(\!^{4n}\!\mathrm{X}) = n \cdot B(\!^4\!\mathrm{He}) + \binom{n}{2} \cdot c_{\alpha\alpha}$;
once $B(\!^4\!\mathrm{He})$ closes, the doubly-magic α-cluster chain
follows without re-fitting.

### Categorical interpretation

The dimensional anomaly $A - [A]_q$ identifies as the deficit of the
**q-dimension of the natural representation**
$V^{(A-1)} = \mathrm{Sym}^{A-1}(V)$ of $U_q(\mathfrak{sl}_2)$:

$$
  A - [A]_q
  \;=\;
  \dim_\mathbb{C} V^{(A-1)} \;-\; q\text{-dim}_q V^{(A-1)}.
$$

At $q > 1$ the q-dimension exceeds the integer dimension, so the
correction has sign $-([A]_q - A) < 0$: the integer Kashaev law
**overestimates** the binding by exactly the dimensional anomaly,
scaled by $m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A)$.

### Restriction to the Z=N line

The Z=N line has a Z$\leftrightarrow$N exchange symmetry of the substrate fluid
that the formula respects. For $Z \neq N$ atoms (${}^{3}$H, ${}^{3}$He), the
formula fails: ${}^{3}$H and ${}^{3}$He have q-corrections differing by $2.9\,\%$,
ruling out any Z$\leftrightarrow$N exchange-symmetric closed form and pointing to
a **Coulomb-asymmetry** correction
(cf. [Coulomb-q-Hecke audit](../../../docs/audits/-coulomb-q-hecke-principled.md))
that the substrate alone cannot absorb.
<!-- FILE_END: z-eq-n-rho-correction.md -->

