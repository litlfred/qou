<!-- FILE_START: calibration-algebraic-mass-intro.md -->
The previous section produced a categorical mass functor that is dimensionless and unfixed in scale. We now anchor it to physical units. The three inputs align with the three Wedderburn channels of $H_3(R, q)$. The calibration is structural: each channel takes one anchor, forcing the rest of the formula. From the anchored mass we derive the algebraic mass formula, the Hoefsmit seminormal $R$-matrix, the Habiro brane tower, and the quantum-dilogarithm $\Phi_q$ that compiles the chapter's canonical witnesses.

The Normal form of the Hecke mass element conjecture identifies the canonical element whose Markov trace carries the mass. The Calibration inputs and predictive content remark establishes the no-fitting rule. The Exactly three calibration inputs proposition ($m_e$, $m_\mu/m_e$, $\mathfrak{Q}_\beta(n)$) proves that exactly three anchors are needed—one per Wedderburn channel. The Two-tier scaling $(p, q)$ remark and Three parameters aligned to Wedderburn channels proposition track how the channels carry the scaling. The Three-invariant atomic mass formula theorem establishes the algebraic mass formula, and the Derived-only mass formula proposition verifies it against the light isotopes.

The remainder of the section develops the seminormal and convergence machinery. The Hoefsmit seminormal matrices proposition supplies the explicit seminormal forms via the figure-eight branching rule. The convergence sequence runs through the Hecke convergence bound, the Markov-trace inductive limit, and the $\mathfrak{Q}_\beta$ categorical-derivation precision ladder. The Habiro ring, $\widehat{Z}$ ring, Algebraic quantum volume, Quantum dilogarithm stratified, and Q-Pochhammer partial product definitions establish the brane-tower layer. The realisation functor packages the bridge from the algebraic substrate to canonical evaluation.

The section closes with structural witnesses: depth-2 and depth-3 base-surface witnesses, Tate-rational and orbit-sum cyclotomic theorems, Baer-* and central-idempotent foundations of the Hecke algebra, and the bi-filtration grid mapping knot convolutions to the joint Galois/braid grading. The falsifiability targets and volume-injectivity probes restrict the base-surface embedding. The Quantum Bloch group and pentagon identity anchors the algebra in Bloch-group terms. The next section uses the three-input calibration and the quantum dilogarithm to ascend the confinement ladder.

**Calibration.**
The internal symmetry and the rigid topology of the state space leave
only a handful of free parameters: **exactly three** weak-sector
inputs fix the framework — a leptonic mass scale and two decay
widths, entering at successive orders $h^0$, $h^2$, $h^3$ — and they
are not chosen freely: they match, one for one, the three real
degrees of freedom of the state space's first cohomology.  The
leptonic mass scale ($m_e$) sets the unit, the *scale* of that
cohomology; the neutron $\beta$-decay width ($\mathfrak{D}_\beta$)
fixes the substrate parameter $q_0$, its *modulus*; and the pion
decay width ($\mathfrak{D}_\pi$) fixes the one remaining *orthogonal*
class, the meson sector whose Hopf-link complement has zero volume.
Each is read off its most precisely measured proxy — $m_e$, the
$Q$-value $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$, and the
pion mass $m_\pi$; the modulus is overdetermined, so it is pinned
numerically by the lepton ratio $m_\mu/m_e$ through the Skein
relation $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$.  Every other
mass, Q-value, binding energy, and coupling constant is a prediction.
<!-- FILE_END: calibration-algebraic-mass-intro.md -->

<!-- FILE_START: mass-element-nf.md -->
The Hecke mass element
$\Phi_{\mathrm{mass}}(\beta) \in H_3(R, q)$
([Hecke mass element](#def:hecke-mass-element)) has a
specific normal form structure determined by the **word
length filtration** on the NF basis.

## Statement

**Proposition (conditional on [`conj:mass-endomorphism`](#conj:mass-endomorphism)).**
*For any particle with braid representative $\beta$ in
$H_3(R, q)$, the Hecke mass element has the NF decomposition:*

$$
  \Phi_{\mathrm{mass}}(\beta)
  =
  a_1(\beta)\,(\sigma_0 + \sigma_1)
  +
  a_3(\beta)\,(L_+ + L_-)
  +
  a_5(\beta)\, e^-
$$

*with $a_0 = 0$ ($\gamma$ coefficient vanishes).  The
coefficients $a_1, a_3, a_5 > 0$ depend on the specific
particle through its brane tower weights.*

## Vanishing of $\gamma$ (photon masslessness)

The :refterm[descent]{#descent} involution $\hat\tau_n$ at the first brane level
projects onto the $H_1(q)$ content of $H_3(R, q)$.  Since
$H_1(q) = \mathrm{span}\{\gamma\}$ (the identity is the
only degree-0 element), the descended component at level
0 is $\gamma$.  The **transient** component at level 0
therefore has zero $\gamma$ coefficient — it lives in
$\ker(\hat\tau_0) = \mathrm{span}\{\sigma_0, \sigma_1, L_+, L_-, e^-\}$.

Since all brane levels $n \geq 1$ contribute to
$\ker(\hat\tau_{n-1})$, and the accumulated mass element is
the sum over all levels, the total $\Phi_{\mathrm{mass}}$
inherits $a_0 = 0$ from the first-level filtration.

This is the **NF statement that the photon is massless**:
the mass endomorphism has zero projection onto $\gamma$.

## Degree filtration and cycling

The NF basis has word lengths (degrees):

| Degree |    Basis elements    |      Tower levels     |
| :----: | :------------------: | :-------------------: |
|   $0$  |       $\gamma$       |   Descended (killed)  |
|   $1$  | $\sigma_0, \sigma_1$ | $n = 1, 4, 7, \ldots$ |
|   $2$  |      $L_+, L_-$      | $n = 2, 5, 8, \ldots$ |
|   $3$  |         $e^-$        | $n = 3, 6, 9, \ldots$ |

The :refterm[descent]{#descent} involution at level $n$ kills elements of degree
$\leq (n-1) \bmod 3$, so the transient contribution at level
$n$ lives in degree $(n \bmod 3)$ elements.  The tower cycles
through degrees $1 \to 2 \to 3 \to 1 \to 2 \to 3 \to \cdots$,
accumulating contributions to $\sigma_i$, then $L_\pm$, then
$e^-$, repeating.

## Explicit NF for the electron

For the electron (trefoil, $\mathrm{Li}_2(q^{-2})/\hbar_q^2$
mass formula), grouping the $\mathrm{Li}_2$ series by
$n \bmod 3$:

$$
  S_k = \sum_{\substack{n \geq 1 \\ n \equiv k \pmod{3}}}
  \frac{q^{-2n}}{n^2},
  \qquad k \in \{1, 2, 0\}
$$

gives:

|             Group             |    Contributes to    | Fraction of $\mathrm{Li}_2$ |   NF coefficient   |
| :---------------------------: | :------------------: | :-------------------------: | :----------------: |
| $S_1$ ($n = 1, 4, 7, \ldots$) | $\sigma_0, \sigma_1$ |           $76.9\%$          | $a_1 \approx 86.2$ |
| $S_2$ ($n = 2, 5, 8, \ldots$) |      $L_+, L_-$      |           $16.7\%$          | $a_3 \approx 37.4$ |
| $S_0$ ($n = 3, 6, 9, \ldots$) |         $e^-$        |           $6.4\%$           | $a_5 \approx 13.4$ |

The electron mass is mostly carried by the **crossing
channels** ($\sigma_0, \sigma_1$), not by the trefoil
channel itself.  The $e^-$ coefficient ($\approx 13.4$
including the descended part) is only $12\%$ of the total
mass element norm.

**Witness**: computed from $\mathrm{Li}_2(q^{-2})$ grouping
at $q_0 = 1.109978595554181\ldots$ (50 dps).
<!-- FILE_END: mass-element-nf.md -->

<!-- FILE_START: calibration-inputs.md -->
The QOU framework requires exactly three calibration inputs from experiment: the leptonic mass scale $m_e$ (CAL-1), the neutron $\beta$-decay width $\mathfrak{D}_\beta$ (CAL-2), and the pion decay width $\mathfrak{D}_\pi$ (CAL-3). Their numerical proxies are $m_e$, the ratio $m_\mu/m_e$ (which pins $q_0$), and $m_\pi$. These inputs match the three real degrees of freedom of the first cohomology $H^1(\mathrm{Bring}) = 2W$. All other masses, binding energies, Q-values, and coupling constants are predictions. $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$ serves as the CAL-2 proxy, validating the framework-derived hadronic energy scale $\mathfrak{E}_0$.

## The three inputs

| Input (proxy) | CAL | Canonical observable | What it fixes | Rel. precision |
|-------|:--:|-------|--------------|:-:|
| $m_e = 0.51099895000 \pm 0.00000000015$ MeV | CAL-1 | $m_e$ (leptonic mass scale) | the MeV unit + cohomological period | $2.9 \times 10^{-10}$ |
| $m_\mu / m_e = 206.7682830 \pm 0.0000045$ | CAL-2 | $\mathfrak{D}_\beta$ ($n$ $\beta$-decay width) | substrate $q_0$ ($W$-plane modulus) | $2.2 \times 10^{-8}$ |
| $m_\pi = 139.57039 \pm 0.00018$ MeV | CAL-3 | $\mathfrak{D}_\pi$ (pion decay width) | orthogonal meson scale ($\mathrm{Vol}(\mathrm{Hopf})=0$) | $1.3 \times 10^{-6}$ |

> **CAL-2 cross-check (not a separate input).** The free-neutron
> $\beta$-decay Q-value $\mathfrak{Q}_\beta(n) = \hbar/\mathfrak{D}_\beta
> = 0.78233341 \pm 0.00000061$ MeV is the **proxy for CAL-2**. The
> hadronic energy scale $\mathfrak{E}_0$ is framework-derived from
> $(m_e, q_0)$; $\mathfrak{Q}_\beta$ reproduced from $q_0$ then validates
> it to $0.17\%$ (subject to the net-ansatz caveat below). It is a
> cross-check, not a fourth calibration.

The first input is a **dimensionless ratio** — it fixes $q_0$
via the **leading-order substrate-truncation** of the canonical
operator-valued mass formula (see SUPERSEDED-$\rho_q$ note below):

$$
\frac{m_\mu}{m_e} \;\stackrel{\text{LO}}{=}\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
$$

([Skein mass relation](#rem:skein-mass-relation)), where
$\mathrm{Vol}(4_1) \approx 2.0299$ is the topological constant
(hyperbolic volume of the figure-eight knot) and
$\hbar_q = (q-1)/q$.  No units are involved.  The precision
is limited by the muon mass ($2.2 \times 10^{-8}$), not
the electron ($2.9 \times 10^{-10}$).

> **Substrate density refinement.**
> The dimensional factor $1/\hbar_q^2$ forms the leading-order scalar substrate density.
> The canonical operator-valued form replaces it with the
> Wedderburn-graded expansion. The Skein form closes $m_\mu/m_e = 206.77$ because it evaluates the Kashaev $q \to 1$ limit (the hyperbolic volume $\mathrm{Vol}(4_1)$), dressed by the scalar $1/\hbar_q^2$. The lepton-sector factor $\xi_\ell(q)$ that replaces $1/\hbar_q^2$ remains open.

The second input sets the **leptonic mass scale** — the
conversion from dimensionless natural units to MeV.  The
electron is the natural choice: it is the simplest charged
lepton, its mass is the most precisely measured particle mass
in the Standard Model, and its brane tower is fully computable
from $q_0$ alone:

$$
  m_e(\text{natural})
  =
  \frac{\mathrm{Li}_2(q^{-2})}{\hbar_q^2}
  \approx  112
$$

where $\mathrm{Li}_2(q^{-2}) = \sum_{n=1}^{\infty} q^{-2n}/n^2$
converges in $\sim 20$ terms.  The conversion factor is then
$m_e(\text{MeV}) / m_e(\text{natural}) \approx 4.57 \times 10^{-3}$ MeV.

**CAL-2 realization — the hadronic energy scale $\mathfrak{E}_0$ and
the $\mathfrak{Q}_\beta$ cross-check.** (CAL-3 proper is the meson scale
$m_\pi$; see below.) The leptonic inputs ($m_e$, $q_0$) give a
framework-derived hadronic scale in two forms — the single-Planck-tick value
$\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV
([energy scale](#rem:energy-scale-planck)) and the tower-summed
$\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2)
\approx 4.228$ MeV ([beta-decay energy scale](../particle-interactions/beta-decay-energy-scale.md)
§"tower-summed form"). The free neutron $\beta$-decay Q-value
calibrates $\mathfrak{E}_0$:

$$
  \mathfrak{E}_0^{(\text{cal})}
  =
  \frac{\mathfrak{Q}_\beta(n)}{|\Delta(\mathrm{net})|}
  =
  \frac{0.78233}{|h(h-2)/2|}
  \approx  4.179 \text{ MeV}
$$

(The typed-crossings 6-term decomposition yields $\lvert\Delta(\text{net,typed})\rvert \approx 0.18829$ and a slightly smaller $\mathfrak{E}_0 \approx 4.155$ MeV; the 0.6% gap is finite-size noise in the typed decomposition — see
[`beta-decay-energy-scale`](../particle-interactions/beta-decay-energy-scale.md) §"three values".)

where $\Delta(\mathrm{net}) = h(h-2)/2$ is the symbolic NF
difference between neutron and proton
([symbolic Q-value](#prop:neutron-qvalue-symbolic)).
The free neutron is the simplest hadronic decay — one
crossing change ($\mathfrak{d} \to \mathfrak{u}$) inside
one nucleon, no nuclear environment. Once $\mathfrak{E}_0$ is fixed,
**$\mathfrak{Q}_\beta$ cross-check gap.**
With the tower form $\mathfrak{E}_0^{\text{full}}$ active, the framework-derived value overshoots the calibrated value by $+1.75\%$. The geometric series direction does not close the $\mathfrak{Q}_\beta$ residual; it widens it. This leaves an explicit residual requiring categorical-derivation review.

**Fitting constraint.**
The relation $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$ constitutes an ansatz. The unweighted $\mathrm{net}$ sum differs structurally from the Markov-trace weighted sums of the mass tower. Until resolved by direct per-braid computation, the $\mathfrak{Q}_\beta$-from-$q_0$ reproduction remains an unclosed cross-check.

## Necessity of exactly three inputs

The physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$
([categorical action](#def:categorical-action)) lives in a
vector space of dimension $\dim \mathrm{End}(A) = (\dim A)^2$.
For $H_3(R, q)$ this is $6^2 = 36$ in principle.  The on-shell
constraint $\star_q F_\nabla = F_\nabla$
([instanton on-shell](#rem:instanton-on-shell)) and gauge
invariance $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([observability](#def:quantum-observable-universe)) eliminate
all but three real parameters:

1. **The deformation parameter $q$.**  This is the single
   continuous parameter of the Iwahori--Hecke algebra $H_n(R, q)$.
   It controls all dimensionless ratios: mass ratios, coupling
   constants, crossing asymmetries.  The observability condition
   forces $q \neq 1$ (otherwise $\mathrm{Ad}(A)$ has invariants),
   and the Descartes condition $\chi(A) = -6$ constrains $q$ to
   a one-parameter family, but does not fix a specific value.
   The value $q_0 \approx 1.110$ is fixed by one dimensionless
   measurement.

2. **The leptonic mass scale.**  The categorical mass
   $\mathfrak{m}(\varrho) = \mathrm{tr}_M(\rho(\beta))$
   ([categorical mass as Markov trace](#prop:categorical-mass-markov))
   is dimensionless (signed at the categorical level;
   the archimedean specialization at $q_0$ takes the positive
   observable value by Wenzl positivity for canonical $T_w$).  Converting to physical units (MeV)
   requires one mass measurement.  The electron mass sets this
   scale, analogous to the speed of light $c$ and Planck's
   constant $\hbar$ in the Standard Model.

3. **The orthogonal meson scale (CAL-3 = $\mathfrak{D}_\pi$, proxy
   $m_\pi$).**  The brane tower converts the single-level Hecke
   algebra to full particle masses, but the meson sector carries an
   orthogonal class ($\mathrm{Vol}(\mathrm{Hopf})=0$) genuinely
   independent of $(m_e, q_0)$ — the charged-pion mass $m_\pi$ fixes
   it (SDP-validated). The hadronic $\beta$-decay scale $\mathfrak{E}_0$
   is *derived* from $(m_e, q_0)$ and cross-checked by
   $\mathfrak{Q}_\beta$ (the CAL-2 proxy), so it is not the third
   independent input. The three inputs correspond to the three
   physical sectors: shape ($q$, via $\mathfrak{D}_\beta$/CAL-2),
   leptonic size ($m_e$/CAL-1), meson scale ($m_\pi$/CAL-3).

No further parameters exist because:
- The knot-particle dictionary is **determined by $\chi = -6$**:
  exactly 6 embeddable torus knots, no choice
  ([cohomological embedding](#prop:cohomological-embedding)).
- The crossing weights $q$ and $-q^{-1}$ are **eigenvalues of
  the $R$-matrix**, determined by $q$ alone.
- The typed crossing operators $C(f_i, f_j; \sigma_k)$ are
  **determined by the Hecke relation and quark flavors**, no
  free parameters
  ([typed crossing operator](#def:typed-crossing-operator)).
- The Markov trace $\mathrm{tr}_M$ is **unique** (up to the
  Markov parameter $z$, which is determined by $q$) by Schur
  orthogonality
  ([RJ canonical inner product](#prop:rj-canonical-inner-product)).

## Predictions from the three inputs

**From $q_0$ alone (dimensionless):**
- Lepton mass ratios: $m_\tau/m_e$, $m_\tau/m_\mu$
- Hecke amplitude: $h = q - q^{-1} \approx 0.209$
- Crossing asymmetry: $q/q^{-1} \approx 1.231$ (matter/antimatter)
- Neutron-proton splitting structure: $m_n - m_p \propto \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}$
- Pair production polarisation selection rule
- All NF decompositions and operator selection weights

**From $q_0$ + $m_e$ (in MeV):**
- Muon mass: $m_\mu = m_e \times \mathrm{Vol}(4_1)/\hbar_q^2$
  (first prediction, by construction matches calibration input)
- Proton mass: via Skein pair formula + dressed quark masses
  from Skein resolution tree (tractable computation)
- Neutron mass: $m_n = m_p + \mathfrak{Q}_\beta$ (Hecke engine)
- Deuteron binding energy: $\Delta E_D \approx 2.224$ MeV
- Beta decay Q-values: 6 benchmarks at 4.4% MAE
- Nuclear shell structure and magic numbers
- Half-life predictions

**Structurally predicted (verified against CODATA):**
- Neutron-proton splitting: $m_n - m_p$ from crossing pair
  isolation (categorical, no calibration beyond $q_0$)
- Q-value ratios: dimensionless, from $q_0$ alone
- Shell structure and magic numbers: from transfer matrix
  eigenvalues at $q_0$

**Open (concrete computation, not conceptual gap):**
- Dressed quark mass $\mu_\mathfrak{u}$ from $q_0$ alone:
  requires Skein resolution of Borromean braid ($\leq 729$ terms,
  each requiring a hyperbolic volume computation)
- Binding energy per nucleon $B/A$: same Skein resolution approach

## Comparison with the Standard Model

The Standard Model has **19 free parameters** (6 quark masses,
3 lepton masses, 3 CKM angles + 1 phase, 3 gauge couplings,
Higgs mass, Higgs VEV, QCD theta angle).  The QOU framework
replaces all 19 with **3** (one dimensionless ratio + two
mass/energy scales), deriving the rest from the topology of
the Bring surface $\Sigma_4$ and the Iwahori--Hecke algebra
$H_n(R, q)$.

The reduction from 19 to 3 is possible because:
- **Particle content** is topological (from $\chi = -6$), not a
  free choice
- **Mass ratios** are knot invariants (from Vol and $\mathrm{tr}_M$),
  not free parameters
- **Coupling constants** are $R$-matrix eigenvalues (from $q$),
  not independent inputs
- **Mixing angles** are Clebsch--Gordan coefficients of the knot
  eigenbasis decomposition
<!-- FILE_END: calibration-inputs.md -->

<!-- FILE_START: two-tier-scaling-pq.md -->
**Remark (two-tier scaling of the confined Laurent polynomial $P_K(q)$).**
*The map from a braid word to a physical mass passes through two logically separate scaling factors. We separate topological constants (intrinsic to the Hecke trace) from dimensional constants (set by the choice of physical anchor).*

## Tier 1: topological scaling — quantum dimension $[N]_q$

Before the Markov trace
([categorical mass as Markov trace](#prop:categorical-mass-markov))
qualifies as an isotopy invariant on the closure $\hat{\beta}$, the
raw graded Euler characteristic of the braid word must be normalised
so that an unbraided strand contributes a factor independent of the
ambient brane content. That normalising factor is the **quantum
dimension** of the fundamental fibre,

$$
  [N]_q
  \;=\;
  \frac{q^{N} - q^{-N}}{q - q^{-1}}.
$$

In Hecke language, $[N]_q$ is the Markov-trace normalisation that
ensures invariance under stabilisation $\beta \mapsto \beta\sigma_n^{\pm 1}$
([axiomatic Markov closed form](#prop:markov-trace-axiomatic-closed-form)).
Physically, it acts as a vacuum subtraction: $P_K(q)$ measures the
*excess* topological complexity of the knot $K$ relative to the
unbraided substrate, not the absolute count of strands. Without
this normalisation the polynomial would grow with every additional
trivial component, and Reidemeister-I invariance would fail
([Reidemeister mass invariance](#conj:reidemeister-mass-invariance)).

## Tier 2: physical scaling — base mass $m_0$

Evaluating the normalised $P_K(q)$ at the substrate parameter
$q_0 = 1.109978595554181\ldots$ (50 dps) produces a dimensionless real number; converting
to MeV requires multiplication by a base mass scale,

$$
  \mathfrak{m}_{\mathcal{K}} \;\approx\; m_0 \cdot \bigl| P_K(q_0) \bigr|.
$$

The choice of $m_0$ is a **boundary condition** of the framework, not
a derivation. Three natural anchors appear in the literature:

| Anchor | Value | Setting |
|--------|-------|---------|
| Leptonic mass | $m_e \approx 0.511\;\mathrm{MeV}$ | adopted by QOU as **CAL-1** ([calibration inputs](#rem:calibration-inputs)) |
| Higgs VEV | $v \approx 246\;\mathrm{GeV}$ | electroweak-localised models |
| Planck mass | $M_{\mathrm{Pl}} \approx 1.22 \times 10^{19}\;\mathrm{GeV}$ | spacetime-fabric models |

QOU selects $m_0 = m_e$ on empirical grounds: $m_e$ is the most
precisely measured particle mass in the Standard Model, and the
leptonic brane tower is fully computable from $q_0$ alone via
$m_e(\text{natural}) = \mathrm{Li}_2(q^{-2})/\hbar_q^2$
([three calibration inputs](#prop:three-calibration-inputs)). The
electroweak ($v$) and Planck ($M_{\mathrm{Pl}}$) choices correspond to
different fibre-functor normalisations and produce algebraically
equivalent predictions for dimensionless ratios such as
$m_\mu/m_e$ and $m_n - m_p$, but require independent calibration of
the leptonic sector to match observed masses.

## Significance of the separation

The two tiers commute with disjoint operations:

- $[N]_q$ acts **inside** the trace (Tier 1 is a categorical
  normalisation; it depends only on the rank $N$ of the fundamental
  fibre and on $q$).
- $m_0$ acts **outside** the trace (Tier 2 is a unit conversion; it
  has dimensions of mass and is independent of the braid word).

Mixing the two — for instance, by absorbing a power of $[N]_q$ into
$m_0$ — would make $m_0$ depend on the local Wedderburn channel and
break the parameter count of [three calibration inputs](#prop:three-calibration-inputs).
The volume-density factorisation
$\mathfrak{m}(K) = \mathrm{Vol}(K) \cdot \rho_q$
([Kashaev volume density](#rem:kashaev-volume-density)) inherits the
same separation: $\rho_q = 1/\hbar_q^2$ is Tier-1 (topological,
substrate-only), while the conversion of $\mathfrak{m}$ to MeV is
Tier-2 (physical, set by $m_e$).

## Summary

The substrate-bound polynomial $P_K(q)$ is a dimensionless
topological multiplier; its Markov normalisation by $[N]_q$ is fixed
by the categorical structure, while the conversion to a macroscopic
mass requires a separate dimensional anchor $m_0$ chosen by
calibration ([three calibration discipline](#prop:three-calibration-discipline)).
QOU pins $m_0 = m_e$; the Higgs-VEV and Planck-mass choices are
mathematically admissible alternatives that re-route the calibration
through the electroweak or gravitational sector respectively.
<!-- FILE_END: two-tier-scaling-pq.md -->

<!-- FILE_START: three-calibration-inputs.md -->
*The QOU framework admits exactly three external calibration inputs.
Beyond these three, no further empirical, fitting, or numerological
input is permitted — every other mass, Q-value, binding energy,
coupling constant, mixing angle, and dimensionless ratio in the paper
is a prediction.*

| ID | Canonical observable | canonical proxy | What it fixes | DOF of $H^1 = 2W$ |
|----|-----------|-------------|--------------|-------------------|
| **CAL-1** | $m_\mathfrak{e}$ (leptonic mass scale, order $h^0$) | electron mass (Penning trap) | the dimensional unit | $W$-plane scale |
| **CAL-2** | $\mathfrak{D}_\beta$ (neutron $\beta$-decay width, order $h^2$) | $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$; the modulus is overdetermined, pinned most precisely by $m_\mu/m_\mathfrak{e} = \mathrm{Vol}(4_1)/\hbar_q^2$, $\hbar_q = 1-q_0^{-1}$ | substrate $q_0$ | $W$-plane modulus |
| **CAL-3** | $\mathfrak{D}_\pi$ (pion decay width, order $h^3$) | charged-pion mass $m_\pi$ (PDG); independent of $(m_\mathfrak{e}, q_0)$ via $\mathrm{Vol}(\mathrm{Hopf})=0$ | meson scale | orthogonal class |

All three are the three real degrees of freedom of the single $H^1 = 2W$
(rank-2 $W$-plane scale + modulus, plus one orthogonal class: $2+1=3$),
**not** three distinct degrees $H^0/H^1/H^2$.

The three canonical inputs are **weak-sector observables** — a leptonic
mass scale and two decay widths $(m_\mathfrak{e}, \mathfrak{D}_\beta,
\mathfrak{D}_\pi)$, entering at successive orders $h^0, h^2, h^3$. They
are read off their most precisely measured **proxies** — the masses
$m_\mathfrak{e}$, $m_\pi$ and the $Q$-value $\mathfrak{Q}_\beta =
\hbar/\mathfrak{D}_\beta$. $m_\mathfrak{e}$ sets the unit, so the
(dimensionless) modulus $q_0$ is pinned by the ratio $m_\mu/m_\mathfrak{e}$
— the most precise anchor for CAL-2.

$\mathfrak{Q}_\beta$ is the **measured proxy for CAL-2** ($\mathfrak{D}_\beta$),
the bar-odd $\sinh$ partner of the bar-even $\cosh$ meson scale $m_\pi$;
it is **not** a fourth calibration. Because the modulus is overdetermined,
$\mathfrak{Q}_\beta$ and the lepton ratio $m_\mu/m_\mathfrak{e}$ are
alternative handles on the *same* CAL-2 — whichever is used to pin $q_0$,
the other becomes a cross-check prediction. In the
**Physical-Observations** layer $q_0$ may instead be anchored on the
more-precise proton ratio $m_p/m_\mathfrak{e}$ (the
muon ratio is then a $9.5\sigma$ cross-check), a precision substitution
within the same $H^1$ datum — not a fourth calibration.

*The three inputs are independent: one dimensionless ratio plus two
dimensional scales. They align to the three (co)homological degrees
of freedom that survive on-shell quotient by
$\star_q F_\nabla = F_\nabla$ and gauge invariance
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ —
namely the three Wedderburn blocks (sym, std, alt) of
$H_3(R, q)$ ([three parameters from Wedderburn](#prop:three-parameters-wedderburn)).*

## Statement

For every canonical observable $\mathcal{O}$ in the paper —
mass $\mathfrak{m}$, Q-value $\mathfrak{Q}_\beta$, binding $B(Z, N)$,
crossing energy $E_{\mathfrak{H}}$, coupling $\alpha$, mixing angle,
shell parameter — there exists a $\mathbb{Q}(q_0)$-element
$\hat{\mathcal{O}}(q_0) \in \mathbb{Z}[q_0^{\pm 1/2}]$ and integers
$a, b \in \mathbb{Z}$ with

$$
  \mathcal{O}
  \;=\;
  \hat{\mathcal{O}}(q_0)
  \cdot
  m_e^{\,a}
  \cdot
  m_\pi^{\,b}
$$

with $a + b \in \{0, 1\}$ (dimensionless, mass-scale, or energy-scale
output) and $q_0$ fixed by CAL-2 ($\mathfrak{D}_\beta$, pinned
canonical through its proxy $m_\mu/m_e$). The two dimensional
bridges to MeV are the proxy scales $m_e$ and $m_\pi$; the derived
hadronic energy scale $\mathfrak{E}_0 = m_e/(q_0(q_0-1))$ and the CAL-2
proxy $\mathfrak{Q}_\beta$ are $m_e^{1}\cdot\mathbb{Q}(q_0)$ expressions, not
independent factors.

## Allowed substitutions

- $q_0$ is a canonical constant *only* via CAL-2; downstream compute
  must carry $q_0$ symbolically as long as possible and substitute
  the CAL-2 exact algebraic values at the final reporting step
  ([symbolic-in-$q$ throughout](https://github.com/litlfred/qou/blob/main/docs/audits/-math-framework-workplan.md#p25)).
- $\mathfrak{E}_0$ has two framework-derived forms and one CODATA
  cross-check, all related by the brane-tower correction $1/(1-\hbar_q^2)$:
    - $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV
      (single Planck-tick, CAL-1 + CAL-2 only),
    - $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2) \approx 4.228$ MeV
      (tower-summed, CAL-1 + CAL-2 only),
    - $\mathfrak{E}_0^{(\text{cal})} = \mathfrak{Q}_\beta(n)/|\Delta(\mathrm{net})| \approx 4.155$ MeV
      (CAL-3 cross-check via CODATA).
  See the [notation register](../notation/notation-register.md) energy
  row and the [collisions note](../notation/notation-collisions.md)
  for the convention $\mathfrak{E}_0 \neq \mathfrak{Q}_\beta(n)$ (they differ by
  the dimensionless factor $1/|\Delta(\mathrm{net})| \approx 5.31$).
- $m_e$ enters as the unique dimensional bridge from $\mathbb{Q}(q_0)$
  to MeV.

## Forbidden substitutions

The framework forbids:

- *Free parameters* beyond CAL-1, CAL-2, CAL-3.
- *Coefficient fits* to AME, CODATA, PDG, or any external dataset
  (e.g. "ad hoc" or "approx" tags on Bethe-Weizsäcker coefficients
  must be derived to symbolic $\mathbb{Q}(q_0)$ form, not retained
  as fits).
- *Numerological substitutions* (e.g. magic numbers
  $\{2, 8, 20, 28, 50, 82, 126\}$ asserted as data; they must be
  derived from Bring's surface period structure or the BB / LR
  homological framework).
- *A second pinning of $q_0$*. The substrate uncertainty floor
  $\delta q_0$ propagated from CODATA $m_\mu/m_e$ is a CAL-2 cross-check;
  it may not be supplemented by independent fits to $m_e$, $m_\mu$,
  $m_\tau$, or any other mass.
- *A second hadronic scale*. $m_{\pi^{\pm}}$ is the CAL-3 proxy; the
  hadronic energy scale $\mathfrak{E}_0$ is derived from CAL-1 + CAL-2,
  and $\mathfrak{Q}_\beta(n)$ is the CAL-2 proxy — neither is an
  independent fourth input. Proton mass, neutron mass,
  and all nuclear binding energies must be derived from
  $\{m_e, q_0, m_{\pi^{\pm}}\}$, not introduced as inputs.

## (Co)homological alignment

The Wedderburn-Artin decomposition
$H_3(R, q) \cong M_1^{\mathrm{sym}} \oplus M_2^{\mathrm{std}} \oplus M_1^{\mathrm{alt}}$
gives three independent block characters $\chi_\lambda$ for
$\lambda \in \{(3), (2,1), (1^3)\}$, with degrees $1, 2, 1$. The
three on-shell parameters of the categorical action survive as the
three independent traces $\mathrm{tr}_\lambda$, one per block.

The calibration map is:

| Wedderburn block | Calibration | Role |
|------------------|-------------|------|
| $\mathrm{alt}$ ($\lambda = (1^3)$) | CAL-2: $\mathfrak{D}_\beta$ (proxy $m_\mu/m_e$) $\mapsto q_0$ | Sets the deformation scale (alt is the "antisymmetric" / antimatter channel; $q_0 = 1$ collapses it). |
| $\mathrm{std}$ ($\lambda = (2,1)$) | CAL-1: $m_e$ | Sets the leptonic mass quantum (std is the 2-dimensional "matter" channel where $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$). |
| $\mathrm{sym}$ ($\lambda = (3)$) | CAL-3: $\mathfrak{D}_\pi$ (proxy $m_{\pi^{\pm}}$) | Sets the chiral / Goldstone scale (sym is the "all crossings positive" / hadronic channel). The pion mass is the pseudo-Goldstone boson of broken chiral $\mathrm{SU}(2)_A$; its mass encodes the chiral condensate $\langle\bar{q}q\rangle^{1/3} \approx 240\;\mathrm{MeV}$ which is absent from $(m_e, q_0)$. $\mathfrak{Q}_\beta(n)$ is the **measured proxy for CAL-2** ($\mathfrak{D}_\beta$); when $q_0$ is pinned by the alternative anchor $m_\mu/m_e$, the relation $\mathfrak{Q}_\beta = m_e \lvert q_0^2 - 2q_0 - 1\rvert(q_0+1)/(2q_0^3) \approx 0.784\;\mathrm{MeV}$ (0.17% miss) makes it a cross-check on the same modulus, not a fourth input. |

This is the meaning of "aligned to (co)homology": the three
calibrations correspond bijectively to the three irreducible
characters of $H_3(R, q)$, which are the three cohomology classes
that survive the on-shell / gauge-invariance quotient. The
framework is rigid in this sense: increasing or decreasing the
number of calibrations would require deforming the categorical
substrate to a different on-shell quotient, which would no longer
satisfy the QOU axioms.

## Comparison with the Standard Model

The Standard Model has 19 free parameters (6 quark masses, 3 lepton
masses, 3 CKM angles + 1 phase, 3 gauge couplings, Higgs mass, Higgs
VEV, QCD theta angle). The QOU framework replaces all 19 with these
**3** ([calibration inputs context](#rem:calibration-inputs)):

- particle content is topological (from $\chi(A) = -6$), not chosen;
- mass ratios are knot invariants (from algebraic quantum volume and
  $\mathrm{tr}_M$), not free;
- coupling constants are $R$-matrix eigenvalues (from $q_0$);
- mixing angles are Clebsch-Gordan coefficients of the knot eigenbasis
  decomposition.

The 19 $\to$ 3 reduction forms a testable claim. Any prediction requiring a fourth calibration falsifies the framework.
<!-- FILE_END: three-calibration-inputs.md -->

<!-- FILE_START: three-parameters-wedderburn.md -->
The number of calibration inputs
([calibration inputs](#rem:calibration-inputs)) is not ad hoc:
it equals the number of **irreducible representations** of
$H_3(R, q)$, which is the number of partitions of $3$.

## Wedderburn-Artin decomposition

The Iwahori--Hecke algebra $H_3(R, q)$ is semisimple for generic
$q$ and decomposes via the Wedderburn theorem as:

$$
  H_3(R, q)
  \;\cong\;
  \underbrace{M_1(k)}_{\lambda = (3)}
  \;\oplus\;
  \underbrace{M_2(k)}_{\lambda = (2,1)}
  \;\oplus\;
  \underbrace{M_1(k)}_{\lambda = (1{,}1{,}1)}
$$

with dimensions $1^2 + 2^2 + 1^2 = 1 + 4 + 1 = 6 = \dim H_3(R, q)$.

Each simple component corresponds to an irreducible
representation labelled by a partition $\lambda \vdash 3$:

| Partition | Irrep | $\dim V_\lambda$ | Eigenvalue of $\sigma_i$ | Physical sector |
|:---:|:---:|:---:|:---:|:---|
| $(3)$ | Symmetric | $1$ | $+q$ | Shape (deformation) |
| $(2,1)$ | Standard | $2$ | $+q$ and $-q^{-1}$ mixed | Scale (mass ruler) |
| $(1{,}1{,}1)$ | Alternating | $1$ | $-q^{-1}$ | Interaction (hadronic) |

## On-shell projection

The physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$
([categorical action](#def:categorical-action)) decomposes
over the three irreps via the central idempotents $e_\lambda$:

$$
  \Phi
  =
  \alpha_1 \cdot e_{(3)}
  +
  \alpha_2 \cdot e_{(2,1)}
  +
  \alpha_3 \cdot e_{(1{,}1{,}1)}
$$

The on-shell condition $\star_q F = F$, observability
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, and gauge
invariance reduce each component to one real scalar:

| Component | Raw dim | $-$ Ad | $-$ $\star$ | $-$ gauge | Surviving |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $M_1$ (symmetric) | $1$ | $0$ | $0$ | $0$ | **$1$** |
| $M_2$ (standard) | $4$ | $1$ | $1$ | $1$ | **$1$** |
| $M_1$ (alternating) | $1$ | $0$ | $0$ | $0$ | **$1$** |
| **Total** | $6$ | | | | **$3$** |

Three irreps, three surviving parameters, three calibration
inputs.

## Physical identification

| Parameter | Irrep | Observable | What it fixes |
|:---:|:---:|:---:|:---|
| $\alpha_1$ | $(3)$ symmetric | $m_\mu/m_e$ | Substrate $q_0$ (all crossings $+q$) |
| $\alpha_2$ | $(2,1)$ standard | $m_e$ | Mass scale (mixed eigenvalues) |
| $\alpha_3$ | $(1{,}1{,}1)$ alternating | $\mathfrak{Q}_\beta(n)$ | Interaction scale (all crossings $-q^{-1}$) |

The symmetric sector sees only $+q$ eigenvalues — it controls
the **shape** of the universe (how far $q$ is from $1$).
The alternating sector sees only $-q^{-1}$ eigenvalues — it
controls the **interaction strength** (the antisymmetric
channel that drives beta decay).  The standard sector mixes
both eigenvalues — it controls the **mass scale** (the
conversion between Hecke algebra units and MeV).

## Sufficiency of three parameters for all $A$

Nuclear computations at Level 0 use $H_A(R, q)$ (one strand per
nucleon), which for $A > 3$ has more than three irreps.
However, the typed crossing operators
([typed crossing operator](#def:typed-crossing-operator))
$C(\mathfrak{p}, \mathfrak{p})$, $C(\mathfrak{p}, \mathfrak{n})$,
$C(\mathfrak{n}, \mathfrak{n})$ are determined entirely by the
three $H_3(R, q)$ parameters:

$$
  C(\mathfrak{p}, \mathfrak{p}) = \sigma \quad (d = 0),
  \qquad
  C(\mathfrak{n}, \mathfrak{n}) = \sigma - h \quad (d = -h),
  \qquad
  C(\mathfrak{p}, \mathfrak{n}) = \sigma - h/2 \quad (d = -h/2).
$$

These three crossing types span all possible nucleon-nucleon
interactions.  The coefficients $(0, -h, -h/2)$ are fixed by
$q$ alone (via $h = q - q^{-1}$), and the energy scale $E_0$
converts NF differences to MeV.  No additional parameters
appear at higher $A$ because the $H_A(R, q)$ computation
factorizes through these three crossing types.

## Cross-check: leptonic sector

For $H_2(R, q)$ (two strands, leptonic physics):
- Partitions of $2$: $(2)$ and $(1{,}1)$
- $H_2(R, q) \cong k \oplus k$, $\dim = 1^2 + 1^2 = 2$
- Two irreps $\to$ two parameters ($q_0$ and $m_e$)
- No standard representation $\to$ no interaction scale needed

Leptonic physics requires only two inputs. The third input ($\mathfrak{Q}_\beta$) is needed only when matter and antimatter crossings coexist within a composite (hadrons).
<!-- FILE_END: three-parameters-wedderburn.md -->

<!-- FILE_START: wedderburn-trace-identity.md -->
The Wedderburn trace identity records the normalization of the Markov
trace on the Wedderburn blocks of the Hecke algebra $H_n(R, q)$: the
total Markov weight is partitioned among the irreducible
representations with unit sum, providing the combinatorial foundation
for the :refterm[descent]{#descent} decomposition of mass and coupling.

**Proposition (Markov-trace normalization).**
*For the Hecke algebra $H_n(R, q)$ over a field $R$ with parameter
$q \neq 0$, the Markov-trace weights $y_\lambda(q)$ and the ordinary
block dimensions $d_\lambda = f^\lambda$ (the number of standard Young
tableaux of shape $\lambda$) satisfy*

$$
  \sum_{\lambda \vdash n} d_\lambda\, y_\lambda(q) = 1 .
$$

*Equivalently $\operatorname{tr}_M(\mathbf{1}) = \sum_\lambda y_\lambda\,\chi^\lambda(\mathbf{1}) = \sum_\lambda y_\lambda d_\lambda = 1$: the Markov trace of the identity is unit, so the weights $y_\lambda$ partition the total Markov weight among the irreducibles.*

**Consequence for mass.**

In the :refterm[descent]{#descent} decomposition of the mass
endomorphism ([BW as :refterm[descent]{#descent}](#prop:mass-categorical-descent)),
the Markov weight $y_\lambda$ of each partition $\lambda$ fixes that
block's contribution to the total binding energy; the unit-sum
normalization is what makes the descent a genuine *partition* of the
weight. The standard representation $[n{-}1, 1]$ carries the dominant
weight, which is why the volume term (sourced by the standard block)
leads the BW formula.

**Scale versus weight — two distinct $q$-objects.**

Two $q$-quantities enter the BW formula and must not be conflated:

- the **Hecke-level scale** $[n]_q! = [1]_q [2]_q \cdots [n]_q$ — for
  example the Wigner coefficient $\lambda_W = [5]_q!\, m_e$ at Hecke
  level $k = 5$ — evaluated directly as the $q$-factorial product;
- the **per-block weight ratio** $\tilde w_\lambda = \dim_q(\lambda)^2 / [n]_q!$,
  used in the LP-dual shadow prices, which coincides with the Markov
  weight $y_\lambda$ only on self-conjugate $\lambda$.

Neither is the bare sum $\sum_\lambda \dim_q(\lambda)^2$: that sum is a
separate $q$-polynomial — the global dimension of the block algebra —
and equals $[n]_q!$ only at $q = 1$.

**Classical limit.** At $q = 1$ the block dimensions satisfy the
Wedderburn–Artin count $\sum_\lambda d_\lambda^2 = n! = \dim H_n$ for
$\mathbb{C}[S_n]$, and dividing by $n!$ recovers the unit-sum
normalization above.
<!-- FILE_END: wedderburn-trace-identity.md -->

<!-- FILE_START: binding-scale-catalan.md -->
*The binding energy scale in the atomic mass formula is
the archimedean evaluation of the algebraic binding scale:*

$$
  \alpha_q = m_e \times \mathrm{Vol}_q(\mathcal{B}_3)
  \;\in\; \mathbb{Z}[q^{1/2}, q^{-1/2}]
$$

*where $\mathcal{B}_3 = \sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_2 \in B_4$
is the canonical Borromean braid word (closure: the Borromean rings
${6^3_2}$, three mutually unlinked yet inseparable components), and
$\mathrm{Vol}_q(\mathcal{B}_3) = \prod \hat{V}_i^{\mathcal{B}_3}(q)$
is its algebraic quantum volume
([algebraic quantum volume](#def:algebraic-quantum-volume)).
At $q = q_0$:*

$$
  \alpha = \lvert\alpha_{q_0}\rvert
         = m_e \times \mathrm{Vol}(\mathcal{B}_3)
         = m_e \times 8G
         \approx 3.7445 \;\mathrm{MeV}
$$

*where $G = \sum_{k=0}^{\infty} (-1)^k/(2k+1)^2 \approx 0.9160$
is Catalan's constant and
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ is the hyperbolic volume of
the Borromean rings complement.*
<!-- FILE_END: binding-scale-catalan.md -->

<!-- FILE_START: binding-error-amplification.md -->
*Write the binding energy as the mass defect*

$$
  B \;=\; M_{\mathrm{free}} - M_{\mathrm{atom}},
  \qquad
  M_{\mathrm{free}} = \textstyle\sum_i \mathfrak{m}(\text{constituent}_i),
$$

*the difference between the free-constituent mass and the bound-state mass,
with $0 < B \ll M_{\mathrm{atom}}$. If the predicted bound-state mass carries
relative error $\delta$,*

$$
  M_{\mathrm{atom}}^{\mathrm{pred}} = M_{\mathrm{atom}}\,(1+\delta),
$$

*and $M_{\mathrm{free}}$ is taken exact, then the predicted binding
$B^{\mathrm{pred}} = M_{\mathrm{free}} - M_{\mathrm{atom}}^{\mathrm{pred}}$ has
relative error*

$$
  \frac{B^{\mathrm{pred}} - B}{B}
  \;=\; -\,\delta \cdot \frac{M_{\mathrm{atom}}}{B}.
$$

*The error is amplified by the dimensionless factor
$\mathcal{A} = M_{\mathrm{atom}}/B$.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: binding-error-amplification.md -->

<!-- FILE_START: deuteron-fusion-frame.md -->
*Let $v = \sqrt{q_0}$ and write the symmetric $q$-integers
$[2]_v = v + v^{-1}$, $[3]_v = v^2 + 1 + v^{-2}$. The dimensionless content
of the deuteron binding magnitude is fixed by three exact identities:*

1. *(**fusion**) $[2]_v^2 = [3]_v + 1$ — the quantum-dimension form of the
   spin coupling $\tfrac12 \otimes \tfrac12 = 1 \oplus 0$;*
2. *(**the classical $5$**) $1 + [2]_v^2 = 5 + (v - v^{-1})^2$, so the total
   quantum dimension of the two-nucleon channel decomposition is $5$ at
   $v = 1$;*
3. *(**criticality**) for the exchange rate $g$ with
   $g^2 = z^2/(1 + z^2)$ and $z = [2]_v^{-1}$, one has
   $g^2\,(1 + [2]_v^2) = 1$: the bond magnitude sits exactly at the
   marginal-stability point $\det(1 + g\,M) = 0$.*

## Why the integer $5$ is not free

The bond factor $z = 1/[2]_v$ is the Ocneanu–Markov normalization of the
Hecke trace $\mathrm{tr}_M$ (the same $z$ that
[`prop:three-strand-color-winding-rigidity`](../braids-and-knots/three-strand-color-winding-rigidity.md)
and the reeb-flow magnitude use), not a modeling parameter. The quantity
$1 + [2]_v^2$ is the total quantum dimension of the two-nucleon channels
$\{V_0\ (\text{direct}),\ V_0 \oplus V_1\ (\text{fused})\}$; by the fusion
identity it equals $2 + [3]_v$, whose classical value is $5$. So the "5" in
the near-match law $B(^2\mathrm{H}) \approx 5g\,E_{\text{unit}}$ is a
counting datum — a total quantum dimension — not an adjustable integer.

## The exchange rate is a linking rate

The rate $g = z/\sqrt{1+z^2}$ is the linking number per unit arc length,
in exchange-cycle units, of a slope-$z$ geodesic pair on the shared torus
(the geometry-independent identity $|\mathrm{Lk}|\cdot 2\pi r / L = g$,
verified symbolically and by Gauss integration). Composing the two facts,
the deuteron magnitude reads *canonical Markov parameter $\to$ channel slope
$\to$ linking rate*: the counting weight (rigid) times the geometric rate
(deformed). Because the weight is topological, the trace-natural deformation
of the classical $5$ is $5g$ itself (the fully-deformed alternative
$(1 + [2]_v^2)\,g = 1/g$ splits from $5g$ by the exact factor
$1 + (v-v^{-1})^2/5$).

The Lean sibling proves the fusion identity, the classical-$5$ identity, the
geometry-independent linking-rate square, the criticality reciprocal, and
the $1/g$ deformation identity, all over a generic field. The archimedean
evaluation at $q_0$ and the MeV unit $E_{\text{unit}}$ are downstream and
remain the open inputs of the linear law.
<!-- FILE_END: deuteron-fusion-frame.md -->

<!-- FILE_START: frakD-energy-decomposition.md -->
*Let $\sigma$ be the bar involution (the substrate $q \mapsto q^{-1}$, an
order-2 ring endomorphism) on a field $F$ of characteristic $\neq 2$. Every
energy $E \in F$ splits canonically as*

$$
E \;=\; \underbrace{\tfrac{1}{2}(E + \sigma E)}_{\text{retained } (\cosh)}
\;+\; \underbrace{\tfrac{1}{2}(E - \sigma E)}_{\text{emitted } (\sinh)},
$$

*with the retained part bar-even ($\sigma$-fixed) and the emitted part
bar-odd ($\sigma$-negated). The emitted (bar-odd, $\sinh$) channel is the
decay-width $\mathfrak{D}$ sector; it vanishes iff $E$ is purely retained.*

## The $\mathfrak{D}$ reinterpretation of $E_{\text{unit}}$

This is the energy-level form of the complex-volume split
$\mathfrak{V} = \mathrm{Vol} + i\,\mathrm{CS}$: the retained part is the
binding-proper (cosh) channel, the emitted part is the radiated
$\gamma\bar\gamma$ / decay-width (sinh) channel. Reading the deuteron law
$B({}^2\mathrm{H}) = 5g \cdot E_{\text{unit}}$ through this split makes the
"$E_{\text{unit}} = \hbar/\mathfrak{D}$" reinterpretation precise: *if* the
unit is a decay-width energy (bar-odd), then it is its own emitted part with
zero retained part — a purely decay-channel energy
(`frakD_is_pure_emitted`). This keeps $E_{\text{unit}}$ inside the three
calibrations (the width $\mathfrak{D}$ is the CAL-2 datum), rather than a
fourth calibration.

The narrative caveat recorded in
[`docs/coordination/e-unit-deuteron-scale.md`](../../../docs/coordination/e-unit-deuteron-scale.md)
stands: whether the deuteron binding actually carries this bar-odd character
is empirically open (the landed §2h data weakly favour a bar-even unit). The
proposition formalizes the *decomposition itself*, which holds regardless;
the parity assignment of the physical $E_{\text{unit}}$ is the open input.

## Already tabulated

The mass-binding dashboard's **Entanglement** table computes this split for
every light nucleus — its `retained E` column is
$E_0 \cdot (\cosh\text{-channel})$ and its `emitted E` column is
$E_0 \cdot |\sinh\text{-channel}|$. The
`emitted/retained` ratio rises from $0.96$ at the deuteron — the least
saturated, most decay-like light binding, matching its $\beta$-threshold
character — toward $1.00$ by ${}^6\mathrm{Li}$. The Lean sibling
(`QOU.MassTheory.FrakD`) proves the projection is well-defined and
parity-correct over a generic field: `evenPart_barEven`, `oddPart_barOdd`,
`even_add_odd` (reconstruction), and `oddPart_eq_zero_iff_barEven` (a
nucleus carries no $\mathfrak{D}$ channel exactly when its binding is purely
retained).
<!-- FILE_END: frakD-energy-decomposition.md -->

<!-- FILE_START: wedderburn-mass-formula.md -->
*Let $(Z, N)$ be a neutral atom with atomic braid
$\mathcal{A} \in H_{A+Z}(q)$
([atomic braid](#def:atomic-braid)).
For each generator $i$ of the braid, let $M_i$ denote the
$2 \times 2$ transfer matrix obtained by chaining the crossing
matrices of all strands $j > i$.  Then the atomic mass is*

$$
  \mathcal{M}(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  + \alpha\bigl(
      \Phi_1
      - 2[3]_q \cdot \Phi_2
      + H_A^2 \cdot \Phi_3
    \bigr)
$$

*where:*

$$
  \Phi_1 = \sum_i \ln\bigl\lvert
    z \cdot (M_i)_{12} + (M_i)_{22}
  \bigr\rvert,
  \qquad
  \Phi_2 = \sum_i \ln\bigl\lvert
    \det M_i
  \bigr\rvert,
  \qquad
  \Phi_3 = \sum_i \ln\left\lvert
    \frac{\lambda_i^{\mathrm{sym}}}
         {\lambda_i^{\mathrm{alt}}}
  \right\rvert.
$$

*The three invariants correspond to the three Wedderburn blocks of
$H_n(R, q)$:*

| Invariant | Wedderburn block | Matrix quantity |
|:----------|:-----------------|:----------------|
| $\Phi_1$ | standard (dim $n{-}1$) | trace of Markov-weighted product |
| $\Phi_2$ | sym $\times$ alt | determinant (product of eigenvalues) |
| $\Phi_3$ | sym $/$ alt | ratio of eigenvalues (chirality) |

*The three invariants correspond to the three **extremal** Wedderburn
blocks of $H_n(R, q)$ (those associated with the symmetric, standard,
and alternating representations).  For $n \geq 4$, the Hecke algebra
has additional irreducible representations (one per partition of $n$),
producing additional invariants not captured by the $2 \times 2$
transfer matrix.  The partition-by-partition computation
(the formal derivation) computes all partitions exactly via
Young's seminormal form in polynomial time.  The mass functional
uses the three extremal invariants as the leading-order formula;
the full partition sum gives the exact Markov trace.*

*The coefficients are:*
- *$\alpha = m_e \times 8G$
  ([binding scale](#prop:binding-scale-catalan)),*
- *$[3]_q = (q^3 - q^{-3})/(q - q^{-1})$, the quantum 3-integer
  ([degree-2 weight](#prop:degree-two-baryon-weight)),*
- *$H_A = q - q^{-1}$, the Hecke parameter.*

*All quantities are derived from $q_0$ and $m_e$.  The formula has
zero fitted parameters.*
<!-- FILE_END: wedderburn-mass-formula.md -->

<!-- FILE_START: frobenius-s-classification.md -->
*Under the Frobenius--Hopf antipode $S \colon \sigma \leftrightarrow
\sigma^{-1}$ on the Hecke algebra $H_n(R, q)$, the three log-functionals
in the Wedderburn mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) carry
exactly the following $S$-eigenvalues:*

See [Table 1](#tbl:frobenius-s-classification-table1-data).

*Together with the $S$-classification of every coefficient in the
formula:*

See [Table 2](#tbl:frobenius-s-classification-table2-data).

*Term by term, the binding correction
$\alpha\bigl(\Phi_1 - 2[3]_q\,\Phi_2 + H_A^2\,\Phi_3\bigr)$
decomposes as:*

$$
\begin{aligned}
\text{Term 1: } & \underbrace{1}_{+1} \cdot \underbrace{\Phi_1}_{+1} = +1 & \text{($S$-even)} \\
\text{Term 2: } & \underbrace{-2[3]_q}_{+1} \cdot \underbrace{\Phi_2}_{+1} = +1 & \text{($S$-even)} \\
\text{Term 3: } & \underbrace{H_A^2}_{+1} \cdot \underbrace{\Phi_3}_{-1} = -1 & \text{($S$-odd)}
\end{aligned}
$$

*Exactly **one** of the three terms is $S$-anti-invariant, namely
the chirality term $H_A^2 \Phi_3$.  Consequently, any
$S$-symmetric ansatz for the binding correction (such as the
2-term $\alpha$-blend $\alpha V_{\mathrm{Frob}} + (1-\alpha) V_{\det}$)
necessarily lives in the 2-dimensional $S$-invariant subspace and
**cannot capture chirality** regardless of the mixing parameter.*
<!-- FILE_END: frobenius-s-classification.md -->

