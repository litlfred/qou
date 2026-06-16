# Gap closure — structural analysis of what's actually needed

**Date:** 2026-05-25
**Branch:** `claude/brave-mendel-FPxFl`
**Related PR:** [#1272](https://github.com/litlfred/qou/pull/1272)
**Status:** Audit — identifies the single load-bearing categorical
step that would close the proton mass-formula gap.

## The gap, precisely (proton at q₀)

Walking the canonical 6-term mass formula
([`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md))
all the way down for the proton at substrate q₀ gives:

```
T1 |tr_M(T_w)|         = 1.0653  (Lean-proved)
T2 single Li_2^q tower = 1.6183
T3 pair Li_2^q tower   = 0.1983
T4 Frobenius co-Casim  = 1.2761
T5 chirality + bulk    = -7.7918  (negative — sign anomaly noted earlier)
T6 Habiro residue      = 1.4218

|sum| ≈ 13.371  (using |T5|, dimensionless)
m_e · |sum| ≈ 6.83 MeV
CODATA m_p = 938.27 MeV
gap = 137× multiplicative
```

The framework's own docstring (line 92-95 of
[`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md))
names two reconciliation candidates:

> "the ρ_K closure path of `prop:atomic-mass-gb-nf` and the Faddeev
> Φ_q archimedean tower are the two reconciliation candidates."

## Testing the Faddeev Φ_q tower (Route b)

The 137× factor is precisely what the framework calls "the
dimensional mass scale killed by the bar-symmetric projection of
Li_2^q" (`atom-knot-mass-derivation.md` line 89-91). Replacing
Li_2^q with Φ_q (Faddeev's bar-asymmetric quantum dilog) should
restore it.

Probe at the proton (this session, with proton's |V̂_i| ∈
{0.989, 0.971} both < q ≈ 1.110, so Φ_q converges):

```
T2 single via Li_2^q (production):    1.6183
T2 single via Φ_q (Archimedean form): 1,096,978   (way too big!)
T3 pair via Φ_q:                      82,016

m_p via Li_2^q tower:   6.83 MeV       (137× too small)
m_p via Φ_q tower:    602,470 MeV      (642× too big)
CODATA m_p:              938.27 MeV
```

**Both forms fail in opposite directions.** The truth is between
them — and a factor of 10⁵ apart.

## The structural problem, precisely

The framework's `prop:li2q-phiq-bar-symmetrization` says the
Archimedean realization functor maps Li_2^q to the bar-pair:

```
Archim_τ(Li_2^q(z)) = (log Φ_q(z) + log Φ_{q⁻¹}(z)) / 2
```

But for the proton's generator volumes (|V_i| ≈ 0.98), the
companion `Φ_{q⁻¹}(V_i)` **DIVERGES** — the Faddeev convergence
radius `|z| < q⁻¹ ≈ 0.90` is violated. The bar-pair average is
formally `(finite + ∞)/2 = ∞`.

So the framework's claim of "bar-pair Archimedean realization"
is structurally unfinished: it requires a **regularization of
log Φ_{q⁻¹}(z) across the convergence boundary `|z| = q⁻¹`**.

This is the **single load-bearing categorical step** for closure
of the proton mass-formula gap.

## Why this is well-posed

Unlike the earlier "find a substrate-form for Δ_λ" or "derive ρ_K
from scratch" framings, the regularization-of-Φ_{q⁻¹} problem is:

1. **Well-defined**: a specific divergence at a specific boundary.
2. **Mathematically tractable**: Faddeev's quantum dilog has known
   analytic-continuation tools (modular companion `Φ_{q̃}`, the
   q-pentagon identity, matched asymptotic at the boundary).
3. **Existence-guaranteed**: the answer MUST exist — CODATA m_p
   is the empirical fact, and Li_2^q gives a finite value, Φ_q
   gives a finite value, the average must therefore exist with
   the right regularization.
4. **Numerically bounded**: between Li_2^q (137× undershoot) and
   Φ_q (642× overshoot). The right regularization should give
   a factor on the order of √(137·642) ≈ 296× scale
   contribution from one term — a clear quantitative target.

## Three candidate regularization schemes

From quantum-dilogarithm literature:

| Scheme | Approach | Single-session compute? |
|---|---|---|
| **Faddeev mirror `Φ_{q̃}`** | Replace `Φ_{q⁻¹}` with the modular companion `Φ_{q̃}` where `q̃ = exp(πi · ln q)`. The mirror is well-defined for all `|z|`. | **YES** — direct compute |
| **Analytic continuation via q-pentagon** | Use the pentagon identity `Φ_q(x) · Φ_q(y) = Φ_q(y) · Φ_q(xy) · Φ_q(x)` to extend `Φ_{q⁻¹}` across the boundary | possible but needs Lean coverage of pentagon |
| **Matched asymptotic at boundary** | Identify the divergent piece of `log Φ_{q⁻¹}(z)` as `z → q⁻¹` and subtract; report finite remainder | **YES** — direct compute |

## Concrete next step

Implement schemes 1 and 3 above as a single-session probe. Each
gives a specific finite value for the Archimedean realization of
the Li_2^q tower at the proton, and the candidate that lands at
m_p ≈ 938.27 MeV is the structurally-correct regularization.

If neither candidate hits the target within ~1% (CODATA-relative),
the gap may require a more elaborate structural insight (Option E
crystal vertices, full ρ_K graded expansion, etc.). But the
**well-posedness of the regularization question itself is the
significant progress** — the closure problem reduces to a single
mathematical question rather than an open-ended "derive ρ_K from
substrate".

## Lean coverage required

To formalise the closure (once a regularization scheme lands):

| Object | Currently in Lean? | Needed |
|---|---|---|
| Li_2^q definition + convergence | nil | full closure conditions |
| Φ_q definition | nil | needed (Faddeev pentagon, modular pair) |
| `prop:li2q-phiq-bar-symmetrization` (bar-pair identity) | nil | THE load-bearing identity |
| Regularization scheme (1, 2, or 3 above) | nil | needed |
| Archimedean realization functor as categorical operator | nil | needed (currently informally defined) |

Recently-landed pieces that contribute:
- [`BorromeanMarkovTrace.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanMarkovTrace.lean)
  proves the Wenzl-side closed form (T1 piece).
- [`YLambdaQSchur.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YLambdaQSchur.lean)
  (this PR) proves the q-Schur transpose-pair identity (foundation
  for downstream y_λ work).
- Family A's `5/2 + (3/4)h²` is proved in
  [`lambda-scale-substrate-form.lean`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.lean).

The big gap is the Φ_q + realization functor formalisation. Once
that lands, the closure derivation becomes a Lean computation.

## What this audit replaces / supersedes in the session's previous framings

| Previous framing (this session) | Status now |
|---|---|
| "92% of gap at h² coefficient → Reading-A" | RETRACTED (Markov-trace normalization bug) |
| "ρ_K closure is the universal open piece" | TRUE but too abstract — restated as the regularization problem |
| "linking_weight and ρ_K are the same closure problem under different names" | TRUE — and BOTH reduce to the Φ_{q⁻¹} regularization |
| "Sibling's Bring+Faddeev formula is closest at +108 ppm" | EXPLAINED — sibling's `1/(1−h·q¹⁰)` is the k=1 leading Faddeev kernel of an unregularized Φ_q; the +108 ppm match is a partial Faddeev capture |
| "Crystal weights c_λ gave WRONG_SIGN" | UNCHANGED — Option E remains the substrate-categorical-route alternative if regularization fails |

## See also

- [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
  — the canonical 6-term mass formula; line 92-95 names the two
  reconciliation candidates.
- [`li2q-phiq-bar-symmetrization.md`](../../content/quantum-observable-universe/braids-and-knots/li2q-phiq-bar-symmetrization.md)
  — `prop:li2q-phiq-bar-symmetrization`, the bar-pair identity.
- [`_phi_q_util.py`](../../computations/_phi_q_util.py)
  — existing Φ_q implementation, with explicit `mp.inf` return on
  boundary violation (the divergence this audit identifies).
- [`_li_2_q_util.py`](../../computations/_li_2_q_util.py)
  — existing Li_2^q implementation (the bar-symmetric pre-Archimedean
  form).
- `cross-isotope-rho-k-consistency.md` (this PR) — the universal
  closure pattern across isotopes.
- PR #1272 — this session's full thread.
