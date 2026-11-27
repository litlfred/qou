# The q-special-function dictionary: which algebra carries which harmonics

Thread "Audit the q-Bessel special-function dictionary", 2026-11-27. PR #9746.

**Question (owner):** are the q-Bessel functions for the Cartan algebra, and the toroidal
versions, complete for every algebra we use? Do we have all the operators or a basis of
them? Do we know how they dissipate, and are their spectral transforms right? Is all of this
accounted for in α decay, β decay and binding? Is anything beyond the sphere and the torus
needed (Bring's surface)?

**Short answer.**

* The **sphere side** (Cartan block of `O_q(SU(2))`) is now complete in Lean. The little
  q-Jacobi polynomials form a basis of the Cartan block. They are orthogonal for a
  nondegenerate Haar pairing with nonzero norms, and the q-NS budget is diagonal in them.
  Every weight-block pairing is nondegenerate too.
* The **torus side** (`E_q(2)` contraction, Hahn–Exton q-Bessel) is only partly in Lean. The
  recurrences are proved. The q-Hankel orthogonality and inversion are checked numerically,
  not proved.
* **Bring's surface:** the holomorphic harmonics need only the sphere and one torus. No
  symmetry quotient has genus 3, and the representation is forced to be std⊗sgn. The Laplace
  (Maass) spectrum is transcendental. Only its exact discrete model is computed.
* **No compute consumes the sphere side.** Exactly one torus number, the Coulomb shape factor
  `f = 0.520011`, reaches a producer, and it reaches one of them with the wrong scope (see §3).

## 1. The dictionary

`p = q²`, assumed not a root of unity. "Lean ✓" means sorry-free and verified with
`lean-verify`.

| Algebra / subalgebra | Special functions | Operator basis | Spectrum and dissipation | Transform | Lean status | Consumed by |
|---|---|---|---|---|---|---|
| **Cartan block** `K[ζ]`, `ζ = βγ` (torus-biinvariant; sphere `S² = SU(2)/T`) | little q-Jacobi `p_n(ζ; 1, 1; q²)` | `L = X₊X₋` (q-Casimir); `X₀` vanishes on the block | `λ_n = [n]_{q⁻²}[n+1]_{q²} = q[n]_q[n+1]_q` (symmetric q-integers), pairwise distinct; `n(n+1)` at `q = 1`. Budget `h(X₊a·X₋a) = −q⁻² Σ λ_n c_n² h(p_n²)`. | Jackson q-integral on `[0,1]`, base `q²`: `h(ζ^m) = (−q)^m/[m+1]_{q²}`. Little q-Jacobi expansion **complete** | Lean ✓: #9666 (L, moments, symmetry, budget); **#9746**: pairing nondegenerate, `ζ` transcendental, `p_n` span `K[ζ]`, `h(p_m p_n) = 0` for `m ≠ n`, `h(p_n²) ≠ 0` | **none** |
| **Weight blocks** `B_s = (αγ)^s K[ζ]` | expected: little q-Jacobi with `α = s` | `L` preserves `B_s` (#9707); `X±` move between blocks | integration by parts `h(X₊a·X₋b) = −q^{2(s−1)} h(a·Lb)` (#9714) | pairing `K[ζ](βδ)^s × B_s` | Lean ✓: #9707, #9713, #9714; **#9746**: pairing nondegenerate on both sides. **Gap**: `L` self-adjoint per block, so no per-block basis yet | none |
| **Full** `O_q(SU(2))` | matrix coefficients `t^l_{mn}` = little q-Jacobi × torus characters (Koornwinder) | PBW basis `α^a β^b γ^c` / `δ^a β^b γ^c` (#9731); `h ∘ X± = h ∘ X₀ = 0` on the whole algebra (#9731) | Casimir on all blocks: per block via #9707; global spectral theorem not stated | Peter–Weyl | Lean: PBW ✓ (#9731). **Gap**: Peter–Weyl / Schur orthogonality for `t^l_{mn}` | none |
| **Torus** `T = Aut⊗(τ)` | characters `z^n` | `R_u` scalings; Cartan field `c⁻¹(f − R_u f)` | zero on `K[ζ]` (`cartanField_ev`) | Fourier series on `T` | Lean: #9722 (open PR); `torus_zeta`, `cartanField_ev` ✓ | none directly |
| **Borel** `U_q(𝔟)` / upper-triangular part | — | — | — | — | **absent** from the corpus | — |
| **`E_q(2)` contraction** (plane motions; "toroidal" side) | Hahn–Exton q-Bessel `J_ν(x; q)` | q-difference operator of `J_ν`; contiguity, Lommel | q-Hankel orthogonality on the full Jackson lattice `p^ℤ`, measure `x d_p x` | q-Hankel transform, base `p²`, `p = 1/q₀` | Lean ✓: `MathlibExt/QBesselContiguityRecurrence`, `Nuclear/QCasoratianAbel`, `QLommelOrderRecurrence`, `QBesselBarCovariance`, `CoulombShellShapeFactor` (dilation invariance only). **Gap**: q-Hankel orthogonality/inversion (probe only) and the contraction limit (analytic, `Transcendental/`) | `coulomb_energy.py` (A ≤ 4); `coulomb_isospin_channel.py` → `mass_table_comprehensive.py` (all A, see §3) |
| **Jacobi–Anger** (Reeb tower phases) | `e^{iz sin θ}` → `Σ J_n e^{inθ}` | — | — | Fourier–Bessel | Lean ✓: `Nuclear/ReebTowerJacobiAnger`, `MassTheory/BindingJacobiAngerBridge`, `BindingQBesselKernel` | probes only (`qbeta/`) |
| **Jackson tunnelling** (α decay) | Thomae–Jackson q-integral | — | Geiger–Nuttall form | Jackson FTC | Lean ✓: `Nuclear/ThomaeJacksonCoulombAndAlphaTunneling` | **none**; `derive_q_values.py` takes Q_α as a pure mass difference, with no barrier term |
| **Bring's surface** `B`, `Aut⁺ = S₅`, genus 4 | holomorphic 1-forms = `[2,1,1,1]` = std⊗sgn (forced); `Jac(B) ~ E⁴` (quoted) | `S₅` isotypic projectors | quotients `B/H`: genus 0, 1 or 2 only (Riemann–Hurwitz). Discrete model: vertex Laplacian spectrum `0, 2, 4, 5, 6, 7` with `S₅` types (probe) | — | Lean ✓ **#9746**: `rh_quotient_genus_le_two`, `h0K_character_forced`, `quotient_genus_table`. **Gaps**: `E⁴` isogeny; Maass spectrum (transcendental) | `StandardModel/BringPrymRiemannRochGenerations.lean` uses **std** (wrong sign twist; bean `qou-efxy`) |

## 2. Is anything beyond sphere and torus needed?

For the holomorphic harmonics, no (`BringSymmetryQuotientGenus.lean`):

1. For any `H ≤ S₅` with `|H| ≥ 2`, Riemann–Hurwitz `6 = |H|(2g' − 2) + R` gives `g' ≤ 2`.
   Genus 2 needs `|H| ≤ 3`, and positive genus needs `|H| ≤ 12`. This holds for every
   subgroup, without enumerating them.
2. Chevalley–Weil, `dim H⁰(K)^H = g(B/H)`, then forces the character to be `[2,1,1,1]`. The
   alternative `[4,1]` would give a transposition quotient of genus 3.
3. The quotients that carry harmonics are 6 torus classes (`⟨(01)⟩, V₄, C₄, C₆`, twisted
   `S₃`, `A₄`) and 2 genus-2 classes (`C₃, ⟨(01)(23)⟩`). The other 11 classes give spheres.

The exact discrete check (`computations/probes/bring_discrete_harmonics_probe.py`) agrees: the
harmonic 1-cochains of the `{5,4}` map have character `2·[2,1,1,1]`.

The Laplace (Maass) eigenfunctions are transcendental. Their `S₅` types reduce, by Frobenius
reciprocity, to Maass forms on the triangle orbifolds `B/H`. That is analytic work for
`QOU/Transcendental/` and is open.

## 3. Compute audit: are the producers up to date?

| Item | State |
|---|---|
| Sphere forms (`L`, `λ_n`, Haar moments) | **No Python consumer** in any mass, binding or decay producer |
| Coulomb shape factor `f = 0.520011` | `coulomb_energy.py:198–220` applies it for A ≤ 4 and the uniform ball above that. `coulomb_isospin_channel.py:59` **pastes** f, and `mass_table_comprehensive.py:611` then applies it at **every A** (Table 3.4b EM field). This is inconsistent. Owner card open. |
| `ACCURACY.md:144` | still says "uniform sphere" at A = 3, which is stale since commit `98608fc2f` |
| `mirror_nuclei_coulomb_systematics` witness | probably predates the f change (docstring at `:12` still says 3/5) |
| `b_over_a_evaluator.py`, `mirror_isospin_coulomb_split.py` | uniform ball with `r₀ = 1.2 fm`, a per-pair r₀ fit, float64. These violate the no-fit and no-float rules. |
| Q_α (`derive_q_values.py`) | pure mass difference; the Lean Jackson/Geiger–Nuttall file has no consumer |
| Q_β producers | no harmonic content |

Candidate updates, ranked by how cleanly each is derived (not by accuracy):

1. Make `coulomb_isospin_channel` read `coulomb_energy.shape_factor(A)`: one source, and the
   corpus's own A ≤ 4 scope. This waits on the owner card.
2. Re-run the two witnesses above, and fix the `ACCURACY.md:144` text.
3. Route the two old-convention Coulomb scripts through `coulomb_energy_mev`.
4. Prove q-Hankel orthogonality in Lean, with its base `p²` stated against the sphere side's
   `q²`.
5. A sphere-side consumer: the A ≥ 5 (p-shell and above) shape factor would need the
   weight-block little q-Jacobi functions. This needs a new derivation; nothing exists to
   wire yet.

## 4. Open gaps, ranked

1. `L` self-adjoint on each weight block, giving a per-block little q-Jacobi basis
   (parameter `α = s`).
2. Peter–Weyl / Schur orthogonality for the full `O_q(SU(2))` (PBW #9731 is the base).
3. q-Hankel orthogonality and inversion in Lean.
4. Whether the Cartan budget is the q-NS transport budget (bean `qou-pa7n`).
5. Borel subalgebra: absent.
6. Bring: `Jac(B) ~ E⁴` with `E` identified (candidate 50a1). The Maass spectrum by `S₅` type
   is transcendental.
7. The classical case `q² = 1` of the nondegeneracy (Hilbert matrix) is not covered.

No empirical value enters any proof cited here.
