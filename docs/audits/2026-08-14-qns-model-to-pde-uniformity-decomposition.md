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

1. **U3 formalization target:** state the Crow-instability dispersion
   relation as a content block with a probe (the growth rate is classical
   linear theory — computable); decide whether the corpus wants the
   reconnection-vs-blowup question in scope.
2. **U4 sharpening:** derive the saturation value `α = Γ/(πV₁)` from the
   Burgers-vortex balance as a conditional Lean statement (the balance
   itself is algebra on the exact solution).
3. **Large-data global persistence** at the low-mode block (epic
   `qou-a3n3` remainder) — unchanged by this session; the millennium core.
