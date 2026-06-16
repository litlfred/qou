# Q_β eigenphase Taylor-in-u — "eigenphase = f" falsified at u¹

**Date:** 2026-06-01
**Probe:** [`qbeta_eigenphase_taylor_in_u.py`](../../computations/qbeta/qbeta_eigenphase_taylor_in_u.py)
→ `qbeta-eigenphase-taylor-in-u.witness.json`
**Goal arm:** 1ppQ-Q_β (`docs/coordination/1ppq-qbeta.md`)
**Probe claim:** `probe-qbeta-habiro-element-search` sub-attack — derive the
scaling map `f` directly (the target sharpened by PR #1593's order audit).
**Status:** characterization (no closure). **Negative-but-informative:**
falsifies the "cos eigenphase IS the scaling map f" hypothesis at order u¹.

---

## TL;DR

The N=1 cos eigenphase `cos(α − b·ℏ²/2)` — the unique right-direction
closed-form scaling from the bridge-narrowing audit — Taylor-expands in
`u = b·ℏ²` with a **nonzero u¹ coefficient `a_1 = -√3/12`**. The Q_β
ladder `Π(1 + c_k u^k)` has **no u¹ rung** (it starts at `c_2 u²`).
Therefore the cos eigenphase is **not, by itself, the `c_k` generating
factor** — it carries an odd-order correction the ladder lacks. The
"eigenphase = f" hypothesis is falsified at u¹.

## What was computed (dual infrastructure)

The probe keeps **both** a symbolic-exact path and a fast numeric path,
sharing one exact symbolic ε = (q−1) series; they cross-check:

| order | symbolic-exact (radicals) | numeric (mpmath, 70 dps) | agree |
|---|---|---|---|
| `u⁰` | `1` | `1.000000000000` | ✓ |
| `u¹` | `-√3/12` | `-0.144337567297` | ✓ |
| `u²` | `-11/32 - √3/12` | `-0.488087567297` | ✓ |
| `u³` | (numeric) | `-0.468215502976` | — |

(The symbolic path is capped at low order — the exact series reversion is
expensive — and is kept for later verification; the numeric path covers
the full range. See "compute note" below.)

## The finding

- The eigenphase additive u-series is `N1 = 1 - (√3/12) u - (11/32 +
  √3/12) u² - …`. The **u¹ term is nonzero**.
- The Q_β ladder is `Q_β/Q_base = Π_{k≥2}(1 + c_k u^k)` — first rung at
  `u²`, no `c_1`.
- Symptom in the q₀-anchor table: `(N1−1)/u² ≈ -22` (not the empirical
  `c_2 = -1`), because `(N1−1) ~ a_1·u`, so `/u² ~ a_1/u ≈ -0.144/0.0085`.

So the cos eigenphase is a right-**direction** part of the scaling, but
**not** the generating factor for the `c_k`.

## What this rules out, and the sharpened constraint on f

- **Ruled out:** "the cos eigenphase IS the scaling map f, and the `c_k`
  are its Taylor coefficients." Falsified at u¹.
- **New constraint on f:** the true scaling map must (a) **cancel the u¹
  term** `-√3/12` that the bare eigenphase carries, and (b) supply the
  `u²` coefficient `= -1` (the proved `c_2`) exactly. The u¹ cancellation
  is the concrete new structural requirement — it points at a *paired*
  or *bar-symmetric* construction (an odd-order term cancelling against a
  partner), consistent with the multi-Wedderburn-block picture from the
  order audit (PR #1593).

## What IS provable (Lean, PR #1602)

The full Taylor-coefficient identities need a power-series development;
the **base-point lemmas** (the `u → 0`, `q = 1` limit) are sorry-free
Lean and anchor the probe:

- `hbarQ_one : hbarQ' 1 = 0`, `heckeH_one : heckeH' 1 = 0`,
  `markovZ_one : markovZ' 1 = 1/2`, `alpha_one : alpha 1 = 0`.
- `hoefsmitB_one : hoefsmitB 1 = √3/2` — the value that sets
  `a_1 = -hoefsmitB(1)/6 = -√3/12`.
- `N1_factor_one : N1_factor 1 = 1` — the `u⁰ = 1` coefficient.

The `c_k≥3` remain `§3b-cond` conditional classes with **no instances**
(unchanged) — there is still no derived `f`, so no `c_3` theorem.

## Discipline

Tiered: eigenphase = proved closed form; "eigenphase = f" = **falsified
at u¹** (this probe); `c_k≥3` = open. **No fitted form proposed.** The
result narrows the search (adds the u¹-cancellation constraint), it does
not close it.

## Compute note (symbolic blow-up)

Expanding `cos(arg)` directly with `sympy.series` to high order blows up:
`cos_x.subs(x, arg_eps)` substitutes the ~9-term ε-polynomial `arg_eps`
into the cosine Maclaurin terms `x², x⁴, x⁶, x⁸`, producing multinomial
expansions of `(Σ₉ aᵢεⁱ)ⁿ` over an exact radical field (≈ 45, 495, 3000,
12000 intermediate terms before truncation), each coefficient a nested
radical SymPy tries to simplify exactly. Cost grows super-linearly in the
truncation order `K`. The probe therefore (a) expands the **argument**
in ε first (cheap), applies the cosine series to the truncated polynomial,
and (b) does the series reversion `u(ε) → ε(√u)` **numerically** in
mpmath. The symbolic-exact path is retained at low order for verification.

## Cross-references

- Order audit (the sharpened target): [`2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md)
- Bridge narrowing (eigenphase = right-direction scaling): [`2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md)
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Lean: `content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.lean` (base-point lemmas, PR #1602)
