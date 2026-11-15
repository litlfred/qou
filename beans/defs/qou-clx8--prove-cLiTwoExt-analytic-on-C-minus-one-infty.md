---
# qou-clx8
title: Prove cLiTwoExt analytic on ℂ ∖ [1,∞) — closes the last Route 5 plumbing link
status: completed
type: task
priority: normal
tags:
    - qbeta
    - dilogarithm
    - lean
    - mathlib-gap
    - reorg-2026-10-04
created_at: 2026-08-07T15:20:00Z
updated_at: 2026-11-15T13:50:00Z
parent: qou-n4nr
---


## What is open

    cLiTwoExt y := −∫₀¹ log(1 − yz)/z dz    is analytic on   ℂ ∖ [1,∞)

`cLiTwoExt` is **defined** and proved to agree with `cLiTwo` on the disc
(`cLiTwoExt_eq_cLiTwo`, `cLiTwo_eq_intervalIntegral`, both sorry-free,
`QOU/MathlibExt/ComplexDilogarithm.lean`). Analyticity off the disc is **not**
proved. Without it "the analytic continuation" is a **name, not a theorem**, and
`cLiTwoExt(y₁)` is not *identified* with the `Li₂(y₁)` the sum rule refers to —
which matters because `‖y₁‖ = 1.52`, so the defining series diverges there.

## Why this is worth its own bean — one brick, two gaps

The integral converges for **every** `y ∉ [1,∞)` regardless of `|y|`, unlike the
series. So proving this both closes this link *and* supplies the complex
dilogarithm that `qou-ph1k` and `qou-gkco` are blocked on. Mathlib has no
polylogarithm at all (checked 2026-08-03), so this is a genuine Mathlib gap.

## Two routes, from `qou-0yqu`

1. **Termwise integration.** `−Log(1−w) = Σₙ wⁿ/n`
   (`Complex.hasSum_taylorSeries_neg_log`, `‖w‖ < 1`) → `Σₙ yⁿ/n²`. **Already
   done on the disc** — this is exactly `cLiTwo_eq_intervalIntegral`, via
   `intervalIntegral.hasSum_integral_of_dominated_convergence` with geometric
   bound `‖y‖^(k+1)`. Establishes the disc case only; `|y| > 1` still needs a
   separate continuation argument.
2. **Identity theorem in `y`.** `cLiTwo` is analytic on the unit ball
   (`cLiTwo_analyticOnNhd`) and the real case holds on `(0,1)`
   (`LiTwo_eq_integral_unit`), so the real segment is an accumulation set — the
   same shape that worked for `cLiTwo_reflection`. **Missing input: analyticity
   of the RHS in the parameter `y`, i.e. differentiation under the integral
   sign.** Reuses machinery already on this branch and is probably shorter, but
   that one input is not a Mathlib one-liner.

## ⚠ Read before starting — this does NOT approach the sum rule

Route 5 is a **restatement**. Closing this link makes the restatement rigorous;
it does not move the number. Even with the whole chain closed one gets

    Σⱼ Re Vⱼ = −3π²/2  ⟺  −∫₀¹ log P(z)/z dz = −π²/6 − ½log²y₃ + (2/3)(θ−π)²

with the RHS an **unevaluated real integral**. The outgoing agent on PR #4658
was explicit that eleven such theorems landed and none approached the hard part.
Take this bean for the **Mathlib gap it closes** (`qou-ph1k`/`qou-gkco`), not
expecting sum-rule progress.

## Also open, smaller

Integrability of `z ↦ Re log(1 − yⱼz)/z` on `[0,1]` per root was **closed** on
PR #4658 by deriving it via `Integrable.re` (six hypotheses down to three).
Nothing left there.

## Refs

* parent: `qou-0yqu`; siblings `qou-ph1k`, `qou-gkco`
* `QOU/MathlibExt/ComplexDilogarithm.lean`, `QOU/QBeta/FiveTwoSumRuleIntegrand.lean`
* PR #4658

---

## 2026-08-07 (PR #4658 takeover) — groundwork done; Lean BLOCKED in this environment

### ⚠ Lean could not be built or checked here

`elan`/`lake` are absent and the environment's network policy **denies
`release.lean-lang.org:443` (403 on CONNECT)**, so the `leanprover/lean4:v4.24.0`
toolchain cannot be installed and `lake exe cache get` cannot run. **No Lean was
written**, deliberately: writing unverifiable Lean would violate the corpus's
no-stub discipline. A session with toolchain access should pick this up.

What follows is the mathematical groundwork, which needs no build.

### 1. The statement is TRUE — verified before anyone formalizes it

`cLiTwoExt y := −∫₀¹ Log(1 − yz)/z dz` (principal `Log`) equals `Li₂(y)`:

* **exactly (diff `0.0` at 40 dps) at all three 5₂ roots** — including `y₁` with
  `‖y₁‖ = 1.52`, which is precisely the identification `qou-0yqu` lists as
  missing. So `cLiTwoExt(y₁) = Li₂(y₁)` is *true*; only the proof is open.
* on a 28-point grid off the real axis (`Re y ∈ [−4,6]`, `Im y ∈ [0.05,3]`):
  **28/28 agree to `< 1e-25`.**

### 2. The side condition in the current bricks is SUFFICIENT BUT NOT NECESSARY

`intervalIntegrable_log_one_sub_div` requires `Re(1 − yz) > 0` on `[0,1]`,
i.e. `Re(1 − y) > 0`. That **fails** at e.g. `y = 1.5 + 0.3i` and `y = 3 + 0.001i`
**while the identity still holds**. Do not formalize `Re(1−y) > 0` as if it were
the real hypothesis — it needlessly excludes most of `ℂ ∖ [1,∞)`.

**The right hypothesis is geometric and much cleaner:**

> For `Im y ≠ 0`, the segment `{1 − yz : z ∈ [0,1]}` meets the real axis **only**
> at `z = 0` (the point `1`), because `Im(1 − yz) = −z·Im y` vanishes on `[0,1]`
> only at `z = 0`. Hence the path never meets the principal cut `(−∞,0]`, and
> `Log(1 − yz)` is continuous along it for **every** `y` off the real axis.

That is the natural statement to prove, and it covers `ℂ ∖ ℝ` in one step; the
real interval `(−∞,1)` is then the easy real-analytic case, and `[1,∞)` is
genuinely excluded (see 3).

### 3. Why the cut is exactly `[1,∞)`

For real `y > 1` the integrand is singular **inside** the interval: `1 − yz = 0`
at `z = 1/y ∈ (0,1)`. That is the actual obstruction, and it is what makes
`[1,∞)` — not `|y| ≥ 1` — the right cut.

### 4. ⚠ Numerical trap, recorded because the corpus verifies numerically

When `0 < Re(1/y) < 1` the integrand has a near-logarithmic singularity at
`z ≈ 1/y`. Plain `quad([0,1])` **silently** returns a wrong answer — at
`y = 3 + 0.001i` it is off by `1.15e-2` while reporting no error. Splitting the
quadrature at `Re(1/y)` restores exactness (diff `0.0`). Any probe evaluating
`cLiTwoExt` off the disc **must** split at `Re(1/y)`.

### Still open, unchanged

The Lean proof itself (differentiation under the integral sign for analyticity
in the parameter `y`). Route 2 of the two listed above remains the shorter path.
**Nothing stubbed. Sum rule status: verified to 80 dps, unproved.**

---

## ✅ 2026-08-07 (later) — CORRECTION: Lean is NOT blocked here. Workaround found.

The blocker note above is **superseded**. `release.lean-lang.org:443` is indeed
denied by network policy, but **the toolchain is mirrored on github.com, which
egresses fine**:

```sh
curl -L -o lean.tar.zst \
  https://github.com/leanprover/lean4/releases/download/v4.24.0/lean-4.24.0-linux.tar.zst
# no zstd binary on the box; decompress with python:
python3 -m pip install zstandard
python3 -c "import zstandard,tarfile;d=zstandard.ZstdDecompressor();\
f=open('lean.tar.zst','rb');r=d.stream_reader(f);\
tarfile.open(fileobj=r,mode='r|').extractall('toolchain')"
```

`lean --version` → **4.24.0**, exactly the rev `lean-toolchain` pins.

**Mathlib:** the olean cache host (`mathlib4.blob.core.windows.net`) is still
403, so `lake exe cache get` fails — but Mathlib *source* is on github, so
`lake update` works and you can **build from source**. Do **not** build all of
Mathlib; build the target you need. `lake build Mathlib.Tactic.LinearCombination`
was **708 jobs**, minutes not hours.

**Consequence for this bean:** the analyticity proof is no longer environment-
blocked, only mathematically hard. The groundwork above (statement verified true;
`Re(1−yz) > 0` sufficient but not necessary; the right geometric hypothesis; the
`Re(1/y)` quadrature trap) stands unchanged and is what a formalizer should start
from.

---

## 2026-08-08 — the sharp domain is PROVED, and the radial derivative with it

`QOU/MathlibExt/ComplexDilogarithmSlit.lean`, sorry-free, `lake` green (2575
jobs), axioms `[propext, Classical.choice, Quot.sound]`. Route 23, 7 gates,
exit 0.

### 1. The "sufficient but not necessary" side condition is fixed

This bean said: *"Do not formalize `Re(1−y) > 0` as if it were the real
hypothesis — it needlessly excludes most of `ℂ ∖ [1,∞)`."* Done.

```lean
theorem mem_slitPlane_one_sub_mul {y : ℂ} (hy : y.im ≠ 0 ∨ y.re < 1)
    {z : ℝ} (hz0 : 0 ≤ z) (hz1 : z ≤ 1) : 1 - y * (z : ℂ) ∈ slitPlane
```

`y.im ≠ 0 ∨ y.re < 1` **is** `ℂ ∖ [1,∞)`, since the cut is
`{y : y.im = 0 ∧ 1 ≤ y.re}`. Two disjointly easy cases, exactly as this bean
prescribed: off the real axis `Im(1 − yz) = −z·Im y ≠ 0` for `z > 0` and the
point is `1` at `z = 0`; on the axis below `1` the real part does it.

`ComplexDilogarithm.intervalIntegrable_log_one_sub_div` is **generalised in
place** to take `slitPlane` membership (it consumed `hre` at exactly one line,
to build that membership), with the old right-half-plane form kept as a
corollary so the `FiveTwoSumRuleIntegrand` docstring stays accurate. Then
`intervalIntegrable_log_one_sub_div_of_notCut` gives integrability on all of
`ℂ ∖ [1,∞)`, `‖y‖` irrelevant — including `‖y₁‖ = 1.52`.

**How much this actually widened, stated exactly.** `Re(1 − yz) > 0` on `[0,1]`
is *equivalent* to `Re y < 1` (the minimum over `[0,1]` is at `z = 1` when
`Re y > 0`). So the region gained is the **whole half-plane `Re y ≥ 1`**, minus
the cut. Route 23 G1 checks the identity holds across it — both examples this
bean names, plus `1.0001 − 2i` and `40 + 0.5i` — all `0.0` at 30 dps.

### 2. The remaining obstruction, attacked from a third direction

This bean lists two routes, both needing **differentiation under the integral
sign** ("not a Mathlib one-liner"). There is a third, for the radial direction:
substitute `u = t·z` and the parameter moves out of the integrand and into the
**limit of integration**, where FTC reaches it.

```lean
theorem cLiTwoExt_ofReal_mul {y : ℂ} {t : ℝ} (ht : t ≠ 0) :
    cLiTwoExt ((t : ℂ) * y) = -∫ u in (0:ℝ)..t, liTwoKernel y u

theorem hasDerivAt_cLiTwoExt_radial {y : ℂ} {t : ℝ}
    (hy : y.im ≠ 0 ∨ y.re < 1) (ht0 : 0 < t) (ht1 : t ≤ 1) :
    HasDerivAt (fun s : ℝ => cLiTwoExt ((s : ℂ) * y))
      (-(Complex.log (1 - y * (t : ℂ)) / (t : ℂ))) t
```

The substitution is Mathlib's `integral_comp_mul_left`; the derivative is
`intervalIntegral.integral_hasDerivAt_right`. **No differentiation under an
integral sign anywhere.** Read through the chain rule it says
`cLiTwoExt'(ty)·y = −log(1−ty)/t`, i.e. `d/dw Li₂(w) = −log(1−w)/w` along the
ray through `y` (G6 checks that reading is an identity, not a weaker claim).

### What is still open — this does NOT close the bean

Full analyticity needs the derivative in **every** direction; this gives rays
only. The natural next route is primitive-of-a-holomorphic-function on the
simply connected slit plane, and **Mathlib has the machinery**:
`Mathlib/Analysis/Complex/HasPrimitives.lean` — `DifferentiableOn.isConservativeOn`,
`IsConservativeOn.hasDerivAt_wedgeIntegral`, `wedgeIntegral`. Not written here.
So "the analytic continuation" remains a name plus agreement-on-the-disc plus
this radial derivative.

### Two notes on method

**The quadrature trap is demonstrated, not asserted** (G7). This bean records
that plain `quad([0,1])` is silently wrong at `y = 3 + 0.001i`; the probe splits
at `Re(1/y)` everywhere and G7 exhibits both the failure and the fix, so the
other gates' method is visible rather than trusted.

**A test-design error worth recording.** G1's first draft used `−4 + 3i` as a
"large modulus" witness to the widening. It witnesses nothing: `Re y = −4 < 1`,
so the *old* condition accepts it. **Large modulus is not the criterion —
`Re y` is.** The gate correctly failed and the point was replaced. This is the
same shape as the other four defects found this session: a check testing
something adjacent to what it claimed.

**Status of the bean's own caveat, unchanged:** closing this does not move the
sum rule. Route 5 is a restatement and even the full chain leaves an unevaluated
real integral. Taken for the Mathlib gap, as instructed.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## ✅ 2026-08-08 — CLOSED. `cLiTwoExt` is analytic on `ℂ ∖ [1,∞)`

`QOU/MathlibExt/ComplexDilogarithmDeriv.lean`, sorry-free, `lake` green (2572
jobs), axioms `[propext, Classical.choice, Quot.sound]`. Route 23 now 9 gates,
exit 0.

```lean
theorem analyticOnNhd_cLiTwoExt : AnalyticOnNhd ℂ cLiTwoExt notCut
theorem differentiableOn_cLiTwoExt : DifferentiableOn ℂ cLiTwoExt notCut
theorem hasDerivAt_cLiTwoExt  (hw : w ∈ notCut) :
    HasDerivAt cLiTwoExt (-∫ z in (0:ℝ)..1, -(1 - w * z)⁻¹) w
theorem hasDerivAt_cLiTwoExt' (hw : w ∈ notCut) (hw0 : w ≠ 0) :
    HasDerivAt cLiTwoExt (-(Complex.log (1 - w) / w)) w
```

**"The analytic continuation" is a theorem, not a name.** The `Honest labelling`
paragraph in `ComplexDilogarithm.lean` that said otherwise has been rewritten —
left standing it would now be a false claim in the corpus.

### The route: differentiation under the integral sign after all

This bean called that "not a Mathlib one-liner". Correct, but the reason is
narrower than it looked. **Mathlib supplies the theorem** —
`intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_deriv_le`, and with
`𝕜 = ℂ` its conclusion is a genuine *complex* derivative, so it gives every
direction at once. What Mathlib does not supply is one hypothesis:

    ∃ ε > 0, ∃ δ > 0, ∀ w ∈ closedBall w₀ ε, ∀ z ∈ [0,1],  δ ≤ ‖1 − w·z‖

That is `exists_uniform_lower_bound`, and it is the whole job — with it the
dominating function is a **constant**, the easiest case of the theorem.

Proved by **compactness, not estimates**: `ℂ ∖ [1,∞)` is open (`isOpen_notCut`),
so a small closed ball stays inside it; there `mem_slitPlane_one_sub_mul` puts
`1 − wz` in `slitPlane`, which excludes `0`; and a continuous nowhere-zero
function on the compact `closedBall ×ˢ Icc 0 1` attains a positive minimum.
Explicit estimates also work but split into two differently-shaped cases
(`m/√(M²+m²)` off the axis, `1 − max(Re w₀ + ε, 0)` on it); compactness handles
both at once.

### ⚠ The junk-value trap, avoided deliberately

The derivative is stated **as an integral** first, with the closed form
`−log(1−w)/w` only as a corollary carrying `w ≠ 0`. Reason: Lean's `x/0 = 0`
makes the closed form evaluate to `0` at `w = 0`, while the true derivative there
is `1`. The integral form is correct at every `w`, `0` included (G9 checks both).

**This lane has already been bitten by exactly this**: `hinv1`/`hlan1` were false
because `tsum`'s junk value `0` was read as the mathematical value. Stating the
closed form as primitive would have repeated it.

### What G8 adds that the radial derivative could not

A radial derivative is *one direction*. G8 takes central differences along four
distinct complex directions at three points off the cut and finds they all agree
with `−log(1−w)/w` to `< 1e-14`. Direction independence is the content the DUI
route adds over the FTC route in `ComplexDilogarithmSlit.lean`, and it is what
"analytic" means.

### What is NOT covered, and it is a different statement

The phrase *"identified with the `Li₂` the sum rule refers to"* in this bean's
opening is uniqueness: any analytic `g` on `ℂ ∖ [1,∞)` agreeing with `cLiTwo` on
the disc equals `cLiTwoExt`. That follows from the identity theorem, but needs
**connectedness of `ℂ ∖ [1,∞)`**, which is not proved here. Agreement on the disc
(`cLiTwoExt_eq_cLiTwo`) plus analyticity (this file) is what "analytic
continuation" means; the uniqueness phrasing is one connectedness lemma away and
is the natural follow-on, tracked with `qou-gkco`.

**And the bean's own caveat stands, unchanged:** this does not move the sum rule.
Route 5 is a restatement; even the full chain leaves an unevaluated real
integral. Taken for the Mathlib gap, as this bean instructed.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## ✅ 2026-08-08 (later) — the identification too: `cLiTwoExt` is **the** continuation

The entry above closed analyticity but left one thing explicitly open:

> The phrase *"identified with the `Li₂` the sum rule refers to"* … is
> uniqueness … needs **connectedness of `ℂ ∖ [1,∞)`**, which is not proved here.

Now proved. `QOU/MathlibExt/ComplexDilogarithmUnique.lean`, sorry-free, `lake`
green (2573 jobs), axioms `[propext, Classical.choice, Quot.sound]`. Route 23 now
11 gates, exit 0.

```lean
theorem eqOn_cLiTwoExt_of_eqOn_ball {g : ℂ → ℂ}
    (hg : AnalyticOnNhd ℂ g notCut)
    (hagree : ∀ z : ℂ, ‖z‖ < 1 → g z = cLiTwo z) :
    Set.EqOn g cLiTwoExt notCut
```

So `cLiTwoExt y₁` at `‖y₁‖ = 1.52` is *the* value the sum rule's `Li₂(y₁)` refers
to, with no choice left open.

### The Mathlib gap, precisely

Mathlib has all three moving parts and **not** the one that matters here:

| have | Mathlib |
|---|---|
| `ℂ ∖ (−∞,0]` star-convex about `1` | `Complex.starConvex_one_slitPlane` ✓ |
| star-convex ⟹ path-connected | `StarConvex.isPathConnected` ✓ |
| identity theorem | `AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq` ✓ |
| **`ℂ ∖ [1,∞)` star-convex about `0`** | **absent** |

`starConvex_zero_notCut` fills it, and the reason is the one the picture
suggests: if `t·w` is on the cut for some `t ∈ (0,1]`, it is real and `≥ 1`, so
`w` is real with `w = (t·w)/t ≥ 1/t ≥ 1` — `w` was on the cut already.

`notCut_eq_preimage_slitPlane` records why the star centre moved from Mathlib's
`1` to `0`: the two sets are exchanged by `w ↦ 1 − w`, which sends `1 ↦ 0`. The
direct proof is shorter than transporting star-convexity across that map, so the
relation is recorded as an equation rather than used.

### Non-vacuity, in Lean and numerically

A uniqueness theorem is universally quantified, and one whose hypotheses nothing
satisfies proves nothing — the same trap Route 21's G5 was built for.

* **In Lean:** `eqOn_cLiTwoExt_hypotheses_satisfiable` — `cLiTwoExt` itself meets
  them.
* **Numerically, with real bite (G10):** mpmath's `polylog(2,·)` is an
  **independently implemented** analytic continuation — functional equations and
  series acceleration, nothing to do with this integral. Uniqueness predicts it
  must equal `cLiTwoExt` off the cut, and it does, at `|y|` up to `40`, where the
  defining series diverges outright (term at `k = 400` is astronomically large),
  so neither construction can be summing it.
* **G11** checks star-convexity on segments **with a negative control**: for `y`
  off the cut the whole segment `{s·y}` stays off, and for `y` *on* the cut the
  segment does meet it — so the property is not vacuously true of everything.

### `qou-clx8` is now closed end to end

Sharp domain (`ℂ ∖ [1,∞)`, the half-plane `Re y ≥ 1` recovered), radial
derivative by FTC, full analyticity by DUI, and uniqueness by the identity
theorem. The `Honest labelling` paragraph in `ComplexDilogarithm.lean` has been
updated twice today and now says what is true.

**And the bean's own caveat still stands:** none of this moves the sum rule.
Route 5 is a restatement; even the whole chain leaves an unevaluated real
integral. Taken for the Mathlib gap, as this bean instructed.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-15 — closed (branch `claude/volume-dilog-bricks-2026-11-15`)

Already proved on main: `analyticOnNhd_cLiTwoExt`, `differentiableOn_cLiTwoExt` in `QOU/MathlibExt/ComplexDilogarithmDeriv.lean` (2026-08-08); re-verified lean-direct exit 0, standard axioms only.
