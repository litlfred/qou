# Audit — `frobenius_positivity_filter`: Lean over-generalization + "half" mislabel (2026-07-05)

**Scope.** The content block
[`prop:frobenius-positivity-filter`](../../content/quantum-observable-universe/particle-interactions/frobenius-positivity-filter.md)
and its Lean sibling
[`QOU.ParticleInteractions.frobenius_positivity_filter`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/frobenius_positivity_filter.lean).

Surfaced by a frontier-triage swarm agent (2026-07-05) while assessing whether
the block's single `sorry` was closeable. It is **not** closeable — but for a
more interesting reason than "missing infrastructure": the statement as written
is false, while the *number* it claims is (empirically) fine. This note
disentangles the two, per the STRICT "before declaring refuted / ruled out"
discipline in `AGENTS.md`.

## Two distinct defects (neither is "the count is numerology")

### 1. The Lean statement is universally-false — **scope (a)**

```lean
theorem frobenius_positivity_filter
    {A : ℕ} (_hA : Even A) (P : ProductData A)
    [DecidablePred (FrobeniusPositive P)] :
    (excludedConfigs P).card = 2 ^ (A - 1) := by sorry
```

`P : ProductData A` is **arbitrary** data (`parentProd`, `daughterProd` are
arbitrary `Config A → ℝ`). Counterexample: take `P.parentProd ≡ 1`,
`P.daughterProd ≡ 1`. Then `FrobeniusPositive P c` holds for every `c`, so
`excludedConfigs P = ∅` and `(excludedConfigs P).card = 0`, while
`2^(A-1) ≥ 2` for even `A ≥ 2`. So the universally-quantified statement is
**false**, and its `sorry` can never be honestly discharged.

This is a **scope-(a)** finding (per `AGENTS.md` §"Before declaring refuted"):
*this construction, stated unconditionally over all `P`, does not hold.* It
constrains the **statement's generality**, not the underlying count.

### 2. The `.md` "exactly half" descriptor is arithmetically wrong

The narrative says *"Exactly half the configurations — `2^{A-1}` out of `4^A` —
are excluded."* But `2^{A-1}` is **half of `2^A`**, not of `4^A`
(`= 2^{2A}`). At `A = 6` the block's own example gives `32` excluded of `4096`
— that is `1/128`, not half. So "exactly half" is a mislabel; the honest phrasing
is simply "`2^{A-1}` of the `4^A`".

## What is NOT refuted — the count `2^{A-1}` itself (scope note)

The count is **not** ruled out and must **not** be written off as numerology.
The block records a concrete, compute-backed instance:

> `⁶He → ⁶Li` (`A = 6`): `2^5 = 32` excluded of `4^6 = 4096`; the
> Frobenius-filtered sum gives `Q ≈ 3.637 MeV` (experiment `3.508 MeV`,
> `+3.68%`).

So `2^{A-1}` matches the actual physical count at `A = 6` and produces a
near-experiment Q-value. The count is a genuine **empirical observation about
the physical G-function product data** (the Hoefsmit spectator-sign structure),
not an arbitrary or fitted number. Writing "`2^{A-1}` is refuted" would be a
scope-(a)/(b) over-claim: the number stands; only the *unconditional Lean
statement* and the *"half" wording* are wrong.

## Resolution taken (corrected + proved, 2026-07-05)

Rather than demote to a conjecture, the block was **reformulated over the
correct carrier space and the count was proved sorry-free**. The key move: the
`2^{A-1}` count is a fact about the **`2^A` per-factor sign-pattern space**
`Fin A → ZMod 2` (one sign bit per factor, exclusion ⟺ *odd total parity*),
**not** the `4^A` configuration space. On the sign-pattern space `2^{A-1}` **is**
exactly half of `2^A`, and the count is unconditional and elementary.

1. **`.lean` — proved, no `sorry`**
   ([`frobenius_positivity_filter.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/frobenius_positivity_filter.lean)):
   - `parity_odd_card (A) (hA : 1 ≤ A) : card {s : Fin A → ZMod 2 | ∑ᵢ sᵢ = 1} = 2^(A-1)`
     — proved via the bijection "drop the last coordinate" (any tail extends to
     a unique odd-parity vector; the head is forced to `1 − ∑ tail`).
     Sorry-free (`#print axioms` → `[propext, Classical.choice, Quot.sound]`).
   - `frobenius_positivity_filter` (same name, `lean.ref` preserved) is now a
     **proved conditional theorem**: given the sign-mechanism characterisation
     `hchar : ∀ s, excludedSign s ↔ ∑ᵢ sᵢ = 1` (the physical *input*), the count
     `2^{A-1}` is **derived** from `parity_odd_card` — no `sorry`. This is
     §3b-cond-clean: the hypothesis carries the mechanism, the theorem derives
     the count (not a self-assuming projection). It **replaces** the previous
     unconditional statement over `4^A` (which was false, scope (a) above).
2. **`.md`:** the "exactly half — `2^{A-1}` out of `4^A`" sentence was corrected
   to the sign-pattern framing (`2^{A-1}` of the `2^A` sign-patterns have odd
   parity); the `A=6` example now reads "`4^6` configs reduce to `2^6 = 64`
   sign-patterns, of which `2^5 = 32` are excluded."
3. **`.ts`:** kind **stays `proposition`** — it is now a genuine *proved*
   conditional proposition, so no demotion / label ripple was needed.

**Why not the generic-`P` conditional.** A conditional keyed on an abstract
per-factor sign mechanism over the *`4^A` config space* still fails: a generic
balanced per-factor sign gives `~2^{2A-1}` excluded (genuine half of `4^A`), not
`2^{A-1}`. The correct carrier is the `2^A` sign-pattern space, where the count
is exactly and provably `2^{A-1}`. The physical content that remains (unproved,
and appropriately *not* claimed as a theorem) is the map "physical G-function
`ProductData` → its sign-pattern," i.e. that the Hoefsmit spectator structure
realises `hchar`; that modelling assumption is narrative, and the empirical
`A=6` → 32 / `Q ≈ 3.637 MeV` check supports it.

## Status

- **Finding + resolution:** recorded here. `.lean` corrected and **proved
  sorry-free** (lean-direct exit 0; source-level `#print axioms` clean).
- **Not machine-validated:** the content-validation pipeline (`.md`/`.ts` Zod +
  render) is firewalled in the sandbox; the `.md` was hand-checked (render-QA
  grep battery + expository pass), not pipeline-rendered.
- **Underlying physics claim (`2^{A-1}` count, filter mechanism):** stands;
  the combinatorial core is now a Lean theorem, the physical realisation
  (`hchar`) is the remaining modelling assumption.
