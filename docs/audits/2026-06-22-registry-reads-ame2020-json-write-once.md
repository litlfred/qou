# Registry reads AME values from `ame2020.json` directly — write a number once (2026-06-22)

**Status:** infrastructure — eliminates the registry/corpus value-duplication at its
source. Value-correcting (toward the authoritative AME2020), no calibration change.

## The problem (owner's question: "why aren't registry and corpus the same?")

The AME binding / atomic-mass values existed as **three independent hand-transcriptions**:
the `codata_constants` registry (via the manual-entry witness
`ame-2020-binding-energies.witness.json`), ~60 inline literals across `computations/*.py`,
and the atomic-mass literals hardcoded in the registry itself. Independent manual entry
**always drifts** — different rounding/editions plus outright typos (the registry's
⁵Li/⁷Li/⁹Be were 0.8–2.7 keV off; assorted corpus 1-ulp differences). There was no
single source of truth.

## The fix (owner's directive: "only write a number once")

`computations/substrate/codata_constants.py` now reads the AME binding **and** atomic-mass
values **directly, by `(Z, A)`**, from the vendored AME2020 evaluation
`qou-mass/src/qou_mass/data/ame2020.json` (Huang/Wang/Kondev/Audi/Naimi, *Chinese Physics
C* 45 (2021) 030002):

```python
AME_B_HE4_MEV_VALIDATION = _ame_binding_mev(2, 4)   # = binding_energy_total_keV / 1000
M_HE4_ATOMIC_MEV_VALIDATION = _ame_atomic_mev(2, 4) # = atomic_mass_micro_u · 1e-6 · u
```

Even the `u → MeV` factor is *parsed from the data file's own metadata*
(`"...1u = 931.49410242 MeV"`), not re-typed. So every AME number now lives in **exactly
one place**; the registry holds no copy. Variable names/interface are unchanged.

The values shift by ≤ a few ×10⁻⁴ MeV vs. the old literals — i.e. value-preserving to
sub-keV and **value-correcting** for the previously-wrong entries (⁵Li/⁷Li/⁹Be, and the
0.3 keV-imprecise `M_LI6` atomic mass), now at full evaluation precision.

## Remaining migration (the safe, now-trivial tail)

- The hand-maintained witness `ame-2020-binding-energies.witness.json` is **superseded for
  the registry** but retained for ~14 legacy scripts that still load it directly; they
  should migrate to `from codata_constants import AME_B_*_MEV_VALIDATION`, after which the
  witness can be deleted.
- The ~60 inline-literal files (per `ame-registry-routing-triage`) should likewise import
  from `codata_constants` — now **safe and value-improving**, because the registry is the
  authoritative AME2020 source rather than a possibly-stale hand copy.

Both are mechanical import-substitutions to be done in a compute-enabled env with per-file
run-verification; neither requires any further value decision.

## Cross-references

- [`computations/substrate/codata_constants.py`](../../computations/substrate/codata_constants.py) — the rerouted registry.
- [`qou-mass/src/qou_mass/data/ame2020.json`](../../qou-mass/src/qou_mass/data/ame2020.json) — the single source of truth.
- [`2026-06-21-ame-registry-routing-triage.md`](2026-06-21-ame-registry-routing-triage.md) — the routing roadmap + the registry data-audit (#2577).
