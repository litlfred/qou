# SM uploads — round-2 reads (bean qou-y139)

**Date:** 2026-08-01. **Scope:** full reads of the four remaining
uploads from the SM batch (`5d1385d1`), each targeted at the
appendix-standard-model gap ledger. Reads performed by four parallel
agents (pypdf extraction); per-paper section references below are to
the PDFs in `library/`. Registry:
[`library/sm-uploads-intake.json`](../../library/sm-uploads-intake.json).
Prior round: `docs/audits/2026-07-31-sm-lit-analysis-bean-workplan.md`.

## 1. Bilson-Thompson–Markopoulou–Smolin, `0603022v2` [bilsonthompson2007]

Helon braids embedded as "encapsulated braids" in framed (ribbon)
spin-network graphs; states H = ⊕_Γ H_Γ over embedded ribbon graphs,
braid sector factored as H_Γ^T ⊗ H_Γ^B (§II–III, Fig. 4).

**Conservation results (the qou-q377 payload):**

- The braid-and-twist sector H^B is a **noiseless subsystem** of the
  evolution algebra (expansion / contraction / exchange moves): the
  moves commute with braiding *and twisting* of edges (§III). So
  **ribbon twist is conserved under evolution** — at
  commutation-argument level, not via a twist-specific invariant.
- Their **reduced link invariant** RL[Γ] (§V.A, Eqs. 9–10) is
  preserved by the moves and lies in the commutant of the evolution
  algebra — but RL is computed from edges-as-curves and **does not see
  twist**. The 15 first-generation states are distinguished by reduced
  links *together with* twist data (§VI).
- **Gap worth recording:** twist conservation and twist-valued
  invariants are separate things in their framework too — there is no
  published twist-valued conserved *invariant*, only conservation of
  the twist data by commutation. `def:strand-twist-datum` +
  `TwistDatum.totalTwist_perm` is precisely the missing invariant-level
  statement, on the QOU side.
- Honest no-go they admit (§VIII.C): exact noiselessness means the
  braid sector is **completely decoupled** from the dynamics — the
  evolution algebra cannot generate SM interactions; their charge
  quantum t = e/3 per ±2π twist (§IV, Eq. 18) matches the battery
  normalisation, but their two selection rules are "ad hoc
  assumptions" (§VI).

## 2. Baez–Schreiber, `0511710v2` [baez-schreiber2007]

Strict 2-groups ↔ Lie crossed modules (G, H, t, α) (Def. 2, §2);
2-connections as holonomy 2-functors on the path 2-groupoid with
pseudonatural transition data (Def. 22, §4); **fake flatness**
F_A + dt(B) = 0 iff surface holonomy is well-defined (Thm. 23).

**Payload for the twist datum and the groupoid categorification:**

- The gauge-invariant surface content is forced into **ker(dt), an
  abelian ideal of 𝔥** (Breen; p. 27): "well-behaved holonomies force
  a 2-connection to be somewhat abelian." Independent structural
  corroboration that the beyond-writhe U(1) datum should be abelian
  and central — the shape `def:strand-twist-datum` has.
- The **loop 2-group** (ΩG, Ω̂_kG) with U(1) = ker t central and
  integer level k (Example 9) is the closest published structure to
  "a U(1) hypercharge datum riding centrally over nonabelian crossing
  data."
- **Automorphism 2-group** AUT(H) (Example 8): "any object in a
  2-category has a 2-group of symmetries" — the direct template for
  categorifying `def:gauge-action-groupoid` one level up (gauge moves
  = objects, equivalences-of-moves = morphisms); the current groupoid
  is the Ob-level truncation. Caveat: such automorphism 2-groups are
  generically weak, not strict.

## 3. Baez–Huerta, `1003.4485v2` [baez-huerta2011]

Expository catalogue of 2-group families (§4): shifted abelian bH,
Poincaré 2-group, tangent 2-group, INN(G), AUT(H), string 2-groups.

**Payload — the categorical home for the per-strand twist:**

- **"Any group representation is secretly a 2-group"** (§4.2, p. 32):
  crossed module with H an abelian G-representation and **t = 0**. This
  is the natural home for the strand twist datum: the twist lives in
  abelian H, gauge transformations rotate it through α, and t = 0
  means it never feeds back into the crossing (1-morphism) level —
  matching the Lean facts (twist multiset gauge-invariant, independent
  of the braid word).
- For the proved single-fibre SU(2): the only construction placing a
  U(1) categorically above a compact simple G is the **level-k string
  2-group** STRING_k(G) via 1 → U(1) → Ω̂_kG → ΩG → 1, one central
  extension per integer k, all nontrivial for k ≠ 0 (§4.6, pp. 41–42).
  If the framework's U(1)_Y is to *emerge* rather than be postulated,
  this is the published candidate mechanism: an integer level above
  the SU(2) fibre, WZW-anomaly-sourced.
- U(1) gerbes classified by **H³(M, ℤ)** (§5.3) — the
  integer-cohomology anchor for any global U(1)-twist datum.

## 4. Dubois-Violette–Todorov, `1808.08110v1` [dubois-violette-todorov2018]

G_SM = SU(3)×SU(2)×U(1)/ℤ₆ realized as the subgroup of
Spin(9) = Aut(J₂⁸) preserving the splitting 𝕆 = ℂ ⊕ ℂ³ (Sec. 4,
eq. 4.1); connected form U(3)×SO(3); equivalently
(SU(3)×SU(3)/ℤ₃) ∩ Spin(9) inside F₄ = Aut(J₃⁸).

**Payload — a concrete faithful colour module (qou-ni4b):**

- Sec. 3 (eqs. 3.3–3.6): the three off-diagonal octonions of a J₃⁸
  element map to H₃(ℂ) ⊕ **M₃(ℂ)**, and colour acts as
  **M ↦ U M V\*** — faithfully, as three copies of the fundamental
  ℂ³, one per off-diagonal-octonion index i ∈ {1,2,3}. A faithful
  su(3) action on a natively **3-strand-indexed** space: the closest
  published candidate for instantiating `ColourStabilizerAction`
  (the class needs an injective ℚ-linear 𝔰𝔲(3) → End(V); the minimal
  faithful candidate is the fundamental ℂ³ itself, dim_ℚ = 6 ≥ 3
  strands' worth of state space, consistent with
  `colour_needs_three_strands`).
- The ℤ₆ is **derived geometrically** (kernel of
  SU(3)×SU(2)×U(1) → its image in Spin(9); ℤ₃ from U(3), ℤ₂ from
  SO(3)) and coincides with Baez–Huerta's representation-kernel ℤ₆ on
  the one-generation module — the same condition
  (τ/3 + w/2 + Y/2 ∈ ℤ) the strand-twist battery implements. Two
  independent derivations of the battery's ℤ₆, one geometric, one
  representation-theoretic.
- **Gap/correction:** the explicit algebraic hypercharge operator Y is NOT in
  this paper, and the prior companion-pointer was wrong. The group-level
  `U(1)`/`Z6` geometry is DV/Todorov; the explicit weak-hypercharge generator
  is instead in C. Furey, arXiv:1806.00612, eq. (43), with arXiv:1611.09182 as
  the longer derivation background.

## Consequences for the gap ledger

| gap | movement |
|---|---|
| hypercharge Y (`qou-q377`) | Twist conservation has literature precedent (noiseless-subsystem commutation), but no published twist-valued *invariant* — the QOU `TwistDatum` lemmas are that statement. Categorical home identified: abelian-H crossed module with t = 0; emergence mechanism candidate: level-k string extension above the proved SU(2). Literature operator source corrected: Furey 1806.00612 eq. (43) (with 1611.09182 as background), not DV/Todorov 1806.09450. |
| colour action (`qou-ni4b`) | Concrete faithful candidate module found: M₃(ℂ) column action (DV–T Sec. 3). Constructing the ℚ-form of 𝕆 = ℂ⊕ℂ³ at the corpus's fixed imaginary unit and exhibiting Φ on ℂ³ is now a *derivation route*, not a search. |
| ℤ₆ battery | Doubly grounded: geometric (F₄ stabilizer) + representation-kernel (trivial-action subgroup) derivations agree. |
| truncation freeze-out | No movement — all four papers either postulate the embedding or admit the dynamics gap (BT–M–S §VIII.C explicitly). |
