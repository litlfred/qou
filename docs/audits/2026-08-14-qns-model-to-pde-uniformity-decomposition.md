# q-NS model-to-PDE uniformity — decomposition of the surviving lock caveat (bean `qou-ohaz`)

**Date:** 2026-08-14 · **Branch:** `claude/q-ns-classical-gaps-9l9mj9` ·
**Bean:** `qou-ohaz` (opened this session; the surviving lock-uniformity
caveat after the Γ-growth escape closed in PR #5019) · **Epic context:**
the q-NS surreal-bridge campaign
([ledger](2026-07-25-qns-surreal-bridge-campaign-ledger.md)).
**Scope (a) throughout: statements are about the two-regime pair-collision
model and named exact NS ingredients — never the general classical problem.**

## 0. TL;DR

The question "does the NS/q-NS PDE dynamics actually follow the two-regime
ODE model through the pair approach?" decomposes into four named
sub-items (U1–U4). Two now carry theorem-grade robustness results — the
race outcome does not depend on the model's least-grounded ingredients —
and two are genuinely open PDE items. New this session:
**the viscous core-growth race** (`pair_viscous_core_race.lean`,
sorry-free): the Lamb–Oseen core-variance law `a²(t) = a₀² + 4νt` — an
*exact* NS solution — against the phase-1 approach `d²(t) = d₀² − (Γ/π)t`
is a linear–linear race whose crossing

$$
t_{\mathrm{ov}} = \frac{d_0^2 - a_0^2}{\Gamma/\pi + 4\nu}
$$

is strictly positive, strictly before the inviscid collision time
`t* = πd₀²/Γ`, at strictly positive separation
(`d²(t_ov) = (4νd₀² + (Γ/π)a₀²)/(Γ/π + 4ν)`), for **every** `ν > 0` —
with *zero* strain-driven core growth assumed. The overlap cutoff's
engagement is therefore doubly robust: it survives removing the model's
strain-driven `V₁` equation (this file) and it survives arbitrary
circulation growth `Γ(t)` (`overlap_at_small_separation`, PR #5019).

## 1. The decomposition

| # | Sub-item | Status | Evidence |
|---|---|---|---|
| U1 | **Approach law** `(d²)' = −Γ/π` (mutual advection) | exact for straight anti-parallel filaments / 2D point vortices; the standard Biot–Savart reduction | `rem:townsend-biot-savart-strain`; owner-proved `kappa_squared_tends_to_zero` (sub-leading strain correction `V₂/V₁ → 0` on approach) |
| U2 | **Core evolution** | *strain-driven* `V₁' = αV₁` is modeling; but the race outcome no longer depends on it: the **viscous channel** `a² = a₀² + 4νt` (Lamb–Oseen, exact NS) alone forces overlap before collision — `viscous_race_won`, sorry-free | `pair_viscous_core_race.lean` (this session); localization hypothesis named (per-core Lamb–Oseen during approach — same locality class as U1) |
| U3 | **3D effects absent from the model** — Crow instability, axial core flow, curvature | **OPEN** — the genuine PDE content of `qou-ohaz`. Note the sign of the known physics: the Crow instability drives anti-parallel pairs toward *reconnection* (topology change), which is regularizing-like, not blow-up-like; but no in-corpus formalization exists and this observation is not evidence | bean `qou-ohaz` (remains open on exactly this) |
| U4 | **Phase-2 saturation law** `α = Γ/(πV₁)` | anchored on the Burgers-vortex strain balance (Burgers vortex is also an exact NS solution); the *engagement* of phase 2 is what U2 now guarantees; the saturation *value* remains modeling | `rem:hyperbolic-overlap-saturation`; Levi lock `κ² = πν/Γ` |

## 2. What is proved vs what is modeling (honesty ledger)

**Theorem-grade (sorry-free, generic ordered field):**
phase-1 closed form is a uniform Riccati flow with exact invariant `d²Ω`
(`pair_phase1_riccati.lean`); the pair channel satisfies the GP5
`riccati_lower_growth` hypothesis with uniform `c′ = Γ/(πd₀²Ω₀)` during
approach (`discrete_riccati_lower`); the overlap race is `Γ(t)`-free
(`overlap_at_small_separation`); the viscous race is won before collision
for every `ν > 0` (`viscous_race_won`).

**Exact-NS ingredients consumed (not modeled):** Lamb–Oseen core
spreading (U2), Burgers vortex strain balance (U4 anchor), Biot–Savart
law for straight filaments (U1).

**Modeling steps, named:** per-core localization during approach (U1/U2 —
the ODE reduction itself); the phase-2 saturation *value* (U4); everything
2D/straight-filament (U3 excluded by construction).

**Open (the bean):** U3 — whether 3D effects preserve or break the
two-regime reduction. This is the honest research frontier; nothing in
this session's results touches it.

## 3. In-model picture after this session

Every route to pair-channel blow-up inside the two-regime model is now
closed by theorem: the approach's self-amplification is real
(`Om_hits_every_level` — phase 1 alone passes every finite level) but the
overlap cutoff *always* engages first, robustly to circulation growth and
robustly to the choice of core-growth channel, and once engaged the
saturation regularizes (`overlap_race_strict`, PC-arc). The pair channel
realises the internal singularity at fixed `q ≠ 1` (Levi lock positive)
and regularises in the classical limit — the per-channel branch-B reading
of `conj:levi-degeneracy` now rests on four theorems and two exact NS
ingredients rather than on probe numerics.

**Blow-up in-model therefore still localises to** channels the model does
not cover: sustained forcing (SF-arc conclusion) and 3D pair effects (U3).

## 4. Next honest steps (in priority order)

> **🛑 CURRENCY, 2026-09-03 — items 1 and 2 below are DONE; this list is
> kept for the record, not as a work plan.** Both closed on 2026-08-14,
> the same day this audit was written, which is why the list never got
> updated. Item 1 (U3) is bean `qou-7fi2`, **completed** — the Crow
> dispersion relation landed as `crow-approach-amplification` plus
> `computations/qns_crow_efolds_probe.py`, with the bounded power law
> `A = (d₀²/V_{1,0})^{s*/3}`. Item 2 (U4) is bean `qou-zuz0`,
> **completed** — `burgers_core_strain_cap.lean` derives the cap
> `Γ/(4πa²)` from the Gaussian profile, sorry-free.
>
> So **all four of U1–U4 now carry results**, and `qou-ohaz`'s *remaining*
> content is not any of them: it is the bean's headline goal, a controlled
> reduction of the two-regime ODE from the Biot–Savart PDE **with error
> bounds** (or the PDE effect that breaks it). U1–U4 constrain that
> reduction from four directions; none of them is it. Item 3 below is
> untouched and is still the millennium core.

1. **U3 formalization target:** state the Crow-instability dispersion
   relation as a content block with a probe (the growth rate is classical
   linear theory — computable); decide whether the corpus wants the
   reconnection-vs-blowup question in scope.
2. **U4 sharpening:** derive the saturation value `α = Γ/(πV₁)` from the
   Burgers-vortex balance as a conditional Lean statement (the balance
   itself is algebra on the exact solution).
3. **Large-data global persistence** at the low-mode block (epic
   `qou-a3n3` remainder) — unchanged by this session; the millennium core.

## 5. The substrate-to-physical rescaling decision (owner brief, 2026-08-14)

`leray_bound_scaling` (PR #5031) made a structural fact explicit: the
q-ladder viscosity $\nu_q = \varepsilon/(2(1+\varepsilon))$ **vanishes** as
$q \to 1^+$, so in substrate units the in-QOU classical limit is a
*vanishing-viscosity* (Euler-type) limit — not the fixed-$\nu$ Navier–Stokes
setting of the Clay formulation. Any "millennium mapping" claim must first
choose units. Three options, with pros/cons and downstream impact:

**Option A — substrate units as-is (status quo).**
$\nu_q$ vanishes; the classical limit is Euler-type.
*Pros:* no new convention; $\nu_q$ is derived from $q$ (zero new DOF);
every existing witness/probe (SF1–SF5, GP, PC arcs) is already in these
units. *Cons:* the Clay problem is fixed-$\nu$; an Euler-limit statement
cannot be presented as the millennium problem without a bridge, and
vanishing-viscosity limits carry their own pathologies (anomalous
dissipation, Onsager-type roughness). *Downstream:* zero migration; but
every "millennium" phrasing in the corpus must be labeled in-QOU-limit,
never Clay-equivalent.

**Option B — $c_q$-rescaled (physical) units.**
Rescale time/length by $c_q = 1/(q-1) = \varepsilon^{-1}$ (an *existing*
canonical substrate scale — not a new fitted constant), making the
effective viscosity $\varepsilon$-independent ($\to 1/2$).
*Pros:* the limit becomes fixed-$\nu$ NS — direct Clay correspondence; the
discrete Leray control becomes $\varepsilon$-uniform in these units (the
$\varepsilon^{-1}$ degradation is exactly absorbed). *Cons:* the ladder
spacing collapses ($k_{\mathrm{phys}} = \varepsilon\,[n]_q$ — a continuum
limit), so the finite-block machinery (norm equivalence, fixed-band split)
does not transfer verbatim; every existing fluid witness number would need
re-expression; unit-straddling risk across the corpus (cf. the $\mu_3$
anchor-straddle incident) — the substrate-unit q-NS content is extensive.
*Downstream:* a migration comparable to a convention change; high
flip-flop risk if done piecemeal.

**Option C — two explicit unit layers with the $c_q$ tie (recommended).**
Keep substrate units for categorical/internal statements; define the
$c_q$-rescaled layer once, as a content block with the conversion lemma;
every Clay-facing statement carries its unit tag. This mirrors the repo's
q₀ ideal/experimental two-pin discipline, including its STRICT
never-straddle rule.
*Pros:* zero migration of existing content; the rescaling is derived (tied
to $c_q$, no new DOF — anti-fit clean); both faces of the uniformity
question become stateable, and probes can report both normalizations
cheaply (SF5 already does). *Cons:* permanent bookkeeping — every new
fluid block must declare its layer; two-layer conventions have caused
straddling bugs before, so the STRICT rule must land with the definition.
*Downstream:* one new definition block + a STRICT note in the fluid
chapter; the tail hypothesis splits into a substrate-unit (Euler-type)
and a $c_q$-unit (fixed-$\nu$) version — which may have *different*
answers, and SF5's dual-normalization output is designed to see that.

**Status: DECIDED — Option C (owner, 2026-08-14, "4 then C").** Implemented
as [`def:qns-unit-layers`](../../content/quantum-observable-universe/fluid-dynamics/qns-unit-layers.md):
the two layers, the derived $c_q$ tie ($\nu_{\mathrm{phys}} = c_q\nu_q =
1/(2q)$ exactly, Lean-proved), the conversion identities, and the
never-straddle STRICT rule. The uniformity question now officially splits:
substrate-layer (Euler-face) — refuted in-model by SF5; physical-layer
(fixed-$\nu$ face) — supported in-model by SF5. Clay-facing statements use
the physical layer, tagged.
