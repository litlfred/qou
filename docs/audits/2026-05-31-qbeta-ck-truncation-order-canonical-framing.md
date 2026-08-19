# Q_β c_k — truncation-order canonical framing (READ FIRST before any c_k wire/un-wire)

> **⮕ SUPERSEDED for status.** The authoritative c_k / d_k canonical-vs-empirical
> status now lives in the single registry
> [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md).
> This doc is retained for its truncation-order framing detail; for the current
> per-rung tier + wiring, read the registry.

**Date:** 2026-05-31
**Status:** CANONICAL — supersedes the binary "wire vs drop c_k" framing
in all prior Q_β c_k audits.
**Compute reference:**
[`qbeta_ck_truncation_order_analysis.py`](../../computations/qbeta/qbeta_ck_truncation_order_analysis.py)
→ `qbeta-ck-truncation-order-analysis.witness.json`.

---

## Why this doc exists — the four-session flip-flop

The Q_β categorical precision ladder

$$Q_\beta(q) \;=\; Q_{\text{base}} \cdot \prod_{k\geq 2}\bigl(1 + c_k\,u^k\bigr),
\qquad u = b\,\hbar_q^2 \approx 0.00852$$

has been **wired and un-wired four times**:

| session | action | result |
|---|---|---|
| #1452 | wired `c_3 = J_Hopf(q=1) = -2` | dashboard claimed Q_β beats 100× |
| #1479 | reverted to `c_2`-only | dashboard Q_β = 1279 ppb (159× miss) |
| deep-audit body (#1479) | re-proposed wiring `c_3 = J−ℏ_q²` | "0.004% match!" |
| deep-audit **addendum** | retracted (the **4th flip-flop**) | "stale-q₀ artifact" |

The flip-flop happens because **two true facts were conflated into one
binary decision**:

- **FACT A** (wiring camp): N=3 **does** beat the experimental 100×
  target — residual +6.0 ppb < 7.8 ppb. ✓
- **FACT B** (discipline camp): `c_3 = -2` is **not** a Taylor-EXACT
  derivation — it is a q₀-dependent near-match (−2.0097 at muon-pin q₀,
  −2.0693 at m_p-pin q₀ — a 3.47% m_p-pin swing, 2.98% cross-anchor
  swing per the probe's Part D). ✓

> **⚠ CORRECTION 2026-08-16 — the three percentages in FACT B are computed
> against a SUPERSEDED muon `c_3`, and the conclusion is unaffected.** This
> doc's "−2.0097 at muon-pin q₀" has since been re-extracted as
> **−2.02020024** (registry §9g; reproduced independently by
> [`qbeta_c3_crossanchor_swing_provenance_probe.py`](../../computations/qbeta/qbeta_c3_crossanchor_swing_provenance_probe.py),
> 3/3 assertions). Against the current anchor pair the **cross-anchor swing is
> 2.3748 %** (proton-normalised) or 2.4571 % (normalised by the candidate
> `−2`) — **not 2.98 %**. Two further notes, because both are traps this doc's
> readers keep hitting:
>
> - The corpus's **2.98 % and 2.88 %** are the *same* stale gap under two
>   normalisations (`÷2` and `÷|c_3^proton|`), not two measurements. So are the
>   **3.47 % / 3.35 %** pair for the proton gap. Do not "fix" either into the
>   other — state the denominator.
> - The stale `−2.00973976` and the *candidate model* `J_Hopf − ℏ_q² =
>   −2.00981718` agree to **four decimals** while being different objects
>   (they differ at 7.7×10⁻⁵). An earlier pass of this very correction
>   identified them and had to retract. Do not identify them by eye.
>
> **Scope-(a): the evidence moved, the verdict did not.** 2.3748 % is smaller
> than the quoted 2.98 % but still vast beside the 10⁻⁵⁰ compute precision, so
> FACT B stands and `c_3` remains a q₀-dependent NEAR-MATCH. No tier changes.

**Both are true.** Treating "wire c_k?" as yes/no forces a false choice.
This doc replaces that with the correct framing.

---

## The correct framing — four rules

### Rule 1 — N is a TRUNCATION ORDER chosen by target precision

The ladder is a **convergent series**. N is not a canonicity gate; it is
how many terms you keep. Because `u = b·ℏ_q² ≈ 0.00852`, `1/u ≈ 117`, and
`log₁₀(1/u) ≈ 2.07`, **each rung gains ~2.07 decimal digits**.

The required truncation order for relative precision `ε`:

$$\boxed{\,N \;\geq\; \frac{\log_{10}(1/\varepsilon_{\text{target}})}{2.07} \;-\; 1\,}$$

| target | N required |
|---|---|
| 100× experimental (7.8 ppb) | **3** |
| 1 ppb | 4 |
| 1 ppt | 5 |
| 1 ppQ (10⁻¹⁵) | 7 |

This is the answer to "what does N depend on?" — **it depends only on the
precision you require**, via the step size `u`.

### Rule 2 — the truncation error is the standard bound

$$\varepsilon_N \;\approx\; \bigl|c_{N+1}\,u^{N+1}\bigr|$$

Per-rung sizes (canonical c_k forms, NOT fitted):

| k | c_k form | \|c_k\| | \|c_k·u^k\| (ppb) | cum. residual (ppb) |
|---|---|---:|---:|---:|
| 2 | −1 (PROVED) | 1.00 | baseline | +1240 |
| 3 | J_Hopf(q=1) = −2 | 2.00 | 1235.7 | **+6.02** |
| 4 | c_3·b⁴ | 1.13 | 5.96 | **+0.055** |
| 5 | c_3²·3 + b | 12.87 | 0.58 | +0.63 |

### Rule 3 — c_2 is PROVED exact; c_k≥3 are NEAR-MATCHES (until a Habiro element makes them exact)

The **q₀-stability test** discriminates exact from near-match: a true
Taylor coefficient of a convergent series is **q₀-anchor-independent**.

- `c_2 = -1` — the exact `u²` coefficient of the explicit-factor product
  `∏_{k≥2}(1 + c_k u^k)`, hence trivially q₀-stable. **STRUCTURAL**, not
  **PROVED**: `N2_factor` is a definition with no theorem deriving it, and the
  Lean identity only re-reads it. (The normalised series, with the cosine
  factor inside, has `c̃_2 = c_2 − 1/8 = −9/8` — say which series.)
- `c_3 = -2` — gap to the candidate is 3.47% at the proton pin (`÷2`; the
  ladder witness reports the same gap as 3.35%, normalised by the extracted
  `c_3`) and 1.01% at the muon pin. Cross-anchor swing **2.3748%**
  (proton-normalised). **NEAR-MATCH.** The `0.49%` / `2.98%` that stood here
  are against the superseded muon `c_3 = −2.0097`; see the correction above.
- `c_4, c_5` — inherit c_3's near-match status; the **N=4→N=5
  non-monotonicity** (+0.055 → +0.63 ppb) is the experimental signature:
  a convergent series with *exact* c_k would be **monotone**.

Per the #1479 discipline lock: *"q₀-dependent residuals are evidence of
form-fitting at the test q₀."* **Correct.** But the conclusion that
follows is **not** "drop k≥3" — it is Rule 4.

### Rule 4 — report TIERED, never binary wired/dropped

The dashboard must report **both facts simultaneously**:

- N=3 value (beats 100× experimental), **tagged** `tier: near-match`.
- N=2 value as the deepest `tier: proved` rung.

`tier ∈ {proved, near-match, fitted}`. The #1479 `qbeta-ck-cache.witness.json`
already introduced this tiering — **keep it, use it, do not collapse it
back to binary.** A near-match that beats the experimental target is
useful information; silently dropping it loses a real result, and
silently wiring it overclaims a derivation. Tag it.

---

## The fix — identify the Q_β Habiro element

The permanent resolution is the **same machinery that closed α_EM**
(PR #1511, merged): the α_EM next-order factor `[2]_q·(1-h²α)` is a
**Habiro element** whose Taylor coefficients are **binomial-exact**,
`c_k = 2·C(1/2, k/2)·(1/4)^(k/2)` — exact, q₀-independent, with a
rigorous truncation bound.

Q_β needs the analogous step: **identify the q-series (Habiro element)
whose Taylor coefficients ARE the c_k.** Then:

- c_k≥3 upgrade from `near-match` to `proved`,
- the q₀-swing vanishes (a true Taylor coefficient is anchor-independent),
- `|c_{N+1}·u^{N+1}|` becomes a rigorous bound to arbitrary N,
- the N(ε) formula (Rule 1) becomes a derivation, not a heuristic.

In-flight infrastructure: `qbeta_habiro_taylor_investigation.py`,
`QbetaHabiroTaylorBridgeClass` (per #1479). The Habiro identification is
the genuine subgoal-2 research target — **NOT** another c_k wire/un-wire.

---

## Checklist for future sessions (do not re-open the flip-flop)

Before touching Q_β c_k wiring, confirm:

- [ ] Am I treating N as a **truncation order** (Rule 1), not a
      canonicity gate? If I'm asking "should we wire c_3?", I'm in the
      flip-flop — re-read Rule 4.
- [ ] Is each c_k **tagged** `proved` / `near-match` / `fitted` (Rule 4)?
- [ ] Did I run the **q₀-stability test** (Rule 3) before calling any
      c_k≥3 "canonical"? A >1% cross-anchor swing ⟹ near-match.
- [ ] If I want c_k≥3 to be `proved`, am I identifying the **Habiro
      element** (the fix), not just re-asserting `c_3 = -2`?
- [ ] Does the dashboard report **both** the proved-N=2 value **and** the
      near-match-N=3 value, with tiers?

---

## Cross-references

- Compute: [`qbeta_ck_truncation_order_analysis.py`](../../computations/qbeta/qbeta_ck_truncation_order_analysis.py)
- Paper: [`prop:q-beta-categorical-precision-ladder`](../../content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md)
- α_EM Habiro precedent: PR #1511 (merged), `alpha_em_habiro_taylor_investigation.py`
- Tiered cache: `qbeta-ck-cache.witness.json` (#1479)
- Prior (superseded-by-this) audits:
  [`2026-05-18-qbeta-n4-sign-investigation.md`](2026-05-18-qbeta-n4-sign-investigation.md),
  [`2026-05-30-qbeta-ck-mp-dk-deep-audit.md`](2026-05-30-qbeta-ck-mp-dk-deep-audit.md),
  [`2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md)
