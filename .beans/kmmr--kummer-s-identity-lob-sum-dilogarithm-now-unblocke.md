---
# kmmr
title: Kummer's identity (Λ-sum = dilogarithm form) — now UNBLOCKED by cLiTwoExt
status: completed
type: task
priority: high
tags:
    - lean
    - dilogarithm
    - hyperbolic-volume
    - stale-claim-corrected
created_at: 2026-08-09T20:30:00Z
updated_at: 2026-08-14T21:02:10Z
---

## The claim that was stale

`QOU/Archimedean/BlochWignerLobachevsky.lean` defines

    BlochWigner_lob z := Λ(arg z) + Λ(arg(1/(1−z))) + Λ(arg(1 − 1/z))

and said of the dilogarithm form `D(z) = Im Li₂(z) + log|z|·arg(1−z)` that the
two agreeing is **Kummer's identity**, "a theorem, not a definitional
unfolding" — and that it "**cannot currently be proved in this corpus**: Mathlib
has no polylogarithm or dilogarithm at all (checked 2026-08-08)".

The Mathlib half remains true. The conclusion does not: **the corpus has its own
dilogarithm**, `QOU.MathlibExt.cLiTwoExt`, with reflection, inversion and the
five-term identity all proved this session. Corrected in place 2026-08-09.

## Why it matters

That file spells out the factorisation: the target `Vol = Λ-sum` splits as
(geometric) `Vol = D` ∘ (analytic) `D = Λ-sum`. **Kummer is the analytic
factor**, and it is the bridge between the two halves of this whole lane:

* the Λ-sum side — angles, `Cl₂`, Rivin concavity, `qou-rvnc`/`qou-mlgp`;
* the dilogarithm side — `cLiTwoExt`, the pentagon, the proved 5₂ sum rule.

Proving it would let dilogarithm facts be transported onto `BlochWigner_lob`,
which the file currently and correctly **forbids** ("do not transport
dilogarithm facts onto this symbol … the name is shared; the objects are so far
only numerically observed to agree").

## Numerical status — exact, checked 2026-08-09 at 40 dps

Against this file's own `Lob`/`tetAngle` definitions, `Λ-sum` vs
`Im Li₂(z) + log|z|·arg(1−z)`, residual `≤ 1.1e-41` (the precision floor) at
`0.3+0.7i`, `1.5+0.8i`, `−0.4+1.2i`, `0.2+2.5i`, and at the **5₂ shape**
`y₁ = 0.78492+1.30714i`. The three `tetAngle`s sum to `π` to `4.6e-41` at each.

And at `y₁`: `3·BlochWigner_lob(y₁) = 2.828122088330783162763899…`, which is
`Vol(5₂)` to every digit the corpus records. So the Λ-sum route *does* reach the
volume — the gap is a proof, not a fact.

## Suggested attack

Both sides are real-valued on the upper half-plane, so the holomorphic
"derivative vanishes on a preconnected open set" trick used all through
`FiveTwoComplexPentagon` does **not** apply directly. Options:

1. Differentiate along the two real directions and match, then pin the constant
   on a ray where both sides are computable (`Lob_zero`/`Lob_pi` and
   `cLiTwoExt` on `(0,1)` give candidate basepoints).
2. Go through `Cl₂`'s Fourier series and `Im Li₂(e^{iθ}) = Cl₂(θ)` — the corpus
   already has `hasDerivAt_Cl_2_series` and `clausen_eq_series`, and
   `QOU/Knot/Clausen.lean` notes `Cl₂′` is *simultaneously* the derivative of
   the dilog-saddle potential `V(θ) = Im Li₂(e^{iθ})`. That coincidence is
   probably the cheapest entry point.

⚠ Do not assume the identity extends off the upper half-plane; `BlochWigner_lob`
is built from `arg`s and the corpus already proves it vanishes on real shapes in
`(0,1)`, which is a branch statement.

## Not this bean

The **geometric** factor `Vol = D` — that a specific triangulation's Λ-sum is
the hyperbolic volume of a specific knot complement. That is `qou-m015` +
`qou-krvm` territory and is not closed by Kummer.

---
**2026-08-09 — first increment landed: Kummer on `|z| = 1`.**

`QOU/Knot/KummerUnitCircle.lean`, sorry-free, standard axioms, `lake build`
exit 0 / 3091 jobs. Probe `qbeta_5two_route72_kummer_unit_circle_probe.py`
(60 dps, 4 gates, all passing); float64 guard clean, run in place.

`blochWigner_lob_exp` — for `θ ∈ (0, π)`,
`BlochWigner_lob(e^{iθ}) = Cl₂(θ)`.

**Why the unit circle is the cheap case, and it is a real reason not an
accident.** There the ideal tetrahedron is **isosceles**: the three angles of
`e^{iθ}` are `(θ, (π−θ)/2, (π−θ)/2)`. So the Λ-sum is `Λ(θ) + 2Λ((π−θ)/2)`,
which is `Cl₂(θ)` by the **duplication formula the corpus already had**
(`Cl_2_duplication`). On `|z| = 1`, Kummer *is* Clausen duplication — three
lines once the angles are computed.

The work was the angle computation, not the identity: `one_sub_exp_mul_I`
factors `1 − e^{iθ} = 2 sin(θ/2)·e^{i(θ−π)/2}`, which pins
`arg(1−e^{iθ}) = (θ−π)/2` with no branch ambiguity, and the other two angles
follow by `Complex.arg_inv` / `Complex.arg_conj` (both need `arg ≠ π`, supplied).

**Two boundaries, both gated so they cannot be blurred:**

* **G3** — the *dilogarithm half* (`Im Li₂(e^{iθ}) = Cl₂(θ)`, hence Λ-sum = the
  Bloch–Wigner dilogarithm form) is numerically true to `1e-45` but is **NOT
  proved** for `cLiTwoExt`. The Lean theorem deliberately states its conclusion
  in terms of `Cl₂` alone and makes **no** dilogarithm claim. Until that half
  lands, `BlochWignerLobachevsky`'s prohibition on transporting dilogarithm
  facts onto the symbol still stands — this increment does not lift it.
* **G4** — this does **not** reach `Vol(5₂)`. `|y₁| = 1.5236`, off the unit
  circle; its tetrahedron is not isosceles and `log|z| ≠ 0`.

**Still open, in order:** (a) `Im Li₂(e^{iθ}) = Cl₂(θ)` for `cLiTwoExt` — the
cheaper of the two, and `QOU/Knot/Clausen.lean` already notes `Cl₂′` is
*simultaneously* the derivative of `V(θ) = Im Li₂(e^{iθ})`, which is the entry
point; (b) general `z`, which needs the two-variable argument
`dD = log|z| d arg(1−z) − log|1−z| d arg z` against `dΛ(θ) = −log|2 sin θ| dθ`.
Only (b) reaches the 5₂ shape.

---
**2026-08-09 — second increment: the dilogarithm half, so BOTH halves now meet
on `|z| = 1`.**

`QOU/Knot/KummerDilogHalf.lean`, sorry-free, standard axioms, `lake build`
exit 0 / 3239 jobs with the `.olean` deleted first, zero `sorry`.

* `im_cLiTwoExt_exp` — `Im cLiTwoExt(e^{iθ}) = Cl₂(θ)` on `(0, 2π)`.
* `kummer_unit_circle` — the two halves combined:
  `BlochWigner_lob(e^{iθ}) = Im cLiTwoExt(e^{iθ}) + log‖e^{iθ}‖·arg(1−e^{iθ})`.

**The proof is the lane's standard move: same derivative, pin the constant.**
Along `z = e^{iθ}`, `dz/dθ = iz`, so `hasDerivAt_cLiTwoExt'` gives
`d/dθ cLiTwoExt(e^{iθ}) = −(log(1−z)/z)·(iz) = −i·log(1−z)`, whose imaginary
part is `−log‖1−z‖ = −log(2 sin(θ/2))` — *verbatim* `Cl₂′(θ)`
(`hasDerivAt_Cl_2_series`). Constant on `(0,2π)`, and `θ = π` kills it:
`cLiTwoExt(−1) = −π²/12` is **real** so its imaginary part is `0`, and
`Cl₂(π) = 0`.

**A domain fact that made it cheap, and is worth remembering.** The *whole*
punctured circle lies in `notCut = {w | w.im ≠ 0 ∨ w.re < 1}` — not by the
obvious `sin θ ≠ 0` argument (which fails at `θ = π`), but because
`cos θ = 1 − 2sin²(θ/2) < 1` on all of `(0, 2π)`. So the `re < 1` disjunct
covers the entire interval and **no case split is needed at all**. That also
keeps `θ = π` inside the domain, which is exactly the basepoint the proof needs.

**Stale claims corrected in the same commit** — the previous increment's own:
* Route 72's G3 asserted the dilogarithm half was "NOT proved in Lean for the
  corpus's cLiTwoExt", with `"proved_in_lean_for_cLiTwoExt": False`. Now false;
  gate text, flag, module docstring and VERDICT string all corrected, kept as
  the numerical control.
* `KummerUnitCircle.lean`'s header listed that half under "WHAT IS NOT PROVED".

**Still open, and this is the one that matters:** Kummer for **general `z`**.
Off the unit circle the tetrahedron is not isosceles and `log|z| ≠ 0`; it needs
the two-variable argument `dD = log|z| d arg(1−z) − log|1−z| d arg z` against
`dΛ(θ) = −log|2 sin θ| dθ`. **`|y₁| = 1.5236`, so nothing here reaches
`Vol(5₂)`.** Only the general case would.

---
**2026-08-09 — third increment: the ideal-tetrahedron LAW OF SINES, and the
radial reduction it unlocks.**

`QOU/Knot/IdealTetLawOfSines.lean`, sorry-free, standard axioms, build exit 0 /
3091 jobs, zero `sorry`. Probe `qbeta_5two_route73_law_of_sines_radial_probe.py`
(60 dps, 4 gates, all passing); guard clean, in place.

    ‖z‖ = sin θ₂ / sin θ₃        (Im z > 0)

with `θ₂ = arg(1/(1−z))`, `θ₃ = arg(1 − 1/z)`. Also `sin_tetAngle₂/₃` (the two
sines in closed form), their positivity, and `log_sin_sub_log_sin` —
`log(2 sin θ₃) − log(2 sin θ₂) = −log‖z‖`, which is the shape the Λ-derivative
actually produces.

**This is the ideal-tetrahedron analogue of the Euclidean law of sines**: the
*modulus* of the shape parameter is a ratio of sines of opposite angles, exactly
as a side length is in a triangle. It is what ties the ANGLE description of a
tetrahedron to the SHAPE-PARAMETER description.

**Why it matters here — it collapses two variables to one.** General-`z` Kummer
looks like it needs the two-variable argument
`dD = log|z| d arg(1−z) − log|1−z| d arg z`. It does not. Fix `arg z` and vary
`r = |z|` along a ray:

* `θ₁ = arg z` is **constant**, so `Λ(θ₁)` contributes nothing;
* `θ₁+θ₂+θ₃ = π` (`tetAngles_sum_eq_pi`) forces `dθ₃ = −dθ₂`;
* so `d/dr (Λ(θ₂)+Λ(θ₃)) = log(sin θ₃/sin θ₂)·dθ₂/dr`;
* while `d/dr` of the dilogarithm side is `−log r · dθ₂/dr`.

These agree **iff** `r = sin θ₂/sin θ₃` — the law of sines. And the basepoint
`r = 1` is `KummerDilogHalf.kummer_unit_circle`, already proved. So general-`z`
Kummer becomes the same "same derivative, pin the constant" shape as everything
else in this lane.

The proof of the law of sines itself is elementary: `Complex.sin_arg` is
*unconditional* in Mathlib, giving `sin θ₂ = Im z/‖1−z‖` and
`sin θ₃ = Im z/(‖z‖·‖1−z‖)` directly; the ratio is `‖z‖` on the nose.

**⚠ NOT yet proved: general-`z` Kummer.** The radial argument is planned and
numerically confirmed (Route 73 G3: the Λ−dilog difference is constant, and
zero, along every ray tested) but **not assembled in Lean**. G3 is evidence the
plan works, *not* a proof. What remains is the differentiability of `θ₂` in `r`
and the chain-rule assembly — mechanical, but real. `Vol(5₂)` needs that plus
the geometric factor and is untouched.

---
**2026-08-09 — ✅ CLOSED. KUMMER'S IDENTITY IS PROVED FOR GENERAL `z`.**

`QOU/Knot/KummerRadial.lean` — `kummer`, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`, `lake build` exit 0 / 3242 jobs with
all five `.olean`s deleted first, zero `sorry`:

    Im z > 0  ⟹  BlochWigner_lob z = Im (cLiTwoExt z) + log‖z‖ · arg(1 − z)

**The route was NOT the two-variable argument this bean predicted.** The bean
said general `z` "needs the two-variable argument
`dD = log|z| d arg(1−z) − log|1−z| d arg z`". It does not. Fixing `arg z` and
moving radially collapses it to **one** variable:

* `θ₁ = arg z` is constant along the ray, so `Λ(θ₁)` drops out;
* `θ₁+θ₂+θ₃ = π` forces `dθ₃ = −dθ₂`;
* the two `Λ′` terms collapse via the **law of sines** to `−log r · θ₂′`;
* the dilogarithm side moves at `−log r · θ₂′` too (`Im cLiTwoExt` at `θ₂/r`,
  the `log r · arg(1−z)` term at `−θ₂/r − log r·θ₂′`);
* so the defect is constant on `(0,∞)`, and `r = 1` kills it —
  `kummer_unit_circle`, the earlier increment, is the basepoint.

Note the shape: **the `|z| = 1` case is an INPUT to the general case, not a
special case of it.** The increments compose, they do not supersede.

Chain, all sorry-free: `KummerUnitCircle` (Λ-side on `|z|=1` = Clausen
duplication) → `KummerDilogHalf` (`cLiTwoExt` side there) → `IdealTetLawOfSines`
(`‖z‖ = sin θ₂/sin θ₃`) → `KummerRadial` (the reduction).

**THE PROHIBITION IS LIFTED.** `BlochWignerLobachevsky.lean` forbade
transporting dilogarithm facts onto `BlochWigner_lob` "without first proving
Kummer's identity". That condition is met; the note is rewritten in place, and
the `qou-idvt` T2 / `qou-5gai` H4 factorisation `Vol = D` ∘ `D = Λ-sum` now has
its **analytic factor closed**.

**Stale claims corrected in the same commit — all of them mine, from the three
previous increments:** Route 73 G4 (`kummer_general_z_proved: False`), Route 72's
`not_proved` list, and the "WHAT IS NOT PROVED" sections of
`KummerUnitCircle.lean`, `KummerDilogHalf.lean`, `IdealTetLawOfSines.lean`.

**⚠ STILL NOT `Vol(5₂)`.** Kummer is the *analytic* factor. The **geometric**
factor — that a particular triangulation's Λ-sum is the hyperbolic volume of a
particular knot complement — is `qou-m015`/`qou-krvm` and is untouched. Nothing
in this bean computes a volume.

**Also recorded: a naming collision.** QOU has two unrelated "Kummer"s — this
dilogarithm identity, and the Kummer sequence/filtration/tower of the Yekutieli
obstruction story (`κₙ ∈ H²(𝒮,ℬ)`, `conj:q-gl-kummer-filtration`,
`rem:hochschild-kummer-connection`), whose "**central element**" language is the
crossed-module boundary `∂ : 𝒪_M^× → SU_{qₙ}(2)`. Disambiguation notes added to
both Kummer modules. The two stories touch only through `Vol(5₂)`, via
`yekutieli-transcendence-shadow.md`'s conjecture that `Vol(4₁)`, `Vol(5₂)`,
`Vol(ℬ₃)` are algebraically independent — and **the proved sum rule does not
threaten it**, because `D` cancels on the Galois orbit the sum rule sums over.

---
**2026-08-09 — first consumer of Kummer: `VOL_5_2` as an exact constant.**

`QOU/Knot/FiveTwoVolumeConstant.lean`, sorry-free, standard axioms, build exit 0
/ 3251 jobs, zero `sorry`.

**Why it was needed.** `FigureEightVolumeLiterature.lean` records that the 4₁
volume conjecture was **unstateable** while `VOL_4_1` was "a truncated rational
decimal ≈ 1e-30 away from `2·Cl₂(π/3)`, making the statement literally false";
bean `qou-yf47` repaired it by *defining* `VOL_4_1 := 2·Cl₂(π/3)`. **5₂ had no
such constant** — only a SnapPy decimal, Lean decimal literals
(`MassDerivation.vol_figure_eight`), and the outright placeholder
`HyperbolicVolume : Knot → ℝ := fun k => 0 * (k : ℝ)`
(`AppendixSurreals/Conjectures.lean`). Any exact 5₂ volume statement written
against those is false or vacuous, for exactly the reason `qou-yf47` found.

Now: `fiveTwoShape` (= `y₁`, from `SaddleRoots.ofRealRoot` on the IVT real root),
`VOL_5_2 := 3 · BlochWigner_lob fiveTwoShape`, with `fiveTwoShape_cubic`,
`fiveTwoShape_im_pos`, `fiveTwoShape_angles_sum`, `fiveTwoShape_law_of_sines`.

**The payoff — `VOL_5_2_eq_dilog`:**

    VOL_5_2 = 3 · ( Im (cLiTwoExt y₁) + log‖y₁‖ · arg(1 − y₁) )

So the constant has an **angle** form and a **dilogarithm** form, proved equal.
**Before Kummer this equation could not have been written down** — it is exactly
the transport `BlochWignerLobachevsky.lean` forbade. That prohibition being
lifted is what makes it a one-line consequence.

**⚠ NOT proved: that `VOL_5_2` is the hyperbolic volume of `S³ ∖ 5₂`.** That is
the *geometric* factor, cited to the literature exactly as `VOL_4_1` cites
Thurston/Milnor. And it is **not currently a statable Lean theorem at all**:
Mathlib has no hyperbolic 3-manifolds and QOU defines no volume functor — the
only "volume" objects in Lean are decimal literals and a placeholder returning
`0`. That is a sharper obstruction than "unproved", and it is what
`qou-m015`/`qou-krvm` would have to change.

Numerically `VOL_5_2 = 2.82812208833078316276389880927663494277…`, matching the
corpus's SnapPy HP 50-dps constant to full recorded precision (Route 71,
residual `4.9e-50`). That is a **control on the definition**, not a proof of the
geometric identification.


---
**2026-08-14 — status corrected `todo` → `completed` (stale frontmatter).**

The body already records the closure: **Kummer's identity is PROVED for
general `z`** (`QOU/Knot/KummerRadial.lean` `kummer`, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`, 2026-08-09), via the radial reduction
(law of sines) with `kummer_unit_circle` as basepoint. The prohibition on
transporting dilogarithm facts onto `BlochWigner_lob` is lifted, and the first
consumer `FiveTwoVolumeConstant.lean` (`VOL_5_2_eq_dilog`) has landed. Only the
frontmatter `status: todo` was stale. NOT this bean (untouched): the geometric
factor `Vol = D` (`qou-m015`/`qou-krvm`).

## 2026-08-31 — the half-plane restriction is now the last thing gating `hbw`. And a roast of my own report of it.

`FiveTwoOhtsukiBridge.volume_conjecture_five_two_wired` (landed sorry-free today)
carries `hbw : ∀ z, z.im ≠ 0 → BlochWigner_lob z = (Li₂ z).im + arg(1−z)·log‖z‖`.
`KummerRadial.kummer` proves it only for `Im z > 0`; the bridge's proof needs it at
`1/y₀`, `1/x₀`, `1/(x₀y₀)`, **all in the lower half-plane** (measured: `Im` =
−1.307, −0.745, −0.745). So extending across the real axis is the last gate.

### Roast of three claims I made when relaying this

**1. "takes no free identity hypotheses at all — only … that `Li₂` is a
dilogarithm." FALSE, and it understates what is assumed.** The signature carries
three explicit hypotheses (`hbw`, `hone`, `hζ`), and `hbw` is not a definitional
property of a dilogarithm — it is the **full Bloch–Wigner identity**, universally
quantified over the punctured plane, tying the corpus's *Lobachevsky-built*
`BlochWigner_lob` to `Im Li₂` with a specific `arg`–`log` normalisation. A function
can satisfy Kummer and not satisfy that. The honest phrasing is "one substantive
identity hypothesis, proved on half its domain".

**2. "it would let the 5₂ bridge be instantiated at a real dilogarithm." OVERSTATED.**
Discharging `hbw` removes a hypothesis; it does not instantiate anything. The theorem
still requires instances of `OhtsukiAsymptotic` and `FiveTwoTriangulation`, and
**neither has one** — deliberately, per §3b-tax. "Instantiated" implies applicable;
it stays gated on two axioms either way.

**3. "it looks short … conjugation commutes with all three Möbius maps, and
`BlochWigner_lob_conj` already proves that on the Λ side." Right conclusion, wrong
warrant — and my own objection to it was also wrong.** The Λ side has no branch cut,
so citing it as evidence for the `Li₂` side was citing the easy case for the hard
one. I then expected the hard case to bite, because `Li₂`'s cut `[1,∞)` lies **on**
the axis one reflects across. Measured, it does not bite:

    Li₂(z̄) = conj(Li₂(z))    exact (0.0 at 30 dps) at 1/y₀, 1/x₀, 1/(x₀y₀),
                             and still exact 1e-7 from the cut at Re = 5.

`Li₂` is discontinuous *across* the cut (jump 4.355 at `Re = 2`), but that never
obstructs the reflection, because `hbw`'s domain `z.im ≠ 0` excludes the real axis
entirely. So "short" survives — for a reason neither the original claim nor my
objection had established.

**Net:** the estimate stands, the justification for it did not, and the two
surrounding claims were wrong in the direction of flattering the result. The three
arguments also sit 1.15–2.02 away from the cut, so even a pointwise argument at
those three values would do — the ∀-quantified form is stronger than the bridge needs.

## 2026-08-31 (later) — CLOSED. The half-plane gate is gone, and so is the `Li₂` parameter.

Two changes, both sorry-free (`#print axioms` → `[propext, Classical.choice,
Quot.sound]` on every declaration named below).

### 1. `hbw` weakened from a half plane to five named points

`FiveTwoOhtsukiBridge` now takes `IsKummerAtOhtsukiArgs Li₂ y` — a five-field
structure, one Kummer instance per non-unit argument of `ohtsukiSum` — instead
of `∀ z, z.im ≠ 0 → …`. The proof applies it at **five** points, not three as the
note above implies: `y₀` and `x₀y₀` are upper, `1/y₀`, `1/x₀`, `1/(x₀y₀)` lower.
`IsKummerAtOhtsukiArgs.of_forall` recovers the old ∀-form, so nothing that could
already discharge it is worse off.

### 2. Schwarz reflection, done — and it was not the shape I predicted

`isKummerAt_of_conj` proves that Kummer at `z̄` gives Kummer at `z` for
`z.im ≠ 0`: every ingredient is odd under conjugation (`BlochWigner_lob_conj`,
`arg_conj_of_im_ne_zero`, `‖z̄‖ = ‖z‖`), so the identity at `z̄` is `(−1)×` the
identity at `z` and `linear_combination -h` closes it.
`IsKummerAtOhtsukiArgs.of_upper_half_plane` then builds all five points from
`KummerRadial.kummer`'s own `Im z > 0` range plus one hypothesis:
`Li₂(z̄) = conj (Li₂ z)` off the real axis.

**No continuation across the cut was needed.** The roast above expected the cut
to be the difficulty and measured that it was not; the reason is now formal — the
lower half plane is reached by an algebraic identity, and `kummer` is only ever
evaluated where it is already proved.

### 3. The hypothesis discharged at `cLiTwoExt` — and the parameter eliminated

`QOU.MathlibExt.cLiTwoExt_conj` proves `Li₂(ȳ) = conj (Li₂ y)` for `y.im ≠ 0`
directly from the integral definition: conjugation passes through the real-interval
integral (`intervalIntegral_conj`, no integrability hypothesis — `conj` is an
isometry, so both sides are Bochner junk `0` together), and pointwise
`conj(log(1 − yz)/z) = log(1 − ȳz)/z` by `Complex.log_conj`, whose side condition
`arg(1 − yz) ≠ π` holds because `Im(1 − yz) = −(Im y · z)` and `z = 0` gives `1`.
`cLiTwoExt_one_im` discharges `hone` the same way, from the stronger local fact
that the integrand is *real* on `[0,1]`.

So `volume_conjecture_five_two_cLiTwoExt` has **no function parameter and no
identity hypothesis**.

**`hy : y.im ≠ 0` is load-bearing, not decorative.** The unrestricted
`∀ y, Li₂(ȳ) = conj (Li₂ y)` is FALSE for the principal branch: on the cut it
degenerates to `Li₂ y ∈ ℝ`, and `mpmath` gives
`Li₂(5) = 1.78371916127 − 5.05619832211i`. Recorded because a theorem whose
hypotheses nothing satisfies is exactly the failure this file already has one
example of (the excised `hinv`).

### What did NOT change — and the roast's claim 2 still stands

`OhtsukiAsymptotic` and `FiveTwoTriangulation` still have **no instances**, per
§3b-tax (`#synth` fails; checked). Eliminating the `Li₂` parameter is not
"instantiating the bridge" and I am not repeating that claim: the theorem remains
conditional on Ohtsuki's published asymptotic expansion and on the `5₂`
triangulation, which is the whole and only residue.
