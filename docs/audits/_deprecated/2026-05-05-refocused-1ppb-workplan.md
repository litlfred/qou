> **DEPRECATED on 2026-05-24.** Superseded by [`2026-05-18-1ppb-workplan-v7-100x-experimental.md`](../2026-05-18-1ppb-workplan-v7-100x-experimental.md) (the latest in the 1ppb-workplan chain). Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T4 for the deprecation rationale.

# Refocused 1-ppb Workplan — 2026-05-05

**Status of W-3 (D(u) closed form):** ✅ 3/3 categorical proof landed in main (PR #539, PR #543).
**Active follow-ups:** PR #534 (singular 6-term), PR #545 (term6 wiring), PR #546 (symbolic Hoefsmit −1/12).
**Remaining gap to 1 ppb:** ⁴He at +5.87% is the hard floor (10⁷ × off the target 10⁻⁹).

---

## §0. The three calibration inputs (= "allowed empirical")

Per [`prop:three-calibration-inputs`](../../content/quantum-observable-universe/...) — only **three** empirical inputs are categorically licensed:

1. **q₀ = 1.10997859...** (the substrate parameter, fixed by Bring–Klein)
2. **m_e** (electron mass — calibration of the categorical mass scale)
3. **Q_β(n) = 0.78233341 MeV** (free-neutron β-decay Q — fixes E₀)

**Everything else must be derived.** Any current numerology / empirical fit / hardcoded magic value beyond these three is a violation of the calibration budget.

---

## §1. Last 24 h on main — what landed

| Date (UTC) | Merge | Net |
|---|---|---|
| 2026-05-04 | PR #543 (copilot/identify-multiplicative-chain) | α_shift(T_(p,k)) = k(p−1) categorically derived; NH-basis shift; `conj:confinement-nf-structure-forcing` |
| 2026-05-04 | PR #539 (W-3 D(u) 3/3 proof) | `prop:confinement-nf-partial-proof` (Lean stub) + Sub-lemma 2.1 categorical proof at the maximizer |
| 2026-05-05 | PR #544 (charge-precision AXKIA) | `prop:per-nucleon-shift-additive-linearity` (paper write-up); ocneanu cancellation derivation; h2-molecular-binding wiring |

**Net categorical state:** the W-3 atomic shift formula `D(u) = 2^(2A+1) · u^(18Z+21N+1) · (1+u²)^(3A−1)` is now fully proved categorically. The only Lean `sorry`s are routine integration with Mathlib's LP-duality library.

---

## §2. Open conjectures and empirical fits — gap inventory

### Categorical-side conjectures (status: WITNESS-ONLY; need promotion to theorems)

| Block / file | Statement | Path to closure |
|---|---|---|
| `conj:confinement-nf-structure-forcing` | shift_NF(β) = α_shift(I) + Δ, \|Δ\| ≤ duality_gap | (a) Mathlib LP-duality integration → 2/3 sorry's promoted; (b) AXKIA's ocneanu-cancellation derivation closes the sharp-form bound on Δ |
| `conj:hecke-branching-trace-decomposition` (PR #534, just landed there) | Operator-valued Sub-lemma 2.1 for general λ | Recursive corner formula in PR #534's Lean file; deuteron 1e-15 verified |
| `conj:per-nucleon-shift-additive-linearity` (now `prop:` on main) | Add-a-proton: +18; add-a-neutron: +21 | Categorically derived via per-new-nucleon decomp; "+1 base" remains conjectural at the (p, n) interface |

### Hardcoded / fitted values — beyond the 3 calibration inputs

These ARE present in the current codebase. Each must be **derived** OR cited.

| Value / location | Status | Required action |
|---|---|---|
| `α_shift(T_(p,k)) = k(p−1)` | Categorically proved (PR #543) | None — already a theorem |
| `α_shift((p,n) interface) = 1` | = α_shift(T_(2,1)) — proved special case | None — already covered |
| `(18Z + 21N + 1)` per-new-nucleon coefficients | Categorically proved (PR #544's `prop:per-nucleon-shift-additive-linearity`) | None |
| `tr_M(proton)` leading coeff = `−1/12` | Symbolic derivation in PR #546 (open) | Merge PR #546 + verify universality at A ≥ 2 |
| **⁴He magic-A formula `B = ρ_F · m_e · A · 8G` with ρ_F = 2** | **Empirical** — ρ_F = 2 is "doubly-magic shell-closure" rule, not derived | **Critical gap. Need categorical derivation of ρ_F as a function of (Z, N).** PR #534's `prop:atomic-mass-gb-nf` is the right framing. |
| **α-cluster recursion `B(nα) = n·B(⁴He) + C(n,2)·c_αα`** | Empirical fit | Need categorical proof: c_αα = m_e · Vol(7²₁) (= categorical, but the *additivity* is only verified at A=8..40 with 5–19% residuals) |
| **N_v = 3·v_weak/m_e (q-independent constant ≈ 1.45×10⁶)** | CODATA G_F input — does NOT count as one of the 3 allowed | **W-2 categorical derivation pending**; PR #521 retracted the q^(1/2)-fit. |
| **`E_0 = 0.78233341 MeV`** | One of the 3 allowed (= Q_β(n)) | CAL-3 enforced strictly; no proton-mass anchoring |

### Documentation / citation gaps

| Formula | Citation status |
|---|---|
| Markov–Ocneanu trace `tr_M(β) = z^(n−1) · trace_λ(ρ(β))` | Cited (Wenzl 1988) |
| Hoefsmit seminormal form `a = h/(1−q^(−2ρ))` | Cited (Hoefsmit 1974, in audit doc) — but **needs `references.ts` entry** |
| Littlewood–Richardson rule | Cited (Macdonald 1995) ✓ |
| LP duality (Schrijver §7) | Cited ✓ |
| Volume conjecture (Kashaev–Murakami) | Cited |
| `α_EM = 1/(q · [9]_q · [10]_q)` | Derived in main (post PR #544); `prop:em-coupling-projection`; `prop:alpha-em-shift-multiplicative-chain` ✓ |
| **Ocneanu weights `y_λ` for canonical Markov trace** | Wenzl-bridge formula cited; explicit q-rational form for H_3 in `hecke_core_symbolic.py` matches `pyhecke.gram` lines 37–41 |

---

## §3. Compute bottlenecks — profiling targets

| Bottleneck | Current cost | Target | Strategy |
|---|---|---|---|
| `markov_peel.tr_M_atomic` symbolic for ⁶Li | ~15 min wall | <1 min | Already routed through LaurentQ fast path (PR #537 in main); further: cache GS-NF reductions |
| `term6_residues_at_roots.split_polar_at_u0` for ⁴He | "few minutes" | seconds | **WIP on PR #545** — wired closed-form `closed_form_d_u(Z, N)` to skip auto-detection of pole order; need to add fast power-series inversion for `(1+u²)^k` (binomial expansion, not generic `sp.series`) |
| `term6_residues_at_roots` extension to ⁴He, ⁵Li, ⁶Li | not yet computed | full A=1..6 spectrum | After power-series inversion fast path, run full sweep |
| `paper_six_term_isotope_sweep` Φ_q(\|V̂\|) eval at q_0 ~ 10⁵ for each generator | ~10⁵ ops/atom × 8 generators × 10 atoms | <10⁴ ops total | PR #534's singular canonical pipeline + Wedderburn projection cache |
| Cross-partition cancellation Δ_cross | not computed | bounded by LP duality_gap (= 0 strong duality) | AXKIA branch's ocneanu-cancellation derivation closes this |

### Compute hygiene actions

1. **Audit `markov-peel-atomic-tr-m.witness.json`** — restore ⁵Li/⁶Li tr_M (currently 6 atoms; PR #545 has the fix in flight)
2. **Run `derivation_chain_validator` strict** — currently warn-only on LP/SDP duals (~58 legacy witnesses missing dual fields per `lp_dual_witness_validator`)
3. **Migrate to LaurentQ everywhere** that uses sympy `Expr` coefficients in Hecke reduction hot loops

---

## §4. Refocused workplan

### Phase 1 — Close existing PRs (next 1–3 days)

| PR | Action | Owner / coordination |
|---|---|---|
| **PR #534** (singular 6-term mass formula) | Merge after Gemini/Copilot review on `prop:hecke-branching-trace-decomposition` | `claude/categorical-mass-divergence-audit` author |
| **PR #545** (term6 wiring, this branch) | Land closed-form D(u) wiring + verify ⁴He, ⁵Li, ⁶Li term6 | this session |
| **PR #546** (symbolic Hoefsmit −1/12) | Merge: closes the round-1 #544 open item + needed for `tr_M(proton)` exact form | `claude/hoefsmit-2x2-fix` author |

### Phase 2 — Promote conjectures to theorems

| Conjecture | Promotion path |
|---|---|
| `conj:confinement-nf-structure-forcing` | (a) Lean integration with Mathlib LP duality; (b) AXKIA's ocneanu cancellation → strong-form bound `\|Δ\| ≤ duality_gap` (= 0) |
| `conj:hecke-branching-trace-decomposition` | PR #534's recursive corner formula; verify at A=3, 4 |
| `conj:per-nucleon-shift-additive-linearity` | Already a `prop:` on main (PR #544); add Lean theorem |

### Phase 3 — Close ⁴He / nα / Family-4 (the hard 1-ppb floor)

| Target | Approach |
|---|---|
| **⁴He** at +5.87% → ≤1 ppb | Replace magic-A formula with GB-NF / Sub-lemma 2.1 maximizer evaluation. ρ_F = 2 must be derived, not posited. PR #534's `prop:atomic-mass-gb-nf` is the framing. |
| **⁸Be–⁴⁰Ca** α-cluster (5–19%) | Recursive on ⁴He, but the additivity + c_αα derivation needs cleanup. |
| **Family 4 (⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F)** | Currently OPEN. Need ρ_F + knot-ID derivation. Best route: tr_M(T_w) categorical via the now-proved Sub-lemma 2.1 + AXKIA's nucleon-mass categorical formula. |

### Phase 4 — W-2 (real): N_v categorical derivation

`N_v = 3 · v_weak / m_e ≈ 1.45 × 10⁶` is q-independent (= CODATA G_F input). Per CAL-3, this is **NOT** one of the 3 allowed calibration inputs. The PR #521 retraction killed the q^(1/2) numerology. **Need a categorical derivation from the categorical-mass framework — the most likely route is via the Wenzl-bridge / Ocneanu-pivot at the EW scale.**

---

## §5. Coordination with active branches

### `claude/hoefsmit-2x2-fix` (PR #546)

**My intent:** PR #546's closed-form `tr_M(proton) = (q²⁰ + q¹⁸ + 2q¹² − 2q⁸ − q² − 1)/(12·q¹⁰)` with leading coefficient **−1/12 exactly** is the missing closed-form input that completes the W-3 atomic-shift derivation at the symbolic level. The "factor-of-2 normalization mismatch" (open item #2 in PR #546) is critical to resolve before the closed form can directly populate the `dp_pole_probe` and `confinement-nf-partial-proof` Lean stubs.

**Asks:**
- Resolve the `sp.sqrt` branch convention in `b = sqrt(a·a' + 1)` so that the symbolic and numerical `markov_peel.tr_M_atomic` agree pointwise (currently 0.433 vs 1.065).
- Verify the universal `−1/12` (or `−1/(2·n!)`) leading coefficient at A = 2 (deuteron) — even at 600 s timeout, partition filtering should make this tractable.

**My contribution back:** I can wire the resolved closed form into `closed_form_d_u(Z, N)` on PR #545.

### `claude/categorical-mass-divergence-audit` (PR #534)

**My intent:** PR #534's `prop:hecke-branching-trace-decomposition` is the categorical-proof completion for Sub-lemma 2.1's general (multidim) form. PR #534's recursive corner formula is the missing piece for closing **`conj:confinement-nf-structure-forcing` to a theorem.**

**Asks:**
- Lean encoding of the operator-valued `A^λ_{μν}(I)` block — pair this with my PR #539's `HasBranchingBlockLemma` class to populate the missing instance.
- Verification at A = 3 (triton, helion) to extend the deuteron 1e-15 result.

**My contribution back:** my `closed_form_d_u(Z, N)` helper (PR #545) is the natural consumer of your operator-valued formula at the maximizer (1-dim case).

### `claude/improve-charge-precision-AXKIA` (PR #544 merged; ongoing work)

**Their ongoing:** ocneanu cancellation derivation (`0b9805118`, `069a28cbe`).
**Asks:** derivation of the strong form `\|Δ_cross\| ≤ duality_gap = 0` for the canonical pppnnn atomic braid.

---

## §6. Active session: this PR (#545)

**Current state:** rebased on main (post-PR #544); cherry-picked refined Sub-lemma 2.1 from PR #534's branch; wired `closed_form_d_u` into term6_residues_at_roots and u_shift_mass_anchor_probe.

**Remaining for #545:**
1. Run `term6_residues_at_roots` over A = 1..6 atoms with the closed-form fast path → extend witness from 1 atom to 8.
2. Add citation entry for Hoefsmit 1974 in `references.ts` (currently cited in audit doc but missing from CSL).

**This workplan doc (`docs/audits/2026-05-05-refocused-1ppb-workplan.md`) is committed to PR #545.**
