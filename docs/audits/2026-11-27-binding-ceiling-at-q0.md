# The merge ceiling at q₀, and reading 3 as a merge cap

**Date** 2026-11-27 · **Brief** C2 (compute-accuracy epic `qou-myts`), part 2 · **Beans** `qou-brng`, `qou-ales`
**Part 1** `docs/audits/2026-11-27-classical-log-binding-cycle-count.md` (PR #9467, merged)
**Lean** [`QOU/MassTheory/ClassicalReading3MergeBound.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/ClassicalReading3MergeBound.lean): sorry-free, lean-direct exit 0 (`-DautoImplicit=false -s 65536`), `#print axioms` = `[propext, Classical.choice, Quot.sound]`
**Probe** [`computations/probes/binding_ceiling_q0/`](../../computations/probes/binding_ceiling_q0/): mpmath 40 dps, convention D, proton pin, no float arithmetic. A = 2: 4/4 checks, 92 s. A = 3: 3/3 checks, 508 s.
**Scope** (a) for every numerical statement; the Lean statement is exact. Nothing fitted, selected, or wired. AME is not read by the probe.

## 0. Result in one paragraph

Part 1 left open whether the classical ceiling `−ln r ≤ ln 2·(n − 1)` survives the deformation to
`q₀`. On every γγ bond word measured it does, with a wide margin: the largest `−ln r` is 2.56 merge
units on six strands (ceiling 5) and 2.47 on nine (ceiling 8). The sharper finding is that reading 3
itself caps the merge count at small `A`. On six strands no passing word merges more than two
components, and that cap is a theorem at `q = 1` (`six_strands_three_cycles` plus parity). On nine
strands every passing word again merges exactly two, although 120 four-merge words pass reading 3
classically: at `q₀` all 120 fail. **The cap is not 2 for every `A`.** At `A = 4` (12 strands) every
word bonding all three junctions merges at least 4, and some pass: `V2V3V4V8` passes reading 3 at
`q₀` with `−ln r = 2.8101`, 4.05 merge units against its classical 4 (§7, run in progress).

## 1. Population and method

Free word: one γγ nucleon `V³` per three strands, `V(s) = σ_s σ_{s+1}⁻¹` (the chiral vertex of the
ruled photon). Bond words: concatenations of `V(0) … V(n−3)` that bond every junction (contain
`V(3j−2)` or `V(3j−1)` for each junction `j`).

| A | strands | lengths | bond words |
|---|---|---|---|
| 2 | 6 | 1–6 | 5334 |
| 3 | 9 | 1–4 | 1360 |

Reading 3 (Frobenius positivity of `E_{n→m}(W)` on every two-row block, every level `m`) is evaluated
with the corpus seminormal helpers (`../h2_one_rule`, `../h2_gg_atom`). The trace of each passing word
is recomputed with an independent Schur–Weyl trace on `(ℂ²)^{⊗n}` (R-matrix with `σ − σ⁻¹ = h`,
quantum-trace weight `diag(q, q⁻¹)`, normalised by `[2]ⁿ`). Merges are `c(σ_free) − c(σ_atom)` from
the underlying permutation, exact.

Checks: K0 the free word passes and the two traces agree; K1 the two traces agree on every passing word
(below 1e-25); K2 (A = 2) the run reproduces the corpus Phase A count of PR #9426, **408 of 5334
passing, 14 pure-junction**; K3 every passing ratio is positive.

## 2. Results

| A | merges | words | pass reading 3 at q₀ | pass classically (q = 1, all levels) | `−ln r(q₀)` over passing | classical `ln 2·m` |
|---|---|---|---|---|---|---|
| 2 | 0 | 46 | 46 | 46 | −0.0352 … +0.0059 | 0 |
| 2 | 2 | 1954 | 362 | 683 | 0.7895 … 1.7720 | 1.3863 |
| 2 | 4 | 3334 | **0** | **0** | — | 2.7726 |
| 3 | 2 | 71 | 28 | 27 | 1.0554 … 1.7097 | 1.3863 |
| 3 | 4 | 767 | **0** | **120** | — | 2.7726 |
| 3 | 6 | 498 | 0 | 0 | — | 4.1589 |
| 3 | 8 | 24 | 0 | 0 | — | 5.5452 |

Ceiling `ln 2·(n−1)`: 3.4657 (A = 2), 5.5452 (A = 3). No passing word comes near it.

The `q₀` and `q = 1` pass sets are not nested: 4 words pass at `q₀` and fail classically on six
strands (for example `V1V2V2V1V2V2`, the smallest `−ln r` among two-merge words), and 2 on nine.

The "classically" column uses the classical form of reading 3. At `q = 1`, `E_{n→m}` sends a
permutation to a positive multiple of its restriction to `{1, …, m}` (later points deleted from their
cycles). The two-row characters of a permutation are `χ_{(m−k,k)} = a_k − a_{k−1}`, with `a_k` the
number of invariant `k`-subsets (Young's rule; [sagan2001] Thm 2.11.2). Scratch script, not committed:
an exhaustive check over `S_n`, `n ≤ 9`.

## 3. The Lean theorem

`ClassicalReading3MergeBound.succ_le_two_pow_of_mono`: if a permutation has `c` cycles, and
`a_0 ≤ a_1 ≤ … ≤ a_{⌊n/2⌋}` (top-level classical reading 3), then `n + 1 ≤ 2^c`. The proof:

1. By complementation, `a_k = a_{n−k}`.
2. So every `a_k ≥ 1` for `k ≤ n`.
3. Distinct sums come from distinct sets of cycles, which gives `n + 1` distinct subsets among `2^c`.

Consequence: merges `≤ n − ⌈log₂(n+1)⌉`, against `n − 1` without reading 3. At `n = 6` this gives
`c ≥ 3` (`six_strands_three_cycles`), so with the parity lemma of part 1 the bond merges at most 2,
which is the A = 2 row above. The bond is even because every pure-junction bond is an even permutation.

The bound is sharp for every `n` (proved, `ClassicalReading3MergeBound.max_merges_eq`): the positive cycle
lengths `n + 1 − 2^d, 2^(d−1), …, 2, 1` with `2^d ≤ n < 2^(d+1)` satisfy the monotonicity hypothesis, which
matches the computation for `n ≤ 30`. The all-levels condition has the same maximum for every `n`
(`exists_allLevels_clog` with `clog_le_of_allLevels`; the binary layout passes at every level `m ≤ n`),
which matches the computation for `n ≤ 9`, so the extra levels do not tighten it classically. The
restriction to level `m` is modelled on cycle labels there, not derived from `E_{n→m}`. Exhaustive count of passing permutations by merges at `n = 9`:
`{0: 1, 1: 35, 2: 409, 3: 2457, 4: 7988, 5: 1368}`.

The bridge from characters to `a_k` is cited, not formalised. The theorem is stated on cycle-length
data. No empirical number appears in it.

## 4. What this changes

- **Open item 1 of part 1 is answered for the measured population.** The deformation never takes a
  γγ-admissible word above the classical ceiling. The largest excess over the word's own classical
  count is +0.386 (A = 2, `V1V2V1V3V2V2`, 1.772 against 1.386).
- **Classically, reading 3 costs only a logarithm**, `⌈log₂(n+1)⌉` cycles. The per-nucleon bound stays
  `E₀ ln 8` asymptotically. Classical reading 3 does not by itself make binding non-extensive.
- **At q₀ the measured cap is 2 merges at A = 2 and A = 3**, stronger than the classical cap at
  A = 3, which allows 4. **It does not stay at 2**: at A = 4 a passing word merges 4 (§7). So this
  bond class is not shown to be non-extensive, and the count of merges available per junction is the
  live question.

The A = 3 population stops at length 4, and the caps are measured, not proved.

## 5. Scorecard (not a derivation, not a selection)

Tower `E₀ = 4.2274834` MeV. The merge unit is `E₀ ln 2 = 2.930268` MeV.

- At A = 2, passing words give `B` in two bands. The non-merging band runs from −0.149 to +0.025 MeV.
  The two-merge band runs from 3.337 to 7.491 MeV. The interval between them is empty. AME ²H
  (2.224566 MeV) lies in that empty interval, so no γγ bond in this population reproduces it. The
  corpus run reported the same ("no passing word within 5 % of AME").
- At A = 3, the passing range is 4.461 to 7.228 MeV, against AME ³H 8.481796 MeV. The shortest
  two-junction bonds (`V2V3V4` and its cyclic shifts) give 5.906 MeV. The shortest merging A = 2
  bond (`V2V3`) gives 5.826 MeV. These two values are nearly equal because both bonds merge 2.

## 6. Open, with options

1. **How do the admissible merges grow with A?** A = 2, 3 give 2; A = 4 gives at least 4 (§7).
   Finish the A = 4 population, then find the invariant that bounds the q₀ merges per junction.
2. **Bond selection** (owner question). This is restated, with the data above, on the decision card in
   the thread. The A = 4 result weakens the case for deferring it. "Cheapest bond" gives ²H −99.7 %. "Cheapest bond that merges" gives `V2V3`: 5.826 MeV
   (+162 %) for ²H and 5.906 MeV for the A = 3 analogue. Choosing the second because it binds would
   be fitting unless the merge requirement is derived independently.
3. **Three-body permutations** (part 1 item 3). Unchanged.

## 7. A = 4 (12 strands), in progress

Producer `binding_ceiling_q0_a4_probe.py`: 1392 words of length 3–4 that bond all three junctions,
reading 3 at `q₀` with the same corpus helpers (about 19 s per word). Classically every one merges at
least 4 (length 3: all merge 6; length 4: 48 merge 4, 1008 merge 6, 288 merge 8), and 96 pass reading 3
at `q = 1`. Those 96 run first. The free word passes, `tr = 0.99426104770`.

First passing words: `V2V3V4V8` and `V2V3V8V4`, merges 4. For `V2V3V4V8`, `r = 0.0602007318`,
`−ln r = 2.8100708`, against `ln 2·4 = 2.7725887` classically, far below the ceiling `11 ln 2 = 7.62`.
At tower `E₀` that is 11.88 MeV (scorecard only). The word is an A = 3 two-junction bond (`V2V3V4`) plus
a single vertex on the third junction, and it merges 2 + 2. This section is replaced by the full table
when the run finishes.
