---
# qou-u96j
title: Walk the canonical derivation chain step by step and catalogue where CONDITIONS emerge
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T07:49:59Z
updated_at: 2026-09-14T09:12:21Z
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
