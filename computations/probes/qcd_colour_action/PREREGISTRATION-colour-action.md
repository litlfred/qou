# Pre-registration: an SU(3) / U_q(sl₃) colour action on the three-strand Hecke state module (bean `qou-ni4b`)

Written and committed **before** the probe is written or run. PR #9059, issue #9058.

## Question

Is there an injective colour action (su(3), or U_q(sl₃)) on a three-strand braid/Hecke state
module of the framework that commutes with the H₃(q) action and whose colour-singlet sector
reproduces the convention-D nucleon model? Convention D (`z_D = q³/(q²+1)`) is the N = 2 partial
trace (`z_N = q^N/[N]_q`, LITERATURE-COMPARISON §48); colour needs N = 3. This probe tests whether
a strand space carrying both resolves that, or sharpens it.

## Corpus-grep (done before writing)

- `ThreeStrandColourTowerCP.lean`: H₃(q) itself is too small; colour must act on a module.
- `OctonionColourActionBaseModule.lean`: tautological action on O = C ⊕ C³ (not the strand module).
- `ColourBridge.lean` / `JimboClassicalLimit.primitive_commute_rCheckN_iff`: a primitive
  (classical-coproduct) gl₃ field commuting with the gl₃ Jimbo Ř forces q = 1.
- `computations/probes/qbeta_colour_factor/`: colour as a separate tensor factor (K0 below).
- `computations/probes/qbeta_colour_gl6/` (issue #8833): flavour ⊗ colour = C⁶ with the gl₆ Jimbo Ř
  (K2 below); its colour action was not examined there; the Ř depends on a label order.
- Spectator audit 2026-11-21 §17(b): "a flavour ⊗ colour strand space is not defined in the corpus".
- Library (`INDEX.md`, sections, ocr): no hit for a Kronecker coproduct of Hecke algebras or quantum
  skew Howe duality on tensor powers. Searched; not found ≠ absent from the literature.

## Constructions (closed family; every member is reported, none is selected)

Flavour: `Ř_f` = the nucleon matrix Rc = [[q,0,0,0],[0,0,1,0],[0,1,q−q⁻¹,0],[0,0,0,q]] on C²⊗C²
(u = e₁ over d, OverStrandWeight). Colour: C³.

- **K0 colour spectator at fixed position.** W = C³ ⊗ C², Ř = 1_c ⊗ Ř_f (colour slots are not
  permuted by the crossing). Colour acts by the classical tensor action of sl₃ on (C³)^⊗3.
- **K1 colour strands only.** W = C³, Ř = Jimbo gl₃. Colour = U_q(gl₃) by its coproduct.
- **K2 flavour ⊗ colour in one Jimbo Ř.** W = C⁶, Ř = Jimbo gl₆, both lexicographic orders
  (isospin-major, colour-major). Colour candidates: (i) classical sl₃ acting on the colour factor of
  each strand; (ii) e_c = Σ_f E_{(f,c),(f,c+1)}, f_c likewise, k_c = Π_f K_{(f,c)}K_{(f,c+1)}⁻¹ acting
  through the U_q(gl₆) coproduct.
- **K3 colour spectator that moves.** Ř = Ř_f ⊗ P_c; and K3′ Ř = Ř_f ⊗ Ř_c (gl₃ Jimbo, same q).
- **K4 colour-invariant class.** If colour acts strand-wise through a Hopf algebra (classical sl₃,
  p = 1; or U_p(gl₃) through Jimbo eigenprojectors, p = q), commuting with Ř forces
  Ř = s_c ⊗ X + a_c ⊗ Y (s_c, a_c the symmetric / antisymmetric projectors of the colour pair).
  Closed class: X, Y ∈ {q·1, −q⁻¹·1, Ř_f, −Ř_f⁻¹}, p ∈ {1, q}: 32 members. The two members with
  X ≠ Y "of opposite sign class" (X = Ř_f, Y = −Ř_f⁻¹ and X = −Ř_f⁻¹, Y = Ř_f) are the only ones
  whose q → 1 limit is ±P on C⁶ ⊗ C⁶; for these two, p is also left symbolic.

## Acceptance test (fixed in advance, applied to every construction)

- (a) the colour action is injective (su(3): 8 independent operators with the sl₃ brackets;
  U_q(sl₃): Chevalley–Serre relations hold on the module and the generators are nonzero).
- (b) it commutes with the H₃ action (σ₁, σ₂) on W^⊗3. (Commutes, not merely intertwines.)
- (c) the Hecke relation (σ−q)(σ+q⁻¹) = 0 and the braid relation hold on W^⊗3.
- (d) on the colour-singlet sector the H₃ action equals the flavour model σᵢ ↦ Ř_f,ᵢ on (C²)^⊗3
  under an explicit flavour identification, and the K_f = diag(q,q⁻¹) Markov trace there gives
  z = z_D = q³/(q²+1). (Then u = e₁ and ε_n = q⁻²ε_p carry over unchanged.)
- (e) the colour-invariant subspace of the colour part is one-dimensional (the baryon is the unique
  colour singlet).
- (f) [reported, part of "compatible with the braid structure"] transport: the colour label moves
  with the strand, i.e. the q → 1 limit of Ř is ±P on W ⊗ W.

## Predictions

K0: (a)–(e) pass, (f) fails. K1: (a)(b)(c)(e) pass, (d) fails (z₃ = q⁵/(q⁴+q²+1) ≠ z_D; no
flavour). K2: (i) fails (b) at q ≠ 1; (ii) fails (a) (the [e,f] relation). K3: (c) fails (four
eigenvalues ±q, ±q⁻¹); K3′: (c) fails (eigenvalues q², −1, q⁻²). K4: members with X = Y reduce to
K0; the two transported members fail the braid relation at q ≠ 1 for p = 1, and (expected) for
p = q; any p solving it symbolically is reported.

## Decision rule

A construction is a closure candidate for `qou-ni4b` only if it meets (a)–(f) exactly over ℚ(q).
One that meets (a)–(e) but not (f) is reported as such, and whether it counts is the owner's call.
No construction is chosen by any numerical comparison with a measured value; none is used.

## Honesty clause

Exact sympy over ℚ(q) (and ℚ(p,q)); no float64. Failures are scope (a): not found in this class.
The bean stays in-progress whatever the outcome. No gluon is identified or selected.
