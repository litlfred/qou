# Q_β c₄ — H₄-tower Stage C: the open σ₃-lift (scope + validated foundation)

**Date:** 2026-06-18
**Branch:** `claude/dreamy-feynman-nns0ol` (PR #2465)
**Goal:** 1ppQ — Q_β; the `c₄` rung of the ladder `∏_{k≥2}(1+cₖu_L^k)`
**Relation:** continues #2106 (Hoefsmit Stage B); preflight for its un-built
Stage C. Synthesis source: #2465 (C13 bridge refutation) + #2469 (counit N=0).

---

## 0. Where c₄ lives (the synthesis, now backed by a preflight)

Three independent results converge:

| result | content | tier |
|---|---|---|
| #2465 (C13) | A=1 `Δtr_M`-seeded (trace) bridge gives `c₃≈−1.5`, not −2 | refuted |
| #2469 | counit `ε(Δ)` is the right functional but **N=0** (+0.17%) | merged |
| #2106 (Stage B) | H₃ level support stops at ℓ=3 ⇒ `c₄..c₈` need H_{n≥4} | established |

⟹ **`cₖ≥3` are the N≥1 / H_{n≥4} brane-tower corrections, not in any A=1
functional (counit or trace).** This is the only surviving axis.

## 1. Preflight result (this PR — `qbeta_h4_tower_branching_preflight.py`)

Validated, exact-at-50-dps, non-fitting:

1. **H₄ Hoefsmit seminormal reps build and are correct** — all λ⊢4
   (dims 1/3/2/3/1) satisfy the Hecke relation `σ_i²=(q−q⁻¹)σ_i+1`, the braid
   relations `σ₁σ₂σ₁=σ₂σ₁σ₂`, `σ₂σ₃σ₂=σ₃σ₂σ₃`, and far-commutation
   `σ₁σ₃=σ₃σ₁`, to `1e-40`. (`young_seminormal.seminormal_sigma`, validated
   `≡ pyhecke_native` to λ⊢6.)
2. **The H₃⊂H₄ branching map holds**: `χ^μ(w) = Σ_{λ↗μ} χ^λ(w)` for every
   σ₃-free decay word `w` and every `μ⊢4` (max rel err `5.6e-52`). Branching:
   `(4)↓=(3)`, `(3,1)↓=(2,1)+(3)`, `(2,2)↓=(2,1)`, `(2,1,1)↓=(1³)+(2,1)`,
   `(1⁴)↓=(1³)`.
3. **σ₃-gating**: by (2), a σ₃-free element's H₄ data is fully determined by
   its H₃ data — **no new DOF**. So the c₄ content cannot come from a σ₃-free
   object; it is gated on a length-4 word involving the new strand σ₃.

This is consistent with **C12** (the scalar trace stabilises, `tr_M^{H₄}(ιw) =
z·tr_M^{H₃}(w)`) and **C13** (the A=1 trace bridge is refuted): both are σ₃-free
and so, by the preflight, structurally incapable of carrying c₄.

## 2. The OPEN Stage-C question (formalize-first — do not fit)

> **Which length-4, σ₃-involving element `Λ ∈ H₄(q)` is the categorically
> correct lift of the free-neutron-decay operator `ΔT ∈ H₃(q)`, such that its
> level-4 Markov-trace component yields `c₄`?**

This is a **categorical specification**, not a search. The discipline
(refuted-class map, flip-flop guard) forbids enumerating σ₃-extensions until
one's c₄ matches — that is fitting. A valid Stage-C answer must:

- **Derive `Λ` from the decay categorical content** (the confinement defect /
  the brane-tower N→N+1 map), not back-solve it from the c₄ target.
- **Pass anchor-stability** (proton+muon swing < 1%, registry §8) — a σ₃-lift
  whose c₄ swings across anchors is empirical, dead on arrival.
- **Respect bar-evenness + the `q=1` shadow** (the §1 invariants of the
  refuted-class map).
- **Reduce to the validated H₄ machinery** here (seminormal reps + branching).

## 3. Foundation handed to Stage C

- `computations/young_seminormal.py::seminormal_sigma(shape,i,q)` — H₄ reps.
- `computations/habiro/qbeta_h4_tower_branching_preflight.py` — branching map
  + relation checks (this PR).
- `computations/free-neutron-decay.py` — `ΔT` as H₃ normal-form words
  (basis `[(),(0,),(1,),(0,1),(1,0),(0,1,0)]`).
- Open: the σ₃-lift `Λ`, the H₄ Markov-weight wiring (`pyhecke.wedderburn`
  needs `q_parameter`/`qou_substrate` on path), the level-4 component
  extractor. These are the Stage-C build, **multi-session**.

## 4. Honest status

This preflight does **not** close c₄. It validates the foundation and pins the
open question precisely, so Stage C starts from a correct, instrumented base
instead of re-deriving C12/C13. The gate (1ppQ Q_β) remains open.
