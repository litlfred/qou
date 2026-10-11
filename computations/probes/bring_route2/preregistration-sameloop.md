# Route 2, option 1b: ropelength with a "same loop up to symmetry" rule, on fresh 13-letter words (pre-registration)

Written 2026-10-11, before anything below was computed. On 2026-10-11 the owner picked "2": write a stricter same-loop test down first, then run it on new fresh words of length 13. Nothing in this file reads Q_β, CODATA, a mass or any target.

## 0. Why, and what is already contaminated

Option 1 (`preregistration-option1.md`, results in `results_option1.md`) failed its pass test. The smallest ropelength Λ = L/τ was tied across 24 fresh 11-letter classes, which fell into 2 GL(2,ℤ) conjugacy classes.

A tie between two loops that are **images of each other under a symmetry of Bring's surface** is forced: Λ is unchanged by an isometry. Such a tie says nothing about whether Λ can discriminate. The GL(2,ℤ) rule did not see this, because the word → Bring map does not respect it. This file replaces that rule with the geometric one and tests it on words never looked at.

Already known, so contaminated:
- Λ(class A) = 2.5188748499… (it equals the 11-letter minimum, since 23 of those minimisers share class A's GL(2,ℤ) class);
- class A's length 4.6031833095…;
- gen_grouped's length 6.3676503714….

So **no outcome of this test can select between the seen words.** A pass would establish only that Λ, with the symmetry rule, is a discriminating energy on fresh words.

## 1. The energy (unchanged)

Λ(γ) = L/τ exactly as in `preregistration-option1.md` §1 and §3:
- L is the Bring length;
- τ is half the smallest distance from the lifted axis to another lift, found with a self-certifying search radius;
- Λ = +∞ for a self-crossing or non-primitive loop;
- smaller is better;
- the bare length L is reported as a secondary.

## 2. The same-loop rule (new; fixed now)

Two loops γ₁ and γ₂ count as **one loop** when an isometry of Bring's surface X carries one onto the other, as unoriented closed curves. Orientation-reversing isometries and reversal of direction are both included.

**How this is decided.** Use the triangle group Δ = Δ(2,4,5) with generators s, u from `bring_route2_probe.delta245()`. The reflection R(z) = −z̄ satisfies R s R = s and R u R = u⁻¹ (checked numerically), so R normalises Δ, and Δ* = ⟨Δ, R⟩ is the extended triangle group. Δ* normalises Γ_B = π₁(X), so each element of Δ* induces an isometry of X. Conversely, every isometry of X lifts to the normaliser of Γ_B. That normaliser is Δ* because (2,4,5) is not on Singerman's list of non-maximal triangle groups (Singerman 1972); this is cited as an assumption.

γ₁ ≅ γ₂ ⟺ some g ∈ Δ* maps the lifted axis A₁ onto A₂ (as a set of endpoints, in either order).

**Search bound.** Let m₁, m₂ be the segment midpoints that `loop_setup` places on each axis. If g·A₁ = A₂, then composing g with powers of the two loop translations moves g·m₁ along A₂ to within L/2 of m₂. So it suffices to search g ∈ Δ* with d(m₂, g·m₁) ≤ L/2. This is a finite ball, enumerated by breadth-first search over s, u, u⁻¹, with R applied once at the end. A match needs both endpoints to agree to 10⁻²⁰.

Two loops of different L (compared to 25 digits) are never the same loop; only equal-L pairs are tested.

## 3. Fresh words (fixed by rule)

Take all positive braid words of length 13 in σ₀, σ₁ (2¹³ = 8192 words), up to cyclic rotation and the σ₀ ↔ σ₁ swap. Since 13 is odd, no word is swap-invariant, so this gives 632 necklaces and **316 classes**. No 13-letter word has been looked at, so none is removed. Each class goes through route 2's map exactly as before; classes without a loop drop out and are counted.

## 4. Computing τ once per isometry class

τ is invariant under isometries, a theorem rather than an assumption. So the loops are first grouped into isometry classes (§2), and τ is computed for one representative of each class: the lexicographically smallest word.

As a check, τ is also computed for a second member of the largest class, and it must agree to 25 digits.

The collar-area bound Λ ≥ L / asinh(6π/L) (area of X = 12π) may still be used to skip classes that cannot be the minimiser; skipped classes are reported.

## 5. Pass test (fixed now)

Λ **passes** when its minimum over the fresh loops is attained by **exactly one isometry class**, comparing values to 25 digits. Also reported:
- the number of isometry classes;
- the multiplicity at each Λ value;
- the same figures for L.

Fail ⇒ scope-(a) negative: Λ with the symmetry rule does not discriminate on this set. Pass ⇒ Λ is a discriminating energy on fresh words; **nothing is selected** (see §0).

## 6. Checks (pre-registered)

1. **Class count.** 316 classes, by brute force over all 8192 words.
2. **Reproduction.** Route 2's L for class A and gen_grouped is reproduced to 25 digits.
3. **Self-consistency of the isometry search.** Every loop must be found isometric to itself (g = identity).
4. **Option 1 cross-check (reported, not used).** The 11-letter minimisers are regrouped by the new rule. This is post-hoc: it is printed for the record, labelled as such, and **plays no part in the verdict.**
5. **τ invariance.** As in §4.
6. **Arithmetic.** mpmath at 30 dps; no float64.
