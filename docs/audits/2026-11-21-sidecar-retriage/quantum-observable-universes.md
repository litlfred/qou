# Sidecar re-triage: quantum-observable-universes (2026-11-21)

Umbrella issue #8766. 34 entries: 31 stale, 3 never hashed.

## Re-stamped (wording-only diffs; earlier verdict kept)

25 blocks: voice changes, label references replaced by descriptive pointers, one archimedean-limit sentence removed (pawlowski-leitner-inner-product), and one Lean-names paragraph removed (su2-emergence). All earlier findings stand. These include the self-assuming class fields, the D: A → Ω¹ type errors in the Dirac and Lagrangian blocks, the false positive-definite-dagger dependency, and the instanton-uniqueness counterexample (5-dimensional charge-1 moduli).

## Full reviews

| block | criterion | was | now | finding |
|---|---|---|---|---|
| braiding-induced-ordering | stmt | fail | **pass** | Rescoped to "deg-lex on W_n is well-founded and concatenation-compatible; not canonical". `braiding_induced_ordering_holds` proves exactly this (base-n encoding replaces a false List.Lex well-foundedness appeal). |
| braiding-induced-ordering-proof | proof | fail | **pass** | Min-length then lex-min argument; prefix/suffix compatibility. The physics is removed. |
| categorical-q-ext-deriv-exists-proof | proof | pass | **pass** | Direct construction d_q = q⁻¹d + (1−q⁻¹)π_V d is a morphism. |
| fiber-adjoint-involution | stmt | fail | **fail** | Lean now an honest cited sorry (was self-assuming). The md is still ill-typed (σ is an embedding, not an involution). |
| quantum-observable-universe-exists | stmt | fail | **fail** | Lean now an honest cited sorry. The md witness O_q(SU(2)) still breaks four axioms. |
| volume-from-rigidity | stmt | fail | **fail** | Lean now derives rank 2 from C(d,2)=1 (correct conditional). The md headline still says the alternating condition alone forces rank 2; Sp(4)'s ℂ⁴ is a counterexample. |
| q-resolvent-exists | stmt | — | **fail** | Lean is the trivial id witness; s ∈ Hom(1,A) + endomorphism is untyped. |
| q-resolvent-unique | stmt | — | **fail** | Lean proves a left inverse unique, given Δ surjective and with no s. The statement claims a unique right inverse of s + Δ. |
| q-resolvent-exists-proof | proof | — | **warn** | The Peter–Weyl route is fine. The Laplace route needs Re(s+λ) > 0, not just s outside the spectrum. "Both agree" is unargued. |

## Ruling check (docs/coordination/owner-rulings.md)

No block in this batch states the photon, the electron or the Lagrangian trace. The categorical Lagrangian blocks define ℒ = ψ*⊗Dψ in the abstract. They are not the two-term scoreboard trace, and that ruling does not bear on them.

Census after this batch: `proof-narrative-lean-equiv` 64 fresh; `da-non-sequitur` 58 fresh.
