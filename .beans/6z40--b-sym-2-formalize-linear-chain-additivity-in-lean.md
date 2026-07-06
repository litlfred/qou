---
# 6z40
title: 'B_sym #2: formalize linear-chain additivity in Lean (B_sym not a theorem as stated; needs Lean env)'
status: completed
type: task
priority: normal
created_at: 2026-06-20T00:58:14Z
updated_at: 2026-06-21T19:14:34Z
parent: qfzy
---

B_sym = a*ln(tr_free/tr_atom) is a DEFINITION + empirical claim, NOT a theorem. Only Lean is trivial subst;rfl. Provable structural alt: the #2343 linear-chain additivity B_sym = a*[(Z-1)L_pp + L_pn + (N-1)L_nn]. BLOCKED: Lean toolchain un-installable (release.lean-lang.org firewalled, SessionStart elan error).

## Result (2026-06-20) — UNBLOCKED + formalized; pending human close

Lean env recovered this session (Mathlib oleans restored from
`lake-cache/qou-v4-24-0`; lean-direct verification working). Formalized the
provable structural alternative — the #2343 linear-chain additivity — in
`QOU.BraidKnot.BsymLinearChain` (verified sorry-free, `lean` exit 0):
- `chain_num_bonds`: chain `p^Z n^N` has `Z+N-1` bonds (Z,N>=1).
- `chain_count_pp/pn/nn`: per-type counts `Z-1, 1, N-1`.
- `chain_binding_sum` / `Bsym_closed_form`: `B_sym = a*[(Z-1)L_pp + L_pn + (N-1)L_nn]`
  as a `List.sum` identity (generic `CommRing R`, per 7c).
- `Bsym_deuteron`: `B_sym(2H) = a*L_pn` (deuteron = the single p-n bond).

The empirical trace-factorization (audit 1/5, 50-dps verified) stays the named
structural input, NOT asserted in Lean — honouring the bean's definition-vs-theorem
distinction. Audit: `docs/audits/2026-06-20-bsym-linear-chain-additivity-lean.md`.
No production rewire, no fit. The open 4He cooperative alpha-unit magnitude (audit 6)
is untouched.

DEDUP (2026-06-20, PR #2540 prepare-merge): PR #2540 independently formalized the same additivity (QOU.HadronicMass.BSymChainAdditive) in parallel; on rebase it was found to DUPLICATE the canonical QOU.BraidKnot.BsymLinearChain already merged to main. The duplicate module + its HadronicMass import were DROPPED; the audit cross-link in 2026-06-16-b-sym-linear-chain-closed-form.md now points to BsymLinearChain. The one complementary piece #2540 had (the ℝ Real.log-of-product lemma that DISCHARGES the per-bond factorization from the multiplicative trace ratio) is noted as an optional follow-up next to BsymLinearChain — not shipped, to avoid editing the just-merged module.
