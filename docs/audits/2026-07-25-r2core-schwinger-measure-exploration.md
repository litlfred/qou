# R2-core Schwinger proper-time measure — exploration: what would derive the unit, where the ½ lives, and the Haar-forcing question

**Date:** 2026-07-25 · **Bean:** qou-lecl · **Axis:** α_EM per-loop measure (R2-core) ·
**Tier:** **EXPLORATION** — scope-(a), audit-only, NO FIT, nothing wired.
**Discipline:** the owner ruling stands throughout
([`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)):
R2 is **not** Lean/derived-proved; $1/(8\pi)$ stays a phase-4 identification.
Nothing in this document proves R2; it maps the candidate space, runs the cheap
exact falsifiers, and locates the residue.

**Probe:** [`computations/probes/r2core_schwinger_measure_explore_probe.py`](../../computations/probes/r2core_schwinger_measure_explore_probe.py)
→ [`r2core-schwinger-measure-explore.witness.json`](../../computations/probes/r2core-schwinger-measure-explore.witness.json)
— 10/10 assertions, exit 0 (sympy exact + mpmath 50 dps; audit-only).

**Follows:** the merged Quillen attack
([`2026-07-25-alpha-em-r2-quillen-curvature-attack.md`](2026-07-25-alpha-em-r2-quillen-curvature-attack.md),
`309729f5`), whose mismatch finding — *R2-core's object is a Schwinger
proper-time measure normalization, not a determinant-line quantity* — is this
tranche's starting point.

## 0. Owner premises (recorded verbatim; tiered)

Two owner statements arrived during this tranche (2026-07-25). Both are
**owner-supplied framework premises** — not derived, not proved; every
conclusion conditional on them is labelled so.

> **P1 (scale-freedom):** *"'substrate has a preferred scale q₀' is FALSE — q₀
> is just our LOCAL value. The substrate itself is scale-free; q₀ is the
> locally realized value of the modulus, not a structural scale of the
> substrate."*

> **P2 (computational time):** *"proper-time is really only computational
> time."*

P1 **inverts** the tension this exploration was originally posed with (Task 3
asked whether the substrate's q₀ scale kills the continuum Haar convention).
Under P1 the resolution runs the other way: substrate scale-freedom is exactly
the hypothesis under which the multiplicative Haar measure is *forced* as the
unique scale-invariant choice, and q₀-dependence enters only through
observables evaluated at the local value — never through the measure unit
(§4). P2 gives the Schwinger parameter an ontology — the substrate's
computation-step count — which demotes the discrete candidates from *rivals*
to *charts* of the same object (§4.2).

## 1. The exact question (Task 1)

The $dt/t$ measure whose unit is open lives in **one** corpus integral: the
ζ-regularized 1-loop photon determinant on the Bring Jacobian,

$$
\log \det{}'\Delta \;=\; -\int_0^\infty \frac{ds}{s}\,
\Bigl[\mathrm{Tr}\, e^{-s\Delta} - \dim\ker\Delta\Bigr],
$$

whose small-$s$ heat coefficient supplies the derived unit
$a_0 = (4\pi s)^{-d/2}\big|_{d=2} = 1/(4\pi)$ (#3909), entering the α_EM tower
as the one-loop insertion weight $\tfrac12\,a_0\,\alpha$ in the derived Habiro
element $[2]_q(1-h^2\alpha)$ (#1511). The provable shell is already Lean-locked
([`SchwingerMeasureShape.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SchwingerMeasureShape.lean)):
the **shape** $c\cdot ds/s$ is the unique scale-invariant density
(`scale_invariant_density_unique`); one e-fold carries measure exactly $c$
(`one_nat_per_efold`); the $s \sim E^{-2}$ Jacobian makes one energy e-fold two
proper-time e-folds (`efold_jacobian_two`); $c = 1$ with the ½ split lands on
$1/(8\pi)$ (`unit_total_gives_eighth`). **Open:** the unit $c = 1$ (R2-core's
"one nat per proper-time e-fold") and the ½-adjudication (which e-fold variable
the convention counts — the ρ-split vs E-Jacobian readings, mutually exclusive,
each alone giving $1/(8\pi)$, both together the excluded $1/(16\pi)$).

## 2. The candidate table (Task 1–2: identity + falsifier + result)

Each candidate is stated as a checkable identity for the unit (or the ½), with
its falsifier and the probe's result. "KILLED" is scope-(a): the stated
candidate identity only.

| # | Candidate | Candidate identity (precise) | Falsifier | Result |
|---|---|---|---|---|
| (a) | **Continuum Haar / nat** | $c = 1$ nat per proper-time e-fold ($k_B = 1$, `boltzmann-constant`) | must be pin-invariant and rational (R2c squeeze: coefficient $= \text{rational}\cdot a_0$) | **survives**; shape forced under P1 (§4.1); unit $c=1$ conditionally forced by (d′) (§5); otherwise stays the convention the ruling names |
| (b) | **q-rung step unit** | one count per rung $t \in \{t_0\, q_0^n\}$: $c_{\mathrm{eff}} = u/\ln q_0$ for an intrinsic per-step weight $u$ | $\ln q_0$ is *local data* (P1/P2): it must cancel in dimensionless outputs; any residual is pin-dependent and non-rational | **KILLED** for every intrinsic $u \in \{1,\ \eta_q,\ \hbar_q,\ \mathfrak{B}\}$: pin-relative shifts $1.1\times10^{-7}$, $1.2\times10^{-7}$, $5.7\times10^{-9}$, $3.5\times10^{-7}$ — all $>10^{-10}$, vs the exactly pin-invariant derived rationals. Unique pin-stable choice: $u = \ln q_0$, i.e. the step's own e-fold width — **Haar restated in the chart** (the cancellation happens only tautologically) |
| (b′) | **Bar-pair ½** (doubled pair $(q, q^{-1})$ ↔ $(t, 1/t)$) | the loop counts the bar-doubled domain with $c = 1$; the physical channel is the bar quotient: for bar-even $f$ ($f(t) = f(1/t)$), $\int_0^\infty f\,\tfrac{dt}{t} = 2\int_1^\infty f\,\tfrac{dt}{t}$ — per channel exactly $\tfrac12\, a_0$ | (i) the ½ appears **only in bar-even channels** — a bar-odd integrand gets $0$, never ½; (ii) must not stack with the E-Jacobian ½ (else $1/(16\pi)$, excluded); (iii) the raw heat trace must support the symmetrization | fold identity **exact** (bar-even ½ ✓, bar-odd $0$ ✓, $<10^{-25}$); **but** the raw trace is *not* bar-even: $\Theta_{\mathbb{Z}^8}(1/s) = s^4\,\Theta_{\mathbb{Z}^8}(s)$ (weight-4 Poisson reflection, verified $<10^{-25}$; $\lvert\Theta(1/s)-\Theta(s)\rvert > 0.1$) — the ½'s bar-even home is **per-channel, post-split**, not the trace. Survives as the sharpest ½ candidate; consistent with $[2]_q$ (bar-even) carrying the insertion. Not derived |
| (c) | **Reeb-period unit** (Seifert $S^1$; `discrete-planck-step`: one Reeb circuit = one time unit, $t_P = q_0/(q_0-1) \approx 10.08$) | $c$ set by the Reeb period as the time unit | none needed: $\int_{a/T}^{b/T} dt/t = \int_a^b dt/t$ **exactly** for any linear unit $T$ | **cannot carry $c$** — a linear time unit is invisible to the multiplicative measure (symbolically exact). Demoted to a chart choice; moreover the two step charts disagree away from $q=1$: $\ln q - \hbar_q = (q-1)^2/2 + O((q-1)^3)$ exact, ratio $\approx 1.053$ at $q_0$ — "one per step" is chart-dependent |
| (d) | **Tower level as discrete time** (one unit per Markov-trace / jet level $n$) | the level index is the proper-time variable | if level = time with unit measure per level, ladder weights would carry $\Gamma(k)$-type moment factors absent from #1511's exact binomial coefficients | object-level mismatch in the *naive* form (the tower level indexes loops / jet order, not intra-loop time) — but the Borel-dual refinement (d′) has real content: |
| (d′) | **Level ↔ proper time via Borel/Laplace** | the forced KeystoneBridgeC1Binding normalizer is the unit-Schwinger moment: $N(n) = (n-1)! = \int_0^\infty s^{n}\,e^{-s}\,\tfrac{ds}{s}$ | with measure $c\cdot ds/s$ the moments are $c\,(n-1)!$; the **proved** bridge identity $n\cdot N(n) = n!$ then forces $c = 1$ exactly; $c = \tfrac12$ gives $n!/2 \ne n!$ | moment identity **exact** (n = 1..6); distinguisher **exact**. **Conditional** on the unproved identification *binding Borel variable = loop proper time* (the keystone's geometric leg, `conj:qdifference-kernel-prolongation-symbol`). See §5 |

**No-4th-calibration prune (applied across the table, per the owner steer §6):**
any resolution of the ½ (or of $c$) that requires a **data-pinned constant**
would be a hidden CAL-4 and is discipline-excluded outright. Every candidate
above is built from framework structure only (bar involution, rung lattice,
Reeb period, proved normalizer); none reads data; all add **zero** calibration
DOF.

## 3. Exact check results (the probe, 10/10)

| Block | Check | Result |
|---|---|---|
| B1 | linear-unit invisibility $\int_{a/T}^{b/T} dt/t = \int_a^b dt/t$ | exact (sympy) — kills (c) as unit carrier |
| B2 | bar-even fold $= \tfrac12$; bar-odd channel $= 0$ (test integrands $e^{-(t+1/t)}$, $(t-1/t)e^{-(t+1/t)}$) | $<10^{-25}$ both — the (b′) falsifier is sharp: ½ only in bar-even channels |
| B3 | $\Theta_{\mathbb{Z}^8}(1/s) = s^4 \Theta_{\mathbb{Z}^8}(s)$ at $s = 0.7, 1.37$; not bar-even | $<10^{-25}$ / $>0.1$ — naive trace-level symmetrization fails |
| B4 | rung measure $\int_{q^n}^{q^{n+1}} dt/t = \ln q$ exact; intrinsic per-step units pin-dependent; $c_{\text{pair}}/c_{\text{rung}} = \tfrac12$ scale-free | exact / all four killed / exact — the ½ is *not* a q-discretization artifact (it is $q_0$-independent even in the chart) |
| B5 | $N(n) = (n-1)! = $ unit-Schwinger moment; $c=\tfrac12$ breaks $n\cdot N(n) = n!$ | exact (n = 1..6) — conditional $c = 1$ forcing + reading distinguisher |
| B6 | $\ln q - \hbar_q = (q-1)^2/2 + O((q-1)^3)$ | exact — step charts agree only classically |

Recorded, not scored: $\eta_q/\ln q_0 \approx 8.5496$ is **not** $b_1 = 8$
(6.9 % off) — pre-empting a numerological re-pitch.

## 4. The Haar-forcing question (Task 3, reworked under P1/P2)

### 4.1 The forcing argument, stated precisely (conditional on P1)

**GIVEN P1** (the substrate is scale-free; $q_0$ is local data, not a
structural scale): the loop's proper-time half-line carries the substrate's
multiplicative scale action with no distinguished point; the measure must be
invariant under it; by the Lean-proved shape rigidity
(`scale_invariant_density_unique`) the *only* such density is $c \cdot ds/s$ —
Haar on $(\mathbb{R}_{>0}, \times)$, unique up to the single constant $c$. So
under P1 the **shape is forced**, and the entire open content of R2-core is
squeezed into the residual constant — which is exactly where the
½-adjudication lives, now sharply isolated: $c_{\text{total}} = 1$ with a
channel ½ (ρ-split reading), or $c_s = \tfrac12$ from counting energy e-folds
(E-Jacobian reading). The original dichotomy ("does q₀ kill the continuum
convention?") is dissolved: there is no structural scale to kill it, and
q₀-dependence may enter observables but **not** the unit.

### 4.2 The computational-time consequences (conditional on P2)

**GIVEN P2**, the Schwinger parameter's ontology is the substrate's
computation-step count; the discrete structures — the q-rung ladder, the Reeb
circuit, the tower level — are **charts** of the same object, and the
continuum $dt/t$ is its archimedean coarse-graining. The sharp consistency
requirement (owner: "identify where a step-count unit vs nat unit would
differ, and verify the difference cancels") resolves as a **finding**:

- In the local chart, one step spans $\ln q_0$ of log-time, so "one unit per
  step" means $c_{\mathrm{eff}} = u/\ln q_0$ for the step's intrinsic weight
  $u$. The probe shows every candidate intrinsic weight the corpus offers —
  $1$ nat, the per-crossing entropy $\eta_q = (2q-1)/q^3$
  (`fibre-channel-capacity`), the Reeb angle $\hbar_q = 1 - 1/q$, the
  Bremermann bandwidth $\mathfrak{B} = q\,\eta_q/(q-1)^2$
  (`information-bandwidth`) — leaves a **pin-dependent, non-rational residue**
  in the per-loop coefficient (shifts $10^{-9}$–$10^{-7}$ between the muon and
  proton q₀ pins), contradicting the exactly pin-invariant derived skeleton
  (#1511 rational coefficients; the R2c $\text{rational}\cdot a_0$ squeeze).
- The **cancellation therefore does not happen for any intrinsic per-step
  unit**: it happens **only** for the tautological weight $u = \ln q_0$ — each
  step weighted by its own e-fold width — which is the Haar/nat unit restated
  in the chart. Under P2 this is the precise sense in which "one nat per
  e-fold" is the unique chart-free coarse-graining of step counting: the
  conversion $\ln q_0$ (local data, per P1) cancels *iff* the measure is Haar.
- The information-theoretic reading of the unit ("literally one nat of entropy
  per computation step", third consequence of P2): **no corpus object ties the
  Schwinger measure to an entropy count directly.** The nearest objects are
  the capacity *bound* $\eta_q$ per crossing and the bandwidth *ceiling*
  $\mathfrak{B}$ per Planck time — both bounds, not measures, and both
  excluded as measure units by the pin falsifier above. What survives is the
  weaker, correct statement already Lean-locked: with $k_B = 1$ the measure's
  scalar *is denominated in* nats per e-fold (`one_nat_per_efold`); whether
  each computation step *carries* that nat is exactly R2-core, still open.
- Under this reading the ½ candidate (b′) acquires the stateable form: *one
  step's unit splits $\tfrac12 + \tfrac12$ between the bar-sides $q$ and
  $q^{-1}$ of the doubled pair.* Its falsifier stands (½ only in bar-even
  channels; bar-odd gets 0; no stacking with the E-Jacobian ½), and B4's
  exact $c_{\text{pair}}/c_{\text{rung}} = \tfrac12$ shows the split is
  scale-free — independent of the local $\ln q_0$ — as a channel/pair fact
  must be. **Stated, not asserted.**

**Net (owner-premise-conditional):** GIVEN P1 + P2, the measure unit is forced
to the chart-free Haar/nat normalization up to the single constant $c$, the
residual ½ is located in the doubled-pair channel split (bar-even home), and
the checkable distinguishers are B2 (bar-parity), B4 (pin-stability), B5
(the keystone moment, §5). Nothing here is unconditional; P1/P2 are owner
premises and the ruling stands.

## 5. The one genuinely new lead: the keystone moment forces $c = 1$ (conditional)

The binding sector independently **forces** a normalizer with no scalar
freedom: [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean)
proves $n \cdot N(n) = n!$, i.e. $N(n) = (n-1)!$, as the unique strip making
the binding OGF the C1 carrier
([`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md)).
The probe's B5 records the exact identity

$$
N(n) \;=\; (n-1)! \;=\; \int_0^\infty s^{\,n}\, e^{-s}\, \frac{ds}{s},
$$

— the forced normalizer **is** the $n$-th moment of the *unit-normalized*
($c = 1$) Schwinger measure. If the binding Borel variable and the loop proper
time are the same substrate object (under P2 both are "computational time"; this
identification is the keystone's **unproved geometric leg**,
`conj:qdifference-kernel-prolongation-symbol`), then:

1. a unit $c \ne 1$ would rescale every moment to $c\,(n-1)!$ and **break the
   proved identity** $n \cdot N(n) = n!$ — so $c = 1$ is forced;
2. the ½-adjudication **tips toward the ρ-split reading** ($c_s = 1$ total,
   ½ in the channel split) and against the E-Jacobian reading
   ($c_s = \tfrac12$ on the proper-time side), by the exact distinguisher
   $n!/2 \ne n!$.

**Honest status:** this is a *cross-sector consistency*, not a derivation. The
identification it needs is of the same species as R2 itself (a dictionary
premise), and it is explicitly unproved. What it adds is falsifiable
structure: two sectors (α_EM loop measure; binding q-Borel) would share **one**
unit, and the binding side's is Lean-forced. A future derivation of the
identification would close R2-core's unit; a refutation of it removes this
lead — either is progress. Recorded as the exploration's sharpest forward
pointer.

## 6. Relation to the ideal CAL triple — verdict: **NOT related, beyond two bookkeeping hooks**

Per the owner steer ("not sure if we need to relate here or not"), checked
against [`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md),
`epistemic-status-of-calibrations`, and the AGENTS.md CAL table
(CAL-1 $= m_e$, $h^0$ scale; CAL-2 $= \mathfrak{D}_\beta$, $h^2$ modulus;
CAL-3 $= \mathfrak{D}_\pi$, $h^3$ orthogonal class $=$ the 3 real DOF of
$H^1(\mathrm{Bring}) = 2W$):

1. **No-4th-calibration check (the real hook).** The Schwinger unit, if pinned
   from data, would be a hidden CAL-4 — forbidden by the three-calibration
   discipline. The owner-premise-forced Haar unit adds **zero** calibration
   DOF (the 3-CAL $=$ 3 $H^1$-DOF count is unchanged), so the derivation
   *satisfies* the discipline; conversely the discipline **prunes** the
   candidate space: any ½ resolution requiring a data-pinned constant is
   excluded up front. Applied to the table in §2 (all candidates pass — none
   reads data).
2. **Dimensional anchoring — orthogonal by construction.** CAL-1 sets the
   dimensional unit and CAL-2/CAL-3 are inverse times (widths
   $\mathfrak{D}$; $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$), so the
   dimensionful anchor of any proper/computational time is CAL-borne. But the
   measure $ds/s$ is **dimensionless and scale-invariant** — B1's exact
   linear-unit invisibility is precisely the statement that the CAL
   dimensional anchor can never reach the unit $c$. The measure question is
   purely the residual dimensionless normalization (the ½), exactly as the R2
   decomposition assumed. No formula mixing found.
3. **Grading crosswalk (recorded, not interpreted).** The bar involution that
   splits the ½ candidate's channels is the same involution under which the
   CAL-2 proxy $\mathfrak{Q}_\beta$ is the bar-odd ($\sinh$) partner of the
   bar-even ($\cosh$) CAL-3 proxy $m_\pi$
   (`three-calibration-discipline` §table). The α_EM ½ sits on the bar-even
   side (the $[2]_q$ insertion is bar-even), the CAL $h^2$/$h^3$ split uses
   the same parity vocabulary — but no exact statement tying the ½ to a CAL
   grading emerged. Observation only.

**Verdict: no relation** beyond (1) the discipline prune (a constraint, which
the exploration satisfies) and (2) dimensional bookkeeping (which the
scale-invariant measure provably cannot see).

## 7. Honest gap list

1. **R2-core itself stays open.** The unit $c = 1$ is forced only conditional
   on owner premises P1/P2 (shape + chart-freedom) or on the unproved
   Borel-variable identification (§5). Unconditionally it remains the
   convention the 2026-07-19 ruling names.
2. **The ½-adjudication stays open.** (b′) is the sharpest candidate and §5
   conditionally disfavors the E-Jacobian rival, but neither is derived; the
   readings remain observationally indistinguishable at this order.
3. **The (b′) trace-level obstruction.** B3 shows the raw heat trace reflects
   with weight 4, so the bar-symmetrization ½ must act per-channel after the
   Hodge/channel split — the per-channel statement is exactly the B2
   τ-identification front (sibling cluster), not closed here.
4. **The §5 identification** (binding Borel variable $=$ loop proper time) is
   unproved and currently unformalized; formalize-first next step would be a
   conditional Lean class naming it, before any further numerics.
5. **The W8 constraint respected, not resolved.** The τ-dictionary
   (modulus-level $q \leftrightarrow \tau$) FAILs its hauptmodul gate
   ([`2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md`](2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md));
   nothing here re-opens it. The measure question uses only $\ln t \propto \pm \ln q$
   chart facts (rung widths, bar flip $t \mapsto 1/t$), never a modular
   dictionary — the MEASURE question is disjoint from the killed MODULUS
   dictionary, as scoped in the tasking.
6. **P1/P2 are premises.** If the owner later withdraws or refines them, §4's
   forcing collapses back to the pre-existing state (shape rigid, unit open).

## 8. Scope discipline (anti-laundering)

- **NO FIT.** No candidate was adjusted toward $1/(8\pi)$; every check is an
  exact identity or a pre-stated-tolerance comparison; no CODATA read (the two
  q₀ pin strings are used only to *demonstrate pin-dependence*, i.e. to kill
  candidates, never to select a value).
- **Scope-(a) throughout.** Each KILLED row refutes its stated candidate
  identity only. B1's invisibility and B4's pair-ratio are exact symbolic
  facts; the pin-dependence kills cite the derived pin-invariant skeleton.
- **Conditional results labelled.** §4 conclusions are owner-premise-
  conditional; §5 is conditional on a named unproved identification; neither
  upgrades any tier. Nothing wires; $1/(8\pi)$ stays phase-4; no `instance`,
  no dashboard, no content block touched.
- **Exploration tier stated in the banner**, per the tasking.
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list-hijack lines inside
  display math; no inline align-family environments). The pipeline render was
  not run in this sandbox — stated explicitly per the render-QA gate: this
  change was **not machine-validated**.

## 9. Cross-references

- Owner ruling (read-first): [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)
- R2 decomposition / R2-core / the Lean shell: [`2026-07-19-alpha-em-r2-decomposition.md`](2026-07-19-alpha-em-r2-decomposition.md), [`2026-07-19-alpha-em-r2core-schwinger.md`](2026-07-19-alpha-em-r2core-schwinger.md), [`SchwingerMeasureShape.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SchwingerMeasureShape.lean)
- The ½ wall: [`2026-07-18-alpha-em-reciprocal-form-consolidation.md`](2026-07-18-alpha-em-reciprocal-form-consolidation.md) (#3925); π-origin: [`2026-07-18-alpha-em-pi-origin-adjudication.md`](2026-07-18-alpha-em-pi-origin-adjudication.md) (#3909); consolidated status: [`2026-07-18-alpha-em-perloop-measure-status-consolidation.md`](2026-07-18-alpha-em-perloop-measure-status-consolidation.md)
- The Quillen mismatch finding this executes on: [`2026-07-25-alpha-em-r2-quillen-curvature-attack.md`](2026-07-25-alpha-em-r2-quillen-curvature-attack.md)
- Bar vs channel-swap involutions: `2026-07-18-alpha-em-channel-swap-involution.md` (#3936); τ-correspondence obstruction: `2026-07-18-alpha-em-tau-correspondence.md`
- Corpus proper-time structures: [`discrete-planck-step.md`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md), [`fibre-channel-capacity.md`](../../content/quantum-observable-universe/information-theory/fibre-channel-capacity.md), [`information-bandwidth.md`](../../content/quantum-observable-universe/information-theory/information-bandwidth.md), [`horizon-conformal-invariance.md`](../../content/quantum-observable-universe/information-theory/horizon-conformal-invariance.md), [`q-gaussian-solves-q-heat.md`](../../content/quantum-observable-universe/information-theory/q-gaussian-solves-q-heat.md)
- Keystone normalizer: [`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md), [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean)
- τ-dictionary W8 gate (kill respected): [`2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md`](2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md), [`2026-07-24-tau-dictionary-fricke-cusp-spin.md`](2026-07-24-tau-dictionary-fricke-cusp-spin.md)
- CAL triple: [`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
