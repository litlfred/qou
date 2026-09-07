# The κ(A) series measures one number — kernel and separation exponent are degenerate

**Date:** 2026-09-07 · **Bean:** `qou-17mq` (with `qou-gcmn`, `qou-u3vw`) ·
**Scope:** (a) scope-limited negative **on a test**, plus (a) on the
hyperbolic-ball separation law. Nothing wired, nothing fitted, no hypothesis
promoted.

Probe: [`em_linking_kernel_exponent_degeneracy_probe.py`](../../computations/em_linking_kernel_exponent_degeneracy_probe.py)
(witness `em-linking-kernel-exponent-degeneracy.witness.json`, 8 assertions,
all passed, two of them end-to-end reproductions of the committed contest).

## The claim

For any hypothesis on this front written as a kernel plus a separation law,

$$\kappa = F(\alpha), \qquad \alpha = c\,A^{p},$$

the chain rule gives, identically,

$$\frac{d\ln\kappa}{d\ln A} \;=\; -\,s\,p, \qquad s := -\frac{d\ln F}{d\ln\alpha}.$$

So the mirror series constrains **the product only**. Kernel and separation
law are jointly unidentifiable: fixing either one predicts the other, and
fixing neither predicts nothing.

**`s` is a span-averaged effective slope, not a constant.** For
`F = coth - c0` the quantity `-d ln F/d ln a` varies across the window — the
corpus measures that `coth` over `a` in [0.3165, 0.8732] is within 0.97 % of
`1/a + a/3`, i.e. the curvature term is resolved. Every `s` below is the OLS
slope of `ln k` on `ln a` over the 29 pairs, and the identity holds in that
averaged sense, not pointwise. Stating it pointwise would confuse a family
with a proposition.

Measured over the 29 bound pairs, `A = 3…63`:

$$-\frac{d\ln\kappa}{d\ln A} \;=\; 0.2604989 \pm 0.00722 \quad (2.77\%,\ \text{1σ OLS}).$$

That is the whole of what the series says — and, per the penultimate section,
it is an **upper bound** on `s·p` rather than a measurement of it.

## What this corrects

[`2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md`](2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md)
("round 6") establishes — correctly, structurally, with no data in it — that
finite-volume quotient neutrality `∫Δu = 0` excludes the unsubtracted kernel
`coth(α)` and admits only a sign-changing zero-mean one, modelled by
`κ = coth(α) − c₀` with `c₀ ≥ 1`. **That exclusion is untouched here and
stands.**

Round 6 then builds a *numerical* case on top of it: scatter rises
monotonically in `c₀` (3.505 % at `c₀ = 0` to 22.32 % at `c₀ = 7.5`), and the
best admissible member carries a residual trend `r = −0.904`, worse than the
hypothesis the contest had rejected for carrying structure.

**Every one of those numbers holds the separation exponent pinned at 1/3.**
In [`em_linking_o2_neutralised_kernel_probe.py`](../../computations/em_linking_o2_neutralised_kernel_probe.py)
the scoring function is

```python
def score(rs, c0):
    """Implied scale constant per pair for kappa = coth(alpha) - c0."""
    ...
    cs.append(acoth(arg) / mpf(r["A"]) ** third)   # third = 1/3, for every c0
```

and the **third finding of that same audit** establishes that `α ∝ A^{1/3}` is
imported Euclidean liquid-drop phenomenology, not framework output — *"no
`α(A)` law can currently be **derived** from framework data; whatever law is
used on this front is imported from outside it."* The free-power diagnostic
that finding runs lives in a different probe
([`em_linking_alpha_scaling_provenance_probe.py`](../../computations/em_linking_alpha_scaling_provenance_probe.py))
and is evaluated at `c₀ = 0` only.

So the exponent was freed for the incumbent and pinned for its rivals. The two
findings were never crossed.

## The measurement

Each kernel at **its own** best exponent, against the same 29 pairs. `rms` is
the relative residual in κ-space, which is comparable across laws:

| `c₀` | admissible? | `p` predicted | `s` | `s·p` | rms, `p` free | rms, `p` pinned at 1/3 |
|---:|---|---:|---:|---:|---:|---:|
| −0.30 | no (anti-neutralised) | 0.47107 | 0.537 | 0.25295 | 4.098 % | 5.572 % |
| −0.20 | no | 0.40559 | 0.634 | 0.25707 | 3.330 % | 4.120 % |
| −0.10 | no | 0.36177 | 0.715 | 0.25882 | 2.983 % | 3.103 % |
| **0** | **no — round 6's incumbent** | **0.32906** | 0.789 | 0.25970 | **2.807 %** | **2.845 %** |
| 0.25 | no | 0.27261 | 0.955 | 0.26046 | 2.662 % | 5.105 % |
| 0.50 | no | 0.23522 | 1.107 | 0.26049 | 2.663 % | 8.442 % |
| **1** | **yes — O2 floor** | **0.18697** | 1.391 | 0.26007 | **2.755 %** | **15.29 %** |
| 1.5 | yes | 0.15633 | 1.660 | 0.25956 | 2.857 % | 22.03 % |
| 2 | yes | 0.13479 | 1.922 | 0.25909 | 2.944 % | 28.66 % |
| 3 | yes | 0.10615 | 2.434 | 0.25834 | 3.077 % | 41.74 % |
| 4 | yes | 0.087786 | 2.937 | 0.25779 | 3.173 % | 54.68 % |
| 7.5 | yes | 0.054974 | 4.669 | 0.25665 | 3.361 % | 99.47 % |

Read the two rightmost columns against each other. **`p` moves by a factor of
6 across the family and `s·p` moves by 1.48 %.** That is the degeneracy,
measured.

Three consequences:

1. **The round-6 gap is carried entirely by the pin.** Admissible-over-incumbent
   rms ratio: **5.3742 pinned → 0.98143 freed.** With its own exponent the
   O2-admissible kernel fits *marginally better* than the inadmissible
   incumbent. Round 6's structural exclusion stands; its numerical case
   against the admissible family does not survive freeing a pin its own third
   finding identifies as an import.

2. **Nothing is resolved from a straight line.** A bare two-parameter power
   law reaches **2.656 %**. Every member of the incumbent-plus-admissible
   family lands between 2.66 % and 3.36 % — within 1.27× of that floor. The
   one-parameter hypotheses are competing for a single slope, and the series
   cannot rank them.

3. **`H_coth`'s apparent success is one number agreeing to 1 %.** Choosing
   `c₀ = 0` *predicts* `p = 0.32906 ± 0.00951`, which is `1/3` to **0.45 σ**.
   That coincidence is the whole of it. Choosing `c₀ = 1` predicts
   `p = 0.18697 ± 0.00548`.

   **`p = 0.187` is an OUTPUT, not an identification.** It is what the
   admissible kernel would require of a separation law, offered as a
   prediction target for a *derived* one. Per the anti-fit directive it is not
   matched against any small rational, and no kernel is promoted on the
   strength of it.

## The move has a precedent in the held literature

Not corpus coverage of this finding — corpus-grep found none, across all six
paths — but worth citing if "jointly unidentifiable" reads as an unusual
claim. Garoufalidis–Zagier, *Knots, Perturbative Series and Quantum
Modularity* (`garoufalidis-zagier-2024`,
`library/arxiv-2111.06645v3/sections/sec-035-…md:48`), on the asymptotic
series of the Kashaev invariant:

> `C^(K,σ)_α` and `Ã^(K,σ)_α(k)` are **not canonically defined numbers, only
> their product is**.

Different objects entirely — a normalisation ambiguity, nothing to do with a
kernel or a separation exponent. But it is the same logical move, stated in
this corpus's own subject area: the product is canonical while its factors
individually are not, so quoting either factor alone is meaningless without a
convention. Here the convention is the separation law, and the corpus does not
supply one.

## The hyperbolic-ball separation law fails, by hundreds of percent

Round 6's finding 3 scored the **multiplicative** law `α ∝ c·ln A` (free
slope) at 9.253 % and called geometric self-consistency "a factor 2.64 in
fit". The law hyperbolic geometry actually forces is **additive**. From
`Vol(B_R) = π(sinh 2R − 2R) ~ (π/2)e^{2R}` with an extensive carrier volume
`V ∝ A`,

$$\alpha \;=\; \tfrac12 \ln A + \beta,$$

whose **slope is fixed at 1/2 per `ln A`** — the only freedom is the additive
`β`. That is one free parameter, the same as every rival, but **two conditions
to meet** (the span and the scale), so it is over-determined. Measured:

| `c₀` | slope delivered (geometry forces 1) | κ-rms at best `β` |
|---:|---:|---:|
| 0 | 0.39428 | 429.4 % |
| 1 | 0.13146 | 740.7 % |

Not marginal — wrong by hundreds of percent, at every kernel in the family.

**This is scope (a), not a structural exclusion.** No proved invariant is
cited, and *both* inputs are assumptions the corpus already flags: `V ∝ A` is
*"itself an assumption. The corpus cannot check it"*
([`em_linking_alpha_scaling_provenance_probe.py`](../../computations/em_linking_alpha_scaling_provenance_probe.py)),
and the one-term subtracted `coth` is *"a model … not the exact Green's
function of a quotient"* (round 6). What fails is the **conjunction**.

The slope reaches 1 only at **`c₀ = −0.359789`**, which is *anti*-neutralised:
more positive than the unsubtracted kernel, i.e. **further from admissible
than the incumbent**.

So the two geometric constraints on the same object point in opposite
directions, and are incompatible by 1.36 in `c₀`:

- **O2 neutrality** (a theorem, `∫Δu = 0`) requires `c₀ ≥ 1`;
- **hyperbolic-ball extensivity** (an assumption about the carrier) requires
  `c₀ ≈ −0.36`.

Since only the first is a theorem, what is excluded is the **conjunction**:
the carrier is not a metric ball of extensive hyperbolic volume, *or* κ is not
a pair-kernel evaluation at all.

## The frozen-`B_pp` confound is not a correction — it is ~80 % of the signal

**This front already knows the drift exists.** `bpp_higher_a_sparse_probe.py`
(merged 2026-08-31, PR #6336, *"B_pp DECLINES with A"*) and its follow-on
`qou-23dn` establish the sign and the low-`A` scale. New here: the log-slope
form, the size, and the consequence.

Bean `qou-gcmn` holds the per-pair Coulomb unit at its `A = 3` value. Round 6
reads this as bounding *"what any scatter comparison can establish"*. Writing
`B_pp` proportional to `A^{-d}`,

$$\kappa_{\text{meas}} = \kappa_{\text{true}}\,(A/3)^{-\delta}
\;\Longrightarrow\; s\,p + \delta \;=\; 0.2604989 .$$

The drift enters **the one number the front measures**, additively. And from
that merged probe's own committed corrections — `kappa_correction` 1.0823957827
at `A = 3` to 1.1494801700 at `A = 4` — the **local** drift is

$$\delta(A{=}3 \to 4) \;=\; 0.20903, \qquad \textbf{80.2\%} \text{ of the whole measured } 0.26050 .$$

So `0.26050` is an **upper bound** on `s·p`, and every exponent in the table
above is an upper bound too.

**That reading is not convenient — it removes the last apparent support for
the framework's preferred kernel.** `H_coth`'s one coincidence is `c₀ = 0`
predicting `p = 0.33007`, which is `1/3` to **0.34 σ**. It survives only at
`δ = 0`:

| | `p` at `c₀ = 0` | distance from 1/3 |
|---|---:|---:|
| `δ = 0` | 0.33007 | **0.34 σ** |
| `δ = 0.20903` (measured, local) | 0.06522 | **28.19 σ** |

**Not extrapolated.** That probe explicitly refuses to carry its three-point
decline across the series — *"Extrapolating a three-point decline across a
factor of ten in `A` would be a fit"* — and the refusal is honoured here:
`δ(A=3→4)` is used as a **measured local scale**, showing the confound is of
order the signal, never as a value for `δ` over `A = 3…63`. Nothing is
corrected by it.

`qou-u3vw` supplies a fourth leg — with a fixed local Borromean configuration
the `A`-dependence could sit in the per-component flux rather than in the
separation at all. One measured scalar, four unknowns.

## Scope

- **(b) structural, UNTOUCHED.** Round 6's O2 exclusion of the unsubtracted
  kernel is an argument from `∫Δu = 0` with no data in it. Nothing here bears
  on it.
- **(a) scope-limited negative on a TEST.** The κ(A) series, with the Coulomb
  unit frozen at `A = 3`, cannot rank kernels. This is about what the
  measurement resolves, not about any hypothesis being true or false.
- **(a) scope-limited negative on the BALL LAW.** The additive hyperbolic-ball
  law fails on this series at every kernel scanned. Both inputs are
  assumptions, so what is excluded is the **conjunction**; no structural claim
  is made.
- **Prior art, cited not claimed.** The `B_pp` drift is established by PR
  #6336 / `qou-23dn`. New here: its log-slope form, its 80 % share, and what
  it does to the 1/3 coincidence.

**Not claimed.** That any kernel is correct. That `p = 0.187` is the
separation exponent. That the metric Coulomb pairing `⟨A₁, J₂⟩` fails — it is
untouched, exactly as rounds 3 and 6 left it.

## What this changes for 4-B

Object **4-B** of [`sm-eightfold-derivation-cheat-sheet.md` §4](../sm-eightfold-derivation-cheat-sheet.md)
stays rank 1 and stays open. Round 6 closed with *"the route is identified, the
kernel is not, and the separation law is imported — three distinct gaps where
the front had been carrying one."* That count is right and the gaps are not
independent: they **share a single measured constraint**, and no further
scoring against κ(A) can separate them.

The constructive form:

> Derive any **two** of {kernel log-slope `s`, separation exponent `p`,
> strong-bond drift `δ`} and the third is predicted by
> `s·p + δ = 0.2605`.

That is falsifiable and it replaces "score more kernels". The cheapest leg is
`δ` — a compute question about `B_pp` at higher `A`, not a geometry question,
already answered in sign and low-`A` scale by PR #6336. Extending it to
`A = 5, 6` (that probe's own named next step) would do more for this front
than any further kernel.

Round 6's own named next step — the zero-mean Green's function of the actual
fibre — remains worth doing, but this changes what it would buy. It would fix
`s`, and therefore *predict* `p`; it would **not** adjudicate the contest,
because the contest has one degree of freedom and its members all fit it.
