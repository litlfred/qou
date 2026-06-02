#!/usr/bin/env python3

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
P2.5 audit: scan every witness-emitting Python script under
`folio-assistant/computations/` and triage each as

  * **compliant**: uses sympy.Symbol('q') symbolically and
    substitutes q₀ only at final reporting; emits a `polynomial_q`
    or equivalent symbolic field in the witness JSON;
  * **mpmath-only**: uses mpmath at the canonical Q_MP precision
    but never substitutes a separate fit; functionally compliant
    in spirit (no early q₀-fit) but doesn't expose a symbolic form;
  * **early-substitution**: substitutes q₀ to a float at script
    start and computes everything numerically afterwards. Reads as
    "fitted" in witness JSONs even when no fit is actually
    happening. **Refactor target.**
  * **no-q-dependence**: doesn't reference q at all (e.g., AME data
    loaders, structural utilities). Out of scope.

Output: `p2-5-symbolic-q-audit.witness.json` listing per-script
classification + the prioritised refactor target list (top-20 by
witness-JSON visibility).

Refs:
  docs/audits/2026-05-01-math-framework-deep-audit.md §3·E
  docs/audits/2026-05-01-math-framework-workplan.md P2.5
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COMPUTE = REPO / "folio-assistant" / "computations"

# ── Triage signatures ────────────────────────────────────────────

# A script is COMPLIANT if it satisfies all of:
SYMBOLIC_Q = re.compile(
    r"sp\.Symbol\(['\"]q['\"]|sympy\.Symbol\(['\"]q['\"]|"
    r"q\s*=\s*sp\.Symbol|q\s*=\s*sympy\.Symbol"
)
SUBS_AT_END = re.compile(
    r"\.subs\(q,\s*q0?\b|\.subs\(\{?\s*q\s*[:,]\s*q0?",
    re.IGNORECASE,
)
EMITS_SYMBOLIC = re.compile(
    # Broadened 2026-05-02: catches more symbolic-emit conventions
    # (e.g. `schur_element`, `*_expression`, `*_form`, `*_eq`, etc.)
    # in addition to the original `*_symbolic` / `*_polynomial_q`.
    r'"(?:polynomial_q|polynomial|symbolic'
    r'|.*_symbolic|.*_polynomial_q|q_polynomial'
    r'|.*_element|.*_expression|.*_eq|.*_form|.*_polynomial)":'
)

# A script is MPMATH-ONLY if it imports/uses mpmath at canonical
# Q_MP but doesn't go through a separate q₀-fit:
MPMATH_USE = re.compile(r"import\s+mpmath|from\s+mpmath\s+import|Q_MP\b")

# A script is EARLY-SUBSTITUTION if it substitutes a float q₀ near
# the top (within first 100 lines) without any sympy.Symbol step:
FLOAT_Q0_NEAR_TOP = re.compile(
    r"q0?\s*=\s*[0-9]+\.[0-9]+|"
    r"q0?\s*=\s*float\(.*\)"
)

# No-q-dependence:
ANY_Q_REF = re.compile(r"\bq\b|\bQ\b|q_0|substrate")


def emits_witness(text: str) -> bool:
    return bool(re.search(r'\.witness\.json', text))


def classify(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return {"path": path.relative_to(REPO).as_posix(),
                "category": "unreadable", "error": str(exc)}
    head = text[:5000]  # first ~100 lines for early-sub heuristic
    rel = path.relative_to(REPO).as_posix()
    base = {
        "path": rel,
        "size_lines": len(text.splitlines()),
        "emits_witness": emits_witness(text),
    }
    if not ANY_Q_REF.search(text):
        return {**base, "category": "no-q-dependence"}
    has_symbolic = bool(SYMBOLIC_Q.search(text))
    has_subs_at_end = bool(SUBS_AT_END.search(text))
    has_emit_sym = bool(EMITS_SYMBOLIC.search(text))
    has_mpmath = bool(MPMATH_USE.search(text))
    has_early_float = bool(FLOAT_Q0_NEAR_TOP.search(head))
    if has_symbolic and (has_subs_at_end or has_emit_sym):
        return {**base, "category": "compliant",
                "details": {"symbolic_q": True,
                            "subs_at_end": has_subs_at_end,
                            "emits_symbolic_field": has_emit_sym}}
    if has_mpmath and not has_early_float:
        return {**base, "category": "mpmath-only",
                "details": {"mpmath_canonical_q": True}}
    if has_early_float and not has_symbolic:
        return {**base, "category": "early-substitution",
                "details": {"float_q_near_top": True,
                            "no_symbolic_q": True}}
    if has_symbolic:
        return {**base, "category": "partial",
                "details": {"symbolic_q": True,
                            "missing_subs_or_emit": True}}
    return {**base, "category": "uncategorised",
            "details": {"has_mpmath": has_mpmath,
                        "has_early_float": has_early_float}}


def main() -> int:
    py_files = sorted(COMPUTE.glob("*.py"))
    classifications = [classify(p) for p in py_files]
    by_category = {}
    for c in classifications:
        cat = c.get("category", "uncategorised")
        by_category.setdefault(cat, []).append(c)
    # Refactor target list: early-substitution scripts, prioritised
    # by witness-JSON visibility (those that emit witnesses come
    # first), then by size (larger scripts touch more).
    targets = sorted(
        by_category.get("early-substitution", []),
        key=lambda c: (not c.get("emits_witness", False),
                       -c.get("size_lines", 0)),
    )[:20]
    witness = {
        "computation": "p2-5-symbolic-q-audit",
        "purpose": (
            "P2.5 audit: triage every Python script in "
            "folio-assistant/computations/ as compliant / "
            "mpmath-only / partial / early-substitution / "
            "no-q-dependence. Emits the prioritised refactor "
            "target list (top-20 by witness-JSON visibility)."
        ),
        "narrative_block": "audit §3·E + workplan P2.5",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "n_files_total": len(py_files),
        "category_counts": {cat: len(items) for cat, items in by_category.items()},
        "top_refactor_targets": [
            {"path": t["path"],
             "size_lines": t.get("size_lines"),
             "emits_witness": t.get("emits_witness", False)}
            for t in targets
        ],
        "classifications": classifications,
    }
    out = COMPUTE / "p2-5-symbolic-q-audit.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"  Witness written to {out.relative_to(REPO).as_posix()}")
    print(f"  Files audited: {len(py_files)}")
    print(f"  Category counts:")
    for cat, items in sorted(by_category.items(), key=lambda x: -len(x[1])):
        print(f"    {cat:>22s}: {len(items)}")
    print()
    print(f"  Top {len(targets)} refactor targets:")
    for t in targets:
        flag = "🟠" if t.get("emits_witness") else "·"
        print(f"    {flag} {t['size_lines']:>4d} lines  "
              f"{t['path']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
