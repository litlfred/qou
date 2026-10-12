---
# qou-gzsp
title: '#7673 assembly: Jimbo side as a continuous family + the KZ≅Jimbo comparison theorem with gaps as explicit hypotheses'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:31:38Z
updated_at: 2026-10-12T19:12:31Z
parent: qou-xhci
---

2026-10-12 (assembly prover, PR #7744, commit e53d0f71cd): QOU/Mass/KohnoAssembly.lean, sorry-free, axioms propext/Classical.choice/Quot.sound. PROVED: strandBraid_eq_eval (Jimbo generator = evaluation of one Laurent-polynomial matrix over R[T,T^-1]); continuous_strandBraid_exp; jimboRep (Hecke-universal-property Jimbo map, agrees with JimboActionKernel.jimbo on generators); permRep + permRep_adjSwap (Jimbo at q=1 = permutation matrix exactly, = KZ at coupling 0, no scalar); conj_of_isPreconnected_hecke (from #7738 comment 6130311989, verbatim); kz_conj_jimbo (conditional on KZQuad); kzQuad_holds (discharged by #7673 LocalMonodromy.kzBraidRep_sigma_isHeckeQuad); kz_conj_jimbo_hecke / kz_conj_jimbo_sigma' UNCONDITIONAL for all m, c in C, t >= 0 along kappa = t/(2 pi i), q = e^t; kz_conj_jimbo_pin at any real q0 >= 1, kappa0 = ln q0/(2 pi i) (kappa_eq, qOf_mem). Normalisation: Lean has q = e^{2 pi i kappa} (audit §5 text says e^{i pi lambda}); only mismatch is the per-crossing scalar e^{2 pi i kappa c}. VERIFIED: lean -DautoImplicit=false -s 65536 exit 0 after a dirty-closure rebuild of the 134-module cone (121 rebuilt, 0 red) into a private shadow. OPEN: t<0 / complex q off the real ray not stated; U is existential (rank comparison), no explicit intertwiner; V=C^2 only. Kept in-progress: the general Drinfeld-Kohno statement is not this bean's closure.

2026-10-12 later: extended to every real q > 0 (kz_conj_jimbo_real, kz_conj_jimbo_pos; rigidity on [t,0] for t<0), sorry-free, axioms clean. Audit doc §5.1/§5.2 updated with the result and the convention q = e^{2 pi i kappa} (lambda = 2 kappa). Still open: complex q off the positive real axis; explicit U; V != C^2; Lean statement jimboRep = JimboActionKernel.jimbo.
