#!/usr/bin/env python3
"""Validate kernel-constraints-registry.json + lint doc citations of conditional lemmas.

The kernel/f-map structural-constraint registry
(ck-dk-canonical-registry.md SS9 + its JSON twin
kernel-constraints-registry.json) is the single source of truth for the
epistemic tier of every structural constraint on the open Q_beta kernel
R(q,xi) / element F(q) / kernel coefficients a_j. Added 2026-07-07 after the
a_1 parity-shadow incident (docs/audits/
2026-07-07-a1-bar-odd-parity-shadow-investigation.md), in which a
CONDITIONAL lemma's hypothesis was propagated as established fact by prose
shorthand and the resulting contradiction (exactly-odd + nonzero q=1 shadow)
sat unnoticed for a month.

Rules:
  R1  every row has a unique id, a statement, a valid tier, and a source.
  R2  tier == "conditional" requires a non-empty `hypothesis`.
  R3  parity/shadow fixed-point rule: parity == "odd" (exact) requires
      q1_shadow in {"0", "vanishes", None}; the string "exactly-odd" is
      forbidden as a parity value alongside a nonzero shadow. This is the
      machine form of QOU.QBeta.fixed_eval_two_mul_kills_bar_odd: a
      bar-compatible evaluation annihilates exactly-bar-odd elements.
  R4  tier == "proved-lean" requires a `lean` decl name.
  R5  (warning) a conditional row's lean decl should carry the hypothesis in
      its name (Mathlib `_of_` style) per local/formalizer.md
      SSConditional-lemma naming.

Doc-lint mode (--lint-docs):
  For every conditional row with a lean decl, grep docs/**/*.md for bare
  citations of the decl's last name component; a citation is CLEAN if the
  decl name itself contains "_of_" (the hypothesis travels with the name) or
  the surrounding +-3 lines contain "conditional" (case-insensitive).
  Violations are WARNINGS by default; --strict promotes all warnings to
  errors (exit 1). Historical docs predating a rename are naturally exempt
  (they cite the old name, which no longer matches).

Usage:
  python3 docs/coordination/kernel_constraints_registry_validate.py [--lint-docs] [--strict]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
REGISTRY = HERE / "kernel-constraints-registry.json"

ZERO_SHADOWS = {None, "0", "vanishes"}


def validate(d: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    tiers = set(d["meta"]["tiers"].keys())
    seen: set[str] = set()

    for row in d.get("constraints", []):
        rid = row.get("id") or "<missing-id>"
        # R1
        if rid in seen:
            errors.append(f"R1: duplicate id {rid}")
        seen.add(rid)
        if not row.get("statement"):
            errors.append(f"R1: {rid} missing statement")
        tier = row.get("tier")
        if tier not in tiers:
            errors.append(f"R1: {rid} invalid tier {tier!r} (allowed: {sorted(tiers)})")
        if not row.get("source"):
            errors.append(f"R1: {rid} missing source")
        # R2
        if tier == "conditional" and not row.get("hypothesis"):
            errors.append(f"R2: {rid} is conditional but names no hypothesis")
        # R3
        parity = row.get("parity")
        shadow = row.get("q1_shadow")
        if parity == "exactly-odd":
            errors.append(f"R3: {rid} uses forbidden parity value 'exactly-odd' — "
                          "encode as parity='odd' with q1_shadow='0'")
        if parity == "odd" and shadow not in ZERO_SHADOWS:
            errors.append(f"R3: {rid} claims exact bar-oddness (parity='odd') with "
                          f"nonzero q=1 shadow {shadow!r} — jointly impossible "
                          "(fixed_eval_two_mul_kills_bar_odd)")
        # R4
        if tier == "proved-lean" and not row.get("lean"):
            errors.append(f"R4: {rid} is proved-lean but names no Lean decl")
        # R5
        if tier == "conditional" and row.get("lean"):
            for decl in re.split(r"[;,]\s*", row["lean"]):
                short = decl.strip().split(".")[-1]
                if short and "_of_" not in short:
                    warnings.append(f"R5: {rid} conditional decl `{short}` lacks an "
                                    "`_of_` name (hypothesis not visible in citations)")
    return errors, warnings


def lint_docs(d: dict) -> list[str]:
    findings: list[str] = []
    decls: list[str] = []
    for row in d.get("constraints", []):
        if row.get("tier") == "conditional" and row.get("lean"):
            for decl in re.split(r"[;,]\s*", row["lean"]):
                short = decl.strip().split(".")[-1]
                if short:
                    decls.append(short)
    docs_dir = REPO / "docs"
    for md in sorted(docs_dir.rglob("*.md")):
        try:
            lines = md.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines):
            for short in decls:
                if short in line:
                    if "_of_" in short:
                        continue  # hypothesis travels with the name
                    ctx = " ".join(lines[max(0, i - 3):i + 4]).lower()
                    if "conditional" not in ctx:
                        findings.append(
                            f"lint: {md.relative_to(REPO)}:{i + 1} cites conditional "
                            f"decl `{short}` without 'conditional' nearby")
    return findings


def main() -> int:
    strict = "--strict" in sys.argv
    do_lint = "--lint-docs" in sys.argv
    d = json.loads(REGISTRY.read_text(encoding="utf-8"))

    errors, warnings = validate(d)
    if do_lint:
        warnings += lint_docs(d)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    n = len(d.get("constraints", []))
    ok = not errors and not (strict and warnings)
    print(f"kernel-constraints-registry: {n} rows, "
          f"{len(errors)} error(s), {len(warnings)} warning(s) -> "
          f"{'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
