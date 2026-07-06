# The pp-Coulomb length-scale is not a cusp-geometry ratio (audit lever closed)

**Status:** FINDING (owner-authorised Subgoal-2 probe, reproducible, no fit). The
one productive direction the [`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md)
audit named but could not test — "derive `r_pp` from the JSJ decomposition of
the ³He binding link (L6a4 = Borromean) as a cusp/horoball separation" — is now
tested (SnapPy 3.3.2 became available in [#3298](https://github.com/litlfred/qou/pull/3298)),
and it comes back **negative**. The pp-Coulomb magnitude length-scale is **not** a
cusp-geometry ratio of the mirror links.

Probe: [`em_linking_cusp_geometry_probe.py`](../../computations/em_linking_cusp_geometry_probe.py)
(witness `em-linking-cusp-geometry-probe.witness.json`; `--live` re-verifies
against SnapPy, matches baked exactly).

## Authorisation

The magnitude gap is a **dimensionful length scale** (`r_strong/r_charge ≈ 3.213`,
[`2026-06-03-em-linking-invariant.md`]) — Subgoal-2, which `precision-goals.md`
declines without explicit owner reversal. The owner **explicitly reversed the
Subgoal-2 decline for this specific probe** (2026-07-04): compute the ³He
Borromean cusp geometry and test the pinned length ratio, formalize-first, no
scan/fit. This audit records that authorised probe and its negative result. The
reversal is narrow (this probe only); it does not reopen Subgoal-2 generally.

## Formalize-first — the pinned hypothesis

Target: `r_strong/r_charge = 6.06 fm / 1.885 fm ≈ 3.2149`. Hypothesis: this is a
single horoball-packing ratio (cusp reach vs cusp separation) in the ³He
Borromean complement. Discipline gate: a real match is `< 1%`; anything looser,
selected post-hoc, is the PSLQ-coincidence antipattern (a CAL-4 fit).

## Result — two independent negatives

### (b) Structural exclusion — S₃ symmetry (invariant cited)

SnapPy: the ³He binding link **L6a4 = Borromean rings** has a fully **S₃-symmetric
complement** — all three cusps are geometrically **identical** (shape `= 2i`,
meridian `√2`, longitude `2√2`, verified). Therefore every within-link
cusp-separation — pp, pn, nn — is **equal**; the geometry carries **no
proton-vs-neutron distinction**. A within-³He cusp ratio is `1.000`, never
`3.213`. The charge asymmetry that sources the Coulomb split cannot be a geometric
feature of a link whose components are interchangeable. This is a genuine scope-(b)
structural exclusion: the invariant is the S₃ symmetry of the Borromean complement.

### (a) Scope-limited negative — cross-link ratios miss the gate

The pp/nn distinction *does* live in the mirror pair (³He = Borromean vs ³H = 8_11
are different links). But no natural cross-link geometric ratio matches `3.2149`
to the `<1%` gate:

| cross-link ratio | value | miss |
|---|---:|---:|
| longitude(8_11)/longitude(L6a4) | 3.3535 | 4.3% |
| \|shape\|(8_11)/\|shape\|(L6a4) | 3.7163 | 15.6% |
| vol(8_11)/vol(L6a4) | 1.1308 | 64.8% |

The closest (longitude, 4.3%) is not a match, and selecting it because it is
closest would be exactly the coincidence-fit the discipline forbids.

## Verdict

- **The audit's "cusp/horoball separation" lever is closed.** The pp-Coulomb
  magnitude length-scale is not a cusp-geometry ratio of the mirror links —
  structurally within ³He (S₃-symmetric), and unmatched across the mirror pair.
- **The magnitude gap stays OPEN and owner-gated.** The `2026-06-03` diagnosis
  stands: the framework supplies the EM-linking *structure* (Hopf `lk = +1 = Q_pp`,
  U(1) framing, trace asymmetry) but not the dimensionful length scale. SnapPy has
  now excluded the one geometric route that was named; no other categorical
  length-scale object exists yet.
- **No fit.** The `3.213×` was never an input; matching a link ratio to it would be
  a CAL-4 violation. The probe asserts the honest negative (`none_match = 1`).

## What this does and does not claim

- **Does** confirm (SnapPy) that L6a4 = Borromean is S₃-symmetric (3 identical
  cusps) — so the within-link cusp route cannot carry a pp/pn charge asymmetry.
- **Does** show no natural cross-link (8_11 vs Borromean) cusp ratio matches the
  `3.213×` to `<1%` (best 4.3%).
- **Does** close the `2026-06-03` audit's named productive direction (cusp/horoball
  separation).
- **Does NOT** fit, tune, or select a ratio to hit `3.213`; does NOT wire to
  production; does NOT advance L2; does NOT reopen Subgoal-2 beyond this probe.
- The Milnor triple-linking μ̄ route (the other natural first-instinct for
  "Borromean pairwise-lk vanish") is separately excluded a priori: μ̄ is a
  *dimensionless* integer and the gap is dimensionful (per the `2026-06-03`
  audit's dimensional argument).

## Cross-references

- The gap this probes: [`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md).
- SnapPy availability + the mirror links: [`2026-07-04-he4-link-volume-braid-closure-refuted.md`](2026-07-04-he4-link-volume-braid-closure-refuted.md).
- Discipline: [`production-vs-exploratory-discipline.md`](../../.claude/skills/local/production-vs-exploratory-discipline.md) (§Antipattern 2, PSLQ coincidence); `precision-goals.md` (Subgoal-2 gate).
