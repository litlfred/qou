---
# qou-lz235
title: 'The sqrt5 slot is Sigma(2,3,5): read Lawrence-Zagier and place the Bring constant'
status: completed
type: task
priority: high
tags:
    - one-loop
    - c-sigma
    - brings-surface
    - poincare-sphere
    - quantum-modular
    - branched-cover
    - lawrence-zagier
created_at: 2026-08-08T19:55:00Z
updated_at: 2026-08-08T21:10:00Z
---

## The ask

`qou-vdvS` and `qou-vdvK` derived `c_sigma` in closed form wherever the Laplace
saddle sits at a regular ideal polyhedron, and identified the obstruction to
going further as ARITHMETIC: `det(Hessian) = tau_DG` is an algebraic number in
the trace field, and radical expressions appear only for the two exceptional
imaginary quadratic fields `Q(sqrt-3)` and `Q(i)`. On that reading a `sqrt5`
is unavailable, because `Q(zeta_5)` is degree 4.

**That reading answers the wrong question.** The corpus's `sqrt5` was never
going to come from a hyperbolic trace field. It comes from a CYCLIC BRANCHED
COVER, and the arithmetic is the same shape:

    |H_1(Sigma_d(K))| = |Res(Delta_K, (t^d-1)/(t-1))|   -- a norm from Z[zeta_d]

Computed (sympy, this session):

    T_{2,3} trefoil     d=5:  |H_1| = 1   Poincare homology sphere Sigma(2,3,5)
    T_{2,5} cinquefoil  d=2:  |H_1| = 5   lens space L(5,q)
    sum_k zeta_5^{k^2} = sqrt5            the Bring constant, as a Gauss sum

Both knots are the ones `bring-trefoil-cinquefoil-channel` names, and
`klein-bring-icosahedral-bridge` already places `S^3/2I -> S^2(2,3,5)`. The
missing sentence is that the trefoil is the BRANCH LOCUS of that cover, and
`|2I| = 120 = |S_5| = |Aut(Bring)|`.

## What to do

1. **Get and read `lawrence-zagier-1999`** (Asian J. Math 3 (1999) 93-107),
   registered but NOT YET READ — the author's page is egress-blocked here, and
   no arXiv copy was found. It computes the asymptotic expansion of the WRT
   invariant of `Sigma(2,3,5)` as the radial limit of an Eichler integral of a
   half-integral-weight modular form. That is the non-hyperbolic analogue of
   `Q_inf`, and it is where the `sqrt5` in a one-loop constant actually lives.
   `zagier2010` (already registered, full text) is its follow-up.
2. Extract the one-loop constant of `Sigma(2,3,5)` in their normalisation and
   compare it to the `2^{-1/2}` that `k_sq_eq_half_of_saddle` shows is forced in
   the hyperbolic case. **They need not agree** — `Sigma(2,3,5)` is Seifert-
   fibred, `Vol = 0`, and there is no Lobachevsky saddle at all. Establishing
   that they are DIFFERENT constants, arrived at by different mechanisms, is a
   perfectly good outcome and is the more likely one.
3. Only then decide whether anything connects the Bring `sqrt5` to `c_sigma`.

## The trap, stated in advance

`Sigma(2,3,5)` is spherical and the torus knots `T_{2,3}`, `T_{2,5}` have zero
simplicial volume. The colored Jones grows POLYNOMIALLY there, not
exponentially; `c_sigma` as this corpus defines it (`lim |J'_N| N^{-3/2}
e^{-Vol N/2pi}`) is not the same object and the volume conjecture is vacuous.
Writing the Bring `sqrt5` and a hyperbolic `sqrt5` into the paper as one thing
would be a category error. Two `sqrt5`s of cyclotomic origin are not
automatically the same `sqrt5`.

## Definition of done

Lawrence-Zagier read at full text, its `Sigma(2,3,5)` constant recorded in a
witness, and a written verdict on whether it relates to `c_sigma` or is a
separate mechanism that merely shares the field `Q(zeta_5)`.

## Progress 2026-08-08 — two of the three mechanisms are now identified, one is BLOCKED

**Mechanism (3), quantum dimension, is done and it identifies with (1).** The
user supplied Jones, Bull. AMS 12 (1985) 103-111 (now full text at
`library/s0273-0979-1985-15304-2/S0273-0979-1985-15304-2.pdf`; `jones1985` was already registered). At
`r = 5` the Markov trace's quantum dimension is the golden ratio directly,
`[2] = [3] = 2 cos(pi/5) = phi`, and the Bring torus knots evaluate to
golden-ratio algebraic integers:

                       |V(zeta_10)|^2         |V(zeta_5)|^2
    3_1 trefoil        phi^2                  3 - 1/phi
    T_{2,5} cinquefoil 2 + phi  = D^2_{Fib}   phi^{-4}

`2 + phi = 1 + phi^2` is the GLOBAL DIMENSION of the Fibonacci category. So the
Gauss-sum `sqrt5` of `bring-trefoil-cinquefoil-channel` and the Markov-trace
`sqrt5` of Jones are the same `sqrt5` — both `Q(sqrt5) = Q(zeta_5)^+`, entering
through `2 cos(pi/5)`. Probe: `bring_golden_jones_probe.py`, exact radicals,
closed forms asserted before evaluation.

**Mechanism (2) is BLOCKED ON READING in this environment — do not re-attempt
the same way.** `lawrence-zagier-1999` is unavailable:

  * `www.math.huji.ac.il/~ruthel/papers/99mfqinv.html`  -> EGRESS_BLOCKED
  * `people.mpim-bonn.mpg.de/zagier/`                   -> EGRESS_BLOCKED
  * `arxiv.org` (papers that restate the result)        -> EGRESS_BLOCKED

The proxy is an allowlist (`selective: false`, but academic hosts are not in
`noProxy`); `pypi.org` and `registry.npmjs.org` are reachable, journals are not.
WebSearch (Anthropic-side) works and was used to confirm the citation; WebFetch
to these hosts does not. Correct citation, verified by search:

    Lawrence, R. and Zagier, D., "Modular forms and quantum invariants of
    3-manifolds", Asian J. Math. 3 (1999), no. 1, 93-108.
    DOI 10.4310/AJM.1999.v3.n1.a5

(the first registration of this ref said 93-107; corrected to 93-108)

Both are network-policy denials of the remote execution environment, not
transient failures, and must not be routed around. Either run from an
environment whose network policy permits them, or have the PDF uploaded to
`library/` the way `jones1985` was.

**If it stays blocked, compute instead of reading.** `Sigma(2,3,5)` is `-1`
surgery on the trefoil, so its WRT invariant is reachable from the trefoil's
colored Jones by the Reshetikhin-Turaev surgery formula, and its asymptotics can
be extracted numerically exactly as `Q_inf` and `c_sigma(4_1)` were. **Do not
implement a surgery formula from memory** — that is the same failure mode as the
retracted van der Veen premise. Implement it, then SELF-TEST against cases with
known answers (`tau_r(S^3) = 1`; lens-space values are Gauss sums) BEFORE
trusting any Poincare-sphere number. One hook worth checking on arrival: the
Lawrence-Zagier modulus is `q^{n^2/120}` and `4 * 2 * 3 * 5 = 120 = |2I| =
|S_5| = |Aut(Bring)|`.

**The trap in the original ask still stands** and is now sharper: the `c_sigma`
closed forms live in `Q(i)` and `Q(sqrt-3)`, the two exceptional IMAGINARY
quadratic fields. `Q(sqrt5)` is REAL. So a `sqrt5` cannot enter `c_sigma` by the
polyhedral route at all, and any connection would have to be of a different
kind. Expect a separation, not a unification.

## CORRECTION 2026-08-08 — this bean was largely redundant, and I duplicated a reference

Two mistakes, both mine, both recorded rather than quietly fixed.

**1. The corpus already has this.** Before opening this bean I did not check what
`Sigma(2,3,5)` work already exists in-repo. It is extensive and machine-validated:

    computations/lr_modulus_identification_sigma235.py
    computations/probes/keystone_colored_lr_modulus_s013.py
    computations/probes/keystone_valuemap_genuine_smatrix_s013.py
    computations/probes/keystone-colored-sigma235-wrt.witness.json
    computations/deltalambda/deltalambda_icosahedral_smatrix_magnitude_probe.py

including the Hikami odd characters `chi^{(1,1,a)}_{60}`, the genuine S-matrix,
the McKay `2I <-> E8-hat` correspondence, and `sum mark^2 = 120 = |2I|`. It also
already contains `[3]_zeta = [2]_zeta = phi` at `zeta = e^{i pi/5}` — which
`bring_golden_jones_probe.py` REDISCOVERED. That probe's docstring now says so;
its genuinely new content is only the Jones-polynomial evaluations of the two
Bring torus knots and the `jones1985` link.

**2. `lawrence-zagier-1999` was already registered** (correct pages 93-108, DOI,
and a note calling it the "foundation of the Sigma(2,3,5) keystone false-theta
machinery"). I registered a second copy. Removed; the one new fact — that every
host is egress-blocked here, and that `hikami2005brieskorn` restates the result
— was merged into the surviving entry. This is the SECOND duplicate reference I
have created in this session (the first was `ohtsuki-takata-2015`). The lesson is
mechanical: **grep `references.ts` for the id AND the title before adding, and
grep `computations/` for the topic before opening a bean.**

**The reading block is moot.** `hikami2005brieskorn` is already in `library/`
(`0405028v2.pdf`) and contains the Poincare-sphere result as its **Theorem 10**,
attributed to Lawrence-Zagier, plus the generalisation to all
`Sigma(p1,p2,p3)` and — section 6 — the identification of the S-matrix with the
**Reidemeister torsion**. So no retrieval is needed. Corollary 11 gives

    tau_N(Sigma(p)) ~ sqrt(N/i) sum_l S_l e^{-(i/2) pi P N (1 + sum l_j/p_j)^2} + tail

with `S_l` the torsion, a `sqrt(N)` prefactor (not `N^{3/2}`), and the exponential
a PHASE only since `Vol = 0`. The `sqrt5` appears in exactly the slot the
c_sigma law's `|tau|^{-1/2}` occupies — e.g. `1/sqrt5` for `Sigma(3,4,5)`,
`2/sqrt7` for `Sigma(2,3,7)`. Note `Sigma(2,3,5)` is the exceptional case
`sum 1/p_j > 1` (spherical), handled separately by Theorem 10.

## What is actually left

Not "read Lawrence-Zagier". Rather: **is the Hikami torsion `S_l` for
`Sigma(2,3,5)` related to the hyperbolic `c_sigma = k |tau_DG|^{-1/2}`, or is it
a parallel structure sharing only the field?** The N-powers differ
(`sqrt N` vs `N^{3/2}`), the exponential is a phase rather than a volume, and
`Q(sqrt5)` is REAL where the hyperbolic closed forms live in the imaginary
quadratics `Q(i)` and `Q(sqrt-3)`. Expect a separation. Before any further work,
READ the five in-repo files above — the answer may already be there.

## Resolution — the three mechanisms are separated, and the verdict is PARALLEL

(1) Gauss sum and (3) quantum dimension are the SAME sqrt5: both are
`Q(sqrt5) = Q(zeta_5)^+` entering through `2 cos(pi/5) = phi`.

(2) The branched cover to `Sigma(2,3,5)` is a **parallel structure, not the same
law**, and it was never blocked — `hikami2005brieskorn` was already in
`library/`. His Corollary 11 gives

    tau_N(Sigma(p)) ~ sqrt(N/i) sum_l S_l e^{-(i/2) pi P N (1+sum l_j/p_j)^2} + tail

with `S_l` the Reidemeister torsion (his section 6). Compare:

                  c_sigma (hyperbolic)          S_l (Seifert)
    manifold      cusped complement, Vol > 0    closed, Vol = 0
    invariant     colored Jones of a knot       WRT of a 3-manifold
    N-power       N^{3/2}                       sqrt(N)
    exponential   growth e^{Vol N/2pi}          pure phase
    field         Q(i), Q(sqrt-3)  (imaginary)  Q(sqrt5)  (real)
    constant      k = 2^{-1/2}                  sqrt2 (folded-MTC normalizer)
    forced by     the Gaussian saddle           the 2:1 fold D_E8^2 = 2 D_MTC^2

Both constants are FORCED, by different mechanisms. They share `Q(sqrt5)` by
cyclotomy, not by mechanism. Expect no unification, and do not write one.

## The one new thing: the cinquefoil joins the keystone tower

    |V(T_{2,5})(zeta_10)|^2 = D_Fib^2 = D_SU(2)_3^2 / 2 = D_E8hat^2 / 4 = (5+sqrt5)/2

so the Bring chapter's `zeta_5` carrier sits exactly at the bottom of the
dimension tower `lr_modulus_identification_sigma235.py` already builds. That
links the torus-knot Jones values to the keystone instead of leaving them a
separate coincidence.

Lean, sorry-free: `golden_quantum_dimension` ([2] = 2cos(pi/5) = phi, from
Mathlib's `Real.cos_pi_div_five` — the tower's input is a theorem, not a table),
`keystone_dimension_tower` (D_SU2^2 = 2 D_Fib^2 and D_E8hat^2 = 4 D_Fib^2, for
EVERY phi — the ratios come from the mark multiset, not from sqrt5),
`marks_sq_sum_eq_120` (by `decide`, axioms [propext] only),
`keystone_core_identity` ((10-2sqrt5)(10+2sqrt5) = 80),
`cinquefoil_value_is_fib_dimension`.

Probe: `bring_golden_jones_probe.py`, 4/4.
