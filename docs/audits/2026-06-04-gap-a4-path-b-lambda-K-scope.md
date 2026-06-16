# GAP-A-4 — Path B per-atom λ(K) substrate-derivation

**Date:** 2026-06-04
**Audit type:** research-grade scoping for the productive direction identified in the just-merged consolidated audits (#1864) and reinforced by PR #1870 (deuteron P_λ probe REFUTED, synthesis points to GAP-A-4).
**Status:** scoping doc. No probe in this PR.
**Sibling chain:** #1816 → #1841 → #1850 → #1853 → #1860 → #1864 → #1868 (GAP-A-3 scope) → #1870 (GAP-A-3 deuteron P_λ — all channels refuted) → **this PR (GAP-A-4 scope)**.

---

## §1. Why GAP-A-4 now

The just-completed [PR #1870 deuteron P_λ probe](https://github.com/litlfred/qou/pull/1870) refuted **all five natural brane-tower content channels** for the per-partition projection `P_λ(D)`. Combined with [#1860 (Kashiwara, 5/5 refuted)](https://github.com/litlfred/qou/pull/1860) and the six prior Δ_λ-gate failures, that's **14 no-fit closure attempts** for `Δ_λ` — none works.

Yet the [Δ_λ Phase-4 amplitude](./2026-05-19-delta-lambda-phase4-z4N-closure.md) `A(K) = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}` is substrate-derived to ≤ 2.5 % across D, T, ³He, ⁴He with **zero free parameters** — the per-atom layer works.

The structural reading: **don't decompose at the per-partition layer; close per-atom directly.** That's exactly what Path B (Borromean tower extension) does, and `λ(K)` is its gate. GAP-A-4 is the natural next probe.

## §2. Path B vs Path D

From the [Δ_λ-gate audit](./2026-05-18-delta-lambda-gating-context.md) table:

| Path | Formula | Gate |
|---|---|---|
| **B. Borromean tower extension** | `m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)` | **per-atom λ(K) substrate-derivation** ← GAP-A-4 |
| D. ρ_K · m_e · \|tr_M\| (canonical) | `M = ρ_K · m_e · \|tr_M\|`, `ρ_K = ρ_K^{LO} + (1/\|tr_M\|) Σ y_λ χ^λ Δ_λ` | Δ_λ ← exhausted by 14 no-fit attempts |

Path D was declared canonical in [PR #564](https://github.com/litlfred/qou/pull/564) (T6-unit-convention resolution). Path B was preserved as an alternative. After 14 negatives on Path D's `Δ_λ` gate, Path B's `λ(K)` is the structural pivot.

The Δ_λ-gate doc notes: *"Reverting Path D in favour of Path B (Borromean tower extension) would bypass the Δ_λ gate at the cost of opening the per-atom λ(K) derivation problem — which the framework is already working on for individual baryons (#751)."*

## §3. Empirical λ(K) for the light series

Inverting Path B at q₀:

`λ(K) = m(K) · ℏ_q² / (m_e · Vol(K))`

**Anchors used in this section** (so the numbers are reproducible):
- `q₀` is the canonical substrate parameter `1.1099785827513808075916690956107688798744991218736` (50-dps; the value pinned in every chi-cache witness header, e.g. [`chi-proton-h3-at-q0-50dps.witness.json`](../../computations/chi-proton-h3-at-q0-50dps.witness.json), and matching `substrate/q_parameter.py:Q_50_DIGIT_STR`).
- `Vol(K)` in the inverted formula `λ(K) = m(K)·ℏ_q²/(m_e·Vol(K))` is **specialised to `Vol(𝓑₃) = 8·G` (the proton's small-knot Borromean volume)** for every atom in the table below — this is the *uniform-Vol* convention production currently uses (`vol_density_borromean`); the table therefore measures the gap between empirical mass and the uniform formula, NOT a per-atom Path B closure (which would use per-knot Vol_hyp; see §3 note).

Using PR #1816's data: `geom_uniform(q₀) = Vol(𝓑₃)/ℏ_q² ≈ 1890.51` so `m_e · Vol(𝓑₃)/ℏ_q² ≈ 966.05 MeV` per unit-λ (i.e. uniform `λ = 1` would predict every nucleon mass as 966.05 MeV). For the light series:

| atom | m(K) CODATA | m(K) / 966.05 = λ_uniform | empirical λ(K) (per-atom Path B) |
|---|---|---|---|
| p | 938.272 MeV | 0.9712 | **0.9712** |
| n | 939.565 | 0.9726 | **0.9726** |
| D | 1875.61 MeV total; per-nucleon m(D)/A = 937.81 | 0.9708 / nucleon | per-atom interpretation needs Path-B reformulation |
| ³He | per-nucleon ≈ 936.13 | 0.9690 | ditto |
| ⁴He | per-nucleon ≈ 931.84 | 0.9646 | ditto |

The proton's empirical `λ(p) ≈ 0.971` is suggestively close to **1 − ε** with `ε ≈ 0.029` (≈ the +2.89 % gap noted in the `vol_density_borromean` docstring at [`computations/_li_2_q_util.py`](../../computations/_li_2_q_util.py), search for *"the 2.53 is a CODATA-implied-λ near-match that lands near λ = m_p / (m_e·Vol/ℏ²) ≈ 2.46"* — line numbers may drift but the docstring is the canonical reference). If λ(K) factors as `1 − ε(K)` with ε(K) a small substrate-derived perturbation, the per-atom Path B formula closes to leading order.

**Note on the per-atom Path B re-derivation for A ≥ 2.** Path B's `m(K) = m_e · Vol(K) / ℏ_q² · λ(K)` was originally formulated for single-baryon masses (PR #751). For compound atoms (D / T / ³He / ⁴He), the Path B formulation needs `Vol(K)` to mean the *atomic-braid-closure* hyperbolic volume (matching Phase-4's `Vol_hyp` convention) rather than the small-knot Borromean volume. This re-formulation isn't yet on main — the §4 probe scopes its first step.

## §4. Cheap formalize-first probe direction

Per [PR #1826](https://github.com/litlfred/qou/pull/1826), narrow before scanning. Three candidate forms for `λ(K)`, all substrate-derived:

| Candidate | `λ(K)` form | Substrate-derivation route |
|---|---|---|
| **L1** Phase-4 carrier | `λ(K) = A(K) / (m_e · Vol(K) / ℏ_q²)` with `A(K)` = Phase-4 amplitude | Phase-4 already substrate-derives `A(K)` to ≤ 2.5 %; this candidate plugs it in directly |
| **L2** small-perturbation `1 − ε(K)` | `λ(K) = 1 − ε(K)` with `ε(K) = α_EM · f(Z, N)` for some simple substrate function | The proton's `λ_emp ≈ 0.971` and the gap suggest α_EM-order correction; matches the `_li_2_q_util.py:298-313` framing |
| **L3** trace identity | `λ(K) = tr_M(β_K)^a · (q^{1/2}+q^{-1/2})^b` with `a, b` fixed by the Phase-4 carriers | Per-atom analog of Phase-4 amplitude in a Path B normalization |

**L1 is the cheapest.** Phase-4 already does the heavy lift; L1 just re-expresses it in Path B coordinates. The probe (not in this PR) would compute `λ_predicted(K) = A_Phase-4(K) / (m_e · Vol_𝓑₃ / ℏ_q²)` for each light atom and compare to `λ_empirical(K)` derived above. If L1 closes to better than 5 %, the Path B formulation is consistent with Phase-4 substrate-derivation.

## §5. Honest expected outcome

The Phase-4 amplitude already works to ≤ 2.5 % zero-parameter at the per-atom level (D, T, ³He, ⁴He). L1 essentially asks whether the Path B re-expression is consistent with that. **Expected outcome**: L1 lands at the same ≤ 5 % accuracy as Phase-4 (since it's a re-expression, not a new derivation); L2 may sharpen the proton-side framing; L3 is a structural cross-check.

If all three refute, the Phase-4 amplitude is genuinely Path-D-specific and Path B requires its own substrate-derivation. If L1 succeeds, **GAP-A-4 closes for the light series at the same precision as Phase-4** — the framework can drop the Δ_λ decomposition layer entirely without losing accuracy.

## §6. Discipline

- **EXPLORATORY** scoping doc only; no probe in this PR.
- **Builds on**: 14 prior no-fit negatives for `Δ_λ` + Phase-4's substrate-derived per-atom amplitude → Path B re-formulation is the natural pivot.
- **Formalize-first** — narrows to three candidates derived from existing substrate quantities (L1 reuses Phase-4; L2 uses α_EM; L3 reuses Markov trace + spin carrier).
- **No 7th fit ansatz** — none of L1/L2/L3 introduces a fitted scalar; each is a closed-form substrate quantity.
- **Research-grade**: Path B reformulation for A ≥ 2 is a framework infrastructure question (PR #751-level) above the probe layer; the §4 plan is one cheap re-expression script per candidate, no Path-B framework refactor in this PR.

## §7. Cross-references

- [`2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md) — Δ_λ gate doc + Path B/D framing
- [`2026-05-19-delta-lambda-phase4-z4N-closure.md`](./2026-05-19-delta-lambda-phase4-z4N-closure.md) — Phase-4 amplitude formula
- [`2026-06-04-three-paths-refuted-roadmap-update.md`](./2026-06-04-three-paths-refuted-roadmap-update.md) — 14-negatives consolidation (#1864)
- [`2026-06-04-gap-a3-brane-tower-level-selection-scope.md`](./2026-06-04-gap-a3-brane-tower-level-selection-scope.md) — GAP-A-3 scope (#1868); this PR is the orthogonal Path B axis
- PR #751 / #690 / #777 — prior per-atom λ(K) substrate-derivation work for single baryons
