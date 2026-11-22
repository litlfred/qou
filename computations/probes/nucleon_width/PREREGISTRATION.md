# Preregistration: nucleon decay width as Im of the complex volume (bean qou-zslg)

Written 2026-11-22, before any number was computed. Owner choice "1" on the option list in the
n–p cell thread (PR #8955).

## The reading under test

`conj:complex-mass-constituent-functional` reads mass as Re Vol_ℂ(K) and the decay width as
Im Vol_ℂ(K) = CS(K), where Vol_ℂ = Vol + i·CS is the Neumann–Zagier complex volume of the link
complement. The nucleon is the closure of β_Bor = (σ₁σ₂⁻¹)³, which is the Borromean rings. The
neutron is the mirror braid, and its closure is the mirror link.

## Claims, preregistered

1. **Structural, no computation needed.** The Borromean rings are amphichiral, so the mirror closure
   is the same link up to an orientation-reversing homeomorphism of S³. Orientation reversal sends
   CS ↦ −CS (mod 1). So CS(n) = −CS(p) = CS(p) mod 1, and CS(p) ∈ {0, ½} mod 1. Under this reading
   the closure gives **the same width for proton and neutron**.
2. **Consequence.** Experimentally the proton is stable (τ_p > 10³⁴ yr) and the neutron is not
   (τ_n ≈ 879 s). A reading that gives Γ_p = Γ_n from the closure alone therefore cannot produce the
   n–p width difference. It is excluded **as a closure-only statement**, which is scope (a). The
   width would have to come from decorations of the braid, which is the same conclusion that
   issue #9002 reached for the mass.
3. **The value.** CS(Borromean complement) is to be computed with SnapPy if it can be installed. If
   it is 0, the reading gives width 0 for both nucleons: proton stability is derived, and neutron
   decay is unexplained. If it is ½ (mod 1), both get the same nonzero phase.
4. **Units.** CS is defined mod 1 (or mod π², depending on the normalization). No map from CS to a
   width in MeV or s⁻¹ is derived in the corpus, so no MeV or lifetime number is quoted. Only the
   p/n comparison, which is invariant, is a result.

## Expected verdict

Claim 1 holds whatever the value of CS. So a closure-only reading cannot be the width, and this is
reported as a scope-(a) negative for that reading. If the CS value can be computed, it is recorded
as a side result.
