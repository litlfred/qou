# Borel / alien-calculus (resurgence) utilization audit

**Date:** 2026-07-12
**Status:** AUDIT (survey + prioritized opportunity map) — no derivation, no
wiring, no c_k value proposed (flip-flop guard). Maps where Écalle
resurgence machinery (Borel transform 𝓑, alien derivatives Δ_ω, the bridge
equation Δ_ω f̃ = A_ω ∂f̃/∂z, Stokes constants, median resummation) can be
**utilized** across four axes: compute speed/accuracy, proof-gap closure,
exposition, and proof consolidation. Every opportunity carries the file it
attacks and the concrete failure mode or gap it addresses — per the
formalize-first discipline, structural targets are stated before any
numerical probe is proposed.

**Companions (read first):**
[`2026-07-11-qbeta-ck-untested-avenues-and-literature.md`](2026-07-11-qbeta-ck-untested-avenues-and-literature.md)
(literature: Andersen–Mistegård resurgence of Ẑ, GMP arXiv:1605.07615,
Crew–Fantini–Goswami–Osburn–Wheeler arXiv:2304.07001, state-integral
summability arXiv:2410.20973),
[`../coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) (master ledger),
[`../coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
(F(q) keystone axis).

**Terminology caution.** Two unrelated "Borel"s live in the corpus:
[`borel-zagier-qou-volumes`](../../content/quantum-observable-universe/predicted-spectra/borel-zagier-qou-volumes.md)
and `QOU/Archimedean/BorelZagierQouVolumes.lean` concern the Borel
**regulator** on K₃ (ℚ-linear independence of hyperbolic volumes) — not
Borel **resummation**. This audit is about the latter; the two must not be
cross-linked as if they were one topic.

---

## 0. What already exists (do not duplicate)

| Artifact | What it is | Verdict / state |
|---|---|---|
| [`docs/audits/scripts/qbeta_borel_pade_action.py`](scripts/qbeta_borel_pade_action.py) | Borel transform of the 4₁ Ohtsuki ladder κ₁..κ₁₁ + [M/M] Padé; poles = Borel singularities = instanton action ±A | Borel–Padé pole **Froissart-unstable** (nearest pole jumps 0.714 → 0.049 → 0.049+0.12j across M = 3,4,5); action A ≈ 0.6937 taken instead from large-order ratio + Richardson — **phase-blind** |
| [`docs/audits/scripts/qbeta_resurgence_action_halffig8.py`](scripts/qbeta_resurgence_action_halffig8.py) | Order-6 predecessor (large-order growth ratio) | Superseded by the above; witness says tight value "needs ~20 orders / Borel–Padé" |
| `QOU/Mathlib/BorelResummation.lean`, `QOU/Infra/BorelRank.lean` | Lean scaffolds (Mathlib-gap tier, bean `el8w`) | Scaffold only |
| [`computations/qbeta/phi_b_evaluator.py`](../../computations/qbeta/phi_b_evaluator.py) + `phi_b_substrate_regime.py` | Faddeev Φ_b (state integral / modular double) | Landed 2026-07-11 (PR #3540); substrate regime pinned |

No conformal-map-of-the-Borel-plane and no transseries reconstruction exists
anywhere in the corpus.

## 1. Compute axis — speed / accuracy opportunities (ranked)

### C1. Stabilize the 4₁ action extraction: conformal-mapped Borel plane (highest ROI)

[`qbeta_borel_pade_action.py`](scripts/qbeta_borel_pade_action.py) abandoned
the raw Borel–Padé because of Froissart doublets and fell back to Richardson
on coefficient ratios — which yields |A| but **cannot recover the phase** of
the Borel singularity (the script flags that θ ≲ π/11 would not flip signs).
The textbook cure for exactly this instability is a **conformal map of the
Borel plane** (uniformize the cut, ζ = 4Aw/(1+w)²-style, Padé in w):

- stable branch-point location at the existing order 11 (no new κ_k needed);
- resolves real-vs-complex A — i.e. **phase-resolves the f-map Stokes
  datum**, the keystone quantity deciding 𝔙 = Vol ± iCS.

### C2. Un-block the ℚ(√−3) saddle-coefficient PSLQ: run it on 𝓑-transformed coefficients

[`qbeta_action_qsqrt3_saddle_probe.py`](scripts/qbeta_action_qsqrt3_saddle_probe.py)
was refuted for a Borel-shaped reason recorded in its own verdict: the saddle
coefficients grow factorially, c_m ~ m!/A^m, so the rescaled c_m·m!·(2π)^m
explodes past PSLQ's entropy reach. The **Borel-transformed coefficients
b_m = c_m/m! are O(1/A^m)** — bounded and PSLQ-tractable. Re-running the
identical probe on b_m removes the stated blocker without touching the
anti-fit discipline (hypothesis-class test, not a value fit).

### C3. Exact κ₂..κ_K via transseries anchored on A

[`qbeta_ohtsuki_kappa1_extract.py`](scripts/qbeta_ohtsuki_kappa1_extract.py)
recovered κ₁ = 11√3π/108 exactly but higher κ_k are
asymptotic-truncation-limited (the full-ladder sibling run was
entropy-blocked by the same factorial growth). A Borel-plane fit anchored on
the C1-stabilized A (or a Borel–Écalle transseries reconstruction) yields
κ₂, κ₃, … beyond the numerical fit's reach, unblocking the ℚ(√3)·πʲ PSLQ
that succeeded only at κ₁.

### C4. Decide bounded-vs-factorial for the c_k ladder with a clean Borel ratio test

Three probes disagree in substance:
`qbeta_ck_genfunc_bounded_vs_factorial_probe.py` (BOUNDED; "keystone is NOT
Borel resummation"), `qbeta_ck_closed_form_candidate_fits_probe.py`
(c_k = −(k−1)! divergent-Borel-summable reading), and
`qbeta_ck_truncation_order_analysis.py` (convergent-series framing; also the
KC8 geometric-growth datum `c_{k+1}/c_k → 1/u`). A single Borel-transform
ratio/Padé test on **symbolic (non-SDP-contaminated)** c_k would adjudicate.
Analytic-vs-resurgent is the fork the 1 ppQ roadmap hangs on; the genfunc
probe's residual-boundedness heuristic ran on SDP-contaminated data.

### C5. Φ_b near-|q|=1 speed: resurgent/modular resummation of the tail

`phi_b_substrate_regime.py` needs ~900 product terms for 40 dps at
|q| = 1/q₀ (term count ∝ 1/ln q₀ — diverges as q₀ → 1). The modular dual
q̃ = e^{−4π²/t} piece (currently negligible, ~1e-164, and dropped) is exactly
the resurgent transseries partner; a modular resummation replaces the
O(1/ln q₀) sum with a closed asymptotic + exponentially small correction.
Only matters for future scans pushing q₀ toward 1 — lower priority.

### C6. State-integral saddle-fluctuation transseries (infrastructure gap)

`qbeta_c3_phib_saddle_state_integral_probe.py` +
`qbeta_c3_state_integral_ladder_bridge_probe.py` establish the saddle
𝔙(m) is smooth/anchor-blind and name the exact even/odd ladder D(u) as "the
residual open object". The resurgent transseries around that saddle produces
its fluctuation orders one by one (the i·t·κ₁ finite-b correction already in
use is the leading term). No script computes it — pure opportunity, and the
audits call it "the wall".

*(C7 — weak: A→∞ subleading constant of the super-exponential w_std tower
sum via Borel–Écalle; existing Cauchy–Schwarz proof already closes the
structural claim, so this matters only if a quantitative scale is wanted.)*

## 2. Proof-gap axis

The corpus already carries a Borel-transform scaffold
(`QOU/Mathlib/BorelResummation.lean`) and a non-abelian Stokes scaffold
(`QOU/Mathlib/NonAbelianStokes.lean`), both written as conditional-class
placeholders. Each gap below is stated in the corpus as a class field, a
`sorry`, an "entropy-blocked" numeric, or an open kernel.

**Anti-laundering guard (applies to every item):** axiomatizing a
resurgence statement as a §3b-cond class does **not** prove it. The
"realistic" items below are realistic because a *literature theorem* exists
for the specific instance (citable, then honestly transcribed as a class
instance with `-- Ref:`); the rest stay conjectures.

### G1. Discharge `VolumeConjecture41` via Nevanlinna–Sokal on the 4₁ Kashaev series (highest leverage)

`QOU/Knot/FigureEightVolume.lean` carries the 4₁ volume conjecture as an
axiomatized class (`limit_eq_vol`). The header of
`QOU/Mathlib/BorelResummation.lean` states verbatim that the proof "goes
through Borel resummation of the asymptotic series of the Kashaev sum" and
that closing `BorelSummable` for that series is what would discharge the
conditional. The 4₁ case **is a literature theorem** (Andersen–Hansen;
higher-order expansion Ohtsuki) — replacing the placeholder
`BorelTransformConverges` with a genuine Nevanlinna–Sokal / Watson
uniqueness instance for this one series, cited per §1 `-- Ref:` rules,
mechanically discharges `VolumeConjecture41`. **Downstream payoff:**
[`kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md)
(ρ_F = ν_SDP, currently doubly-conditional) drops to singly-conditional.

### G2. Dissolve the κ-ladder entropy block with the bridge equation

`QOU/QBeta/Qsqrt3SaddleArithmetic.lean` +
[`2026-07-11-fmap-action-qsqrt3-saddle-lean.md`](2026-07-11-fmap-action-qsqrt3-saddle-lean.md):
b₁ = √3π/54 Lean-certified, κ₁ = 11√3π/108 PSLQ-identified, higher `[1/N^k]`
coefficients "entropy-blocked (#3571)" — PSLQ on divergent-series numerics
can't reach exact ℚ(√−3) arithmetic. The Écalle **bridge equation**
Δ_ω f̃ = A_ω ∂f̃/∂z generates the higher coefficients *arithmetically* from
the Stokes constant (already found at 2-loop) instead of recognizing them
numerically — a derivation route, not a fit, so it passes the anti-fit
discipline where PSLQ could not pass the entropy bound.
Literature: Garoufalidis–Gu–Mariño give the explicit resurgent structure
and Stokes automorphism for 4₁ over ℚ(√−3).

### G3. Sharpen `conj:kashaev-volume-conjecture` (general KVC) resurgently

The class field `kvc_holds` is a bare identity. The resurgence framing
sharpens it: the leading Borel singularity of the saddle series sits at the
**complex volume 𝔙 = Vol + i·CS**, and median resummation across the Stokes
ray yields the growth rate. General case research-grade (GMP /
Andersen–Mistegård programme), but **per-knot instances** (5₂, 6₁ — where
resurgence is numerically verified in the literature) are citable as
concrete class instances, matching the block's own "locality" design.

### G4. Recognize the open Habiro kernel `R(q,ξ)` as a Stokes automorphism

`prop:q-beta-c-k-recursion-from-habiro-q-difference`: `c_k` for k ≥ 3 are
"conjectural pending the kernel R(q,ξ)" — the same open input as the
absolute-mass `F_Bor` term-6 Habiro tail. The Habiro sum is q-holonomic;
its divergent tail is Borel-summable, and the higher `c_k` are the
alien-derivative data of that series (the `tau-M` block already calls them
"higher Ohtsuki invariants of the correction factor" — which *is* the
resurgence identification). Recognition-level reframing; if it holds, the
c_k recursion **is** the bridge recursion. Note the §1.C4 fork: the ladder's
KC8 geometric growth (simple pole) vs the Ohtsuki series' Gevrey-1 growth
must be reconciled at the f-map — this reframing lives on the fibre side.

### G5. Surreal `st` = median resummation (provable identification)

[`kashaev-surreal.md`](../../content/quantum-observable-universe/appendix-surreals/kashaev-surreal.md)
isolates its hard row to "st application: asymptotic transseries reduction
(Berarducci–Mantova)". The standard part of the surreal evaluation on the
Stokes ray is exactly a **median resummation** (the canonical
real-single-valued choice resolving the lateral-Borel ambiguity), and
Écalle transseries are the Berarducci–Mantova transseries the block already
invokes. Provable-now reframing that turns an unspecified "reduction" into
a named resurgence theorem; the geometric identity itself stays open (= G3).

### G6. Upgrade the `chernSimons_volume_correspondence` tautology

`QOU/Mathlib/NonAbelianStokes.lean` carries it as a `∃ vol, ∀ h, vol h =
vol h` placeholder (flagged NEEDS-NEW-INPUT). The resurgent reading — Re of
the Borel-singularity location = Vol, Im = CS, i.e. the **phase of the
Stokes constant carries CS** — is the actual content clause, backed by the
same instance as G1; it is also exactly the two channels the
ζ₄-partner block (`ComplexVolumeZeta4Partner.lean`) splits.

### G7. The Φ_q ↔ Li₂^q two-saddle bridge is a Stokes automorphism

[`phi-q-aj-machinery-identification.md`](../../content/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md)
posits the real-q vs root-of-unity saddle regimes "via Stokes" with the
modular S-transform as the connecting move — which is precisely the
resurgence connection formula / Stokes automorphism (Garoufalidis–Kashaev
state-integral evaluations, Andersen–Kashaev). Realistic for the bridge
statement; the Borromean AJ input (𝓑₃) stays research-grade open.

### Explicitly NOT resurgence targets

`conj:borel-zagier-qou-volumes`, `prop:borel-partial-resolution`, and the
depth-3 residue `Cl₃(2π/5) − Cl₃(4π/5)`: Borel **regulator** / Beilinson
transcendence (Armand Borel, not Émile Borel). Resurgence does not bear on
ℚ-linear independence of volumes. Likewise all fluid-dynamics /
Yekutieli "Stokes" hits (surface theorem, not Stokes phenomenon).

## 3. Exposition axis

### The triple-overloading hazard (framing finding)

"Borel" carries **three unrelated senses** in the corpus, and only one is
resurgence:

1. **Borel subalgebra** (Lie theory) — `q-geometric-langlands/q-oper.md`,
   `q-oper-hecke.md`, `q-oper-hecke-proof.md`.
2. **Borel's 1977 K-theory regulator** — the appendix-surreals B1 cluster
   (`borel-partial-resolution`, `k-theory-period-rosetta`, `b1-*`,
   `qou-infra-discharges-goncharov-zeta5`) + `conj:borel-zagier-qou-volumes`
   — the **only** "Borel" in the definition index.
3. **Écalle–Borel resummation** (this audit's sense) — exactly **two**
   corpus mentions:
   [`appendix-surreals-archimedean/analytic-obstructions.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/analytic-obstructions.md)
   ("Écalle–Borel transserial functions") and
   [`mass-theory/q-beta-c3-continuum-geometry.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c3-continuum-geometry.md)
   ("high-precision Borel–Padé extrapolation").

There is **no** notation-register or definition-index entry for Borel
transform / alien derivative / Stokes constant / transseries. Also excluded
as false positives: every fluid-dynamics "Stokes" (surface theorem) and the
Yekutieli non-abelian Stokes hits.

### E1. New definition block `def:ecalle-borel-resummation` (home for the framework)

Place in `appendix-surreals-archimedean`; content: Borel transform
𝓑{f̃}(ξ) = Σ aₙ ξ^{n−1}/(n−1)!, lateral/median resummation, optimal
truncation, alien derivative Δ_ω + bridge equation. **Do not** name it
`def:borel-transform` (collides with senses 1–2). Immediate consumers:
`analytic-obstructions.md` (its "Écalle–Borel" mention is currently
dangling) and `q-beta-c3-continuum-geometry.md` (its "Borel–Padé
extrapolation" claim is orphaned — no definition, no cross-ref — on a block
already carrying a 2026-07-11 overclaim-correction banner). Buys: closes a
dangling technical term on a flagged block; single home for
beyond-all-orders error language; disambiguates the three Borel senses.

### E2. Notation-register + definition-index rows

Add register rows for transseries, `st`, `ordw`, Stokes constant A_ω, Δ_ω —
`st`/`ordw` are load-bearing across appendix-surreals yet unregistered. A
register-level note disambiguating the three "Borel" senses is a real
reader-hazard fix.

## 4. Consolidation axis

Two clusters currently re-derive the same asymptotic machinery:

**Cluster A — dilog saddle / Kashaev asymptotics (re-derived ~5×):**
`q-beta-c3-continuum-geometry.md` (saddle §, Borel–Padé),
`phi-q-aj-machinery-identification.md` (real vs root-of-unity saddle "via
Stokes"), `q-zero-stokes-region-identification.md` (Stokes region of the
colored-Jones generating function), `kashaev-volume-density.md` /
`kashaev-volume-conjecture.md` / `kashaev-as-archimedean-realization.md`
(the N→∞ bridge restated per block), `phi-q-resums-trace-series.md`,
`q-beta-cos-resummation.md`.

**Cluster B — transseries → standard-part reduction (re-stated ~5×):**
`kashaev-surreal.md` (Berarducci–Mantova transseries reduction),
`body-asymptotics-catalog.md` (Big-O → `ordw` catalog),
`surreal-blowup-calculus.md` (the canonical definition),
`perpetual-obstruction-depth-omega.md` (beyond-all-orders term = depth-ω
grade), `conway-normal-form.md`, `analytic-obstructions.md`.

### K1. Factor the dilog-saddle computation into one block

New `rem:dilog-saddle-regime` carrying
`d/dθ Im Li₂(e^{iθ}) = −log|2 sin(θ/2)| = 0 ⇒ θ = π/3 ⇒ Vol(4₁)`; wire
`q-beta-c3-continuum-geometry`, `phi-q-aj-machinery-identification`,
`q-zero-stokes-region-identification` to `uses[]` it. Removes 3
re-derivations (~12–15 lines from q-beta-c3 alone).

### K2. One home for the Kashaev N→∞ identity

`Vol = 2π lim log|J_N|/N` is written in ≥3 blocks; keep it in
`rem:kashaev-volume-density` and have `kashaev-surreal` + the mass-theory
Kashaev blocks `uses[]` it, keeping only their distinctive content (surreal
`st`-lift; ρ mass substitution).

### K3. Fan Cluster B into the existing `def:surreal-blowup-calculus`

`perpetual-obstruction-depth-omega` already `uses[]` it; extend the same
wiring to `kashaev-surreal.md` and `body-asymptotics-catalog.md` (same
section per the chapter manifest — no reshuffle needed). One
transseries-reduction definition instead of three prose restatements.

### K4. Finish the Φ_q context-sorting hub

`phi-q-aj-machinery-identification.md` *is* the intended unification node
("wiring this explicitly unifies the context-sorting into a single algebraic
statement") but `phi-q-resums-trace-series.md` and
`q-beta-cos-resummation.md` don't yet `uses[]` it and re-introduce Φ_q from
scratch. Wire both; the "Φ_q factors through Markov traces" argument then
lives in one place.

## 5. Prioritized cross-axis shortlist

| # | Action | Axis | Cost | What it buys |
|---|---|---|---|---|
| 1 | **G1** — Nevanlinna–Sokal instance for the 4₁ Kashaev series in `BorelResummation.lean` (literature theorem, `-- Ref:` cited) | proof gap | small Lean file + citation transcription | discharges `VolumeConjecture41`; de-conditions `kashaev-density-equals-sdp-multiplicity` one level |
| 2 | **C1** — conformal-mapped Borel plane in `qbeta_borel_pade_action.py` | compute accuracy | 1 probe script edit | cures documented Froissart instability; phase-resolves the f-map Stokes datum (Vol ± iCS decision) at existing order 11 |
| 3 | **C2** — rerun ℚ(√−3) saddle PSLQ on Borel-transformed b_m = c_m/m! | compute accuracy | trivial (flip a failing probe) | removes the probe's own stated factorial-overflow blocker; bounded coefficients fit the entropy budget |
| 4 | **E1+E2** — `def:ecalle-borel-resummation` block + notation-register rows + three-Borel disambiguation | exposition | 1 block + register edit | closes 2 dangling term uses (one on an overclaim-flagged block); makes the framework vocabulary discoverable |
| 5 | **C4** — clean Borel ratio/Padé test on symbolic c_k | compute (decider) | 1 probe | adjudicates the bounded-vs-factorial contradiction between three probes — the fork the 1 ppQ roadmap hangs on |
| 6 | **G2** — bridge-equation generation of κ₂..κ_K (with C3 as numeric cross-check) | proof gap + compute | research-grade, literature-guided | derivation route around the #3571 entropy block; anti-fit compliant |
| 7 | **K1–K4** — dilog-saddle block, Kashaev-identity fan-in, Cluster-B fan-in, Φ_q hub wiring | consolidation | mechanical `uses[]` + block edits | ~5× duplicated saddle machinery and ~3× transseries-reduction prose collapse to single homes |
| 8 | **G5** — surreal `st` = median resummation reframing | proof gap (reframe) | 1 block edit + citation | names the unspecified "transseries reduction" row; provable now |

Items 1–4 are bounded, this-branch-sized. Items 5–6 need probe runs
(long-compute logging discipline applies). Item 7 is a follow-up
consolidation branch (touches ~12 blocks). Nothing here proposes a c_k
value or wires anything to production.
