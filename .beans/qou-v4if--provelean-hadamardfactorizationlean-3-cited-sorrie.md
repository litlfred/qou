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
updated_at: 2026-08-07T18:40:00Z
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
