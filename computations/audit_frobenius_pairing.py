#!/usr/bin/env python3
"""
Frobenius-pairing compute audit — classifies every script under
``computations/`` that touches a Markov trace
(``tr_M``, ``markov_trace``, or any "trace of a braid word" pattern)
into one of three buckets, per the master formula

    ⟨O⟩_T = Σ_{i,j ∈ A*(T)}  u_i*  (G^{-1})_{ij}  ⟨O, b_j⟩

(conj:confinement-frobenius-reciprocity).

Buckets
-------

(A) **Trace-only.**  The script computes ``tr_M(W)`` directly — for
    example to evaluate a binding-energy / mass-defect of a closed
    braid word.  This is a CORRECT use of the raw Markov trace: the
    binding observable is the Hamiltonian $H$ acting diagonally on
    NF basis elements, and the categorical mass identity reduces to
    $|\\mathrm{tr}_M(W)|$ at single brane level
    (knot-factor-frobenius-pairing § Step 1).

(B) **Observable-on-state.**  The script computes
    ``tr_M(O · ρ(β_T))`` for some non-Hamiltonian observable $O$.
    The dependence on $T$ is then the *raw* Frobenius pairing
    $\\langle O, T\\rangle$, NOT the physical expectation value
    $\\langle O\\rangle_T$.  To recover physics, the script must
    apply the Gram inverse $G^{-1}$ AND restrict to the LP-active
    set $A^*(T)$ with shadow-price weights $u^*$.  A script is
    **correct in bucket (B)** iff its witness exposes the four
    fields ``gram_matrix``, ``gram_inverse``, ``lp_active_set``,
    ``shadow_prices``.

(C) **Conjugation pattern $\\mathrm{tr}_M(\\beta\\,X\\,\\beta^{-1})$.**
    By cyclicity of the Markov trace this equals
    $\\mathrm{tr}_M(X)$ exactly, independent of $\\beta$.  Any script
    that interprets such a quantity as a "bound-state observable
    for braid $\\beta$" is structurally wrong — the dependence on
    $\\beta$ has been silently erased.  These are confirmed bugs;
    the fix is always to replace the conjugation pattern with the
    master formula above.

Output
------

A JSON report listing, for each bucket, the scripts found, the
matched pattern, and (for (B) and (C)) whether the sibling witness
exposes the bound-state-observable fields.

Usage
-----
    python3 computations/audit_frobenius_pairing.py [--report PATH]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Optional

# ── Patterns ────────────────────────────────────────────────────

# (A) trace-only: any reference to tr_M / markov_trace / TR_M.
TRACE_TOKEN = re.compile(
    r"\b(tr_M|markov_trace|MarkovTrace|TR_M|tr_markov|atom_markov_trace)\b"
)

# (B) observable-on-state: trace applied to a product of an operator
#     and a braid representation, e.g. tr(O @ rho(beta)) /
#     mat_trace(O · M_braid). We look for trace(...) / tr_*(...) where
#     the argument contains a multiplication / matmul AND a "rho",
#     "M_", "evaluate_braid", "ρ(β" or similar braid-evaluation token.
OBS_PATTERN = re.compile(
    r"(?:tr_M|markov_trace|mat_trace|trace_std|tr_std|tr_standard"
    r"|np\.trace|sympy\.trace|Trace)\s*\("
    r"[^()\n]{0,200}?"
    r"(?:@|\*|·|matmul|dot|hecke_mul)"
    r"[^()\n]{0,200}?"
    r"(?:rho|M_braid|M_std|M_full|evaluate_braid|braid_matrix|"
    r"sigma\d|σ\d|s1|s2|conversion_op)"
)

# (B) observable-on-state, secondary heuristic: a braid word built by
# concatenating an explicit operator variable into a "bound-state"
# braid variable, then traced. Catches patterns like
#     full_op = beta_borr + conversion_op + beta_borr_inv
# even when the trace call doesn't lexically contain the operator name.
# Kept simple to avoid catastrophic regex backtracking on large files.
OBS_OP_CONCAT = re.compile(
    r"\b(?:full_op|op_braid|obs_braid|operator_word|conv_word)\s*="
)

# (C) conjugation pattern: a comment OR a code construct that
#     concatenates a braid word with its own inverse around something.
CONJ_PATTERN_CODE = re.compile(
    r"(beta[a-zA-Z0-9_]*)\s*\+\s*"
    r"(?:[a-zA-Z_][a-zA-Z0-9_]*\s*\+\s*)?"
    r"(beta[a-zA-Z0-9_]*_inv|\1_inv)"
)
CONJ_PATTERN_COMMENT = re.compile(
    r"(?:β\s*[·.* ]\s*[A-Za-z_]\w*\s*[·.* ]\s*β\s*[⁻^]\s*1"
    r"|beta\s*\*\s*\w+\s*\*\s*beta_?inv"
    r"|β·σ_?\d+·β\s*[⁻^]?\s*1?"
    r"|β\\cdot\s*\w+\\cdot\s*β\^?-?1)"
)

REQUIRED_FIELDS = (
    "gram_matrix",
    "gram_inverse",
    "lp_active_set",
    "shadow_prices",
)
OPTOUT_FIELD = "observable_type"
OPTOUT_VALUE = "raw_trace"


# ── Helpers ─────────────────────────────────────────────────────

def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _sibling_witnesses(script: Path) -> list[Path]:
    """Heuristic: same-directory *.witness.json with stem matching
    the script's stem (with both - and _ variants)."""
    stem = script.stem
    candidates = {stem, stem.replace("_", "-"), stem.replace("-", "_")}
    out = []
    for cand in candidates:
        for suffix in (".witness.json", "-witness.json"):
            p = script.parent / f"{cand}{suffix}"
            if p.exists():
                out.append(p)
    return sorted(set(out))


def _witness_has_required(path: Path) -> tuple[bool, list[str], bool]:
    """Returns (ok, missing_fields, opted_out)."""
    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return False, list(REQUIRED_FIELDS), False

    def _has(node, key):
        if isinstance(node, dict):
            if key in node:
                return True
            return any(_has(v, key) for v in node.values())
        if isinstance(node, list):
            return any(_has(v, key) for v in node)
        return False

    # Opt-out: top-level observable_type == "raw_trace"
    opted_out = data.get(OPTOUT_FIELD) == OPTOUT_VALUE
    missing = [f for f in REQUIRED_FIELDS if not _has(data, f)]
    return (not missing) or opted_out, missing, opted_out


# ── Classification ──────────────────────────────────────────────

def classify(script: Path) -> dict:
    text = _read(script)
    if not TRACE_TOKEN.search(text) and not re.search(
        r"\b(?:mat_trace|tr_std|tr_standard|trace_std)\b", text
    ):
        return {"bucket": "skip", "reason": "no trace token"}

    bucket_c = bool(
        CONJ_PATTERN_CODE.search(text) or CONJ_PATTERN_COMMENT.search(text)
    )
    bucket_b = bool(OBS_PATTERN.search(text) or OBS_OP_CONCAT.search(text))
    bucket_a = TRACE_TOKEN.search(text) is not None

    if bucket_c:
        bucket = "C"
        reason = "conjugation pattern β · X · β⁻¹"
    elif bucket_b:
        bucket = "B"
        reason = "trace(O · ρ(β)) — observable-on-state"
    elif bucket_a:
        bucket = "A"
        reason = "raw tr_M / markov_trace (no operator-on-state)"
    else:
        return {"bucket": "skip", "reason": "no trace pattern"}

    witnesses = _sibling_witnesses(script)
    witness_status = []
    for w in witnesses:
        ok, missing, opted_out = _witness_has_required(w)
        witness_status.append(
            {
                "witness": str(w.relative_to(Path(__file__).resolve().parents[1])),
                "ok": ok,
                "missing_fields": missing,
                "opted_out_raw_trace": opted_out,
            }
        )
    return {
        "bucket": bucket,
        "reason": reason,
        "witnesses": witness_status,
    }


# ── Driver ──────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "--report",
        default="docs/audits/frobenius-pairing-compute-audit.witness.json",
        help="Output JSON report path (relative to repo root)",
    )
    parser.add_argument(
        "--root",
        default="computations",
        help="Directory to scan",
    )
    args = parser.parse_args()

    here = Path(__file__).resolve()
    repo_root = here.parents[1]
    scan_dir = (repo_root / args.root).resolve()
    out_path = (repo_root / args.report).resolve()

    by_bucket: dict[str, list[dict]] = {"A": [], "B": [], "C": [], "skip": []}
    scripts = sorted(scan_dir.glob("*.py"))
    for s in scripts:
        if s.name.startswith("audit_frobenius_pairing"):
            continue
        if s.name in {"witness_base.py", "lp_dual_solver.py",
                      "lp_dual_witness_validator.py",
                      "bound_state_observable_validator.py"}:
            # infra, not a compute script
            continue
        result = classify(s)
        result["script"] = s.relative_to(repo_root).as_posix()
        by_bucket[result["bucket"]].append(result)

    # Failures: (B) or (C) with witnesses missing required fields
    failures = []
    for bucket in ("B", "C"):
        for entry in by_bucket[bucket]:
            for w in entry.get("witnesses", []):
                if not w["ok"]:
                    failures.append(
                        {
                            "script": entry["script"],
                            "bucket": bucket,
                            "witness": w["witness"],
                            "missing": w["missing_fields"],
                        }
                    )

    summary = {
        "scan_dir": args.root,
        "n_scripts_scanned": len(scripts),
        "counts": {b: len(v) for b, v in by_bucket.items()},
        "buckets": by_bucket,
        "failures": failures,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    summary.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        summary, script_path=__file__, engine=None, q0_anchor=False)
    out_path.write_text(json.dumps(summary, indent=2))

    print(f"Scanned {len(scripts)} scripts under {args.root}")
    for b in ("A", "B", "C", "skip"):
        print(f"  bucket {b}: {len(by_bucket[b])}")
    print(f"\nFailures (bound-state-observable witnesses missing required fields):")
    print(f"  {len(failures)}")
    for f in failures[:20]:
        print(f"    ✗ [{f['bucket']}] {f['script']} -> {f['witness']}")
        print(f"        missing: {f['missing']}")
    if len(failures) > 20:
        print(f"    ... ({len(failures) - 20} more)")

    print(f"\nReport written to {out_path}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
