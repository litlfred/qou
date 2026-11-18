---
# qou-ar7f
title: 'Prop-field drain re-scoped: the HeckeAlgebra trio are SHADOWS, and wenzlBridge is rfl on a def'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-03T13:45:21Z
updated_at: 2026-10-04T15:22:15Z
parent: qou-59vq
---

Measured 2026-09-03 while draining the `Prop`-valued-field category the cited-not-proved audit added (#6491). The drain is **not** 96 independent reshapes, and `QOU/Mathlib/HeckeAlgebra.lean` — which has four of them, i.e. the Hecke representation theory the mass derivation runs through — is the worked case.

## What the four carriers actually are

| carrier | inhabited? | states its claim? | disposition |
|---|---|---|---|
| `StandardYoungCount` | was no → **yes** | was no → **yes** | **DONE** (#6491): field restated as `∑_λ (dim λ)² = n!`, inhabited from `dimSYT` + `RSKBridge.RSK_substrate_proved`. Had ZERO consumers, so free. |
| `WenzlBridge` | no | no | shadow — see below |
| `MarkovTrace` | yes | no | shadow — see below |
| `WedderburnDecomposition` | yes (`triv_wedderburn`) | no | shadow — see below |

The bottom two are the worst combination and the class-count alone misses them: **an instance exists, so downstream code resolves the class happily, and it asserts nothing.**

## The three are SHADOWS of a concrete development, not reshape targets

There are two `WedderburnDecomposition`s, in two namespaces:

* `QOU.HeckeAlgebra.WedderburnDecomposition` — `abbrev … : Type` (`Wedderburn.lean:68`), a concrete indexed family of matrices. No `Prop`-valued fields. Real.
* `QOU.Mathlib.HeckeAlgebra.WedderburnDecomposition` — the `class` with `blocks_sum_to_one : Prop` etc.

The concrete development (`QOU.HeckeAlgebra.MarkovTrace`) uses the **concrete** one. Only **3 files** import `QOU.Mathlib.HeckeAlgebra`, and one of them (`Mathlib/Summary.lean`) is red on main anyway (established in `qou-fngs`). So the abstract trio has essentially no traffic.

**Consequence for the drain:** reshaping `WenzlBridge` is not even expressible without first reshaping `MarkovTrace` and `WedderburnDecomposition`, because its statement needs their fields — the three form a dependency chain, and `StandardYoungCount` was the only leaf. Re-pointing consumers at the concrete development and retiring the shadows is the cheaper and more honest move, but it is an owner call about what that abstract bundle is for, so it is NOT done here.

## The genuine gap is the AXIOMS, not the Prop fields

`wenzlBridge` (`MarkovTrace.lean:283`) is proved `rfl`, because `markovTraceOnWedderburn` is **defined** as exactly the sum it equates to:

```
noncomputable def markovTraceOnWedderburn (x) : ℝ :=
    ∑ lam ∈ partitions_as_finset n, JonesMarkovCoefficient lam QSubstrate.q_0 * (x lam).trace

@[simp] theorem wenzlBridge (x) : markovTraceOnWedderburn x = ∑ … := rfl
```

So the "Wenzl bridge (categorical identity)" is **true by definition, not derived** — its own docstring calls the def "(axiomatised)". The `AGENTS.md` §"Defined residual ≠ derived decomposition" trap, one file over: a `def` written with `:=` and then reasoned about as though it were *the* categorical identity.

What is genuinely unproved is that this def agrees with the **actual** Markov trace `markovTrace : HeckeElement n → ℝ`, and that is carried by real axioms already in the audit's 21: `markovTrace_linear`, `MarkovTrace_markov_axiom` (`HeckeAlgebra/MarkovTrace.lean:169`), `markov_trace_unique_axiom` (`Hecke/MarkovTrace.lean:125`).

`wenzlBridge` being `@[simp]` is harmless as a rewrite. What is not harmless is the docstring presenting it as "the categorical content that the Python compute layer implements" — a reader can take it as establishing the identity, and it establishes that the def is the def.

## Next, in priority order

1. **Owner call:** retire the `QOU.Mathlib.HeckeAlgebra` abstract trio, or re-point it at the concrete development. Cheap either way (3 importers, one already red); not an agent decision.
2. **The real work:** the three Markov-trace axioms above. That is where "cited and not Lean proved" actually sits for this axis.
3. The other 92 `Prop`-valued fields — re-triage with the same question first, since this case suggests many are shadows rather than reshape targets.

## Method note

This is the **fifth** "it already exists elsewhere / X is not needed" of the session (after RSK for the branching identity, spectral-sequence theory for the collapse, Goursat for Cauchy, and the SYT count "when it lands"), and the **fourth** namespace collision (`rskBurnsideHolds` ×2, `RSK_substrate_proved`'s prefix, `MarkovTrace`'s 123 false consumers, and now `WedderburnDecomposition`). Both are worth checking first, by reflex, on anything in this corpus that looks blocked or looks like a fresh build.


## 2026-09-03 — the 11 HeckeAlgebra Prop fields are NOT part of the defect population

Measured on `origin/main` with `scripts/lean-cited-not-proved-audit.py --kind
prop-field`, after adding a `consumed` / `unconsumed` discriminator (PR #6543).

I have twice told the author that the 39 self-nominating `Prop` fields were a
queue, and that 11 of them were blocked on this bean's owner decision. **Both
halves were wrong.** The corpus splits:

| | count |
|---|---|
| `Prop` fields total | 95 |
| parameterised (legitimate) | 56 |
| self-nominating | 39 |
| — **consumed** (a proof term projects the witness) — the defect | **24** |
| — unconsumed (an open input carried as an input) | 15 |

**All 11 of this bean's `QOU/Mathlib/HeckeAlgebra.lean` fields are
`unconsumed`.** Nothing projects `markov_axiom`, `blocks_sum_to_one`,
`bridge_identity`, `hecke_relation`, … into a conclusion. They are the honest
§3b conjecture-class pattern: an open input declared as an input.

So this bean's decision — retire the shadow trio, or re-point it — stands
entirely on its own merits (three carriers duplicating a concrete
`QOU.HeckeAlgebra` development that the real code actually uses). It is **not**
blocking 11 Prop-field defects, because there are none there. Nothing about the
Prop-field work waits on this bean, and this bean gains no urgency from it.

The discriminator came from a false positive on
`QOU/BraidKnot/BringWPlaneMonodromy.lean`, which is exemplary: its
`is_seifert_gauss_manin : Prop` is a deliberately-abstract geometric
identification, and the file's theorem derives from the content-bearing
`unimodular` field via a proved lemma, explicitly not from the witness. Its own
docstring says so.

Recorded here rather than acted on: no change to the trio, no change to the
recommendation (still **retire**).
