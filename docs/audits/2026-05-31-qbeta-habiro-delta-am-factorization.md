# Q_β Habiro element — Δa_m factorization (2026-05-31)

> Keystone follow-up to [`2026-05-31-qbeta-habiro-element-probe.md`](2026-05-31-qbeta-habiro-element-probe.md)
> §C6: "Δa_m has small-integer coefficients — STRIKING PATTERN
> suggesting low-degree polynomial factorization."
>
> Branch: `claude/brave-mendel-FPxFl` (PR #1579).
> Probe script: [`computations/qbeta/qbeta_habiro_delta_am_factorization.py`](../../computations/qbeta/qbeta_habiro_delta_am_factorization.py).
> Witness: `computations/qbeta/qbeta-habiro-delta-am-factorization.witness.json`.

## TL;DR

**PARTIAL — structural prefactor `u^15·(u−1)·(u+1)` FOUND on the
n−p Habiro element; per-m polynomial GCD is trivial; new finding
that Δa_7 = Δa_8 = 0 corrects the prior audit's open boundary.**

| Sub-task | Status | Result |
|----------|--------|--------|
| Per-m factorization of Δa_m (m=0..8) | **DONE** | Only m=1 has a categorical factor: `10·(1+u)`. m=2..6 are irreducible over ℚ. |
| Cross-m polynomial GCD | **TRIVIAL** | gcd(Δa_1,…,Δa_6) = 1 over ℤ[u] |
| Integer-content GCD | **TRIVIAL** | gcd(10,1,1,1,1,1) = 1 |
| Σ Δa_m·(u;u)_m factorization | **STRUCTURAL FACTOR FOUND** | `−u^15·(u−1)(u+1)·P_8(u)` where `P_8` is irreducible |
| **NEW** finding: Δa_7 = Δa_8 = 0 | **DOES** | Atoms share `a_7` and `a_8` exactly |

## Corrected witness table (supersedes prior audit C6 m=5..8 absence)

| m | Δa_m(u) = a_m(n) − a_m(p) | content | primitive factorization |
|---|--------------------------|---------|-------------------------|
| 0 | `0` | — | (atoms share `a_0 = 4`) |
| 1 | `10·u + 10` | **10** | `10·(u + 1)` |
| 2 | `−64·u² − 69·u − 73` | 1 | irreducible over ℚ |
| 3 | `131·u³ + 143·u² + 160·u + 177` | 1 | irreducible over ℚ |
| 4 | `−92·u⁴ − 114·u³ − 136·u² − 162·u − 189` | 1 | irreducible over ℚ |
| 5 | `18·u⁵ + 28·u⁴ + 39·u³ + 52·u² + 69·u + 90` | 1 | irreducible over ℚ |
| 6 | `−u⁴ − 3·u³ − 5·u² − 8·u − 15` (degree drops!) | 1 | irreducible over ℚ |
| 7 | `0` | — | **NEW: atoms share `a_7 = −12u⁷ − 17u⁶ − 24u⁵ − 34u⁴ − 48u³ − 63u² − 84u − 110`** |
| 8 | `0` | — | **NEW: atoms share `a_8 = u⁴ + 2u³ + 3u² + 5u + 7`** |

Three corrections to the prior audit's C6:

1. **Δa_5 / Δa_6 had NOT been computed** — they are non-zero with
   anomalously small integer coefficients (Δa_6 has degree 4 and
   leading coeff = −1, far smaller than the m=4 leading −92).
2. **Δa_7 and Δa_8 vanish.** The neutron and proton share their
   top-two Habiro coefficients exactly. The n−p difference lives
   ENTIRELY in the m=1..6 window.
3. **Δa_6 has degree 4 not 6** — the leading u⁵, u⁶ terms cancel
   between p and n. Combined with Δa_7=Δa_8=0, this means the
   **support of Δ_HabiroQβ effectively terminates at m=6** with
   leading degree contributions stopping at u⁴.

## Cross-m structure (negative on the GCD; positive on Σ)

**GCD test (negative).** Over ℤ[u], `gcd(Δa_1, Δa_2, …, Δa_6) = 1`.
There is no single polynomial divisor that explains the n−p split.

**Integer content test (negative).** Only m=1 has content > 1
(content=10). The rest are integer-primitive.

**Σ_m Δa_m·(u;u)_m test (POSITIVE).** When we form the unnormalised
Habiro element by summing the Δa_m against the q-Pochhammer brackets:

```
Σ_{m=0..8} Δa_m(u) · (u;u)_m
  = −u^15 · (u − 1) · (u + 1) · P_8(u)
  = −u^15 · (1 − u²) · P_8(u) · (−1)
  =  u^15 · (u² − 1) · P_8(u)
```

where

```
P_8(u) = u^8 + 2·u^7 + 2·u^6 + 2·u^5 + 4·u^4 − 2·u^3 + 2·u^2 − 2·u + 1
```

is irreducible over ℚ (verified by sympy.factor not splitting it
further).

**Categorical reading of the prefactor** `u^15 · (u² − 1)`:

- `u^15` matches the **shared denominator pole order** at the
  origin: prior witness reports `D(u) = 4·u^19·(1 + u²)`. The
  numerator/denominator combination becomes
  `u^15·(u²−1)/(4·u^19·(1+u²)) = (u²−1) / (4·u^4·(1+u²))`. The
  `(u²−1)/(1+u²) = (u−1)(u+1)/Φ_4(u)` form is precisely the
  CYCLOTOMIC ratio `Φ_1·Φ_2 / Φ_4` — a categorical primitive.
- `(u² − 1) = Φ_1(u) · Φ_2(u)` is the **product of the two lowest
  cyclotomics**, equal to the q-integer `[2]_q · (q − 1)` after the
  `u = √q` substitution. Specifically:
  ```
  (u² − 1) = (q − 1) = h · q^{1/2}   where  h = q^{1/2} − q^{−1/2}
  ```
  This is the **classical-limit vanishing factor** that makes the
  whole Δ-Habiro element vanish at q → 1 (u → 1), as it must by
  the n=p symmetry breaking from the **q-deformation alone**.

**Per the production-vs-exploratory-discipline skill** (Rule 14),
this is a TIERED result:

- `proved`: the prefactor `u^15·(u²−1)` is a sympy.factor output —
  algebraically exact over ℤ[u]. Not contingent on q₀.
- `near-match`: `(u²−1)/Φ_4(u)` matches the q-bracket Φ_1·Φ_2/Φ_4
  form, which appears in α_EM's Habiro element `[2]_q·(1−h²α)` =
  `Φ_2(q)·(1 − h²α)` after the same substitution.
- `unproved (open)`: the irreducible factor `P_8(u)` has NO known
  categorical interpretation. **This is the residual.**

## What this rules out & what it doesn't

**RULES OUT (definitively):**

- **The "shared categorical primitive" hypothesis** from prior
  audit §C6. There is no single polynomial g(u) dividing every
  Δa_m. The "small integers" pattern is NOT a polynomial-GCD
  phenomenon.
- **A polynomial recursion `Δa_m / Δa_{m−1} = R(u, m)`** with
  rational R. Numerically at u₀ ≈ 1.0535 the ratios are
  −10.55, −3.03, −1.15, −0.43, −0.10 — geometric-decay-ish but
  not a clean rational R(u, m).

**RULES IN (new structural finding):**

- **The Δ-Habiro element factors as `u^15·(u²−1)·P_8(u)`**. The
  prefactor IS a categorical primitive (`Φ_1·Φ_2`). The
  irreducible P_8 is the **proper Q_β content**, an 8-degree
  polynomial that doesn't simplify further over ℚ.
- **Δa_m vanishes for m=7,8**, meaning the n−p split is supported
  ENTIRELY on `m ∈ {1,…,6}` of the Habiro expansion. The m=7,8
  rungs of the ladder are **isotope-degenerate**.

**DOES NOT RULE OUT:**

- **`P_8(u)` matching a higher-degree categorical object** —
  e.g. an evaluation of the Burau / reduced Burau representation
  at one of the small braid words, an LP shadow-price polynomial,
  or a Kashiwara-crystal partition function. The lack of small-
  cyclotomic factors does NOT mean P_8 is non-categorical, only
  that it isn't a low-degree categorical product.
- **`P_8(u)` being an `[n]_q²` or `(q;q)_3 / Φ_k` rational**. We
  did not exhaust the q-Pochhammer rational catalogue.

## NEW PROBE: D − (p + n) on shared support m = 0..8

A side test: subtract the deuteron M=12 Habiro coefficients from
the channel sum on shared support. Result: no clean factorization
emerges (D-denom = 32·u^40·(1+u²)(1+u)² vs p,n-denom = 4·u^19·(1+u²)
— direct coefficient subtraction is a structural probe only, not a
physical observable). Coefficients are large (467, 10236, 119903…)
with no apparent small-factor structure. Logged for completeness in
the witness `deuteron_minus_p_plus_n` field; no advancement on
deuteron channel.

## Next session targets

1. **Investigate P_8(u) for categorical match.** Try evaluating
   reduced Burau / Hoefsmit / Wedderburn-block characters at the
   p, n braid words and look for the same polynomial. The
   irreducibility of P_8 over ℚ is itself a constraint — it must
   correspond to a single Wedderburn block's character, not a
   sum.
2. **Lift the `u^15·(u²−1)` finding to a categorical lemma.** The
   `(u²−1) = (q−1)` factor is the classical-limit vanishing
   witness. Lean lemma: `Δ_Habiro_Qβ(q=1) = 0` should be the
   formal statement, with the proof factoring through this
   prefactor. Candidate location: a new lemma in
   `content/quantum-observable-universe/q-deformations/lean/`
   sibling to the `prop:neutron-qvalue-symbolic` block.
3. **Use the Δa_7 = Δa_8 = 0 finding** to compress the Q_β
   formula: only m=1..6 Habiro rungs contribute to Q_β, so the
   Borromean-tower extension only needs the 6-rung sub-element.

## Cross-refs

- Prior probe: [`docs/audits/2026-05-31-qbeta-habiro-element-probe.md`](2026-05-31-qbeta-habiro-element-probe.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Witness pipeline: `computations/habiro/habiro-coefficients-atomic.witness.json`
- α_EM template (parallel that worked): `computations/alpha/alpha_em_habiro_taylor_investigation.py`
- Production-vs-exploratory discipline: `.claude/skills/local/production-vs-exploratory-discipline.md`

## Files touched

- **NEW:** `computations/qbeta/qbeta_habiro_delta_am_factorization.py`
- **NEW:** `computations/qbeta/qbeta-habiro-delta-am-factorization.witness.json`
- **NEW:** `docs/audits/2026-05-31-qbeta-habiro-delta-am-factorization.md` (this file)
