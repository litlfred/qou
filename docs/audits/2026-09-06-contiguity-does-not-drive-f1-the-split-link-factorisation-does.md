# Contiguity does **not** drive `f₁/f₀` — I was wrong in #6910, and the cause is the corpus's own split-link multiplicativity

**Corrects my own merged result.**
[#6910](https://github.com/litlfred/qou/pull/6910) (`ef33f1c6f8`,
[`2026-09-06-contiguity-drives-f1-but-it-saturates.md`](2026-09-06-contiguity-drives-f1-but-it-saturates.md))
is titled *"Contiguity does drive `f₁/f₀` — but it saturates at ⅔"*. The
saturation half was the right instinct; the driving half is **refuted**, and the
⅔ ceiling is an artifact of the measure rather than a threshold in the object.
Beans `qou-brng` / `qou-pdg9` / `qou-hu1f`.

## What I asserted, what is actually true, and how the new figure was measured

**Asserted (#6910, merged):** along a greedy contiguity-increasing walk from the
Borromean word, `f₁/f₀` rose `1/2 → 8 → 17 → 37/2 → 37/2` at contiguities
`0.1905 → 0.3810 → 0.5714 → 0.6667 → 0.7619`, and *"contiguity drives `f₁/f₀`"*
up to a ceiling reached at ⅔.

**Actually true:** those five numbers are correct and are not retracted. What is
wrong is the causal reading. Two measurements, either one sufficient:

1. **A word at contiguity 0.238 and a word at contiguity 0.857 carry the
   *same* value.** Twelve re-orderings of the `pn` atom word that permute the
   two nucleons into each other while preserving each nucleon's own internal
   letter order give `f₁/f₀ = 37/2` **12 out of 12**, at contiguities spanning
   `0.2381 … 0.6190`, against the canonical grouped word's `0.8571`. If
   contiguity drove the value, 0.238 could not produce the ceiling value.

2. **At *fixed* contiguity the value spreads across most of its whole range.**
   Random orderings binned by contiguity, `pn` and `pp`, `n = 6`, `P = 3`, exact
   `Fraction`, 6 words per bin:

   ```
   pn  (total range of the sample  -2.5 .. 18.5)      pp  (range 0 .. 21)
     bin    n     min     max  spread                  bin    n     min     max  spread
     0.0    6    -2.5     9.5    12.0                  0.0    6     0.0    10.5    10.5
     0.1    6     0.5     6.5     6.0                  0.1    6     4.5    12.0     7.5
     0.2    6     2.0    15.5    13.5                  0.2    6     6.0    16.5    10.5
     0.3    6     5.0    18.5    13.5                  0.3    6     3.0    15.0    12.0
     0.4    6     6.5    18.5    12.0                  0.4    6     3.0    15.0    12.0
     0.5    6     2.0    15.5    13.5                  0.5    6    10.5    18.0     7.5
     0.6    6     8.0    18.5    10.5                  0.6    6    13.5    21.0     7.5
     0.7    6    14.0    18.5     4.5                  0.7    6    16.5    21.0     4.5
     0.8    2    12.5    14.0     1.5                  0.8    6    13.5    21.0     7.5
   ```

   The pre-declared discriminator was the **spread at contiguity ≥ 0.6**: a real
   threshold predicts near-zero spread above it, an artifact predicts
   substantial spread. Measured **10.5** (`pn`) and **7.5** (`pp`), against total
   sample ranges of 21.0 and 21.0. Both nuclei return the artifact verdict, and
   `pp` still spreads by 7.5 in its *highest* bin.

**Measured this session** by
[`computations/probes/word_order_commutation_and_additivity_probe.py`](../../computations/probes/word_order_commutation_and_additivity_probe.py)
(4/4, exact `Fraction`, `pn`, `n = 6`, `P = 3`, `include_inter=False`) plus a
binned survey whose numbers are the table above. Nothing was carried from a
prior session.

## Why — and the mechanism was already derived in this corpus

In the `pn` atom word the proton occupies generators `{0,1}` and the neutron
`{3,4}`. Every cross pair has `|i−j| ≥ 2`, so the two nucleons act on **disjoint
strand sets**, and
[`markov-axioms-primitive.md`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md)
already derives from the Markov axioms that

$$\mathrm{tr}_M(K_1 \sqcup K_2) = \mathrm{tr}_M(K_1)\cdot \mathrm{tr}_M(K_2),$$

while
[`subset-cumulant-recursion.md`](../../content/quantum-observable-universe/mass-theory/subset-cumulant-recursion.md)
already names the consequence — multiplicativity of `tr_M` on split links *"turns
into additivity of `L` on disjoint bonded parts"*.

`f₁/f₀` is a logarithmic derivative, so it is **additive** over that
factorisation. Measured exactly, 6/6 trials:

    v(P*,N*) − v(P0,N0)  ==  [v(P*,N0) − v(P0,N0)] + [v(P0,N*) − v(P0,N0)]

and the canonical split is `21/2 + 8 = 37/2`, reproducing the per-letter counts
(proton 21, neutron 16) that `c1_leading_coefficient_derived_probe.py` carries.

**So this is a CONFIRMATION of derived corpus content, not a discovery — and it
is the THIRD independent statement of the same fact.** The corpus-grep found two
predecessors before this document was written:

1. **Derived** from the Markov axioms in `markov-axioms-primitive.md` (above).
2. **Measured numerically** by
   [`computations/qbeta/qbeta_disjoint_support_factorisation_probe.py`](../../computations/qbeta/qbeta_disjoint_support_factorisation_probe.py)
   (7/7, 2026-09-04, bean `qou-ib3g`): *"`tr_M` factorises over disjoint
   non-adjacent generator blocks EXACTLY (rel. diff 0.0 at 40 dps), for
   non-trivial words with generators repeated inside each block"* — which is
   exactly T2's premise, established there to discharge the colour-tube
   assumption in the `B_sym` extensive-term work.
3. **This document**, at the log-derivative level in exact `Fraction`.

Per AGENTS.md §"Parallel exploration", re-measuring an open result from a
different direction is permitted and the two confirmations strengthen each other
— but it must be **cited, not passed off as new**, so it is cited. What is
genuinely additional here is narrow and should be read as narrow: the prior probe
established factorisation of `tr_M` at 40 dps; this establishes the induced
**additivity of the log-derivative** in exact rational arithmetic, and puts it to
a use the prior probe was not put to — refuting the contiguity reading.

Beyond that the confirmation earns its keep twice: it is a correctness check on
the word-level entry point, and it *derives* why the per-letter formula is
additive in `Z` and `N` rather than leaving that as an empirical shape.

## 🛑 "Contiguity" means three different things in this corpus — check which one

The word is heavily overloaded here, and two of the three senses are unrelated to
this document:

| sense | where | what it means |
|---|---|---|
| **q-Bessel contiguous relations** | `prf:jackson-q-bessel-contiguity`, `QBesselContiguityRecurrence.lean`, beans `qkhc` / `c370` / `fwr11` / `z2bn` / `qou-avra` / `qou-qbes` / `cmiy` / `s013` / `qou-rdvo` | the classical basic-hypergeometric contiguous-parameter recurrence. **Nothing to do with braid words.** This is the majority of hits. |
| **strand-layout contiguity** | beans `qou-ib3g` / `qou-0c19`, `QOU/Hecke/LayoutConflict.lean` | whether a nucleon's three strands sit adjacent in the `3A` layout. Proved there that no ordering makes nucleon triples contiguous *and* the interface couplings single generators — max `A−1` of `3(A−1)`. |
| **letter-adjacency contiguity** | #6910 and this document | fraction of adjacent letter pairs sharing a generator index. |

The second and third are close cousins — both about adjacency in the braid word —
and are the ones most likely to be conflated. They are still different: the
layout sense is a property of the *strand assignment*, the letter sense a
property of the *word order given that assignment*. A grep for "contiguity" lands
mostly in the first sense, which is a different subject entirely.

## What went wrong in #6910, stated precisely

The greedy walk raised *global* contiguity, which mixes two things:

- **intra-nucleon order** — which each nucleon's own letters sit adjacent — and
  this genuinely moves the value;
- **inter-nucleon interleaving** — which the algebra cannot see at all.

A greedy walk from the Borromean word repairs the intra-nucleon orders early,
because that is where the cheapest contiguity gains are. After that it keeps
raising global contiguity by de-interleaving the nucleons, which buys nothing.
**That is the ⅔ plateau**: not a threshold in `f₁/f₀`, but the point at which
the walk switched from the variable that matters to the one that does not.

#6910's own scope section said *"correlation along one path is not causation"*
and *"the saturation is evidence against the simplest causal story"* — so the
body was hedged correctly. **The title was not**, and titles are what get
quoted. That is the transferable lesson here, and it is mine: a hedge in §Scope
does not neutralise a causal claim in the headline.

## The obvious repair does not work either

Replacing global contiguity with *intra-nucleon* contiguity is the natural fix.
It fails: three proton orders at intra-contiguity `0.400` give `f₁/f₀` for the
whole word of `31/2`, `8` and `14` — per-nucleon contributions `15/2`, `0` and
`6`, against the canonical `21/2`. And intra-contiguity `0.600` gives whole-word `11`, i.e. `φ = 3` —
*below* all three of the 0.400 cases. So intra-nucleon contiguity is **not monotone** in the value and does
not determine it either.

**What determines the per-nucleon contribution is an open combinatorial
question**, and it is now well-posed in a way it was not before: by additivity,
it is a function `φ` of an 11-letter word on two adjacent generators alone, with
`φ(canonical proton) = 21/2` and `φ(canonical neutron) = 8`. That is a much
smaller object than the 22-letter problem — a real narrowing, and the one
durable gain of this correction.

## What this contaminated, and what it does not

**Contaminated — one document, now carrying a correction banner:**
[`2026-09-06-contiguity-drives-f1-but-it-saturates.md`](2026-09-06-contiguity-drives-f1-but-it-saturates.md).
Its five walk numbers stand; its title and §"The refinement" are wrong.

**Checked and NOT contaminated.** The contiguity reading originated as
*interpretation offered in* #6905
([`2026-09-06-canonical-extremality-is-grouped-specific.md`](2026-09-06-canonical-extremality-is-grouped-specific.md)),
which labelled it as interpretation rather than measurement. #6905's own
*measurements* — grouped is a 1-swap local maximum, Borromean is not
(110/196 neighbours beat it) — are untouched by this and remain as recorded.
The `c₁` audit chain (#6538 / #6559 / #6607 / #6675) makes no contiguity claim.
Grepped `docs/`, `content/`, `computations/` and `.beans/` for `contiguit`.
Outside the two documents above there are twelve bean hits and several Lean /
content blocks, and **none of them carries this document's claim** — they are the
q-Bessel and strand-layout senses tabulated above. So the contaminated surface is
one document.

## Scope, and what is NOT established

- **Scope-(a).** One nucleus pair (`pn`, `pp`), `A = 2`, `n = 6`, one truncation
  `P = 3`, `include_inter=False`. Nothing here is a claim about the physics.
- **The bin table is a survey, not a law.** 6 words per bin, uniform shuffles.
  It establishes that spread at fixed contiguity is large; it does not measure a
  distribution.
- **The bin *minimum* appears to rise with contiguity, and that is NOT claimed
  as a finding.** It is non-monotone in both nuclei (`pn` 6.5 → 2.0 across
  0.4 → 0.5; `pp` 16.5 → 13.5 across 0.7 → 0.8), and a minimum over 6 samples is
  the least stable statistic available. A real bound would need a directed
  search for the minimising word at each contiguity, not a shuffle sample.
- **Additivity is measured on `pn` with `include_inter=False`.** The inter-nucleon
  terms are exactly the part that breaks the disjoint-strand premise, so nothing
  here says anything about them — and they are where the binding lives.
- **`φ` is not derived.** Its existence is; its form is open.

## An unrelated finding, recorded because getting this PR's own hygiene wrong surfaced it

`scripts/precommit-precision-warn.sh` — the **warn-only** `PreToolUse` hook —
runs `witness_raw_float64_audit.py --strict`, which **writes**
`computations/witness-raw-float64-audit.witness.json` via `WitnessBuilder`. So
any commit touching `computations/` silently dirties a contended, drain-only
ratchet witness, and the next `git add -A` commits it.

Isolated rather than assumed: after reverting four such witnesses this branch had
picked up, the raw-float64 one came back dirty on the very next commit with
`precision-gates.sh` not running.

`qou-v0t8` covers the *other* writer (`precision-gates.sh`) and is `completed` —
its 2026-08-30 guard fixes that script's banner. It names `precommit`, `hook` and
`WitnessBuilder` **zero times**, so this is a separate surface, tracked as
`qou-y8d0`. Three mitigations are named there and **none is applied**: a
warn-only hook writing a tracked file is the hook owner's call.
