# Attack plan — atomicity from self-duality: derive `TensorGenerationFree`, don't assume it

**Date:** 2026-07-25 · **Milestone bean:** `qou-atsd` · **PR:** #4285 (extends the atomicity order-separation) ·
**Owner ruling in force:** Subgoal-2 / substrate-derivation open for all (2026-07-11); anti-fit / anti-laundering STILL STANDS.

## Goal

Replace the bare bridge premise `TensorGenerationFree` (PR #4285) with a **derivation** of rank-one
from the QOU axioms. The order-theoretic half is already closed:
`rankOne_of_chain_of_bridge : [TensorGenerationFree W S] → IsTotal W (·≤·) → Subsingleton S`.
This plan derives the antecedents from **symplectic self-duality of `V` + `dim V = 2`**.

## The chain (what forces rank-one)

$$
\underbrace{\varepsilon\colon V\otimes V\to\mathbf 1\ \text{symplectic, non-deg}}_{\text{volume-form axiom}}
\ +\ \underbrace{\dim V = 2}_{\Lambda^2 V\cong\mathbf 1\ \Rightarrow\ \binom{n}{2}=1\ \Rightarrow\ n=2}
\ \Rightarrow\ G\subseteq \mathrm{Sp}(V)=\mathrm{Sp}_2=\mathrm{SL}_2
\ \Rightarrow\ \mathrm{rank}\,G\le \tfrac{\dim V}{2}=1
\ \Rightarrow\ |S|\le 1 .
$$

**Key distinction (do not conflate):** `dim V = 2` is the *cohomological* input
(`H¹(Bring) = 2W` is rank 2 = `dim V`); it is **not** `rank G = 2`. It is *self-duality* that
collapses `dim V = 2 ⇝ rank G = 1` (the `Sp₂ = SL₂` dim-2 accident: `rank Sp(2m) = m`).

## Tiers

| Tier | Statement | Lean status | Bean |
|---|---|---|---|
| **T0** | `Λ²V ≅ 𝟙` non-deg ⟹ `dim V = 2` — arithmetic crux `n.choose 2 = 1 → n = 2` | **tractable now, sorry-free** | `qou-atsd-t0` |
| **T1** | `Sp₂ = SL₂`: `A ∈ symplecticGroup (Fin 1) R ↔ det A = 1`, via `A·J·Aᵀ = det A • J` for 2×2 | **attempt now** (Mathlib-ext infra) | `qou-atsd-t1` |
| **T2** | reduction skeleton: compose `[G ⊆ Sp(V)] + [rank Sp(2m)=m] + [dim V=2] ⟹ Subsingleton S`; wire to `rankOne_of_chain_of_bridge` | **tractable now** (rank-Sp fact = single named residual, cited, no instance) | `qou-atsd-t2` |
| **T3** | formalize `rank(Sp(2m)) = m` (symplectic root system `C_m`) via `Mathlib.LinearAlgebra.RootSystem` | **hard Mathlib gap** (multi-session) | `qou-atsd-t3` |
| **T4** | Tannakian reconstruction: `G` connected reductive of positive dim (rank *exactly* 1, not a finite subgroup of `SL₂`) | **hard Mathlib gap** (multi-session) | `qou-atsd-t4` |

## Honest residual after T0–T2

Atomicity `⟸ [self-duality axiom] + [dim V = 2] + [rank Sp(2m) = m] + [G connected reductive]`.
The first two are **QOU axioms** (volume-form + cohomological); the last two are **classical facts**
(T3, T4) — named, cited, and *not faked*. No `instance` of the rank-Sp residual is fabricated
(AGENTS.md §"Axiomatization is NOT a Proof"): T2 leaves it as a conjectural-class field, so the
conditional is honest, and T3 discharges it for real.

## Anti-laundering guardrails

- The rank-Sp residual (T3) is a **named classical theorem**, not an axiom smuggling the conclusion;
  T2's reduction *derives* rank-one *from* it, never projects it.
- `dim V = 2` stays explicitly the cohomological input; the write-up keeps `dim V` (rep dimension) and
  `rank G` (torus dimension) separate at every step.
- Scope-(a): each tier's negative/positive is stated for its exact object.

## Cross-references

- Order-side (done): [`AtomicityRankOneOrderSeparation.lean`](../../folio/quantum-observable-universe/lean/QOU/ParticleInteractions/AtomicityRankOneOrderSeparation.lean), [`2026-07-25-atomicity-rankone-order-separation.md`](../audits/2026-07-25-atomicity-rankone-order-separation.md)
- Axioms: [`fundamental-object.lean`](../../folio/quantum-observable-universe/quantum-universes/fundamental-object.lean) (volume form), [`tannaka-dual.md`](../../folio/quantum-observable-universe/quantum-universes/tannaka-dual.md)
- Sibling route: #4266 (`qou-ngwo`)
- Mathlib: `Mathlib.LinearAlgebra.SymplecticGroup` (`symplecticGroup`, `mem_iff`, `symplectic_det`)
