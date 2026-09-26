---
# qou-rp9i
title: 'Cyclic-triple word class re-read under the surviving log binding law (#6611): extensive now, and measured against the log-law residuals'
status: completed
type: task
priority: normal
created_at: 2026-09-04T10:25:55Z
updated_at: 2026-09-04T10:28:53Z
---

Branch claude/cyclic-triple-under-log-law-2026-09-04. Re-reads qou-sorn's cyclic-triple result under the law #6611 leaves standing, B = E_0·ln(tr_free/tr_atom), E_0 = m_e/(q0(q0−1)) = 4.18598 MeV (derived).

STRUCTURAL: a monotone word's log-trace is a sum of run log-traces, so a cyclic triple at bond k shifts B by a per-bond constant E_0·ln(f_prod/f_cyc) that depends only on the bond's species pair + adjacent nucleon — EXTENSIVE (checked to 50 dps across nuclei: p–p +3.773, p–n +5.653, n–n +14.093 MeV per bond). Under the linear law the same reorder was intensive; this is a change in kind, hence the re-read.

RESULT (probe cyclic_triple_under_log_law_probe.py, 20/20, closed forms = production tr_m_atom_zn to 50 dps): log-law residuals 2H −0.61 (already over-bound), 3H +1.85, 3He +2.83, 4He +19.61 MeV; all-bonds-cyclic ΣΔB = +5.65 / +19.75 / +9.43 / +23.52 → B_cyc/AME = 3.81 / 3.11 / 1.85 / 1.14×. Over-shoots everywhere; wrong-signed at 2H; species pattern n–n ≫ p–n > p–p is the +N−Z asymmetry #6611 already RETRACTED (data wants κ ≈ −0.15), 3–4× larger; the n–n figure is a near-cancelled block (0.012) so 3.4 nats is fragility.

VERDICT scope-(a) negative under the log law too, for a different reason. Weakens qou-sorn's 'not a functional of tr_M' (a reorder IS extensive under log) but the cyclic triple is the wrong functional. Recommendation (judgement): default, the log law's own lead is the symmetry energy and this class supplies the wrong-sign asymmetry.

RETRACTION SWEEP (qou-2pnv): my own two linear-law surfaces from this morning (qou-sorn audit doc + cyclic_triple_bond_cross_term_probe.py docstring) now carry superseded-law notes. Audit: docs/audits/2026-09-04-cyclic-triple-under-log-law.md. Nothing wired or fitted.
