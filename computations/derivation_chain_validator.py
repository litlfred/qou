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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import FirstPrinciple, Q_0  # noqa: E402
from witness_producer_executes_audit import (  # noqa: E402
    is_prose as _is_prose,
    producer_of as _producer_of,
)
from witness_base import WitnessBuilder  # noqa: E402
from mpmath import mp, mpf  # noqa: E402 — chain values are carried as mpf, never float64

mp.dps = 50


HERE = Path(__file__).parent
# The audit's own output filename — excluded from the trust audit so
# the audit does not classify itself as `computational-only`.
AUDIT_WITNESS_NAME = "derivation-chain-audit.witness.json"

# Repo root resolution: prefer the `QOU_REPO_ROOT` env var if set
# (lets CI / external runners override the relative path).  Default
# walks up from this file via `.git` discovery, falling back to
# `HERE.parent.parent` (i.e. <repo>/computations →
# <repo>) which is the standard layout.
def _resolve_repo_root() -> Path:
    env_root = os.environ.get("QOU_REPO_ROOT")
    if env_root:
        return Path(env_root).resolve()
    cur = HERE.resolve()
    for ancestor in [cur, *cur.parents]:
        if (ancestor / ".git").exists():
            return ancestor
    return HERE.parent.parent


REPO_ROOT = _resolve_repo_root()

# Match `script:` or `Script:` (case-insensitive); accommodates legacy
# chains that use the capitalized form.
SCRIPT_REGEX = re.compile(
    r"script:\s*([\w\-./]+\.(?:py|sing|sage|sh))",
    re.IGNORECASE,
)


# ── Per-chain validation ───────────────────────────────────────

@dataclass
class ChainResult:
    chain_path: Path
    target: str
    target_value: Any
    target_is_numeric: bool
    target_tolerance: Any
    computed_value: Optional[Any]
    structural_ok: bool
    leaf_matches: bool
    issues: list[str]
    trust_summary: dict[str, int]
    has_script_frontier: bool


def _eval_simple_algebra(operation: str, q: Any) -> Optional[Any]:
    """Try to recognise a small set of canonical algebraic operations
    in the `operation` field; return the numerical result at q if
    possible, else None.

    Arithmetic is done in `mpf`, not float64: `c_q = 1/(q - 1)` amplifies its
    input by q/(q-1) ~ 10, so a float64 round-trip here would eat a decade of
    the 1e-12 tolerance the chains are checked against.
    """
    op = operation.replace(" ", "")
    # c_q derivation algebra
    if "1/(q-1)" in op or "1/(q−1)" in op:
        qq = q if isinstance(q, mpf) else mpf(str(q))
        return mpf(1) / (qq - 1)
    return None


#: `q_0 = <digits>` as written into a chain step's prose `operation` field.
_DECLARED_Q0_RE = re.compile(r"q_0\s*=\s*([0-9]+\.[0-9]+)")


def _declared_q0(operation: str) -> Optional[Any]:
    """The q_0 a chain step *declares it evaluated at*, as `mpf`, or None.

    A chain records which substrate pin it was built against; the module-level
    `Q_0` is the experimental (proton) pin that new compute defaults to
    (AGENTS.md, owner directive 2026-08-07).  Re-evaluating a muon-pinned chain
    against the proton `Q_0` mixes the two layers inside one comparison, which
    is the straddle AGENTS.md forbids -- and `c_q` amplifies the ~11.5 ppb
    mu-p tension to ~1.16e-7, three decades past the 1e-12 chain tolerance, so
    the straddle reads as a hard formula failure rather than as the pin
    difference it is.  Prefer the chain's own declared pin; fall back to `Q_0`
    only for a chain that names none.

    The migration posture (AGENTS.md rule 4) keeps recorded muon-layer
    artifacts as recorded until the tracked sweep (bean `qou-1c4y`) runs, so
    this check must be able to validate them where they stand.
    """
    m = _DECLARED_Q0_RE.search(operation)
    return mpf(m.group(1)) if m else None


def _ser(v: Any) -> Any:
    """Serialize a carried value for the witness.

    `mpf` is not JSON-serializable, and `float(v)` would reintroduce exactly the
    float64 downcast this module now avoids, so numeric values leave as
    full-precision decimal text.  `WitnessBuilder.add_assertion` documents
    strings as the drained convention (qou-t0rf) and still coerces with
    `float()` for the pass/fail decision, so nothing downstream changes.
    """
    return mp.nstr(v, mp.dps) if isinstance(v, mpf) else v


def validate_chain(chain_path: Path) -> ChainResult:
    with chain_path.open("r", encoding="utf-8") as f:
        # `parse_float=str` keeps every JSON float literal as its exact source
        # text, so `mpf` below reads the authored digits rather than a value
        # already rounded through float64.  Without this the downcast happens
        # inside `json`, before this module ever sees the number.
        chain_data = json.load(f, parse_float=str)

    target = chain_data["target"]
    target_value_raw = chain_data["target_value"]
    try:
        target_value: Any = mpf(str(target_value_raw))
        target_is_numeric = True
    except (TypeError, ValueError):
        target_value = target_value_raw
        target_is_numeric = False
    target_tolerance = mpf(str(chain_data.get("target_tolerance", "1e-9")))
    steps = chain_data["steps"]

    # 1. Structural well-formedness re-check (defended by the schema,
    #    but a chain might have been hand-edited).  Initialise the
    #    `defined` set from the canonical FirstPrinciple enum to avoid
    #    drift between schema and validator.
    defined: set[str] = {fp.value for fp in FirstPrinciple}
    structural_issues: list[str] = []
    for i, s in enumerate(steps):
        # 1. inputs reference earlier outputs or first principles
        for inp in s.get("inputs", []):
            if inp not in defined:
                structural_issues.append(
                    f"{s['name']!r}: input {inp!r} not defined"
                )

        trust_basis = s.get("trust_basis")

        # 2. AXIOM / MATHLIB_CITED / LEAN_PROVEN must declare lean_ref
        if trust_basis in {"axiom", "mathlib-cited", "lean-proven"} \
                and not s.get("lean_ref"):
            structural_issues.append(
                f"{s['name']!r}: {trust_basis} step requires lean_ref"
            )

        # 3. SCRIPT_CITED must include a `script:` note + the cited
        #    script must exist on disk
        if trust_basis == "script-cited":
            notes = s.get("notes") or ""
            matches = list(SCRIPT_REGEX.finditer(notes))
            if not matches:
                structural_issues.append(
                    f"{s['name']!r}: script-cited step requires a "
                    "`script: <path>` note"
                )
            for m in matches:
                script_path = REPO_ROOT / m.group(1)
                if not script_path.exists():
                    # Dead-code sweep (commit 191bd9f5) moved retired
                    # producers under computations/_deprecated/.
                    # Accept the cited script if a copy exists there;
                    # provenance is preserved for future refresh.
                    deprecated_path = (
                        script_path.parent / "_deprecated" /
                        script_path.name
                    )
                    if not deprecated_path.exists():
                        structural_issues.append(
                            f"{s['name']!r}: cited script {m.group(1)!r} "
                            f"not found at {script_path}"
                        )

        # 4. COMPUTATIONAL is the leaf only
        if trust_basis == "computational" and i != len(steps) - 1:
            structural_issues.append(
                f"{s['name']!r}: computational step must be the final "
                "step (numerical eval is leaf-only)"
            )

        defined.add(s["output_name"])
    structural_ok = not structural_issues

    # 2. Trust summary.
    trust_summary: dict[str, int] = {}
    for s in steps:
        tb = s["trust_basis"]
        trust_summary[tb] = trust_summary.get(tb, 0) + 1
    has_script_frontier = trust_summary.get("script-cited", 0) > 0

    # 3. COMPUTATIONAL leaf consistency.  Symbolic chains (no
    #    COMPUTATIONAL leaf, target_value is a string formula) are
    #    vacuously leaf-matched.
    leaves = [s for s in steps if s["trust_basis"] == "computational"]
    computed = None
    if not target_is_numeric and not leaves:
        leaf_matches = True
    elif not target_is_numeric and leaves:
        structural_issues.append(
            "chain has a COMPUTATIONAL leaf but target_value is not numeric "
            f"({target_value!r})"
        )
        leaf_matches = False
    elif target_is_numeric and not leaves:
        structural_issues.append(
            f"chain target_value is numeric ({target_value}) but no "
            "COMPUTATIONAL leaf step is present"
        )
        leaf_matches = False
    else:
        last = leaves[-1]
        try:
            computed = mpf(str(last["output_value"]))
        except (TypeError, ValueError):
            structural_issues.append(
                f"COMPUTATIONAL leaf {last['name']!r} output_value not "
                f"numeric: {last['output_value']!r}"
            )
            leaf_matches = False
        else:
            if target_value == 0:
                leaf_matches = computed == 0
            else:
                rel = abs(computed - target_value) / abs(target_value)
                leaf_matches = rel <= target_tolerance

    # 4. Re-evaluate simple algebraic targets (c_q chain) at the shared Q_0.
    if "c_q" in target and target_is_numeric:
        leaf_op = steps[-1].get("operation", "")
        declared = _declared_q0(leaf_op)
        q_eval = declared if declared is not None else mpf(str(Q_0))
        pin = "chain-declared" if declared is not None else "module Q_0 (proton)"
        recomputed = _eval_simple_algebra(leaf_op, q_eval)
        if recomputed is not None:
            rel = abs(recomputed - target_value) / abs(target_value)
            if rel > target_tolerance:
                structural_issues.append(
                    f"c_q algebra re-eval at q_0={mp.nstr(q_eval, 20)} "
                    f"[{pin}] gives {mp.nstr(recomputed, 20)} "
                    f"vs target {target_value} (rel_diff {rel:.2e}, "
                    f"target_tolerance {target_tolerance:.2e})"
                )

    return ChainResult(
        chain_path=chain_path,
        target=target,
        target_value=target_value,
        target_is_numeric=target_is_numeric,
        target_tolerance=target_tolerance,
        computed_value=computed,
        structural_ok=structural_ok,
        leaf_matches=leaf_matches,
        issues=structural_issues,
        trust_summary=trust_summary,
        has_script_frontier=has_script_frontier,
    )


# ── Witness trust audit ────────────────────────────────────────

def _scan(root: Path, pattern: str) -> list[Path]:
    """Recursively collect `pattern` under `root`, skipping the retired-producer
    archive `_deprecated/`.

    Previously these scans used a NON-recursive `glob`, so every witness and
    chain living in a subdirectory (`probes/`, `qbeta/`, `deltalambda/`,
    `alpha_em/`, ...) was invisible to the trust audit — ~1.25k live witnesses,
    i.e. the audit's "computational-only" headline *understated* the real gap
    rather than overstating it. A coverage hole in a gap-measuring tool is the
    one defect that hides itself, so the scan is recursive.
    """
    return sorted(q for q in root.rglob(pattern) if "_deprecated" not in q.parts)


def collect_referenced_scripts(chains_dir: Path) -> set[str]:
    """Walk every chain JSON and collect the set of script paths
    referenced via `script: <path>` in any step's `notes`."""
    refs: set[str] = set()
    for cp in _scan(chains_dir, "*.derivation.json"):
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


def collect_fully_trusted_scripts(chains_dir: Path) -> set[str]:
    """Walk every chain JSON and collect scripts referenced by chains
    that have **zero** SCRIPT_CITED steps — those scripts are
    derivation-fully-trusted (the chain proves their output from
    first principles, no computational shortcuts)."""
    fully: set[str] = set()
    for cp in _scan(chains_dir, "*.derivation.json"):
        with cp.open("r", encoding="utf-8") as f:
            data = json.load(f)
        steps = data.get("steps", [])
        if any(s.get("trust_basis") == "script-cited" for s in steps):
            continue
        for s in steps:
            notes = s.get("notes") or ""
            for m in SCRIPT_REGEX.finditer(notes):
                fully.add(m.group(1))
    return fully


def audit_witness_trust(chains_dir: Path) -> dict:
    referenced = collect_referenced_scripts(chains_dir)
    referenced_basenames = {Path(r).name for r in referenced}
    fully_trusted = collect_fully_trusted_scripts(chains_dir)
    fully_trusted_basenames = {Path(r).name for r in fully_trusted}

    out: dict[str, list[str]] = {
        "derivation-fully-trusted": [],
        "derivation-backed": [],
        "audit-only-exempt": [],
        "computational-only": [],
    }

    def _is_in_set(witness_name: str, script_field: Optional[str], basenames: set[str], fullpaths: set[str]) -> bool:
        if script_field and (script_field in basenames or any(script_field in r for r in fullpaths)):
            return True
        guessed = _expected_script_for_witness(witness_name)
        return guessed in basenames

    for wp in _scan(chains_dir, "*.witness.json"):
        # Skip the audit's own output to avoid self-reference noise.
        if wp.name == AUDIT_WITNESS_NAME:
            continue
        try:
            with wp.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        # Some witnesses are top-level JSON arrays (e.g. iterative-knot-builder),
        # not objects; tolerate them. Prefer scriptFile from the first dict
        # element (preserves metadata); otherwise fall back to the name-based
        # guess in _is_in_set.
        # `scriptFile` is only ONE of the spellings a witness uses to name its
        # producer -- `producer` and `computation.script` are equally common,
        # and the whole chi-at-q0 family (8 witnesses) declares `producer`.
        # Reading `scriptFile` alone left them uncredited: a chain that claimed
        # their producer moved the count by zero, so the drain looked like it
        # had done nothing. `witness_producer_executes_audit.producer_of` knows
        # every spelling and the categorizer already uses it; use the same one
        # here so the two tools cannot disagree about who produced what.
        if isinstance(data, dict):
            script_file = _producer_of(data)
        elif isinstance(data, list):
            first = next((item for item in data if isinstance(item, dict)), None)
            script_file = _producer_of(first) if first else None
        else:
            script_file = None
        # A prose provenance value ("(legacy -- no matching producer found ...)")
        # names no script; treat it as absent rather than as a basename.
        if script_file and _is_prose(script_file):
            script_file = None
        if script_file:
            script_file = Path(script_file).name
        # A witness that declares `auditOnly` records a QA/audit tool's FINDING,
        # not a derivation of a physical target — demanding a first-principles
        # chain for the output of a sorry-counter is a category error. This is the
        # same basis on which the audit already skips its own witness above; it is
        # reported in a dedicated bucket, never dropped, so the exemption stays
        # visible and auditable rather than shrinking the denominator silently.
        audit_only = isinstance(data, dict) and bool(
            data.get("auditOnly") or data.get("audit_only") or data.get("auditOnlyDoc")
        )
        if _is_in_set(wp.name, script_file, fully_trusted_basenames, fully_trusted):
            out["derivation-fully-trusted"].append(wp.name)
        elif _is_in_set(wp.name, script_file, referenced_basenames, referenced):
            out["derivation-backed"].append(wp.name)
        elif audit_only:
            out["audit-only-exempt"].append(wp.name)
        else:
            out["computational-only"].append(wp.name)
    return out


# ── Main ───────────────────────────────────────────────────────

def main() -> int:
    chain_files = _scan(HERE, "*.derivation.json")
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
    # Audit-only: this is a per-CI-run validator emitting an audit
    # report, not a content-block dependency.  Audit doc cites the
    # CI failure post-mortem that introduced the validator (2026-05-02).
    w.set_audit_only("docs/audits/2026-05-02-pr503-ci-failure-postmortem.md")
    # No `def:derivation-chain` content block exists yet (the
    # methodology lives in `DERIVATION-CHAIN-METHODOLOGY.md`); leaving
    # contentBlock unset avoids generating broken cross-reference
    # warnings in the content pipeline.
    w.add_data("chain_results", [
        {
            "chain": r.chain_path.name,
            "target": r.target,
            "target_value": _ser(r.target_value),
            "computed_value": _ser(r.computed_value),
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
        # Numerical leaf assertions only.  Tolerance honours the
        # chain's declared `target_tolerance` (relative; high-precision
        # chains declare tighter values).  Symbolic chains (no
        # COMPUTATIONAL leaf) skip this — they are validated purely
        # structurally + via `chain_valid[...]` above.
        if r.target_is_numeric and r.computed_value is not None:
            abs_tol = (
                abs(r.target_value) * r.target_tolerance
                if r.target_value != 0
                else r.target_tolerance
            )
            w.add_assertion(
                f"leaf_value[{r.chain_path.stem}]",
                computed=_ser(r.computed_value),
                expected=_ser(r.target_value),
                tolerance=_ser(abs_tol),
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
    n_full = len(audit["derivation-fully-trusted"])
    n_backed = len(audit["derivation-backed"])
    n_comp = len(audit["computational-only"])
    n_exempt = len(audit["audit-only-exempt"])
    print(
        f"\nWitness trust audit: "
        f"fully-trusted={n_full}, derivation-backed={n_backed}, "
        f"audit-only-exempt={n_exempt}, computational-only={n_comp}"
    )
    if audit["derivation-fully-trusted"]:
        print("  derivation-fully-trusted witnesses:")
        for w_name in audit["derivation-fully-trusted"][:5]:
            print(f"    - {w_name}")
    if audit["computational-only"]:
        print("  computational-only witnesses (need a derivation chain):")
        for w_name in audit["computational-only"][:10]:
            print(f"    - {w_name}")
        if len(audit["computational-only"]) > 10:
            print(f"    ... ({len(audit['computational-only']) - 10} more)")
    return 0 if overall_ok else 2


if __name__ == "__main__":
    sys.exit(main())
