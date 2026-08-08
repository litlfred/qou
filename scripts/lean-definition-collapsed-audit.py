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

DEFAULT_ROOTS = [
    "content/quantum-observable-universe/lean/QOU",
    "content/unital-groebner-bases/lean",
    "content/fred2005-formal-groups/lean",
]

# `def foo`, but NOT `opaque foo` / `axiom foo` — those are honest primitives.
PLAIN_DEF = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(?:def|abbrev)\s+([A-Za-z_][A-Za-z0-9_'.]*)")
THM = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(theorem|lemma|example)\s+([A-Za-z_][A-Za-z0-9_'.]*)")
DOC_OPEN = re.compile(
    r"open input|open analytic|body is\s*`?sorry|not in mathlib|"
    r"needs the|needs yekutieli|is the conjecture|open conjecture|"
    r"unproved|not yet proved", re.I)
SIMP_ARGS = re.compile(r"\b(?:simp|simp only|unfold|rw|delta)\s*\[?([^\]\n]*)\]?")
TRIVIAL_TAIL = re.compile(r"^\s*(?::=\s*rfl|:=\s*by\s+rfl|:=\s*by\s*$)")


def parse_file(path: str):
    src = open(path, encoding="utf-8", errors="replace").read()
    lines = src.split("\n")

    local_defs: set[str] = set()
    for ln in lines:
        m = PLAIN_DEF.match(ln)
        if m:
            local_defs.add(m.group(1).split(".")[-1])

    findings = []
    i = 0
    while i < len(lines):
        m = THM.match(lines[i])
        if not m:
            i += 1
            continue
        kind, name = m.group(1), m.group(2)

        # docstring: contiguous /-- ... -/ immediately above (skip -- Ref: lines)
        doc, j = [], i - 1
        while j >= 0 and (lines[j].lstrip().startswith("--") or not lines[j].strip()):
            j -= 1
        if j >= 0 and lines[j].rstrip().endswith("-/"):
            k = j
            while k >= 0:
                doc.append(lines[k])
                if lines[k].lstrip().startswith("/--"):
                    break
                k -= 1
        docstring = "\n".join(reversed(doc))

        # body: from the theorem line to the next top-level declaration
        body, k = [], i
        while k < len(lines):
            if k > i and re.match(r"^\S", lines[k]) and not lines[k].startswith(")"):
                break
            body.append(lines[k])
            k += 1
        body_txt = "\n".join(body)
        after = body_txt.split(":=", 1)[1] if ":=" in body_txt else ""

        # --- signal A ---------------------------------------------------
        collapsed, why = False, ""
        stripped = after.strip()
        if stripped in ("rfl", "by rfl") or re.fullmatch(r"by\s+intro[^\n]*\n\s*rfl", stripped):
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
            # only if the proof is *just* that tactic (short body)
            if hits and len(stripped.split("\n")) <= 3:
                collapsed = True
                why = "proof is `simp`/`unfold` over local def(s): " + ", ".join(hits[:4])

        if not collapsed:
            i = k
            continue

        # --- exclusion: genuine conditional derivation --------------------
        # If the proof discharges the goal using a *hypothesis field* of an
        # instance/structure binder (`C.ruleLinear`, `h.foo`), it is deriving
        # from a stated assumption, not collapsing on a local definition.
        # Real example: BraneTowerLevelAmplitude.fullCoordAmplitude_eq, whose
        # docstring correctly disclaims ("not a proof of the rule; the rule
        # `ruleLinear` is the open input") — the disclaimer used to trip
        # signal B and report a false CRITICAL.
        binders = set(re.findall(r"[\[(]\s*([A-Za-z_][A-Za-z0-9_']*)\s*:", body_txt))
        if any(re.search(rf"\b{re.escape(b)}\.[A-Za-z_]", after) for b in binders):
            i = k
            continue

        # --- signal B ---------------------------------------------------
        open_claim = bool(DOC_OPEN.search(docstring))
        findings.append({
            "file": path, "line": i + 1, "kind": kind, "name": name,
            "severity": "CRITICAL" if open_claim else "ADVISORY",
            "why": why,
            "doc_claims_open": open_claim,
            "doc_excerpt": " ".join(docstring.split())[:160],
        })
        i = k
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
