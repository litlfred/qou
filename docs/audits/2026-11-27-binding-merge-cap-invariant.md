# The q₀ merge cap counts merges per support component

**Date** 2026-11-27 · **Brief** C2 front B (epic `qou-myts`) · **Bean** `qou-brng`
**Follows** [`2026-11-27-binding-ceiling-at-q0.md`](2026-11-27-binding-ceiling-at-q0.md) (§6 open item 1)
**Lean** [`QOU/MassTheory/MergeComponentAdditivity.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/MergeComponentAdditivity.lean): sorry-free, lean-direct exit 0 (`-DautoImplicit=false -s 65536`), `#print axioms` = `[propext, Classical.choice, Quot.sound]`
**Probes** [`computations/probes/binding_merge_cap/`](../../computations/probes/binding_merge_cap/): corpus seminormal helpers, convention D, proton pin, mpmath; no float arithmetic, no ratio, AME not read.
**Scope** (a) for every numerical statement. The Lean statement is exact and contains no `q₀` and no empirical number. Nothing fitted, selected, or wired.

## 0. Result

The question: why does every four-merge bond word fail reading 3 at `q₀` at `A = 3` (120 pass
classically, 0 at `q₀`), while `V2V3V4V8` merges 4 and passes at `A = 4`?

**Measured invariant (H).** Split a bond word into *support components*: the vertex `V(s)` occupies
strands `s, s+1, s+2`, and two vertices are in the same component when their strand sets overlap.
On every word measured, a word that passes reading 3 at `q₀` has **every support component merging
at most 2**. Merges add over components (proved), so the total is at most `2 × (number of
components)`.

- `A = 3`, length ≤ 4: every word bonds both junctions, so a four-merge word has either one
  component merging 4 (96 classically admissible, all fail at `q₀`), or two components merging 2
  each (24 classically admissible, all fail at `q₀`). (H) explains the first 96; it does not explain
  the other 24 (§3).
- `A = 4`: `V2V3V4V8` has two components, `V2V3V4` (strands 2–6) and `V8` (strands 8–10), each
  merging 2. (H) allows it.
- Test of (H) where it makes a prediction: at `A = 4`, length 5, all **34/34** commutation classes
  of single-component four-merge words that pass reading 3 classically fail at `q₀`. RESULTS_62_82

The hypothesis as first stated, "about 2 merges per bonded junction group / per connected component
of the **nucleon** bond graph", is **falsified at `A = 4`**: every population word bonds all three
junctions, so that graph is connected and the hypothesis predicts a cap of 2, while `V2V3V4V8`
passes with 4. The support-component version is what survives. On every passing word measured, each
support component contains a junction vertex, so "per bonded junction group" in the sense of
"per support component" is the same statement on this data.

## 1. What is proved (Lean)

`MergeComponentAdditivity.lean`, generic over a finite type, no `q`:

| theorem | content |
|---|---|
| `merges` | `|supp σ| − #(non-trivial cycles)` = `n − #orbits` |
| `merges_mul_of_disjoint` | disjoint permutations: merges add |
| `merges_prod_of_pairwise` | pairwise disjoint product: merges are the sum |
| `merges_prod_le` | a cap `k` per factor gives `k · #factors` |
| `disjoint_of_support_subset` | supports in disjoint strand sets ⇒ disjoint permutations |
| `merges_le_card_support_sub_one` | one factor on `s` points merges at most `s − 1` |

This is the reduction that turns a per-component cap into the global bound
`merges ≤ 2 · components`. **The per-component cap itself (`≤ 2` at `q₀`) is not proved**; it is
measured. It is not a classical fact: at `q = 1` reading 3 admits 96 single-component four-merge
words at `A = 3` and the 34 classes above at `A = 4`.

## 2. Data

Tallies from `binding-merge-cap-per-component.witness.json` (producer `merge_cap_summary.py`).
"max comp" = largest merge count of a single support component.

| source | words | `q₀` pass | classical pass | `q₀` passers with max comp > 2 | classical passers with max comp > 2 (all fail at `q₀`) |
|---|---|---|---|---|---|
| A = 2, length ≤ 6 (census) | 5334 | 408 | 729 | 0 | 0 |
| A = 3, length ≤ 4 (census) | 1360 | 28 | 147 | 0 | 96 |
| A = 4, length ≤ 4 (sweep checkpoint, rows at run time) | ROWS_A4 | PASS_A4 | — | 0 | CL_A4 |
| A = 4, length 5, one component, merges 4 (classes) | 34 | 0 | 34 | 0 | 34 |
RESULTS_TABLE

At `A = 2` the classical cap already gives 2 (the six-strand theorem of part 2), so `A = 2` does not
test (H). It does show that `q₀` pass is **not a function of the permutation**: for many single
permutations some words realising it pass and others fail (for example `(0 2)(4 5)`: 15 pass, 15
fail). So no invariant of the classical permutation alone can characterise `q₀` pass; (H) is a
bound, not a characterisation.

## 3. Mechanism at A = 3, and what (H) does not explain

At `A = 3` all 120 classically admissible four-merge words fail at `q₀` **only on cells where the
classical two-row character is exactly 0** (Young's rule value `a_k − a_{k−1} = 0` of the restriction
to level `m`). They are on the boundary of classical reading 3, and the deformation tips those zeros
negative. Most failing cells are at the top level, `(5,4)` and `(6,3)` on 9 strands. This marginal
pattern is not general: at `A = 4` some single-component failures include a cell that is
classically positive.

The 24 two-component four-merge words at `A = 3` are commutation variants of `{V1V2 or V2V1} ×
{V5V6 or V6V5}` (components on strands 1–4 and 5–8). Each component merges 2, so (H) allows them, yet
they fail at `q₀` (cells `(4,1)` at level 5 and `(6,3)`, `(8,1)` at level 9, magnitudes 0.01–0.13).
Compare `V1V2` alone at `A = 2`, which also fails at level 5, while `V2V3` passes. So whether a
two-merge component survives depends on where it sits relative to the nucleon boundaries; (H) is
necessary on the data, not sufficient. The same holds at `A = 4`: `V2V3V4V7` (third component on
strands 7–9) fails while `V2V3V4V8` (strands 8–10) passes.

## 4. What this changes

- The `A = 3` result is explained in part: the 96 single-component four-merge words fail because
  (H) caps a component at 2. The 24 two-component ones fail for a placement reason not captured by
  any merge count.
- **Binding is not capped at 2 merges per nucleus.** Under (H) the cap grows with the number of
  support components a bond word can hold, which grows with `A` (one component needs at least one
  vertex, three strands). So (H) does not make binding non-extensive; it says each extra unit of
  merge needs an extra, disjoint, admissible component.
- Under (H), the classical-ceiling per-nucleon bound `E₀ ln 8` of part 1 is replaced, on the
  measured population, by about `2 ln 2` per support component; how many admissible components fit
  per nucleon is the next question.

## 5. Open, with options

1. **Prove the per-component cap at `q₀`.** Not attempted in Lean: it needs the seminormal
   characters of 9- and 12-strand words as functions of `q`. A route: show that a single connected
   component merging ≥ 4 has a two-row cell that is classically 0 with negative `q`-derivative. The
   `A = 4` cell found classically positive argues against a purely marginal proof.
2. **The placement rule** (which two-merge components survive: `V2V3`, `V2V3V4`, `V8` yes; `V1V2`,
   `V7` no). Data in the censuses; not analysed here.
3. **(H) beyond length 5 at `A = 4` and at `A ≥ 5`.** Untested.

## 6. Reproduce

```
PYTHONPATH=computations:tools/qou-substrate/python python3 -u computations/probes/binding_merge_cap/merge_cap_census.py 6 2   # 80 s
PYTHONPATH=computations:tools/qou-substrate/python python3 -u computations/probes/binding_merge_cap/merge_cap_census.py 4 3   # 10 min
PYTHONPATH=computations:tools/qou-substrate/python python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 4 1   # 34 classes, 17 min
PYTHONPATH=computations:tools/qou-substrate/python python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 6 2
PYTHONPATH=computations:tools/qou-substrate/python python3 -u computations/probes/binding_merge_cap/merge_cap_a4_targeted.py 5 8 2
MERGE_CAP_A4_CKPT=<path to binding-ceiling-q0-A4-L4.checkpoint.jsonl> \
PYTHONPATH=computations:tools/qou-substrate/python python3 computations/probes/binding_merge_cap/merge_cap_summary.py
```
