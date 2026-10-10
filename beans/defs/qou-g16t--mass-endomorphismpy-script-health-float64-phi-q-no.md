---
# qou-g16t
title: 'mass_endomorphism.py script health: float64 Phi_q, non-Molien weights, crashing diagnosis caller'
status: completed
type: task
priority: normal
created_at: 2026-10-10T07:00:16Z
updated_at: 2026-10-10T08:01:23Z
parent: qou-d8c7
---

Carrier M7 of the mass-endomorphism epic. `computations/mass_endomorphism.py` (and its
generated mirror `qou-mass/src/qou_mass/_internal/mass_endomorphism.py`, which must not be
hand-edited — regenerate with `scripts/sync-qou-mass-vendor.py`) had defects spread across
five beans and owned by none of them.

Verified on `main` 2026-10-10:

- `Phi_q` computes in float64 (`product = 1.0`, `1e-300` guard) beside an mpmath twin
  `Phi_q_mp` (about lines 146 / 280). Source: `qou-47sx`.
- `w_sym`, `w_std`, `w_alt` are self-normalised `dim_q^2/[3]_q!` (about lines 136-138), not
  the owner-ruled Molien weights. They feed `m_p_m_e_li2q`, an already-recorded 407 % miss,
  so no published number moves. Source: `qou-oots`.
- `additive_wedderburn_volumes` is float64. Source: `qou-oots`.
- `brane_tower_isospin_diagnosis.py:180` still crashes against the module; `qou-47sx`'s
  verdict is retire or port, not patch.
- Already resolved, recorded for completeness: `z_mark` is convention D
  (`q^3/(q^2+1)`, `qou-lbgh`, `qou-bsec`); production binding uses `towerTerm`, not `Phi_q`
  (`qou-2tuv`).

Next honest step: decide retire-vs-port for the diagnosis script, then carry the module to
mpf end to end per the NO-FLOAT64 rule and run `scripts/precision-gates.sh --changed`.
Changing the weights is an owner-ruled change and moves no live number; say so in the PR.

## 2026-10-10 — CORRECTION to this bean's own body, and the port (issue #7552)

**What I asserted above, and what is true.** The body says the weights
`w_sym, w_std, w_alt` (self-normalised `dim_q^2/[3]_q!`) are "not the owner-ruled
Molien weights" and that changing them "is an owner-ruled change". **Both overstate
the ruling.** The Molien choice (owner, 2026-09-05, re-affirmed 2026-09-08, bean
`qou-oots`) is scoped to the **Φ_k functional** of
`docs/audits/2026-09-05-phi-k-weight-family.md` — a log-ratio that is not a trace.
The H_3 Wedderburn average in `additive_wedderburn_volumes` is a different object.
The same weights are also hard-coded in `substrate/hecke_core.py` (`W_SYM` …),
`crt_markov.py`, `pn_alpha_lp_dual.py` and `pyhecke/atom.py`, so switching this
module alone would make it disagree with them. **The swap is not a corpus-derived
change and is not proposed.** The same wording sits in the M7 row of epic
`qou-d8c7`; corrected there by an appended note.

**Precision item: nothing to change inside the module.** It already carries an mpf
twin of every f64 function and writes its witness from the mpf side; the f64 half
is kept by documented design for ~40 importers. Re-run 2026-10-10: witness numbers
reproduce byte-identically. "Carry the module to mpf end to end" is really the
importer sweep tracked by `qou-47sx`, not a fix in this file.

**Diagnosis script: PORTED (owner chose port over retire).**
`computations/brane_tower_isospin_diagnosis.py` now uses
`mass_at_3A_proper.per_generator_V_hat_3A` (with `QOU_H3A_MPF=1`) and
`mass_endomorphism.Phi_q_mp`. Measured: no generator reaches the Φ_q pole at q0;
the neutron's second quark generator, |V̂| = 1.08837 (about 2 % below q0), gives
Φ_q = 2.77e7 and dominates. Σ Φ_q(³He) − Σ Φ_q(T) = −2.24e7 Hecke units — opposite
sign and ~37× the old H_3 figure. ⁴He is NOT computed: the mpf seminormal path
hands an object-dtype matrix to `scipy.sparse` at 12 strands (already
tracked as `qou-fmoi`, "exact chi_lambda at A=4 needs a sparse-mpf character
product"; a pointer note is appended there).



2026-10-10: closed on merge of PR #7554. Crashing caller ported to mpf; module precision unchanged by design. Remaining importer sweep stays with qou-47sx; the A=4 sparse-mpf wall stays with qou-fmoi.

2026-10-10 (bean qou-we2d, PR #7557): Lean now proves the Molien weight M_mu(q^2) = q^{-kappa}/prod[h]_q is the z = 0 Markov trace and equals the symmetrising trace tau(T_w)=delta_{w,1} (QOU.SchurWeyl.SeminormalRep.molienMarkovTrace_symmetrising, eq_molien_of_zero; ocneanuWeight q 0 = molienWeight). Consequence for this bean: Molien as a TRACE weight has z = 0, so any channel that needs a Markov property with z != 0 (interface mu = tau(sigma)) cannot use it; Molien as a MEASURE is unaffected.
