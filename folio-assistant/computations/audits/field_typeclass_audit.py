#!/usr/bin/env python3
"""Field-typeclass over-strength audit.

Scans the QOU Lean library for declarations that constrain a type variable
with a *field-strength* typeclass — ``[Field V]``, ``[LinearOrderedField V]``,
``[DivisionRing V]`` — and classifies whether the declaration actually uses a
field-only operation (division ``/``, inverse ``⁻¹``/``Inv``), or whether a
weaker class (``CommRing``, ``Semiring``, …) would suffice.

This is the §7c "start generic, use the weakest typeclass that admits the
construction" discipline turned into a checker: an over-strong ``[Field V]``
that never divides is a code smell — it blocks the construction from being
reused over a commutative ring (e.g. the substrate ground ring ``R`` /
``LaurentPolynomial ℤ``).

Classification (per declaration that has a field-strength binder on ``V``):

* ``phantom``       — ``V`` never appears in the decl body/signature except in
                      the binder. The class is pure dead-weight; relax to the
                      weakest sensible class (``CommRing`` by default).
* ``over-strong``   — ``V`` is used, but no field-only operation on ``V`` was
                      found. ``CommRing V`` (or weaker) very likely suffices;
                      flagged for relaxation + a build check.
* ``genuine``       — a field-only operation on ``V`` was found (``/`` or
                      ``⁻¹`` / ``Inv`` / a field-only lemma). Keep the class.

Output: a witness JSON (``field-typeclass-audit.witness.json``) and a human
markdown summary on stdout. ``--strict`` makes the script exit non-zero when
any ``phantom`` or ``over-strong`` finding is present (CI gate).

Heuristic, line-based — intended as a *warn-level* audit signal, not a
typechecker. Comments / string literals are stripped before scanning for
operators so URLs (``http://``), file paths, and prose ``/`` do not produce
false "genuine" hits.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# --- configuration --------------------------------------------------------

LEAN_ROOT = Path("content/quantum-observable-universe/lean/QOU")
SKIP_DIR_PARTS = {".lake", "_Scratch"}

# field-strength classes we audit (var-capturing)
FIELD_CLASS_RE = re.compile(r"\[\s*(Field|LinearOrderedField|DivisionRing)\s+([A-Za-z_][A-Za-z0-9_']*)\s*\]")

# a top-level declaration opener (allow leading attrs/modifiers handled separately)
DECL_KW = (
    "theorem", "lemma", "def", "abbrev", "structure", "class", "instance",
    "example", "axiom",
)
DECL_OPEN_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?"
    r"(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|partial\s+|unsafe\s+)*"
    r"(" + "|".join(DECL_KW) + r")\b"
)


@dataclass
class Finding:
    file: str
    line: int
    decl_kw: str
    decl_name: str
    type_var: str
    field_class: str
    classification: str  # phantom | over-strong | genuine
    evidence: str        # what triggered the classification


def strip_comments_strings(text: str) -> str:
    """Remove block comments /- -/, line comments --, and "..." strings.

    Replaces removed spans with spaces (preserving line structure roughly) so
    operator scanning does not pick up prose / URLs / paths.
    """
    out = []
    i, n = 0, len(text)
    depth = 0  # block-comment nesting
    while i < n:
        two = text[i:i + 2]
        if depth > 0:
            if two == "/-":
                depth += 1; i += 2; continue
            if two == "-/":
                depth -= 1; i += 2; continue
            out.append(" " if text[i] != "\n" else "\n"); i += 1; continue
        if two == "/-":
            depth += 1; i += 2; continue
        if two == "--":
            # line comment to EOL
            j = text.find("\n", i)
            if j == -1:
                j = n
            out.append(" " * (j - i)); i = j; continue
        if text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                if text[j] == "\\":
                    j += 1
                j += 1
            out.append(" " * (min(j, n) - i + 1)); i = j + 1; continue
        out.append(text[i]); i += 1
    return "".join(out)


# field-only signals (on the stripped body). Comments / strings / URLs are
# stripped beforehand, so a surviving single `/` is a (H)Div — including
# digit-prefixed forms like `1/q` that a digit lookbehind would miss. The
# `(?<!/)/(?!/)` guard skips Lean subtype notation `{ x // p x }` (the `//`
# is not a comment delimiter, so it survives stripping) while still catching
# real single-slash division. (Gemini review #2072.)
DIV_RE = re.compile(r"(?<!/)/(?!/)")
INV_RE = re.compile(r"⁻¹")
FIELD_LEMMA_RE = re.compile(
    r"\b(Inv\.inv|inv_|_inv\b|div_|_div\b|mul_inv|inv_mul|field_simp|"
    r"Field\.|DivisionRing|IsField|GroupWithZero)\b"
)

# Constructs that, while not literal division, require field strength in
# practice (semisimplicity / dimension theory / Wedderburn / bases over a
# field). A decl invoking these over `V` almost always genuinely needs
# `[Field V]`; treat as genuine to avoid false "relax me" advice.
FIELD_REQUIRING_RE = re.compile(
    r"\b(finrank|FiniteDimensional|Module\.Free|Module\.rank|Basis\b|"
    r"Wedderburn|[sS]emisimple|IsSemisimple|Matrix\.rank|LinearIndependent|"
    r"iSupIndep|finrank_|_finrank|Subspace|Cardinal\.toNat|"
    # decls that consume the base QOU universe structs inherit their
    # `[Field k]` requirement — relaxing those is the QuantumUniverse
    # cascade (own PR), not a leaf fix, so treat as field-requiring here.
    r"QuantumObservableUniverse|QuantumUniverse)\b"
)


def split_decls(text: str):
    """Yield (start_line_idx, header_line, decl_block_text) per top-level decl.

    A decl block runs from its opener line up to (but not including) the next
    top-level opener or a column-0 ``end``/``namespace``/``section``/``open``/
    ``import``/``variable`` line.
    """
    lines = text.splitlines()
    starts = []
    for idx, ln in enumerate(lines):
        if DECL_OPEN_RE.match(ln):
            starts.append(idx)
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else len(lines)
        block = "\n".join(lines[s:e])
        yield s, lines[s], block


NAME_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?"
    r"(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|partial\s+|unsafe\s+)*"
    r"(" + "|".join(DECL_KW) + r")\s+([A-Za-z_][A-Za-z0-9_'.]*)"
)


def classify(block_stripped: str, var: str) -> tuple[str, str]:
    # does the var appear outside the binder at all?
    # remove the binder occurrences then look for the bare token
    body = re.sub(r"\[\s*(?:Field|LinearOrderedField|DivisionRing)\s+"
                  + re.escape(var) + r"\s*\]", " ", block_stripped)
    token = re.compile(r"(?<![A-Za-z0-9_'])" + re.escape(var) + r"(?![A-Za-z0-9_'])")
    used = bool(token.search(body))
    if not used:
        return "phantom", f"type var `{var}` unused outside the field binder"
    # field-only operations anywhere in the decl (heuristic — not var-scoped,
    # but a decl that divides at all almost always divides in `var`)
    if INV_RE.search(body):
        return "genuine", "uses `⁻¹` (inverse)"
    if FIELD_LEMMA_RE.search(body):
        m = FIELD_LEMMA_RE.search(body)
        return "genuine", f"uses field-only token `{m.group(0)}`"
    if FIELD_REQUIRING_RE.search(body):
        m = FIELD_REQUIRING_RE.search(body)
        return "genuine", f"uses field-requiring construct `{m.group(0)}` (dimension/semisimplicity)"
    if DIV_RE.search(body):
        return "genuine", "uses `/` (division)"
    return "over-strong", f"`{var}` used but no division/inverse found"


def audit() -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(LEAN_ROOT.rglob("*.lean")):
        if any(part in SKIP_DIR_PARTS for part in path.parts):
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        stripped = strip_comments_strings(raw)
        rel = str(path)
        for s_idx, header, block in split_decls(raw):
            block_stripped = strip_comments_strings(block)
            for m in FIELD_CLASS_RE.finditer(block_stripped):
                fclass, var = m.group(1), m.group(2)
                cls, ev = classify(block_stripped, var)
                # name may sit on a continuation line — match against the
                # first few joined lines of the block, not just the header.
                head_join = " ".join(block.splitlines()[:4])
                nm = NAME_RE.match(head_join)
                kw = nm.group(1) if nm else "?"
                name = nm.group(2) if nm else "?"
                findings.append(Finding(
                    file=rel, line=s_idx + 1, decl_kw=kw, decl_name=name,
                    type_var=var, field_class=fclass,
                    classification=cls, evidence=ev,
                ))
    return findings


EXCEPTIONS_PATH = Path("folio-assistant/computations/audits/field-typeclass-audit.exceptions.json")


def apply_exceptions(findings: list[Finding]) -> list[Finding]:
    """Reclassify findings listed in the exceptions file as genuine.

    An exception records a decl whose `[Field]` relaxation was *attempted and
    failed the build* — so the field strength is genuine-by-build even though
    no field-only token is syntactically visible. Format: a list of
    ``{"decl_name": ..., "file_suffix": ..., "reason": ...}``.
    """
    if not EXCEPTIONS_PATH.exists():
        return findings
    exceptions = json.loads(EXCEPTIONS_PATH.read_text())
    for f in findings:
        if f.classification != "over-strong":
            continue
        for ex in exceptions:
            if (f.decl_name == ex["decl_name"]
                    and f.file.endswith(ex["file_suffix"])):
                f.classification = "genuine"
                f.evidence = f"build-verified exception: {ex['reason']}"
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any phantom/over-strong finding present")
    ap.add_argument("--witness", default="folio-assistant/computations/audits/field-typeclass-audit.witness.json")
    args = ap.parse_args()

    findings = apply_exceptions(audit())
    by_cls: dict[str, list[Finding]] = {"phantom": [], "over-strong": [], "genuine": []}
    for f in findings:
        by_cls[f.classification].append(f)

    # markdown summary
    print("# Field-typeclass over-strength audit\n")
    print(f"Scanned `{LEAN_ROOT}` — {len(findings)} field-strength binder(s) across declarations.\n")
    print(f"- **phantom** (relax now): {len(by_cls['phantom'])}")
    print(f"- **over-strong** (CommRing likely suffices; verify): {len(by_cls['over-strong'])}")
    print(f"- **genuine** (keep Field): {len(by_cls['genuine'])}\n")
    for cls in ("phantom", "over-strong"):
        if not by_cls[cls]:
            continue
        print(f"## {cls}\n")
        for f in by_cls[cls]:
            print(f"- `{f.file}:{f.line}` `{f.decl_kw} {f.decl_name}` "
                  f"`[{f.field_class} {f.type_var}]` — {f.evidence}")
        print()

    witness = {
        "audit": "field-typeclass-over-strength",
        "scanned_root": str(LEAN_ROOT),
        "total": len(findings),
        "counts": {k: len(v) for k, v in by_cls.items()},
        "findings": [asdict(f) for f in findings],
    }
    Path(args.witness).parent.mkdir(parents=True, exist_ok=True)
    Path(args.witness).write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n",
                                  encoding="utf-8")
    print(f"witness → {args.witness}")

    if args.strict and (by_cls["phantom"] or by_cls["over-strong"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
