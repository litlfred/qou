# Habiro `[3]_q/25` — fibre Composite 4 (②) + m_τ prediction (③), post-refutation scope

**Branch:** `claude/jolly-hypatia-5kpWP` · **PR:** #1802
**Date:** 2026-06-04

Scopes tasks ② and ③ of the 2026-06-04 handover **after** the upstream
work that landed the same day: the Lean compile fixes (#1795, merged)
and the **`/25 = (T(2,5) framing)²` refutation** (#1801, merged). This
doc records what survives, corrects one effort estimate, and points the
next agent away from two dead ends.

## Upstream state (as of `origin/main` 878c32c9, 2026-06-04 06:20)

- **① Lean is fixed on main** via #1795: `MmuR9V9Closure` Theorems 14/15
  carry the correct `[3]_q/n²` normalisation (`9·T(3)=25·T(5)`,
  `25·T(5)=49·T(7)`), Theorem 19 has its trailing `ring`,
  `SpectralSequenceBasic.d` has the `(r:ℤ)` cast. `main` is **not red**.
  This branch therefore carries **no Lean changes** — only this scope
  doc + the web-sandbox toolchain addendum to `lean-environment-setup.md`.
- **`/25` framing² conjecture REFUTED** by
  [`qbeta_rung1_div25_framing_squared_test.py`](../../computations/qbeta/qbeta_rung1_div25_framing_squared_test.py)
  (#1801): the q-deformed `/[5]_q²` gives **worse** c_3 precision than
  the q-undeformed `/25`, so `/25` is **not** a categorical framing²
  that q-deforms. Verdict: `/25` is a q-undeformed empirical constant;
  structural source **OPEN** among three candidates —
  (a) classical-limit framing, (b) integer-denominator Habiro element,
  (c) unreduced Markov normalisation at 5 strands.

## ② Fibre-level Composite 4 — survives, and sharpened by #1801

### Effort-estimate correction (unchanged by the refutation)

`nf_tr` in [`tools/pyhecke/python/pyhecke/gram.py:107`](../../tools/pyhecke/python/pyhecke/gram.py)
is `sum(nf[i]·TR_M[i])` — a dot product, hence **already linear**. So
`tr_M(Σ cᵢ σ_wᵢ) = nf_tr(Σ cᵢ·NF(σ_wᵢ))` is a **< 1-session wrapper**
over the existing `_reduce_nf`, not the 5-6 sessions the handover
estimated. (Not shipped here: pyhecke's numpy/`q_parameter` import chain
isn't runnable in the web sandbox, and untested code must not land in a
published package.)

### The refutation points AT candidate (c)

#1801's surviving candidate (c) — **"unreduced Markov normalisation at
5 strands"** — is exactly the linear-combination / projector-trace
object that the ② wrapper computes. Combined with candidate (b)
("integer-denominator Habiro element"), the live ② hypothesis is now
concrete: **`/25` is the q-undeformed Markov normalisation of a
5-strand Jones-Wenzl projector / Habiro element**, whose archimedean
evaluation at real `q₀ > 1` is the empirical constant `25` (no
q-dependence — consistent with #1801). The genuinely-hard step remains
the **fibre-level** evaluation (formal `q`, then roots of unity, then
τ) needed for the Q_β *residue A* — `laurent_q.py` →
a real `QOU.Machinery.MarkovTraceOnHecke` instance. PR #1795 already
showed the archimedean q-Pochhammer route is 42/42 NEGATIVE.

## ③ m_τ cross-lepton prediction — premise weakened, not dead

| Claim | Status after #1801 |
|-------|--------------------|
| Lean `[3]_q/n²` family is internally consistent (Thms 14/15) | **holds** — pure algebra, q-undeformed; the cheap structural test passes |
| `/n²` comes from the **T(2,n) framing²** (so τ→`/49`) | **REFUTED** — `/25` is not a q-deforming framing² |
| `/n²` is a q-undeformed integer denominator with `n` = T(2,n) strand index | **OPEN** — candidates (a)/(c) above could still give integer `n²` at the classical/strand level |

So the τ→`[3]_q/49` prediction is no longer derivable from a framing²
argument. It survives **only** under the weaker hypothesis that the
undeformed integer denominator tracks the strand index `n` (candidates
a/c). Even then it is **empirically untestable**: a corpus scan
confirms **no settled m_τ bare-mass formula** and **no `Vol(K)≈34`
hyperbolic-knot assignment** exist. ③ is a prediction-without-baseline
*and* without a confirmed categorical mechanism — lowest priority of
the three.

## Recommended next moves

1. **②** (highest value): build the < 1-session linear-`tr_M` wrapper in
   a working pyhecke env, then the fibre-level roots-of-unity evaluator;
   test candidate (c) (5-strand Markov normalisation = 25 undeformed)
   directly against the c_3 residue A.
2. **m_τ baseline** (prerequisite for ③): the Vol≈34 hyperbolic-knot
   assignment is the real blocker — a separate research task, not a
   probe. Do **not** fit it (Δ_λ-gate).
3. Drop the framing² interpretation from any remaining `[3]_q/25`
   narrative — #1801 settled it.

## Δ_λ-gate

No fitted forms; nothing wired to production. All `[3]_q/25` content
remains NEAR-MATCH tier.
