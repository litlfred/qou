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
    comment_cone,
)

DEFAULT_ROOTS = [
    "folio/quantum-observable-universe/lean/QOU",
    "folio/unital-groebner-bases/lean",
    "folio/fred2005-formal-groups/lean",
]

# PLAIN_DEF / THM now come from scripts/lib/lean_decl_scan (bean qou-rfq9).
PROVABLE = {"theorem", "lemma", "example"}
# Phrases in which an author admits, in their own prose, that the declaration
# below is NOT the proof of what it is named after.
#
# The second group was added 2026-08-30 (bean `qou-rfq9`) and is the half that
# actually matters.  The bean diagnosed the `b3_nf_wedderburn_uniqueness` miss
# as `--`-comment blindness; reading the whole comment cone was implemented and
# measured as a **no-op** -- 2255 -> 2255 findings, 2 -> 2 CRITICAL.  The reason
# that declaration was invisible is that it says "Full proof requires
# Wedderburn-Artin over R_q" and "The formal proof needs: Wedderburn for
# finite-dim algebras", and neither the old `needs the` nor `unproved` matches
# either phrasing.  Cone blindness was real but was never what was hiding it.
#
# These are deliberately narrow: they require the words `proof`/`proved`/
# `formalis(z)ed` near the admission, so ordinary mathematical prose about what
# a THEOREM requires as a hypothesis does not match.
DOC_OPEN = re.compile(
    r"open input|open analytic|body is\s*`?sorry|not in mathlib|"
    r"needs the|needs yekutieli|is the conjecture|open conjecture|"
    r"unproved|not yet proved|"
    # "(full|formal|complete|rigorous|real) proof requires/needs/would ..."
    r"(?:full|formal|complete|rigorous|actual|real)\s+proof\s+"
    r"(?:requires|needs|is|would|remains)|"
    # "proof sketch", "sketch of proof", "we do not prove", "not formalised"
    r"proof\s+sketch|sketch\s+of\s+(?:the\s+)?proof|"
    r"(?:we|this)\s+do(?:es)?\s+not\s+prove|"
    r"not\s+(?:formali[sz]ed|formally\s+prove)", re.I)
SIMP_ARGS = re.compile(r"\b(?:simp|simp only|unfold|rw|delta|dsimp)\s*\[?([^\]\n]*)\]?")
TRIVIAL_TAIL = re.compile(r"^\s*(?::=\s*rfl|:=\s*by\s+rfl|:=\s*by\s*$)")
SUB_ZERO_GOAL = re.compile(r":\s*([^:=\n]+?)\s*-\s*\(.*\)\s*=\s*0\s*$", re.S)


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
    has_import = bool(re.search(r"^\s*import\s+\S+", src, re.M))

    findings = []
    for kind, name, line_no, chunk in decl_spans(src):
        if kind not in PROVABLE:
            continue
        stmt, after = split_statement(chunk)
        docstring = docstring_before(lines, line_no)
        # Signal B reads the whole COMMENT CONE, not the docstring alone --
        # see the `cone_only` note below and `comment_cone`'s docstring.
        cone = comment_cone(lines, line_no, chunk.count("\n") + 1)

        # --- signal A: COLLAPSED -----------------------------------------
        collapsed, why = False, ""
        stripped = after.strip()
        sub_zero_laundered = False
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
            elif hits and SUB_ZERO_GOAL.search(stmt.strip()) and re.search(r"\b(?:omega|ring|linarith|rfl)\b\s*$", stripped):
                collapsed = True
                sub_zero_laundered = True
                why = "subtraction-zero tautology `f x - (<body of f x>) = 0` over local def(s): " + ", ".join(hits[:4])

        if not collapsed:
            continue

        # --- exclusion: genuine conditional derivation --------------------
        # The goal is discharged from a STATED assumption (a field of an
        # instance/structure binder), not by unfolding a local definition.
        if not sub_zero_laundered and discharges_via_binder_field(after, assumption_binders(stmt)):
            continue

        # --- signal B: OPEN-CLAIM -----------------------------------------
        # Read the docstring AND the `--` comments above and inside the decl.
        # Prose in `--` comments was invisible here until 2026-08-30; the
        # worked case is `b3_nf_wedderburn_uniqueness`, whose docstring ends
        # "PROVED CORRECT" while an inline comment in its own statement says
        # "Full proof requires Wedderburn-Artin over R_q".  Both halves are
        # authored prose about the same declaration and only one was read.
        doc_claim = bool(DOC_OPEN.search(docstring))
        open_claim = bool(DOC_OPEN.search(cone)) or sub_zero_laundered or (not has_import and bool(hits if 'hits' in locals() else False))
        excerpt = docstring if doc_claim else cone
        findings.append({
            "file": path, "line": line_no, "kind": kind, "name": name,
            "severity": "CRITICAL" if open_claim else "ADVISORY",
            "why": why,
            "doc_claims_open": open_claim,
            # True when ONLY the `--` comments carry the admission, i.e. this
            # finding is new as of the comment-cone change.  Kept as its own
            # field so the delta stays auditable rather than being folded into
            # a count someone has already quoted.
            "cone_only": open_claim and not doc_claim,
            "doc_excerpt": " ".join(excerpt.split())[:160],
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
