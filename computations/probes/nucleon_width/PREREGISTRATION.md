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

## Addendum 1 (2026-11-22): the hydrogen capture braid, both electron placements (owner: "Compute CS for the capture-braid closure in both electron placements, preregistered first")

Written and committed before any number for this addendum is computed.

**Objects (from #8804 §43, as Lean-registered in `claude/hydrogen-capture-lean-2026-11-22`).**
- Proton left: `W_L = (σ₀σ₁⁻¹)³ · (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹`, proton strands 0–2, electron strand 3.
- Proton right: `W_R = (σ₁σ₂⁻¹)³ · (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹`, proton strands 1–3, electron strand 0.
- The closure of each (no braid axis), and for comparison the closure together with its axis.

**Predictions derived in advance (no compute).**
- **P1.** Both words are pure braids, so each closure has 4 components: the three Borromean
  components and one electron circle.
- **P2.** The capture factor `σ₂σ₁σ₀²σ₁σ₂` (resp. `σ₀σ₁σ₂²σ₁σ₀`) makes the electron strand wind
  once around the bundle of the three proton strands. Its closed component is then a (1, ±1) curve
  on the boundary torus of the bundle, which is isotopic in the bundle's complement to the braid
  axis. So each closure is expected to be the Borromean rings plus their braid axis, the 4-cusp
  manifold already computed (CS ≈ 0).
- **P3.** `W_R` is the strand-reversed image of `W_L` with the core mirrored; strand reversal is
  conjugation by the half twist, so the two closures are expected to be isometric up to
  orientation. Then CS(W_R) = ±CS(W_L), and with P2 both are 0.

**Verdict rule, fixed now.** If the two placements give equal |CS| (including both 0), the capture
braid's closure gives no p/n width difference: scope-(a) negative, as for the bare core. Only a
nonzero difference |CS(W_L)| ≠ |CS(W_R)| mod ½ would be a closure-level p/n asymmetry, and even
then no CS → width map is derived, so no width in MeV or s⁻¹ is quoted.

**Method.** SnapPy high precision, `snappy.Link(braid_closure=…)` for the bare closure and
`Braid:` for closure plus axis; `is_isometric_to` between placements; `identify()`.
