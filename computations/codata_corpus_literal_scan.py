"""Corpus-wide scan for CODATA literals that are close to, but not, the table.

Answers "are there other edition straddles like the muon ratio?" mechanically
instead of by grep-and-hope.

Method
------

Every numeric literal in the corpus with enough significant digits to be a
physical constant is compared against every value in the NIST CODATA-2022
table (`library/allascii.txt`). A literal is reported when it is

    NEAR   a table value  (relative difference below `--near`, default 1e-5)
    BUT    not equal to it,

which is exactly the signature of a stale edition or a mis-transcription: the
leading digits match, the trailing ones do not. Literals that match a table
value exactly are silent, and literals nowhere near any table value are silent
(they are not CODATA quantities at all).

This deliberately does **not** try to understand what each literal means. It
cannot tell a stale CODATA value from a legitimately different quantity that
happens to sit nearby, so its output is a **candidate list for agent review**,
not a gate. The `--near` threshold trades recall for noise.

What it *can* tell is whether a literal is **executable**, and that turned out
to matter more than the near-miss test itself. Sites are split four ways:

    CODE         executable -- the only class that can compute a wrong number
    PROSE        inside a comment or a string; inert
    ADJUDICATED  executable, but carrying the reviewed-literal marker
    RECORD       witness JSON / audit output; a number already computed

Measured on 2026-08-21, the split of 448 `.py`/`.lean`/`.ts` sites was **61
code, 381 prose, 6 adjudicated** -- so the label this script printed for two
weeks, *"SOURCE sites (compute a wrong number)"*, was wrong for 87 % of what
it counted, and the actionable queue is ~61, not 448.

The prose majority is not incidental. A drain that replaces a stale literal
with a registry read and **records the superseded value beside it** lands
squarely in PROSE, so counting prose as defects makes the number go *up* when
the corpus gets better, and rewards deleting the provenance to bring it down.
That is exactly what happened: the tranche-a drain moved this count 447 -> 448.
Only CODE gates under `--strict`.

Run:  python3 -u computations/codata_corpus_literal_scan.py
      python3 -u computations/codata_corpus_literal_scan.py --near 1e-7
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import tokenize
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))

from codata_table import table  # noqa: E402

mp.mp.dps = 60

REPO = Path(__file__).resolve().parent.parent

# Where to look. `library/` is excluded: it holds the table itself plus the
# source PDFs, so scanning it would report the authority as a suspect.
SCAN_EXTS = {".py", ".ts", ".md", ".lean", ".json"}
SKIP_DIRS = {
    ".git", "node_modules", ".lake", "__pycache__", "library",
    ".beans", "build", "dist", ".pytest_cache", "_deprecated",
    # `.claude` because agent worktrees live at `.claude/worktrees/<agent-id>/`
    # — a FULL SECOND CHECKOUT of the repo, gitignored (.gitignore:120), 0
    # tracked files. Without it this gate scans every file twice and reports
    # the copy as a finding.
    #
    # Measured 2026-08-22 with one worktree present: **83 of 83** reported
    # literals were under `.claude/worktrees/`, and **zero** were real. So
    # this BLOCKING gate went red on a clean tree, for files nobody touched,
    # purely because an agent had a worktree checked out — and it would go
    # green again when that worktree was removed, with no code change.
    #
    # That environment-dependence is the serious part: a gate whose verdict
    # depends on local checkout state cannot be trusted or reproduced, and the
    # cost of a false red is that people learn to skip the preflight. Same
    # root cause as the fix to `f64_into_mpmath_audit.py` (bean `qou-myk3`),
    # which is why that bean flags every `rglob` scanner as a candidate.
    ".claude",
}

# A literal needs enough digits to identify a constant. Below ~7 significant
# digits almost every number is "near" something.
_NUM = re.compile(r"(?<![\w.])(\d{1,6}\.\d{4,20})(?![\w.])")

MIN_SIG_DIGITS = 7


def _sig_digits(s: str) -> int:
    return len(s.replace(".", "").lstrip("0"))


def _same_number(a: str, b: str) -> bool:
    """Decimal-string equality ignoring trailing-zero padding.

    `'3477.23000000'` and `'3477.23'` are the same value written to different
    widths; reporting that pair as a near-miss is noise.
    """
    def norm(s: str) -> str:
        return s.rstrip("0").rstrip(".") if "." in s else s

    return norm(a) == norm(b)


# ── Digit-prefix prefilter ──────────────────────────────────────────
#
# MEASURED before writing this: the scan took 87.5 s over 25,233 files, of
# which read + regex was 15.2 s. The other ~72 s was mpmath, and cProfile
# attributes it to two things, in this order:
#
#   mpf.__sub__  6,448,043 calls   <- the inner loop over by_exp[exp]
#   mp.log10       372,558 calls   <- one per literal, for its exponent
#
# 372,265 literals clear MIN_SIG_DIGITS, so the inner loop runs about 17 mpf
# subtractions per literal. Neither number is I/O.
#
# The cheap necessary condition: a near-miss at rel < 1e-5 agrees with its
# table row to roughly five significant digits, so its first FOUR significant
# digits and its decimal exponent must match one of a small set precomputed
# from the table. Both are obtainable from the literal's characters -- no mpf
# is constructed, no logarithm is taken -- and a literal that misses is
# dropped before any mpmath runs at all.
#
# THE FILTER MUST NEVER DROP A CANDIDATE THE FULL COMPARISON WOULD HAVE
# REPORTED. The keys are enumerated from the INTERVAL around each table
# value, not from the value itself, so any v within `near` of a row t lands
# in one of t's buckets by construction; the endpoints are then widened by
# one bucket each way against log10 rounding. Over-inclusion costs a few
# extra mpf comparisons and nothing else. The claim is checked two ways: by
# self-test cases below, and by diffing the full listing against the
# pre-filter scan over the real corpus (identical, 1791 lines).
_PREFIX_K = 4

# Above this threshold the interval spans too many buckets for the prefilter
# to be worth enumerating (roughly 2*near*10^K of them), so it is switched
# off entirely rather than truncated. Truncating would silently narrow the
# scan, which is the one thing this optimisation must not do.
_PREFILTER_MAX_NEAR = 1e-3


def _prefix_key(lit: str) -> tuple[int, int] | None:
    """(decimal exponent, first _PREFIX_K significant digits) by string ops.

    Exact, and free of mpmath. `938.27208816` -> `(2, 9382)`;
    `0.51099895` -> `(-1, 5109)`. Returns None for an all-zero literal.
    """
    ip, _, fp = lit.partition(".")
    digits = ip + fp
    i, n = 0, len(digits)
    while i < n and digits[i] == "0":
        i += 1
    if i == n:
        return None
    return len(ip) - 1 - i, int(digits[i:i + _PREFIX_K].ljust(_PREFIX_K, "0"))


def _key_of(v) -> tuple[int, int]:
    """The same key for an mpf, used to bucket the table side."""
    e = int(mp.floor(mp.log10(v)))
    lo, hi = 10 ** (_PREFIX_K - 1), 10 ** _PREFIX_K
    d = int(mp.floor(v / mp.mpf(10) ** (e - _PREFIX_K + 1)))
    # log10 can land a hair either side of a decade boundary; correct from the
    # digit count, which cannot.
    if d >= hi:
        e, d = e + 1, d // 10
    elif d < lo:
        e -= 1
        d = int(mp.floor(v / mp.mpf(10) ** (e - _PREFIX_K + 1)))
    return e, d


def _prefilter_for(entries, near: float) -> set[tuple[int, int]] | None:
    """Bucket set for the whole table, or None meaning "compare everything".

    None is the pre-optimisation behaviour, kept reachable so a wide --near
    degrades to the full comparison instead of to a truncated bucket walk.
    """
    if near > _PREFILTER_MAX_NEAR:
        return None
    keys: set[tuple[int, int]] = set()
    for e in entries:
        if e.value > 0:
            keys |= _prefix_keys_for(e.value, near)
    return keys


def _prefix_keys_for(value, near: float) -> set[tuple[int, int]]:
    """Every bucket the open interval (v(1-near), v(1+near)) can touch."""
    lo_v = value * (1 - mp.mpf(near))
    hi_v = value * (1 + mp.mpf(near))
    if lo_v <= 0:
        return set()
    lo, hi = 10 ** (_PREFIX_K - 1), 10 ** _PREFIX_K
    (le, ld), (he, hd) = _key_of(lo_v), _key_of(hi_v)
    keys: set[tuple[int, int]] = set()
    e, d = le, ld
    while True:
        keys.add((e, d))
        if (e, d) == (he, hd):
            break
        d += 1
        if d >= hi:
            e, d = e + 1, lo
    # One bucket of slack on each end.
    for ee, dd in ((le, ld - 1), (he, hd + 1)):
        if dd < lo:
            keys.add((ee - 1, hi - 1))
        elif dd >= hi:
            keys.add((ee + 1, lo))
        else:
            keys.add((ee, dd))
    return keys


# This scan's own witness lists every literal it found, so scanning it would
# count each finding a second time and grow the total on every re-run. Exclude
# the producer's own output.
# Likewise this finding's own audit note, which quotes each offending literal
# beside its table value in order to report them. An artifact ABOUT the
# finding is not an instance of it -- the same reason
# `hardcoded-literal-audit.witness.json` is a listing rather than a use.
# This scanner's OWN source, for the third instance of the same defect: its
# module docstring and its self-test both quote stale CODATA values in order
# to explain and to test for them, and adding that documentation moved
# prose_sites 381 -> 397. An artifact ABOUT the finding is not an instance of
# it -- the same reason the witness and the audit note are excluded.
SELF_ARTIFACTS = {
    "codata-corpus-vintage-scan.witness.json",
    "2026-08-19-codata-edition-straddle-corpus-sweep.md",
    "codata_corpus_literal_scan.py",
}


# ── Executable code vs comment/docstring ────────────────────────────
#
# A near-miss literal in a .py/.lean/.ts file was reported as a SOURCE site
# that "computes a wrong number". Measured, that label is wrong for the large
# majority of them: of 448 such sites, 53 are executable and 395 sit inside a
# comment or a string. Most of the latter are the OPPOSITE of a defect -- a
# drain that replaces a stale literal with a registry read, and records the
# superseded value beside it so a reader can see what moved, ADDS a site.
# Counting those as defects rewards deleting the provenance.
#
# So each site is classified, and only `code` can compute anything.


def _nonexec_spans_py(path: Path) -> list[tuple[int, int, int, int, str]]:
    """(start_line, start_col, end_line, end_col, kind) for comments/strings.

    Uses `tokenize` rather than line heuristics: a literal in a trailing
    comment on an otherwise-executable line must not tar the whole line, and a
    multi-line docstring must cover every line it spans.
    """
    spans: list[tuple[int, int, int, int, str]] = []
    try:
        with open(path, "rb") as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type == tokenize.COMMENT:
                    spans.append((*tok.start, *tok.end, "comment"))
                elif tok.type == tokenize.STRING:
                    spans.append((*tok.start, *tok.end, "string"))
    except (tokenize.TokenError, IndentationError, SyntaxError, OSError, UnicodeDecodeError):
        # An unparseable file yields no spans, so every hit in it stays
        # `code` -- the conservative direction: over-report, never hide.
        return []
    return spans


_LINE_COMMENT = {".lean": "--", ".ts": "//"}
_BLOCK_COMMENT = {".lean": ("/-", "-/"), ".ts": ("/*", "*/")}
_QUOTES = {".lean": '"', ".ts": "\"'`"}


def _nonexec_spans_text(path: Path, text: str) -> list[tuple[int, int, int, int, str]]:
    """Same, for .lean/.ts, by scanning characters with a small state machine.

    STRING LITERALS ARE TRACKED, and that is not a nicety. The first version
    of this function handled only comments, on the reasoning that an untracked
    string could merely let a delimiter inside it open a comment that is not
    there -- an under-report. That reasoning was wrong in the direction that
    matters: prose sitting inside a string is then classified `code`, which
    OVER-reports. Measured, `content/values/registry.ts:647` is a CODATA value
    quoted inside a `description:` string and was reported as executable.

    Still cruder than the Python path: no escape-aware interpolation, no
    nested `/- -/`, and a `--` inside a Lean string is handled only because
    strings are now tracked at all.
    """
    line_tok = _LINE_COMMENT.get(path.suffix)
    if line_tok is None:
        return []
    open_tok, close_tok = _BLOCK_COMMENT[path.suffix]
    quotes = _QUOTES[path.suffix]

    spans: list[tuple[int, int, int, int, str]] = []
    lines = text.split("\n")
    state = "normal"          # normal | block | string
    quote_ch = ""
    start: tuple[int, int] = (0, 0)

    for lineno, line in enumerate(lines, 1):
        i = 0
        n = len(line)
        while i < n:
            if state == "normal":
                if line.startswith(open_tok, i):
                    state, start = "block", (lineno, i)
                    i += len(open_tok)
                elif line.startswith(line_tok, i):
                    spans.append((lineno, i, lineno, n, "comment"))
                    break
                elif line[i] in quotes:
                    state, quote_ch, start = "string", line[i], (lineno, i)
                    i += 1
                else:
                    i += 1
            elif state == "block":
                if line.startswith(close_tok, i):
                    spans.append((*start, lineno, i + len(close_tok), "comment"))
                    state = "normal"
                    i += len(close_tok)
                else:
                    i += 1
            else:  # string
                if line[i] == "\\":
                    i += 2
                elif line[i] == quote_ch:
                    spans.append((*start, lineno, i + 1, "string"))
                    state = "normal"
                    i += 1
                else:
                    i += 1
        if state == "string" and quote_ch not in '"""':
            # An unterminated single-line string is a lexing artifact (an
            # apostrophe in a comment-free line, a Lean `'` in an identifier).
            # Close it at end of line rather than swallowing the whole file.
            spans.append((*start, lineno, n, "string"))
            state = "normal"

    if state != "normal":
        spans.append((*start, len(lines), len(lines[-1]) if lines else 0,
                      "comment" if state == "block" else "string"))
    return spans


# An agent that has looked at a site and judged the literal correct marks it
# with the corpus-wide reviewed-literal marker. Re-reporting an adjudicated
# site every run is how a candidate list stops being read. Measured: the
# `markov_trace_axiomatic_multi_atom` proton/neutron rows carry the marker AND
# a comment naming the live value they defer to, and were still being counted.
# Two markers, from two different subsystems, both meaning "an agent looked
# at this literal and it is correct as written":
#
#   `# noqa: P31`                     the corpus-wide reviewed-literal marker
#   `:leanval[sym]{precision=N}`      the witnessed-values system's DECLARED
#                                     truncation -- the literal is pinned to a
#                                     witness and deliberately carried to N
#                                     digits, which is machine-checked
#                                     elsewhere (see local/witnessed-values)
#
# The second was found the hard way: `partition-sum-proton-residual.lean:66`
# carries `precision=8` on an m_e truncated to exactly 8 digits, and two
# further sites in the same file mirror that value inside the proof of
# `electronMass_witness`. "Draining" any of the three would have broken a
# declared, machine-checked arrangement to satisfy a detector that could not
# see it -- the same failure mode as counting a provenance comment as a
# defect. 11 sites in the corpus carry a `precision=` declaration.
# `#` for Python/TS, `--` for Lean. Without the Lean form a `.lean` site
# could not be adjudicated at all, and 20 of the 36 remaining sites are
# Lean -- so the marker was unusable exactly where it was most needed.
_NOQA_P31 = re.compile(r"(?:#|--)\s*noqa:\s*[\w,\s]*\bP31\b")
_LEANVAL_PRECISION = re.compile(r":leanval\[[^\]]*\]\{[^}]*\bprecision=(\d+)")


def _adjudicated(line: str, lit: str, want: str) -> bool:
    """Is this literal already reviewed, or declaredly truncated *and correct*?

    `noqa: P31` is an agent's flat assertion and is taken at face value.

    `precision=N` is NOT, and the difference matters. It declares only that
    the literal is deliberately carried to N significant digits -- it says
    nothing about which CODATA edition those digits came from. Treating it as
    a blanket exemption would have silently excused
    `partition-sum-proton-residual.lean:59`, where `precision=11` sits on
    `938.27208816`: the truncation is declared and fine, and the value is
    CODATA-2018. So the declaration is *checked*: the literal is adjudicated
    only if it equals the table value truncated to those N digits. A declared
    truncation of the right number is fine; a declared truncation of the wrong
    number is still a defect, and now still reported.
    """
    if _NOQA_P31.search(line):
        return True
    m = _LEANVAL_PRECISION.search(line)
    if not m:
        return False
    n = int(m.group(1))
    digits = lambda x: x.replace(".", "").replace("-", "").lstrip("0")[:n]  # noqa: E731
    return digits(lit) == digits(want)


def _classify(spans, lineno: int, col: int) -> str:
    """`code`, `comment` or `string` for one match position."""
    for sl, sc, el, ec, kind in spans:
        if lineno < sl or lineno > el:
            continue
        if lineno == sl and col < sc:
            continue
        if lineno == el and col >= ec:
            continue
        return kind
    return "code"


def _iter_files():
    for path in REPO.rglob("*"):
        if not path.is_file() or path.suffix not in SCAN_EXTS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SELF_ARTIFACTS:
            continue
        yield path


def self_test() -> int:
    """Exercise the classifier on the shapes that were actually wrong.

    Each case below is a defect this scan had, not a hypothetical: the
    trailing-comment case is why classification is by column span rather than
    by line, and the `.ts` string case is why `.lean`/`.ts` strings are
    tracked at all.
    """
    import tempfile

    cases = [
        # (suffix, source, {lineno: expected kind for the literal on it})
        (".py", 'X = 938.27208816\n', {1: "code"}),
        (".py", '# was 938.27208816 before the drain\n', {1: "comment"}),
        # A trailing period must not abut the literal: `_NUM` refuses a
        # digit run followed by another `.`, so it would match nothing here.
        (".py", '"""Docstring quoting 938.27208816 MeV."""\n', {1: "string"}),
        # Both on one line: the comment must not tar the code.
        (".py", 'X = 938.27208816  # was 939.56542052\n', {1: "code"}),
        (".py", 'S = "938.27208816"\n', {1: "string"}),
        (".lean", 'def p : Float := 938.27208816\n', {1: "code"}),
        (".lean", '-- CODATA 2018 was 938.27208816\n', {1: "comment"}),
        (".lean", '/- block: 938.27208816 -/\n', {1: "comment"}),
        # The registry.ts false positive, in miniature.
        (".ts", 'const d = "CODATA 2022 value 938.27208816 MeV";\n', {1: "string"}),
        (".ts", 'const v = 938.27208816;\n', {1: "code"}),
        (".ts", '// legacy 938.27208816\n', {1: "comment"}),
    ]

    failures = 0
    for suffix, text, expected in cases:
        with tempfile.NamedTemporaryFile("w", suffix=suffix, delete=False) as fh:
            fh.write(text)
            path = Path(fh.name)
        try:
            spans = (
                _nonexec_spans_py(path)
                if suffix == ".py"
                else _nonexec_spans_text(path, text)
            )
            for lineno, line in enumerate(text.split("\n"), 1):
                if lineno not in expected:
                    continue
                m = _NUM.search(line)
                assert m is not None, f"no literal found in {line!r}"
                got = _classify(spans, lineno, m.start(1))
                want = expected[lineno]
                flag = "ok  " if got == want else "FAIL"
                if got != want:
                    failures += 1
                print(f"  [{flag}] {suffix:<6}{line.rstrip()!r:<52} -> {got} (want {want})")
        finally:
            path.unlink(missing_ok=True)

    # `lit` and the table value the site is scored against, then the verdict.
    ME = "0.51099895069"
    MP = "938.27208943"
    for line, lit, want, expect in [
        ("X = 938.27208816  # noqa: P31 - reviewed", "938.27208816", MP, True),
        ("X = 938.27208816  # noqa: E501,P31", "938.27208816", MP, True),
        ("X = 938.27208816  # noqa: E501", "938.27208816", MP, False),
        ("X = 938.27208816  # P31 is discussed here", "938.27208816", MP, False),
        # Lean comment token.
        ("def m : R := 938.27208816  -- noqa: P31 - AME-derived, not CODATA",
         "938.27208816", MP, True),
        # A declared truncation of the CORRECT value: adjudicated.
        ("def electronMass : R := 0.51099895  -- :leanval[m_e_MeV]{precision=8}",
         "0.51099895", ME, True),
        # A declared truncation of a STALE-EDITION value: still a defect.
        # This is the real site partition-sum-proton-residual.lean:59.
        ("def protonCodata : R := 938.27208816  -- :leanval[m_p_MeV]{precision=11}",
         "938.27208816", MP, False),
        # A leanval reference with no precision claim is NOT an adjudication.
        ("def v : R := 0.51099895  -- :leanval[m_e_MeV]", "0.51099895", ME, False),
    ]:
        got = _adjudicated(line, lit, want)
        flag = "ok  " if got == expect else "FAIL"
        if got != expect:
            failures += 1
        print(f"  [{flag}] marker {line[:58]!r:<62} -> {got} (want {expect})")


    # ── Prefilter soundness ─────────────────────────────────────────
    #
    # The prefilter is the one change here that could make the gate quietly
    # narrower rather than merely wrong, so it is tested for the property
    # that matters -- NEVER DROPS A CANDIDATE -- and not just for a few
    # hand-picked keys.
    #
    # The chain has two links, and both are checked:
    #   (a) the string key and the mpf key agree, so a literal is bucketed
    #       the same way the table was;
    #   (b) every value within `near` of any table row is in that row's
    #       bucket set.
    # (b) is checked against ALL 293 rows at four offsets each, rather than
    # against a sample, because the failure it guards is a silent one.

    # (a) string key == mpf key, across the whole domain `_NUM` admits,
    #     including the decade boundaries where floor(log10) is delicate.
    for lit in ("938.27208816", "0.51099895", "1.0000000", "999.9999999",
                "1000.0000001", "0.00010000001", "137.035999177",
                "999999.9999", "0.0009999999"):
        want = _key_of(mp.mpf(lit))
        got = _prefix_key(lit)
        flag = "ok  " if got == want else "FAIL"
        if got != want:
            failures += 1
        print(f"  [{flag}] key    {lit:<16} -> {got} (mpf says {want})")

    # (b) nothing within `near` of a row escapes the filter.
    near = 1e-5
    rows = [e for e in table().values() if e.value > 0]
    keys: set[tuple[int, int]] = set()
    for e in rows:
        keys |= _prefix_keys_for(e.value, near)
    escaped = 0
    for e in rows:
        for frac in (-0.99, -0.5, 0.5, 0.99):
            if _key_of(e.value * (1 + mp.mpf(near) * frac)) not in keys:
                escaped += 1
    flag = "ok  " if escaped == 0 else "FAIL"
    if escaped:
        failures += 1
    print(f"  [{flag}] filter {len(rows)} rows x 4 offsets within near -> "
          f"{escaped} escaped (want 0), {len(keys)} buckets")

    # A `--near` too wide to bucket must switch the filter OFF, not truncate
    # it: a truncated enumeration is exactly the silent narrowing above. The
    # check calls the real selector, so it fails if the guard is removed.
    wide, narrow = _PREFILTER_MAX_NEAR * 10, _PREFILTER_MAX_NEAR
    off, on = _prefilter_for(rows, wide), _prefilter_for(rows, narrow)
    ok = off is None and isinstance(on, set) and len(on) > 0
    if not ok:
        failures += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] filter --near {wide:g} -> "
          f"{'disabled' if off is None else 'STILL ON'}; "
          f"--near {narrow:g} -> {len(on) if on else 0} buckets")

    print()
    print("self-test FAILED" if failures else "self-test passed")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--near", type=float, default=1e-5,
                    help="relative distance within which a literal counts as "
                         "'meant to be' a table value (default 1e-5)")
    ap.add_argument("--quiet", action="store_true",
                    help="summary only, no per-site listing")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any near-miss is in EXECUTABLE .py/.lean/.ts "
                         "code. Comments, docstrings, witness JSON and audit "
                         "output all record a number rather than computing one, "
                         "and never gate.")
    ap.add_argument("--no-witness", action="store_true",
                    help="skip writing the witness JSON")
    ap.add_argument("--self-test", action="store_true",
                    help="check the code/comment/string classifier and exit")
    args = ap.parse_args()
    started = time.time()

    if args.self_test:
        return self_test()

    entries = list(table().values())
    # Index by magnitude so each literal compares against a handful of
    # candidates rather than all 293.
    by_exp: dict[int, list] = defaultdict(list)
    for e in entries:
        if e.value == 0:
            continue
        by_exp[int(mp.floor(mp.log10(abs(e.value))))].append(e)

    prefilter = _prefilter_for(entries, args.near)

    print("=" * 78)
    print("CODATA corpus literal scan — near-misses against the NIST table")
    print("=" * 78)
    print(f"threshold: relative distance < {args.near:g}, and not exactly equal")
    print(f"table    : {len(entries)} entries (2022 CODATA adjustment)")
    print()

    # {(literal, table quantity): [(file, line), ...]}
    findings: dict[tuple[str, str, str], list[tuple[str, int]]] = defaultdict(list)
    files_scanned = 0

    for path in _iter_files():
        files_scanned += 1
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "." not in text:
            continue
        # Spans are computed on this file's FIRST finding, not up front:
        # tokenizing every .py file cost ~7 s, and the overwhelming majority
        # have no candidate literal in them at all.
        spans: list[tuple[int, int, int, int, str]] | None = None
        for lineno, line in enumerate(text.split("\n"), 1):
            for m in _NUM.finditer(line):
                lit = m.group(1)
                if _sig_digits(lit) < MIN_SIG_DIGITS:
                    continue
                key = _prefix_key(lit)
                if key is None:
                    continue
                if prefilter is not None and key not in prefilter:
                    continue
                val = mp.mpf(lit)
                exp = key[0]
                # One literal can sit near several table rows that share a
                # value (m_e in MeV is also "natural unit of energy in MeV"
                # and "natural unit of momentum in MeV/c"). Report the
                # alias set once, not three times.
                matched: list = []
                exact = False
                for e in by_exp.get(exp, ()):
                    if e.value == 0:
                        continue
                    # Exact-equality test on the DIGIT STRING, not on mpf:
                    # two mpf built from the same decimal string can differ
                    # in the last bit depending on the working precision at
                    # construction, which reported identical values as
                    # 1e-17-apart near-misses. Trailing zeros are padding,
                    # not disagreement ('3477.23000000' == '3477.23').
                    if _same_number(lit, e.value_str):
                        exact = True
                        break
                    rel = float(abs(val - e.value) / abs(e.value))
                    if rel < args.near:
                        matched.append(e)
                if exact or not matched:
                    continue
                # Report against the NEAREST row only. Rows that merely sit
                # close are different quantities, not synonyms: the
                # electron-muon mag. mom. ratio is within 1e-5 of the
                # muon-electron MASS ratio but is a different constant, and
                # scoring a mass literal against its uncertainty gave a
                # nonsense 282 sigma. Genuine aliases (rows sharing one
                # value, e.g. m_e in MeV = 'natural unit of energy in MeV')
                # are listed together because they are the same number.
                best = min(matched, key=lambda e: abs(val - e.value))
                aliases = sorted(
                    e.quantity for e in matched if e.value_str == best.value_str
                )
                rel_path = str(path.relative_to(REPO))
                if spans is None:
                    spans = (
                        _nonexec_spans_py(path)
                        if path.suffix == ".py"
                        else _nonexec_spans_text(path, text)
                    )
                kind = _classify(spans, lineno, m.start(1))
                if kind == "code" and _adjudicated(line, lit, best.value_str):
                    kind = "adjudicated"
                findings[(lit, " / ".join(aliases), best.value_str)].append(
                    (rel_path, lineno, kind)
                )

    # Rank by number of sites: a value repeated across the corpus is a
    # propagated transcription, which matters more than a one-off.
    ranked = sorted(findings.items(), key=lambda kv: -len(kv[1]))

    total_sites = sum(len(v) for v in findings.values())
    print(f"scanned {files_scanned} files; "
          f"{len(ranked)} distinct near-miss literals across {total_sites} sites")
    print()

    for (lit, quantity, want), sites in ranked:
        rel = float(abs(mp.mpf(lit) - mp.mpf(want)) / mp.mpf(want))
        # Every alias in the group shares one value, so any of them gives the
        # same uncertainty for the sigma figure.
        entry = next(e for e in entries if e.quantity == quantity.split(" / ")[0])
        sigma = ""
        if entry.uncertainty and entry.uncertainty != 0:
            n = float(abs(mp.mpf(lit) - entry.value) / entry.uncertainty)
            sigma = f", {n:.3g} sigma"
        print(f"  {lit}  vs  {want}   [{quantity}]")
        print(f"      {len(sites)} site(s), {rel * 1e9:.4g} ppb{sigma}")
        kinds = Counter(k for _f, _l, k in sites)
        print("      " + ", ".join(f"{n} {k}" for k, n in sorted(kinds.items())))
        if not args.quiet:
            files = sorted({f for f, _, _ in sites})
            for f in files[:6]:
                n_in_file = sum(1 for ff, _, _ in sites if ff == f)
                print(f"        {f}" + (f"  (x{n_in_file})" if n_in_file > 1 else ""))
            if len(files) > 6:
                print(f"        ... and {len(files) - 6} more file(s)")
        print()

    # Three populations, and only one of them can compute anything.
    #
    # A witness or an audit listing RECORDS a number already computed;
    # rewriting it would falsify history. Within source files, a literal in
    # a comment or a docstring is likewise inert -- and is very often the
    # opposite of a defect, because a drain that replaces a stale literal
    # with a registry read and records the superseded value beside it lands
    # exactly there. Only CODE sites gate.
    # ONE definition of "is this a source site", used by both the top-level
    # buckets below and the per-finding counts in the witness. They disagreed:
    # the top-level filtered on suffix first and the per-finding field did
    # not, so a finding reported `code_sites: 292` for a literal whose true
    # executable count was 0, and the per-finding field summed to 1645 against
    # a top-level 0. The gate was never affected -- it reads the top-level --
    # but anything consuming findings[].code_sites read a number that was
    # wrong by its entire magnitude. Caught by noticing the two numbers in the
    # same file could not both be true.
    def _is_source(f: str) -> bool:
        return f.endswith((".py", ".lean", ".ts")) and "/audits/" not in f

    code_sites: list[tuple[str, str, int]] = []
    prose_sites: list[tuple[str, str, int]] = []
    adjudicated_sites: list[tuple[str, str, int]] = []
    record_sites = 0
    for (lit, _q, _w), sites in ranked:
        for f, ln, kind in sites:
            if _is_source(f):
                if kind == "code":
                    code_sites.append((f, lit, ln))
                elif kind == "adjudicated":
                    adjudicated_sites.append((f, lit, ln))
                else:
                    prose_sites.append((f, lit, ln))
            else:
                record_sites += 1
    source_sites = code_sites + prose_sites + adjudicated_sites

    print("=" * 78)
    print(f"CODE sites   (.py/.lean/.ts, executable -- can compute a wrong number) : {len(code_sites)}")
    print(f"PROSE sites  (.py/.lean/.ts, inside a comment or string -- inert)      : {len(prose_sites)}")
    print(f"ADJUDICATED  (executable, but marked reviewed with `noqa: P31`)        : {len(adjudicated_sites)}")
    print(f"RECORD sites (witness/audit/markdown, historical)                      : {record_sites}")
    print("=" * 78)
    print("Only CODE gates. A stale literal quoted in a docstring or recorded in")
    print("a comment beside the registry read that replaced it is provenance, not")
    print("a defect -- counting it as one rewards deleting the provenance.")
    print("Candidates for agent review, NOT a gate by default. A near-miss is the")
    print("signature of a stale edition or a mis-transcription, but this scan")
    print("cannot tell that from a genuinely different quantity that sits nearby.")
    print("Check each against what the surrounding code means before changing it.")
    print("Never rewrite a committed witness to match: it records what a producer")
    print("actually computed. Fix the producer and re-run it.")
    print("=" * 78)

    if not args.no_witness:
        out = REPO / "computations" / "codata-corpus-vintage-scan.witness.json"
        payload = {
            "engine": "python-stdlib",
            "computedAt": datetime.now(timezone.utc).isoformat(),
            "computation": "codata-corpus-vintage-scan",
            "scriptFile": "codata_corpus_literal_scan.py",
            "description": (
                "Numeric literals in the corpus that are NEAR a NIST CODATA-2022 "
                "table value but not equal to it -- the signature of a stale "
                "edition. Sites are split into code_sites (executable, the only "
                "class that can compute a wrong number), prose_sites (inside a "
                "comment or string, inert -- and often the RESULT of a drain "
                "recording what it superseded), adjudicated_sites (executable but "
                "marked reviewed), and record_sites (witness/audit output). Quote "
                "code_sites as the actionable queue, never source_sites, which is "
                "their sum and over-states it ~7x. "
                "Complements codata_truncation_audit.py, which compares "
                "literals against the in-repo codata_constants module and so "
                "catches short prefixes but is structurally blind to a "
                "full-length literal from an earlier CODATA edition. Reference "
                "values are READ from library/allascii.txt, never typed here."
            ),
            "q0Anchor": "not-applicable",
            "q0AnchorReason": (
                "String/lexical scan of source text against the NIST table. No "
                "substrate quantity is evaluated, so no q0 pin is involved."
            ),
            # Serialized as a STRING: a bare float64 in a witness trips the
            # NO-FLOAT64 ratchet, and the fix belongs at the producer rather
            # than in a baseline.
            "near_threshold_relative": repr(args.near),
            "min_significant_digits": MIN_SIG_DIGITS,
            "table_entries": len(entries),
            "files_scanned": files_scanned,
            "distinct_literals": len(ranked),
            "total_sites": total_sites,
            "source_sites": len(source_sites),
            "code_sites": len(code_sites),
            "prose_sites": len(prose_sites),
            "adjudicated_sites": len(adjudicated_sites),
            "record_sites": record_sites,
            "findings": [
                {
                    "literal": lit,
                    "table_value": want,
                    "quantity": quantity,
                    "sites": len(sites),
                    "code_sites": sum(
                        1 for f, _l, k in sites if k == "code" and _is_source(f)
                    ),
                    "prose_sites": sum(
                        1 for f, _l, k in sites
                        if k not in ("code", "adjudicated") and _is_source(f)
                    ),
                    "adjudicated_sites": sum(
                        1 for f, _l, k in sites
                        if k == "adjudicated" and _is_source(f)
                    ),
                    "record_sites": sum(1 for f, _l, _k in sites if not _is_source(f)),
                    "files": sorted({f for f, _, _ in sites}),
                }
                for (lit, quantity, want), sites in ranked
            ],
        }
        # A WITNESS MUST NOT CONTRADICT ITSELF. The per-finding counts are a
        # partition of the same sites the top-level counts partition, so they
        # must sum to it. This invariant is what turns the class of bug fixed
        # above (two counts of one thing, computed by two predicates that
        # drifted apart) from "spotted by eye, once" into "cannot be
        # committed". Checked for every bucket, not just the gating one.
        for _field, _total in (
            ("code_sites", len(code_sites)),
            ("prose_sites", len(prose_sites)),
            ("adjudicated_sites", len(adjudicated_sites)),
            ("record_sites", record_sites),
        ):
            _sum = sum(f[_field] for f in payload["findings"])
            if _sum != _total:
                raise SystemExit(
                    f"internal inconsistency: per-finding {_field} sums to "
                    f"{_sum} but the top-level count is {_total}. The two are "
                    "partitions of the same sites and must agree; fix the "
                    "predicate, do not adjust the number."
                )

        # P30: a raw json.dump emits a witness with NO scriptHash /
        # scriptCommitSha / engineVersion, so run_pipeline.py cannot tell
        # whether it is stale -- the witness is PROV_MISSING. `wrap_legacy`
        # preserves every key above verbatim and adds the staleness fields, so
        # this is a provenance change and not a payload change.
        #
        # Found by scripts/check-sidecars.sh once the same commit that fixed
        # its file-collection made it examine this file at all. It had been
        # reporting "no changed files" on a branch with three commits.
        try:
            from qou_substrate.witness import WitnessBuilder

            WitnessBuilder.wrap_legacy(
                "codata-corpus-vintage-scan",
                payload,
                script_path=__file__,
                engine="python-stdlib",
                output_dir=out.parent,
                start_time=started,
            ).save()
        except ImportError:
            # qou-substrate is not installed in every sandbox, and a scan that
            # cannot import it must still produce its witness rather than
            # crash -- the gate itself runs with --no-witness and is unaffected
            # either way.
            out.write_text(json.dumps(payload, indent=1) + "\n")
            print("  (qou_substrate unavailable — wrote without provenance)")
        print(f"wrote {out.relative_to(REPO)}")

    if args.strict and code_sites:
        print()
        print(f"STRICT: {len(code_sites)} executable site(s) carry a near-miss literal.")
        for f, lit, ln in code_sites:
            print(f"    {f}:{ln}  {lit}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
