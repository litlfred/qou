# χ-convention mass-path verdict — averaged (B) is correct, NOT a bug

**Date:** 2026-06-29
**Branch / PR:** `claude/chi-convention-massB-verdict-2026-06-29`
**Resolves:** the ⚠ "off-canonical consumer finding" from #3047
([`2026-06-28-chi-convention-label-audit.md`](2026-06-28-chi-convention-label-audit.md))
**Probe:** [`computations/chi_convention_trM_ratio_probe.py`](../../computations/chi_convention_trM_ratio_probe.py)
+ `chi-convention-trM-ratio-probe.witness.json`

## The question

#3047 flagged that `canonical_tr_m_via_chi_cache.py` — consumed by the mass /
vol-density / per-knot path (incl. `_li_2_q_util.vol_density_per_block`) —
loads the **averaged-crossings (B)** χ cache, while the canonical *binding*
path (`binding_canonical.py`) uses the Jones–Markov trace (C). Since
`vol_density_per_block = [Vol(K)/ℏ_q²]·tr_M_K` is **linear** in `tr_M_K`, the
production delta from switching to the sign-only (A) cache is exactly the
ratio `tr_M_A / tr_M_B`. Is the current B-usage a bug?

## The measurement

`tr_M = Σ_λ y_λ(q₀)·χ^λ` computed from both caches with the **same** `y_λ`:

| atom | tr_M avg (B) | tr_M sign-only (A) | A/B |
|---|---|---|---|
| proton | **1.06531** | 1.63315 | 1.533× |
| neutron | **0.92323** | 1.63315 | 1.769× |
| deuteron | 0.38836 | 1.33178 | 3.429× |
| ⁴He | 0.05387 | 0.88562 | 16.44× *(B partial 22/77 — unreliable)* |

So switching would move the per-knot density (and anything linear in it) by
**1.5–3.4×**. But that does **not** make the current value wrong.

## Verdict: NOT a bug — B is the correct convention for the mass path

Two facts settle it:

1. **Sign-only (A) collapses the p/n distinction.** A gives
   `proton = neutron = 1.63315` (identical — the crossing *signs* are the same
   for both nucleons). It therefore **cannot** produce `m_n ≠ m_p`. The
   averaged (B) color-weighting gives `proton 1.06531 ≠ neutron 0.92323` — the
   asymmetry the mass path needs (cheat-sheet §"Bring color-tube weighted
   averaging": the averaging reproduces `Δm_{n-p}`).
2. **The documented canonical-for-mass values ARE the averaged ones.**
   `_li_2_q_util.py` (the `vol_density_per_block` docstring) states *"the H₃
   Markov trace tr_M(𝓑₃) ≈ 1.065 (proton) / 0.923 (neutron)"* — exactly the
   averaged (B) values, not sign-only's 1.633/1.633.

Switching the mass path to A would **destroy the proton–neutron mass
difference**. So B is required there.

## Correction to the #3047 framing

#3047's "mass/vol-density path runs on B while binding runs on C — a real
convention inconsistency" over-flagged it. The honest picture is an
**intentional three-convention structure**, each path using the trace correct
for its purpose:

| path | convention | why |
|---|---|---|
| production character catalogue / `chi_lambda_braid` | **A** sign-only | the Geck–Pfeiffer braid character; marshalling maps averaged→sign |
| mass / vol-density / per-knot density | **B** averaged | **required for the p/n asymmetry**; documented `1.065`/`0.923` |
| binding (`binding_canonical`, free − bound) | **C** Jones–Markov | `prop:categorical-mass-markov` |

`canonical_tr_m_via_chi_cache`'s "canonical" name is therefore correct *for
its path* (mass/density). No code change is warranted; the convention labels
added in #3047 already make each cache's convention explicit, which is what
prevents a future mis-consume across these three paths.

## Note for the audit tool

The #3047 `chi_convention_audit.py` tags averaged (B) caches as
"off-canonical" — that label is scoped to the **binding** convention (where B
is deprecated). It should not be read as "off-canonical for mass": for the
mass/vol-density path, B is the canonical trace. The `off-canonical` count is
informational only and does not gate `--strict`, so this nuance does not
cause false CI failures.
