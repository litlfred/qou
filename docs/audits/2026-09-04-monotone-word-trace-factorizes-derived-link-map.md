# Monotone words factorize — the derived nucleus→link map is torus connected sums, and the same ordering hypothesis kills the n = 4 cross term

**Date:** 2026-09-04 · **Beans:** `qou-kru4` (closed by this), `qou-5vhf` (completed; this is the
follow-on it pointed at), `qou-ls86`, `qou-brng` (frontier) · **Arc:** many-body collective term /
carrier question · **Scope:** formalize-first, sorry-free Lean + synthesis of already-measured
facts. **Nothing is wired, nothing is fitted, no production number moves.**

## The question

`qou-kru4` (2026-09-03) proved that the Markov trace is **not** bond-multiplicative in general:
at `n = 4` the interleaved word `g₀ g₁ g₀ g₂ g₁` differs from the sequential word `g₀² g₁² g₂` by
the exact cross term `z (z² − h z − 1)`, with the sign the collective term `R > 0` needs. It left
one thing unproved and one thing unsaid:

- **Unproved:** that the production atom word is in fact exempt — that a *monotone* word
  (ascending, one run per generator) always factorizes. The production trace's per-bond product
  implementation assumes this; the corpus had it only for bare generator words
  (`MarkovTrace.tr_genWord`, `z^k`), not for the superposition letters `c·σ + d·1` the production
  word is built from, nor for runs.
- **Unsaid:** that this is the *same* hypothesis under which the 2026-08-25 audit showed every
  production closure is a connected sum of `(2, k)` torus links with `Vol = 0`.

`qou-5vhf` (completed 2026-09-03) had boxed "which word class a nucleus is" as **the** carrier
blocker. This note closes the algebraic half of that box and states what it means.

## Result — monotone ⇒ factorizes (Lean, sorry-free)

`content/quantum-observable-universe/lean/QOU/MathlibExt/MonotoneWordTraceFactorizes.lean`
(namespace `QOU.MathlibExt.MonotoneWordFactorizes`), over the corpus's `MarkovTrace` structure
(T1–T3, generic `CommRing R`, `Ring A`):

| declaration | statement |
|---|---|
| `tr_mul_stabWord_prod` | letters `s m ∈ H (m+1)` stabilising `H m` by `c m` ⇒ `tr(a · s n ⋯ s (n+k−1)) = (∏ c) · tr a` |
| `stab_const_eq_tr` | the stabilising constant *is* the letter's trace, `c m = tr (s m)` |
| **`tr_stabWord_eq_prod_tr`** | **the trace of a monotone word is the product of its letter traces** |
| `tr_mul_affine`, `tr_affine`, `affine_mem` | the affine letter `a•1 + b•g m` stabilises with `a + b z` |
| **`tr_affineWord`** | **the production word class**: ascending affine letters ⇒ `∏ (a + b z)` |
| `affine_mul_affine` | under the Hecke quadratic the affine letters at one level close under product — a *run* of superposition letters is one affine letter |
| `runCoeff`, `tr_mul_gpow`, `tr_runWord` | a run `g m ^ e` stabilises with the Chebyshev-type `runCoeff h z e` (`1, z, hz+1, …`); run-words factorize |
| `sequential_eq_runWord`, `tr_sequential_via_factorization` | `kru4`'s sequential word *is* the run-word `(2,2,1)`; its `(hz+1)²z` re-derives from the general theorem |
| **`content_reorder_defect`** | `tr(g₀g₁g₀g₂g₁) = (∏ over the same content) + z(z² − hz − 1)`: same letters, non-ascending order, cross term |
| `pnLetterTrace_convD` | the deuteron letter `σ − (h/2)·1` has trace `(q⁴+1)/(2q(q²+1))` at convention D |

`lean`-direct exit 0; `#print axioms` on the eight load-bearing declarations =
`{propext, Classical.choice, Quot.sound}`; zero `sorry`.

## Why the production word is monotone (measured, not assumed)

`atom_braid_word_3A` (`computations/mass_at_3A_proper.py`, docstring at the definition) walks the
chain once: nucleon `k` on generators `3k, 3k+1`, then the single inter-nucleon letter at `3k+2`.
Every letter is a Hecke element `c·σ_g + d·1`; `2A+1` of them are the averaged superposition letters
(`d = −h/2`, or colour-weighted `−h(½ − δ/4)`). Concretely for ²H (23 letters): a run of 7 at `g₀`,
4 at `g₁`, 1 at `g₂` (the bond), 7 at `g₃`, 4 at `g₄` — ascending, one run per generator. By
`affine_mul_affine` each run is one affine letter, so ²H's word is `stabWord s 0 5` with five affine
letters, and `tr_affineWord` applies verbatim: **its trace is the product of five letter traces,
one of which is the bond letter `z − h/2`.**

## Consequences

1. **Bond-additivity of the production binding is a theorem about ordering, not about the
   Markov trace.** The per-bond product form the production trace implements is exact *because*
   the word is monotone (`tr_affineWord`), and would fail for the same letters in a non-ascending
   order (`content_reorder_defect`). `qou-ls86`'s `n = 3` identity is the smallest instance of the
   first fact; `qou-kru4` is the smallest instance of the second.

2. **The two open questions were one question.** The `n = 4` cross term — the only non-bond-graph
   structural source found for the collective term after `qou-brng` closed the bond-graph routes
   from four directions — can only appear in a **non-monotone** word. And the 2026-08-25 audit's
   `Vol = 0` for every production closure (32/32 SnapPy for ²H) is also a consequence of
   monotonicity: a monotone braid closes to a connected sum of `(2, k)` torus links. So:

   > A derived hyperbolic carrier and a derived collective term both require the substrate to
   > emit a **non-monotone** word. Neither can come from `atom_braid_word_3A` as written.

   The census carriers (`6₂`, `8₁₁`, `L6a4`) are admitted AME-driven fits
   (`2026-08-25-knot-id-is-an-admitted-fit.md`), and owner ruling A (2026-08-29) already retired
   `6₂` for the deuteron in favour of the canonical braid closure with `Vol = 0`. This note gives
   the algebraic reason the two facts are consistent: the derived word cannot be hyperbolic **and**
   its trace cannot carry a cross term, for the same reason.

3. **What the monotone modelling choice buys and forecloses.** The chain-walk ordering is a
   *convention* (it matches `hecke_core.atom_per_generator_volumes`), not a derived fact about
   the substrate. It buys exact bond-additivity, `Vol = 0`, and a trace that is a product of `A`
   nucleon factors and `A−1` bond factors. It forecloses both a hyperbolic-volume mass term for
   nuclei and any many-body cross term — i.e. exactly the two things the mass/binding frontier
   is missing.

## What this is not

- **Not a derivation of a non-monotone word.** Whether the substrate *should* re-cross a bond
  after a neighbour bond is not settled here, and I make no claim about it. Every bond in the
  production word is one letter (`single_crossing_binds` covers it).
- **Not a change to anything computed.** Production words are monotone; the theorem confirms
  their trace implementation is exact. No witness, no dashboard, no bean number moves.
- **Not a licence to fit interleavings to `R`.** The `0.895` nats per interleaving at the proton
  pin (`kru4`) against `R/α ≈ 1.32` (`ls86`) is an order-of-magnitude remark; matching them would
  be a fit and is not done.

## Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** Production stays monotone and exactly multiplicative, `Vol = 0`,
  census carriers stay labelled fits, `qou-brng`'s extensive-term frontier stays open. Cost 0.
  Safe to defer indefinitely.
- **Formalize-first probe of a non-monotone word class.** Before any compute: a structural
  argument for *why* an inter-nucleon bond would re-cross after its neighbour (a second-order
  Markov step in the chain walk, a closed coordination cycle at `A ≥ 3`, or the interface as a
  two-letter clasp). Then a probe measuring the resulting cross term against `R` at `A = 3, 4`
  with **no** fitted count. Cost: one Lean statement pruning the class + one probe (hours). Risk:
  the class may be empty, or the natural non-monotone word may be hyperbolic-but-wrong-volume;
  either is a scope-(a) negative. Commits to nothing in production.
- **Do not** re-assign census carriers or re-order the production word to reproduce a
  volume — that is the fit this arc has already retired twice.

**Recommendation (judgement):** the second option, gated on the structural argument existing
first. The value here is that two previously separate open items (`5vhf`'s carrier, `kru4`'s
collective term) now have one discriminating question, so a single negative result would close
both and a single positive result would open both.

## Verification

Lean: `lean`-direct exit 0, sorry-free, axiom-clean as above (the imported
`MarkovTraceInterleavedCrossTerm.olean` was built lean-direct from `main`). No `computations/`
file was touched, so the precision gates are not in scope. Repo CI is `workflow_dispatch`-only;
this agent verification is the gate.
