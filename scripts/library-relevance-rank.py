#!/usr/bin/env python3
"""
library-relevance-rank — rank uncited library documents by how much they
talk about what *this* corpus talks about.

The first triage pass ranked by extracted formalizable content, which
measures how much formal material a document offers and says nothing about
whether we want it. A 236-candidate journal volume topped that list. This
ranks by topical overlap with the qou corpus instead.

## What "uncited" means, and why it changed

It used to mean "no `references.ts` entry names this copy". That backlog is
drained — every library document is registered — so the measure went to
zero and the ranking with it, which made the output an empty table under
prose describing a queue that no longer existed.

Registered is not cited. An entry can name a copy and be referenced by
nothing in the paper, and 278 of the 351 held sources are in exactly that
state. So "uncited" now means what it says: no content block cites the
entry, by `\cite{}` in a `.md`, by `cites: []` in a `.ts`, or by a Lean
`-- Ref: [key]`. That is the question `local/paper-relevance-triage`
exists to work.

## Where the vocabulary comes from

Not a hand-supplied topic list — those encode whatever the author happened
to think of that morning. The vocabulary is derived:

  * every content-block `title:` (~2,968) and `defines: [...]` entry
  * the notation register's symbol glosses

...then filtered to terms that are *discriminating* over the library
itself. A term matching 200 of 332 documents ("theorem", "group") carries
no signal; one matching five does. That is plain IDF, computed over the
library rather than over English, so the weighting is corpus-relative.

Scoring reads each document's `candidates.json` statements plus its title
and section titles — the substantive claims, not the prose — so a passing
mention in a bibliography does not inflate a score.

## What the number is and is not

It ranks *topical proximity*, which is a prior for relevance, not a
verdict. A high score means "this document is written in our vocabulary",
which is where triage should start, not where it should end. The
`local/paper-relevance-triage` skill and a human still decide.

Usage:
    scripts/library-relevance-rank.py                 # print ranking
    scripts/library-relevance-rank.py --write-triage  # regenerate the audit doc
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import glob
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
REFS = os.path.join(REPO, "content", "schema", "references.ts")
TRIAGE = os.path.join(REPO, "docs", "audits", "2026-08-15-library-uncited-triage.md")

# Words that are technical but say nothing about *which* technical area.
GENERIC = set("""
theorem lemma proposition corollary definition conjecture remark example proof
group space set map function element result case section chapter paper article
number value form type class order property structure system model method
following given first second third above below where when with from that this
these those which such have been will more than also into over under
""".split())

TOKEN = re.compile(r"[a-z][a-z0-9\-']{3,}")


def cited_docs() -> set[str]:
    """doc-ids whose references.ts entry is cited by some content block.

    Three citation paths, and all three count: `\\cite{}` in a `.md`,
    `cites: [...]` in a `.ts` manifest, and a Lean `-- Ref: [key]`. Reading
    only the first would call a document uncited when a proof cites it.
    """
    refs = open(REFS, encoding="utf-8").read()
    # entry id -> doc-id, taken from each entry's `library:` block. Read by
    # brace-matching from `ref({` rather than by a flat regex: `id` and
    # `docId` sit in different nested objects, and a file-wide scan pairs
    # them across entry boundaries.
    id_to_doc: dict[str, str] = {}
    for m in re.finditer(r"\bref\(\{", refs):
        i = refs.index("{", m.start())
        depth = 0
        blk = ""
        for j in range(i, len(refs)):
            if refs[j] == "{":
                depth += 1
            elif refs[j] == "}":
                depth -= 1
                if depth == 0:
                    blk = refs[i:j + 1]
                    break
        a = re.search(r'\bid:\s*"([^"]+)"', blk)
        b = re.search(r'docId:\s*"([^"]+)"', blk)
        if a and b:
            id_to_doc[a.group(1)] = b.group(1)

    keys: set[str] = set()
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.md"), recursive=True):
        t = open(path, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", t):
            keys.update(k.strip() for k in m.group(1).split(","))
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.ts"), recursive=True):
        t = open(path, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"cites:\s*\[([^\]]*)\]", t):
            keys.update(k.strip().strip("\"'") for k in m.group(1).split(","))
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.lean"), recursive=True):
        t = open(path, encoding="utf-8", errors="replace").read()
        keys.update(re.findall(r"--\s*Ref:\s*\[([^\]]+)\]", t))
    keys.discard("")
    return {doc for rid, doc in id_to_doc.items() if rid in keys}


def corpus_vocabulary() -> Counter:
    """Terms this corpus uses, with frequencies, from titles and defines[]."""
    vocab: Counter[str] = Counter()
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.ts"), recursive=True):
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        for t in re.findall(r'title:\s*"([^"]{4,120})"', text):
            vocab.update(TOKEN.findall(t.lower()))
        for d in re.findall(r"defines:\s*\[([^\]]*)\]", text):
            vocab.update(TOKEN.findall(d.lower()))
    # Notation register: only the gloss cells of its symbol tables. An
    # earlier version tokenised the whole file, which dragged its prose
    # ("sits", "unless", "earlier") into the vocabulary and let plain
    # English words outrank topical ones on library-IDF alone.
    for path in glob.glob(os.path.join(REPO, "content", "**", "notation*.md"), recursive=True):
        try:
            for line in open(path, encoding="utf-8", errors="replace"):
                if line.lstrip().startswith("|"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    for c in cells[1:]:
                        vocab.update(TOKEN.findall(c.lower()))
        except Exception:
            pass
    return Counter({w: n for w, n in vocab.items() if w not in GENERIC and n >= 2})


def doc_terms(docdir: str) -> tuple[set[str], dict]:
    """Substantive terms for one document + its facts."""
    facts: dict = {"doc": os.path.basename(docdir)}
    words: set[str] = set()

    sj = os.path.join(docdir, "structure.json")
    if os.path.exists(sj):
        try:
            art = json.load(open(sj))
        except Exception:
            art = {}
        md = art.get("metadata") or {}
        facts["title"] = (md.get("title") or "")[:110]
        facts["pages"] = art.get("source", {}).get("pages")
        words.update(TOKEN.findall((facts["title"] or "").lower()))
        secs = art.get("sections") or []
        facts["nsec"] = len(secs)
        for s in secs:
            words.update(TOKEN.findall((s.get("title") or "").lower()))
        # A bound volume repeats a paper's furniture: several distinct
        # "Introduction"/"References" sections rather than one of each.
        titles = [(s.get("title") or "").lower() for s in secs]
        facts["volume_signal"] = sum(
            1 for t in titles if re.match(r"^(introduction|references|bibliography)\b", t)
        )

    cj = os.path.join(docdir, "candidates.json")
    if os.path.exists(cj):
        try:
            c = json.load(open(cj))
        except Exception:
            c = {}
        s = c.get("summary", {})
        facts["cand"] = s.get("candidates", 0)
        facts["fml"] = s.get("formalization_candidates", 0)
        for x in c.get("candidates", [])[:400]:
            words.update(TOKEN.findall((x.get("statement") or "").lower()))
    return words, facts


def main() -> int:
    ap = argparse.ArgumentParser(description="Rank uncited library docs by corpus overlap")
    ap.add_argument("--write-triage", action="store_true")
    ap.add_argument("--top", type=int, default=40)
    args = ap.parse_args()

    vocab_c = corpus_vocabulary()
    vocab = set(vocab_c)
    cited = cited_docs()

    docs: list[tuple[set[str], dict]] = []
    for d in sorted(glob.glob(os.path.join(LIB, "*"))):
        if not (os.path.isdir(d) and os.path.exists(os.path.join(d, "structure.json"))):
            continue
        # A container (a bound issue that has been split) holds the same
        # pages as its children, and a duplicate is another copy of a work
        # already ranked; either way, ranking both counts one work twice
        # and inflates its apparent support.
        try:
            art = json.load(open(os.path.join(d, "structure.json")))
            if art.get("container") or art.get("duplicate_of"):
                continue
        except Exception:
            pass
        docs.append(doc_terms(d))

    # IDF over the library: a term in most documents discriminates nothing.
    N = len(docs)
    df: Counter[str] = Counter()
    for words, _ in docs:
        df.update(words & vocab)
    # Weight = how rare in the library x how central to this corpus. IDF
    # alone rewards any rare word; the corpus factor is what makes it
    # reward rare *and ours*.
    idf = {w: math.log(N / (1 + n)) * math.log(1 + vocab_c[w])
           for w, n in df.items() if n >= 1}

    ranked = []
    for words, facts in docs:
        if facts["doc"] in cited:
            continue
        hits = sorted(((idf.get(w, 0.0), w) for w in words & vocab), reverse=True)
        score = sum(s for s, _ in hits[:60])          # cap so length ≠ relevance
        facts["score"] = round(score, 1)
        facts["top_terms"] = [w for _, w in hits[:8]]
        ranked.append(facts)
    ranked.sort(key=lambda f: -f["score"])

    print(f"vocabulary: {len(vocab)} corpus terms, {len(idf)} discriminating in library")
    print(f"ranked {len(ranked)} uncited documents of {N}\n")
    print(f"{'#':>3} {'score':>6} {'vol':>3} {'fml':>4}  doc-id / title")
    for i, f in enumerate(ranked[: args.top], 1):
        vol = "!" if f.get("volume_signal", 0) >= 3 else ""
        print(f"{i:>3} {f['score']:>6} {vol:>3} {f.get('fml', 0):>4}  "
              f"{f['doc'][:30]:<30} {(f.get('title') or '')[:52]}")
        print(f"{'':>20}{', '.join(f['top_terms'][:6])}")

    if args.write_triage:
        vols = [f for f in ranked if f.get("volume_signal", 0) >= 3]
        out = [
            "# Uncited library documents — triage queue",
            "",
            "**Generated** by `scripts/library-relevance-rank.py --write-triage`.",
            "Regenerate rather than edit — the numbers below move whenever a source is",
            "cited or a document is added, and a stamped date here just goes stale (this",
            "line used to read \"Generated 2026-08-15\" long after it was not).",
            "",
            f"{len(ranked)} of {N} library documents are **held and registered but",
            "cited by nothing** — no content block references their `references.ts`",
            "entry, by `\\cite{}` in a `.md`, by `cites: []` in a `.ts`, or by a Lean",
            "`-- Ref: [key]`. That is the backlog",
            "[`local/paper-relevance-triage`](../../.claude/skills/local/paper-relevance-triage.md)",
            "exists to work.",
            "",
            "**This measures something different than it used to.** It counted documents",
            "with no `library:` back-reference from the bibliography — i.e. unregistered.",
            "That backlog is drained: every library document now has an entry, so the",
            "count went to zero and this page became an empty table under prose",
            "describing a queue that no longer existed. Registered is not cited, and the",
            "gap between them is the whole of this list.",
            "",
            "## How this is ranked",
            "",
            "By **topical overlap with the qou corpus**, not by volume of extracted",
            "material. An earlier pass ranked by formalizable-candidate count and put a",
            "whole journal issue first — that measures how much formal content a document",
            "*offers*, which is not the same question.",
            "",
            "The vocabulary is derived from this corpus, not hand-supplied: every content-block",
            f"`title:` and `defines:` entry plus the notation register, yielding {len(vocab)} terms,",
            f"of which {len(idf)} discriminate within the library. Weighting is library IDF times",
            "corpus frequency: a term must be both rare in the library and central here, so",
            "neither a ubiquitous word nor a rare-but-alien one scores. Scoring reads each",
            "document's extracted *claims*",
            "(`candidates.json`) plus its title and section titles — not its prose — so a",
            "passing mention in a bibliography does not inflate a score.",
            "",
            "**The score is a prior, not a verdict.** It says \"this document is written in our",
            "vocabulary\", which is where triage should start, not where it should end.",
            "",
            f"## Bound volumes ({len(vols)} flagged)",
            "",
            "Marked `!` below. A single paper has one Introduction and one References;",
            "these have three or more. Two different things produce that, and they want",
            "different handling:",
            "",
            "* **A bound journal issue** (`ant-v14-n7-s`, 19) really is several unrelated",
            "  papers in one file. Its score mixes them, so it is close to meaningless.",
            "  Split before triaging.",
            "* **A thesis** (`klein-…`, `malkin-…`) is one coherent work whose chapters each",
            "  carry their own furniture. The score is fine; only the section-count signal",
            "  is misleading. No split needed.",
            "",
            "The detector cannot tell them apart — it counts furniture, not authorship —",
            "so the flag means *check which of these it is*, not *split it*.",
            "",
            "**Classified 2026-08-15: every currently flagged document was checked and",
            "none needs splitting.** `scripts/split-bound-volume.py` was dry-run against",
            "all of them and refused each one for want of a repeating masthead, which is",
            "the mark of a published issue. Spot-checked the largest,",
            "`arxiv-math-0203194v1` (256pp, 6 flags): it is the André–Baldassarri",
            "Tôhoku-Hokkaido lecture volume — one coherent work whose chapters restart",
            "their numbering, exactly the thesis-shaped false positive. `ant-v14-n7-s`",
            "was the only genuine bound issue and is already split into its 10 papers.",
            "",
        ]
        if vols:
            out += ["| doc-id | Intro/Ref sections | pp | title |", "|---|---|---|---|"]
            out += [f"| [`{f['doc']}`](../../library/{f['doc']}/) | {f['volume_signal']} | "
                    f"{f.get('pages')} | {(f.get('title') or '')[:70]} |" for f in vols[:15]]
            out.append("")
        out += [
            "## Ranking",
            "",
            "| # | score | doc-id | fml | pp | title | strongest shared terms |",
            "|---|---|---|---|---|---|---|",
        ]
        for i, f in enumerate(ranked[:80], 1):
            mark = " `!`" if f.get("volume_signal", 0) >= 3 else ""
            out.append(
                f"| {i} | {f['score']} | [`{f['doc']}`](../../library/{f['doc']}/){mark} | "
                f"{f.get('fml', 0)} | {f.get('pages')} | {(f.get('title') or '_(none extracted)_')[:70]} | "
                f"{', '.join(f['top_terms'][:5])} |"
            )
        out += ["", f"_Showing 80 of {len(ranked)}. Full data: `library/*/candidates.json`._", ""]
        os.makedirs(os.path.dirname(TRIAGE), exist_ok=True)
        open(TRIAGE, "w", encoding="utf-8").write("\n".join(out))
        print(f"\nwrote {TRIAGE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
