---
# qou-jgg0
title: 'qou-atbr: def:atomic-braid and the mass law''s atomic braid are DIFFERENT objects sharing a name and a symbol'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T09:58:53Z
updated_at: 2026-10-10T07:58:20Z
parent: qou-d8c7
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
`folio/quantum-observable-universe/mass-endomorphism/atomic-mass-gb-nf.md:3`
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

## 2026-09-11 — ANSWERS one "Not established" item: the mass-formula citation IS load-bearing

This bean's own list says:

> *"That the 7 mass-chapter citations are load-bearing; whether any **depends**
> on the `A+Z` count for a result was not measured."*

**Measured for `wedderburn-mass-formula.md`: yes — and the dependence is not a
shift in a number, it is a change of subject.**

| reading | strand count | unique atom with `p(n) = 3` |
|---|---|---|
| **(a)** `def:atomic-braid` | `A + Z = 2Z + N` | **deuterium** (`n = 3`) |
| **(b)** production | `3A = 3(Z+N)` | **hydrogen-1** (`n = 3`) |

`p(n) = 3` is the condition that the **three extremal Wedderburn blocks exhaust
the partitions of `n`** — the whole reason the `n = 3` point is interesting, since
it is the one place where "the three extremal invariants" are not a truncation of
a longer list. Under (b), deuterium sits at `n = 6` where `p(6) = 11`, so it is
**not** an exhaustion point at all.

**Exact, not swept.** `p` is strictly increasing on `n ≥ 1`, so `p(n) = 3` iff
`n = 3`. Then `2Z + N = 3` with `Z ≥ 1` has the unique solution `(1,1)`, and
`3(Z+N) = 3` with `Z ≥ 1` has the unique solution `(1,0)`. The `Z ≥ 1` restriction
is load-bearing: admitting `Z = 0` manufactures a spurious `(0,3)` under (a).

### Where this bites right now

PR #7171 (merged, `20671dcc1`) added `rem:level-zero-discards-braid-noncommutativity`,
which states flatly:

> *"Deuterium is the unique atom with `n = A + Z = 3`."*

True under (a). Under (b) that sentence names the wrong atom. The remark does not
mention the `3A` reading or this bean — verified mechanically, check 6. The same
applies to `deuterium_is_the_untested_exact_point_probe.py` check 1 (*"D sits in
`H_{A+Z}` = `H_3`"*) and to the whole framing of #7162.

So those artifacts are **(a)-conditional and assert their premise flatly** — the
"conditional-proved ≠ premise-established" defect, in content I authored hours
before measuring this.

### Scope

**This does NOT adjudicate (a) vs (b)**, which this bean reserves to the author,
and it does not claim either object is wrong. It measures what turns on the
choice. Scope (a): it constrains what depends on the reading; it excludes nothing.

**Not established here:** whether the other six mass-chapter citations are
load-bearing. Only `wedderburn-mass-formula.md` was measured.

**Verification:** `computations/probes/strand_count_reading_is_load_bearing_probe.py`,
**15/15**, exit 0. Every quantity is an exact integer (partition counts, strand
counts) — no float64 is reachable, no mpmath, no witness.

**Bean stays open** (rule 13a): the (a)/(b) decision is unresolved mathematics.

## 2026-09-11 — the blast-radius line counts CITATIONS; the dependency surface is ~1 block

This bean's blast-radius section reads *"24 citing blocks, 7 in the mass chapters"*
and lists them. **Citing `def:atomic-braid` is not the same as depending on its
strand count**, and measured, almost none of them do.

The 24 (re-derived independently — same count) classify by the strand count each
block actually uses:

| bucket | n | blocks |
|---|---|---|
| **no strand count at all** | **16** | they cite the crossing table or the ground-state ordering, both reading-independent |
| `3A` | 4 | `atom-knot-exists-proof.md`, `active-set-trace-concentration.ts`, `canonical-closure-torus-chain.md`, `subset-cumulant-recursion.md` |
| `3A + Z` (the third count) | 1 | `mass-endomorphism/atomic-mass-gb-nf.md` |
| `A + Z` | 3 | see below |

Of the three `A+Z` hits, **two are not consumers**:

- `knots-particles-confinement/atomic-braid.ts` is **the definition's own
  manifest** (`label: "def:atomic-braid"`), whose `title` is
  *"Atomic braid `$H_{A+Z}(q)$`"*;
- `index-of-definitions/definition-index.md` is a **catalogue echoing that
  title** on one row — its `3A` hits belong to unrelated entries
  (`rho-k-h3a-refinement`, `atom-braid-exterior-algebra`,
  `psd-trace-orthogonality`).

**So exactly one consumer carries the `A+Z` reading: `mass-theory/wedderburn-mass-formula.md`.**

### Why this matters for the (a)/(b) decision

It re-prices option **(b)** — *"`def:atomic-braid` is superseded; retire it and
rehome its 24 citations"*. The content-side rehoming is **one consumer block,
plus the definition's own title and one index row**, not 24 and not 7. The other
five counted blocks have already committed to the production side (`3A`, or `3A+Z`),
and 16 never touch a strand count.

That does **not** argue for (b) — the electron rows in Table 1 are still specific
and physically motivated, which is this bean's own evidence for (a). It removes a
cost from (b)'s side of the ledger, nothing more.

### Scope, and what is NOT measured

- **Content blocks only.** The code side is already this bean's: 824 strand-count
  lines across 377 files on `3A` against 9 lines across 4 files on `A+Z`.
- **"Uses a strand count" is a textual classification**, ordered so that `3A + Z`
  is matched before `3A` and `A + Z` (it contains both). A block could depend on
  the count without writing it; that is not detected here.
- Still **not** adjudicating (a) vs (b).

**Verification:** `computations/probes/strand_count_reading_is_load_bearing_probe.py`
checks 8–10, part of **22/22**, exit 0.

**Bean stays open** (rule 13a).

## 2026-09-11 — RETRACTION of my own entry above: the A+Z surface is ≥ 4, not 1

The entry immediately above concludes *"exactly one consumer carries the `A+Z`
reading"* and re-prices option (b) on it. **That is wrong as a dependency claim,
and I flagged the exact gap it falls into in its own scope note** — *"whether a
block could depend on the count without writing it; that is not detected here."*
Three do.

**All three are in `molecular-construction`, and the arithmetic is spelled out in
words:**

| block | says | that is |
|---|---|---|
| `co-molecular-braid-carbon-monoxide.md` | *"`𝒜_C ∈ H_{18}(q)` has 18 strands (12 nucleons + 6 electrons)"* (`Z=6,N=6,A=12`) | `A+Z = 18`; `3A` would be **36** |
| same | *"24 strands (16 nucleons + 8 electrons)"* (`Z=8,N=8,A=16`) | `A+Z = 24`; `3A` would be **48** |
| same + its `.ts` | *"`H_{42}(q)` (`18 + 24 = 42` strands)"* | under `3A`: `36 + 48 = 84` |
| `h2-molecular-braid.md` | *"an atomic braid in `H_2(q)`: one proton and one electron"*, then `H_4` for the molecule | `A+Z = 2`; `3A` would be **3** |

**"nucleons + electrons" IS the `A+Z` construction.** None of these blocks writes
the string `A+Z`, so the textual classification counted all of them as *"no strand
count at all"*.

### This reverses the re-pricing, and it strengthens reading (a)

Option (b) does **not** cost one block. The molecular chapter is built on
`A + Z` numerically, and under (b) — `3A`, **no electrons** — it has no electrons
to bond with. That is not a rehoming; it is a structural problem for (b).

It also answers this bean's own *"The electron content has nowhere to go"*: it
does have somewhere to go. It goes into `molecular-construction`, which is
entirely built on it.

### The full numeric census, exhaustive

Seven of the 24 citing blocks carry a bare numeric `H_n`, and **a numeric `H_3`
means three different things** among them:

| kind | n | blocks |
|---|---|---|
| `A+Z` arithmetic | **3** | the molecular ones above |
| **per-nucleon** `H_3` (the quark triple) | 2 | `atom-knot-exists-proof.md` (*"each nucleon … canonical NF in `H_3(R,q)` on 3 strands"*, and it writes `H_{3(Z+N)}` for the atom), `active-set-trace-concentration.ts` (`(H_3)^{⊗A}`) |
| the **trefoil's** `H_3` (`T_{2,3} = σ₀σ₁σ₀`) | 1 | `electron-shell-braid-capacity.md` |
| catalogue | 1 | `definition-index.md` (18× `H_3` from other entries' titles) |

The last two are false positives for any scan that reads a numeric `H_n` as a
strand count, and both were caught by reading the block rather than by the regex.

### What stands from the entry above

The **16 blocks that use no strand count at all** and the **5 on the production
side** are unchanged. What is retracted is only the final step: *citations (24) ≫
dependencies (1)*. The correct figure is **≥ 4**, and "≥" is deliberate — the
numeric scan keys on `H_n`, so a block depending on the count through prose or a
witness would still be missed.

**Verification:** `strand_count_reading_is_load_bearing_probe.py` checks 11–14,
part of **31/31**, exit 0. Check 11's first assertion failed at 4 and was corrected
to the measured 7 before this was written.

**Bean stays open** (rule 13a).

## 2026-09-11 — a FOURTH surface (Lean), and the pattern that ties all of them together

This bean measured **content blocks** and **Python**. The `.lean` surface was
never counted — the same omission AGENTS.md records for the convention-C audit,
whose detector walked the tree four times and every pass was `rglob("*.py")`.

**Both readings have Lean carriers. `3A` dominates numerically; every `A+Z`
carrier is in the electron domain.**

| reading | Lean files | character |
|---|---|---|
| `3A` | **20** | incl. `conj-rho-prefactor-structural.lean`'s *"Sanity: the strand count is exactly `3 * (Z + N)`"* — a **constraint** |
| `A + Z` | **3** | below |

The three `A+Z` carriers:

1. **`knots-particles-confinement/atomic-braid.lean`** — the definition's own
   sibling. It encodes `A+Z` as a **field default** (`totalStrands : Nat := A + Z`)
   and its one theorem is `rfl` on that default. Its own docstring says *"for an
   arbitrary `NeutralAtom` the `A` and `totalStrands` fields are independent and
   may be set to non-default values"* — so a `NeutralAtom` with
   `totalStrands := 3*A` is well-typed. **The Lean does not force (a); it defaults
   to it.** Per AGENTS.md rule 8, a proposition true by unfolding is notation
   rather than a theorem; flagged as a shape, not declared a violation.
   It also carries the six `PairType` constructors **including `pe`, `ne`, `ee`**.
2. **`lean/QOU/BraidKnot/ElectronShell.lean`** — a **library** file, and a real
   construction rather than a default: the cabling `H_A(q) ↪ H_{A+Z}(q)` plus an
   SDP-selected binding subword `W_bind ∈ BraidWord (A+Z)`, *"Total strand count
   `A + Z` after cabling"*. 24 mentions of "electron".
3. **`molecular-construction/h2o-molecular-braid.lean`** — water, with the
   arithmetic explicit: *"oxygen `O(8,8)` (A+Z = 16+8 = 24 strands)"*.

### The pattern, across all four surfaces

Of the **seven** `A+Z` carriers now identified — 3 Lean, 3 content
(`co-molecular-braid-carbon-monoxide.{md,ts}`, `h2-molecular-braid.md`), 1
mass-theory (`wedderburn-mass-formula.md`) — **six are electron-shell or
molecular.** Only `wedderburn-mass-formula.md` is not.

That is the sharpest form of this bean's own evidence for (a): the `A+Z` reading
is not scattered residue, it is **the reading the electron/molecular/shell domain
is built in** — and reading (b) is `3A` with **no electrons**, so it cannot serve
that domain at all.

**The Lean count itself cuts the other way** (20 vs 3), and that is recorded as
found. The two observations are not in conflict: `3A` is where the *mass* pipeline
lives, `A+Z` is where the *electron* content lives. That is closer to this bean's
option (a) — two real objects needing two names — than to (b).

### Two scan errors of mine, both the same class

- I grepped `lean/QOU/` for `NeutralAtom`, got **zero**, and nearly reported the
  definition's Lean ref as dangling. It is the **content-block sibling**
  (resolution path 1, AGENTS.md §0a); `lean/QOU/` is path 2 only.
- I then asserted the sole `A+Z` Lean carrier was that sibling. The counting check
  fired and returned **three**. The two extras are the substantive ones.

Both were caught by making the probe count rather than assert. Recorded because
this is the third and fourth time in this arc that a scan's *scope* — not its
pattern — was the defect.

**Verification:** `strand_count_reading_is_load_bearing_probe.py` checks 15–19,
part of **44/44**, exit 0.

**Bean stays open** (rule 13a). (a)/(b) still the author's.

## 2026-09-12 — 🟧 OWNER RULING: option (a). `𝒜` is the `A+Z` object. And the corpus already held the deciding measurement.

**Ruling (owner, verbatim instruction: *"try Recommendation 1 + 5"*).** `𝒜 ∈ H_{A+Z}(q)`
— the atom with its electron shell, as `def:atomic-braid` states — is canonical for the
symbol. The production `3A` word is the electron-free nuclear core and is written
`𝓑_K ∈ H_{3A}(q)`, the name it already has in `notation-register-table3-data.md:7`.

**It is a SCOPING decision, not a rename, and that is what makes it cheap.** No call
site moves. #6952 measured renaming the `3A` object at **685 call sites across 382
files**, considered and rejected in #5765. Under (a) no rename is needed, because the
`3A` object was never missing a name — what was missing was the statement that the two
are different objects.

### What decided it, and it was already here

This bean spent 2026-09-05 → 09-11 measuring **where** each reading is carried and
**what turns on** the choice, and repeatedly said no reading is free. It never found a
quantity that **decides**. There is one: the recorded **Φ₃ column** of the Z=1–20 mass
table, sitting in `phi_allpairs_reconstruction.py` (on `main`, `1fe569c05`) since before
this bean opened.

**Parameter-free** — Table 1's crossing signs, each cell's own pair counts, exact
integers, no tolerance:

| cell | Φ₃ column | He, against a recorded −6 |
|---|---|---|
| `A` (nucleons only) | **0/19** | 0 |
| **`A+Z` (a)** | **19/19** | **−6** |
| `3A` (b) | **0/19** | 0 |
| `3A+Z` (c) | **0/19** | −22 |

The `ee` count `C(Z,2)` and the `pe` count `Z²` presuppose `Z` electron strands. The
electron contribution has an exact closed form on all 20 rows:
`w(A+Z) − w(A) = 2[C(Z,2) − Z²] = −Z(Z+1)`, which at Ar is **342**.

**Then GRANT each cell three fitted coefficients** — deliberately generous, run
symmetrically, labelled a fit; exact rational Cramer over all 969 anchor triples:

| cell | best fit | coefficients | integral? |
|---|---|---|---|
| `A` | 18/19 | `(2, 0, −2)` | yes — **misses Ar, and only Ar** |
| **`A+Z` (a)** | **19/19** | **`(4, −2, −2)`** | **yes** |
| `3A` (b) | 10/19 | `(7/15, 1/5, −4/9)` | no |
| `3A+Z` (c) | 10/19 | `(13/15, −1/5, −4/3)` | no |

**The second table is the sharper half.** A three-parameter search on (a)'s basis
**recovers the parameter-free answer** — `(4, −2, −2)` is `2(pp+ee)`, `2·nn`, `2·pe`
read straight off Table 1 — while (b) and (c) cannot reach the column even when fitted,
and want coefficients no crossing table produces. Under the owner's no-fitting directive
that is the ranking that counts: (a) wins the *derivational* test, not an accuracy
tie-break.

### 🛑 CORRECTION to this bean's own evidence for (b)

The 2026-09-05 entry says, as evidence *for* (b):

> *"For (b): nothing in `computations/` has ever built the `A+Z` object."*

**That is FALSE.** `atom_gen_chains` / `atom_gen_chains_sym`
(`computations/substrate/hecke_core_symbolic.py:271`) build all-pairs nucleon crossings
**plus `Z` electrons each contributing `(1, −h)`** — the `pe` crossing.
`computations/unified-mass-molecular.py` emits a witness and says so in its own header
(*"Full atomic braid `H_{A+Z}(q)`: nucleons + electrons"*).

Measured on `main` `03d6c9485`: **23** importers of the `A+Z` family against **380** of
`atom_braid_word_3A`, and **5 files import BOTH** — including
`tools/pyhecke/python/pyhecke/atom.py` (a library module) and
`scripts/word-provenance-gate.py` (a gate), a live layer-straddle surface.

**Re-measure; do not quote those integers.** The `3A` figure was **378** at `1c443dddc`
the same morning and reached 380 when two sibling probes landed
(`brng_dominant_summand_ursell_probe.py`, `binding_word_3A_reembedding_probe.py`) —
nothing in this analysis moved. The durable fact is the **shape**: both objects are
implemented, `3A` by ~16× as many files, and a handful import both. Check 16 of the
probe recomputes the counts against whatever base it runs on and asserts only that
shape, so it cannot go stale the way this sentence can.
So the ledger line reading "(a) has the definition, (b) has all the code" was wrong in
its second half: both objects are implemented, and they serve different things.

### Instruments landed (PR #7215)

- `notation-collisions.md` — a `𝒜` vs `𝓑_K` entry, the register being authoritative
  for symbols per AGENTS.md §7aa.
- `def:atomic-braid.md` — a scope paragraph in the definition's own voice (the electron
  rows are part of the definition; `H_{A+Z}` cannot contain a `3A` word at any `A`).
- `atomic-braid.ts` `authorNotes` — the dated ruling and its provenance, per §4d. The
  first draft put the ruling in prose as a dated banner and `voice-author-notes-pollution`
  flagged it; baseline for that block is **1** pre-existing hit (line 11) and the
  rewrite is back at 1.
- Probe `computations/probes/phi3_column_discriminates_the_strand_count_probe.py`, 35/35,
  and `docs/audits/2026-09-12-phi3-column-discriminates-the-strand-count.md`.

The probe **derives** the six Φ₃ signs from Table 1's own `(c, d)` by exact symbolic
arithmetic rather than transcribing them — `phi_allpairs_reconstruction.py` hardcodes
them. It also caught two of my own scan defects: the row parser could not see `ee` (a
lookaround on a bare `e` cannot separate two adjacent `e`s), and the importer scan
counted the probe itself as a layer straddle.

### 🛑 SCOPE — what the ruling does NOT settle, and why this bean STAYS OPEN (rule 13a)

- **Scope-(a), not a structural exclusion.** *These* pair-count constructions on *these*
  bases fail. A colour-weighted quark-level construction on `3A` is **untested** and is
  not excluded.
- **The third count `3A+Z` is still live** in `mass-endomorphism/atomic-mass-gb-nf.md:3`,
  which cites `def:atomic-braid` while using a count that definition contradicts. The
  ruling names two cells; it does not resolve that citation, and it was deliberately not
  edited.
- **Φ₂ does not discriminate** (`Z·N` is identical under `A` and `A+Z`); **Φ₁ is not
  closed** under any reading.
- **The target is a recovered producer's intermediate**, not the published paper table:
  the witness `atom-mass-complete-wedderburn` is out of tree since the miga split, and
  its own `β₃ = 0.0499` disagrees with the published `h_A² = 0.0437073` by **14.2 %**.
  Verified rather than assumed that the column is `w·ln q₀` with integer `w` at the
  proton pin (worst rel dev **1.23e-5**, uniform — the six-decimal recording precision).
- **#6919's `f₁/f₀` disjoint-support additivity is only statable under `3A`/`3A+Z`** —
  the counter-pressure recorded on 2026-09-06 is unchanged by this ruling, and under (a)
  that question has no referent rather than a different answer.
- **`qou-q6pp`'s wrong-signed p–n splitting is untouched.** Its leading explanation is
  stated in the `A+Z` reading already, so the ruling leaves it where it was — open.

## 2026-09-12 (later) — the producer's own recorded ORDERING is A+Z

Probe [`recovered_witness_ordering_confirms_a_plus_z_probe.py`](../computations/probes/recovered_witness_ordering_confirms_a_plus_z_probe.py), 22/22; PR #7232.

**Independent corroboration of the owner's ruling, from a direction this arc has
not used.** The recovered witness `atom-mass-complete-wedderburn` (commit
`1359fe23ac`) carries an `ordering` field the published table does not — a
per-atom string over `{p, n, e}`. For **all 13** atoms with `A+Z ≤ 40`,
`len(ordering) == A+Z` exactly **and** the letter counts are exactly
`(#p, #n, #e) == (Z, N, Z)`. Thirteen of thirteen, no exceptions.

That is not a content block, not a Lean declaration, not an importer count — it
is the recorded **internal state of the producer that generated the published
numbers**. `A` is excluded on every row (`len ≠ A`); `3A` and `3A+Z` exceed
`A+Z` for every `Z ≥ 1`.

**🛑 `git show` cannot reach the witness here.** Agent clones are shallow, so
`1359fe23ac` is absent (`fatal: Not a valid object name`), and per AGENTS.md a
direct `git fetch origin <sha>` does not help. The GitHub contents API does:
`mcp__github__get_file_contents(path=…, sha="1359fe23ac")`. Recorded so the next
agent does not repeat the dead end.

**Two limits on the data.** The last 7 rows (28Si onward, `A+Z ≥ 42`) are
**truncated at exactly 40 characters**, so their orderings are unrecoverable and
their letter counts no longer match — do not read that as contradicting the
result above. And the orderings are **interleaved**, never blocked (`4He` is
`enpepn`, `7Li` is `epenpenpnn`).

**A side finding that is not about `jgg0`:** the producer's nucleon masses are
**not CODATA** — `m_p` 41.6 keV low, `m_n` 33.4 keV low, while `m_e` matches to
1e-7 — so the table's `Z·m_p + N·m_n` baseline carries a systematic on every row.
Their difference is 0.64 % high, which is `qou-q6pp`'s p–n splitting. Provenance
unknown and not guessed. Tracked in `qou-1jw9`.

**Bean stays open** (rule 13a): the `3A+Z` third cell in
`mass-endomorphism/atomic-mass-gb-nf.md:3` is still untouched — the owner ruled
on two cells.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — reparented to the mass-endomorphism epic

This bean is carrier M9 of epic `qou-d8c7` (issue litlfred/qou#7547). Parent moved from `qou-v2om` to `qou-d8c7`; nothing in the body above was changed by the move.



## 2026-10-10 — 3A+Z cell resolved: owner choice B1

`mass-endomorphism/atomic-mass-gb-nf.md` now states `𝓑_K` on `3A` strands (the electron-free core), naming `𝒜 ∈ H_{A+Z}` only as the object it is the core of. Corpus-consistent: its producer `canonical_mass_table_extended.py` uses `n = 3*A`, and its interpretation block already writes A=3 as n=9. `notation-collisions.md` updated from 'unresolved'. PR #7559. Bean STAYS OPEN (rule 13a): the SCOPE items of 2026-09-12 (colour-weighted 3A construction untested, qou-q6pp p–n sign, #6919 additivity) are untouched.
