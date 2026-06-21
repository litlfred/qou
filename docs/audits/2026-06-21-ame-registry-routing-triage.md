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

## Cross-references

- Bean `fvxq`; sibling `claude/fvxq-atomic-mass-registry-2026-06-21` (registry exports + first route).
- [`computations/substrate/codata_constants.py`](../../computations/substrate/codata_constants.py) — the registry.
