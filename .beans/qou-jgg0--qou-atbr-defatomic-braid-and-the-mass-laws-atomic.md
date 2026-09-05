---
# qou-jgg0
title: 'qou-atbr: def:atomic-braid and the mass law''s atomic braid are DIFFERENT objects sharing a name and a symbol'
status: todo
type: task
priority: normal
created_at: 2026-09-05T09:58:53Z
updated_at: 2026-09-05T10:01:26Z
---

## 2026-09-05 — measured: they are DIFFERENT OBJECTS, not a disagreement about a number

**Probe:** `computations/probes/two_atomic_braids_one_name_probe.py`, 5/5, exit 0, no witness.
**Audit:** `docs/audits/2026-09-05-two-atomic-braids-one-name.md`.

`qou-oots` / PR #6806 listed this under *not established* as *"the strand count … is still unreconciled by any block"*. That framing is too weak.

| | `def:atomic-braid` | production `atom_braid_word_3A` |
|---|---|---|
| algebra | `H_{A+Z}(q)` | `H_{3A}(q)` |
| strands | `A` nucleons **+ `Z` electrons** | 3 quarks/nucleon, **no electrons** |
| interactions | 6 pair types, **3 electronic** (`pe`, `ne`, `ee`) | β_Bor core + inter-nucleon bonds |

Both are written `\mathcal{A}`; both are called "the atomic braid".

### `H_{A+Z}(q)` cannot hold the production word — at every A

| atom | A | A+Z (def) | 3A | word needs | fits? |
|---|---|---|---|---|---|
| proton H-1 | 1 | 2 | 3 | **3** | **NO** |
| helium-4 | 4 | 6 | 12 | **12** | **NO** |
| iron-56 | 56 | 82 | 168 | **168** | **NO** |

`max(gen index) + 2` over the word the producer actually returns, asserted equal to `3A` at each atom. The proton's word uses `σ₀` and `σ₁` — 3 strands; the definition gives it 2. A containment failure, not a convention difference.

### The electron content has nowhere to go

Table 1 of `def:atomic-braid` specifies `pe` (EM attraction), `ne` (no interaction), `ee` (EM repulsion). The production source does not contain the string `electron` at all.

### Blast radius: 24 citing blocks, 7 in the mass chapters

`mass-endomorphism/atomic-mass-gb-nf.md`, `mass-theory/{active-set-trace-concentration.ts, canonical-closure-torus-chain.{md,ts}, subset-cumulant-recursion.{md,ts}, wedderburn-mass-formula.md}`.

`wedderburn-mass-formula.md` opens *"atomic braid `𝒜 ∈ H_{A+Z}(q)` ([atomic braid](#def:atomic-braid))"* while its sibling `schur-weyl-mass-decomposition.md` opens *"the atomic braid `𝒜 ∈ H_{3A}(q)`"*. Same chapter, same symbol, different algebra.

*(I first said 12 citing blocks — a truncated grep. The probe counts 24.)*

### Production is self-consistent; this is not a claim that the mass law is wrong

824 strand-count lines across 377 files use `3A`; 9 lines across 4 files use `A+Z`, and of those one carries deprecation markers and one is a test.

### The decision is the author's, and the two readings call for opposite actions

**(a) `def:atomic-braid` is a real, separate, uncomputed object** — the atom *with* its electron shell, of which the 3A braid is the electron-free core. Then nothing is wrong except that two objects share one name and one symbol; the fix is **naming** (give the 3A object its own label, repoint the mass-chapter citations, disambiguate `𝒜` in the register), and Table 1's electron rows are content worth keeping.

**(b) `def:atomic-braid` is superseded** by the 3A construction. Then it needs retiring and its 24 citations rehoming.

Evidence for (a): the electron rows are specific and physically motivated, not vestigial. For (b): nothing in `computations/` has ever built the `A+Z` object. **What is settled is that the status quo cannot be right under either reading.**

### Not established

- That either object is wrong — only that they differ and share a name.
- That the 7 mass-chapter citations are load-bearing; whether any *depends* on the `A+Z` count for a result was not measured.
- Which meaning of `𝒜` the notation register intends — it does not disambiguate them, and that block has no QA coverage (PR #6817), so no collision detector could have caught this.
