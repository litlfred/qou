---
# z2bn
title: 'Lever 1 [FOCUS]: derive/test fibre q-difference kernel R(q,x) for binding genfun; kill-switch = magic-A ⁴He +5.87%'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-23T14:19:27Z
updated_at: 2026-10-04T15:13:13Z
parent: qou-v2om
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
  `W` is the **S₅-Hodge multiplicity space = candidate H¹(color elliptic E_z)** (B largely
  resolved). Probe: `τ_binding=2.6424>2` ⇒ `B` hyperbolic; the color `E_z` monodromy = trefoil
  holonomy is **compact SU(2)** (`(H₁H₂)³=id`, `tr=−1`, `|tr|≤2`) ⇒ `B` **structurally excluded
  from compact SU(2)** ((b), trace invariant) — it's the non-compact `SU_q(2)→E_q(2)`
  continuation, the **same arena the keystone reached from the W_λ side** (independent
  convergence). Refines the torus refutation: torus is *also* hyperbolic (2.044), so binding≠torus
  is a *rapidity* mismatch (`θ_b/θ_t=3.74`), not compact-vs-noncompact. Next (tractable, NOT
  genus-4): compute the color `E_z` (genus-1) Picard–Fuchs rapidity, test `=θ_binding=0.7815`.
  Probe `lever1_binding_monodromy_hyperbolicity.py` (8/8); audit
  `2026-06-24-lever1-binding-monodromy-hyperbolicity.md`. Hygiene flag: M-workplan's 3 `.py`
  scripts are NOT in the tree (only Lean+props back it).
- **C — lw(2) still circularity-gated (clean (a)-negative).** Independent Hopf-link `T(2,2)`
  Markov trace `tr_M(σ₁²)=1+(q−1)/√q ≈ 1.1044` (no selection-rule input) ≠ `lw(2)≈1.337`. Reason:
  `lw(c)` is a **mean quantum dimension** (rep count), NOT a single-link trace — wrong *kind* of
  object. (a)-scope: constrains the identification, not lw(2)'s validity. Still needs a
  non-circular c=2 mass-consumer. Probe `lw2_c2_independent_hopf_test_attempt.py` (4/4); audit
  `2026-06-24-lw2-c2-independent-test-attempt.md`.

Net: B resolved to the color-`E_z` rank-2 factor; A sharpened to a tractable genus-1 Picard–Fuchs
rapidity test + keystone-arena convergence; C confirmed circularity-gated. No closure; no fit;
nothing wired. Owner closes (§4a).

## Option 2 (2026-06-24, PR #2708) — color `E_q` confirmed; `tr B` non-integer reframes the test

Ran the genus-1 color `E_q` step (Sage unavailable ⇒ analytical):
- **Color `E_q` = descartes `E_q` CONFIRMED** by the invariant `j`: `j(q₀)=129.86` (descartes 129.9),
  `j(1)=128`, `p(1)=2/3`, `r(1)=20/27` exact. Direction-B curve half **closed** (single identified curve,
  not genus-4).
- **Decisive reframing:** `tr B = 2.6424 ∉ ℤ`, but the **topological** Gauss–Manin monodromy of an
  elliptic family is in `SL₂(ℤ)` (integer trace). So `B` is **NOT** the topological monodromy — it is the
  **abelianised `λ_SW` Cartan-connection holonomy** (real/hyperbolic, `τ=2cosh θ`), per the M-workplan
  abelianisation. The literal option-2 goal (genus-1 Picard–Fuchs *topological* monodromy) computes the
  wrong (integer-trace) object. `τ_torus=2.0437` also non-integer ⇒ same connection-holonomy nature.
- **Still open (keystone):** the explicit abelianised-connection holonomy `=θ_binding=0.7815` at q₀.
Probe `lever1_color_eq_monodromy_integrality.py` (7/7); audit
`2026-06-24-lever1-color-eq-monodromy-integrality.md`. No fit; nothing wired. Owner closes (§4a).

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
sibling's open `j(E)` is answered by the color `j(q₀)=129.86`. Probe
`lever1_lw_depth2_recurrence_test.py` (7/7); audit `2026-06-24-lever1-lw-depth2-recurrence-falsified.md`.
No fit; nothing wired. Owner closes (§4a).

## Continuation (a) (2026-06-24, PR #2708) — NO shortcut; golden τ=3 refuted; residual is owner-gated

Checked for a topological/integer/golden shortcut to `τ=2.6424` before the deep `λ_SW` integration.
The seed `τ` is **forced** by the three wired anchors (`a_D²=1`, `a_D³=lw(2)`, `a_D⁴=Family-A` = the
production proton multiplier), is non-integer, strictly in (2,3). **No integer `τ` reproduces the wired
Family-A**: τ=2 misses 34%, the icosahedral **golden τ=3 (`λ=φ²`) misses 19%**, τ=4 misses 72%. So `B`
is not any topological `SL₂(ℤ)` monodromy and the golden hypothesis is **refuted by the seed**
(numerology guard held — tested, not forced). The genuine `2.6424`-object is the **owner-gated
abelianised `λ_SW` real connection holonomy** on the color `E_q` (`SL₂(ℝ)`, hyperbolic, θ=0.7815).
Concrete owner-gated next step: integrate `λ_SW = x dz` on `E_q` + its Gauss–Manin prolongation (genus-1
period integration; sandbox Sage blocked; sibling `mass-open-keystone-w-l2-root` holds the curve side).
Probe `lever1_lambda_sw_no_shortcut.py` (4/4); audit `2026-06-24-lever1-lambda-sw-no-shortcut.md`.

**Lever-1 frontier now fully mapped:** curve = color/descartes `E_q` (j confirmed); `B` = abelianised
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
  holonomy on color E_q) AND confirmed Sage is gettable. Tooling now present in-container
  (mpmath 1.3.0 + sympy 1.14.0 pip-installed; full Sage may not be needed — numerical
  elliptic-period integration suffices). Coordinated with sibling #2722 (geometric tr B side) to
  avoid double-work. **Next focused step (formalize-first):** locate the color/descartes E_q curve
  eqn in corpus, set up λ_SW = x dz period/Gauss-Manin holonomy, derive τ WITHOUT fitting to 2.6424
  (numerology guard). NOT yet started — deep effort, pending owner go / #2722 coordination.

## Algebraic half FORMALIZED sorry-free (2026-06-25, PR #2755)

Rather than chase the owner-gated `λ_SW` holonomy (the obvious period probe is
already refuted — topological PF monodromy is integer-trace `SL₂(ℤ)`, but
`τ=2.6424∉ℤ`, per `2026-06-24-lever1-color-eq-monodromy-integrality.md`),
formalized the **algebraic** lever-1 skeleton in Lean
(`QOU/Mass/BindingTauAnchorClosure.lean`, sorry-free + axiom-free, lean-direct
exit 0, v4.24.0):

- `tauAnchor_closed_form`: the three wired anchors `a_D^(2,3,4)=lw(1,2,3)` force
  `τ = 3(3q⁴+8q²+3)/(4q(q+1)²)` (`field_simp; ring`);
- `tauAnchor_gt_two`: `0<q → 2<τ` for the whole substrate regime (SOS
  `504·(τ·den−2·den)=56(9q²−4q)²+(56q−36)²+3240>0`, `nlinarith`);
- `binding_extensive_at_substrate`: composes with `lambdaPlus_gt_one` ⇒ `λ₊>1`
  (extensive) given the anchors.

Discharges the spectral bridge's `2<τ` hypothesis at the substrate; the lever-1
skeleton is now machine-checked, so the ONLY open thing is sharply the geometric
`a_D^(n)=∮λ_SW^(n)=lw(n−1)` identification (owner-gated keystone `M`). MBA
step-09b appendix synced. Non-overlapping with sibling #2524 (W_λ facet). No fit;
nothing wired. Owner closes (§4a).

## Owner reversal — binding-τ keystone geometry GREEN-LIT (2026-06-25)

Owner (chat, this session) **extended the narrow Subgoal-2 reversal to the
binding-τ side**: authorized attempting the `λ_SW`-holonomy / SW-residue
derivation of `a_D^(n) = ∮_{S_c} λ_SW^(n) = lw(n−1)` on color `E_q`. (The prior
narrow reversal, 2026-06-19 / AGENTS.md §Subgoal-2, covered ONLY the `W_λ` side —
#2503/#2524.) **AGENTS.md §Subgoal-2 + the s5-so3 ledger should be updated to
record this binding-τ extension** (flagged to owner; STRICT-rule edit deferred to
explicit confirm).

**Scoping verdict (PR #2755 Explore agent, formalize-first preflight):**
- Curve explicit: color `E_q` = descartes `y²=x³+p(q)x+r(q)` (`s=√q`), j(q₀)=129.86.
- `λ_SW^(0) = X dz` explicit; `λ_SW^(1) = dX` (implicit deriv of color cubic).
- **GAP located:** `λ_SW^(n≥2)` is "higher jets follow by induction" —
  abstract, NOT a closed-form/computable rule. Residue framework
  (`sw-period-residue-sum`) *interprets* each residue as a per-block `dim_q`
  weight (= `lw`), but that identity is **asserted, not computed**.
- ⇒ Option 2 is a **CONSTRUCTION** (make the prolongation explicit), not a
  turn-crank compute. Falsifiable first step: low-jet residue (n=0,1) vs lw(1).

## Construction Step 1 EXECUTED (2026-06-25, PR #2755) — residue gap rigorously located

Probe `computations/substrate/lever1_color_sigma_geometry_probe.py` (6/6, pure
sympy+mpmath, **no Sage**): color spectral curve Σ: X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0
over the z-line, λ_SW=X dz (Liouville form on T*ℙ¹). Verified:
- **six singular fibres** (deg Δ=6, Δ palindromic ⇒ z↔1/z bar symmetry), squarefree;
- **genus 1** (Riemann–Hurwitz 2g−2=3(−2)+6=0) = color/descartes E_q;
- branch locus = 3 bar-symmetric pairs at |z|≈{1.000,0.943,1.060} (reciprocal);
- **CRUX: Res(X dz)=0 at every finite branch point** (Puiseux slope finite ⇒ no 1/t
  pole); only z=∞ carries residue {0,±5i/16}, sheet-sum 0.

**Finding:** the asserted a_D^(n)=2πiΣRes structure is EMPTY at finite branch points
for the bare n=0 differential — so a_D^(n)=lw(n−1) (n≥2) must come from the
prolongation λ_SW^(n) (n≥1). Gap rigorously located (not asserted): the explicit
jet-prolongation map, nothing upstream. First decidable lw(1)=1 check unreachable
until λ_SW^(2) is explicit. Consistent with merged sibling #2764 ((b)-exclusion of
constant-τ depth-2: my aD5(q=1)=251/48 ≠ lw(4)=26/5, residual 7/240; τ(q=1)=21/8 = their seed).
## Progress 2026-06-25 cont. (PRs #2767, #2768) — converges with Step 1; operator NARROWED to q-difference

Parallel to the #2755 Step-1 probe above (same color Σ, same `λ_SW=X dz`). My two probes:
- **Probe 1 (PR #2767, merged):** τ closed form `(a_D²+a_D⁴)/a_D³ = 3(3q⁴+8q²+3)/(4q(q+1)²)`
  Lean-proved sorry-free (`Lever1TauClosedForm.lean`; #2755 deduped against it, commit 8558da53); color
  `E_q` confirmed (`j(q₀)=129.86`, `j(1)=128`; flagged a −16 bug in `descartes-elliptic-curve.lean::j_invariant`).
- **Probe 2 (PR #2768):** sorry-free `color_power_sums` (color cubic + classical d/dz jets + power sums all
  q-FREE) ⇒ **(b)-EXCLUSION of the classical-jet identification** (q-indep periods ≠ q-dep anchor `(q+1)²/(3q)`).
  **Increment over #2755 Step 1:** Step 1 showed `Res(X dz)=0` at finite branch points (residues only at z=∞);
  Probe 2 adds *why a classical prolongation can't rescue it* — the operator **must be q-DIFFERENCE** (`R(q,x)`).
- **Convergent target (both probes + Step 1):** construct the explicit q-difference `R(q,x)` whose `∮λ_SW^(n)`
  residues reproduce `1, (q+1)²/(3q), Family-A`. Owner-gated keystone; coordinate with the #2755 sibling +
  #2722 (geometric `tr B`) before constructing. No fit; nothing wired.
## Calibration (2026-06-25, PR #2752) — spectral-bridge `→λ₊` is tautological; physical `lw` is super-geometric

Reconciled the two same-day, same-lever results that were in direct tension (no cross-ref between them):
- **#2718 spectral bridge** tabulates `aD_sequence` = the ITERATED fixed-τ recurrence (→λ₊ by
  construction) and asserted it "Empirical (non-tautological) / tests the actual a_D^(n) sequence".
- **#2708** shows the PHYSICAL `a_D^(n)=lw(n−1)` grow **super-geometrically** (ratios 1.34→2.76, past
  λ₊=2.185), diverging from the iterated seq by **≤32% (n=7)**. `5.356 = τ·2.533−1.337` proves the
  bridge seq is the recurrence's own output, not the physical lw.

Independent **float64 q-hook recompute reproduces BOTH probes exactly** (validated vs corpus closed
forms lw(2)=(q+1)²/(3q), lw(3)=Family-A). **(a)-scope re-calibration, NOT a refutation:** qualitative
"extensive not saturating" CONFIRMED + reinforced (super-geometric > geometric); quantitative "λ₊ is
the binding growth rate" is a **seed artifact** — λ₊>1 witnesses only the SEED kernel's extensivity.
Lean `lambdaPlus_gt_one` (τ>2⇒λ₊>1) is a correct **conditional**, unchanged.

Source re-scoped (e748e062): producer comment/caveat/description + Lean docstring; also dropped the
already-retracted magic-A finite-truncation over-claim from the witness caveat. Deferred (full-env,
mpmath absent — same constraint as ct80/#2747): witness JSON regen + producer enhancement to emit lw
beside the iterated seq (reference q-hook algorithm in the audit). Audit:
`docs/audits/2026-06-25-spectral-bridge-tautology-recurrence-vs-lw.md`. No fit; nothing wired; no tier
change. Owner closes (§4a).
## Probe 3 (PR #2774) — PF-monodromy SL₂ synthesis; τ is bar-even in [2]_q

Synthesises #2755 (M=Bring PF operator), #2768 (M must be q-difference), 2026-06-24 integer-trace audit.
Derived, no fit; Lean `QOU/Mass/TauQuantumIntegerForm.lean` sorry-free:
- **M∈SL₂**: transfer `!![τ,−1;1,0]` has det=1 (`transfer_det_one`); λ_± ×=1, +=τ.
- **NEW: τ = 3(3[2]²+2)/(4([2]+2)), [2]=q+q⁻¹** — rational in the quantum integer ALONE ⇒ **bar-even**
  (`tau_quantum_integer_form`, `tau_bar_even`). The Hecke/q-difference fingerprint (a classical-jet trace
  wouldn't collapse onto [2]_q) — falsifiable constraint any candidate `R(q,x)` must satisfy.
- **τ>2 ∀q** (min 21/8 at q=1; [2]≥2 & 9[2]²−8[2]−10>0) ⇒ M hyperbolic, λ₊(q₀)=2.185. **Per the #2752
  calibration above, λ₊ is the SEED kernel's extensivity rate (λ₊>1), NOT the full physical binding rate
  — the physical lw grows super-geometrically PAST λ₊.** Topological PF monodromy at the I₁ fibres
  (squarefree Δ, #2755) is parabolic trace 2.
- **(b)**: τ∉ℤ ⇒ M∉SL₂(ℤ) ⇒ M is NOT the topological monodromy (formalises the 2026-06-24 audit via the
  SL₂ trace). **Indicated:** real/q-difference SL₂(ℝ) operator with bar-even trace τ([2]_q). Construction
  of M still genuine multi-session math — NOT faked. Three probes done; operator now sharply characterised.



**Update 2026-06-27 (PR #2899):** formalize-first probe on the fibre kernel. Tested parameter-free q-involution recurrence S(m)=S(m-1)+[m-1]_q·S(m-2) for S(m)=Σ_{λ⊢m}dim_q(λ) (lw(c)=S(c+1)/(c+1)). q=1 limit IS the involution numbers (skeleton correct). Bare ansatz exact at seed m=2,3, drifts beyond. KEY FINDING: correction D(m) carries a universal (q-1)² prefactor (O(h²), pure fibre effect) and factors cyclotomically (D4 carries Φ3; D7 Φ3²Φ5; D8 Φ3Φ5Φ7) — the Habiro-ring signature. So the lever-1 kernel = q-involution operator dressed by a cyclotomic/Habiro correction = the SAME object class kehn's c_k/Q_β closure needs. Scope: refutes the bare ansatz (a) only, not the q-holonomic class; the D(m) cyclotomic tower is the derived parameter-free constraint. Next: fit D(m) to a single Habiro element, verify held-out m. Audit: docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md

**Update 2026-06-28 (Stage 6) — the correction tower is NOT a single low-order q-hypergeometric element.** Executed the 2026-06-27 stated next step. Tested whether either the additive correction D(m) (nonzero m=4..10) or the q-EGF log-tower L_m (m=1..10) is q-hypergeometric — i.e. its ratio T(m+1)/T(m) is a FIXED rational R(q,q^m) — by order-1 guess-and-verify with held-out-m falsification (the Stages 3-4 methodology, on the correction towers), plus the literal contiguity template r_k=−q^k/[(1−q^{k+1})(1−a q^k)] (one param a). RESULT (negative, sharp): empty train nullspace at every strongly over-determined bidegree up to (q±3,X≤3) for both towers; the one near-square nullspace (L_m, 56u/65c, dim 3) is killed by held-out; the literal template fails held-out for both. So the binding correction tower is NOT a single low-order ₂φ₁ element — sharpens Stages 3-4 (S(m) not q-holonomic) to "even its Habiro correction isn't a single low-order element". (a)-scoped; Habiro class NOT refuted (no proved invariant) — constrains order/shape. Next decidable: cyclotomic-basis (q;q)_n expansion of D(m)/C(z) directly, not a finite q-difference operator (Stages 3-6 show none exists at low order). No fit; nothing wired; no tier change. Probe: computations/substrate/lever1_binding_habiro_single_element_test.py; witness: …-single-element-test.witness.json; audit: docs/audits/2026-06-28-lever1-binding-correction-not-single-qhypergeometric.md

**Update 2026-06-28 (Stage 7) — exact cyclotomic structure of D(m): universal (q−1)² + Φ_d tower + GROWING non-cyclotomic core.** Direct cyclotomic factorization of the correction tower D(m) (clears to a Laurent poly; exact poly-division over ℚ) through m=11. Findings: (1) (q−1)² prefactor universal through m=11 (Stage-1 had m≤8); (2) Φ_d first-appearance rule, clean for odd d: Φ_d first divides D(d+1) (Φ3→m4, Φ5→m6, Φ7→m8, Φ9→m10); (3) NON-CYCLOTOMIC CORE GROWS monotone: deg 0,0,8,10,14,28,34,46 for m=4..11 ⇒ D(m) is NOT a finite cyclotomic object, its essential growing core is the genuine Habiro-ring content (consistent with Stages 3-6: no finite low-order operator). m=4..8 factorizations reproduce the merged 2026-06-27 audit exactly (cross-check). Scope: (q−1)²/Φ_d-rule/core-growth are positive derived facts; "core unbounded" is a bounded-MMAX observation, NOT a proved (b)-exclusion; Habiro class not refuted. Methodology: first classifier silently dropped the core (reported D(6) core 0 vs prior audit's deg-8); caught via corpus cross-check (D4,D5 matched but D6 didn't), fixed to exact poly-division. Next: characterize the growing core R_m (degree law, palindromy). Probe: computations/substrate/lever1_binding_correction_cyclotomic_structure.py; witness: …-cyclotomic-structure.witness.json; audit: docs/audits/2026-06-28-lever1-binding-correction-cyclotomic-core-growth.md

**Update 2026-06-28 (Stage 8) — the core R_m is a tower of pairwise-coprime, irreducible, bar-symmetric, substrate-positive polynomials.** Characterized the non-cyclotomic cores R_m (read from Stage-7 witness; exact in q). Findings on m=6..11: (1) ALL R_m palindromic (bar-symmetric q↔1/q) — extends 2026-06-27's single D(7) observation to all m; binding residue is bar-even; (2) each R_m IRREDUCIBLE over ℚ; (3) cores PAIRWISE COPRIME (no nesting, no fixed growing factor — each order brings a genuinely new irreducible core); (4) R_m(1)>0 and R_m(q0)>0 (the (q−1)² carries all q=1 vanishing). Degree seq 8,10,14,28,34,46 and R(1) seq 28,16,34,1232,1328,9024 — no simple closed form. Net Stages 1-8 picture: S(m)=q-involution skeleton + D(m) = (q−1)²·[Φ_d cyclotomic tower, odd-d rule Φ_d|D(d+1)]·[tower of pairwise-coprime irreducible bar-symmetric substrate-positive cores R_m] — the genuine cyclotomic-completion (Habiro) residue. Scope: palindromy/irreducible/coprime/positive are exact derived facts; "grows unboundedly/not a single finite element" is bounded-MMAX, not proved (b); Habiro class not refuted. Next: (i) identify R_m(1) seq combinatorially; (ii) root distribution on/off unit circle. Probe: computations/substrate/lever1_binding_core_characterization.py; witness: …-core-characterization.witness.json; audit: docs/audits/2026-06-28-lever1-binding-core-bar-symmetric-irreducible.md

**Update 2026-06-28 (Stage 9) — cores are GENERIC bar-symmetric residues; algebraic-characterization line CONCLUDED.** Exact on/off-unit-circle root split (Dickson y=q+1/q reduction + Sturm count_roots, no numerics) + R_m(1) factorization. Findings m=6..11: (1) MIXED root distribution — on-circle 4/8,6/10,6/14,14/28,24/34,32/46 (43–71%), substantial off-circle z↔1/z pairs ⇒ cores are NOT cyclotomic-type, NOT Salem, NOT a recognizable q-special-function; generic bar-even residues; (2) R_m(1)=28,16,34,1232,1328,9024 = 2²·7,2⁴,2·17,2⁴·7·11,2⁴·83,2⁶·3·47 — no combinatorial law. NET (Stages 6-9): the real-q algebraic structure of the binding correction is fully mapped — D(m)=(q−1)²·[Φ_d tower, odd-d rule]·[pairwise-coprime irreducible bar-symmetric generic cores], genuine Habiro/cyclotomic-completion content, NO finite special-function closed form. Further algebraic probing has diminishing returns. The genuine DERIVATION (not description) is the OWNER-GATED λ_SW-holonomy keystone on color E_q (tr B side, #2722) — the algebraic side has now handed it a complete exact parameter-free TARGET. Scope: exact derived facts m=6..11; "no finite closed form" is (a)-cumulative, not proved (b). Probe: computations/substrate/lever1_binding_core_root_distribution.py; witness: …-core-root-distribution.witness.json; audit: docs/audits/2026-06-28-lever1-binding-core-root-distribution.md

## Update 2026-07-12 — headline is STALE: fork RESOLVED; open piece is the super-exp kernel, not "derive τ"

The bean's "frontier = derive τ = tr B geometrically" headline is superseded. `sw_period_growth_probe.py`
(audit) + `prop:sw-period-residue-sum` (Lean `sw_period_eq_residue_sum`) + `Lever1Depth2Exclusion.lean`
already RESOLVE the SW-period prolongation fork: the explicit jet rule `λ_SW^(n)=X^(n)(z)dz` gives a
super-exponential period = lw/#1765 (= Σ_λ dim_q residue sum), so the depth-2 τ-recurrence is an n≤4
EFFECTIVE FIT (Lean (b)-excluded). τ is settled — NOT the live object.

Refined this session (`lever1_sw_period_lw_rate_refine.py`, mpmath-only, audit
`docs/audits/2026-07-12-lever1-sw-period-lw-rate-refine.md`): fork reproduced in-container (lw ratio
1.34→3.10 super-exp vs depth-2 → λ₊≈2.184 constant, split n≥5); NEW quantitative finding — the naive
single-branch rate (n−½)/R OVERSHOOTS the true lw ratio ~2.6× at n=8. The color cubic has 6 branch
points (3 pairs |z|≈0.943/1.0/1.061); the exact rate is the FULL multi-branch residue sum, and lw
tracks the involution-class ~√n (q→1 telephone limit).

**Live open object (sharpened):** the exact super-exponential `a_D^(n)` kernel — the q-Bessel-class /
multi-branch residue sum — NOT the τ derivation (τ is its n≤4 shadow). Coordinated with active keystone
sibling #3662 (W_λ side).

## Update 2026-07-12 (b) — EXACT classical kernel DERIVED + Lean-proved (τ is NOT a fit)

Answering "τ is settled — n≤4 is a fit?": τ is NOT a fit — it is an exact q-rational of the DERIVED
anchors a_D^(n)=lw(n−1) (Lean tauAnchor_closed_form). Only the FIXED-τ depth-2 as an all-n model is
n≤4-effective. The EXACT kernel is now derived at q=1:
- q→1: S(n)=Σf^λ=I(n) (RSK/Burnside = Identity I; telephone A000085), verified exact.
- a_D^(n)=I(n)/n satisfies the EXACT variable-coefficient kernel a_D(n)=((n−1)/n)a_D(n−1)+
  ((n−1)(n−2)/n)a_D(n−2) — Lean-proved sorry-free from the telephone recurrence
  (`QOU/Mass/BindingClassicalKernel.lean`, `aDClassical_variable_coeff`, lean-direct exit 0).
  Super-exp; the fixed-τ depth-2 is its n≤4 shadow.
- q-deformation: S(n)=S(n−1)+[n−1]_q S(n−2)+D(n), c_3=[2]_q exact, Habiro tail grows.

Closes the classical-kernel gap MODULO Identity I (Σf^λ=I(n)) — the SAME keystone P1–P5 RSK input.
So binding + keystone share ONE open input; classical binding kernel otherwise proved. Probe
`lever1_binding_classical_kernel_derive.py`; audit `docs/audits/2026-07-12-lever1-sw-period-lw-rate-refine.md`.

## Update 2026-07-12 (c) — alien-calculus review distilled: Gevrey-1/2 Lean-proved; Borel(1/2) singularity ξ=1/√2; q₀ class change to q-Gevrey; Habiro-basis expansion (PR #3694)

Owner-approved distillation of an external alien-calculus/resurgence dialog into utility
(branch claude/alien-calculus-resurgence-nvvezn). The dialog's Gevrey-1/standard-Borel premise
is REFUTED-and-corrected: (W1) the classical period a_D^(n)=I(n)/n is GEVREY-1/2 — Lean-proved
two-sided sandwich n! ≤ 4ⁿ·I(n)² ≤ 8ⁿ·n! (QOU/Mass/BindingGevreyHalf.lean, sorry-free,
lean-direct exit 0) ⇒ the level-1 Borel plane is entire (no alien derivatives there); level-1/2
is canonical. (W2) Level-1/2 Borel–Padé (n≤60): dominant singularity at ξ = 1/√2 on the positive
real axis, NON-POLAR (accumulating Padé poles — mixed-level transseries signature); at q₀ the
root test rises without plateau under the exact q^{n(n−1)/2} envelope ⇒ the q-deformation CHANGES
the class to q-GEVREY — the alien-calculus geometry at q₀ is an Écalle acceleration chain, not
one Borel plane. The (ρ=1/√2, positive axis, non-polar) datum is the derived analytic TARGET the
open multi-branch super-exp kernel must reproduce (complements the concluded algebraic line,
Stages 6–9 + #3686 not-Salem). (W3) Stage-6 queued next step executed: exact Habiro
(q;q)_k-basis expansion of D(4..9) — round-trip exact, c₀=0 universal, depth k_max ≈ n−1 growing,
height ×8–9/step (basis-side face of no-finite-closed-form). NOT done deliberately: Bridge-eq
Stokes multipliers (no proved resurgence for a non-q-holonomic series), OP/spectral-network
construction (already pruned). Probes: lever1_gevrey_order_pin.py,
lever1_borel_half_singularity_probe.py, lever1_habiro_tail_habiro_basis_expansion.py (+3
witnesses). Audit: docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md.
No fit; nothing wired; scope-(a) + Lean-proved core. Owner closes (§4a).

## Update 2026-07-12 (d) — KERNEL IDENTIFIED at the statistic level: S^bal is the involution
## statistic 2·maj + content∘RSK (exact, n≤8); kernel = insertion recursion, not q-difference

Owner steer "try find kernel". EXACT identification (PR #3694, probe
lever1_kernel_maj_involution_identification.py, all n≤8 bit-exact):
S^bal(n)·q^{n(n−1)/2} = Σ_{w∈Inv(Sₙ)} q^{2·maj(w)+content(λ(w))} — derived from Stanley's
q-hook-maj + RSK/Schützenberger (both verified shape-refined in-container) + the balanced
twist dim_q^bal = q^{content−n(n−1)/2}·fakedeg(q²). DIFFERENT statistic from the pruned
q-Hermite crossing id (2026-06-26). Kernel consequence: fixed-point-insertion weight ratio
is NON-monomial with growing spread (2,4,6,10,15,22 terms, n=3..8) ⇒ maj not Markovian
under RSK insertion ⇒ the kernel is an INSERTION RECURSION at statistic level, not a finite
q-difference operator — explains the (re-verified) non-q-holonomicity + the Habiro tail
combinatorially. Next: statistic-level transfer operator (descent-set refinement under
insertion); promote identity to content block + Lean. No fit; nothing wired.

## Update 2026-07-12 (e) — Habiro cofactors NOT Salem/Lehmer (mpmath cross-check of Stage 9)

Independent mpmath cross-check of Stage 9 (2026-06-28): the n≥6 non-cyclotomic cofactors of the
Habiro tail D(n) are NOT Salem/Lehmer numbers — each has ≥2 off-circle reciprocal pairs (off-pairs
2,2,4,7), not the single pair a Salem polynomial requires. Generic bar-even non-cyclotomic; the n=6
boundary is the onset of non-q-holonomic content, not a distinguished arithmetic class. REPRODUCES
Stage 9 (Dickson/Sturm) via a different method (numerical root isolation), agrees. Magnitudes not
interpreted (numerology guard). Probe `lever1_habiro_cofactor_root_classification.py`; audit
`docs/audits/2026-07-12-lever1-habiro-tail-closed-form.md` (cofactor-roots section).

## Update 2026-07-12 (f) — conj:cyclotomic-boundary-at-keystone (NEW, non-duplicate) + McKay mechanism

Beyond the Stage 7-9 arithmetic (cross-checked by (e)): the NEW content is that the cyclotomic-pure
regime of the Habiro tail is EXACTLY n≤5 = the framework's {calibration orders c=1,2,3 → n=2,3,4} ∪
{S₅ keystone n=5}; first non-cyclotomic content at n=6 = first order beyond cal+keystone.
MECHANISM (ties to merged #3685): at the keystone n=5 the four bwS0 classes of S₅ carry dim_q = the
E₈ McKay marks [1]_q,[4]_q,[5]_q,[5]_q+1 (McKay 2I↔Ê₈, exact no-fit); A₅ = icosahedral = the LAST
McKay-ADE alternating group (A₄↔Ê₆, A₅↔Ê₈, A₆ not binary polyhedral). At n=6 the McKay-mark
structure exits (4/11 single-[m]_q vs 7/7 at n=5) and D(6) leaves the cyclotomic ring. Conjecture
(correlation, causation OPEN): D(n) cyclotomic ⟺ n≤5=keystone order. Two dovetailing candidate
causes: (a) A₅ = last McKay-ADE alt. group (keystone dims = E₈ marks); (b) n=6 = the UNIQUE S_n with
a nontrivial outer automorphism (S₆). Ties binding arithmetic to s5-so3 keystone + Identity-I
(S(n)=Σdim_q=ΣW_λ). Probe `lever1_cyclotomic_boundary_keystone_conjecture.py`; audit
`docs/audits/2026-07-12-lever1-cyclotomic-boundary-keystone-conjecture.md`. Content block:
`conj:cyclotomic-boundary-at-keystone` (mass-theory).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-06-28 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

### Progress (Round 72 — PR litlfred/qou#8311)
- Formalized in PR `litlfred/qou#8311` (`feat/round72-su4gate-markovzd-interface-vassiliev-lever1-43c1`, Commit 1 `120f8595e20646e98de0e5ba129245b973aa1574`, Head `be2282b84c903a928b1e78fc59abcd496c8ceea5`, `scriptHash: 3cfc48bf2b24`).
