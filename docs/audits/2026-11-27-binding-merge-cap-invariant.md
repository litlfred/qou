# The q₀ merge cap at A = 3 is a length-4 truncation of the classical cap

**Date** 2026-11-27 · **PR** #9618 · **Brief** C2 front B (epic `qou-myts`) · **Bean** `qou-brng`
**Follows** [`2026-11-27-binding-ceiling-at-q0.md`](2026-11-27-binding-ceiling-at-q0.md) (§6 item 1). **Agrees with** front A, `docs/audits/2026-11-27-binding-three-body-perms.md` (PR #9587, open), which found nine length-5 four-merge passers independently.
**Lean** [`QOU/MassTheory/MergeComponentAdditivity.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/MergeComponentAdditivity.lean): sorry-free, lean-direct exit 0 (`-DautoImplicit=false -s 65536`), `#print axioms` = `[propext, Classical.choice, Quot.sound]`.
**Probes** [`computations/probes/binding_merge_cap/`](../../computations/probes/binding_merge_cap/): corpus seminormal helpers, convention D, proton pin, mpmath; no float arithmetic, no ratio, AME not read. Witness `binding-merge-cap-per-component.witness.json` (q0Anchor proton, 2/2 assertions).
**Gates** `scripts/precision-gates.sh --changed`: two reds, both from files this branch does not touch (`raw-float64`: `probes/light_nuclei_a2_a3/binding-scale-tl.witness.json`; `value-copy`: `probes/gg_ntower/gg_scalar_per_step_probe.py:96`).
**Scope** (a) for every numerical statement. Nothing fitted, selected, or wired.

## 0. Result

The question was why every four-merge bond word fails reading 3 at `q₀` at `A = 3` (120 pass
classically, 0 at `q₀`), while `V2V3V4V8` merges 4 and passes at `A = 4`.

**There is no `q₀`-specific merge cap of 2 at `A = 3`.** The earlier population stopped at length 4.
At length 5, **22 of 284** commutation classes of single-component four-merge words that pass reading
3 classically also pass at `q₀` (for example `V4V2V3V4V6`, smallest cell `+0.022`). Four merges is
the classical cap on nine strands (`n + 1 ≤ 2^c` gives `c ≥ 4`, and bond words are even, so at most
4), so at length 5 the `q₀` maximum equals the classical maximum.

**Why all 120 fail at length ≤ 4.** On nine strands, every permutation that passes classical
reading 3 and merges at least 4 has a two-row character equal to **zero** at the top level
(exhaustive over `S₉`; at merges 3 no admissible permutation has one). Four-merge words therefore sit
exactly on the classical boundary, and the deformation to `q₀` decides the sign of those zeros. At
length ≤ 4 it makes all of them negative: each of the 120 fails **only** on cells that are
classically 0. At length 5 it makes some positive (22 classes pass; 239 fail only on zero cells; 23
fail also on a classically positive cell).

**The hypothesis "about 2 merges per bonded junction group / per connected component of the bond
graph" is falsified in both readings.**
- Nucleon bond graph: connected for every population word at `A = 4`, so it predicts cap 2;
  `V2V3V4V8` merges 4 and passes.
- Support components (vertices `V(s)` joined when their strands `{s, s+1, s+2}` overlap), the version
  that explains `V2V3V4V8` (two components, `V2V3V4` and `V8`, 2 merges each): it held on every word of
  length ≤ 4 at `A = 2, 3, 4` and on all 126 classically admissible `A = 4` length-5 classes tested,
  but the 22 `A = 3` length-5 passers are single components merging 4.

## 1. What is proved (Lean)

`MergeComponentAdditivity.lean`, generic finite type, no `q`, no empirical number:
`merges σ = |supp σ| − #(non-trivial cycles)` (= `n − #orbits`); merges add over disjoint permutations
(`merges_mul_of_disjoint`) and over pairwise disjoint products (`merges_prod_of_pairwise`); a cap `k`
per factor gives `k · #factors` (`merges_prod_le`); disjoint strand sets give disjoint permutations
(`disjoint_of_support_subset`); one factor on `s` points merges at most `s − 1`.

This is the bookkeeping that lets a bond word's merges be read component by component. It does not
prove any cap at `q₀`.

**Not formalised:** the `S₉` top-level-zero fact of §0. It depends only on the cycle type, and
top-level monotonicity alone suffices: the cycle types of nine points with at most five cycles that
pass top-level classical reading 3 are `4+2+2+1`, `4+2+1+1+1`, `3+3+1+1+1`, `3+2+2+1+1`,
`2+2+2+2+1`, and each has some `a_k = a_{k+1}`. A `decide` over `Nat.Partition 9` does not reduce in
the kernel; a proof needs an explicit enumeration of those partitions. Left as a finite computation
(witness field `classical_exhaustive_top_level_zero`, `S₄ … S₉`).

## 2. Data

From `binding-merge-cap-per-component.witness.json`. "max comp" = largest merge count of one support
component. Length-5 rows are one representative per commutation class (`V(s)V(t) = V(t)V(s)` for
`|s − t| ≥ 3`, an equality of Hecke elements), classically admissible words only.

| source | words | `q₀` pass | classical pass | `q₀` passers with max comp > 2 |
|---|---|---|---|---|
| A = 2, length ≤ 6 (census) | 5334 | 408 | 729 | 0 |
| A = 3, length ≤ 4 (census) | 1360 | 28 | 147 | 0 |
| A = 3, length 5, one component, merges 4 | 284 | **22** | 284 | **22** |
| A = 3, length 5, one component, merges 6 | 0 | — | — | none classically admissible |
| A = 4, length ≤ 4 (sweep checkpoint, 302 of 1392 rows, all 96 classical passers in) | 302 | 12 | 96 | 0 |
| A = 4, length 5, one component, merges 4 | 34 | 0 | 34 | 0 |
| A = 4, length 5, two components, merges 6 | 84 | 0 | 84 | 0 |
| A = 4, length 5, two components, merges 8 | 8 | 0 | 8 | 0 |

The `A = 4` length ≤ 4 rows are another process's run (`binding_ceiling_q0_a4_probe.py`), read
only. Its 12 passers are the commutation and rotation variants of `V2V3V4 · V8`.

Other measured facts:

- `q₀` pass is **not a function of the permutation.** At `A = 2` the same permutation passes for some
  words and fails for others (`(0 2)(4 5)`: 15 and 15). No invariant of the classical permutation can
  characterise it.
- Placement matters at fixed merges. `A = 3`: `V1V2 · V5V6` (two components, 2 + 2) passes classically
  and fails at `q₀`. `A = 4`: `V2V3V4 · V7` fails, `V2V3V4 · V8` passes (same cycle type).
- The marginal pattern is cleanest at `A = 3`, length ≤ 4 (120/120 fail only on classical zeros). It
  is not universal: at `A = 4` length 5, 12 of 126 failures include a classically positive cell.

## 3. What this changes

- **The "cap 2 at A = 2 and A = 3" in the binding-ceiling audit is a length artefact at `A = 3`.** At
  `A = 2` it is the classical cap (six strands). At `A = 3` the `q₀` maximum through length 5 is the
  classical maximum, 4. Front A reached the same conclusion from nine words.
- The mechanism to keep: **at the classical merge cap the two-row characters have zeros, and `q₀`
  decides their sign word by word.** Below the cap (≤ 3 merges at nine strands) admissible
  permutations have no top-level zero, so `q₀` has slack there.
- No merge-count invariant was found that bounds `q₀` merges below the classical cap. On this data
  the binding question is back to the classical bound `n − ⌈log₂(n+1)⌉`, made even, plus a
  word-dependent sign decision at the boundary.

## 4. Open, with options

1. **Which boundary words survive at `q₀`.** 22 of 284 at `A = 3` length 5. Data in
   `merge-cap-A3-L5-m4-c1.jsonl` (failing cells recorded); not analysed. A candidate route: the
   first-order term in `q − 1` of each classically zero cell.
2. **`A = 4` beyond length 5.** Only the 34 length-5 single-component four-merge classes were tested
   (all fail); single-component six- and eight-merge words are not classically admissible at length 5.
3. **Formalise the `S₉` top-level-zero fact** by an explicit partition enumeration (§1).

## 5. Reproduce

```
export PYTHONPATH=computations:tools/qou-substrate/python
python3 -u computations/probes/binding_merge_cap/merge_cap_census.py 6 2            # 80 s
python3 -u computations/probes/binding_merge_cap/merge_cap_census.py 4 3            # 10 min
python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 4 1 3  # A = 3, 284 classes, 2 min
python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 6 1 3  # A = 3, 0 classes
python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 4 1    # A = 4, 34 classes, 17 min
python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 6 2    # A = 4, 84 classes
python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 8 2    # A = 4, 8 classes
MERGE_CAP_A4_CKPT=<binding-ceiling-q0-A4-L4.checkpoint.jsonl> \
  python3 computations/probes/binding_merge_cap/merge_cap_summary.py
```
