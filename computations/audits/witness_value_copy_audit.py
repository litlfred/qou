#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; emits no numeric physics.
"""Catch a script that HARDCODES a value another producer computed.

## The defect

A producer computes a number and records it in its `*.witness.json`. A second
script needs that number and, instead of reading the witness, types it in:

    # binding_probe.py
    TR_M_ATOM = 0.5751234567        # <- copied from atomic-tr-m.witness.json

Two things then go wrong, and the second is the dangerous one:

* **Truncation.** The literal carries fewer digits than the witness did.
* **Staleness.** The producer is re-run, the witness changes, and the copy does
  not. The two silently disagree from then on, with nothing to detect it --
  no gate compares a source literal against a witness.

This is the generalisation of the AME case in `codata_truncation_audit.py`.
There, `8.481798` / `7.718043` / `28.295673` were traced to the *deprecated*
`ame-2020-binding-energies.witness.json` -- a hand-maintained file the registry
says "had drifted", retired as a source of truth, and still being copied from.
That was found by hand. This audit is the general version.

## Why the digit floor is high

Short decimals collide by coincidence: `0.5`, `1.25`, `2.0` appear in every
witness and every script and mean nothing. The floor is deliberately set so
that a match is implausible by chance -- with `MIN_SIG` significant digits a
collision needs the same ~11-digit mantissa to arise twice independently.

Lower it and this audit becomes noise; that is the failure mode it is most
likely to be "improved" into.

## What is NOT a finding

* A literal in the producer's OWN witness. A producer that asserts its own
  expected value is doing a regression check, not copying someone else's
  number. Keyed on the witness's `scriptFile`, not on filename similarity.
* Anything the CODATA/AME audit already owns -- reported there, not twice.
* Values inside a non-constructor string (test fixtures), same rule as the
  sibling audit.

Output: `witness-value-copy-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import ast
import io
import json
import re
import tokenize
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent

#: This audit's own output. Derived, not spelled, so a rename cannot desync it.
OWN_WITNESS = Path(__file__).stem.replace("_", "-") + ".witness.json"
ROOT = HERE.parent.parent
COMP = ROOT / "computations"

# A match needs at least this many significant digits to beat coincidence.
MIN_SIG = 11

NUMBER = re.compile(r"\d+\.\d+")
_NUMERIC_CTORS = {"mpf", "mpmathify", "Decimal", "Fraction", "float",
                  "mpc", "mpi"}


def sig_digits(lit: str) -> int:
    return len(lit.replace(".", "").replace("-", "").lstrip("0"))


def index_witnesses() -> dict[str, set[str]]:
    """decimal literal -> set of witness paths carrying it."""
    idx: dict[str, set[str]] = defaultdict(set)
    for w in COMP.rglob("*.witness.json"):
        if w.name in REPORT_WITNESSES:
            # A detector's report, not a producer's output -- see the block on
            # REPORT_WITNESSES. OWN_WITNESS is in that set; the check below is
            # kept because its comment carries the self-reference measurement.
            continue
        if w.name == OWN_WITNESS:
            # SELF-REFERENCE. This audit writes every literal it reports into
            # its own witness, which is then indexed on the next run -- so the
            # audit became a carrier for all 232 of its own findings, and the
            # contamination ran in BOTH directions:
            #
            #   * 2 findings had NO carrier but this file: once reported, they
            #     re-reported themselves forever. Self-sustaining phantoms.
            #   * every count was inflated by 1, and the NARROW/SHARED cut is
            #     `<= 3`, so literals genuinely carried by 3 witnesses read as
            #     4 and were filed SHARED. Measured: 47 real NARROW findings
            #     were HIDDEN this way (232 -> 277 once excluded).
            #
            # The audit already refuses to scan its own .py (see `scan`); this
            # is the same principle applied to the other half of the loop, and
            # the omission made the gate LOOSER rather than noisier.
            continue
        if ("_deprecated" in w.parts or "fsh-guts" in w.parts):
            # Still indexed: copying from a RETIRED witness is the worst
            # case, not an exempt one. See the AME instance in the docstring.
            pass
        try:
            raw = w.read_text()
        except OSError:
            continue
        for m in NUMBER.finditer(raw):
            lit = m.group(0)
            if sig_digits(lit) >= MIN_SIG:
                idx[lit].add(str(w.relative_to(ROOT)))
    return idx


def own_witnesses(py: Path) -> set[str]:
    """Witness paths this script itself writes (by scriptFile provenance)."""
    out = set()
    for w in COMP.rglob("*.witness.json"):
        try:
            d = json.loads(w.read_text())
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and d.get("scriptFile") == py.name:
            out.add(str(w.relative_to(ROOT)))
    return out


def fixture_lines(src: str) -> set[tuple[int, str]]:
    out: set[tuple[int, str]] = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    protected = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            nm = getattr(n.func, "id", None) or getattr(n.func, "attr", None)
            if nm in _NUMERIC_CTORS:
                for a in ast.walk(n):
                    if isinstance(a, ast.Constant) and isinstance(a.value, str):
                        protected.add(id(a))
    for n in ast.walk(tree):
        if (isinstance(n, ast.Constant) and isinstance(n.value, str)
                and id(n) not in protected):
            for m in NUMBER.finditer(n.value):
                for ln in range(n.lineno, (n.end_lineno or n.lineno) + 1):
                    out.add((ln, m.group(0)))
    return out


# ---------------------------------------------------------------------------
# Intent marker.
#
# The sibling reference-literal gate honours `# reference-literal-intentional:`
# and this one honoured nothing, which left a hand-read verdict with nowhere to
# land: a finding reviewed and found DELIBERATE (a deliberately-frozen historical
# pin, a classifier's own self-test fixture) and a finding nobody has looked at
# yet both ended up in the same baseline bucket, indistinguishable. That is the
# defect AGENTS.md describes for the Lean vacuity ledger -- the machine can
# flag, only an agent can clear, and the clearing has to be recorded somewhere
# the next agent can read.
#
# Per-literal and reason-bearing, deliberately: a blanket per-file opt-out is
# how a gate stops being one.
_INTENT_RE = re.compile(r"witness-copy-intentional:")


def _marker_above(lines: list[str], lineno: int) -> bool:
    """Is the marker anywhere in the contiguous comment block above this line?

    Walking the run rather than checking one line: a reason worth giving takes
    more than one line, so authors write a block and the marker lands at its
    top. The run stops at the first non-comment line, so it cannot reach past
    an intervening statement and stays per-literal.
    """
    i = lineno - 2  # 0-based index of the line directly above
    while i >= 0:
        st = lines[i].strip()
        if not st.startswith("#"):
            return False
        if _INTENT_RE.search(st):
            return True
        i -= 1
    return False


#: Witnesses that are a DETECTOR'S REPORT, not a producer's output.
#:
#: This audit's premise is "a producer computed a number and recorded it; a
#: second script typed it in". An audit's witness TABULATES the literals it
#: found -- `cal4_disguise_hunt` says so in its own docstring, that it hunts
#: "hardcoded high-precision literals (>= 10 digits)". Two detectors agreeing
#: they saw a number is not evidence that a producer computed it, so a report
#: in the carrier set inflates every count it touches.
#:
#: DECLARED rather than pattern-matched, deliberately. A name match on
#: `audit`/`hunt`/`scan` is the shape AGENTS.md's detector-blindness taxonomy is
#: largely a catalogue of, and this audit has contributed two rows to it. The
#: list is validated STRUCTURALLY by `_selftest` -- each entry must exist and
#: must carry file/line beside its literals -- so it cannot rot into a set of
#: names that no longer describe reports.
#:
#: Measured (bean qou-4kc0): excluding these was blocked for a session because
#: it promoted alpha_em, m_e and the proton q0 into "one producer's output,
#: COPIED", which they are not. That was a symptom of the CANON exclusion below
#: never having been implemented; with canonical constants correctly owned by
#: the sibling gate, the 10 remaining promotions are all genuine producer
#: outputs (TAU_P, the extensivity mu targets, VOL_6_1, the Q_beta convention-B
#: value) and the promotion is correct.
#: THREE, not six. My first draft of this list had six, chosen because they
#: were the most frequent carriers -- i.e. pattern-matched on prominence, the
#: exact failure the paragraph above warns against, committed while writing the
#: warning. The structural self-test caught it immediately:
#: deuteron-delta-i-audit, hardcoded-literal-audit and
#: fitted-labelled-canonical-audit are ordinary PRODUCER witnesses carrying
#: `assertions`/`data` (the first even carries LP dual fields), not literal
#: tabulations. Excluding them would have hidden real carriers.
REPORT_WITNESSES = frozenset({
    "witness-value-copy-audit.witness.json",       # this audit
    "cal4-disguise-hunt.witness.json",             # hunts hardcoded literals
    "codata-truncation-audit.witness.json",        # the sibling gate
})


def _canon_owned() -> set[str]:
    """Literals the CODATA/AME gate owns, so this audit does not double-report.

    The module docstring has always promised *"anything the CODATA/AME audit
    already owns -- reported there, not twice"*, and NOTHING implemented it.
    CANON was never imported. So a shared reference constant reached this audit
    on the same footing as one producer's output, and the only thing keeping it
    out of the actionable bucket was the SPREAD heuristic -- "carried by more
    than 3 witnesses, so probably a constant".

    That proxy is what blocked bean qou-4kc0. Removing report witnesses from the
    carrier set drops counts below the `<= 3` cut, and alpha_em, m_e and the
    proton q0 get promoted into "one producer's output, COPIED", which they are
    not. Asking the authoritative question instead of the proxy makes the
    exclusion correct rather than incidental, and it only became precise once
    alpha entered CANON.

    Prefixes are included: a TRUNCATION of a canonical constant is the sibling
    gate's finding, not a witness-copy.
    """
    import sys  # noqa: PLC0415
    if str(COMP) not in sys.path:
        # `_path_bridge` puts substrate/ on the path, not computations/ itself,
        # so a sibling module one directory UP is not importable from here.
        sys.path.insert(0, str(COMP))
    try:
        from codata_truncation_audit import CANON  # noqa: PLC0415
    except Exception as exc:  # pragma: no cover - reported, never silent
        # LOUD, not silent. The first version of this returned an empty set on
        # failure, and the failure duly happened -- ModuleNotFoundError, because
        # computations/ was not on the path -- so the exclusion silently did
        # nothing while the counts looked plausible. A guard that cannot say it
        # is off is the defect this audit exists to catch, one level up.
        print(f"  !! CANON exclusion UNAVAILABLE ({type(exc).__name__}: {exc})")
        print("     Canonical constants will be double-reported here.")
        return set()
    return {canon for canon, _ in CANON.values()}


def _canon_classify():
    """The sibling gate's own classifier, or None if it cannot be imported."""
    import sys  # noqa: PLC0415
    if str(COMP) not in sys.path:
        sys.path.insert(0, str(COMP))
    try:
        from codata_truncation_audit import classify  # noqa: PLC0415
    except Exception:
        return None
    return classify


def _is_canon(lit: str, owned: set[str], classify=None) -> bool:
    """Does this literal belong to the CODATA/AME gate?

    Uses that gate's OWN `classify()` rather than a prefix test here. A prefix
    test under-matches exactly where it matters: `0.51099895000` is not a
    prefix of m_e (`0.51099895069`), it is a DIVERGENT value — the sibling
    gate's most serious verdict — and a prefix-only check would leave it in this
    audit's actionable bucket to be reported twice under the wrong name.

    Falls back to the prefix test only if that import fails, so this audit still
    runs standalone.
    """
    if classify is not None:
        try:
            if classify(lit):
                return True
        except Exception:
            pass
    return any(c == lit or c.startswith(lit) or lit.startswith(c) for c in owned)


def marked_lines(src: str) -> set[int]:
    """Every line covered by a `witness-copy-intentional:` marker.

    A line-only marker (the sibling gate's shape) cannot express the commonest
    deliberate case here, which is a whole TABLE of reference values:

        # witness-copy-intentional: the classifier's own self-test fixtures.
        CASES = [
            ("clean anchor migration", {"x": 0.20906032199559366}, ...),
            ...                                   # 20 literals, 200 lines
        ]

    Marking each literal would need twenty comment lines interleaved through a
    data structure. So a marker above an ASSIGNMENT covers that assignment's
    whole extent -- bounded by the AST, not by a blank-line or indentation
    heuristic, so it stops exactly where the statement stops and cannot leak
    onto the next constant.
    """
    out: set[int] = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    lines = src.splitlines()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        if not _marker_above(lines, node.lineno):
            continue
        end = node.end_lineno or node.lineno
        out.update(range(node.lineno, end + 1))
    return out


def comment_cols(src: str) -> dict[int, int]:
    """line number -> column where that line's trailing comment starts.

    A number inside a comment is PROSE, not a value the program computes, so it
    must not be reported. `line.strip().startswith("#")` already skipped
    whole-line comments and missed TRAILING ones -- measured at exactly 2
    findings, both real false positives:

        _Q0_PREFIX = 14   # muon 1.1099785956..., proton 1.1099785827...
        PHI2_PROTON = sp.Rational(146324616887618, 100000000000000)  # 1.4632...

    Tokenizing rather than searching for `#`: a `#` inside a string literal is
    not a comment, and a regex cannot tell the two apart.
    """
    cols: dict[int, int] = {}
    try:
        toks = tokenize.generate_tokens(io.StringIO(src).readline)
        for tok in toks:
            if tok.type == tokenize.COMMENT:
                row, col = tok.start
                if row not in cols or col < cols[row]:
                    cols[row] = col
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return {}
    return cols


def scan(idx: dict[str, set[str]]) -> list[dict]:
    rows: list[dict] = []
    canon_owned = _canon_owned()
    canon_classify = _canon_classify()
    provenance: dict[str, str] = {}
    for w in COMP.rglob("*.witness.json"):
        try:
            d = json.loads(w.read_text())
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and isinstance(d.get("scriptFile"), str):
            provenance[str(w.relative_to(ROOT))] = d["scriptFile"]

    # SCAN ROOTS. `computations/` alone was a floor, as every report said; the
    # sibling reference-literal gate was extended the same way in #6885.
    #
    # `tests/` is EXCLUDED, and that exclusion is measured rather than assumed.
    # Of 9 NARROW findings outside computations/, 3 are in test files where the
    # literal is the test's OWN assertion target for the precision machinery —
    #     assert str_at_true_precision(v) == "1.5597586581034242"
    # That is the value under test, not a copy of a producer's output that can
    # go stale, so flagging it would be a false positive of exactly the kind
    # this audit's digit floor exists to avoid.
    roots = ["computations", "tools", "qou-mass", "scripts"]
    for f in sorted(g for r in roots
                    for g in ROOT.joinpath(r).rglob("*.py")):
        if ("_deprecated" in f.parts or "fsh-guts" in f.parts) or "__pycache__" in f.parts:
            continue
        if "tests" in f.parts or f.name.startswith("test_"):
            continue
        if f.name == Path(__file__).name:
            continue
        try:
            src = f.read_text()
        except OSError:
            continue
        fx = fixture_lines(src)
        srclines = src.splitlines()
        ccols = comment_cols(src)
        marked = marked_lines(src)
        for i, line in enumerate(srclines, 1):
            st = line.strip()
            if st.startswith("#"):
                continue
            ccol = ccols.get(i)
            for m in NUMBER.finditer(line):
                lit = m.group(0)
                if sig_digits(lit) < MIN_SIG or lit not in idx:
                    continue
                if _is_canon(lit, canon_owned, canon_classify):
                    continue  # the CODATA/AME gate owns it — see _canon_owned
                if (i, lit) in fx:
                    continue
                if ccol is not None and m.start() >= ccol:
                    continue  # inside a trailing comment: prose, not a value
                if i in marked or _marker_above(srclines, i):
                    continue
                carriers = idx[lit]
                # a producer asserting its own recorded value is not copying
                foreign = {w for w in carriers
                           if provenance.get(w) != f.name}
                if not foreign:
                    continue
                # SPREAD is the discriminator between the two things an
                # 11-digit match can mean.
                #
                # A value carried by ONE or a FEW witnesses is one producer's
                # output, and a script holding it has copied it: when that
                # producer is re-run the copy goes stale silently.
                #
                # A value carried by DOZENS is a shared reference constant
                # flowing in as an input -- m_e (0.51099895069) sits in 137
                # witnesses, 1/alpha_em (137.035999084) in 16. Those are not
                # copies of anybody's output, and the CODATA/AME audit already
                # owns them. Reporting them here would double-count the
                # backlog and bury the actionable class under it.
                spread = "NARROW" if len(foreign) <= 3 else "SHARED"
                rows.append({
                    "file": str(f.relative_to(ROOT)),
                    "line": i,
                    "literal": lit,
                    "sig_digits": sig_digits(lit),
                    "spread": spread,
                    "witnesses": sorted(foreign)[:4],
                    "witness_count": len(foreign),
                    "deprecated_source": any(("_deprecated" in w or "fsh-guts" in w)
                                             for w in foreign),
                })
    return rows


def _selftest() -> int:
    """The digit floor must reject coincidence and accept a real copy."""
    cases = [("0.5", False, "a short decimal collides by chance everywhere"),
             ("2.224566", False, "7 digits — below the floor, coincidence"),
             ("0.57512345678", True, "11 digits — implausible by chance")]
    bad = 0
    print("selftest — digit floor")
    for lit, want, why in cases:
        got = sig_digits(lit) >= MIN_SIG
        ok = got == want
        bad += not ok
        print(f"  [{'ok ' if ok else 'FAIL'}] {lit:<16s} "
              f"accepted={got!s:<5s} want={want!s:<5s}  {why}")
    # The marker must cover a marked assignment ENTIRELY and must not leak past
    # its end. Both halves are load-bearing: a marker that stops at line 1 does
    # not express the table case it exists for, and one that runs to the next
    # blank line silently exempts the constant after it.
    fixture = (
        "# witness-copy-intentional: the classifier\'s own self-test inputs.\n"
        "CASES = [\n"
        "    (\'a\', 0.20906032199559366),\n"
        "    (\'b\', 0.10453016099779683),\n"
        "]\n"
        "UNMARKED = 0.57517224391777187\n"
    )
    marks = marked_lines(fixture)
    mcases = [(2, True, "the marked assignment's first line"),
              (3, True, "a literal inside the marked table"),
              (4, True, "the last literal inside the marked table"),
              (6, False, "the NEXT constant — the marker must not leak")]
    print("\nselftest — intent marker extent")
    for ln, want, why in mcases:
        got = ln in marks
        ok = got == want
        bad += not ok
        print(f"  [{'ok ' if ok else 'FAIL'}] line {ln}  "
              f"marked={got!s:<5s} want={want!s:<5s}  {why}")

    # The self-reference exclusion must actually name this audit's own witness.
    # Derived from __file__ rather than spelled, so it cannot desync on a
    # rename -- but a change to the naming convention would, so it is pinned.
    ok = OWN_WITNESS == "witness-value-copy-audit.witness.json"
    bad += not ok
    print("\nselftest — self-reference exclusion")
    print(f"  [{'ok ' if ok else 'FAIL'}] OWN_WITNESS = {OWN_WITNESS!r}")
    ok2 = OWN_WITNESS not in {w for w in ()} and OWN_WITNESS.endswith(".witness.json")
    bad += not ok2
    print(f"  [{'ok ' if ok2 else 'FAIL'}] names a witness file")

    # The REPORT_WITNESSES list must be CHECKED, not trusted. A declared list
    # is auditable but rots; this is the structural half of the recommendation
    # in qou-4kc0 — each entry must still exist and must still look like a
    # report, i.e. carry file/line beside its literals. If one stops being a
    # report, excluding it silently hides real carriers.
    print("\nselftest — REPORT_WITNESSES are still reports")
    for name in sorted(REPORT_WITNESSES):
        hits = list(COMP.rglob(name))
        if not hits:
            # Absent is not a failure: an audit may not have run in this
            # container. It IS worth saying, because an excluded name that
            # matches nothing is silently doing nothing.
            print(f"  [--  ] {name:46s} absent here (exclusion inert)")
            continue
        try:
            d = json.loads(hits[0].read_text())
        except (OSError, ValueError):
            print(f"  [FAIL] {name:46s} unreadable")
            bad += 1
            continue
        blob = json.dumps(d)
        looks_like_report = '"file"' in blob and '"line"' in blob
        bad += not looks_like_report
        print(f"  [{'ok  ' if looks_like_report else 'FAIL'}] {name:46s} "
              f"{'carries file/line beside its literals' if looks_like_report else 'NOT a report — remove it'}")

    # A number inside a TRAILING comment is prose, not a value.
    cc = comment_cols("X = 14   # muon 1.1099785956..., proton 1.1099785827\n")
    ok = cc.get(1) == 9
    bad += not ok
    print("\nselftest — trailing comment")
    print(f"  [{'ok ' if ok else 'FAIL'}] comment starts at col {cc.get(1)}, "
          "want 9")

    if bad:
        print("\nSELFTEST FAILED — the floor no longer separates a real copy "
              "from a coincidence, or the marker no longer bounds itself; "
              "findings are not trustworthy.")
        return 1
    print(f"\nselftest ok — floor is {MIN_SIG} significant digits; "
          "marker is AST-bounded")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--self-test", "--selftest", dest="selftest",
                    action="store_true")
    ap.add_argument("--baseline", action="store_true",
                    help="ratchet: exit 1 only on NARROW copies absent from "
                         "the baseline (blocks NEW copies)")
    ap.add_argument("--write-baseline", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()

    idx = index_witnesses()
    rows = scan(idx)
    narrow = [r for r in rows if r["spread"] == "NARROW"]
    dep = [r for r in narrow if r["deprecated_source"]]

    out = HERE.parent / "witness-value-copy-audit.witness.json"
    out.write_text(json.dumps({
        "engine": "python-stdlib",
        "computation": "witness-value-copy-audit",
        "scriptFile": Path(__file__).name,
        "description": (
            "Source literals of >= %d significant digits that also appear in "
            "a *.witness.json the script does not itself produce — a value "
            "copied instead of loaded. Such a copy goes stale silently when "
            "the producer is re-run." % MIN_SIG),
        "min_sig_digits": MIN_SIG,
        "indexed_literals": len(idx),
        "total": len(rows),
        "narrow_total": len(narrow),
        "narrow_files": len({r["file"] for r in narrow}),
        "shared_total": len(rows) - len(narrow),
        "files": len({r["file"] for r in rows}),
        "from_deprecated_witness": len(dep),
        "findings": rows,
    }, indent=2) + "\n")

    print("=" * 74)
    print("WITNESS-VALUE COPY AUDIT — a computed value typed in, not read")
    print("=" * 74)
    print(f"  indexed witness literals (>= {MIN_SIG} sig digits): {len(idx)}")
    print(f"  NARROW (<=3 witnesses — one producer's output, COPIED): "
          f"{len(narrow)} in {len({r['file'] for r in narrow})} file(s)")
    print(f"  SHARED (>3 — a reference constant; the CODATA/AME audit owns "
          f"these): {len(rows) - len(narrow)}")
    print(f"  of the NARROW, copied from a _deprecated/ witness: {len(dep)}")
    for r in (narrow if a.list else narrow[:20]):
        src = r["witnesses"][0]
        print(f"    {r['file']}:{r['line']}  {r['literal']}")
        print(f"        also in {src}"
              + (f" (+{r['witness_count'] - 1} more)"
                 if r["witness_count"] > 1 else ""))
    if not a.list and len(narrow) > 20:
        print(f"    ... and {len(narrow) - 20} more (--list)")
    print(f"\n  witness -> {out.name}")
    # Ratchet on NARROW only, keyed on (file, literal) -> count. Never on the
    # line number: an edit anywhere above a finding shifts it, and a ratchet
    # that cries wolf on every edit is one people re-baseline past.
    #
    # BLOCKING ON NEW, NOT ON THE BACKLOG, and deliberately so. Some of the
    # 264 existing NARROW copies are DELIBERATE freezes -- see
    # alpha_em_nonD_index_route_probe.py, whose header says "frozen from the
    # merged falsifications". Separating deliberate from accidental needs a
    # hand pass, and an attempt to automate it here (scan nearby comments for
    # "frozen"/"copied") got that very file WRONG, because its note sits six
    # lines above the value and the window was four. That split is not
    # shipped. Until the backlog is triaged the honest gate is: no NEW copies.
    bl = HERE.parent / "witness-value-copy-baseline.json"
    key = lambda r: f"{r['file']}::{r['literal']}"  # noqa: E731
    if a.write_baseline:
        counts: dict[str, int] = {}
        for r in narrow:
            counts[key(r)] = counts.get(key(r), 0) + 1
        bl.write_text(json.dumps(
            {"_comment": "Pre-existing NARROW witness-value copies, as "
                         "<file>::<literal> -> count. DRAINS, never grows. "
                         "Some entries are deliberate freezes and need a hand "
                         "pass; none may be added to silence a new copy.",
             "counts": dict(sorted(counts.items()))}, indent=2) + "\n")
        print(f"\nbaseline written: {len(counts)} entries -> {bl.name}")
        return 0
    if a.baseline:
        try:
            known = json.loads(bl.read_text())["counts"]
        except (OSError, ValueError, KeyError):
            known = {}
        seen: dict[str, int] = {}
        fresh = []
        for r in narrow:
            k = key(r)
            seen[k] = seen.get(k, 0) + 1
            if seen[k] > known.get(k, 0):
                fresh.append(r)
        print(f"\n  RATCHET: {sum(known.values())} baselined, "
              f"{len(fresh)} NEW")
        if fresh:
            print("  NEW copies — read the witness instead of typing the "
                  "value; do NOT baseline:")
            for r in fresh[:20]:
                print(f"    {r['file']}:{r['line']}  {r['literal']}"
                      f"  (in {r['witnesses'][0]})")
            return 1
        return 0

    if a.strict and narrow:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
