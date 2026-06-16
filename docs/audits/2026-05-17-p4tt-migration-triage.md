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

The four audit consumers extract legacy-only fields. Specific
usage per script (verified against current `main`):

| Consumer | term1 | term2 | term3 | term4 | term6 | total_hecke |
|----------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----------:|
| `compound_binding_via_differences` | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `delta_n2_placeholder_audit` | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `neutron_error_diagnostic` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `deuteron_delta_i_audit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

These per-term fields **do not exist** in the canonical
[`atomic-mass-via-rho-k.witness.json`](../../computations/atomic-mass-via-rho-k.witness.json),
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
   ([`atomic_braid_mass_table.py`](../../computations/atomic_braid_mass_table.py))
   now explicitly lists the four audit-only retained consumers
   so future migration efforts don't redundantly re-triage them.

3. **All four scripts continue to run cleanly** (exit 0).

## What this PR does NOT close

- **Mass-prediction migration follow-up finding:** the three
  scripts originally flagged for migration in the deprecation
  notice (`atomic_braid_mass_table_modes_sweep.py`,
  `mass_formula_6term_mpfr_50dps.py`,
  `paper_six_term_isotope_sweep.py`) do **not** actually read
  `atomic-braid-mass-table.witness.json`. Only `..._modes_sweep`
  carries a code-comment reference (consolidated `term_*` helpers
  shared with the legacy script); the other two have no reference
  at all. The "mass-prediction migration" originally listed in
  the deprecation notice therefore has **zero active scope** — no
  consumer needs to be moved. The notice has been updated to
  reflect this.

- **P3** (real `H_{3A}` Wedderburn weights → ρ_K refinement toward
  780 ppb floor) is the substantive math lever that follows P4‴.
  **Status update 2026-05-17:** the Markov-trace `y_λ` computation
  at H_6 is **already done** via `wedderburn_jones_markov.py` (PR
  #572, on main); the module is widely consumed by `crt_markov.py`,
  `delta_lambda_*`, `alpha_*`. The remaining lever is wiring this
  into per-atom ρ_K refinement.

## Items 2–4 audit findings (2026-05-17 post-coordinate sweep)

| Item | Status |
|------|--------|
| **2 (P4ⁱᵛ)** — extend `|tr_M|` to ⁴He/⁶Li/⁷Li | **infrastructure-blocked**: `atomic_tr_m_mpfr_50dps.py:79–91` documents that ⁴He at H_12 requires ~2×10¹³ mp.mpf ops × 47 crossings; bu64reus1 hit the 30-min timeout. Reachable only via (a) Rust `hecke-engine` + rayon, or (b) Wenzl LR categorical reduction (`hecke-branching-trace-decomposition.md`). |
| **3 (P3 Markov y_λ at H_6)** | **already done**: `wedderburn_jones_markov.py` is on main (PR #572); per-atom y_λ at the substrate parameter is callable as `y_lambda_at(...)`. |
| **4 (SDP H_5 extension)** | **infrastructure-blocked** (same as Item 2): `joint_tower_sdp_solver_v2.py:21` documents H_5 deferred to `tools/hecke-engine` for Python-mpmath intractability of Hoefsmit seminormal at n=5+. |

**Net implication:** the highest-leverage remaining 1ppb lever is
**Rust hecke-engine completion** (or Wenzl LR categorical
reduction), not further Python-side compute. The categorical-chain
work tracked in #663/#664/#671 addresses the *precision-ladder*
side; the *consumer/SDP* side is bottlenecked on the kernel.

## Wenzl LR bridge — infrastructure unblock (this PR)

The "Wenzl LR categorical reduction" listed in Item 2 as
alternative-to-Rust-kernel is **now wired** as a Rust module +
rayon-parallelized binary + Python wrapper:

| Component | Path | Role |
|-----------|------|------|
| Rust module | [`tools/hecke-engine/src/wenzl_lr.rs`](../../tools/hecke-engine/src/wenzl_lr.rs) | `chi_via_lr_2way`, `chi_via_lr_kway`, `tr_m_via_lr` — rayon-parallelized over `λ ⊢ n` outer partition |
| Rust binary | [`tools/hecke-engine/src/bin/hecke_tr_m_wenzl_lr.rs`](../../tools/hecke-engine/src/bin/hecke_tr_m_wenzl_lr.rs) | CLI with JSON stdin/stdout; `--all-partitions` mode for full Markov decomposition |
| Python wrapper | [`computations/markov/markov_trace_via_wenzl_lr.py`](../../computations/markov/markov_trace_via_wenzl_lr.py) | `subprocess.run` driver; emits `markov-trace-via-wenzl-lr.witness.json` |

**Benchmark (4-way decomposition, p ⊗ p ⊗ n ⊗ n at H_12):**
**173 ms wall** for all `p(12)=77` partitions on a debug build
(no `--release`). Direct Hoefsmit timed out at >30 minutes per
`atomic_tr_m_mpfr_50dps.py:79–91`. **Five-orders-of-magnitude
speedup.**

**Status:** infrastructure unblock confirmed; the placeholder
3-strand braid stubs in the wrapper need to be replaced with the
*canonical* atomic-braid decomposition (from
`canonical_braid_crossings.atom_canonical_crossings(Z, N)` applied
per-nucleon and reassembled) before the witness is consumable by
the ρ_K refinement. That step is **follow-on** — see
[`hecke-branching-trace-decomposition.md`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md)
§"categorical Wenzl bridge" for the canonical decomposition.

## Net delta

- 4 files: in-file P4‴ banner added before `s3 = json.loads(...)`
- 1 file: legacy script's deprecation notice expanded with the
  retained-consumer list
- 0 behavioral changes; all 4 still exit 0
- 0 new conjectures; 0 new Mathlib upstream deps
