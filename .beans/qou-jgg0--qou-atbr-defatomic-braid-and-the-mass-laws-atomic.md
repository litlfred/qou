---
# qou-jgg0
title: 'qou-atbr: def:atomic-braid and the mass law''s atomic braid are DIFFERENT objects sharing a name and a symbol'
status: todo
type: task
priority: normal
created_at: 2026-09-05T09:58:53Z
updated_at: 2026-09-06T07:16:38Z
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


### 2026-09-06 — RETRACTED my own "not a third braid", and the structure is a 2×2

The entry above says `3A + Z` is a third strand COUNT but "NOT a third braid
construction". **That is a claim about one FILE promoted to a claim about the
CORPUS, and it is wrong at corpus level.**

The file-level evidence stands and is re-verified: `electron_sigma_f_chain.py`
uses `3A + Z` as the confinement-SDP normalisation `tr Φ = n_target`, sweeps
`Z = 0…8`, and never imports or calls `atom_braid_word_3A`. But
`content/quantum-observable-universe/mass-endomorphism/atomic-mass-gb-nf.md:3`
— a **content block** — asserts *"atomic braid $\mathcal{B}_K \in B_{n}$, where
$n = 3A + Z$"*. `B_n` is the braid group. So it is a third count **and** a third
braid, and my sentence would have sent the next agent past the block that has it.

Found by corpus-grep. The file was measured correctly both times; what failed
was the scope of the inference.

**The structure**: two independent binary choices, not a three-way argument.

|  | electrons in | electrons out |
|---|---|---|
| nucleon-strand | `A+Z` — `def:atomic-braid`, **7** blocks | `A` — coarsening only |
| quark-strand | `3A+Z` — `atomic-mass-gb-nf`, **1** block | `3A` — production, **26** blocks |

`H_A` is `level-sufficiency-interprets.md:41`'s explicit **"Default-coarse"**
approximation, not a competing claim — the live disagreement is three-way.

**Three things that make it worse than a count discrepancy**
(`computations/probes/strand_count_is_a_two_by_two_probe.py`, 12/12):

1. The collision is on the symbol `\mathcal{B}_K`, and one disputant is the
   **notation register** (`notation-register-table3-data.md:7` → `H_{3A}(q)`),
   which AGENTS.md §7aa makes authoritative for symbols.
   `notation-collisions.md` has **no entry** for it — unregistered.
2. `atomic-mass-gb-nf.md` links `#def:atomic-braid` **while using a count that
   definition contradicts**. Inside one citation edge, not two chapters drifting.
3. `A+Z < 3A < 3A+Z` strictly for every `A ∈ 1..60`, `Z ∈ 1..A` (0 clashes), so
   nothing reconciles them by coincidence; and `3A+Z` is exactly the **join** —
   `(3A+Z) − 3A = Z`, `3A − A = 2A`, the two axes independent.

**Blast radius, named.** `qou-q6pp` works entirely in `H_{A+Z}` and derives its
generator count `A+Z−1` from it; if the canonical home is `3A` or `3A+Z` that
derivation's arithmetic changes. `notation-register-table3-data.md` and the 26
`3A` blocks are the production majority, so `def:atomic-braid` (`A+Z`) is the
**minority** reading despite being the definition.

**This makes the (a)/(b) decision three-way, not two-way.** Whoever renames now
has three cells to name, and the register — not just a chapter — is one of the
disputants.

**Guard added.** Check 1 asserts every cited path EXISTS before asserting its
content, because the sibling audit cited two of these very sites at paths that
resolve to nothing (`mass-theory/atomic-braid.md`, bare `hecke_3a_weights.py`)
while the claims themselves were true.


### 2026-09-06 — the strand-count reading is not cosmetic: it moves `qou-q6pp`'s leading explanation

The entry above frames three live strand counts as a **naming** problem. It is
not only that, and here is the counter-example — one of the three readings is
**not interchangeable** with the others.

`qou-q6pp` (status `todo`, unclaimed since 2026-08-25) offers, as the better of
its two candidate explanations for the wrong-signed p-n splitting: the three-Φ
formula is leading-order, exact only while the three extremal blocks (sym, std,
alt) exhaust the partitions of `n`; `n = 3` is the unique such `n`; and D is the
only right-signed atom. **The force of it is a coincidence** — the uniquely-exact
`n` is occupied by the uniquely right-signed atom. The bean computes `n = A+Z`
throughout, because `thm:wedderburn-mass-formula` says `H_{A+Z}(q)`.

`p(3) = 3` is the only partition count equal to the extremal count, so the whole
argument turns on **which atom has `n = 3`**:

| reading | atom at `n = 3` | its verdict in `qou-q6pp` | the coincidence |
|---|---|---|---|
| `A+Z` | **D** | RIGHT sign (1.448) | **holds** |
| `3A` | **H-1** | over-specified, 5e5 off | **inverts** — lands on its worst point |
| `3A+Z` | *(none)* | — | **evaporates** — `3A+Z = 3` needs `Z = 0` |

So `3A` would move that bean's leading explanation onto its own worst data
point, and `3A+Z` would remove the explanation's subject entirely. The three
readings also differ at **every** atom in its five-atom sample (H-1, D, T, ³He,
⁴He).

**What this does NOT claim.** The p-n sign is unresolved and `qou-q6pp` stays
open and unclaimed — I did not take it. No vote is cast on which reading is
right; that stays with the author. And the bean's argument is **not refuted**:
under the reading it uses, which its own source theorem states, it stands.

**What it establishes** is only that "three counts, pick one later" understates
the cost. The naming decision on this bean now has a priced consequence outside
naming.

Probe: `computations/probes/q6pp_unique_n_is_reading_dependent_probe.py`, 10/10,
exit 0. Exact integer partition DP and integer strand arithmetic; no witness.
Check 2 reproduces `qou-q6pp`'s own `n` column at 5 of 5 atoms before departing
from it, so the departure is not an artifact of a differently-built table.
