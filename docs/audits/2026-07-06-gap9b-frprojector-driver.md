# Gap-9b: H_{3A} Borromean FR-projector driver — tiered verdicts (bean yfvb)

> **🛑 LANDED LATE, AND RE-SCOPED BY LATER WORK. Read this banner before
> the body (added 2026-09-03).**
>
> **Provenance.** This document was written on 2026-07-06 but **never
> merged**: PR #3440 merged at `c2ff21f88` while the session kept
> committing, stranding four commits (tip `3409f9df39`) on the branch.
> It is restored here as the historical record of the FR-projector probe.
> Its numbers are as-measured on 2026-07-06 and have **not** been re-run.
>
> **Frame it was written in, which has since moved three ways:**
>
> 1. **The question changed.** This probe hunted "the missing per-λ Δ_λ
>    content". Since then the per-λ **value** was *proved*
>    (2026-08-02, sorry-free, general-n):
>    `Δ_λ = (−1)^{n(λ)}·dim V_λ`. What is open is the many-body binding
>    **magnitude** — a separate, extensive, super-pairwise additive term.
>    Read this probe as an early entry in the *extensive-term* search,
>    not as a Δ_λ-value search.
> 2. **The route is now excluded more broadly than this probe showed.**
>    The cheat-sheet §9.3 currency banner (2026-08-30) relocates the gate
>    to the **assembly functional**: no per-block weight can turn an
>    intensive quantity into an extensive one, so the refutation here —
>    scope-(a), about one proxy — is *absorbed by* a stronger structural
>    result rather than standing alone.
> 3. **Convention and pin.** The run used a **convention-C** `z` in α₂
>    and the **then-canonical muon-era witness q₀ (pin A,
>    1.10997859555733471…)**. Convention D became canonical 2026-08-15;
>    pin A was retired 2026-08-22/28. The verdict margin (~4%) is far
>    larger than either shift, so the *conclusion* stands — but do not
>    quote these numbers as current-frame values.
>
> **What in here is still live and useful:** the normalization-convention
> finding of §4 (the balanced-convention `dim_q²/[n]_q!` is not a
> probability measure), which remains **unregistered** in the
> trace-convention registry, and the feasibility wall of §3.

**Date:** 2026-07-06
**Branch:** `claude/cheat-sheet-derivation-gaps-0ykco4` (PR #3440)
**Bean:** `yfvb` — gap-9b FR frontier: producer→witness q₀ refactor (prereq) + H_{3A} Borromean FR driver
**Driver:** [`computations/fr_pullback_borromean_h3a_test.py`](../../computations/fr_pullback_borromean_h3a_test.py)
**Witness:** [`computations/fr-pullback-borromean-h3a-test.witness.json`](../../computations/fr-pullback-borromean-h3a-test.witness.json)
**Scope discipline:** derive-or-refute; no new constants; every negative is **(a) scope-limited** unless a proved invariant is cited. Δ_λ "no 7th fit-based ansatz" gate respected — the FR weight is built from χ^λ of a *fixed canonical word* (β_Bor), not fitted.

## 1. What was tested

The FR-restricted knot-ideal projector candidate `χ^λ → χ^λ·χ^λ(e_{K*})`
([`2026-06-28-brane-tower-formalize-first-plan.md` §7](2026-06-28-brane-tower-formalize-first-plan.md))
with **K\* = the nucleon's own knot** β_Bor = (σ₁σ₂⁻¹)³ embedded in the ambient
atom algebra H_{3A} — the corpus's frontier object for the missing per-λ Δ_λ
content (the un-weighted Markov re-decomposition is null to ≤ 6.6e-7:
[`2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md`](2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md)).

Mechanism (`fr_pullback`, per `conj:depth-stratified-frobenius-reciprocity`):
within each depth-k stratum of λ ⊢ 3A, redistribute the **self-normalized**
q-Plancherel weight `dim_q²(λ)/Σ_μ dim_q²(μ)` (see §4 for why the textbook
`dim_q²/[3A]_q!` form is wrong in the balanced convention) proportionally to
`|χ^λ(β_{K*} ⊂ H_{3A})|`, preserving each stratum's total mass. Binding is the depth-stratified
functional `B = Σ_k α_k·(Φ_k^free − Φ_k^atom)` (same as
`fr_pullback_k3_test.py`), swept over D, T, ³He, ⁴He vs AME2020, with:

- **modes**: `k3` (depth-3 stratum only — directly comparable to the k3-test
  winners) and `all` (every stratum — §7's candidate is not k=3-restricted);
- **K\* columns**: `borromean` (the candidate) and `4_1` (the k3-test
  empirical best, re-validated at the canonical witness q₀), vs the
  `uniform` no-FR baseline.

## 2. Prereq 1 — producer→witness q₀ discipline (executed for this driver; measured finding)

The bean's Prereq 1 (producers must source q₀ from the canonical pinning
witness, not the runtime `q_parameter.Q`) is **implemented in this driver**
and the underlying inconsistency is now **measured, not hypothesized**:

- Runtime `q_parameter.Q_50_DIGIT_STR` (proton tower-free solver) =
  `1.10997858275138…` — **−11.537 ppb** from the canonical pinning witness
  `q₀ = 1.10997859555733471…` (`q-pinning-50-digit.witness.json`).
- **Provenance finding (new):** the committed
  `atom-chi-rust-{d,t,3he,4he}.witness.json` χ^λ inputs sit at the **runtime
  proton q, not the canonical witness q₀**. Recomputing D's free-config χ^λ
  from the same word bridge reproduces the committed 50-digit strings
  **exactly (rel dev 0.0 < 1e-45)** at the runtime q, and drifts by
  **4.9e-7** at the witness q₀ (χ-level amplification of the 11.5-ppb q
  drift by the 22-crossing word). Encoded as the witness assertion
  `committed_atomchi_is_proton_q`.
- Consequence: consuming the committed atom-chi witnesses under a witness-q₀
  driver would produce a **q-inconsistent hybrid**. The driver therefore
  **recomputes every χ^λ at the witness q₀ inside itself** (canonical MPFR
  tier, 50 dps, no f64 on the production path), via a q-parameterised port of
  the `chi_cd_mpfr` linearity bridge (which hard-bakes the runtime
  `Q_50_DIGIT_STR` — the Prereq-1 defect).
- The **~72-producer refactor** (all producers sourcing q₀/q_inv/ℏ_q from the
  pinning witness) remains **owner-gated** (bean `tnjb`-adjacent; the failed
  runtime-patch attempt and the import-time-baking mechanism are documented in
  the bean). This driver is the working exemplar of the target pattern:
  `load_q_50dps()` + in-script recompute + provenance assertions.

## 3. Compute unblock + feasibility wall

- `pyhecke_native` 0.9.0 wheel built from source in this sandbox per the
  [unblock recipe](2026-07-05-gap9b-frprojector-unblock-and-kappa-asymptote.md)
  (`maturin build --release --no-default-features`; rug compiles GMP/MPFR;
  litlfred/Clarabel.rs resolves through the session proxy). Build ~13 min.
- Kernel sanity at witness q₀: χ^{(2,1)}((σ₁σ₂⁻¹)³) matches the proved closed
  form 2−3h⁴−h⁶ to **2.9e-50**; χ^{(3)} = χ^{(1³)} = 1 exactly.
- **Wall (bounded, per the long-compute discipline):** A ≤ 4. The cost driver
  is the **max seminormal irrep dimension f^λ** (dense matrices), not the
  partition count:
  - H_12 (⁴He): p(12) = 77, max f^λ = 7,700; a 6-crossing word ≈ 46 s, the
    47-crossing atom word ≈ 7.2 min per linearity term (2 terms → 14.5 min;
    full ⁴He block β_atom + β_free + 2 K* words ≈ 22.5 min wall, ~4 threads).
  - H_15 (⁵Li): p(15) = 176, max f^λ = 292,864 — hours at best.
  - H_18 (⁶Li): p(18) = 385, max f^λ = 16,336,320 — a dense 1.6e7² MPFR
    matrix is out of reach; no committed upstream atom-chi witness exists
    either.
  - H_48 (¹⁶O): p(48) = 147,273 blocks, max f^λ ≈ √(48!) ≈ 3.5e30 —
    **structurally infeasible** for dense seminormal character evaluation.
    The ¹⁶O 2.3× normalization miss can only be probed at H_{3A} level
    through a structural (closed-form / branching / LR-factorised) route,
    not brute character evaluation.

## 4. Normalization convention finding (v1 run invalidated; v2 = corrected)

The **v1 run** (17:57–18:19 UTC) used the textbook Plancherel form
`w = dim_q²/[n]_q!` with **balanced** q-integers
(`[k] = (q^k − q^{−k})/(q − q^{−1})`). Its own `plancherel_completeness`
assertion caught that this is **not a probability measure** in that
convention: `c_n = Σ_λ dim_q²/[n]_q!` deviates from 1 by
0.0089 / 0.111 / 0.517 at n = 6/9/12 at the witness q₀ (main-session
cross-diagnosis; `q^{±2n(λ)}` and `q^{±(n(λ)−n(λ′))}` prefactors do not
close the gap). The per-n distortion exceeds the v1 verdict margin, so
**the v1 variance numbers are recorded as invalidated-by-normalization,
not as findings**:

- v1 (invalid normalization): uniform 1.8217, fr_borromean_k3 1.8009,
  fr_borromean_all 1.7487, fr_4_1_k3 1.5506, fr_4_1_all 1.7257 (signs all +).

**Fix (v2 = the committed driver):** the base measure is **self-normalized**
— `w(λ) = dim_q(λ)²/Σ_μ dim_q(μ)²`, a probability measure by construction,
q-integer-convention-free. `c_n` stays recorded in the witness
(`plancherel_convention_gap`) as an open normalization item. Note the
FR-vs-uniform ratio *within* one atom is scale-invariant (both weights scale
by the same 1/c_n), so the correction moves the **cross-atom variance** (the
verdict metric), not the per-atom FR effect.

## 5. Results (v2 — self-normalized, all at witness q₀, MPFR 50 dps)

Variance metric: max/min of |B_pred/B_AME| over {D, T, ³He, ⁴He} (1.0 = flat
= per-λ content fully supplies the missing normalization shape at A ≤ 4).

| variant | max/min variance | signs + | per-atom ratios (D, T, ³He, ⁴He) |
|---|---|---|---|
| uniform (no FR) | 1.1901 | yes | 0.2753, 0.2980, 0.3094, 0.3276 |
| fr_borromean_k3 | 1.1764 | yes | 0.2791, 0.2995, 0.3063, 0.3284 |
| fr_borromean_all | 1.1423 | yes | 0.2917, 0.3053, 0.3090, 0.3332 |
| fr_4_1_k3 | **1.1355** | yes | 0.3206, 0.2854, 0.3028, 0.3240 |
| fr_4_1_all | 1.1447 | yes | 0.2864, 0.2882, 0.2821, 0.3229 |

k3-test reference (committed proton-q run, f64 FR weights, v1-style
`dim_q²/[n]_q!` normalization): uniform baseline 1.82×, best = 4_1 at 1.55×.
The v1 run reproduced both at the witness q₀ (1.8217 / 1.5506) **before**
the normalization fix — i.e. the published k3-test variance numbers inherit
the same balanced-convention distortion and should be re-read against v2.

## 6. Tiered verdicts

- **REFUTED, scope-(a)** — the Borromean FR projector (K\* = β_Bor, this
  redistribution form, alone, as-is) does not supply the missing per-λ
  Δ_λ content: best Borromean variant trims the light-series spread only
  1.190 → 1.142 (~4% of the ~19% needed to flatten), and — the decisive
  structural point — **fails to beat the 4₁ proxy** (1.1355), so the
  specific hypothesis "the *nucleon's own knot* supplies the weight"
  fails on its own terms. Scope-(a): constrains THIS proxy
  |χ^λ(β_K\* ⊂ H_3A)| with stratum-preserving redistribution only; the
  knot-ideal idempotent e_{K\*}, volume-enriched weights, and the
  geometric W_λ build remain open.
- **DERIVED (side result):** self-normalization finding — in the balanced
  q-integer convention `dim_q²/[n]_q!` is NOT a probability measure
  (c_n = Σ dim_q²/[n]_q! = 0.9911 / 1.1109 / 1.5171 at n = 6/9/12,
  witness q₀; standard `q^{±2n(λ)}`, `q^{±(n(λ)−n(λ′))}` prefactors do
  not close it). All v1 numbers and the committed k3-test variance
  figures inherit this distortion — **the k3-test's published 1.82×/1.55×
  baseline should be re-read against the self-normalized 1.19×/1.14×**
  (an open normalization-convention item for the trace-convention
  registry).
- **DERIVED (Prereq-1):** the committed atom-chi caches are proton-q
  inputs (rel dev 0 at runtime q, 4.9e-7 at witness q₀) — the bean's
  producer→witness q₀ question answered; this driver rebuilds
  coefficients at the witness q₀ directly.
- **Feasibility wall (recorded):** cost driver is max seminormal irrep
  dim f^λ, not partition count — H₁₂ (⁴He) ≈ 25 min; H₁₈ (⁶Li,
  max f^λ = 16.3M) out of dense reach; H₄₈ (¹⁶O) structurally
  infeasible for this route.

## 7. Assertions (witness, v2)

| assertion | result |
|---|---|
| `borromean_chi21_closed_form` (native vs proved closed form, 1e-45) | PASS (2.93e-50) |
| `committed_atomchi_is_proton_q` (Prereq-1 provenance) | PASS |
| `plancherel_completeness` (self-normalized Σ w = 1, 1e-40; c_n gap recorded separately) | PASS (v1 FAILED at 0.517 under `dim_q²/[n]_q!` — the convention finding above) |
| `fr_stratum_mass_preserved` (redistribution preserves stratum mass, 1e-40) | PASS (9.1e-72) |
| `data_loaded` (AME D) | PASS |
| `fr_borromean_variance_recorded` (tier + numbers) | PASS (1.1423) |

## 8. What this does and does not constrain

- The projector is **proxied** by the braid character `|χ^λ(β_{K*} ⊂ H_{3A})|`
  with stratum-mass-preserving redistribution — the same proxy the k3 test
  used. The knot-ideal **idempotent** e_{K*} itself (a projector in the
  Habiro-completed ideal, not a braid character), volume-enriched weights,
  and the geometric `W_λ` build (s5-so3 keystone, owner-gated) are **not**
  tested here and remain open regardless of this driver's verdict.
- Negative outcomes are **(a)-scoped**: they constrain THIS redistribution
  form with THIS proxy, alone, as-is. No structural invariant excludes
  per-λ FR weights in general (per the state report's scope discipline).
