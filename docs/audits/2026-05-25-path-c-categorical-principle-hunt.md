# Path C — Categorical-principle hunt for `−G·h²` linking-weight

**Date:** 2026-05-25
**Branch:** `claude/h-expansion-mpf-50dps-2026-05-25` (PR #1287 stack)
**Status:** Workplan — enumerates and pre-screens 7 candidate categorical
principles that could yield `−G·h²` as the h² coefficient of
`linking_weight` for the Borromean 𝓑₃ baryon mass formula.

## Why we're here

[Reading-A residual probe at 50 dps](../../computations/reading_a_residual_at_50dps.py)
shows that **`5/2 − G·h²`** matches the m_p-anchored target
linking_weight to within 1.38e-5 (≈ 5.6 ppm in m_p), closing
99.98 % of the Family A gap with a single h² coefficient swap.

But existing audits foreclose two natural derivations:

- [PR #701 (2026-05-18)](https://github.com/litlfred/qou/pull/701)
  falsified the **Wedderburn-sum form** of `5/2 − G·h²` across
  5 structural routes. The −G coefficient does not arise from
  any Σ_{λ ⊢ N} dim_q V_λ on H_N(q).
- [audit 2026-05-23](2026-05-23-yekutieli-bijection-natural-reading-negative.md)
  found that the **natural reading of the Yekutieli half-symmetric
  projection** at H_4 yields +0.5 (not −G); load-bearing bijection
  conjecture (from 2026-05-22 audit) NEGATIVE.

Family A's `+3/4·h²` is **Lean-proved**
([`lambda-scale-substrate-form.lean`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.lean)).
So any new principle yielding `−G·h²` cannot replace Family A; it
must either (a) yield a CORRECTION term added to Family A summing to
`(3/4 − x)·h²` for some x or (b) come from a DIFFERENT categorical
chain than the H_4 Wedderburn sum (i.e. `linking_weight` is not the
Wedderburn sum).

## Acceptance criteria (every candidate is judged on these)

1. **Substrate-natural derivation.** Must derive from a categorical
   principle native to the QOU substrate stack (q-Hecke, Yekutieli
   non-abelian Stokes, KLR / Kashiwara crystal, etc.). No empirical
   fit, no PSLQ candidate that PR #701 already falsified.
2. **h² coefficient = `−G − 3/4` (= −1.666)** if additive to Family A,
   OR **h² coefficient = `−G`** if replacing Family A's `+3/4`.
3. **Bar-symmetric** — partitions (3,1) ↔ (2,1,1) carry identical
   contributions (AGENTS.md §7b Type-B folding).
4. **Doesn't contradict PR #701's 5 falsified routes.** PR #701
   ruled out Wedderburn-sum incarnations; new candidates must come
   from elsewhere.
5. **Doesn't contradict the audit-2026-05-23 natural-reading.** Natural
   Π_HS at H_4 gives +0.5; new candidates must invoke a twisted /
   non-natural reading with stated rationale.

## Candidate enumeration

### C1 — Higher-N Wedderburn limit `(1/N) · Σ_{λ ⊢ N} dim_q V_λ` as N → ∞

**Hypothesis.** Family A is `(1/4)·Σ_{λ ⊢ 4} dim_q V_λ` evaluated at H_4.
What if the "correct" linking_weight is the **N → ∞ limit** of the same
sum normalized differently?

**Status.** Testable. Compute `(1/N)·Σ_{λ ⊢ N} dim_q V_λ` for
N = 5, 6, 8, 12, ... at q_0 and check whether the h² coefficient
stabilizes near −G.

**Pre-screen at q_0.** The Wedderburn sum on H_N has h-coefficient
structure dictated by `[k]_q` factors. At leading order `(1/N) · Σ`
grows linearly with strand count (Stirling-bound estimate), so the
limit likely DIVERGES, not converges to −G. **Plausibility: LOW.**

**Foreclosure check.** PR #701 specifically falsified `−G` as a
Wedderburn-sum, but the falsification was at fixed N. The limit
hasn't been explicitly tested.

**Verdict.** Cheap to test (1 single-session compute). If h²
coefficient diverges with N → ∞, ruled out. If converges to −G, big
discovery. Worth a probe.

### C2 — Yekutieli with sign-reversed / twisted reading

**Hypothesis.** The natural reading of `Π_HS` at H_4 gives +0.5 (audit
2026-05-23). What if the TWISTED reading — e.g. `Π_HS` with a sign
flip on conjugate-pair partitions, or with a different projection
ordering — gives `−G` instead?

**Status.** Speculative; needs an EXPLICIT alternative projection
construction.

**Pre-screen.** The Yekutieli per-cell integral is sensitive to
orientation. A "wrong" orientation choice changes the sign but not
the magnitude (so +0.5 → −0.5, still not −G ≈ −0.916). To get from
+0.5 to −0.916 requires both a sign flip AND a magnitude correction
of 1.83×. The 1.83 factor isn't obviously natural — no simple
involution or symmetry yields it.

**Foreclosure check.** The 2026-05-23 audit explicitly tested the
natural reading; it didn't enumerate ALL readings. Some non-natural
reading could exist.

**Verdict.** Hard to investigate without a CONCRETE alternative
projection candidate. Lower priority unless someone identifies one.

### C3 — KLR / Kashiwara crystal h² correction

**Hypothesis.** AGENTS.md §7b mentions "Type B folding for chirality /
CPT" and "decategorifying to KL bases for the classical limit." The
KLR algebra has its own categorification of the q-deformation. Maybe
the h² coefficient of linking_weight in the KLR canonical basis
differs from the H_4-Wedderburn h² coefficient.

**Status.** Mathematically rigorous (KLR is well-studied); needs a
concrete bridge between KLR canonical basis and the Borromean
linking-weight formula.

**Pre-screen at q_0.** No closed-form pre-screen possible without
building the bridge. KLR's `+1·h⁴` driver appears in PR #1276's
13-driver menu (driver xiii). If the h² channel has a similar KLR
identity, the coefficient would come from a structural sum like
`Σ_λ a_λ · [some KLR weight](λ)`.

**Foreclosure check.** Not in PR #701's 5 routes (PR #701 tested
Wedderburn / Frobenius / Demazure / LP-Plancherel / LP-Frobenius).
KLR is a separate categorical layer.

**Verdict.** **HIGH PRIORITY.** Genuinely new layer; not foreclosed
by prior audits. Multi-session research (need to build KLR machinery
in Python/Lean), but the framework already cites KLR as a substrate
principle (`docs/canonical-derivation-cheat-sheet.md §brane tower`).

### C4 — q-Langlands / motivic-period derivation

**Hypothesis.** Catalan's constant `G` is a motivic period — it
appears as `L(2, χ_4)` (Dirichlet L-function at s=2) and as
`Vol(4_1)/2 = Λ(π/4)` (the figure-eight ideal-tetrahedral volume in
half-units). Maybe linking_weight's h² coefficient is a motivic
period attached to 𝓑₃.

**Status.** Speculative; needs a specific motivic chain.

**Pre-screen.** Vol(𝓑₃) = 8·G (Adams 1985). The h²-coefficient `−G`
would equal `−Vol(𝓑₃)/8`, i.e. `−V_oct` (volume of ONE ideal
octahedron). This is exactly what the Yekutieli per-cell conjecture
(2026-05-22 audit) attempted, and the natural reading was negative.

**Foreclosure check.** This is the SAME `−G ≈ −V_oct` interpretation
the 2026-05-23 audit found NEGATIVE at h². The motivic framing
doesn't add new content — it's a rebranding of the Yekutieli
per-cell conjecture.

**Verdict.** Same plausibility as C2 (twisted Yekutieli) — needs a
non-natural reading. Don't double-count.

### C5 — Faddeev iterated tower in the h² channel (not h⁴)

**Hypothesis.** PR #1276 uses Faddeev iteration `1/(1−h⁴)` for the h⁴
channel. What about Faddeev iteration in the h² channel:
`f(q) = 1 + α·h² + α²·h⁴ + α³·h⁶ + ... = 1/(1 − α·h²)`. Find α such
that f at q_0 matches `5/2 + (−G)·h²`.

**Pre-screen.** At q_0, f(q_0) = 1/(1 − α·0.0437). Setting f = 2.46:
α·0.0437 = 1 − 1/2.46 = 0.5935, so α ≈ 13.58. That's a large α; the
geometric series converges only for |α·h²| < 1, i.e. α < 22.9. So
α = 13.58 is barely within radius of convergence — fragile.

The h² coefficient of f around h=0 is α ≈ 13.58, NOT −G ≈ −0.916.
This h²-Faddeev candidate doesn't produce a −G coefficient — it
matches linking_weight AT q_0 but has wildly different h⁰ and h²
structure.

**Foreclosure check.** This is structurally similar to PR #1276's
candidate (rational matching at q_0, NOT an h-series correction).
Ruled out as a "−G·h² coefficient" candidate; could still be a
totally different replacement, but that's PR #1276's territory.

**Verdict.** **LOW PRIORITY** — doesn't yield −G·h², just matches
linking_weight at q_0 via a different rational.

### C6 — Reading B + Faddeev h⁴ tower "happens to equal" Reading-A at q_0

**Hypothesis.** Reading B (Family A + Yekutieli additive) gives
`5/2 + (3/4 − G)·h² = 2.4927` at q_0. Adding a Faddeev h⁴ tower
`α·h⁴/(1 − β·h²)` calibrated to push 2.4927 → 2.4599 might be a
substrate-natural CORRECTION sequence.

**Pre-screen.** Need 2.4927 → 2.4599 = −0.0328 correction. At
h² ≈ 0.0437, this could be h² · (−0.75) = `−0.0328`. So Reading B + (−0.75·h²)
= 5/2 + (3/4 − G)·h² + (−0.75)·h² = 5/2 + (−G)·h² = **exactly
Reading-A**.

Interesting — Reading-A is `Reading B + (−3/4)·h²`. The `(−3/4)`
EXACTLY CANCELS Family A's `+3/4`. Result: the Wedderburn h²
contribution disappears entirely, leaving only the Yekutieli per-cell
`(−G)·h²` term.

**Categorical interpretation.** This would mean the substrate-pure
linking_weight is **the Yekutieli per-cell ALONE**, NOT the
Wedderburn sum. The Wedderburn sum is a structurally different
quantity (some other Hecke-algebra invariant) that happens to share
h⁰ = 5/2 by coincidence.

**Foreclosure check.** This contradicts the audit 2026-05-22's
"framework B only — Family A + Yekutieli additive" directive,
which explicitly REJECTED the "Reading-A replacement" interpretation.
But it's a categorically coherent alternative.

**Verdict.** **WORTH FORMALIZING AS PATH B** (conditional Lean
theorem). Doesn't prove Reading-A categorically, but encodes its
structural meaning clearly: Reading-A = "linking_weight is the
Yekutieli per-cell, NOT the Wedderburn sum."

### C7 — Two-form 𝓑₃-bounding-Seifert-surface integral

**Hypothesis.** The Borromean rings bound a Seifert surface S in
S³ \ 𝓑₃. Integrating the q-deformed Chern-Simons 2-form over S
(rather than over the 8-octahedra tessellation) might give a
different h² coefficient.

**Status.** Speculative; needs a specific Seifert surface and 2-form
choice.

**Pre-screen.** The Borromean rings have a 3-component Seifert
surface of genus 1 (the "triple-twist" surface). Its area depends
on the choice of metric / 2-form normalization. No obvious reason it
gives `−G` over `+0.5`.

**Verdict.** **LOW PRIORITY** — same conceptual layer as Yekutieli
(2-form integration over a different geometric object), inherits the
sign / magnitude ambiguity.

## Path-C priority summary

| Candidate | Verdict | Effort | Why |
|-----------|---------|--------|-----|
| **C1 — Higher-N Wedderburn limit** | TESTABLE | 1 session | Diverges or converges; cheap probe |
| **C3 — KLR / crystal h² correction** | HIGH PRIORITY | Multi-session | Genuinely new categorical layer |
| **C6 — Reading-A as Yekutieli-only** | FORMALIZE AS PATH B | 1 session | Conditional Lean theorem |
| C2 — Twisted Yekutieli | LOW | needs alternative projection | No concrete candidate |
| C4 — Motivic period | DUPLICATE | — | Same as C2 |
| C5 — h²-Faddeev tower | LOW | — | Doesn't yield −G coefficient |
| C7 — Seifert-surface integral | LOW | — | Same layer as Yekutieli |

## Recommended next single-session actions

1. **C1 quick probe** — compute `(1/N) · Σ_{λ ⊢ N} dim_q V_λ` for
   N = 5, 6, 8, 12 at q_0. Check if h² coefficient drifts toward
   `−G` or diverges. Tractable with existing `pyhecke_native.partitions_of` infrastructure.
2. **C6 → Path B Lean conditional** — formalize Reading-A as
   "linking_weight is the Yekutieli per-cell alone" via a `class`
   axiomatisation (§3b-cond conditional-class pattern). Prove
   downstream `m_p < 6 ppm of CODATA` conditional on the class.

C3 (KLR / crystal) is the **highest-value direction** but is
multi-session research; deferred to a follow-up branch unless the
owner directs in-session escalation.

## Cross-references

- [PR #1285](https://github.com/litlfred/qou/pull/1285) — markov_trace mpf precision fix
- [PR #1287](https://github.com/litlfred/qou/pull/1287) — h-expansion + per-partition + redistribution probes
- [PR #1272](https://github.com/litlfred/qou/pull/1272) — γγ̄ decomposition, Reading-A target
- [PR #1276](https://github.com/litlfred/qou/pull/1276) — Bring + Faddeev h⁴ candidate
- [audit 2026-05-22](2026-05-22-yekutieli-percell-conjecture-formalized.md) — Reading B framework canonical
- [audit 2026-05-23](2026-05-23-yekutieli-bijection-natural-reading-negative.md) — natural-reading negative
- [PR #701](https://github.com/litlfred/qou/pull/701) — Wedderburn-search falsification
- AGENTS.md §7b — Type-B folding for bar-invariance
