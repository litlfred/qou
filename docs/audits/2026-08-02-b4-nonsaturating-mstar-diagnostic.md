# The A=4 det-gate magnitude is bracketed by derived constants but supplied by none — scope-(a), 0-fit

**Date:** 2026-08-02 · **Branch:** `claude/j16x-nonsaturating-4body-2026-08-02` ·
**PR:** #4620 · **Bean:** `qou-j16x` ·
**Type:** FINDING — honest negative (scope-(a)) with a sorry-free structural bracket
capstone. Δ_λ closure, Option-E **front 4** (the non-saturating 4-body operator search).
No fit, nothing wired.

- Probe: [`computations/deltalambda/b4_nonsaturating_mstar_diagnostic.py`](../../computations/deltalambda/b4_nonsaturating_mstar_diagnostic.py)
  (witness [`b4-nonsaturating-mstar-diagnostic.witness.json`](../../computations/deltalambda/b4-nonsaturating-mstar-diagnostic.witness.json),
  3/3 assertions, mpmath 50 dps, exit 0).
- Lean: [`content/quantum-observable-universe/lean/QOU/MassTheory/B4NonSaturatingBracket.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/B4NonSaturatingBracket.lean)
  (sorry-free, builds on the merged `A4InterfaceMagnitude`; `lean`-direct exit 0, v4.24.0).

## 0. The question (bean qou-j16x)

PR #4605 established that the **multiplicative** interface cumulant
`b₄ = fourthDiff(E₀·τ_vac·(1−∏f))` supplies only ~6.3 % of the ⁴He `b₄` target because
`(1−∏f)` **saturates**. The surviving gap needs a **non-saturating** connected 4-body
operator. Candidate (1) is the `A4InterfaceMagnitude` one-scalar det-gate. The sibling
already proved (merged, #3924) that

    b₄(m) = −ln det(I + m·S) = −ln[(1 − 5m²)(1 − m²)],   S ⁴He [1⁴] exchange, spectrum {±√5, ±1}

is **surjective** onto (0,∞) in `m ∈ (0, 1/√5)` — so *inverting* the target to pick `m`
is a FIT. **The crux this note settles: can `m` instead be DERIVED — does the required
value coincide (0-fit) with an independently-derived framework constant?**

## 1. Confirmations from the corpus (0-fit)

- **Closed form.** `det(I + m·S) = (1+m√5)(1−m√5)(1+m)(1−m) = (1 − 5m²)(1 − m²)` — confirmed
  against `A4InterfaceMagnitude.detG_eq_spectral_product` / `detG_expand`.
- **Normalization.** The corpus writhe witness `b4-1four-complete-graph-writhe-signs`
  (w_pn=0 row) records `det = 0.563519`, `neg_log_det = 0.573554`, `MeV = 2.400885`, with
  `E0_MeV = 4.1859808`. Since `4.1859808 · 0.573554 = 2.40088`, the canonical det-gate
  normalization is **`MeV = E₀·(−ln det)`**. (The multiplicative-B object of PR #4605 uses
  the *different* scale `E₀·τ_vac ≈ 8.90 MeV` — reported here as an alternative, not the
  det-gate convention.)

## 2. The diagnostic (DIAGNOSTIC-ONLY — `m*` never wired)

Required magnitude to hit `b₄ = 9.243 MeV` under the E₀ norm:
`t* = 9.243/E₀ = 2.20808`, `det* = e^{−t*} = 0.10991`, ⇒
**`m* = √((6 − √(16 + 20·det*))/10) = 0.416421`** (`A4InterfaceMagnitude.uStar` closed
form). This `m*` is an anchor-inversion (a FIT) — it is **never wired**.

**Forward test (the non-inverting direction).** Plug each *derived* constant in AS `m`
(zero inversion) and read off the resulting `b₄` as a fraction of the target:

| derived `m` | value | forward `b₄` (E₀ norm) | % of 9.243 MeV |
|---|---|---:|---:|
| `2h` (Hecke, `h≈0.209060`) | 0.418121 | 9.4797 MeV | **102.56 %** (over) |
| `h/z` | 0.418690 | 9.5620 MeV | **103.45 %** (over) |
| `z − h/2` | 0.394790 | 7.0340 MeV | 76.10 % (under) |
| `1/√5 − h/2` | 0.342683 | 4.2262 MeV | 45.72 % |
| `√(hz)` | 0.323091 | 3.5508 MeV | 38.42 % |
| `h + (q₀−1)` | 0.319039 | 3.4263 MeV | 37.07 % |
| `2h − (q₀−1)` | 0.308142 | 3.1130 MeV | 33.68 % |
| `z − h` | 0.290260 | 2.6577 MeV | 28.75 % |

(The naive uniform `z ≈ 0.4993` is already `A4InterfaceMagnitude`-excluded: `5z² > 1` ⇒
`det < 0`, unphysical, scope-(b).)

## 3. Verdict — scope-(a), no derived `m`

The required `m* = 0.416421` is **bracketed** by derived constants — `2h` and `h/z`
overshoot by 2.6 % / 3.5 %, and the next-nearest (`z − h/2`) and everything below
undershoot by ≥ 24 % — but is supplied by **none** to framework precision. The nearest,
`2h`, is off by **0.41 % in `m`** (**2.56 % forward**), i.e. ~10⁷× the L1 compute floor
(10⁻¹⁵). Per the c_k truncation-order / near-match discipline
([`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)),
a 2.6 % "near-match" of `2h` is **fitted-adjacent, not an identity**; it is not wired and
not claimed as canonical.

> **VERDICT: scope-(a) fit-needed.** The det-gate magnitude `m` is open. No identified
> categorical driver fixes it; the required value sits in the open interval between the
> two nearest derived constants (`z − h/2` below, `2h` above), matching neither. This
> sharpens `A4InterfaceMagnitude`'s one-scalar WALL with the concrete required value +
> the bracketing derived constants.

**Surviving sub-question.** Is there a categorical principle producing a per-pair bond
magnitude in the narrow band `(z − h/2, 2h) ≈ (0.395, 0.418)` — strictly below the naive
`z` and above the bar-even projection — that lands at `0.41642`? The `2h`/`h/z` proximity
(both ~2.6–3.5 % over) is suggestive of a *bar-odd-doubled* amplitude but is not derived;
it is recorded as a near-coincidence to test, not a lead to wire.

## 4. What the Lean adds (sorry-free, structural)

Built on the merged `A4InterfaceMagnitude` (surjectivity + strict monotonicity + `detG`
closed form), `B4NonSaturatingBracket.lean` proves the generic bracket-and-uniqueness
content of the finding — the numerics stay in the witness:

- **`required_magnitude_strictly_bracketed`** — for a positive target `t` and physical
  `c_lo < c_hi` with `b₄ c_lo < t < b₄ c_hi`, the unique `m` with `b₄ m = t` lies strictly
  in `(c_lo, c_hi)`.
- **`no_endpoint_reproduces_target`** — hence `b₄ c_lo ≠ t` and `b₄ c_hi ≠ t`.
- **`detGate_no_endpoint_hits`** — the det-space form (target determinant `D` straddled).
- **`a4_magnitude_bracketed_scope_a`** — capstone packaging both, parametrised by the
  witness-supplied straddle `c_lo = z−h/2`, `c_hi = 2h`, `t* = 9.243/E₀` (numerically
  `b₄(z−h/2) ≈ 1.681 < 2.208 < 2.265 ≈ b₄(2h)`).

**Discipline.** `m*` is a fit and never wired; the forward direction plugs derived
constants in with zero inversion. B_AME/targets diagnostic-only; `free_parameters = 0`.
Nothing wired. Bean `qou-j16x` records the verdict + the surviving sub-question.
