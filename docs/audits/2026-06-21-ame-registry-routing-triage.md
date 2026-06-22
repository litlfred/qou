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

## Registry ⟷ corpus value disagreement (the reconciliation crux)

`pyhecke_native` was built in-sandbox (≈42s) and the SAFE candidate files now run
exit 0, so routing *could* be verified here. But inspecting the actual `B_AME` dicts
reveals the deeper problem: **within a single dict, only the tritium value
(`8.481798`) is byte-exact to the registry** — every other isotope uses a value the
registry does *not* share. The disagreement is not uniform precision; for ⁶Li/⁷Li it
is ~100× larger:

| isotope | registry (`AME_B_*`) | corpus literal (common) | Δ | class |
|---------|---------------------|-------------------------|---|-------|
| D   | 2.224566   | 2.22456607 | ~0.07 eV | precision (corpus longer) |
| T   | 8.481798   | 8.481798   | 0        | **byte-exact (SAFE)** |
| ³He | 7.718043   | 7.7180428  | ~0.2 eV  | 7th-digit |
| ⁴He | 28.295673  | 28.295674  | ~1 eV    | 1 ulp |
| **⁶Li** | **31.99405** | **31.99464** | **~590 eV** | **substantive — registry suspect** |
| **⁷Li** | **39.24397** | **39.24454** | **~570 eV** | **substantive — registry suspect** |

The ⁶Li/⁷Li gaps (~0.6 keV) are two orders of magnitude larger than the others and
**consistent** (both ≈ +0.58 keV in the corpus over the registry), pointing to a
data error or stale-source in the registry's `B_li6_MeV` / `B_li7_MeV` (the source
witness `ame-2020-binding-energies.witness.json`), not a precision nicety. The corpus
literals (`31.99464`, `39.24454`) are the values to verify against an authoritative
AME2020 table.

**Consequence for routing:** mechanically routing corpus files *toward* the registry
would (a) for most isotopes change the value by 1 ulp (already a violation), and (b)
for ⁶Li/⁷Li propagate a **likely-wrong** registry value over the corpus value. So the
"route to registry" direction is not safe even where the literal is close.

## Reconciliation policy needed (answers blocker b)

Before any routing, the registry must be **audited against an authoritative AME2020
source**, isotope by isotope, to decide per value which side is canonical:

1. **⁶Li, ⁷Li (~0.6 keV gaps):** verify against AME2020; if the corpus is right, **fix
   the registry** (`B_li6_MeV`, `B_li7_MeV`) — do not route corpus → registry.
2. **D, ³He, ⁴He (≤1 ulp):** pick one canonical precision and align both registry and
   corpus to it (a deliberate, documented value choice).
3. **T (`8.481798`):** the only value both agree on — the 93 "SAFE" routes are
   dominated by this single repeated literal; routing just it leaves mixed dicts, so
   it is low value until the rest is reconciled.

This is an owner / data-audit decision, not a mechanical sweep. The routing should
follow the audit, not precede it.

## Cross-references

- Bean `fvxq`; sibling `claude/fvxq-atomic-mass-registry-2026-06-21` (registry exports + first route).
- [`computations/substrate/codata_constants.py`](../../computations/substrate/codata_constants.py) — the registry.
