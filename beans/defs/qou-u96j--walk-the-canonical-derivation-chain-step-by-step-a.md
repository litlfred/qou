---
# qou-u96j
title: Walk the canonical derivation chain step by step and catalogue where CONDITIONS emerge
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T07:49:59Z
updated_at: 2026-10-04T15:14:22Z
parent: qou-v2om
---

## 2026-09-14 — first tranche: steps 5 and 10 walked

PARTIAL walk. Measured steps 5, 6 (partially), 10. Step 2's condition is already
in the cheat sheet's own §2a (curvature 2-form stipulated) and is cited, not
re-derived. **Not walked: 1, 3, 4, 7, 8, 9, 11** — named so the gap is visible.

### C5a — step 5's partition sum runs over TWO-ROW partitions only
The step says `tr_M = Σ_{λ⊢n} y_λ χ^λ` over ALL partitions. Measured against the
committed `y-lambda-at-q0.witness.json`: at **every n from 2 to 12**, every `y_λ`
with ≥3 rows is **exactly 0** and every nonzero one has ≤2 rows (at n=12: 7
nonzero, 70 zero). Production family is `y_lambda_su_n(n, q, 2)` — the trailing
`2` is a row cap. AGENTS.md does say "convention D = the two-row truncation", so
the fact is known; what is missing is that **the chain's own step statement does
not carry it**.

### C5b — `α` is a Wenzl weight, not an ad-hoc ratio
`y_(3)` at n=3 equals `(q⁴+1)/(q²+1)²` **exactly** (45 dps, |diff| 5.0e-47). That
is the same α as the 2026-09-08 Q_β ruling's augmentation-to-z_D factor and as
the flavour-split fork in #7334. Two arcs reached α independently; both were
reaching the trivial block's Wenzl weight.

### C5c — normalisation is dimension-weighted (and I got it wrong first)
`Σ d_λ y_λ = 1` exactly at every n (this is `tr_M(1)=1`, since `χ^λ(1)=d_λ`). The
unweighted `Σ y_λ` is 1 only at n=2 and falls to 0.0133 by n=12. My first reading
was the unweighted one and produced a false "the y are not a measure" claim.
Distinct from the `w_λ(q)` non-normalisation in the notation register — that is
the quantum Plancherel family, a different object.

### C10a — `n_target` has three inequivalent production meanings
Spec declares `n_target ∈ ℤ≥0` (integer). Measured at source:
* `aK_via_lp_dual_hecke_basis.py:175` — `tr_M_atom`, a Markov trace (REAL)
* `pn_alpha_lp_dual.py:375` — `float(pn_vec.sum())` (REAL, α-dependent)
* `option_b_proton_mass_full_chain.py:588` — `float(n_gg)`, γγ count (INTEGER)

Each cites a different authority. Only the third matches the declared type.
`n_target` is what *selects* `T_w`, so this is step 10's emergent condition.

### C10b — the cheat sheet states an objective the code does not have
§1 and §2 render step 10 as `min ‖tr_M(T_w)·𝔈₀ − B_tgt‖`. The authoritative
algorithm block has **no B_tgt** (`min Σ tᵢxᵢ s.t. net(x)=n_target, Gx≥0`) and
`solve_operator_selection_lp(t, G, n_target)` has no such argument. The defect
points the SAFE way — the doc looks more fitted than the code — but it is in the
primary coordination document and would lead a reader to conclude the chain fits
AME at its selection step.

### Next
Step 3's "unique trace" — where `z` enters, and the likeliest root of the
`qou-99qc` / `qou-qqm4` fork. Not established here, so not asserted.


## 2026-09-14 (cont.) — step 3 walked, and it CORRECTS the tranche above

Walking step 3 closed the question **in the direction opposite to my expectation**,
and corrects C5a.

### The whole fork reduces to ONE condition, and it sits at STEP 1

`rem:markov-axioms-primitive` states correctly that axioms 1-2 admit a
**one-parameter family** — so the cheat sheet's "unique trace" at step 3 is the
compressed form. But the parameter is then **forced**, sorry-free:

    V = fundamental of SU_q(2)      <- the HYPOTHESIS, and the only one
      => l(lambda) <= 2               lem:feynman-eigenbasis-decomposition
      => y_(1^3) = 0
      => [+ faithfulness]             markovWeights_eq_jones_of_threeRow_eq_zero
      => y_(2,1) = 1/[2]_q^2, y_(3) = alpha, z = q^3/(q^2+1) = z_D

Verified symbolically and against the committed witness (both reproduce to 30 dps).

### 🛑 This CORRECTS C5a

I called the two-row cap "a condition the chain's step statement does not carry",
which reads as a truncation bolted on at step 5. **It is not** — it is derived
from the step-1 choice of `V`, and it is what FORCES `z_D`. What step 5 omits is
the **hypothesis**, not the truncation. The measurement was right; the emphasis
was wrong.

### alpha is DERIVED, not coincidental

`y_(3) = 1 - 2/[2]_q^2 = (q^4+1)/(q^2+1)^2`. It follows from the theorem; it was
never an observed coincidence needing explanation.

### A derivation-first discriminator on the fork

`z = q` is `markovWeights_degenerate_root`: `y = (1,0,0)`, so `y_(2,1) = 0` and
the trace is **not faithful** on TL_3 (`z[2]_q = q^2+1 != q^2`).

That discriminates the `qou-99qc` / `qou-qqm4` fork **using no residual at all** —
the ranking the anti-fit rule demands — and it points **away** from the
augmentation, the cell that reproduced the flavour-split baseline exactly in
#7334. **Recorded, not acted on**: which cell to adopt is still the owner's call;
what changes is that it is no longer a choice between two equally-derived options.

### Measurement note

`grep -c sorry` on MarkovTraceTLUniqueness.lean returns 1 — the word inside a
COMMENT ("sorry-free, lean-direct exit 0"). No `sorry` tactic. I raised a false
alarm on it before checking. Counting the word is not counting the tactic.

### Next

**Step 1 itself: is the choice of `V` derived, or is it the framework's
primitive?** Everything above now hangs on that one sentence, so it is the
highest-value remaining question. Steps 4, 7, 8, 9, 11 also remain unwalked.

## 2026-09-14 — (1) answered: no route to g=4 escapes SU(2)

The walk's top-priority open question was whether any corpus route to the genus
is independent of SU(2). **Answer: no.** Three routes exist; all three name
SU(2) in their own first or last sentence, and route 3 declares
`uses: ["prop:cohomological-embedding"]` so is not even formally independent.

**And route 3's stated criterion is not met at g = 4.** Its claim that the 6x5
character matrix 'has rank 5 (verified numerically)' is structurally impossible:
T_{r,s} closes a braid word on r strands, so M is block-diagonal and rank is
additive; at g=4 four r=2 rows (rank <=2) and TWO r=3 rows (rank <=2) give
rank <= 4 < 5, at no q rather than at some q. Exact sweep over Q(q):
g = 1..7 -> rank 1,2,3,4,4,5,5. First met at g=6, where the proof's own
restriction to r in {2,3} lapses (T_{4,5} has genus 6). No producer computes
the matrix; Lean carrier is validation: not_checked.

Corrected my own claim mid-probe: rank at g=3 is 3, not 4, so the *exclusion*
of g=3 is correct and only the *acceptance* at g=4 is wrong — by one.

Scope (b), invariant = rank subadditivity over a block decomposition. NOT a
claim that g != 4; routes 1 and 2 untouched and route 2's arithmetic is clean.

Probe `computations/audits/genus_completeness_rank_probe.py` (22/22, exact,
no float). Commit f504492523, PR #7362.

**Still open** (the bean stays in-progress): the g=4 completeness sentence needs
an owner disposition (re-scope / restate / retire); the why-b3 rank-1 vs
descartes-knot rank-2 contradiction; steps 7, 8, 9, 11 unwalked.

## 2026-09-14 — step 4: the "6 <-> 6" is a coincidence of counts

Walked step 4 with the tool the genus finding built. The cheat sheet's arrow
`6 basis elements <-> 6 torus knots <-> particle content` sets two different
sixes against each other. The corpus is clearer than the diagram:
`knot-operator-basis-table.md` names the NF basis
`{gamma, sigma_0, sigma_1, L_+, L_-, e^-}` and treats the knots as OPERATORS
on it.

Measured, exact over Q(q) via the faithful rep (3)+(2,1)+(1,1,1) — so the span
in the ALGEBRA, not of characters: the six torus-knot words span **4 of H_3's
6 dimensions**. Four 2-strand words span 2 (Hecke collapses sigma_1^s into
span{1,sigma_1}; seven of them still span 2, measured s=3..15), two 3-strand
words span 2.

**The same 2+2 as the genus finding, one level down** — there four 2-strand
ROWS filled two H_2 columns and two 3-strand rows two of three H_3 columns.
One structural fact surfacing in both a character space and an algebra.

Scope (b) for the narrow claim only. NOT a claim step 4 is wrong; the knots are
used as operators and a 4-dim operator family is not defective. The "6<->6"
simply cannot be a linear-algebraic identification.

Probe `computations/audits/step4_torus_knot_span_probe.py` (17/17). Commit
bba57cb415, PR #7362.

**Still open:** the g=4 completeness sentence; the cheat-sheet step-4 arrow
wording; the why-b3 rank-1 vs descartes-knot rank-2 contradiction; steps 7, 8,
9, 11 unwalked.

## 2026-09-14 — step 11: the cheat sheet's hadronic E_0 is circular

Step 9 gives `E_0 = Q_beta/|h(h-2)/2|` (hadronic); step 11 gives
`Q_beta = |Delta(net)|.E_0`. Substituting: **Q_beta = Q_beta, identically** —
step 11 derives its own input. AGENTS.md Derive-then-check item 8 verbatim.

**Convention-independent**, which is the point: whichever Delta is right
(z=1 / z=q / the ruled z_D), `E_0 := Q_beta/|Delta|` then `Q_beta := |Delta|.E_0`
is an identity. qou-99qc cannot repair it. Shown over exact rationals at 4 Deltas.

**What the hadronic form is:** `E_0 lept / E_0 had = 1.00167757`, a gap of
0.1678 % — i.e. the famous '0.17 % vs CODATA' written backwards, and a cell
AGENTS.md has RETIRED as the base.

**Production is NOT circular** — 4 computations/qbeta/ files carry
`E0 = M_E/(Q0*(Q0-1))/(1-HBAR_Q**2)`, a closed substrate expression with no
Q_beta in it. So the defect is in the coordination document, not the compute;
same class as C10b but worse (C10b overstates fittedness, this makes a step
vacuous).

Scope (b), invariant = |D|.(X/|D|) = X.

**Two corrections to my own probe**: (i) I asserted bit-equality at dps=60 for
arbitrary Delta and it correctly FAILED on pi/10 — the identity is algebraic,
not arithmetic; now over exact rationals. (ii) The precision gate caught
`mpf(str(Q))` laundering a float64 — fixed to `mpf(Q_50_DIGIT_STR)`; same pass
found Q_beta hardcoded from prose vs the live `Q_NEUTRON_MEV`, moving E_0 had
in its 9th digit.

Probe `computations/audits/step11_qbeta_e0_circularity_probe.py` (10/10).
Commit 119b61f7fb, PR #7362.

**Still open:** the g=4 completeness sentence; the step-4 arrow wording; this
hadronic-E_0 line (highest priority of the three doc fixes); the why-b3 rank
contradiction; steps 7, 8, 9-leptonic unwalked.

## 2026-09-14 — steps 7-8 walked: ALL ELEVEN STEPS NOW COVERED

Measured over the corpus dependency graph (3565 labelled blocks from .ts):

1. `conj:jet-convergence-classical-limit` (step 8) is a **dependent**
   conjecture — `uses: [conj:jet-filtered-knot-factor]`. The step table flags
   it as a conjecture but not that it stands on a second one.
2. None of steps 9/10/11 reaches — through `uses[]` — any of the three
   carriers the step table NAMES for steps 7-8. Cones: 79 / 3 / 102.

**Corrected my own framing**: I first wrote 'steps 9-11 stand independently of
the GB/jet machinery'. Too strong — step 9's cone DOES reach
`prop:jet-prefix-gb-filtration`, the same machinery under a different label.
So the claim is about LABELS: the diagram's arrow is not a `uses[]` edge.

Conjectures in cones: step 9 has 4 via two routes; steps 10, 11 have zero.

**PRIOR ART, cited not re-derived** (corpus-grep caught both before writing):
`prop:atom-knot-mass-derivation` is an already-adjudicated §3b-cond item-5
violation — bean **qou-tmmt**, 8 confirmed of 9, still todo; and `MassIdentity`
reducing to a 25 % AME tolerance is in `2026-06-07-proof-rater-baseline-audit.md`.
What survives as new is the graph measurement alone.

Probe `computations/audits/chain_uses_graph_vs_diagram_probe.py` (12/12).
Commit 0a92add9ed, PR #7362.

**Bean stays in-progress.** All eleven steps are walked to the level of 'what
condition enters', but four document fixes are open for the owner (g=4
completeness sentence; step-4 arrow; hadronic E_0; step-7/8 labels) plus the
why-b3 rank contradiction — and the interior mathematics of steps 7-9 (the GB
collapse, the Archimedean realisation functor) is untouched.

## 2026-09-14 — step 9 walked; the walk is COMPLETE

Step 9 is where the chain crosses Q(q) -> R, so where an unstated condition
would matter most. **It is the most carefully written step**, and the finding is
small.

- `def:archimedean-realization-functor` **withdraws its own name**: 'functor' is
  legacy; R_top is a ring hom out of K_0(Var), a realization/evaluation.
- **The condition IS declared**: `R_top = tau_arch on M_QOU subset M` — so tau's
  'exclusive exit to R' holds on a SUBDOMAIN, not in general.
- **One defect**: `M_QOU` occurs **exactly once** across every `.md` in
  `content/` — in the sentence that uses it — and is defined nowhere. Its two
  siblings (`vol-through-tau`, `vol-as-motivic-period`) state the identical
  agreement scoped to `def:algebraic-quantum-volume`, which EXISTS. One-symbol fix.
- **Not claimed**: that `chi_top` is ill-defined. The remark allows it to be an
  Euler characteristic OR a hyperbolic volume — two codomains, one name, no
  notation-register entry. Recorded as an overload, not measured as a defect.

The contrast with step 11 is the point: both concern the crossing to R; step 9
states its scope, step 11's E_0 line inverts its own output.

Pinned as section 8 of `canonical_chain_condition_walk_probe.py` (4 quotes at
source + the corpus-wide count). VERDICT PASS. Commit 254d250f3c, PR #7362.

### Walk status: all 11 steps covered

FIVE document defects open for the owner, none in the compute, all with safe
no-op defaults:
1. step 11 hadronic `E_0` — makes the step **vacuous** (highest)
2. `g = 4` completeness sentence — **false as written**, no producer
3. step-4 `6 <-> 6` arrow — reads as an identification that does not hold
4. step-7/8 labels — do not match the `uses[]` graph
5. step-9 `M_QOU` — undefined symbol (cheapest, one symbol)
plus the why-b3 rank-1 vs descartes-knot rank-2 contradiction.

**Bean stays in-progress**: the interior mathematics of steps 7-9 is untouched —
the GB spectral sequence's actual collapse, and the Archimedean realisation
whose absence `MassIdentity`'s 25 % tolerance stands in for.

## 2026-09-14 — step 7 is PRIOR ART; process miss recorded

Step 7's interior: the step-9 theorem's HYPOTHESES are free —
`GbSpectralSequenceCollapseAtE2 := (gbSpectralCollapsePage = 2)` i.e. `2 = 2`,
and `YekutieliFiniteSliceMultiplicativeTrace T_w := Nonempty T_w`.

**Already reported verbatim** in `2026-09-08-l2-1ppq-research-program-gaps.md`
row 7, bean **wpdb**. I re-derived it. The Lean declares it itself in its
docstrings ('pinning the collapse page to 2 by construction … awaits Mathlib
spectral-sequence support') — honest authoring, not laundering.

**THE PROCESS MISS.** That audit walks the SAME CHAIN step by step and I did not
find it until step 7. Every corpus-grep I ran was scoped to the FINDING; none
asked 'has anyone walked this chain?'. A topic-scoped grep is how the checklist
gets skipped without feeling skipped.

**Measured overlap** — 4 of 5 defects are NOT in that audit (#1 hadronic E_0
circularity, #2 g=4 rank-5, #3 step-4 span, #4 uses[] graph, #5 M_QOU); the
step-7 one IS. Its step-10 row is close to but not identical with C10a (one
caller named circular, vs three inequivalent meanings measured).

**Possibly new, stated cautiously:** the collapse PAGE disagrees — cheat sheet
says E_2 in three places, `prop:spectral-sequence-collapse` says E_1. E_1 is
strictly stronger and matches the block's own HH^k=0 argument, so the cheat
sheet understates its own proposition.

Commit ef5fcb5f5b, PR #7362.

## 2026-09-14 — 🛑 WITHDRAWING the step-4 conclusion (defect #3)

I claimed the step-4 arrow '6 basis elements <-> 6 torus knots' is 'a coincidence
of counts, not a linear-algebraic identification'. **Too strong; withdrawn.**

Cheat-sheet **§9.5** names the diagram's six explicitly — `{1, s1, s2, s1s2,
s2s1, s1s2s1}`, the GB basis of H_3 — and exists precisely to correct 'a
recurrent agent confusion … reading 6 basis elements as 6 INDEPENDENT
SM-equivalent operators'. It calls them **GENERATORS**.

Measured: span of the six knot words = **4 of 6**; subalgebra **generated** =
**6 of 6**, products alone, no inverses. **Under §9.5's reading the six torus
knots DO generate H_3(q).** My span result refutes only the BASIS reading, which
§9.5 refutes at greater length — so the section corroborates the corpus.

Residue: the §1 diagram's bare '<->' still invites the basis reading and §9.5 is
~700 lines below it. And `{gamma, sigma_0, sigma_1, L_+, L_-, e^-}` is a THIRD
six from another appendix, not what the diagram means.

**Second instance of the same process failure in one session** (after step 7 /
bean wpdb): greps scoped to the finding, never to whether the document already
addressed it. §9.5 is in the SAME FILE as the diagram I was criticising. Pattern,
not incident: **when the subject is a document, read the document.**

Defect count drops 5 → 4. Probe 19/19 (new section 2b). Commit 7c746a9862.

### Also read this session: 2026-09-08 audit §7.3 / §8.4
C1 ('update the cheat sheet') is an **already-authorised** coordination repair,
run for §0 rows 9b/11 and §9.3. My remaining defects sit in the **§1 diagram and
§2 step table**, which C1's scope does not name — so they are an uncovered
surface of an authorised repair, not four new asks. §7.4 'Do not' checked
against my work: clean.

## 2026-09-14 — #7362 MERGED (e8289b4971); defect #2 now has a DERIVED disposition

Walk PR merged (rebase, 17 commits). Then answered the 'restate' branch of
defect #2 **from the corpus**, so it is no longer a three-way judgement.

**The repair.** The criterion asks the torus-knot EVALUATIONS to span the
character space of H_2 + H_3. An evaluation here is a MARKOV TRACE (step 3:
`J_K(q) = tr_M(rho(beta_K))`), and `tr_M = sum_lambda y_lambda chi^lambda`. A
block with `y_lambda = 0` is invisible to every evaluation at every genus. Under
convention D's two-row truncation — derived from `dim V = 2`, pinned in Lean as
`markovWeights_eq_jones_of_threeRow_eq_zero`'s hypothesis `y_(1^3) = 0`, and
EXACTLY 0 in the committed witness — `(1,1,1)` is such a block:

    observable directions = (2),(1,1) | (3),(2,1) = **4**, not 5

Exact sweep over Q(q): rank_obs = 1,2,3,**4**,4,4,4 at g = 1..7. **g_min = 4
exactly, first crossing.** The proof's ARITHMETIC was right; only its TARGET was
wrong. Its conclusion stands.

**Anti-fit, answered:** derivation order is truncation → target → genus; the cap
predates anything about genus; the corrected criterion is met at 4,5,6,7 (not
only 4 — a tuned target would be met at 4 alone); and it was derived AFTER the
refutation, which is not withdrawn and is re-asserted in the probe.

**NOT claimed:** that g=4 is derived — the route still opens in `Rep(SU_q(2))`
and still `uses: [prop:cohomological-embedding]`, so it remains inside the
chi=-6 <-> SU(2) cycle. No content block edited.

Probe `computations/audits/genus_completeness_observable_target_probe.py`
(13/13). Commit 86194f8f7e, **PR #7365**.

**Remaining open:** defects #1 (step-11 hadronic E_0 — vacuous), #4 (step-7/8
labels), #5 (M_QOU) still want the C1 scope decision; the interior mathematics
of steps 7-9 untouched.

## 2026-09-14 — defect #1 also answerable from the corpus; 4 judgements → 2

`computations/qbeta/qbeta_e0.py` opens **'the ONE place E_0, the Q_beta energy
scale, is defined'**, and its ENTIRE public API is:

| `order_zero()` | `m_e/(q(q-1))` | **'NOT canonical'** |
| `tower_summed()` | `m_e/(q(q-1))/(1-hbar_q^2)` | canonical |
| `canonical()` | = tower_summed | 'every new producer should call' |

**No hadronic variant.** One scale, both channels. So the cheat-sheet step-9 line
is wrong TWICE: its 'lept' form IS `order_zero` (explicitly non-canonical), and
its 'had' form names an object the API does not have (and is circular).

The fix is **completed, owner-instructed work** the document has not absorbed —
the module records two forms differing 0.9915 % 'with no signal at either call
site', 'Unified here on owner instruction, 2026-09-12', tower_summed canonical by
the 2026-09-03 full-tower ruling.

Corpus-determined correct form: `E_0 = m_e/(q_0(q_0-1))/(1-hbar_q^2)`, call
`qbeta_e0.canonical()`. Measured 4.1859813633 / 4.2274833556, ratio 1.00991486;
12 producers route through it, 15 hand-roll (reported, NOT adjudicated —
qou-y3bm's business).

🛑 NOT claimed, and the module says it first: that the tower sum IS
`sum_k hbar^2k = 1/(1-hbar^2)` — 'taken from the one live precedent, NOT
derived' (qou-y3bm). **Canonical = BY RULING, not proved.** 🛑 And this is a doc
line, not the Q_beta residual: E_0 moves Q_beta 0.9915 %, the convention-D
functional 257x.

Probe `computations/audits/step9_e0_canonical_form_probe.py` (9/9). Commit
890105c71c, PR #7365 (now carries both #1 and #2).

**Status: 4 judgements → 2.** #4 (step-7/8 labels) and #5 (M_QOU) still want the
C1 scope decision. Neither #1 nor #2 makes g=4 DERIVED — the route still opens in
`Rep(SU_q(2))` and stays inside the chi=-6 <-> SU(2) cycle.

## 2026-09-14 — #5 measured: a JUDGEMENT, not a fix. PR #7365 MERGED (612cb27265)

**#5 does NOT collapse the way #1 and #2 did**, and my 'one-symbol fix'
characterisation is **withdrawn**.

1. The symbol is **not meaningless** — its own sentence glosses it: 'On motivic
   QOU inputs, R_top coincides exactly with the archimedean component of tau'.
   'Defined nowhere' was true of a definition BLOCK, overstated as a
   description of the reader's position.
2. The gloss **has a Lean carrier** — 'QOU motivic' in six .lean files, incl.
   `archimedean-functor-uniqueness.lean` and `MotivicSubstrate.lean`, which
   axiomatises 'the QOU motivic substrate'.
3. **But it is not a defined SUBSET.** `MotivicSubstrate`'s `Mhat` is 'the
   dimension-completed localization K_0[L^-1]^' — i.e. Mhat IS \widehat{M},
   entire. The Lean has no proper subobject, so `Mhat_QOU subset Mhat` names a
   restriction the formalisation does not have.
4. **And nothing EQUATES it with the siblings' scope.**
   `def:algebraic-quantum-volume` is `Vol_alg(W) := tr_M(W)` — a trace value,
   a different KIND of object. Exactly one block mentions both (the remark),
   and relates them by **'exemplifies'** — an instance, not an equation.

**Verdict:** replacing the symbol would ASSERT an identification the corpus
does not make. Three non-equivalent dispositions, none corpus-chosen: define
the subset / assert the identification / leave it.

🛑 Negative result with its surface: searched content/**, docs/**, .beans/, the
Lean tree. What would separate the readings is a block saying Mhat_QOU is (or
is not) the image of the algebraic quantum volume — not found, which differs
from proving none can exist.

Probe caught my own over-claim again: I first asserted 'NO block mentions both'
and it FAILED on the remark's Synthesis sentence.

Probe `computations/audits/step9_mqou_scope_probe.py` (8/8). Commit 6118cb69a6.

### PR #7365 merged (612cb27265, rebase) — carries #1, #2 and #5

**Final tally of the walk's four defects:**
- **#1** step-9/11 E_0 — **corpus-determined** (one canonical form, qbeta_e0)
- **#2** g=4 completeness — **corpus-determined** (target 4; g_min=4 recovered)
- **#4** step-7/8 labels — **still a judgement** (is the arrow a dependency claim?)
- **#5** M_QOU — **still a judgement**, but smaller than the walk implied

So ONE genuine judgement (#4) plus #5's disposition choice remain for the owner.


## 2026-09-14 — the derivation attempt on steps 7–9 returned PRIOR ART; and a fourth `J^•`

**Step 7's interior is closed.** I derived what I took to be a new obstruction
— `1 = Σ_λ e_λ` uses every primitive idempotent, so a filtration with `1 ∈ F_0`
whose induced centre grading is `span{e_λ : δ(λ) = c}` forces `δ` constant,
which `gbDepth_ne_on_H4` refutes from `n = 4` up. **That is Route A**, proved
sorry-free on 2026-08-26 as
`QOU.BraidKnot.unit_in_degree_zero_forces_constant_grading`, and formalised
better than mine (it keys on `π l u = 1`, never mentioning a basis). Its
docstring already excludes the candidate I would have tried next — the
Jucys–Murphy content filtration. Four audits, three sorry-free Lean files,
three exact probes. Nothing there to derive.

**Defect #4 has changed, and half of it is now corpus-determined.** The
cheat-sheet step-7 row says *"Filtration by Coxeter length `ℓ(w)`; spectral
sequence collapses at `E_2`"*, while the carrier block
`prop:spectral-sequence-collapse` says **`E_1`** in its own first line — and
`E_1` collapse is strictly stronger, so the document **understates its own
carrier**. Separately, the Coxeter-length reading is the one excluded at every
`n ≥ 2` (`no-shift-rescues`, sorry-free `shift_cannot_fill_a_gap`).

**🛑 And the walk found a FOURTH reading of `J^•` that no audit has** —
`def:confinement-level`, cited by `prop:gb-spectral-sequence` itself. It
evades both exclusion routes structurally (unit at the top, non-monomial) and
ties step 7 to step 10. Bean **`qou-sw8n`**, priority high.

The residue of defect #4 is still a judgement: whether the §1 diagram's arrow
asserts *dependency* (so the labels should name `prop:jet-prefix-gb-filtration`,
which is where the `uses[]` graph actually routes) or is narrative.

Probe: `computations/audits/step7_bridge_disposition_probe.py`, 23/23. PR #7375.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 76 Progress (2026-11-17T12:02:46Z)
- Advanced in PR `litlfred/qou#8337` (branch `feat/round76-torusmass-pinchoct-gramsig-motivic-spectrahedral-43c1`, head `df1ab810bdd422f72dc74878dc341f5f55564271`).
