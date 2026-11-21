# SDeformedVolumeChannel — making `V` concrete, and the sign-flip probe

**Date:** 2026-07-26 · **Branch:** `claude/keystone-conj-attack-2026-07-26` ·
**Beans:** milestone `qou-o93x`; T1 `qou-6s8k`; T2 `qou-fook` ·
**Tier:** concrete realization of a §3b abstract field + scope-(a)/(b) probe
(anti-fit / anti-laundering respected).

Attack on the keystone class
`QOU.QBeta.PhiBSArgumentIdentification.SDeformedVolumeChannel S`
(fields `u : ℝ→ℂ`, `V : ℂ→ℂ`, `S_eq : S q₀ = Im (V (u q₀))`), the S-channel of
`conj:binding-qbeta-complex-volume`. Goal: make the abstract deformed-complex-
volume field `V` **concrete** from existing figure-eight geometry, then test
whether the channel identity can reproduce the measured sign-flipping leak.

## T1 — the concrete figure-eight deformed complex volume `V₄₁`

New Lean file
[`QOU/Knot/FigureEightComplexVolume.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean)
(additive; the existing `Knot/*` siblings untouched), lean-verify **exit 0,
sorry-free**.

**The literature object.** The generalized volume conjecture for `4₁` is a
theorem (Gukov 2003; H. Murakami; Ohtsuki 2016; Murakami–Yokota; citable
restatement [`murakami2006`] §1, which states it for `r` near 1, i.e. small `u`):
`J_N(4₁; e^{(2πi+u)/N}) → 𝔙(u) = Vol(u) + i·CS(u)`, `u` = log meridian holonomy.
Its Neumann–Zagier leading term is fixed by the figure-eight **cusp modulus** —
the leading longitude coefficient

    τ = ± i·√3   (PURELY IMAGINARY, ℚ(√−3);  v(u) = τ·u + O(u³)),

recognised exactly from the CCGLS A-polynomial by
[`qbeta_nz_even_series_fourone_probe.py`](../../computations/probes/qbeta_nz_even_series_fourone_probe.py)
(`τ = (0,∓1,1)`, `v₃ = (0,∓1,3)`). With the NZ relation `𝔙′(u) ∝ v(u)` (real
proportionality), the leading complex-volume coefficient `a₂ = 𝔙″(0)/2` is
**purely imaginary**, `a₂ = i·√3/4`, hence

    𝔙₄₁(u) = Vol(4₁) + i·(√3/4)·u² + O(u⁴),   Vol(4₁) = 2·Cl₂(π/3),
    Im 𝔙₄₁(u) = (√3/4)·Re(u²) = (√3/4)·(Re²u − Im²u).

The sole geometric datum is `√3/4` (`√3/2 = sin(π/3) = Im ω`, ω = e^{iπ/3});
**not a fit** — independent of the S targets. The exact object differs by an
**even** `O(u⁴)` tail (`NeumannZagierParity`: classical potential even, no odd
rung), carried as a cited residual; it does not alter the Im-sign structure.

**Proved sorry-free** (`V₄₁ : ℂ → ℂ` realizes the abstract `V` field):

| lemma | content |
|---|---|
| `V₄₁_zero_re` | `Re 𝔙₄₁(0) = 2·Cl₂(π/3)` (EXACT — a₂ purely imaginary, no residual) |
| `V₄₁_zero_im` | `Im 𝔙₄₁(0) = 0` (CS = 0, amphichiral) |
| `V₄₁_even` | `𝔙₄₁(−u) = 𝔙₄₁(u)` (Neumann–Zagier evenness) |
| `nzPoly₄₁_no_u3` | no u³ rung, via the proved `NeumannZagierParity.no_cubic_rung` on the concrete potential (a genuine `NeumannZagierEvenPotential ℝ` instance) |
| `imV₄₁` | `Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u)` — harmonic quadratic form |
| `imV₄₁_pos_iff` / `imV₄₁_neg_iff` | sign of the CS part = sign of `Re²u − Im²u` |
| `imV₄₁_zero_on_diagonal` | Im 𝔙₄₁ vanishes on the DIAGONALS `|Re u|=|Im u|`, not on the axes |
| `signflip_forces_diagonal_cross` | the T2 invariant (below) |
| `f3_re_linear_same_sign` | the #3773 F3 survivor refuted (below) |

**Open surface reduced:** the class goes from `{u, V, S_eq}` to `{u, S_eq}`.
No `SDeformedVolumeChannel` instance is fabricated — `u(q₀)` and `S_eq` stay
open (anti-laundering).

## T2 — sign-flip probe: verdict **structural-partial**

Probe
[`sdeformed_channel_signflip_probe.py`](../../computations/probes/sdeformed_channel_signflip_probe.py)
(mpmath, exit 0, not wired to production), witness
`sdeformed-channel-signflip.witness.json`. Target: the measured bar-odd leak
`S(muon) ≈ +0.00968298 > 0 > S(proton) ≈ −0.03945936`.

### The correction (why F3 no longer survives)

The #3773 constraint probe
[`qbeta_udeform_map_constraint_probe.py`](../../computations/qbeta/qbeta_udeform_map_constraint_probe.py)
and the gluing-newton probe both inverted the **heuristic** leading form
`Im 𝔙 ≈ √3·Re(u)·Im(u)` (= `(√3/2)Im(u²)`). That corresponds to a **real**
`a₂` — which **contradicts** the rigorous `τ = −i√3`. Verified numerically here
by integrating the closed-form geometric-branch longitude
`𝔙(u) = Vol(4₁) − ½∫₀ᵘ v`: the true leading form is `κ(Re²u − Im²u)` (matches to
`O(u⁴)`, `7e-6` at `|u|=0.1`), vanishing on the **diagonals** `|Re u|=|Im u|`
(`7e-6` at φ=π/4), **not** the axes as the heuristic predicts.

Against the corrected form the #3773-"surviving" family **F3** (one component
of `u` linear-through-zero at `q*`, the other anchor-constant `c₀`) gives

    S = κ·((k·d)² − c₀²),   d = q − q*,

which is **even in d** and, near `q*` where `|k·d| ≪ |c₀|` (probe: `|k·d_muon| =
0.0056`, `|k·d_proton| = 0.023`, vs `c₀ ~ O(0.1)`), has the **same sign** at
both anchors (both `≈ −κ c₀² < 0`). **F3 cannot sign-flip** — its survival in
#3773 was an artefact of the heuristic `√3·Re·Im` form. Lean:
`f3_re_linear_same_sign`.

### The channel is not excluded — it needs a diagonal crossing

`Im 𝔙₄₁ = κ(Re²u − Im²u)` **does** change sign — when `u` crosses a diagonal
`|Re u| = |Im u|`. Inverting the anchors:

    (Re²u − Im²u)_muon   = S/κ ≈ +0.0224   (|Re u| > |Im u|),
    (Re²u − Im²u)_proton = S/κ ≈ −0.0911   (|Re u| < |Im u|).

Opposite signs ⇒ any `u(q₀)` realizing the measured flip **must cross the
diagonal** `|Re u| = |Im u|` between muon and proton (Lean:
`signflip_forces_diagonal_cross`). This is a **sharper** open constraint than
F3 ("one-linear-one-const") — but `u(q₀)` itself remains **open**.

### Classification

- **`structural-partial`.** Making `V₄₁` concrete makes the channel testable and
  reduces the class's open surface, but does not determine `u(q₀)`.
- **scope-(b) sub-result:** the #3773 F3 family is **refuted** against the
  corrected form. Invariant: `a₂` purely imaginary (`τ = −i√3`, A-polynomial) ⇒
  `Im 𝔙₄₁ = κ(Re²u − Im²u)` is an even quadratic form vanishing on the diagonals,
  so an F3-linear component crossing zero keeps both anchors on the same side of
  the diagonal ⇒ same sign. Lean-proved (`f3_re_linear_same_sign`,
  `imV₄₁_neg_iff`).
- **channel NOT scope-(b) excluded:** `S = Im 𝔙₄₁(u(q₀))` remains viable with a
  diagonal-crossing `u(q₀)`.

## Honesty ledger

- **Anti-fit:** `V₄₁` is the literature NZ leading form; its only constant `√3/4`
  is the figure-eight cusp modulus, geometric, independent of S.
- **Anti-laundering:** no keystone instance fabricated; `u(q₀)`, `S_eq` open; no
  `c_k` produced or wired; probe not in the production consumer set.
- **Honest negative surfaced (not buried):** the heuristic `√3·Re·Im` form used
  by two prior probes is corrected here; F3's survival is retracted. The prior
  probes' witnesses are left in place (their *measurement* content stands); this
  audit records the corrected Im-structure. A follow-up may re-scope the F3
  entry in `qbeta_udeform_map_constraint_probe.py` to the diagonal-crossing
  constraint.

## Follow-up: probe corrections landed + contradicted Lean companion (2026-07-26)

The two prior probes that used the wrong `√3·Re·Im` heuristic form were
rewritten to the corrected `(√3/4)(Re²u−Im²u)` form (both run exit 0):

- [`qbeta_udeform_map_constraint_probe.py`](../../computations/qbeta/qbeta_udeform_map_constraint_probe.py)
  — inversion target now `(Re²u−Im²u) = 4S/√3`; **F1, F2, F3 all REFUTED**
  under the corrected form; the surviving admissible constraint is the
  **diagonal crossing** (`(Re²−Im²) = +0.0224` muon, `−0.0911` proton). F2's old
  `S∝d³` was a wrong-form artefact (corrected: `S∝d²`, even).
- [`qbeta_c3_barodd_gluing_newton_solve.py`](../../computations/qbeta/qbeta_c3_barodd_gluing_newton_solve.py)
  — `cs_lead` fixed from `(√3/2)|u|²sin2φ` to `(√3/4)(Re²u−Im²u) =
  (√3/4)|u|²cos2φ`; the Vol Newton solve is unchanged (both assertions still
  pass); the displayed leading Im now vanishes at `arg u = π/4` and is negative
  beyond, matching `imV₄₁`.

**F3 refinement (sharper than the "same sign" statement in §T2 above).** Re-
evaluating the #3773 F3 survivor *faithfully* — respecting the OLD-form product
slope `Re·c₀ = S/√3` (so `Re = S/(√3·c₀)`, `c₀` free) rather than fixing the
Re-slope — shows the "same sign at both anchors" claim holds only for large
`c₀` (`c₀ > c_pr*`). The fully honest statement: reproducing the **measured**
`S(muon) > 0 > S(proton)` needs `c₀ < c_mu* = (S_mu/√3)^½ ≈ 0.0748` **and**
`c₀ > c_pr* = (|S_pr|/√3)^½ ≈ 0.1509` simultaneously; since `c_pr* > c_mu*`
these are **incompatible**, so **no `c₀ > 0` reproduces the measured flip**. (A
*wrong-direction* flip `S(muon) < 0 < S(proton)` opens in the window
`c_mu* < c₀ < c_pr*`, never the measured one.) F3 is still REFUTED — via
incompatibility, not uniform same-sign. This does not change any T2/Lean verdict;
it sharpens the argument.

**Contradicted Lean companion — flagged for follow-up (NOT edited here).** The
laws in
[`QOU/QBeta/UDeformFamilyPruning.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/UDeformFamilyPruning.lean)
are built on the wrong leading form `nzLeading x y = √3·x·y` (= `√3·Re·Im`) and
are contradicted by the correction:

| Lean decl | status under the correction |
|---|---|
| `nzLeading` (`= √3·x·y`) | **wrong form** — should encode `(√3/4)(x²−y²)` |
| `cubic_ratio_law` (F2 obeys an `S∝d³` cross-anchor law) | **contradicted** — corrected F2 is `S∝d²`, no cubic law |
| `linear_family_eq` / `linear_family_sign_flip` / `hasDerivAt_linear_family` (F3 sign-flips, survives) | **contradicted** — corrected F3 is even in `d` and cannot produce the measured flip |
| `fixed_phase_product_nonneg` / `fixed_phase_family_excluded` (F1 refuted) | conclusion (F1 refuted) still correct, but **proved about the wrong form** |

Recommended follow-up (separate PR, not this one): rewrite `nzLeading` to the
harmonic quadratic form and re-derive the family laws (F1/F2/F3 all become
even-in-`d` sign exclusions; the surviving object is the diagonal-crossing law
already proved in `FigureEightComplexVolume.lean` — `signflip_forces_diagonal_cross`,
`f3_re_linear_same_sign`). No Lean was edited in the probe-correction commits.

**RESOLVED (2026-07-26, PR #4384).** `UDeformFamilyPruning.lean` was rewritten
exactly as recommended: it now feeds the family components through the concrete
`V₄₁` (`familyIm x y = (V₄₁ ⟨x,y⟩).im = (√3/4)(x²−y²)` via `imV₄₁`), and the wrong
`nzLeading = √3·x·y` def + the contradicted `cubic_ratio_law` /
`linear_family_eq` / `linear_family_sign_flip` / `hasDerivAt_linear_family` are
gone. F1/F2/F3 are all refuted as even-in-`d` sign exclusions
(`fixed_phase_family_excluded`, `phase_crossing_family_excluded`,
`transverse_const_family_excluded`), and the survivor is
`signflip_requires_diagonal_cross` (reusing `signflip_forces_diagonal_cross`).
lean-verify exit 0, sorry-free; no removed decl is referenced elsewhere. The
`binding-qbeta-complex-volume.md` prose was corrected in the same PR.

## Cross-references
- Coordination: [`keystone-sdeformedvolume-channel-attack.md`](../coordination/keystone-sdeformedvolume-channel-attack.md)
- Keystone Lean: [`PhiBSArgumentIdentification.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/PhiBSArgumentIdentification.lean)
- Parity prune: [`NeumannZagierParity.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/NeumannZagierParity.lean)
- Prior conditional audit: [`2026-07-11-complex-volume-conditional-mass-binding.md`](2026-07-11-complex-volume-conditional-mass-binding.md)
- AGENTS.md §"Before declaring refuted"; §"Axiomatization is NOT a Proof"; §3b.
