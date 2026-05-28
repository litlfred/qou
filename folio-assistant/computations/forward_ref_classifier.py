#!/usr/bin/env python3
"""Forward-reference classifier with documented waiver taxonomy.

Every cross-chapter forward reference (a block in chapter N whose
`uses[]` / `interprets` points at a block in chapter M > N) is
classified into one of six categories. Categories C–F are WAIVED —
they are permitted by the paper's structural design and excluded
from the "actionable" forward-ref count. Categories A and B are
ACTIONABLE — they represent genuine misplacements that block-moves
or chapter reordering could resolve.

Waiver taxonomy
---------------
  A. proof-dep         provable block uses[] a provable block later.
                       ACTIONABLE unless the target is a foundational
                       object intentionally developed late (see the
                       FOUNDATIONAL_LATE allowlist).
  B. definition-consumer  block uses[] a `def:` that lives later.
                       ACTIONABLE — the def could often move earlier.
  C. remark-interprets  a `remark` interprets a proposition proved
                       later. WAIVED — the interpretation is placed
                       where it reads naturally; the proof belongs in
                       its formal chapter. Moving the remark would
                       divorce it from its narrative context.
  D. framing-preview    an intro / overview / framing-chapter block
                       previews later content. WAIVED — framing
                       chapters (models-of-qous, notation) and section
                       intros exist precisely to preview.
  E. observational      the observations / molecular / organic chapters
                       cite predictions or dynamics proved upstream of
                       them in narrative but downstream in the manifest
                       (cross-Part story arc). WAIVED.
  F. appendix-surreal   target is an appendix, the surreal lift, or the
                       models-of-qous gallery. WAIVED — appendices and
                       the surreal lift are deliberately terminal.

Run: python3 forward_ref_classifier.py [--json] [--actionable-only]
"""

import json
import os
import re
import sys

BASE = os.path.join(os.path.dirname(__file__), "..", "..",
                    "content", "quantum-observable-universe")
BASE = os.path.normpath(BASE)

# Foundational objects intentionally developed in a late chapter but
# referenced early. A proof-dep edge whose TARGET is on this list is
# reclassified from ACTIONABLE-A to WAIVED-A (documented exception).
FOUNDATIONAL_LATE = {
    "def:habiro-ring",        # Habiro ring — used in Ch 2 q-exponential,
                              # formally developed in the mass machinery.
    "def:z-habiro-ring",
    "def:qz-bicompletion",
    "def:motivic-substrate",
    "def:archimedean-realization-functor",
}

# Chapters whose forward refs are waived wholesale.
FRAMING_CHAPTERS = {"models-of-qous", "notation"}
OBSERVATIONAL_CHAPTERS = {"observations", "molecular-construction",
                          "organic-chemistry"}
APPENDIX_PREFIXES = ("appendix-",)
SURREAL_CHAPTERS = {"appendix-surreals"}

PROVABLE = {"theorem", "lemma", "proposition", "corollary",
            "definition", "proof"}

WAIVED_CATEGORIES = {"C", "D", "E", "F"}


def load_chapter_order():
    manifest = os.path.join(BASE, "quantum-observable-universe.ts")
    with open(manifest) as f:
        dirs = re.findall(r'dir:\s*"([^"]+)"', f.read())
    return {d: i for i, d in enumerate(dirs)}, dirs


def load_label_info(chapters):
    info = {}
    for ch in chapters:
        ch_dir = os.path.join(BASE, ch)
        if not os.path.isdir(ch_dir):
            continue
        for fn in os.listdir(ch_dir):
            if not fn.endswith(".ts") or fn == f"{ch}.ts":
                continue
            try:
                with open(os.path.join(ch_dir, fn)) as f:
                    text = f.read()
                lm = re.search(r'label:\s*"([^"]+)"', text)
                km = re.search(r"export default (\w+)\(", text)
                if lm:
                    info[lm.group(1)] = (ch, km.group(1) if km else "?")
            except OSError:
                pass
    return info


def classify(src_ch, src_kind, tgt_ch, tgt_kind, tgt_label):
    """Return (category_letter, waived_bool, reason)."""
    if (tgt_ch.startswith(APPENDIX_PREFIXES) or tgt_ch in SURREAL_CHAPTERS
            or tgt_ch in FRAMING_CHAPTERS or src_ch in FRAMING_CHAPTERS):
        return "F", True, "appendix / surreal / framing-gallery target"
    if tgt_label in FOUNDATIONAL_LATE:
        return "A", True, ("foundational object intentionally developed "
                           "late (FOUNDATIONAL_LATE allowlist)")
    if src_kind == "remark" and tgt_kind in PROVABLE:
        return "C", True, ("remark interprets a later-proved result; "
                           "interpretation placed in its natural chapter")
    if src_ch in OBSERVATIONAL_CHAPTERS:
        return "E", True, ("observational / physical-realization chapter "
                           "citing upstream theory (cross-Part story arc)")
    if src_kind in ("prose",) or "intro" in (tgt_label or ""):
        return "D", True, "framing / preview (intro or overview block)"
    if src_kind in PROVABLE and tgt_kind in PROVABLE:
        return "A", False, "proof-dependency: provable block uses later provable block"
    if tgt_kind == "definition":
        return "B", False, "definition-consumer: uses a later-defined object"
    return "D", True, "narrative preview"


def main():
    as_json = "--json" in sys.argv
    actionable_only = "--actionable-only" in sys.argv

    ch_order, chapters = load_chapter_order()
    info = load_label_info(chapters)

    rows = []
    for ch in chapters:
        ch_dir = os.path.join(BASE, ch)
        src_idx = ch_order.get(ch, 999)
        if not os.path.isdir(ch_dir):
            continue
        for fn in os.listdir(ch_dir):
            if not fn.endswith(".ts") or fn == f"{ch}.ts":
                continue
            try:
                with open(os.path.join(ch_dir, fn)) as f:
                    text = f.read()
            except OSError:
                continue
            lm = re.search(r'label:\s*"([^"]+)"', text)
            if not lm:
                continue
            src_label = lm.group(1)
            km = re.search(r"export default (\w+)\(", text)
            src_kind = km.group(1) if km else "?"
            uses = re.findall(
                r'"((?:def|prop|thm|lem|cor|conj|rem|ex|prf|sim|tbl):[\w-]+)"',
                text)
            for u in set(uses):
                if u not in info:
                    continue
                tgt_ch, tgt_kind = info[u]
                if ch_order.get(tgt_ch, 0) <= src_idx:
                    continue
                cat, waived, reason = classify(
                    ch, src_kind, tgt_ch, tgt_kind, u)
                rows.append({
                    "src_chapter": ch, "src_label": src_label,
                    "src_kind": src_kind, "tgt_chapter": tgt_ch,
                    "tgt_label": u, "tgt_kind": tgt_kind,
                    "category": cat, "waived": waived, "reason": reason,
                })

    total = len(rows)
    waived = sum(1 for r in rows if r["waived"])
    actionable = total - waived

    if as_json:
        print(json.dumps({
            "total": total, "waived": waived, "actionable": actionable,
            "rows": [r for r in rows
                     if not actionable_only or not r["waived"]],
        }, indent=2))
        return

    by_cat = {}
    for r in rows:
        key = (r["category"], r["waived"])
        by_cat.setdefault(key, 0)
        by_cat[key] += 1

    print(f"Forward references: {total} total")
    print(f"  WAIVED:     {waived}")
    print(f"  ACTIONABLE: {actionable}\n")
    print("By category:")
    cat_names = {
        "A": "proof-dep (provable→provable)",
        "B": "definition-consumer",
        "C": "remark-interprets-later",
        "D": "framing/preview",
        "E": "observational consumer",
        "F": "appendix/surreal/framing target",
    }
    for (cat, w), n in sorted(by_cat.items()):
        tag = "WAIVED   " if w else "ACTIONABLE"
        print(f"  {cat} [{tag}] {n:3d}  {cat_names.get(cat, '?')}")


if __name__ == "__main__":
    main()
