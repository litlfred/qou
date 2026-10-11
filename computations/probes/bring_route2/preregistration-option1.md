# Route 2, option 1: a non-degenerate energy, tested on fresh words (pre-registration)

Written 2026-10-10, before anything below has been computed. The owner asked for this the same day ("2" = *write option 1 down formally before computing*).

Why this exists: the route 2 energy E (in `preregistration-energy.md`) was 0 for both loops it could rank, so the result was a tie. A loop gets E = 0 whenever every shortest path between two of its points runs along the loop itself. Short loops on Bring's surface are therefore *expected* to give 0, so E cannot discriminate between them. Option 1 replaces E with an energy that is strictly positive on every embedded loop. It is first tested on words that **nobody has looked at**.

Nothing in this file reads Q_β, CODATA, a mass, or any target.

## 0. What was already seen, and what that contaminates

Already seen:
- the Bring lengths of class A, 4.6031833095…, and of gen_grouped, 6.3676503714…;
- their energies, E = 0 for both;
- a post-hoc "self-approach margin", `margin_diag.py`: 1.3534 for class A and 0 for gen_grouped.

That margin measures roughly the same thing as the thickness τ defined below. **So any verdict of the new energy on class A versus gen_grouped is NOT a clean test.** It is reported, labelled CONTAMINATED, and carries no evidential weight. Only the fresh-word results in §4 are clean.

## 1. The energy: ropelength on Bring's surface (primary)

Let γ be a closed geodesic on X = Bring's surface with length L. Lift it to the hyperbolic plane as the axis A of the deck element g^r (route 2's construction). Write Γ_B for π₁(X), the kernel of Δ(2,4,5) → S₅.

**Thickness.** τ(γ) = ½ · min d_H(A, h·A), over the h ∈ Γ_B that do **not** preserve A.

Here d_H is the distance between two geodesics of the hyperbolic plane. Put A as the imaginary axis (endpoints 0, ∞) and let h·A have endpoints e₀, e₁:
- if e₀ and e₁ have opposite signs, the geodesics cross and d_H = 0;
- otherwise cosh d_H = (|e₀| + |e₁|) / | |e₀| − |e₁| |;
- if they share an endpoint, d_H = 0.

τ is the radius of the largest embedded collar (tube) around the loop. It is 0 exactly when the loop crosses itself.

**Ropelength.** Λ(γ) = L / τ.

- **Λ is never 0**, since L > 0 and τ is finite on a compact surface.
- **Λ = +∞ when the loop crosses itself.** That is the analogue of route 2's "E = +∞" rule.
- **A smaller Λ ranks higher:** a short loop with a wide collar. This is the standard ideal-knot convention, fixed here.

**Secondary (robustness only).** The bare length L, ranked smaller first. It is reported alongside Λ but never combined with it. If Λ and L disagree on the top word, the result is reported as **energy-dependent**.

**Words with no loop** (the image is a rotation, as for nuc9 and class B) get no Λ, as in `preregistration-energy.md` §3.

## 2. The fresh words (fixed by a rule, not chosen)

Start from all positive braid words of length 11 in σ₀, σ₁, which is 2¹¹ = 2048 words. Identify two words when either:
- they are cyclic rotations of each other, which is conjugation in B₃; or
- they differ by swapping σ₀ ↔ σ₁, which is conjugation by Δ in B₃.

Length 11 is odd, so no word is fixed by the swap. That leaves 188 necklaces and so **94 classes**. Then remove every class containing one of the five already-seen 11-letter words: nuc11_interleaved = gluon_s0_s0, gluon_s0_s1, gluon_s1_s0, gluon_s1_s1, nuc11_gen_grouped. Nothing else is removed by hand. That includes σ₀¹¹, which simply has no loop and will drop out under the no-loop rule.

What remains is the fresh set, at most 94 − 5 = 89 classes (fewer if two seen words share a class). Every word in the 9-letter-core-plus-gluon family is already seen, so the fresh set contains no core-plus-gluon word. The pending gluon ruling therefore does not change this set.

Each fresh word goes through route 2's map exactly as in `preregistration.md`: B₃ → SL(2,ℤ) at t = −1, then Γ₀(2), then H₄, then Δ(2,4,5), then Bring. Words with no loop drop out of the ranking and are counted.

## 3. Computing τ (with a self-certifying search radius)

Kernel elements are enumerated as in `bring_loop_energy_probe.py`. A first pass uses radius R₀ = 1.5·L at the axis foot. Suppose the closest translate found has 2τ*.

The true minimiser has displacement at most L + 2τ_true, which is at most L + 2τ*. So:
- if L + 2τ* ≤ R₀, the minimum is certified;
- otherwise the search re-enumerates at radius L + 2τ* and repeats.

The bound itself: shift the nearest point into the fundamental segment along the axis, then apply the triangle inequality. Both steps are written out in the probe's docstring.

Arithmetic: mpmath, 30 dps, no float64. No quadrature is needed, since L and τ are closed forms.

## 4. The test, and what "pass" means (fixed now)

Over the fresh loop-carrying classes, Λ **passes** when its minimum is attained by exactly one loop, compared to 25 digits.

Two classes that tie are first checked for being the same loop. If their SL(2,ℤ) images are conjugate in GL(2,ℤ) (decided exactly from reduced quadratic-form cycles), they are counted as one loop and flagged. Any other tie is a genuine tie, and Λ fails.

Also reported:
- the number of distinct Λ values;
- the number of ties at every rank;
- the same figures for L.

The test asks only whether the energy can discriminate at all. **It selects nothing among the fresh words**, which are not candidates for anything.

## 5. What happens after

- **If Λ fails,** it is not applied to the seen words. Option 1 is reported as a negative (scope (a): this energy alone does not discriminate).
- **If Λ passes,** its value on class A and gen_grouped is computed and reported as CONTAMINATED (see §0). Using that verdict to choose the scored word is the owner's decision, not this probe's.

## 6. Checks (pre-registered)

1. **Reproduction.** For class A and gen_grouped the probe reproduces route 2's L to 25 digits. These are the only seen values it is allowed to recompute before the fresh test.
2. **Conjugate invariance.** gluon_s1_s0 and gluon_s1_s1 give identical Λ. This is computed after the fresh test, under §5.
3. **Radius certificate.** Every reported τ carries a certificate: L + 2τ ≤ the search radius used.
4. **Class count.** The number of classes before removal equals 94, computed by brute force over all 2048 words.
