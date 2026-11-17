---
# qou-zlra
title: Is graded binding +c_k or -c_k? The sign convention the type-two result hangs on
status: in-progress
pr: 8278
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T12:02:10Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
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

---

## 2026-09-12 — the last leg: the UIC per-block log, measured (PR #7230)

PR #7223 answered the headline question — the `+c_k / -c_k` sign is EMPTY for
every product-additive functional, so the live binding law `E0*log(tr_free/tr_atom)`
cannot carry the pair term whatever sign it takes. It left one item: the third
possibility this bean's own checklist named, `B_lambda = m_e H_q(lambda) u_lambda
(ln|tr M_lambda| - ln d_lambda)` -- a LOG, and a log of a SINGLE Wedderburn block,
which is not multiplicative over the word even when the total is. The production
call exceeded 300 s per atom and the scan was recorded as unmeasured.

Measured now: A = 3..8, every Z, k_exact = 4..9 (36 cells), proton pin,
convention D, mp.dps = 70, mpmath end to end, reading the gated and ungated
totals as `mpf` from the per-step rows so the producer's float64 boundary cast
is never taken.

### The answer, both halves

**(1) The per-block log IS outside the additive class.** Third difference in Z
nonzero in every cell -- GATED AND UNGATED alike, which is the decisive
decomposition: the non-additivity is the functional, not the Pass-2 selector.

The discriminator is the THIRD difference and not the second, because
`_step_chain_generic` (hecke_core_legacy.py:1622-1630) crosses each nucleon with
every PREVIOUS one, so the UIC word is the ALL-PAIRS layout, on which
`n_pn = Z(A-Z)` makes even a census-affine functional exactly quadratic in Z.
Proved sorry-free: `census_secondDiff`, `census_thirdDiff`.

Mechanism, exact and proved: a two-branch block trace has non-multiplicativity
defect `T2(d1,d2) - T(d1)T(d2) = wP*wM*(x-y)^2`, which under convention D's
normalisation is exactly `wP(q) = 0.75270211325196540159`, INDEPENDENT OF BOTH
BOND OFFSETS (verified to 2.1e-70 over 25 offset pairs including two arbitrary
rationals). For n crossings, `log|tr_n|` factorises through ONE multiplicative
statistic -- a nonlinear function of an additive quantity, which is exactly how
a per-block log leaves the additive class.

**(2) It still gives no valley.** argmax_Z does NOT track N = Z -- it coincides
with N=Z in only 3 of the 36 cells and never at more than one truncation order
per A (it is NOT true that it never lands there; that weaker claim is the
correct one), it sits at an ENDPOINT in 15 of 36, and it has not converged in
k_exact. Before any of that the functional gets the SIGN of the binding wrong
(negative for every atom, reproducing 2026-09-05-uic-sign-forced-by-gate) and
the A-scaling wrong (|B| falls 4.81 -> 3.71 MeV across 2H..4He while AME rises
2.22 -> 28.30, a factor 12.7). And the one FORCED fact
points the wrong way: the all-pairs symmetry curvature
`L_pp + L_nn - 2 L_pn = +0.04351846501566097275` is POSITIVE, so the additive
part makes the symmetric nucleus the LEAST bound -- an anti-valley. That sign
holds for every q > 1 (`symmetryCurvature_pos`, sorry-free), not just at q0,
because convention D's pn letter is the pp/nn average shifted upward
(`ChainTraceFactor.deltaPN_nonneg`).

### A finding this bean did not ask for: the block and the producer disagree

`unified-iterative-correction.md` and `hecke_core_legacy.py` describe DIFFERENT
functionals, in three ways: the block's `u_lambda` is named an LP shadow price
which the producer's own `lp_shadow_price` docstring disclaims ("solves no
program"); the producer carries an extra q-Laplacian resolvent `rho_lambda(hbar_q)`
the block never mentions; and the block says "sums these strictly over all
lambda" while the producer sums only the Pass-2 gated subset (the producer's own
note measures 3.4-4.6x between them). Reported, not resolved -- picking one
would be choosing a functional.

### Status

The bean's three checklist items are all discharged: the combination rule was
read (it is a log, per-block, gated, with a resolvent); the sign question is
empty for the additive class (#7223) and, for this non-additive one, is not a
convention at all but a computed quantity whose forced component has the
anti-valley sign. Nothing is wired; nothing is fitted; AME enters nowhere.


## 2026-09-12 — the Pass-2 sign gate's LP justification has no referent (qou-8urh, PR #7251)

Relevant to this bean because the sign convention it tracks sits downstream of a
gate whose *stated* derivation turns out not to hold.

The owner ruled 2026-09-12 to drop the Pass-2 gate in
`hecke_core_legacy.unified_iterative_correction` AND to hunt the primal LP its
comment invokes. The hunt closed as **case (b)**: the LP exists
(`prop:operator-selection-lp`, Lean `QOU.ParticleInteractions.operator_selection_lp`,
sorry-free) and complementary slackness on it does **not** give the sign gate.

Four independent mismatches, all in
`QOU.MassTheory.UICGateNotFromComplementarySlackness` (8 decls, lean-direct
exit 0, sorry-free):

1. the LP's constraints are indexed by NF basis elements (`d = n!`), the gate by
   partitions (`p(n)`); no partition-indexed LP exists in the corpus;
2. CS constrains `(Gx*)_i`, a function of the operator being SELECTED, while the
   gate reads `t_lambda = tr(M_lambda(W_atom))`, an input;
3. `IsFeasible` demands `0 <= (Gx)_i`, so a "<= 0" gate on a constraint value IS
   the tightness gate `= 0` (`frobeniusValue_nonpos_iff_eq_zero`);
4. the optimum is a positive-dimensional face, so "the OPTIMAL primal-dual pair"
   is not a well-defined object.

**Sign-relevant detail for this bean.** The gate is a predicate on the SIGN of
the per-block final trace, and that sign is exactly what CS cannot speak to:
under a diagonal Wedderburn Gram (orthogonal projectors) CS decouples to
`s_l * G_ll * x_l = 0`, in which the atom's traces do not appear at all
(`complementarySlackness_diagonal_iff`). So whatever fixes the +c_k / -c_k
convention, it is not LP duality on this program.

Measured (`computations/probes/uic_gate_vs_lp_complementary_slackness_probe.py`,
mp.dps = 70, proton pin, convention D): the gate keeps 4 of 10 blocks at 2H
(the only non-zero one is `(2,1,1)`) and 2 of 10 at 4He (`(2,2)`, `(3,1)`),
while the LP's active set is 9 of 10 at every reachable target for both atoms.

Audit: `docs/audits/2026-09-12-uic-gate-primal-lp-hunt.md`. Stays OPEN — the
sign convention is untouched by this.

## Cross-reference: the UIC resolvent cone is now mpf (2026-09-12, bean `qou-oiz3`, PR #7245)

Owner directive "excise float64" of the same day. Every quantity this bean's
sign question runs through — `C_lambda_resolvent_MeV`, `mu_lambda`, `s_*`,
`rho_lambda`, and the per-atom gated/ungated totals — has moved, at the
~1e-16 relative level. If this bean quotes a `C_lambda` or a gated total to
more than ~15 significant digits, re-read it from the refreshed witness rather
than from the recorded figure.

**What did NOT change:** no sign flips. The gated/ungated totals keep their
signs and their tight-partition counts at every atom measured
(k_exact = 4 and 6, A = 1..8), so nothing in this bean's argument is affected
in direction — only in the last digits.

**What is worth carrying over:** the residual. `C_lambda = m_e * H_q * y_lambda
* rho_lambda` is still float64-limited through THREE of its four factors,
because `q_hook_product` / `q_factorial` / `wedderburn_weight` accumulate
`mp.mpf(1) * q_int(k)` over the float64 `q_int` — mpf-typed, float64-valued.
Measured: 1.0212424e-15 at lambda = (2,2), against the 2.4946976e-16 that PR
removed. So a sign-convention argument that turns on a difference smaller than
~1e-15 in `C_lambda` is not yet decidable by this code.


## 2026-09-12 — the block/producer mismatch this bean REPORTED is now RESOLVED (PR #7237, bean `qou-t6be`)

PR #7230 measured three divergences between `prop:unified-iterative-correction`
and `hecke_core_legacy.unified_iterative_correction` and deliberately did not
resolve them, because picking one would be choosing a functional. The owner then
ruled, verbatim: **"resolve functionals ... what lean provable"**.

**The criterion settles it, and the discriminator is sharper than "pick one".**
The block's displayed summand reads the trace only through `ln|tr|`, so it is
EVEN in the trace; the producer's gate reads `sign(tr)`. Proved sorry-free
(`QOU.MassTheory.UICFunctionalSelection.gate_not_a_function_of_displayed_data`)
and measured: flipping every trace's sign leaves the ungated total BIT-IDENTICAL
and moves the gated one `-0.0895596831 -> -0.3226525092` (2H). So the block's
formula could not DENOTE the producer's functional at all — the mismatch was
structural, not editorial, and something had to move whatever the physics.

**All three divergences resolved against the content side; the producer is
untouched and no number moves.** A FOURTH was found by `qa-sweep
proof-statement-integrity` firing on the fix: the block's own `.lean` sibling
`stepDelta` carries `m_e * H_q * w_lambda`, a third scale matching neither of
the producer's two.

**One correction to this bean's own report.** #7230's table ranks the omitted
q-Laplacian resolvent as the lesser divergence (*"a per-partition factor spanning
~100x"*) and the summation range as *"the serious one"*. Measured on the TOTALS
rather than on the factor's range, that ordering is backwards: deleting `rho`
moves the gated total **4.1208754x** (A=2) and **9.8660639x** (A=4), against the
gate's own 4.6026535x / 3.4030381x. At A=4 the omission is ~2.9x the gate's
effect.

**What stays open:** whether the gate belongs in the physics. The criterion shows
it is underived and its stated justification false; it does NOT show it is wrong.
`qou-sv7h` / `qou-brng`.

Audit: `docs/audits/2026-09-12-uic-functional-resolution.md`.
Probe: `computations/probes/uic_functional_resolution_probe.py` (16/16).

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress Update (PR #8278 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/IsospinChannelReachabilityAndB3ChainSign.lean`, `QOU/MassTheory/PeeledMarkovDefectAndHigherInterleaving.lean`, `QOU/MassTheory/GradedLogPairCancellationAndH3TowerCollapse.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/isospin_b3chain_markov_defect_logjet_h3tower_probe.py` and 2-commit stamped witness `computations/probes/isospin-b3chain-markov-defect-logjet-h3tower-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8278](https://github.com/litlfred/qou/pull/8278) (`ready: b3288da132ea8d0d185d184a5e18432c89e4858e`).
