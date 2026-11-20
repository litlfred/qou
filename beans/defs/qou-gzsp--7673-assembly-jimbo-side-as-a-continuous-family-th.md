---
# qou-gzsp
title: '#7673 assembly: Jimbo side as a continuous family + the KZ≅Jimbo comparison theorem with gaps as explicit hypotheses'
status: todo
type: task
priority: normal
created_at: 2026-10-12T18:31:38Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-59vq
---

2026-10-12 (assembly prover, PR #7744, commit e53d0f71cd): QOU/Mass/KohnoAssembly.lean, sorry-free, axioms propext/Classical.choice/Quot.sound. PROVED: strandBraid_eq_eval (Jimbo generator = evaluation of one Laurent-polynomial matrix over R[T,T^-1]); continuous_strandBraid_exp; jimboRep (Hecke-universal-property Jimbo map, agrees with JimboActionKernel.jimbo on generators); permRep + permRep_adjSwap (Jimbo at q=1 = permutation matrix exactly, = KZ at coupling 0, no scalar); conj_of_isPreconnected_hecke (from #7738 comment 6130311989, verbatim); kz_conj_jimbo (conditional on KZQuad); kzQuad_holds (discharged by #7673 LocalMonodromy.kzBraidRep_sigma_isHeckeQuad); kz_conj_jimbo_hecke / kz_conj_jimbo_sigma' UNCONDITIONAL for all m, c in C, t >= 0 along kappa = t/(2 pi i), q = e^t; kz_conj_jimbo_pin at any real q0 >= 1, kappa0 = ln q0/(2 pi i) (kappa_eq, qOf_mem). Normalisation: Lean has q = e^{2 pi i kappa} (audit §5 text says e^{i pi lambda}); only mismatch is the per-crossing scalar e^{2 pi i kappa c}. VERIFIED: lean -DautoImplicit=false -s 65536 exit 0 after a dirty-closure rebuild of the 134-module cone (121 rebuilt, 0 red) into a private shadow. OPEN: t<0 / complex q off the real ray not stated; U is existential (rank comparison), no explicit intertwiner; V=C^2 only. Kept in-progress: the general Drinfeld-Kohno statement is not this bean's closure.

2026-10-12 later: extended to every real q > 0 (kz_conj_jimbo_real, kz_conj_jimbo_pos; rigidity on [t,0] for t<0), sorry-free, axioms clean. Audit doc §5.1/§5.2 updated with the result and the convention q = e^{2 pi i kappa} (lambda = 2 kappa). Still open: complex q off the positive real axis; explicit U; V != C^2; Lean statement jimboRep = JimboActionKernel.jimbo.

2026-10-12 (third pass): kz_conj_jimbo_complex / _complex_sigma: every complex kappa with q = e^{2 pi i kappa} not a root of unity (root-of-unity couplings countable, complement path-connected and dense; rigidity set = {q^2-integers separate}, contains kappa=0). jimboRep_eq_jimbo proved after rebuilding JimboActionKernel's stale cone (59 modules, 0 red). Remaining open: roots of unity q != 1 (non-semisimple); explicit U; V != C^2 / general Drinfeld-Kohno.

2026-10-12 (fourth pass, PR #7744): QOU/Mass/KohnoWeighted.lean, sorry-free. Weight-space rigidity: commute_kzBraidRep (KZ equivariance via ODE uniqueness), both families preserve each total-weight space V_k, trace_res_kz_eq_jimbo, weighted_trace_kz_eq_jimbo (any D scalar on each V_k), siteWeight_trace_kz_eq_jimbo, braidTrace_eq_kz (PR #7632's Markov trace = wi^{m+1} Tr(K^{tensor} KZ(x_beta))), all at q not a root of unity. Not done: the assembled block-diagonal U on all of V^{tensor n} (only its trace consequence).

**2026-10-12 — single intertwiner assembled (sorry-free).** `QOU/Mass/KohnoIntertwiner.lean`: `kz_jimbo_intertwiner` gives ONE unit U, weight-preserving (commutes with every `wproj`), with U·kzHeckeC(h) = jimboRep(h)·U for all h, every complex κ with q(κ) not a root of unity; `braidTrace_eq_kz_of_intertwiner` recovers the KZ-side mass identity by conjugation. PR #7767, bean qou-dgsw.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `qou-xhci` → `qou-59vq`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

- Round 74 (`lane-e667`): Formalized `qou-gd90`, `qou-gzsp`, `qou-h56b`, `qou-hah4`, `qou-luq7` in `QOU.Foundations.PeriodicStateTriangularInversionWeightSpaceEquivarianceBlockScalingWeightedDecomposition` with 80-dps `mpmath` 2-commit witness stamp (`90a852e5501c98f68c32c2d227ae5dc2719d5bb6` -> `ae44845094878bbd65a4bf4b8065339b39d10e57`, `scriptHash=0a79a20314ed167467fce31136d40aeaf330204cb85b728199138a30d69455e2`) in PR `litlfred/qou#8399` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8399, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
