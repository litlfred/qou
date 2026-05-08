# Categorical Mass Formula — Three Divergent Implementations

**Date:** 2026-05-03
**Source:** post-PR #524 follow-up; user-directed survey of `v4_mass_pipeline` revealed the divergence
**Scope:** documents that the repo carries THREE different "categorical mass" implementations that compute different braids, give different `tr_M` values, use different binding-scale calibrations, and produce different mass predictions.

## TL;DR

The repository contains three "categorical mass formula" implementations. They compute **different mathematical objects** and use **different calibrations**:

| # | Module | Braid | Binding scale | tr_M(D) | Predicts D mass |
|---|--------|-------|---------------|---------|-----------------|
| 1 | `paper_six_term_isotope_sweep.py` | `atom_per_generator_volumes` (per-gen) | proton-fit `E_0 ≈ 7.95e-4 MeV/Hecke` | 0.337 (legacy) | 1481 MeV (−21%) |
| 2 | `hecke_characters.compute_mass_at_level` (v3) | `nuclear_braid_character` (nucleon-strand) | `E_0 = 0.782 MeV` (free-neutron β-decay) | 1.3e-17 | 1878 MeV (+0.1%) |
| 3 | `markov_peel` / Hoefsmit-Wenzl bridge (canonical) | `atom_braid_word_3A` (3A quark-strand) | none (returns dimensionless `tr_M`) | 0.388 | not a mass formula |

None of these is the canonical "six-term mass formula" of `six-term-mass-formula-complete.md` evaluated correctly. **The correct evaluation does not exist in the repo as of this audit.**

## The three implementations in detail

### Implementation 1 — `paper_six_term_isotope_sweep.py`

**Braid construction:** `atom_per_generator_volumes(Z, N)` in `hecke_core.py`, which builds per-generator additive Wedderburn `(a, b, sp, ap)` accumulators for the full atomic braid in H_{3A}, using strand-typed `(c, d)` tables `_PROTON_G0`, `_PROTON_G1`, `_NEUTRON_G0`, `_NEUTRON_G1` derived via `nucleon_gen_chains(quarks)` from the quark composition (proton = `uud`, neutron = `udd`).

**Mass formula** (the paper's six-term formula):
```
m(ρ) = T1: Π |V̂_i|                       ← legacy "T1" (per-gen product, NOT canonical Markov trace)
     + T2: Σ_i Φ_q(|V̂_i|)                ← brane-tower single-gen
     + T3: z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)    ← brane-tower pair-gen
     + T4: m_e · Σ_λ 1/dim_q(λ)          ← Frobenius co-Casimir
     + T5: a_K · C_K                      ← chirality
     + T6: Σ_ℓ residues / (q_0 - ζ_ℓ)    ← cyclotomic series
```

**Calibration:** proton mass via `E_0 = 938.272 / m_p_hecke ≈ 7.95×10⁻⁴ MeV per Hecke unit`.

**Pathology:** T2 dominates by 10⁶× because Φ_q(0.99) ≈ 6.7×10⁵ and most per-gen `|V̂_i|` are 0.85–0.99. Tiny p/n asymmetries get amplified by 10⁵× → predicted T − ³He = −737 MeV (CODATA: +0.019 MeV). See `brane-tower-isospin-diagnosis.witness.json`.

**Predictions (after PR #524 corrections):**

| atom | M_pred | M_CODATA | err |
|------|--------|----------|-----|
| p | 938.27 | 938.272 | 0.00% (CAL) |
| n | 412.50 | 939.565 | **−56.1%** |
| D | 1480.88 | 1876.124 | **−21.1%** |
| T | 2086.47 | 2809.432 | **−25.7%** |
| ³He | 2823.11 | 2809.413 | +0.49% |
| ⁴He | 3559.90 | 3728.401 | −4.5% |

### Implementation 2 — `hecke_characters.compute_mass_at_level` (v3) + `crt_markov_v4` extension (v4)

**Braid construction:** `nuclear_braid_character(Z, N)` in `hecke_characters.py`. **Different from #1**: each nucleon is treated as a **single strand**, not 3 quark strands. Pair crossings between nucleons (i, j) at generator `g = (i+j) mod n_gens` use `crossing_coeffs(ti, tj)`:
- pp: (1, 0) = σ
- nn: (1, −h) = σ⁻¹
- pn: (1, −h/2) = mixed

**Mass formula:**
```
markov_trace = Σ_λ (dim_q²/[k]_q!) · χ_λ / dim(λ)
binding = |1 − |markov||
B(Z, N) = E_0 · binding             with E_0 = 0.782 MeV (free-neutron β-decay)
M_pred = Z·m_p + N·m_n + Z·m_e − B
```

**Calibration:** `E_0 = 0.782 MeV` (free-neutron β-decay Q-value). NOT the m_e·8G ≈ 3.74 MeV used by #1.

**v4 extension** (`crt_markov_v4.total_mass_h3a`): adds depth-1 + depth-2 tower terms to v3's markov_trace, then converts via `ALPHA_BIND = m_e · 8 · Catalan ≈ 3.7445 MeV`. Verdict in v4's own witness: **"v4 makes it worse — wrong calibration"** (0/4 atoms improved over v3).

**Predictions (v3 only):**

| atom | M_pred | M_CODATA | err |
|------|--------|----------|-----|
| p | 938.78 | 938.78 | 0.000% (no CAL needed) |
| D | 1878.35 | 1876.12 | +0.119% |
| T | 2817.91 | 2809.43 | +0.302% |
| ³He | 2817.13 | 2809.41 | +0.275% |

**These look great** — but they're misleading. v3 returns `M_pred = Mfree − E_0·|1−markov|`. Since `|markov| ≈ 0` for all atoms (e.g., `markov(D) = 1.3×10⁻¹⁷`), `binding ≈ E_0·1 = 0.782 MeV` regardless of atom — much smaller than actual binding (B(D) = 2.22, B(T) = 8.48). The 0.1–0.3% accuracy is just because **Mfree dominates** total atomic mass by 1000×. The CATEGORICAL part of v3 is essentially saturated at zero and contributes a near-constant 0.782 MeV.

**Smoking gun:** v3's `markov_trace` values disagree with the canonical Hoefsmit+Wenzl bridge by orders of magnitude:

| atom | v3 markov | bridge canonical | ratio |
|------|-----------|------------------|-------|
| p | 1.0 | 1.0653 | 0.939 |
| D | 1.3e-17 | 0.3883 | ≈ 0 |
| T | 8.2e-4 | 0.1041 | 0.008 |
| ³He | 2.7e-6 | 0.2065 | 1.3e-5 |

This is because v3 uses the **nucleon-strand braid** (A strands, pair crossings), NOT the canonical **3A quark-strand atomic braid** (`atom_braid_word_3A`). They're different categorical objects.

### Implementation 3 — `markov_peel` / Hoefsmit-Wenzl bridge (canonical `tr_M` only)

**Braid construction:** `mass_at_3A_proper.atom_braid_word_3A` — full 3A-strand atomic braid with B₃ quark-confinement per nucleon plus inter-nucleon crossings.

**Two equivalent algorithms:**
- `markov_peel.tr_M_atomic` (recursive Markov-axiom ascent, PR #520)
- Hoefsmit + Wenzl bridge (witness `atomic-tr-m-mpfr-50dps.witness.json`)
- Both compute `Σ_λ y_λ(q) · χ^λ(β)` and agree to 15+ digits.

**This is the canonical `tr_M` per the paper.** It is NOT a mass formula by itself — it's just the Markov trace of the atomic braid. Mass formulas reference it as Term 1.

**Values:**

| atom | tr_M(q_0) |
|------|-----------|
| p | 1.0653062286 |
| n | 0.9232332972 |
| D | 0.3882864715 |
| T | 0.1040521187 |
| ³He | 0.2065408586 |
| ⁴He | 0.0553483459 |

**T ≠ ³He** (ratio 1.985) — the literal atomic braids encode quark-content asymmetry through per-strand `(c, d)` tables.

## Where the divergence comes from

| Object | #1 (six-term) | #2 (v3) | #3 (canonical) |
|--------|---------------|---------|----------------|
| Braid strands | 3A | A | 3A |
| `(c, d)` per strand | quark-level | nucleon-level | quark-level |
| Confinement | B₃ per nucleon (`σ₀σ₁⁻¹`)³ | none (single nucleon strand) | same as #1 |
| `tr_M` formula | per-gen `Π \|V_i\|` (legacy) or canonical (PR #524 fix) | `Σ_λ wχ/dim` over partitions of A | `Σ_λ y_λ χ_λ` over partitions of 3A |
| Binding scale | `m_e·8G ≈ 3.74 MeV` | `E_0 = 0.782 MeV` | n/a |
| Best agreement w/ data | proton-cal forces 0% on p, 25% off elsewhere | 0.1-0.3% on all atoms (but driven by Mfree) | n/a |

## Recommendation

The repo has been carrying conflicting "categorical mass" infrastructure for some time. The right resolution is **content-level** — pick ONE formula as canonical and retire (or relabel) the others:

- **Option A** — declare the six-term formula in `six-term-mass-formula-complete.md` canonical. Then implementation #1 needs the brane-tower fix, and implementations #2, #3 should be relabeled (#2 as a different observable, #3 as just `tr_M`).
- **Option B** — declare v3 (`compute_mass_at_level` + `E_0 = 0.782 MeV`) canonical. Then the six-term formula and #3 are exploratory tools; the paper text needs updating to reflect that nucleon-strand-level evaluation is the actual prescription.
- **Option C** — admit the paper's mass formula is incomplete at q_0; document this audit's findings as a Section "Open Issues" and stop adding ad-hoc mass-prediction scripts until a derivation question is resolved.

I lean toward **Option C** because:
- #1 has a known structural problem (Φ_q amplification) that no simple fix addresses
- #2 is technically incorrect (Markov trace ≠ canonical Markov trace; binding model gives constant 0.782 MeV)
- #3 alone is just `tr_M`, not a mass formula

Adding more implementations without resolving the underlying question (which braid, which binding scale, which formula?) creates more divergence, not less.

## Files

- `paper_six_term_isotope_sweep.py` (#1) — the legacy 6-term implementation
- `paper_six_term_canonical_t1.py` (PR #524) — same with canonical T1 (sub-MeV change)
- `hecke_characters.compute_mass_at_level` (#2 v3)
- `crt_markov_v4.total_mass_h3a` + `v4_mass_pipeline.py` (#2 v4 — verdict: "wrong calibration")
- `markov_peel.tr_M_atomic` + `atomic-tr-m-mpfr-50dps.witness.json` (#3 canonical `tr_M`)
- `markov_invariant_unified_mass.py` — fourth implementation, calibrates 3 prefactors (α_M, α_F, α_T7) from D, T; superseded by PR #524 retraction

## Witnesses

- `paper-six-term-canonical-t1.witness.json` (#1 with canonical T1)
- `brane-tower-isospin-diagnosis.witness.json` (#1's −737 MeV pathology)
- `v4-mass-pipeline.witness.json` (#2 v4's "wrong calibration" verdict)
- `atomic-tr-m-mpfr-50dps.witness.json` (#3 canonical tr_M values)
- `markov-peel-atomic-tr-m.witness.json` (#3 alternative algorithm; PR #520)
- `canonical-tr-m-three-path-comparison.witness.json` (PR #524's three-path comparison)

## Refs

- `prop:categorical-mass-markov`
- `prop:mass-endomorphism-tower`
- `thm:knot-mass-formula-unified`
- `six-term-mass-formula-complete.md`
- PR #518, #520, #524, #525
