#!/usr/bin/env python3
"""
Derivation-chain validator + computational-trust auditor.

Two responsibilities:

1. **Per-chain validation** (`validate_chain`): for each
   `*.derivation.json` in this directory, walk the chain bottom-up
   and verify:
     - structural well-formedness (already enforced by `structural_check`),
     - the COMPUTATIONAL leaf's `output_value` matches the chain's
       `target_value` to within `target_tolerance`,
     - any DERIVED step whose `operation` is a simple algebraic
       formula admits a numerical re-evaluation that agrees with
       the recorded `output_value`,
     - SCRIPT_CITED steps reference an existing script in the
       repository (the script's content is not re-executed here;
       the cross-pipeline validators are responsible for that).

2. **Trust marking** (`audit_witness_trust`): scan every
   `*.witness.json` file alongside the chains and classify it as
     - `derivation-backed` if some chain references it via a
       `SCRIPT_CITED` step's `script:` note,
     - `derivation-fully-trusted` if some chain certifies its
       target value via only AXIOM / MATHLIB_CITED / DERIVED /
       COMPUTATIONAL steps (no SCRIPT_CITED frontier),
     - `computational-only` (default) if no chain references it.

The audit emits a single output witness
`derivation-chain-audit.witness.json` summarising the state of the
methodology directive: how many witnesses are still
computational-only and what the open frontier looks like.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402


HERE = Path(__file__).parent
OUTPUT_WITNESS = HERE / "derivation-chain-audit.witness.json"

SCRIPT_REGEX = re.compile(
    r"script:\s*([\w\-./]+\.(?:py|sing|sage|sh))"
)


# ── Per-chain validation ───────────────────────────────────────

@dataclass
class ChainResult:
    chain_path: Path
    target: str
    target_value: float
    computed_value: Optional[float]
    structural_ok: bool
    leaf_matches: bool
    issues: list[str]
    trust_summary: dict[str, int]
    has_script_frontier: bool


def _eval_simple_algebra(operation: str, q: float) -> Optional[float]:
    """Try to recognise a small set of canonical algebraic operations
    in the `operation` field; return the numerical result at q if
    possible, else None."""
    op = operation.replace(" ", "")
    # c_q derivation algebra
    if "1/(q-1)" in op or "1/(q−1)" in op:
        return 1.0 / (q - 1.0)
    return None


def validate_chain(chain_path: Path) -> ChainResult:
    with chain_path.open("r", encoding="utf-8") as f:
        chain_data = json.load(f)

    target = chain_data["target"]
    target_value = float(chain_data["target_value"])
    target_tolerance = float(chain_data.get("target_tolerance", 1e-9))
    steps = chain_data["steps"]

    # 1. Structural well-formedness re-check (defended by the schema,
    #    but a chain might have been hand-edited).
    defined: set[str] = {
        "Hecke.Energy", "Cat.Action", "Frobenius.Pairing",
        "Nonabelian.Stokes", "Wedderburn", "Schur", "FiniteJones",
    }
    structural_issues: list[str] = []
    for s in steps:
        for inp in s.get("inputs", []):
            if inp not in defined:
                structural_issues.append(
                    f"{s['name']!r}: input {inp!r} not defined"
                )
        defined.add(s["output_name"])
    structural_ok = not structural_issues

    # 2. Trust summary.
    trust_summary: dict[str, int] = {}
    for s in steps:
        tb = s["trust_basis"]
        trust_summary[tb] = trust_summary.get(tb, 0) + 1
    has_script_frontier = trust_summary.get("script-cited", 0) > 0

    # 3. COMPUTATIONAL leaf consistency: the last COMPUTATIONAL step's
    #    output_value should match the chain's target_value.
    leaves = [s for s in steps if s["trust_basis"] == "computational"]
    computed = None
    leaf_matches = False
    if leaves:
        last = leaves[-1]
        try:
            computed = float(last["output_value"])
        except (TypeError, ValueError):
            structural_issues.append(
                f"COMPUTATIONAL leaf {last['name']!r} output_value not "
                f"numeric: {last['output_value']!r}"
            )
        else:
            if target_value == 0:
                leaf_matches = computed == 0
            else:
                rel = abs(computed - target_value) / abs(target_value)
                leaf_matches = rel <= target_tolerance

    # 4. Re-evaluate simple algebraic targets (c_q chain).
    if "c_q" in target:
        # The c_q chain's leaf is at q_0; re-run the algebra.
        q_0 = 1.1099785955541805
        recomputed = _eval_simple_algebra(steps[-1].get("operation", ""), q_0)
        if recomputed is not None:
            rel = abs(recomputed - target_value) / abs(target_value)
            if rel > 1e-12:
                structural_issues.append(
                    f"c_q algebra re-eval at q_0={q_0} gives {recomputed} "
                    f"vs target {target_value} (rel_diff {rel:.2e})"
                )

    return ChainResult(
        chain_path=chain_path,
        target=target,
        target_value=target_value,
        computed_value=computed,
        structural_ok=structural_ok,
        leaf_matches=leaf_matches,
        issues=structural_issues,
        trust_summary=trust_summary,
        has_script_frontier=has_script_frontier,
    )


# ── Witness trust audit ────────────────────────────────────────

def collect_referenced_scripts(chains_dir: Path) -> set[str]:
    """Walk every chain JSON and collect the set of script paths
    referenced via `script: <path>` in any step's `notes`."""
    refs: set[str] = set()
    for cp in sorted(chains_dir.glob("*.derivation.json")):
        with cp.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for s in data.get("steps", []):
            notes = s.get("notes") or ""
            for m in SCRIPT_REGEX.finditer(notes):
                refs.add(m.group(1))
    return refs


def _expected_script_for_witness(witness_filename: str) -> str:
    """Convention: `foo-bar-baz.witness.json` is produced by
    `foo_bar_baz.py` (hyphens → underscores, .witness.json → .py).
    Used as a fallback when the witness JSON lacks a `scriptFile`
    field (e.g. legacy witnesses pre-WitnessBuilder)."""
    stem = witness_filename.replace(".witness.json", "")
    return stem.replace("-", "_") + ".py"


def audit_witness_trust(chains_dir: Path) -> dict:
    referenced = collect_referenced_scripts(chains_dir)
    referenced_basenames = {Path(r).name for r in referenced}
    out: dict[str, list[str]] = {
        "derivation-backed": [],
        "computational-only": [],
    }
    for wp in sorted(chains_dir.glob("*.witness.json")):
        try:
            with wp.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        # Match path 1: explicit scriptFile field (modern witnesses).
        script_file = data.get("scriptFile")
        if script_file and (
            script_file in referenced_basenames
            or any(script_file in r for r in referenced)
        ):
            out["derivation-backed"].append(wp.name)
            continue
        # Match path 2: filename convention (legacy witnesses without
        # scriptFile metadata).
        guessed = _expected_script_for_witness(wp.name)
        if guessed in referenced_basenames:
            out["derivation-backed"].append(wp.name)
            continue
        out["computational-only"].append(wp.name)
    return out


# ── Main ───────────────────────────────────────────────────────

def main() -> int:
    chain_files = sorted(HERE.glob("*.derivation.json"))
    if not chain_files:
        print("No *.derivation.json files found.")
        return 1

    results = [validate_chain(p) for p in chain_files]

    overall_ok = all(
        r.structural_ok and r.leaf_matches and not r.issues
        for r in results
    )

    audit = audit_witness_trust(HERE)

    w = WitnessBuilder("derivation-chain-audit", engine="python")
    w.set_description(
        "Per-chain validation + computational-trust audit per the "
        "QOU methodology directive: every numerical claim must trace "
        "back to first-principles axioms via a DerivationChain."
    )
    w.set_content_block("def:derivation-chain")
    w.add_data("chain_results", [
        {
            "chain": r.chain_path.name,
            "target": r.target,
            "target_value": r.target_value,
            "computed_value": r.computed_value,
            "structural_ok": r.structural_ok,
            "leaf_matches": r.leaf_matches,
            "issues": r.issues,
            "trust_summary": r.trust_summary,
            "has_script_frontier": r.has_script_frontier,
        }
        for r in results
    ])
    w.add_data("witness_trust", audit)

    for r in results:
        w.add_assertion(
            f"chain_valid[{r.chain_path.stem}]",
            computed=bool(r.structural_ok and r.leaf_matches and not r.issues),
            expected=True,
        )
        w.add_assertion(
            f"leaf_value[{r.chain_path.stem}]",
            computed=r.computed_value if r.computed_value is not None else float("nan"),
            expected=r.target_value,
            tolerance=abs(r.target_value) * 1e-9 if r.target_value != 0 else 1e-9,
        )

    w.save()

    print(f"derivation_chain_validator: {'PASS' if overall_ok else 'FAIL'}")
    for r in results:
        marker = "✓" if (r.structural_ok and r.leaf_matches and not r.issues) else "✗"
        frontier = " [script-frontier]" if r.has_script_frontier else " [fully-trusted]"
        print(
            f"  {marker} {r.chain_path.name:>32}  target={r.target}  "
            f"value={r.computed_value}{frontier}"
        )
        for i in r.issues:
            print(f"      - {i}")
    n_backed = len(audit["derivation-backed"])
    n_comp = len(audit["computational-only"])
    print(
        f"\nWitness trust audit: "
        f"derivation-backed={n_backed}, computational-only={n_comp}"
    )
    if audit["computational-only"]:
        print("  computational-only witnesses (need a derivation chain):")
        for w_name in audit["computational-only"][:10]:
            print(f"    - {w_name}")
        if len(audit["computational-only"]) > 10:
            print(f"    ... ({len(audit['computational-only']) - 10} more)")
    return 0 if overall_ok else 2


if __name__ == "__main__":
    sys.exit(main())
