# Brane-tower isospin-blindness — formalized sorry-free in Lean (2026-06-29)

**Status:** formalize-first **(b)-structural exclusion**. Discharges the owner-selected
*step 2* of the T2/T3 trace-invariance synthesis
([`2026-06-26-t2t3-trace-invariance-status-synthesis.md`](2026-06-26-t2t3-trace-invariance-status-synthesis.md),
§"Next steps", item 2). Cited invariant: the Markov axiom `tr_M(σ_i) = z` is reduced-word
independent. **Nothing wired** — a search-pruning lemma, not a production change; no `Φ_q`
numerics wired, no `α_M` number chased (both forbidden per the synthesis).

## What was open

The synthesis pinned the structural corollary as "the sharpest current constraint and the
recommended next formalisation target":

> Any **trace** (Markov-invariant) reformulation of the brane tower `T₂/T₃` carries **zero**
> mirror-splitting — its value is fixed by the strand count `n = 3A`, so two isobars of the
> same `A` receive an identical tower. Hence the entire mirror (T/³He) split must be carried by
> `T₁` (descended `tr_M`) and `T₅` (chirality), **not** the brane tower.

## What is now formalized (sorry-free)

[`QOU/Mass/BraneTowerIsospinBlind.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BraneTowerIsospinBlind.lean),
`lean`-direct verified `exit 0`, sorry-free, over a generic `[CommRing R]` (§7c-clean — no
gratuitous `ℝ`; `z` and the weights live in an abstract ring):

- **`braneTowerW_isospin_blind`** — the **(b)-exclusion** as a *conditional*: model the tower of
  a braid word `β` with an a-priori word-dependent per-subset weight `w β`; **if** the weight is
  Markov-invariant (`w β₁ = w β₂`, the cited word-independence), **then** two isobars on the same
  `n = 3A` strands receive an identical tower. The Markov hypothesis is the genuine content (not a
  vacuous identity) — word-independence *forces* zero mirror split.
- **`braneTowerR_eq_binom_sum`** — the algebraic collapse: the word-independent tower
  `∑_{S ⊆ Fin (n−1)} z^{|S|} f(|S|)` equals `∑_{k ≤ n−1} C(n−1, k) z^k f k`, a function of
  `(n, z, f)` **only** (proved by grouping the powerset sum by card via `Finset.sum_powerset` +
  `Finset.card_powersetCard`). No braid-word input survives — this is the algebraic face of
  isospin-blindness.
- **`braneTowerR_isospin_blind`** — isobar corollary: the same-`A` tower is
  `∑_k C(3A−1, k) z^k f k`.

## Consequence (search pruning)

The trace-invariant brane tower is **excluded** as a source of mirror splitting (a true
(b)-exclusion, cited invariant = Markov word-independence). Any future binding-sector closure must
put the T/³He split in `T₁ + T₅`, not in `T₂/T₃`. This narrows the still-open question
(the binding prefactor / `α_M` substrate derivation, which remains gated) without touching the
forbidden numerics.
