# Pre-registration: the matter pairing with λ = ε (2026-11-21)

Committed before the probe `mn_counit_pairing_probe.py` is run.

## Disclosure

Before writing this file, while reading the corpus, I proved (Lean, sorry-free) that
`coevaluation = unit ≫ comul` forces `counit = frobeniusForm` in every `FrobeniusHopfData`
(`CounitIsFrobeniusForm.lean`). That argument also shows the pair rescales together:
`(λ, coev) ↦ (sλ, s⁻¹coev)` comes with `(Δ, ε) ↦ (s⁻¹Δ, sε)`. So I expect test A to show that
λ = ε does **not** fix the scale, which withdraws the claim in my last reply that this route fixes it.
I also noticed that at q = 1 both test-B pairings equal 1 (group elements), so ratio 12 is already
excluded at q = 1. Both are stated so the tests are not read as blind.

## Test A — does λ = ε fix the scale? (class: H_2(q), dim 2)

Frobenius forms on H_2(q) = span{1, σ}, σ² = (q − q⁻¹)σ + 1: λ(1) = a, λ(σ) = b, generic.
Build coev from the inverse Gram matrix, Δ = (coev-derived Frobenius coproduct), and ε from the
counit law. Record: (A1) ε = λ identically; (A2) under a ↦ sa, b ↦ sb, ε ↦ sε.
Pass condition for "λ = ε fixes the scale": some normalisation of (a, b) is forced. Expected: none.

## Test B — the pairing ratio (class: H_3(q), regular representation)

Frobenius form: the canonical symmetrising trace τ(T_w) = δ_{w,e} (non-degenerate). Excluded: the
Ocneanu trace at z_D and at z = q, which are degenerate (they kill a Wedderburn block), so they are
not Frobenius forms. Antipode analogue: the anti-involution S(T_w) = T_{w⁻¹}, which preserves τ.
Pairing P(X) = τ(S(X)·X), with X_e = σ₀σ₁σ₀ and X_N = (σ₀σ₁⁻¹)³.
Record the exact ratio P(X_N)/P(X_e) in Q(q). Pass: ratio = 12 identically. Anything else is a
scope-(a) negative for this class.
