# Q_β c_k ladder — is it a cyclotomic-in-q Habiro element? (NEGATIVE)

**Date:** 2026-06-17
**Status:** RESOLVED — clean negative result.
**Verdict:** The Q_β precision-ladder `c_k` are **NOT** a clean cyclotomic-in-q
Habiro element. The documented "Q_β Habiro element permanent fix" is **not
viable** as a real-q integral (or even cyclotomically-localised) element.
**Compute:**
[`computations/probes/qbeta_habiro_cyclotomic_probe.py`](../../computations/probes/qbeta_habiro_cyclotomic_probe.py)
→ [`qbeta-habiro-cyclotomic.witness.json`](../../computations/qbeta-habiro-cyclotomic.witness.json)
(EXACT symbolic over ℚ(q), sympy — no floats in the algebra, no fitting).

---

## What was tested

The q-side analogue of this session's **z-Habiro machinery**
([`z_habiro_increment_probe.py`](../../computations/probes/z_habiro_increment_probe.py),
Lean [`QOU.MassEndomorphism.ZHabiroCauchy`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/ZHabiroCauchy.lean)).
The z-probe tested whether the quantum dilogarithm `Φ_q(z) = ∏(1−q^{-k}z)^{-1}`
admits a cyclotomic-in-z expansion `Σ_n c_n(q) P_n(q,z)` (verdict: exists, c_n in
a cyclotomic localisation, not ℤ[q^±1]).

This probe applies the **same exact triangular base-change + integrality test**
to the Q_β precision-ladder coefficients of

$$\mathfrak{Q}_\beta(q) \;=\; \mathfrak{Q}_{\text{base}}(q)\cdot\prod_{k\ge 2}\bigl(1 + c_k\,u^k\bigr),\qquad u = b\,\hbar_q^2,$$

asking whether the `c_k` sequence is a fibre-level **q-Habiro element**
`Σ_n a_n (q;q)_n` with `(q;q)_n = ∏_{j=1}^n (1−q^j)` and `a_n ∈ ℤ[q^±1]` — the
"permanent fix" parallel to the α_EM Habiro element `[2]_q·(1−h²α)` (PR #1511,
merged).

Per AGENTS.md §"Im(q) at fibre vs observable level", the question is **not**
"is there a real formula `c_3 = f(q_0_real)`?" (already refuted —
`dc_3/dq ≈ 4.6e6`), but whether the `c_k` admit an integral cyclotomic-in-q
expansion at the fibre level.

## The c_k values used (registry §3, exact symbolic)

Substrate q-rational: `b²(q) = (q⁴+q²+1)/(q²+1)²` (bar-symmetric per
[`qbeta_bar_even_kernel_invariant_probe.py`](../../computations/qbeta/qbeta_bar_even_kernel_invariant_probe.py)).
This is **rational in q but already NOT Laurent** — it carries the cyclotomic
denominator `(q²+1)²`.

| k | canonical form (registry §3) | tier |
|---|---|---|
| 2 | `−1` | CANONICAL (Taylor-exact, anchor-stable, Lean-proved) |
| 3 | `−2.06934…` @ proton q₀ (cands `J_Hopf(q=1)=−2`, `J−ℏ_q²`) | EMPIRICAL — **refuted** as real-q element |
| 4 | `c_3·b⁴` | EMPIRICAL — CODATA fit/artifact |
| 5 | `−(b²+½)` | EMPIRICAL — outlier |
| 6 | `c_3²·b² = 4b²` | imposed (self-consistent) |
| 7 | `c_3³ = −8` | imposed |
| 8 | `c_3²·b⁴ = 4b⁴` | **first free rung — pattern breaks** |
| 9 | `c_3³·b² = −8b²` | silver-anchored |
| 10 | `c_3²·b⁶ = 4b⁶` | silver-anchored |

Sources:
[`qbeta-ck-cache.witness.json`](../../computations/qbeta/qbeta-ck-cache.witness.json)
(c_2, c_3 numeric),
[`ck-dk-canonical-registry.md §3`](../coordination/ck-dk-canonical-registry.md)
(canonical forms + tiers),
[`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
(the "permanent fix" framing).

## Result — two experiments, both exact over ℚ(q)

### EXPERIMENT 1 — the b²-backbone (c_3 → −2 integer surrogate)

Substituting the documented integer surrogate `c_3 → −2` (its J_Hopf(q=1) value),
every `c_k≥4` form becomes a clean q-rational `P_k(b²(q))`. The cyclotomic
`(q;q)_n` triangular base-change **reconstructs the generating polynomial
exactly** (residual = 0), but:

- **all `a_n` are rational in q** (✓), yet
- **NO `a_n` is integral ℤ[q^±1]** — the first non-integral coefficient is `a_2`,
  and every `a_n` carries the cyclotomic denominator inherited from `b²(q)`'s
  `(q²+1)` factor.

**EXP-1 verdict: `backbone-localised`** — the b²-backbone lives in the cyclotomic
**localisation** of ℤ[q^±1] at `(q²+1)`, not the integral Habiro ring. (This
exactly parallels the z-probe's `cauchy-limit-exists-localised`: an expansion
exists over ℚ(q) but integrality fails at the cyclotomic poles.)

### EXPERIMENT 2 — the binding obstruction: c_3 has no clean q-rational

The c_3 rung is the **seed** of every higher canonical form (c_4..c_10 are all
polynomials in c_3 and b²). But c_3 is **refuted as a real-q element**: its best
real-q candidates (`J_Hopf(q=1)=−2`, `J−ℏ_q²`) miss the proton-q₀ value by
3.35% / 2.88%, are anchor-**rigid** (`dc_3/dq ≈ 4.6e6`), and swing 2.88% across
the proton↔muon anchors (falsification audit
[`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)).

A genuine **integral** q-Habiro element requires every coefficient — the c_3
seed most of all — to be an element of ℤ[q^±1] (or its cyclotomic localisation).
c_3 fails this at the **rational-function level**: there is no clean `c_3(q) ∈ ℚ(q)`
to expand in the first place.

## Overall verdict — `refuted-c3-not-q-rational`

The Q_β c_k ladder is **NOT** a cyclotomic-in-q Habiro element, on two
independent grounds:

1. **c_3 has no q-rational representative** (refuted, anchor-rigid) — so the
   ladder cannot live in ℤ[q^±1] or its localisation at all.
2. Even granting the `c_3 → −2` integer surrogate, the b²-backbone sits in the
   cyclotomic **localisation** at `(q²+1)`, not the integral Habiro ring.

**Is the "Q_β Habiro element permanent fix" viable?** Not as a real-q
element. This probe (and the z-Habiro machinery it mirrors) can certify exactly
the class of real-q rational / Laurent / cyclotomically-localised elements — and
the Q_β c_k are not in it. Consistent with AGENTS.md §"Im(q) at fibre vs
observable level": **if** a genuine fibre-level Q_β Habiro element exists, it
must be **complex-analytic / root-of-unity**, not a real-q rational element. The
real-q "permanent fix" hypothesis is refuted; the complex-fibre route is neither
confirmed nor refuted here (out of scope of an exact-ℚ(q) probe).

## No Lean

Per the task honesty directive: the math result (a negative) is the deliverable.
No Lean theorem is forced — there is no positive cyclotomic-integral structure to
formalise (unlike the z-side, where `cyclotomicPartialSum_isCauchy` had a real
integral increment to prove). Forcing a Lean `: True` stub would violate the
no-shadowing-stubs rule (AGENTS.md §"No shadowing stubs").

## Relation to prior c_k work (no duplication)

- This is the **q-Habiro-element / cyclotomic-localisation** angle specifically —
  distinct from `qbeta_habiro_element_probe.py` (which tested **product ansätze**
  `[2]_q·(1−h²c)` for the Taylor coefficients, NEGATIVE) and from the c_3
  cross-anchor rigidity falsification (which tested **real-q closed forms**).
- It **confirms** the registry §8 flip-flop guard from a new direction: the c_k≥3
  are empirical, and there is no integral cyclotomic-in-q element to promote them
  to canonical. Does **not** change production (Q_β remains c_2-only).

## Cross-references

- z-side analogue: [`z_habiro_increment_probe.py`](../../computations/probes/z_habiro_increment_probe.py),
  [`ZHabiroCauchy.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/ZHabiroCauchy.lean)
- Registry: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
- Canonical framing: [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- c_3 falsification: [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)
- α_EM Habiro precedent: PR #1511 (merged)
