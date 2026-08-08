# 1ppq lever map — after the substrate-q₀ FOREVER GATE (2026-08-02)

Companion to the [`substrate-q₀ FOREVER GATED` ruling](../audits/2026-08-02-subgoal2-q0-derivation-forever-gated.md)
(bean `qou-eic1`). Records what "1ppq progress" can and cannot mean now that
q₀-derivation is permanently off the table, so the next session does not
re-walk the closed region.

## Today's structural region — CLOSED (L2-orthogonal, machine-verified negatives)

The arc **offset → A_ω=3 → Stokes=DT=BPS bridge → driver-14** is fully mapped
and closed. All negatives are sorry-free Lean (several Mathlib-free ⇒
machine-verified past the sandbox disk wall):

| result | verdict | PR |
|--------|---------|-----|
| saddle-offset "centred at q=1" — archimedean | refuted (bar-grade ≠ chirality-grade) | #4583 |
| saddle-offset — fibre-level Habiro | vacuous-or-fit (non-selective) | #4587 |
| A_ω=3 internal integer | derived (q→0 symmetry constant) | #4554 |
| A_ω=3 as BPS/DT count | conditional on imported bridge | #4569 |
| Stokes=DT derivable from QOU drivers | **no** — Euler-char gives −2 (norm), not 3 (count); −6 = (−2)·3 | #4599 |
| driver-14 (character-variety DT moduli) | irreducibly external; a chirality-refined *set-valued* count outside the 13 drivers | #4601 |
| torsion = ν_SDP | refuted (scope-a) | #4576 |

**Unification:** `Δ_λ` (partition-level) and `A_ω` (knot-level) are the same
missing input — a categorical Behrend-weighted DT moduli — at two levels. And
(#4601, derive-then-check) that missing input is **distinct** from the `Δ_λ`
*magnitude* gate: the derived `Δ_λ = (−1)^{n(λ)}·dim V_λ` fragment gives the
deuteron **B(D)=0.380 MeV (−82.9%)**, so closing the DT count would NOT close
binding.

## The L2 dashboard (per-observable 100× accuracy) — 2/7 met

| obs | role | miss factor |
|-----|------|-------------|
| m_e | CAL-1 anchor | **met** |
| m_K/m_π | meson ratio | **met** |
| m_p | CAL-2 anchor | 437× |
| m_μ | validation | 964× |
| m_n | validation | 416× |
| Q_β | derived | 160× |
| Δ_pn | derived | 159× |

## The sharp strategic conclusion (why the pivot to Δ_λ is forced, not chosen)

Two independent facts now bound what framework compute can do to the **7 L2
observables**:

1. **The 2026-07-18 measurement-limited ceiling** (two sorry-free Lean
   theorems): absent a substrate-derivation of q₀, **4 of the 5 L2 misses are
   gated on the experimental neutron Q_β measurement**, not on any framework
   compute.
2. **q₀-derivation is now FOREVER GATED** (2026-08-02).

Together — **re-scoped 2026-08-08 (bean `qou-qb8a`); the conclusion below is
narrower than originally written, and the numbers are unchanged.**

**Original wording:** *"the 5 L2 mass/Q_β misses are no longer
framework-closable."* That is a **scope-(b) structural exclusion asserted without
a proved invariant**, and per AGENTS.md §"Before declaring refuted" it must be
scope-(a).

**Correct scope-(a) statement:**

* **Verification** below `σ_exp = 779.7 ppb` is measurement-limited. TRUE.
* **Extracting** c₃ *from* a measured Q_β is measurement-limited
  (`dq*/dQ_β ≈ −0.54`). TRUE.
* **Re-pinning q₀ cannot move them.** TRUE — the anchor swing is 29.96 ppb,
  2.4% of the 1248 ppb residual.
* **But the 1248 ppb Q_β prediction error is the c₃ truncation — a framework
  quantity.** Under the proton pin, q₀'s measurement uncertainty contributes
  `≈ 0.16 ppb`, four orders below it. **No proved invariant excludes a
  categorical derivation of c₃ from improving the prediction.** So "grinding the
  c_k tower" is dead as a *fit*; a *derived* c₃ is not excluded.
* And a better neutron measurement **tightens** `σ_exp`, making the L2 target
  (`σ_exp/100`) proportionally **harder** — so waiting on the measurement does
  not close L2 by itself.

The practical consequence for this lever map is unchanged: the binding / `Δ_λ`
magnitude closure remains the better-value derivation lever, because it is
scale-free. What changes is that the c₃ route is recorded as **open and hard**,
not as **excluded**.

**Therefore the remaining framework-*derivation* precision lever is NOT the 7 L2
masses — it is the per-isotope binding / `Δ_λ` magnitude closure (Subgoal-1),
which is scale-free (q₀ cancels) and outside the measurement-limited ceiling.**
The deuteron is its gate (6 ansätze failed; DT-count is distinct per #4601).

## Live levers, ranked (all q₀-free)

1. **`Δ_λ` magnitude / deuteron binding gate** — the one open framework-derivation
   precision target. *(under active attack: `claude/deltalambda-magnitude-deuteron-2026-08-02`)*
2. **Option-E A=3 anti-self-adjoint lift** — "the single open door is one free
   amplitude E" (sibling work, main `33131b24`/`aaacb1e9`); adjacent to the
   binding combiner.
3. **Absolute binding via non-q₀ routes** — the `M_n(K)` edge-set / coordination-graph
   closure (`conj:binding-manybody-eq-jet-filtration`).

## Forbidden (permanent)

- **Any route that derives q₀ from the substrate** — FOREVER GATED, `qou-eic1`.
