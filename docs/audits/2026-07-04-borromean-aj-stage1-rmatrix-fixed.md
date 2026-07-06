# Borromean AJ stage 1 — R-matrix FIXED; tower established, exactly diagonal

**Date:** 2026-07-04
**Beans:** `1iqq` (R-matrix fix — done), `moqg` (Borromean stage 1 — unblocked),
`n920` (cyclotomic c_k identification vs Habiro [H1] — open follow-up),
`ds4b` (AJ-for-links literature — done, no Borromean theorem found).
**Supersedes** the WIP-blocked audit
[`2026-07-04-borromean-aj-stage1-rmatrix-blocked.md`](2026-07-04-borromean-aj-stage1-rmatrix-blocked.md)
(merged #3297). That doc's diagnosis of a *single* inverse bug was itself
incomplete — see below.
**Lineage:** the 4₁ / trefoil programs (PRs #3263, #3279); this opens the
Borromean (𝓑₃) program with a verified ground truth.

## Status: FIXED — stage 1 established

[`aj_borromean_colored_jones_tower.py`](../../computations/aj_borromean_colored_jones_tower.py)
now builds the multi-colored Jones tower J_B(m₁,m₂,m₃) of the Borromean rings
(closure of `(σ₁σ₂⁻¹)³`) from a **verified** U_q(sl₂) R-matrix. At MMAX=3 (all
triples m_i ≤ 3, exact symbolic t with q = t⁴):

| Anchor | Result |
|---|---|
| Convention pin (inverse + YBE on V₂⊗V₂) | both diag-first variants pass; `diag_first=False` pinned |
| **Color-3 gate** (R·R⁻¹=id AND YBE on V₃⊗V₃) | **OK** — the n≥2 terms now verify |
| Unlink reductions J(1,·,·)=1 | OK |
| Bar symmetry J(1/q)=J(q) (amphichirality) | OK on all triples incl. J(2,3,3), J(3,3,3) |
| q-numerator-integrality (reduced link ⇒ rational fn of q) | OK (5 denominator forms, all quantum-integer products) |
| **Habiro diagonality** J = Σ_k c_k ∏ᵢσ_k(mᵢ) | **OK on all computed triples** |

The colored Jones of 𝓑₃ is **exactly diagonal in the cyclotomic σ_k basis** —
the *same* basis as the Lean 4₁ ladder (`QOU.BraidKnot.HabiroNewtonLadder`,
`σ_k(m) = ∏_{j≤k}(Λ_m − λ_j)`) — established by over-determined verification on
the computed range, not assumed from the (firewalled) literature.

## The bug was TWO bugs, not one — correcting the blocked audit

The blocked audit claimed the **forward action was always correct** and only
the analytic inverse was wrong at color ≥ 3. **That was wrong.** The inverse
failure was the visible symptom; the deeper cause was a wrong nilpotent q-power
in the *forward* R:

1. **Forward action.** `coeff_n` used `t^{2n(n-1)}` for the nilpotent term
   `E^n⊗F^n`. This makes the **Yang–Baxter equation FAIL at color 3**
   (7/27 basis vectors of V₃⊗V₃⊗V₃). It was never caught because the V₂⊗V₂
   convention-pin caps the nilpotent sum at n=1, where `t^{2n(n-1)} = t⁰ = 1` —
   the n≥2 terms were simply never exercised. A parameter scan over the
   nilpotent exponent shows **only `t^{n(n-1)}`** makes YBE hold at colors 2,
   3, and 4. Since n≤1 is unchanged, the previously-validated color-2 (Jones)
   values are untouched.

2. **Inverse.** The naive termwise analytic inverse (sign/power flip of
   `E^n⊗F^n`) breaks once the E/F operators from the two tensor factors
   interleave through the K-weights at n≥2. Replaced by the **exact symbolic
   inverse of the forward R matrix** (`_R_pair` builds R on V_m⊗V_m' as a
   matrix and calls `.inv()`), so R·R⁻¹=id holds *by construction* at every
   color.

Both fixes are required and were verified together: YBE OK at colors 3 and 4,
R·R⁻¹=id on V₄⊗V₄, and the amphichiral bar-symmetry restored on the triples
that had "failed" purely as artifacts of the two bugs. Lesson recorded per the
critical-distance discipline: a machine check that only exercises the n≤1
regime (V₂⊗V₂) does **not** license a "forward always correct" claim — the
blocked audit over-narrowed the diagnosis. The new `main()` gates on the
color-3 checks (R·R⁻¹=id **and** YBE) precisely so this class of bug cannot
recur silently.

## The cyclotomic coefficients c_k (stage-1 output)

From the diagonal J(m,m,m) (exact, factored over ℚ(t)):

- `c_0 = 1`
- `c_1 = -t¹⁶ / [Φ-product]²` (denominator = squared product of cyclotomic
  factors through Φ₁₂)
- `c_2 = t⁴⁴ / [Φ-product]²` (through Φ₂₀)

None of the five hand-entered closed-form candidates (in {n}=sⁿ−s⁻ⁿ
arithmetic) matched — the exact c_k are recorded in the witness
(`cyclotomic_c_k`) for identification. **Closed-form identification of c_k is
the open stage-1b follow-up** (bean `n920`); the target reference is Habiro
[H1] (*On the colored Jones polynomial of some simple links*, RIMS Kokyuroku
1172), cited by Masbaum math/0306345 but not reachable here. The alternating
sign and the `t^{k(...)}` numerator with squared-cyclotomic denominator are the
structural fingerprints to match. This is a *scope-(a)* open item ("not yet
identified from the computed values"), **not** a claim that no closed form
exists.

## Literature status (unchanged from the blocked audit)

Bounded search (arXiv full-text firewalled; titles/abstracts reachable): strong
AJ is published for torus knots/cables (Tran 2013), the figure-eight
(`[nguyen-tran-2021]`), and two-bridge classes (Lê–Tran). **No published AJ
statement for the Borromean rings** surfaced — Borromean stages 2–3 (diagonal
recurrence reconstruction + A-ideal specialization) target a statement with no
literature theorem to cite; any Lean class must carry it as a §3b
conjecture-grade input. **Provenance:** Masbaum math/0306345 is a *twist-knot*
paper (corrected in #3279); it carries no Borromean formula. Scoped claim:
bounded search from a firewalled sandbox, not an exhaustive sweep.

## Next (stage 1b → stage 2)

1. `n920`: identify c_k in closed form (match against Habiro [H1] cyclotomic
   coefficients when reachable, or PSLQ the exact ℚ(t) values).
2. Stage 2: reconstruct the q-difference recurrence for the symmetric-diagonal
   tower J(N,N,N) from the c_k, mirroring the 4₁ Habiro-ladder recurrence.
3. Stage 3: specialize the recurrence ideal at q→1 and compare to the classical
   A-ideal of the Borromean complement (a §3b conjecture-grade statement).
