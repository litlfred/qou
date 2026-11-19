---
# qou-dxbw
title: 'EPIC: Drain Uninstantiated Lean Axiom-Fields & Build Missing Mathlib4 Infrastructure'
status: todo
type: epic
priority: high
tags:
    - lean
    - mathlib-gap
    - axiom-field-audit
    - de-vacuification
created_at: 2026-11-19T08:19:49Z
updated_at: 2026-11-19T08:19:49Z
parent: qou-rtxm
---

## Overview & Motivation

Owner directive (2026-11-19): *"audit axioms fields - sign of a gap to be filled. lots of missing mathlib infra. bean up epic"*

Zero `sorry` and zero `axiom` in `#print axioms` does **not** certify that a theorem's mathematical or physical premises are proved when those premises are shifted into uninstantiated `[MyClass ...]` instance binders or `(h : MyStruct ...)` hypothesis structures, or satisfied only by `Unit` / `Fin 1` / constant-zero skeleton instances.

- **Reproducible Scanner:** `computations/audits/lean_axiom_field_and_mathlib_gap_audit.py`
- **Machine-Counted Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Parent Milestone:** `qou-rtxm` (*Lean / Mathlib foundations*)
- **Cross-Linked Sibling Epics:** `qou-c8p8` (*Mathlib infra: close class field debt*), `qou-6qbv` (*De-vacuify Lean :True carriers*), `08a2` (*keystone de-abstraction*), `mlgp`, `qou-59vq`, `qou-k4oq`, `qou-o9ge`

---

## Corpus-Wide Audit Baseline (`4228` `.lean` files: `3315` library + `913` chapter)

- **Raw declarations:** `985` `class`es + `1184` `structure`s = `2169` (`366` pure-data structures without `Prop` fields or `extends` excluded $\to$ **`1803` audited carriers**)
- **Standalone assumptions:** `61` `axiom`, `118` `opaque`, `8` real `sorry`, `1` `native_decide`
- **Cross-detector overlap:** `43` axiom-shim-guarded carriers, `34` unpinned `: Prop` carriers, `416` carriers with unconstrained data fields

### Instantiation Status $\times$ Root-Cause Taxonomy Matrix

| Instantiation Status | Type M (`MISSING_MATHLIB_INFRA`) | Type P (`QOU_BRIDGE_OR_PHYSICS_GAP`) | Type D (`LEGITIMATE_ALGEBRAIC_INTERFACE`) | Total |
|---|---:|---:|---:|---:|
| `UNINSTANTIATED_AXIOM_CLASS` | 479 | 853 | 4 | **1336** |
| `TOY_ONLY_INSTANCE` | 16 | 13 | 0 | **29** |
| `GENUINELY_INSTANTIATED` | 0 | 0 | 438 | **438** |
| **Total** | **495** | **866** | **442** | **1803** |

### Breakdown by Cohesive Mathlib4 Infrastructure Cluster (`M1..M7`) & QOU Bridge (`P1`)

| Cluster | Uninst/Toy Carriers | Cls / Str / Toy | Standalone `axiom` / `opaque` | Prop Fields | Downstream Consumers | Existing Cross-Linked Beans |
|---|---:|---:|---:|---:|---:|---|
| **M1: Polylog / Li₂ / Bloch–Wigner 5-Term / Bloch–Suslin B₂,B₃** | 37 | 31 / 6 / 0 | 0 / 8 | 57 | 44 | `mlgp`, `qou-o41q`, `qou-mlbg`, `qou-gkco`, `qou-tc8y` |
| **M2: Riemann Surfaces / Riemann–Roch / Hodge / Contour & Hadamard** | 16 | 7 / 9 / 0 | 2 / 5 | 20 | 13 | `qou-bmyx`, `qou-dgtf`, `qou-kp89`, `qou-n4pv`, `qou-nuxb`, `qou-wdgz`, `qou-z4jb` |
| **M3: Hyperbolic 2D/3D / Triangle Groups Δ(p,q,r) / Mostow / Ohtsuki** | 60 | 41 / 16 / 3 | 0 / 1 | 119 | 116 | `qou-5gai`, `qou-322e`, `qou-h2mb`, `qou-i0sr`, `qou-m8xt`, `qou-sd8y`, `qou-6x4m` |
| **M4: Iwahori–Hecke H_n(q) / Hoefsmit / Ocneanu Markov / Macdonald** | 204 | 123 / 74 / 7 | 13 / 18 | 408 | 357 | `qou-59vq`, `qou-k4oq`, `qou-0cyu`, `qou-1oif`, `qou-1o8n`, `qou-utb3`, `qou-ep0a` |
| **M5: Quantum Groups U_q(sl_N) / R-Matrix / Ribbon MTC / GPMT Traces** | 28 | 14 / 13 / 1 | 2 / 1 | 65 | 100 | `qou-o9ge`, `rtqd`, `rtrb`, `bwrt`, `hkmt`, `qou-ga7i`, `qou-xsmr` |
| **M6: Siegel H_g / Theta Characteristics / Bring S₅ / X₀(15) Periods** | 12 | 0 / 11 / 1 | 0 / 0 | 32 | 4 | `qou-k7ad`, `qou-r7qm`, `5lcg` |
| **M7: Hochschild HKR / Gerbes / 2-Stokes / q-Borel / Surreals / SDP** | 138 | 63 / 71 / 4 | 3 / 32 | 271 | 328 | `qou-a8rj`, `qou-6ers`, `qou-ghc6`, `qou-jvua`, `qou-vspi`, `qou-pan0`, `qou-7b7v`, `qou-x1rm`, `qou-yc05`, `qou-9h4t`, `hypr` |
| **P1: QOU Physics / Calibration / Bridge Premises** | 866 | 457 / 396 / 13 | 41 / 53 | 1766 | 1394 | `qou-6qbv`, `qou-c8p8`, `08a2` |

---

## Child Feature Beans Minted Under This Epic

| Child Bean ID | Cluster | Title | Uninst/Toy Carriers | Downstream Consumers |
|---|---|---|---:|---:|
| `qou-eao2` | `M1_DILOG_BLOCH_SUSLIN` | M1 [Mathlib4 Infra]: Polylogarithms, Bloch–Wigner 5-Term Relation & Bloch–Suslin Groups B₂(ℂ)/B₃(ℂ) | 37 | 44 |
| `qou-mq3p` | `M2_RIEMANN_SURFACES_HODGE_CONTOUR` | M2 [Mathlib4 Infra]: Compact Riemann Surfaces, Riemann–Roch, Hodge Decomposition & Complex Contour/Hadamard | 16 | 13 |
| `qou-ct0m` | `M3_HYPERBOLIC_UNIFORMIZATION_3MANIFOLDS` | M3 [Mathlib4 Infra]: Hyperbolic 2D/3D Geometry, Triangle Groups Δ(p,q,r), Mostow Rigidity & Ohtsuki Asymptotics | 60 | 116 |
| `qou-ltwg` | `M4_HECKE_MARKOV_SPECHT_MACDONALD` | M4 [Mathlib4 Infra]: General-n Iwahori–Hecke H_n(q), Hoefsmit/Murphy Bases, Ocneanu Markov Trace & Macdonald/Plancherel | 204 | 357 |
| `qou-3exy` | `M5_QUANTUM_GROUPS_RIBBON_GPMT` | M5 [Mathlib4 Infra]: Quantum Groups U_q(sl_N), Universal R-Matrix, Ribbon/Modular Categories & GPMT Modified Traces | 28 | 100 |
| `qou-2eum` | `M6_SIEGEL_THETA_MODULAR_CURVES` | M6 [Mathlib4 Infra]: Siegel Upper Half-Space H_g, Theta Characteristics, Bring's Curve S₅ & X₀(15) Period Isogeny | 12 | 4 |
| `qou-0yxl` | `M7_HOCHSCHILD_GERBES_STOKES_QBOREL_SDP` | M7 [Mathlib4 Infra]: Hochschild HKR, O^×-Gerbes, Non-Abelian 2-Stokes, Surreal Transfer, q-Borel & Conic SDP Duality | 138 | 328 |
| `qou-6f4w` | `P1_QOU_PHYSICS_BRIDGE` | P1 [QOU Bridge Drain]: Discharge QOU Physics-Bridge Axiom-Field Classes, Shim Guards & Toy Instances | 866 | 1394 |
