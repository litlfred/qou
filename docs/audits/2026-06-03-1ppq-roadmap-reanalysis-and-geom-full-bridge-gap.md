# 1ppQ roadmap reanalysis — Geom_full bridge gap + multi-option plan

**Date:** 2026-06-03
**Session:** post-PR #1748 merge (chi-cache MPFR rayon kernel landed)
**Trigger:** owner request for "thorough analysis with several options for plans of attack" on the 1ppQ path, with focus on the **Geom_full bridge formula derivation gap**.

> **Status header.** Working draft on a fresh branch
> (`claude/1ppq-roadmap-reanalysis-2026-06-03`). Sections 1-5 below
> are based on session-gathered evidence; the literature analogies
> in §6 are produced by a parallel background research agent and
> get appended on completion. Branch + PR open for review BEFORE
> the lit section lands — early visibility per ALWAYS-PR.

---

## 1. Where the framework actually is (last 4 weeks)

### 1.1 Precision-goal status (snapshot 2026-06-03)

| Leg | Target | Status |
|-----|--------|--------|
| **L1** (compute precision, internal cross-method) | ≤ 1 ppQ = 10⁻¹⁵ | **met** (65 dps compute, 50 dps serialization, dashboard reports `max_rel_delta = 0.0` across 8 atoms) |
| **L2** (per-observable accuracy, ≤ σ_exp / 100) | 7 observables; target hits CODATA σ/100 | **0 of 5 genuine predictions met** (m_p / m_e are anchors; m_μ, Q_β, m_n, Δ_pn, m_K/m_π all miss) |

Headline pieces of the L2 miss:

- **m_μ** misses by **963.6×** (209.8 ppb vs 0.2177 ppb target). Post-re-pin (the 2026-05-28 proton-anchor swap) m_μ became a *prediction* rather than a calibration anchor; the μ-p floor is independent of the Q_β chain.
- **Q_β** misses by **164×** (1279 ppb vs 7.8 ppb target). Earlier "Habiro-exact 5.7 ppb" claim was against the pre-re-pin q₀ and is stale.
- **m_n, Δ_pn, m_K/m_π** — also miss; share a single root cause per [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md).

### 1.2 Recent settled / advanced wins (last ~4 weeks)

| Theme | Status | Where |
|---|---|---|
| **Q_β Habiro pre-archimedean recursion** | Settled: explicit 3-term recursion for τ_M(T_β) Markov-parameter coefficients (PRs #1739, #1750, #1752 + main `21e599dbf2`, `b280903a4b`, `fd30d71d5c`). c_k are now derived, not fitted. | qbeta/* |
| **T_β = S·𝟙 (Markov-trace SHAPE collapse)** | Proved in paper + Lean (sorry-free) (`fd30d71d5c`). Major structural finding. | qbeta/* |
| **α_EM RT phases 2/3/4** | Schwinger structural derivation (1−h²α from 2-vertex Hecke), 1/(8π) = 1/(π·dim H¹(M_Bring)) identified (PRs #1538, #1549, #1552). | brings-surface/, alpha-em/ |
| **§3b-cond strengthening** | 5 substrate→EW empirical hypotheses bundled into classes; downstream theorems no longer leak `True := trivial` (merged PR #1736). | content/ |
| **Single-rank q-Pochhammer ansatz** | Closed: BOTH universal and doubly-magic forms refuted (PR #1733 + my analytic refutation `be12ac28a7` on the same branch). q^{r(r+1)/2} super-exponential growth at q>1 makes any `r=4A-1` rule break catastrophically at A ≥ 16. | folio-assistant/computations/alpha_r_* |
| **Bar-pairing observable** | Bar-length underbinds monotonically D −70 % → ⁴He −98 % (PR #1742 + my #1748 extension). Reinforces "archimedean observation = |χ(q_0)|" structural conclusion. Surprise: B_arch ALSO fails past D. | folio-assistant/computations/bar_pairing_* |
| **chi-cache MPFR rayon kernel** | PR #1748 (merged today): ⁴He chi-cache regen feasible at 10.4 min wall (was effectively infeasible). Unblocks #1742, #1733, #1726, #1731 downstream. | tools/hecke-engine/, folio-assistant/computations/chi_at_* |
| **α-cluster Phase 2 wire-up** | NEW (`dc3a01bc5c` on main, today): α-cluster recursion in `try_binding_canonical` improves 7 isotopes by **10×**. | folio-assistant/computations/try_binding_canonical |
| **`|content|`(λ) scalar candidates** | 4 of 5 falsified (PR #1746). Only candidate 1 (trace of `|Ω_q|`) remains, with basis-convention objection. **Δ_λ-gate discipline sharpened:** "no more scalar combinatorial candidates for `|c|(λ)`". | docs/coordination/2026-06-02-abs-content-hecke-energy-scoping.md |

### 1.3 The frontier is **step 9 of the canonical chain**

Per [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §0, steps 1-8 are settled or in proof-cleanup. The frontier is two parts of step 9:

- **9a. Mass identity per atom.** Production uses `m_e × Geom_full(K = 𝓑₃, q₀)` — i.e. the proton's knot — for **ALL atoms**. The Vol(𝓑₃) uniform usage covers **64 of 65 atom-touching scripts** per [`docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`](2026-06-02-vol-usage-audit-uniform-vs-per-knot.md). Even at the proton, the formula uses an `H_4` dimension count where the proton's braid lives in `H_3` — see §3.
- **9b. Per-isotope binding `B(K)` (the Δ_λ closure).** Six closure ansätze refuted on the deuteron (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov). Track-A blocked. Productive directions: GAP-A-3 / GAP-A-4 (categorical brane-tower level selection / ρ general rule) and Option E (Kashiwara crystal).

---

## 2. The user's "derivation gap on the bridge formula around Geom_full"

The user named this gap directly. Below is its anatomy, with the math made explicit.

### 2.1 Two competing forms of `Geom_full` are alive in production

**Form 1 — `geom_full_borromean(q)` (the production-installed scalar):**

```
m(K) ?= m_e × Vol(K) / ℏ_q² × linking_weight_family_a(q)
      = m_e × Vol(K) / ℏ_q² × (5/2 + 3h²/4)            [h = q − q⁻¹]
```

`linking_weight_family_a(q) = (1/4) Σ_{λ ⊢ 4} dim_q V_λ` is the **H₄ Wedderburn count**: an algebraic constant landing ~2.53 at q_0.

- Proven Family-A categorical identity (`lambda-scale-substrate-form.lean`).
- At proton: lands m_p = m_e × Vol(𝓑₃) / ℏ_q² × 2.53 ≈ 965 MeV, **+2.89 %** over the CODATA 938.27 MeV.
- Used as the production mass formula for **every atom** (`geom_full_borromean(q)` is called uniformly).

**Form 2 — `geom_full_per_block(vol_K, tr_M_K, q)` (the paper-faithful per-knot sum):**

```
m(K) ?= m_e × Vol(K) / ℏ_q² × tr_M(K, q)
      = m_e × Vol(K) / ℏ_q² × Σ_λ w_λ χ^λ(β_K) / dim λ      [sum over λ ⊢ n_K]
```

`tr_M(K, q)` is the **per-knot Markov trace** over partitions of the knot's own strand count `n_K`.

- Stage 4 of `prop:hoefsmit-scattering-pipeline` (the "paper version").
- At proton (n_K = 3, H_3): tr_M(𝓑₃) ≈ 1.065 → m_p ≈ 405 MeV, **−57 %** off CODATA.
- PR #1756 just confirmed this fails RED across all 6 atoms (mean abs err 80.7 %).

**The ratio** between the two: 2.53 / 1.065 ≈ **2.38×**. That ratio is exactly what makes Form 1 land near the right answer at proton and Form 2 catastrophically off.

### 2.2 What the inconsistency *means*

The H_4 count `(5/2 + 3h²/4)` appears as `(1/4) Σ_{λ ⊢ 4} dim_q V_λ` — i.e. it sums over partitions of `4`. **But the proton braid lives in `H_3`** (3 strands, the Borromean rings). So Form 1 is **mixing strand counts**: it computes Vol of a 3-strand object but linking-weight from a 4-strand Wedderburn.

Form 2 fixes the strand-count consistency (uses `H_3` throughout for the proton) — but the numerical answer is wrong.

So the actual derivation question is:

> **What is the categorical reason that `(1/4) Σ_{λ ⊢ 4} dim_q V_λ` should appear in the proton mass formula, given that the proton braid lives in `H_3`?**

The cheat-sheet's own framing ([`docs/lambda-scale-absorbed-into-geom-full.md`](../lambda-scale-absorbed-into-geom-full.md)) acknowledges this: the `2.46` value (= what would make the formula round-trip m_p exactly) is "a CODATA-implied-λ near-match". The 2.53 from Family-A is a near-match for 2.46 — coincidence or structural?

### 2.3 Hypotheses for the H_3 → H_4 jump

Four hypotheses, only one currently has a derivation chain:

| # | Hypothesis | Derivation? | Predicts? |
|---|---|---|---|
| H1 | `H_4` is the **canonical extension** of `H_3` via Markov stabilization: adding a free strand to a closed braid. The Family-A linking weight is what the extended trace evaluates to in the limit of "no new entanglement". | Partial. Markov stabilization theorem says `tr_M(σ_n) = z·tr_M(β)` for `β ∈ H_n`. So `tr_M(𝓑₃ ⊗ 𝟙)` in `H_4` = `z·tr_M(𝓑₃)`, NOT the half-Wedderburn count. **This doesn't directly give 2.53.** | — |
| H2 | `(5/2 + 3h²/4)` is the result of a **resolution-of-identity / quantum-dimension sum** over the *target* Hilbert space `V^{⊗4}` after braid action. The mass formula is `〈𝟙\| ρ(𝓑₃) ⊗ 𝟙_extra \|𝟙〉` over the extended space. | Hand-wavy: the H_4 count "appears" because adding the lepton fibre extends the substrate by one strand. **But the framework has no explicit `〈𝟙\|ρ\|𝟙〉` identity that ties to 2.53.** | Should reduce to tr_M on the original H_3 (with a known correction). It doesn't. |
| H3 | `(5/2 + 3h²/4)` is a **renormalization constant** — the mass formula's "Wilson coefficient" — and its proper derivation goes through the brane tower contributions `T_2 = −Σ Li_2^q(...)`, `T_3 = ...`. The H_4 dim count is the LEADING term of an expansion. | Not done. The brane tower exists in code (`mass_endomorphism_tower.py`) but its summation hasn't been shown to recover Family-A as the leading-order term. | Yes, would explain why proton lands at +2.89 % and not 0 % — H_4 is leading-order. |
| H4 | The formula is **wrong as stated.** The proton's actual canonical form is some other knot-dependent expression that *evaluates to* m_e · Vol(𝓑₃)/ℏ_q² · 2.46 (within 2.89 % round-off). The Family-A coincidence is a numerical accident that the framework anchored on accidentally. | None. | Yes — predicts a different formula. Would invalidate all current Lean proofs of `linking_weight_family_a`. |

**My read** (without lit input yet): H3 looks most likely structurally — the brane tower exists, its summation hasn't been done, and Bar-pairing (#1742) + per-knot demo (#1756) both find that *first-order* per-block sums miss by ~50-90 %, suggesting higher-order corrections are needed. But H1 + H2 + H4 are open and worth probing.

### 2.4 The Vol(β_K) data gap (Step 9a wire-up)

Even *if* the linking-weight question above resolves, the per-knot wire-up of `Vol(β_K)` for atoms A ≥ 2 is unfinished:

- `mass_table_comprehensive.py:99-111` explicitly TAGS deuteron, T, ³He as `"manual-historical-volume-match"` (i.e. KLUDGE-tagged)
- No Python script currently produces `Vol(β_K)` for `K = atom_braid_word_3A(Z, N)`
- SnapPy could compute these (`Manifold(...).volume()`) but isn't installed in the current container

This is **infrastructure**, not math. Plugging in SnapPy + computing 4-5 Vol(β_K) values per atom is mechanical. But until done, every per-knot attack is hamstrung.

---

## 3. The Δ_λ closure gap (Step 9b)

Different from §2's mass-formula gap. The per-isotope binding-energy formula is:

```
B(K) = m_e × Σ_λ y_λ χ^λ(β_K) Δ_λ
```

where `Δ_λ` is a per-partition weight that's currently **unknown**. Six closure ansätze refuted on the deuteron alone (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov).

The discipline (CLAUDE.md §"Precision goals" / Δ_λ gate) **forbids** another scalar combinatorial guess — the productive directions are:

1. **GAP-A-3 / GAP-A-4**: categorical brane-tower level selection / ρ general rule
2. **Option E**: Kashiwara crystal (PR #1697 / #1516 / #1709)
3. **Operator-valued LR branching combiner** (PR #1443): per-channel decomposition that avoids the scalar collapse — this is the framework's bet that **the wrong question is "what scalar Δ_λ"**, the right one is "what operator-valued combiner replaces the scalar?"

The α-cluster Phase 2 wire-up (`dc3a01bc5c`, today) hits 7 isotopes at 10× better than baseline. This is **partially** Δ_λ-adjacent — α-clustering builds B(⁴⁺α) tower from D + α + d/p/n recombination terms. Cluster of two pieces:
- The recursion structure is categorically motivated (not fit)
- The per-cluster scale factors are still partially anchored on AME values
- 10× improvement says *something* about per-isotope binding structure, but the categorical derivation chain to `B(K) = m_e × Σ y_λ χ^λ Δ_λ` is not yet closed

**My read:** The α-cluster wire-up is the closest active progress on Δ_λ. It's worth understanding whether the cluster-recursion form maps to a canonical Δ_λ structure or whether it's an empirical near-match — and that mapping is the test of whether α-clustering closes Δ_λ or is orthogonal.

---

## 4. The full list of L2 gaps + which structural piece each maps to

| Observable | L2 miss | Maps to | Productive lever |
|---|---|---|---|
| m_μ | 963.6× | μ-p floor, independent of Q_β chain | m_μ lepton torus-tower (PR #1753) |
| Q_β | 164× | post-re-pin staleness + c_k truncation order | Habiro element identification (PR #1739 ongoing) |
| m_n | unknown | shares root with Q_β, Δ_pn | same as Q_β |
| Δ_pn | unknown | p-n flavor asymmetry; Bring color-weighted | `bring_color_weighted` in `closed_form_tau_M.py` |
| m_K/m_π | unknown | meson sector via `meson_geom_full.py` | meson Geom (related to §2 main gap) |
| m_p | met (anchor) | substrate anchor | — |
| m_e | met (anchor) | CAL-1 | — |

**The §2 Geom_full bridge gap is the bottleneck for m_n, Δ_pn, m_K/m_π** — all three depend on the per-knot mass formula. So §2 isn't just about m_p +2.89 %; it gates **three of the five missing L2 observables**.

---

## 5. Multi-option attack plans

Five options, ordered roughly by depth-of-bet (shallow → deep):

### Option A — Wire up `Vol(β_K)` for the light series (infrastructure-only)

**What:** Install SnapPy (or use `knot-volumes.py` if it already has the kernel), compute `Vol(β_K)` for K ∈ {β_D, β_T, β_³He, β_⁴He}, wire those values into `geom_full_per_block(vol_K, ...)` instead of `geom_full_borromean(q)` uniform.

**Cost:** Low (1-3 days, mostly SnapPy install + 4-5 SnapPy queries + script changes).

**Win:** Doesn't fix the math gap, but **separates the Vol-uniform bug from the linking_weight question**. After this, we can ask "given the right Vol(β_K), does Form 2 still fail RED?" — which it must (because the failure was at the proton already where Vol(𝓑₃) IS correct).

**Risk:** None — pure infra cleanup. May reveal that Form 2 fails LESS catastrophically with correct Vol(K), which would shift the question to "Form 2 is right modulo a constant rescaling" — and the constant might be exactly `(5/2 + 3h²/4) / tr_M(𝓑₃)`.

**Verdict:** Should be done regardless of which other option is pursued. Cheap and disambiguates.

### Option B — Test H3 (brane-tower expansion gives Family-A as leading)

**What:** Compute the full brane tower `m(K) = m_e × Σ_n T_n(K, q)` where `T_n` are the n-th order brane corrections from `mass_endomorphism_tower.py`. Test whether truncation at `T_0` gives Family-A `(5/2 + 3h²/4)` and whether `T_0 + T_1 + ...` recovers the missing +2.89 % at proton.

**Cost:** Medium (1-2 weeks). The brane tower code exists; the open question is "what's the canonical truncation order, and how does it factor through Family-A?"

**Win:** If yes, this **derives** the H_4 count as a leading-order brane-tower expansion. That fixes the Form 1 / Form 2 inconsistency: Form 1 IS the per-knot result, just truncated to leading order. The +2.89 % is then **explainable** as the truncation error.

**Risk:** The brane tower might NOT factor through Family-A. In that case Form 1 is genuinely a non-canonical near-match, and H3 is refuted.

**Verdict:** High-information experiment. Worth doing.

### Option C — Test H2 (Hilbert-space resolution-of-identity)

**What:** Build the explicit `〈𝟙 \| ρ(𝓑₃) ⊗ 𝟙_extra \| 𝟙〉` identity claim: does there exist a canonical extension `𝓑₃ ⊗ 𝟙` to `H_4` whose Markov trace IS `Vol(𝓑₃) × (5/2 + 3h²/4)`?

**Cost:** Medium-high (2-3 weeks). Needs explicit Hilbert-space construction in H_4 + a categorical projection back to H_3 measurements.

**Win:** If yes, derives the H_4 jump from Markov-stabilization + adjunction.

**Risk:** Markov stabilization gives `z·tr_M(β)` not `Family-A·tr_M`. So this hypothesis is *prima facie* wrong unless the "stabilization" is the wrong language and the extension is something more subtle (e.g. ribbon or fusion).

**Verdict:** Lower-priority than B unless lit review surfaces a specific construction.

### Option D — Categorical brane-tower level selection (GAP-A-3 / GAP-A-4)

**What:** The Δ_λ-closure productive direction. Define a canonical level (highest weight of the brane tower at given A) and predict B(K) from it. PR #1697 / #1516 / #1709 has scaffolding; needs Kashiwara crystal Option E to land.

**Cost:** High (4-6 weeks, depends on PR #1443 operator-valued combiner).

**Win:** Directly attacks Δ_λ. If it works, fixes B(K) for all A.

**Risk:** Operator-valued combiner not yet built. Δ_λ has resisted 6 prior closure attempts.

**Verdict:** The strategic "right answer" per cheat-sheet, but expensive.

### Option E — Look outside the framework (literature analogy)

**What:** Find an analogous problem in the math/physics literature where a categorical chain produces an MeV-scale observable from a hyperbolic invariant — and import their machinery. Candidates: volume conjecture, complex volume, Khovanov-Rozansky, Habiro ring, asymptotic expansions of quantum invariants near q → 1.

**Cost:** Variable. Pure-lit scan: days. Concrete import: weeks-months.

**Win:** Might surface a derivation chain we haven't tried. Or confirm that what we have is essentially novel and the work to do is internal.

**Risk:** Could be a rabbit hole.

**Verdict:** Worth doing in **parallel** with B — running lit scan as background-research agent NOW (see §6 below when it lands).

---

## 6. Literature analogies — placeholder

A parallel background-research agent (`a42dee546fc7df05b`) is surveying the math/physics lit for analogous "categorical-invariant-to-MeV-observable" bridges across 6 directions:

1. Volume conjecture / complex volume (Kashaev, Murakami, Andersen-Hansen, Yokota)
2. Chern-Simons / Bloch-Wigner dilogarithm L²(z)
3. Quantum group categorification (KhR_n)
4. TQFT-to-classical limit analytic continuation (Witten, Gukov)
5. Habiro ring / cyclotomic completion (Habiro 2004, Garoufalidis)
6. Asymptotic expansions near q → 1 (Andersen, Garoufalidis-Levin)

Will append when complete. Sections 1-5 above don't depend on this — they're based on session-gathered codebase + audit-doc evidence.

---

## 7. Recommended order

If the user is asking "what next":

1. **Option A immediately** (~1-3 days) — gives clean per-knot Vol data; cheap; disambiguates the Form 1 / Form 2 question.
2. **Option B in parallel** (~1-2 weeks) — high-information; tests whether the brane tower factors through Family-A.
3. **Lit scan (§6) in background** — wait for the parallel agent; integrate its findings on Habiro / volume-conjecture analogies into Options B and C.
4. **Option D (operator-valued combiner)** — the strategic long-game; needs PR #1443 to land. Track it but don't gate on it.

Three branches of work, ~6 weeks total compute to a much-better understanding of the Geom_full bridge.

The key reframe from this analysis: **Geom_full is the bottleneck for 3 of 5 missing L2 observables (m_n, Δ_pn, m_K/m_π), not just m_p**. Closing it has wide leverage.

---

## Coordination

This analysis doc lives on branch `claude/1ppq-roadmap-reanalysis-2026-06-03`. PR open for owner triage of the Option A/B/C/D/E split. No production code touched.

Related coord ledgers:
- [`docs/canonical-derivation-cheat-sheet.md §9a, §9b`](../canonical-derivation-cheat-sheet.md)
- [`docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`](2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)
- [`docs/precision-goals.md`](../precision-goals.md)
- [`docs/lambda-scale-absorbed-into-geom-full.md`](../lambda-scale-absorbed-into-geom-full.md)
- [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)

Active sibling PRs that this analysis names:
- PR #1739 (Q_β Habiro recursion)
- PR #1752 (Q_β SDP strict-complementarity)
- PR #1753 (m_μ lepton torus-tower)
- PR #1754 (Nuclear A=3 binding tranche)
- PR #1756 (per-knot 6-atom RED verdict — referenced as the empirical confirmation of the Form 2 failure)
