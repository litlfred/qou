---
# z2bn
title: 'Lever 1 [FOCUS]: derive/test fibre q-difference kernel R(q,x) for binding genfun; kill-switch = magic-A ⁴He +5.87%'
status: in-progress
type: task
priority: normal
created_at: 2026-06-23T14:19:27Z
updated_at: 2026-06-24T11:45:00Z
---


## Coordination breadcrumb (2026-06-24) — ⁴He binding falsification thread

Empirical input for the R(q,x) derivation + the magic-A ⁴He kill-switch, from the
merged binding thread (PRs #2630/#2681/#2703):

- **B_joint^model (|χ| joint trace) is nearly A-INDEPENDENT**: ³H 3.25 → ³He 3.47 →
  ⁴He 3.80 MeV, while B_AME explodes (8.48 / 7.72 / 28.30). ⁴He captures only **13%**
  of its binding. The multiplicative deficit `1−∏f` **saturates**
  (`productModel_3body_nonpos`).
- **Implication for R(q,x):** its solution **must grow with A** (the `Iν` q-Bessel
  growth regime). A saturating/intensive trace object cannot source the extensive
  binding — that is the dominant gap, bigger than any phase/sign correction.
- The q-Reeb phase `|Δθ_λ|` is only a **directional** correlate (the constant-scale
  `0.206 MeV/rad` relation was falsified at ⁴He, +69%), not the magnitude source.

Witnesses: `he4-qreeb-phase-falsification.witness.json`,
`yardstick-free-phase-binding.witness.json`.
Audit: `docs/audits/2026-06-24-he4-qreeb-phase-falsification.md`.

## Deliverable (2026-06-24, PR #2718) — spectral bridge: the kernel IS extensive

The depth-2 kernel `R=x²−τx+1` (τ(q₀)=2.6424 from the selection-rule anchors,
#2612) has characteristic roots **λ₊=2.1846, λ₋=0.4577** (product 1, det=1). The
dominant root **λ₊>1 is the extensive-growth eigenvalue** the saturating `|χ|`
trace (λ_eff≈1, the degenerate τ=2 boundary) lacks — so the *existing* kernel
already supplies the extensive (A-scaling) binding PR #2703 found missing. The
`a_D⁽ⁿ⁾` body-order sequence grows with ratio → λ₊.

Formalized sorry-free: `QOU/Mass/BindingRecurrenceSpectral.lean`
(`lambdaPlus_gt_one`: τ>2 ⇒ λ₊>1). Probe:
`binding_recurrence_spectral_bridge_probe.py`. Non-overlapping with the geometric
monodromy derivation of τ (sibling `lever1-trB`, owner-gated DG). Does NOT close
the magic-A ⁴He +5.87% (finite-truncation residual).
## Frontier (2026-06-24, post #2674 / #2701 / #2704) — reduced to ONE owner-gated number

The lever-1 binding kernel `R(q,x)` is the depth-2, `det = 1` recurrence `R = x² − τx + 1`.
Everything reduces to the single trace `τ = tr B`:

- **Selection rule confirmed** at c=1 (muon `lw(1)=1`) + c=3 (proton `lw(3)=Family-A`, bit-for-bit
  production `linking_weight_family_a`). `a_D^(n) = lw(n−1)`, `lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q`.
- **Whole identification = one checkable number:**
  `τ = (a_D^(2)+a_D^(4))/a_D^(3) = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6424 at q₀`
  (algebra: num `(3q⁴+8q²+3)/(4q²)` ÷ `(q+1)²/(3q)`; cross-checked this session).
- **Torus shortcut REFUTED (#2701):** `τ_torus = 2cosh(2η₀) = 2.0437 ≠ 2.6424`. The binding W-plane is a
  genuinely separate genus-4 Bring object, not the substrate torus.

## The decisive step is OWNER-GATED (sharp reframing, #2701)

`tr B` is a q-FAMILY Gauss–Manin **monodromy** trace, not a fixed-curve period — a single fixed curve
has no monodromy. So the Sage fixed-curve period work (done) cannot supply it; `tr B(q₀)` needs the
**q-family matrix M = the s5-so3 keystone (owner-gated, residual i)**. Fixed-curve facts settled exactly
(Sage + character theory): `H^{1,0}(Bring)` is the standard 4-dim S₅ irrep, A₅-irreducible ⇒
`H¹(Bring)=2W` is NOT an A₅-form-subspace; `W` must be a **CM/isogeny factor of `Jac(Bring)`**
(Riera–Rodríguez), at the de Rham level.

## Three sub-directions (none a quick win; pick with owner)

| # | direction | gating |
|---|-----------|--------|
| A | q-family Gauss–Manin monodromy `M` on the W-plane (supplies `tr B`) | **owner-gated** (keystone residual i; the decisive step) |
| B | Riera–Rodríguez CM/isogeny decomposition of `Jac(Bring)` → exhibit the rank-2 `W` | tool-gated (Sage, fixed-curve; deep, NOT owner-gated) |
| C | non-circular c=2 mass-consumer to TEST `lw(2)=(q+1)²/(3q)≈1.337` | research-grade, circularity-gated (Hopf link non-hyperbolic → no Kashaev/Vol route) |

Refs: `docs/audits/2026-06-24-lever1-trB-geometric-target.md`,
`2026-06-24-lw2-c2-prediction-untested-status.md`, `2026-06-23-delta-lambda-three-lever-status.md`.
Kill-switch (magic-A ⁴He +5.87%) unchanged. No fit; nothing wired. Owner closes (§4a).

## Progress 2026-06-24 (PR #2708) — A/B sharpened, C clean (a)-negative

Owner picked all three (B, A, C). Disciplined increments (formalize-first; Sage unavailable in
this container ⇒ analytical/corpus synthesis, not compute):

- **A + B — binding monodromy is HYPERBOLIC, not compact SU(2).** Corpus-grep surfaced the
  un-cross-referenced **2026-06-06 M-workplan**: `H¹(Bring)=W⊗ℂ²` (Riera–Rodríguez; `W`=irred
  4-dim S₅ rep), `M=id_W⊗B`, `B∈SL₂`, `det=1` (Lean `sl2_prolongation_recurrence`). So the rank-2
  `W` is the **S₅-Hodge multiplicity space = candidate H¹(coral elliptic E_z)** (B largely
  resolved). Probe: `τ_binding=2.6424>2` ⇒ `B` hyperbolic; the coral `E_z` monodromy = trefoil
  holonomy is **compact SU(2)** (`(H₁H₂)³=id`, `tr=−1`, `|tr|≤2`) ⇒ `B` **structurally excluded
  from compact SU(2)** ((b), trace invariant) — it's the non-compact `SU_q(2)→E_q(2)`
  continuation, the **same arena the keystone reached from the W_λ side** (independent
  convergence). Refines the torus refutation: torus is *also* hyperbolic (2.044), so binding≠torus
  is a *rapidity* mismatch (`θ_b/θ_t=3.74`), not compact-vs-noncompact. Next (tractable, NOT
  genus-4): compute the coral `E_z` (genus-1) Picard–Fuchs rapidity, test `=θ_binding=0.7815`.
  Probe `lever1_binding_monodromy_hyperbolicity.py` (8/8); audit
  `2026-06-24-lever1-binding-monodromy-hyperbolicity.md`. Hygiene flag: M-workplan's 3 `.py`
  scripts are NOT in the tree (only Lean+props back it).
- **C — lw(2) still circularity-gated (clean (a)-negative).** Independent Hopf-link `T(2,2)`
  Markov trace `tr_M(σ₁²)=1+(q−1)/√q ≈ 1.1044` (no selection-rule input) ≠ `lw(2)≈1.337`. Reason:
  `lw(c)` is a **mean quantum dimension** (rep count), NOT a single-link trace — wrong *kind* of
  object. (a)-scope: constrains the identification, not lw(2)'s validity. Still needs a
  non-circular c=2 mass-consumer. Probe `lw2_c2_independent_hopf_test_attempt.py` (4/4); audit
  `2026-06-24-lw2-c2-independent-test-attempt.md`.

Net: B resolved to the coral-`E_z` rank-2 factor; A sharpened to a tractable genus-1 Picard–Fuchs
rapidity test + keystone-arena convergence; C confirmed circularity-gated. No closure; no fit;
nothing wired. Owner closes (§4a).

## Option 2 (2026-06-24, PR #2708) — coral `E_q` confirmed; `tr B` non-integer reframes the test

Ran the genus-1 coral `E_q` step (Sage unavailable ⇒ analytical):
- **Coral `E_q` = descartes `E_q` CONFIRMED** by the invariant `j`: `j(q₀)=129.86` (descartes 129.9),
  `j(1)=128`, `p(1)=2/3`, `r(1)=20/27` exact. Direction-B curve half **closed** (single identified curve,
  not genus-4).
- **Decisive reframing:** `tr B = 2.6424 ∉ ℤ`, but the **topological** Gauss–Manin monodromy of an
  elliptic family is in `SL₂(ℤ)` (integer trace). So `B` is **NOT** the topological monodromy — it is the
  **abelianised `λ_SW` Cartan-connection holonomy** (real/hyperbolic, `τ=2cosh θ`), per the M-workplan
  abelianisation. The literal option-2 goal (genus-1 Picard–Fuchs *topological* monodromy) computes the
  wrong (integer-trace) object. `τ_torus=2.0437` also non-integer ⇒ same connection-holonomy nature.
- **Still open (keystone):** the explicit abelianised-connection holonomy `=θ_binding=0.7815` at q₀.
Probe `lever1_coral_eq_monodromy_integrality.py` (7/7); audit
`2026-06-24-lever1-coral-eq-monodromy-integrality.md`. No fit; nothing wired. Owner closes (§4a).

## Option 3 (2026-06-24, PR #2708) — depth-2 recurrence FALSIFIED beyond seed; θ_binding is a fit

Tried to derive `θ_binding` as the rate of the `a_D=lw` depth-2 recurrence. **It fails.** `τ` fit to
the n=2,3,4 seed (=2.6424, the closed form) **does not satisfy the n=5 check**: `lw(4) − (τ·lw(3)−lw(2))
= 0.0205` (0.4%), n=6 1.887 (14%), n=7 6.91 (18%). The **windowed kernel drifts** 2.6424 → 2.6505 →
2.9933; `lw(c)` ratios 1.34→2.76 *increase* (super-geometric, like involution numbers) ⇒ not `Aλᶜ+Bλ⁻ᶜ`
for fixed `λ`. So `lw(n−1) ≠ φ(Mⁿv₀)` for any fixed 2×2 `M` (Cayley–Hamilton) — **(b)-exclusion** of the
const-coeff depth-2 model (invariant: window-independent kernel). **`θ_binding=0.7815` is a 3-point
seed-fit artifact, not a derived rate.** Does NOT refute the `Jac(Bring)~E⁴` isogeny (sibling
`mass-open-keystone-w-l2-root`) or the 2×2 `M`'s existence — only that the `lw` values ARE its prolonged
periods beyond the seed. Convention validated (lw(2), lw(3)=Family-A match corpus). Cross-link: the
sibling's open `j(E)` is answered by the coral `j(q₀)=129.86`. Probe
`lever1_lw_depth2_recurrence_test.py` (7/7); audit `2026-06-24-lever1-lw-depth2-recurrence-falsified.md`.
No fit; nothing wired. Owner closes (§4a).

## Continuation (a) (2026-06-24, PR #2708) — NO shortcut; golden τ=3 refuted; residual is owner-gated

Checked for a topological/integer/golden shortcut to `τ=2.6424` before the deep `λ_SW` integration.
The seed `τ` is **forced** by the three wired anchors (`a_D²=1`, `a_D³=lw(2)`, `a_D⁴=Family-A` = the
production proton multiplier), is non-integer, strictly in (2,3). **No integer `τ` reproduces the wired
Family-A**: τ=2 misses 34%, the icosahedral **golden τ=3 (`λ=φ²`) misses 19%**, τ=4 misses 72%. So `B`
is not any topological `SL₂(ℤ)` monodromy and the golden hypothesis is **refuted by the seed**
(numerology guard held — tested, not forced). The genuine `2.6424`-object is the **owner-gated
abelianised `λ_SW` real connection holonomy** on the coral `E_q` (`SL₂(ℝ)`, hyperbolic, θ=0.7815).
Concrete owner-gated next step: integrate `λ_SW = x dz` on `E_q` + its Gauss–Manin prolongation (genus-1
period integration; sandbox Sage blocked; sibling `mass-open-keystone-w-l2-root` holds the curve side).
Probe `lever1_lambda_sw_no_shortcut.py` (4/4); audit `2026-06-24-lever1-lambda-sw-no-shortcut.md`.

**Lever-1 frontier now fully mapped:** curve = coral/descartes `E_q` (j confirmed); `B` = abelianised
`λ_SW` real holonomy (not compact SU(2), not topological `SL₂(ℤ)`, not an `lw`-recurrence rate, no
integer/golden shortcut); the explicit holonomy = θ_binding is the owner-gated keystone `M` on the
elliptic factor. No fit; nothing wired. Owner closes (§4a).

## Progress 2026-06-25 — depth-2 (b)-exclusion Lean-formalized; τ-derivation OWNER-AUTHORIZED

- **(b)-exclusion now Lean-backed (PR #2764):** `QOU/Mass/Lever1Depth2Exclusion.lean` (sorry-free,
  lean-direct exit 0) proves `∀ τ, ¬(lw₃=τ·lw₂−lw₁ ∧ lw₄=τ·lw₃−lw₂)` at the classical limit q=1
  (lw=(1,4/3,5/2,26/5); seed forces τ=21/8, c=4 needs 26/5=251/48, residual −7/240). Substrate-free
  (pure ℚ); the q=1 residual ≠ 0 ⇒ the q-rational residual is not identically zero ⇒ q-general
  failure. Dims computed via hook-length (decide, dodge-proof). Backs the audit "θ_binding is a
  seed-fit artifact". (b)-scope: const-coeff model only; variable-τ monodromy B untouched.
- **Owner LIFTED the gate (2026-06-25):** authorized the gated τ-derivation (abelianised λ_SW
  holonomy on coral E_q) AND confirmed Sage is gettable. Tooling now present in-container
  (mpmath 1.3.0 + sympy 1.14.0 pip-installed; full Sage may not be needed — numerical
  elliptic-period integration suffices). Coordinated with sibling #2722 (geometric tr B side) to
  avoid double-work. **Next focused step (formalize-first):** locate the coral/descartes E_q curve
  eqn in corpus, set up λ_SW = x dz period/Gauss-Manin holonomy, derive τ WITHOUT fitting to 2.6424
  (numerology guard). NOT yet started — deep effort, pending owner go / #2722 coordination.
