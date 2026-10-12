# γγ climbing placements under three closures: pre-registration

Written and committed **before any number in this file's scope was computed**. It follows up PR #7733 (issue #7727) and its `preregistration.md`, whose construction (vertex, shifts, range, reading 3 at every level) is reused unchanged. Owner request, 2026-10-12, on #7733: *"explore differences w/ 2 (bottom closure, there os also another closre -- see corpus)"*. Owner ruling 2026-10-11: reading 3 applies at **every** level of the tower. Beans `qou-ales`, `qou-99qc`.

Nothing here ranks, selects, or compares with Q_β, CODATA, AME or any mass. No check below has a target value taken from data.

## 1. The three closures (all fixed now)

The element is the same as in #7733: W_k^(s) = V_{p_0}⋯V_{p_{k−1}} ∈ H_n(q), with V_i = σ_iσ_{i+1}⁻¹ (primary) or U_i = σ_iσ_{i+1} (secondary), p_j = s·j shifted to start at 0, n = |s|(k−1) + 3, s ∈ {0, +1, −1, +2, −2, +3}, n ≤ 9 (s = 0: k ≤ 6). Generators are indexed σ_0 … σ_{n−2}; strand 0 is the bottom, strand n−1 the top.

**Closure 1, TOP (as in #7733).** The convention-D Markov conditional expectation E: H_{m+1} → H_m closes the top strand: E(a) = a, E(aσ_m b) = z_D·ab for a, b ∈ H_m, z_D = q³/(q²+1). Levels m = n, n−1, …, 3.

**Closure 2, BOTTOM.** Close the lowest strand instead: E_bot(a σ_0 b) = z_D·ab and E_bot(a) = a for a, b ∈ ⟨σ_1, …, σ_{m−1}⟩, with the result identified with H_m by σ_i ↦ σ_{i−1}. Let φ_n be the flip σ_i ↦ σ_{n−2−i}. Then E_bot = φ_m ∘ E ∘ φ_{m+1}, and φ_m is conjugation by T_{w_0} (inner), so

    χ_μ(E_bot^{n→m}(W)) = χ_μ(E^{n→m}(φ_n W)).

The probe computes closure 2 this way. Levels m = n, n−1, …, 3.

**Closure 3, PAIR (Jones projection, cap–cup).** This is the corpus's pair-creation/annihilation closure: the Jones projection e_i = (q·1 − σ_i)/(q + q⁻¹) (`QOU/Machinery/HeckeTowerBasicConstruction.lean:65`, idempotent proved at :113) and the basic-construction absorption law e·y·e = ι(ε y)·e (`class JonesBasicConstruction`, :211–222, an **open** class). At q = 1, e_i is the projector onto the singlet of strands i, i+1, i.e. a cap followed by a cup. Closure 3 removes the **top two strands together** by a cap and a cup:

    e_{m−1} x e_{m−1} = Φ(x)·e_{m−1},   Φ: H_m → H_{m−2} (on the y_λ > 0 blocks),

so the two strands are annihilated as a pair instead of each being closed onto itself. Levels m = n, n−2, n−4, ….

How it is computed. On a two-row Specht module S^λ, λ = (a, b) with b ≥ 1, the image e_{m−1}S^λ is isomorphic to S^μ with μ = (a−1, b−1) as an H_{m−2}-module (removing the last two boxes from different rows is the only way to get the −q⁻¹ eigenvalue of σ_{m−1}). Since Φ commutes with right multiplication by H_{m−2}, iterating j times gives

    χ_μ(Φ^j(W)) = χ_{μ+(j,j)}(W · e_{n−1} e_{n−3} ⋯ e_{n−2j+1}),   μ ⊢ n − 2j two-row.

This formula is what check K4 tests against closure 1.

**Closure 3′, PAIR from the bottom.** The same with the pairs taken from the bottom: computed as closure 3 of φ_n W (same inner-automorphism argument). Reported in its own column.

## 2. Reading 3 per closure (fixed)

At each level m, reading 3 holds if χ_μ ≥ 0 for every μ ⊢ m with at most two rows (those with y_μ > 0 under convention D). An element is **admissible under a closure** if reading 3 holds at every level that closure reaches with m ≥ 3. For closure 3 with n even the chain ends at m = 2; the m = 2 characters are reported but **not** part of the verdict, so that the verdict uses the same range m ≥ 3 as #7733. Exact zeros pass. Signs are reported at the proton pin q₀ (`Q_50_DIGIT_STR`, mpmath 60 dps) and on all of (1, ∞) (Sturm counts on numerator and denominator, roots isolated only when a count is nonzero).

## 3. The q = 1 (permutation) model, stated before computing

At q = 1, H_n = ℚS_n, z_D = 1/2, and the convention-D trace is the normalised trace of S_n on (ℚ²)^{⊗n}. Each vertex V_i or U_i becomes a 3-cycle on strands i, i+1, i+2. Closing one strand of a permutation π gives (1/2)·π̂ if the strand is moved (π̂ = π with that point cut out of its cycle) and π itself if the strand is fixed. So at q = 1 a closure to three strands gives 2^{−c}·π̂ with π̂ ∈ S_3, and χ_(2,1)(π̂) = 2, 0, −1 for the identity, a transposition and a 3-cycle. **At q = 1, reading 3 at level 3 fails exactly when the closed-down permutation is a 3-cycle.** This model is independent of the Hecke code and is used as check K3 for closures 1 and 2.

## 4. Checks (pass/fail fixed in advance)

- **K1.** Closure 1 reproduces, exactly, every character recorded in `gg-ntower.witness.json` (#7733).
- **K2.** For every (vertex, s, k), the top-level characters (m = n) of W and φ_n W are equal. This is the statement that φ_n is inner; all closures agree at m = n.
- **K3.** At q = 1, the level-3 value of χ_(2,1) under closures 1 and 2 equals the permutation-model value 2^{−c}·χ_(2,1)(π̂).
- **K4.** The pair-closure formula and the absorption law agree with closure 1: for sample words y ∈ H_m (m = 3, 4, 5) placed in H_{m+1}, χ_{μ+(1,1)}(y·e_m) = χ_μ(E(y)) for every two-row μ ⊢ m − 1. This tests e_m y e_m = E(y) e_m on characters, under convention D.

## 5. Reported, with no expected answer

For each closure and each (vertex, s, k):

- admissible or not, and the failing levels;
- at level 3 (or the lowest level ≥ 3): the q = 1 value of each χ_μ and the leading order in t = q − 1 at which it moves (as in #7733 §5);
- whether the closed-down element at level 3 is, on the y > 0 blocks, a positive multiple of a single vertex (χ_(2,1)/χ_(3) equal to the single-vertex ratio). Answer yes/no per row. This question came up while explaining #7733's result; it is asked here before it is computed for closures 2 and 3.

Comparison across closures: per (vertex, s, k), do the four closures give the same admissibility verdict? Listed as agree/differ, with the differing levels.

## 6. Outcomes (stated before computing)

- (i) Some climbing placement (s ∉ {0, +1}) is admissible under closure 2, 3 or 3′. Reported; nothing is adopted.
- (ii) No climbing placement is admissible under any closure.
- (iii) The verdict depends on the closure for some (s, k). Reported per row.

## 7. What this does not do

No quark letters, gluons or two nucleons. No placement other than a rigid shift. The Jones absorption law is checked on characters in these representations (K4); it is not proved in Lean and the class `JonesBasicConstruction` stays open. Exact sympy arithmetic over ℚ(q); mpmath at 60 dps for values at q₀; no float64.
