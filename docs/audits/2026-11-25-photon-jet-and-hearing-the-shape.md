# Where the photon lives, and whether you can hear the shape of a QOU

Session 2026-11-25, interactive child session. Beans `qou-y2o9` (epic), `qou-yidh` (Q1),
`qou-asw0` (Q2), `qou-t3qi` (critique). Photon = `def:photon`,
γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ ∈ H₃(R,q) (owner ruling 2026-11-18/20). Convention D,
z = q³/(q²+1), h = q − q⁻¹.

## §0 Pre-registered predictions (written and committed BEFORE any computation)

Write W = span_R{σ₀, σ₁, V}, V = σ₀σ₁⁻¹.

- **P1.** The first-order jet I/I² of H₃(q) at the trivial augmentation ε(σᵢ) = q is
  killed by [2]_q = q + q⁻¹. Over a field with [2]_q ≠ 0 it is zero; over R = ℤ[q^±] it is
  cyclic, ≅ R/([2]_q). Same at the sign augmentation ε(σᵢ) = −q⁻¹.
- **P2.** γ(φ) ∈ 1 + ker ε only on the hyperplane q(φ₀+φ₁) + φ₀₁ = 0 (trivial) or
  −q⁻¹(φ₀+φ₁) + φ₀₁ = 0 (sign). So "γ ∈ 1 + I" is not true of the photon family.
- **P3.** tr_M(γ) = 1 + z(φ₀+φ₁) + z(z−h)φ₀₁. φ₀ and φ₁ enter symmetrically.
- **P4.** In the Frobenius form G(x,y) = tr_M(xy) on W, G(σ₀,V) ≠ G(σ₁,V) generically:
  the σ₀↔σ₁ degeneracy of P3 is broken at bilinear (two-photon) order.
- **P5.** Photon filtration F_k = span of products of ≤ k elements of {1} ∪ W has ranks
  1, 4, 6 (F₂ = H₃); gr₂ has rank 2 with basis the classes of L₋ = σ₁σ₀ and e⁻ = σ₀σ₁σ₀;
  gr is not commutative.
- **P6.** The "su(2) triad" reading fails: the traceless parts of ρ₍₂,₁₎(σᵢ) are
  semisimple, not nilpotent, so σ₀, σ₁ cannot be raising/lowering operators.
- **P7.** Under convention D the single-photon response φ ↦ tr_M(γ(φ)) determines q
  (excluding q⁴ = −1, q² = −1).

## §1 Results against the predictions

All arithmetic exact (sympy over ℚ(q), or `Fraction`). Producers and witnesses:
`computations/probes/photon_jet_spectral/photon_jet_probe.py` →
`photon-jet-probe.witness.json`; `s5_gassmann_and_h4_filtration.py` →
`s5-gassmann-h4-filtration.witness.json`. Lean: `QOU/StandardModel/PhotonJet.lean`.

| | prediction | result | how |
|---|---|---|---|
| P1 | I/I² is [2]_q-torsion, zero over a field | **confirmed**: rank I = rank I² = 5 over ℚ(q) | probe; Lean `hecke_sub_mul_self`, `sub_eq_smul_sq` |
| P2 | γ ∈ 1+ker ε only on a hyperplane | **confirmed**: ε(γ) = 1 + q(φ₀+φ₁) + φ₀₁ (trivial), 1 − q⁻¹(φ₀+φ₁) + φ₀₁ (sign) | probe; Lean `augmentation_photon` |
| P3 | tr_M(γ) = 1 + z(φ₀+φ₁) + z(z−h)φ₀₁ | **confirmed** | probe |
| P4 | G(σ₀,V) ≠ G(σ₁,V) | **confirmed**: difference h(z−q)(z+q⁻¹); under D = −(q⁶−1)/(q(q²+1)²) | probe; Lean `gram_vertex_asymmetry(_factor)` |
| P5 | filtration ranks 1,4,6; gr₂ = ⟨L₋, e⁻⟩; gr not commutative | **confirmed** | probe |
| P6 | σ₀, σ₁ not raising/lowering | **confirmed**, and more (see §2.4) | probe |
| P7 | single-photon response determines q under D | **confirmed** except q⁴ = −1 | probe; Lean `audible_q` |

Additional measurements (not pre-registered, so read as exploratory):

- Two-photon trace, convention D: tr_M(γ(φ)γ(ψ)) minus its σ₀↔σ₁-relabelled copy is
  −(q⁶−1)/(q(q²+1)²) · (φ₀ψ₀₁ + φ₀₁ψ₀ − φ₁ψ₀₁ − φ₀₁ψ₁). The vertex weight couples to the
  difference φ₀ − φ₁.
- Photon filtration in H₄ with the sliding photon (owner ruling 2026-11-22), W₄ = span of
  σᵢ, σᵢ₊₁, σᵢσᵢ₊₁⁻¹ for i = 0, 1: ranks **1, 6, 15, 22, 24** at q = 7/5 and q = 11/3
  (ranks at a specialisation bound the generic rank from below; both values agree, and 24
  is the full dimension).
- S₅ = Aut⁺(Bring): 156 subgroups in 19 conjugacy classes, **0** Gassmann (almost-conjugate,
  non-conjugate) pairs.

## §2 Q1 — where the photon lives

### 2.1 Not in the augmentation jet I/I² (negative, proved)

The natural "first-order dual of the jet" of an augmented algebra (H, ε) is I/I², I = ker ε.
For H_n(q) this space is killed by [2]_q = q + q⁻¹, because (σ−q)² = −[2]_q(σ−q). So over any
field where [2]_q ≠ 0 (in particular at real q₀), I = I² and I/I² = 0. The same holds at the
sign augmentation. This is the semisimple-algebra fact that the trivial block is a direct
factor. Scope (b): the invariant is the quadratic Hecke relation. **The photon cannot be
placed in I/I² because that space is zero.** It is nonzero only over ℤ[q^±]/([2]_q), i.e.
at q = ±i, which is not the substrate.

Moreover γ itself is not in 1 + I: ε(γ) = 1 + q(φ₀+φ₁) + φ₀₁ ≠ 1 generically (P2). The
owner ruled on 2026-11-22 that the photon keeps the fixed constant term 1 and is not moved
to a norm-one definition, so the photon family is not an augmentation-normalised family.

The corpus already has the companion negative one level up: the jet object
J¹(S) = (S⊗S)/I² admits no bialgebra structure compatible with both sections
(`TwistedFrobeniusHopf/JetNoBialgebra.lean`, sorry-free). So reading (b) of the brief —
the photon as a primitive element of a Hopf structure on the jet — is blocked by an existing
theorem, not open.

### 2.2 Where it does live (precise, definitional)

The photon family is the affine 3-space 1 + W ⊂ H₃(R,q), W = span{σ₀, σ₁, V},
V = σ₀σ₁⁻¹. The "first order" in "first-order perturbation of the vacuum" is the degree in
the colour weights φ, not an ideal-adic order:

  γ(φ)γ(ψ) = 1 + (w_φ + w_ψ) + w_φ w_ψ,  w_φ = φ₀σ₀ + φ₁σ₁ + φ₀₁V.

So W is the tangent space of the photon family at the bare photon 1, and the two-photon
(γγ) term is the multiplication map W ⊗ W → H₃. This is the precise content of the external
discussion's reading (3), "(1+δ₁)(1+δ₂) = 1 + (δ₁+δ₂) + δ₁δ₂".

### 2.3 The photon filtration (the "q-tower of photonic information")

Define F₀ = R·1 and F_k = F_{k−1}·(R1 + W): the span of products of at most k photons.
In H₃ the ranks are 1, 4, 6: two photons already span H₃. The new directions at order 2 are
L₋ = σ₁σ₀ and the electron word e⁻ = σ₀σ₁σ₀ (the electron ruling of 2026-11; this is a fact
about spans, not a derivation of the electron). In H₄ with sliding photons the ranks are
1, 6, 15, 22, 24, so the tower has length 4.

The associated graded is **not commutative**: [σ₀, σ₁] ≡ −L₋ ≠ 0 in gr₂. So the tower is
not a symmetric-algebra (Fock-space) grading, and "multi-photon = Sym^k W" is false here.
F₁ is not closed under commutators either, so W is not a Lie subalgebra of H₃.

H₃(q) has no ℤ-grading that puts W in degree 1: it has no U(1) grading at all
(`no_scaling_of_hecke`, cited in the 2026-11-22 linking-neutrality ruling). The filtration
is the most one can have.

### 2.4 The reflection block and the "su(2) triad" claim

Project W into the two-dimensional (reflection, λ = (2,1)) block of H₃(q) and take trace-free
parts. Exact results:

- The three trace-free parts are linearly independent: Gram determinant of the form
  tr(XY) is −(q²−q+1)²(q²+q+1)²/(2q⁴) ≠ 0. So W maps onto **sl₂** of that block.
- The form has signature **(2, 1)** for real q: it is sl₂(ℝ) ≅ so(2,1), a Lorentzian form.
  It is not su(2), whose form is definite.
- The flip-symmetric direction σ₀ + σ₁ has norm exactly 2 for every q and is orthogonal
  to both σ₀ − σ₁ and V. The chiral plane span{σ₀−σ₁, V} has signature (1,1).
- V's trace-free part has norm (q²−q−1)(q²+q−1)(q⁴+q²+1)/(2q⁴); it is timelike for
  1/ϕ < q < ϕ (ϕ the golden ratio), which contains q₀.
- σ₀, σ₁ have semisimple trace-free parts (square = (q²+1)²/(4q²) ≠ 0), so they are not
  nilpotent and cannot be raising/lowering operators.

In the one-dimensional blocks σ₀ and σ₁ act identically, so σ₀ − σ₁ is seen only by the
reflection block. That is why the trace asymmetry of §1 vanishes exactly at z = q and
z = −q⁻¹, the two one-dimensional characters.

**Owner-facing caution (anti-fit).** The signature (2,1) and the timelike vertex are exact
algebraic facts about this block. Identifying them with 2+1 Lorentz symmetry, a photon
polarisation count, or a "longitudinal" mode is an interpretation, and none is proposed
here. In particular no "3 degrees of freedom" should be matched to the physical photon:
the physical massless photon has 2 helicities, and three parameters in γ is a fact about
the definition, not a prediction.

### 2.5 What would make γγ natural categorically

What is precise: γγ is multiplication W ⊗ W → F₂, and the reading-3 Frobenius selection
and linking-neutrality ruling (2026-11-21/22) act on the image. A categorical reason would
be a statement of the form "the photon is the universal first-order deformation of the
vacuum in a monoidal category, and γγ is its tensor square". §2.1 rules out the two
off-the-shelf candidates (augmentation jet, primitive elements of the jet bialgebra). A
candidate not yet tested: W as the image of the degree-1 part of a **braided** (not
symmetric) tensor algebra on V⊗V, with γγ the braided product. That is a conjecture shape,
not a result.

## §3 Q2 — can you hear the shape of a QOU?

Owner framing (2026-11-25, chat): the drum skin is the aether / observable layer; photons are
the perturbation waves. Precise version used here:

- **Drum** = the observable layer: the trace functional τ on the Hecke tower (Markov
  parameter z, aether parameter q, block weights y_λ). The corpus already calls q the
  "aether parameter" (`measurement-observation/observation-intention-intro.md`).
- **Sound** = the k-photon response functions φ¹,…,φᵏ ↦ τ(γ(φ¹)⋯γ(φᵏ)·x).
- **Hearing the drum** = recovering τ from the responses. **Hearing a state** = recovering
  x (a braid, up to conjugacy and Markov moves) from τ(γ⋯γ·x).

Results:

1. **The drum is audible (proved).** The one-photon response 1 + z(φ₀+φ₁) + z(z−h)φ₀₁ gives
   z and h. Under convention D these fix q unless q⁴ = −1 (`audible_q`). Since F₂ = H₃, the
   one- and two-photon responses determine τ on all of H₃; in H₄ four photons suffice.
   This is the opposite of Kac: the observable layer is spectrally rigid.
2. **States are not audible (literature + corpus).** Every response is a cyclic trace, so it
   factors through the cocenter H/[H,H], whose rank is the number of partitions of n. Mutant
   knots (e.g. Conway and Kinoshita–Terasaka) have equal HOMFLY polynomial, which is the
   Ocneanu trace, so distinct closed braids are trace-isospectral. The corpus already
   records the same phenomenon as "isospectral isobars" (p ≡ n ≡ ³He at H₃,
   `docs/audits/2026-06-28-brane-tower-formalize-first-plan.md`) and the Kac–Sunada analogy
   (`braids-and-knots/bar-involution-geometric-kac-sunada.md`), and proves that a trace
   cannot tell a word from its flip-reverse (`trace_flip_reverse`). This is the Kac answer:
   **no**. (Citation of mutant HOMFLY equality is from memory; the papers are not in
   `library/` or in `qou-private/library/`.)
3. **The geometric drum (Bring's surface).** Laplace isospectrality of Bring's surface is not
   settled here. Sunada's method with G = S₅ gives nothing: S₅ has no Gassmann pair (§1).
   An isospectral partner of Bring would need a Gassmann triple in a larger group acting on a
   cover. Literature recalled but not held in either library: Sunada (1985), Buser's
   isospectral surfaces, Brooks–Tse genus-4 examples, Wolpert's genericity of spectral
   rigidity. The closest held source is Cook's thesis (`library/210811825v1`, eigenvalues of
   surfaces with large symmetry groups). Status: **open in this corpus**; settling it needs
   either a Gassmann triple (G, H₁, H₂) with Bring = X/H₁, or a proof of rigidity.

## §4 Critique of the external discussion (pasted by the parent)

- "Three DOF is expected in a medium / Proca / Riemann–Silberstein." Correct as physics
  literature, but not connected to QOU by anything computed here. Using any of them to
  justify the photon's three parameters is matching a parameter count to physics, which the
  anti-fit rule forbids.
- "The 1 is the vacuum; γ is a group-like perturbation." Precise (§2.2), and the owner's
  2026-11-22 ruling fixes the constant term at 1.
- "γ ∈ 1 + I (augmentation splitting)." **False** for the photon family (P2), and the
  first-order jet I/I² is zero anyway (§2.1).
- "(1+δ₁)(1+δ₂): δ₁δ₂ is γγ." Precise (§2.2–2.3).
- "σ₀, σ₁, σ₀σ₁⁻¹ mirror su(2): J± and J_z." **Half right, half wrong.** They do give a
  basis of sl₂ in the reflection block. But the real form is so(2,1), not su(2); σ₀, σ₁ are
  not raising/lowering operators; and the distinguished axis is σ₀ + σ₁, not V.
- Its question: "do φ₀, φ₁ behave as degenerate transverse modes and φ₀₁ as distinct?"
  Answer: at one photon, yes, trivially (σ₀ and σ₁ are conjugate). At two photons, no: the
  vertex weight couples to φ₀ − φ₁ with coefficient ∝ (q⁶−1), which is nonzero under
  convention D and vanishes only for the one-dimensional traces. So the triad is not
  "two degenerate + one distinct"; it is one symmetric axis σ₀+σ₁ plus a chiral plane.
- "Braid medium with locally varying q(x)." Nothing here models a varying q; untested.

## §5 Cross-check of the external follow-up predictions (pasted by the owner, same day)

The owner pasted a second round from the same external AI, with predictions written before
it saw these results. Checked exactly in
`computations/probes/photon_jet_spectral/external_predictions_check.py` →
`external-predictions-check.witness.json`.

| its claim | verdict | evidence |
|---|---|---|
| γ−1 ∈ ker ε₊ iff q(φ₀+φ₁)+φ₀₁ = 0 | **correct** | P2 |
| I² = I at generic q, so I^k/I^{k+1} = 0 | **correct** | P1, `sub_eq_smul_sq` |
| a non-collapsing I-adic jet appears at q = 1 | **imprecise**: over ℤ[q^±], I/I² ≅ R/([2]_q); torsion lives at [2]_q = 0, i.e. q = ±i. At q = 1 it gives ℤ/2 (from [2]₁ = 2), which vanishes over any field of characteristic ≠ 2 | `hecke_sub_mul_self` |
| word-length filtration is the right one | **agrees with §2.3** | P5 |
| H₃(q) carries no bialgebra coproduct for q ≠ ±1 | **false as stated**. A coproduct with σᵢ group-like is impossible (the product eigenvalue −1 would need (−1)² = −h + 1, i.e. h = 0; witness). But over ℚ(q), H₃(q) ≅ ℚ(q) ⊕ ℚ(q) ⊕ M₂(ℚ(q)) ≅ ℚ(q)[S₃] (Tits deformation; the algebra is split), so it does carry a Hopf structure transported from the group algebra, just not one in which σᵢ is group-like | witness `B_grouplike_constraint_at_eig_-1` |
| rank of μ_sym : Sym²(W) → H₃ is 5, missing [σ₀,σ₁] | **correct** | rank 5; [σ₀,σ₁] not in the image |
| linear trace sees only φ₀+φ₁; σ₀−σ₁ ∈ [H₃,H₃] | **correct** | P3 |
| *-Gram (σ* = σ⁻¹): tr(V*σ₀) = z, tr(V*σ₁) ≠ z | **correct**; difference h(z−q)(z+q⁻¹), the same factor as §1 | witness `2.2_diff` |
| S₅ has no Gassmann pair | **correct** | §1 |
| "smallest symmetric group with a Gassmann triple is S₆, via the outer automorphism" | **reason is false**. The point-stabiliser S₅ ⊂ S₆ contains 10 transpositions; its image under the outer automorphism (PGL(2,5) on P¹(F₅)) contains none and has 10 elements of type (2,2,2) instead. They are not almost conjugate | witness `3_profile_*` |
| mirror QOU (A^op, q⁻¹) may be isospectral | **not under the photon response**: h(q⁻¹) = −h(q), so the one-photon response tells q from q⁻¹ unless q = ±1 | `audible_q` hypotheses |

## §6 Verification

- Probes: exact (sympy over ℚ(q), `Fraction`); no floating point in any committed script.
- Lean: `QOU/StandardModel/PhotonJet.lean`, `lean -DautoImplicit=false -s 65536`, exit 0,
  against the restored cache plus a lean-direct olean of `QOU.StandardModel.Photon` (not in
  the cache seed). `#print axioms` on all six theorems: `propext`, `Quot.sound`, and
  `Classical.choice` for the two field lemmas. No `sorryAx`.
- No content block is added: §2.1, §2.4 and §3.1 are theorems, but they are small and
  should go into a block only if the owner wants them in the paper.

## §7 The photons as a tangent space (owner question, same day)

Owner: *"The photons span an R module (3 dim), can we interpret that as a tangent space?"*
Yes, in a precise sense, and it reconciles the "first-order dual of the jet" idea with the
negative of §2.1. Measured in the same exact setting (H₃ over ℚ(q)).

- **The ambient group.** The units of H₃ form an algebraic group G = GL₁(H₃); over ℚ(q),
  G ≅ G_m × G_m × GL₂. Its tangent space at 1 is Lie(G) = H₃ with the commutator bracket.
  The tangent vectors are the dual-number points 1 + εx, x ∈ H₃, ε² = 0.
- **Photons sit in G near 1.** det ρ_reg(γ(φ)) factors as q⁻⁷ times ε₊(γ)·q, ε₋(γ)·q, and
  the square of the reflection-block determinant. It equals 1 at φ = 0, so γ(φ) is a unit on
  a Zariski-open neighbourhood of the bare photon. It fails to be a unit exactly where one of
  the three block images vanishes.
- **Tangent space.** The photon family is a 3-dimensional smooth subvariety of G through 1,
  and its tangent space there is W = span{σ₀, σ₁, V} ⊂ Lie(G). The γγ product is the group
  multiplication restricted to the family; to first order it is addition in W.
- **The first-order dual.** The cotangent space of the photon family at 1 is m/m², where m
  is the ideal of the bare photon in the family's coordinate ring R[φ₀, φ₁, φ₀₁]. It has
  rank 3, and the colour weights φ₀, φ₁, φ₀₁ are its basis. This is where the I/I² idea
  lives non-trivially: in the coordinate ring of the photon variety, not in H₃ itself.
- **Not a subgroup.** W is not closed under the bracket. The Lie algebra W generates has
  dimension 5: everything except the identity direction. So infinitesimal photons generate
  every direction of Lie(G) except the overall scale. The family is a 3-dimensional slice,
  not a Lie subgroup, and "the photon group" does not exist as a subgroup of G.

What is NOT established: a reason why the slice is this W, rather than some other
3-dimensional subspace. The choice is the owner's ruling (def:photon), not derived here.

## §8 Follow-up round (owner: "1y, 2y, 3y, W is tangent = y")

### §8.0 Pre-registered predictions (committed before computing)

- **P8 (tangent-line factorisation).** In H₃(q), 1, V, V² are linearly independent and
  V³ = 1 + h²V − h²V². Hence V³ = (1 + aV)(1 + bV) has exactly one unordered solution,
  {a, b} = {qh, −q⁻¹h}: the photon weights of the Borromean factorisation are forced by the
  minimal polynomial of V, not chosen.
- **P9.** Aut(Bring) including orientation-reversing maps, S₅ × C₂ (order 240), has no
  Gassmann pair either.
- **P10.** Let R ⊂ W⊗W be the kernel of W⊗W → gr₂ H₃. The quadratic algebra T(W)/(R) has
  degree-3 part 0, so gr H₃ (ranks 1, 3, 2) is a quadratic algebra generated by the photons.

### §8.1 Results

| | prediction | result |
|---|---|---|
| P8 | V³ = 1 + h²V − h²V²; unique collinear factorisation {qh, −q⁻¹h} | **confirmed** (rank{1,V,V²} = 3; coefficients 1, h², −h²) |
| P9 | S₅ × C₂ has no Gassmann pair | **confirmed**: 535 subgroups, 57 classes, 0 pairs |
| P10 | T(W)/(R) has degree-3 part 0 | **confirmed**: dim R = 7, Hilbert series 1 + 3t + 2t² = that of gr H₃ |

**Not pre-registered, and stronger than P8.** Solving γ(φ)γ(ψ) = V³ over all six colour
weights (Gröbner basis, finite solution set, all complex solutions) at q = 3/2 and q = 7/5
gives exactly two solutions: φ = (0,0,qh), ψ = (0,0,−q⁻¹h) and the same pair swapped. So the
two factors are forced to be pure vertex photons and their weights are forced. Two rational
specialisations, not a generic-q proof.
(`borromean_general_factorisation_probe.py`, witness `borromean-general-factorisation.witness.json`.)

### §8.2 What "W is tangent" buys downstream (owner question)

1. **A derivation gap narrows: the Borromean photon weights.** The 2026-11-21 ruling row
   records "the photon weights qh, −q⁻¹h are still ruled, not derived". On the tangent line
   R·V, a product of two photons is 1 + (a+b)V + abV², and V's minimal polynomial forces
   a + b = h², ab = −h², so {a, b} = {qh, −q⁻¹h}. Proved in Lean given that 1, V, V² are
   independent (`QOU.PhotonTangent.borromean_weights_forced`; independence measured, not
   proved). Over all photons, not only the line, the measured solution set is the same pair
   at two rational q. **What is still not derived:** why the Borromean core should be a
   product of two photons at all. That premise is the γγ reading of β_Bor; once it is
   granted, nothing about the weights is chosen.
2. **Factorisation into collinear photons becomes root-finding.** A word P(V) with
   P(0) = 1 factors into k photons on the line R·V iff P, reduced by V's minimal polynomial
   (x−1)(x² + (1+h²)x + 1), splits over R with constant term 1. This is a reusable test for
   other γγ candidates on a single vertex direction.
3. **Exposition.** The constant term 1 (owner ruling 2026-11-22, "keep the photon as one
   fixed") reads as the base point of the family, not a normalisation. The colour weights are
   coordinates (a cotangent basis). "Bare photon = identity" is "the tangent vector 0". To
   first order γγ is addition of colour weights (`photon_mul_photon_of_sq_eq_zero`); the
   genuine two-photon content is the second-order term w_φw_ψ, which is exactly what the
   Frobenius and linking-neutrality selections act on.
4. **A structural fact for the γγ question.** gr H₃ is the quadratic algebra on the photons
   with 7 relations (P10). So "photons generate everything, with relations only in degree 2"
   is a theorem-shaped measurement, and the braided-tensor-algebra question becomes the
   precise one: is the 7-dimensional relation space an eigenspace of a braiding?
   (`QOU/StandardModel/PhotonBraidedConjecture.lean`, conjecture carrier, no instance.)
   The two standard braidings on a 3-dimensional space are ruled out by dimension: their
   eigenspaces have dimensions (6, 3) for the U_q(gl₃) vector and (5, 3, 1) for U_q(sl₂)
   spin 1, and no sum of these is 7. Scope (a): this excludes those two braidings, not
   braidings in general.
5. **What it does not buy.** It does not select W (the ruling does), does not give a
   grading (H₃ has none), and does not touch the L2 precision rows. The Lie algebra W
   generates is 5-dimensional, missing only the identity direction; I found no downstream
   use for that and record it as a fact only.

### §8.3 Bring's surface (owner "2y")

Sunada's method needs a group G acting on a cover X of Bring with a Gassmann pair H₁, H₂
and Bring = X/H₁. Neither Aut⁺(Bring) = S₅ nor Aut(Bring) = S₅ × C₂ contains a pair (§1, P9),
so any partner must come from a group acting on a proper cover. Next measurable step: the
finite quotients of the genus-4 surface group that contain S₅ (equivalently, finite-index
normal subgroups of the (2,4,5) triangle group, since Bring is H/Γ with Γ ⊲ Δ(2,4,5) of
index 120; Riemann–Hurwitz: 120·(1 − 1/2 − 1/4 − 1/5) = 6 = 2g − 2 at g = 4), searched for a Gassmann pair whose one member's quotient is Bring. This is a
finite-group computation (GAP's library of quotients of Δ(2,4,5) would do it; GAP is not
installed here). Rigidity side: no route found in the held literature. Status: open.
