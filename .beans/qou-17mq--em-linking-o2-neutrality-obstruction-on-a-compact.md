---
# qou-17mq
title: 'EM-linking O2 (neutrality obstruction): on a COMPACT quotient int(Laplacian u)=0 forces total charge zero — ''two like charges alone'' is NOT admissible as stated; the Green''s fn acquires a -1/vol(M) offset. Re-pose the two-like-charge invariant relative to a neutralizing background (only charge-neutral combinations well-posed; physically the nucleus IS neutral). Blocks/reshapes the STATEMENT of qou-o6ml, not just its solution'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T20:31:20Z
updated_at: 2026-09-07T08:19:14Z
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
