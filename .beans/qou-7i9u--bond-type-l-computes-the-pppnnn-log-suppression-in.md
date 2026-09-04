---
# qou-7i9u
title: _bond_type_L computes the pp/pn/nn log-suppression in float64 inside a witness-emitting producer
status: todo
type: task
priority: normal
created_at: 2026-09-03T14:56:24Z
updated_at: 2026-09-03T14:56:24Z
---

Found 2026-09-03 while reading what the production pp/nn bond IS (session qou-s42j follow-up).

DEFECT: computations/binding_single_pipeline_comparison.py::_bond_type_L does
    out[key] = math.log(float(tf) / float(ta))
on the 50-dps mpf traces from tr_m_atom_zn — a float64 cast + math.log inside a producer that emits binding-single-pipeline-comparison.witness.json. This violates the NO-FLOAT64 rule for computations/ (AGENTS.md §Precision preflight; probes are not exempt either). _forms() in the same file also uses math.log / float arithmetic on tf, ta.

IMPACT: the two-nucleon SIGN conclusion is unaffected (tf/ta is far from 1 for pp/pn/nn, so float64 cannot flip log's sign), but every L_pp/L_pn/L_nn digit past ~1e-16 in that witness is float64 noise presented at witness precision, and downstream B_qCLT_fac_* inherit it.

FIX (one producer): carry mp.mpf end to end — L = mp.log(tf/ta) with tf, ta as mpf; drop float() casts in _forms (use mp arithmetic; format with _precision.fmt or mp.nstr for display); re-run the producer (fast: ⁶Li/⁷Li via transfer ~0.2 s each per its docstring) with 2>&1 | tee, regenerate the witness, run scripts/precision-gates.sh --changed, confirm the producer leaves the raw-float64 ratchet's dirty list. Do NOT widen a baseline.
