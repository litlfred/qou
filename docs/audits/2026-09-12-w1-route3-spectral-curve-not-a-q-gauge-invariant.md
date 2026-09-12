# Route 3's spectral curve does not exist: a Seiberg–Witten cubic is not a q-gauge invariant

**Date:** 2026-09-12 · **Bean:** `qou-ar4v` · wall `qou-d8de` · follows `qou-ei4q` (#7185), `qou-hmrm` (#7114), `qou-lmnq` (#6769), `qou-7fnr` (#6738), `qou-1z28` (#6695)
**Lean:** [`QOU/Mass/QGaugeSpectralRigidity.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/QGaugeSpectralRigidity.lean) — sorry-free, `scripts/lean-shadow-verify.sh` exit 0, `#print axioms` on all 11 declarations gives `propext / Classical.choice / Quot.sound` and no `sorryAx`
**Probe:** [`w1_route3_qgauge_spectral_rigidity_probe.py`](../../computations/probes/w1_route3_qgauge_spectral_rigidity_probe.py) — 31/31; exact sympy over ℚ (and ℚ(i)) for every conclusion-bearing step; three controls; no witness by design
**Sources read, not paraphrased from memory:** RSZ Astérisque 355 §2.1.1 (`library/arxiv-0903.0853v3`), DVRSZ §2.4–2.5 (`library/equations-aux-q-differences`)
**Cited, not re-derived:** the q-freeness of Σ ([`2026-06-25-z2bn-prolongation-qdifference-constraint.md`](2026-06-25-z2bn-prolongation-qdifference-constraint.md)); the lift identity and the genus (#7114/#7185); the base-dilation rigidity (#6769)

## What was asked

W1 (`qou-d8de`) wants a q-difference prolongation `D_q` on the colour spectral
curve `Σ : P(X,z) = 0`, `λ_SW = X dz`. Routes 1 and 2 are closed. The bean's own
next step is route 3, verbatim:

> *"pick route 3 (import the q-difference D-module framework from the literature)
> before attempting routes 1–2, so `D_q` is built on a real definitional
> foundation rather than an ad-hoc operator."*

This tranche performs that import and measures whether its obvious instantiation
exists. It does not.

## What route 3 requires — read from the sources we hold

Ramis–Sauloy–Zhang, *Local analytic classification of q-difference equations*,
Astérisque 355 §2.1.1:

> *"We call difference field a pair `(K, σ)`, where `K` is a (commutative) field
> and `σ` a field automorphism of `K`."*

Di Vizio–Ramis–Sauloy–Zhang, *Équations aux q-différences* §2.5: a q-difference
module is a pair `(M, Φ)` of a finite-dimensional `K`-space and a `σ_q`-linear
automorphism. A **system** `σ_q X = A X` is read modulo **gauge**, and the gauge
law is DVRSZ eq. (2.4.1), verbatim:

> *"la même transformation de jauge ramène le système (2.3.1) au système
> `σ_q Y = B Y`, où `B = (σ_q F)⁻¹ A F`."*

That one equation is the whole content of this tranche.

## The finding — scope (b), invariant cited

In the **differential / Hitchin** case a gauge acts on a Higgs field by
conjugation `Φ ↦ F Φ F⁻¹`, so `det(X·1 − Φ)` is gauge-invariant and the
Seiberg–Witten spectral curve is a well-defined invariant of the object. That is
**verified here, not assumed** — probe T3 confirms `det(X·1 − FΦF⁻¹) = det(X·1 − Φ)`
exactly for a symbolic `Φ` and a concrete `F ∈ GL₃(ℚ)`.

Eq. (2.4.1) is a *twisted* action. With the monomial gauge `F = z^k·1`,

  `B = (σ_q F)⁻¹ A F = ((qz)^k)⁻¹ · z^k · A = q^{-k}·A`   (probe T1, exact)

so the scalars a monomial gauge can apply to the system matrix are exactly `q^ℤ`,
and a scalar multiple **moves** the characteristic cubic: its `X^{3−k}`
coefficient picks up exactly `t^k` (`charCubic_smul`; probe T2). A spectral cubic
is therefore an invariant of a q-difference module only if it is stable under
`X ↦ t·X` for every `t ∈ q^ℤ`.

`weight_relations` (sorry-free) says what stability costs, coefficient by
coefficient:

  `a₀(1 − t³) = 0`,  `a₁·t·(1 − t²) = 0`,  `a₂·t²·(1 − t) = 0`

and `coeffs_vanish_of_scaling` draws the consequence: if `t ≠ 0` and none of
`t, t², t³` is `1` — in particular **any real `t > 1`**
(`no_scaling_survives_of_one_lt`) — then `a₂ = a₁ = a₀ = 0`.

> **The only monic cubic stable under a non-root-of-unity gauge scaling is
> `X³ = 0`.**

This is general. It is not a fact about this `Σ`, and it is the reason the result
is worth recording independently of the colour curve.

For the colour cubic the conclusion is immediate and does not need the general
theorem: the fibre over `z = 0` is `X³ + X² + X + 1`, whose three non-leading
coefficients are all `1`, so no weight can be absorbed and `t = 1`
(`gauge_scaling_fixes_colorCubic_iff`; probe T5.2).

## The joint move, which no prior tranche reaches

#6769 moves the **base** (no dilation `z ↦ l·z` preserves the branch locus);
this file moves the **fibre**. Neither covers a q-operator that does both at once,
so `colorCubic_weighted_rigid` proves the joint statement:

  `P(λX, μz) = ν·P(X,z)`  ⟹  `λ = μ = ν = 1`

(probe T6.1 confirms the unique solution by exact elimination).

## Read as descent to the Tate curve

RSZ §6.3 associates to a q-difference module a bundle on `E_q = ℂ*/q^ℤ`. For the
spectral data to live there, each fibre's root set must be `q`-invariant. Over
`z = 0` the cubic factors as `(X+1)(X²+1)`, roots `{−1, i, −i}` — all nonzero, and
every ratio of two of them is a 4th root of unity (probe T9, exact over ℚ(i)). So
`q·B = B` forces `q⁴ = 1`, and `q₀⁴ = 1.51795…  ≠ 1`. **The `z = 0` fibre does not
descend to `E_q`.**

## Why this is structural, not a coincidence of this cubic

`P` **is** quasi-homogeneous — for the **paired** action. That is exactly why the
palindromic involution lifts (#7185): `z³·P(X/z, 1/z) = P(X,z)`, because the
coefficients are truncated geometric sums `a_k = 1 + z + ⋯ + z^{3−k}`, so
`a_k(1/z) = z^{k−3}a_k(z)` and the `X`-scaling is paid for by the `z`-inversion.

The gauge asks for an `X`-motion with **no compensating `z`-motion**. For that to
be absorbable every `a_k` would have to be a *monomial* in `z`; they have 2, 3 and
4 terms respectively (probe T7). There is simply no weight available.

**And this is the same property that created the need.** The 2026-06-25 z2bn audit
excludes the classical `d/dz` prolongation because Σ is **q-free** — a q-free curve
has q-free classical periods, while the anchor `a_D^{(3)} = (q+1)²/(3q)` is
q-dependent — and that is what forces the operator into the q-difference class. The
q-freeness that forces the class is the q-freeness that leaves the gauge nothing to
absorb. The two results are a pincer on the same property, approached from opposite
sides.

## Controls — three, because a negative from an elimination is only evidence if the same elimination can return something else

| control | what it shows |
|---|---|
| **T3** conjugation, the differential/Higgs case | the same determinant computation **certifies invariance** when invariance is there |
| **T4.7** `t` a primitive cube root of `1` | the `a₀` weight relation goes **vacuous** — the method can say "not forced" |
| **T5.3 / T6.2** the quasi-homogeneous `X³ + z³` | returns **three** scalars, and a **1-parameter family** for the joint move — a singleton is not an artifact |

## Scope — what is NOT excluded

Fixed before the argument was run:

- **Route 3 is not dead.** A q-difference module over `(ℂ(z), σ_q)` is a perfectly
  good object, and this corpus already uses RSZ that way for *scalar* kernels
  ([`2026-07-20-qlift-routeA-rsz-invariants.md`](2026-07-20-qlift-routeA-rsz-invariants.md)
  reads Newton polygons and slopes off `L1`/`L2` directly). What is excluded is
  reading `Σ` as such a module's gauge-invariant characteristic-polynomial curve.
- **Σ may still enter route 3 as something other than a char-poly curve** — Newton
  polygon, slopes, the Birkhoff connection matrix, the `E_q` bundle of RSZ §6.3.
  Those are not touched here.
- **One may always fix a gauge and compute.** The objection is only that `Σ` would
  then not be an invariant of the module — which is what "the spectral curve of"
  means.
- `D_q` is **not constructed.** No fit, nothing wired.

**The bridge is an assumption and is carried as one.** *"The sought `D_q` would
have `Σ` as its spectral curve"* is what `λ_SW = X dz` sets up and what the phrase
*"a q-difference prolongation of `Σ`"* means — but it is a hypothesis, stated as one
in the Lean docstring and in the probe, and never used as a fact. If a future
tranche builds `D_q` with `Σ` playing a different role, nothing here obstructs it.

**Not formalised, prose only:** the covering/gauge dictionary — that "a gauge
transformation of the q-difference system" and "a change of the `X` coordinate over
the base" are the same move — is DVRSZ's, cited above, and is not re-proved in Lean.
The Lean proves the rigidity that the dictionary is applied to.

## One defect worth recording

`sympy.Poly(E, X).all_coeffs()` **silently drops the leading slot** when the
leading term cancels. In T4 the `X³` coefficient cancels identically — that is the
whole point of the weight computation — so the returned list had three entries, not
four, and the probe was comparing `a₂`'s relation against `a₁`'s slot. It surfaced
as an `IndexError` on the fourth read rather than as a wrong answer, which is luck:
had the cubic been a quartic the same bug would have produced a plausible,
consistently-shifted, wrong table. The probe now reads coefficients by degree
(`E.coeff(X, k)`), which cannot shift.

## How this composes

| where | closed by |
|---|---|
| route 1, base coordinate `z` | #6695 |
| route 1, ramified local coordinate `t` | #6738 |
| route 1, Σ itself (dilations) | #6769 |
| route 2, `q` = the local fibre-monodromy eigenvalue | #7114 |
| every base automorphism of `P¹` | #7185 |
| **route 3, Σ as a q-difference module's spectral curve** | **this tranche** |

Each tranche has replaced a specific negative with a more structural one. This one
leaves the route open while removing the reading of it that everything upstream was
pointing at — so the question it hands forward is sharper than the one it received:
**if `Σ` is not the spectral curve of the q-difference module, what is it?**

## Reproduce

```bash
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/w1_route3_qgauge_spectral_rigidity_probe.py

scripts/lean-shadow-verify.sh \
  content/quantum-observable-universe/lean/QOU/Mass/QGaugeSpectralRigidity.lean
```

`scripts/precision-gates.sh --changed` reports 11 gates RED. **None is
attributable to this branch, and that is measured rather than asserted:** a control
run with the new probe moved out of the tree produces a byte-identical `RED:` line,
and the branch diff carries zero `.witness.json`.
