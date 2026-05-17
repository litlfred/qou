# P4‴ migration — atomic_braid_mass_table downstream consumer triage (2026-05-17)

> Per [`docs/coordination/1ppb.md`](../coordination/1ppb.md) §Open
> phases · P4‴: "migrate legacy `atomic_braid_mass_table.py` and
> downstream consumers to the ρ_K path."

## Finding: four consumers cannot mechanically swap witnesses

The 12 files that reference `atomic_braid_mass_table` split as:

| Category | Files | Action |
|----------|-------|--------|
| **Docstring/comment mentions only** | `brane_tower_isospin_diagnosis`, `derived_masses`, `atomic_braid_mass_terms`, `probe_shift_derivation_provenance`, `atom_mass_derived`, `derivation_chain`, `m_n_difference_formula`, `braid_encoding_audit`, `atomic_mass_via_rho_k` | No-op (mentions, not consumers) |
| **Audit-only consumers of legacy six-term decomposition** | `compound_binding_via_differences`, `delta_n2_placeholder_audit`, `neutron_error_diagnostic`, `deuteron_delta_i_audit` | Add P4‴ banner; **retain on legacy witness by design** |

The four audit consumers extract legacy-only fields:
`term1_atomic_total`, `term2_markov_z2`, `term3_markov_z4`,
`term4_frobenius_codim`, `term6_cyclotomic_tail_MeV`, `total_hecke`.

These per-term fields **do not exist** in the canonical
[`atomic-mass-via-rho-k.witness.json`](../../folio-assistant/computations/atomic-mass-via-rho-k.witness.json),
because the resolved formula `M(K) = ρ_K · m_e · |tr_M(K)|`
(per `AUDIT-DEEP-2026-05.md` §3.3a Options A + C, landed via
PR #564) is **not** an additive six-term sum. The canonical
witness emits per-atom `M_pred_MeV` / `err_pct` only.

Therefore the four consumers cannot mechanically swap their
witness reads — they probe a structural decomposition the canonical
path **does not have**. They remain audit-only diagnostic
consumers of the legacy witness, by design.

## What this PR delivers

1. **Each of the four audit consumers** carries an in-file P4‴
   banner noting:
   - it reads legacy six-term decomposition by design,
   - mass predictions live in the canonical ρ_K witness,
   - the specific legacy fields it depends on.

2. **The legacy script's deprecation notice**
   ([`atomic_braid_mass_table.py`](../../folio-assistant/computations/atomic_braid_mass_table.py))
   now explicitly lists the four audit-only retained consumers
   so future migration efforts don't redundantly re-triage them.

3. **All four scripts continue to run cleanly** (exit 0).

## What this PR does NOT close

- **Mass-prediction consumers** flagged in the original deprecation
  notice (`atomic_braid_mass_table_modes_sweep.py`,
  `mass_formula_6term_mpfr_50dps.py`,
  `paper_six_term_isotope_sweep.py`) remain open — they emit
  predicted masses, not diagnostic decompositions, and a real
  migration is possible. Not in scope for this PR.

- **P3** (real `H_{3A}` Wedderburn weights → ρ_K refinement toward
  780 ppb floor) is the substantive math lever that follows P4‴.
  The building blocks (V_(2,1) closed form from PR #672,
  height-6 partition enum) are in place; what's needed is
  computing the **Markov-trace y_λ** (not Plancherel weights —
  these diverge at H_n ≥ 4) per atomic braid.

## Net delta

- 4 files: in-file P4‴ banner added before `s3 = json.loads(...)`
- 1 file: legacy script's deprecation notice expanded with the
  retained-consumer list
- 0 behavioral changes; all 4 still exit 0
- 0 new conjectures; 0 new Mathlib upstream deps
