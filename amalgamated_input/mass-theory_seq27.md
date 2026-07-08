<!-- FILE_START: lepton-mass-tower-canonical.md -->
> **⚠ Resolution update (2026-06-30).** The muon knot-ID is the torus knot $T(2,5)$, and $4_1$ is the Higgs. Torus-knot leptons carry zero intrinsic hyperbolic volume. The charged lepton mass originates from its coupling to the Higgs. The per-braid tower evaluation presented below tests the lepton's intrinsic isolated tower, not its mass. The material is retained as a scope-limited negative on the isolated-tower hypothesis.

**Conjecture (canonical lepton-mass tower).**
*Let $\ell \in \{\mathfrak{e}, \mu, \tau\}$ be a charged lepton with canonical braid representative $K_\ell$. The lepton mass evaluates as:*

$$
  \mathfrak{m}(K_\ell)
  \;=\;
  m_e \cdot \mathcal{F}_\ell(q)
  \;=\;
  m_e \cdot \xi_\ell(q) \cdot \mathrm{Vol}_q^{\mathrm{tower}}(K_\ell).
$$

*The evaluation occurs entirely within the canonical per-braid mass tower, without invoking the superseded scalar density $\rho_q$.*

The atomic graded expansion evaluates nuclear mass by adding constituent nucleon masses to binding-energy corrections. Leptons lack nucleon constituents. The isolated lepton mass requires a separate canonical formula.

The operative Skein formula evaluates the $m_\mu / m_e$ ratio using the Kashaev limit $\mathrm{Vol}(4_1)/\hbar_q^2$. The direct operator-level Markov-trace ratio yields $\sim 0.27$, falsifying the Skein formula as a direct pre-limit identity. The canonical $\mathcal{F}_\ell(q)$ must supply the missing magnitude at the finite substrate $q_0$.

**Two-constraint obstruction.**
Any working $\mathcal{F}_\ell(q)$ must satisfy two constraints simultaneously. 
1. **Nonzero on torus knots.** The electron $T(2,3)$ and tau $T(2,7)$ are torus knots. Their hyperbolic volume vanishes identically. The Skein formula fails to predict $m_\tau / m_e$ entirely. 
2. **$O(10^2)$ mass ratios.** If $\xi_\ell(q)$ is a universal scalar, it cancels in inter-lepton ratios. The symmetric $\mathrm{Li}_2^q$ tower yields $O(1)$ ratios, missing CODATA values by factors of $30$ to $130$. 

The symmetric $\mathrm{Li}_2^q$ tower lacks the $1/\hbar$ Kashaev blow-up required to supply the $O(10^2)$ magnitude.

**Faddeev $\Phi_q$ probe.**
Substituting the Faddeev quantum dilogarithm $\Phi_q$ injects the required $1/\hbar$ enhancement but fails to reproduce CODATA. The muon $4_1$ evaluation diverges severely near the $\Phi_q$ convergence radius. The $T(2,5)$ evaluation undershoots. The muon knot-ID split ($4_1$ vs $T(2,5)$) governs the divergence behavior entirely.

The isolated $\Phi_q$ per-braid tower cannot close the lepton mass ratios. The mass generation requires the $4_1$ Higgs coupling mechanism.
<!-- FILE_END: lepton-mass-tower-canonical.md -->

<!-- FILE_START: lepton-bring-surface-h3-3channel.md -->
*For any torus-knot lepton candidate $K_\ell = \sigma_1^{2m+1}$, the additive Wedderburn volume $\hat V_\ell^{\mathrm{full}}$ evaluates via the $H_3$ 3-channel Plancherel-weighted character sum:*

$$
  \hat V_\ell^{\mathrm{full}}
  \;=\;
  W_{\mathrm{sym}} \cdot q^{2m+1}
  \;+\;
  W_{\mathrm{std}} \cdot (z \cdot a_{2m+1} + b_{2m+1})
  \;+\;
  W_{\mathrm{alt}} \cdot (-q^{-1})^{2m+1},
$$

*where $W_\lambda$ are the $H_3$ Plancherel weights and $(a_{2m+1}, b_{2m+1})$ are the Hecke recursion coefficients.*

The framework embeds nucleons on the Bring surface via 3 quark color tubes. The lepton embedding utilizes the 3 $H_3$ Wedderburn channels. Both configurations project 3-fold substrate representations into single observables. The $H_3$ evaluation satisfies the cohomological discipline linking 3 calibration inputs to 3 Wedderburn channels.

Evaluating the electron $\sigma_1^3$ recovers the calibration $\hat V_e^{\mathrm{full}} \approx 0.586$. The tau candidate $T(2,7)$ forces $\hat V > q_0$, breaching the $\mathrm{Li}_2^q$ convergence radius and diverging. The lepton mass evaluation requires the Higgs coupling resolution.
<!-- FILE_END: lepton-bring-surface-h3-3channel.md -->

<!-- FILE_START: conj-lepton-tower-h-n-plus-1-branching.md -->
**Conjecture (lepton-tower closure factor).**
*Let $K_\ell$ be the canonical knot for the lepton at tower-index $m$ (electron $m=1$, muon $m=2$, tau $m=3$). The canonical mass-tower correction factor is*

$$
  \xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q}.
$$

The factor $(2m-1, m, 2m)$ exhibits strict symmetry in $h = q - q^{-1}$. The odd upper index contributes a bar-anti-symmetric upper-jet bracket. The even lower index contributes a bar-symmetric closing trace. This precise amphichiral reflection reflects the knot-operator equivalence structural directive.

The predicted muon factor $[3]_q \cdot [2]_q / [4]_q$ matches the empirical requirement to within $0.001\%$. The tau factor $[5]_q \cdot [3]_q / [6]_q$ matches to within $0.79\%$. The algebraic identities reducing these brackets are Lean-verified. The full categorical derivation of this branching factor from the $H_{2m+1}$ substrate remains open.
<!-- FILE_END: conj-lepton-tower-h-n-plus-1-branching.md -->

<!-- FILE_START: conj-atom-braid-exterior-algebra.md -->
**Conjecture (atom-braid exterior-algebra structure).**
*Let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word. Its image in $H_{3A}(q)$ generates a sub-algebra whose Gröbner-Shirshov normal-form filtration shape is given by:*

$$
  \dim_R \bigl(F_k(T_w(Z, N))\bigr) \;=\; \binom{3A - Z}{k - (Z - 1)}.
$$

*The sub-algebra is isomorphic to the exterior algebra $\Lambda^*(R^{3A - Z})$ with grade shift $\delta = Z - 1$.*

The canonical atom-braid populates a fermion Fock-space subalgebra of $H_{3A}(q)$. Each interface between adjacent strands contributes one binary degree of freedom. The proton count $Z$ enforces dimension reduction (removing one degree of freedom per proton) and a grade shift (offsetting the filtration bound).

This exterior structure restricts the active dimension profoundly. For $^4\mathrm{He}$, the dimension collapses from the $12!$ standard Wedderburn basis to exactly $2^{10} = 1024$. The restriction governs the computational complexity of the canonical solver.
<!-- FILE_END: conj-atom-braid-exterior-algebra.md -->

<!-- FILE_START: conj-psd-trace-orthogonality.md -->
**Conjecture (PSD-vs-trace orthogonality).**
*Decompose $H_{3A}(q)$ into Wedderburn blocks. The partitions maximising the Hecke Markov-trace weight $|y_\lambda(q_0)|$ are 1- or 2-row long-string partitions. The partitions minimising the PSD-cone scaling eigenvalue are 3+row multi-step tall-narrow partitions. No partition belongs to both classes.*

The two objectives of the operator-selection problem—maximising the Markov trace and minimising the PSD scaling penalty—pull the solution toward disjoint sectors of the Young lattice. The tension forces the optimal knot operator into compromise Wedderburn channels.
<!-- FILE_END: conj-psd-trace-orthogonality.md -->

<!-- FILE_START: three-halves-structural-factor.md -->
*Let
$R$ be a field, $q \in R$ with $q \neq 0$, $h = q - q^{-1}$, and
$[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ the symmetric
q-integer. The following five algebraic identities hold:*

**Muon set** *(canonical for $T(2,5)$, used by `conj:lepton-tower-h-n-plus-1-branching` at $m = 2$):*

$$
3 + h^2 = [3]_q
$$
$$
(2 + h^2) \cdot [2]_q = [4]_q
$$
$$
\frac{3 + h^2}{2 + h^2} = \frac{[3]_q \cdot [2]_q}{[4]_q}
$$

**Tau set** *(canonical for amphichiral $10_{43}$ candidate, used by `conj:lepton-tower-h-n-plus-1-branching` at $m = 3$):*

$$
[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)
$$
$$
\frac{[5]_q \cdot [3]_q}{[6]_q} = \frac{[5]_q}{[2]_q \cdot (1 + h^2)}
$$

## Lean

All five identities are proved in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean)
over generic `[Field R]` per AGENTS.md §7c, using
`field_simp; ring`. Generic-ring proofs apply at the substrate
$q_0 \approx 1.110$ by specialisation; canonical cross-checks at
exact representation exact algebraic structures verify each identity to $\leq 10^{-40}$ in the
[`tau-amphichiral-sdp-canonical evaluation.witness.json`](../../../computations/canonical evaluations/tau-amphichiral-sdp-canonical evaluation.witness.json)
witness (assertions `lean_three_plus_h_sq_eq_bracket3`,
`lean_two_plus_h_sq_times_bracket2_eq_bracket4`,
`lean_bracket6_eq_bracket2_bracket3_times_one_plus_h_sq`).

## Role in the framework

The structural identities reveal that the canonical lepton-tower
closure factors $\xi_m$ live in a single $h$-graded family of
$q$-bracket products. Concretely:

- **Muon** ($m = 2$, $K_\mu = 4_1$): closure factor
  $\xi_2 = [3]_q \cdot [2]_q / [4]_q = (3+h^2)/(2+h^2)$ — closes
  $m_\mu/m_e$ via $\mathrm{Vol}(4_1)/\hbar_q^2$ to 0.034 % of CODATA
  (`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`).
- **Tau** ($m = 3$, $K_\tau = 10_{43}$ candidate): closure factor
  $\xi_3 = [5]_q \cdot [3]_q / [6]_q$ — closes $m_\tau/m_e$ via
  $\mathrm{Vol}(10_{43})/\hbar_q^2$ to +0.79 % of CODATA
  (`docs/audits/-t6-f-ell-derivation-attempt.md`
  followup section). The reduction
  $[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)$ is the fundamental
  identity behind this closure.

The generic family is the subject of
`conj:lepton-tower-h-n-plus-1-branching`; this proposition supplies
the proved algebraic core for the muon (m=2) and tau (m=3) cases.
<!-- FILE_END: three-halves-structural-factor.md -->

<!-- FILE_START: rem-im-q-vs-p-skew.md -->
The framework has **two distinct projection mechanisms** that each
discard structural content. They are often conflated, yet **must
be kept separate**:

## Two mechanisms

### Mechanism 1 — bar projection (real-q phenomenon)

Per [bar-involution.md](bar-involution.md), every Hecke-algebra
element decomposes as $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$
under the bar involution $q \mapsto q^{-1}$ (equivalently
$\eta = \log q \mapsto -\eta$). The framework's **canonical
projection is $P_{\mathrm{avg}}$** (bar-symmetric, $\cos$/$\cosh$/$\mathrm{Li}_2^q$
content); the bar-anti-symmetric $P_{\mathrm{skew}}$ ($\sin$/$\sinh$/$\Phi_q$
content) is **discarded by construction**.

For **real** $q > 0$, $\eta = \log q$ is real, $\sinh(\eta)$ is a
real number, and $P_{\mathrm{skew}}$ content is **real-valued**.
Sibling makes
this explicit for torus knots:
$Q_m(\eta) = \sinh((2m+1)\eta) / (2 \cosh \eta)$ is real at real $q_0$.
Per
[`crossing-energy-interpretation.md`](../observations/crossing-energy-interpretation.md),
$\sinh(\log q)$ is the **EM / Coulomb channel**. So the EM /
P_skew content **exists** for real $q$ and is discarded by the
canonical projection.

### Mechanism 2 — modulus projection (complex-q phenomenon)

Per [`prop:categorical-mass-markov`](categorical-mass-markov.md),
the categorical mass formula is

$$\mathfrak{m}_{q, \mathcal{K}} = \mathrm{tr}_M(\rho(\beta_\mathcal{K})).$$

The $|\cdot|$ is the modulus. For real $q$, $\mathrm{tr}_M$ is real
and $|\cdot|$ is trivial (absolute value of a sign). For
**complex** $q$, $\mathrm{tr}_M$ becomes complex and $|\cdot|$
genuinely projects: $\mathrm{Im}(\mathrm{tr}_M)$ is discarded.

## A common incorrect claim

A natural-but-incorrect claim is "Im(q) = EM channel = P_skew channel".
This conflates the two mechanisms. The correct statements are:

| Quantity | Source | Status at real q |
|---|---|---|
| $P_{\mathrm{skew}}$ content (sinh, EM channel) | bar projection | **Real-valued, non-zero**, discarded |
| $\mathrm{Im}(q)$ content | complex-q parameter | **Zero by convention** (q real); would generate complex tr_M if non-zero |
| $\mathrm{Im}(\mathrm{tr}_M)$ content | modulus projection | **Zero by convention** for real q; generated by Im(q) $\ne$ 0 |

So:
- P_skew is **kept then discarded** by the framework even at real q.
- Im(q) is **set to zero** by the framework's real-q convention, not "discarded by a projection".
- These are independent.

## Significance

Quantitative consequences differ between the two mechanisms:

1. **Resolving the +0.17% $\mathfrak{Q}_\beta$ residual**: this requires either
   (a) the missing P_skew content at real q (the P_skew channel
   that bar-projection discards), or (b) Im(q) $\ne$ 0 producing
   complex tr_M whose modulus closes the residual.
   - Per [Phase A v2 audit](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md)
     §Path D + the audit at
     [`m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md):
     **(b) is ruled out under the current ansatz** (residual is
     positive everywhere on the Apollonius circle).
   - **(a) is open** — accessible via the explicit Q_m P_skew
     content from .

2. **Resolving the canonical lepton-mass formula** $F_\ell(q)$
   ([`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md)):
   the ratio $|\mathrm{tr}_M(K_\mu)| / |\mathrm{tr}_M(K_e)|$ is
   robust against $\mathrm{Im}(q)$ at leading order (modulus
   projection invariance), but **NOT** robust against the
   bar-projection discarding $P_{\mathrm{skew}}$ content
   (the discarded sinh-channel could shift the LO ratio).

3. **Physical interpretation**: $P_{\mathrm{skew}} = $ EM/charge-distinguishing
   channel (sibling  documents this for torus knots).
   $\mathrm{Im}(q) = $ a substrate moduli parameter (not directly
   physical until tied to an observable Im observable, which the
   framework does not currently provide).

## Cross-references

- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — bar vs Hermitian * involutions; this remark interprets/refines its complex-q discussion
- [`prop:q-zero-complex-extension`](q-zero-complex-extension.md) — substrate polymorphism (admits complex q)
- [`prop:categorical-mass-markov`](categorical-mass-markov.md) — modulus projection definition
- [`bar-involution.md`](bar-involution.md) — bar projection definition
- Sibling PR [#1153](https://github.com/litlfred/qou/pull/1153) — explicit P_skew = sinh formula for torus knots
- Audit: [`docs/audits/-complex-q-historical-trajectory.md`](../../../docs/audits/-complex-q-historical-trajectory.md) — historical context of ℂ in physics
- Audit: [`docs/audits/-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md) §Implications — Phase 3 finding distinguishing the two mechanisms
- [`crossing-energy-interpretation.md`](../observations/crossing-energy-interpretation.md) — `sinh(log q)` = Coulomb channel identification
<!-- FILE_END: rem-im-q-vs-p-skew.md -->

<!-- FILE_START: conj-im-q-physical-role.md -->
**Conjecture (physical role of Im(q)).**
*The substrate parameter $q$ admits a complex extension
([prop:q-zero-complex-extension](q-zero-complex-extension.md)).
The current QOU framework's observables (categorical masses
$\mathfrak{m}_{q,\mathcal{K}} = |\mathrm{tr}_M|$ and per-braid
mass tower) are real-valued and **insensitive to $\mathrm{Im}(q)$
at leading order** under modulus projection ($\mathrm{Im}(q)$
shifts both numerator and denominator of mass ratios in tandem
via the modulus operation). The physical role of $\mathrm{Im}(q)$
— if any — must therefore be sought in observables not currently
in the framework.*

*This conjecture catalogues three candidate roles, each
testable against a specific observable class. Identifying
which (if any) is the correct physical interpretation is open
work.*

## Exclusions for Im(q)

Per [`rem:im-q-vs-p-skew`](rem-im-q-vs-p-skew.md), Im(q) is **NOT**:
- The EM / $P_{\mathrm{skew}}$ channel (this is a real-q mechanism)
- A fourth calibration input (the 3-CAL count is cohomologically forced)
- An observable in the current framework (mass formula uses $|\cdot|$)
- Equal to $\mathrm{Im}(\mathrm{tr}_M(\rho(\beta)))$ — Im(q) is a parameter; Im(tr_M) is the value induced

## Three candidate physical roles

### Candidate (i) — chirality / orientation parameter

In the Kashaev regime ($q$ a root of unity, $q = e^{2\pi i/N}$),
the q-deformed Hecke algebra produces N-fold quantum symmetries
whose Markov traces give hyperbolic volumes (Kashaev volume
conjecture). For complex $q = |q| e^{i \arg q}$ near the unit
circle, $\arg q$ is naturally a **chirality coordinate** —
positive arg gives clockwise braid orientation; negative arg
gives counterclockwise. The categorical mass formula is invariant
under $q \mapsto \bar q$ (complex conjugation under modulus
projection), consistent with mass being chirality-invariant.

**Testable**: does the framework's prediction for an explicitly
chirality-sensitive observable (e.g., parity-violating decay
asymmetry; CP violation in $K^0$-$\bar K^0$ mixing) require
$\arg q \neq 0$?

### Candidate (ii) — phase coordinate dual to CAL-2

CAL-2 ($m_\mu/m_e = 206.7682830$) gives **one real equation** on
two real unknowns ($\mathrm{Re}(q), \mathrm{Im}(q)$). The solution
set is an **Apollonius circle** in the complex q-plane (center
$\approx 1.010$, radius $\approx 0.100$ per the formal derivation).
The framework's real-axis solution $q_0 \approx 1.10998$ is one
point on this circle; Im(q) is the arc coordinate parametrizing
the other admissible q values.

**Testable**: does another CAL-2-like independent constraint
(a second real equation from $m_\tau/m_e$, or from a different
observable) fix a unique complex $q_0$? If only real solutions
exist, candidate (ii) is closed; if a complex solution is needed,
the framework has missed an Im(q)-coupled measurement.

### Candidate (iii) — non-Hermitian deformation / open-system parameter

The Hoefsmit seminormal Hecke representation has real-coefficient
matrices for $q > 0$ real, giving **unitary** $H_n(q)$ representations.
For complex $q$ with $|q| \neq 1$, unitarity breaks: representations
become non-unitary; eigenvalues become complex. In quantum mechanics,
non-Hermitian operators arise in **open systems** (decay, dissipation,
resonance widths).

**Testable**: do decay widths (Γ for unstable particles — W, Z,
top, resonances) correlate with the Im(q) needed to make Hecke
representations describe their non-Hermitian dynamics? Most decay
widths in the Standard Model have categorical interpretations open
in the QOU framework.

## Obstacles to a current proof

Each candidate requires an observable the framework does not yet
provide:
- (i) needs explicit chirality-sensitive observables (CP violation, parity asymmetry)
- (ii) needs a second independent CAL-2-like constraint
- (iii) needs a categorical formula for decay widths $\Gamma$

The framework's mass formula explicitly **projects away** Im(q)
content via $|\cdot|$, so no mass observable can detect Im(q)
directly. The candidate roles are all in **non-mass observables**.

## Connection to other conjectures

- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) F_ℓ
  — the canonical lepton-mass formula is Im(q)-robust (modulus projection
  invariance); F_ℓ does NOT distinguish the three candidate Im(q) roles.
  Hence the F_ℓ conjecture is consistent with ALL three candidates.
- [`prop:rho-k-pair-gen-canonical-form`](conj-rho-k-pair-gen-canonical-form.md) —
  similarly Im(q)-robust at LO.
- The complex-q machinery is **decoupled** from the mass-formula closure;
  closing the $\mathfrak{Q}_\beta$ residual or deriving F_ℓ does **not** require resolving
  Im(q)'s role.

## Default value: Im(q) = 0

In the absence of an Im(q)-sensitive observable, the framework's
canonical choice is **$\mathrm{Im}(q_0) = 0$** (real q). This is:
- **Computationally simple**: real Hecke arithmetic, real
  $\mathrm{tr}_M$, real masses.
- **Empirically sufficient**: all known mass observables fit
  with real $q_0$ to the precision documented in `per-observable-100x-status.witness.json`.
- **NOT structurally forced**: nothing in the QOU framework's
  cohomological discipline requires $\mathrm{Im}(q) = 0$; it is a
  convention pending an Im-sensitive measurement.

## Cross-references

- [`prop:q-zero-complex-extension`](q-zero-complex-extension.md) — substrate polymorphism
- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — involution split for complex q
- [`rem:im-q-vs-p-skew`](rem-im-q-vs-p-skew.md) — the distinction from P_skew
- [`prop:categorical-mass-markov`](categorical-mass-markov.md) — modulus projection
- Audit: [`docs/audits/-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md) — Phase 3 finding
- Audit: [`docs/audits/-complex-q-historical-trajectory.md`](../../../docs/audits/-complex-q-historical-trajectory.md) — historical context
- Audit: [`docs/audits/-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md) §Q3 — Apollonius parametrization

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: conj-im-q-physical-role.md -->

