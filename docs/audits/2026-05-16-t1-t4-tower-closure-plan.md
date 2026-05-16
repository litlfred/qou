# T1+T4 mass-endomorphism tower closure — audit + plan

**Date**: 2026-05-16
**Trigger**: User option 3 + 2 on PR #663 — "try a tightening (30 min
budget), then write a research plan / sub-task breakdown"
**Conclusion**: structural gap, not numerical; multi-PR research work.

## Audit finding

The proton-mass chain ([`build_proton_mass_50dps_chain.py`](../../folio-assistant/computations/build_proton_mass_50dps_chain.py))
produces `m_p_pred = 0.5974 MeV` vs CODATA 938.272 MeV — a gap of
**9 orders of magnitude**. The chain's own derivation.json marks the
T1+T4 mass-endomorphism tower assembly as `SCRIPT_CITED`; this audit
identifies *what specifically* is missing.

### Trace

`build_proton_mass_50dps_chain.py` step 6 computes

```
m_p_pred_MeV = (M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE) × M_E_MEV_CODATA
             = (2.341 / 2.003) × 0.51100
             = 1.169 × 0.51100
             = 0.597 MeV
```

The ratio `M_P_HECKE / M_E_HECKE = 1.169` should be ≈ 1836.15 (CODATA
m_p/m_e). The framework is producing the right *kind* of object
(dimensionless mass ratio × CAL-1 scale) but the ratio's magnitude is
off by a factor of 1571 (~63 ppm to the correct value when squared
into the m_p prediction, but ~10^6 to the correct m_p MeV scale).

### Why M_P_HECKE = 2.341 instead of ~4000

[`derive_m_p_hecke_path_a.py`](../../folio-assistant/computations/derive_m_p_hecke_path_a.py)
line 126 makes the truncation explicit:

```python
m_p_hecke_partial = t1 + t4
```

— only T1 (descended trace) and T4 (Frobenius co-Casimir per vortex)
are summed. The full tower per [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
is

```
𝔪(β) = |Π V̂_i|  +  Σ_i Φ_q(|V̂_i|)  +  Σ_{i<j} z² · Φ_q(|V̂_i V̂_j|)  +  τ(C_dim_q)  +  …
        ──T1──     ─────T2──────       ───────T3────────────         ─T4─
```

For the proton, T1 ≈ 1.065, T4 ≈ 1.276, sum 2.341 — what we observe.
T2+T3 should add the brane-tower blow-ups. By comparison with
deuteron in the 6-term witness:

| Atom | T1 | T2 (single) | T3 (pair) | T4 | T5 chirality | T6 habiro |
|---|---:|---:|---:|---:|---:|---:|
| p   | 1.065 | **0.0** | **0.0** | 1.276 | -7.79 | 0.681 |
| n   | 0.923 | **0.0** | **0.0** | 1.276 | -7.47 | 0.681 |
| D   | 0.388 | 905,477 | 62,150 | 2.552 | -5.63 | 0.042 |
| T   | 0.104 | 1,381,420 | 190,668 | 3.828 | 8.52 | 0.0006 |
| ³He | 0.207 | 1,335,045 | 180,422 | 3.828 | 7.78 | 0.0006 |

For p and n, T2 and T3 are **explicitly zero with an error**:

```
"term23_error": "KeyError: 'No MPFR-native per-generator volumes
                 found for Z=1, N=0 in ...'"
```

So the gap is **not** "the tower formula is wrong" or "the
arithmetic is wrong at 50 dps" — it is "the proton and neutron rows
were never wired into the MPFR-precision per-generator-volume table
that [`mass_formula_6term_mpfr_50dps.py`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)
consumes for T2+T3".

### Sanity check via the float64 path

[`mass_endomorphism.atom_per_generator_volumes`](../../folio-assistant/computations/hecke_core.py)
*does* return per-generator volumes for proton (Z=1, N=0) at float64:

```python
>>> from hecke_core import atom_per_generator_volumes
>>> atom_per_generator_volumes(1, 0)
[{'std': 1.146, 'sym': 1.880, 'alt': -0.538, 'full': 0.989},
 {'std': 0.930, 'sym': 0.735, 'alt':  1.375, 'full': 0.971}]
```

So the volumes are computable; what's missing is their **MPFR
lift** for the proton/neutron rows in
`mass-formula-6term-mpfr-50dps.witness.json`. The deuteron and
heavier atoms have their MPFR per-generator volumes wired
(producing the 905,477 / 62,150 etc. above); the single-strand atoms
do not.

### Quick float64 estimate of what T2+T3 would add

Using float64 volumes ≈ {0.989, 0.971} for the proton, both close
to q₀⁻¹ = 0.901:

```python
Phi_q(|0.989|) → very large (Φ_q diverges as z → q₀)
Phi_q(|0.971|) → also large
z² · Phi_q(|0.989·0.971|) → also large
```

The float64 `mass_endomorphism.mass_from_tower(proton_cross)` (run
directly) produces a result in the order of 10⁴–10⁵, not 2.34.
That order of magnitude is what the proton needs for m_p_hecke/m_e_hecke
to land near 1836.

**Net diagnosis**: the proton/neutron 9-order-of-magnitude gap is a
**wiring gap**, not a structural gap. The mass-endomorphism tower
formula is correct; the bridge from `atom_per_generator_volumes`
(float64) to MPFR is missing for {Z=1, N=0}, {Z=0, N=1}, and the
electron's 2-strand single-generator atom.

## Why "30 min tightening" is not sufficient

Patching this requires:

1. **Add the MPFR per-generator-volume entries** for proton, neutron,
   electron in `mass_formula_6term_mpfr_50dps.py`'s lookup table.
   This means producing a high-precision (50 dps) computation of
   the Wedderburn-block-resolved volumes (`std`, `sym`, `alt`,
   `full`) for the single-strand atoms.
2. **Cross-check** the float64 estimate against the MPFR version
   to confirm no precision-related cancellation.
3. **Re-run** `mass_formula_6term_mpfr_50dps.py` → re-run
   `derive_m_p_hecke_path_a` → re-run
   `build_proton_mass_50dps_chain.py` → check that the new
   `m_p_pred_MeV` is in the right ballpark (≲ 1 ppm of CODATA).
4. **Audit possible truncation issues** at Φ_q's convergence when
   |V̂| is very close to q₀ (the float64 `Phi_q` returns `inf`
   for `|z| >= q₀` — MPFR may not).
5. **Re-derive** with attention to `term5_chirality_bw` and
   `term6_habiro_residue` (they're already wired but their sign
   structure needs to be sanity-checked against the new ~10⁴ T2+T3
   magnitudes).

Step 1 alone is a substantial sub-task (the MPFR per-generator
volume derivation has its own chain to close). Steps 4 and 5 are
where unexpected residuals may surface; precision-floor diagnosis
in the same vein as PR #657's "underdetermined at CODATA Q_β floor"
finding is likely.

## Concrete sub-tasks (separate PRs)

Listed in dependency order. Each one is one-PR-sized.

### PR-X1 — MPFR per-generator volumes for {p, n, e}

- **Producer**: extend
  [`mass_formula_6term_mpfr_50dps.py`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)'s
  per-generator-volume lookup to include Z=1/N=0 (proton),
  Z=0/N=1 (neutron), and the electron's 2-strand single-generator
  atom.
- **Numeric**: lift `atom_per_generator_volumes` (currently float64)
  to a 50-dps MPFR variant; verify each entry's float64 ↔ MPFR
  agreement to ~10⁻¹⁴.
- **Output**: extended
  `mass-formula-6term-mpfr-50dps.witness.json` with non-zero T2, T3,
  and a clean `term23_error: None` for p, n, and electron.
- **Verification**: re-run `derive_m_p_hecke_path_a` and confirm
  `m_p_hecke` is in the 10³–10⁴ range (rather than 2.34).

### PR-X2 — Validate the m_p/m_e ratio at the new T2+T3 magnitudes

- After PR-X1, the m_p/m_e ratio should be checkable against CODATA
  1836.15 directly.
- Likely surfaces residual issues in T5 / T6 weighting (signs,
  inter-block normalisation) — handle as they appear.
- **Output**: `proton-mass-codata-50dps.witness.json` rewritten with
  the closed chain; `allPassed = true` at some precision rung
  (target 1 ppm, stretch 1 ppb).

### PR-X3 — Tighten `M_P_DERIVED_MAX_REL_DIFF` on the no-cal chain

- After PR-X2 lands, lift the sanity threshold in
  [`low_isotope_mass_table.py`](../../folio-assistant/computations/low_isotope_mass_table.py)
  from 1 % to either 1 ppm or whatever precision rung PR-X2 closes
  to. ¹H row lifts from `derivation_pending` to genuinely
  `derived` (with a small residual reflecting the actual prediction
  error).

### PR-X4 — Cascade to {²H, ³H, ³He, ⁴He+}

- With m_p and m_n both derived (and PR #666's Δ_λ catalog wired),
  the binding sub-table cascades through `low-isotope-mass-table.witness.json`.
- ²H, ³H, ³He lift to `derived`; ⁴He awaits the H_12 canonical
  tr_M closure (the long-standing open frontier).

## Anti-pattern guard

Per CLAUDE.md "Don't add features beyond what the task requires"
and the no-calibration rule: at no point should the closure
introduce a fit parameter, an empirical offset, or a CODATA m_p
injection. The 1 % rel-diff sanity threshold on PR #663 is the
gate against accidentally re-introducing the historical 543 ppm
calibration-leak pattern that produced the ¹H tautology in the
first place.

If PR-X2's closed chain lands with `m_p_pred_MeV` close to but not
on CODATA, the **residual is the deliverable** — record it
honestly in the `m_p_within_1_ppb` assertion (currently false)
and propagate the actual number into all downstream witnesses.
The chain becomes useful when the residual is small *and* it
emerges from CAL-1/2/3 alone.

## Coordination

- This audit's findings will be referenced from
  [`docs/coordination/isotope-mass-witness-data.md`](../coordination/isotope-mass-witness-data.md)
  as the post-#663 watch item.
- PR-X1 through PR-X4 are sequential — each unblocks the next.
- The single-strand MPFR per-generator-volume gap (PR-X1) is the
  ONE THING that unblocks every downstream piece. It is the
  highest-leverage next step on the mass-prediction track.
