# Audit Ledger — Specht `CharZero` Classification (`qou-73kb`) & GGM Stokes / A-Polynomial Source Transcription (`qou-m1tr`)

**Date:** 2026-11-24
**Beans:** `qou-73kb`, `qou-m1tr` (related closed prerequisite: `qou-52sn`)
**Lean 4 Formalizations (`0 sorry`, `0` custom axioms, §7c clean):**
- [`QOU/BraidKnot/SpechtCharFreeStandardBasis.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidKnot/SpechtCharFreeStandardBasis.lean)
- [`QOU/Mass/FourOneAPolynomialFromGluing.lean`](../../folio/quantum-observable-universe/lean/QOU/Mass/FourOneAPolynomialFromGluing.lean)
**80-dps Verification Probe & Witness:**
- [`computations/probes/ggm_stokes_apoly_and_specht_charfree_audit_probe.py`](../../computations/probes/ggm_stokes_apoly_and_specht_charfree_audit_probe.py)
- [`computations/probes/ggm-stokes-apoly-and-specht-charfree-audit.witness.json`](../../computations/probes/ggm-stokes-apoly-and-specht-charfree-audit.witness.json)

---

## Part 1 — Bean `qou-73kb`: Complete Classification of `[CharZero k]` Across All 25 `Specht*.lean` Modules

### 1.1 Executive Summary

Across all 25 `*Specht*.lean` modules in the corpus (`21` `QOU/BraidKnot/Specht*.lean` + `PieceASpechtCharacter.lean` + `SnIsotypicSpechtSplitInstance.lean` + `QOU/SchurWeyl/QuantumGLHWSpecht.lean` + `QuantumGLHWSpechtId.lean`):

1. **Category 1 (Mathematically load-bearing — FALSE in prime characteristic $p \le n$):**
   Every theorem asserting nondegeneracy of the Specht bilinear form (`specht_form_nondegenerate`), orthogonal complement decomposition (`isCompl_specht_perp`), irreducibility of $S^\mu$ (`specht_isSimple`), pairwise non-isomorphism / exhaustion of irreducibles (`specht_pairwise_noniso`, `specht_exhausts_irreducibles`), or Maschke–Wedderburn semisimplicity of $k[S_n]$ (`SpechtWedderburn*`, `SpechtSchurDiagonal`, `SpechtRegularMultiplicity`, `SpechtCentralC2Scalar`, `SpechtAbsolutelyIrreducible`).
   - **Machine-checked counterexample:** `SpechtCharFreeStandardBasis.specht_form_rad_nontrivial_zmod2` proves over $K = \mathrm{ZMod}\ 2$ (`[Field (ZMod 2)]`) that for $\mu = [1, 1] \vdash 2$, $e_t \ne 0$ satisfies $\langle e_t, y\rangle = 0$ for all $y \in S^{[1,1]}$, refuting `specht_form_nondegenerate` when `[CharZero k]` is dropped.

2. **Category 2 (Proof-artifact — TRUE over every field / commutative ring; `[CharZero k]` entered only by dividing by $|H|$ or $|C_t|$):**
   Exactly **two root declarations** in the entire 25-file tree:
   - **`SpechtCrossKappa.polytabloid_ne_zero` (`SpechtCrossKappa.lean:219`):** Proved via $\langle e_t, e_t\rangle = |C_t| \ne 0$ in `[Field K] [CharZero K]`. Generalized in `SpechtCharFreeStandardBasis.polytabloid_ne_zero_charFree` to **`[CommRing R] [Nontrivial R]`** via $(e_t)_{\{t\}} = +1$ (`C_t \cap R_t = \{1\}`).
   - **`SpechtStandardBasisCore.transversal_sum_eq_zero` (`SpechtStandardBasisCore.lean:712`):** Divided by $|H| = |S_A \times S_B|$ to cancel the Garnir coset factor, propagating `[CharZero k]` into `straightening_step_colMax` (`:2880`), `straightening_step` (`:2961`), `standardPolytabloid_straightening` (`:2998`), `standardPolytabloid_span_eq_specht` (`:3019`), `standardPolytabloid_span` (`:3032`), `SpechtStandardBasis.standardBasis` (`:115`), `SpechtStandardBasis.specht_finrank_eq_numSYT` (`:137`), and `SpechtFinrankWired`. Generalized in `SpechtCharFreeStandardBasis` (`transversal_rep_sum_eq_zero_of_rat` → `standardBasis_charFree` → **`specht_finrank_eq_numSYT_charFree`**) over **arbitrary `[Field k]`** (any characteristic $p \ge 0$) by transferring the $\mathbb{Q}$ Garnir transversal identity through $\mathbb{Z}$-coordinates (`SpechtBaseChange.polytabloid_apply_eq_intCast`).

   > **Namespace / `.olean` isolation note:** Per active Q3 namespace-isolation coordination, the characteristic-free proofs are landed additively in `SpechtCharFreeStandardBasis.lean` so prebuilt `.olean` signatures of the 25 existing modules remain untouched; in-place removal of `[CharZero k]` on `SpechtStandardBasis` / `SpechtFinrankWired` is a mechanical 1:1 replacement onto these proved lemmas whenever a full `QOU.BraidKnot` rebuild runs.

3. **Category 3 (Section-variable / inherited-only):**
   Modules declaring `variable {k : Type} [Field k] [CharZero k]` at file scope where either every declaration already carries `omit [CharZero k]` or `[CharZero k]` was kept solely to match the former `SpechtStandardBasis` signature contract.

### 1.2 Module-by-Module Classification Table (25 `Specht*.lean` Files)

| Module | `CharZero` Presence | Category | Audit Verdict & Exact Mechanism |
|---|---|---|---|
| `Specht.lean` | None (`[CommRing k]`) | Clean | Base construction $M^\mu$, $e_t$, $S^\mu$ already over `[CommRing k]`. |
| `SpechtBranchingMultiplicityOne.lean` | None | Clean | Combinatorial SYT branching; no base-characteristic assumption. |
| `SpechtCrossDominance.lean` | None | Clean | Combinatorial pigeonhole / Gale–Ryser dominance (`Sagan 2.2.6`). |
| `SpechtBaseChange.lean` | Explicit on `:133`, `:151` | **Cat 1 / Bridge** | `mapRing`, `polytabloid_apply_eq_intCast`, `mem_span_map` are `[CommRing]`; only `spechtSubmodule_eq_span_of_rat` (`ℚ →+* k`) requires `[CharZero k]` because `ℚ` embeds into `k` iff $\mathrm{char}(k) = 0$. |
| `SpechtIrreducible.lean` | Explicit on `:892..1301` | **Cat 1 (Load-bearing)** | `specht_form_nondegenerate`, `isCompl_specht_perp`, `specht_isSimple` require `[CharZero k]` (Gram det divides hook-length product; false for $\mu=[1,1]$ in char $2$, $\mu=[2,1]$ in char $3$). |
| `SpechtCrossKappa.lean` | Explicit on `:219` only | **Cat 2 (Proof artifact)** | `kapCross`, `dominance_of_kapCross_ne_zero` over `[CommRing k]`. Only `polytabloid_ne_zero` (`:219`) used `[Field K] [CharZero K]`; generalized to `[CommRing R] [Nontrivial R]` in `SpechtCharFreeStandardBasis.polytabloid_ne_zero_charFree`. |
| `SpechtStandardBasisCore.lean` | `variable` + 51 `omit`s; active at `:712`, `:2880..3045` | **Cat 2 (Proof artifact)** | Root site `transversal_sum_eq_zero` (`:712`) divides by $|S_A \times S_B|$. Discharged over arbitrary `[Field k]` via $\mathbb{Z}$-coordinate transfer in `SpechtCharFreeStandardBasis`. |
| `SpechtDominanceCore.lean` | `variable` (`:55`), `omit`ted on exported lemmas | **Cat 3 (Inherited)** | Order/dominance core; `dominance_relation_exists` omits `[CharZero k]`. |
| `SpechtTriangularCore.lean` | `variable` (`:72`), `omit`ted on all 6 exported lemmas | **Cat 3 (Inherited)** | `standardPolytabloid_diag_coeff`, `standardPolytabloid_triangular'` already omit `[CharZero k]`. |
| `SpechtStandardBasis.lean` | `variable` (`:71`); active on `standardBasis` (`:115`), `specht_finrank_eq_numSYT` (`:137`) | **Cat 2 (Inherited from Core)** | Inherited solely from `standardPolytabloid_span`. Generalized to arbitrary `[Field k]` in `SpechtCharFreeStandardBasis.standardBasis_charFree` and `specht_finrank_eq_numSYT_charFree`. |
| `SpechtFinrankWired.lean` | `variable` (`:71`) + `unusedSectionVars false` | **Cat 2 / Cat 3** | Kept for signature parity with `SpechtStandardBasis`; superseded over arbitrary `[Field k]` by `specht_finrank_eq_numSYT_charFree`. |
| `SpechtActionInjective.lean` | `variable`, `omit`ted | **Cat 3 (Inherited)** | Faithful $S_n$-action on $M^{(n-1,1)}$ / tabloids (`1 ≠ 0` suffices for $n \ge 3$). |
| `SpechtBlockDimension.lean` | `variable`, 4/4 `omit`s | **Cat 3 (Inherited)** | All 4 declarations already carry `omit [CharZero k]`. |
| `SpechtRegularMultiplicity.lean` | `variable`, 3/3 `omit`s | **Cat 3 / Cat 1 consumer** | Local algebra omits `[CharZero k]`; Wedderburn multiplicity interpretation is semisimple (`p ∤ n!`). |
| `SpechtClassification.lean` | `variable` (`:99`) | **Cat 1 (Load-bearing)** | Irreducibles of $k[S_n]$ are indexed by *all* partitions of $n$ iff $p = 0$ or $p > n$ (in char $p \le n$, only $p$-regular partitions $D^\lambda$ survive). |
| `SpechtAbsolutelyIrreducible.lean` | `variable` | **Cat 1 (Load-bearing)** | $\mathrm{End}_{k[S_n]}(S^\mu) = k$ fails in prime characteristic (e.g. $\mu = (2,2)$ in char $2$). |
| `SpechtCentralC2Scalar.lean` | `variable` | **Cat 1 (Load-bearing)** | Schur scalar action on simple $S^\mu$ requires irreducibility (`specht_isSimple`). |
| `SpechtSchurDiagonal.lean` | `variable` | **Cat 1 (Load-bearing)** | Pairwise Schur orthogonality requires simple non-isomorphic $S^\mu$ (`char = 0` or $p > n$). |
| `SpechtWedderburnCriterion.lean` | `variable` | **Cat 1 (Load-bearing)** | Maschke semisimplicity of $k[S_n]$ fails iff $\mathrm{char}(k) \mid n!$. |
| `SpechtWedderburnGeneral.lean` | `variable` | **Cat 1 (Load-bearing)** | Full matrix-block Wedderburn decomposition $k[S_n] \cong \bigoplus_{\mu \vdash n} M_{f^\mu}(k)$ requires $\mathrm{char}(k) \nmid n!$. |
| `SpechtWedderburnLe12.lean` | `variable` | **Cat 1 (Load-bearing)** | Explicit $n \le 12$ Wedderburn instances over semisimple $k[S_n]$. |
| `PieceASpechtCharacter.lean` | `variable` (`:30`) | **Cat 2 / Cat 1 split** | Dimension identity $\chi^\mu(1) = f^\mu \cdot 1_k$ needs only `standardBasis_charFree` (note in char $p \mid f^\mu$ the trace in $k$ reduces mod $p$); character orthogonality requires Cat 1. |
| `SnIsotypicSpechtSplitInstance.lean` | `variable` | **Cat 1 (Load-bearing)** | Isotypic projector idempotents divide by $n!$ / hook lengths (`char = 0` or $p > n$). |
| `SchurWeyl/QuantumGLHWSpecht.lean` | `[LinearOrder K] [IsStrictOrderedRing K]` (implies `CharZero`) | **Cat 1 (Load-bearing)** | Uses `[Field K]` alone on `exists_eq_mul_trace_of_comm`; Hecke Wedderburn block split + Jimbo density require generic $q$ (not a root of unity) over an ordered field. |
| `SchurWeyl/QuantumGLHWSpechtId.lean` | `[LinearOrder L] [IsStrictOrderedRing L]` (`omit`ted on `:37`) | **Cat 1 (Load-bearing)** | Pins $HW_\mu \cong S_{\lambda(\mu)}$ via `trace_seminormalRep_test` dividing by $f^\nu \ne 0$ in `L` (`CharZero` load-bearing when $p \mid f^\nu$). |

---

## Part 2 — Bean `qou-m1tr`: Source-LaTeX & Census Transcription Audit

Every literature datum flagged in `qou-m1tr` was cross-checked directly against the held arXiv e-print `.tex` sources and Culler's `A_census.tgz` in `library/`, and promoted to sorry-free algebraic derivations where previously typed.

| Corpus Carrier | Primary Held Source (`library/`) | Exact Source Equation / Line | Verification Verdict |
|---|---|---|---|
| `StokesMatrixProvenance.DT` (`5₂` DT matrix) | `library/arxiv-2012.00062v3/source/files/GGM_peacock_20v4.tex` | Eq. `\label{GZ52}` (line 2107): `\begin{pmatrix} 0 & 4 & 3 \\ -4 & 0 & -3 \\ -3 & 3 & 0 \end{pmatrix}` | **EXACT MATCH** (also cross-checked against `2111.06645v3` `sigma24-055.tex` $4\times 4$ bordered matrix up to $\sigma_3 \mapsto -\sigma_3$ basis sign). |
| `FiveTwoDTSpectrumSplit.Splus0` (`[[1,4,0],[0,1,0],[-3,-9,1]]`) | `GGM_peacock_20v4.tex` | Eq. `\label{eq:S0pu052}` (lines 2077–2088): $\mathfrak{S}_{\sigma_3,\sigma_1}\mathfrak{S}_{\sigma_3,\sigma_2}\mathfrak{S}_{\sigma_1,\sigma_2}$ | **EXACT MATCH** (`FourOneAPolynomialFromGluing.fiveTwo_stokes_split_eq_provenance_recon` proves cross-module equality). |
| `FiveTwoDTSpectrumSplit.Sminus0` (`[[1,0,3],[-4,1,-3],[0,0,1]]`) | `GGM_peacock_20v4.tex` | Eq. `\label{eq:S0nu052}` (lines 2090–2100): $\mathfrak{S}_{\sigma_1,\sigma_3}\mathfrak{S}_{\sigma_2,\sigma_3}\mathfrak{S}_{\sigma_2,\sigma_1}$ | **EXACT MATCH** (`S^+(0)^T S^-(0) = I_3`, GGM eq `\label{Ssym}` line 669). |
| `FiveTwoDTSpectrumSplit.Splus0_41` (`[[1,3],[0,1]]`) | `GGM_peacock_20v4.tex` | Eq. `\label{eq:S0u041}` (lines 1473–1482): $S^+(0) = \begin{pmatrix}1&3\\0&1\end{pmatrix}$, $S^-(0) = \begin{pmatrix}1&0\\-3&1\end{pmatrix}$ | **EXACT MATCH** (`FourOneAPolynomialFromGluing.fourOne_stokes_inversion_eq17`). |
| `RouteANewtonPolygonDT.a41Monomials` (`4₁` A-polynomial) | `library/A_census.tgz:apolys/K2_1.apoly` + `nz-gluing-from-braid-monodromy.witness.json` + `AJFigureEight.lean` | `A_K2_1 := M^4 + L(-1 + M^2 + 2M^4 + M^6 - M^8) + L^2 M^4` | **NOW DERIVED IN LEAN (`FourOneAPolynomialFromGluing`)**: proved directly from the Neumann–Zagier gluing equations of $S^3 \setminus 4_1$ via a division-free Bezout identity (`A41_bezout_certificate`), proved equal to `A_K2_1`, `AJFigureEight.aPolyFigureEight`, and $-A_{4_1}^{\mathrm{RouteA}}$, with exact monomial support `a41Monomials`. |
| `RouteANewtonPolygonDT.a52Monomials` & `fiveTwoMaxAbsSlope = 10` (`5₂` slopes `{0,-4,-10}`) | `library/A_census.tgz:apolys/K3_2.apoly` + `two-bridge-cusp-rows-apoly.witness.json` + `FiveTwoAPolynomialFromFareyWord.lean` | `A_K3_2 := 1 + L(-1 + 2M^2 + 2M^4 - M^8 + M^{10}) + L^2(M^4 - M^6 + 2M^{10} + 2M^{12} - M^{14}) + L^3 M^{14}` | **EXACT MIRROR MATCH (`L^3 A(L^{-1}, M) = A_K3_2(L, M)`)** — already derived without SnapPy in `#6985` (`qou-52sn` completed); boundary slopes `{-10,-4,0}` (census mirror `{0,4,10}`) and connection count `4` unconditionally verified. |
