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

Run:  python3 -u computations/codata_corpus_literal_scan.py
      python3 -u computations/codata_corpus_literal_scan.py --near 1e-7
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
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


# This scan's own witness lists every literal it found, so scanning it would
# count each finding a second time and grow the total on every re-run. Exclude
# the producer's own output.
# Likewise this finding's own audit note, which quotes each offending literal
# beside its table value in order to report them. An artifact ABOUT the
# finding is not an instance of it -- the same reason
# `hardcoded-literal-audit.witness.json` is a listing rather than a use.
SELF_ARTIFACTS = {
    "codata-corpus-vintage-scan.witness.json",
    "2026-08-19-codata-edition-straddle-corpus-sweep.md",
}


def _iter_files():
    for path in REPO.rglob("*"):
        if not path.is_file() or path.suffix not in SCAN_EXTS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SELF_ARTIFACTS:
            continue
        yield path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--near", type=float, default=1e-5,
                    help="relative distance within which a literal counts as "
                         "'meant to be' a table value (default 1e-5)")
    ap.add_argument("--quiet", action="store_true",
                    help="summary only, no per-site listing")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any near-miss is in a .py/.lean/.ts SOURCE "
                         "file (witness JSON and audit output are records of "
                         "what was computed, not code that computes)")
    ap.add_argument("--no-witness", action="store_true",
                    help="skip writing the witness JSON")
    args = ap.parse_args()

    entries = list(table().values())
    # Index by magnitude so each literal compares against a handful of
    # candidates rather than all 293.
    by_exp: dict[int, list] = defaultdict(list)
    for e in entries:
        if e.value == 0:
            continue
        by_exp[int(mp.floor(mp.log10(abs(e.value))))].append(e)

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
        for lineno, line in enumerate(text.split("\n"), 1):
            for m in _NUM.finditer(line):
                lit = m.group(1)
                if _sig_digits(lit) < MIN_SIG_DIGITS:
                    continue
                val = mp.mpf(lit)
                exp = int(mp.floor(mp.log10(abs(val)))) if val != 0 else 0
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
                findings[(lit, " / ".join(aliases), best.value_str)].append(
                    (rel_path, lineno)
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
        if not args.quiet:
            files = sorted({f for f, _ in sites})
            for f in files[:6]:
                n_in_file = sum(1 for ff, _ in sites if ff == f)
                print(f"        {f}" + (f"  (x{n_in_file})" if n_in_file > 1 else ""))
            if len(files) > 6:
                print(f"        ... and {len(files) - 6} more file(s)")
        print()

    # Sites in SOURCE compute a wrong number; sites in a witness or an audit
    # listing merely record one that was already computed. Rewriting the
    # latter would falsify history, so they are counted separately and never
    # gate.
    source_sites: list[tuple[str, str, int]] = []
    record_sites = 0
    for (lit, _q, _w), sites in ranked:
        for f, ln in sites:
            if f.endswith((".py", ".lean", ".ts")) and "/audits/" not in f:
                source_sites.append((f, lit, ln))
            else:
                record_sites += 1

    print("=" * 78)
    print(f"SOURCE sites (.py/.lean/.ts, compute a wrong number) : {len(source_sites)}")
    print(f"RECORD sites (witness/audit/markdown, historical)    : {record_sites}")
    print("=" * 78)
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
                "edition. Complements codata_truncation_audit.py, which compares "
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
            "record_sites": record_sites,
            "findings": [
                {
                    "literal": lit,
                    "table_value": want,
                    "quantity": quantity,
                    "sites": len(sites),
                    "files": sorted({f for f, _ in sites}),
                }
                for (lit, quantity, want), sites in ranked
            ],
        }
        out.write_text(json.dumps(payload, indent=1) + "\n")
        print(f"wrote {out.relative_to(REPO)}")

    if args.strict and source_sites:
        print()
        print(f"STRICT: {len(source_sites)} source site(s) carry a near-miss literal.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
