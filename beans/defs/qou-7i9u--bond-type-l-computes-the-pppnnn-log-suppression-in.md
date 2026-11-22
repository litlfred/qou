---
# qou-7i9u
title: _bond_type_L computes the pp/pn/nn log-suppression in float64 inside a witness-emitting producer
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T14:56:24Z
updated_at: 2026-11-22T21:33:06Z
parent: qou-9nnz
---

Found 2026-09-03 while reading what the production pp/nn bond IS (session qou-s42j follow-up).

DEFECT: computations/binding_single_pipeline_comparison.py::_bond_type_L does
    out[key] = math.log(float(tf) / float(ta))
on the 50-dps mpf traces from tr_m_atom_zn — a float64 cast + math.log inside a producer that emits binding-single-pipeline-comparison.witness.json. This violates the NO-FLOAT64 rule for computations/ (AGENTS.md §Precision preflight; probes are not exempt either). _forms() in the same file also uses math.log / float arithmetic on tf, ta.

IMPACT: the two-nucleon SIGN conclusion is unaffected (tf/ta is far from 1 for pp/pn/nn, so float64 cannot flip log's sign), but every L_pp/L_pn/L_nn digit past ~1e-16 in that witness is float64 noise presented at witness precision, and downstream B_qCLT_fac_* inherit it.

FIX (one producer): carry mp.mpf end to end — L = mp.log(tf/ta) with tf, ta as mpf; drop float() casts in _forms (use mp arithmetic; format with _precision.fmt or mp.nstr for display); re-run the producer (fast: ⁶Li/⁷Li via transfer ~0.2 s each per its docstring) with 2>&1 | tee, regenerate the witness, run scripts/precision-gates.sh --changed, confirm the producer leaves the raw-float64 ratchet's dirty list. Do NOT widen a baseline.

## Progress Update (Round 49 — PR #8170)

- Lifted `_bond_type_L()`, `_constants()`, `_load_canonical_traces()`, `_transfer_traces()`, and `_forms()` in `computations/binding_single_pipeline_comparison.py` from `float` / `math.log` to `mpmath.mpf` / `mp.log` at `compute_dps=70` (`set_compute_dps()`).
- Regenerated `computations/binding-single-pipeline-comparison.witness.json` via `_precision.fmt` with `0` raw float64 values.
- PR: https://github.com/litlfred/qou/pull/8170 (`8b83507c7e14547848b5b991bdd3396fc7f3a703`)

## 2026-11-22 — CLOSED: the fix is on main via port #8170 (bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Checked against main `3c4c98fccf3`.

The "Progress" entry above records the fix on a batch PR that never merged. It reached main as `ca6b5d6dd9` ("port #8170: ..."), which names this bean. Verified on main: `_bond_type_L` in `computations/binding_single_pipeline_comparison.py` has no `math.log`/`float(` left and uses `mp.log`.

## 2026-11-22 — Applicability review (owner instruction 2026-11-22, bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Retroactive review of this pass's closure against `docs/coordination/owner-rulings.md` on main `3c4c98fccf3`.

**Verdict: ALREADY-DONE, with a scope flag.** The precision fix (float64 removed from `_bond_type_L`) stands and is what the bean asked for. But the object it computes, the pp/pn/nn log-suppression of the single-crossing interface letters of `atom_braid_word_3A`, is on a word the owner superseded on 2026-11-15 (γγ rule covers the nuclear bond letters; `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`). So the numbers this producer prints are records, not canonical. No reopening: a precision fix to a superseded producer is still correct.
