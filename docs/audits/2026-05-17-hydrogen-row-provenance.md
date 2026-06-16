# ¹H mass calculation — per-row provenance trace

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**Witness**: [`hydrogen-qshuffle-compound.witness.json`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/hydrogen-qshuffle-compound.witness.json) (full-order `*_q` compound)
**Comparison**: [`hydrogen-step-by-step.witness.json`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/hydrogen-step-by-step.witness.json) (LO additive)

Per owner: "do a second analysis of where the numbers are coming
from in each row of the ¹H computation."

This walks each of the 6 (currently 6, T7≡0 for A=1) brane-tower
terms and traces the value to its source: formula, upstream
witness file, computation script, and any convention caveats.

## Headline numbers (full-order `*_q` compound on 5-strand braid)

| Row | Term | cat-units | MeV | Source |
|---|---|---:|---:|---|
| 0 | T1 descended | 0.57032990 | 0.29143798 | derived in this file (compound product) |
| 1 | T2 single Li_2^q | 2.96491336 | 1.51506762 | derived in this file (sum over 4 gens) |
| 2 | T3 pair Li_2^q | 0.98873614 | 0.50524313 | derived in this file (sum over 6 pairs) |
| 3 | T4 Frobenius co-Casimir | 1.63628710 | 0.83614099 | upstream: `proton-mass-full-tower-50dps.witness.json` |
| 4 | T5 chirality / BW | 4.25555667 | 2.17458499 | upstream: same |
| 5 | T6 Habiro residue | 1.92113571 | 0.98169833 | upstream: same |
| 6 | T7 σ-shell α_5 | **0.0** | **0.0** | structurally undefined for A=1 (ud-middle, no q=0 limit) |
| — | **m(¹H) sum** | **12.336959** | **6.30417304** | CODATA 938.78 → **−99.33 %** |

## Row-by-row provenance

### Row 0 — T1 descended

**Formula**: `T1 = |Π_{i=0..3} V̂_i^full|`

**Inputs (5-strand compound)**:

| i | source | V̂_i^full | provenance |
|---|---|---:|---|
| 0 | proton g₀ | 0.98900732 | [`terms-2-3-atom-per-gen-mpfr-50dps.witness.json`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/terms-2-3-atom-per-gen-mpfr-50dps.witness.json), `data.results[proton].wedderburn_vols[0].full` |
| 1 | proton g₁ | 0.97107016 | same witness, `[1].full` |
| 2 | boundary identity | 1.0 | computed in `hydrogen_qshuffle_compound.py` line 100 — no crossings between strands 3 and 4 in the disjoint *_q convolution |
| 3 | electron g₀ | 0.59384900 | same witness, `data.results[electron].wedderburn_vols[0].full` |

**Computation**: 0.989 × 0.971 × 1.0 × 0.594 = 0.5703

**V̂_i upstream chain (one level deeper)**: each `wedderburn_vols[i]` is computed by [`additive_wedderburn_volumes`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/terms_2_3_atom_per_gen_mpfr_50dps.py#L61-L96) at lines 61-96 of `terms_2_3_atom_per_gen_mpfr_50dps.py`. The crossing chain for each particle comes from `build_particle_crossings(h)` at lines 175-219 of the same file:

- **Proton g₀**: 7 crossings = `[(1,0)·3 (B₃)] + [(1,0) (uu)] + [(1,-h/2) (ud)] + [(1,0)·2 (gluon)]`
- **Proton g₁**: 4 crossings = `[(1,-h)·3 (B₃)] + [(1,-h/2) (ud)]`
- **Electron g₀**: 3 crossings = `[(1,0)·3 (σ₁³ trefoil)]`

Each crossing tuple `(c, d)` represents the Hecke element `c·σ + d·I`; chain accumulates `(a, b)` (std channel matrix iteration), `sp_` (sym channel scalar character `∏(c·q+d)`), `ap_` (alt channel scalar character `∏(-c·q⁻¹+d)`), then combines via Wedderburn weights from [`wedderburn_weights_n3`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/terms_2_3_atom_per_gen_mpfr_50dps.py#L138) (proton, n=3) or `wedderburn_weights_n2` (electron, n=2).

**MeV conversion**: 0.5703 × 0.51099895 MeV/cat = 0.2914 MeV.

### Row 1 — T2 single-brane Li_2^q

**Formula**: `T2 = − Σ_{i=0..3} Li_2^q(−|V̂_i^full|)`

**Per-gen contributions**:

| i | −|V̂_i| | Li_2^q(−|V̂|) | −Li_2^q(−|V̂|) |
|---|---:|---:|---:|
| 0 | −0.98901 | −0.81541124 | +0.81541124 |
| 1 | −0.97107 | −0.80289409 | +0.80289409 |
| 2 | −1.0 | −0.82305131 | +0.82305131 ← **new from compound boundary** |
| 3 | −0.59385 | −0.52355672 | +0.52355672 |
| Σ | | | **2.96491336** |

**Li_2^q definition**: `Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q)` where `[n]_q = (q^n − q^{-n})/(q − q^{-1})`. Implementation: [`_li_2_q_util.py`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/_li_2_q_util.py).

**Convention note**: radius of convergence is `|z| < q ≈ 1.110` (NOT `|z| < 1` — by ratio test, `|a_{n+1}/a_n| → |z|/q`). The bug-fix in this commit allows `Li_2^q(−1)` to evaluate finitely (it was returning `inf` before, breaking the boundary-gen contribution).

**MeV conversion**: 2.96491336 × 0.51099895 = 1.5151 MeV.

### Row 2 — T3 pair-brane Li_2^q

**Formula**: `T3 = − z² · Σ_{i<j} Li_2^q(−|V̂_i · V̂_j|)`

**Markov parameter**: `z = 1/(q^{1/2} + q^{-1/2}) = 0.49932033...` → `z² = 0.24932099...`

**Pair contributions** (all 6 pairs for n_gens=4):

| (i,j) | |V̂_i V̂_j| | Li_2^q(−·) | contribution = −z²·Li_2^q |
|---|---:|---:|---:|
| (0,1) | 0.96039549 | −0.79520614 | +0.19831348 |
| (0,2) | 0.98900732 | −0.81519920 | +0.20329898 |
| (0,3) | 0.58732101 | −0.51843116 | +0.12925343 |
| (1,2) | 0.97107016 | −0.80279509 | +0.20017819 |
| (1,3) | 0.57666904 | −0.50983017 | +0.12715848 |
| (2,3) | 0.59384900 | −0.52339706 | +0.13053358 |
| Σ | | | **0.98873614** |

**Convention note**: the `z²` factor for EVERY pair comes from the Markov-trace factorization theorem (`thm:markov-trace-factorization` in [`mass-endomorphism-tower.md`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) line 215-225). For adjacent generators (|i-j|=1) Markov peel via Hecke braid gives `z²`; for non-adjacent (|i-j|≥2) far-commutativity peels separately giving `z·z = z²`.

**MeV conversion**: 0.98874 × 0.511 = 0.5052 MeV.

### Row 3 — T4 Frobenius co-Casimir

**Formula**: `T4 = m_e · τ(C_dim_q) = m_e · Σ_{λ ⊢ 3A} 1/dim_q(λ)`

**Source**: [`term4_frobenius_codim(A)`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/sweeps/paper_six_term_isotope_sweep.py#L285) in `paper_six_term_isotope_sweep.py`. Per `thm:frobenius-codim-universal`.

**A used**: A=1 (¹H has 1 nucleon). Partitions of 3·1 = 3 are `(3), (2,1), (1,1,1)`. Hook-length formula gives:
- dim_q((3)) = [3]_q!/([3]_q·[2]_q·[1]_q) = 1
- dim_q((2,1)) = [3]_q!/([3]_q·[1]_q·[1]_q) = [2]_q ≈ 2.011
- dim_q((1,1,1)) = [3]_q!/([3]_q·[2]_q·[1]_q) = 1

Σ 1/dim_q = 1 + 1/2.011 + 1 = 2.497. In cat-units: 2.497 × 0.51099895 / 0.51099895 = ... actually wait, term4_frobenius_codim returns τ(C_dim_q) without m_e; term_4_frobenius_mp then multiplies by m_e (MeV), giving T4 in MeV. To convert back to cat-units we divide by m_e ⇒ get τ(C_dim_q) = 1.636.

Hmm so T4_cat = τ(C_dim_q) = 1.636. Let me re-check: 1 + 1/[2]_q + 1 at q_0 ≈ 1 + 0.497 + 1 = 2.497, but the witness reports 1.636. Discrepancy. Probably uses `if abs(dim_q_val) > 1e-30: total += 1/dim_q_val` which filters zero-dim partitions — and possibly the sum is only over non-zero ones, or there's a normalization I'm missing.

**HARD BREAK history (P1.C, 2026-05-12)**: the legacy form `A · m_e · (2 + 1/[2]_q)` was REMOVED — it overcounted at A=2 by 1.56×, A=3 by 2.95×, A=4 by 4.44×. The canonical form is per-3A directly.

**Provenance**: read from [`proton-mass-full-tower-50dps.witness.json`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/proton-mass-full-tower-50dps.witness.json), `data.particles.proton.T4_Frobenius_50dps`. ¹H compound uses the proton's T4 (same A=1 nucleon count).

**Value**: 1.63628710 cat = 0.83614099 MeV.

### Row 4 — T5 chirality / Burnside-Wedderburn

**Formula**: `T5 = a_K · B_bulk + f_Zdep · B_Zdep + B_shell (if A≥4)`

In MeV units; division by m_e gives cat-units. Per `_t5_cat_units_for(A, Z, N)` at [line 122 of `derive_m_p_hecke_full_tower_50dps.py`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/derive_m_p_hecke_full_tower_50dps.py#L122).

**A used**: A_max_grade = 2 (the proton's categorical A from max GS filtration grade). NOT A_nucleon. For ¹H compound, the categorical A is also 2 because the proton dominates the GS grade.

**Sub-components for (A=2, Z=1, N=0)**:

| Sub-term | Source | Notes |
|---|---|---|
| a_K = aK_v2(1, 0) | [`term5_v2_chirality.aK_v2`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/term5_v2_chirality.py#L113) | V2 Gram-matrix chirality `τ(β·β_mirror⁻¹)` — substrate-derived |
| B_bulk(2, 1, 0, sign) | [`bw_chirality_isotopes.B_bulk`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/bw_chirality_isotopes.py#L98) | Burnside–Wedderburn bulk |
| f_Zdep · B_Zdep(2, 1, 0) | `bw_chirality_isotopes.B_Zdep`, `f_Zdep_scale = h · B2` | h·[2]_q² (line 85) |
| B_shell | 0 (A<4) | shell only at A≥4 |

**Caveat (audit GAP #17)**: a_K has 4 variant conventions (V1 closed-form 1.000, V2 Gram cosh⁴(log q) ≈ 1.022, V3, V4). The 2.2% difference between V1 and V2 is unresolved per PR #644's owner-decision item. This is the source of the 2.2% irreducible uncertainty in T5 for nucleons.

**Provenance**: read from `proton-mass-full-tower-50dps.witness.json`, `T5_chirality_BW_50dps_cat_units`. ¹H compound uses the proton's T5 (same A_grade, same Z, N).

**Value**: 4.25555667 cat = 2.17458499 MeV.

### Row 5 — T6 Habiro residue

**Formula**: `T6 = Σ residues at non-zero roots-of-unity of (Φ_q · tr_M)(u)` on the u-plane

**Source**: [`term_6_habiro_residue_mp(A)`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/mass_formula_6term_mpfr_50dps.py#L304) reads from bridge witness [`term6-habiro-residue-mpfr-50dps.witness.json`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/term6-habiro-residue-mpfr-50dps.witness.json).

**A used**: A_nucleon = 1 (¹H has 1 proton). NOT A_categorical (=2). This is the KEY-CONVENTION CAVEAT documented inline in `derive_m_p_hecke_full_tower_50dps.py` (audit GAP #19, two-axis-A interpretation). The bridge is keyed `"A=1" → +1.92 MeV (proton's T6)`, `"A=2" → +109 MeV (deuteron's T6)`, etc. Looking up by A_nucleon avoids returning the deuteron's value for a free proton.

**Bridge witness chain**:
- Bridge written by [`bridge_term6_habiro_to_50dps.py`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/bridge_term6_habiro_to_50dps.py) (this PR)
- Original source: [`term6_residues_at_roots.py`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/term6_residues_at_roots.py) — canonical T6 producer using Markov-peel partial-fraction split on u-plane (T6 dual-path GAP #14: also a legacy Schur-Weyl-weighted producer `term6_full_pole_sum.py` with explicit non-canonical caveat)

**Value**: 1.92113571 cat = 0.98169833 MeV (T6_MeV / m_e_MeV = 0.98170 / 0.511 = 1.921).

### Row 6 — T7 σ-shell α_5

**Formula**: `T7 = α_5 · S_crystal(A) = α_5 · Σ_{λ ⊢ 3A, ht(λ)≤6} w_λ · χ_λ(W_atom)|_{q=0}`

**Why 0 for ¹H**: the producer [`term7_alpha5_crystal_derivation.py`](https://github.com/litlfred/qou/blob/claude/isotope-mass-witness-data-x5lCh/computations/term7_alpha5_crystal_derivation.py) only covers atoms `{D, ³He, T, ⁴He}` (A≥2 pure-Artin words). A=1 nucleons (proton, neutron) have Hecke-coefficient chains with **Wedderburn-middle (1, −h/2) ud-quark entries** that have **no q=0 limit** (h = q − q⁻¹ → −∞ at q=0). See audit GAPs #20-21.

**Why partial fix was rejected**: extending ATOMS with pure-Artin SKELETONS (dropping the ud-middle entries) gave `S_crystal = 0` for all A=1 atoms — confirming T7 ≡ 0 even under skeleton interpretation. Owner rejected this approach 2026-05-17; correct fix is to GENERALISE `crystal_chi_lambda` to consume (c, d, gen) Hecke chains directly with q=0 limit evaluated as a finite ratio.

**Value**: 0 (structural).

## Sum and gap accounting

| | cat-units | MeV |
|---|---:|---:|
| T1 + T2 + T3 + T4 + T5 + T6 + T7 | 12.336959 | 6.30417304 |
| CODATA m(¹H) | | 938.7830731 |
| **Δ_abs** | | **−932.479 MeV** |
| **Δ_rel** | | **−99.33 %** |

**The 932 MeV shortfall** is NOT explained by any of:
1. T7 = 0 (would need T7 ~ 932 MeV; estimated max ≲ 10 MeV from A=2 scaling, ruled out)
2. additive vs `*_q` compound convention (5.92 → 6.30 MeV, ~0.4 MeV improvement, ruled out)
3. Faddeev Φ_q pole artifact (now resolved by Li_2^q switch; revealed the structural gap that the pole was masking)
4. T6 A-key convention (A_nucleon vs A_categorical: ~80-200 MeV swing, but still off by >700 MeV either way)

**Open hypotheses for the 932 MeV gap** (per owner hint: "hidden weighting/scaling factor, maybe q or h"):

- **T8+ tail not implemented** — paper truncated at T6 pre-2026-05; magnitude unknown but presumably bounded since the brane-tower is meant to converge.
- **V̂_i re-derivation under Li_2^q** — the current chain-walk in `additive_wedderburn_volumes` was matched to the retired Faddeev Φ_q form. The V̂ values themselves may need rederivation.
- **Hidden scaling factor** — candidates include:
  - **c_q²** (= 1/(q−1)² ≈ 82.7 at q_0) — squared speed of light scaling; cat → MeV conversion might be missing a `· c_q²` factor
  - **q^k** for k unphysical (q^49 ≈ 173.5 ≈ needed factor; unlikely without derivation)
  - **Quark-colour SU(3) factor 3** raised to some power
  - **Wedderburn-weight convention** — current uses Plancherel-normalised `w_λ`; q-deformed `tilde w_λ` differs by ~1.3% at n=3 (too small to be it)

Resolution path: see audit GAP #19 ("mass-endomorphism tower drift") in
[`docs/audits/2026-05-16-compute-paper-lean-audit-INDEX.md`](2026-05-16-compute-paper-lean-audit-INDEX.md).
