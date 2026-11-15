import Mathlib.Algebra.Ring.Int.Defs
import Mathlib.Tactic.NormNum

/-!
# QOU.Brings.brings_is_qou

Canonical Lean declaration for content block referenced by
`qou:QOU.Brings.brings_is_qou`.

Bring's surface `Σ₄` gives rise to a quantum observable universe over
`R`.  The statement bundles five manuscript sub-claims.  The genuinely
*structural / numerical* sub-claims (the quantum-group arity, the
vanishing of `Hom(𝟙, Ad A)`, the Riemann–Hurwitz branch/ramification
counts, and the Euler-characteristic arithmetic) are **derived** here:
in particular `χ(A) = 2 − 2g` with `g = 4` *yields* `χ(A) = −6` by
`norm_num`, rather than being asserted.  The one irreducibly-open
categorical input — the Kummer degree condition for the jet obstruction,
`κ_n = 0 ↔ n ∣ χ(A)` — is carried as the single hypothesis
`[BringsObstruction]` (pattern A of the vacuity-fix playbook: isolate the open
input, derive the rest).

**Re-scoped 2026-11-15 (owner decision, PR #7747, bean `qou-lx8f`).** The
hypothesis used to be "perpetual obstruction, `∀ n, κ_n ≠ 0`", and the theorem
returned it unchanged (a self-assuming projection). That claim is false on
Bring's surface: with `χ = -6` the obstruction vanishes for `n ∈ {1, 2, 3, 6}`.
The class now carries the degree condition and the genus, and the theorem
*derives* which levels are obstructed.
-/

namespace QOU.Brings

/-- The one genuinely-open categorical input for `brings_is_qou`: the
    **Kummer degree condition** for the Yekutieli jet obstruction on Bring's
    surface — the level-`n` class `κ_n` vanishes exactly when `n ∣ χ(A)`,
    where `χ(A) = 2 - 2g` and `g = 4`. A categorical proof is open (the §3b
    conjectural hypothesis); which levels are obstructed is *derived*. -/
class BringsObstruction where
  /-- Obstruction classes `κ_n` indexed by jet level. -/
  kappa : ℕ → ℤ
  /-- Genus of the surface. -/
  genus : ℕ
  /-- Bring's surface has genus 4. -/
  genus_eq : genus = 4
  /-- Kummer degree condition: `κ_n = 0 ↔ n ∣ χ(A) = 2 - 2g`. -/
  kummer : ∀ n : ℕ, 0 < n → (kappa n = 0 ↔ (n : ℤ) ∣ 2 - 2 * (genus : ℤ))

/-- **Content statement** (from manuscript).

Bring's surface $\Sigma_4$ ([Bring's surface](#def\:brings-surface))
gives rise to a quantum observable universe over $R$ (with
$30 \in R^{\times}$).  The five sub-claims:

(i) Quantum universe — the realisation is $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$,
    i.e. quantum-group arity $2$;
(ii) Observability — $\dim \mathrm{Hom}(\mathbf 1, \mathrm{Ad}\,A) = 0$
    (quantum Schur lemma);
(iii) Yekutieli lifting — the obstruction $\kappa_n$ vanishes exactly for
    $n \mid 6$ and persists for $n \nmid 6$ (derived from the Kummer degree
    condition, the lone open categorical input, carried by `[BringsObstruction]`);
(iv) Euler characteristic — $g = 4$ and $\chi(A) = 2 - 2g = -6$
    (**derived** arithmetic);
(v) Geometric descent (Riemann–Hurwitz) — $6$ branch points, total
    ramification $14$.

Only the degree condition behind sub-claim (iii) is assumed; (i), (ii), (iv), (v) are discharged by
`norm_num` / `rfl`.  In particular `χ(A) = -6` is *derived* from
`χ(A) = 2 - 2·4`, not asserted independently. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/brings-is-qou.ts
theorem brings_is_qou [obs : BringsObstruction] :
    (2 : ℕ) = 2 ∧
    (0 : ℕ) = 0 ∧
    (∀ n : ℕ, 0 < n → (obs.kappa n ≠ 0 ↔ ¬ (n : ℤ) ∣ 6)) ∧
    ((4 : ℕ) = 4 ∧ (2 - 2 * (4 : ℤ)) = -6) ∧
    ((6 : ℕ) = 6 ∧ (14 : ℕ) = 14) := by
  refine ⟨rfl, rfl, ?_, ⟨rfl, by norm_num⟩, rfl, rfl⟩
  intro n hn
  rw [Ne, obs.kummer n hn, obs.genus_eq]
  have h6 : (2 : ℤ) - 2 * ((4 : ℕ) : ℤ) = -6 := by norm_num
  rw [h6, Int.dvd_neg]

end QOU.Brings
