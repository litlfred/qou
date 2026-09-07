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

**19 content blocks cite `def:atomic-braid`; 5 of them are in the mass
chapters** (check 4).

> **🛑 CORRECTED 2026-09-05 — this read "24 blocks; 7 of them", which are the
> FILE counts.** A block is a `.ts`/`.md` pair sharing one stem, so a block
> citing the definition in both its manifest and its prose is two files.
> Measured: **24 files (10 `.md` + 14 `.ts`) over 19 blocks**; in the mass
> chapters **7 files over 5 blocks**. The file figures are correct as files and
> were reported as blocks. Check 4 now prints both and asserts they differ, so
> the unit cannot silently drift again. (This is the second unit/count defect
> in this same probe — the first was a truncated grep reporting 12.)

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
retiring, and its citations — 19 blocks, 24 files — rehoming.

The evidence does not settle which. (a) is supported by the electron rows being
specific and physically motivated rather than vestigial.

> **🛑 THE EVIDENCE I GAVE FOR (b) IS FALSE — corrected 2026-09-05.** This
> paragraph read *"(b) by nothing in `computations/` ever having built the
> `A+Z` object."* Measured, that is wrong:
> **[`computations/_deprecated/atom_braid_electron.py`](../../computations/_deprecated/atom_braid_electron.py)
> builds exactly this object**, and its own docstring says so —
>
> > *"ATOMIC BRAID: electrons included in the `H_{A+Z}(q)` braid. The nuclear
> > braid `H_A(q)` uses A nucleon strands. This script adds Z electron strands,
> > creating `H_{A+Z}(q)` with crossing coefficients …"*
>
> — with **all six pair types**, including the three electronic ones the
> definition specifies (`pe → α_EM mixed`, `ne → trivial`, `ee → α_EM
> repulsion`), and `α = α_EM` derived from `q₀`. A committed witness
> (`p2-5-symbolic-q-audit.witness.json`) references it. So the A+Z object was
> **built and then deprecated**, which is a different claim from *never built*
> and only one of the two was measured. Check 5 now asserts it.
>
> **Which way this cuts is not obvious, and I am not going to pretend it is.**
> Deprecation is evidence the corpus *moved off* the object, which reads
> toward (b). Its existence with the full electronic pair table is evidence the
> object is real and specified, which reads toward (a). What is now certain is
> that "(a) requires building something new" is false — a prior implementation
> exists to start from.

**And a third strand COUNT is live — but be precise about what it is.**
[`electron_sigma_f_chain.py`](../../computations/electron_sigma_f_chain.py)
uses `n_target = 3A + Z`: three quark strands per nucleon **plus** Z electrons,
which is neither the definition's `A+Z` nor production's `3A` (check 6, 1 live
producer, `_deprecated/` excluded).

> **🛑 RETRACTED, same branch, 2026-09-06 — this said "it is NOT a third braid
> construction" and that is a claim about one FILE promoted to a claim about the
> CORPUS.** The file-level evidence below is correct and re-verified (check 8 of
> the new probe): `electron_sigma_f_chain.py` uses `3A + Z` as the
> confinement-SDP normalisation `tr Φ = n_target`, sweeps `Z = 0…8` to show
> `σ_F = n_target·y₀*` is monotone in the electron count, and **never** imports
> or calls `atom_braid_word_3A`. All of that stands.
>
> What does not stand is the inference. A **content block** asserts the braid
> itself on `3A + Z` strands:
>
> > [`mass-endomorphism/atomic-mass-gb-nf.md:3`](../../content/quantum-observable-universe/mass-endomorphism/atomic-mass-gb-nf.md)
> > — *"atomic braid $\mathcal{B}_K \in B_{n}$, where $n = 3A + Z$"*
>
> `B_n` is the braid group. So `3A + Z` is a third strand count **and** a third
> braid, and the sentence telling the next agent not to look for one would have
> sent them past the block that has it. Found by corpus-grep, not by re-reading
> the file — the file was measured correctly both times.
>
> The narrower thing the file does establish is unchanged and still useful: the
> corpus models **an atom's electron dressing on top of a 3A nuclear core**,
> reading (a)'s picture arrived at from the SDP side rather than the braid side.

**The structure is a 2×2, not a three-way argument.** Two independent binary
choices — is a nucleon one strand or three, and are the Z electrons in or out:

|  | electrons **in** | electrons **out** |
|---|---|---|
| **nucleon**-strand | `A + Z` — `def:atomic-braid`, **7** blocks | `A` — *coarsening only* |
| **quark**-strand | `3A + Z` — `atomic-mass-gb-nf`, **1** block | `3A` — production, **26** blocks |

Three cells are asserted as the home of the atomic braid. The fourth appears in
[`level-sufficiency-interprets.md:41`](../../content/quantum-observable-universe/knots-particles-confinement/level-sufficiency-interprets.md)
as `|H_A(R,q)| = A!` but explicitly as **"Default-coarse computation"** — an
approximation, not a competing claim, so the live disagreement is three-way.

Three facts that make this worse than a count discrepancy, all measured
([`strand_count_is_a_two_by_two_probe.py`](../../computations/probes/strand_count_is_a_two_by_two_probe.py), 12/12):

1. **The collision is on a symbol, and the notation register is a disputant.**
   `notation-register-table3-data.md:7` says $\mathcal{B}_K \in H_{3A}(q)$;
   `atomic-mass-gb-nf.md:3` says $\mathcal{B}_K \in B_n$, $n = 3A+Z$. Same
   symbol, same described object. AGENTS.md §7aa makes the register
   authoritative for symbols, and `notation-collisions.md` carries **no entry**
   for $\mathcal{B}_K$ — the collision is unregistered.
2. **The disagreement sits inside one citation edge.** `atomic-mass-gb-nf.md`
   links `#def:atomic-braid` *while using a different count than that
   definition gives*. It is not two chapters drifting apart; it is one block
   contradicting the definition it points at.
3. **They never coincide.** `A+Z < 3A < 3A+Z` strictly for every `A ∈ 1..60`,
   `Z ∈ 1..A` (0 clashes), so no atom and no reading reconciles them by
   accident. And `3A+Z` is exactly the **join**: `(3A+Z) − 3A = Z` and
   `3A − A = 2A`, the two axes independent — which is why the one construction
   that carries electrons *and* splits nucleons lands there.

So a renaming that assumes two objects has a third *count* **and** a third
*braid* to account for — three cells, not two.

What *is* settled is that the status quo — two objects under one name, cited
across chapters — cannot be right under any of these readings.

## 6. Not established

- **That either object is wrong.** Only that they are different and share a name.
- **That the 5 mass-chapter citing blocks are load-bearing.** They cite the
  definition; whether any of them *depends* on the `A+Z` strand count for a
  result was not measured.
- **Which of `\mathcal{A}`'s two meanings the notation register intends.** The
  register (`notation-collisions.md`) does not currently disambiguate them —
  and that block has **no QA coverage at all**, because `qa-sweep` enumerates
  blocks by label and `notation-collisions.ts` declares none, so no collision
  detector could have caught this. (Measured separately; the write-up is on the
  unmerged branch of PR #6817, deliberately not linked here so this note carries
  no forward reference to a file `main` does not have.)
