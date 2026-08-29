# Canonical-derivation cheat sheet vs the paper — alignment audit

**Date:** 2026-08-25 · **PR:** [#5765](https://github.com/litlfred/qou/pull/5765) · **Bean:** `qou-9ot5`

Scope: `docs/canonical-derivation-cheat-sheet.md` (847 lines) against `mass-theory/`,
`appendix-mass-binding-algorithms/`, the two calibration observation blocks,
`standard-part-functor.md`, `ck-dk-canonical-registry.md`, the 2026-08-15 owner-ruling
audit, and the live producers. Numerics recomputed at 40–60 dps.

## Headline

The cheat sheet declares itself (line 12) *"the PRIMARY coordination document for the
canonical chain … do not fork a parallel status doc."* **Four parallel status documents
exist, contradict it and each other, and it does not link the most important one.**

- **Three mutually incompatible 11-step chains** (cheat sheet §2, `mba-chain-map.md`, the `mba-step0N` blocks).
- **Three different Step-9a mass formulas**, one silently carrying a documented CODATA fit.
- **Five mutually inconsistent Step-9b binding formulas with five disjoint error sets.**
- **Step 2 — the one step connecting geometry to algebra — is marked "✅ proved"** on the
  strength of a Lean theorem closed by `field_simp; ring`, citing a paper proposition that
  does not exist.

The document is **10 days to 8 weeks stale** in its numerics and **has absorbed no owner
ruling after 2026-08-11**. Zero occurrences of "2026-08-15", "R1/R2/R3", or "convention C".

## G1 — Step 2 is not derived. It is a definition wearing a geometry name. [load-bearing]

Cheat sheet `:41` marks Step 2 ("Non-abelian Stokes → Hecke") **✅ proved**. What exists:

`content/…/lean/QOU/Mass/HeckeStokesEigenvalues.lean:38-41`
```lean
theorem stokes_curvature_factors (q : K) (hq : q ≠ 0) (X : K) :
    X ^ 2 - (q - q⁻¹) * X - 1 = (X - q) * (X + q⁻¹) := by
  field_simp
  ring
```

No connection, no curvature form, no surface, no multiplicative integral — a quadratic
factorisation over a field. `NaStokesKeystone.lean:22-25` supplies the interpretation:
the abelianised Cartan connection *"**has** curvature 2-form `F(σ) = σ² − (q−q⁻¹)σ − 1`"*,
so flatness `F = 0` recovers the Hecke quadratic **tautologically**. Nothing computes a
curvature that *turns out* to be this polynomial. The appendix's Step-2 block says it
outright: the braiding obeys the Hecke relation because `def:categorical-action` says so.

The paper proposition both Lean files cite — **`prop:hecke-spectral-sequence` — does not
exist** (0 `label:` declarations in `content/`).

This is AGENTS.md §"Derive-then-check" item 8 verbatim: *if it is true by unfolding or by
`ring`, it is notation, not a theorem.* **The single bridge from the categorical substrate
to `H_n(q)`, on which steps 3–11 and every number in the framework ride, is an assumption
labelled "proved" in the coordination hub.**

Scope **(a)**: the current formalisation does not derive it. This does not exclude a
genuine Yekutieli derivation existing.

## G2 — Step 9a is an anchor round-trip presented as settled

> **🛑 CORRECTED 2026-08-25, same day — the "~40 digits" in this section was WRONG, and
> it was mine.** I reported `2·(m_μ·F_Bor − 6·m_e) = 938.2720881603789027…` as matching
> CODATA to ~40 digits. Measured at 80 dps against `codata_constants.M_P_MEV_VALIDATION =
> 938.27208943`, that value is **−1.35 ppb away** — it is not the CODATA match, it is the
> **de-fitted documented-pin round-trip** AGENTS.md already records as "+1.35 ppb". I
> computed a real number and then described it as something it is not.
>
> **What is actually true, and it makes the point better:**
>
> | quantity | value | vs CODATA |
> |---|---|---|
> | committed witness `m_p_MeV` | `938.2720894273242637274` | **−0.00285 ppb (2.85 ppq)** |
> | de-fitted round-trip | `938.2720881603789027` | −1.35 ppb |
> | `m_p,can/m_e` (the **ratio**) | `1836.152673426000032` | ~**1.7e-17** vs the anchor `1836.152673426` |
>
> **And no MeV figure here can be verified past ~11 digits regardless of working
> precision, because CODATA only *quotes* 11** — `m_e = 0.51099895069`,
> `m_p = 938.27208943`. A "40-digit agreement" against an 11-digit quote is not a
> measurable claim. The round-trip is real and tight (1.7e-17 in the ratio, where `m_e`
> cancels); the MeV number then inherits the 11-digit quote. Nothing about the
> anchor-round-trip conclusion changes — only the digit count, which was unverifiable as
> stated.

Recomputed: the *ratio* `m_p,can/m_e = 1836.152673426000032` against the CODATA anchor
`1836.152673426` — agreement to ~1.7e-17 relative, because `q₀` was solved from exactly
that ratio. That is the inverted solve, not a prediction.

`mba-step09a` says so honestly (*"q₀ is pinned by solving exactly this form against
m_p/m_e … so the identity round-trips m_p by construction"*), and the live witness marks
m_p `NOT SCORED … the framework content cancels`. The cheat sheet's §0 status column says
**"🟢 absolute nucleon mass settled (m_p ≈ 938.27 — CODATA)"**.

The genuine Step-9a predictions are `m_μ` (211.2 ppb, **970×** miss) and `m_n` (**177×**).

## G3 — Step 9b has no agreed formula; the paper's canonical block is a self-declared fit

Five disjoint error sets for the same step:

| source | ²H | ³H | ³He | ⁴He |
|---|---|---|---|---|
| cheat sheet §0 `:49` / §9.3 `:525` | +0.19 % | −0.16 % | −2.97 % | (+5.87 % magic-A) |
| cheat sheet §9.5.1 `:800-806` (depth-stratified) | −73 % | −67 % | −66 % | −50 % |
| `canonical-mass-table-242ppb.witness.json` (appendix 9b witness) | +23 % | +6 % | +13 % | +3.6 % |
| `mba-step09b` CKRecursion | — | (doublet ordering) | — | "~3.4 keV" |
| **live `B_sym`** | **−27.5 %** | **+38 %** | **+44 %** | **+69 %** |

`mba-step09b`'s algorithm is a `CKRecursion` with `r_res ≈ 2.596`, `a_0 = 1/2`, and an
SU(4) shift `+1.4947 m_e`, which the block itself calls *"calibrated, not derived … a
structural fit, **not** a parameter-free derivation"*. The cheat sheet's own 9b row says
that package was **"ADVERSARIALLY REFUTED as presented"** (#3723) — *"the 'SU(4)
differential 1.4947 m_e' IS the measured ³H–³He split relabeled; `r_res=2.596` ≠ the
advertised invariant 5/2"*. Its Input list declares `r_residual = 2.5` then computes 2.596.

**The paper's canonical Step-9b algorithm block is the thing the coordination hub records
as refuted, with those exact constants.** Its named witness `dashboard_and_sweep_results.md`
**does not exist** (`find` → 0); its alternate witness `canonical-mass-table-242ppb` has
`computedAt: null`, `scriptHash: null` and no producer (bean `qou-ahbz`). **Step 9b has no
valid witness by either route.**

## G4 — Δ_λ: the hub asserts a value contradicting a sorry-free theorem

Cheat `:500`: *"`Δ_λ = (q-Reeb phase density)_λ`"*.
Lean `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` (sorry-free, general-n,
2026-08-02): `Δ_λ = (−1)^{n(λ)}·dim V_λ`, the signed Springer dimension.

The hub has neither absorbed the proof nor retracted its incompatible claim. Zero
occurrences of `dtEuler`, `deltaLambda`, `Springer`, or `2026-08-02`.

## G5 — `conditional-proved ≠ premise-established`, twice on one formula

- `:107`, `:321` cite **`prop:geom-universality`** as authority for "there is one canonical
  mass formula". Only **`conj:geom-universality`** exists.
- `:189` cites `prop:hecke-spectral-sequence` — does not exist (G1).
- `:231` cites `prop:averaging-resonance-rule`; the actual label is `thm:`.

A `prop:` prefix on a conjecture, inside the coordination hub, is the laundering AGENTS.md's
STRICT section is written against.

&gt; The 2026-07-05 currency audit asserts *"All 14 §2 step-table paper labels resolve"*. It
&gt; stem-grepped rather than label-grepped; **two of its fourteen do not resolve.** Do not
&gt; treat that audit as clearance.

## G6 — Step-11 circularity + a possible CAL-3 dependence

`mba-step11` computes `Q_base` from `m_n`; `mba-step09a` step 5 computes
`m_n = m_p + Q_β + m_e`. Whether this closes (9a uses the N=2 Kashiwara `Q_β`, 11 the full
ladder) is nowhere stated. Step 11 also lists **CAL-3 (pion width) as an input to a β-decay
Q-value** — if real, that makes `Q_β` 3-CAL-dependent rather than the CAL-2 cross-check both
the cheat sheet and `three-calibration-discipline.md` call it.

## G7 — the `α_k` set is not a derived object

Listed at `:774` under **"α_k coefficients (NOT empirical fits)"**. But the same section's
PROBE-2 verdicts three lines below call α₃ = 1 a **10.4 % near-match** and the α_{k≥4}
plateau **REFUTED-(a)**; `α_{k≥4} = m_e·8G ≈ 3.7445` carries **MeV units in an otherwise
dimensionless list** inside `B = m_e·Σ_k α_k(…)` where `m_e` is already factored out; and
`α_2 = z²` is `z_C²`.

## Convention-C contamination in the hub

| site | claim | correct under D |
|---|---|---|
| `:221` | `z = 1/(q^{1/2}+q^{-1/2})` = `√q/(q+1)` = **0.4993203342** | `z_D = q³/(q²+1) = **0.6126880371**` |
| `:774` | `α_2 = z² ≈ 0.2493` under **"NOT empirical fits"** | `z_D² = **0.3753866309**` — a **50 % error** in a coefficient called non-fitted |
| `:783–787` | `tr_M(T_Δ) = z·(1+√q−1/√q) ≈ 0.5514`, PROBE-2 verdict "DERIVED (exact)" | correct **as C-arithmetic**; half-integer powers of `q` are impossible under D — the derivation must be **redone**, not `z`-substituted |
| `:650` | correctly registers the production trace as **convention D** | so the hub is **internally C in §3/§9.5.1 and D in §9.3** |
| `:51`, `:341` | Step 11 "🟢 derived; `c_k` truncation" | the `c_k` ladder is **C-frame end-to-end**; re-extraction under D shifts `c₃ → ≈ −974` (bean `qou-cds1`) |

**Why no detector caught this:** `scripts/convention-c-producer-audit.py` is AST-verified
over `.py`. It structurally cannot see a `z` written in markdown. **The coordination hub is
the one convention-C surface with no automated guard.**

## STRICT violation and stale numerics

| site | says | live |
|---|---|---|
| `:340` | `beats_100x_count = 2` — "**2 of 7**" | `beats_100x_scoreable = **1**`, `scoreable_total = **5**`. AGENTS.md STRICT: *"never bare `beats_100x_count`"*. 2026-08-22 red team: unconditional **0/5** |
| `:340` | five gaps = (m_p, m_μ, Q_β, m_n, Δ_pn) | m_p is `NOT SCORED` (anchor round-trip); the scoreable five are {m_μ, Q_β, m_n, Δ_pn, m_K/m_π} |
| `:340` | m_μ 209.8 ppb / 963.6× | **211.2 ppb / 970.2×** |
| `:346` | `η_0 = log q_0 ≈ 0.10416` ⇒ ratio 0.8913 | `log q₀ = **0.1043407203**` ⇒ **0.8908357** |
| `:358` | `g = π·h_0 = π·0.20856 = 0.6552`, dev **+0.26 %** | `h(q₀) = **0.2090602988**`, `π·h = **0.6567823**`, dev **+0.50 %** — **2× the advertised deviation**, in a table whose entire content is the size of that deviation |
| `:198` | `Δ(net) = h(h−2)/2 ≈ −0.1883` | **−0.1872071945** |
| `:422` | proton pin "**0.06 ppb**" | `MASS_RATIO_P_E_ERR = 3.2e-08` ⇒ **0.0174 ppb** (same stale figure at `epistemic-status-of-calibrations.md:41`) |
| `:49` vs `:626` | `Vol₄ = 8.05` vs `Vol(L6a4) = 8G = 7.3277` | unreconciled, same document |

## Coverage holes

| what | where it lives | hub coverage |
|---|---|---|
| the **live binding compute** `mass_binding_dashboard.py` (61 KB, driven by this repo's own `/dashboard-low`) and its forms | that file + `standard-part-functor.md` | **0** occurrences of `B_lin`, `B_sym`, `B_qCLT`, `B_magic`, `mass_binding_dashboard`. §9.5.1 still calls the superseded `binding_depth_stratified_rust.py` the "canonical default" |
| **`appendix-mass-binding-algorithms/`** — the maintenance contract AGENTS.md makes STRICT | 22 blocks + 4 sidecars + chain map | **0 hits** |
| the **standard-part functor** `St : No_fin/No_inf ≅ ℝ` — the paper's formalisation of step 9's τ | `standard-part-functor.md` | **0** occurrences of "standard part" or "surreal" |
| **q₀-derivation is FOREVER GATED** (owner, 2026-08-02) | AGENTS.md | 0 hits for "forever"/"Subgoal-2" — a hub routing agents to step-9 research with no guard against the one permanently forbidden route |

## Adjacent authoritative files needing correction (found in passing)

- **`ck-dk-canonical-registry.md`** §1/§3 still say `c_2 = −1` is *"CANONICAL (proved,
  Taylor-exact)"*; AGENTS.md retracted "proved" 2026-08-16 (`N2_factor` is a bare `def` with
  no theorem) and **`mba-step11` already carries the corrected wording — the registry is
  behind its own downstream block**.
- Same registry §3 still carries `dc_3/dq ≈ 4.6×10⁶`; live is **3.84e6**. AGENTS.md said
  "five other sites"; **≥19 measured**, the registry included. Re-scope bean `qou-3nva`.
- **`mba-step11`** instructs *"`c_k` **never** reported as 'fitted'"* while the authoritative
  registry classifies **c_4 as "EMPIRICAL — CODATA fit / artifact"**. An anti-fit-discipline
  inversion sitting in the paper.
- **`mba-step08`/`mba-step11`/chain-map sidecar** restate the `N ≥ ⌈log₁₀(1/ε)/2.07⌉ − 1`
  truncation rule in three places; AGENTS.md 2026-08-16 says it *"does not describe the
  canonical producer"* — `qbeta_ck_cache.py` inverts for one rung and `c_4…c_7` are never
  computed.
- **`binding_canonical.py:295`** uses `pn_convention="strict_averaged"` against R3 — a file
  named *canonical* asserting a non-canonical convention, exactly as the owner-ruling audit
  predicted (`…:214`). 16 live sites use `bring_color_weighted`, 9 `chi_lambda_braid`, 6
  `strict_averaged`.

## Checked and cleared (so nobody re-opens them)

The two `Q_β` forms (`E₀·|h(h−2)/2|` and `m_e|q₀²−2q₀−1|(q₀+1)/(2q₀³)`) agree to 40 digits —
one identity, not a divergence. `E₀ = m_e c_q² ℏ_q` ✓. `tr_M(β_Bor) = 0.998562163836787265951`
matches the registry's convention-D value exactly ✓. The `:650` "registered as convention D"
is correct and is **not** a name collision with the owner's D — same `z = q³/(q²+1)` row.
`markov_trace_unique_axiom` exists as claimed. `u ≈ 0.008517` ✓, magic-A `+5.87 %` ✓,
`μ₀ ≈ 1.63 MeV` ✓, `m_e·8G ≈ 3.7445` ✓. LP-dual infra healthy (2/27 flagged, warn-only) —
the "58 of 58" era is over. All 13 scripts/witnesses in `mba-chain-map.md` exist.
