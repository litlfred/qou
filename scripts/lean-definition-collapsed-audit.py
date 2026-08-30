#!/usr/bin/env python3
"""Detect *definition-collapsed* theorems: statements made true by a local
definition rather than by an argument.

Motivation (bean `qou-sk6h`).  Three `QOU/LiftingDescent/tm_*.lean` files
carried six theorems documented as "**Open input** ... body is `sorry`" that
contained no `sorry` and asserted nothing: the objects they quantified over
had been *defined* so the statement collapsed.

    def descendedBlowupCount : ℕ := 0     -- ⇒ ∏ over Finset.range 0 is empty
    def descendedMIdisc (i : ℕ) : ℝ := 1  -- ⇒ "contribution is trivial" is rfl
    def MI i := ∫ ...                      -- ⇒ "MI equals that integral" is rfl

This shape is invisible to every existing checker.  A vacuous proof has no
`sorry`, no `axiom`, and no `native_decide`, so `#print axioms` reads clean:

    before  [propext, Classical.choice, Quot.sound]            <- looks proved
    after   [propext, sorryAx, Classical.choice, Quot.sound]   <- honestly open

Two independent signals are computed per theorem:

  A. COLLAPSED   the proof is `rfl` / `by rfl` / `by intro..; rfl`, or
                 `by simp [xs]` / `by unfold xs` where some `x` is a plain
                 `def` declared in the SAME file (not `opaque`, not `axiom`).
  B. OPEN-CLAIM  the docstring claims the statement is unproved or hard:
                 "open input", "open analytic", "body is `sorry`",
                 "not in Mathlib", "needs ...", "conjecture".

`A and B` is the laundering shape: the prose says open, the proof says
definitional.  That combination is reported as CRITICAL and is near-certain.
`A` alone is ADVISORY — plenty of definitional restatements are legitimate and
say so (e.g. `phi_q_integral_representation`, whose docstring states it is
definitional).  As with the other vacuity criteria this is a high-recall
candidate generator: the genuine/legit verdict is an agent call.

Usage:
    python3 scripts/lean-definition-collapsed-audit.py [root ...]
    python3 scripts/lean-definition-collapsed-audit.py --json out.json
Exit: 0 always (advisory); use --strict to exit 1 when any CRITICAL is found.
"""
from __future__ import annotations
import os, re, sys, json

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from lean_decl_scan import (            # noqa: E402  (path set above)
    blank_comments, split_statement, decl_spans, docstring_before,
    assumption_binders, local_def_names, discharges_via_binder_field,
)

DEFAULT_ROOTS = [
    "content/quantum-observable-universe/lean/QOU",
    "content/unital-groebner-bases/lean",
    "content/fred2005-formal-groups/lean",
]

# PLAIN_DEF / THM now come from scripts/lib/lean_decl_scan (bean qou-rfq9).
PROVABLE = {"theorem", "lemma", "example"}
DOC_OPEN = re.compile(
    r"open input|open analytic|body is\s*`?sorry|not in mathlib|"
    r"needs the|needs yekutieli|is the conjecture|open conjecture|"
    r"unproved|not yet proved", re.I)
SIMP_ARGS = re.compile(r"\b(?:simp|simp only|unfold|rw|delta)\s*\[?([^\]\n]*)\]?")
TRIVIAL_TAIL = re.compile(r"^\s*(?::=\s*rfl|:=\s*by\s+rfl|:=\s*by\s*$)")


def parse_file(path: str):
    """Findings for one file.  Scanning primitives are shared with the
    borrowed-name detector via `scripts/lib/lean_decl_scan` (bean `qou-rfq9`);
    signals A and B below are this detector's own."""
    raw = open(path, encoding="utf-8", errors="replace").read()
    # Comments are blanked BEFORE parsing -- this detector previously scanned
    # raw lines, so a `rfl` or a def name inside a `--` comment was read as
    # code.  Line numbers survive blanking, so docstring lookup still indexes
    # into `lines` below.
    src = blank_comments(raw)
    lines = raw.split("\n")

    local_defs = local_def_names(src)

    findings = []
    for kind, name, line_no, chunk in decl_spans(src):
        if kind not in PROVABLE:
            continue
        stmt, after = split_statement(chunk)
        docstring = docstring_before(lines, line_no)

        # --- signal A: COLLAPSED -----------------------------------------
        collapsed, why = False, ""
        stripped = after.strip()
        if stripped in ("rfl", "by rfl"):
            collapsed, why = True, "proof is `rfl`"
        elif re.fullmatch(r"(?s)by\s+intro[^\n]*\s*rfl\s*", stripped):
            collapsed, why = True, "proof is `intro; rfl`"
        else:
            used = set()
            for sm in SIMP_ARGS.finditer(after):
                for tok in re.split(r"[,\s]+", sm.group(1)):
                    tok = tok.strip().split(".")[-1]
                    if tok:
                        used.add(tok)
            hits = sorted(used & local_defs)
            if hits and len(stripped.split("\n")) <= 3:
                collapsed = True
                why = "proof is `simp`/`unfold` over local def(s): " + ", ".join(hits[:4])

        if not collapsed:
            continue

        # --- exclusion: genuine conditional derivation --------------------
        # The goal is discharged from a STATED assumption (a field of an
        # instance/structure binder), not by unfolding a local definition.
        if discharges_via_binder_field(after, assumption_binders(stmt)):
            continue

        # --- signal B: OPEN-CLAIM -----------------------------------------
        open_claim = bool(DOC_OPEN.search(docstring))
        findings.append({
            "file": path, "line": line_no, "kind": kind, "name": name,
            "severity": "CRITICAL" if open_claim else "ADVISORY",
            "why": why,
            "doc_claims_open": open_claim,
            "doc_excerpt": " ".join(docstring.split())[:160],
        })
    return findings


def main() -> int:
    args = [a for a in sys.argv[1:]]
    strict = "--strict" in args
    if strict:
        args.remove("--strict")
    out_json = None
    if "--json" in args:
        idx = args.index("--json")
        out_json = args[idx + 1]
        del args[idx:idx + 2]
    roots = args or DEFAULT_ROOTS

    findings = []
    for root in roots:
        for dp, _, fns in os.walk(root):
            if "/.lake/" in dp:
                continue
            for fn in fns:
                if fn.endswith(".lean"):
                    findings.extend(parse_file(os.path.join(dp, fn)))

    crit = [f for f in findings if f["severity"] == "CRITICAL"]
    adv = [f for f in findings if f["severity"] == "ADVISORY"]
    print(f"definition-collapsed audit: {len(crit)} CRITICAL, {len(adv)} advisory\n")
    for f in crit:
        print(f"CRITICAL {f['file']}:{f['line']}  {f['kind']} {f['name']}")
        print(f"         {f['why']}")
        print(f"         doc claims open: {f['doc_excerpt'][:120]}")
    if adv:
        print(f"\n-- advisory ({len(adv)}): definitional restatements; many are legitimate --")
        for f in adv[:40]:
            print(f"  {f['file']}:{f['line']}  {f['name']}  ({f['why']})")
        if len(adv) > 40:
            print(f"  ... and {len(adv) - 40} more")
    if out_json:
        json.dump(findings, open(out_json, "w"), indent=1)
        print(f"\nwrote {out_json}")
    return 1 if (strict and crit) else 0


if __name__ == "__main__":
    sys.exit(main())
