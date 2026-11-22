# PREREG — a strand that "naturally interacts with the octonions" and carries colour

Issue #9096 / PR on `claude/helon-battery-chirality-2026-11-22`. Bean context: `qou-ni4b` (no colour
action on qou's own state space compatible with the braiding), `qou-cb3r` (octonion colour
stabiliser vs the tower's colour). Written and pushed **before** any number below is computed.

Owner framing (verbatim): *"So what we need is somehow a strand that naturally interacts with the
octanians ...."*; *"Could it be something in with octanians and the su(3) associated to them?"*;
added mid-task: *"We have Brings surface and we have the handles. Those should somehow correspond
to i, j and k as directions."*

Rulings respected: photon γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ ∈ H₃(q); Hecke σ² = (q−q⁻¹)σ + 1,
formal q; exact arithmetic only; **the gluon is open — this probe identifies candidate families
and what forces / excludes members; it selects nothing.**

## 0. The structural issue, stated first

𝕆 is not associative, so 𝕆 itself cannot be the fibre of a strand in an associative monoidal
tensor power whose structure maps use the octonion product. Every candidate below replaces 𝕆 by an
associative or representation-theoretic shadow of it:

- its **left-multiplication algebra** ℂ⊗𝕆 → Cl(6) ≅ M₈(ℂ), acting on a minimal left ideal ℂ⁸
  (Furey; Gresnigt 2018, `library/arxiv-1803.02202v2`), which decomposes under su(3)⊕u(1) as
  **1 ⊕ 3 ⊕ 3̄ ⊕ 1**;
- its **automorphism group** G₂ acting on Im 𝕆 = 7 = 1 ⊕ 3 ⊕ 3̄ under su(3) = Stab_{G₂}(e);
- the quantum group U_q(g₂) on its 7-dim module V₇ (the q-deformation of Im 𝕆).

Already in the corpus (not re-derived; cited): classical sl₃ commutes with Jimbo Ř only at q = 1
(`primitive_commute_rCheckN_iff`, `docs/audits/2026-11-15-colour-stabilizer-bridge.md` §0 item 3);
every U_q(g₂)-intertwiner of V₇⊗V₇ that preserves 3⊗3 is scalar there
(`computations/eightfold/quantum-g2-braiding-on-colour-triplet.witness.json`, commutant dim 4);
PR #9059 (as relayed): colour as a position label is consistent, colour moving with the strand in
the classes K4 / colour+spin forces q² = 1 (scope (a)); the Jimbo (C³)ⁿ tower carries U_q(gl₃)
colour and convention D is its rank-2 colour-breaking twist with every colour singlet in D's radical.

## 1. Candidate strand types and the exact question for each

### S1 — the G₂ strand: V₇ with a U_q(g₂)-equivariant braiding

Question: does there exist **any** U_q(g₂)-equivariant operator x on V₇⊗V₇ with exactly two
eigenvalues (Hecke type, any ratio t) satisfying the braid relation on V₇^{⊗3}? (The canonical
U_q(g₂) Ř has four eigenvalues on 1, 7, 14, 27 by Drinfeld's formula; Kuperberg's G₂ spider,
`library/kuperberg-1996-cmp-180-109-spiders`; that alone rules out Ř itself, cited not computed.)

Method: exact commutant End_{U_q(g₂)}(V₇⊗V₇) at sample q ∈ {2, 3} over ℚ (same module and Jantzen
coproduct as `quantum_g2_braiding_on_colour_triplet_probe.py`); primitive idempotents P_λ; for every
split of {1,7,14,27} into S ⊔ Sᶜ (7 classes) test x = P_S + t·P_{Sᶜ}, t ≠ 0, 1, for the braid
relation x₁x₂x₁ = x₂x₁x₂, with t a free variable (D(t) is cubic in t; compute its coefficient
matrices and their common roots). Arithmetic: sympy ℚ for the projectors; braid products mod a
prime p < 2²⁶ (a nonzero residue proves the identity fails over ℚ at that q; any surviving t is
re-checked over ℚ).

- **PASS (a G₂-natural Hecke strand exists at that q):** some (S, t) satisfies the braid relation
  with t ≠ 0, 1.
- **FAIL:** none does, at q = 2 and q = 3. Scope: equivariant two-eigenvalue braidings on V₇ only;
  failure at a sample q proves failure of the generic identity (a generic identity specialises).

### S2 — the Furey strand: ℂ⁸ = 1 ⊕ 3 ⊕ 3̄ ⊕ 1 (minimal ideal of Cl(6)) with Jimbo Hecke braiding

The braiding is Jimbo's Ř for U_q(gl₈) on ℂ⁸ with each colour block contiguous (Levi). Colour is
U_q(sl₃) acting through the **Hopf map** f = (ι₃ ⊗ ι₃̄∘θ)∘Δ into the Levi U_q(gl₃)⊗U_q(gl₃) ⊂ U_q(gl₈),
θ the Dynkin-diagram automorphism of A₂ (a Hopf automorphism sending 3 to 3̄).

Questions and pass/fail:
- **Q2a (Hecke):** Ř satisfies (Ř−q)(Ř+q⁻¹) = 0 and the braid relation on (ℂ⁸)^{⊗3}, exactly over
  ℚ(q). Expected PASS (Jimbo); a fail means a coding error, not physics.
- **Q2b (colour is a U_q(sl₃) rep, of type 1⊕3⊕3̄⊕1):** the images of E_c, F_c, K_c satisfy the
  U_q(sl₃) relations (KE, KF, [E,F], quantum Serre) on ℂ⁸, and the weights of the four blocks are
  0, those of 3, those of 3̄, 0.
- **Q2c (colour moves with the strand without q² = 1):** (f⊗f)Δ(u) on ℂ⁸⊗ℂ⁸ commutes with Ř for u
  in {E_c, F_c, K_c}, exactly over ℚ(q). PASS = commutes at generic q.
- **Q2d (classical limit):** at q = 1 the colour action on 3 ⊕ 3̄ is x ⊕ (−xᵀ) up to a basis change
  of the 3̄ block, i.e. Furey's su(3). Checked by comparing weights and the q = 1 matrices.
- **Q2e (convention D):** classify all diagonal Markov twists Tr(D^{⊗n}·) for Ř on ℂ⁸
  (Ocneanu condition on the support), then those that are colour-invariant
  (Tr(D^{⊗n} Δ⁽ⁿ⁾(u) X) = Tr(D^{⊗n} X Δ⁽ⁿ⁾(u)), checked n = 1, 2). Report the family and the
  Markov parameter z for each; report which colour-invariant twists give z_D = q³/(q²+1). This is
  a classification, not a selection.
- **Q2f (photon-like octet element):** by double centraliser, everything in the image of H_n(q)
  commutes with colour, so the colour-adjoint component of every braid word, and of every
  γ(φ) ∈ H₃(q), is zero. Checked: the ad-action of colour on the images of σ₀, σ₁, σ₀σ₁⁻¹ in
  End((ℂ⁸)^{⊗3}) vanishes. Consequence to be stated: a colour-octet object cannot be a braid word
  in this setting; it lives on the commutant (Hopf) side.

Robustness: Q2a–Q2c rerun with a second block order (3, 1, 3̄, 1).

### S3 — 3 ⊕ 3̄ ⊕ 1 (Im 𝕆 under su(3)) with Jimbo U_q(gl₇)

Same as S2 with one singlet removed (the G₂ decomposition of Im 𝕆). Only Q2e changes: colour-
invariant twists have ranks from block sums {1, 3, 3}. Reported from the same code.

### S4 — Bring handles ↔ 1, i, j, k / 𝕆 (owner sub-question, scope-limited)

Question: is there an Aut-equivariant structural map from H¹(Bring; ℝ) (dim 2g = 8) to ℍ⊕ℍ, ℍ, or
𝕆 whose target structure (unit, multiplication, Im-part) is preserved, beyond the dimension
coincidence 8 = dim 𝕆?

Method: character of S₅ = Aut(Bring) on H¹(Bring; ℂ) by Lefschetz (tr g = 2 − #Fix(g), g ≠ 1),
#Fix from the (2,4,5) signature computed over S₅ by enumeration (exact integers); decompose over
S₅ and A₅.

Pre-declared structural criteria:
- an equivariant **unital** algebra structure (𝕆 or ℍ⊕ℍ with G acting by automorphisms) needs a
  G-fixed unit, i.e. a trivial summand; FAIL if the trivial multiplicity is 0;
- an equivariant identification of a 3-dim piece with Im ℍ = (i, j, k) with G acting by algebra
  automorphisms needs a 3-dim real summand on which G acts through SO(3); FAIL if no 3-dim
  irreducible summand occurs;
- a G₂-route needs G → G₂ with H¹ ≅ 1⊕7 restricted; FAIL if no trivial summand.
- Anything else (an 8-dim real orthogonal rep identified with 𝕆 as a vector space) is a dimension
  count and is reported as **not evidence**.

## 2. What is not tested

No q-deformed octonion algebra; no U_q(g₂) on 1⊕7 (non-commutative 15-dim commutant); no
U_q(so₇)/U_q(so₈) (BMW, three eigenvalues, not Hecke by the same eigenvalue count); no coideal /
QSP colour (another agent, `PREREGISTRATION-coideal-colour.md` on #9059); no spin; no numbers at
q₀ (nothing here is a comparison with measurement).

## Addendum A (written before any S2 number; pushed alone)

**Correction to the S2 setup, found while coding, before computing.** The map
f = (ι₃ ⊗ ι₃̄∘θ)∘Δ is an algebra map but **not** a Hopf map: Δ is a coalgebra map only for a
cocommutative Hopf algebra. So S2 has no a-priori guarantee, and Q2c is a genuine test. It is
sharpened to two sub-tests on ℂ⁸⊗ℂ⁸:

- **Q2c-Levi (control):** Δ_{gl₈} of the Levi elements ι₃(x) and ι₃̄(θx) separately commute with
  Ř (expected, Jimbo). This is colour as **two independent** quantum gl₃'s on 3 and 3̄.
- **Q2c-diag (the test):** one U_q(sl₃) acting on 3 ⊕ 3̄ through its own coproduct,
  E_c ↦ ρ(E_c)⊗ρ(K_c) + 1⊗ρ(E_c) (and the three other standard coproduct conventions), with
  ρ(K_c) acting on **both** blocks. PASS iff the commutator with Ř vanishes at generic q. If it
  vanishes only at q² = 1 (or q = 1), that is the octonionic form of the known obstruction.

**Added candidate S5 (post-hoc in the sense that it was added after S1–S4 were registered, but
before any computation):** the **oriented** colour strand. 3̄ is not a separate fibre: it is the
U_q(gl₃) strand ℂ³ with reversed orientation, so Im 𝕆 = 1 ⊕ 3 ⊕ 3̄ is read as "one coloured strand,
two orientations, plus a colour-neutral line". The orientation bit is the corpus's charge-conjugation
bit (`2026-11-15-colour-stabilizer-bridge.md` §0 item 2: su3(e) = su3(−e), L_{−e} = −L_e). Mixed
crossings use R_{V,V*} = (id ⊗ t)(R⁻¹) from Jimbo's R; the algebra is the quantised walled Brauer
algebra (Kosuda–Murakami; Leduc), Schur–Weyl dual to U_q(gl₃) on V^{⊗r}⊗V*^{⊗s}.

- **Q5a:** R_{V,V*} intertwines the genuine U_q(gl₃) coproduct action on V⊗V* (V* via the antipode),
  exactly over ℚ(q). PASS = colour moves with the strand at generic q.
- **Q5b:** mixed braid (Yang–Baxter) relations on V⊗V*⊗V and V*⊗V⊗V, exactly.
- **Q5c:** the monodromy M = Ř_{V*,V}Ř_{V,V*} on V⊗V* has exactly two eigenvalues, on 1 and 8;
  report them and the octet projector P₈ as an element of span(1, e) (e the q-contraction).
  This names a colour-adjoint **channel**; it does not select a gluon.
- **Q5d:** the photon letters live on same-orientation strands, H_r(q) ⊂ walled Brauer; check that
  σ₀σ₁⁻¹ on V⊗V⊗V commutes with colour (it must; Jimbo) — no colour-octet braid word.
