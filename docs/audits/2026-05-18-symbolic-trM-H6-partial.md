# Symbolic Markov trace at H_6 — partial result + Ocneanu-fallback diagnosis

## Goal

Compute `tr_M(β_EW Δ_I^minimal)(q)` as a closed-form q-rational
expression at H_6 to test substrate-derivation hypotheses for the
staircase EW-residual conjecture (`conj:staircase-ew-residual`)
without relying on single-point matches at q = q_0 that the
q-derivative falsification test ruled out.

## Pipeline tested

`hecke_laurent_fast.incremental_reduced_element_fast` →
`markov_trace_canonical.tr_M_element` — the standard QOU pipeline
for symbolic Markov traces of arbitrary braid words.

## Diagnosis: when does the pipeline succeed?

* **LaurentQ reduction (H_6 level)**: succeeds. β_EW Δ_I^minimal
  (length 27, generators σ_1..σ_5) reduces to **52 unique terms**
  in 0.3 s, each with **σ_5 appearing at most once**. Hecke
  quadratic R1 + commutation R2 + Yang-Baxter R3 fully resolve
  σ_5 clusters.
* **Markov-axiom peel (H_6 → H_5)**: succeeds. 42 / 52 terms peel
  via the Markov axiom `tr_M(α σ_5 β) = z · tr_M(α β)` cleanly
  (single σ_5 occurrence per term).
* **H_5 intermediate is structurally clean.** One representative
  intermediate-coefficient (post-peel) is the palindromic Laurent
  polynomial in q:
  ```
  q^19 − 7q^17 + 24q^15 − 56q^13 + 103q^11 − 161q^9
  + 223q^7 − 281q^5 + 327q^3 − 353q
  + 353/q − 327/q^3 + 281/q^5 − 223/q^7 + 161/q^9
  − 103/q^11 + 56/q^13 − 24/q^15 + 7/q^17 − 1/q^19
  ```
  multiplied by `z`. Palindromic structure with integer coefficients
  — *prima facie* evidence the symbolic Markov trace HAS a clean
  q-rational closed form.
* **H_5 → H_4 step**: **fails for ~10 terms**. After Markov peel of
  σ_5, the H_5 sub-element has terms where σ_4 (the new top) appears
  ≥ 2 times in non-adjacent positions separated by σ_3 (which doesn't
  commute with σ_4). `reduce_laurent_rules` doesn't bring the σ_4's
  together via the braid relation σ_4 σ_3 σ_4 = σ_3 σ_4 σ_3.
* **Ocneanu fallback** is what `markov_trace_canonical.tr_M_element`
  falls back to here. The fallback path requires NUMERIC q, z, h
  (it computes ω-weighted seminormal character sums numerically) —
  blocking the symbolic q derivation.

## What "fixing the fallback" would require

The blocker is **braid-relation-driven canonicalisation** of words
with multiple occurrences of the same generator separated by
non-commuting partners. Specifically:

1. **Detect commutation closure**: for a word `w` containing σ_top
   at positions `i < j`, check whether the subword `w[i+1:j]`
   commutes with σ_top (all generators ≥ top+2 away). If yes,
   move σ_top together; apply Hecke quadratic.
2. **Apply braid relations to escape commutation barriers**:
   σ_top σ_{top−1} σ_top → σ_{top−1} σ_top σ_{top−1}. This trades
   one σ_top for the relation but shifts the obstruction one
   index lower.
3. **Iterate (1)–(2) until canonical form is reached**: at most
   `O(n)` braid-relation applications per word per σ_top pair.

This is a non-trivial algorithmic addition to `reduce_laurent_rules`
or a new dedicated function `bring_top_together(elem, top)`. The
existing pipeline punts to Ocneanu precisely because this
implementation is missing.

## Partial result + recommendation

* The H_6 → H_5 step ALREADY produces structurally-clean palindromic
  Laurent intermediates. Continuing symbolically through H_5 → H_4
  would likely produce similar clean structure — strong reason to
  invest in the braid-relation fix.
* For the immediate goal (testing whether `z`, `q^a`, or some other
  substrate scale is the structural EW reading), the current
  pipeline output at H_5 is enough to start: the palindromic
  coefficient above already reveals that the eigenvalue spectrum of
  the H_5 reduction has q ↔ q^(-1) symmetry, consistent with the
  bar-pair structure verified in `probe_staircase_ew_k3_block_decomposition.py`.

## Provenance

* Probe attempts: documented in this audit (run interactively, not
  committed as a probe script — the partial-success result is the
  diagnostic, not a reproducible artifact).
* Existing pipeline files:
  - `folio-assistant/computations/hecke_laurent_fast.py` —
    `incremental_reduced_element_fast`, `reduce_laurent_rules`
  - `folio-assistant/computations/markov_trace_canonical.py` —
    `tr_M_element` (with Ocneanu fallback)
  - `folio-assistant/computations/ocneanu_weights.py` —
    `canonical_markov_trace_via_ocneanu` (numeric-only)
* Related: `prop:markov-trace-recursive-reducer` (the structural
  proposition the pipeline implements).
