# Precision Audit Coverage Extension to `tools/` and `qou-mass/` (`qou-4w77`)

**Date:** 2026-11-24  
**Bean:** `qou-4w77` (parent epic `qou-9nnz`, extracted from `qou-psjm`)  
**Scripts & Witness:**
- [`computations/module_const_precision_audit.py`](../../computations/module_const_precision_audit.py) (`DEFAULT_SCAN_DIRS = ("computations", "tools", "qou-mass")` + `--scan-root`)
- [`computations/audits/tools_qou_mass_precision_audit.py`](../../computations/audits/tools_qou_mass_precision_audit.py) $\to$ [`computations/audits/tools-qou-mass-precision-audit.witness.json`](../../computations/audits/tools-qou-mass-precision-audit.witness.json)
- [`scripts/precision-gates.sh`](../../scripts/precision-gates.sh) (`tools/qou-mass precision` blocking gate with `--strict --no-witness`)

---

## 1. Measured Coverage Gap Before `qou-4w77`

Auditing every gate in `scripts/precision-gates.sh` on `origin/main` (`acb646cc6fe`) showed:

| Precision Gate | Pre-`qou-4w77` Scan Surface | Missing Surface |
|---|---|---|
| `codata_truncation_audit.py` | `computations`, `tools`, `qou-mass`, `scripts` (`#6885`) | None |
| `audits/witness_value_copy_audit.py` | `computations`, `tools`, `qou-mass`, `scripts` | None |
| `codata_corpus_literal_scan.py` | Whole repo (`REPO.rglob("*")`) | None |
| `mpf_context_dps_audit.py` | Whole repo (`ROOT.rglob("*.py")`) | None |
| `numpy_mpmath_dtype_leak_audit.py` | Whole repo (`ROOT.rglob("*.py")`) | None |
| `f64_into_mpmath_audit.py` | Whole repo (`ROOT.rglob("*.py")`) | None |
| `witness_raw_float64_audit.py` | `computations/` + `--scan-root qou-mass/src` baseline | Covered via `--scan-root` |
| **`module_const_precision_audit.py`** | `computations/` **only** | `tools/`, `qou-mass/` |
| **`mpf_float_source_audit.py`** | `computations/`, `tools/` | `qou-mass/` |
| **`never_raises_dps_audit.py`** | `computations/` **only** | `tools/`, `qou-mass/` |
| **`mpf_mixed_arithmetic_audit.py`** | `computations/`, `tools/` | `qou-mass/` |

## 2. Implementation & Contention-Free Design (`qou-v0t8` Safe)

1. **`module_const_precision_audit.py`:** Extended default scan directories from `("computations",)` to `("computations", "tools", "qou-mass")` and added repeatable `--scan-root <dir>` CLI support (writes no witness file, so zero `qou-v0t8` contention).
2. **`computations/audits/tools_qou_mass_precision_audit.py`:** Dedicated `< 0.5s` static gate covering `mpf(<non-dyadic float>)` defects, module-const `LOSSY` literals, `never_raises_dps` witness producers, and `qou-mass/` `mpf_mixed_arithmetic` tainted sinks across all `128` `.py` files in `tools/` and `qou-mass/` (`0` blocking defects measured; `--self-test` verifies both positive detection and zero false positives).
3. **`scripts/precision-gates.sh`:** Wired `tools_qou_mass_precision_audit.py --strict --no-witness` as a blocking gate (`--no-witness` prevents preflight runs from dirtying tracked witnesses on sibling branches).
