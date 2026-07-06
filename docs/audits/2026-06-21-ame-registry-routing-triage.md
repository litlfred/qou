# AME-literal → registry routing triage (bean fvxq, 2026-06-21)

**Status:** infrastructure triage — the routing roadmap for bean `fvxq`. No physics,
no value change. Complements the active sibling `claude/fvxq-atomic-mass-registry`.

## Why a triage (not a sweep)

The atomic-mass registry exports landed on main
(`computations/substrate/codata_constants.py`: `M_*_ATOMIC_MEV_VALIDATION`,
`AME_B_*_MEV_VALIDATION`). Routing the remaining inline-literal tail is **not** a
uniform mechanical sweep, because the registry's canonical value strings differ at
the last digit(s) from many corpus literals:

- `AME_B_HE4 = 28.295673` (registry) vs the corpus-ubiquitous `28.295674`
- deuteron `2.224566` (registry) vs `2.22456607` / `2.22456612` in various files
- `AME_B_HE3 = 7.718043` vs `7.71804` / `7.718058` / `7.7180375`

Routing a mismatched literal would **silently change the value** — a
value-preservation violation. So the literals split into two classes.

## The triage

Probe [`computations/probes/ame_registry_routing_triage.py`](../../computations/probes/ame_registry_routing_triage.py)
· witness `ame-registry-routing-triage.witness.json` (pure string/value compare,
runs anywhere — no compute deps):

| class | count | meaning |
|-------|------:|---------|
| **SAFE** (byte-exact to a registry value) | **93 routes / 60 files** | value-preserving route: `mp.mpf("8.481798")` → `AME_B_TRITIUM_MEV_VALIDATION` |
| **UNSAFE** (within ~5e-6 but not exact) | **222 / 94 files** | routing changes the value — needs a *reconciliation decision*, not a route |

The witness lists every SAFE route (file → literal → export) and every UNSAFE
near-match. The SAFE list is the value-preserving work; the UNSAFE list is a set of
owner/sibling decisions (*is the registry value canonical, or is the corpus literal?*)
that must precede any routing.

## Infra note

Routing + the fvxq per-file run-verification ("each runs exit 0, witness refreshed")
is **infra-gated** in some sandboxes: many SAFE target files import `pyhecke_native`
(buildable, ~42s) or have pre-existing runtime errors (e.g. `KeyError: 'dim'`), so they
cannot be run-verified everywhere. This triage runs anywhere and is the verifiable
roadmap; the actual routing of the 60 SAFE files should be done where the compute env
can confirm value-preservation.

## Recommendation

1. **Route the 93 SAFE literals** (60 files) in batches, in a compute-enabled env,
   coordinating with the active sibling to avoid collision.
2. **Escalate the 222 UNSAFE near-matches** as a value-reconciliation question — most
   are 1-ulp differences from the registry's chosen AME2020 values; deciding whether
   to (a) align the registry to the corpus literal, (b) fix the corpus literal to the
   registry value (a deliberate value change), or (c) leave them is an owner call, not
   a mechanical route.

## Registry ⟷ corpus disagreement — RESOLVED against vendored AME2020 (correction)

`pyhecke_native` was built in-sandbox (≈42s), unblocking verification, and the SAFE
candidate files run exit 0. Inspecting the `B_AME` dicts showed that within each dict
only tritium (`8.481798`) is byte-exact to the registry — every other isotope differs.

**An earlier draft of this audit mis-diagnosed the cause** (it claimed the registry's
⁶Li/⁷Li were wrong and the corpus matched AME2020). Cross-checking **all** registry
values against the **vendored AME2020 evaluation** (`qou-mass/src/qou_mass/data/ame2020.json`,
`binding_energy_total_keV` — the authoritative source) corrects the record:

| isotope | registry (orig) | vendored AME2020 | Δ keV | corpus literal | verdict |
|---------|-----------------|------------------|------:|----------------|---------|
| D, T, ³He, ⁴He, ⁸Be, ¹²C, ¹⁶O | … | … | < 0.1 | (various) | registry OK |
| **⁶Li** | 31.99405 | **31.99399** | +0.06 | 31.99464 | **registry OK; corpus is the +0.65 keV outlier** |
| **⁵Li** | 26.32800 | **26.33066** | −2.66 | — | **registry error → FIXED** |
| **⁷Li** | 39.24397 | **39.24508** | −1.11 | 39.24454 | **registry error → FIXED** (corpus also −0.54 keV off) |
| **⁹Be** | 58.16480 | **58.16402** | +0.78 | — | **registry error → FIXED** |

So the genuine errors were **manual-entry transcription mistakes in the registry's
⁵Li / ⁷Li / ⁹Be values** (the witness `engine` is `"manual-entry"`), not ⁶Li. These
three are corrected in this PR to the vendored AME2020 values (provenance note added
to `ame-2020-binding-energies.witness.json`). The corpus literals (`31.99464`,
`39.24454`, `2.22456607`, …) are a *separate* set of slightly-off values — the routing
tail still needs them reconciled, but **toward the verified AME2020 values, not toward
each other**.

## Reconciliation policy (verified)

1. **Registry data (done here):** ⁵Li/⁷Li/⁹Be corrected to vendored AME2020; all other
   registry binding values verified within 0.1 keV.
2. **Corpus literals (the routing tail):** the ≤1-ulp and the ⁶Li `31.99464` /
   ⁷Li `39.24454` corpus values should be routed to the (now-verified) registry
   exports — which *is* value-improving toward AME2020. This is the safe routing
   direction, to be done in a compute-enabled env with per-file run-verification.
3. **Tritium (`8.481798`):** already agrees everywhere; the 60 "SAFE byte-exact" routes
   are dominated by it.

The lesson: "route literals → registry" is sound **only after** the registry is itself
audited against the authoritative AME2020 source — which this PR does.

## Cross-references

- Bean `fvxq`; sibling `claude/fvxq-atomic-mass-registry-2026-06-21` (registry exports + first route).
- [`computations/substrate/codata_constants.py`](../../computations/substrate/codata_constants.py) — the registry.
