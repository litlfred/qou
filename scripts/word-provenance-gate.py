#!/usr/bin/env python3
"""Fail a change that hardcodes a BRAID WORD instead of obtaining it from the
producer that is supposed to emit it.

WHY THIS EXISTS
---------------
Three times in two days, on one bean (`qou-hu1f`), a claim about "which word
route X traces" was made by READING route X's source instead of instrumenting
it, and was wrong each time:

  1. `atom_braid_word_3A` was said to "use the grouped word `sigma_0^3
     sigma_1^-3`, 82 % from the Lean closed form". The real production block is
     eleven letters, two of them averaged, hence not a braid at all and 14.7 %
     away. Caught by a probe that finally measured the block.

  2. The 2026-09-05 ordering fix was described as making the function "emit
     beta_Bor", and each nucleon's block "the Borromean rings". Only the
     six-letter confinement CORE was reordered; the block still is not a braid
     and has no single closure to name.

  3. `nf_vs_canonical_word_order_probe.py` carried

         nf_seq = [("s", 0), ("S", 1)] * 3 + [
             ("s", 0), ("A", 0), ("A", 1), ("s", 0), ("s", 0)]

     as "the word `build_atom_nf_mp` traces", transcribed from
     `build_atom_nf`'s source. It omitted the electron crossing that
     `build_atom_nf` adds and `atom_braid_word_3A` does not, so the probe
     asserted "same multiset, different order" against a word whose trace it
     could not reproduce. **This one was green in CI for a day**, and it is what
     kept the `5.045e-4` A=1 residual mis-attributed to the word ordering when
     it was ordering and electron nearly cancelling.

Instance 3 is the one a gate can catch, and catching it would have caught the
mis-attribution: writing down *why* the literal was trusted is exactly the
moment the author looks for the electron.

WHAT IT CATCHES
---------------
A literal sequence of crossing letters — a list/tuple display of 2- or 3-tuples,
including `+` and `*` combinations of them — assigned to a name, in a file that
also references a word producer or a Markov-trace entry point. Those are the
files making word claims; elsewhere such a literal is just data.

WHAT IT DOES NOT CATCH
----------------------
Prose. Instances 1 and 2 above were sentences in a bean and a docstring, and no
static check reaches them. This gate narrows the class, it does not close it.
The discipline is still the rule: **if you state what word a producer emits, you
must have called it.**

ESCAPE HATCH
------------
`# word-literal-ok: <reason>` on any line the assignment spans, or anywhere in
the contiguous comment block directly above it — so the marker may HEAD a
multi-line provenance note, which is the shape a useful one takes. It applies to
ONE assignment: two adjacent literals need two notes.

Legitimate uses are common and expected — building `(sigma_0 sigma_1^-1)^3` from
first principles to compare AGAINST a producer is exactly right, and the
annotation should say so. What it must never say is "transcribed from
<producer>": that is the defect, and the fix is to call the producer.

USAGE
-----
    python3 scripts/word-provenance-gate.py                  # survey, never fails
    python3 scripts/word-provenance-gate.py --diff a.py b.py # gate the changed files
    python3 scripts/word-provenance-gate.py --strict         # gate the whole scan root
    python3 scripts/word-provenance-gate.py --selftest       # detector self-test only

SELF-TEST
---------
Runs on every invocation and ABORTS if it stops matching, per AGENTS.md
§"thirteen blind spellings" and the warning in bean `qou-5pgl`: a detector
without a known positive can report the whole class clean. The known positive is
the exact `nf_seq` literal above, in its original spelling.
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCAN_ROOT = "computations"

#: Functions that BUILD a word. A file naming one of these is making word claims.
PRODUCERS = {
    "atom_braid_word_3A", "atom_canonical_crossings", "atom_gen_chains",
    "nucleon_gen_chains", "nucleon_word_letters", "build_atom_nf",
    "build_atom_nf_mp", "build_atom_nf_exact", "build_nucleon_nf",
    "atom_braid_word_3A_to_crossings", "atom_braid_word_3A_sdp_gluon",
}
#: Entry points that CONSUME a word. Same reasoning.
TRACES = {
    "trM", "tr_M", "_trM", "tr_m_atom", "tr_m_atom_zn", "hm_mp", "hm_exact",
    "chi_lambda_of_word", "q_character_on_braid_word", "jones_closure",
}
ANNOTATION = "word-literal-ok:"
MIN_LEAVES = 2

#: Substrings marking a variable as holding a WORD rather than a data table.
WORD_NAMES = ("word", "seq", "letter", "crossing", "braid", "nf", "bor")
#: Crossing-kind vocabulary. A literal spelling these is a word by construction.
CROSSING_STRINGS = {
    "sigma", "sigma_inv", "sigma^-1", "averaged", "averaged_weighted",
    "s", "S", "A", "inv",
}


def _is_word_name(name: str) -> bool:
    low = name.lower()
    return any(k in low for k in WORD_NAMES)


def _string_members(leaves) -> set[str]:
    out = set()
    for leaf in leaves:
        for m in leaf.elts:
            if isinstance(m, ast.Constant) and isinstance(m.value, str):
                out.add(m.value)
    return out


def _all_triples_no_strings(leaves) -> bool:
    """`(c, d, gen)` shape — the exact-engine word format. Excludes the isotope
    and decay tables, which carry a name string in every row."""
    return bool(leaves) and all(
        len(leaf.elts) == 3
        and not any(isinstance(m, ast.Constant) and isinstance(m.value, str)
                    for m in leaf.elts)
        for leaf in leaves
    )


def _leaf_tuples(node: ast.AST) -> list[ast.AST] | None:
    """Leaf tuples of a word-literal expression, or None if not one.

    Accepts `[...]`, `(...)`, and `+` / `*` combinations, which is how these
    literals are actually written (`[a, b] * 3 + [c]`). Every leaf must be a 2-
    or 3-tuple of constants, unary-minus constants, or bare names — the shape of
    a `(kind, gen)` or `(c, d, gen)` crossing letter.
    """
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Mult)):
        out: list[ast.AST] = []
        for side in (node.left, node.right):
            if isinstance(side, ast.Constant):      # the `3` in `[...] * 3`
                continue
            sub = _leaf_tuples(side)
            if sub is None:
                return None
            out += sub
        return out
    if not isinstance(node, (ast.List, ast.Tuple)):
        return None
    leaves: list[ast.AST] = []
    for el in node.elts:
        if not isinstance(el, ast.Tuple) or not (2 <= len(el.elts) <= 3):
            return None
        for m in el.elts:
            ok = (isinstance(m, ast.Constant)
                  or isinstance(m, ast.Name)
                  or (isinstance(m, ast.UnaryOp) and isinstance(m.op, ast.USub)))
            if not ok:
                return None
        leaves.append(el)
    return leaves


def _names_used(tree: ast.AST) -> set[str]:
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Name):
            out.add(n.id)
        elif isinstance(n, ast.Attribute):
            out.add(n.attr)
        elif isinstance(n, ast.alias):
            out.add((n.asname or n.name).split(".")[-1])
    return out


def scan_source(src: str, path: str = "<src>") -> list[tuple[int, str, str]]:
    """`(lineno, target_name, snippet)` for every unannotated word literal."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    used = _names_used(tree)
    if not (used & PRODUCERS) and not (used & TRACES):
        return []                      # not a file that makes word claims
    names_a_trace = bool(used & TRACES)
    lines = src.splitlines()
    hits: list[tuple[int, str, str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        value = node.value
        if value is None:
            continue
        leaves = _leaf_tuples(value)
        if leaves is None or len(leaves) < MIN_LEAVES:
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        name = next((t.id for t in targets if isinstance(t, ast.Name)), "<expr>")
        # Is this a WORD, or just a table of tuples? Three routes, each narrow.
        # Without this the gate fires on every isotope list -- measured 151 hits
        # across computations/, of which the large majority were `(Z, N)` pairs
        # and `(name, Z, N)` rows that have nothing to do with braid words.
        strings = _string_members(leaves)
        # A literal carrying strings from OUTSIDE the crossing vocabulary is a
        # data table however it is named: `SEQ = [("D", 1, 1), ("3He", 2, 1)]`
        # is isotopes, not letters. Without this, the name route alone flags it.
        tabular = bool(strings - CROSSING_STRINGS)
        is_word = ((_is_word_name(name) and not tabular)
                   or bool(strings & CROSSING_STRINGS)
                   or (names_a_trace and _all_triples_no_strings(leaves)))
        if not is_word:
            continue
        # The annotation may sit on any line the assignment spans, or anywhere
        # in the contiguous comment block directly above it. A one-line reason
        # is rarely enough here -- the useful annotations explain provenance and
        # run to several lines -- so the marker is allowed to HEAD that block
        # rather than having to be its last line.
        lo, hi = node.lineno, getattr(node, "end_lineno", node.lineno) or node.lineno
        span = list(range(lo, min(hi, len(lines)) + 1))
        i = lo - 1
        while i >= 1 and lines[i - 1].lstrip().startswith("#"):
            span.append(i)
            i -= 1
        if any(ANNOTATION in lines[j - 1] for j in span):
            continue
        snippet = lines[lo - 1].strip()
        hits.append((lo, name, snippet[:96]))
    return hits


# ── self-test: the known positive, in its original spelling ──────────────────
_SELFTEST_BAD = '''
from mass_at_3A_proper import atom_braid_word_3A
def f():
    nf_seq = [("s", 0), ("S", 1)] * 3 + [
        ("s", 0), ("A", 0), ("A", 1), ("s", 0), ("s", 0)]
    return nf_seq
'''
_SELFTEST_OK_ANNOTATED = '''
from mass_at_3A_proper import atom_braid_word_3A
def f():
    # word-literal-ok: built from first principles to compare against the producer
    inter = [(1, 0, 0), (1, -h, 1)] * 3
    return inter
'''
#: The marker HEADING a multi-line comment block, which is how a real
#: provenance note is written. Locked in because the one-line-above rule
#: silently failed on exactly this shape when the gate was first wired.
_SELFTEST_OK_BLOCK_ANNOTATED = '''
import _exact_trace_engine as E
def f():
    # word-literal-ok: the two candidate confinement cores, from first
    # principles -- neither is transcribed from a producer; they are what the
    # producers are compared AGAINST, two lines below.
    inter = [(1, 0, 0), (1, -h, 1)] * 3
    return E.trM(3, inter)
'''
_SELFTEST_OK_DERIVED = '''
from mass_at_3A_proper import atom_braid_word_3A
def f():
    canon = atom_braid_word_3A(1, 0)
    return [(k, g) for _c, k, g in canon]
'''
_SELFTEST_OUT_OF_CLASS = '''
POINTS = [(1, 2), (3, 4), (5, 6)]
'''
#: Real false positives from the first survey (151 hits across `computations/`).
#: These are data tables, not words, and every one of them was flagged before
#: the `is_word` predicate was narrowed. Kept so a future widening cannot
#: silently reintroduce the noise that would make the gate unshippable.
_SELFTEST_DATA_TABLES = '''
from mass_at_3A_proper import atom_braid_word_3A
import _exact_trace_engine as E
NUCLEI = [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1)]
ISOTOPES_BASE = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
atoms = [(1, 0, "proton"), (0, 1, "neutron"), (1, 1, "deuteron")]
decays = [("free n -> p", "neutron", "proton"), ("x", "y", "z")]
cases = [(1, 0), (0, 1), (1, 1), (2, 1)]
SEQUENCE = [("p", 1, 0), ("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2)]
SEQ = [("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2)]
def f():
    return E.trM(3, [])
'''
#: A genuine word literal whose NAME gives nothing away -- caught only by the
#: `(c, d, gen)` shape route, in a file that names a trace entry point.
_SELFTEST_UNNAMED_WORD = '''
import _exact_trace_engine as E
def f():
    W = [(1, 0, 0), (1, 0, 1), (1, 0, 0)]
    return E.trM(3, W)
'''


#: `(label, source, must_flag)`. The count is derived, never written down —
#: a hardcoded "4/4" was wrong within an hour of this file existing, which is
#: the same stale-literal failure the gate itself is about.
#: NAME-route positive: a real case from the survey
#: (`trm_proton_five_values_census.py`). No crossing strings, not all 3-tuples,
#: so ONLY the word-ish name reaches it. Without this the name route can be
#: deleted and the self-test still passes — verified: it did, the first time.
_SELFTEST_NAME_ROUTE = '''
import _exact_trace_engine as E
def f():
    WORD = [(1, 1)] * 7 + [(1, 2)] * 4
    return E.trM(3, WORD)
'''
#: CROSSING-STRING-route positive: name gives nothing, shape is 2-tuples, so
#: only the crossing vocabulary reaches it.
_SELFTEST_TOKEN_ROUTE = '''
import _exact_trace_engine as E
def f():
    x = [(0, "sigma"), (1, "sigma_inv")] * 3
    return E.trM(3, x)
'''

_SELFTEST_CASES = [
    ("known positive: the nf_vs_canonical `nf_seq` literal", _SELFTEST_BAD, True),
    ("(c, d, gen) word with an uninformative name [SHAPE route]",
     _SELFTEST_UNNAMED_WORD, True),
    ("word-ish name, no crossing strings [NAME route]",
     _SELFTEST_NAME_ROUTE, True),
    ("crossing vocabulary, uninformative name [TOKEN route]",
     _SELFTEST_TOKEN_ROUTE, True),
    ("escape hatch, marker on the assignment", _SELFTEST_OK_ANNOTATED, False),
    ("escape hatch, marker heading a comment block", _SELFTEST_OK_BLOCK_ANNOTATED, False),
    ("producer-derived word", _SELFTEST_OK_DERIVED, False),
    ("literal in a file naming no producer", _SELFTEST_OUT_OF_CLASS, False),
    ("isotope / decay DATA TABLES", _SELFTEST_DATA_TABLES, False),
]


def selftest() -> tuple[list[str], int]:
    """`(failures, total)`. A detector with no known positive can report the
    whole class clean — AGENTS.md §"thirteen blind spellings", bean `qou-5pgl`."""
    fails = []
    for label, src, must_flag in _SELFTEST_CASES:
        hits = scan_source(src)
        if must_flag and not hits:
            fails.append(f"NOT MATCHED — {label}. The gate would under-report; "
                         f"fix the detector, do not ship it.")
        elif not must_flag and hits:
            fails.append(f"FALSE POSITIVE — {label} "
                         f"({[n for _l, n, _s in hits]}).")
    return fails, len(_SELFTEST_CASES)


def in_scope(p: Path) -> bool:
    try:
        rel = p.resolve().relative_to(REPO)
    except ValueError:
        return False
    return rel.parts[0] == SCAN_ROOT and p.suffix == ".py"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--diff", nargs="*", help="gate only these files")
    ap.add_argument("--strict", action="store_true",
                    help="gate the whole scan root, not just --diff")
    # BOTH spellings. `scripts/precision-gates.sh` invokes this with
    # `--self-test` (hyphenated) and treats a non-zero exit as "a detector that
    # cannot be shown to fire is a no-op". argparse exits 2 on the unrecognized
    # flag, so this gate's self-test has never actually run and the harness has
    # been reporting it failed for a reason unrelated to braid-word provenance.
    ap.add_argument("--self-test", "--selftest", action="store_true",
                    dest="selftest", help="self-test and exit")
    args = ap.parse_args()

    fails, n_cases = selftest()
    if fails:
        for f in fails:
            print(f"word-provenance-gate SELFTEST FAILED: {f}", file=sys.stderr)
        return 2
    if args.selftest:
        print(f"word-provenance-gate: self-test passed ({n_cases}/{n_cases})")
        return 0

    if args.diff is not None:
        named = [Path(f) for f in args.diff]
        files = [p for p in named if in_scope(p) and p.exists()]
        missing = sum(1 for p in named if not p.exists())
        scope_note = (f"{len(files)} of {len(named)} named file(s) in scope "
                      f"({SCAN_ROOT}/), {missing} missing")
        if not files:
            print(f"word-provenance-gate: nothing to scan -- {scope_note}. "
                  f"This is NOT a pass; it means no in-scope file was handed "
                  f"to the gate.")
            return 0
        blocking = True
    else:
        files = sorted((REPO / SCAN_ROOT).rglob("*.py"))
        scope_note = f"{len(files)} file(s) under {SCAN_ROOT}/"
        blocking = args.strict

    total = 0
    for p in files:
        try:
            hits = scan_source(p.read_text(encoding="utf-8", errors="replace"), str(p))
        except OSError:
            continue
        for lineno, name, snippet in hits:
            rel = p.resolve().relative_to(REPO)
            print(f"  {rel}:{lineno}  [word-literal]  {name} = {snippet}")
            total += 1

    if total:
        print(f"\nword-provenance-gate: {total} hardcoded word literal(s) "
              f"({scope_note}).")
        print("A literal claiming to be some producer's word must be OBTAINED "
              "from that producer.")
        print("If the literal is built from first principles (e.g. "
              "`(sigma_0 sigma_1^-1)^3` to compare against), annotate it:")
        print(f"    # {ANNOTATION} <why this literal is trustworthy>")
        print("Never annotate with \"transcribed from <producer>\" — that IS the "
              "defect (bean qou-hu1f, three instances).")
        return 1 if blocking else 0

    print(f"word-provenance-gate: clean -- {scope_note}, no unannotated word "
          f"literals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
