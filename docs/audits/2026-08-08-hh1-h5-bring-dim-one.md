# dim HH¹(H₅(ζ₅)) = 1 — the fibre-level c₃ SHAPE carrier exists at the Bring root (2026-08-08)

Branch `claude/q-deformed-saddle-offsets-bdn992` (PR #4794). Bean qou-jcmw
(dimension leg). Probe [`computations/hh1_h5_dim.py`](../../computations/hh1_h5_dim.py),
witness `computations/hh1-h5-dim.witness.json`. Exact-cyclotomic, no float64, no
fit, nothing wired.

## Result

**`dim HH¹(H₅(ζ₅)) = 1`.** The outer-derivation home of the Iwahori–Hecke algebra
`H₅(q)` at the Bring root of unity `ζ₅` (where `[5]_q = 0`, non-semisimple) is
**exactly one-dimensional** — so the fibre-level outer carrier for the Q_β c₃
SHAPE leg **exists and is unique up to scale** at the Bring root. This is the
necessary-existence datum bean qou-jcmw asked for: **positive, dim 1.**

## Method + verification

Generator-restricted derivations: a derivation of `H_n(q)` is determined by its
values on the Coxeter generators `s₁…s_{n-1}` subject to Leibniz-preservation of
the defining relations (quadratic, braid, commuting). The `T_w`-basis generator
multiplication is pure Coxeter length/permutation combinatorics — **no
pyhecke/GS engine needed**. Exact cyclotomic arithmetic (mpmath, 40 dps); rank by
partial-pivot Gaussian elimination with a pivot-gap certificate.

| case | N | dim Z | dim Inn | dim Der | **dim HH¹** | pivot gap |
|---|---|---|---|---|---|---|
| n=3 `q=i` (`[2]=0`) | 6 | 3 | 3 | 4 | **1** | 1.0 / 4.6e-41 |
| n=3 `q=ζ₆` (`[3]=0`) | 6 | 3 | 3 | 4 | **1** | 1.0 / 2.3e-41 |
| n=3 `q=2` (semisimple) | 6 | 3 | 3 | 3 | **0** | 1.0 / 2.3e-41 |
| n=5 `q=2` (ss control) | 120 | 7 | 113 | 113 | **0** | 1.0 / 5.4e-40 |
| **n=5 `q=ζ₅` (BRING)** | 120 | 7 | 113 | 114 | **1** | 0.387 / 1.78e-39 |

The n=3 rows reproduce the prior probe **exactly**; the n=5 semisimple control
returns a clean 0 through the identical 120-dim pipeline (validating the commuting
relations); the ζ₅ integer is certified by a ~38-order pivot gap. **Independently
re-run this session** (main loop, not the authoring subagent) — n=3 gate
reproduced, n=5 ζ₅ = 1.

## Scope — SHAPE only, and one identification stays assumed

- **SHAPE-only ceiling.** Even a fully successful HH¹ carrier supplies only the
  *shape* `S = (q−q⁻¹)·(bar-even)` (the Skein term). The c₃ **VALUE** leg is
  **proved measurement-limited** — `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
  + `QOU.QBeta.MeasurementLimitedFloor` (sorry-free). This does **not** close Q_β
  or its L2 target (the 1248 ppb residual is the c₃-and-beyond truncation,
  unchanged).
- **Archimedean access.** The substrate `q₀ ≈ 1.10998` is **not** a root of unity
  (`[2]_q ≈ 2.011 ≠ 0`), so no outer derivation exists at the archimedean
  evaluation point; access is via Habiro-ring continuation from the cyclotomic
  locus. dim 1 at ζ₅ is the *expected structure*, not an archimedean match.
- **Open assumption.** "The c₃ swing **is** this HH¹ class" is **not** established
  — a nonzero bar-odd *component* is not a bar-odd *eigenvector*, and the HH₀↔HH¹
  degree link (c₃ arrives via `tr_M ∈ HH₀`; derivations live in HH¹) is the open
  bean **qou-dilv**. Treat the identification as an assumption.

## Relation to the parity leg (already resolved by a sibling)

The companion *parity* question — is the outer class's action on the cocenter
bar-odd or bar-even? — is **not** a clean prune: the class parity is
normalization-dependent (an invariant only after pairing against `tr_M`, where the
number is *mixed* with a nonzero bar-odd component → screen **passed**, live-shape
branch). That was settled today by beans qb8b/qb8d,
[`2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`](2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md).
This dimension result is the complementary *existence* datum.

## Disposition

- **qou-jcmw** — dimension leg **delivered: dim HH¹(H₅(ζ₅)) = 1** (parity leg
  already answered n-independently). Human to close.
- The real open gate is **qou-qb8e (MAGNITUDE)** — nothing reproduces c₃'s value
  or its anchor swing; that is where effort should go, not another parity probe.
- **qou-dilv** (He–Nie cocenter → HH¹ lift) is the honest next structural step for
  the HH₀↔HH¹ degree link that the "swing = HH¹ class" assumption needs.

Nothing wired, no fit, no tier change; c₃ stays empirical/refuted-as-real-q.
