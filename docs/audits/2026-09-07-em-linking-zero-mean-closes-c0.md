# The zero-mean condition closes `c₀` — the kernel is determined by the fibre volume

**Date:** 2026-09-07 · **Bean:** `qou-17mq` ·
**Scope:** a derivation, plus an untestable prediction stated as such. Nothing
fitted, nothing wired, no hypothesis promoted.

Probe: [`em_linking_zero_mean_closes_c0_probe.py`](../../computations/em_linking_zero_mean_closes_c0_probe.py)
(witness `em-linking-zero-mean-closes-c0.witness.json`, 7 assertions, all
passed).

Third in today's sequence, after
[the degeneracy](2026-09-07-em-linking-kernel-and-exponent-are-degenerate.md)
(the series measures one scalar) and the quotient-correction derivation (the
one-term family **is** the exact quotient kernel to `O(r²)`, and `c₀` is its
Robin constant).

## The claim

`c₀` is not a free parameter. Round 6 scans it over a 140-member grid and
calls the family *"the simplest realisation of the zero-mean condition, not
the exact Green's function of a quotient"* — and that scan is precisely what
leaves the kernel unidentified.

But the admissible kernel **is** the zero-mean one, so

$$\langle\kappa\rangle_M \;=\; \langle\coth\alpha\rangle_M - c_0 \;=\; 0
\qquad\Longrightarrow\qquad c_0 = \langle\coth\rangle_M ,$$

a property **of the manifold**, not a modelling choice. On a geodesic ball in
`H³` the mean is elementary, because `coth·sinh² = cosh·sinh`:

$$\langle\coth\rangle_M = \frac{1}{V}\int_0^R \coth r\,\cdot 4\pi\sinh^2 r\,dr
= \frac{4\pi}{V}\int_0^R \cosh r \sinh r\,dr = \frac{2\pi\sinh^2 R}{V},$$

and with `V = π(sinh 2R − 2R)`,

$$\boxed{\;c_0(R) = \frac{\sinh^2 R}{\sinh R\,\cosh R - R}\;}$$

with **no free parameter**. Checked against direct quadrature of `⟨coth⟩` at
`R = 0.25, 0.5, 1.1103, 2, 4`: worst relative gap **1.567e-39**. Both limits
correct — `c₀ → 1` as `R → ∞`, which is exactly the infinite-volume boundary
round 6 identifies as its best admissible member and *scans to*; and
`c₀ → ∞` as `R → 0`.

## What it determines

Fixing the kernel predicts the separation exponent (the degeneracy result), so
a fibre volume now yields a **prediction** rather than a fit:

| fibre | vol | `c₀` **derived** | admissible? | `p` predicted | `s·p` | κ-rms | `A_zero` |
|---|---:|---:|---|---:|---:|---:|---:|
| L6a4 / Borromean (³He) | 7.3277 | **1.56994** | yes | 0.15288 | 0.25949 | 2.870 % | 9.09e3 |
| knot 8₁₁ (³H) | 8.2863 | **1.53094** | yes | 0.15478 | 0.25953 | 2.862 % | 9.85e3 |
| figure-eight 4₁ | 2.0299 | **2.13403** | yes | 0.13004 | 0.25897 | 2.965 % | 4.40e3 |

## Three non-trivial checks

**1. Admissibility is derived, not imposed.** O2 requires `c₀ ≥ 1`. All three
hyperbolic volumes the corpus carries land there on their own. Nothing in the
construction knows about the admissible region.

**2. It survives round 6's own falsification test.** For `c₀ > 1` the kernel
changes sign at `α* = arccoth(c₀)`, hence at a finite `A_zero`. Round 6
contradicted **48 of its 140** scanned members because that crossing fell
inside `A ∈ [3, 63]`, where every measured κ is strictly positive (min 1.4020).
The derived members put it at `A ~ 4×10³–10⁴` — sign-changing as O2 demands,
with the crossing far beyond the heaviest known nuclide (`A = 294`).

**3. It is robust across the A=3 links.** L6a4 and 8₁₁ differ by **13.1 %** in
volume and give `c₀` within **2.55 %** and `p` within **1.24 %**. The answer
does not hinge on which A=3 link is taken as the fibre.

A fourth, `s·p = 0.2595` against the measured `0.26050`, **must** hold by the
degeneracy — it checks the arithmetic and is not independent evidence.

## The objection this most invites does not reach the conclusion

The ball-vs-quotient identification is the single model input. Its leverage is
measured rather than argued:

$$\frac{d\ln p}{d\ln V} = 0.10279$$

| `V/V₀` | 0.25 | 0.5 | 1 | 2 | 4 | 10 |
|---|---:|---:|---:|---:|---:|---:|
| `c₀` | 2.1936 | 1.8358 | 1.5699 | 1.3775 | 1.2427 | 1.1295 |
| `p` | 0.12804 | 0.14113 | 0.15288 | 0.16279 | 0.17060 | 0.17783 |

So the assumed fibre volume would have to be wrong by **2.53×** to move `p` by
10 %, and by **1965×** to reconcile the derived `p` with the imported Euclidean
`1/3` (which is 2.18× the derived value). A ball-vs-quotient error is at most a
factor of a few.

## What this does NOT do

**It identifies the kernel; it does not confirm it.** The predicted
`p ≈ 0.153` **cannot be tested on this series** — the degeneracy result
establishes that the series constrains only the product `s·p`. A prediction the
available observable cannot check is still a prediction, falsifiable by any
*independent* determination of the separation law. It is not evidence today.

Per the NO-FITTING directive, `p ≈ 0.153` is reported as an **output** and
deliberately not matched against any small rational.

## Model inputs, stated rather than buried

- **The mean uses a geodesic ball's distance distribution.** A closed
  hyperbolic quotient — still more a cusped complement — has a different one.
  This is the same one-term idealisation round 6 names, now used for what it
  can actually deliver: a number instead of a scan.
- **The corpus's volumes are cusped link-complement volumes**, used as ball
  volumes. That is an identification, not a theorem. All three are reported and
  **none is selected**; choosing whichever fit best would be a fit.

## Scope

- **Derived:** `c₀`, in closed form in the fibre volume. It was a scanned
  parameter; it is now determined.
- **Predicted but untestable here:** `p ≈ 0.153`.
- **Untouched, and load-bearing:** round 6's structural O2 exclusion of the
  *unsubtracted* `coth`. This derivation **depends** on it — without zero-mean
  there is nothing to close `c₀` with.
- **Not claimed:** that the kernel is confirmed; that `p = 0.153` is measured;
  that any corpus volume *is* the fibre volume.

## What is left on 4-B

The front's unknown count drops by one. Of `{s, p, δ}`:

- **`s`** — now determined by the fibre volume, via `c₀`.
- **`p`** — predicted at 0.153, untestable on this series.
- **`δ`** — still unmeasured beyond A=4 (`qou-gcmn`), and ~80 % of the one
  measured scalar.

`δ` is now the binding constraint on the whole front.
