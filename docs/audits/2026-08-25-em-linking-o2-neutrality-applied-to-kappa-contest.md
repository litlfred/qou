# O2 applied to the κ(A) contest — the winning kernel is not admissible

**Status:** FINDING (reproducible, nothing fitted beyond the single scale the
incumbent hypothesis already carries, nothing wired). Bean `qou-17mq`, opened
2026-08-01 and untouched since.

Probe: [`em_linking_o2_neutralised_kernel_probe.py`](../../computations/em_linking_o2_neutralised_kernel_probe.py)
(witness `em-linking-o2-neutralised-kernel.witness.json`, 4 assertions, all
passed).

## Why this exists

[`2026-08-01-em-linking-reads-round1.md`](2026-08-01-em-linking-reads-round1.md)
records two structural obstructions from its round-2 reading of the primary
sources. **O1** (total antisymmetry) is cited constantly downstream and has
shaped every subsequent route. **O2** has not been applied to anything:

> On a closed manifold `∫Δu = 0` forces total charge zero … the pp-pair energy
> must be defined relative to the neutralizing background (equivalently, only
> charge-neutral combinations are well-posed), and the Green's function
> acquires a `−1/vol(M)` offset.

Corpus-grepped 2026-08-25: `neutralis*` / `neutraliz*` / "compact-quotient
neutrality" appear at **four** sites, all inside that one audit, and at **zero**
sites in `computations/`. No probe, no witness, and no Lean file has ever
applied O2. Meanwhile the same front's headline result — the κ(A) hypothesis
contest of `em-linking-mirror-series.witness.json` — scores a kernel that O2
excludes.

## The argument

The surviving route is the metric Coulomb pairing `⟨A₁, J₂⟩` on the `H³` scalar
Green's function `φ₀(α) = −coth(α)/4π`, and the hypothesis scored against the
mirror series is

$$H_{\mathrm{coth}}:\quad \kappa = \coth(\alpha),\qquad \alpha = c\,A^{1/3}$$

a one-parameter law. It won the contest on scatter, and the qualitative feature
that separated it from its rivals is **saturation**: `coth α → 1`, so `κ → +1`
in heavy nuclei while the power laws send `κ → 0`.

**An unsubtracted `coth` is exactly what O2 forbids.** On a finite-volume `M`
the admissible pair kernel is the *zero-mean* Green's function. The robust
consequence needs no model of that kernel:

> A zero-mean function that is not identically zero **must take both signs**.
> `coth(α)` is strictly positive and monotone. So no admissible kernel is a
> positive saturating function of the separation.

Physically this is ordinary jellium: a like-charge pair against a neutralising
background is repulsive at short range and *attractive* beyond a critical
separation. The saturation that won the contest is a property of the
**excluded** member.

Two scoping notes, both in the direction that weakens the claim:

- **Finite volume suffices** — `∫Δu = 0` does not need compactness, so the
  argument covers the corpus's *cusped* finite-volume hyperbolic complements
  (`4₁`, `L6a4`) as well as a closed quotient. The audit asserts the QOU fibre
  is a compact hyperbolic quotient; this probe takes that premise as given and
  notes it is stronger than the argument needs.
- **The one-term model is a model.** Writing the admissible family as
  `coth(α) − c₀` with `c₀ = ⟨coth⟩_M > 1` (strictly, since `coth > 1`
  pointwise) is the simplest realisation of the zero-mean condition, not the
  exact Green's function of a quotient, which is a regularised Poincaré series.
  The sign-change conclusion above does **not** depend on it; the numbers below
  do.

## The numbers

Re-scoring the **same** committed κ series (29 bound mirror pairs, `A = 3…63`),
with the same statistic the contest used — form the implied scale constant per
pair, report its relative scatter:

| kernel | `c₀` | admissible? | scatter | residual `r` vs `A` |
|---|---:|---|---:|---:|
| `H_coth`, as scored | 0 | **no** | **3.505 %** | +0.049 |
| best admissible member | 1.0 | boundary | 11.15 % | **−0.904** |
| | 2.0 | yes | 15.27 % | |
| | 4.0 | yes | 19.30 % | |
| | 7.5 | yes | 22.32 % | |

An end-to-end assertion checks that the incumbent row reproduces the committed
bound-only `H_coth` scatter to `< 10⁻⁶`, so the admissible rows are being
compared against the same arithmetic rather than against a quoted number.

Three readings, in descending order of how much they rest on the model:

1. **Scatter is monotone in `c₀`.** Every step toward a genuinely neutralised
   kernel makes the description worse, and the best admissible member is the
   `c₀ = 1` infinite-volume *boundary* — the least-neutralised point of the
   family, and not an interior member for any finite `M`. There is no
   admissible optimum in the interior to appeal to.
2. **The admissible boundary member fails the corpus's own residual test.**
   `em-linking-residual-structure.witness.json` separated `H_coth` from
   `H_FH_Z` on exactly this criterion: structureless residuals (`r = 0.049`)
   for the winner against a strong systematic trend (`r = 0.799`) for the
   loser, and the drift was counted against the loser. The admissible kernel
   carries `r = −0.904` — *more* structure than the hypothesis that was
   rejected for carrying structure.
3. **48 of 140 scanned admissible members are contradicted without any appeal
   to scatter.** For `c₀ > 1` the predicted `κ` crosses zero at a finite
   `A_zero = (\mathrm{arccoth}(c₀)/c)³`; for 48 of them that crossing lands
   inside `A ∈ [3, 63]`, where every measured `κ` is strictly positive
   (min 1.4127).

At the heaviest pair (`A = 63`, `Z = 32`, `κ = 1.4127`) the inadmissible
incumbent predicts 1.4225 and the admissible boundary member 1.1593.

## Scope

Per the STRICT (a)/(b) discipline:

- **(b) structural exclusion, invariant cited.** Compact- (indeed
  finite-volume-) quotient neutrality, `∫Δu = 0`, excludes the *unsubtracted*
  kernel `coth(α)` from the admissible family, and with it the saturation
  prediction. This is an exclusion of **the kernel as written**, not of the
  hyperbolic Coulomb route.
- **(a) scope-limited negative.** The admissible family, scored on this series
  with this frozen `B_pp` unit, does not improve on the inadmissible incumbent
  and gets monotonically worse with neutralisation. That is a statement about
  this parameterisation on this data.

**Not claimed.** The metric Coulomb pairing `⟨A₁, J₂⟩` on the hyperbolic
Green's function remains the surviving route, exactly as round 3 left it.
Nothing here excludes it, nothing here proposes a replacement, and nothing is
wired.

## What this changes for the standard-model chain

The two-like-charge EM-linking invariant is object **4-B** of
[`sm-eightfold-derivation-cheat-sheet.md` §4](../sm-eightfold-derivation-cheat-sheet.md),
ranked **1** in that file's near-term-derivable table because it is the only
one of the three gating objects that needs no `SU(3)` and because it closes
`m_d − m_u` and 69 % of the ³He mirror residual together.

Its status is unchanged — still open, still the gate. What changes is the
evidential situation *inside* it. The contest that appeared to have selected a
kernel compared:

- an **inadmissible** kernel (this finding), against
- two hypotheses whose **warrant had already been withdrawn** as a
  misattribution of a single-torus bound to a link (round 5).

So no member of that contest carried a live structural warrant at the time it
was scored, and its ranking should not be cited as support for
hyperbolic-saturation. The honest position on 4-B is that the *route* is
identified and the *kernel* is not.

## Carried confound

Bean `qou-gcmn`: the per-pair Coulomb unit is held at its `A = 3` `H₆` value
across the whole series, so any `A`-dependence of the strong bond `B_pp` is
absorbed into `κ`. That bounds what **any** scatter comparison on this series
can establish, this probe included. It does not touch the structural argument,
which involves no data at all.

## Next

The question this sharpens is well-posed and does not need more literature:
what is the zero-mean Green's function of the actual fibre? The one-term model
is a stand-in; a real Poincaré-series computation on a specific finite-volume
quotient would either produce a kernel whose shape fits `κ(A)` or establish
that no admissible kernel does — and the second outcome is as valuable as the
first, since it would move 4-B from "route identified" to "route excluded" and
force the search elsewhere.

## Housekeeping — four audit witnesses deliberately NOT regenerated

`scripts/precision-gates.sh --changed` reports RED on the raw-float64 ratchet
and flags four stale committed audit witnesses. Both are inherited from `main`,
not introduced here:

- The 5 newly-dirty witnesses are `deltalambda/deuteron-interface-handle-curvature`,
  `qbeta/birkhoff-barodd-pythagoras-bridge`, `qbeta/a3-branching-asymmetry-vs-required`,
  `deltalambda/yekutieli-trefoil-surface2form-discretization` and
  `deltalambda/sigma1cubed-seifert-surface-term`. None is touched by this
  change. The witness added here carries **zero** raw-float64 fields.
- The four regenerations were **reverted rather than committed**. This
  container has no `numpy`, `scipy`, `sympy` or `clarabel`, carries
  `mpmath 1.4.1` against the corpus's `1.3.0`, and a different
  `pyhecke_native_build`. Committing them would have overwritten real
  provenance with a degraded environment record and moved counts
  (`Q0_OK 963 → 970`, `STALE 229 → 228`) that cannot be attributed to content
  from inside this container. Leaving a witness honestly stale beats
  committing one that measures the harness.

---

# Addendum — the discrimination test could not discriminate

Second probe:
[`em_linking_kappa_regime_reachability_probe.py`](../../computations/em_linking_kappa_regime_reachability_probe.py)
(witness `em-linking-kappa-regime-reachability.witness.json`, 3 assertions,
all passed). Same bean.

The finding above says the contest's winner is not an admissible kernel. That
prompts a prior question nobody had asked, and it is cheaper to answer than the
one it supersedes: **does the series reach the regime where its hypotheses
diverge at all?**

Bean `qou-i6rg` extended the mirror series to `A = 63` and called it *"the
measurement that selects the hyperbolic kernel or kills it"*, on the grounds
that `H_coth` saturates at `κ → 1` while the power laws send `κ → 0`, so they
*"diverge at large A and in opposite directions"*. That is true asymptotically.
It is not true at `A = 63`.

Computed from the contest's **own** fitted constants — no new hypothesis,
nothing scored, nothing fitted:

| quantity | value |
|---|---|
| `α` spanned by the series (`A = 3…63`) | **[0.3165, 0.8732]** |
| `α` for `coth` within 10 % of its limit | 1.5223 → **`A = 334`** |
| … within 5 % | 1.8568 → `A = 606` |
| … within 1 % | 2.6517 → `A = 1764` |
| heaviest known nuclide | `A = 294` |

**Saturation begins past the end of the nuclear chart.** Not "the test was run
and came out close" — the discriminating regime is not reachable in any
nucleus. There is no heavier mirror pair to go and measure.

Two corollaries, both quantitative:

1. **`coth` is not separable from its own short-range expansion here.** Over
   the measured range `coth α = 1/α + α/3 − α³/45 + …` agrees with its two-term
   truncation to **0.97 %**, against the **3.505 %** scatter the hypotheses are
   judged on. So whatever `H_coth`'s advantage tracks on this data, it is the
   curvature term `α²/3` — not saturation. (The *one*-term `1/α` **is**
   separable, at 19.49 %, which is consistent with `H_FH_A` scoring worse. The
   data resolves the first curvature correction and nothing beyond it.)
2. **The separation actually achieved is 1.79 × the noise.** `H_coth` and
   `H_FH_Z`, each at its own fitted constant, differ by at most **6.285 %**
   across the whole series (mean 3.247 %) against 3.505 % scatter. A gap of
   order the noise is not a discrimination.

## A second, O2-independent route to the same subtraction

Worth recording because it needs neither compactness nor finite volume. The
radial Laplacian on `H³` is `u'' + 2 coth(r) u'`, so harmonic solutions off the
origin are `−C coth(r) + D`: the fundamental solution is fixed only up to an
additive constant. `C` is set by the delta normalisation; `D` by the boundary
condition. Requiring decay at infinity gives `D = C`:

$$G(r) = -\frac{\coth(r) - 1}{4\pi} \sim -\frac{1}{2\pi}e^{-2r}$$

So **the decaying Green's function of `H³` is already the subtracted one**, and
the saturating `−coth(r)/4π` is the `D = 0` choice, which does not vanish at
infinity. The subtraction the main finding derives from finite-volume
neutrality is also just the ordinary boundary condition one level down.

Relatedly, and standard: for finite-covolume `Γ` the critical exponent is
`δ(Γ) = 2` and lattice points satisfy `#{d ≤ R} ~ c e^{2R}`, exactly cancelling
the `e^{−2R}` decay — so the Green's-function Poincaré series diverges. That
divergence *is* O2 in analytic form: a finite-volume quotient admits no Green's
function without the `−1/vol(M)` source correction. Stated as the known fact it
is, not re-derived; nothing above rests on it.

## Scope

**(a) scope-limited negative on a TEST, not on a hypothesis.** What is claimed:
the `A = 63` series does not reach the regime in which its hypotheses diverge,
so it cannot have selected among them on the stated grounds. What is **not**
claimed: that `H_coth` is false, that a power law is true, or that the metric
Coulomb route fails. This is about what the measurement can resolve.

## What this changes

`qou-i6rg` is marked `completed`, and the front has been reading its ranking as
a settled selection. It is not one, and no amount of further AME data can make
it one — the bean's own premise was that the test *"needs NO new theory, only
more AME data"*, and the missing ingredient turns out to be neither. Combined
with the main finding, the position on 4-B is:

- the two `H_FH` hypotheses lost their warrant (round 5, misattribution);
- the winner is not an admissible kernel (main finding, O2);
- and the measurement could not have separated them in any case (here).

The route — the metric Coulomb pairing on the hyperbolic Green's function —
is untouched by all three. What is gone is the belief that its kernel has been
identified.

**The honest next step changes accordingly.** Not "extend the series"; that is
now known to be futile. Either derive the kernel (compute the zero-mean Green's
function of an actual finite-volume quotient and *predict* `κ(A)` rather than
score parameterisations against it), or find an observable that probes
`α ≳ 1.5` — which, since `α ∝ A^{1/3}` in this parameterisation, no nucleus
supplies.

---

# Third finding — the separation law is an unexamined Euclidean import

Third probe:
[`em_linking_alpha_scaling_provenance_probe.py`](../../computations/em_linking_alpha_scaling_provenance_probe.py)
(witness `em-linking-alpha-scaling-provenance.witness.json`, 3 assertions,
all passed). Same bean.

The two findings above score **kernels** against `κ(A)`. This one is upstream
of both: it asks about the **separation law** every kernel is fed.

## The import

`em_linking_coth_separation_probe.py` is explicit about its premise, and
unusually honest about its limits — four caveats, null transforms scored
alongside, *"this cannot confirm anything; it can only fail"*. Credit where
it is due. But caveat (3) reads:

> *"(3) `A^(1/3)` was fixed in advance as the standard nuclear radius law, not
> selected post hoc."*

Fixing a law in advance protects against **post-hoc selection**. That is real
and worth having, and it is not the same as the law being **derived**. And
this law is not merely underived — it comes from the wrong geometry. The same
file says of the kernel:

> *"`H_coth` has NO free parameter in the kernel — `coth` is forced by the
> Green's function."*

So the kernel is hyperbolic **by construction** while the separation law fed
into it is the Euclidean liquid-drop nuclear radius. Two geometries inside one
quantity.

## What the geometry would require

In `H³` a ball of radius `R` has volume `π(sinh 2R − 2R) ~ (π/2)e^{2R}`, so
`R ~ ½ ln(2V/π)`: hyperbolic size grows **logarithmically** in volume. For an
extensive carrier volume `V ∝ A`, the hyperbolic separation scale therefore
goes like `ln A`, not `A^{1/3}`.

Scored on the same series with the same statistic:

| separation law | scatter |
|---|---:|
| `A^{1/3}` — Euclidean nuclear radius, **imported** | **3.505 %** |
| `A^{1/4}` | 6.358 % |
| `ln A` — **hyperbolic self-consistent** (`V ∝ A`) | **9.253 %** |
| `A^{1/2}` | 13.95 % |

**Geometric self-consistency costs a factor 2.64 in fit.** So `H_coth`'s fit
quality depends on the geometric *mixture*, not on the hyperbolic kernel alone.

(`ln A` and `½ ln A` are the same hypothesis once the scale constant is free
and must score identically; that identity is asserted in the witness as a
self-check on the scoring, not reported as a result.)

## The corpus cannot adjudicate this

[`binding-link-volumes.witness.json`](../../computations/binding-link-volumes.witness.json)
carries hyperbolic link volumes for **`A = 2` and `A = 3` only** — Hopf
(0, Seifert-fibred), `8₁₁` (8.2863), `L6a4` (7.3277) — and its own description
records that *"the A-dependence is not in a single binding-link volume"*.

There is no per-isotope hyperbolic geometry in the corpus beyond `A = 3`. So no
`α(A)` law can currently be **derived** from framework data; whatever law is
used on this front is imported from outside it. That is a statement about the
framework's reach, not about this probe's diligence.

## The deflationary reading, stated plainly

A free-power diagnostic — a fit with one more DOF than any fixed-`p`
hypothesis, and reported as a diagnostic, never as support — lands at
`p = 0.33`, at 3.482 % against 3.505 % for exactly `1/3`. Indistinguishable.
**The data independently prefers the Euclidean exponent.**

Put together with the pure-`1/r` comparator already in the contest
(`H_FH_A` *is* `κ = 1/(cA^{1/3})`, i.e. Coulomb with a Euclidean nuclear
radius and no curvature term):

| model | scatter |
|---|---:|
| pure Coulomb `1/r`, Euclidean radius | 5.499 % |
| `coth` — adds the hyperbolic curvature term | 3.505 % |

So `κ(A)` is close to what **plain Coulomb repulsion in a Euclidean nucleus**
gives, with the hyperbolic kernel contributing a curvature correction worth a
factor **1.57** in scatter on one shared parameter.

That factor is *real* — the correction buys something — but it is
**suggestive, not decisive**, and it is comparable to what the frozen-`B_pp`
confound (`qou-gcmn`) could account for on its own. Combined with finding 2
(over this range `coth` is within 0.97 % of `1/α + α/3`), the position is that
the data resolves the first curvature correction and nothing beyond it.

## Scope

**(a) scope-limited negative on an INPUT ASSUMPTION** shared by every
hypothesis on this front.

- **Claimed:** `α ∝ A^{1/3}` is imported Euclidean phenomenology rather than
  framework output; the corpus holds no data from which to derive a rival; and
  geometric self-consistency costs 2.64× in fit.
- **Not claimed:** that `A^{1/3}` is *wrong* — the data prefers it. That the
  geometry is Euclidean. That there is no hyperbolic content. That `H_coth` is
  refuted. The measured range does not resolve the question, which is the
  point.

## What the three findings amount to

Nothing here refutes the metric Coulomb route, and none of the three should be
read as doing so. What they remove, together, is a chain of impressions:

1. that a contest selected a kernel — no member of it held a live structural
   warrant when it was scored;
2. that more AME data would settle it — the discriminating regime sits past the
   end of the nuclear chart;
3. that the hyperbolic reading was load-bearing for the fit — the fit rests on
   a Euclidean separation law, and using the geometry consistently costs 2.64×.

4-B remains rank 1 and remains open. The honest statement of its state is that
the *route* is identified, the *kernel* is not, and the *separation law* is
imported — three distinct gaps where the front had been carrying one.
