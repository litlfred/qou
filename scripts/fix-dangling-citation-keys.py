#!/usr/bin/env python3
"""
fix-dangling-citation-keys — repoint citation keys that resolve to nothing
onto the entry they were always meant to name.

`references.ts` is the bibliography; three things cite it, and only one is
checked. A `\\cite{}` in a `.md` is validated by the content pipeline, while
a `cites: [...]` in a `.ts` manifest and a Lean `-- Ref: [key]` are not — so
68 keys across those two paths resolve to no entry (bean qou-ghy5). AGENTS.md
§1 is explicit that a `-- Ref:` key "must match an entry in
content/schema/references.ts exactly", and a `sorry` carrying one that does
not reads as cited when it is not.

## This only ever applies a mapping a reader wrote down

A key that *looks* like an existing id is not evidence it means that entry.
Measured over this corpus, id similarity and same-work are close to
unrelated: `zagier2007` scores 0.78 against `zagier2010` and they are
different papers (the dilogarithm survey vs Quantum Modular Forms);
`bridgeland2007` scores 0.85 against `bridgeland2016` and means "Stability
conditions on triangulated categories", which is not in the bibliography at
all. Applying a similarity threshold would silently repoint a proof's
citation at the wrong paper, which is worse than leaving it dangling —
a dangling key is visibly broken, a wrong one is not.

So the mapping below is a hand-checked table, and every row records the
evidence that the two names denote one work. Two shapes qualify:

  * **punctuation only** — the two ids are identical once `-`/`_` are
    stripped, so there is no second candidate to confuse it with;
  * **the extra token is the target's own title** — `macdonald1995symmetric`
    against "Symmetric Functions and Hall Polynomials", `stanley1999ec2`
    against "Enumerative Combinatorics, Volume 2".

Anything needing a judgement about *which* of an author's papers is meant
stays out of this table and is resolved by reading the citing block.

## Scoped replacement, not a string swap

A key is replaced only inside a citation: `-- Ref: [key]` in Lean and a
quoted element of a `cites: [...]` array in a manifest. A blanket
find-and-replace would also rewrite the key where it appears in prose
discussing the reference, and in the `note:` text of the bibliography entry
itself.

Usage:
    scripts/fix-dangling-citation-keys.py            # dry run
    scripts/fix-dangling-citation-keys.py --apply
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# old key -> (new key, why these are one work)
MAPPING: dict[str, tuple[str, str]] = {
    # Punctuation only: identical ids once - and _ are stripped.
    "khovanov-lauda2009": ("khovanovlauda2009", "hyphenation only"),
    "chlouveraki2016hdr": ("chlouveraki2016-hdr", "hyphenation only"),
    "dimofte-garoufalidis2013": ("dimofte-garoufalidis-2013", "hyphenation only"),
    "ramis-sauloy-zhang-2013": ("ramis-sauloy-zhang2013", "hyphenation only"),
    "kontsevich-soibelman2008": ("kontsevich-soibelman-2008", "hyphenation only"),
    "habeggermasbaum2000": ("habegger-masbaum2000", "hyphenation only"),
    # The extra token is the target entry's own title.
    "macdonald1995symmetric": (
        "macdonald1995", 'target title is "Symmetric Functions and Hall Polynomials"'),
    "stanley1999ec2": (
        "stanley1999", 'target title is "Enumerative Combinatorics, Volume 2" (EC2)'),
    "milnor1982hyperbolic": (
        "milnor1982", 'target title is "Hyperbolic geometry: The first 150 years"'),
    "donagi-markman1996cubics": (
        "donagi-markman1994",
        'target title is "Cubics, Integrable Systems, and Calabi-Yau Threefolds"; '
        "the year differs because the key uses the journal year and the entry the "
        "arXiv one (alg-geom/9408004)"),
    # A block label with the wrong kind prefix. The block exists; it is a
    # conjecture, and both citing sites are conditional Prop classes that
    # axiomatise it — so the Lean is right and only the prefix is wrong.
    # Worth fixing beyond tidiness: citing a conjecture as a proposition is
    # the conjectural-propagation slip AGENTS.md §3b exists to catch, and it
    # would read to a reviewer as proved backing.
    "prop:jet-convergence-classical-limit": (
        "conj:jet-convergence-classical-limit",
        "same block, wrong kind prefix: it is declared "
        'label: "conj:jet-convergence-classical-limit" in '
        "mass-theory/jet-convergence-classical-limit.ts"),
    # Confirmed against the copy we hold, not against id similarity.
    "beliakova2011": (
        "beliakova-le2011",
        'library/arxiv-1106.6298v1 is "On the unification of quantum 3-manifold '
        'invariants" by Beliakova and Le, which is that entry'),
    "futer-gueritaud2011": (
        "futer-gueritaud-angled",
        'library/angled-survey is "From angled triangulations to hyperbolic '
        'structures" by Futer and Gueritaud, which is that entry'),
    # Matched on the IDENTIFIER the citing comment carries, not on the name.
    # This is the reliable key: `garoufalidis2020` scores 0.97 against three
    # different garoufalidis entries and is none of them — its comment names
    # arXiv 2012.00062, which is the Peacock Patterns paper.
    "garoufalidis2015stateintegrals": (
        "garoufalidis-kashaev2015",
        "the citing comment gives arXiv 1411.6062, which is that entry "
        "(Evaluation of State Integrals at Rational Points)"),
    "donagi1997swintegrable": (
        "donagi1997",
        "the citing comment gives arXiv alg-geom/9705010, which is that entry "
        "(Seiberg-Witten Integrable Systems)"),
    "faddeev-kashaev-volkov-2001": (
        "faddeev-kashaev-volkov2000",
        "the citing comment gives arXiv hep-th/0006156, which is that entry — "
        "confirmed by identifier rather than by the year being one off"),
    "garoufalidis2020": (
        "garoufalidis-gu-marino2023peacock",
        "the citing comment gives arXiv 2012.00062 (Peacock Patterns and "
        "Resurgence in Complex Chern-Simons Theory). Name similarity pointed at "
        "three other garoufalidis entries at 0.97 and every one was wrong"),
    "rsz2013": (
        "ramis-sauloy-zhang2013",
        "the citing comment reads \"Asterisque 355 §3.3 (Ramis-Sauloy-Zhang)\" "
        "and that entry is Asterisque vol. 355, 2013, by Ramis, Sauloy and "
        "Zhang — RSZ is the authors' initials"),
    # Same authors, same work, the key simply carries no year.
    "fulton-harris": (
        "fulton-harris1991",
        'sole Fulton-Harris entry, "Representation Theory: A First Course"'),
}


def fix_lean(text: str, old: str, new: str) -> tuple[str, int]:
    pat = re.compile(r"(--\s*Ref:\s*\[)" + re.escape(old) + r"(\])")
    return pat.subn(r"\g<1>" + new + r"\g<2>", text)


def fix_cites(text: str, old: str, new: str) -> tuple[str, int]:
    """Replace the key only inside a `cites: [...]` array."""
    n = 0

    def one(m: re.Match) -> str:
        nonlocal n
        body, k = m.group(2), 0
        body, k = re.subn(r'(["\'])' + re.escape(old) + r'\1',
                          lambda q: q.group(1) + new + q.group(1), body)
        n += k
        return m.group(1) + body + m.group(3)

    return re.sub(r"(cites:\s*\[)([^\]]*)(\])", one, text), n


def main() -> int:
    ap = argparse.ArgumentParser(description="Repoint dangling citation keys")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    # Every target must exist before anything is rewritten: a bibliography
    # id in references.ts, or — for a block-label target — a `label:` in the
    # content tree.
    refs = open(os.path.join(REPO, "content", "schema", "references.ts"),
                encoding="utf-8").read()
    labels: set[str] = set()
    for f in glob.glob(os.path.join(REPO, "content", "**", "*.ts"), recursive=True):
        labels.update(re.findall(r'label:\s*"([^"]+)"',
                                 open(f, encoding="utf-8", errors="replace").read()))
    missing = [new for _, (new, _) in MAPPING.items()
               if not re.search(r'\bid:\s*"' + re.escape(new) + r'"', refs)
               and new not in labels]
    if missing:
        sys.exit(f"targets resolve to neither an entry nor a block label: {missing}")

    total, files = 0, 0
    for path in sorted(glob.glob(os.path.join(REPO, "content", "**", "*.lean"), recursive=True)
                       + glob.glob(os.path.join(REPO, "content", "**", "*.ts"), recursive=True)):
        text = open(path, encoding="utf-8").read()
        orig, hits = text, []
        for old, (new, why) in MAPPING.items():
            if path.endswith(".lean"):
                text, n = fix_lean(text, old, new)
            else:
                text, n = fix_cites(text, old, new)
            if n:
                hits.append((old, new, n, why))
        if text == orig:
            continue
        files += 1
        rel = os.path.relpath(path, REPO)
        print(f"  {rel}")
        for old, new, n, why in hits:
            print(f"     {old} -> {new}  x{n}   ({why})")
            total += n
        if args.apply:
            open(path, "w", encoding="utf-8").write(text)

    print(f"\n{total} citation(s) repointed across {files} file(s)")
    if not args.apply:
        print("dry run — re-run with --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
