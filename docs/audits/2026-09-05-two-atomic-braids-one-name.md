# `def:atomic-braid` is not the object the mass law traces — two constructions, one name, one symbol

**Date:** 2026-09-05
**Bean:** `qou-jgg0`
**Probe:** [`computations/probes/two_atomic_braids_one_name_probe.py`](../../computations/probes/two_atomic_braids_one_name_probe.py) — 5/5, exit 0, no witness
**Follows:** [`2026-09-05-which-n-the-nucleus-is-a-state-at.md`](2026-09-05-which-n-the-nucleus-is-a-state-at.md) §5, which reported the strand count as "unreconciled" and did not measure it

---

## 0. What was reported, and what is actually the case

The prior note listed, under *not established*:

> **The strand count.** `H_{A+Z}` (`atomic-braid.md:2`, `wedderburn-mass-formula.md:2`)
> against `H_{3A}` (`schur-weyl-mass-decomposition.md:1`, `hecke_3a_weights.py:5`)
> is still unreconciled by any block.

Measured, that framing is too weak. It is **not a disagreement about a number.**
The two are different constructions:

| | `def:atomic-braid` | production `atom_braid_word_3A` |
|---|---|---|
| algebra | `H_{A+Z}(q)` | `H_{3A}(q)` |
| strands | `A` nucleons **+ `Z` electrons** | 3 quarks per nucleon, **no electrons** |
| per nucleon | one strand | three strands |
| interactions | 6 pair types, **3 electronic** (`pe`, `ne`, `ee`) | intra-nucleon confinement core (β_Bor) + inter-nucleon bonds |

Both are written `\mathcal{A}` and both are called *"the atomic braid"*.

## 1. `H_{A+Z}(q)` cannot hold the production word

Not a convention difference — a containment failure, at every `A` (check 1):

| atom | `A` | `A+Z` (the definition) | `3A` | strands the word needs | fits? |
|---|---|---|---|---|---|
| proton, H-1 | 1 | 2 | 3 | **3** | **NO** |
| helium-4 | 4 | 6 | 12 | **12** | **NO** |
| iron-56 | 56 | 82 | 168 | **168** | **NO** |

"Strands the word needs" is `max(generator index) + 2` over the word
`atom_braid_word_3A` actually returns, and it equals `3A` exactly at each atom
(asserted, not eyeballed). The proton's word uses `σ₀` and `σ₁`, which requires
3 strands; `def:atomic-braid` gives it 2.

## 2. The definition's electron content has nowhere to go

`def:atomic-braid`'s Table 1 specifies six pair types, of which **three are
electronic** — `pe` (EM attraction), `ne` (no interaction), `ee` (EM repulsion).
The production word's source does not contain the string `electron` at all
(check 2).

So this is not a definition that got the strand count wrong. It is a definition
of a **different object**: an atom *including its electron shell*, which the 3A
construction does not model and has no strands for.

## 3. Blast radius

**24 content blocks cite `def:atomic-braid`; 7 of them are in the mass
chapters** (check 4):

- `mass-endomorphism/atomic-mass-gb-nf.md`
- `mass-theory/active-set-trace-concentration.ts`
- `mass-theory/canonical-closure-torus-chain.{md,ts}`
- `mass-theory/subset-cumulant-recursion.{md,ts}`
- `mass-theory/wedderburn-mass-formula.md`

The last is the sharpest: it opens *"Let `(Z, N)` be a neutral atom with atomic
braid `\mathcal{A} ∈ H_{A+Z}(q)` ([atomic braid](#def:atomic-braid))"* while
sitting in the chapter whose sibling block `schur-weyl-mass-decomposition.md`
opens *"The Markov trace of the atomic braid `\mathcal{A} ∈ H_{3A}(q)`
decomposes over partitions `λ ⊢ 3A`"*. Same chapter, same name, same symbol,
different algebra.

*(The prior draft of this section said 12 blocks. That was a truncated grep;
the probe counts 24. Quote the probe.)*

## 4. Production is self-consistent — this is not a claim that the mass law is wrong

Strand-count lines across `computations/`, excluding `_deprecated`:

| reading | lines | files |
|---|---|---|
| `3A` | **824** | **377** |
| `A+Z` | 9 | 4 |

and of those four A+Z files, one carries deprecation markers and one is a test
(`wedderburn_Mi_constructor_test.py`). Production computes the 3A object
throughout. **Nothing here says a number is wrong**; it says a definition block
describes something else.

## 5. The decision this leaves, and it is the author's

Two readings, and they call for opposite actions. This note takes no position.

**(a) `def:atomic-braid` is a real, separate, currently-uncomputed object** — the
atom *with* its electron shell, of which the nuclear 3A braid is the
electron-free core. Then nothing is wrong except that **two objects share one
name and one symbol**, and the fix is naming: the 3A object needs its own label
(`def:nuclear-braid`, say), the mass chapters' citations get repointed, and
`\mathcal{A}` is disambiguated in the notation register. The electron rows in
Table 1 are then content worth keeping, not an error.

**(b) `def:atomic-braid` is superseded** by the 3A construction. Then it needs
retiring, and its 24 citations rehoming.

The evidence does not settle which: (a) is supported by the electron rows being
specific and physically motivated rather than vestigial; (b) by nothing in
`computations/` ever having built the `A+Z` object. What *is* settled is that
the status quo — both under one name, cited across chapters — cannot be right
under either reading.

## 6. Not established

- **That either object is wrong.** Only that they are different and share a name.
- **That the 7 mass-chapter citations are load-bearing.** They cite the
  definition; whether any of them *depends* on the `A+Z` strand count for a
  result was not measured.
- **Which of `\mathcal{A}`'s two meanings the notation register intends.** The
  register (`notation-collisions.md`) does not currently disambiguate them —
  and that block has **no QA coverage at all**, because `qa-sweep` enumerates
  blocks by label and `notation-collisions.ts` declares none, so no collision
  detector could have caught this. (Measured separately; the write-up is on the
  unmerged branch of PR #6817, deliberately not linked here so this note carries
  no forward reference to a file `main` does not have.)
