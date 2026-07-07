<!-- FILE_START: intro-alpha-k-procedure.md -->
The categorical mass coefficients $\alpha_k$ that appear in the
six-term mass formula are not free parameters: each $\alpha_k$ is
fixed by a deterministic substrate-split procedure that this
section formalises.  The procedure separates the flavor-dressing
contribution from the bare categorical mass and identifies the
$k$-dependence as a Jacobi–Pochhammer factorial in the
substrate parameter.

The arc has two layers.  The first six blocks define the
substrate-split decomposition and prove uniqueness of the
flavor-dressed mass; the remaining blocks specialise to small $k$
and verify the procedure against the explicit cases the next
section consumes.  The output of this section is the table
$\{\alpha_k\}_{k=1,\dots,6}$ that drives the six-term mass formula.
<!-- FILE_END: intro-alpha-k-procedure.md -->

<!-- FILE_START: confinement-sdp.md -->
The scalar [confinement LP](#prop:confinement-lp) is the
diagonal projection of a richer **semidefinite program** over
matrix-valued operators.  The SDP is the actual selection
principle computed by the multi-level pipeline
(the formal derivation,
the formal derivation, the formal derivation); the LP
obtains only when every Wedderburn block decouples.

## Primal SDP (matrix operator selection)

**Proposition.**
*Let $n$ be the Hecke strand count at confinement level $\ell$
and let $(\pi_\lambda)_{\lambda \vdash k, k \le n}$ be the
central idempotents projecting onto the Wedderburn blocks of
$H_n(q)$.  Let $T \in \mathrm{End}_R(H_n(R, q))$ be the cost
operator (Markov-trace weighting, or the $q$-Laplacian
resolvent).  The confined operator at $q$ is the solution
$\Phi^* \succeq 0$ of:*

$$
  \min_{\Phi} \quad \langle T, \Phi \rangle
  \qquad (\text{matrix action})
$$

*subject to:*

$$
  \Phi \;\succeq\; 0
  \qquad (\text{global PSD cone})
$$

$$
  \langle \pi_\lambda, \Phi \rangle \;\ge\; 0
  \quad \forall\, \lambda \vdash k,\ k \le n
  \qquad (\text{per-block Frobenius positivity})
$$

$$
  \begin{pmatrix}
    \Phi_{ii} & \Phi_{ij} \\
    \Phi_{ji} & \Phi_{jj}
  \end{pmatrix}
  \;\succeq\; 0
  \quad \forall\, \text{adjacent generator pairs } (i, j)
  \qquad (\text{$2 \times 2$ pair PSD})
$$

$$
  \mathrm{tr}(\Phi) \;=\; n_{\mathrm{target}}
  \qquad (\text{normalisation})
$$

*where the 2$\times$2 blocks range over adjacent pairs $(\sigma_i, \sigma_{i+1})$
in the Hecke generator chain — one block per confinement level from
$\ell = 3$ (baryonic) up to $\ell = 7$ (molecular), as tabulated in
the multi-level SDP infrastructure.*

## Dual SDP (matrix shadow prices)

*The dual program is:*

$$
  \max_{y_0, (y_\lambda)} \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to the **matrix inequality**:*

$$
  y_0 \cdot I \;+\; \sum_\lambda y_\lambda \cdot \pi_\lambda \;-\; T
  \;\preceq\; 0
$$

$$
  y_\lambda \ge 0 \quad \forall\, \lambda
$$

*The dual variable $y_0$ is the shadow price of the normalisation
constraint; $(y_\lambda)$ are the per-block shadow prices.
Strong duality holds under Slater's condition (a strictly
feasible $\Phi \succ 0$ exists at generic $q$), and at optimum:*

$$
  \Phi^* \cdot \bigl(y_0^* I + \textstyle\sum_\lambda y_\lambda^* \pi_\lambda - T\bigr) \;=\; 0
$$

*as a matrix equation.*

## Companion interpretive remarks

The exposition of *why* this SDP is the right object — feasibility
as a Hecke spectral-gap, the active-support reading of the dual,
the relation to the scalar LP, and the integer-restricted MISDP
variant — has been split into four companion remarks so that the
proposition statement above stays minimal:

* [Spectral-gap feasibility](#rem:confinement-sdp-spectral-gap):
  feasibility iff $|q + q^{-1}| > 0$; deconfinement = gap closure.
* [Multi-operator binding](#rem:confinement-sdp-multi-operator):
  active support $\mathcal{S}^*$, binding multiplicity, and why
  complementary slackness is a *matrix* equation.
* [Relation to the scalar LP](#rem:confinement-sdp-vs-lp):
  the LP as the diagonal restriction of the SDP; when each is
  exact.
* [MISDP variant](#rem:confinement-misdp): integer-constrained
  confinement levels.

The geometric face of this proposition — SDP optimality as
Picard--Lefschetz steepest descent, dual variables as thimble
depths — is developed in
the SDP-as-thimble-flow remark below.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: confinement-sdp.md -->

<!-- FILE_START: flavor-dressed-mass-from-substrate-split.md -->
**Proposition.**
*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor
dressing functor of [`def:flavor-dressing-functor`](flavor-dressing-functor.md),
let $M_N$ be the nucleon-mass average $(m_p + m_n)/2$, and let
$q = q_0$ be the substrate parameter.  Then the splitting between
the down- and up-quark dressed masses is determined by the substrate
flavor formula:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;=\;
  M_N \cdot \frac{(q - 1)^2 (1 - q^{-4})}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left(\bigl(\Delta m / M_N\bigr)^2\right).
$$

*The leading-order substrate-pure form (dropping the
$O\!\left((\Delta m / M_N)^2\right)$ correction) reads, using the
algebraic identity $(q-1)^2 (1 - q^{-4})/3 = (1/3)\,\hbar_q^2 \cdot h_q \cdot [2]_q$,*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;\approx\;
  \frac{M_N}{3} \cdot
  \hbar_q^2 \cdot h_q \cdot
  \frac{[2]_q\,(q^{1/2} + q^{-1/2})}{q + q^{-1}}
  \;=\;
  \frac{M_N}{3} \cdot
  \hbar_q^2 \cdot h_q \cdot
  \frac{1}{z_{\mathrm{mkv}}}
  \;\;\;\;\text{(at } q = q_0 \text{)},
$$

*where $z_{\mathrm{mkv}} = (q^{1/2} + q^{-1/2})^{-1}$.  The
canonical evaluation at $q = q_0$ and the matching CODATA residual
are tabulated in
[`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md)
(Observations chapter; per the manuscript convention canonical
substrate values stay out of geometry / braids chapters and are
collected with the other Physical-Observations numerology there).*

## Derivation

Combine two identities:

1. **Substrate side** ([`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md)):

   $$
     \frac{m_n - m_p}{M_N}
     \;\approx\;
     \frac{(q-1)^2 (1 - q^{-4})}{3}.
   $$

2. **Skein side** (proved via [`lem:pair-skein-mass-formula`](../observations/pair-skein-mass-formula.md)
   applied to the Borromean baryon braids of the proton and neutron):

   $$
     m_n - m_p
     \;=\;
     \frac{q + q^{-1}}{q^{1/2} + q^{-1/2}}
     \cdot
     (\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}).
   $$

Solving (2) for $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ and
substituting (1) gives the closed-form expression above.

## Calibration discipline

The CODATA value $m_n - m_p = 1.29333236\,\text{MeV}$ is **no longer
an input** of the production formula under
[`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md).
This proposition makes $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ a
derived output of the substrate parameter $q_0$ plus the nucleon-mass
scale $M_N = (m_p + m_n)/2$ (CODATA-anchored), removing the $u$–$d$
splitting from the calibration count.  $M_N$ itself is currently a
CODATA input (its substrate derivation is open — see
[`docs/audits/-1ppb-workplan-v4.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-1ppb-workplan-v4.md)),
The calibration boundary for this proposition is $\{m_e, q_0,
M_N\}$.

The remaining calibration inputs at the production-formula boundary
are $m_e$ and $q_0$ (with $\mathfrak{Q}_\beta$ as the third input until the
$\mathfrak{Q}_\beta$ substrate derivation lands; see
[`docs/audits/-1ppb-workplan-v4.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-1ppb-workplan-v4.md) for the open status).

## Individual values

The proposition pins the **difference** $\mu_{\mathfrak{d}} -
\mu_{\mathfrak{u}}$.  The individual values
$\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$ require additionally an
average $\bar\mu = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2$,
which is pinned by the baryon-content sum-rule
([`prop:neutron-proton-mass-splitting`](../observations/neutron-proton-mass-splitting.md)
of the proton and neutron braids):

$$
  m_p + m_n = 3(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})
    + \text{(Skein cross-terms)},
$$

so $\bar\mu \approx M_N / 3 \approx 312.97\,\text{MeV}$.  Combined
with the substrate splitting, this gives
$\mu_{\mathfrak{u}} \approx 311.10\,\text{MeV}$ and
$\mu_{\mathfrak{d}} \approx 312.39\,\text{MeV}$; see the companion
remark [`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md)
for the full numerology.
<!-- FILE_END: flavor-dressed-mass-from-substrate-split.md -->

<!-- FILE_START: flavor-mass-splitting-bound.md -->
**Theorem (substrate bound on the dressed-quark splitting).**
*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor
dressing functor of [`def:flavor-dressing-functor`](flavor-dressing-functor.md),
let $M_N$ be the nucleon-mass average, and let $q > 1$ be the
substrate parameter. Then the down–up splitting satisfies the
two-sided substrate bound*

$$
  0 \;<\; \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;<\; M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q,
$$

*where*
$\hbar_q = (q - 1)/q$,
$h_q = q - q^{-1}$,
*and* $[2]_q = q + q^{-1}$
*are the substrate Planck constant, the Hecke crossing scale, and
the doublet quantum integer respectively.*

## Rationale for the splitting-only form

The theorem statement bounds the **difference**
$\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ rather than the
individual masses $\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$. The
splitting-only form is preferred because:

- It is the **directly substrate-derivable** quantity — every factor
 on the right-hand side is a substrate-pure expression in $q$
 (no CODATA inputs, no fits).
- Individual values require an additional input
 $\bar\mu = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2$
 pinned by baryon-content sum rules (see
 [`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md)).
 Bounding the individual values would carry that pinning into the
 theorem statement, mixing substrate content with CODATA anchoring.
- The Lean proof factors through the existing substrate
 identities (no new bound props need to be authored).

## Slack ratio (symbolic)

The realised splitting from
[`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md)
relates to the bound expression by

$$
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q}
  \;=\;
  \frac{1}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left((\Delta m / M_N)^2\right).
$$

The dominant factor is the explicit $1/3$ in the substrate formula
of [`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md);
the Skein-side correction
$(q^{1/2} + q^{-1/2})/(q + q^{-1})$ is close to $1$ at the substrate
regime and contributes a small additional reduction. Together they
explain why the theorem's upper bound is loose: it does not absorb
either the explicit $1/3$ or the Skein correction. Tightening the
bound to match the realised value is open (no canonical closed form
is committed in this revision). The canonical evaluation at $q_0$
of both sides is tabulated in
[`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md).
<!-- FILE_END: flavor-mass-splitting-bound.md -->

<!-- FILE_START: alpha-k-derivation-procedure.md -->
**Setup.**
Working over $A = H_n(R, q)$ at generic $q$, with Markov parameter
$z = 1/(\sqrt q + 1/\sqrt q) \in R$.  Let $\{e_\lambda\}_{\lambda
\,\vdash\, n}$ be the central idempotents of the Wedderburn
decomposition.  The Jones–Markov trace
([Jones–Markov trace](#thm:jones-markov-trace)) admits a unique
expansion in central characters

$$
  \mathrm{tr}_M(\beta) \;=\; \sum_{\lambda \,\vdash\, n}
    y_\lambda \cdot \chi_\lambda(\beta),
  \qquad y_\lambda \in R,
$$

with $p(n) = \#\{\lambda \,\vdash\, n\}$ unknowns
$\{y_\lambda\}_{\lambda \,\vdash\, n}$.

**Proposition (linear-system characterisation of $y_\lambda$).**
*The Markov-trace property
$\mathrm{tr}_M(x \cdot T_n^{\pm 1}) = z^{\pm 1} \cdot
\mathrm{tr}_M(x)$, applied iteratively, fixes $\mathrm{tr}_M(w_\mu) =
z^{\,n - \mathrm{len}(\mu)}$ for every reduced word $w_\mu$ realising
the cycle type $\mu \vdash n$.  Substituting into the central
expansion yields the $p(n) \times p(n)$ linear system*

$$
  \sum_{\lambda \,\vdash\, n}
    \chi_\lambda(w_\mu)\, y_\lambda
  \;=\;
  z^{\,n - \mathrm{len}(\mu)},
  \qquad \mu \,\vdash\, n.
$$

*The character matrix $\bigl[\chi_\lambda(w_\mu)\bigr]_{\mu, \lambda}$
is invertible at generic $q$ (Schur–Weyl-Hecke duality), so the
system has a unique solution $y_\lambda \in R(\!(z)\!)$ — explicit,
$q$-rational, no fitting.*

**Formalization Goal Plausibility.** The current formalization proves the existence of a programmatic solution by effectively yielding `∃ y, y = solveJonesMarkov n S := ⟨_, rfl⟩`. The mathematical claim of *uniqueness* and *invertibility* of the character matrix is not yet fully formalized in Lean, as it requires a deep library of Schur-Weyl-Hecke duality and generic semisimple character theory. However, this gap is highly plausible to close because it is a standard, well-documented result in algebraic combinatorics (the non-degeneracy of the Hecke character table). The physical model relies on the existence of this unique derivation procedure, which is computationally verified, making the unformalized uniqueness a localized algebraic gap rather than a structural flaw in the mass theory.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: alpha-k-derivation-procedure.md -->

<!-- FILE_START: alpha-k-categorical-closure.md -->
The categorical mass formula
([unified mass](#prop:unified-curvature-rank-mass-formula))
expresses the vortex mass as a stratum-graded sum

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\;
  \sum_{k \geq 0} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)
  \;+\; m_e \cdot \tau(C_{\dim_q}),
$$

where $\alpha_k$ are the **stratum prefactors** at depth $k$,
computed via the Markov-pairing procedure of
[`prop:alpha-k-derivation-procedure`](#prop:alpha-k-derivation-procedure)
as $\alpha_k = \langle \mathrm{tr}_M, r_k \rangle$ with $r_k$ a
depth-$k$ reduced word representative.

At the **substrate level** (vortex-free, evaluated at a single
Planck-tick expansion variable $x = \hbar_q^2$) the resummation
should give a single dimensionless **tower correction factor**
multiplying the leading energy scale $E_0^{(N=0)} = m_e/(q_0(q_0-1))$,
producing the brane-tower-summed value
$E_0^{\text{full}} = E_0^{(N=0)} \cdot \mathcal{F}(\hbar_q^2)$
([`rem:beta-decay-energy-scale`](../particle-interactions/beta-decay-energy-scale.md)
§"tower-summed form").

## Statement

**Conjecture.**
*The categorical resummation $\mathcal{F}(\hbar_q^2)$ admits a
closed form in $q$, and that closed form lies in one of the two
families below (or is uniquely determined as a third closed
form that interpolates them):*

| Candidate | Closed form $\mathcal{F}(x)$ | Substrate $E_0^{\text{full}}$ | CAL-3 residual |
|-----------|-------------|--------------------------:|---------------:|
| **(a) Geometric** | $1/(1-x) = \sum_{k\geq 0} x^k$ | $:val[E_0_full_MeV]{precision=4}$ MeV | overshoots by $\approx +1.75\%$ |
| **(b) Symmetric q-dilogarithm** | $1 + (-\mathrm{Li}_2^q(-x)) = 1 + \sum_{n\geq 1} (-1)^{n+1} x^n/(n \cdot [n]_q)$ | $:val[E_0_full_li2q_MeV]{precision=4}$ MeV | overshoots by $\approx +1.74\%$ |
| **(c) Unknown / interpolating** | open | open | open |

(The dimensionless factor $\mathcal{F}(\hbar_q^2)$ at $q_0 \approx 1.110$ is the ratio of either column to $:val[E_0_N0_MeV]{precision=4}$ MeV — computed live from the witness.)

*The conjecture has three substantive sub-claims:*

1. **Existence:** *the resummation $\mathcal{F}(\hbar_q^2)$
   admits a closed form in $q$ derivable from the categorical
   $\alpha_k$ (no fitting, no opt-in parameter).*

2. **Selection:** *exactly one of the families (a), (b), or (c)
   is the correct closure, and the selection is fixed by the
   Frobenius pairing on $A$ via the Markov reduction structure of
   [`prop:categorical-mass-markov`](#prop:categorical-mass-markov).*

3. **CAL-3 closure direction:** *the correct closed form lies
   **below** $\mathcal{F}_{\mathrm{geom}}(\hbar_q^2) \approx 1.00992$,
   producing a framework-derived $E_0$ that **agrees** with the
   CODATA-calibrated $E_0^{(\text{cal})} \approx 4.155$ MeV instead
   of overshooting it.*

## Failure of the naive geometric recursion

A naive bridging would assert $\alpha_k = \hbar_q^{2(k-1)} \cdot \alpha_{k-1}$
for $k \geq 1$, so that $\sum_k \alpha_k \cdot \hbar_q^{2k} = \alpha_0 / (1 - \hbar_q^2)$.
**This recursion does not match the explicit $\alpha_k$ values at
$H_3$** computed by the Markov-pairing procedure
([`prop:alpha-k-derivation-procedure`](#prop:alpha-k-derivation-procedure)
"Worked example: $H_3(R, q)$"):

$$
  \alpha_0 = 1, \qquad
  \alpha_1 = 0, \qquad
  \alpha_2 = z^2, \qquad
  \alpha_3 = z(1 + q^{1/2} - q^{-1/2}),
$$

with $z = 1/(q^{1/2} + q^{-1/2}) \approx 0.499$ the Markov
parameter. The naive recursion would require $\alpha_2 = \hbar_q^2 \cdot \alpha_1 = 0$,
but the actual value is $z^2 \neq 0$. So the geometric closure
(a) is **not** the naive substitution; if it holds, it does so as
a non-obvious resummation identity over the $\alpha_k$ family.

## Plausibility of the bounded Li_2^q candidate

The mass-endomorphism tower
([`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)
lines 162–183) **proves** that the brane-tower integral evaluates
to $-\mathrm{Li}_2^q(-V)$ (symmetric q-dilogarithm), not
$\Phi_q(V)$ (Faddeev quantum dilogarithm — empirically off by
$10^6$ per
[`kashaev-integration-identity.witness.json`](https://github.com/litlfred/qou/blob/main/computations/kashaev-integration-identity.witness.json)).
At the substrate level (single Planck-tick variable $x = \hbar_q^2$)
the bounded analog $\mathcal{F}_{\mathrm{Li}_2^q}(x)$ matches the
geometric form $1 + x + O(x^2)$ at leading order and stays
bounded as $x \to 1$.

**However**, the substrate Li_2^q form **does not** close CAL-3 in
the correct direction (it gives $\approx +1.74\%$ vs the geometric
$\approx +1.75\%$ — a $0.01\%$ improvement). The per-atom Li_2^q
evaluation (per the prop's proper form $-\mathrm{Li}_2^q(-|\hat V_i|)$
summed over generators with atom-specific volumes
$|\hat V_i^{\text{full}}|$) may give a different and possibly
correct closure; that evaluation requires atomic-braid input and
is not a substrate-only computation.

## canonical evidence (substrate level)

Computed in
the canonical formalism
at $q_0 \approx 1.110$:

- $E_0^{(N=0)} \approx :val[E_0_N0_MeV]{precision=4}$ MeV — single Planck-tick (CAL-1 + CAL-2)
- $E_0^{\text{full,geom}} = :val[E_0_full_MeV]{precision=4}$ MeV — geometric closure
- $E_0^{\text{full,}Li_2^q} = :val[E_0_full_li2q_MeV]{precision=4}$ MeV — bounded q-dilogarithm closure
- $E_0^{(\text{cal})} \approx :val[E_0_calibrated_MeV]{precision=4}$ MeV — CODATA cross-check

The two candidate closures agree to four significant figures at
the substrate level. The CAL-3 residual remains an open finding
in the same direction for both.

## Discussion

**Open conjecture.** All three sub-claims (existence, selection,
direction) require categorical derivation. The closure proposal
is the recommended **first follow-up** after the E_0 disentanglement
([``](https://github.com/litlfred/qou/pull/673)) and is
listed as item 6 in the post-PR-#665 R&D inventory
(`rem:post-pr665-open-rd-inventory`).
The required input infrastructure (per-irrep $\chi_\lambda$ closed
forms, Wedderburn-block scaffolding) is in place and ready for the
categorical resummation analysis.
<!-- FILE_END: alpha-k-categorical-closure.md -->

<!-- FILE_START: chi-lambda-w0-sign-weighting.md -->
The empirical $c_k$ chain at $H_3$ (extracted from the
$\varepsilon^{2k}$ coefficients of $\chi_\lambda(\mathcal{B}_n; q) - \chi_\lambda(\mathcal{B}_p; q)$
at $q = 1 + \varepsilon$ per
[`rem:chi-per-irrep-cyclotomic-closed-forms`](#rem:chi-per-irrep-cyclotomic-closed-forms))
does **not** match a uniform Plancherel-weighted sum
$\sum_\lambda w_\lambda \cdot c_k^{(\lambda)}$ with the canonical
$w_\lambda = (\dim V_\lambda)^2 / n!$: the Plancherel-weighted
sum has the **wrong sign** at both $k = 5$ and $k = 6$ (see the
`per-wedderburn-block-ck` canonical evaluation witness's `c5_match_status` and
`c6_match_status` fields).

This proposition identifies the **correct weighting**: the
**character values at the long element** $w_0 \in S_3$, i.e.
$\chi_\lambda(w_0) = (1, 0, -1)$ for $\lambda \in \{(3), (2,1), (1,1,1)\}$.

## Statement

**Proposition.**
*Let $\mathcal{B}_p, \mathcal{B}_n \in \mathbf{B}_3$ be the canonical typed-braid
representatives of the proton and neutron, and define*

$$
  c_k^{(\lambda)} \;:=\; [\varepsilon^{2k}]\,
  \bigl(\chi_\lambda(\mathcal{B}_n;\,q) - \chi_\lambda(\mathcal{B}_p;\,q)\bigr)\Big|_{q = 1 + \varepsilon}
  \qquad (\lambda \vdash 3,\ k \geq 0).
$$

*Let $w_0 \in S_3$ denote the longest element (the unique element
of length $3$ in the Coxeter realisation; equivalently the
order-reversing involution $(1\,3)$ in cycle form). Then the
character-weighted sum*

$$
  S_k^{(w_0)} \;:=\; \sum_{\lambda \vdash 3}
    \chi_\lambda(w_0) \cdot c_k^{(\lambda)}
  \;=\; c_k^{(3)} \;-\; c_k^{(1,1,1)},
$$

*has the same sign as the empirical $c_k$ measured by the
Wenzl-bridge Markov trace at $H_3$
([`prop:alpha-k-derivation-procedure`](#prop:alpha-k-derivation-procedure))
for $k = 5$ and $k = 6$. The character values used are the
standard $S_3$ irreducible-character evaluations at the long
element:*

| $\lambda \vdash 3$ | irrep | $\dim V_\lambda$ | $\chi_\lambda(w_0)$ |
|--------------------|-------|------------------|---------------------|
| $(3)$              | trivial | $1$ | $+1$ |
| $(2,1)$            | standard (Hoefsmit) | $2$ | $0$ |
| $(1,1,1)$          | sign | $1$ | $-1$ |

## canonical structural verification

From [`per-wedderburn-block-ck.witness.json`](https://github.com/litlfred/qou/blob/main/computations/per-wedderburn-block-ck.witness.json)
( merge, per-Wedderburn-block canonical evaluation at $q = 1 + \varepsilon$
to order $\varepsilon^{12}$):

| $k$ | $c_k^{(3)}$ | $c_k^{(2,1)}$ | $c_k^{(1,1,1)}$ | $S_k^{(w_0)}$ | empirical $c_k$ | sign agreement |
|----:|------------:|--------------:|----------------:|--------------:|----------------:|:--------------:|
| $5$ ($\varepsilon^{10}$) | $0.25$ | $16.25$ | $266.5$ | $-266.25$ | $-395.41$ | yes |
| $6$ ($\varepsilon^{12}$) | $0.25$ | $22.5$ | $477.5$ | $-477.25$ | $-45485$ | yes |

Both signs agree. The magnitude ratios are
$|\text{empirical}/S_k^{(w_0)}| \approx 1.49$ at $k = 5$ and
$\approx 95.3$ at $k = 6$; the $S_3$ character weights are **necessary
but not sufficient** for full magnitude closure. The residual
factor must come from cross-block coupling (e.g. via the
$\sigma_1$ matrix elements that mix the 2-dimensional $V_{(2,1)}$
into the per-block-diagonal sum).

## The role of $w_0$ versus $-I$

The canonical evaluation agent that surfaced this finding referred to
the weighting as "character $\chi_\lambda(-I)$." In the symmetric
group $S_n$ realised as a Coxeter group, "$-I$" has no canonical
meaning (the group is not realised as matrices acting on a real
vector space with a $-I$ element); the closest analog is the
**longest element** $w_0 \in S_n$, which is the unique involution
of maximal length and plays the role of "central reversal." For
$S_3$ specifically, $w_0 = (1\,3)$ is the order-reversing
transposition, and its character values agree with the
informal "$-I$" reading because $w_0 \cdot w_0 = 1$ (involution)
and the irreducible $S_3$-characters on involutions are
$\chi_{(3)} = 1, \chi_{(2,1)} = 0, \chi_{(1,1,1)} = \mathrm{sgn}(w_0) = -1$.

The substantive content of the proposition is therefore: **the
$c_k$ Markov-trace decomposition is governed by the long-element
character, not the identity character**. This is consistent with
the Coxeter-theoretic role of $w_0$ as the maximal mixing element.
<!-- FILE_END: chi-lambda-w0-sign-weighting.md -->

<!-- FILE_START: atom-knot-mass-derivation.md -->
The prefactor $\nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$ used throughout
this block is the **SDP-solution multiplicity** in the Wedderburn
decomposition; it is distinct from the categorical density $\rho_K \in
\mathbb{R}_{>0}$ of
[`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md).

**Statement (categorical, pre-Archimedean form).** Let
$\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum
observable universe at substrate parameter $q_0$
([def:quantum-observable-universe](#def:quantum-observable-universe)),
let $\mathfrak{H}$ be a confined particle/atom of confinement level
$\ell$ and strand count $n_0$ with canonical Hecke element
$T_w \in H_{n_0}(q_0)$ in Gröbner–Shirshov normal form
([def:confined-particle](#def:confined-particle)). The
**categorical mass invariant** of $\mathfrak{H}$ is the finite-sum
element of $\mathbb{Q}(q)$

$$
M(\mathfrak{H}) \;:=\; \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H}) \;=\; \nu_{\mathrm{SDP}} \cdot \bigl[\,\mathrm{tr}_M(T_w) + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})\,\bigr],
$$

where $m(\mathfrak{H})$ is the **categorical mass invariant** in
the multi-term form of the
[unified knot mass formula](#thm:knot-mass-formula-unified):
$\mathrm{tr}_M(T_w)$ is the descended Markov trace
$\sum_\lambda y_\lambda(q)\,\chi_\lambda(T_w)$
(Wenzl-bridge coefficients $y_\lambda$,
$q$-Murnaghan–Nakayama character $\chi_\lambda$),
$\mathrm{tower}(T_w) = \sum_i \mathrm{Li}_2^q(-\hat{V}_i) + z^2 \sum_{i<j} \mathrm{Li}_2^q(-\hat{V}_i \hat{V}_j)$
is the brane tower built from per-generator additive-Wedderburn
volumes $\hat{V}_i$ (symmetric $q$-dilogarithm
$\mathrm{Li}_2^q$ per the paper canon,
[mass endomorphism tower](#prop:mass-endomorphism-tower)).
Per [`prop:li2q-phiq-bar-symmetrization`](li2q-phiq-bar-symmetrization.md),
$\mathrm{Li}_2^q$ is the **pre-Archimedean (categorical, $R$-side)**
form, bar-invariant under $q \mapsto q^{-1}$ and living in the Habiro
ring $\widehat{\mathbb{Z}[q]}[\![z]\!]$. The post-Archimedean
realization under $\tau_{\mathrm{arch}}$ is the bar-pair
$\tfrac{1}{2}(\log \Phi_q(z) + \log \Phi_{q^{-1}}(z))$, **not**
naive canonical substitution of $\mathrm{Li}_2^q$ at $q = q_0$; the
naive substitution kills the dimensional mass scale by the
bar-symmetric projection (empirical: $m_{\mathfrak{p}}/m_e \approx
3.31$ vs CODATA $1836$; see
[`m-p-m-e-li2q.witness.json`](https://github.com/litlfred/qou/blob/main/computations/m-p-m-e-li2q.witness.json)).
The $\sim 173\times$ shortfall flagged below is consistent with this
bar-projection structure; the $\rho_K$ closure path of
[`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md) and the Faddeev
$\Phi_q$ archimedean tower are the two reconciliation candidates.
The third summand $\mathrm{tr}_M(C_{\dim_q}) = \sum_{\lambda \vdash n_0} 1/\dim_q(\lambda)$
is the Frobenius co-Casimir trace
([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)).
The scalar $\nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$ is the
multiplicity of $T_w$'s SDP solution in the Wedderburn
decomposition (see algorithm step below). This expression is
**finite, exact, and entirely pre-Archimedean** — every quantity
on the right-hand side lives in $\mathbb{Q}(q)$.

**Mass identity (structural form).** After applying the
Archimedean realization functor
([archimedean realization functor](#def:archimedean-realization-functor)),
the binding energy of $\mathfrak{H}$ is

$$
\boxed{ \quad B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0} \;=\; m_e \cdot \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H})\big|_{q = q_0} \quad }
$$

— a single finite-categorical pipeline, no analytic asymptotic
content. The volume conjecture is *not* used in the derivation; it
appears only as a post-functor naming convention (see "Post-Archimedean
interpretation" below). **At $q_0$, this structural form
under-predicts $m_{\mathfrak{p}}$ by $\sim 173\times$; the closure
requires the additional categorical density $\rho_K$
([atomic-mass-gb-nf](#prop:atomic-mass-gb-nf)) whose substrate-only
derivation is open.**

## Architecture (single categorical pipeline; Yekutieli at finite slices)

The derivation is a **single categorical pipeline** that lives entirely
pre-Archimedean. Yekutieli's non-abelian Stokes theorem (multiplicative
integration on surfaces) at finite slice depth gives the following
correspondence between 2-categorical / surface-integration data and
the Iwahori–Hecke structure on $H_{n_0}(q_0)$:

See [Table 1](#tbl:atom-knot-mass-derivation-table1-data).

**Collapsing spectral sequence.** The GB filtration on $H_{n_0}(q)$
gives rise to a multiplicative spectral sequence
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence),
[prop:spectral-sequence-h3-explicit](#prop:spectral-sequence-h3-explicit))
whose $E_1$-page is the associated graded $\bigoplus_k \mathrm{gr}_k H_{n_0}(q)$.
By [prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse)
the spectral sequence **collapses at $E_2$ for semisimple $H_n(q)$ at
generic $q$** (the $d_2$-differential captures the Hecke quadratic
relation; higher differentials vanish because $H_n(q)$ has no further
relations beyond braid + Hecke). The $E_\infty$-page identifications
([prop:e-infinity-page-identifications](#prop:e-infinity-page-identifications))
recover the Wedderburn decomposition $\bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q))$.

Collapse is **the reason finite-slice computation suffices**: at finite
slice depth (= filtration grade $\leq$ some $k$), the surviving
$E_\infty$-classes already account for all of $\mathrm{tr}_M(T_w)$
because $d_r = 0$ for $r \geq 3$. No higher slices contribute. The
GB-filtration tracker's certificate
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json))
records exactly the data the $E_2 \Rightarrow E_\infty$ collapse needs:
filtration-graded coefficients per term, in jet order.

The *finite slice* is essential: at every finite resolution Yekutieli's
multiplicative integral is a finite product / finite sum in $\mathbb{Q}(q)$,
exact, with no asymptotic limit. This is exactly the categorical
content captured by the GB-filtration + jet-order certificate
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json)).

### Pipeline

```tex
\begin{tikzcd}[row sep=large, column sep=large]
\textbf{Categorical action of } \mathbf{C} \text{ on } \mathcal{S} \arrow[d, "\text{Yekutieli, finite slice}"]
\\
\textbf{Joint-tower confinement SDP at } q_0 \arrow[d, "\text{GB filtration} + \text{jet order}"]
\\
T_w \in H_{n_0}(q_0) \text{ (canonical, GB-NF)} \arrow[d, "\text{Wedderburn}"]
\\
H_{n_0}(q) \cong \bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q)) \arrow[d, "{y_\lambda \text{ (Wenzl)}, \chi_\lambda \text{ (q-MN)}}"]
\\
\mathrm{tr}_M(T_w) \;=\; \sum_\lambda y_\lambda(q) \chi_\lambda(T_w) \;\in\; \mathbb{Q}(q) \arrow[d, "\nu_{\mathrm{SDP}} \cdot m(\cdot)"]
\\
M(\mathfrak{H}) \;=\; \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H}) \;\in\; \mathbb{Q}(q)
\\
{} \arrow[d, "\text{\textbf{Archimedean realization functor}}"]
\\
B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0} \;\in\; \mathbb{R} \text{ (MeV)}
\end{tikzcd}
```

Everything above the Archimedean functor lives in $\mathbb{Q}(q)$;
$\mathbb{R}$ enters exactly once, at the substitution $q := q_0$
together with the multiplication by $m_e$. No analytic limit, no
volume conjecture, no Reeb-density construction is invoked.

### Post-Archimedean interpretation (borrowed, optional)

If $K = \widehat{T_w}$ is hyperbolic, the post-Archimedean number
$\mathrm{tr}_M(T_w)|_{q = q_0}$ admits a conventional 3-manifold-theory
naming via the **volume conjecture** (Kashaev 1997, Murakami–Murakami
2001): the asymptotic of $|J_K(\zeta_N)|^{1/N}$ at roots of unity
$\zeta_N = e^{2\pi i / N}$ as $N \to \infty$ equals
$\exp(\mathrm{Vol}_{\mathrm{hyp}}(K)/2\pi)$. This is a **borrowed
theorem about post-Archimedean analytic continuation**, allowing
$B(\mathfrak{H})/(m_e \nu_{\mathrm{SDP}})$ to be *named* as a hyperbolic volume in
conventional language. The QOU mass identity does **not** depend on
the conjecture — it depends only on the finite-categorical
$\mathrm{tr}_M(T_w)$.

In particular the geometric construction (Reeb-vortex density $\to$
Mostow $\to$ Gromov), available on the post-Archimedean side as
*another* way to write the same number, is **not part of the QOU
derivation** and need not be derived internally.

## Algorithm

```tex
\begin{algorithm}
\caption{\textsc{AtomKnotMass}: end-to-end categorical mass derivation
from $\mathfrak{H}$ to $B(\mathfrak{H})$.  Single categorical pipeline,
finite-slice (Yekutieli), no asymptotic content.}
\textbf{Input.}  Confined particle $\mathfrak{H}$ with confinement
level $\ell$, strand count $n_0$, registry entry in
\texttt{def:confined-particle}.  Substrate parameter $q_0$.
\\
\textbf{Output.}  $B(\mathfrak{H}) \in \mathbb{R}_{\geq 0}$ in MeV,
with methodology tag and high-precision certificate.
\\
\hrulefill
\\
\textbf{Pre-Archimedean (in $\mathbb{Q}(q)$, exact, finite):}
\begin{enumerate}
  \item Run the joint mass-tower confinement SDP on all
        $\ell' \leq \ell$ atoms simultaneously.  Output: a
        \emph{structured certificate} per atom recording
        \begin{enumerate}
          \item the canonical Hecke element $T_w \in H_{n_0}(q_0)$ in GB-NF,
          \item the Gröbner--Shirshov filtration grade per term
                (= Yekutieli slicing depth at finite slice),
          \item the jet-order of reductions
                (= temporal slice-traversal order).
        \end{enumerate}
  \item Compute the Markov trace symbolically in $q$ via the
        Wedderburn decomposition + Wenzl bridge:
        $\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda(q) \chi_\lambda(T_w)$
        (\texttt{prop:alpha-k-derivation-procedure}, $y_\lambda$ from
        Wenzl-bridge witness, $\chi_\lambda$ from $q$-Murnaghan--Nakayama).
        Yekutieli at finite slice ⇒ this is exactly the multiplicative
        trace on the closed surface obtained by Markov closure of
        $T_w$; the Hecke quadratic relation is the curvature 2-form
        at adjacent slices.
  \item Read $\nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$ from the
        structural prefactor rule on $(Z, N)$ (= the multiplicity
        of $T_w$'s SDP solution in the Wedderburn decomposition).
        Currently OPEN in general; confirmed values from the
        joint-tower SDP witness are $\nu_{\mathrm{SDP},D} = 1$,
        $\nu_{\mathrm{SDP},T} = 2$, $\nu_{\mathrm{SDP},{}^3\mathrm{He}} = 2$.
        The earlier statement "$\nu_{\mathrm{SDP}} = 1$ for
        $\ell \leq 1$" was too narrow — it holds for $D$ but is
        contradicted by the
        SDP witness for $T$ and ${}^3\mathrm{He}$ (each carrying
        $\nu_{\mathrm{SDP}} = 2$ from the multiplicity of the
        trefoil-like constituent in the $H_5$ / $H_3$ Wedderburn
        decomposition).
  \item Form the categorical mass invariant
        $M(\mathfrak{H}) := \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H}) \in \mathbb{Q}(q)$
        (multi-term form per the Statement above; the
        single-term shorthand $M = \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w)$
        is structurally inadequate and is no longer used).
\end{enumerate}
\textbf{Archimedean realization (functor $\mathbf{C} \to \text{Top}$, $\mathbb{Q}(q) \to \mathbb{R}$):}
\begin{enumerate}
  \setcounter{enumi}{4}
  \item Apply the Archimedean realization functor at $q = q_0$ and
        multiply by $m_e$:
        $B(\mathfrak{H}) := m_e \cdot M(\mathfrak{H}) \big|_{q = q_0}
        = m_e \cdot \nu_{\mathrm{SDP}} \cdot m(\mathfrak{H})\big|_{q = q_0}$,
        evaluated to $\geq 50$ decimal digits via MPFR.
  \item Compare to AME 2020 binding: residual
        $\Delta = B - B_{\mathrm{AME}}$ in MeV and ppb.
  \item Tag the result with one of:
        \texttt{principled-derivation} (categorical pipeline complete
        end-to-end), \texttt{principled-gb-nf} (trivial-NF entries
        only), \texttt{manual-historical-volume-match} (knot ID by
        earlier work, GB-NF derivation pending),
        \texttt{magic-A-formula} (algebraic shell-closure rule),
        \texttt{recursive-on-${}^{4}$He} (cluster recursion).
\end{enumerate}
\textbf{Optional post-Archimedean naming (borrowed, not in derivation):}
\begin{enumerate}
  \setcounter{enumi}{7}
  \item For hyperbolic $K = \widehat{T_w}$, the volume conjecture
        identifies $M(\mathfrak{H})/(m_e \nu_{\mathrm{SDP}})\big|_{q_0}$ with
        $\mathrm{Vol}_{\mathrm{hyp}}(K)$ in conventional 3-manifold
        terminology.  Used only as a name for the post-Archimedean
        number; \emph{not} part of the derivation.
\end{enumerate}
\end{algorithm}
```

## Categorical pipeline implementation

The categorical pipeline is now implemented in two parallel
implementations:

- **Python prototypes** (the canonical formalism,
 the canonical formalism,
 the canonical formalism) — design-spec
 reference, exact in $q$ via SymPy + cvxpy SDP feasibility for $H_3$.
- **Rust production scaling** ([`tools/hecke-engine/src/{gb_nf_reducer,joint_tower_sdp_certificate,wedderburn_psd,cross_level_embedding,sdp_verifier}.rs`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/src/),
 binary [`joint-tower-sdp`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/src/bin/joint_tower_sdp.rs)) — bit-for-bit
 match with Python on small cases; **3,400$\times$ speedup** (47.5 s $\to$ 14 ms
 for the 7-atom registry); scales to $H_5+$ where Python defers.
 See [RUST_INTEGRATION.md](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/tools/hecke-engine/RUST_INTEGRATION.md)
 for the implementation plan.

See [Table 2](#tbl:atom-knot-mass-derivation-table2-data).

### PSD-cone $\alpha^*$ ranking (Rust R5-minimal, $q_0 = 1.109978595554181\ldots$, 50 dps)

For each historical entry the verifier emits
$\alpha^*(\mathfrak{H}) := \max\{\alpha \in [0,1] :
\alpha \cdot \rho_\lambda(T_w) + (1-\alpha) \cdot I \succeq 0
\text{ for all } \lambda\}$. $\alpha^* = 1$ $\Rightarrow$ all blocks PSD;
$\alpha^* < 1$ quantifies the gap.

See [Table 3](#tbl:atom-knot-mass-derivation-table3-data).

Steps 5–8 currently substitute $\mathrm{Vol}_{\mathrm{hyp}}(K)$ from
SnapPy for $\mathrm{tr}_M(T_w)|_{q=q_0}$ on entries flagged
\texttt{manual-historical-volume-match} (${}^2$H, ${}^{3}$H, ${}^{3}$He) — i.e.\ the
post-Archimedean naming convention is used in place of the
pre-Archimedean Markov-trace evaluation. This is acceptable for
existing established knot identifications because the volume
conjecture commits both quantities to the same number, but the
*principled* path (Step 1a $\to$ Step 5) does not depend on this
substitution.

Running *backwards* from Step 6 to a candidate knot — a brute-force
volume-match search that bypasses Step 1a entirely — is forbidden by
this proposition: it reverse-engineers the knot from the AME target
rather than deriving it from the categorical pipeline.

## Location of the remaining gaps

After the pre-Archimedean / post-Archimedean simplification (Yekutieli
at finite slices replaces the geometric leg with finite-categorical
Markov-trace computation) and the production-scale Rust port
(R1–R4 + R5-minimal landed), the remaining open structural item is:

1. **Joint mass-tower confinement SDP — solver mode (R5-full).**
 The current Rust binary verifies that *given* candidate $T_w$
 inputs (electron $\sigma_1^3$, proton/neutron Borromean, ${}^2$H/${}^{3}$H/${}^{3}$He
 historical IDs) the certificate format is well-formed and quantifies
 the PSD-cone gap $\alpha^*$. The remaining work is to invert this:
 for ${}^{6}$Li ($H_{18}$), ${}^{7}$Li ($H_{21}$), and α-cluster atoms ($H_{24}$
 to $H_{120}$) where canonical $T_w$ is *unknown*, formulate and
 solve the SDP

 $$
   \min_{c_{w}(q_0) \in \mathbb{R}} \, \|\,c\,\|_1 \quad\text{s.t.}\quad
   \rho_\lambda(T_w) \succeq 0 \,\forall \lambda,\ \pi_{\mathfrak{H}\to\mathfrak{H}'}(T_w(\mathfrak{H})) = T_w(\mathfrak{H}')
   $$

 via Clarabel.rs + system BLAS. Slots into the existing
 `JointTowerSdpCertificate` schema. Once R5-full lands, the
 deprecated `li-atom-knot-search` is fully retirable.

 **Status ( issue #604 deliverable 1).** A first-pass
 Python R5-full prototype landed at
 the canonical formalism
 with witness
 [`r5-full-canonical-knot-solver.witness.json`](https://github.com/litlfred/qou/blob/main/computations/r5-full-canonical-knot-solver.witness.json).
 It enumerates $B_3$ braid words up to length $L_{\max} = 8$,
 filters via a KLR canonical-basis "cemetery" prune (drops $\sigma_i^{\pm k}$
 pure-power Demazure-trivial classes per AGENTS.md §7b symmetric-
 crystal guidance) plus a $\chi$-fingerprint dedup that collapses
 Markov-equivalent words to a single canonical-basis-class
 representative, and emits an operator-selection LP with strong-
 duality dual fields ($y_0^*$, $y_\lambda^*$, active set) per the
 AGENTS.md "LP / SDP duals — first-class infra" rule.

 The cemetery + dedup pass compresses the search space by **99 %**
 ($13088 \to 138$ canonical-basis classes at $L_{\max} = 8$). The
 historical canonical $T_w$ for ${}^{3}$He ($L_{6a4}$) is found to be
 **fully PSD-feasible** at $q_0$ ($\alpha^* = 0$) and ranks in the
 top 17 % of the 138 canonical-basis classes by single-term cost;
 ${}^2$H ($6_2$) is **not** PSD-feasible on its own ($\alpha^* = 0.89$
 on the standard $(2,1)$ block) and ranks in the top 45 %. The
 single-term shorthand $B = m_e \cdot \nu_{\mathrm{SDP}} \cdot \mathrm{tr}_M(T_w)$
 (retired — see Statement above) has the known structural offset documented in
 [`canonical evaluation-sdp-canonical-paper-formula.witness.json`](https://github.com/litlfred/qou/blob/main/computations/canonical evaluation-sdp-canonical-paper-formula.witness.json),
 which prevents the historical $T_w$ from being the unique global
 winner; wiring the multi-term tower (T2--T6 of
 [`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified))
 into the cost is the next-session deliverable. ${}^{3}$H ($8_{11}$ in
 $B_5$) is also next-session work — needs Hoefsmit seminormal at
 $H_5$, consistent with the deferred-to-Rust posture in
 the canonical formalism.

A second item — the structural prefactor rule $\nu_{\mathrm{SDP}}(Z, N)$ — is a
downstream consequence: once the SDP-solver returns canonical $T_w$
per atom, $\nu_{\mathrm{SDP}}$ is read off as the multiplicity of $T_w$'s solution
in the Wedderburn decomposition. No separate derivation is needed.

The geometric "leg" (Reeb density $\to$ Mostow $\to$ Gromov $\to$ Vol) and the
volume conjecture are *not* part of the QOU derivation. They appear
post-Archimedean as borrowed theorems that name the same number in
conventional 3-manifold-theory language.

## Refs

- Volume conjecture: Kashaev (1995), H.\ Murakami--J.\ Murakami (2001).
- Mostow rigidity: Mostow (1968), Prasad (1973).
- Gromov norm: Gromov (1982), Thurston (1979).
- Wenzl bridge $y_\lambda = s_{\lambda, r}(Q)/Z$: Wenzl (1988), Jones (1989).
- Iwahori--Hecke algebra + GB-NF: Kassel--Turaev (2008).
- Confinement SDP: [prop:confinement-sdp](#prop:confinement-sdp).
- AME 2020: Wang et al.\ (2021).
<!-- FILE_END: atom-knot-mass-derivation.md -->

