# qou-substrate

Pure-Python substrate infrastructure for the Quantum Observable Universe paper. The 1.1k-LOC layer that **67 % of QOU compute scripts depend on**.

Three modules, no Rust dependency, no system libraries beyond CPython + mpmath:

| Module | Purpose |
|---|---|
| `qou_substrate.constants` | The substrate parameter `q_0 = 1/(1 - √(V(4_1) / (m_μ/m_e)))` + derived constants + uncertainty propagation. Single source of truth. |
| `qou_substrate.precision` | `set_compute_dps(50)` + `fmt()` — mpmath precision discipline (compute at OUTPUT_DPS + GUARD digits, serialise at OUTPUT_DPS). |
| `qou_substrate.witness`   | `WitnessBuilder`, the schema-shaped JSON emitter with git provenance, per-file content-hash staleness, and upstream-witness drift detection. |

## Install

```bash
pip install qou-substrate
```

Pyodide-loadable via `micropip.install("qou-substrate")` — no native code.

## Quick start

```python
from qou_substrate import Q, HA, q_int, set_compute_dps, fmt, WitnessBuilder

# Substrate constants (float, bit-stable across installs)
print(Q)                # 1.1099785955...   the substrate parameter
print(HA)               # q - q^-1
print(q_int(9))         # quantum integer [9]_q

# Precision discipline for mpmath-based computations
set_compute_dps()       # set mp.mp.dps to 50 (default)
from mpmath import mp, mpf
x = mp.sqrt(mpf(2))
print(fmt(x))           # "1.4142135623..." trimmed to 40 dps for witness JSON

# Witness emission with git provenance + staleness tracking
w = WitnessBuilder(
    block_id="my-computation",
    description="What this witness records",
    engine="mpmath",
)
w.add_data("answer", fmt(x))
w.write("computations/my-witness.witness.json")
```

## Where this fits in the QOU framework

This package contains the **Layer 0** (substrate-infra) of the QOU compute pipeline:

```
LAYER 0  qou-substrate                           ← you are here
            (1.1 k LOC, pure Python, mpmath only)
                │
   ┌────────────┴────────────┐
   ▼                         ▼
LAYER 1a hecke-engine        LAYER 1b  pyhecke
            (Rust, 14 k LOC)            (pure Python, 1.8 k LOC)
                │                         │
                ▼                         │
LAYER 2   pyhecke-native (PyO3)           │
          snappea-wasm (Emscripten)       │
                │                         │
                └────────────┬────────────┘
                             ▼
LAYER 3   539 compute scripts → 858 .witness.json files
                             ▼
LAYER 4   content/ (TS) — 450 blocks → paper PDF
```

See [docs/canonical-derivation-cheat-sheet.md](https://github.com/litlfred/qou/blob/main/docs/canonical-derivation-cheat-sheet.md) for the framework overview and [docs/workplans/2026-05-24-library-reuse-production-readiness.md](https://github.com/litlfred/qou/blob/main/docs/workplans/2026-05-24-library-reuse-production-readiness.md) for the publication roadmap.

## License

MIT. See [LICENSE](https://github.com/litlfred/qou/blob/main/LICENSE) in the parent repository.
