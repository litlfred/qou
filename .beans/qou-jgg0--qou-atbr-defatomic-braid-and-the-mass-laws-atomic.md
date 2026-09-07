---
# qou-jgg0
title: 'qou-atbr: def:atomic-braid and the mass law''s atomic braid are DIFFERENT objects sharing a name and a symbol'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T09:58:53Z
updated_at: 2026-09-07T18:00:00Z
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


### 2026-09-06 — a SECOND reading-dependent consumer, and the two point opposite ways

#6919 (sibling) asked whether its `f₁/f₀` additivity across the two nucleons is
contingent on which strand count `def:atomic-braid` means. Measured at the
producer (`mass_at_3A_proper.atom_braid_word_3A`), check 9 of
`strand_count_is_a_two_by_two_probe.py` (now **16/16**):

Their premise is exactly right in the `3A` reading. The deuteron generator
sequence is `[0,1,0,1,0,1,0,0,1,0,0, 2, 3,4,3,4,3,4,3,3,4,3,3]` — proton `{0,1}`
11 ops, neutron `{3,4}` 11 ops, **min cross `|i−j| = 2`**.

**But the full word carries the inter-nucleon bond at generator 2**, once, and 2
is adjacent to *both* blocks. So the factorisation is a property of the **vacuum
part**, not the whole word. Flagged to them: `atom_braid_word_3A_to_crossings`
defaults to `include_inter=False`, so measuring the bond-free word and reporting
additivity of "the pn atom word" is one keyword away and reads identically.

| reading | disjoint-support premise |
|---|---|
| `3A` | **holds** — the layout above, production's reading |
| `A+Z` | **not statable** — D has 3 strands, 2 generators; a nucleon is *one strand*, so there is no per-nucleon block, and the neutron block would need index 4 |
| `3A+Z` | blocks survive, but the electron generator (5) is **adjacent** to the neutron block; `pe`/`ne`/`ee` crossings couple it in |

**The consequence for the naming decision, and it is new: no reading is free.**
Two independent consumers now price it in **opposite** directions —

- `qou-q6pp` is cheapest under **`A+Z`** (its coincidence holds there, inverts
  under `3A`, evaporates under `3A+Z`);
- #6919's additivity is only statable under **`3A`** or **`3A+Z`**.

The sharpest case is not that `A+Z` gives a *different* answer to #6919 — it is
that the question has **no referent** there, since "which generators does nucleon
`k` own" presupposes three strands per nucleon.

Comment 5558064329.


### 2026-09-06 — the bond question is ANSWERED, by the sibling, and better than I put it

My comment 5558064329 flagged that #6919's additivity description omits the
inter-nucleon bond at generator 2, and asked which word they measured. **Answered
— `include_inter=False`.** Their audit landed on `main` at **09:21:39Z**
(`80cc738916`, 45 min after the flag),
[`2026-09-06-contiguity-does-not-drive-f1-the-split-link-factorisation-does.md`](../docs/audits/2026-09-06-contiguity-does-not-drive-f1-the-split-link-factorisation-does.md),
and its scope section says it outright:

> **Additivity is measured on `pn` with `include_inter=False`.** The inter-nucleon
> terms are exactly the part that breaks the disjoint-strand premise, so nothing
> here says anything about them — **and they are where the binding lives.**

That last clause is the sharper form of the point and is theirs, not mine. So the
flag was correct in substance, it is closed, and **no further reply is owed** —
recording here rather than posting a fourth comment on #6821.

**What is NOT superseded.** Their scope note covers the inter-nucleon bond; it
says nothing about the **electron** strand, because they work at `n = 6` (`pn`,
the `3A` reading) where there is none. So the reading-dependence table stands
unchanged:

| reading | disjoint-support premise |
|---|---|
| `3A` | holds — and is what they measured |
| `A+Z` | not statable — one strand per nucleon, no per-nucleon block |
| `3A+Z` | blocks survive, but the electron generator is adjacent to the neutron block; `pe`/`ne`/`ee` crossings couple it in |

**Also not affected: their retraction is a different claim from the one I
analysed.** `80cc738916` retracts *"contiguity drives `f₁/f₀`"* (their #6910).
My reply was about the **additivity / split-link factorisation**, which their new
title affirms rather than withdraws. Do not read the retraction as weakening the
additivity result the reading-dependence applies to.

## 2026-09-07 — the measurement MERGED (#6821); the DECISION is open and is the author's

PR #6821 merged onto `main` (rebase, per-commit). The audit, the three probes
(7/7, 16/16, 10/10 — re-run green against a `main` that had moved 683 commits)
and the cross-references are on `main`.

**Nothing was decided, deliberately.** No content block changed; the three
strand counts `A+Z` / `3A` / `3A+Z` are all still live. This bean stays open
because its subject is a naming decision only the author can make.

**What merging added: the decision is now PRICED, and no option is free.**

* **(a) `A+Z` canonical** — cheapest for bean `qou-q6pp`, whose leading
  explanation for the wrong-signed p–n splitting is stated in this reading
  already. Minority in production, 7 blocks against 26.
* **(b) `3A` canonical** — the production majority. But `qou-q6pp`'s explanation
  INVERTS: the atom at the uniquely-exact `n = 3` becomes H-1, which that bean
  itself records as over-specified and 5e5 off.
* **(c) `3A+Z` canonical** — loses no structure and is the join of the other
  two. But `qou-q6pp`'s explanation EVAPORATES: no neutral atom reaches `n = 3`,
  since `min(3A+Z) = 4` over `A ≥ 1, Z ≥ 1`.

A second consumer points the other way: #6919's `f₁/f₀` additivity across the
two nucleons is **only statable** under `3A` or `3A+Z` — under `A+Z` a nucleon
is one strand, so "which generators does nucleon k own" has no referent.

**Default if the author says nothing: nothing moves.** Three counts stay live,
the `𝓑_K` collision stays unregistered in `notation-collisions.md`, and the
audit now records the disagreement accurately instead of understating it. That
is a safe place to leave it.

**Sibling constraint on option (a).** #6952's rename tranche records the
corpus's own measurement that renaming the `3A` object costs **685 call sites
across 382 files**, and that this was considered and rejected in PR #5765. So
the cheap instrument for whichever cell wins is a scoping note plus a
notation-register entry — not a rename. #6952 excluded
`mass-endomorphism/atomic-mass-gb-nf.md:3` by name, recording that this bean's
decision governs it.
