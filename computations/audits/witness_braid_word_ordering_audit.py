#!/usr/bin/env python3
"""Braid words STORED IN WITNESSES, and whether they carry the superseded order.

The 2026-09-05 ordering ruling (`qou-hu1f`) made the canonical intra-nucleon
core the interleaved Borromean `(s0 s1^-1)^3`. Four selectors have now looked
for fallout from it, and every one of them keys on CODE:

  * the `qou-hu1f` witness sweep      -- witness fields, but the ANCHOR fields
  * `binding_canonical`'s own audit   -- the producer's import cone
  * `qou-cvky` / PR #6940             -- files that RAISE
  * `self_built_braid_word_audit`     -- chi-kernel call sites (PR #6960)

None of them can see a braid word that is **stored in a witness JSON and read
back at runtime**. That is not a hypothetical gap. `qou-36i2`:
`canonical-mass-table-extended.witness.json` (`computedAt` 2026-08-28, a week
before the ruling) stores the GROUPED word for all 9 rows in a field named
`braid_word_canonical` -- and `qou_mass.api.canonical_braid` and
`compute_tr_M` both read that shard **first, deliberately**, so a pre-ruling
witness overrides a correctly-fixed live code path. The shipped package still
answers `tr_M(p) = 1.1458` (superseded) against the canonical 0.6293.

This audit is the data-side analogue: a value-keyed scan over the witness
corpus for stored braid words that are in the superseded order.

## The discriminator

Most stored words are not atom words at all -- torus knots `T(2,3)`, Hopf
links, Demazure reduced words, single generators -- and their orderings mean
nothing here. Two facts separate the atom words:

**1. Length.** The 3A-strand atom word has exactly `12A - 1` letters. Verified
against the shard's own rows: A=1 -> 11, A=2 -> 23, A=3 -> 35.

**2. Monotonicity.** The ruling's word is non-monotone BY CONSTRUCTION (the
core alternates `s0`, `s1`); the superseded one laid the core down grouped, so
its generator sequence is non-decreasing. For a word of atom length, therefore:

    monotone      <=>  grouped     (superseded)
    non-monotone  <=>  borromean   (the ruling)

A word that is atom-LENGTH and monotone is the defect shape. Anything else is
reported for a reader, not flagged.

## What it does NOT do

It does not decide whether a witness OUGHT to hold an atom word -- a probe may
legitimately record a grouped word as the historical control, exactly as
`compute_tau_M_nucleon_H3` keeps one behind `intra_order="grouped"`. It narrows
3830 witness files to the few a human must read.

No arithmetic: this reads integers out of JSON and compares them. No precision
surface.

Exit 0 by default (a census). `--strict` exits 1 when any atom-length monotone
word is found.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

SEARCH_ROOTS = ["computations", "qou-mass"]
SKIP_PARTS = {"_deprecated", ".git", "node_modules", "__pycache__", ".lake"}

# A field holding a braid word. Matched on the JSON path, case-insensitively.
WORD_KEY = re.compile(r"braid|(^|[/_])word|generator", re.I)


def _iter_witnesses():
    for r in SEARCH_ROOTS:
        base = ROOT / r
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.witness.json")):
            if any(part in SKIP_PARTS for part in p.parts):
                continue
            yield p


def _gen_sequence(value):
    """Recover a generator sequence from a stored word, or None.

    Three encodings occur in this corpus and all three are handled, because
    keying on one of them is how a scan of stored data ends up measuring its
    own assumptions rather than the corpus:

        [[0, "sigma"], [1, "sigma_inv"], ...]   pair-per-letter (the shard)
        [0, 0, 1, 1, ...]                       bare generator indices
        [{"gen": 0, ...}, ...]                  dict-per-letter
    """
    if not isinstance(value, list) or not value:
        return None
    out = []
    for e in value:
        if isinstance(e, bool):
            return None
        if isinstance(e, int):
            out.append(e)
        elif isinstance(e, list):
            # A LETTER is `[gen, "sigma"]` -- exactly two slots, the second a
            # crossing type. A list whose entries are lists of INTS is a list
            # of WORDS, not a word, and reading `e[0]` from each takes the
            # first letter of every word and calls the result a word.
            #
            # Measured, and it is why this branch is not the one-liner it was:
            # `hecke-agtb-lineage-schedule` `/data/cases[14]/U_words_rel_i`
            # holds 23 words of 14 letters at `n = 17`. The old rule turned
            # that into a monotone 23-letter sequence of atom length and
            # flagged it. Nothing about it is an atom word.
            if len(e) != 2 or isinstance(e[1], (int, bool, list, dict)):
                return None
            if not isinstance(e[0], int) or isinstance(e[0], bool):
                return None
            out.append(e[0])
        elif isinstance(e, dict):
            g = next((e[k] for k in ("gen", "generator", "gen_idx", "g", "i")
                      if isinstance(e.get(k), int)
                      and not isinstance(e.get(k), bool)), None)
            if g is None:
                return None
            out.append(g)
        else:
            return None
    return out or None


def _atom_A(length: int):
    """The mass number whose atom word has this length, or None.

    The 3A-strand atom word has `12A - 1` letters.
    """
    if length < 11 or (length + 1) % 12:
        return None
    return (length + 1) // 12


def _is_atom_shaped(gens, A):
    """Does this sequence plausibly live on 3A strands?

    Length alone is not enough, and the corpus proves it. Two real fields are
    atom-LENGTH and monotone while being nothing of the kind:

        joint-tower-sdp-rust  /...**/canonical_word  [1,2,3,...,11]
        hecke-agtb-lineage-schedule  /...U_words_rel_i  [1]*12

    The first is an index list, the second a uniform word. A braid word on 3A
    strands has generators in a window of at most `3A - 1` values (0..3A-2, or
    1..3A-1 where the corpus writes them 1-indexed), and an ATOM word must join
    its nucleons, so it uses at least two. Both facts are about the strand
    count, not about the ordering, so this filter cannot hide a grouped word.

        span 11 > 2  for A=1  ->  not a 3-strand word
        span  1 < 2           ->  not an atom word
    """
    span = max(gens) - min(gens) + 1
    return 2 <= span <= 3 * A - 1


def scan():
    rows = []
    for path in _iter_witnesses():
        try:
            doc = json.loads(path.read_text(encoding="utf-8", errors="replace"))
        except (json.JSONDecodeError, ValueError, OSError):
            continue
        rel = str(path.relative_to(ROOT))

        def walk(node, jpath=""):
            if isinstance(node, dict):
                for k, v in node.items():
                    walk(v, f"{jpath}/{k}")
                return
            if not isinstance(node, list):
                return
            if WORD_KEY.search(jpath):
                gens = _gen_sequence(node)
                if gens is not None:
                    A = _atom_A(len(gens))
                    mono = all(a <= b for a, b in zip(gens, gens[1:]))
                    shaped = A is not None and _is_atom_shaped(gens, A)
                    rows.append({
                        "file": rel, "json_path": jpath, "length": len(gens),
                        "atom_A": A, "atom_shaped": shaped, "monotone": mono,
                        "flagged": bool(shaped and mono),
                        "span": max(gens) - min(gens) + 1,
                        "head": gens[:12],
                    })
                    return
            for i, v in enumerate(node):
                walk(v, f"{jpath}[{i}]")

        walk(doc)
    return rows


_SELFTEST = [
    ("pair-per-letter, atom length 11, GROUPED -- the qou-36i2 shape",
     [[0, "s"], [0, "s"], [0, "s"], [0, "s"], [0, "s"], [0, "s"], [0, "s"],
      [1, "s"], [1, "s"], [1, "s"], [1, "s"]], True),
    ("same length, BORROMEAN (non-monotone) -- the ruling's word",
     [[0, "s"], [1, "s"], [0, "s"], [1, "s"], [0, "s"], [1, "s"], [0, "s"],
      [0, "s"], [1, "s"], [0, "s"], [0, "s"]], False),
    ("bare ints, atom length 23, grouped -- the A=2 word CLIMBS; an earlier\n"
     "          fixture here dropped back to 0 and the self-test caught it",
     [0] * 7 + [1] * 4 + [2] + [3] * 7 + [4] * 4, True),
    ("1-INDEXED grouped atom word -- the markov-trace spelling",
     [1] * 7 + [2] * 4, True),
    ("atom LENGTH but an index list [1..11] -- joint-tower-sdp-rust",
     list(range(1, 12)), False),
    ("atom LENGTH but uniform [1]*23 -- hecke-agtb-lineage-schedule",
     [1] * 23, False),
    ("dict-per-letter, atom length 11, grouped",
     [{"gen": 0}] * 7 + [{"gen": 1}] * 4, True),
    ("a TORUS word T(2,3) -- monotone but NOT atom length",
     [0, 0, 0], False),
    ("a long monotone word of non-atom length", [0] * 12, False),
    ("a LIST OF WORDS is not a word -- hecke-agtb-lineage-schedule, where\n"
     "          reading e[0] from each took the first letter of 23 words",
     [[1, 0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0],
      [1, 0, 2, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 0],
      [1, 2, 0, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 0]], False),
]


def _selftest() -> int:
    bad = 0
    for label, value, want in _SELFTEST:
        gens = _gen_sequence(value)
        got = False
        if gens is not None:
            A = _atom_A(len(gens))
            got = bool(A is not None and _is_atom_shaped(gens, A)
                       and all(a <= b for a, b in zip(gens, gens[1:])))
        ok = got == want
        bad += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n"
              f"          flagged {got} (want {want})")
    print(f"\n  {len(_SELFTEST) - bad}/{len(_SELFTEST)} self-test shapes")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when an atom-length monotone word is stored")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    rows = scan()
    if args.json:
        print(json.dumps(rows, indent=2))
        return 0

    files = {r["file"] for r in rows}
    atom = [r for r in rows if r["atom_A"] is not None]
    flagged = [r for r in rows if r["flagged"]]

    print(f"  stored word fields: {len(rows)} in {len(files)} witness files")
    shaped = [r for r in rows if r["atom_shaped"]]
    print(f"  of atom length (12A-1): {len(atom)}")
    print(f"  and atom-SHAPED (2 <= generator span <= 3A-1): {len(shaped)}")
    print(f"  ATOM-LENGTH AND MONOTONE (the superseded order): {len(flagged)}\n")

    by_file: dict[str, list] = {}
    for r in flagged:
        by_file.setdefault(r["file"], []).append(r)
    for f in sorted(by_file):
        print(f"  {f}")
        for r in by_file[f][:6]:
            print(f"       {r['json_path']}  A={r['atom_A']} "
                  f"len={r['length']}  gens={r['head']}")
        if len(by_file[f]) > 6:
            print(f"       ... and {len(by_file[f]) - 6} more field(s)")

    print("\n  A word of atom length whose generators are non-decreasing IS the\n"
          "  grouped (pre-2026-09-05) ordering. That is a CANDIDATE, not a\n"
          "  verdict: a probe may legitimately record the historical word as a\n"
          "  control. What it is not is invisible, which is what it was.")
    return 1 if (args.strict and flagged) else 0


if __name__ == "__main__":
    raise SystemExit(main())
