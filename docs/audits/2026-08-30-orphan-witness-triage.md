# Triage of the 19 producerless witnesses: 4 are paper-consumed, 15 are not

**Date:** 2026-08-30 · **Bean:** `qou-cdvx` · **Upstream:** `qou-agvb`,
[`2026-08-30-witness-producer-resolution.md`](2026-08-30-witness-producer-resolution.md)

The producer-resolution audit found **19** live witnesses that nothing in the
tree produces. Their numbers cannot be re-derived. This triages them by what
actually depends on them — measured per witness, not sampled.

## Tier A — paper-consumed, needs a producer (4)

| witness | how it is depended on |
|---|---|
| `hecke-core-symbolic-migration` | named in the `computation.witness` field of **two `.ts` manifests** (`mba-step02-gs-reduction`, `e-hartree-categorical-derivation`) and as the *"Canonical witness"* in `mba-step02-gs-reduction.md` |
| `canonical-mass-table-242ppb` | `computation.witness` of `mba-step09b-per-isotope-binding.ts`; the *"Witness contract"* of its `.md`; a row in `mba-chain-map.md` |
| `4he-binding-full-pipeline` | `BraneGeometricResummation.lean` cites its `tower_MeV ≈ 2×10⁶` blow-up figure |
| `whitehead-volume-identification` | cited in `b1-hyperbolic-rows-theorem-audit.md` as where the supporting computation is recorded |

The first two are the sharp cases: a `computation.witness` field is a
**maintenance contract** under the Mass-and-Binding-Algorithms appendix rule,
and it currently points at an artifact no one can regenerate.

`4he-binding-full-pipeline` deserves a note. Its own `scriptFile` reads
*"(legacy — no matching producer found; provenance pending manual triage)"* —
it declares its own condition honestly — and `content/values/registry.ts`
carries a comment recording that a prior agent already **de-pinned** a value
from it, calling it *"a producerless artifact whose own run is recorded as a
FAILURE"*. So the registry hit is a removal note, not a live pin. The Lean
citation is live.

## Tier C — no live consumer (15)

`chi-deuteron-h6-at-q0-90dps-matrix-m`, `chi-helium-3-free-h9-at-qinv-50dps`,
`chi-helium-4-free-h12-at-qinv-50dps`, `chi-helium-4-h12`,
`chi-tritium-free-h9-at-q0-50dps`, `chi-tritium-free-h9-at-qinv-50dps`,
`binding-lp-delta-audit`, `forward-ref-classification`,
`meson-spectral-analysis`, `mu3-submodularity-vacuous-deuteron`,
`bring-jacobian-isogeny-factors`, `lever1-bring-period-trB`,
`tau-hat-n-proton-level-1-empty`, `tritium-interface-decomposition`,
`weak-isospin-t3-grading`

Every remaining reference to these is either an audit witness that enumerates
*every* witness, or a dated `docs/`-or-bean mention recording history.

## A substring bug in this triage, caught before it was published

`chi-helium-4-h12` first measured **111 references** — by far the most of the
nineteen — including a Lean file and a `qou-mass` module, which put it at the
top of tier A. **All of it was substring contamination.** The corpus contains
`chi-helium-4-h12-at-q0-50dps`, `-at-q0-50dps-muon` and `-numeric`, and a
plain `in` test matches the orphan's name inside all three.

Re-measured with the exact filename, **nothing reads
`chi-helium-4-h12.witness.json`**. The one call site that looked decisive,
`nucleus_operator_selection_sdp.py:66`, holds the string only as a *stem* and
globs `f"{stem}-at-q0-50dps-matrix-m.witness.json"` — a different file.

It was the only one of the nineteen whose name is a prefix of another witness,
so the other eighteen counts are unaffected. Recorded because it is the third
instance this session of the same failure — a detector keyed on one spelling,
or here on a substring, in a corpus that writes several — and because it would
have promoted a witness nothing uses to the top of the "must fix" list.

## Recommendation

**Do the four, leave the fifteen.** Writing producers for tier C would be
speculative work on artifacts nothing consumes, and the anti-fit discipline
cuts the same way here: a producer written to reproduce a number whose
derivation nobody remembers is a transcription, not a derivation.

**"No live consumer" is not "safe to delete."** The fifteen are cited in dated
audit docs as historical records, and deleting them would break those. If they
are retired, retire them by marking — the `_deprecated/` convention — never by
removing the file.

Ordering within tier A, by strength of the contract: the two
`computation.witness` manifest entries first, the Lean citation second, the
audit-doc citation last.

Not started: this document triages and recommends; it changes nothing.
