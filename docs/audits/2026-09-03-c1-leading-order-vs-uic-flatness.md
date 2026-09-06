# The leading order is strongly A-dependent; by k = 11 the A-dependence is gone

> **🛑 THE `c_k` BELOW ARE GROUPED-WORD VALUES — CORRECTED 2026-09-06 BY THEIR
> OWN AUTHOR.** `7db032fb48` (owner ruling, bean `qou-hu1f`) made the Borromean
> intra-nucleon ordering canonical, and these coefficients were computed on the
> old default without pinning it. They move — `c₁(⁴He)` by a factor of **37**,
> `259/128 → 7/128` — and `c₁(nn)` becomes **exactly 0**.
>
> **Scope, not refutation:** the `c₁` values here are correct as recorded for the
> grouped word and are superseded as current values.
>
> Full table under both orderings, and what survives:
> [`2026-09-06-the-c1-c2-crossover-is-grouped-specific.md`](2026-09-06-the-c1-c2-crossover-is-grouped-specific.md).
> The `c₀` floor IS ordering-invariant, so everything resting on it is untouched.

> **🛑 NAMING CORRECTION (added 2026-09-04).** The `c_k` in this document are
> **NOT** the Q_β precision-ladder `c_k` that
> [`ck-dk-canonical-registry.md` §2](../coordination/ck-dk-canonical-registry.md)
> governs, and not that registry's `a_n` either. They are the `ℏ_q`-expansion
> coefficients of `Δtr = tr_M(W_free) − tr_M(W_atom)` — a **third object with no
> registry row**. The separation is not subtle: ladder `c₂ = −1`, `c₃ = −2.0693`;
> here `c₂ = +29.90`, `c₃ = +247.98`. The registry's `a_n` is excluded by its own
> 3-term recursion (predicts `a₂ = −1.52` against an actual `27.87`). This
> matters because the ladder's headline claim is about **the non-monotonicity of
> a `c_k` series**, and so is this document's — same glyph, same-sounding claim,
> unrelated objects. Full working:
> [`2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md`](2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md).
> The glyph came from PR #6492's probe; not checking the registry before
> propagating it across three documents is mine.

**Cross-check between two independently-derived results, verified against landed
code rather than against a PR comment.** Beans `qou-brng` / `qou-pdg9`.

## The two results

**#6492 (`qou-pdg9`, merged)** derives the leading `ℏ_q` coefficient of the trace
difference `tr_M(W_free) − tr_M(W_atom)` in closed form
([`c1_leading_coefficient_derived_probe.py`](../../computations/probes/c1_leading_coefficient_derived_probe.py):554):

    c₁(Z,N) = (21Z + 16N)·(2^{−A−1} − 2^{−2A}) − 4·(I_pp − I_nn)·2^{−2A}
    with   i_pp, i_nn = max(Z−1, 0), max(N−1, 0)

**#6427 (`qou-brng`, merged)** measures `unified_iterative_correction` to
`k_exact = 11` at matched truncation, ⁴He against ⁶Li, and finds it **flat**:
ratio **0.9504** while `C(A,2)` grows 2.5×.

## The comparison

At Z = N the `I_pp − I_nn` term vanishes (`(Z−1) − (N−1) = 0`), so both nuclei
evaluate cleanly:

    c₁(⁴He) = 74 · 7/256    = 259/128  = 2.0234375
    c₁(⁶Li) = 111 · 31/4096 = 3441/4096 = 0.840087890625
    leading-order ratio     =   93/224  = 0.41518

    measured uic ratio at k = 11        = 0.9504
    factor                              = 2.29

`c₁(⁴He) = 259/128` **reproduces #6492's own recorded value** for ⁴He exactly
(line 389 of that probe), so the arithmetic here is checked against their table
and not merely against their formula.

## What it says: the cancellation, quantified

`c₁` at Z = N decays roughly like `2^{−A}`:

    A     2       4       6       8      10      12
    c₁  2.3125  2.0234  0.8401  0.2868  0.0902  0.0271

**So at first order in `ℏ_q` the A-dependence is strong and falls off
exponentially. By k = 11 it is gone** — the summed accumulator returns
essentially the same number at A = 4 and A = 6. That is the cancellation
`qou-brng` localised to the `y_λ`-weighted telescoped sum, now with a magnitude
attached at its first order: the leading term alone would predict a **2.4×**
drop from ⁴He to ⁶Li, and the full sum delivers **1.05×**.

## Scope — this is a comparison, not an identity

**The two objects are not the same series, and this note does not assert they
are.** #6492's `c₁` is the leading coefficient of `tr_M(W_free) − tr_M(W_atom)`;
`unified_iterative_correction` is a `y_λ`-weighted telescoped sum over
partitions whose chains come from `_step_chain_generic`, not from
`atom_canonical_crossings`. Checked: no shared call.

So the factor 2.29 is **not** evidence of a defect in either result. It is what
you would expect if the higher orders of a genuinely A-dependent series
progressively cancel — and it is equally consistent with the two objects simply
having different A-behaviour. **Distinguishing those two readings requires
`c₂`, `c₃`, … of the same expansion**, which nothing here supplies.

## A correction to my own reasoning, not to the number

When I first ran this cross-check (comment on #6492, before it merged) I stated
that I had guessed `I_pp`/`I_nn` to be **pp and nn pair counts**, i.e.
`C(Z,2)` and `C(N,2)`. **That guess was wrong.** They are *chain interface*
counts, `max(Z−1,0)` and `max(N−1,0)` — a different quantity.

The conclusion was unaffected, and for a reason worth stating rather than
glossing: **both readings are symmetric in Z and N**, so both give difference
zero at Z = N. Getting the right answer from the wrong definition is not the
same as getting it right, and the check that settled it was reading the landed
source — which is why the cross-check was deliberately re-run after #6492 merged
rather than left standing on the pre-merge comment.
