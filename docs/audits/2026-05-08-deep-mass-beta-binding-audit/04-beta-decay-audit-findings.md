# 04 — Beta-Decay Audit Findings

**Scope:** Every β-decay-related computation in `folio-assistant/computations/`. Special focus on g_A, V_ud, G_F, N_v, sin²θ_W, and Q-values.

**Headline finding:** **The N_v derivation gap gates the entire weak sector.** Every G_F-dependent prediction is conditional on `conj:n-v-bring-action`, which is unproved (W-2 numerical search returned a null result; see `2026-05-05-nv-categorical-impasse.md`).

## §A. Coupling constants

### A.1 `g_A` — axial-vector coupling (post-fix)

**Compute script:** `borromean-axial-coupling.py` (current; the cyclic-trivial version is in `_deprecated/`).

**Compute path (post-fix):**
- Frobenius reciprocity: `⟨O⟩_T = Σ u_i (G⁻¹)_{ij} ⟨O,b_j⟩` (the master formula, [02 §7](02-pre-archimedean-derivation-chain.md))
- LP dual gives shadow prices `u_i*` and active set `A*(T)` for the proton.
- `g_A = |⟨O_A⟩_T| / |⟨O_V⟩_T|` evaluated on the active set.

**Backing:** `prop:confinement-frobenius-reciprocity` (stated, has `sorry`).

**Class:** DERIVED.

**Current value:** q-dependent; tolerance ~5% pending isospin-projector tightening (see `2026-05-06-frobenius-pairing-compute-audit.md §3.1`).

**Audit:** OK. Clean win — bug found and fixed; trail preserved in `_deprecated/`. Tightening to <1% requires `prop:categorical-clebsch-gordan` (isospin projector on bound states).

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-401]** — `prop:confinement-frobenius-reciprocity` has `sorry`; discharge requires the bound-state master formula proof (DEEP-2026-05-08-106).

**[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-402]** — Isospin projector on bound states (`prop:categorical-clebsch-gordan`) not yet authored; gates the g_A tolerance from ~5% to <1%.

### A.2 `V_ud` — CKM matrix element

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-403]**
- file: (no file exists)
- description: V_ud is **completely absent from the codebase**. The CKM matrix is not represented categorically.
- backing: NONE
- remediation: Either (a) author `conj:ckm-from-categorical-ew` deriving V_ud from EW gauge structure; or (b) explicitly document that the CKM matrix is outside QOU scope.

### A.3 `G_F` — Fermi constant

**Compute path:** `G_F = g_W² / (8 m_W²)` is the standard relation; in QOU, `G_F` is **input** (CODATA value `1.166e-11 MeV⁻²`) and used to **extract** `N_v` via the `G_F ∝ N_v⁻⁴` relation in the weak crossing-count formula.

**Class:** FITTED (input); inversion produces a HEURISTIC value of N_v.

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-404]** — G_F is FITTED (CODATA); the `N_v` extracted by `G_F → N_v` inversion is HEURISTIC because the inversion direction is not the "categorical → physical" direction. Every downstream weak-rate prediction is therefore not a prediction.

### A.4 `N_v` — number of weak-sector crossings

**Backing conjecture:** `conj:n-v-bring-action` (UNPROVED).

**Status of attempts:**
- W-2 numerical-search line **closed as null result**: constrained PSLQ on `tr_pure`-based basis returns 0 hits at CODATA tolerance for 116 k-element bar-symmetric basis; FDR ≈ 0.06 (per `2026-05-05-nv-categorical-impasse.md`).
- No alternative derivation in flight at HEAD.

**Class:** HEURISTIC (extracted from G_F).

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-405]** — `conj:n-v-bring-action` is the **single largest gating gap** in the weak sector. Every G_F-dependent prediction (β-decay rate, CKM unitarity, EW precision tests) is conditional on this conjecture.

### A.5 `sin²θ_W` — Weinberg angle

**Compute path (current):**
- `staircase_ew_predictions.py`: ρ_4=(4,3,2,1) β_EW top eigenvalue is degenerate; only ρ_3=(3,2,1) gives non-degenerate split.
- `close_321_weinberg_gap.py`: `cot θ_W ≈ (max+/2nd-max+ of M_(3,2,1)) · q^(1/h_corner)` closes 2.19% gap → 0.13%, where `h_corner = 5` is the corner hook of (3,2,1).
- Hook-ratio derivation falsified: `[5]_q/[4]_q = 1.270 ≠ 1.783` (eigenvalue ratio).

**Backing:** `conj:hoefsmit-ew-cell-content` (UNPROVED), `conj:weinberg-angle-categorical` (open, gated on linking + Hoefsmit + Higgs-vev).

**Class:** EMPIRICAL_FIT (eigenvalue pattern-matching). The choice of denominator `(max+/2nd-max+)` and the correction factor `q^(1/h_corner)` were arrived at by closing the gap, not derived from first principles.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-406]** — sin²θ_W extraction is pattern-matching: the formula was selected to close the residual gap. Either prove `conj:hoefsmit-ew-cell-content` and `conj:weinberg-angle-categorical`, or reclassify θ_W as EMPIRICAL_FIT in the witness JSON.

## §B. Q-values

### B.1 `Q_n` — free-neutron β⁻ decay (calibration anchor)

`Q_n = m_n − m_p − m_e = 0.78233 MeV` (CODATA).

**Use:** Calibrates `E_0 = Q_n / |Δ(net)|` in `mass_formula_6term.py`.

**Class:** FITTED (calibration anchor; the third constant of the framework).

**Audit:** OK *as long as* the paper acknowledges Q_n as the third calibration constant.

**[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-407]** — Confirm paper text labels Q_n as a calibration anchor, not a "prediction".

### B.2 `Q_β(³H → ³He)`, other isotope Q-values

**Compute:** From the symbolic GB-NF formula `Q_β = |Δ(net)| · E_0`.

**Class:** DERIVED algebraically (the formula follows from GB normal forms).

**However:** The numerical value depends on:
- `E_0` (FITTED via Q_n)
- The knot assignment for ³H and ³He (HEURISTIC; census-assigned per [01 §B](01-baseline-mass-table.md))

So while the *formula* is DERIVED, the *prediction* inherits HEURISTIC status from the knot assignment.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-408]** — Isotope Q-value predictions inherit HEURISTIC status from knot census-assignment (DEEP-2026-05-08-110, DEEP-2026-05-08-307).

## §C. Isospin breaking δ_I

### C.1 `beta_ew_delta_I_*` family

Six scripts: `_321_and_wedderburn`, `_conjugate_pairing`, `_eigenvalues`, `_full_spectrum`, `_numerical_spectrum`. Plus the recent `staircase_ew_residual_conjecture.py` (PR #560, k=4 verified).

**Recent finding (verified per memory):** Staircase EW q^(1/(2k-1)) confirmed for k=4: dim-768 spectrum of β_EW on ρ_4=(4,3,2,1), pairwise ratio e[254]/e[188]=1.01357 matches q^(1/7)=1.01502 (rel.err 0.14%).

**Class:** DERIVED at the spectral level; the IDENTIFICATION of δ_I with the q^(1/h_corner) residual is HEURISTIC (correct in numerical agreement, but the categorical reason is not formalised).

**[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-409]** — δ_I = q^(1/(2k-1)) residual is verified numerically but lacks a `prop:` block giving the categorical statement of the correspondence.

## §D. Beta-decay scripts inventory

| Script | Inputs | Class | Flag |
|--------|--------|-------|------|
| `borromean-axial-coupling.py` | Frobenius G + LP duals | DERIVED (post-fix) | DEEP-2026-05-08-401 |
| `c_alpha_from_Q_beta_trace.py` | Q_β values + Markov trace | DERIVED algebraically | inherits 408 |
| `beta-decay-energy-scale.py` | E_0 from Q_n | FITTED anchor | OK |
| `beta-decay-from-q.py` | q-symbolic | DERIVED | — |
| `beta-decay-matrix.py` | EW matrix elements | DERIVED modulo δ_I | inherits 409 |
| `beta_ew_delta_I_*.py` (6 scripts) | spectrum of β_EW(δ_I) | DERIVED spectrum, HEURISTIC identification | DEEP-2026-05-08-409 |
| `free-neutron-decay.py` | Q_n + g_A + V_ud | mixed; **V_ud absent** | DEEP-2026-05-08-403 |
| `staircase_ew_residual_conjecture.py` | ρ_3, ρ_4 spectrum | DERIVED; conjecture for k≥3 | OK; conjecture is open |
| `bw_chirality_isotopes.py` | bw chirality table | EMPIRICAL_FIT | DEEP-2026-05-08-410 |
| `categorical_q_decay_ba_low_isotopes.py` | low-iso β-decay rate q-poly | DERIVED algebraically; HEURISTIC ladder coeffs | DEEP-2026-05-08-310 (cross-ref) |
| `sigma_all_symbolic_decay.py` | full σ-symbolic decay | DERIVED | OK |

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-410]** — `bw_chirality_isotopes.py` chirality table is EMPIRICAL_FIT; per [07 §B.1](07-crystal-bases-optimizations.md) replaceable by Type-B-folded bar-involution projector.

## §E. LP/SDP dual infrastructure (β-decay scripts)

Per memory: 58/58 historical LP/SDP witnesses lacked dual variables before the 2026-05-07/08 backfill. Per `2026-05-08-lp-dual-wired-audit.md`, the validator now supports `--list-wired` and `--strict-wired` to enforce duals only on *wired* witnesses (not all 58).

Status of β-decay scripts re LP-dual emission:
- `borromean-axial-coupling.py` ✅ wired (uses `lp_dual_solver.py`)
- `pn_alpha_lp_dual.py` ✅ wired
- `lp-duality-check.py` (probe) ✅ wired
- Other LP-using β-decay scripts: status mixed — see `2026-05-08-lp-dual-wired-audit.md` for the per-script list.

**[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-411]** — Run `bun run scripts/audit-wiring.ts` and confirm all *wired* β-decay LP/SDP witnesses pass `lp_dual_witness_validator.py --strict-wired`. Open follow-on PR for any failures.

## §F. Top-15 critical gaps (β-decay)

| # | Flag | Gap | Severity |
|---|------|-----|---------:|
| 1 | DEEP-2026-05-08-405 | `conj:n-v-bring-action` UNPROVED — gates entire weak sector | critical |
| 2 | DEEP-2026-05-08-403 | V_ud completely absent from codebase | critical |
| 3 | DEEP-2026-05-08-404 | G_F → N_v inversion is reverse-direction; N_v not categorical | critical |
| 4 | DEEP-2026-05-08-406 | sin²θ_W is EMPIRICAL_FIT pattern-matching | high |
| 5 | DEEP-2026-05-08-401 | `prop:confinement-frobenius-reciprocity` `has_sorry` | high |
| 6 | DEEP-2026-05-08-408 | Isotope Q_β inherits HEURISTIC status from knot census-assignment | high |
| 7 | DEEP-2026-05-08-410 | `bw_chirality_isotopes` table EMPIRICAL_FIT | high |
| 8 | DEEP-2026-05-08-402 | Isospin projector `prop:categorical-clebsch-gordan` not authored | medium |
| 9 | DEEP-2026-05-08-409 | δ_I = q^(1/(2k-1)) numerical match lacks `prop:` block | medium |
| 10 | DEEP-2026-05-08-407 | Confirm paper labels Q_n as calibration anchor | medium |
| 11 | DEEP-2026-05-08-411 | Run wired-LP-dual audit on β-decay scripts | medium |

## §G. β-decay dependency DAG

```
conj:n-v-bring-action (UNPROVED)  ←─── W-2 null result
   │
   ├─→ N_v derivation
   │      │
   │      ├─→ G_F prediction
   │      │      └─→ all weak-rate predictions
   │      └─→ CKM unitarity (if V_ud authored — it isn't)
   │
   └─→ sin²θ_W categorical derivation
          │
          ├─→ conj:hoefsmit-ew-cell-content (UNPROVED)
          ├─→ conj:linking-operation (UNPROVED)
          └─→ conj:categorical-higgs-mechanism (UNPROVED)

prop:confinement-frobenius-reciprocity (HAS_SORRY)
   │
   └─→ g_A derivation
          │
          └─→ prop:categorical-clebsch-gordan (NOT AUTHORED)
                 └─→ tightens g_A from ~5% to <1%

knot census-assignment for ³H, ³He (HEURISTIC)
   │
   └─→ Q_β(³H → ³He) prediction (HEURISTIC)
          └─→ all isotope Q_β predictions
```

**Critical path to weak-sector 1-ppb:** discharge `conj:n-v-bring-action` *or* find an alternative N_v derivation. This is currently the single largest blocker. See [08 §3](08-1ppb-workplan-revised.md) for the proposed alternatives.

## §H. Honest reclassification (recommended)

| Claim | Current framing | Recommended honest framing |
|-------|-----------------|----------------------------|
| g_A | "predicted" | "derived (post-fix); tolerance ~5% pending Clebsch-Gordan" |
| sin²θ_W | "0.13% match" | "EMPIRICAL_FIT (eigenvalue pattern-matching); proof requires three open conjectures" |
| Q_β isotopes | "predicted" | "DERIVED algebraically modulo HEURISTIC knot assignment" |
| G_F | "categorical relation" | "FITTED input; used to extract HEURISTIC N_v" |
| V_ud | (absent) | "outside current scope; conj:ckm-from-categorical-ew not yet authored" |
| EW δ_I | "predicted via β_EW spectrum" | "DERIVED at spectral level; identification with δ_I is HEURISTIC modulo `conj:staircase-ew-residual`" |
