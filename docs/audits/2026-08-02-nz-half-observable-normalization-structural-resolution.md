# The NZ-½ observable normalization (qou-yh67): κ_shape vs κ_pot is the full-potential-Φ vs complex-volume-𝔙 object choice — STRUCTURALLY OPEN, physically favouring κ_pot

> **Notation note.** This document predates the 2026-09-05 calibration rename and uses
> the superseded symbols `𝔇_β` (CAL-2) and/or `𝔇_π` (CAL-3). Those are now
> `P_skew^β` (the bar-skew β-channel) and `P_avg^π` (the bar-even π-channel); the
> `𝔇` family is reserved for genuine decay rates (`𝔇_n`, `𝔇_μ`, `𝔇_K` = ℏ/τ).
> The analysis below is left as the record of what was analysed at the time.

**Date:** 2026-08-02 · **Bean:** qou-yh67 · **Axis:** Q_β c₃ bar-odd `S` boost
factor `c = √A` — the single surviving open target of the c₃-odd / Subgoal-2 chain.
**Branch:** `claude/yh67-nz-half-structural-resolution-2026-08-02`.
**Tier:** structural (Lean-exact dictionary) + assessment. **No `c_k` wired;
nothing inverts `Q_β`/CODATA; no `SDeformedVolumeChannel` instance fabricated; no
tier change.**

- **Lean:** [`QOU/QBeta/ObservableComplexVolumeVsFullPotential.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ObservableComplexVolumeVsFullPotential.lean) — the `Φ = 2·𝔙` object dictionary (sorry-free).
- **Companion (#4541):** [`QOU/QBeta/BoostFactorNZNormalization.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BoostFactorNZNormalization.lean) — `κ_shape = 2·κ_pot`, conditional `c = √2`.
- **Sibling (coordinated):** PR #4515 (`qou-iyj5`) — the exact-CS-integral numerics that isolated `c = √A ≈ 1.4305`.

## The question (restated, structural)

The whole c₃-odd chain reduces to one binary (#4541,
[`2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md`](2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md)):
does the bar-odd observable leak `S = Q_β/E₀`, evaluated through the
τ/archimedean functor, carry the coefficient

$$\kappa_{\mathrm{shape}} = \tfrac{\sqrt3}{2}\quad(\Rightarrow A=2,\ c=\sqrt2)
\qquad\text{or}\qquad
\kappa_{\mathrm{pot}} = \tfrac{\sqrt3}{4}\quad(\Rightarrow A=1)\ ?$$

#4541 proved `κ_shape/κ_pot = 2` (the NZ ½) sorry-free AND proved the number is at
the **precision ceiling** (σ_A ≈ 40 % at the ppb q₀-pin; {A=2, Vol(4₁),
q₀+q₀⁻¹, q₀²+q₀⁻²} indistinguishable). **So this cannot be settled numerically —
asserting `S` carries `κ_shape` to match `c=√2` is a fit.** It must be a
structural argument about *which normalization the observable inherits*.

## Contribution 1 — the binary IS a genuine geometric-object choice, not a free convention

The two coefficients are not two "conventions" for one number; they are the
imaginary parts of **two genuinely different objects**, per the A-polynomial
ground-truth audit
([`2026-07-27-nzImVolume-sincos-convention-bug.md`](2026-07-27-nzImVolume-sincos-convention-bug.md),
convention map):

| coefficient | object | definition | NZ ½ |
|---|---|---|---|
| `κ_shape = √3/2` | **full NZ potential** `Φ(u) = ∫₀ᵘ log(−L(t)) dt` | the raw A-polynomial longitude integral | **absent** |
| `κ_pot = √3/4` | **complex volume** `𝔙 = Vol + i·CS = Φ/2` | the deformed Chern–Simons invariant (`∂𝔙/∂u = ½·v`) | **present** |

so `Φ = 2·𝔙` exactly. The [Lean file](../../content/quantum-observable-universe/lean/QOU/QBeta/ObservableComplexVolumeVsFullPotential.lean)
makes this precise and sorry-free:

- `imFullPotential_eq_two_mul_imComplexVolume` — `Im Φ(u) = 2·Im 𝔙(u)` for all `u`;
- `boost_factor_dictionary` — for real `r ≠ 0`, the ratio to the complex-volume
  scale `κ_pot·r²` is **exactly 1** for `𝔙` and **exactly 2** for `Φ`.

**So the opaque `A ∈ {1, 2}` (#4541) is precisely the object binary "observable =
complex volume `𝔙` (A=1) vs full potential `Φ = 2𝔙` (A=2)" — the presence/absence
of the Neumann–Zagier ½.** The `#4541` `κ_shape`/`c=√2` candidate is *exactly* the
statement "the observable is the **full longitude integral** `Φ`, i.e. **twice**
the Chern–Simons invariant `𝔙`."

## Contribution 2 — a LIVE corpus inconsistency: the bar-odd `S` is normalized BOTH ways

The corpus currently carries the SAME bar-odd decay observable with **both**
coefficients, in two production Lean files, unreconciled:

| file | normalization of the bar-odd `S` face | object |
|---|---|---|
| [`QOU/QBeta/ArgUPhaseBranchSelection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ArgUPhaseBranchSelection.lean) | `nzImVolume = (√3/2)·r²·cos(2φ)` = `κ_shape` | **full potential Φ** (states verbatim: "this file keeps the full-potential normalisation √3/2") |
| [`QOU/QBeta/PhiBSArgumentIdentification.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/PhiBSArgumentIdentification.lean) `SDeformedVolumeChannel` | `S = A_ω · Im 𝔙` with `Im 𝔙 = (√3/4)(…)` = `A_ω·κ_pot` | **complex volume 𝔙** (via `FigureEightComplexVolume.imV₄₁`) × Stokes scale `A_ω` |

The mass-face companion
[`QOU/MassTheory/NZBarEvenVolumeFace.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/NZBarEvenVolumeFace.lean)
also uses `√3/2` (full potential). So the S/decay channel is normalized as
`κ_shape` in one place and `κ_pot·A_ω` in another. **This is the qou-yh67 question
sitting live and unreconciled inside the corpus — it is not merely an external
"which constant?" numerology question.** Whichever way qou-yh67 resolves, one of
these two files needs the NZ ½ inserted or removed to agree with the other. (No
edit is made here — the reconciliation is beaned, not silently applied, because
the correct direction depends on the still-open observable identification.)

## Contribution 3 — the physical evidence favours κ_pot (complex volume); κ_shape/c=√2 is the "twice-the-CS-invariant" reading

Which object does the physical decay observable inherit? The weight of structural
evidence points to `κ_pot` (the complex volume `𝔙`), which makes `#4541`'s
`κ_shape`/`c=√2` a within-ceiling coincidence rather than a derivation:

1. **`𝔙 = Φ/2` is THE Chern–Simons invariant.** The parametrized volume conjecture
   (Gukov; H. Murakami; Ohtsuki) produces the complex volume `𝔙` as the
   asymptotic *exponent* of `J_N(4₁; e^{(2πi+u)/N})` — the object with the NZ ½,
   `κ_pot`. The 2026-07-27 A-polynomial audit's **own convention map** blesses
   `V₄₁ = Φ/2` (`κ_pot`) as the "**CORRECT** complex volume" and labels `Φ`
   (`κ_shape`) the "full potential" = twice it. A physical decay energy `Q_β` is
   naturally the Chern–Simons *action* `Im 𝔙`, not `Im Φ = 2·Im 𝔙`.

2. **The keystone channel already uses `κ_pot`.** The `SDeformedVolumeChannel`
   keystone (`conj:binding-qbeta-complex-volume`) identifies `S = A_ω · Im 𝔙` —
   `κ_pot` times the categorical **Stokes scale** `A_ω` (anti-fit target: the
   **integer** `A_ω = 3`, a Donaldson–Thomas / 3d-index count — the G3 keystone,
   [`2026-08-01-fibre-to-observable-bridge-verdict.md`](2026-08-01-fibre-to-observable-bridge-verdict.md)
   §4). In this reading the observed `A ≈ 2` is **not** the NZ ½ dropped; it is
   `A_ω` **attenuated** by the complex-`u`/spin reduction
   (`Im 𝔙 = κ(Re²u − Im²u) ≤ κ·Re²u`, the leading-bound decoupling
   [`FigureEightComplexVolume.imV₄₁_le_cuspModulus_reSq`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean)).
   So `A ≈ 2.054` is a *reduced Stokes 3*, not a clean *dropped ½*.

3. **No mechanism for "twice the CS invariant."** There is no construction in the
   corpus by which a physical observable equals `Im Φ = 2·Im 𝔙` (twice the
   Chern–Simons invariant). Choosing `κ_shape` to obtain `c = √2` therefore has no
   geometric backing — it matches the measured `1.4305` to `2.63 %`, well inside
   the `σ_A ≈ 40 %` ceiling (#4541 Contribution 2), so the match is **coincidence
   within the precision band**, not a derivation. (Exactly the PR #1805
   entropy/precision pattern applied to the boost factor.)

## Contribution 4 — but it is NOT proved-forced: genuinely open

Being disciplined (`conditional-proved ≠ premise-established`; anti-laundering):
the favouring in Contribution 3 is **physical/structural weight, not a proved
invariant**. Two facts keep it open:

- **The channel identity is conjectural.** `S = A_ω·Im 𝔙` (`SDeformedVolumeChannel`)
  is a §3b-cond OPEN class (its `S_eq` field is *assumed*, not derived); `S = Q_β/E₀`
  carries `Q_β = ℏ/𝔇_β = CAL-2`, so *deriving* the identification ⟺ substrate-deriving
  CAL-2 = **Subgoal-2** (open-for-all since 2026-07-11; the anti-fit discipline
  gates *how*, not *whether*).
- **No `u=0` anchor pins the deformation coefficient.** The `u=0` complete-structure
  volume `Vol(4₁) = 2·Cl₂(π/3)` is added the same way to `𝔙` and `Φ` (it is order
  `u⁰`; the ½ acts on the order-`u²` deformation). So the true hyperbolic volume on
  the bar-even face does **not**, by itself, force the deformation-coefficient
  normalization. There is currently no proved invariant that forbids `κ_shape`.

## Verdict — STRUCTURALLY OPEN; re-scoped, and physically pointed at κ_pot

- **Not κ_shape-forced.** No proved invariant forces `κ_shape` (`A=2`, `c=√2`); and
  it would require the observable to be **twice** the Chern–Simons invariant
  (`Φ = 2𝔙`), for which the corpus has no mechanism. Asserting it to hit `c=√2` is
  a fit (the anti-laundering line #4541 already drew).
- **Not κ_pot-forced either.** The complex-volume identification is conjectural
  (CAL-2 / Subgoal-2), and no `u=0` anchor pins the order-`u²` coefficient. So this
  is **not** a Lean-provable exclusion.
- **Genuinely open — with the frontier sharpened.** The qou-yh67 binary is now
  pinned as the concrete geometric-object choice **complex volume `𝔙` (κ_pot, A=1,
  the physical CS invariant) vs full NZ potential `Φ = 2𝔙` (κ_shape, A=2, twice the
  CS invariant)**; the corpus's own inconsistency (`ArgU` `κ_shape` vs keystone
  `κ_pot·A_ω`) is surfaced; and the physical weight favours `κ_pot`, recasting the
  measured `A ≈ 2.054` as a **reduced Stokes `A_ω`** (integer 3, attenuated) rather
  than a **dropped NZ ½**. The precise missing ingredient is stated below.

## The precise missing ingredient (what would close it)

To settle qou-yh67 one must derive **which object the τ/archimedean evaluation of
`Q_β` inherits** — the Chern–Simons action `Im 𝔙` (`κ_pot`, then the residual
`A ≈ 2` is the Stokes scale `A_ω`) or the raw longitude integral `Im Φ` (`κ_shape`,
then `A = 2` is the NZ ½ absent). That is the same categorical Stokes/monodromy
derivation as the G3 keystone integer-`A_ω = 3` identification (bridge-verdict §4):
a derivation of the normalization the fibre→observable functor applies, not a
numerical match. Until then, neither may be wired (canonical-mass guardrail;
Q_β stays c₂-only in production, ≈1279 ppb).

## Anti-laundering

No `c_k` value produced or wired; `S` is never fitted to either coefficient;
nothing inverts `Q_β`/CODATA; no `SDeformedVolumeChannel` instance fabricated;
`c₃` stays a q₀-dependent near-match (SETTLED #1580). The Lean file states only the
unconditional `Φ = 2·𝔙` arithmetic dictionary. Base ring: genuinely archimedean
(`Real.sqrt`, `Complex`) — §7c-correct.

## Coordination

Posted intent on PR #4515 (`qou-iyj5`) naming this parallel structural route (the
`Φ`-vs-`𝔙` object identification + the corpus-inconsistency surfacing) and its
distinct angle vs the exact-CS-integral numerics, per the measured-overlap rule.

## Beans

- **qou-yh67** (this) — re-scoped: the binary is the `Φ`-vs-`𝔙` object choice;
  physical weight favours `κ_pot`; missing ingredient = derive the
  fibre→observable normalization (= the G3 integer-`A_ω` derivation). Stays open.
- **NEW (file)** — reconcile the live corpus inconsistency: `ArgUPhaseBranchSelection`
  / `NZBarEvenVolumeFace` normalize the S/decay face as `κ_shape = √3/2` (full
  potential) while `PhiBSArgumentIdentification`'s keystone uses `κ_pot·A_ω`
  (complex volume × Stokes). One direction is wrong; the fix depends on qou-yh67.

## Cross-references

- [`2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md`](2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md) (#4541) — `κ_shape = 2κ_pot`; the precision ceiling.
- [`2026-07-27-nzImVolume-sincos-convention-bug.md`](2026-07-27-nzImVolume-sincos-convention-bug.md) — A-polynomial convention map: `Φ` (√3/2, full) vs `V₄₁ = Φ/2` (√3/4, complex volume, CORRECT).
- [`2026-08-01-fibre-to-observable-bridge-verdict.md`](2026-08-01-fibre-to-observable-bridge-verdict.md) — the c₃-odd home is the complex volume; `A_ω = 3` integer-Stokes target open.
- [`FigureEightComplexVolume.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean) — `κ_pot`, `imV₄₁`, the leading-bound decoupling.

-- Ref: [manuscript] docs/audits/2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md
