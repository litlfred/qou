---
# qou-cons
title: 'T2: hratio — prove entireness of Φ₁/Φ₂ ratio (divisor cancellation: two FaddeevPhi solutions share zero/pole lattice)'
status: in-progress
pr: 8224
updated_at: 2026-11-17T06:27:22Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T14:57:31Z
updated_at: 2026-10-04T15:24:43Z
parent: qou-r9ih
---


## 2026-08-08 — NOT PROVABLE AS STATED. The class has no regularity field.

After qou-rp5f was reduced to this bean, `hratio` is the single remaining input
to uniqueUpToScalar. It cannot be derived from `FaddeevPhi b Phi` and
`FaddeevPhi b Psi`.

`FaddeevPhi` has exactly three fields — `hb`, `shift_b`, `shift_binv` — and NONE
asks for holomorphy, continuity, or even measurability. So the solution set is
closed under multiplication by ANY doubly-periodic function, however bad.
Sorry-free in `QOU/Mathlib/FaddeevSolutionSet.lean`:

    faddeevPhi_mul_periodic          FaddeevPhi Phi + E periodic under ib and i/b
                                     => FaddeevPhi (Phi * E)
    latticeIndicator                 the indicator of Z.ib + Z.(i/b)
    latticeIndicator_periodic_b/binv doubly periodic, values in {0,1}
    faddeevPhi_mul_latticeIndicator  the witness: Phi * latticeIndicator is
                                     another FaddeevPhi solution

Both shift axioms carry a prefactor that does not see E, and the half-shifts
+-ib/2 differ by exactly the period ib — so E cancels. Pure algebra, no analysis.

WHY THIS IS THE RIGHT DIAGNOSIS, not a technicality: the classical solution set
is Phi_b * {ELLIPTIC}, and "elliptic" carries the regularity that makes the ratio
meromorphic. Strip regularity from the class and "elliptic" degrades to "doubly
periodic", which is far too big. DoublyPeriodicLiouville.const_of_doublyPeriodic
is precisely the statement that DIFFERENTIABILITY closes that gap — the missing
hypothesis is exactly the one the class lacks.

TWO HONEST ROUTES, pick one:
  (a) add a regularity field to FaddeevPhi (meromorphy) and re-derive the divisor
      statement from the shift equations; or
  (b) keep the class and carry hratio as a hypothesis about the specific pair —
      which is what ratio_const_of_entire_ratio already does.

What is NOT available is proving this bean from what is currently there. Anyone
who tries using only the three class fields is wasting the attempt.

Status left todo: the bean is real work, but its statement needs fixing first.

## 2026-08-08 (later) — AND THE REDUCTION IS CIRCULAR. hratio IS the theorem.

Beyond being unprovable from the class, `hratio` is not a sub-problem at all.
Proved sorry-free in `QOU/Mathlib/RigidityReductionScope.lean`:

    hratio_iff_conclusion (hper) :
      Differentiable C (fun z => Psi z / Phi z)  <->  exists c, forall z, Psi z / Phi z = c

Forward is `ratio_const_of_entire_ratio`; backward is that a constant is
differentiable. Given `hper` — which IS smaller, and is now discharged
(qou-rp5f / FaddeevRatioPeriodic) — the hypothesis `hratio` and the conclusion
`uniqueUpToScalar` are the SAME STATEMENT. Classically: the ratio is elliptic,
and an elliptic function is entire exactly when it is constant.

So the advertised reduction

    uniqueUpToScalar  <==  hratio (qou-cons) + hper (qou-rp5f)

has one real edge (hper, done) and one identity edge. Anyone who "proves this
bean" has proved uniqueUpToScalar outright, using an input that is nowhere in the
current chain.

WHAT THE MISSING INPUT IS. FaddeevSolutionSet shows the solution set absorbs any
doubly-periodic factor, so the functional equations ALONE cannot pin a solution
up to scalar; with regularity that becomes "elliptic", and non-constant elliptic
functions exist. An extra condition is MANDATORY: a growth bound, a minimality
principle, or a pinned divisor.

THIS PARTIALLY REHABILITATES THE HADAMARD DIRECTION (qou-v4if). Its retracted
motivation — "phiBProd is selected among its elliptic multiples by a
growth/minimality principle" — was reaching for exactly this mandatory input, and
was RIGHT that one is needed. What was wrong was aiming Hadamard at phiBProd,
which is not entire. A growth argument aimed at the two entire HALVES, or at a
pinned divisor, is still a live candidate — a much smaller claim than the one
retracted, and proved nowhere yet.

RESTATE THIS BEAN before working it. As written it is the theorem, not a step.

---

## 2026-08-08 — RESTATED. The bean is now "supply the selection principle".

The two notes above diagnose this correctly and both end by saying the statement
must change before anyone works it. Here is the changed statement.

**OLD (do not work):** *prove `hratio` — that `Ψ/Φ` is entire.* Dead twice over:
unprovable from `FaddeevPhi`'s three fields (no regularity), and — given `hper`
— identical to the conclusion (`RigidityReductionScope.hratio_iff_conclusion`).

**NEW:** *supply the hypothesis that selects `Φ_b` from `Φ_b · {elliptic}`, in the
divisor-plus-order form, and close the argument with the bricks already proved.*

### The route, with every existing piece named

`phiBProd b z = (∏' numFactor b z k) / (∏' denFactor b z k)`
(`QOU.MathlibExt.PhiBProd`) — a ratio of two entire products. `phiBProd` itself
is NOT entire (`QOU.Mathlib.HadamardApplicability.denFactor_eq_zero` exhibits a
denominator zero), which is what killed the previous aim. **Its halves are**, and
that is proved: `differentiable_numProd`, `differentiable_denProd`.

So write a competing solution the same way, `Ψ = N_Ψ / D_Ψ`, and assume:

    H1  same divisor : N_Ψ and N_Φ share their zeros with multiplicity,
                       and likewise D_Ψ and D_Φ
    H2  finite order : all four are entire of order ≤ ρ

Then Hadamard factorization applied to each pair — to the HALVES, which are
entire, not to `phiBProd`, which is not — gives

    N_Ψ = N_Φ · e^g ,   D_Ψ = D_Φ · e^h ,   g, h polynomials of degree ≤ ρ

whence

    Ψ/Φ = e^(g−h)      entire, and nowhere zero.

Now `hper` closes it with nothing further assumed. `Ψ/Φ` is doubly periodic
(`QOU.Mathlib.FaddeevRatioPeriodic.ratio_periodic_b` / `ratio_periodic_binv`,
both sorry-free, bean qou-rp5f, discharged), so
`DoublyPeriodicLiouville.const_of_doublyPeriodic` applies directly to `e^(g−h)`
— it is differentiable and doubly periodic, so it is constant. No auxiliary
"`e^p` periodic ⇒ `p` constant" lemma is needed; the general Liouville statement
already covers it.

    uniqueUpToScalar  ⟸  H1 + H2  +  hper (done)  +  Hadamard-on-the-halves

**Why this is a real reduction and the old one was not.** H1/H2 are hypotheses
about the COMPETING solution's divisor and growth. They are not restatements of
the conclusion: a doubly-periodic multiplier `E` with `Φ·E` still a `FaddeevPhi`
solution (`FaddeevSolutionSet.faddeevPhi_mul_latticeIndicator` constructs one)
generally violates H1 — multiplying by `E` moves zeros. That is exactly the
class of counterexample the bean's own diagnosis says must be excluded, and
H1/H2 exclude it by naming the divisor rather than by assuming the answer.

### This gives the Hadamard bricks their consumer back

`qou-v4if`'s motivation was retracted for aiming at `phiBProd`
(`docs/audits/2026-08-08-hadamard-vs-liouville-route.md`), and the audit
recorded the bricks as "good infrastructure with no current consumer". That
second half is now wrong and should be corrected when this is worked:
`WeierstrassFactorEstimate` (PI-2), `multipliable_canonicalProduct` (PI-3) and
`BorelCaratheodory` are exactly what the step above needs. What stays retracted
is the TARGET — Hadamard applies to `numProd`/`denProd`, never to `phiBProd`.

The earlier note already said "a growth argument aimed at the two entire HALVES
… is still a live candidate". This is that argument written down.

### Sub-tasks, in dependency order

1. **T2a** — state H1/H2 in Lean: a structure over a `FaddeevPhi` solution
   carrying the num/den splitting plus divisor equality and an order bound.
   Cheap; no analysis.
2. **T2b** — the closing lemma `H1 + H2 + hper ⇒ ∃ c, ∀ z, Ψ z = c · Φ z`,
   assuming Hadamard as a hypothesis. Also cheap: it is bookkeeping plus
   `const_of_doublyPeriodic`. **Do this before T2c** — it makes the payoff
   real before the expensive part, and it is the step that proves the route
   closes at all.
3. **T2c** — discharge Hadamard for the two halves. This is the genuinely hard
   analytic core (PI-4/PI-5 in `QOU.Mathlib.HadamardFactorization`), and the
   one legitimate reason to work it.

### What is still NOT established

That `Φ_b` itself satisfies H2, i.e. that `numProd`/`denProd` have finite order,
and what ρ is. Nothing in the corpus computes it. Until that is settled the
route is conditional on a property of the target, which is a weaker position
than it looks — check it early, because if the order is infinite the whole
route dies and only a pinned-divisor argument survives.

Status stays `todo`: restated and now workable, not started.

## Progress Update (PR #8224)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8224` at `9725d15463b70fb5b273b6c495db79723640032c`).
- **Lean Formalization**: `QOU.QBeta.FaddeevHalvesSelectionAndQGevreyCauchyEnvelope.faddeev_halves_divisor_cancellation_and_scalar_rigidity` (Divisor cancellation and scalar rigidity for two Faddeev solutions sharing zero/pole lattices.)
- **80-dps Witness**: `computations/probes/faddeev-halves-selection-and-q-gevrey-cauchy-envelope.witness.json` (`scriptHash: cea527e5468d`, `scriptCommitSha: 9d85aecf9640ed04a9fa33fe94c3662500eae503`).
