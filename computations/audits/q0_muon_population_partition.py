#!/usr/bin/env python3
"""Partition the muon-valued q₀ population in computations/.

Why this exists
---------------
`qou-1c4y` has twice carried a headline count of "muon witnesses" that was
produced by grepping a *prefix* of the muon pin.  A 12-digit prefix does not
identify the muon pin: the corpus carries **two** muon values that agree to
11 digits and diverge at the 12th —

    current     1.10997859555733471989...   (live ideal / CAL-2 pin)
    superseded  1.10997859555418057528...   (the "old muon value")

so a prefix grep silently sums two populations with different defects and
different fixes.  This script keeps the split honest and re-runnable.

It is pure string/JSON inspection — no arithmetic — so the NO-FLOAT64
discipline is satisfied vacuously.

Usage
-----
    python3 computations/audits/q0_muon_population_partition.py
    python3 computations/audits/q0_muon_population_partition.py --list-contradictions
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(HERE))
from _source_normalise import code_only  # noqa: E402

# The THREE muon-family values, to enough digits to separate them.
#
#   A  current      1.109978595557334...   the frozen anchor as it stands
#   B  superseded   1.109978595554180...   CODATA 2018
#   C  CODATA 2022  1.109978595642739...   what the 2026-08-22 owner ruling
#                                          re-derives the anchor to (PR #5500)
#
# A and B share 11 digits; C diverges from both at the 10th.  Every prefix
# below is >= 13 significant digits, which is the shortest that separates A
# from B -- a 12-digit prefix silently sums them.
MUON_CURRENT = "1.109978595557334"
MUON_OLD = "1.109978595554180"
MUON_CODATA2022 = "1.109978595642739"
# Loose prefix for the A/B pair.  Deliberately does NOT match C, so the
# historical A/B/both/rounded tally and its TOTAL stay comparable across runs.
MUON_LOOSE = "1.1099785955"
# Loose prefix for the whole muon FAMILY including C.  Still excludes proton
# (1.10997858275...), which diverges one digit earlier.
MUON_FAMILY_LOOSE = "1.10997859"

# 18-SIG-DIGIT CEILING -- do NOT lengthen these prefixes (measured 2026-08-28).
#
# The superseded value has TWO renderings in the corpus, diverging at the 19th
# significant digit:
#
#     1.10997859555418057528...   107 files  (the ROUNDED form -- AGENTS.md,
#                                             bean qou-khac, content .qa.json)
#     1.10997859555418056776...     5 files  (the TRUNCATED form -- d-from-scratch,
#                                             q0-value-drift-audit, 3 deprecated)
#
# |d| ~ 7e-19: three orders below the 3.15e-12 that makes superseded a distinct
# pin at all, and below the 1 ppQ (1e-15) L1 target. It moves no observable --
# it breaks DETECTORS. An exact-match scan built on the 19-char literal
# "1.10997859555418057" reports 0 hits on nine of the nineteen genuine
# candidates, all of which carry the value.
#
# CORRECTED 2026-08-28, twice over. This read "14 digits is the SHORTEST
# prefix that separates superseded from current". Two faults:
#
#   UNIT. That 14 counted CHARACTERS INCLUDING THE DECIMAL POINT --
#   "1.109978595554" is 14 characters but 13 digits. Right boundary,
#   wrong unit.
#
#   CURRENCY. It compared against 1.10997859555733471..., which main's
#   fca08de7d DEMOTED (muon anchor -> CODATA 2022, owner ruling). Three
#   muon renderings are now in play, not two.
#
# Re-derived in SIGNIFICANT DIGITS:
#
#     vs demoted   1.10997859555733471...   12 common -> 13 needed
#     vs canonical 1.10997859564273904...   10 common -> 11 needed
#
# CODATA-2022 moved the anchor at the 11th figure rather than the 13th,
# so the window LOOSENS at the bottom: 11..18 against the canonical pin,
# 13..18 against the demoted one. The 18 ceiling is unchanged -- it comes
# from the superseded value's OWN two renderings diverging at digit 19,
# which is independent of what the current value is. The 16 above sits
# inside both windows, so the count of 19 stands under either reading.

PIN_WITNESS = "q-pinning-50-digit"
ROUTES_ANCHOR = re.compile(
    r"(import\s+q_parameter|from\s+q_parameter"
    r"|qou_substrate.*constants|\bq_at\(|Q_50_DIGIT_STR)"
)
READS_JSON = re.compile(r"(json\.load|read_text|open\()")


def classify_value(text: str) -> str:
    """Which muon-family value does this witness blob CARRY?

    The test is on the whole blob, not on `q0Value`, and that distinction is
    the reason this function exists.  A witness can carry the pin anywhere --
    in a `parameters` block, in an input echo, inside a nested result -- while
    its `q0Value` stamp says something else or is absent entirely.  Counting
    only the stamped ones under-reports the population that a re-pin actually
    moves; see `stamp_vs_value()`.
    """
    cur = MUON_CURRENT in text
    old = MUON_OLD in text
    c22 = MUON_CODATA2022 in text
    hits = [n for n, f in (("A", cur), ("B", old), ("C", c22)) if f]
    if len(hits) > 1:
        return "both"          # cross-anchor comparison, or a straddle
    if hits:
        return {"A": "current", "B": "old", "C": "codata2022"}[hits[0]]
    return "rounded"


def witness_rows() -> list[dict]:
    """One row per witness carrying ANY muon-family value.

    Scans on MUON_FAMILY_LOOSE so C is visible; `in_ab_scan` records whether
    the row would also have been seen by the historical A/B-only prefix, so
    the legacy tally and its TOTAL stay reproducible from the same pass.
    """
    rows = []
    for path in sorted(COMP.rglob("*.witness.json")):
        text = path.read_text(errors="replace")
        if MUON_FAMILY_LOOSE not in text:
            continue
        try:
            doc = json.loads(text)
        except Exception:
            doc = {}
        if not isinstance(doc, dict):
            doc = {}
        rows.append({
            "path": str(path.relative_to(COMP)),
            "value": classify_value(text),
            "stamp": doc.get("q0Anchor"),
            "q0Value": (doc.get("q0Value") or "")[:20] or None,
            "in_ab_scan": MUON_LOOSE in text,
        })
    return rows


def witness_populations(rows: list[dict] | None = None) -> dict:
    """Split every witness carrying a muon-family value by WHICH muon value."""
    rows = witness_rows() if rows is None else rows
    tally = Counter()
    stamp_by_value = Counter()
    for r in rows:
        if not r["in_ab_scan"]:
            continue          # keeps the historical A/B tally comparable
        tally[r["value"]] += 1
        stamp_by_value[(r["stamp"], r["value"])] += 1
    return {"tally": tally, "stamp_by_value": stamp_by_value}


def stamp_vs_value(rows: list[dict]) -> Counter:
    """Cross-tab of the anchor STAMP against the value actually carried.

    The off-diagonal is the point.  A migration scoped by
    `q0Anchor == "muon"` moves only the stamped column; every other cell in
    the A row is a witness that carries the pin and would be left behind.
    """
    return Counter((r["stamp"], r["value"]) for r in rows)


# One-hop transitive path through `_li_2_q_util.load_q_50dps`.
#
# HISTORY, because the right pattern here changed once already.  Until
# 2026-08-22 that helper's signature was `load_q_50dps(path=None)` and a
# `None` path defaulted to the MUON-anchored pin witness -- so the BARE
# no-arg call was the muon route, and a scan that only looked for the
# witness filename inside each producer missed it, undercounting the
# contradictions by 9.
#
# The helper now takes `anchor="proton"` and the bare call resolves to the
# experimental pin.  So the bare form is CORRECT and must NOT be flagged;
# the muon route is now an explicit `anchor="muon"` or an explicit path to
# the pin witness.  A detector keyed on the old shape would report every
# fixed caller as a defect.
_MUON_ANCHOR_ARG = re.compile(
    r"(?<![\w.])load_q_50dps\s*\([^)]*anchor\s*=\s*[\"']muon[\"']"
)
_LOAD_WITH_PIN_PATH = re.compile(
    r"(?<![\w.])load_q_50dps\s*\(\s*[A-Za-z_][\w.]*\s*[,)]"
)


def _uses_muon_via_helper(text: str) -> bool:
    """True if the producer asks `load_q_50dps` for the ideal/muon pin.

    Comment and docstring lines are excluded via `code_only`: a `# Was: load_q_50dps()`
    marker left by an earlier fix records the trap, it is not an instance.
    """
    return bool(_MUON_ANCHOR_ARG.search(code_only(text)))


def _is_direct_pinner_source(text: str) -> bool:
    """True if `text` binds q₀ straight out of the muon-anchored pin witness without routing via `q_parameter`.

    Evaluated on `code_only(text)` so a docstring explaining that the module
    computes at the muon pin *regardless of* `q_parameter` (e.g. `derived_masses.py`)
    does not falsely exempt the module under `ROUTES_ANCHOR`, and a comment
    describing `d["derived_50_digit"]["q"]` in an audit does not falsely indict
    that audit (bean qou-5li4).
    """
    code = code_only(text)
    direct = (
        PIN_WITNESS in code
        and bool(READS_JSON.search(code))
        and bool(re.search(r'derived_50_digit["\']\]', code))
        and bool(re.search(r'\[\s*["\']q["\']\s*\]', code))
    )
    via_helper = _uses_muon_via_helper(code)
    if not (direct or via_helper):
        return False
    if ROUTES_ANCHOR.search(code):
        return False  # resolves its anchor properly in code
    return True


def direct_pinners() -> list[tuple[str, str]]:
    """Producers that bind q₀ straight out of the muon-anchored pin witness.

    A producer here never imports the anchor-resolving module, so it inherits
    whatever anchor that witness carries rather than choosing one.  Returns
    (relative path, manifest bucket).
    """
    manifest = json.loads((COMP / "q0_anchor_manifest.json").read_text())
    bucket = {
        stem: name
        for name in ("ideal_muon", "physical_proton", "ambiguous")
        for stem in manifest.get(name, [])
    }
    out = []
    for path in sorted(COMP.rglob("*.py")):
        if ("_deprecated" in path.parts or "fsh-guts" in path.parts):
            continue
        text = path.read_text(errors="replace")
        if not _is_direct_pinner_source(text):
            continue
        code = code_only(text)
        rel = str(path.relative_to(COMP))
        out.append((rel, bucket.get(path.stem, "UNDECLARED"), classify_intent(text),
                    co_read_fields(code)))
    return out


# Intent signals, searched in COMMENTS AND DOCSTRINGS only.
#
# The CAL-2 trap: a comment saying "CAL-2 q_0" names WHICH CALIBRATION, not
# which pin to evaluate at.  AGENTS.md is explicit that the 2026-08-07
# directive "is about which numerical evaluation code defaults to, not about
# redefining the 3-CAL triple".  Reading a CAL-2 mention as ideal-layer intent
# is the exact conflation the directive prevents -- it was made and retracted
# on this branch, and applying the correction as a rule reclassified 3 of 5
# producers.  So CAL-2 / CAL-1 mentions are deliberately NOT muon signals here.
_PROTON_INTENT = re.compile(
    r"proton[- ]pin|proton anchor|physical[- ]observation|experimental (pin|anchor)", re.I)
_MUON_INTENT = re.compile(
    r"muon[- ]pin|muon anchor|ideal (pin|anchor|layer)", re.I)


def _prose(text: str) -> str:
    """Comments and docstrings only -- intent is stated, not computed."""
    comments = "\n".join(l for l in text.splitlines() if l.strip().startswith("#"))
    docstrings = "\n".join(re.findall(r'"""(.*?)"""', text, re.S))
    return comments + "\n" + docstrings


def classify_intent(text: str) -> str:
    """Which layer does this producer SAY it wants?  Most say nothing."""
    blob = _prose(text)
    proton, muon = bool(_PROTON_INTENT.search(blob)), bool(_MUON_INTENT.search(blob))
    if proton and muon:
        return "both (comparison?)"
    if proton:
        return "proton-intent"
    if muon:
        return "muon-pin intent"
    return "silent on the pin"


# Fields of the pin witness OTHER than the q₀ bind itself.  A producer that
# reads one of these too cannot be migrated by re-pointing only its `["q"]`
# read -- the rest would stay on the muon anchor, straddling two layers inside
# one quantity, which AGENTS.md forbids outright.
_CO_READ_FIELDS = (
    "calibration_inputs", "quantum_integers", "quantum_factorials",
    "plancherel_weights_n3", "physical_anchoring_bound",
    "universal_shape_coupling", "hbar_q", "hbar_q_sq", "q_inv",
    "H_A", "two_q", "z_markov", "s_skein", "Vol_4_1_str",
)


def co_read_fields(text: str) -> list[str]:
    """Which other pin-witness fields does this producer actually READ?

    The test is dict-key use -- a subscript or `.get()` against the loaded
    witness -- NOT the bare field name appearing anywhere in the file.  That
    distinction is the whole point: a substring scan counts local variables
    (`hbar_q_num`, `hbar_q_sym`) and emitted output keys (`hbar_q_50dps`) as
    though they were reads, and it over-reports by 7x.  Measured 2026-08-22:
    substring says 21 producers, dict-key says 3.  The inflated figure reached
    a merged audit doc before it was caught.
    """
    found = []
    for field in _CO_READ_FIELDS:
        quoted = re.escape(field)
        if re.search(r'\[\s*["\']' + quoted + r'["\']\s*\]', text) or \
           re.search(r'\.get\(\s*["\']' + quoted + r'["\']', text):
            found.append(field)
    return found


def _selftest() -> int:
    """Verify docstring mentions of q_parameter do not exempt direct pinners."""
    fails: list[str] = []

    # 1. Synthetic: docstring mentioning Q_50_DIGIT_STR / q_parameter must NOT exempt a direct pinner
    doc_denial = (
        '"""Computes at the muon pin regardless of what q_parameter or Q_50_DIGIT_STR resolves."""\n'
        'import json\n'
        'd = json.load(open("q-pinning-50-digit.witness.json"))\n'
        'q = d["derived_50_digit"]["q"]\n'
    )
    if not _is_direct_pinner_source(doc_denial):
        fails.append("docstring mention of q_parameter falsely exempted a direct pinner")

    # 2. Synthetic: real q_parameter import DOES exempt
    real_routed = (
        'from q_parameter import Q_50_DIGIT_STR\n'
        'import json\n'
        'd = json.load(open("q-pinning-50-digit.witness.json"))\n'
        'q = d["derived_50_digit"]["q"]\n'
    )
    if _is_direct_pinner_source(real_routed):
        fails.append("real q_parameter import was not exempted")

    # 3. Synthetic: comment quoting d["derived_50_digit"]["q"] must NOT count as a direct pinner
    comment_only = (
        '# Always subscripts d["derived_50_digit"]["q"] from q-pinning-50-digit.witness.json\n'
        'import json\n'
        'x = json.load(open("other.json"))\n'
    )
    if _is_direct_pinner_source(comment_only):
        fails.append("comment-only mention of derived_50_digit was counted as a direct pinner")

    # 4. Live tree: derived_masses.py must be present in direct_pinners()
    dm_path = COMP / "derived_masses.py"
    if dm_path.exists() and not _is_direct_pinner_source(dm_path.read_text(errors="replace")):
        fails.append("live derived_masses.py was silently exempted by its docstring")

    for f in fails:
        print(f"  FAIL  {f}")
    print("self-test:", "PASS" if not fails else f"FAIL ({len(fails)})")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", "--selftest", dest="selftest",
                    action="store_true",
                    help="verify prose/code separation on direct_pinners")
    ap.add_argument("--list-contradictions", action="store_true",
                    help="list only the producers declared proton that pin muon")
    ap.add_argument("--list", action="store_true",
                    help="emit the per-witness LIST rather than a count")
    ap.add_argument("--value", choices=("A", "B", "C", "both", "rounded"),
                    help="restrict --list to one value class "
                         "(A=current, B=superseded/CODATA-2018, C=CODATA-2022)")
    ap.add_argument("--stamp", help="restrict --list to one q0Anchor stamp; "
                                    "use 'none' for witnesses carrying no stamp")
    ap.add_argument("--json", action="store_true",
                    help="with --list, emit JSON instead of a table")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    if args.list:
        wanted = {"A": "current", "B": "old", "C": "codata2022",
                  "both": "both", "rounded": "rounded"}.get(args.value)
        rows = witness_rows()
        if wanted:
            rows = [r for r in rows if r["value"] == wanted]
        if args.stamp:
            want = None if args.stamp.lower() == "none" else args.stamp
            rows = [r for r in rows if r["stamp"] == want]
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            for r in rows:
                print(f"{r['value']:<11} {str(r['stamp'] or '-'):<12} {r['path']}")
            print(f"\n{len(rows)} witness(es)")
        return 0

    pins = direct_pinners()
    contradictions = [r for r, b, _, _ in pins if b == "physical_proton"]

    if args.list_contradictions:
        for rel in contradictions:
            print(rel)
        return 1 if contradictions else 0

    all_rows = witness_rows()
    pops = witness_populations(all_rows)
    tally = pops["tally"]
    print("witness populations carrying a muon-family q₀ value")
    print(f"  current  {MUON_CURRENT}…  {tally['current']}")
    print(f"  OLD      {MUON_OLD}…  {tally['old']}   <- superseded pin, stale on its own terms")
    print(f"  both (cross-anchor comparison)          {tally['both']}")
    print(f"  rounded / low-precision                 {tally['rounded']}")
    print(f"  TOTAL matching the loose prefix         {sum(tally.values())}")
    print()
    print("  NOTE: a grep for the 12-digit prefix sums the first two rows and")
    print("        reports one number.  They are different defects.")
    print()
    c22 = [r for r in all_rows if r["value"] == "codata2022"]
    print(f"  CODATA-2022  {MUON_CODATA2022}…  {len(c22)}"
          "   <- the re-pin target (PR #5500)")
    print("    C diverges from A and B at the 10th digit, so the A/B loose")
    print("    prefix above cannot see it and it is counted separately.")
    for r in c22:
        print(f"      {r['path']}")
    print()
    print("stamp x value cross-tab — the OFF-DIAGONAL is the migration's blind spot")
    xt = stamp_vs_value(all_rows)
    stamps = sorted({s for s, _ in xt}, key=lambda x: (x is None, str(x)))
    kinds = ("current", "old", "codata2022", "both", "rounded")
    print(f"    {'stamp':<14}" + "".join(f"{k:>12}" for k in kinds) + f"{'total':>8}")
    for st in stamps:
        cells = [xt[(st, k)] for k in kinds]
        print(f"    {str(st or '(none)'):<14}"
              + "".join(f"{c:>12}" for c in cells) + f"{sum(cells):>8}")
    tot = [sum(xt[(st, k)] for st in stamps) for k in kinds]
    print(f"    {'TOTAL':<14}" + "".join(f"{c:>12}" for c in tot) + f"{sum(tot):>8}")
    print()
    stamped_A = xt[("muon", "current")]
    all_A = sum(xt[(st, "current")] for st in stamps)
    print(f"  A carried by {all_A} witnesses; only {stamped_A} are STAMPED muon.")
    print(f"  A migration scoped by q0Anchor==muon therefore misses "
          f"{all_A - stamped_A}.")
    print()
    print(f"producers binding q₀ direct from {PIN_WITNESS}.witness.json")
    print("  (no anchor resolution — inherits whatever that witness carries)")
    by_bucket = Counter(b for _, b, _, _ in pins)
    for name, count in by_bucket.most_common():
        print(f"  {count:4d}  declared {name}")
    print()
    print("  of the UNDECLARED, what each producer SAYS it wants:")
    by_intent = Counter(i for _, b, i, _ in pins if b == "UNDECLARED")
    for name, count in by_intent.most_common():
        print(f"    {count:4d}  {name}")
    print()
    print("    'silent' means the directive default (proton) already answers it;")
    print("    a 'CAL-2 q_0' mention is NOT a muon signal -- see classify_intent().")
    print()
    co = [(r, f) for r, _, _, f in pins if f]
    print(f"  co-read a SECOND pin-witness field (cannot be re-pointed alone): {len(co)}")
    for rel, fields in co:
        print(f"    {rel}  {fields}")
    print("    (dict-key test, not substring -- see co_read_fields())")
    print()
    if contradictions:
        print(f"CONTRADICTION — declared physical_proton, pins muon: {len(contradictions)}")
        for rel in contradictions:
            print(f"    {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
