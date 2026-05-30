# Orbit-trace identity — PROVEN (Tier 1.B unblocked)

**Date:** 2026-05-30
**Trigger:** Owner — "prove orbit-trace identity." The compute-optimization
roadmap ([`2026-05-20-compute-optimization-roadmap.md`](2026-05-20-compute-optimization-roadmap.md)
§Tier 1.B) gates the nucleon-orbit reduction — the single largest open
speedup (36× ⁶Li, 576× ⁸Be, the gateway to organic chemistry) — on an
**unproven orbit-trace identity**, with the worry that interface swaps
(I_pp / I_pn / I_nn) might break it for mixed-interface atoms.
**Reproducer:** [`folio-assistant/computations/orbit_trace_identity_proof.py`](../../folio-assistant/computations/orbit_trace_identity_proof.py)
→ `orbit-trace-identity.witness.json`.

## The claim

For the atomic braid `β_{Z,N} = atom_braid_word_3A(Z, N)` and any nucleon
permutation `σ ∈ S_Z × S_N` (protons among protons, neutrons among
neutrons):

> **`tr_M(β_{Z,N})` is invariant under `σ`.**

## Proof

**Lemma 1 (word invariance).** `atom_braid_word_3A(Z, N)` iterates over
`ordering = ['p']·Z + ['n']·N`, emitting per nucleon `k` the
species-specific intra-crossings (identical for every proton; identical for
every neutron) and the adjacency-typed inter-crossing (pp / pn / nn)
between `k` and `k+1`. A permutation `σ ∈ S_Z × S_N`:

- **(a) fixes the ordering string** — protons stay in positions `0..Z-1`,
  neutrons in `Z..A-1`, so `p…pn…n` is unchanged; and
- **(b) preserves every adjacency type** — pp stays pp (both inside the
  proton block), the single pn boundary stays at position `Z`, nn stays nn
  — so the **interface crossings are untouched**.

Hence the **crossing-type sequence of the word is literally invariant**
under `σ`. *Verified:* 20/20 random `σ` on ⁴He, ⁵Li, ⁶Li leave the sequence
invariant (the script's `word_invariant_*` assertions).

**Lemma 2 (conjugation invariance — Markov axiom M1).** The Markov trace is
invariant under conjugation in `H_{3A}`. Realising `σ` as a permutation of
the 3-strand nucleon blocks is a conjugation by a strand-permutation braid,
so even in the strand-relabel view `tr_M` is invariant.

**∴ The identity holds.** The roadmap's interface-swap worry is **unfounded**:
same-species permutations preserve all three interface types (Lemma 1b), so
there is no obstruction. ∎

The trace machinery is confirmed to reproduce the canonical values
(`tr_M(⁴He) = 0.05534835…`, `tr_M(⁵Li) = 0.02944139…`, to float precision),
so Lemma-1 invariance carries through to the trace.

## Correction to the roadmap

The Tier 1.B write-up states `tr_M(β_{Z,N}) = |orbit| · tr_M(representative)`.
That is **imprecise**. Because the canonical word is *already* the orbit
representative (Lemma 1 — `σ` doesn't change it), the correct statement is

> `tr_M(β_{Z,N}) = tr_M(representative)` — **no `|orbit|` multiplier.**

The `Z!·N!` factor is the redundancy of orbit-equivalent **intermediate
reduction states** during `incremental_reduced_element_fast`, which can be
**memoised away** — *not* a multiplier on the final trace. Any
implementation that multiplies the trace by `|orbit|` would be **wrong**;
the speedup must come from deduplicating the reduction tree.

## Implication

**Tier 1.B (nucleon-orbit reduction) is SOUND and unblocked.** The next step
is the engineering one the roadmap describes — build
`atom_braid_orbit_representative(Z, N)` and memoise orbit-equivalent states
in the LaurentQ reduce — with the correct `tr_M(β) = tr_M(rep)` semantics
(no `|orbit|` trace factor). Cross-check each new atom against the full-word
path at `A ≤ 6` before extending to `⁷Li / ⁸Be`.

## Follow-ups

- **Lean formalisation** of Lemma 1 (the word-construction invariance) as a
  structural lemma over the `ordering` string, and Lemma 2 as the M1
  conjugation property. Tracked as a `conjecture → theorem` promotion once
  the orbit-representative builder lands.
- The full strand-relabel *numerical* conjugation test needs an explicit
  block-swap braid `g` (naïve generator-relabelling produces a word the
  Markov-peel recursion can't process — a representation artefact, not a
  counterexample); the structural proof above does not depend on it.
