---
# qou-zlra
title: Is graded binding +c_k or -c_k? The sign convention the type-two result hangs on
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T12:02:10Z
updated_at: 2026-09-12T12:33:09Z
---


Opened 2026-09-04 from `qou-oooq`. Small, cheap, and everything in the type-two
result hangs on it.

## The problem

`the_asymmetry_term_lives_at_vassiliev_type_two_probe` reads binding as
`-alpha c_2/c_0`. With that sign the asymmetry PENALISES `|N-Z|` and the
volume-like term is positive — both correct.

With the opposite sign every conclusion inverts: symmetric nuclei become the
LEAST bound and the volume term becomes negative.

**And the opposite sign is the more natural reading of the corpus.**
`vassiliev-filtration-mass-tower` writes the trace as
`tr_M = c_0 + c_1 h + c_2 h^2 + ...` and calls the higher terms "precision
refinements" that are ADDED. A mass formula built from `tr_M` would then carry
`+c_2 h^2`, not `-c_2 h^2`. The probe's `-` was chosen because it makes the
physics come out right, which is exactly the kind of choice this corpus's
discipline is meant to catch.

Note also that `c_2/c_0` is MINIMISED at `N = Z` (it is `(N-Z)^2/2` plus a
constant), so the sign is not a cosmetic convention — it decides whether the
symmetric nucleus is the most or the least bound.

- [x] Read how `unified-iterative-correction` and the six-term mass formula
      actually combine trace coefficients into an energy: is there a `-log`, a
      shadow price `u_lambda`, or a bare sum? `B_lambda = m_e H_q(lambda)
      u_lambda (ln|tr M| - ln d_lambda)` suggests a LOG of the trace, which is a
      third possibility and would change the graded analysis again.
- [x] Settle the sign, then re-state the type-two result with it — or retract
      the sign-dependent half.
- [x] If the natural sign is `+`, say so plainly: the type-two term would then
      make symmetric nuclei least bound, which is a falsification rather than a
      caveat.


## ANSWERED 2026-09-12 (PR #7223) — the question is EMPTY for the corpus's functional

Audit: `docs/audits/2026-09-12-graded-binding-sign-convention.md`.
Lean: `QOU/Mass/GradedBindingFunctionalPairTerm.lean` (sorry-free, generic ring).
Probe: `computations/probes/graded_binding_sign_convention_probe.py` (21/21).

**What the corpus fixes.** Every binding law the corpus carries is a LOGARITHM of
a trace: the live law `B = E_0 log(tr_free/tr_atom)` (owner ruling 2026-09-04
Option B + 2026-09-05 `E_0`; `binding_log_free_energy.py`;
`rem:markov-trace-gibbs-free-energy`; Lean `bindingOfTrace` "the production
shape", `ChainTraceFactor.L_*`, `BondCutSymmetry` `e = -ln b`), and
`unified-iterative-correction`'s `Sum_lambda m_e H_q y_lambda ln|tr M_lambda|`.
The one BARE binding law, `Q_beta (tr_free - tr_atom)`, was refuted 2026-09-05.
The bare `|tr_M|` readings that survive (`prop:per-braid-mass-tower`,
`thm:six-term-mass-formula-complete`) are MASS functionals.

**The theorem.** For a product of unital jets, `[h^2] prod = sum c_i + e2(b)` —
the pair convolution, present for `+` and for `-` (`prod_c2`, `neg_prod_c2`) —
while ANY product-additive `F` (log, -log, alpha log) has
`F(prod) = sum F(f_i)`, linear in the counts (`additive_census`); the formal
log's `[h^2]` is `sum (c_i - b_i^2/2)`, the pair term removed by
`(sum b)^2 = sum b^2 + 2 e2` (`logJet_c2_prod`, `sq_sum_eq`). Sign and scale
never enter (`neg_additive`, `smul_additive`).

**Measured on the corpus's letters (convention D, proton pin, exact Fraction
h-series):** second difference in Z of `[h^2] prod` is 4 at every A = 3..12
(the `(N-Z)^2/2`); of `[h^2] (+log)` and `[h^2] (-log)` it is 0 everywhere.
`c_2/c_0 = (N-Z)^2/2 + (5-A)/8` reproduced exactly.

**Valley scan at q_0 (argmax_Z, A = 3..12):** live log-ratio law: endpoint
(Z = 1) at every A, no valley. `-c_2/c_0` alone: interior maximum at N = Z for
A = 4..12 (the qou-oooq valley); `+c_2/c_0` alone: endpoint — the sign turns the
valley into a hill; resummed bare product either sign: monotone. So the valley
of the type-two result belongs to a functional the corpus does not read binding
with, under a sign nothing derives.

**So the answer to this bean's third item is:** neither `+` nor `-` is "the
natural sign", because the framework does not read binding as a bare
coefficient at all. Under the log the symmetric nucleus is neither most nor
least bound at type two — the term is absent. Retract the sign-dependent half
of the type-two result as a statement about the framework; keep it as a
statement about the product.

**Scope (b):** invariant = `additive_census` / `logJet_c2_census` +
`L_chain_eq_sum_of_intra` (chain trace is a scalar product, measured 1e-59,
connected-sum multiplicativity classical and not formalised).

**What is NOT closed, and is the one live thread:** the corpus carries TWO
inequivalent log readings — log of the Markov-weighted total (additive over
bonds) vs UIC's weighted sum of per-BLOCK logs. A single Wedderburn block
`tr_lambda(prod (c sigma + d))` is NOT multiplicative even on the chain: its
`[h^2] log` has nonzero, non-constant second differences in Z for
lambda = (3,1), (3,2), (4,1) (rational Hoefsmit form, relations checked exactly,
characters cross-checked against `hecke_core_legacy` at q_0 to < 1e-50). Its
type-two sign is computed, mixed across Z. Whether the PRODUCTION accumulator
`unified_iterative_correction(Z, N)` has an interior maximum in Z at fixed A is
unmeasured — it exceeded 300 s at (2,2) here and was killed. That is the next
measurement; nothing changes if it stays unmeasured, since the live law is the
total-trace log and no dashboard row reads the UIC for a valley.

Also settled here, for `qou-eqwg`'s open item: there is NO non-commutativity
inside a generator (the transfer matrices `[[ch+d, c],[c, d]]` commute exactly —
regular representation of a commutative algebra); what is non-multiplicative
inside a generator is the two-branch state sum when two INTERFACE letters share
a generator, which the chain never does.

Remaining open item of this bean: the production-UIC valley scan. Left open
under rule 13a (the subject — which log functional the framework means — is
an unresolved collision, not a mechanical task).
- [ ] Scan `hecke_core_legacy.unified_iterative_correction(Z, N)` over
      A = 3..8 across Z with a real budget (> 300 s per atom at A = 4 here) and
      report argmax_Z per A; compare against the UIC-shaped single-block rows
      of the probe.
