---
# qou-0y6h
title: 'B3: invariant Gram bilinear form on cell modules; Schur element = hook/content product (reuse WenzlSchurElement.schurElement); det(Gram)=∏ Schur (Geck-Pfeiffer)'
status: completed
type: task
priority: normal
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-09-02T21:39:56Z
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
* `TwMul.σ_mul_Tw` — the full generator multiplication table, both
  branches. Index handedness is `T_v . T_w = T_{wv}` (right factor acts
  first); documented, not hidden.
* `TwTrace.trace_lmul_σ` — tr(L_{sigma_i}) = (q-1) * #descents, and
  `two_mul_trace_lmul_σ` — 2*tr = (q-1)*(n+1)!, doubled so it holds in
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
tau(sigma_i . T_u) = q * <T_u>_{s_i} in BOTH branches of σ_mul_Tw (the
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


## 2026-09-02 — the blocker is NOT combinatorial; price the rest as Mathlib-scale

Probe: computations/hecke/tw_regular_trace_statistics_probe.py
Audit: docs/audits/2026-09-02-tw-regular-trace-not-combinatorial.md

The single thing blocking det(twGram) at rank >= 2 is [T_u T_w : T_w] for
general u, i.e. tr(L_{T_u}). Measured exactly, it is determined by NONE of the
three obvious statistics:

  length(u) alone      -- NO, fails from S_4 on
  cycleType(u) alone   -- NO, fails from S_3 on
  (length, cycleType)  -- NO: holds in S_4, FAILS in S_5

Witness, same length 4 and same cycle type (2,2,1) in S_5:
  u = (0,3,4,1,2)  tr =  5 (q-1)^2 (q^2 + 4q + 1)
  u = (1,0,4,3,2)  tr = 10 (q-1)^2 (q^2 +  q + 1)
Not proportional; not even the same irreducible factors. Exact finite
computation => a refutation with a witness, not a numerical near-miss.

TRAP, recorded because I walked into it twice in one session. S_2 satisfies all
three, S_3 two, S_4 the joint one, S_5 none. From S_3 I concluded 'depends only
on length'; from S_4 I concluded 'depends on (length, cycle type)'. Both were
consistent with every datum I had at the time and both are false. In this corpus
a Hecke pattern first breaks at n = 4 or n = 5 — that is where S_n first has two
elements of equal length in one class. DO NOT promote a rank-3 or rank-4 pattern
here without testing S_5. The probe asserts both halves of the split so a future
edit that breaks either fails loudly.

NOT established: that no closed form exists. tr(L_{T_u}) = sum_lambda d_lambda
chi_lambda(T_u), and this is the signature of Geck-Pfeiffer's minimal-length
class-representative theory: the trace at a class's minimal length differs from
the trace at higher length in the same class, which is exactly why cycle type
cannot determine it. In S_4, class (3,1) has minimal length 2 with 4(q-1)^2 and
reappears at length 4 with (q-1)^2(q+1)^2.

=> The closed form, if wanted, IS Geck-Pfeiffer 7.2.6, the theorem this bean
names. PRICE THE REMAINDER AS MATHLIB-SCALE CHARACTER THEORY: multi-session,
research formalisation, not a proof to be typed out. Combined with the
characteristic bound already recorded (det != 0 => semisimple is
one-directional, so the route cannot reach small characteristic even when
finished), that is the honest state.

UNCONDITIONAL and independent of all of the above, already on main:
isSemisimpleRing_rank_one (+ the substrate corollary over R, q > 0), twGram and
isSemisimpleRing_of_twGram_det_ne_zero at every rank, the full σ_mul_Tw
table, trace_lmul_σ, and IsHeckeOfFullRank for IwahoriHecke at every rank.


## 2026-09-02 — CLOSED at what is proved; the remainder is qou-kwoa

Owner instruction, this session: close this bean at what is proved and split
Geck-Pfeiffer 7.2.6 into its own Mathlib-scale bean, because this title reads as
though a lemma is missing when the remainder is a book-length development.

### Delivered, all sorry-free and on main (#6053, #6134, #6165)

* basisTwOfField — the T_w basis, a real Module.Basis over a field, WITHOUT
  Matsumoto (still a Mathlib TODO); finrank_eq_factorial : dim = (n+1)!.
* twGram + isSemisimpleRing_of_twGram_det_ne_zero — det != 0 => H_n(q)
  semisimple, AT EVERY RANK. This is the statement the 2026-08-29 gap inventory
  §3b recorded as 'cannot even be stated without the basis'.
* TwMul.σ_mul_Tw — the full generator multiplication table, both branches.
* TwTrace.trace_lmul_σ / two_mul_trace_lmul_σ — the generator trace is
  counted by descents; 2 tr = (q-1)(n+1)!.
* twGram_det_rank_one = (1+q)^2 and isSemisimpleRing_rank_one — the first
  end-to-end discharge, on IwahoriHecke ITSELF rather than a power-basis model,
  unconditional (axioms clean on the discharge and both keystones it composes
  with).
* isHeckeOfFullRank_iwahoriHecke — the Iwahori basis theorem was a GRANTED
  ASSUMPTION in FullRank.lean's own docstring and no longer is.
* The determinant VALUE at n = 1,2,3 with the constant identified as
  prod_lambda d_lambda^(d_lambda^2); n=3 as a polynomial identity.
* The route BOUNDED: det != 0 => semisimple is one-directional, converse false.
* The blocker CHARACTERISED: not combinatorial, refuted with an S_5 witness;
  and then IDENTIFIED as a character sum, verified against the corpus's own
  seminormal engine with the convention bridge measured
  (tw_trace_equals_character_sum_probe.py).

### Not delivered, and now carried by qou-kwoa

det(twGram) != 0 at rank >= 2 in Lean. The mathematics is not the obstacle —
qou-avt2 already supplies exact symbolic chi_lambda at general n, and the
identity tr(L_{T_u}) = sum_lambda d_lambda chi_lambda(T_u) is measured. What
remains is formalising that character theory, which is Mathlib-scale.

SchurElementCriterion still has NO instance; both obligations the gap inventory
§3b separates remain open. Nothing here bears on the P!=NP wall — semisimplicity
is a magnitude-axis fact.
