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
testable against a specific observable class. All three are now
settled on the **archimedean** side of the substrate wall — the
evaluation at $q_0$ — and all three remain open on the **fibre**,
where $q$ is a formal variable and $\mathrm{Im}(q)$ is
unconstrained. The conjecture is therefore restated as a
fibre-level question; the archimedean findings are recorded in
the section *Reality of $\mathfrak{Q}_\beta$ at the substrate*
below.*

## Exclusions for Im(q)

Per [Im(q) is not the EM / P_skew channel — distinct mechanisms](rem-im-q-vs-p-skew.md), Im(q) is **NOT**:
- The EM / $P_{\mathrm{skew}}$ channel (this is a real-q mechanism)
- A fourth calibration input (the 3-CAL count is cohomologically forced)
- An observable in the current framework (mass formula uses $|\cdot|$)
- Equal to $\mathrm{Im}(\mathrm{tr}_M(\rho(\beta)))$ — Im(q) is a parameter; Im(tr_M) is the value induced

## Reality of $\mathfrak{Q}_\beta$ at the substrate

The framework does possess an $\mathrm{Im}(q)$-sensitive observable, which
the opening paragraph's "not currently in the framework" did not anticipate:
the decay Q-value $\mathfrak{Q}_\beta$. Its closed form carries the modulus on
a single factor, so unlike the mass formula it does **not** project
$\mathrm{Im}(q)$ away. Since $\mathfrak{Q}_\beta$ is a measured Q-value it is
real, and $\mathrm{Im}\,\mathfrak{Q}_\beta = 0$ is one real equation on
$(\mathrm{Re}\,q, \mathrm{Im}\,q)$.

| candidate | conclusion at $q_0$ | scope | carrier |
|---|---|---|---|
| (i) chirality | the identification $\text{chirality} = (q \mapsto \bar q)$ holds exactly on $\lvert q\rvert = 1$; the substrate sits $18.83\,\%$ of $q_0$ away from it | (b) | `qou:QOU.QBeta.conj_eq_inv_iff_modulus_one` |
| (ii) phase dual to CAL-2 | $\mathrm{Im}\,q = 0$ on the whole admissible set | (b) | `qou:QOU.QBeta.im_qbeta_zero_iff_e2` |
| (iii) non-Hermitian | premise correct; **open**, but re-scoped — the framework *does* carry a categorical decay rate, and that rate is built entirely at real $q$ | (a) | `qou:QOU.QBeta.two_width_mechanisms_are_independent` |

For (i), the corpus's own chirality operation is the **bar involution**
$q \mapsto q^{-1}$ — the mirror knot, $J_{\bar K}(q) = J_K(q^{-1})$ — and
$\bar q = q^{-1}$ exactly when $\lvert q\rvert = 1$. At $q_0$ the mirror is
$q_0^{-1} \approx 0.9009182840$, a real number carrying no $\mathrm{Im}(q)$,
so the chirality content sought here is already present at real $q$ as the
$P_{\mathrm{skew}}$ part of the bar decomposition.

For (iii), a width obtained as $\mathfrak{D} = \hbar / \mathfrak{Q}$ with
$\mathfrak{Q}$ real is a different mechanism from a width obtained as
$-2\,\mathrm{Im}\,E$: on a real spectrum the second vanishes identically while
the first does not. That much is arithmetic and is scope (a), not (b).

What it does **not** establish is that the framework realises the first
mechanism. CAL-2 is named the neutron $\beta$-sector bar-skew channel $P_{\mathrm{skew}}^{\beta}$,
and the corpus relates it to the CAL-2 proxy by
$\mathfrak{Q}_\beta = P_{\mathrm{skew}}^{\beta}$; but a width and a lifetime are
reciprocal by definition, so if $P_{\mathrm{skew}}^{\beta}$ is the width then
$P_{\mathrm{skew}}^{\beta}$ is the neutron lifetime, $878.4\;\mathrm{s}$, and not
an energy. Defining $P_{\mathrm{skew}}^{\beta} := \hbar/\mathfrak{Q}_\beta$ instead is
dimensionally consistent but gives $8.40 \times 10^{-22}\;\mathrm{s}$, which is
$24.02$ orders of magnitude from that lifetime. Equivalently the neutron's
actual width $\Gamma_n = \hbar/\tau_n = 7.49 \times 10^{-19}\;\mathrm{eV}$ sits
$24.02$ orders below $\mathfrak{Q}_\beta$.

So $\mathfrak{Q}_\beta$ and $\Gamma_n$ are **independent** properties of one
decay rather than reciprocals: a $Q$-value is fixed by mass differences alone,
while a width additionally requires the coupling and the phase-space integral.
The framework reproduces the $Q$-value to $0.17\,\%$ — that result is untouched —
and $\Gamma_n$ is a width the reciprocal mechanism demonstrably fails to produce.

The coupling and the phase-space integral are, however, **supplied elsewhere in
the corpus**. The rate formula
of [hadron half-life](../predicted-spectra/hadron-half-life.md) is

$$
  \Gamma_\beta
  =
  \frac{\lvert\mathcal{W}(q)\rvert^2\,\mu_0}{2\pi^3}
   \cdot
  [2]_q
   \cdot
  \lvert\mathcal{M}_q\rvert^2
   \cdot
  f(Q),
  \qquad f(Q) \propto Q^5 ,
$$

whose coupling has a closed form — the canonical Markov trace of the $T_{3,5}$
braid word in $H_3(q)$, $\mathcal{W}(q) = q^2(q^{12}+q^8-1)/(q^2+1)^2$, with
$\mathcal{W}(1) = 1/4$. So the missing object is **not** the rate.

This re-scopes candidate (iii) rather than discharging it, and it re-scopes it
*against* the candidate. Every factor above is real for real $q$: a modulus
squared, $[2]_q = q + q^{-1}$, a trace ratio, and $Q^5$. The framework therefore
produces a decay width with **no $\mathrm{Im}\,q$ anywhere** — the same posture
the mass formula takes. What (iii) needs is not a width the framework lacks but
a reason a width should require $\mathrm{Im}\,q$ when the framework's own does
not. Scope (a): this says the corpus's construction needs no
$\mathrm{Im}\,q$, not that no construction does.

What the rate formula genuinely lacks is its **scale**, not its shape. The
weak-scale crossing count $N_v$ in $v = N_v\,\mathfrak{E}_\times\,\mu_0$ is
undetermined, so $G_F$ enters numerically from experiment;
[the Fermi-relation block](../predicted-spectra/hadron-half-life-fermi.md)
lists it as open computation 1. Since $m_e = 3\mathfrak{E}_\times\mu_0$, both
$\mathfrak{E}_\times$ and $\mu_0$ cancel and
$N_v = 3v/m_e = 1445519.51 \pm 0.37$ is $q$-independent — carrying no anchor and
no Markov-parameter convention.

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

**Testable (fibre)**. Scope (b) at $q_0$, by the section above. The
surviving question is whether $\arg q$ is a chirality coordinate on the
fibre, in the Kashaev regime $\lvert q\rvert = 1$ where $\bar q = q^{-1}$
and the two candidate operations coincide. There the identification is
correct, and the open part is whether a fibre-level chirality-sensitive
element has an archimedean image at all. Superseded archimedean form: does
the framework's prediction for an explicitly
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

**Testable (fibre)**. Scope (b) at $q_0$. This candidate
states its own closure condition — *"if only real solutions exist,
candidate (ii) is closed"* — and the second constraint it asks for is
$\mathrm{Im}\,\mathfrak{Q}_\beta = 0$, from the CAL-2 proxy itself. Under
both complex extensions the corpus supports, the zero set factors as
$y \cdot (\text{branch})$ with every branch empty on
$\mathrm{Re}\,q > 1/2$, and the Apollonius circle above lies entirely in
that half-plane: its centre is $1.0099145$ and its radius $0.1000641$, so
its leftmost point is $0.9098504$ — closed forms $1/(1-k^2)$, $k/(1-k^2)$ and
$1/(1+k)$ with $k^2 = \mathrm{Vol}(4_1)/(m_\mu/m_e)$, reproduced exactly; **no $q_0$ enters**: CAL-2 is the equation that
*defines* $q_0$, so neither the anchor question nor the CODATA vintage reaches
these three numbers. Only the two real intersections survive,
and the circle's arc coordinate is not a live degree of freedom. The
surviving question is the fibre one: whether $\mathrm{Im}(q)$ parametrises
anything at the level of the formal variable, where no reality condition
is imposed.

### Candidate (iii) — non-Hermitian deformation / open-system parameter

The Hoefsmit seminormal Hecke representation has real-coefficient
matrices for $q > 0$ real, giving **unitary** $H_n(q)$ representations.
For complex $q$ with $|q| \neq 1$, unitarity breaks: representations
become non-unitary; eigenvalues become complex. In quantum mechanics,
non-Hermitian operators arise in **open systems** (decay, dissipation,
resonance widths).

**Testable**. Open. The exhibit asked for — a $\Gamma$ the reciprocal
mechanism fails to produce — is the neutron's own, by $24.02$ orders of
magnitude (see the section above), so this candidate's obstacle is not
retired. Original form: do decay widths (Γ for unstable particles — W, Z,
top, resonances) correlate with the Im(q) needed to make Hecke
representations describe their non-Hermitian dynamics? Most decay
widths in the Standard Model have categorical interpretations open
in the QOU framework.

## Obstacles to a current proof

Each candidate was stated as requiring an observable the framework does not
yet provide. Two of those three requirements are met by observables already
present; the third is not.

- (i) asked for a chirality-sensitive observable. The corpus already carries a
  chirality operation — the bar involution $q \mapsto q^{-1}$, the mirror knot —
  and it acts at real $q$.
- (ii) asked for a second CAL-2-like constraint.
  $\mathrm{Im}\,\mathfrak{Q}_\beta = 0$ is one, supplied by the CAL-2 proxy
  itself.
- (iii) asked for a categorical formula for decay widths $\Gamma$. That
  requirement is **met**: [hadron half-life](../predicted-spectra/hadron-half-life.md)
  states one, with a closed-form coupling. What stands in (iii)'s way is the
  opposite of an absence — the corpus's rate is manifestly real at real $q$, so
  it exhibits a width needing no $\mathrm{Im}\,q$. Separately, the reciprocal
  mechanism $\Gamma = \hbar/\mathfrak{Q}_\beta$ misses $\Gamma_n$ by $24.02$
  orders of magnitude, and the rate's overall scale is imported pending the
  weak-scale crossing count $N_v$.

The framework's mass formula explicitly **projects away** Im(q)
content via $|\cdot|$, so no mass observable can detect Im(q)
directly. The candidate roles are all in **non-mass observables**.

## Connection to other conjectures

- [Canonical operator-level lepton-mass-tower formula](lepton-mass-tower-canonical.md) F_ℓ
  — the canonical lepton-mass formula is Im(q)-robust (modulus projection
  invariance); F_ℓ does NOT distinguish the three candidate Im(q) roles.
  Hence the F_ℓ conjecture is consistent with ALL three candidates.
- [Conjectural canonical form of the pair-gen piece $\rho_K^{\text{pair-gen}}$](../mass-endomorphism/conj-rho-k-pair-gen-canonical-form.md) —
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
  with real $q_0$ to the documented per-observable precision.
- **Structurally forced at the archimedean layer**, and no longer a
  convention. `qou:QOU.QBeta.im_qbeta_zero_iff_e2` derives
  $\mathrm{Im}(q_0) = 0$ from the reality of $\mathfrak{Q}_\beta$ on
  $\mathrm{Re}\,q > 1/2$, which contains the whole CAL-2 admissible set.
  The Im-sensitive measurement this clause was waiting for is
  $\mathfrak{Q}_\beta$ itself.
- **NOT forced on the fibre**: nothing in the framework's cohomological
  discipline requires $\mathrm{Im}(q) = 0$ for the formal variable, and the
  fibre-vs-observable separation makes that the layer where the three
  candidates remain live.

## Cross-references

- [The pre-Archimedean substrate is polymorphic in its base ring](q-zero-complex-extension.md) — substrate polymorphism
- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — involution split for complex q
- [Im(q) is not the EM / P_skew channel — distinct mechanisms](rem-im-q-vs-p-skew.md) — the distinction from P_skew
- [Categorical mass as Markov trace](../mass-endomorphism/categorical-mass-markov.md) — modulus projection

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
