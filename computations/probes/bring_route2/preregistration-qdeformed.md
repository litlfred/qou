# Route 2, recipe R-q: pre-registration (written before any number was computed)

Owner request, 2026-10-10: compute recipe **R-q** from `preregistration-energy.md` §4
(reduced Burau at a deformation parameter tied to the proton pin q₀), keeping it as a
registered option beside the classical recipe. That section said R-q "requires a further
definition … which must itself be pre-registered before it is computed". This file is
that definition. Every fork below is a **default chosen before computing**; the owner may
overrule any of them, and a result obtained under an overruled default is reported as
POST-HOC.

## 0. What R-q can and cannot give

At t = −1 the reduced Burau map lands in SL(2,ℤ), which is discrete and folds onto
Bring's surface; that is what made route 2's lengths and energies definable. At t = ±q₀
the image is a non-discrete subgroup of GL(2,ℝ). **There is no Bring's surface here**, so:

- no fold onto Bring, no S₅ order r, no Bring length r·2·arccosh(|tr|/2);
- no knot energy E (the energy needs a closed curve on a surface);
- only the **translation length of a single matrix** acting on the hyperbolic plane.

So R-q gives one number per word: a length (or, for an elliptic matrix, a rotation
angle). It is a **different quantity** from the route 2 Bring length, and the two must
not be compared as if they were the same.

## 1. The representation (fixed)

Reduced Burau for B₃, the convention that reproduces `preregistration.md` exactly at t = −1:

    σ₀ ↦ S₀(t) = [[−t, 1], [0, 1]]        σ₁ ↦ S₁(t) = [[1, 0], [t, −t]]

At t = −1 these are T = [[1,1],[0,1]] and L = [[1,0],[−1,1]], the generators used by the
route 2 probe. A word w = (g₁ … g_n) maps to M_w(t) = S_{g₁}(t) ⋯ S_{g_n}(t), multiplied
left to right as in `bring_route2_probe.py`.

det S_i(t) = −t, so det M_w(t) = (−t)^n with n the word length (all letters positive).

## 2. Which t (a fork; default fixed here)

The request reads "t = q₀". Two readings are possible and they are **not** equivalent:

- **t = +q₀ (PRIMARY, as registered).** Literal reading. Near t = +1, where reduced
  Burau is the finite permutation representation, so this deforms the *permutation*
  picture, not the SL(2,ℤ) one.
- **t = −q₀ (SECONDARY).** The deformation that continues the classical map: t = −q
  with q → 1 recovers t = −1, i.e. exactly route 2's SL(2,ℤ) images.

Both are computed and both are reported, in separate columns. **Neither is chosen by
its numbers.** Which one is "the" R-q is an owner decision; the default if nobody
decides is that the primary column is what R-q means and the secondary is a
cross-reference.

> **Owner ruling, 2026-10-11 (decision card):** t = −q₀ defines the q-deformed recipe. It is the reading that returns to route 2's matrices as q₀ → 1. The t = +q₀ column stays in the results as a cross-reference. The ruling was made after both columns had been computed. Neither column ranks the words, so the choice could not have been steered by the numbers.

q₀ = the proton pin, `qou_substrate.constants.Q_50_DIGIT_STR`
= 1.1099785827513808075916690956107688798744991218736.

## 3. The length (fixed)

For a real 2×2 matrix M with d = det M ≠ 0, put x = |tr M| / √|d| (the trace after
scaling M to determinant ±1; scaling does not change the action on the hyperbolic plane).

- **d > 0** (orientation-preserving):
  - x > 2: hyperbolic, ℓ = 2·arccosh(x/2);
  - x = 2 (to within 10⁻⁴⁰): parabolic, ℓ = 0;
  - x < 2: elliptic, report the rotation angle θ = 2·arccos(x/2) and set ℓ = 0.
- **d < 0** (orientation-reversing, a glide reflection): ℓ = 2·arcsinh(x/2). This is
  log of the ratio of the two eigenvalues, which have opposite signs.

Because every candidate word has odd length (9 or 11), det = (−q₀)^n < 0 at t = +q₀ for
**every** candidate: they are all glide reflections there. At t = −q₀, det = q₀^n > 0.
This is stated now, before computing, so it cannot be presented later as a finding.

## 4. Candidates (unchanged from route 2)

nuc9, nuc11_interleaved (= gluon_s0_s0), gluon_s0_s1, gluon_s1_s0, gluon_s1_s1,
nuc11_gen_grouped. Exactly the set and spelling in `bring_route2_probe.py`.

## 5. Outputs, and the ranking rule (there is none)

For each word and each t: det, |tr|, x, type, ℓ (and θ where elliptic).

**No word is selected.** No ranking rule is registered, so the lengths are reported and
nothing is ranked by them. In particular the probe does not read Q_β, CODATA, any mass,
or any target. A ranking rule may be registered later, in a new file, before it is
applied; applying one to these numbers after seeing them is POST-HOC by definition.

## 6. Checks that must pass (all fixed in advance)

1. **Classical limit.** At t = −1 the probe's M_w equals route 2's integer SL(2,ℤ)
   image exactly, for every candidate.
2. **Full twist is a scalar.** M_{(σ₀σ₁)³}(t) = t³·I exactly (symbolic in t). So the γγ
   core contributes only a scale factor, which drops out of x.
3. **Conjugation invariance.** Words that route 2 records as conjugate in B₃
   (`CONJUGATE_PAIRS`) give equal x at both t (to 10⁻⁴⁰).
4. **Determinant.** det M_w(t) = (−t)^n, checked against the computed matrix.

Arithmetic: matrices are built symbolically in t with exact integer coefficients
(sympy), then evaluated with mpmath at 60 dps. No float64 anywhere.
