# The 1-loop `|det J|` is not a topological invariant — so `c_σ = 2^{−3/4}` is not derived by it

**Date:** 2026-08-07
**Probe:** `computations/probes/one_loop_triangulation_invariance_probe.py`
**Witness:** `computations/one-loop-triangulation-invariance.witness.json`
**Bears on:** PR #4571 / #4671 (Cluster B), `computations/whitehead_c_sigma_torsion.py`, bean `qou-pn5j`

## What was claimed

`whitehead_c_sigma_torsion.py` computes a 1-loop determinant over
(*N* − *c* independent edge equations) + (one meridian per cusp), sets
`|τ| = |det J|`, and reports

```
|τ(4_1)|  = √3        (c=1)
|τ(L5a1)| = 2^{5/2}   (c=2)
|τ(L6a4)| = 2^6 = 64  (c=3)
```

reconciling them with the Jones-side constant through a per-cusp factor

```
c_σ = 2^{(c−1)/2} · |τ|^{−1/2}
```

described there as *"the standard per-cusp Gaussian-integration factor in the
GGMW/Ohtsuki saddle asymptotic"*, with the general-`c` proof left open as "a
smaller open sub-item". On that basis `c_σ = 2^{−3/4}` was upgraded from
IDENTIFICATION to **DERIVATION**.

The non-circularity argument was explicit: the same `det J` construction
reproduces the classically-known `|τ(4_1)| = √3`, so the normalization is
pinned by calibration and `L5a1` is a genuine prediction rather than a fit.

## What was tested

Before proving a general-`c` formula for the correction factor, the
prerequisite question is whether the quantity being corrected is well-defined.
The Dimofte–Garoufalidis 1-loop invariant is conjecturally **topological**, so
it must not change when the manifold is retriangulated.

The probe retriangulates each manifold 25 times via `randomize()` (Pachner
moves) and recomputes. Two confounds are controlled rather than assumed away:

1. **Same manifold.** Every trial is checked with `is_isometric_to(original)`
   *and* by hyperbolic volume at 212 bits. Both hold in every case reported.
2. **Non-geometric solutions.** `randomize()` can land on a degenerate or
   negatively-oriented solution, where `det J` is meaningless. Those trials are
   skipped and counted, never mixed in. (0 skipped in all cases below.)

Values are clustered at relative tolerance 1e−15, so last-digit noise is not
counted as a distinct value. Shapes are read at `bits_prec=212`, converted
through decimal strings, with mpmath's working precision set by the canonical
`set_compute_dps()` (70 dps).

That last clause was wrong in the first version of this probe, and the repo's
own gates caught it: reading SnapPy at 212 bits achieves nothing if mpmath is
left at its default `dps=15`, which parses the high-precision strings straight
back down to a double. The probe's `volume` fields were then float64
expansions printed at 30 digits — textbook fake precision — and both
`witness_float64_padding_audit.py` and the new `witness_raw_float64_audit.py`
failed on it. Recorded here because it is the same failure mode this audit is
about: high-precision input is worthless if the working precision downstream is
not raised to match.

The table below is unchanged between the two runs. The differences being
measured are 30–300%, orders of magnitude larger than any precision effect.

## Result

| manifold | cusps | tetrahedra | distinct `\|det J\|` in 25 trials | |
|---|---:|---:|---:|---|
| `4_1` | 1 | 2 | **1** | invariant |
| `m003` | 1 | 2 | **1** | invariant |
| `m004` | 1 | 2 | **1** | invariant |
| `5_2` | 1 | 3 | **8** | varies |
| `6_1` | 1 | 4 | **2** | varies |
| `6_2` | 1 | 5 | **19** | varies |
| `L5a1` | 2 | 4 | **5** | varies |
| `L6a4` | 3 | 8 | **7** | varies |

Controls pass on all eight.

**`|det J|` is not a topological invariant.** The split is **not** about cusp
number: `5_2` is a one-cusped knot with eight distinct values, and `6_2` gives
nineteen. The correlate is tetrahedron count — every 2-tetrahedron
triangulation is invariant, every triangulation with ≥3 tetrahedra is not,
because a 2-tetrahedron triangulation has almost no room to move under Pachner
moves.

## Why this specifically defeats the calibration

The non-circularity argument rests on calibrating against `4_1`. `4_1` has
**two tetrahedra** — it is the one class of case that *cannot exhibit the
dependence*. Calibrating there is the least informative choice available, and
it cannot detect what is missing.

What is missing is structural. The DG 1-loop invariant carries a flattening
monomial and a global ½:

```
τ_DG = ± (1/2) · det(A·D_{z″} + B·D_{z′}) / ∏( z″^{f″} · z′^{f′} )
```

`whitehead_c_sigma_torsion.py` drops both, its docstring stating *"NO 1/2
factor and NO flattening monomial are needed for the MODULUS, because the
calibration below reproduces the known figure-eight value √3."* The flattening
is precisely what makes the expression triangulation-invariant. A single
2-tetrahedron calibration cannot see its absence — and the table above is what
happens when the check is run anywhere else.

## Consequences for the c_σ arc

**The values are default-triangulation artifacts.** `|τ(L5a1)| = 2^{5/2}` and
`|τ(L6a4)| = 2^6` are properties of the triangulation SnapPy happens to hand
back, not of the link. On retriangulation, `L5a1` yields `2^{1/2}, 2^{2/2},
2^{3/2}, 2^{4/2}, 2^{5/2}, 2^{7/2}` and `L6a4` yields `2^{6/2}` through
`2^{12/2}` — and the "canonical" values occur in a minority of trials
(`2^{5/2}` in 4/25; `2^6` in 2/25).

**The per-cusp factor is fitted against its own ambiguity.** The multi-cusp
spreads form a clean **√2 ladder** — exactly the magnitude of the claimed
`2^{(c−1)/2}`. A factor of `√2` per cusp cannot be distinguished from choosing
a different rung, so the three "confirmations" (c=1, 2, 3) do not constrain it.

**Therefore `c_σ = 2^{−3/4}` is not DERIVED by this route.** It reverts to
IDENTIFICATION. Bean `qou-pn5j`'s anti-circularity requirement is not met by
the current script: not because the reasoning was circular, but because the
quantity fed into it is not well-defined.

## What is NOT affected — stated precisely

**The numerical value `c_σ = 2^{−3/4}` stands.** It is pinned to ~20 digits by
`whitehead_c_sigma_hiprec.py`, an independent computation: pure mpmath, van der
Veen exact colored Jones plus Neville 1/N extrapolation, no SnapPy and no
`det J` anywhere. That was re-run and reproduces byte-identically (timestamp
only), with the three rival closed forms at ~0 digits. The `4_1` calibration
`c_σ(4_1) = 3^{−1/4}` likewise reproduces to ~17 digits.

So this audit removes a *derivation*, not a result. The Jones-side asymptotic
is untouched; what falls is the claim to have obtained it from a geometrically
computed torsion.

## What would fix it

1. **Restore the flattening monomial and the ½** and re-test invariance with
   this probe. If `|det J|` becomes triangulation-independent on `5_2`, `6_2`,
   `L5a1` and `L6a4`, the construction is sound and the values can be trusted.
2. **Re-derive the per-cusp factor against the corrected torsion.** It may
   survive, vanish, or change form — it is currently untested, since it was
   fitted against the ambiguity.
3. **Never calibrate on a 2-tetrahedron manifold alone.** The probe here is the
   cheap general check; `5_2` costs nothing and would have caught this.

## Secondary finding — a float64 entry point

`whitehead_c_sigma_torsion.py` reads shapes as `mp.mpc(complex(s))`. `complex()`
is float64, so despite `mp.mp.dps = 40` the computation is capped near 16
digits; its own `4_1` values wobble at digit 16 across runs while this probe's
high-precision path is stable past 20. This is the entry-point class PR #4677
tracks, and it is why the probe converts through decimal strings instead.

It does not cause the invariance failure — that reproduces at 212 bits — but it
means the digit counts that script reports are not what they appear to be.

## Reproduce

```sh
python3 computations/probes/one_loop_triangulation_invariance_probe.py
```

Runs in about a minute. The finding is reproducible with the repo's own
unmodified `one_loop_torsion()` by handing it a randomized triangulation; the
probe reimplements it only so shapes can be read at high precision.
