# Downstream consumer libraries — status (2026-05-24)

Snapshot of the cross-language consumer-library work from
[`docs/workplans/2026-05-24-library-reuse-production-readiness.md`](2026-05-24-library-reuse-production-readiness.md)
v2, §3.6 "Where do Node.js / Kotlin / R / C come in".

## TL;DR

| Consumer language | Witness reader | Hecke core compute |
|---|---|---|
| **Python (CPython, Pyodide)** | ✅ `qou-substrate` (PR #1068) | ✅ `pyhecke-native` (already on PyPI) |
| **TypeScript / Node / Deno / Bun** | ✅ `@litlfred/witness-schema` (PR #1078) | ⚠️ Tier-2 item 2d **(in progress this PR)** |
| **Browser / WASM** | ✅ Same npm artefact as above | ⚠️ Tier-2 item 2d **(in progress this PR)** |
| **R** | ✅ JSON Schema (`jsonvalidate`) | ⏳ Tier-3 — out of scope for greenlight |
| **Kotlin / JVM** | ✅ JSON Schema (`com.networknt.schema`) | ⏳ Tier-3 — out of scope for greenlight |
| **Java** | ✅ JSON Schema (`com.networknt.schema`) | ⏳ Tier-3 — out of scope for greenlight |
| **Swift** | ✅ JSON Schema (Ajv-compatible libs) | ⏳ Tier-3 — out of scope for greenlight |
| **C** | ✅ JSON Schema (json-c + validator) | ⏳ Tier-3 — out of scope for greenlight |

## What's done

### Tier-2 item 2a — `qou-substrate` (Python substrate-infra)

- **PR**: #1068 (merged 2026-05-24)
- **Package**: PyPI candidate `qou-substrate` at `tools/qou-substrate/`
- **Contents**: `WitnessBuilder` + `_precision` + `q_parameter` (substrate trio,
  62 % of compute scripts depend on at least one of these)
- **Status**: Phase A (parallel package) and Phase B (back-compat shim) both
  merged. PyPI publish workflow is a follow-up (item 1b).

### Tier-1 item 1c — `@snappea/kernel` npm publish

- **PR**: #1078 (merged 2026-05-24)
- **Package**: npm `@snappea/kernel` from `folio-assistant/snappea-wasm/`
- **Contents**: SnapPea hyperbolic 3-manifold kernel as WASM
- **Status**: workflow gains a `publish` job (manual `workflow_dispatch`
  trigger, OIDC provenance, `secrets.NPM_TOKEN`). Also fixed a pre-existing
  working-directory bug. Not yet auto-published.

### Tier-1 item 1d — `witness-schema` (universal interchange)

- **PR**: #1078 (merged 2026-05-24)
- **Packages**:
  - **PyPI**: `witness-schema` (Pydantic v2 models at
    `tools/witness-schema/python/witness_schema/`)
  - **npm**: `@litlfred/witness-schema` (Zod v3 / v4 at
    `tools/witness-schema/js/`)
  - **Canonical artefact**: `tools/witness-schema/schema/witness.schema.json`
    (JSON Schema draft 2020-12 — universal)
- **Verification**: 9 smoke tests pass; cross-validated against two real
  in-repo witnesses (`binding-K-direct.witness.json`,
  `canonical-isotope-witness-Z00.witness.json`) including `null`-bearing
  upstream-hash records
- **Status**: the schema artefact is what enables R / Kotlin / Java /
  Swift / C consumers to read `*.witness.json` files **without any
  language-specific package**. No JVM-published artefact yet —
  consumers fetch the schema from the npm or PyPI download or from the
  GitHub blob URL.

### Tier-2 item 2b Phase A — pyhecke carve-out

- **PR**: #1085 (open, awaiting review)
- **Effect**: `hecke_core.py` 3,183 LOC → 1,120 LOC (−65 %) by carving the
  Phase-5 EXPLORATORY surface into `_deprecated/hecke_core_legacy.py`.
  Full back-compat preserved.
- **Why this matters for downstream**: the slimmed canonical surface
  is what gets promoted into `tools/pyhecke/` for the PyPI 1.0 publish
  (item 1a). The carve-out is the structural prerequisite.

## What's in flight

### Tier-2 item 2d — WASM hecke-engine ⚠️ **THIS PR**

- **Branch**: `claude/wasm-hecke-engine-phase-a-2026-05-24`
- **Goal**: feature-gate `rug`/GMP + Clarabel out of `hecke-engine`'s
  WASM build; new sibling crate `tools/hecke-engine-wasm/` with
  `wasm-bindgen` exports of the canonical surface; `.github/workflows/`
  build + test step
- **Why**: WASM target cannot link GMP / MPFR / LAPACK / OpenBLAS (the
  hecke-engine's MPFR + Clarabel-SDP optional deps depend on these).
  Need a pure-Rust core for the WASM artefact.

## What's not started (Tier-3 / future)

### Tier-3 — Node.js / Kotlin / Java / R / C native hecke

These were explicitly **out of scope** per owner directive (workplan v2
§3.6 confirmed): the priority order is Python → JS / WASM →
witness-schema → other-language wrappers (Tier-3). The witness-schema
already covers cross-language witness *reading*; native compute in JVM /
R / C languages is a separate sub-tier.

| Item | Mechanism | Effort |
|---|---|---|
| Node.js native | `napi-rs` binding of `hecke-engine` | ~3-5 d after 2d |
| Kotlin / Java native | JNI binding via UniFFI of `hecke-engine` | ~5-10 d after 2d |
| R native | `extendr` binding of `hecke-engine` | ~5 d after 2d |
| C native | C-ABI via `cbindgen` of `hecke-engine` | ~3 d after 2d |
| Swift native | `swift-bridge` of `hecke-engine` | ~3-5 d after 2d |

**Common gating**: all of these depend on `hecke-engine`'s feature
gates landing first (2d Phase A in this PR). After 2d, each
target is a relatively self-contained binding crate.

## Path-B consumers (witness reader only, no compute)

The `witness-schema` package already enables these consumers
**today** — no further packaging needed:

```r
# R
library(jsonvalidate)
schema <- readLines("https://github.com/litlfred/qou/raw/main/tools/witness-schema/schema/witness.schema.json")
witness <- readLines("/path/to/hyperbolic-volumes.witness.json")
json_validate(witness, schema)  # → TRUE
```

```kotlin
// Kotlin (Maven: com.networknt.json-schema-validator)
val factory = JsonSchemaFactory.getInstance(SpecVersion.VersionFlag.V202012)
val schema = factory.getSchema(URI("https://.../witness.schema.json"))
val witness = ObjectMapper().readTree(File("hyperbolic-volumes.witness.json"))
schema.validate(witness)  // → empty Set of validation errors
```

```c
// C (json-c + json-c-schema-validator)
json_object *schema = json_object_from_file("witness.schema.json");
json_object *witness = json_object_from_file("hyperbolic-volumes.witness.json");
schema_validate(schema, witness, NULL);  // → 0 if valid
```

The downstream user does not need to wait for QOU to publish a
language-specific package — the JSON Schema is the contract.

## Summary

| Goal | Status |
|---|---|
| Cross-language **witness reading** | ✅ Done (PR #1078 — `witness-schema` artefact) |
| Python compute | ✅ Done (`qou-substrate` + existing `pyhecke-native` on PyPI) |
| TypeScript / WASM compute | ⚠️ **In flight this PR** (2d Phase A) |
| JVM / R / C native compute | ⏳ Tier-3, after 2d lands |
