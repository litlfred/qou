# KLR tranche-2 follow-up: Composite-3 + Demazure-Lusztig preflights — combined results

**Companion** to the [Composite-4 RUN](2026-06-06-qbeta-klr-composite4-preflight-run-results.md) and [Composite-1 standard RUN](2026-06-06-qbeta-klr-composite1-preflight-run-results.md) (PR #1914, merged). User direction (2026-06-06): "1 merge after comments resolved, then 2 3" — proceed to two more preflights after merging #1914.

**Both verdicts**: ❌ **REFUTED at u² by sign**. cont. 9 Options C (full reading) and D (Composite 3 build) **NOT AUTHORISED**.

---

## Option D — Composite 3 (Type-B folded crystal): REFUTED at u² sign

### Ansatz
```
F(u) = Σ_{T ∈ B_{Type-B fold}(λ)} q^{c(T)} · u^{|T|}
```
σ-fixed subset of the sl_n Kashiwara crystal under the Dynkin automorphism σ (AGENTS.md §7b: "Type-B folding for chirality / CPT").

### Concrete result (sl_4 → C_2 folding, ω_2)
σ-fixed 2-subsets at |T|=2 under σ = (1↔4, 2↔3): **{1,4}** and **{2,3}**. So `[u²]F = q^3 + q^3 = 2q^3`.

| anchor | `q` | `q^3` | **`[u²]F = 2q^3`** | sign | vs `c_2 = -1` |
|---|---|---|---|---|---|
| proton | `1.1099786` | `1.3675518` | **`+2.7351037`** | **POS** | **MISMATCH** |
| muon | `1.1099786` | `1.3675519` | **`+2.7351038`** | **POS** | **MISMATCH** |

Both anchors identical to 7 figs. 2 assertions pass.

### Why this is convention-robust + STRONGER than Composite 1

The Composite-3 ansatz has **no q-Pochhammer factor** at u². At every `u^k` rung:
- `[u^k]F = Σ_{|T|=k} q^{c(T)}` is a sum of **positive q-powers**.
- Positive q-powers at q > 0 are positive ⇒ `[u^k]F > 0` at **every** k.
- Target `c_k < 0` for k = 2, 3, 4 at q₀ — **mismatch at every rung**.

AGENTS.md §7b's "σ-fixed crystals are bar-involution invariant" is *true* but *orthogonal to sign-negativity*: bar-invariance and sign-positivity are independent properties; folding does not introduce signs. **The 12-17 session cont. 9 Option D build is NOT authorised.**

Probe + witness: [`qbeta_klr_composite3_preflight_run.py`](../../computations/qbeta/qbeta_klr_composite3_preflight_run.py), [`qbeta-klr-composite3-preflight-run.witness.json`](../../computations/qbeta/qbeta-klr-composite3-preflight-run.witness.json).

---

## Option C′ — Demazure-Lusztig (Lusztig-dual) variant of Composite 1: REFUTED for natural variants (exotic UNTESTED)

### Ansatz
Same as Composite 1 (`F(u) = Σ_w D_w(λ)·(q;q)_{ℓ(w)}·u^{ℓ(w)}`) but with the **Lusztig-dual** Demazure character:
```
D_w^{dual}(λ; q) = q^{ht(w,λ)} · D_w(λ; q^{-1})
```

### Concrete result (sl_3 / ω_1 / ℓ=2)

For this case the Lusztig dual is **palindromic-equal to the standard**:

- `D_{s_1 s_2}(q) = 1 + q`; `D_{s_1 s_2}^{dual}(q) = q·(1 + q^{-1}) = q + 1` — **same**.
- `D_{s_2 s_1}(q) = 1 + q + q²`; `D_{s_2 s_1}^{dual}(q) = q²·(1 + q^{-1} + q^{-2}) = q² + q + 1` — **same**.

Σ_dual = Σ_standard = 5.4520. So **[u²]F_dual = 0.1391 > 0** at both anchors (identical to Composite-1 standard).

| anchor | `Σ D` (standard = dual) | `[u²]F_dual` | sign | vs `c_2 = -1` |
|---|---|---|---|---|
| proton | `+5.4520096197` | **`+0.13914`** | **POS** | **MISMATCH** |
| muon | `+5.4520096737` | **`+0.13914`** | **POS** | **MISMATCH** |

2 assertions pass.

### Honest scope: NARROWS but does not FULLY refute

Lusztig 1990's positivity theorem (canonical bases are positive integral bases) implies that **all natural Lusztig-canonical Demazure variants** (dual, T_i-action on the polynomial ring with standard normalisations) inherit sign-positivity. So:

- ✅ **Standard Demazure** — refuted at u² sign (PR #1914 RUN).
- ✅ **Lusztig dual** — refuted at u² sign (this RUN; reduces to standard in palindromic cases).
- ✅ **Natural T_i-action** (Demazure-Lusztig operator with non-negative coefficients) — refuted via positivity (Lusztig 1990).
- ❓ **Exotic signed variants** — Lusztig-Yun-Zhu Whittaker basis, twisted T_i with sign-changing coefficients, etc. — UNTESTED. These are mathematically defined but not in this corpus's natural categorical framework. Refuting them would require a separate convention-pinning preflight scope.

So cont. 9 Option C's **natural reading** is fully refuted; the residual escape route is exotic-signed Lusztig variants, which is a separate research-grade scope item — not a 5-7 session build candidate.

Probe + witness: [`qbeta_klr_lusztig_demazure_preflight_run.py`](../../computations/qbeta/qbeta_klr_lusztig_demazure_preflight_run.py), [`qbeta-klr-lusztig-demazure-preflight-run.witness.json`](../../computations/qbeta/qbeta-klr-lusztig-demazure-preflight-run.witness.json).

---

## Combined four-preflight outcome (Composites 4 + 1 + 3 + Lusztig variant)

| cont. 9 Option | preflight result | mechanism | saved infra |
|---|---|---|---|
| **B** Composite 4 (Wenzl × q-Poch) | REFUTED at u² magnitude | ~92× too small | 5-6 sessions |
| **C** Composite 1 standard (Demazure × q-Poch) | REFUTED at u² sign | positivity | 5-7 sessions |
| **C'** Composite 1 Lusztig dual | REFUTED at u² sign | Lusztig 1990 positivity | (same 5-7) |
| **C''** Composite 1 exotic signed | UNTESTED | NARROWS only | — |
| **D** Composite 3 (Type-B folded crystal) | REFUTED at u² sign | folded ≠ signed | 12-17 sessions |
| **A** accept residue A as CAL-3-anchored | reinforced by **3 corpus + 4 preflight refutations** | — | — |

**Total infra saved by today's four one-session preflights:** ~22-30 sessions of Lean + `pyhecke` infra build. Combined ROI ~6-7× per preflight session.

## Residual cont. 9 menu

| status | option |
|---|---|
| ✅ refuted (B, C standard, C-dual, D) | majority of menu dead |
| ❓ UNTESTED, requires specialised scope | C'' exotic signed Lusztig (Whittaker / Yun-Zhu / twisted T_i) |
| 🛑 viable (and now strongly reinforced) | **A** — accept residue A as inherently CAL-3-anchored permanently |

**Recommendation**: cont. 9 Option A is the natural state of the residue-A categorical-ID question. Three corpus-side closures (cont. 6 / 9 / 11) + four preflight refutations (today) ≫ "residue A categorical ID is reachable by single-formula or low-factor compositions of natural categorical atoms". The remaining theoretical-research escape route (exotic signed Lusztig) is a research-grade scope item — not a build-cost-saving short-term tranche.

## Cross-refs

- Master KLR-infra roadmap: [`2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md).
- KLR program kickoff scope: [`2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md).
- KLR tranche 1 (merged PR #1911): [`2026-06-06-qbeta-residue-habiro-dual-tau-eval.md`](2026-06-06-qbeta-residue-habiro-dual-tau-eval.md).
- KLR tranche 2 scope (merged PR #1914): [`2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md`](2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md).
- Composite-4 RUN result: [`2026-06-06-qbeta-klr-composite4-preflight-run-results.md`](2026-06-06-qbeta-klr-composite4-preflight-run-results.md).
- Composite-1 standard RUN result: [`2026-06-06-qbeta-klr-composite1-preflight-run-results.md`](2026-06-06-qbeta-klr-composite1-preflight-run-results.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) (cont. 16 + cont. 17 update).
