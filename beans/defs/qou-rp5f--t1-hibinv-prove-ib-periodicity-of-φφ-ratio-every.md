---
# qou-rp5f
title: 'T1: hibinv — prove i/b-periodicity of Φ₁/Φ₂ ratio everywhere (identity theorem off dual pole lattice)'
status: todo
type: task
created_at: 2026-07-27T14:57:31Z
updated_at: 2026-07-27T14:57:31Z
---


## 2026-08-08 — REDUCED TO qou-cons. This is no longer an independent input.

`QOU/Mathlib/FaddeevRatioPeriodic.lean`, sorry-free, standard axioms:

    ratio_shift_b / ratio_shift_binv        the ratio is shift-invariant wherever
                                            the shared prefactor is nonzero
    ratio_periodic_b / ratio_periodic_binv  period form (ib and i/b)
    dense_compl_zeros                       an entire g nonzero somewhere has a
                                            zero set with dense complement
    periodic_b_of_continuous                given a CONTINUOUS ratio, ib-periodicity
    periodic_binv_of_continuous             ... and i/b-periodicity, EVERYWHERE

WHY IT IS ALGEBRA. Both `FaddeevPhi` shift axioms carry the SAME prefactor
`1 + e^{2 pi b z}` (resp. `1 + e^{2 pi z/b}`), so it cancels from the ratio. One
`mul_div_mul_left`. Nothing about the zeros of Phi is needed: where Phi vanishes
both sides are 0 and the lemma still applies.

WHY THE GUARD LIFTS. The prefactor zero sets are zero sets of entire functions
that take the value 2 somewhere, so by the identity theorem they have empty
interior, hence dense complement. A continuous function is determined on a dense
set. So `hibinv` follows from `hratio` — the title's own mechanism ("identity
theorem off dual pole lattice") supplied.

STATUS: this bean is now a COROLLARY of qou-cons, not a peer of it. Put effort
there. Left as todo rather than completed only because the final `hper` in the
exact `Basis (Fin 2)` shape that `ratio_const_of_entire_ratio` consumes still
needs the two periods packaged as a basis — bookkeeping, not analysis.
