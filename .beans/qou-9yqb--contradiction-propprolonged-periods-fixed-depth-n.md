---
# qou-9yqb
title: 'CONTRADICTION: prop:prolonged-periods-fixed-depth (n-independent kernel) is inconsistent with a_D^(n)=I(n)/n growing super-exponentially — at most one holds'
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:16:24Z
updated_at: 2026-08-30T07:48:22Z
parent: qou-mhj9
---

VERIFIED against primary sources 2026-08-30 (not from a sibling's prose).

## The two claims

(1) prop:prolonged-periods-fixed-depth (content/.../mass-theory/), verbatim:
    "a_D^(n+d) = SUM_{j<d} c_j a_D^(n+j), with **n-independent** kernel c, for
    every n", d <= rank V <= 2g = 8, derived by Cayley-Hamilton on the
    jet-prolongation operator M acting on the Gauss-Manin period space V.

(2) PR #6052 branch claude/arithmetic-upgrade-pending-543abd,
    QOU/Mass/SWPeriodSuperExponential.lean (sorry-free):
      involution_ratio_unbounded    -- I leaves EVERY geometric class
      factorial_le_involution_two_mul -- n! <= I(2n)
      classical_period_ratio_unbounded
    reading a_D^(n)|_{q=1} = lw(n-1) = I(n)/n via prop:sw-classical-jet-exactness.

## Why they cannot both hold

A linear recurrence with CONSTANT coefficients has solutions
SUM_i p_i(n)*lambda_i^n -- at most exponential growth. Elementary form:
|a_{n+d}| <= (SUM_j |c_j|) * max_{j<d} |a_{n+j}| gives |a_n| <= M*K^n with
K = max(1, SUM|c_j|). Super-exponential growth (ratio unbounded) contradicts it.

THE TELL IS IN THEIR OWN LOAD-BEARING STEP. involution_succ_succ reads

    I(n+2) = I(n+1) + (n+1)*I(n)

-- a depth-2 recurrence whose coefficient (n+1) is n-DEPENDENT, which is exactly
what (1) forbids. The n-dependence is sitting in the coefficient, in plain view.

## What must give (one of)

  a. the identification a_D^(n) = I(n)/n (prop:sw-classical-jet-exactness); or
  b. a_D^(n) = phi(M^n v_0) for a FIXED finite-rank M (prop:mi-sw-abelianisation)
     -- if the periods grow super-exponentially they cannot be the orbit of a
     fixed finite-rank operator, whatever V's rank; or
  c. the "n-independent" in (1).

## Status of each side

(2)'s ARITHMETIC is solid and elementary: involution_ratio_unbounded follows from
the recurrence by omega. But (2)'s IDENTIFICATION is not proved -- their own
docstring says Sum_{lam|-n} f^lam = I(n) (RSK) "is open in the corpus", beans
qou-m3xr and qou-jlam, both todo, both blocked on the missing Mathlib
StandardYoungTableau layer. So route (a) is the cheapest suspect BY THEIR OWN
SCOPE NOTE, not by my preference.

## Relation to what already landed

Merged #6059 QOU/MassTheory/BodyOrderRecurrenceDepth.no_equivariant_prolongation
already recorded that something in this cluster must give, via a DIFFERENT route
(Schur on H1(Bring) = W_(4,1)^+2 forces d <= 2 against a proved d >= 3). This is
a SECOND independent crack in the same proposition, arrived at from growth rather
than from equivariance. Two independent routes now say the fixed-depth picture is
in trouble.

## Next unit (cheap, Lean)

Formalize the elementary exponential bound
  |a_n| <= M * K^n  for any depth-d constant-kernel recurrence
and pair it with a super-exponential hypothesis to give False. That converts this
bean from an argument into a machine-checked incompatibility. It does NOT decide
which of (a)/(b)/(c) is wrong -- that is a corpus judgement.

NOT MINE TO RESOLVE: (2) belongs to #6052. Flagged to them on that PR
(issuecomment-5466412367); they were told explicitly I had not read their Lean at
the time. This bean records the verification I have since done.


## LANDED + a CORRECTION TO MY OWN ARGUMENT (2026-08-30)

> **SUPERSEDED 2026-08-30 (PR #6088, Copilot review) — the artifacts named in
> this block DO NOT EXIST.** `QOU/MassTheory/FixedDepthGrowthBound.lean` and its
> `abs_le_geometric` / `not_factorial_growth` were DELETED, not merged — see the
> two sections below. The live artifacts are:
>
> | result | lives in | declarations |
> |---|---|---|
> | constant-kernel recurrence => geometric bound; no super-exponential solution | `QOU/Mass/ConstantKernelGrowthBound.lean` | `exists_exponential_bound`, `not_isConstKernelRec_of_superExponential`, `not_superExponential_of_isConstKernelRec` |
> | factorial => super-exponential (the bridge #6101 withdrew) | `QOU/MassTheory/FactorialSuperExponential.lean` | `superExponential_of_factorial_le`, `not_isConstKernelRec_of_factorial_le` |
>
> The block below is kept as the record of what was built and of the correction
> it carries; it is not a pointer to live code.

Lean: QOU/MassTheory/FixedDepthGrowthBound.lean, sorry-free, lean-direct exit 0,
#print axioms clean on both decls.

  abs_le_geometric   -- a depth-d constant-kernel recurrence obeys
                        |a n| <= M * K^n, K >= max(1, sum|c_j|), M bounds the
                        d initial terms. Elementary strong induction.
  not_factorial_growth -- no such sequence satisfies n! <= a(2n) for all n.
                        Via Real.summable_pow_div_factorial: (K^2)^n / n! is
                        summable so its terms -> 0, and the factorial outruns
                        every geometric.

### CORRECTION — the ratio form does NOT contradict the bound

The original body above says the contradiction is with "involution_ratio_unbounded
-- I leaves every geometric class". THAT IS TOO QUICK AND IS WRONG AS STATED.

A geometric UPPER bound does not by itself forbid unbounded two-step ratios: a
sequence may dip far below K^n at some n and jump back, making a(n+2)/a(n)
arbitrarily large while never exceeding M*K^n. Excluding that needs a LOWER bound
as well, which the ratio statement alone does not supply.

The FACTORIAL statement (factorial_le_involution_two_mul : n! <= I(2n)) IS a
genuine lower bound and does contradict the geometric one. So the incompatibility
is real, but it rests on the factorial bound, NOT on the ratio bound. The Lean
proves the version that survives.

This matters for what to tell #6052: the load-bearing half of their file, for
this purpose, is factorial_le_involution_two_mul -- not involution_ratio_unbounded.

### What is still NOT settled

Which premise is false. One of: the identification a_D^(n) = I(n)/n; that
a_D^(n) = phi(M^n v_0) for a FIXED finite-rank M; or the n-independence of the
kernel. Note I(n+2) = I(n+1) + (n+1)I(n) is depth 2 with an n-DEPENDENT
coefficient, consistent with everything here and inconsistent with the
proposition. Corpus judgement, not mine to make unilaterally.


## SUPERSEDED ON MAIN 2026-08-30 — #6101 landed a stronger version

My FixedDepthGrowthBound.lean was DELETED rather than merged. #6101 (merged
06:42) landed QOU/Mass/ConstantKernelGrowthBound.lean:
  exists_exponential_bound
  not_isConstKernelRec_of_superExponential
  not_superExponential_of_isConstKernelRec

Theirs is strictly more general: it quantifies over a SuperExponential predicate
rather than my factorial instance (n! <= a(2n)), and proves BOTH directions.
Landing mine would have put a second copy of a general result into the corpus
behind a weaker hypothesis -- the #3594 duplication class.

The FINDING is unchanged and is now on main. The correction recorded above --
that the contradiction rests on the factorial lower bound and NOT on
involution_ratio_unbounded -- still stands and is still mine; #6101's own
writeup reaches the same "does not decide which side gives" conclusion, and
independently names the identification a_D^(n) = I(n)/n as the cheapest suspect.

Coordination note: I flagged the duplicate to them at 04:24 on #6088 (their
qou-9nt7). They had already written it. Flagging worked in the sense that the
overlap is now visible and adjudicated; it did not arrive in time to prevent it.


## CORRECTION TO MY OWN DEDUP DECISION 2026-08-30

I deleted FixedDepthGrowthBound.lean as "subsumed by #6101's more general
version". That was too quick, and #6101's own comments (issuecomment-5467079264,
-5467208270) are what corrected it:

  * They offered me priority -- mine landed ~40 min before theirs.
  * Their ONLY increment is the SuperExponential PREDICATE over my factorial
    instance.
  * AND THEY WITHDREW THE BRIDGE. They tried factorial => SuperExponential,
    mis-indexed M*K^n at 2n, could not find the Mathlib limit lemma
    (tendsto_pow_div_factorial_atTop does not exist under that name in this
    toolchain), and stopped rather than half-prove it -- correctly, and they
    recorded it in their docstring rather than leaving a sorry.

So their generality is UNUSABLE against the corpus's actual growth statement.
SWPeriodSuperExponential.factorial_le_involution_two_mul gives n! <= I(2n), a
factorial bound on the even subsequence; without the bridge,
not_isConstKernelRec_of_superExponential cannot be applied to it. Verified by
git grep on main: no summable_pow_div_factorial, no factorial/SuperExponential
bridge anywhere in .lean.

RESOLVED by supplying the bridge, not by restoring my file:
QOU/MassTheory/FactorialSuperExponential.lean (sorry-free, axioms clean)
  superExponential_of_factorial_le      -- against THEIR SuperExponential
  not_isConstKernelRec_of_factorial_le  -- composition with THEIR theorem

The limit input is Real.summable_pow_div_factorial (summable => terms -> 0),
which is the lemma they could not locate. Indexing at 2n is what makes it hold
for EVERY real K including negative: K^(2n) = (K^2)^n >= 0.

Net: one home for the general result (theirs), one home for the bridge (mine),
no duplicate. The deletion of my file stands; the deletion of the FINDING it
carried would have been wrong, and nearly happened.
