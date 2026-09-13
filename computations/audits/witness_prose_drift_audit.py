#!/usr/bin/env python3
"""witness_prose_drift_audit.py — a witness whose PROSE quotes a number its own
DATA does not contain.

Bean `qou-n62l`. Every staleness mechanism here compares a witness against its
PRODUCER — `scriptHash`, `q0Anchor`, the raw-float64 ratchet, the dps floor.
None of them reads a `description`. So a description that hardcodes a finding
keeps asserting it after the data moves underneath, and the witness ends up
contradicting itself in a single file, green the whole time.

MEASURED, not hypothetical. `rho-binding-constancy.witness.json` said

    "the ratio varies ~182% (D 5.73, T 81.5, ³He 37.4)"

while carrying D 3.87 / T 36.99 / ³He 19.12 — and after regeneration under the
corrected atom word (bean qou-hu1f) 14.64 / 291.0 / 131.7. The prose matched
NEITHER the committed data nor the fresh data: it had been stale across at
least two regenerations. Same file also claimed "the D ratio 5.728 reproduces
the published α_M 5.729 (cross-validates the pipeline)", a CLAIM that had
silently stopped holding.

Checking the other witnesses regenerated in that pass found two more, and one
that looked stale and was not:

    delta-lambda-qdim-route-probe          0.41, 5.62, 82.9   worst 33 %
    delta-lambda-cancellation-ascaling     0.28, 1.27, 1.31   worst  8 %
    delta-lambda-l1-ceiling-sign-prune     0.59 vs 0.5661     4 %  ROUNDING

That last one is why this reports distance rather than a boolean: a naive
"is the string present" test flags an honest 3-significant-figure rounding as
loudly as a 49 % contradiction.

METHOD. For each witness with a `description`, pull every decimal number out of
the prose and every number out of the rest of the document, then bucket each
prose number by its distance to the NEAREST data value:

    EXACT      the digits appear verbatim in the data
    ROUNDING   rel < 5e-3   — a quoted 3-4 sig-fig form of a value present
    NEAR       rel < 5e-2   — plausible rounding, or a small genuine drift
    DRIFT      5e-2 .. 0.6  — REPORTED: close enough that it looks like it
                              should match, far enough that it does not
    UNRELATED  rel > 0.6    — a different quantity: an external constant, a
                              tolerance, a count. Not reported.

The upper edge is set FROM the measured cases, not guessed: the three known
drifts sit at 0.058, 0.069, 0.079, 0.33 and 0.55. Everything the first run put
above 0.6 saturated at the cap and ranked identically, which is the signature
of an unrelated quantity rather than a drifted copy.

The band is bounded on BOTH sides deliberately. Ranking by raw relative
distance flags a prose tolerance of `9.0e-18` beside data of order 1e-2 at
5e15 and buries every real finding underneath it. The three measured cases all
land inside: 5.73-vs-3.87 is 0.33, 81.5-vs-36.99 is 0.55, 82.9-vs-55.4 is 0.33.

A decimal point is REQUIRED, which drops years, PR numbers (#1105), bean ids
and issue numbers without needing a list of them. Percent forms are matched
against both `x` and `x/100`, because prose says "~189.6 %" where the data
carries `1.89576`.

⚠ FAR IS A CANDIDATE, NOT A VERDICT. A description may legitimately quote a
number that is not in its own data: a published constant, an AME value, a
figure from a cited bean. `rho-binding`'s own "α_M 5.729" is exactly that — an
external reference — sitting right beside "5.728", a stale claim about a
computed quantity. No static rule separates those two; a reader must. This
audit narrows 4-figure haystacks to a handful of lines to read.

VALIDATED against the four cases whose status was already known:

    delta-lambda-qdim-route-probe          FLAGGED 0.41, 5.62   (known stale)
    delta-lambda-cancellation-ascaling     FLAGGED 0.28, 1.27, 1.31  (known stale)
    delta-lambda-l1-ceiling-sign-prune     clean               (known ROUNDING)
    rho-binding-constancy                  FLAGGED 5.728, 5.729

The last is the limitation demonstrating itself, and is worth reading. That
description was FIXED to interpolate its numbers, and none of its live figures
(189.6, 14.64, 291.0, 131.7) is flagged. What is flagged is the sentence
withdrawing the old claim — "used to claim 'the D ratio 5.728 reproduces the
published α_M 5.729', which no longer holds". Those digits are quoted history
and an external constant, correctly absent from the data. The audit cannot tell
a withdrawn number from a live one, and should not pretend to.

SCOPE. A DETECTOR. The durable fix is not to correct the numbers, which only
resets the clock — it is to make the prose DERIVE them.
`rho_binding_constancy_probe.py` now interpolates its description from the
computed ratios, so it cannot go stale again; that is the pattern.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

import mpmath as mp                                        # noqa: E402
from _precision import fmt, set_compute_dps                # noqa: E402

set_compute_dps()

SKIP_DIRS = ("_deprecated", "__pycache__", "node_modules", ".git")
# A decimal number that is NOT part of an identifier.
#
# The lookbehind drops digits glued to a preceding character -- `A5.4` (a bean
# section), `v1.2`. Label words (`Phase 1.3`, `Step 23.5`) cannot go in the
# same regex: Python's `re` requires a FIXED-WIDTH lookbehind and an
# alternation is not, so they are filtered afterwards by `prose_numbers`.
#
# Both classes came out of reading a 10-witness sample of the findings: 4 of
# the 10 were false positives and these were half. A detector that reports a
# section number as a drifted measurement trains its reader to skim.
NUM = re.compile(r"-?\d+\.\d+(?:[eE][-+]?\d+)?")
# The leading boundary group is load-bearing, not tidiness: without it the
# alternation matches a label word GLUED INSIDE a longer one, and `table`
# lives inside `stable`. Measured on the corpus, the guard changes two prose
# numbers. One is a real loss it recovers -- `...holds a stable -0.00225962
# there`, a measured value silently dropped because "stable" ends in "table".
# The other, `AGMV 4.18`, was being dropped by accident (the `v` of AGMV) and
# is a citation, so it comes back as a candidate; that is the honest trade,
# and the arXiv shape filter does not cover an author-initials + equation-
# number citation of this form.
#
# Written as a CONSUMING group, not a lookbehind. `re` requires a fixed-width
# lookbehind and this alternation is not one -- the same constraint that put
# the label filter outside the number regex in the first place. The 16-char
# window is sized so the longest label ("section") plus its separators still
# leaves the boundary character inside it; a shorter window would let `^`
# match at the cut and re-admit the glued case it exists to stop.
_LABEL_BEFORE = re.compile(
    r"(?:^|[^0-9A-Za-z])"
    r"(?:phase|step|section|item|rule|figure|fig|table|tier|round|part|pr|v)"
    r"[\s.#:-]*$", re.IGNORECASE)
# A SECTION SYMBOL is a label the word list cannot see. `_LABEL_BEFORE` matches
# the word "section"; the prose writes `md § 3.1`, and `§` is neither
# alphanumeric nor a dot, so `3.1` arrived as a measurement. Two witnesses.
_SECTION_SYMBOL = re.compile(r"[\u00a7\u00b6]\s*$")

# An arXiv identifier is shaped exactly like a measurement: `2410.20973`.
# MEASURED over the whole corpus: 32 prose numbers match `YYMM.NNNNN` with a
# plausible year and month, and all 32 are citations -- zero false drops. The
# shape test is what catches them, not a marker: the corpus cites in at least
# four styles (`arXiv:2410.20973`, bare `2509.02354 §5.2`, author-initials
# `GK 1411.6062`, `GGM 2007.10190 eq 20`), and a prefix-based filter sees
# barely half. A real measurement of this exact shape WOULD be dropped; that
# is the accepted cost, and it is the same trade the `Phase 1.3` filter makes.
_ARXIV_SHAPE = re.compile(r"^(\d{2})(\d{2})\.\d{4,5}$")


def _is_arxiv_id(raw: str) -> bool:
    g = _ARXIV_SHAPE.match(raw)
    if not g:
        return False
    yy, mm = int(g.group(1)), int(g.group(2))
    return 7 <= yy <= 26 and 1 <= mm <= 12     # arXiv's YYMM since 2007-04


def prose_numbers(text: str) -> list[str]:
    """Decimal numbers in prose, minus the ones that are labels.

    Filters WHOLE matches rather than constraining the pattern. A lookbehind
    inside the regex looked equivalent and was not: `(?<![0-9A-Za-z.])-?\d...`
    puts the guard before the OPTIONAL SIGN, so where a `-` follows an
    alphanumeric the engine is blocked at the sign and RETRIES at the digit --
    turning `-3.79` into `3.79`. That flips the sign, changes the distance to
    the nearest data value, and INVENTS findings: two witnesses gained
    candidates while the population overall fell, and the ratchet refused the
    rebaseline over it. Deciding to keep or drop the match the plain pattern
    already found has no retry to exploit.

    Dropped: digits glued to a preceding character (`A5.4`, a bean section) and
    digits after a label word (`Phase 1.3`, `Step 23.5`, `Rule 14.2`). Both
    classes came from reading a 10-witness sample of the findings, in which 4
    of 10 were false positives and these were half of them.
    """
    out = []
    for m in NUM.finditer(text):
        before = text[:m.start()]
        if before and (before[-1].isalnum() or before[-1] == "."):
            continue                       # A5.4, v1.2, 3.14.15
        if _LABEL_BEFORE.search(before[-16:]):
            continue                       # Phase 1.3, Step 23.5
        if _SECTION_SYMBOL.search(before[-6:]):
            continue                       # md § 3.1
        if _is_arxiv_id(m.group(0)):
            continue                       # arXiv:2410.20973, GK 1411.6062
        out.append(m.group(0))
    return out


ROUNDING_REL = 5e-3
NEAR_REL = 5e-2
# Above this the prose number is almost certainly a DIFFERENT quantity -- an
# external constant, a tolerance, a count -- not a drifted copy of a data
# value. Ranking by raw relative distance without this cap is useless: a prose
# tolerance of 9.0e-18 beside data of order 1e-2 scores 5e15 and buries every
# real finding. The interesting band is bounded on BOTH sides.
UNRELATED_REL = 0.6

# Schema-level PROVENANCE. Stripped from the document before any number is
# read out of it, because a `description` never quotes the toolchain it ran
# on -- and leaving these in breaks the audit in BOTH directions at once.
#
# MASKING (the worse half). `classify` opens with `if raw in body` -> EXACT,
# a raw SUBSTRING test against the serialised document. `environment` is a
# substring sponge: measured on this corpus,
#
#     python=3.11.15   swallows  3.1
#     numpy=2.4.6      swallows  2.4  AND  4.6
#     clarabel=0.11.1  swallows  0.1
#     pyhecke_native=0.9.0  swallows  0.9
#     sympy=1.14.0     swallows  1.1
#
# so a prose number that happens to be a PREFIX of a dependency version reads
# as "present verbatim in the data" and is suppressed. Five for five on the
# cases checked by hand; 31 findings across the corpus were hidden this way.
#
# MANUFACTURING. The same numbers also enter `data_vals`, a dense grid of
# small decimals sitting exactly where physics values live. 34 prose numbers
# were reported as DRIFT solely because their nearest "data" value was a
# version string -- `binding-hbarq-rung-forward-test`'s 2.961 % scored 0.0503
# against engineVersion `python 3.11.15`, three thousandths inside the DRIFT
# edge, while the prose was CORRECT to 4 significant figures.
#
# Measured 2026-09-13 over 3041 witnesses carrying a description: 34
# manufactured findings drop, 31 masked ones surface. Bean `qou-n62l`.
#
# The list is a BLOCKLIST, not an allowlist, and deliberately so: 819 of those
# witnesses carry a description with no `data` key at all, so "keep only the
# findings" is not a well-defined partition. These 13 keys are named by the
# witness schema and emitted by the writer, never by the author.
#
# Nothing borderline is here. `q0Value`, `q0Anchor`, `dps` and `parameters`
# are all quotable by prose and all stay.
PROVENANCE_KEYS = frozenset({
    "engine", "engineVersion", "environment",          # toolchain versions
    "commitSha", "scriptCommitSha", "scriptHash", "scriptFile",
    "computedAt", "timestamp",                         # clock
    "durationMs", "durationMsBaseline",                # wall time
    "invocation", "schema",
    # precisionMetadata joined the list on the SECOND pass, measured the same
    # day. It holds compute_dps/output_dps/guard_digits/truncation_bound --
    # configuration, the same nature as `environment`, and `guard_digits: 10`
    # turns out to be the widest sponge in the file once the PERCENT branch is
    # taken into account: `classify` tries `prose_num / 100`, so EVERY prose
    # number in roughly [1000, 2500] divides into [10, 25] and lands within
    # 0.6 of 10. That is how an arXiv id (2410.20973 -> 24.10) and the neutron
    # mass quoted from CODATA (939.6 MeV -> 9.396, rel 0.064) were both
    # reported as drifted copies of a guard-digit count.
    #
    # Nothing is lost by dropping it: prose quotes precision as "70 dps" or
    # "120 dps", which carry no decimal point and were never candidates. The
    # audited effect is 9 spurious findings drained and 4 real ones unmasked
    # (they had been reading as NEAR against `guard_digits`).
    "precisionMetadata",
})


def _numbers_in(obj, out=None):
    """Every number anywhere in a JSON document, including numeric strings."""
    out = [] if out is None else out
    if isinstance(obj, bool):
        return out
    if isinstance(obj, (int, float)):
        out.append(float(obj))
    elif isinstance(obj, str):
        for m in NUM.findall(obj):
            try:
                out.append(float(m))
            except ValueError:
                pass
    elif isinstance(obj, dict):
        for v in obj.values():
            _numbers_in(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _numbers_in(v, out)
    return out


def _nearest_rel_mp(raw: str, vals: list[float]):
    """Nearest relative distance, in mpf, from the prose number's own digits.

    The bucketing above runs in float because the band edges (5e-3, 5e-2, 0.6)
    sit nowhere near float64 resolution, so triage is unaffected. The value
    RECORDED is another matter: the raw-float64 gate is right that a float64
    quotient discards digits the source decimal strings actually carried, and a
    witness is not the place to do that (NO-FLOAT64). `mp.mpf(raw)` reads the
    prose digits exactly; `repr` is the shortest round-tripping form of a float
    that arrived as a JSON number, the same conversion `codata_constants`
    uses.
    """
    x = mp.mpf(raw)
    if x == 0:
        return None
    best = None
    for v in vals:
        if v == 0.0:
            continue
        mv = mp.mpf(str(v))
        for cand in (x, x / 100):
            d = abs(mv - cand) / abs(cand)
            if best is None or d < best:
                best = d
    return None if best is None else fmt(best)


def classify(prose_num: float, raw: str, data_vals: list[float], body: str) -> str:
    if raw in body:
        return "EXACT"
    # A ZERO is never a drifted copy of a nonzero result, but witnesses are full
    # of zero counts and flags -- and |0 - x| / |x| is EXACTLY 1.0 for every x,
    # so leaving zeros in makes every prose number in every such witness score
    # 1.0 and saturates the ranking. 225 "candidates" collapsed to a handful
    # once they were dropped.
    data_vals = [v for v in data_vals if v != 0.0]
    if not data_vals:
        return "NO-DATA"
    best = None
    # try the plain value and the percent form: prose says "189.6 %" where the
    # data carries 1.89576
    for cand in (prose_num, prose_num / 100.0):
        for v in data_vals:
            d = abs(v - cand) / max(abs(cand), 1e-300)
            if best is None or d < best:
                best = d
    if best < ROUNDING_REL:
        return "ROUNDING"
    if best < NEAR_REL:
        return "NEAR"
    if best <= UNRELATED_REL:
        return "DRIFT"
    return "UNRELATED"


def scan_witness(doc: dict):
    """-> (findings, reason_skipped). findings = [(raw, bucket, nearest_rel)]"""
    desc = doc.get("description") or doc.get("data", {}).get("description")
    if not isinstance(desc, str) or not desc.strip():
        return [], "no-description"
    rest = {k: v for k, v in doc.items()
            if k != "description" and k not in PROVENANCE_KEYS}
    body = json.dumps(rest)
    vals = _numbers_in(rest)
    out = []
    for raw in dict.fromkeys(prose_numbers(desc)):     # de-dup, keep order
        try:
            x = float(raw)
        except ValueError:
            continue
        b = classify(x, raw, vals, body)
        if b == "DRIFT":
            out.append((raw, b, _nearest_rel_mp(raw, vals)))
    return out, None


# ───────────────────────── PAIRED mode (--pairs), ADVISORY ─────────────────
#
# A SECOND detector over the same corpus, answering a different question, and
# it exists because the one above cannot be made precise.
#
# `classify` asks "is this prose number near ANY number in the document?".
# That has no null model. A witness holds hundreds of values spanning orders
# of magnitude, so for any prose number the chance that SOMETHING lands in a
# [0.05, 0.6] relative window is high -- "close-ish but not exact" is the
# COMMON case under the null, not the surprising one. Measured two ways and
# they agree: a precision-matched random control matched at 53 % against the
# real candidates' 58 %, a lift of +5 pp; and hand-reading 34 NEW/GREW
# findings found 3 genuine, i.e. ~9 % precision. No re-tuning of the band
# edges fixes that, because the statistic is wrong rather than mis-calibrated.
#
# This asks instead: "does the prose NAME a field, and disagree with THAT
# field?" `Reproduces tr_M = 0.160974145442` names tr_M; the witness carries
# tr_M_at_q0. Compare those two and nothing else. No band, no upper cap, no
# coincidence -- and no need for UNRELATED_REL, which is what had hidden the
# largest drift in that very witness (0.160974145442 against data of
# 0.0112374176598, a factor of 14.3).
#
# MEASURED on the corpus: 6 disagreements across 6 witnesses. Hand-read, 3
# are genuine, 2 are candidates needing a domain read, 1 is a marginal
# truncation, and none is clearly wrong. Against ~9 %, on a list short enough
# to read in full.
#
# ADVISORY BY CONSTRUCTION. `--pairs` prints and exits 0; the gate's
# invocation is untouched. A second detector should earn a blocking slot by
# being run, not by being asserted.

# The identifier must be the WHOLE left-hand side of the assignment.
_PAIR_CONNECTOR = r"(?:\s*(?:=|==|≈|~|:|\bis\b|\bof\b|\bat\b|\bwas\b)\s*)"
_PAIR_TOKEN = re.compile(r"([A-Za-z][A-Za-z0-9_]{1,39})" + _PAIR_CONNECTOR + r"$")

# Three guards, each from a measured false positive. Without them the same
# scan reports 16 rather than 6, and 10 of the 16 are this one mistake:
#
#   `1/q_0 = 0.9009182840`         -> 0.90 is 1/q_0, and CORRECT
#   `b3/b2 = 0.64`                 -> 0.64 is the ratio, not b2
#   `max(t)*n_target = 0.146058`   -> a product
#   `m_eta/m_K = 1.109758`         -> a ratio; m_K itself is 493.677 MeV
#   `S_free is 5.5x SMALLER than`  -> a multiplier, not a value
#
_PAIR_OPERATOR_LEAD = "/*+-^("
_PAIR_COMPARATIVE = re.compile(
    r"^\s*[x×]?\s*(?:smaller|larger|bigger|times|fold|short|above|below|"
    r"higher|lower|more|less)\b", re.IGNORECASE)
_PAIR_MULTIPLIER = re.compile(r"\s*(?:[x×]|-?fold)\b", re.IGNORECASE)
# `0.78233341(61)` is concise-uncertainty notation: a MEASURED literature
# constant with its standard error, so a citation rather than this witness's
# own value, however its name collides. Corpus-wide only three prose numbers
# carry it -- PDG `2.16(7)` and the two CODATA Q_beta figures -- and all
# three are citations.
_PAIR_UNCERTAINTY = re.compile(r"\(\d{1,3}\)")

# Suffixes a data key adds that the prose leaves off: tr_M vs tr_M_at_q0.
_PAIR_SUFFIXES = ("atq0", "q0", "deg", "mev", "gev", "kev", "pct", "percent",
                  "ratio", "value", "abs", "sum")


def _pair_norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _pair_key_variants(key: str) -> set:
    """Every name the prose might use for this key, by peeling unit suffixes."""
    out = {_pair_norm(key)}
    changed = True
    while changed:
        changed = False
        for suf in _PAIR_SUFFIXES:
            for v in list(out):
                if v.endswith(suf) and len(v) > len(suf) and v[:-len(suf)] not in out:
                    out.add(v[:-len(suf)])
                    changed = True
    return {v for v in out if len(v) >= 2}


def _pair_leaves(obj, out=None, path=""):
    """Leaf key -> [(numeric value, json path)], numeric strings included."""
    out = {} if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                _pair_leaves(v, out, path + "/" + k)
            elif not isinstance(v, bool):
                val = None
                if isinstance(v, (int, float)):
                    val = float(v)
                elif isinstance(v, str):
                    try:
                        val = float(v)
                    except ValueError:
                        val = None
                if val is not None:
                    out.setdefault(k, []).append((val, path + "/" + k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _pair_leaves(v, out, path + f"[{i}]")
    return out


def _pair_tolerance(raw: str) -> float:
    """Half a unit in the last place the PROSE actually wrote.

    This is the principled form of the ROUNDING bucket. A prose value written
    `0.59` asserts two decimals and nothing more, so 0.5661 is consistent with
    it; one written to twelve decimals asserts twelve, and
    `L_nn = 0.907262271178` against data of 0.907262265533 is a real
    disagreement at the ninth even though the relative distance is 6e-9. A
    fixed relative band cannot express both.
    """
    low = raw.lower()
    if "e" in low:
        mant, _, exp = low.partition("e")
        dec = len(mant.split(".")[1]) if "." in mant else 0
        return 0.5 * 10 ** (-dec + int(exp))
    dec = len(raw.split(".")[1]) if "." in raw else 0
    return 0.5 * 10 ** (-dec)


def scan_witness_pairs(doc: dict):
    """-> [(raw, prose_token, data_key, data_value, json_path, context)]."""
    desc = doc.get("description") or (doc.get("data") or {}).get("description")
    if not isinstance(desc, str) or not desc.strip():
        return []
    rest = {k: v for k, v in doc.items()
            if k != "description" and k not in PROVENANCE_KEYS}
    index = {}
    for key, entries in _pair_leaves(rest).items():
        for variant in _pair_key_variants(key):
            index.setdefault(variant, []).append((key, entries))
    out = []
    for match in NUM.finditer(desc):
        raw = match.group(0)
        before = desc[:match.start()]
        if before and (before[-1].isalnum() or before[-1] == "."):
            continue
        if _LABEL_BEFORE.search(before[-16:]) or _SECTION_SYMBOL.search(before[-6:]):
            continue
        if _is_arxiv_id(raw):
            continue
        window = before[-60:]
        tok = _PAIR_TOKEN.search(window)
        if not tok:
            continue
        if tok.start() > 0 and window[tok.start() - 1] in _PAIR_OPERATOR_LEAD:
            continue
        after = desc[match.end():match.end() + 20]
        if (_PAIR_UNCERTAINTY.match(after) or _PAIR_COMPARATIVE.match(after)
                or _PAIR_MULTIPLIER.match(after)):
            continue
        cands = index.get(_pair_norm(tok.group(1)))
        if not cands or len(cands) != 1:
            continue                       # ambiguous name -> say nothing
        key, entries = cands[0]
        values = {v for v, _ in entries}
        if len(values) != 1:
            continue                       # same key, many values -> ambiguous
        value = next(iter(values))
        if abs(value - float(raw)) > _pair_tolerance(raw):
            ctx = re.sub(r"\s+", " ",
                         desc[max(0, match.start() - 70):match.end() + 30])
            out.append((raw, tok.group(1), key, value, entries[0][1], ctx))
    return out


def _report_pairs(files: list) -> int:
    print("=" * 78)
    print("witness PROSE disagreeing with the field it NAMES  (advisory)")
    print("=" * 78)
    total = 0
    for path in files:
        try:
            doc = json.loads((ROOT / path).read_text())
        except Exception:                                  # noqa: BLE001
            continue
        if not isinstance(doc, dict):
            continue
        hits = scan_witness_pairs(doc)
        if not hits:
            continue
        total += len(hits)
        print(f"\n  {path}")
        for raw, tok, key, value, jpath, ctx in hits:
            print(f"     prose {tok} = {raw}")
            print(f"     data  {key} = {value!r}   ({jpath})")
            print(f"     …{ctx}…")
    print(f"\n  paired disagreements : {total}")
    print("\n  ADVISORY: this mode never fails the build. A prose number is "
          "compared\n  ONLY against the field its own sentence names, to half a "
          "unit in the\n  last place the prose wrote -- so a 2-decimal quote is "
          "held to 2 decimals\n  and a 12-decimal one to 12.")
    return 0


BASELINE = HERE / "witness-prose-drift-baseline.json"


def _load_baseline() -> dict:
    if BASELINE.exists():
        try:
            return json.loads(BASELINE.read_text())["files"]
        except Exception:                              # noqa: BLE001
            return {}
    return {}


def _ratchet(current: dict, strict: bool, rebaseline: bool) -> int:
    """Tolerate the committed backlog, block anything NEW.

    The pattern the gates array already uses (`q0_anchor_ratchet`,
    `never_raises_dps_audit`): blocking is only safe because the gate is GREEN
    at its own baseline, so it can fire on a regression and never on the
    backlog it inherited.

    DO NOT add a file to the baseline to silence a failure. A finding here is a
    name that is not defined; the fix is to define it, or to find out where the
    definition went.
    """
    prior = _load_baseline()
    new_files = sorted(set(current) - set(prior))
    grew = sorted(f for f in current if f in prior and current[f] > prior[f])
    drained = sorted(set(prior) - set(current))
    print(f"\n  baseline files              : {len(prior)}")
    print(f"  drained since baseline      : {len(drained)}")
    print(f"  NEW (not baselined)         : {len(new_files)}")
    print(f"  GREW above baseline         : {len(grew)}")
    for f in new_files:
        print(f"      NEW   {f}  ({current[f]})")
    for f in grew:
        print(f"      GREW  {f}  {prior[f]} -> {current[f]}")
    if rebaseline:
        # Bootstrap: with no baseline on disk every file reads as NEW, so the
        # draining-only guard would refuse to create the very first one.
        if BASELINE.exists() and (new_files or grew):
            print("\n  REFUSED to rebaseline: counts went UP. Rebaselining is for "
                  "DRAINING only -- fix the finding instead of recording it.")
            return 1
        BASELINE.write_text(json.dumps(
            {"files": current, "total": sum(current.values())},
            indent=1, sort_keys=True) + "\n")
        print(f"\n  Rebaselined: {len(current)} file(s), "
              f"{sum(current.values())} finding(s).")
        return 0
    if strict and (new_files or grew):
        return 1
    return 0


def _selftest() -> int:
    cases = [
        ({"description": "the ratio is 5.73", "r": "3.8677"}, ["5.73"],
         "the type case: prose number far from the data it sits beside"),
        ({"description": "the ratio is 3.8677", "r": "3.8677"}, [],
         "EXACT — digits present verbatim"),
        ({"description": "the ratio is 0.59", "r": "0.5661373968"}, [],
         "ROUNDING at 4% is NOT drift — the calibrated false positive"),
        ({"description": "spread ~189.6%", "relative_spread": "1.89576"}, [],
         "PERCENT FORM: prose says 189.6%, data carries 1.89576"),
        ({"description": "see PR #1105 from 2026-08-19", "x": "1.0"}, [],
         "a decimal point is required, so PR ids and dates never enter"),
        ({"description": "tolerance 1e-9 held", "x": "1.0"}, [],
         "no decimal point in 1e-9 either — not a candidate"),
        ({"description": "value 2.2245662", "x": 2.2245662}, [],
         "matches a numeric (non-string) data value"),
        ({"description": "nothing numeric here", "x": "1.0"}, [],
         "no numbers in prose"),
        ({"description": "value 7.5", "note": "no numbers at all"}, [],
         "witness carries no data numbers -> NO-DATA, not a finding"),
        ({"description": "value 7.5", "count": 0, "flag": 0.0}, [],
         "ZEROS DROPPED: |0-x|/|x| is exactly 1.0 for every x, which would "
         "otherwise flag every prose number in every witness holding a zero"),
        ({"description": "A5.4 (bean qou-3yxn) extends it", "x": "1.0"}, [],
         "IDENTIFIER: digits glued to a letter are a section, not a value"),
        ({"description": "Phase 1.3 prototype", "x": "1.0"}, [],
         "LABEL: 'Phase 1.3' is a label, not a measurement"),
        ({"description": "Step 23.5 said otherwise", "x": "1.0"}, [],
         "LABEL: same for Step/Rule/Figure/Table/Item/Section"),
        ({"description": "p -> n holds a stable -0.00225962 there",
          "x": "-0.0021"}, ["-0.00225962"],
         "BOUNDARY: 'table' lives inside 'stable', and without the leading "
         "boundary group this measured value was dropped as a table label"),
        ({"description": "the ratio is 5.73", "r": "3.8677"}, ["5.73"],
         "...and a bare number after ordinary words is still reported"),
        # -------- provenance is not data (both directions, measured) --------
        ({"description": "the coupling is 3.1",
          "environment": {"python": "3.11.15"}, "r": "4.0"}, ["3.1"],
         "UNMASKED: 3.1 is a substring of python 3.11.15, so the EXACT test "
         "used to suppress it; environment is not data"),
        ({"description": "the ratio is 0.9",
          "environment": {"pyhecke_native": "0.9.0"}, "r": "1.4"}, ["0.9"],
         "UNMASKED: same sponge via a dependency version"),
        ({"description": "they differ by 2.961 %",
          "engineVersion": "python 3.11.15", "r": "9.9"}, [],
         "NOT MANUFACTURED: 2.961 vs engineVersion 3.11 scored 0.0503, just "
         "inside the DRIFT edge, while the prose was right to 4 sig figs"),
        ({"description": "duration was 1.5 s",
          "durationMs": 1502.0, "r": "9.9"}, [],
         "wall time is provenance: it moves every run and prose never "
         "quotes it as a finding"),
        ({"description": "the value 2.5 holds",
          "environment": {"numpy": "2.4.6"}, "r": "2.5"}, [],
         "stripping provenance does not break an honest EXACT match in data"),
        ({"description": "CODATA m_n is ~939.6 MeV",
          "precisionMetadata": {"guard_digits": 10}, "r": "0.5"}, [],
         "PERCENT SPONGE: 939.6/100 = 9.396 sits 6 % from guard_digits 10, so "
         "every prose number in ~[1000,2500] used to match a guard count"),
        ({"description": "see the Fantini-Wheeler (arXiv:2410.20973) result",
          "r": "0.5"}, [],
         "arXiv id by shape -- 32 of 32 in the corpus, zero false drops"),
        ({"description": "the GK 1411.6062 eq 2 closed form", "r": "0.5"}, [],
         "...and by shape ALONE, so author-initial citations go too"),
        ({"description": "as md § 3.1 sets out", "r": "0.5"}, [],
         "SECTION SYMBOL: the word list matches 'section', not the glyph"),
        ({"description": "the residual is 3.1", "r": "3.5"}, ["3.1"],
         "...and the same digits after ordinary words are still a finding"),
    ]
    pair_cases = [
        ({"description": "Reproduces tr_M = 0.160974145442 over the stratum",
          "data": {"tr_M_at_q0": 0.0112374176598}}, ["0.160974145442"],
         "the type case: prose NAMES tr_M and the witness carries "
         "tr_M_at_q0, 14.3x away -- invisible to the band detector, which "
         "read it EXACT against a stale source string"),
        ({"description": "Reproduces tr_M = 0.0112374 over the stratum",
          "data": {"tr_M_at_q0": 0.0112374176598}}, [],
         "ULP: a 7-decimal quote is held to 7 decimals and agrees"),
        ({"description": "L_nn = 0.907262271178 per type",
          "data": {"L_nn": 0.907262265533}}, ["0.907262271178"],
         "...and a 12-decimal quote is held to 12, so a 9th-decimal "
         "disagreement IS reported though it is 6e-9 relative"),
        # reference-literal-intentional: a self-test FIXTURE, not a compute
        # path. The case asserts that `1/q_0 = 0.90...` is read as the value
        # of an expression rather than of q_0, so the document under test has
        # to CONTAIN a q0-shaped number. Binding it to q_parameter.Q_MP would
        # make the assertion depend on the live anchor and stop testing the
        # operator guard. Flagged by codata_truncation_audit when the --pairs
        # cases landed 2026-09-13; this is the narrow marker that audit
        # documents for exactly this shape.
        ({"description": "the chirality flip is 1/q_0 = 0.9009182840",
          # reference-literal-intentional: fixture, see the block above
          "data": {"q_0": 1.1099785827513808}}, [],
         "OPERATOR: 0.90 is the value of 1/q_0, and it is correct"),
        ({"description": "Large b3/b2=0.64 so binding is cooperative",
          "data": {"b2": 2.2245662}}, [],
         "OPERATOR: a ratio names its denominator last"),
        ({"description": "the block-level S_free is 5.5× SMALLER than scalar",
          "data": {"S_free": 0.6064289647}}, [],
         "COMPARATIVE: 5.5 is a multiplier, not a value"),
        ({"description": "CODATA gives Q_beta = 0.78233355931(38) here",
          "data": {"Q_beta_MeV": 0.22356166452995638}}, [],
         "UNCERTAINTY: 0.xxx(38) is a cited literature constant with its "
         "standard error, so a citation whose name merely collides"),
        ({"description": "the ratio r = 0.5 holds",
          "data": {"r": 0.5, "nested": {"r": 0.9}}}, [],
         "AMBIGUOUS: one name, two values -> say nothing rather than guess"),
    ]
    bad = 0
    for doc, want, why in cases:
        got = [r for r, _, _ in scan_witness(doc)[0]]
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} want={want!s:10} got={got!s:10}  {why}")
    print("\n  --pairs (advisory second detector):")
    for doc, want, why in pair_cases:
        got = [r for r, _, _, _, _, _ in scan_witness_pairs(doc)]
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} want={want!s:10} got={got!s:10}  {why}")
    total = len(cases) + len(pair_cases)
    print(f"\nselftest: {total - bad}/{total} passed")
    return 1 if bad else 0


def _tracked_witnesses() -> list[str]:
    out = subprocess.run(["git", "ls-files", "*.witness.json"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    return [f for f in out if not any(d in f.split("/") for d in SKIP_DIRS)]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    # BOTH spellings. `scripts/precision-gates.sh` invokes
    # `python3 <script> --self-test` (hyphenated) and treats a non-zero exit as
    # "a detector that cannot be shown to fire is a no-op" -- so a script
    # offering only `--selftest` fails its gate on arrival, silently, for a
    # reason that has nothing to do with what it detects. Found by running the
    # harness rather than by reading the array.
    ap.add_argument("--self-test", "--selftest", action="store_true",
                    dest="selftest")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-witness", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on a NEW candidate, or a baselined witness "
                         "whose count grew (the gates-array ratchet contract)")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (DRAINING only)")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--pairs", action="store_true",
                    help="ADVISORY second detector: compare a prose number "
                         "ONLY against the field its own sentence names, to "
                         "half a unit in the last place the prose wrote. "
                         "Always exits 0; the ratchet is untouched.")
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()

    files = _tracked_witnesses()
    if a.pairs:
        return _report_pairs(files)
    findings, no_desc, unparsed = [], 0, 0
    for f in files:
        try:
            doc = json.loads((ROOT / f).read_text(encoding="utf-8"))
        except Exception:                          # noqa: BLE001
            unparsed += 1
            continue
        if not isinstance(doc, dict):
            unparsed += 1
            continue
        hits, why = scan_witness(doc)
        if why == "no-description":
            no_desc += 1
            continue
        for raw, bucket, rel in hits:
            findings.append({"witness": f, "prose_number": raw,
                             "nearest_relative_distance": rel})

    by_file: dict[str, list] = {}
    for x in findings:
        by_file.setdefault(x["witness"], []).append(x)
    # Rank by HOW MANY prose numbers in one description drift, then by
    # distance. A single stray number is usually an external citation; three or
    # four in one sentence is a finding that was written once and never updated,
    # which is the shape this audit exists to catch.
    def _worst(xs):
        vals = [mp.mpf(y["nearest_relative_distance"]) for y in xs
                if y["nearest_relative_distance"] is not None]
        return max(vals) if vals else mp.mpf(0)

    ranked = sorted(by_file.items(), key=lambda kv: (-len(kv[1]), -_worst(kv[1])))

    if a.json:
        print(json.dumps({"findings": findings, "scanned": len(files),
                          "no_description": no_desc, "unparsed": unparsed},
                         indent=2, default=str))
        return 1 if findings else 0

    print("=" * 78)
    print("witness PROSE quoting a number its own DATA does not contain")
    print("=" * 78)
    print(f"  witnesses scanned           : {len(files)}")
    print(f"  without a description       : {no_desc}")
    print(f"  unparsed                    : {unparsed}")
    print(f"  witnesses with candidates   : {len(by_file)}")
    print(f"  candidate numbers           : {len(findings)}")
    print(f"\n  worst {min(a.top, len(ranked))} by distance"
          f"  (DRIFT is a CANDIDATE, not a verdict — prose may cite an")
    print("   external constant that is legitimately absent from the data):")
    for f, xs in ranked[:a.top]:
        nums = ", ".join(sorted({x["prose_number"] for x in xs}))
        worst = _worst(xs)
        w = f"{mp.nstr(worst, 3)} rel"
        print(f"\n  {f}\n      {nums}\n      worst {w}")
    current = {f: len(v) for f, v in by_file.items()}
    rc = _ratchet(current, a.strict, a.rebaseline)
    if a.rebaseline:
        return rc

    if not a.no_witness:
        from witness_base import WitnessBuilder      # noqa: E402
        w = WitnessBuilder("witness-prose-drift-audit", engine="python")
        w.set_description(
            "Witness descriptions quoting a number the witness's own data does "
            "not contain. No staleness mechanism here reads a description -- "
            "they all compare a witness to its PRODUCER -- so a description "
            "that hardcodes a finding keeps asserting it after the data moves, "
            "and the file contradicts itself while staying green. Measured: "
            "rho-binding-constancy said '~182% (D 5.73, T 81.5, He3 37.4)' "
            "while carrying 3.87/36.99/19.12, matching neither the committed "
            "nor the regenerated data. Buckets by DISTANCE, not presence, so a "
            "4% three-sig-fig rounding is not flagged like a 49% "
            "contradiction. FAR is a candidate, not a verdict: prose may cite "
            "an external constant. Bean qou-n62l.")
        w.add_data("witnesses_scanned", len(files))
        w.add_data("without_description", no_desc)
        w.add_data("witnesses_with_candidates", len(by_file))
        w.add_data("findings", findings)
        w.add_assertion("no witness prose quotes a number absent from its data",
                        computed=len(findings), expected=0)
        w.set_audit_only("computations/audits/witness_prose_drift_audit.py")
        out = w.save()
        print(f"\n[witness] {out}")
    return rc if a.strict else (1 if findings else 0)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
