---
# qou-nk3h
title: term4 Frobenius co-Casimir reads a witness that has NEVER existed — two producers silently fall back to a constant
status: completed
type: task
priority: normal
created_at: 2026-08-26T16:53:01Z
updated_at: 2026-08-26T17:16:21Z
---

Found 2026-08-26 while answering "are the low-isotope dashboard's witnesses
updated?". Not the question that was asked, and worse than the answer.

## The finding

`computations/probe-term4-conventions.witness.json` **has never existed in this
repository**, and **no producer in the tree writes it.**

    git log --oneline --diff-filter=AD --all -- '*probe-term4-conventions*'
    (empty)

Two producers read it, with an identical loader that swallows the failure twice:

    computations/unified_low_isotope_predictor.py:88   _load_sigma_3A
    computations/mass_formula_6term.py:73             _load_sigma_3A_table

        if not path.exists():
            return {}
        try:
            ...
        except Exception:
            return {}

No warning on either path. A third file, `rho_k_h3a_co_casimir.py:4`, cites the
same witness in a source comment as its data source.

## What it costs

In `unified_low_isotope_predictor`, `term4_frobenius` is documented as
*"m_e · Σ_{λ⊢3A} 1/dim_q(λ), per prop:frobenius-codim-universal"* with
*"Coverage: witness covers A ∈ {1..7} exactly"*. With the table empty it takes
its `A >= 8` fallback for **every** isotope, so T4 is the constant
`m_e · 2.05 = 1.0475 MeV` from D to 16O. That is visible in the producer's own
output and nobody had looked:

    sym   A        T1        T4        T5    T6       k>=3   Δshell
    D     2    3.1857    1.0475    0.0000  0.00 -261785.13   0.0435
    T     3    2.1264    1.0475    8.7501  0.00 -340659.01   0.0435
    3He   3    2.5104    1.0475    8.2429  0.00      0.0000  0.0435
    4He   4    0.0000    1.0475   22.5467  0.00      0.0000  0.0435

The docstring describes an algebraic per-3A trace; the code returns a literal.

## Fixed here (the guard), NOT fixed here (the table)

Both loaders now warn on stderr and name this bean; `unified_low_isotope_
predictor` also records `_SIGMA_3A_UNAVAILABLE`, and its `term4_frobenius`
fallback comment says plainly that it is taken for every A. The docstrings that
claimed coverage are corrected.

**The table is deliberately not reconstructed.** `Σ_{λ⊢3A} 1/dim_q(λ)` is
computable — but there are **ten LIVE `dim_q` implementations** under
`computations/` with differing signatures (`phase5/phase5_n8_dim_q_table.py`,
`delta_lambda_empirical_tabulation.dim_q_at_q0`, `term7_chi5_basis.dim_q`,
`chirality_avg_content_atomic.dim_q`, four under `deltalambda/`, ...), so
building it is a **choice among conventions**, not a computation. Picking one
silently is the same failure as the one being fixed. Whoever takes this should
name the implementation and say why.

**Correction to my own first pass, recorded because it is the same error class:**
I initially reported that every `dim_q` was deprecated and concluded the
machinery was gone. That came from reading `head -8` of a grep whose output
happened to sort `_deprecated/` first. Ten live ones exist. Truncated view,
confident conclusion — check the whole listing.

## Also fixed in the same commit (small, same file)

- `import numpy as np` with **zero** `np.` uses, and the witness declaring
  `engine="python+numpy"`. Removed the import; engine is now `python+mpmath`.
- `term4_frobenius` returned a Python float literal `2.05`; now `mp.mpf("2.05")`.
  This is the NO-FLOAT64 discipline at the one site the fix touched — it does
  **not** address the producer's other 70 raw-float64 payload fields, which are
  `qou-syit`.

## Not in scope

Whether `B_pred_MeV = -261780` for deuterium means anything. It does not, but
that is the producer's physics, and the k>=3 tail rather than term 4.


## RESOLVED 2026-08-26 — the table is built, and the convention was measured not chosen

`computations/probe_term4_conventions.py` now produces
`probe-term4-conventions.witness.json`, and both consumers read it. T4 in
`unified_low_isotope_predictor` varies with A again — 1.6363 / 1.2999 / 1.1507
/ 1.0670 / 1.0526 MeV at A = 2,3,4,6,7 — instead of the flat 1.0475.

### The convention decision I said needed the owner: it did not

I wrote in the guard commit that reconstructing the table was "a choice among
conventions, not a computation". That was the right caution and the wrong
conclusion. Measured, two axes are genuinely free and both move the answer:

| axis | option A | option B | Σ at A=7 |
|---|---|---|---|
| q-integer | balanced `(q^h−q^-h)/(q−q^-1)` | unbalanced `(q^h−1)/(q−1)` | **2.0599** vs 2.0337 |
| row cap | all λ ⊢ 3A | ≤ 6 rows | **2.0599** vs 1.0299 |

The row cap is a factor of 2, because capping removes the column partition
`(1^{3A})`, which contributes exactly 1.

Three facts already in the corpus pin both axes, so nothing was selected here.
Each is a passing assertion in the witness:

1. **The consumer's own docstring.** It quotes *"at A=7 the actual value is
   2.060, at A=6 it is 2.088"*. Balanced/uncapped gives **2.0599** and
   **2.0881**. Unbalanced gives 2.0337/2.0506; the 6-row cap gives
   1.0299/1.0440. Neither of the other three combinations produces the quoted
   pair.
2. **The legacy constant.** `FROB_N3 = m_e·(2 + 1/[2]_q)` with balanced
   `[2]_q = q + q⁻¹` is `2.4972905456049155559958…`, and the table's `n=3`
   entry is `2.4972905456049155559958…` — every digit computed, an independent
   corpus object landing on the A = 1 case.
3. **The extreme blocks.** `dim_q((n)) = dim_q((1ⁿ)) = 1` (a single row's hooks
   are exactly n, n−1, …, 1, so the hook product *is* `[n]_q!` — convention
   free), so Σ → 2 from above. That is the behaviour the fallback constant 2.05
   was estimating, and A = 8 measures 2.0419, still decreasing.

The lesson generalises: *"this needs a convention decision"* was itself a
measurable claim, and measuring it collapsed the option space to one. Do the
measurement before escalating.

### The table

    A   n=3A    #λ    Σ 1/dim_q at q₀
    1      3     3    2.497290545604915556
    2      6    11    3.202134001221746245
    3      9    30    2.543883846981462374
    4     12    77    2.251934048039022824
    5     15   176    2.137440963561643627
    6     18   385    2.088090699685484443
    7     21   792    2.059888298036941438
    8     24  1575    2.041868785885538295

Parameter-free: a finite combinatorial sum at the substrate q₀ (proton pin), no
experimental input. mpmath at 60 dps, serialised as 50-digit strings.

### Two precision defects fixed on the way in

- **`mass_formula_6term` parsed the table with `float(val)`.** Harmless while
  the table was absent; a real 50-digit → float64 truncation the moment it
  exists. Both loaders now go through `_mpf_from_witness_value`, which parses a
  string and **refuses a JSON number** rather than wrapping the loss in an mpf
  — `mp.mpf(str(<float>))` is the laundering pattern the precision gates flag,
  and writing it would have been the easy wrong fix.
- **My own assertion bounds were float literals.** The raw-float64 ratchet
  caught 12 fields (`expected`/`tolerance`) on the first run of the new
  producer. Carried as `mp.mpf` instead.

Display-only `float()` casts were added at five f-string sites across the two
consumers, which now receive mpf where they used to receive float. Arithmetic
stays mpf; AGENTS.md permits the cast inside an f-string.

### Verification

Both consumers exit 0 with the table wired and no warning.
`scripts/precision-gates.sh --changed`: **all blocking gates green, exit 0**,
before and after.

### Explicitly NOT claimed

**This does not make the predictor's physics right.** `B_pred(D)` is still
−261780 MeV — the k≥3 tail, not term 4. And ⁶Li now lands at **+0.00 %**
(31.9946 vs 31.9940 AME), which is **not** a result: in a predictor that misses
deuterium by 10⁷ %, one isotope landing on target is noise finding a target, and
its T1 is 0.0000 there. Do not quote it. The predictor's stale witness
(`qou-syit`) is now *more* stale, and still cannot be refreshed until its 70
raw-float64 payload fields are fixed at the producer.

---

## 2026-09-07 — correction: the witness AND its producer both existed

Not my bean; adding a finding, not resolving it.

`mass_formula_6term._load_sigma_3A_table` carried this in bold: "**That witness
has never existed in this repository and no producer in the tree writes it**"
(measured 2026-08-26, cited to this bean). Both halves are false. The
measurement was taken on a shallow clone, where a negative claim about history
is only as good as the depth. Against the full **36771-commit** history:

    computations/probe_term4_conventions.py
    computations/probe-term4-conventions.witness.json
    folio-assistant/computations/probe_term4_conventions.py       (earlier path)
    folio-assistant/computations/probe-term4-conventions.witness.json
    _deprecated/probes/probe_term4_conventions.py                 (final path)
    _deprecated/probes/probe-term4-conventions.witness.json

    git show 530e326cab3:computations/probe-term4-conventions.witness.json

**And it fits the loader exactly.** The recovered payload is
`data.sigma_inv_dim_q_at_q0`, keyed `n=3, 6, 9, … 24` (A = 1…8) as 49-digit
decimal strings, plus `n_partitions`. That is precisely the shape
`_load_sigma_3A_table` reads — including the `data`-nesting the 2026-08-26
note says the pre-fix loader would have missed. So the loader would work
against this file verbatim, with no adaptation.

    n=3   2.4972905456049155559958392316648696318481907303285
    n=6   3.2021340012217462447876888457263824407351830058928
    n=9   2.5438838469814623740414261832455538873537132874296
    n=12  2.2519340480390228235777192335579209844500138474823
     …    (through n=24)

**Deliberately not restored.** Two reasons, and the first is absolute: placing
a witness recovered from history is hand-placing numbers that no producer ran
in this tree, which is the one move this corpus forbids outright. Second, it
is a numbers-move — Term 4 would switch from the caller's fallback to the real
Σ_{λ⊢3A} 1/dim_q(λ) table inside a live mass formula, so it wants sequencing,
not a side effect of a docstring fix.

**The supported route is to revive `probe_term4_conventions.py` from
`_deprecated/` and RE-RUN it**, which produces a witness with today's q₀
anchor and precision rather than a 2026-05 artifact. Note the recovered
witness predates the q₀-anchor work entirely, so its values should be treated
as a schema reference, not as an answer.

The docstring now says all of the above instead of "never existed". Commit
`3b87ba5558d`; sibling finding on `qou-imkb`, whose claim failed the same way.
