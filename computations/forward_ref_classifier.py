#!/usr/bin/env python3
"""Forward-reference classifier — logical-vs-storytelling severity axis.

The PRIMARY question for any cross-chapter forward reference (a block in
chapter N whose `uses[]` / `interprets` points at a block in chapter
M > N) is:

    Does the reader have to KNOW or RELY ON the target's content to
    follow the argument made HERE?

If yes, it is a **logical / expository forward reference** — a genuine
defect: the exposition asks the reader to depend on something not yet
established. If no — the source merely motivates, narrates, interprets,
or points at the target — it is **storytelling**, which is benign and
expected in a connected scholarly work.

Severity (the axis that matters):

  - logical      BOTH source and target carry logical content (def /
                 prop / thm / lem / cor / proof / conjecture) AND the
                 source builds its argument on the target. THE DEFECT.
  - storytelling source is narrative (prose / remark / example /
                 simulator / equation / diagram / table) OR a logical
                 source merely cites a later data-table/diagram. Benign.
  - structural   target is an appendix or a framing chapter
                 (models-of-qous / notation). Benign by construction.

A logical forward reference is WAIVED (reclassified out of the
actionable defect count) in four cases:

  - target is the surreal-number lift (`appendix-surreals`) — a
    deliberate terminal construction the main text may rely on;
  - target is on the `FOUNDATIONAL_LATE` allowlist (objects used early
    but formally developed late, each justified inline);
  - **L-result-callback** (triage Table B): the target is a proven
    *result* (prop / lemma / cor / thm / proof) or a conjecture, not a
    definition — a result is established in its own chapter and an
    earlier citation is a deliberate forward callback, not a mis-home
    (there is no def to move);
  - **L-subject-matched** (triage Table A): the target is a definition
    whose subject matches its (later) home chapter, or whose placement
    is a considered prior decision — listed in `SUBJECT_MATCHED_DEFS`.

Everything else with a logical source AND a *definition* target whose
subject does NOT match its chapter remains an actionable
`L-dependency` defect — the small author-decision set the watcher
surfaces. See `docs/audits/2026-06-09-cross-chapter-forward-ref-triage.md`
for the per-edge triage that curated the two waive lists.

The legacy A–F category lettering is retained only in this taxonomy
prose for continuity; the emitted `category` field uses the
severity-prefixed labels `L-*` (logical), `T-*` (storytelling),
`S-*` (structural). The headline metric is the **logical-defect
count** (`L-dependency`).

Every cross-chapter forward reference (a block in chapter N whose
`uses[]` / `interprets` points at a block in chapter M > N) is
emitted with a `category` plus a boolean `waived` flag. WAIVED edges
— storytelling (`T-*`), structural (`S-*`), and the sanctioned
logical cases `L-foundational` / `L-result-callback` /
`L-subject-matched` — are permitted by the paper's structural design
and excluded from the "actionable" count. The only ACTIONABLE edges
are un-waived logical ones (`L-dependency`): genuine misplacements a
block-move or chapter reorder could resolve.

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

def _find_base():
    # `computations/` is one level below the repo root, so walk up from this
    # file until we find `content/quantum-observable-universe` rather than
    # hard-coding a `..` count (the previous two-`..` overshot the repo root,
    # e.g. to /home/user/ instead of /home/user/qou/, and the tool crashed).
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(8):
        cand = os.path.join(d, "content", "quantum-observable-universe")
        if os.path.isdir(cand):
            return cand
        d = os.path.dirname(d)
    return os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "content", "quantum-observable-universe"))


BASE = _find_base()

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
    "def:adelic-substrate",   # the ring of adeles 𝔸 — foundational substrate
                              # object, peer of motivic-substrate +
                              # archimedean-realization-functor above; used
                              # early (lifting-and-descent motivic-Galois
                              # character), formally developed in mass-theory
                              # (2026-06-09 author decision, edge #2).
}

# Definition targets that genuinely BELONG in their (later) home
# chapter: the def's SUBJECT matches the chapter, so an earlier block
# that forward-references it is a deliberate coupling, not a mis-home.
# Each entry is keyed "tgt_chapter::tgt_label". Curated from the
# 2026-06-09 cross-chapter forward-ref triage (Table A, subject-vs-
# chapter waive). A def→def or prop→def edge whose TARGET is on this
# list reclassifies from ACTIONABLE (L-dependency) to WAIVED
# (L-subject-matched). Do NOT add a label merely to lower the count —
# the test is "does the definition's subject match its home chapter?"
# (and, where relevant, "was its placement a considered prior
# decision?"). The author-decision edges still surfaced on main as
# actionable L-dependency (deliberately NOT added to any waive list)
# are skein→computational-horizon,
# embeddable-knot-operator→covalent-bond-types, and
# quark-antiquark→breit-wheeler — left for an author call.
SUBJECT_MATCHED_DEFS = {
    "brings-surface::def:su2-generators",          # PR #823 prior relocation
    "brings-surface::def:brings-surface",          # Bring's-surface def
    "brings-surface::def:briggs-klein-chart",      # Bring's-surface chart
    "brings-surface::def:local-cohomology-group",  # cohomological defect
    "climax-volume-mass::def:knot-operator-energy",   # q-hyperbolic energy
    "climax-volume-mass::def:local-shadow-ordering",  # shadow ordering
    "information-theory::def:operational-entropy",    # entropy
    "lifting-and-descent::def:yekutieli-lifting-condition",  # Yekutieli lift
    "mass-endomorphism::def:mass-identity",           # mass identity
    "measurement-observation::def:bundle-isotopy-equivalence",
    "particle-interactions::def:knot-particle-generation",
    # classical-limit functor 𝓛:𝐂_q→𝐂_1 — subject is the classical limit
    # (7 consumers across stochastic-mechanics + appendix-surreals); the
    # adelic-substrate forward reference is the archimedean-projection
    # pointer, not a mis-home (2026-06-09 author decision, edge #3).
    "stochastic-mechanics::def:classical-limit-functor",
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
    with open(manifest, encoding="utf-8") as f:
        dirs = re.findall(r"""dir:\s*["']([^"']+)["']""", f.read())
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


# Kinds that carry NO logical content — a forward ref FROM one of these
# is always storytelling (motivation, narration, preview), never a
# dependency the reader must resolve to follow an argument.
NARRATIVE_SRC = {"prose", "remark", "example", "simulator",
                 "equation", "diagram", "table"}

# Kinds that carry logical content. A logical forward ref needs a
# logical SOURCE (the block builds an argument) and a logical TARGET
# (the thing relied upon) — the same kind-set on both ends. Defined
# once and aliased so there is a single authoritative source, importable
# by sibling tooling (e.g. chapter-complexity-review's edge classifier).
LOGICAL_KINDS = {"definition", "proposition", "theorem", "lemma",
                 "corollary", "proof", "conjecture"}
LOGICAL_SRC = LOGICAL_KINDS
LOGICAL_TGT = LOGICAL_KINDS

# The ONE accepted reason a logical forward ref is permitted: the
# surreal-number appendix is a deliberate terminal lift that the main
# text may rely on by forward reference (author-sanctioned exception).
SURREAL_CHAPTERS = {"appendix-surreals"}


def classify(src_ch, src_kind, tgt_ch, tgt_kind, tgt_label):
    """Classify a forward reference.

    Returns (category, severity, waived, reason) where severity is one
    of "logical" (reader must rely on future content — the real defect),
    "storytelling" (motivation/preview/interpretation — benign), or
    "structural" (appendix/framing — benign by construction).

    The primary axis is logical-vs-storytelling. A forward ref is
    LOGICAL iff BOTH the source and target carry logical content
    (source builds an argument ON the target). Everything else is
    storytelling or structural and is waived.
    """
    # ── Structural waivers (benign by construction) ──────────────────
    if tgt_ch in SURREAL_CHAPTERS:
        return ("S-surreal", "structural", True,
                "target is the surreal-number lift — author-sanctioned "
                "terminal forward reference (the only accepted logical "
                "forward-ref exception)")
    if tgt_ch.startswith(APPENDIX_PREFIXES):
        return ("S-appendix", "structural", True,
                "target is an appendix — appendices are terminal; the "
                "main text may reference them forward")
    if src_ch in FRAMING_CHAPTERS or tgt_ch in FRAMING_CHAPTERS:
        return ("S-framing", "structural", True,
                "framing chapter (models-of-qous / notation) — exists to "
                "preview the arc; forward refs are its purpose")

    # ── Storytelling (no logical reliance) ───────────────────────────
    if src_kind in NARRATIVE_SRC:
        return ("T-narrative", "storytelling", True,
                f"source is a {src_kind} block — it motivates / narrates / "
                "interprets the target; the reader is not asked to rely on "
                "the target's content to follow an argument")

    # ── Logical forward references (the real defect) ─────────────────
    if src_kind in LOGICAL_SRC and tgt_kind in LOGICAL_TGT:
        if tgt_label in FOUNDATIONAL_LATE:
            return ("L-foundational", "logical", True,
                    "LOGICAL forward ref, but target is on the "
                    "FOUNDATIONAL_LATE allowlist (an object intentionally "
                    "used early, formally developed late — author-sanctioned)")
        # Rule 1 (2026-06-09 triage Table B): the target is a *proven
        # result* (prop / lemma / cor / thm / proof) or a conjecture, not
        # a definition. A result is established in its own chapter; an
        # earlier block citing it forward is a deliberate narrative
        # callback (consumption coupling), not a placement error — there
        # is no "move the def earlier" remedy because there is no def.
        if tgt_kind != "definition":
            established = ("stated in its own chapter"
                          if tgt_kind == "conjecture"
                          else "established where it lives")
            return ("L-result-callback", "logical", True,
                    f"LOGICAL forward ref to a later {tgt_kind} — a "
                    f"{tgt_kind} is {established}; the earlier citation is a "
                    "deliberate forward callback / consumption coupling, not "
                    "a misplacement (triage Table B)")
        # Rule 2 (2026-06-09 triage Table A): the target is a definition
        # whose subject matches its (later) home chapter — the def belongs
        # there, so the earlier forward reference is a deliberate coupling.
        if f"{tgt_ch}::{tgt_label}" in SUBJECT_MATCHED_DEFS:
            return ("L-subject-matched", "logical", True,
                    "LOGICAL forward ref to a later definition whose subject "
                    "matches its home chapter (or whose placement is a "
                    "considered prior decision) — the def belongs there; "
                    "the earlier reference is a deliberate coupling, not a "
                    "mis-home (triage Table A subject-vs-chapter waive)")
        return ("L-dependency", "logical", False,
                f"LOGICAL forward ref: a {src_kind} relies on a later "
                f"{tgt_kind} — the reader must know future content to "
                "follow the argument here. THIS IS THE DEFECT.")

    # ── Logical source, non-logical target (citing a later table etc.)
    if src_kind in LOGICAL_SRC:
        return ("T-cite", "storytelling", True,
                f"logical source cites a later {tgt_kind} (data table / "
                "diagram / example) — a pointer, not an argument dependency")

    return ("T-other", "storytelling", True, "non-logical forward reference")


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
                with open(os.path.join(ch_dir, fn), encoding="utf-8") as f:
                    text = f.read()
            except OSError:
                continue
            lm = re.search(r"""label:\s*["']([^"']+)["']""", text)
            if not lm:
                continue
            src_label = lm.group(1)
            km = re.search(r"export default\s+(\w+)\s*\(", text)
            src_kind = km.group(1) if km else "?"
            uses = re.findall(
                r"""["']((?:def|prop|thm|lem|cor|conj|rem|ex|prf|sim|tbl):[\w-]+)["']""",
                text)
            for u in set(uses):
                if u not in info:
                    continue
                tgt_ch, tgt_kind = info[u]
                if ch_order.get(tgt_ch, 0) <= src_idx:
                    continue
                cat, severity, waived, reason = classify(
                    ch, src_kind, tgt_ch, tgt_kind, u)
                rows.append({
                    "src_chapter": ch, "src_label": src_label,
                    "src_kind": src_kind, "tgt_chapter": tgt_ch,
                    "tgt_label": u, "tgt_kind": tgt_kind,
                    "category": cat, "severity": severity,
                    "waived": waived, "reason": reason,
                })

    total = len(rows)
    logical = [r for r in rows if r["severity"] == "logical" and not r["waived"]]
    storytelling = [r for r in rows if r["severity"] == "storytelling"]
    structural = [r for r in rows if r["severity"] == "structural"]
    logical_waived = [r for r in rows
                      if r["severity"] == "logical" and r["waived"]]

    if as_json:
        print(json.dumps({
            "total": total,
            "logical_defects": len(logical),
            "logical_waived": len(logical_waived),
            "storytelling": len(storytelling),
            "structural": len(structural),
            "rows": logical if actionable_only else rows,
        }, indent=2))
        return

    print(f"Forward references: {total} total\n")
    print("By severity (primary axis):")
    print(f"  LOGICAL DEFECT   {len(logical):3d}  "
          "(reader must rely on future content — FIX THESE)")
    print(f"  logical-waived   {len(logical_waived):3d}  "
          "(surreal lift / FOUNDATIONAL_LATE — sanctioned)")
    print(f"  storytelling     {len(storytelling):3d}  "
          "(motivation / interpretation / cite — benign)")
    print(f"  structural       {len(structural):3d}  "
          "(appendix / framing chapter — benign)")

    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["category"], 0)
        by_cat[r["category"]] += 1
    print("\nBy category:")
    for cat, n in sorted(by_cat.items()):
        print(f"  {cat:16s} {n:3d}")

    if logical:
        print(f"\n{'='*70}\nLOGICAL DEFECTS — {len(logical)} forward refs to fix:\n{'='*70}")
        for r in sorted(logical, key=lambda x: (x["src_chapter"], x["src_label"])):
            print(f"  {r['src_chapter']}/{r['src_label']} "
                  f"({r['src_kind']})\n     →  {r['tgt_chapter']}/{r['tgt_label']} "
                  f"({r['tgt_kind']})")


if __name__ == "__main__":
    main()
