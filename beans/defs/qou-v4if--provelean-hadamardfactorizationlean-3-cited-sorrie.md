---
# qou-v4if
title: 'PROVE(lean): HadamardFactorization.lean — 3 cited sorries [cited manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - repo-infra
    - tractable
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-08-08T07:40:00Z
parent: qou-k1mq
---

STILL-OPEN (honest) for norm_one_sub_weierstrassFactor_le (the PI-2 brick). Statement TRUE and standard (Ahlfors 5.3): for ||z||<=1, ||1 - E_p(z)|| <= ||z||^(p+1), E_p(z)=(1-z)exp(sum_{k<p} z^(k+1)/(k+1)).

NOT tractable in Mathlib v4.24.0 within reason. The classical proof is NOT an elementary norm inequality: it goes through the power-series identity E_p'(z) = -z^p * exp(g(z)) with g nonneg-coeff, hence 1 - E_p(z) = z^(p+1) * sum_{n>=0} d_n z^n with d_n >= 0 and sum d_n = 1 - E_p(1) = 1; then |1-E_p(z)| <= ||z||^(p+1) sum d_n ||z||^n <= ||z||^(p+1). Formalizing needs: (i) exp of a nonneg-coeff formal/analytic series has nonneg coeffs, (ii) term-by-term integration of E_p' to get the coeff structure, (iii) evaluating the coeff-sum at z=1 via E_p(1)=0. Mathlib has Complex.exp series + FormalMultilinearSeries but no Weierstrass primary factor / canonical-product infra; assembling (i)-(iii) is a multi-hundred-line build. The file's own roadmap marks it PI-2 'not elementary; deferred', and the other two sorries in the file (multipliable_canonicalProduct PI-3, hadamard_factorization PI-5) are strictly harder (Jensen/Nevanlinna).

No sub-case removes the sorry (statement is universally quantified over p and ||z||<=1; p=0 is just the equality ||z||=||z||). Left sorry + -- Ref: [Ahlfors] intact; NOT weakened or faked. Recommend building the nonneg-coeff exp-series lemma as a dedicated brick first. Branch claude/prove-tractable-cited-sorries-2026-08-01.

---

## 2026-08-07 — PI-2 **PROVED, sorry-free**. 3 cited sorries -> 2.

`norm_one_sub_weierstrassFactor_le` is closed in
`QOU/Mathlib/WeierstrassFactorEstimate.lean` (PR #4696). Verified by
`#print axioms`: `[propext, Classical.choice, Quot.sound]` — no `sorryAx`.
`multipliable_canonicalProduct` in the same file still reports `sorryAx`,
which is the contrast that shows the closure is real.

**This bean's own tractability assessment was wrong, and usefully so.** It
concluded "NOT tractable in Mathlib v4.24.0 within reason", because it costed
the TEXTBOOK route: (i) exp of a nonneg-coeff series has nonneg coeffs,
(ii) term-by-term integration, (iii) evaluate the coeff-sum at z=1. That is
indeed a multi-hundred-line build.

The route actually used needs NONE of (i)-(iii), and is ~230 lines:

  1. `E_p'(z) = -z^p exp(S_p(z))` — the telescoping `(1-z)sum_{k<p} z^k = 1-z^p`
     cancels the -1 from the linear factor, leaving one monomial.
  2. FTC along `t -> tz`:  `1 - E_p(z) = int_0^1 z^{p+1} t^p exp(S_p(tz)) dt`.
  3. `Re(w^k) <= ||w||^k` termwise bounds the integrand by its real value.
  4. `int_0^1 t^p exp(S_p(t)) dt = 1` EXACTLY, by the real FTC on `1 - E_p`
     with endpoints 0 and `1 - E_p(1) = 1`.

Step 4 is what makes the constant sharp: the crude bound `exp(H_p)/(p+1)`
exceeds 1 for every `p >= 1` and does not prove the theorem. `E_p(1) = 0` is
the single fact that pins it.

**Generalisable lesson:** "needs nonneg power-series coefficients" was a
property of the chosen proof, not of the statement. Before costing a cited
sorry as intractable, check whether an integral/FTC route reaches the same
bound — Mathlib's `intervalIntegral` support is much stronger than its
power-series support.

### Remaining 2 — roasted 2026-08-07, both survive as genuine gaps

- **`multipliable_canonicalProduct` (PI-3).** Needs a normed
  *summable => multipliable* criterion. Searched the reachable environment at
  wide scope (7 analysis modules, full enumeration of every declaration
  matching `ultipliable` + {`ummable`,`norm`,`one_add`}): exactly ONE hit,
  `multipliable_one_add_of_summable_prod`, whose hypothesis is
  `Summable fun s : Finset i => prod_{i in s} f i`. That is equivalent to the
  theorem being proved, so it is not a route. **Gap confirmed.** Note PI-2 is
  no longer the blocker here — the norm bound it needs now exists.
- **`hadamard_factorization` (PI-5).** Jensen + zero-counting +
  Borel-Caratheodory; `#eval` enumeration finds ZERO declarations matching
  `eierstrass`/`adamard`/`ensen` in Mathlib. Unchanged.

---

## 2026-08-08 — PI-3 CLOSED. Two of the three sorries are now gone.

`multipliable_canonicalProduct` is proved, sorry-free:
`#print axioms` = [propext, Classical.choice, Quot.sound]. Verified with
scripts/verify-lean-direct.sh; the file now carries exactly ONE live sorry
(`hadamard_factorization`, PI-5), confirmed by axioms — only that declaration
still depends on sorryAx.

  PI-2  norm_one_sub_weierstrassFactor_le   closed 2026-08-07 (WeierstrassFactorEstimate)
  PI-3  multipliable_canonicalProduct       closed 2026-08-08  <- this pass
  PI-5  hadamard_factorization              OPEN

WHAT THE PROOF NEEDED, AND WHERE THE ROADMAP WAS WRONG.

The roadmap said "PI-3 from PI-2 + `Summable.multipliable`". There is no such
lemma. The working criterion in Mathlib v4.24.0 is

    Complex.multipliable_one_add_of_summable : Summable f → Multipliable (1 + f)

so the product is written as prod (1 + (E_p(z/a_n) - 1)) and the work is showing
`Summable (fun n => E_p(z/a_n) - 1)`.

The real subtlety is the side condition. PI-2's estimate needs ‖z‖ <= 1, and
‖z/a_n‖ <= 1 is FALSE for small n in general — it holds only eventually,
because summability forces 1/‖a_n‖^{p+1} -> 0 hence ‖a_n‖ -> infinity. No
finite-set surgery is needed: `Summable.of_norm_bounded_eventually_nat` accepts
an eventual bound. Comparing against 1/(‖z‖^{p+1} + 1) instead of 1/‖z‖^{p+1}
keeps the constant positive at z = 0 and avoids a case split.

Lemma names that had drifted in this Mathlib version and cost a round each:
`one_div_lt_one_div_iff` -> `lt_of_one_div_lt_one_div`,
`lt_of_pow_lt_pow_left` -> `lt_of_pow_lt_pow_left₀`. `positivity` also cannot
prove 0 < ‖a n‖^(p+1) without being handed `a n ≠ 0` — use `pow_pos`.

PI-5 REMAINS, and it is not a matter of finding the right lemma names: it needs
Jensen's formula, zero-counting/exponent-of-convergence, and Borel-Caratheodory
growth machinery, none of which Mathlib v4.24.0 has in usable form. That is a
multi-week build, not a session. Not attempted here, and not faked.

<!-- 2026-08-08T03:10:00Z branch claude/dg-scope-correction -->

---

## 2026-08-08 (later) — THE REMAINING SORRY SAT ON A FALSE STATEMENT.

Roasting the PI-5 statement instead of the proof turned up something worse than
difficulty. `hadamard_factorization` enumerated the zeros as `a : N -> C` with
`forall n, f (a n) = 0`. That statement is **FALSE**, and the refutation is now
in the file, sorry-free and machine-checked:

    isEntireOfOrderLE_exp                    -- exp has order 1, exp 0 = 1 /= 0
    no_nat_indexed_zero_enumeration_for_exp  -- exp has no zeros at all

`Complex.exp` satisfies every hypothesis and cannot satisfy the conclusion,
because an `N`-indexed enumeration cannot express "finitely many zeros", let
alone none. So the sorry could never have been closed. It could only ever have
been used to derive anything at all — and it was wired into QOU.lean's transitive
imports, so anything downstream that touched it inherited that.

REPAIRED. The index type is now existentially quantified,
`exists (iota : Type) (_ : Countable iota) (a : iota -> C)`, so `iota = Empty`
covers the zero-free case. `hadamard_factorization_statement_satisfiable_for_exp`
checks — sorry-free — that the repaired statement IS satisfiable in exactly the
case that refuted the old one. That is a regression test, not a restatement.

The sorry remains, on a statement that is now at least true.

WHY THIS WENT UNNOTICED. The file's own docstring argued, correctly, that the
product equation forces the enumeration to be COMPLETE (no zero of f can be
missing, and multiplicities must match). That defence survives the roast. What
nobody checked was the opposite direction: whether the enumeration could be
forced to be NON-EMPTY when f has no zeros. The docstring's "honest,
non-vacuous" note reasoned about one failure mode and read as if it had covered
both.

LESSON, and it is the same one twice in this session: a statement can be
carefully defended against the failure mode you thought of and still be false.
The cheap check is to instantiate at the simplest object in scope — here `exp`,
which took two lines.

Sorry accounting for this file: 3 -> 2 (PI-2, 2026-08-07) -> 1 (PI-3,
2026-08-08) -> 1, but now on a TRUE statement.

---

## 2026-08-08 (final pass) — THE MOTIVATION IS RETRACTED. This chain has no consumer.

Chasing "does the minimality principle survive restatement about the halves?"
answered a different and more useful question: it does not need to.

`QOU/MathlibExt/DoublyPeriodicLiouville.lean` is SORRY-FREE and already reduces
`PentagonRigidity.uniqueUpToScalar` to two smaller named inputs — `hratio`
(bean qou-cons) and `hibinv` (bean qou-rp5f) — with the doubly-periodic =>
constant Liouville step PROVED (`const_of_doublyPeriodic`,
`ratio_const_of_doublyPeriodic`). Bean qou-lv34 (in-progress) calls that route
"the only honest route to A_omega=3".

NEITHER remaining input is Hadamard factorization, and neither is made easier by
having it. Finishing PI-4/PI-5 would not discharge uniqueUpToScalar.

WORSE: that same sibling file already stated, in prose, that Phi_b "is
meromorphic with a genuine zero/pole lattice (poles at c_b + i(mb + nb^-1), zeros
at the reflected lattice), so the bridge as stated does not apply to it directly
— a hypothesis/application mismatch worth naming rather than working around."
It named the mismatch BEFORE this chain was written. This chain's docstring
asserted the opposite and defined IsEntireOfOrderLE to carry it.

So my HadamardApplicability finding (an explicit vanishing point of the phiBProd
denominator factor) is a machine-checked instance of something route B had
already said. What is new is only its consequence for THIS file's hypothesis.

WHAT IS NOT RETRACTED — the bricks are good and stay:
  PI-2  WeierstrassFactorEstimate         sorry-free
  PI-3  multipliable_canonicalProduct     sorry-free
        BorelCaratheodory                 sorry-free (qou-8cwi)
        differentiable_tprod_one_add and the two halves   sorry-free
All correct, all Mathlib-gap-shaped, all reusable. They have NO CURRENT CONSUMER.

ACTION: do not resume PI-4/PI-5 on the current justification. Put effort on
qou-cons and qou-rp5f. If canonical products are wanted for some other target,
name that target first — the current one does not hold.

Audit: docs/audits/2026-08-08-hadamard-vs-liouville-route.md

<!-- 2026-08-08T07:40:00Z branch claude/dg-scope-correction -->
