---
# qou-17mq
title: 'EM-linking O2 (neutrality obstruction): on a COMPACT quotient int(Laplacian u)=0 forces total charge zero — ''two like charges alone'' is NOT admissible as stated; the Green''s fn acquires a -1/vol(M) offset. Re-pose the two-like-charge invariant relative to a neutralizing background (only charge-neutral combinations well-posed; physically the nucleus IS neutral). Blocks/reshapes the STATEMENT of qou-o6ml, not just its solution'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T20:31:20Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-10v9
---

## WORKED 2026-08-25 — O2 applied; it excludes the contest's winner

Probe: computations/em_linking_o2_neutralised_kernel_probe.py
Witness: em-linking-o2-neutralised-kernel.witness.json (4 assertions, pass)
Audit: docs/audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md

O2 had never been applied to anything: neutralis*/neutraliz* appears at 4
sites corpus-wide, all in the round-1 audit, 0 in computations/.

STRUCTURAL (no data): a zero-mean kernel that is not identically zero must
take BOTH SIGNS. coth(alpha) is strictly positive and monotone. So no
admissible kernel saturates at kappa -> +1 — and saturation is exactly what
separated H_coth from its rivals in the mirror-series contest. The
unsubtracted coth is outside the admissible family. Finite volume suffices
(covers the cusped complements 4_1, L6a4), so this does not rest on the
compactness premise.

NUMERICAL (same 29-pair series, same statistic):
  c0 = 0 (inadmissible)  3.505%  r_vs_A +0.049   <- committed incumbent, reproduced to <1e-6
  c0 = 1 (boundary)     11.15%   r_vs_A -0.904
  c0 = 2               15.27%
  c0 = 7.5             22.32%
Monotone in c0 — every step toward genuine neutralisation is worse, and the
best member is the infinite-volume BOUNDARY, not an interior optimum.
48/140 scanned members predict a kappa zero-crossing inside A in [3,63],
contradicted outright by kappa > 1 throughout (min 1.4127).

The r = -0.904 is the sharpest part: em-linking-residual-structure rejected
H_FH_Z for r = +0.799. The admissible kernel carries MORE structure than the
hypothesis rejected for carrying structure.

SCOPE: (b) exclusion of the kernel AS WRITTEN, invariant cited (int(Laplacian
u) = 0). (a) scope-limited negative on the parameterisation. The metric
Coulomb route <A_1, J_2> SURVIVES — nothing here excludes it, nothing wired.

NET FOR qou-o6ml: round 5 withdrew the two H_FH warrants; this removes the
third from the admissible family. No member of that contest carried a live
structural warrant when scored. 4-B stays rank 1 and stays open.

NEXT (sharpened, needs no literature): compute the zero-mean Green's function
of an actual finite-volume quotient rather than the one-term stand-in
coth - c0. Either it fits kappa(A) or no admissible kernel does — and the
second outcome moves 4-B from 'route identified' to 'route excluded'.

CARRIED: qou-gcmn (B_pp frozen at A=3) bounds every scatter number here. The
structural half involves no data and is unaffected.

## ADDENDUM 2026-08-25 — the discrimination test could not discriminate

Probe: computations/em_linking_kappa_regime_reachability_probe.py
Witness: em-linking-kappa-regime-reachability.witness.json (3 assertions, pass)

Prior question nobody asked, computed from the contest's OWN fitted
constants (no new hypothesis, nothing scored, nothing fitted):

  series spans alpha in [0.3165, 0.8732] over A = 3..63
  coth within 10% of limit -> alpha 1.5223 -> A = 334
  within  5% -> A = 606     within 1% -> A = 1764
  heaviest known nuclide      A = 294

SATURATION BEGINS PAST THE END OF THE NUCLEAR CHART. Not 'the test was run
and came out close' — the discriminating regime is unreachable in any
nucleus. qou-i6rg's premise ('needs NO new theory, only more AME data') is
wrong: more data cannot settle it.

Two quantitative corollaries:
 - coth vs its two-term expansion 1/alpha + alpha/3: max dev 0.97% over the
   measured range, against the 3.505% scatter. NOT separable. So H_coth's
   advantage tracks the curvature term alpha^2/3, not saturation. (The
   one-term 1/alpha IS separable at 19.49%, consistent with H_FH_A scoring
   worse — the data resolves the first curvature correction and nothing
   beyond it.)
 - H_coth vs H_FH_Z predictive spread: max 6.285%, mean 3.247% = 1.79x the
   scatter. A gap of order the noise is not a discrimination.

SECOND, O2-INDEPENDENT ROUTE TO THE SAME SUBTRACTION. Radial Laplacian on
H^3 is u'' + 2 coth(r) u', so harmonic solutions off the origin are
-C coth(r) + D. Decay at infinity forces D = C:
    G(r) = -(coth r - 1)/4pi ~ -(1/2pi) e^(-2r)
The DECAYING Green's function of H^3 is already the subtracted one; the
saturating -coth(r)/4pi is the D=0 non-decaying choice. Needs neither
compactness nor finite volume, so independent of O2.
Relatedly (standard, stated not re-derived): finite covolume => delta = 2
and #{d<=R} ~ c e^(2R) cancels the e^(-2R) decay, so the Green's-function
Poincare series diverges — O2 in analytic form.

SCOPE: (a) negative on a TEST, not on a hypothesis. NOT claimed: H_coth
false, power law true, or the metric Coulomb route failing.

NET on 4-B, all three together: the two H_FH warrants withdrawn (round 5);
the winner is not an admissible kernel (O2); and the measurement could not
have separated them anyway (here). The ROUTE is untouched. What is gone is
the belief that its kernel has been identified.

NEXT CHANGES: 'extend the series' is now known futile. Either derive the
kernel (zero-mean Green's fn of an actual finite-volume quotient, PREDICTING
kappa(A) instead of scoring parameterisations against it), or find an
observable probing alpha >= 1.5 — which no nucleus supplies, since
alpha ~ A^(1/3) here.

## THIRD FINDING 2026-08-25 — the separation law is an unexamined Euclidean import

Probe: computations/em_linking_alpha_scaling_provenance_probe.py
Witness: em-linking-alpha-scaling-provenance.witness.json (3 assertions, pass)

Upstream of both earlier findings: they scored KERNELS against kappa(A);
this asks about the SEPARATION LAW every kernel is fed.

em_linking_coth_separation_probe.py caveat (3): 'A^(1/3) was fixed in
advance as the standard nuclear radius law, not selected post hoc.' That
guards against POST-HOC SELECTION — real, worth having — but is not
DERIVATION. And the same file says the kernel has 'NO free parameter --
coth is forced by the Green's function'. So a Euclidean liquid-drop radius
law is fed into a hyperbolic-by-construction kernel: two geometries in one
quantity.

WHAT THE GEOMETRY REQUIRES. In H^3, V(R) = pi(sinh 2R - 2R) ~ (pi/2)e^(2R),
so R ~ (1/2)ln(2V/pi) — LOGARITHMIC. For extensive V ~ A the hyperbolic
separation goes like ln A, not A^(1/3).

SCORED (same series, same statistic):
  3.505%  A^(1/3)   EUCLIDEAN nuclear radius, imported
  6.358%  A^(1/4)
  9.253%  ln A      HYPERBOLIC self-consistent (V ~ A)
  13.95%  A^(1/2)
=> geometric self-consistency costs 2.64x in fit. H_coth's fit quality
depends on the geometric MIXTURE, not the hyperbolic kernel alone.

CORPUS CANNOT ADJUDICATE. binding-link-volumes.witness.json holds link
volumes for A = 2 and 3 ONLY (Hopf 0, 8_11 8.2863, L6a4 7.3277) and its own
description says 'the A-dependence is not in a single binding-link volume'.
No per-isotope hyperbolic geometry beyond A=3 exists, so no alpha(A) law can
currently be DERIVED from framework data.

DEFLATIONARY READING, stated plainly. Free-power diagnostic (one extra DOF,
labelled as such) lands at p = 0.33 at 3.482% vs 3.505% for exactly 1/3 —
indistinguishable. The data INDEPENDENTLY PREFERS the Euclidean exponent.
And pure Coulomb 1/r with a Euclidean radius (= H_FH_A) scores 5.499% vs
coth's 3.505%: the hyperbolic curvature term is worth a factor 1.57 on one
shared parameter. Real, but suggestive not decisive, and comparable to the
qou-gcmn frozen-B_pp confound. With finding 2 (coth within 0.97% of
1/alpha + alpha/3 over this range), the data resolves the first curvature
correction and nothing beyond it.

SCOPE: (a) on an INPUT ASSUMPTION shared by every hypothesis on the front.
NOT claimed: that A^(1/3) is wrong (the data prefers it), that the geometry
is Euclidean, that there is no hyperbolic content, or that H_coth is
refuted.

NET OF ALL THREE. 4-B now carries THREE distinct gaps where the front had
one: the ROUTE is identified, the KERNEL is not, and the SEPARATION LAW is
imported. None refutes the metric Coulomb pairing. What is removed is the
impression that (1) a contest selected a kernel, (2) more data would settle
it, (3) the hyperbolic reading was load-bearing for the fit.


## ROAST 2026-08-30 — two corrections to this bean's own three findings

Both are about **scope and attribution, not about the results**. Every number
below reproduces this bean's published figures before departing from them.

### R1 — finding 2's "A = 334" is conditional on the separation law finding 3 questions, and the bean does not say so

Finding 2 concludes *"SATURATION BEGINS PAST THE END OF THE NUCLEAR CHART"*
flatly. It computes that from `α = c·A^(1/3)` — the **same Euclidean import**
that finding 3, three sections later in this same bean, calls *"an unexamined
Euclidean import"* and *"two geometries in one quantity"*. Finding 3 is
**upstream** of finding 2; the bean's "NET OF ALL THREE" presents them as
independent and cumulative.

Re-measured at `mp.dps = 50`, anchoring `α = 0.8732` at `A = 63` (this bean's
own top-of-span), thresholds `α = arccoth(1.10 / 1.05 / 1.01)`:

| separation law | 10 % | 5 % | 1 % |
|---|---|---|---|
| `A^(1/3)` — Euclidean, as used | **333.8** | 605.7 | 1764.2 |
| `A^(1/4)` | 581.9 | 1288.1 | 5357.4 |
| `ln A` — hyperbolic self-consistent | **1370.3** | 6701.1 | 291119 |
| `A^(1/2)` | **191.5** | 284.9 | 581.0 |

The first row reproduces the bean's `334 / 606 / 1764` exactly, so the method
is the bean's own.

**The conclusion survives where it matters and fails at one member of this
bean's own scanned set.** Under `ln A` — the law finding 3 says the hyperbolic
geometry actually requires — saturation is reached at `A = 1370`, i.e. **the
unreachability is strengthened, not weakened**. But under `A^(1/2)`, one of the
four laws finding 3 itself tabulates, the 10 % regime lands at `A = 191` and
the 5 % regime at `A = 285`, **both inside the chart** (heaviest nuclide
`A = 294`).

So the honest statement is: *unreachable under the law the data prefers and
under the law the geometry demands; reachable under the worst-scoring member
of the bean's own set.* `A^(1/2)` scores 13.95 % against `A^(1/3)`'s 3.505 %,
so this is not a live threat — but that defence is a **fit** argument, and
finding 3's whole point is that the fit and the geometry disagree about which
law is right. A claim that "more data cannot settle it" should not rest
silently on the input the same bean flags as unexamined.

### R2 — finding 1's scope-(b) warrant should be attributed to the decay argument, not to O2

Finding 1 is labelled scope-(b) citing the invariant `∫Δu = 0`. That is a
**closed-manifold** statement. The carriers named throughout this front — `4₁`
and `L6a4` — are **cusped**, i.e. finite-volume *non-compact*, where the
divergence theorem needs a vanishing boundary term that a non-decaying `coth`
does not obviously supply. The bean asserts *"Finite volume suffices ... so
this does not rest on the compactness premise"* without establishing the
boundary term.

It does not need to. This bean's **own second route** already carries the
warrant with no topological premise at all: the radial Laplacian on `H³` is
`u'' + 2coth(r)u'`, harmonic solutions off the origin are `−C coth(r) + D`,
and decay at infinity forces `D = C`, giving `G(r) = −(coth r − 1)/4π`. That
argument needs neither compactness nor finite volume, and it delivers the same
subtraction.

**Re-attributing makes the (b) label stronger, not weaker** — it moves the
exclusion off a premise the carriers may not satisfy and onto one they
certainly do. Note the two routes do not agree on the *family*: O2 gives
`c₀ ≥ 1` strictly, the decay argument gives `c₀ = 1` exactly (the boundary
member). The exclusion of `c₀ = 0` holds either way, since this bean's own
scan puts `c₀ = 1` at 11.15 % against `c₀ = 0`'s 3.505 %.

### What is NOT being corrected

The scatter figures, the `r = −0.904`, the zero-crossing count, the
`0.97 %` coth-vs-expansion deviation and the three SCOPE labels' *direction*
all stand. Nothing here reopens `H_coth`; the kernel stays outside the
admissible family and the ROUTE stays identified-but-underived.

Cross-reference: `qou-o6ml` ROAST 2026-08-30 records that this bean's O2
requirement is **structurally satisfied** by route (2)'s Möbius/O'Hara energy,
whose regularising subtraction is intrinsic — so O2 discriminates *between*
o6ml's routes rather than only damaging the front.


## 2026-09-07 — the kappa(A) contest cannot rank kernels: it measures ONE number

`docs/audits/2026-09-07-em-linking-kernel-and-exponent-are-degenerate.md`,
probe `computations/em_linking_kernel_exponent_degeneracy_probe.py`
(9 assertions, all passed, two end-to-end against the committed contest).

**This bean's structural (b) result is UNTOUCHED.** O2 neutrality
`int(Laplacian u) = 0` excluding the unsubtracted `coth(alpha)` is an
argument with no data in it and stands.

**Round 6's NUMERICAL case against the admissible family does not.** Every
number in it (scatter 3.505% -> 22.32%, residual `r = -0.904`) holds the
separation exponent pinned at 1/3: `score(rs, c0)` in
`em_linking_o2_neutralised_kernel_probe.py:131` hardcodes
`acoth(kappa + c0) / A**third` for every `c0` in its 140-member scan. The
same audit's third finding establishes that `alpha ~ A^(1/3)` is imported
Euclidean phenomenology, and its free-power diagnostic runs at `c0 = 0` only.
The exponent was freed for the incumbent and pinned for its rivals.

Identically, `-dln(kappa)/dln(A) = s*p` with `s` the span-averaged
`-dln F/dln alpha`. Across `c0 = 0..7.5`, `p` moves by a factor of 6 while
`s*p` moves by **1.48%**. Admissible-over-incumbent rms ratio: **5.3742
pinned -> 0.98143 freed** — with its own exponent the O2-admissible kernel
fits marginally BETTER. Every member lands within 1.27x of a bare
2-parameter power law (2.656%), so the series cannot rank them.

The hyperbolic-ball law (additive `alpha = (1/2)lnA + beta`, slope forced by
`V ~ (pi/2)e^{2R}` with `V ~ A`) fails by 429%/741% in kappa-rms and reaches
its forced slope only at `c0 = -0.3598`, ANTI-neutralised. O2 needs
`c0 >= 1`: the two geometric constraints point in opposite directions.
Scope (a) on the conjunction — both inputs are flagged assumptions.

See `qou-gcmn` for the part that matters most: the frozen-B_pp drift is
~80% of the measured slope, so `0.26050` is an upper bound and `H_coth`'s
1/3 coincidence (0.34 sigma) becomes 28.19 sigma at the measured local drift.

## Still open (do not close)

The kernel. Round 6's named next step — the zero-mean Green's function of the
actual fibre — is still worth doing, but this changes what it buys: it would
fix `s` and therefore PREDICT `p`; it would not adjudicate the contest,
because the contest has one degree of freedom and its members all fit it.

## Zero mean closes c0 — PR #7080 (2026-09-07)

The one free scalar in the O2-admissible kernel `kappa = coth r - c0` is NOT
free. O2 IS the zero-mean condition, so it IS the equation for c0:

    c0 = <coth>_M

and on a geodesic ball in H^3 it closes, because coth r * sinh^2 r = cosh r sinh r:

    c0(R) = sinh^2 R / (sinh R cosh R - R),   V = pi (sinh 2R - 2R)

Verified against quadrature to 1.567e-39; limits c0 -> 2/R (R->0, Euclidean)
and c0 -> 1 (R->inf) both correct.

At the corpus's fibre volumes:
  L6a4 / Borromean (3He)  Vol 7.3277  c0 1.56994  p 0.15288  A_zero 9.09e3
  knot 8_11 (3H)          Vol 8.2863  c0 1.53094  p 0.15478  A_zero 9.85e3
  figure-eight 4_1        Vol 2.0299  c0 2.13403  p 0.13004  A_zero 4.40e3

Three non-circular checks, each its own assertion (7/7 pass):
 1. c0 >= 1 is DERIVED, not imposed — admissibility was an INPUT to round 6's
    scan and is an OUTPUT here.
 2. survives round 6's own zero-crossing falsification, which contradicted
    48 of the 140 kernels round 6 scanned.
 3. robust across the two A=3 links: 13.1% volume spread -> 2.55% c0, 1.24% p.

Sensitivity d ln p / d ln V = 0.10279. Volume would have to be wrong 2.53x to
move p by 10%, and 1965x to reach the Euclidean 1/3.

## WHY THIS BEAN STAYS OPEN

This IDENTIFIES the kernel; it does not CONFIRM it. PR #7020 proved the
kappa(A) mirror series constrains only the product s*p, so p ~ 0.153 is
UNFALSIFIABLE on the one measurement that motivated it. Scope (a): no proved
invariant excludes any other kernel.

Closing this needs a measurement of p independent of s — i.e. something that
sees the SEPARATION exponent without going through the kernel. That is the
open item; nothing here supplies it.

Probe: computations/em_linking_zero_mean_closes_c0_probe.py
Audit: docs/audits/2026-09-07-em-linking-zero-mean-closes-c0.md

## And the derived c0 is INVISIBLE to the series — measured, PR #7080 (2026-09-07)

The 'identifies but does not confirm' note above rested on the degeneracy
ALGEBRA. That could have been over-modest: a derived c0 sitting at a sharp
optimum of the fit landscape WOULD be visible to the series. Probe 4 checked.

It is not. Scale-free, R^2 across the whole c0 = 0..7.5 scan spans
0.9625-0.9800 — a spread of 0.0175, SMALLER than the 0.0200 of variance the
best member leaves unexplained. Between-model variation below within-model
residual is the precise sense in which this observable cannot rank these
kernels. The derived c0 = 1.5699 lands at R^2 = 0.9746: sixth of nine, 0.0054
from the top of a 0.0175-wide range. Both other fibres sit alongside it.

THE METRIC TRAP, worth carrying forward because it nearly became a claim.
rms of ln(alpha) on ln(A), with alpha = acoth(kappa + c0), falls monotonically
0.03461 -> 0.00760 across the scan, a factor of 4.56 — apparently a decisive
ranking that picks the LARGEST c0. Artifact: as c0 grows, acoth(kappa + c0)
-> 1/c0, a constant, and a constant lies on a power law trivially with p -> 0.
The p column collapses in lockstep, 0.3291 -> 0.0550. The metric rewards a
kernel for flattening the quantity whose variation it is meant to explain.
Any future scoring on this front must be scale-free (R^2, rms/span) or it will
reproduce this.

TWO SIDE FINDINGS ON ROUND 6, whose numerical case was computed with p pinned
at 1/3. With p freed and the metric scale-free: the landscape is FLAT, not
monotone rising; and its shallow optimum is at c0 ~ 0.25-0.50 — inadmissible
(below the O2 floor) but NOT at c0 = 0, so it does not favour the unsubtracted
incumbent either. A LOCATION, not a preference: 0.0054 in R^2 over 29 points
discriminates nothing. Independent of, and consistent with, #7020's correction
of the same audit.

ONE TEST BANKED AS VACUOUS. alpha = acoth(kappa + c0) is real only for
kappa + c0 > 1, which looks like a falsification test. It cannot fail:
min(kappa) = 1.4020 > 1 over the bound series, so it holds for ANY c0 >= 0.

## WHAT WOULD CLOSE THIS BEAN — sharpened

Unchanged in kind, sharper in degree: a measurement of p independent of s.
Probe 4 now bounds how badly the kappa(A) series fails to supply one — it
cannot even rank c0 across a range spanning admissible and inadmissible
members, so no refinement of THIS observable will help.

Candidate route, NOT yet attempted: inter-cusp geodesic distance in the
per-atom link complements (L6a4 for 3He, 8_11 for 3H, ...) as a function of A.
That is a topological invariant of objects the corpus already assigns, and it
sees the separation without passing through the kernel. Blocked in this
container: snappy and spherogram are both absent (mpmath/numpy/sympy present,
scipy absent). A corpus-grep for prior art on this was launched and had not
returned when this was written.

Probe: computations/em_linking_derived_c0_is_invisible_to_the_series_probe.py

## CORRECTION to my own entry above, and to a corpus-grep report (2026-09-07)

I wrote above that the inter-cusp route is "Blocked in this container: snappy
and spherogram are both absent". That names the WRONG blocker and would send
the next agent to install a package. Installing SnapPy would not unblock it.

THE REAL BLOCKER: there is no derived atom->knot map beyond A <= 3. The
hyperbolic geometry the corpus has sits on HAND-ASSIGNED links (Hopf at A=2,
8_11 and L6a4 at A=3), and PR #1421 records "no derived atom->knot rule".
A=4's Vol_4 ~ 8.05 is an INVERSION of the bond tower against AME (a fit,
he4_vol4_prediction_test_probe.py, and conj:canonical-knot-id-sdp is open);
A=5 carries nothing at all. So even with SnapPy installed there are at most
three links at two distinct A values. You cannot measure an exponent in A
from that, whatever geometry you compute on them.

THE SURFACE IS GENUINELY UNTOUCHED, established vocabulary-independently.
Enumerating the SnapPy API the corpus actually calls, across all of
computations/:
    202 .volume(   50 .num_cusps(   19 .tetrahedra_shapes(
      8 .complex_volume(   2 .cusp_info(   2 .cusp_areas(
      1 .cusp_translations(
and ZERO .length_spectrum / .dirichlet_domain / .horoball_list / .drill /
.cusp_neighborhood. No geodesic length spectrum, no horoball diagram, no
drilled or inter-cusp distance has ever been computed here. That is stronger
than an empty grep because it keys on the API rather than on a chosen word.
Note also that .cusp_translations measures translation lengths ON the cusp
torus -- a DIFFERENT object from the geodesic distance BETWEEN two cusps, and
2026-07-04-em-linking-cusp-geometry-excluded.md is titled as though the whole
class were closed when what it closes is the RATIO hypothesis at A=3.

## DO NOT CITE THE "TRIPLE REFUTATION" -- ITS THIRD LEG NEVER RAN

computations/probes/binding_volume_difference_probe.py has a description
claiming a triple refutation, whose observable C is "SnapPy on the derived
braid closures returns Vol ~ 0 at every A -- closures are non-hyperbolic /
Seifert-fibred". A corpus-grep report handed me that as settled fact. It is
not, and the probe SAYS SO in its own add_caveat:

    "Observable C ... was NOT EVALUATED: SnapPy is not installed, and
     _snappy_braid_vols returns (None, None, False) on ImportError --
     indistinguishable at the call site from a genuine non-hyperbolic
     result. vol_free is null in the committed witness as well, so C has
     never been evaluated in this repo. ... the 'triple refutation' in the
     description and the 'refuted -- closures non-hyperbolic' conclusion
     overstate what ran (bean qou-26f2)."

So the derived braid closures are UNMEASURED, not refuted. Anyone reading the
description alone will treat this route as structurally dead when it is merely
untested -- and will then not bother installing SnapPy, which is the one thing
that WOULD settle observable C. Observables A (log-volume, kappa spans 313%)
and B (cosh-inversion degenerate, all |tr_M| < 2, elliptic, so no real
translation length) DID run and stand.

Reusable lesson, and it is the corpus-grep discipline one level up: a witness
DESCRIPTION is not a primary source either. Read the caveats.

## A SECOND BLINDNESS TO THE SEPARATION LAW -- Lean-proved, scope (b)

QOU/Mass/HyperbolicSurfaceLaw.lean:244, sorry-free (verified: the only
"sorry" string in the file is the phrase "sorry-free" in a docstring about
CrossedModuleSurfaceHolonomy.lean, so a naive grep -c reads 1 and is wrong):

    theorem hyperbolic_not_hasBulk (Rof : R -> R) (hR : forall A, 0 < Rof A) :
        not (HasBulk (hypSurfaceCount Rof))

READ THE BINDER: Rof is quantified over ANY positive radius assignment, so the
surface fraction CANNOT SEE R(A) -- for the same reason, structurally, that the
kappa(A) series cannot see p (#7020) and cannot see c0 (#7080). That is now
THREE observables blind to the separation law, and this one carries a proved
invariant, so unlike the other two it is quotable as a scope-(b) exclusion.

## ALSO NOT NOVEL -- alpha ~ ln A is already in the corpus

The hyperbolic objection to a power law (V(R) ~ (pi/2)e^{2R} so R ~ (1/2)ln V,
and an extensive carrier then gives alpha ~ ln A rather than A^p) is already
scored on this series at 9.253% (em_linking_alpha_scaling_provenance_probe),
and the ADDITIVE form is already in the merged degeneracy probe. Do not
re-derive it.

## WHAT WOULD ACTUALLY CLOSE THIS BEAN, restated

Not a geometry computation on three hand-assigned links. Either:
  (i) a DERIVED atom->knot rule at A >= 4 (conj:canonical-knot-id-sdp), which
      would make a geometric length-vs-A measurable at all; or
  (ii) an observable outside the {kappa(A), surface-fraction} pair that is not
      blind to R(A) -- and the Lean above is a warning that blindness here is
      the rule rather than the exception.

## CORRECTION to the entry above: TWO observables, not three (2026-09-07)

I wrote "That is now THREE observables blind to the separation law". Wrong on
the word OBSERVABLES. There are two, carrying three findings:

  finding                                observable          mechanism
  ---------------------------------------------------------------------------
  #7020: series constrains only s*p      kappa(A)            chain rule on a
                                                             composition; the
                                                             SLOPE is a product
  #7080: fit quality cannot rank c0      kappa(A) -- SAME    residual structure
                                                             also fails to
                                                             discriminate
  hyperbolic_not_hasBulk                 surface fraction    in H^3 volume and
                                         -- DIFFERENT        boundary area grow
                                                             at the same rate,
                                                             so the ratio
                                                             forgets R

"Three independent blindnesses" reads as strong convergent evidence. Two
observables, one measured twice, is weaker, and is the honest version.

WHAT THIS DOES NOT DO is collapse the first two into one fact. They are
logically independent, which is why the second was worth measuring: a
degenerate SLOPE does not imply flat FIT QUALITY. A wrong kernel could match
s*p and still leave systematic curvature in the residuals, and that would have
been visible. It is not -- R^2 spread 0.0175 against 0.0200 unexplained -- so
the second finding is real and does not follow from the first.

The genuinely independent leg is the third, and it is the only one carrying a
proved invariant. So when weighing "is the separation law reachable at all",
count ONE independent proved blindness plus one twice-measured degeneracy, not
three.

## SHARPENING the blocker: ONE distinct A, not two (2026-09-07)

I wrote "even with SnapPy installed there are at most three links at two
distinct A values". Checked at source (binding-link-volumes.witness.json) and
that UNDERSTATES the blocker. The table holds:

    Hopf_2H         0 (Seifert-fibred)   <- A=2, NOT HYPERBOLIC
    knot_8_11_3H    8.2863168178         <- A=3, hyperbolic
    L6a4_3He        7.3277247534         <- A=3, hyperbolic
    Vol_B3_8G       7.327724753417752    <- same manifold as L6a4, not a 4th

So the corpus carries TWO hyperbolic links and they are BOTH AT A = 3.
Exactly ONE distinct A value has any hyperbolic geometry attached to it.

That makes the blocker airtight rather than merely severe: an exponent in A
cannot be fitted to a single A, however perfectly the geometry on those two
links is computed. Even a flawless inter-cusp geodesic distance for L6a4 and
8_11 yields two numbers at the same A -- which is a consistency check between
two A=3 assignments (worth having, and that is what
2026-07-04-em-linking-cusp-geometry-excluded.md already did with cusp
translation lengths, finding a 4.3% miss), never a measurement of p.

The other volumes in the corpus do not rescue it. The pion/cusp probe adds
4_1 (assigned A=1), L6a5 (A=3), and L8a21/L8a20 (A=4) -- but the A=4
assignments are PRE-REGISTERED CANDIDATES, not derived, and A=4's Vol_4 ~ 8.05
elsewhere is an inversion of the bond tower against AME. Adding a fitted point
to a one-point series does not make an exponent measurable; it makes it
circular.

CONSEQUENCE FOR PRIORITISATION. This removes any reason to install SnapPy for
the sake of qou-17mq specifically. (It remains the right thing to do for
qou-26f2, which is about a probe whose observable C has never been evaluated --
a different and genuinely open question.) The only thing that unblocks p here
is a DERIVED atom->knot rule at A >= 4, i.e. conj:canonical-knot-id-sdp.

## MERGED to main as 98dd4f7129 (PR #7080, 2026-09-07)

Rebase-merged on explicit owner permission ("merge"). Landed:
  computations/em_linking_zero_mean_closes_c0_probe.py                 (7/7)
  computations/em_linking_derived_c0_is_invisible_to_the_series_probe.py (7/7)
  computations/em-linking-zero-mean-closes-c0.witness.json
  computations/em-linking-derived-c0-is-invisible-to-the-series.witness.json
  docs/audits/2026-09-07-em-linking-zero-mean-closes-c0.md

THIS BEAN STAYS OPEN (AGENTS.md 13a — never close a bean whose subject is an
open conjecture). What merged is a derivation plus a measurement of its own
limits; the kernel IDENTIFICATION remains a conjecture.

State of the front after the merge:
  DERIVED    c0 = <coth>_M = sinh^2 R / (sinh R cosh R - R), quadrature-checked
             to 1.567e-39, admissible at every corpus volume without being
             placed there.
  PREDICTED  p ~ 0.153, and MEASURED to be untestable on the kappa(A) series:
             R^2 spread 0.0175 across the whole c0 scan against 0.0200 of
             variance unexplained by the best member.
  BLOCKED    p has no measurement independent of s. The corpus carries TWO
             hyperbolic links and both are at A = 3 (Hopf at A=2 is
             Seifert-fibred, Vol = 0), so exactly ONE distinct A has hyperbolic
             geometry. No exponent in A is fittable to one A.
  ONE LIVE   a DERIVED atom->knot rule at A >= 4 (conj:canonical-knot-id-sdp).
  ROUTE      Put to the owner; not started unilaterally.

No reason to install SnapPy for this bean. (Still worth it for qou-26f2, whose
observable C has never been evaluated.)



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

- **Round 56 Progress (`2026-11-16T21:20:58Z`)**: Opened [`litlfred/qou#8207`](https://github.com/litlfred/qou/pull/8207) (`cfc03c4131df1ea758c17554768f2274e708f38b`, Commit 1 `0a9d3f269d6c23f614dc40aac55d5f0a7b2baafd`). Keeping bean at `status: in-progress` pending owner review.
