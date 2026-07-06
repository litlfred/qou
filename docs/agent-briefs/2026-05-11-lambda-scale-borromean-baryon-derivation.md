# Agent brief: derive $\lambda_{\text{scale}}$ in the Borromean-baryon mass formula

**Fork point:** branch `claude/neutron-mass-50dps-chain` of
litlfred/qou at commit `cc780694` (PR #640).

Builds directly on PR #487 (`claude/knot-volumes-review-Pgt8o`,
merged 2026-04-29) which introduced the Borromean-baryon
interpretation but left $\lambda_{\text{scale}}$ undefined.

## Background — read these blocks first

1. [`topological-mass-trefoil.md`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-trefoil.md)
   — the canonical mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$
   for single-knot leptons. Confirmed: $\mathrm{Vol}(4_1)/\hbar_q^2 =
   :val[m_mu_over_e]{precision=6} = m_\mu/m_e$ (CAL-2 anchor, exact).
2. [`borromean-baryon-interpretation.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-interpretation.md)
   (introduced by PR #487) — the multi-component formula:
   $$
     \mathfrak{m}(B) \;=\; m_e \cdot \biggl[\,
       \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}\,\lambda_{\text{scale}}
       \;+\; S(B)
     \,\biggr]
   $$
3. [`skein-mass-from-linking.md`](../../content/quantum-observable-universe/braids-and-knots/skein-mass-from-linking.md)
   — the Skein-polynomial weighting for hadron mass:
   $\mathcal{M}(H) = Q(q) \cdot \mathcal{M}(\mathcal{L}_{\text{Hopf}})
   + \sum_i \mathrm{Vol}(K_i)/\hbar_q^2$.
4. [`docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md`](../../docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md)
   — the audit that motivated this brief.

## Empirical state (the numbers you'll need)

From [`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py)
(this brief's anchor script, 50-dps mpmath):

| Quantity | Value at $q_0$ | Status |
|----------|----------------|--------|
| $q_0$ | 1.10997859555... | CAL-2 (50 dps) |
| $\hbar_q^2 = ((q_0-1)/q_0)^2$ | 0.00981718851... | derived |
| $\mathrm{Vol}(4_1)$ | 2.02988321281... | topological constant |
| $\mathrm{Vol}(\mathcal{B}_3)$ | 7.32772475587... | topological constant |
| $\mathrm{Vol}(4_1)/\hbar_q^2$ | **206.7682830** | = CODATA $m_\mu/m_e$ exactly |
| $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ | **746.4179** | "Borromean common factor" |
| $\lambda_{\text{scale}}$ closure target (proton) | **2.4599527869** | OPEN — needs substrate derivation |
| $\lambda_{\text{scale}}$ closure target (neutron) | **2.4633436333** | OPEN |
| $\Delta\lambda(n-p)$ closure target | 0.00339085 | derivable (see below) |

### What's already substrate-derived

The **Skein-correction difference** between neutron and proton is
substrate-derivable from CAL-1 + CAL-2 + the topological constant
$\mathrm{Vol}(\mathcal{B}_3)$ — **no $m_p$ / $m_n$ input**:

$$
  \Delta S(n - p)
  \;=\;
  \frac{Q_\beta + m_e}{m_e} \cdot \frac{\hbar_q^2}{\mathrm{Vol}(\mathcal{B}_3)}
  \;\approx\; 0.003394
$$

where $Q_\beta$ comes from the framework's closed form
$Q_\beta = m_e \cdot |q_0^2 - 2q_0 - 1| (q_0+1) / (2 q_0^3)$
(`prop:neutron-qvalue-symbolic`, `derived_masses.q_beta_predicted_mev`).

Agreement with empirical target: **1015 ppm** (the same residual as
$Q_\beta$'s closed form vs CODATA, +0.17%). So $\Delta S$ is
already as accurate as the framework's best Q_β prediction.

### What's NOT substrate-derived

The **common Borromean scale** $\lambda_{\text{scale}}$ — declared
in `borromean-baryon-interpretation.md` but never defined. Empirical
target $\approx 2.460$ at $q_0$.

## Core directive: NO empirical / fitting / numerology

Every coefficient must be derived from QOU categorical structure.
No $\pi$, no transcendentals, no PSLQ-fitting that produces post-hoc
identifications. If you can't derive it from category, mark it open.
(Per `docs/agent-briefs/2026-05-03-e-hartree-categorical-derivation.md`.)

## Your task: derive $\lambda_{\text{scale}}$ from substrate

### Hypothesis space

$\lambda_{\text{scale}}$ should be a function of $q_0$, $\hbar_q$,
$[n]_q$ values, and possibly topological invariants of $\mathcal{B}_3$.
The closure target is **2.4599527869** at $q_0 = :val[q_0]{precision=6}...$.

Initial candidate sweep (from this branch's prior probe) — none
matched to better than 0.06%:

| Candidate at $q_0$ | Value | Match (target 2.460) |
|--------------------|-------|----------------------|
| $[2]_q$ | 2.011 | 18% off |
| $[5]_q / 2$ | 2.610 | 6% off |
| $[5]_q / [2]_q$ | 2.596 | 5.5% off |
| $q_0 + q_0^2$ | 2.342 | 4.8% off |
| $(1 + \hbar_q) \cdot [2]_q$ | 2.210 | 10% off |

### Promising structural directions to investigate

1. **Skein polynomial $Q(q_0)$ of $\mathcal{B}_3$.** Per
   `skein-mass-from-linking.md`, $\mathcal{M}(H) = Q(q) \cdot
   \mathcal{M}(\mathcal{L}_{\text{Hopf}}) + \sum \mathrm{Vol}/\hbar_q^2$.
   If $\lambda_{\text{scale}} = Q(q_0) \cdot \mathcal{M}(\mathcal{L}_H)
   / (\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2)$ for some substrate-defined
   $\mathcal{M}(\mathcal{L}_H)$, that's the path. Compute $Q(q_0)$ for
   $\mathcal{B}_3$ first.

2. **Graded Hecke energy at the Borromean braid.** Per
   `graded-hecke-energy-truncation-bound.md` and
   `graded-hecke-energy-probe.py`, the mass-spectrum generating
   function $P_K(q) = \sum_d c_d q^d$ is graded by GS-confinement
   filtration. For $\beta_{\text{Bor}} = (\sigma_1^{-1}\sigma_2)^3$
   in $B_3$: compute $P_{\mathcal{B}_3}(q_0)$ and check whether it
   equals $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2 \cdot \lambda_{\text{scale}}$.

3. **The $H_3$ Wedderburn structure on $\beta_{\text{Bor}}$.** The
   Borromean braid lives in $B_3 \subset H_3(q)$. Its Markov-trace
   image $|\mathrm{tr}_M((\sigma_1^{-1}\sigma_2)^3)|$ at $q_0$ —
   does it equal $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2 \cdot
   \lambda_{\text{scale}}$? If yes, $\lambda_{\text{scale}}$ is a
   ratio of two known substrate quantities. **Highest-leverage
   check** — it directly tests whether the two parallel formalisms
   (Markov-trace and Vol/ℏ_q²) agree on $\beta_{\text{Bor}}$.

4. **Cl_2(π/3) substructure.** $\mathrm{Vol}(\mathcal{B}_3) =
   8 \cdot \mathrm{Cl}_2(\pi/3)$. If $\lambda_{\text{scale}}$ involves
   the same Clausen-function value (with different prefactor), there
   may be a substrate-only identity hidden in the ratio
   $\mathrm{Vol}(\mathcal{B}_3) \cdot \lambda_{\text{scale}} / \mathrm{Vol}(\mathrm{something})$.

5. **The 11-crossing braids (canonical proton / neutron).** Per
   PR #612 (`atomic-braid-recipe-p`), the canonical proton braid has
   11 crossings, not the 6 of the simple Borromean $(\sigma_1^{-1}\sigma_2)^3$.
   Maybe $\lambda_{\text{scale}}$ corresponds to the additional
   structure of the 11-crossing canonical braid vs the bare Borromean.

### Falsifiability

A correct $\lambda_{\text{scale}}$ closure must satisfy three tests:

1. **Substrate-only** — uses only $m_e$, $q_0$, $\mathrm{Vol}(\mathcal{B}_3)$
   (or other named topological constants), and standard substrate algebra
   (no $\pi$ outside Clausen-function arguments, no PSLQ fits).
2. **Numerical match** — reproduces 2.4599527869 at $q_0 = :val[q_0]{precision=6}...$
   to at least 4 significant figures (0.01% level), preferably to the
   precision of the framework's $Q_\beta$ closed form (~0.17%).
3. **Universality at A=1** — the same $\lambda_{\text{scale}}$ must
   apply to *both* proton and neutron (with their differences coming
   only from the Skein orientation correction $S(p)$ vs $S(n)$).
   Currently $\lambda(p) = 2.4600$ and $\lambda(n) = 2.4633$; the
   substrate-derived $\lambda$ should be the common base, with
   $\lambda(n) - \lambda(p) = \Delta S(n-p) \approx 0.00339$ already
   matched by the Skein-difference formula above.

### Hint: where $\lambda$ might live structurally

The framework's other ratios at $q_0$ that are substrate-derived:
- $m_e/m_e = 1$ (definitional)
- $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2 \approx 206.77$ (CAL-2, exact)
- $Q_\beta/m_e \approx 1.532$ (from `q_beta_predicted.py`, +0.17%)
- $c_q = 1/(q_0-1) \approx 9.092$ (speed-of-light analog)
- $1/\hbar_q = q_0/(q_0-1) \approx 10.09$ (Planck-constant analog)

None of these matches 2.460 directly. The closure likely involves a
**non-trivial topological invariant of $\mathcal{B}_3$** — most plausibly the
Skein polynomial $Q(q_0)$ or a graded-Hecke-energy ratio. Start there.

## Concrete first-pass plan (if you pick this up)

1. Compute $Q(q_0)$ for the Borromean link via the canonical Skein
   reduction (or use the SnapPy / Jones-polynomial-of-link routines).
   Confirmed Borromean Jones: $V(\mathcal{B}_3) = -q^4 + 2q^2 - 3 + 2q^{-2} - q^{-4}$.
2. Compute $|\mathrm{tr}_M((\sigma_1^{-1}\sigma_2)^3, q_0)|$ via the
   existing Wenzl-bridge pipeline (`wedderburn_jones_markov.py`).
3. Compare the two against 2.4599527869 and the Borromean common
   factor 746.4179. Look for a closed-form identity.
4. If a match emerges to 4+ digits, write it up as a new content
   block `prop:lambda-scale-substrate-derivation.md` with the proof.
5. Update `derive_m_baryon_volume_form.py` to consume the substrate
   $\lambda_{\text{scale}}$, replacing the empirical-target value.
6. Cross-check: with substrate $\lambda_{\text{scale}}$, the
   topological mass formula should now reproduce $m_p/m_e$ to within
   the $Q_\beta$ residual (~0.17%), the same precision as $\Delta S$.

## Out of scope for this brief

- Closing the $Q_\beta$ residual itself (+0.17% / +1.31 keV). That's
  the `brane-tower-z-habiro` $n_\star$ truncation rule (separate open
  conjecture).
- A→ 1ppb on individual hadron masses requires *both* $\lambda_{\text{scale}}$
  closure (this brief) and $Q_\beta$ residual closure (separate).
- Heavier-atom binding (D, T, ³He, ⁴He) closure — the Vol-form here
  is for A=1 single-nucleon mass; composite binding lives in the
  ρ_K + Δ_λ pipeline ([`recomputed-low-isotope-mass-table.md`](../../content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md)).

## Cross-references

- PR #487 (`claude/knot-volumes-review-Pgt8o`) — introduced the
  Borromean-baryon block.
- PR #640 (this branch) — Vol-form chain + audit + this brief.
- [`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py)
  — the script you'd extend / consume from.
- [`docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md`](../audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md)
  — the analytical motivation.

## Questions for the previous PR #487 agent (if reachable)

1. What substrate quantity was $\lambda_{\text{scale}}$ supposed to derive from? (Skein? $\mathrm{tr}_M$? graded-Hecke ratio?)
2. Was an empirical $\lambda_{\text{scale}}$ ever computed in any witness on the PR #487 branch?
3. The PR table showed T1+T2+T3 algebraic Vol_q gave D binding to -5.5%. Did you check T1+T2+T3 against individual nucleon masses? Result?
4. $\beta_{\text{Bor}} = (\sigma_1^{-1}\sigma_2)^3$ (6 crossings) vs the canonical 11-crossing proton braid (PR #612) — are these Markov-equivalent? If yes, why does the canonical recipe have 11 crossings?

## Answers from PR #487 agent (2026-05-11)

The PR #487 agent replied with the following findings (paraphrased; ✓ direct, ◐ partial, ✗ unknown):

1. **λ_scale undefined in PR #487, no obvious substrate-only candidate matches 2.456** (✗). The agent tried $[2]_q \cdot q$, $[3]_q^2 / [2]_q^2$, $(q+1)$, and several other ratios — all 6–14% off. Closest match $q_0^{8.63} \approx 2.456$ has non-integer exponent (coincidence).

2. **No closed-form Skein correction for $(p, n) = (k, 3-k)$ in PR #487** (✗). The natural candidate is the HOMFLYPT polynomial of $\mathcal{B}_3$ evaluated with orientation $(k, 3-k)$, but this was never computed symbolically.

3. **T1+T2+T3 result on D** (✓): $\mathrm{Vol}_q^{\text{tower}}(D) = 3.827$ at $q_0$; T1+T2+T3 = 2.103 MeV vs AME 2.225 = −5.5%. T2+T3 in the agent's probe used **all per-generator volumes (intra + inter)**, not inter-only — different convention from Phase 2's "T2+T3 empty at A=1".

4. **τ_M / τ_SW relabelling status** (◐) — *critical finding for this branch*:
   - D was relabelled in PR #447 (`D-tr-M` is $\tau_{\mathrm{SW}}$; `D-tau-M` is canonical $\tau_M = 0.336821$).
   - **Proton and neutron registry files are still labelled "tr_M" but carry $\tau_{\mathrm{SW}}$ values** ($2.123$ for proton, $1.589$ for neutron).
   - Direct re-computation of the canonical $\tau_M$ on the free single-knot braid gives $|\tau_M(p_{\text{free}})| = 1.7339$, $|\tau_M(n_{\text{free}})| = 1.4060$.
   - The existing `atomic-tr-m-wenzl-bridge.witness.json` reports $0.998$ for **both** proton and neutron — flagged as a witness-generation bug.
   - **Consequence for this brief**: the `derivation_chain.TR_M_AT_Q0` table (with $p = 1.0653$, $n = 0.9232$, $D = 0.3883$) appears to be a **mixed-convention table**. The Frobenius non-degeneracy proof in commit `25a204efa` proves the canonical Frobenius pairing on $H_n(R, q)$ is $\tau_M$ (Jones-Markov), not $\tau_{\mathrm{SW}}$.

5. **Vol/ℏ_q² vs ρ_K · m_e · |tr_M| identification** (◐): the two formalisms can only coincide if $\rho_K$ varies per knot — i.e. there is **no substrate-only identity** $\mathrm{Vol}(K) / \hbar_q^2 = \rho_K \cdot |\tau_M(K)|$ in $\{m_e, q_0\}$ alone. The two pipelines compute different invariants.

6. **The 6-crossing $\beta_{\text{Bor}}$ and the 11-crossing canonical proton braid are NOT Markov-equivalent** (◐) — they have different component counts (3-link vs 1-knot). They are **alternative ansätze**, not different presentations of the same word. The atomic-braid-recipe registry uses the 11-crossing word as canonical for the $\tau_M$-based mass formula; the Borromean baryon is a separate, Vol-based formalism.

7. **T5 quarantine consistent** (✓) — T5 dominates negatively (−5.63 MeV for D), flipping the naive 6-term sum, hence the sign-indefinite quarantine.

8. **Best leads for $\lambda_{\text{scale}}$ derivation** (✗ open):
   - **Most actionable**: compute $J_{\mathcal{B}_3}(q_0; \text{orientation} = (2, 1))$ and $J_{\mathcal{B}_3}(q_0; (1, 2))$ symbolically. If the ratio matches $m_p / m_n$, the Skein term is pinned and $\lambda_{\text{scale}}$ is constrained residually.
   - **Calibration route** (least theoretically satisfying): $\lambda_{\text{scale}} = m_e \cdot \rho_p \cdot |\tau_M(p_{\text{free}})| / (\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2)$ — one equation in one unknown, but $\rho_p$ then becomes a free parameter per knot.
   - The 2.46 may be a **representation-translation factor** between the Vol-based (3-link Borromean) and $\tau_M$-based (1-knot 11-crossing) formalisms, not a substrate quantity in either.

## Implications for the Borromean-baryon programme

The Vol-form derivation in this branch
([`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py))
sits in the **Borromean / Vol-based** formalism. Under PR #487 agent
finding #6, this formalism's "proton" and "neutron" predictions
correspond to **different braid representatives** than the canonical
11-crossing $\tau_M$-based pipeline.

The two formalisms must agree on observable mass values
($m_p = :val[m_p_MeV]{precision=6}\;\text{MeV}$ regardless of which braid you use to
compute it) — but $\lambda_{\text{scale}}$ in the Vol formalism may
NOT have a substrate derivation independent of the bridging map to
the $\tau_M$ formalism.

**Three diagnostic computations** would settle this:

(a) Verify the PR #487 agent's direct $|\tau_M(p_{\text{free}})| = 1.7339$ against the canonical Wenzl-bridge / `from_scratch/` pipeline.

(b) Compute $J_{\mathcal{B}_3}(q_0; \text{orientation} = (2, 1))$ vs $J_{\mathcal{B}_3}(q_0; (1, 2))$ at 50 dps.

(c) Test whether $\lambda_{\text{scale}} = m_e \cdot |\tau_M(p_{\text{free}})| \cdot \rho_p / (\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2)$ with $\rho_p$ from
[`rho-k-graded-expansion.md`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md).

Until (a)–(c) close, the
[`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)
should be read as: *the Vol-based mass formula for the
Borromean baryon ansatz, with $\lambda_{\text{scale}}$ as the
representation-translation factor to the canonical $\tau_M$-based
mass formula on the 11-crossing braid (not a free parameter, but
not yet derived in $\{m_e, q_0\}$ either).*
5. Is there a direct identity $|\mathrm{tr}_M(\beta_{\text{Bor}}, q_0)| = \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2 \cdot \lambda_{\text{scale}}$, or are these distinct dimensionless masses that the framework expects to coincide via a $\rho_K$ correction?
