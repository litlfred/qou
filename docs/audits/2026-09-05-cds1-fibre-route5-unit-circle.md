# Route 5 on the fibre: the locus is `|q| = 1`, exactly

**Bean:** `qou-cds1` / `qou-pdix` route 5.
**Probe:** [`computations/qbeta/qbeta_fibre_unit_circle_opens_route5_probe.py`](../../computations/qbeta/qbeta_fibre_unit_circle_opens_route5_probe.py) (5/5).
**Scope: (a)** for the arithmetic; the ellipticity criterion is an identity.

## Where this picks up

`e68347cc12` retargeted [`conj:im-q-physical-role`](../../content/quantum-observable-universe/mass-theory/conj-im-q-physical-role.md)
**to the fibre**: all three candidate roles for `Im(q)` are settled at `q₀` and
*"all three remain open on the fibre, where `q` is a formal variable and
`Im(q)` is unconstrained."*

Route 5 needs an **elliptic** generator — `det A > 0`, spectrum `±iθ` — because a
real-spectrum holonomy has character `cosh a ≥ 1` while the required correction
is below 1 (`HolonomySpectrumSignObstruction`, step 18). Step 19 refuted `Im(q)`
as the source **at the archimedean level**, reasoning from `Re q = 1.10998 > 1`.
This is the fibre question that leaves open.

## The fibre locus is the unit circle, and the reason is exact

Matching the Kohno–Drinfeld holonomy to the Hecke eigenvalues forces
`ħ = 2 ln q`, giving `det A = −(ln q)²`. Hence

```
det A > 0  ⟺  (ln q)² < 0  ⟺  ln q purely imaginary  ⟺  |q| = 1
```

At the real anchor, `ln q₀ = 0.10434` and `det A = −0.010887 < 0` — hyperbolic,
exactly the step-18 exclusion. On `|q| = 1`, `ln q = iφ` and `det A = +φ² > 0` —
**elliptic by construction**, with eigenphase `θ = |arg q|`.

So the unit circle is not one candidate locus among several. It is **the entire
solution set** of the condition that lifts the exclusion.

## It is the same locus the conjecture block already names

Candidate (i) of `conj:im-q-physical-role` is the **Kashaev regime** `|q| = 1`,
where `q̄ = q⁻¹` and the corpus's own chirality operation — the bar involution,
the mirror knot — coincides with complex conjugation. The block records the
substrate as sitting 18.83 % of `q₀` away from that circle.

Two independent requirements — ellipticity here, chirality there — select one
locus. Recorded as a structural correspondence, **not** as evidence for either.

## The Kashaev sublocus reduces to a question no measurement can answer

A root of unity `q = e^{2πik/N}` gives `θ = 2πk/N`, so it supplies the required
phase **iff `θ/2π` is rational**. Measured, `θ/2π = 0.009010923285895504`.

That is not decidable numerically — every real has rational approximations of
arbitrary accuracy. The continued-fraction convergents make the point rather
than settling it:

| `k/N` | `θ` | rel. err |
|---|---|---|
| 1/110 | 0.0571198664 | 8.9e-3 |
| **1/111** | **0.0566052730** | **−2.1e-4** |
| 42/4661 | 0.0566174175 | 2.1e-6 |
| 85/9433 | 0.0566172746 | −4.6e-7 |
| 1145/127068 | 0.0566173008 | −8.0e-11 |

The large-denominator rows fit better and mean nothing: a denominator is a free
parameter.

**`k/N = 1/111` is the only low-denominator candidate, and the target's own
uncertainty is larger than its miss.** Correcting the quoted target from the
form's value to the experimental one moved it by **4.0e-4**
([`2026-09-04-cds1-branch3-target-phase-provenance.md`](2026-09-04-cds1-branch3-target-phase-provenance.md));
`N = 111` sits at 2.1e-4, inside that band.

So **`N = 111` is not excluded — and equally is not evidence.** Per this arc's
own discipline a target may be checked *against*, never searched *on*. No search
for a reason `N` should be 111 was run, and none should be until something
independent selects it.

## A coincidence, flagged and not pursued

`2π/θ = 110.9764` sits 1.9e-4 from `100·q₀ = 110.9979`. These are different kinds
of object — an integer index against a dimensionless modulus, with a factor of
100 inserted by hand — and this corpus has documented precedent for exactly this
trap (the stale `−2.00973976` against `J_Hopf − ħ_q²`, agreeing to four decimals
while being different objects). Recorded so a later reader does not rediscover
it as new. No mechanism, no search.

## What this changes for `qou-cds1`

The fibre reading is not merely "open" — it has a **specific, exactly
characterised locus**, and the arc now has one arithmetic question rather than an
open search. What it does **not** have is a derivation: nothing here produces a
fibre element on `|q| = 1`, and nothing selects `N`.
