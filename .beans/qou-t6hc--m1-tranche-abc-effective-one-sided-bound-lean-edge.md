---
# qou-t6hc
title: 'M1 tranche A+B+C: effective one-sided bound, Lean edge-calculus, and the kappa_n correction exponent'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T09:43:34Z
updated_at: 2026-08-30T10:04:31Z
---

Tranche under qou-k5r5 (M_1 > 0 all-n), taking all three options put to the owner.

State at claim: M_1 > 0 is reduced to ONE one-sided claim -- (a) exact M_1 > 0
for n <= 12 [DONE, in fact exact to n = 50], AND (b) kappa_n >= kappa for
n >= 13, where kappa = 128/(225 pi^2) is DERIVED (not fitted) via the
Ivanov-Olshanski field. Track A (Sniady genus) is dead: sub-result (1) split
Sigma_h = p2sharp_sym + T with Cov(p2sharp_sym, omega3) = 0, so M_1 = Cov(T,
omega3) with T the non-Lambda* part, and genus only reaches Lambda* x Lambda*.
Track D (Fulman exchangeable pair) is principal because its premises need
neither leg polynomial.

- [ ] C: fit the exact kappa_n series against candidate correction exponents
      (edge/Tracy-Widom n^{-2/3} is the corpus's stated candidate) to tell A
      what order it must prove. Track B's scoped job: "guiding A's order
      prediction". Only 11 rows (n = 68..78) are stored as a witness, so the
      series n <= ~50 has to be recomputed exactly first.
- [ ] B: formalize the Fulman edge calculus in Lean -- Fact A's per-edge
      inequality d(Sum|c|) d(omega3) = (|c_r|-|c_a|)^2 (|c_r|+|c_a|) >= 0,
      giving P >= 0 UNCONDITIONALLY (half of M_1 = P - N, with a sign); the
      three local increments; and the 1-Lipschitz lemma |D(u+1) - D(u)| <= 1
      which is what bounds the per-edge ratio by 4. All four are flagged
      "Lean-formalizable, verified exact" and none is done. The omega3
      J-eigenfunction identity needs the up-down chain and is heavier -- scoped
      OUT of the first pass.
- [ ] A: the one-sided effective bound. The real gap. Elementary routes are
      already REFUTED in the parent bean: per-edge ratio is unbounded (max 4, so
      no FKG) and weight-suppression fails because N/P < 1 is an averaging
      phenomenon, not worst-case. Attempt informed by C; report honestly if it
      walls, do not launder.

Connection worth recording: the corpus's T = Sum_box(i+j) - n IS Sigma_h under
1-based box indexing (checked: difference exactly 0 on every partition of
n <= 12; exactly 2n under 0-based). So `sum_hookZ_eq_bStat`, merged today in
QOU/BraidKnot/HookSumClosedForm.lean, is the reduction's own central identity,
now machine-checked. That was accidental.


## Outcome (2026-08-30)

**B — DONE, sorry-free.** `QOU/BraidKnot/M1EdgeCalculus.lean`, 8 theorems, all on
`[propext, Classical.choice, Quot.sound]`, wired into the umbrella (not an
orphan). Two findings from doing it:

- **Fact A is not combinatorics.** `(|c_r|-|c_a|)(c_r^2-c_a^2) =
  (|c_r|-|c_a|)^2(|c_r|+|c_a|) >= 0` holds for ANY two integers, because
  `c^2 = |c|^2`. So `P >= 0` per-edge needs no property of Young diagrams at
  all; the diagrams only supply the two increment formulas. `factA_nonneg` is
  therefore stated for arbitrary `cr ca : Z`, which is the honest strength.
  Also proved `factA_eq_zero_iff`: the product vanishes iff `|c_r| = |c_a|`,
  identifying the omega_3-neutral edges a domination argument may discard.
- **The 1-Lipschitz lemma has a three-line proof.** Diagonal indices are
  downward closed, hence an initial segment; if `D c` exceeded `D (c+1)` by two,
  the two indices in the gap would both force `rowLen i = i + c + 1`, giving a
  strictly longer row below a shorter one against `rowLen_anti`. Reuses the
  corpus's own `HookSumComplete.downward_closed_eq_range`. Cross-checked: 3561
  diagonals over all partitions of n <= 14, 0 violations, max jump exactly 1 --
  so the Lean bound is tight.

**C — DONE, and it overturns the workplan's target.**
`computations/deltalambda/m1_kappa_correction_exponent_probe.py`, 8/8, witness
committed. kappa_n recomputed in exact integer arithmetic for n = 3..58 (the
series was NOT stored -- only the 11-row window n = 68..78 was) with a
Plancherel control `sum W = n!` at every n.

- Reproduces the corpus exactly: crossing at n0 = 13, peak delta = 0.001556 at
  n = 32.
- Decay exponent alpha[68..78] = 0.4310, strictly between 1/3 and 1/2, and STILL
  RISING (alpha[58..68] = 0.3853). Not converged.
- Measured local correction exponent 5/2 - alpha = **2.069 > 2**, so the
  workplan's `M_1 >= kappa n^{5/2} - C n^2` ansatz is NOT supported in the
  accessible range.

**But the order is genuinely UNSETTLED, and I nearly shipped the overclaim.**
My first version of the probe asserted "correction exponent exceeds n^2" as a
conclusion. Testing candidate FORMS by residual drift across five disjoint
windows shows two survive with drift shrinking to zero -- `n^(2/5)` and
`n^(2/3)/log n` (the corpus's own edge/Tracy-Widom candidate, with a log) --
while `n^(1/2)/log n` and `n^(2/3)/log^(3/2)` drift away. The two survivors
STRADDLE the ansatz:

    delta ~ A n^(-2/5)        =>  correction ~ n^2.1        ansatz FAILS
    delta ~ A n^(-2/3) log n  =>  correction ~ n^(11/6) log n  ansatz HOLDS

The local exponent 2.069 sits between them because a log biases it downward.
The probe now asserts the ambiguity rather than either branch.

**A — NOT CLOSED, and one route is now closed off.** The two surviving forms
differ by `n^(4/15)/log n`, which grows 1.02x by n=120, 1.06x by n=200, 1.12x
by n=400 and only 1.73x by n=10000 -- against measured residual drifts of ~0.4%
and partition counts of p(200) = 4.0e12, p(400) = 6.7e18. **Exact enumeration
can never separate the two forms.** Track B is therefore closed as a route to
deciding the correction's ORDER, not merely deprecated: only the analysis can
decide it, and it must decide it before an effective bound can be aimed.

That is the concrete handoff to A: do not target `-C n^2` until the form is
settled, because the data does not support it and cannot be made to.
