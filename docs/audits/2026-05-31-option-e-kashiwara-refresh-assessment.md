# 2026-05-31 — Option E (Kashiwara crystal) refresh — discipline assessment

**Branch:** `claude/option-e-kashiwara-refresh-2026-05-31` (PR #1586)
**Audience:** anyone evaluating whether Option E (Kashiwara crystal weight → Δ_λ) is a live closure path or another fit.
**Verdict (BLUF):** Option E, as implemented in `option_e_v6/v7/v8/v9.py`, **does NOT close Δ_λ from first principles.** The parameter-free crystal-weight prediction for the deuteron captures only **17.1%** of the binding (B_pred = 0.380 MeV vs AME 2.225 MeV, **−82.9%**); the honest Δ_λ residual is **−0.744 m_e predicted vs −4.353 m_e target**, leaving **−3.609 m_e (82.9%) unaccounted with zero free parameters.** Every "closure" in these scripts is achieved by a **back-solved correction factor** (`correction_target = target/base`) name-matched to a substrate-expression menu — the exact post-hoc-fit antipattern flagged for the isospin-v9 `(1+q)/2` factor (PR #1578) and retracted for the 2026-05-26 `C_knot = 5.852` deuteron claim (2026-05-29).

**Recommendation: do NOT promote.** Option E remains a *direction* (CLAUDE.md §7b authoring guidance) but the current compute is fit-anchored, not derived. No closure CANDIDATE witness is emitted (the parameter-free margin is 82.9%, far outside any defensible band).

---

## 1. What the scripts actually compute (fresh re-run on `origin/main` @ ced5e28306)

All four scripts re-ran clean (exit 0). Logs: `/tmp/opt-e-v{6,7,8,9}.log`. Crucially, **none of them computes a per-partition Δ_λ from crystal structure** (crystal vertices `w`, multiplicities `n^w_λ`, canonical-basis traces `ρ_w`). The 2026-05-25 audit's formula

$$\Delta_\lambda(K) = \sum_{w \in \mathcal{B}_\lambda(\mathcal{B}_K)} n^w_\lambda \cdot \rho_w(K)$$

has **no implementation on disk** — `ρ_w` is listed as "(NOT EXIST)" in that audit's survey table and is still absent. What v6–v9 actually do is a **scale × combination menu search** over cached `χ^λ` and `y_λ`:

| Script | What it computes | Targets | "Best" result | Mechanism |
|--------|------------------|---------|---------------|-----------|
| **v6** | `E_rot = μ₀·ℏ_q·J_q²(n/2)` + Reeb-phase mirror decomposition | D/T/³He absolute + T−³He diff | D −9.2%, T −48.6%, ³He −43.5%; mirror diff all ≥ −81% | rotational scale + 6-candidate scale menu |
| **v7** | self-conj + bar-(anti)symmetric `χ` combinations | D/T/³He absolute + mirror | best absolute **max err 95.8%**; best mirror **+58.4%** | 5 scales × 7 involution sums = 35-candidate menu |
| **v8** | isospin-mirror identity + cross-isotope bar combos | T−³He diff only | `m_π·ℏ_q·Σy·M_sym` = **−6.15%** | 6 scales × 5 inputs = 30-candidate menu |
| **v9** | "all symmetries" on top of v8 | T−³He diff only | `m_π·ℏ_q·(1+ℏ_q)·M_asym` = **+2.52%** | 9 scales × 9 inputs (81 candidates) **+ explicit back-solve** |

Three observations kill the closure claim before we even reach the deuteron:

1. **v8/v9 never touch the deuteron.** They fit only the T−³He *mirror difference* (0.7637 MeV), a much easier 1-parameter target than the absolute Δ_λ. The deuteron Δ_λ — the actual gating quantity — is computed only by v6/v7's *absolute* branch, where every candidate fails (best D err −9%; T/³He worse).
2. **The "best" results migrate across the scale menu** as more scales/inputs are added (v8 lands on `m_π·ℏ_q·M_sym`, v9 lands on `m_π·ℏ_q·(1+ℏ_q)·M_asym`). A genuine derivation does not change formula when you enlarge the candidate menu.
3. **v9 contains the literal back-solve.** Lines 192–211: `correction_target = diff_target / base_v8` (= 1.056050), then a 9-candidate substrate menu where `(1+q)/2 = 1.054855` matches at **−0.11%**. This is the identical pattern caught for the isospin-mirror `(1+q)/2` factor in PR #1578 — back-solve the needed factor, then name-match it to a menu.

---

## 2. Honest parameter-free deuteron Δ_λ residual

**Target (verified):** `−B_D^AME / m_e = −2.224566 / 0.51099895069 = −4.353367 m_e`. This matches the gating audit's stated −4.353.

**Parameter-free crystal-weight prediction** (the 2026-05-26 form `B = m_e·|Σ_λ y_λ·χ^λ(β_D)·sgn(w₀^{S_{λ'}})·f^λ|`, evaluated at 50 dps on the interface-inclusive `atom-chi-rust-d.witness.json` + `chi-deuteron-h6-at-q0-50dps.witness.json`, **with NO C_knot, NO scale menu**):

| Quantity | Value |
|----------|-------|
| `Σ_λ y_λ·χ^λ_atom·sgn(w₀)·f^λ` (signed) | −0.743901 |
| **B_pred** = `m_e·|Σ|` | **0.380132 MeV** |
| B_D^AME | 2.224566 MeV |
| **rel err** | **−82.91%** |
| **Δ_λ residual predicted** | **−0.743901 m_e** |
| **Δ_λ residual target** | **−4.353367 m_e** |
| **captured fraction** | **17.1%** |
| **unaccounted residual** | **−3.609467 m_e (82.9%)** |

This reproduces the 2026-05-29 retraction's deuteron figure (−82.9%) to the digit.

**The C_knot back-solve, confirmed:** the only factor that makes B_pred hit AME is `C_knot = B_AME / (m_e·|Σ|) = 5.852082`, which equals the retraction's quoted 5.852. C_knot **is** the missing residual divided out — i.e. the "closure" is achieved by defining the correction as `(target / prediction)`, the canonical back-solve. With zero free parameters the prediction is off by **5.85×**.

---

## 3. Per-script fit-vs-derived verdict

| Script | Derived (no free param)? | Smoking gun | Verdict |
|--------|--------------------------|-------------|---------|
| **v6** | partly — `E_rot = μ₀·ℏ_q·J_q²` uses only derived scales (μ₀ from m_e, ℏ_q from q₀); the Reeb-phase *mirror* part is a 6-candidate scale menu | `candidates = {…}` dict (L228–235) picks min-err scale | **DERIVED scale, FITTED selection.** The rotational scale is honest but fails (D −9%, T/³He −44–49%); the mirror decomposition is menu-selected and also fails (all ≥ −81%). Not a closure. |
| **v7** | no | `scales × inputs` grid (L218–249); `sorted_results[:10]` reports the menu min | **FITTED selection.** 35-candidate menu; best absolute closure still 95.8% off. Bar/transpose symmetry is correctly applied but does not produce Δ_λ — it just enlarges the menu. |
| **v8** | no | `for sname,scale in scales: for ikey…: results[…]` (L219–228); `best_mirror_formula = sorted_results[0]` | **FITTED selection.** 30-candidate menu on the *easy* mirror-diff target; "−6.15%" is the menu min, not a derivation. Does not address the deuteron. |
| **v9** | **no — explicit back-solve** | **L194: `correction_target = diff_target / base_v8`**; L197–211 name-matches `(1+q)/2 = 1.054855` at −0.11% | **FITTED + BACK-SOLVED.** This is the PR #1578 `(1+q)/2` antipattern verbatim: compute the needed factor as target/base, then find a substrate expression that matches it. The 81-candidate menu min (+2.52%) is also a fit. |

**Is the v8/v9 isospin work parameter-free?** No. It smuggles in a fit two ways: (a) the scale-menu selection (`m_π·ℏ_q` vs `m_π·ℏ_q·(1+ℏ_q)` etc. chosen by min-err), and (b) in v9, the explicit `correction_target = target/base` back-solve. The isospin-mirror *identity test* (v8 Test A) is honest and informative — it finds Σ|χ_T(λ)−χ_He3(λᵀ)| = 72.2 (atom) / 556.6 (free), i.e. the mirror identity does **not** hold exactly — but that negative result is then papered over by the menu search in Test C.

---

## 4. Does the crystal weight give Δ_λ from first principles? (tiered, per factor)

| Factor in `B = m_e·|Σ_λ y_λ·χ^λ·sgn(w₀)·f^λ|` | Tier | Note |
|-----------------------------------------------|------|------|
| `y_λ` (Wenzl–Jones–Markov central coeff) | **PROVED** | closed form, cached 50 dps; not in question |
| `χ^λ(β_D)` (Hecke character, interface-inclusive) | **PROVED** | Hoefsmit; cached |
| `sgn(w₀^{S_{λ'}})` (longest-element sign) | **PROVED** | Macdonald I.1.5 |
| `f^λ = dim V_λ` (hook-length) | **PROVED** | Burnside |
| **Δ_λ = (the per-block assignment that reproduces B)** | **FITTED** | the product of the four proved factors gives only **17.1%** of B_D; the remaining 82.9% is supplied by `C_knot = 5.852`, a back-solve = `B_AME/(m_e·|Σ|)` |
| **`ρ_w` crystal-vertex trace** (the genuine Option-E object) | **NOT IMPLEMENTED** | the formula `Δ_λ = Σ_w n^w_λ·ρ_w` has no compute on disk; without it there is no first-principles crystal weight to test |

The individual algebraic factors are proved, but **their product is not Δ_λ** — it misses by 5.85×. The genuine crystal-weight object (`ρ_w` per crystal vertex) was never implemented, so the "crystal" framing is currently aspirational; what runs is a Hecke-character sum dressed with a fitted scalar.

---

## 5. Closure-candidate decision

**No witness emitted.** Per the task gate ("emit a closure-CANDIDATE witness only if genuinely parameter-free AND within a defensible margin"), neither condition holds:

- **Parameter-free margin:** −82.9% (deuteron). Far outside any defensible band.
- **Parameter-free?** No — every script's headline number is either a menu-min selection or an explicit `target/base` back-solve.

A closure CANDIDATE witness would misrepresent the state. The honest artifact is this assessment doc plus the (already-written) v6–v9 witness JSONs that record the menu searches as exploratory probes. **Option E does NOT close Δ_λ.**

---

## 6. Recommendation

1. **Do not promote** any v6–v9 result to a content proposition or remark claiming closure. (None attempted; this doc + the existing exploratory witnesses are the only artifacts.)
2. **Do not author a 7th fit-based ansatz.** The scale-menu + back-solve pattern in v8/v9 IS a fit, regardless of the "crystal/isospin" framing. The three-calibration discipline review (and PR #1578) already caught this shape.
3. **Option E remains a paper *direction*** under CLAUDE.md §7b (Type B folding, KLR→KL classical limit, Demazure resonances) and the GAP-A-3 / GAP-A-4 conjectures — but a relaunch must meet the 2026-05-30 KLR-dialog relaunch criteria: a **per-partition, q-independent, categorical** Δ_λ candidate sharpened *on paper first*, tied to GAP-A-3/A-4 progress, with a testable prediction **beyond** the deuteron stated up front. A bare crystal compute sweep without `ρ_w` implemented recapitulates the prior failure.
4. **Productive non-Δ_λ-gated work** (per the gating audit) remains Track B (recursive ρ_ξ for the branching combiner), not another Δ_λ probe.

---

## Cross-references

- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — Δ_λ gate, six failed ansätze, **2026-05-29 retraction** (D −82.9%, C_knot fitted).
- [`docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md`](2026-05-25-option-e-crystal-weight-delta-lambda.md) — Option E scaffolding; `ρ_w` listed as NOT EXIST.
- [`docs/audits/2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md) — KLR/crystal relaunch criteria; "crystal" on the failed-ansatz list.
- PR #1578 — isospin-mirror v9 `(1+q)/2` post-hoc-fit finding (same back-solve pattern as this doc's §3/v9).
- Scripts: `computations/option_e_v{6,7,8,9}*.py`. Fresh-run logs: `/tmp/opt-e-v{6,7,8,9}.log`.
- Witnesses (exploratory menu searches, not closure): `option-e-v{6,7,8,9}-*.witness.json`.
- CLAUDE.md §7b (symmetric-crystal authoring guidance) + Δ_λ gate warning ("do not propose a seventh fit-based ansatz").
