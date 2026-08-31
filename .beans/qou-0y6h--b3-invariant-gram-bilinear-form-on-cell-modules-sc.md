---
# qou-0y6h
title: 'B3: invariant Gram bilinear form on cell modules; Schur element = hook/content product (reuse WenzlSchurElement.schurElement); det(Gram)=∏ Schur (Geck-Pfeiffer)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-08-31T07:35:56Z
---

## 2026-08-29 — this is closer than the standing plan implies (from qou-0ubf)

The Schur-element NON-VANISHING half is **already proved for all n**:
`WenzlSchurElement.schurElement_ne_zero` (line 231) is sorry-free, hypotheses
`1 < Q` and `X <= 0` only, no class hypothesis. And `semisimple_of_substrate`
already composes it into all-rank semisimplicity — but conditionally, on
`[SchurElementCriterion Q X ss]`, which has NO INSTANCE (verified by grep over
content/**/lean/QOU on main @ df81b22be4).

So this bean's remaining content is **exactly** Geck-Pfeiffer Thm 7.2.6 — 'every
Schur element nonzero => semisimple'. Formalising it turns `semisimple_of_substrate`
from class-conditional into an outright theorem at every rank, which discharges the
`WenzlCriterion` hypothesis of PNeqNpEquivalence for real.

Note the 2026-07-25 status audit §5 item 1 sends you to build the T_w/Matsumoto
basis + the symmetrizing-trace Gram determinant instead. That route is still the
honest Mathlib gap for the DETERMINANT approach and is worth doing on its own
merits, but it is NOT on the critical path to all-n semisimplicity. Corrected in
place in that audit; full re-measurement in
docs/audits/2026-08-29-pneqnp-gap-inventory-refresh.md.

Crosses no barrier — semisimplicity is a magnitude-axis fact. It removes one of the
two remaining cited classes from the conditional chain.

## 2026-08-29 (later) — CORRECTION: this is DOWNSTREAM of the T_w basis, not an alternative to it

My own note above, and the audit §3 ranking it came from, presented this bean and
the T_w/Matsumoto basis as **alternatives** — `0y6h` ranked #1 'chippable', the
T_w basis ranked #5 'no longer P!=NP critical path'. **That is wrong.**

Measured: `WenzlSchurElement.schurElement` is **purely combinatorial** — a
hook/content product over ℝ. A grep of the whole file for
`IwahoriHecke|HeckeAlgebra|Algebra|Module|Basis` returns **nothing**. No algebra
is attached to it anywhere.

So `SchurElementCriterion` silently bundles TWO obligations:
  (i) the combinatorial formula *equals* the algebra-theoretic Schur element, and
  (ii) Geck-Pfeiffer 7.2.6 proper (all Schur ≠ 0 => semisimple).
Both need the algebra side: a **basis** of H_n(q) to state det(Gram) against, plus
the symmetrizing-trace/Wedderburn theory. For H_n(q) that basis is T_w.

The downstream half of the chain already exists and is fine —
`RegTraceGram.isSemisimpleRing_of_regTraceGram_det_ne_zero` and the
`TraceFormSemisimple` keystone give det(Gram) ≠ 0 => semisimple. What is missing
is precisely 'Schur ≠ 0 => det(Gram) ≠ 0', i.e. det(Gram) = ∏ Schur, and that
cannot even be *stated* without the basis.

**What remains true:** `semisimple_of_substrate` does give all-n semisimplicity
without the T_w basis — but only CONDITIONALLY, on the unproved criterion. The
distinction I blurred is between an all-n *conditional* statement (no T_w needed,
true) and an all-n *discharge* (T_w needed, which is this bean).

**Verdict: not chippable in isolation. Genuine Mathlib-scale, gated on T_w
(qou-lrz1 / qou-twwf).** Do those first or accept the conditional.


## 2026-08-30 — measured: stated at every rank, computed at rank one (PR #6134)

Six commits on `claude/p-neq-np-gaps-n8dxxl`. What is now unconditional
(`#print axioms` = propext / Classical.choice / Quot.sound on every
declaration, and on both downstream keystones it composes with):

* `TwGram.twGram` + `isSemisimpleRing_of_twGram_det_ne_zero` — det != 0 =>
  semisimple, at EVERY rank. This is the statement §3b recorded as 'cannot
  even be stated without the basis'.
* `TwMul.sigma_mul_Tw` — the full generator multiplication table, both
  branches. Index handedness is `T_v . T_w = T_{wv}` (right factor acts
  first); documented, not hidden.
* `TwTrace.trace_lmul_sigma` — tr(L_{sigma_i}) = (q-1) * #descents, and
  `two_mul_trace_lmul_sigma` — 2*tr = (q-1)*(n+1)!, doubled so it holds in
  any characteristic.
* `TwGramRankOne.twGram_det_rank_one` — det(twGram K q 1) = (1+q)^2, hence
  `IsSemisimpleRing (IwahoriHecke K q 1)` for 1+q != 0. First end-to-end
  discharge on `IwahoriHecke` ITSELF rather than on a power-basis model.

Cross-check that matters: H2TraceForm.h2_regTraceGram_det independently gives
[2]_q^2 for AdjoinRoot(X^2-(q-1)X-q). Same value, different object, different
route — so the TwRep -> TwIndependent -> TwBasisField -> TwGram -> TwTrace
stack agrees with a computation that predates it.

### What is still open, precisely

det(twGram) at rank >= 2. The generator case does NOT imply it: tr(L_{T_u})
for general u needs the diagonal structure constant [T_u T_w : T_w], and that
has no closed form in the corpus. At q=1 it is delta_{u,1}(n+1)!; at generic q
the u = s_i case is (q-1)*(n+1)!/2, so it is not concentrated at u=1.

### Route rejected on measurement, not taste

The tau-form / symmetrizing-trace route to GP 7.2.6 was scoped first, per the
owner instruction, and rejected: docs/audits/2026-08-30-gp726-tau-route-scoping.md.
Every piece of GP 7.2.6's vocabulary is absent from Mathlib;
Mathlib/LinearAlgebra/SymmetricAlgebra/ is Sym(V), a name collision rather
than Frobenius theory; RepresentationTheory/Character.lean is finite GROUP
characters; isSemisimpleRing_iff_pi_matrix_divisionRing is a Mathlib
proof_wanted.

Note for whoever picks up the tau route anyway: tau(x) := <x>_1 satisfies
tau(sigma_i . T_u) = q * <T_u>_{s_i} in BOTH branches of sigma_mul_Tw (the
ascent branch cannot land on T_1, the descent branch cannot start at u=1).
That is clean but it does NOT close by induction on length — it moves the
coefficient from index 1 to index s_i, so the induction needs the full
structure constants, not just the tau-column. The mirror computation on the
right, tau(z . sigma_i) = q * <z>_{s_i}, has the same shape and the same
obstruction. Measured this session before choosing the determinant route.

### Not claimed

SchurElementCriterion still has NO instance. Both obligations §3b separates —
that the combinatorial schurElement equals the algebra-theoretic one, and GP
7.2.6 proper — are untouched. Nothing here bears on the P!=NP wall;
semisimplicity is a magnitude-axis fact.


## 2026-08-30/31 — det(twGram) MEASURED at ranks 1-3, and the route is bounded

Probe: computations/hecke/tw_gram_determinant_probe.py.
Audit: docs/audits/2026-08-30-tw-gram-determinant-measured.md. PR #6165.

  n=1  det = [2]_q^2
  n=2  det = - 2^4 . q^2 . [2]_q^2 . [3]_q^6
  n=3  det = - 2^4.3^18 . q^22 . [2]_q^28 . [3]_q^6 . [4]_q^20

The integer constant is exactly prod_lambda d_lambda^(d_lambda^2) over the
partitions of n+1: 1 / 16 / 6198727824 for S_2 / S_3 / S_4.

Firmness, strongest first. n=1 reproduces twGram_det_rank_one, proved sorry-free
in Lean, so the arithmetic is validated against a result the probe did not
produce. n=2 is symbolic over Q(q) with NO fitting -- the 16 falls out of the
determinant directly, which is what makes the identification of the constant a
prediction rather than a curve fit. n=3 is a POLYNOMIAL IDENTITY, not a sample:
row-degree bound 216, candidate degree 122, agreement at 298 integer points.

### The finding is a NEGATIVE and it bounds this whole bean

The constant is > 1 for n >= 2, so in a characteristic dividing it det = 0 EVEN
WHERE H_n(q) IS SEMISIMPLE -- the regular trace form of M_d(K) is degenerate
exactly when char K | d, and the constant is the product of those obstructions
across the Wedderburn blocks. So

    det(twGram) != 0  ==>  H_n(q) semisimple

is all this route can ever give. The CONVERSE IS FALSE. Explicit counterexample:
char 2, q of multiplicative order > 3, n = 2 -- q, [2]_q and [3]_q are all
nonzero while 2^4 = 0, and Dipper-James still gives semisimplicity there.

Consequences:
* Any general Lean theorem along this route MUST carry a characteristic
  hypothesis. QGeneric q n (q^k != 1) does not supply one and is an incorrect
  hypothesis set on its own.
* Do not attempt the converse (semisimple => det != 0) as a clean criterion --
  it is false, counterexample above.
* Costs nothing for the substrate case K = R, q > 1, which is the shape
  isSemisimpleRing_rank_one_of_pos is already in.

Scope-(b) structural exclusion with the invariant cited, per AGENTS.md.

### Shape confirms this bean's target, with the derivation labelled as a reading

'det(Gram) = prod Schur' is the right target. The structural reading -- NOT
proved -- is that the regular trace is the symmetrizing trace twisted by the
central element z = sum_lambda d_lambda s_lambda e_lambda, giving
det(regGram) = det(tauGram) . det(L_z) = +- q^(sum_w l(w)) . prod (d s)^(d^2).
That reading predicts the integer constant and the prediction holds. It does NOT
predict the q-exponents as written (sum_w l(w) is 9 and 72 against the measured
2 and 22, because the s_lambda carry q-powers), and the factorisation into
[k]_q is not canonical since [4]_q = [2]_q(1+q^2). Read the table as a value,
not as a normal form.

### Still open

det(twGram) in LEAN at rank >= 2. Knowing the value does not supply the proof:
the general diagonal structure constant [T_u T_w : T_w] still has no closed form
in the corpus, and the proved generator case does not imply it -- at q=1 the
trace is delta_{u,1}(n+1)!, at generic q the u = s_i case is (q-1)(n+1)!/2, so
it is not concentrated at u=1.
