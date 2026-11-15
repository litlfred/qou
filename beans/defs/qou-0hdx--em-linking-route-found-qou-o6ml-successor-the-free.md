---
# qou-0hdx
title: 'EM-linking ROUTE FOUND (qou-o6ml successor): the Freedman-He ASYMPTOTIC CROSSING NUMBER clears every obstruction — symmetric in the pair (a norm, so O1-proof), nonzero when lk=0 (unsigned, so Brunnian-proof), Flux^2 scaling (not Flux^3), and carries an explicit Vol^{-1/3} geometric factor (Khesin Thm 3.6 = Freedman-He). CONVERGENCE: Vol^{-1/3} = A^{-1/3} is exactly the ''1/kappa null'' that tied H_coth in em-linking-coth-separation.witness.json — so that ''null'' has independent literature backing. Next: derive the per-PAIR crossing-number energy (Thm 3.6 as stated is single-tube and vacuous for unknot components) and test against kappa(A)'
status: scrapped
type: task
priority: normal
created_at: 2026-08-01T20:49:51Z
updated_at: 2026-09-02T21:41:15Z
---

## SCRAPPED 2026-09-02 — the route's two distinguishing claims are FALSE, verified against the primary source

This bean was `todo` with `updated_at == created_at` (2026-08-01T20:49:51Z) for a
month while the audit trail refuted it. **Its title is the artifact carrying the
false claims**, and a title is what the next agent greps, so it is scrapped rather
than left standing. Nothing here deletes a finding: the numerical work survives and
is named below.

### What the title claims, and what is actually true

The title asserts four clearances. **Two survive; two are false**, and the two false
ones are exactly the ones that made this route look better than route (2).

| title claim | verdict |
|---|---|
| symmetric in the pair (a norm, so O1-proof) | **holds** |
| nonzero when lk = 0 (unsigned, so Brunnian-proof) | **holds** |
| "carries an explicit `Vol^{-1/3}` geometric factor (Khesin Thm 3.6 = Freedman–He)" | **FALSE** |
| "CONVERGENCE: `Vol^{-1/3} = A^{-1/3}` is exactly the '1/kappa null' … so that 'null' has independent literature backing" | **RETRACTED** — it rests on the above |

And the title's stated next step — *"derive the per-PAIR crossing-number energy"* —
is **malformed**: no pair-indexed object exists in either source.

### Verified against the primary source, not taken on a prior agent's word

`library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:203-216` (Komendarczyk,
arXiv:0808.1533v1, p. 26) states the Freedman–He link bound verbatim as

    E_{3/2}(X) >= (pi/16)^{1/4} ( sum_{k=1}^{n} ac(L_k, L)|Flux(X_k)| ) * min_{1<=k<=n}{|Flux(X_k)|}   (43)

Three things read straight off it:

1. **The index is `ac(L_k, L)` — one component against the WHOLE link — and the sum
   runs over the `n` components, not the `n(n-1)/2` pairs.** There is no
   `ac(L_i, L_j)` anywhere in Komendarczyk or Khesin; Khesin never writes `ac(.,.)`
   at all, and his Rmk 3.5 "minimising over all homotopies of two given space
   curves" is a survey gloss on the two-curve warm-up, not the invariant in (43).
2. **The constant is `(pi/16)^{1/4}` — pure, with NO volume factor.** The
   `Vol^{-1/3}` this bean calls "the Freedman–He template" is **Khesin Thm 3.6**,
   the bound for a *single knotted torus*, misapplied to a multi-component
   configuration. So the "convergence" with the `A^{-1/3}` κ-null was never two
   independent routes — it was one route and a misattribution.
3. The genus step is real but weaker than used: (43)'s `ac(L_k, L)` "can be
   estimated below by a smallest genus among surfaces in `R^3 \ {L_1 ∪ … ∪ L̂_k ∪ …
   ∪ L_n}` with a single boundary component" — a complement-constrained
   *single-component* genus, not a constrained pair homotopy.

All three confirm Round 5 of
[`docs/audits/2026-08-01-em-linking-reads-round1.md`](docs/audits/2026-08-01-em-linking-reads-round1.md)
(written 2026-08-08) and `computations/em-linking-fh-link-bound-correction.witness.json`.
That audit flagged FH 1991 itself as absent from `library/`; it still is, but
Komendarczyk's statement of the bound **is** held and is unambiguous on both points,
so the residual gap does not touch either correction.

### The question this bean was reopened to answer

*Does the asymptotic-crossing-number route need a per-nucleus carrier link type, or
does it take the divergence-free field directly?* — the hope being that it sidesteps
the blocker that ended route (2) (`qou-o6ml`: carriers exist only at A=3, and
`qou-5vhf` establishes the A<=4 assignments are an admitted AME-driven census
search, so route (2) fails o6ml's own no-tuned-constant gate).

**Answer: it needs the carrier, unavoidably.** Eq. (43) is indexed on
`L = {L_1,…,L_n}`, an n-component link in `R^3`, and `ac(L_k, L)` is a topological
invariant *of that link*. Evaluating it for a nucleus requires first saying which
link the nucleus is. That is the same carrier assignment, so **route (2)'s blocker
applies here verbatim** — and on top of it, this route's distinguishing advantage
was already retracted a month ago.

### Scope of the refutation — (a), not (b)

Per the refutation-scoping rule this is a **scope-(a)** result on the route as this
bean states it, with one **scope-(b)** component:

- **scope-(b), structural:** the *pair-indexed* formulation does not exist. That is
  a verified fact about the two sources, not a numerical failure, and it will not
  become true later.
- **scope-(a):** eq. (43) is a real theorem and a real lower bound. What is dead is
  this bean's route to it. What survives is a correctly-indexed component-vs-link
  bound whose topological factor is **A-independent** for a fixed local Borromean
  configuration — so it does not explain κ(A), it *relocates* the explanation into
  the flux: κ falls by 2.099 across A = 3…41, which needs the per-component flux to
  fall by 1.449 over the same range. Derivable in principle, **not derived**, nothing
  wired.

### What survives, and where

- `computations/em-linking-fh-link-bound-correction.witness.json` — the correctly
  indexed object: `1 <= ac(L_k, L) <= 3.285` per component, `3 <= sum_k <= 9.856`,
  upper end realisation-dependent at 7.8%.
- `computations/em-linking-borromean-acn.witness.json` — the Gauss-integral ACN
  machinery is sound (signed control vanishes at 4.55e-32, Brunnian; quadrature
  converged to 7.16e-22). Its *object* is the wrong index and the wrong sum, so
  `ACN_pair = 1.6426` and the "total link" reading `3 x that = 4.928` answer nothing.
- `computations/em-linking-crossing-number.witness.json` — the `Vol^{-1/3}` fit. Its
  two assertions still pass, but they now test a template with **no literature
  backing**: `H_FH_A` and `H_FH_Z` revert to bare power laws.

### Successors

- **Live question**, if anyone takes it: derive the per-component flux law from the
  corpus braid geometry. It is the whole remaining obligation, and it is independent
  of crossing numbers.
- `qou-8aed` is **unanswerable as posed** and is scrapped alongside this one: it asks
  *which* volume enters the `Vol^{-1/3}` template, and there is no such template.
- `qou-a9li` / `qou-b5yi` were the (a)-vs-(b) minimisation crux. Both are `completed`
  with **empty bodies** — their answer existed nowhere but the audit doc. Backfilled
  in this same commit.

### Process note — this is the trap corpus-grep path 6 exists for

I recommended reopening this bean on the strength of its title and its `todo` status,
having checked neither `computations/` (path 3) nor the beans it spawned (path 6).
Path 3 held three witnesses on it and path 6 held two `completed` crux beans. **A
bean's status is not a claim about the corpus**, and `updated_at == created_at` on a
month-old bean is a reason to distrust its title, not to trust it.
