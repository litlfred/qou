#!/usr/bin/env python3
"""CAL-4 disguise hunter — extends fitted_labelled_canonical_audit.

The existing audit (`fitted_labelled_canonical_audit.py`, PR #888)
catches the LITERAL pattern: module-level `mp.mpf("<10+ digit
literal>")` definitions that match CODATA-derived constants. After
PR #888 + #892 + #904, all known literal disguises have been
truth-in-named (`LAMBDA_PROTON_FITTED_FROM_CODATA` etc.).

This hunter catches THREE additional disguise patterns the literal
audit does not:

  (A) Möbius / rational q-pencils used as substrate-derived
      formulas without an acknowledged-CAL-4 banner. Example caught
      historically: `a(q) = (4-q)/(4q+3)` (PR #892 demoted to conj:).
  (B) PSLQ search scripts targeting CODATA-derived values that
      claim "substrate", "canonical", or "derived" in their
      docstring without acknowledging the calibration leak.
  (C) Hardcoded high-precision literals (≥ 10 digits) that match
      CODATA-derived ratios at substrate q_0 but are NOT named
      `_FITTED_FROM_CODATA` or wrapped in a `_VALIDATION` suffix.

For each pattern, the hunter:
  - Skips `_deprecated/` and `script-qa/` directories
  - Allows exemption by `# CAL-4` / `# FITTED_FROM_CODATA` /
    `# acknowledged` / `# CAL-[123]` / `# noqa: P3[12]`
  - Emits a witness with the file + line + matched snippet for
    each finding

Run:
    python3 cal4_disguise_hunt.py [--strict]

Emits `cal4-disguise-hunt.witness.json`. With `--strict` exits 1
when findings exist; default exits 0 (advisory).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder

ROOT = HERE
EXEMPT_PATTERN = re.compile(
    r"CAL-4|FITTED_FROM_CODATA|acknowledged|CAL-[123]|cal-[123]|"
    r"noqa:\s*P3[12]|validation only|VALIDATION|"
    r"# polynomial_q_not_applicable|# probe-only|"
    r"# silver_ratio|# golden_ratio|"
    # Hunt A noise reduction (2026-05-22): the (4-q)/(4q+3) pencil
    # is acknowledged across the codebase as conj:mobius-limit-from-
    # thimble (PR #892). Discussions, prints, witness-data labels,
    # and audit narrations all mention it as post-hoc / empirical /
    # fitted — those references are not new disguises.
    r"post.hoc|empirical|fitted|fitting|"
    r"conj:mobius|mobius-limit-from-thimble",
    re.IGNORECASE,
)

# Heuristic A: rational q-pencil with small-integer coefficients in
# the numerator and denominator, of degree ≤ 2 in q each.  Catches
# patterns like `(4 - q) / (4*q + 3)`, `(α + β*q) / (γ*q + δ)`,
# `(q - r) / (q + s)` etc., but NOT polynomial expressions like
# `(q**2 - 2*q - 1) * (q + 1)` (those go through Hunt-C if literal).
MOBIUS_RE = re.compile(
    r"\(\s*"
    r"(?:[+\-]?\d+\s*\*?\s*q|q(?:\s*[+\-]\s*\d+)?|"
    r"[+\-]?\d+\s*[+\-]\s*\d*\s*\*?\s*q|"
    r"[+\-]?\d+\s*[+\-]\s*q)"
    r"\s*\)\s*/\s*\(\s*"
    r"(?:\d+\s*\*?\s*q\s*[+\-]\s*\d+|"
    r"q\s*[+\-]\s*\d+|"
    r"\d+\s*[+\-]\s*\d*\s*\*?\s*q)"
    r"\s*\)"
)

# Heuristic B: PSLQ search whose docstring uses substrate/derived/
# canonical claims AND whose target is a CODATA-derived value.
PSLQ_USE_RE = re.compile(r"mp\.pslq\(|mpmath\.pslq\(|pslq\(")
SUBSTRATE_CLAIM_RE = re.compile(
    r"substrate-(pure|derived|canonical)|canonical-(derive|formula)|"
    r"first-principles|categorical[- ]derived",
    re.IGNORECASE,
)
CODATA_TARGET_RE = re.compile(
    r"M_P_MEV|M_N_MEV|M_E_MEV|Q_BETA_MEV|m_p_codata|m_n_codata|"
    r"codata_m_p|codata_m_n|codata_q_beta|"
    r"VALIDATION|CODATA",
)

# Heuristic C: high-precision literal (≥ 10 digits) not in an
# acknowledged-CAL slot. We re-use the existing literal-audit regex
# but only flag the ones outside `codata_constants.py` and outside
# already-named `_FITTED_*` / `_VALIDATION` slots.
LITERAL_RE = re.compile(
    r"^\s*([A-Z_][A-Z0-9_]*)\s*=\s*"
    r"(?:mp\.)?mpf\(\s*[\"']([0-9]+\.[0-9]{10,})[\"']",
    re.MULTILINE,
)
ALREADY_NAMED_RE = re.compile(
    r"_FITTED_FROM_CODATA$|_VALIDATION$|_CODATA$|_FIT$"
)


def hunt_file(path: Path) -> list[dict]:
    findings: list[dict] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return findings
    lines = text.splitlines()

    # File-level exempt: if the module-level docstring (first
    # triple-quoted block) or the top-of-file comment region
    # explicitly acknowledges the CAL-4 status / post-hoc nature /
    # mobius-limit framing, no need to flag any Hunt-A match in
    # this file.
    file_header = "\n".join(lines[:80])  # first 80 lines covers
                                          # docstrings + imports
    file_acknowledges_cal4 = bool(EXEMPT_PATTERN.search(file_header))

    # Hunt A: Möbius pencil
    if not file_acknowledges_cal4:
        for m in MOBIUS_RE.finditer(text):
            # Find line number + 3-line window
            start = m.start()
            line_no = text[:start].count("\n") + 1
            window = "\n".join(lines[max(0, line_no - 3):line_no + 2])
            if EXEMPT_PATTERN.search(window):
                continue
            # Skip if the surrounding context is a comment / docstring
            line_text = lines[line_no - 1] if 0 <= line_no - 1 < len(lines) else ""
            stripped = line_text.strip()
            if stripped.startswith("#") or stripped.startswith('"""') or stripped.startswith("'''"):
                continue
            findings.append({
                "pattern": "A-mobius-pencil",
                "file": str(path.relative_to(ROOT.parent)),
                "line": line_no,
                "match": m.group(0),
                "context": stripped[:200],
            })

    # Hunt B: PSLQ + substrate-claim + CODATA-target trifecta
    pslq_hits = list(PSLQ_USE_RE.finditer(text))
    if pslq_hits:
        substrate_hit = SUBSTRATE_CLAIM_RE.search(text)
        codata_hit = CODATA_TARGET_RE.search(text)
        # Skip exempt
        if substrate_hit and codata_hit and not EXEMPT_PATTERN.search(
            text[:max(2000, codata_hit.start() + 200)]
        ):
            findings.append({
                "pattern": "B-pslq-substrate-claim-with-codata-target",
                "file": str(path.relative_to(ROOT.parent)),
                "line": pslq_hits[0].start(),
                "substrate_claim_at": substrate_hit.start(),
                "codata_target_at": codata_hit.start(),
                "n_pslq_calls": len(pslq_hits),
            })

    # Hunt C: high-precision literal not in acknowledged slot
    if "codata_constants.py" in str(path):
        return findings  # canonical CODATA slot — exempt
    # File-level exemption: if the script already imports from
    # codata_constants, a local literal definition is a re-instantiation
    # / duplication issue, not a new CAL-4 disguise. Flag separately
    # via the `integration-audit` skill; not in scope here.
    if re.search(r"from codata_constants|import codata_constants", text):
        return findings
    for m in LITERAL_RE.finditer(text):
        name = m.group(1)
        # Skip already-named patterns
        if ALREADY_NAMED_RE.search(name):
            continue
        line_no = text[:m.start()].count("\n") + 1
        window_start = max(0, line_no - 4)
        window = "\n".join(lines[window_start:line_no + 2])
        if EXEMPT_PATTERN.search(window):
            continue
        findings.append({
            "pattern": "C-unnamed-high-precision-literal",
            "file": str(path.relative_to(ROOT.parent)),
            "line": line_no,
            "name": name,
            "value": m.group(2),
        })
    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 if any findings")
    args = parser.parse_args()

    targets: list[Path] = []
    for p in HERE.rglob("*.py"):
        sp = str(p)
        if "_deprecated/" in sp or "/script-qa/" in sp or "/__pycache__/" in sp:
            continue
        if p.name == HERE.joinpath("cal4_disguise_hunt.py").name:
            continue
        targets.append(p)

    all_findings: list[dict] = []
    for p in targets:
        all_findings.extend(hunt_file(p))

    # Tally by pattern
    by_pattern: dict[str, int] = {}
    for f in all_findings:
        by_pattern[f["pattern"]] = by_pattern.get(f["pattern"], 0) + 1

    print(f"CAL-4 disguise hunt:")
    print(f"  scanned:  {len(targets)} scripts")
    print(f"  flagged:  {len(all_findings)} findings")
    for pat, n in sorted(by_pattern.items()):
        print(f"     {pat}: {n}")
    print()
    if all_findings[:20]:
        print(f"First {min(20, len(all_findings))} findings:")
        for f in all_findings[:20]:
            print(f"  [{f['pattern']}] {f['file']}:{f.get('line', '?')}")
            if "match" in f:
                print(f"       {f.get('context', '')[:120]}")
            elif "name" in f:
                print(f"       {f['name']} = {f.get('value', '')[:30]}...")

    w = WitnessBuilder("cal4-disguise-hunt", engine="python")
    w.set_description(
        "Hunt for CAL-4 disguises beyond the literal pattern caught by "
        "fitted_labelled_canonical_audit. Three heuristics: (A) Möbius "
        "rational q-pencils, (B) PSLQ + substrate-claim + CODATA-target "
        "trifecta, (C) high-precision literals not in acknowledged "
        "CODATA/FITTED/VALIDATION slots. Exempts `# CAL-1/2/3/4`, "
        "`# FITTED_FROM_CODATA`, `# acknowledged`, `# noqa: P31/P32`, "
        "`_deprecated/`, and `codata_constants.py`."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_data("scripts_scanned", len(targets))
    w.add_data("total_findings", len(all_findings))
    w.add_data("findings_by_pattern", by_pattern)
    w.add_data("findings", all_findings)
    w.add_assertion(
        "no_unacknowledged_cal4_disguises_found",
        computed=float(len(all_findings) == 0),
        expected=1.0,
    )
    out = w.save()
    print(f"\nWitness: {out.name}")
    if args.strict and all_findings:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
