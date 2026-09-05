# The `s² → |W|²` substitution shortens every half-life by 10⁴, and the two stale `W` values were one engine defect

*2026-09-05 · bean `qou-ix74` · branch `claude/weak-vertex-table-wiring-2026-09-05` · follow-on to #6664 (`qou-egvf`) and #6689 (`qou-4x7c`)*

The owner's instruction was *"merge, then the |W|² table-wiring compute tranche"*: take the
derived weak-vertex form factor `W(q) = tr_M((σ₀σ₁)⁵) = q²(q¹²+q⁸−1)/(q²+1)²` and wire
`|W|²` into the half-life predictions in place of the single-crossing coupling `s²`, as
`prf:hadron-half-life` item 1 and `rem:hadron-half-life-fermi` open computation 2 prescribe,
then measure the heavy-nucleus residual. Three things were measured. The first is the
answer; the other two were found on the way and are larger.

## 1. The prescribed substitution is a scope-(a) negative

`s² = (q^{1/2} − q^{−1/2})² = (q−1)²/q ≈ 0.010897` at the proton pin; `|W(q₀)|² ≈ 1.4101`.
The rate scales by `|W|²/s⁴` and the half-lives by `s⁴/|W|²`:

| quantity at `q₀` | value |
|---|---|
| `|W|²/s⁴` (rate factor) | **1.18754 · 10⁴** |
| `s⁴/|W|²` (half-life factor) | **8.42 · 10⁻⁵** |

Applied to the six s²-based predictions the block's own Lean carries (`pred_*`: 13.0 yr,
6800 yr, 6.2 yr, 32 yr, 33 yr, 5.8 d — the "10–17 % overshoot" set), every substituted
half-life lands at `≈ 10⁻⁴` of the observed value. The substitution is therefore not the
10–17 % correction the corpus attributed to it; it is a four-orders-of-magnitude change.
**This is a negative about the prescribed substitution, not about `W`**: `s²` is a small
crossing amplitude and `W` is an O(1) normalised trace, and nothing in the corpus derives the
normalisation that would make one replace the other. Formalised, sorry-free, at the pin:
`QOU.Braiding.WeakVertexT35.substitutionRateFactor_gt_ten_thousand` and
`…_lt_twenty_thousand`, with the exact closed form
`|W|²/s⁴ = q⁶(q¹²+q⁸−1)²/((q²+1)⁴(q−1)⁴)` (`substitutionRateFactor_eq`).
Producer: `computations/markov/weak_vertex_substitution_scale_probe.py` →
`weak-vertex-substitution-scale.witness.json`, 6/6.

The corpus's own live producer `computations/t35-weak-vertex.py` had been printing this
factor — as `7.9·10³` with its then-wrong `W` — and the sentence *"the corrected half-lives
are 0.0001× the old values"* since 2026-08-29. Nothing read it.

## 2. `hecke_division`'s Markov trace was wrong on every word with a repeated lower generator

`t35-weak-vertex.witness.json` (committed 2026-08-29) carried `W_q = 0.9684` at
`z_D = 0.61269` — a third value for the same word under the same convention as the
canonical `1.18748`. Per-power comparison against the canonical recursion and the Wedderburn
closed forms `y₍₃₎q^{2k} + y₍₂₁₎χ₍₂₁₎((σ₀σ₁)^k)`:

| k | `hecke_division` (old) | canonical | Wedderburn |
|---|---|---|---|
| 1 | 0.37539 | 0.37539 | 0.37539 |
| 2 | 0.42347 | 0.51988 | 0.51988 |
| 3 | 1.33918 | 1.43980 | 1.43980 |
| 4 | 0.80801 | 0.91725 | 0.91725 |
| 5 | 0.96844 | 1.18748 | 1.18748 |

The reducer was never at fault: re-tracing its reduced terms for k = 5 with the correct
basis values gives `1.18748` exactly. The defect was in `_trace_word`, which applied only the
Markov rotation `tr(x·σ_top) = z·tr(x)` and never the Hecke relation, so an intermediate
`σ₁σ₁` was traced as `z·z` instead of `h·z + 1`; on the basis word `σ₁σ₂σ₁` it returned
`z³ = 0.2300` against the Ocneanu `hz² + z = 0.6912`, and that one difference times the
reduced coefficient `0.4750` is the whole `0.2190` gap. A second defect: its memo cache was a
shared mutable default keyed on the word alone, so a second instance with a different `z`
read the first instance's numbers (which is why the first `z_C` re-run returned the `z_D`
number). Fix: `markov_trace`/`_trace_word` now delegate to
`markov_trace_canonical.tr_M_word` with the instance's `z` and `h = q − q⁻¹`; the patched
engine agrees with the canonical trace to `< 5·10⁻¹⁶` at every k, honours a changed `z`, and
traces `σ₁σ₂σ₁` correctly. Blast radius measured: two live importers (`t35-weak-vertex.py`,
which calls `markov_trace`, and `nf-qvalues.py`, which does not), no tests, three witnesses
naming the module.

## 3. The provenance of `0.7036` — and a correction of my own claim

The 2026-09-04 audit doc and everything downstream of it (Lean header, producer docstring,
witness field, the #6689 author note, two beans, two PR bodies) said the published
`0.7036` *"descends from the deprecated convention-C pipeline
`computations/_deprecated/t35-full-calculation.py`"*. That was a guess from file names.
Measured: the defective rule above, `Σ_w c_w z^{|w|}` over the reduced `(σ₀σ₁)⁵`, gives
**0.70355 at `z_C`** and **0.96844 at `z_D`** — the two stale values are one defect at two
Markov parameters, and the deprecated pipeline had nothing to do with it. Asserted in the
probe's witness to four figures. The in-repo sites are corrected in this tranche; the PR
bodies are left as the record.

## 4. Table 4 has no producer

`ex:hadron-half-life-verification` Table 4 (the "Skein-Coulomb enhancement, < 3 %" table:
12.28 yr, 5896 yr, 5.308 yr, 28.92 yr, 30.26 yr, 5.022 d) is reproduced by no script:
zero hits on its six values across `computations/` and `docs/` outside one unrelated audit
line, and the block's `.ts` carries no `computation` field. The Lean `pred_*` (13.0, 6800,
6.2, 32, 33, 5.8) and `t35-weak-vertex.py`'s hard-coded "old pred" list (12.40, 6690, 6.17,
31.9, 32.9, 5.79) are two further, mutually different sets. The `< 3 %` claim is therefore
an unreproduced published table. Not edited here; recorded for the owner (bean `qou-ix74`).

## What this leaves open

The heavy-nucleus residual cannot be measured by the prescribed wiring, because the wiring is
not a like-for-like substitution. What a correct coupling normalisation would be — a ratio
such as `W/W(1)` or `W` against the trefoil trace, or a genuinely different object — is a
derivation question, not a compute one, and is left as the open item on the bean rather than
guessed at here.
