# τ-assignment coherence program: orbit invariants, 1ppq relevance, and the Habiro bridge

**Date**: 2026-07-26 · **Branch**: `claude/5two-habiro-tail-bar-odd-l0k3ol` ·
**PRs**: #4340, #4362, #4366, #4373 (all merged or in flight)

## 1. What was proved (the program record)

| Result | Where | Status |
|---|---|---|
| `(fᵢfⱼ)^m = 1` at every bond order; `simple_injective` for EVERY Coxeter system, zero hypotheses | `CoxeterGeometricRepresentationFull.lean` (#4340) | sorry-free |
| Strict pair-independence of the τ-assignment REFUTED at A₃ (explicit witness) | `HeckeTauAssignmentCanonicity.lean` (#4340) | sorry-free, scope-(a) |
| Diagram-symmetry edges coherent (pullback) | `HeckeTauAssignmentCoherence.lean` (#4340) | sorry-free |
| W-conjugation edges coherent; pair-swap obstructed **target-side** (no function `T` with `τ' = T∘τ`) | `HeckeTauAssignmentSwapConjugation.lean` (#4362) | sorry-free |
| THE ASSEMBLED FUNCTOR: marked-pair category; `tauAssignment_hom_coherent` engine; natural transformation; `Core` groupoid restriction | `HeckeTauAssignmentGroupoidFunctor.lean` (#4366) | sorry-free |
| Pasted square (tower × groupoid); `PairCoherent` gauge discipline; cell Markov trace = ORBIT INVARIANT | `HeckeTauAssignmentOrbitInvariants.lean` (#4373) | sorry-free |
| Diagram symmetries preserve length; `q = i` monodromy DIAGRAM-equivariant | `HeckeTauAssignmentMonodromyEquivariance.lean` (#4373) | sorry-free |

Canonicity resolution: **not** a pair-independent map (refuted) but a
coherently indexed family — a natural transformation on the marked-pair
groupoid.

## 2. Relevance to the categorical-action → mass-binding 1ppq path

**No numeric delta.** Nothing here changes any MeV value; L1/L2
dashboards untouched (L2 stays 2/7). The machinery lives at the fibre
monodromy point `q = i`, not at the archimedean `q₀`.

**Three structural contributions to the canonical chain:**

1. **The "canonical" in `tr_M` is now machine-checked at the gauge
   level.** The chain step "categorical action → Hecke → Markov trace"
   involves gauge choices (which pair, which parabolic, which cell).
   `cellMarkovTrace_pairCoherent` proves the trace — the object the
   mass formula consumes (`F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`) — is
   marked-pair-gauge independent; `trM4_iota34_stabilizes` (merged
   earlier) covers the rank-tower direction. Both coherence directions
   of `tr_M` are proved.
2. **What is NOT canonical is identified.** Isotypic-slot *coordinates*
   are pair-dependent (swap obstruction). Wiring a slot coordinate into
   a "derived" number would be a hidden gauge choice = hidden degree of
   freedom; this failure mode is provably closed.
3. **A formalize-first prune for the Δ_λ gate.** Any candidate derived
   Δ_λ (Track A binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`) must pass
   orbit-invariance (`PairCoherent`) + pasted-square compatibility
   BEFORE numerics. A pair-gauge-dependent candidate is dead on
   arrival. This is the §compute-author formalize-first discipline with
   the pruning invariant already formalized.

## 3. Literature check: orbit structures and Habiro-ring actions

**External (verified 2026-07-26):**

- **Garoufalidis–Scholze–Wheeler–Zagier, *The Habiro ring of a number
  field*** ([arXiv:2412.04241](https://arxiv.org/abs/2412.04241)):
  the Habiro ring of `K` and **modules over it graded by `K₃(K)`**;
  elements are collections of power series **at each root of unity**
  glued by a **Frobenius endomorphism**, with corrections governed by
  Bloch-group elements and the p-adic dilogarithm. I.e., exactly a
  local system over evaluation points with arithmetic transition maps.
- **Wagner, *q-Hodge complexes over the Habiro ring***
  ([arXiv:2510.04782](https://arxiv.org/abs/2510.04782)): module /
  cohomology theory (q-de Rham with q-Hodge filtration) over the Habiro
  ring — representations *over* the Habiro ring exist and are active.
- Habiro's original unified WRT invariant lives in the Habiro ring with
  evaluations at all roots of unity ([arXiv:math/0605314](https://arxiv.org/abs/math/0605314)).

**In-corpus anchors (corpus-grep, same date):**

- `alpha-em-habiro-bar-involution` block: the α_EM Habiro element
  `H(q) = [2]_q(1 − h²α)` is bar-involution-fixed with **exact modular
  zero `H(ζ₄) = 0`** — evaluated at the SAME 4th root of unity as the
  monodromy point `q = i` of the τ-assignment tower.
- `docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`:
  ζ₈ evaluations already in play.
- `docs/coordination/2026-06-02-qbeta-habiro-element-scope.md` Phase B:
  **Galois descent on the Habiro ring** is an already-sanctioned route.

**The bridge this suggests (research framing, nothing claimed):** the
τ-assignment/monodromy apparatus at `q = i` is the **ζ₄ fibre** of what
the Habiro-ring viewpoint would organize as a root-of-unity-indexed
family. The marked-pair groupoid supplies the *horizontal* edges
(change of pair at fixed evaluation point); GSWZ Frobenius/Galois
structure supplies candidate *vertical* edges (change of evaluation
point). Two concrete observations:

1. **The bar involution at ζ₄ is complex conjugation** (`|i| = 1` so
   `q ↦ q⁻¹` is `z ↦ z̄`), and the `TauAssignmentData.rho_compat` law
   (star-compatibility of `toFun`/`toFunBar`) is exactly the statement
   that the assignment is equivariant for this ℤ/2 action. The first
   vertical edge is therefore ALREADY PROVED in the merged corpus —
   it just wasn't stated in this language.
2. A genuine `q₀`-bridge (where the 1ppq battle is) would require the
   family over all roots of unity plus the Habiro/Frobenius gluing —
   the same object #1713 Phase B targets for the c_k. The groupoid
   coherence proved here is a *precondition*: without pair-gauge
   independence, a root-of-unity family would not even be well-defined.

## 4. Open items (beaned)

1. Conjugation-edge monodromy equivariance — inner automorphisms do
   not preserve length; diagram half proved
   (`monodromyN_diagram_equivariant`), conj half OPEN (decide or
   refute with the length-rule obstruction made explicit).
2. `PairCoherent` prune interface for Δ_λ candidates — wire the
   orbit-invariance gate into the Δ_λ candidate checklist
   (documentation + a Lean predicate any candidate must instantiate).
3. Habiro ζ₄ bridge — state `rho_compat` as ℤ/2 (bar) equivariance at
   ζ₄ in Lean; scope the root-of-unity family (GSWZ-style) for the
   assignment tower. Research-grade; coordinate with the 1ppq-qbeta
   ledger (#1713 Phase B).

## 5. Scope discipline

All results scope-(a) or proved exclusions with explicit invariants;
no fits; nothing wired to production compute; L2 count unchanged (2/7).
The Habiro-bridge section is research framing with citations, not a
claim.

## Addendum (same date) — the three beans worked

**qou-yvel — DECIDED as a criterion**
(`HeckeTauAssignmentGaugeGate.lean` §1).
`monodromyN_equivariant_iff_descent_transport`: monodromy equivariance
along a marking homomorphism holds for all states **iff** the
homomorphism transports the descent condition pointwise. Sufficient
condition in clean general form: any **length-preserving** marking
homomorphism is equivariant (`monodromyN_equivariant_of_length_preserving`
— subsumes the diagram-edge theorem; covers `w₀`-conjugation in finite
systems). Analysis of a generic conjugation edge (scope-(a), prose
only): in A₃ the 4-cycle `c = (1234)` carries pair `(0,1)` to `(1,2)`;
the descent criterion at `l = 0` reads `c(x(1)) > c(x(2)) ↔ x(1) > x(2)`
in the value-comparison form, and `c` is order-preserving except
`4 ↦ 1` — so any permutation `x` with `x(1) = 4` (e.g. the
transposition `(14)`, length 5) violates transport. Generic conj edges
are therefore expected to FAIL equivariance; a machine-checked
refutation needs `ℓ((14)) = 5`-grade length certificates and is left
open — the criterion reduces it to finite combinatorics per edge.

**qou-fc35 — the master gate LANDED**
(`HeckeTauAssignmentGaugeGate.lean` §2).
`pairCoherent_of_cell`: every functional factoring through the
six-element cell restriction is pair-coherent, in one stroke;
`pairCoherent_comp` closes the class under post-composition. This is
the Δ_λ prune gate in executable form: a candidate routed through
marked-pair cell data passes automatically; anything else must supply
its own coherence proof or is dead on arrival.

**qou-vegn — first vertical edge NAMED; family scoping recorded**
(`HeckeTauAssignmentGaugeGate.lean` §3).
`zeta4_inv_eq_star` (`i⁻¹ = conj i`) +
`tauAssignment_zeta4_bar_equivariance`: the `rho_compat` law of every
`TauAssignmentData` **is** ℤ/2 bar-equivariance at the ζ₄ fibre. The
GSWZ and Wagner papers are now in-repo
(`uploads/2412.04241v2.pdf`, `uploads/2510.04782v2.pdf`, commit
4c05849); sandbox PDF extraction is currently broken (system
`cryptography`/pypdf conflict), so the deep-read of the Frobenius
gluing definitions (needed to state candidate vertical edges beyond
bar) remains queued on the bean. Bean stays in-progress.
