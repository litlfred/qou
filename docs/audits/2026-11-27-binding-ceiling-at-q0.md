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
itself caps the merge count. On six strands no passing word merges more than two components, and that
cap is a theorem at `q = 1` (`six_strands_three_cycles` plus parity). On nine strands every passing
word again merges exactly two, although 120 four-merge words pass reading 3 classically: at `q₀` all
120 fail. If this cap stays at 2 as `A` grows, γγ bonds of this kind cannot produce an extensive
binding term, and the bond-selection question of part 1 does not reach the extensive problem.

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

The bound is sharp for `n ≤ 30`: cycle lengths `1, 2, 4, …` attain it (computed, not proved). The
all-levels condition gives the same maximum for `n ≤ 9`, so the extra levels do not tighten it
classically. Exhaustive count of passing permutations by merges at `n = 9`:
`{0: 1, 1: 35, 2: 409, 3: 2457, 4: 7988, 5: 1368}`.

The bridge from characters to `a_k` is cited, not formalised. The theorem is stated on cycle-length
data. No empirical number appears in it.

## 4. What this changes

- **Open item 1 of part 1 is answered for the measured population.** The deformation never takes a
  γγ-admissible word above the classical ceiling. The largest excess over the word's own classical
  count is +0.386 (A = 2, `V1V2V1V3V2V2`, 1.772 against 1.386).
- **Classically, reading 3 costs only a logarithm**, `⌈log₂(n+1)⌉` cycles. The per-nucleon bound stays
  `E₀ ln 8` asymptotically. Classical reading 3 does not by itself make binding non-extensive.
- **At q₀ the measured cap is 2 merges at both A = 2 and A = 3.** This is stronger than the classical
  cap at A = 3, which allows 4. If it holds for all `A`, the γγ bond class of this kind binds every
  nucleus by about two merge units, about 5.9 MeV at tower `E₀`, independent of `A`. That is not
  extensive.

Two limits on the measurement. The A = 3 population stops at length 4. And the cap is measured, not
proved. The A-dependence of the cap is the first open item below.

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

1. **Is the q₀ merge cap 2 for every A?** Measure A = 4 (12 strands) on the shortest bond words that
   bond every junction. The TL-quotient engine of PR #9474 (`hecke_tl.py`, exact convention-D trace,
   Catalan(12) = 208k diagrams) makes this cheap. If the cap is 2, prove it at `q₀`, or find the
   invariant that forces it.
2. **Bond selection** (owner question). This is restated, with the data above, on the decision card in
   the thread. "Cheapest bond" gives ²H −99.7 %. "Cheapest bond that merges" gives `V2V3`: 5.826 MeV
   (+162 %) for ²H and 5.906 MeV for the A = 3 analogue. Choosing the second because it binds would
   be fitting unless the merge requirement is derived independently.
3. **Three-body permutations** (part 1 item 3). Unchanged.
