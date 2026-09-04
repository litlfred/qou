# The Markov trace is NOT bond-multiplicative at n = 4 — the interleaved word carries an exact cross term

**Date:** 2026-09-03 · **Beans:** `qou-kru4` (this), `qou-ls86` (the open question answered),
`qou-brng` (frontier) · **Arc:** many-body collective term / extensive-term frontier ·
**Scope:** scope-(a) **positive existence**, exact, deliberately narrow. **Nothing is wired,
nothing is fitted, no production number moves.**

## The question, as the corpus posed it

Bean `qou-ls86` (2026-08-18) needed to know whether the Markov trace can couple *distinct* bonds,
because that multi-bond level is "the one place the many-body collective term could come from" and
the only place a `Q²`-type (quadratic Coulomb) term could live (a single interface generates only
`span{1, σ}`, so every single-bond quantity is affine in the crossing). Its probe
`markov_multiplicativity_interleaved_probe.py` proved by exact algebra that on `H₃`

    tr(s₀ s₁ s₀) = tr(s₀² s₁)   identically in (q, z, h),

so the per-bond product formula is exact there — then sharpened its own caveat: the identity works
only because `H₃`'s single interleaved word is a cyclic rotation of a sequential one, and *"for
larger `n` there are interleaved words with no such rotation (e.g. `s₀ s₁ s₀ s₂ s₁`) … the general-`n`
question is **open**."*

## The answer: the product formula fails at n = 4

Two independent routes, agreeing as rational functions.

**(1) Ocneanu axioms only** — `tr 1 = 1`, the trace property, Markov `tr(x gₙ) = z·tr x` for
`x ∈ Hₙ`, the Hecke quadratic `g² = h g + 1`, the braid relation:

| word | Markov trace |
|---|---|
| interleaved `s₀ s₁ s₀ s₂ s₁` | `z (z² + h z + h² z²)` |
| sequential `s₀² s₁² s₂` (the per-bond product) | `z (h z + 1)²` |
| **difference** | **`z (z² − h z − 1)`** |

Derivation: rotate the trailing `s₁` to the front (trace property) so `s₂` is last and peel it
(Markov, `z·`); the remaining `s₁ s₀ s₁ s₀ = s₀ s₁ s₀ · s₀` by the braid relation; collapse `s₀²`
by Hecke; use the `n = 3` identity for `tr(s₀ s₁ s₀)`. The sequential word peels `s₂`, then two
Hecke collapses.

**(2) Independent: the spin-½ representation on `V^{⊗4}`** (16-dim, brick-1 R-matrix) with the
μ-weighted quantum trace normalised by `[2]⁴` — convention D, computed directly with no axioms
assumed. Same closed form. In the same representation the `n = 3` identity reproduces as exactly
`0` (control), and `tr(σ) = q³/(q²+1) = z_D` (convention check).

**At convention D** (`z = q³/(q²+1)`, `h = q − q⁻¹`):

    interleaved − product = − q³ (q² − q + 1)(q² + q + 1) / (q² + 1)³  < 0   for q > 0.

The factor `z² − h z − 1` is not new to the corpus: `qou-19jc` names it the **convention-D Markov
defect**, and `qou-xzrj` shows `z² − hz − 1 = −(q⁴+q²+1)/q² · y₍₂,₁₎` — the two-row Wedderburn
weight. So the cross term is `z × (Markov defect)`: **interleaving is priced by exactly how far `z`
sits from a root of the Hecke quadratic, i.e. by the `(2,1)` block weight.** At the proton anchor
the interleaved trace is `0.40852` of the product — an extra `0.8952` nats of log-suppression per
interleaving.

**Sign.** The interleaved trace is *smaller*, so an interleaved word class carries **extra
binding** — the direction the collective term needs (`qou-ls86`: `R` is strictly positive on the
well-bound regime, `R/α ≈ 1.32` per nucleon at plateau).

## Formalisation

`content/quantum-observable-universe/lean/QOU/MathlibExt/MarkovTraceInterleavedCrossTerm.lean`
(namespace `QOU.MathlibExt.InterleavedCrossTerm`), built directly on the corpus's
`MarkovTrace` structure (`QOU.MathlibExt.OcneanuTrace`: T1 trace property, T2 normalisation,
T3 Markov stabilisation, the `g`/`H` tower), with the Hecke quadratic and the braid relation as
hypotheses on the generators — generic `CommRing R`, `Ring A`:

| declaration | statement |
|---|---|
| `tr_g0`, `tr_g0_g1`, `tr_g0_sq`, `tr_g0sq_g1` | the `H₂`/`H₃` ladder (`z`, `z²`, `hz+1`, `z(hz+1)`) |
| `tr_g0_g1_g0` | the `qou-ls86` `n = 3` identity, by cyclicity |
| `tr_g1_g0_g1_g0` | `h·z(hz+1) + z²` via braid + Hecke |
| `tr_interleaved` | `tr(g₀g₁g₀g₂g₁) = z(z² + hz + h²z²)` |
| `tr_sequential` | `tr(g₀²g₁²g₂) = z(hz+1)²` |
| **`interleaved_sub_sequential`** | **difference `= z(z² − hz − 1)`** |
| `markovDefect_convD` | `z² − hz − 1 = −(q⁴+q²+1)/(q²+1)²` at convention D (generic `Field`) |
| `crossTerm_neg_convD` | the cross term is `< 0` for real `q > 0` |

Exact companion: `computations/probes/markov_trace_n4_interleaved_cross_term_probe.py`
(sympy exact + mpmath 50 dps at the proton pin; **11/11**).

## What this is, and is not

- **Positive existence, exact.** The framework's own trace carries a multi-bond cross term for
  interleaved word classes at `n = 4`. The multi-bond source `qou-ls86` closed at `n = 3` is
  **open at `n = 4`**, with an exact closed form and the right sign.
- **No production number moves.** The production atom word (`atom_braid_word_3A`) is
  *sequential*: one inter-nucleon letter per bond, and no generator recurs after its neighbour has
  appeared. So the production trace's bare-product implementation is exact for the production word
  class. This is a candidate **source**, not a correction to anything computed today.
- **Which word class a nucleus is** — whether any nucleus is an interleaved word, and how many
  interleavings per nucleon — is the carrier blocker (`qou-5vhf`). Reading the `0.895` nats against
  `R/α ≈ 1.32` is an order-of-magnitude remark only; matching them would be a fit and is not done.
- **`n = 4` only.** General `n` remains open; this adds the smallest instance where the product
  formula fails, next to `qou-ls86`'s smallest instance where it holds.
  **CORRECTED 2026-09-04 (same author):** `n = 4` is *not* the smallest instance. At `n = 3`,
  content `(2, 2)`, the cyclic square `(g₀ g₁)²` and the Hopf chain `g₀² g₁²` differ by exactly
  `z² − h z − 1` — the Markov defect with no `z` prefactor; the `n = 4` word above is that
  three-strand object stabilised once. `qou-ls86`'s `n = 3` identity covered content `(2, 1)`
  only. Lean: `QOU.MathlibExt.RevisitClass.cyclicSquare_cross_term`,
  `interleaved_eq_stab_cyclicSquare`; see
  `docs/audits/2026-09-04-cyclic-triple-word-class-prune-and-probe.md`.

## Recommendation (judgement, marked as such)

The extensive-term frontier's bond-graph routes were closed from every direction (`qou-brng`).
This identifies a *non-bond-graph* structural source with the right sign and a corpus-native
interpretation (the Markov defect / two-row weight). The honest next step is **not** to fit
interleaving counts to `R`; it is to ask whether the substrate's own word class for a bound
nucleus is interleaved — i.e. whether inter-nucleon bonds re-cross after a neighbour bond in any
derived (not census-fitted) carrier. That is the same carrier question `qou-5vhf` boxes; this
result says what an answer would buy.
