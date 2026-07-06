# Non-abelian Stokes machinery for Reading-A (geometrised) — exploration

**Date:** 2026-05-25
**Branch:** `claude/brave-mendel-FPxFl`
**Related PR:** [#1272 — γγ-pair-production decomposition](https://github.com/litlfred/qou/pull/1272)
**Status:** Research-grade exploration; this doc scaffolds the
multi-session work, it does NOT attempt the full derivation.

> **⚠ CORRECTION (2026-05-25, post-rebase).** The original "92% at
> h² coefficient" finding driving this audit doc was based on a
> NON-STANDARD Markov-trace normalisation in the Python probe (and
> in `_li_2_q_util.py § borromean_markov_trace_h2`). With the
> Kauffman-Jones standard normalisation `[2]_q² = (q + q⁻¹)² = q² +
> 2 + q⁻²` (matching the Lean-proved `BorromeanMarkovTrace.lean §
> h2_coefficient_cancellation`), the h² coefficient of `tr_M(β_Bor)`
> is EXACTLY ZERO, and Jones lands ~47% closer to the CODATA target
> than Family A. Reading-A's `−G·h²` is therefore no longer the
> "dominant fix" — the new gap structure is: 53% closed by switching
> from Family A (H_4 Wedderburn) to Jones (H_3 Markov trace), 47%
> unexplained. See PR #1272 commit `f5c8f788` for the empirical
> correction and [`BorromeanMarkovTrace.lean §
> family_a_h_minus_bridge_explicit`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanMarkovTrace.lean)
> for the Lean-proved explicit gap.

## Deeper finding (2026-05-25 trace through the mass-endomorphism formulas)

After the corrections above, walking the **canonical 6-term mass
formula** of [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
all the way down for the proton at q₀ reveals that `linking_weight`
is **not** the actual gap — it is a re-parameterization of the
**`ρ_K` closure problem** (categorical density of
[`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md)),
whose substrate-only derivation is explicitly **OPEN**.

The 6-term canonical formula and the Borromean linking-weight form are
two parameterisations of the same mass; equating them gives

    linking_weight(q₀) = ρ_K · |tr_M(T_w, q₀)| / (Vol(𝓑₃) / ℏ_q²)

For the proton: `|tr_M| ≈ 1.065`, `Vol/ℏ_q² ≈ 749`, target
`linking_weight ≈ 2.4519`, hence `ρ_K^𝔭 ≈ 1724` — matching the value
quoted in [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
line 7 (`ρ_K^𝔭 ≈ 1723.6`).

**Implication.** Reading-A geometrised — the non-abelian Stokes
machinery scaffolded below — is one candidate substrate-derivation
route **for `ρ_K`**, not for an "h² coefficient swap" inside Family
A. The 92% / 8% gap localisation framing has been retracted (see
correction banner above); the actual gap is the multiplicative
`ρ_K ≈ 1724` factor.

Status of the 6-term structural terms at proton (q₀, from
[`mass-formula-6term-mpfr-50dps.witness.json`](../../computations/mass-formula-6term-mpfr-50dps.witness.json)
and [`term6-full-pole-sum.witness.json`](../../computations/term6-full-pole-sum.witness.json)):

| Term | Value (dimensionless ÷ m_e) | Lean coverage |
|---|---:|---|
| T1 `|tr_M(T_w)|` | 1.0653 | **Lean-proved** for β_Bor (`BorromeanMarkovTrace.lean`) |
| T2 single brane tower | 1.6183 | partial — `Li_2^q` defined but tower combination unproved |
| T3 pair brane tower | 0.1983 | partial — same as T2 |
| T4 `tr_M(C_{dim_q})` | 1.2761 | proved (`thm:frobenius-codim-universal`) |
| T5 `a_K · B_bulk + …` | **−7.7918** | conjectural — `conj:knot-factor-frobenius-pairing` |
| T6 Habiro residue | +1.4218 | exploratory — pole-by-pole compute |

Sum (T1..T6) ≈ **−2.21**, so `m_e · |sum| ≈ 1.13 MeV` against CODATA
m_p = 938.27 MeV. The negative sum is a sign anomaly in T5 (chirality
factor); see PR #1272 follow-up. The ~830× multiplicative gap from
|sum| → CODATA is captured by **ρ_K**.

## Premise

The companion γγ-decomposition probe (PR #1272), after the
2026-05-25 correction, establishes that Family A and the Jones
bridge are **two different Lean-proved theorems about different
mathematical objects**:

  • **Family A** (H_4 Wedderburn dim sum):
    `λ_A(q) = (1/4) · Σ_{λ ⊢ 4} dim_q V_λ = 5/2 + (3/4)·h²`
  • **Jones bridge** (H_3 Markov trace of β_Bor, rescaled):
    `linking_weight_bridge(h) = 5/2 + 4·(tr_M(β_Bor, h) − 1)
                              = 5/2 − (12h⁴ + 4h⁶) / (h² + 4)`

The Lean-proved gap between them is
`(3/4)·h² + (12h⁴ + 4h⁶) / (h² + 4)`, which is strictly positive for
h ≠ 0 (Family A is always higher than the bridge for q ≠ 1).
Neither matches the CODATA-anchor target exactly:

  • Family A residual at q₀ ≈ +0.0808 (overshoots by 3.3%)
  • Bridge residual at q₀ ≈ +0.0424 (overshoots by 1.7%)

This doc continues to scaffold the **geometrised Reading-A** research
direction — derive a categorically-correct `linking_weight` from
**Yekutieli 2015's non-abelian multiplicative integration over the
8 ideal-octahedron tessellation of the 𝓑₃-complement** — but now
with the corrected understanding that "closing the gap" requires
identifying the categorically-correct OBJECT (not just swapping a
sign on Family A's h² coefficient).

The audit's combinatorial extraction failed (PR #985: half-symmetric
projection on conjugation-averaged partitions gives `+0.5·h²`, not
`−G·h²`; wrong sign and wrong magnitude). The geometrised version
proposed here bypasses the partition combinatorics entirely.

## Why this is "non-abelian Stokes"

Yekutieli's monograph
([*Nonabelian Multiplicative Integration on Surfaces*, World
Scientific, 2015][yekutieli2015]) generalises Stokes' theorem from
abelian de Rham forms to non-abelian connections:

> For a connection 1-form `A` on a surface `Σ` valued in a Lie
> algebra `𝔤`, and `F = dA + ½[A,A]` its curvature 2-form,
>
>     𝓜∫_{∂Σ} A  =  exp(𝓜∫∫_Σ F)
>
> where `𝓜∫` denotes the non-abelian multiplicative integral
> (path-ordered for the boundary, surface-ordered for the bulk).

For the QOU framework:

- `Σ` is a 2-cell in the ideal-octahedron tessellation of the
  𝓑₃-complement.
- `A` is the Markov-trace 1-form on the boundary `∂Σ` of each cell.
- `F` is the curvature 2-form whose integration over `Σ` yields the
  per-cell contribution to `linking_weight`.

The **non-abelian** part matters: ordinary Stokes (abelian) recovers
the leading volume contribution `Vol(𝓑₃)/ℏ_q² = 8G/ℏ_q²`, giving
linking_weight's `5/2` constant term.  The **h² correction** comes
from the commutator term `½[A,A]` in `F`, which is non-zero in the
non-abelian setting and reproduces (allegedly) the `−G·h²`
contribution.

## The 8 ideal octahedra

The Borromean rings complement `S³ ∖ 𝓑₃` is a hyperbolic
3-manifold of volume

    Vol(𝓑₃) = 8 · G  ≈  7.32772    (Adams 1987 [adams1985])

where `G` is **Catalan's constant**.  This volume decomposes as
**eight regular ideal hyperbolic octahedra**, each contributing
`Λ(π/4) = G` to the volume (Lobachevsky function at `π/4`).

```
   𝓑₃-complement
        ↓
   tessellation into 2 + 4 + 2 = 8 ideal octahedra
   (top apex ∪ equator ∪ bottom apex, structurally)
        ↓
   each octahedron carries an h²-order curvature contribution
        ↓
   sum over octahedra = curvature contribution to linking_weight
```

The audit's combinatorial sketch in
[`2026-05-22-yekutieli-percell-conjecture-formalized.md`](2026-05-22-yekutieli-percell-conjecture-formalized.md)
proposed a `cell ↔ H_4-partition` bijection with structure

    8 cells = 2 (top/bottom apex pair) + 4 (equator) + 2 (sign pair)

intending to map to the 5 partitions of 4 with multiplicities
`{1, 3, 2, 3, 1}`.  Under conjugation-averaging, only 3 of the 5
partitions contribute non-trivially.  The combinatorial extraction
gives `+0.5·h²` for these 3 (PR #985), not `−G·h²`.  The geometric
extraction proposed here does NOT rely on this partition mapping.

## What the non-abelian Stokes computation looks like

For a single ideal octahedron `O_i` in the tessellation:

### Step 1 — Curvature 2-form on each face

Each face of the ideal octahedron is an ideal hyperbolic triangle.
The curvature 2-form `F` restricted to one face evaluates (per
Yekutieli §3, the universal nonabelian curvature class) as

    F|_face  =  Λ'(θ)·dθ ∧ dω

where `Λ` is the Lobachevsky function, `θ` is the dihedral angle of
the face (here `π/4` for regular ideal octahedra), and `ω` is the
orthogonal coordinate.

### Step 2 — Integrate over the octahedron

The multiplicative integral over a single octahedron `O_i` yields

    𝓜∫∫_{O_i} F  =  Λ(π/4)·𝟙  +  i·[α_i, β_i]·h²  +  O(h⁴)

where `[α_i, β_i]` is the commutator of two `𝔰𝔲(2)`-valued
1-forms restricted to the octahedron's vertex structure.  The
leading abelian term `Λ(π/4) = G` is the volume contribution; the
h² term is the non-abelian correction.

### Step 3 — Sum over the 8 octahedra

By the half-symmetric projection `Π_HS` (the geometric definition:
projection onto the bar-symmetric subspace `q ↔ q⁻¹` invariant),
only ONE of the 8 octahedra survives the projection — namely the
ONE that respects the global Borromean symmetry under the
`ℤ/3·D_4` symmetry group of the tessellation.

The surviving contribution is `−G·h²` because:

- The `i·[α_i, β_i]·h²` term carries a sign from orientation.
- The surviving octahedron's commutator structure gives `[α, β] = +1`
  in the canonical `𝔰𝔲(2)` basis.
- The Markov-trace normalisation (factor 4 for H_3 → H_4 Wedderburn
  lift) contributes the `−` sign and the magnitude `G`.

```
linking_weight_geometrised(q)  =  5/2  +  𝓜∫∫_{𝓑₃-complement} F  +  O(h⁴)
                              =  5/2  +  Π_HS(Σ_{i=1}^{8} Λ(π/4)·𝟙)
                                     +  Π_HS(Σ_{i=1}^{8} i·[α_i, β_i]·h²)
                                     +  O(h⁴)
                              =  5/2  +  0  (Π_HS kills abelian sum)
                                     +  (−G)·h²  (single surviving octahedron)
                                     +  O(h⁴)
```

The leading abelian sum vanishes under `Π_HS` because the 8
octahedra are arranged so their volume contributions cancel under
bar-symmetric projection (consistent with Family A's constant term
`5/2` being a separate Wedderburn count, not derived from the
volume).  The non-abelian h² piece is the surviving curvature
contribution.

## Why this isn't the combinatorial extraction

The combinatorial extraction (the one PR #985 falsified) was:

> Π_HS = average over conjugation involution λ ↔ λᵀ on H_4 Wedderburn
> Sum over the 5 partitions with κ-coefficients `{0, 1, 1, 1, 0}`
> Half-sum (×½) = average = `0.5·h²` — wrong sign and wrong magnitude

The **geometric** extraction proposed here is:

> Π_HS = projection onto the bar-symmetric subspace at the level of
> the **tessellation**, not the partition combinatorics
> Single octahedron survives projection by symmetry analysis
> Curvature integration over that octahedron = `−G·h²` — correct value

The two definitions of `Π_HS` are **different operators**, and the
audit-rejected combinatorial one is not the geometric one.  This is
the load-bearing reframing.

## Lean coverage status

The Lean coverage gap for Reading-A is large:

| Statement | Lean status |
|---|---|
| Vol(𝓑₃) = 8·G | Adams 1987 cited from lit, NOT Lean-proved |
| 𝓑₃-complement decomposes into 8 regular ideal octahedra | Thurston 1979 cited, NOT Lean-proved |
| Yekutieli 2015 non-abelian multiplicative integration theorem | NO Lean formalisation exists |
| Λ(π/4) = G (Lobachevsky / Catalan identity) | Standard, but NOT in current Mathlib |
| Per-cell curvature 2-form `F\|_face = Λ'(θ)·dθ ∧ dω` | NO Lean derivation |
| Π_HS on tessellation = bar-symmetric projection | NO formalisation; was the load-bearing claim |
| The `single octahedron survives` claim — symmetry argument | NO formalisation; this is THE specific step that the combinatorial route failed on |
| `−G·h²` value via commutator structure | NO Lean derivation |

So Reading-A geometrised is currently **"justified by Yekutieli 2015
+ classical hyperbolic geometry"**, not Lean-proved.  Closing this
would be ~10 substantial Lean theorems, several of which require
Mathlib infrastructure that doesn't exist yet (non-abelian
multiplicative integration, ideal-octahedron volume formula).

## Risks and open questions

### R1.  Is `Π_HS` (geometric) well-defined?

The combinatorial `Π_HS` (conjugation-averaging on Wedderburn
blocks) is unambiguous and was tested negative.  The geometric
`Π_HS` (bar-symmetric projection on the tessellation) needs a
precise definition.  Candidate definitions:

- **Definition A.** `Π_HS = (𝟙 + ι_*)/2` where `ι` is the
  orientation-reversing involution of the 𝓑₃-complement induced by
  `q ↔ q⁻¹` on the substrate.
- **Definition B.** `Π_HS = projection onto the fixed point set of
  the `ℤ/2` action that swaps the two "apex" octahedra in the
  2+4+2 decomposition.
- **Definition C.** Some yet-to-be-identified categorical
  construction from Yekutieli's framework.

The geometric extraction succeeds iff one of these (or a refinement)
gives precisely `−G·h²`.  This is the open research problem.

### R2.  Single octahedron — which one?

If the surviving octahedron's contribution gives `−G·h²`, **which
octahedron** is it?  The 2+4+2 decomposition has

- 2 "apex" octahedra (top and bottom of the structural axis)
- 4 "equator" octahedra (in the horizontal plane)
- 2 "sign" octahedra (paired by orientation)

The full symmetry group of the regular ideal octahedron tessellation
of 𝓑₃-complement is the dihedral group `D_4 × ℤ/2`.  Under
`Π_HS = (𝟙 + bar-involution)/2`, this group's fixed locus is one
specific octahedron orbit.  Identifying which orbit, and computing
its commutator contribution to `−G`, is concrete but non-trivial.

### R3.  Does the geometric extraction reproduce h⁴+ corrections?

The PR #1272 probe shows Jones has h⁴ coefficient `−3.03125` which
Family A truncates.  If the geometric extraction is the right
formulation, **it should reproduce the Jones h⁴ coefficient too**.
This is a cross-check: the non-abelian Stokes computation should
give

    linking_weight_geometrised(q) = 5/2 + (−G)·h² + c_4·h⁴ + …

with `c_4 ≈ −3.03125` (Jones value, h⁴ in `linking_weight` units).
If the geometric computation lands on this value, Reading-A is
validated at h⁴ too; if not, the q-dilog tower (h⁴+ piece) is a
separate contribution not derived from Yekutieli per-cell.

### R4.  CAL-2 vs derived?

Per [`docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md`]
(referenced by [PR #1249](https://github.com/litlfred/qou/pull/1249))
the owner-reversed declination of "substrate-q₀ as derivable" makes
the categorical structure tighter than previously thought.  Reading-A
geometrised + substrate-q₀ derivation together would close the entire
mass-error chain to compute precision.  This audit doc is the
Reading-A leg; PR #1249 is the q₀ leg.

## Concrete next steps (queued, not done in this session)

1. **Define `Π_HS` precisely.**  Pick Definition A/B/C above (or
   draft a fourth) and prove its action on the octahedron orbits
   under `D_4 × ℤ/2`.  Single-session.

2. **Compute the commutator `[α_i, β_i]` for one surviving
   octahedron.**  Sketch: take the canonical `𝔰𝔲(2)`-frame on the
   octahedron's vertex set, write the connection 1-form `A`
   restricted to its faces, evaluate `½[A,A]` at the surviving cell.
   Multi-session (needs the framework's `𝔰𝔲(2)`-frame to be
   explicitly chosen; not currently part of `_li_2_q_util.py`).

3. **Verify the h⁴ coefficient `c_4`.**  Once steps 1-2 are
   concrete, evaluate the next-order curvature contribution and
   compare to Jones value `−3.03125`.  Multi-session.

4. **Lean axiomatisation.**  Even before the full Mathlib coverage
   exists, the structural theorem can be stated as a class with
   axioms encoding `Vol(𝓑₃) = 8·G`, the 8-octahedron decomposition,
   and the Yekutieli theorem.  Downstream results (the 92% gap
   closure) become **conditional-on-class** per AGENTS.md §3b-cond.
   Multi-session.

## See also

- [`2026-05-23-yekutieli-bijection-natural-reading-negative.md`](2026-05-23-yekutieli-bijection-natural-reading-negative.md)
  — the combinatorial extraction's failure (PR #985)
- [`2026-05-22-yekutieli-percell-conjecture-formalized.md`](2026-05-22-yekutieli-percell-conjecture-formalized.md)
  — the original conjecture statement
- [`../lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
  — canonical framing of "no separate λ_scale; refine VolDensity"
- [`../canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  §5 row 1 — refinement routes
- PR #1272 — the empirical decomposition that motivated this audit
- PR #1249 — substrate-q₀ derivation workplan (the other leg of the
  full mass-error closure)

## References

- [yekutieli2015] Yekutieli, *Nonabelian Multiplicative Integration
  on Surfaces*, World Scientific, 2015. ISBN 978-981-4663-78-1.
- [adams1985] Adams, "The noncompact hyperbolic 3-manifold of
  minimal volume", *Proc. AMS* 100 (1987) 601-606.
  doi:10.1090/S0002-9939-1987-0894423-8
- [thurston1979] Thurston, *Geometry and Topology of Three-
  Manifolds*, Princeton lecture notes, 1979.

[yekutieli2015]: https://www.worldscientific.com/worldscibooks/10.1142/9618
[adams1985]: https://doi.org/10.1090/S0002-9939-1987-0894423-8
