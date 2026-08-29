#!/usr/bin/env python3
"""Which substrate anchor did each witness actually use?

AGENTS.md (owner directive, 2026-08-07) requires every new witness to record
its q₀, so a later reader can tell which layer it belongs to without inferring
it from a call site. This measures whether that is happening, and classifies
what was recorded.

It exists because the `tnjb` migration ("move the ~840 muon-q₀ witnesses to
proton") has been discussed as a bulk sweep without anyone measuring its actual
shape. A sweep you cannot count is a sweep you cannot scope.

CLASSIFICATION IS BY PHYSICAL DISTANCE, NOT STRING EQUALITY
-----------------------------------------------------------
An earlier pass of mine classified by exact float match against the f64 pin
literals and put ~350 files in an "other" bucket. That was wrong: most of them
record the muon pin at *higher* precision (a 50-dps string), which is the same
anchor, not a different one. Distance-based bucketing avoids that whole class
of error, and it is also the only framing in which the answer is meaningful —
what matters is which anchor a number sits on, not how many digits were typed.

Buckets, by |q − q_proton| / q_proton:

    proton     < 1 ppb        the production default
    muon      ~11.5 ppb       the ideal-layer CAL-2 proxy
    truncated ~1277 ppb       the 5-significant-digit `1.10998` literal
    other      anything else  neither pin — needs a human look

Usage:
    python3 computations/q0_provenance_audit.py
    python3 computations/q0_provenance_audit.py --list-other
"""
from __future__ import annotations

import argparse
import collections
import decimal
import json
import pathlib
import re
import sys

Q_PROTON = 1.1099785827513808
Q_MUON = 1.1099785955541805

# Canonical 50-dps muon q0, DERIVED not typed: `q_muon_at(60)` from CODATA
# m_mu/m_e = 206.7682830 and Vol(4_1) = 2*Cl_2(pi/3) reproduces exactly this.
# Owner ruling 2026-08-15: the muon string is the correct one, and CODATA +
# the corpus formula determine it.
Q_MUON_50 = "1.10997859555418057528159407960950937799328227995870"

# A NON-REPRODUCIBLE 50-dps muon string, carried by 243 witnesses. It agrees
# with the canonical value to 12 digits, then diverges by 2.842e-12 RELATIVE
# (3.154e-12 absolute -- the two are quoted interchangeably elsewhere and are
# not the same number; the comparisons below are all relative).
#
# CALIBRATE THIS BEFORE QUOTING IT. An earlier version of this comment (mine)
# called the trailing digits "38 digits of noise" and compared the gap to the
# L1 1 ppQ compute goal, making it sound like an accuracy defect. That was an
# OVERCLAIM, and the correction matters:
#
#   CODATA m_mu/m_e = 206.7682830 +/- 4.6e-6  ->  2.2e-8 relative, ~7 sig figs
#   propagated to q_muon                      ->  1.22e-9 relative, ~8 sig figs
#   A-vs-B gap                                ->  2.84e-12
#
# The gap is 431x SMALLER than the experimental uncertainty on q_muon itself.
# So BOTH strings are physically meaningless past ~digit 8 — the canonical one
# is not "more accurate", and no derived physical quantity changes by choosing
# between them.
#
# What is genuinely wrong with this string is REPRODUCIBILITY, not accuracy:
# it cannot be regenerated from the stated inputs. `q_muon_at(60)` — a closed
# form, q = 1/(1 - sqrt(Vol(4_1)/(m_mu/m_e))), reading only CODATA and an
# exactly-computed Vol — yields the canonical string and not this one. A
# 50-dps constant earns its digits by being *deterministically recomputable*
# (the L1 compute-agreement goal), which is a different property from being
# physically accurate to 50 places. This one is not recomputable, so it
# cannot be checked, which is the defect.
Q_MUON_50_WRONG = "1.10997859555733471989976322048322502665620840878015"

# Keys that name a substrate anchor. Deliberately narrow: `q` alone is also
# used for unrelated quantities, so a value only counts when it also lands in
# the q₀ neighbourhood (see `classify`).
# Substrate-anchor key names, as a PATTERN rather than a literal set.
#
# Two earlier revisions of this file used a hardcoded set and undercounted
# twice: first by omitting the camelCase `q0Value`/`q0Anchor` that
# `stamp_staleness_metadata` actually writes, then by omitting `q_0_50dps`,
# `q0_proton`, `q_0_numeric` and ~16 others — ~179 witnesses reported as
# "NOT RECORDED" that do record an anchor. Extending the list a third time
# would just move the miss.
#
# The pattern is deliberately paired with the q0-neighbourhood test in
# `classify`, and BOTH must hold. Neither is sufficient alone, which the
# corpus shows plainly: the single commonest key holding a value in that
# range is the generic `value` (1801 occurrences), and `frobenius_norm`,
# `chi_lambda`, `miss_x` all land there too. Name-matching alone over-matches;
# range-matching alone over-matches harder.
_Q_NAME = re.compile(
    r"""(?ix)
    ^(
        q_?0                # q0, q_0, q0Value, q0_50dps, q_0_numeric, ...
          [a-z0-9_]*
      | q                   # bare q, and q_proton / q_muon / q_50dps
          (_(proton|muon|parameter|pinned|used|value)
           |_?\d*dps)?
      | (substrate|muon|proton)_q_?0[a-z0-9_]*
    )$
    # DELIBERATELY NOT matched: `*_at_q0` / `*_at_q_0`. That suffix means
    # "evaluated AT q0", so the key names the OTHER quantity -- tr_M_at_q0,
    # chi_lambda_at_q0, jones_at_q0, z_at_q0, one_plus_q_over_2_at_q0. An
    # earlier draft of this pattern included that arm and swept up ~90 such
    # keys as anchors, purely because a Markov trace or character happens to
    # land in the same numeric window as q0. Range-matching cannot separate
    # them; only the name can, and the name says they are not anchors.
    """,
)


def is_anchor_key(name: str) -> bool:
    """True if `name` names a substrate anchor (pattern half of the test)."""
    return bool(_Q_NAME.match(name))


# The canonical provenance pair, reported separately from raw q0 VALUES: a
# witness can carry a q0 number without the anchor label, and vice versa, and
# only the label survives a re-anchoring unambiguously.
CANONICAL_FIELDS = ("q0Anchor", "q0Value")

# Distance thresholds in ppb from the proton pin.
PROTON_PPB = 1.0
MUON_PPB_LO, MUON_PPB_HI = 5.0, 30.0
TRUNC_PPB_LO, TRUNC_PPB_HI = 1000.0, 1600.0


def classify(value) -> tuple[str, float] | None:
    """Bucket a recorded value, or None if it is not a substrate anchor."""
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    # Only values in the q₀ neighbourhood count — this is what keeps a bare
    # `q` key holding an unrelated number out of the census.
    if not (1.05 < f < 1.20):
        return None
    ppb = abs(f - Q_PROTON) / Q_PROTON * 1e9
    if ppb < PROTON_PPB:
        return "proton", ppb
    if MUON_PPB_LO <= ppb <= MUON_PPB_HI:
        return "muon", ppb
    if TRUNC_PPB_LO <= ppb <= TRUNC_PPB_HI:
        return "truncated-5-digit", ppb
    return "other", ppb


def _sig_digits(s: str) -> int:
    """Decimal digits a string CLAIMS -- trailing zeros included.

    This is the "how much precision is being asserted" count, and it is what
    the false-precision gate keys on: `1.10997859555733470000000000` claims
    28 digits while backing 17, and that padding is precisely the defect.
    """
    return len(s.replace(".", "").replace("-", "").lstrip("0"))


def _backed_digits(s: str) -> int:
    """Decimal digits a string can BACK UP -- trailing zeros stripped.

    The counterpart to `_sig_digits`, and the one that sets a comparison
    tolerance. A trailing zero is the one digit that may be padding rather
    than measurement, so it cannot be held against the other operand.

    The distinction is not academic: `Q_MUON_50` itself ends in a padding
    zero (its 51st digit; the true value continues ...58686...). Counting
    that zero made the tolerance 10x too tight and pushed 13 witnesses
    carrying the canonical value at 60 digits into "origin unknown", missing
    by a factor of 1.24.
    """
    return len(s.replace(".", "").replace("-", "").strip("0"))


def _agrees_to_stated_precision(raw: str, known: str) -> bool:
    """Do two decimal strings name the same number, to the precision claimed?

    The tolerance is one unit in the last place of whichever string carries
    FEWER significant digits: a value written to 20 digits cannot be held to
    a 50-digit standard, and a 50-digit value compared against a 20-digit one
    is only being asked about its first 20.

    This is what makes the check immune to the round-vs-truncate difference
    that broke the previous string-prefix version -- a rounded last digit is
    half an ulp away, well inside one ulp, while a genuinely different
    constant diverges at digit 17 or earlier and is many orders outside it.
    """
    with decimal.localcontext() as ctx:
        ctx.prec = max(len(raw), len(known)) + 10
        try:
            a, b = decimal.Decimal(raw), decimal.Decimal(known)
        except decimal.InvalidOperation:
            return False
        if not b:
            return False
        m = min(_backed_digits(raw), _backed_digits(known))
        return abs(a - b) / abs(b) <= decimal.Decimal(10) ** (1 - m)


def false_precision(raw) -> str | None:
    """Detect a q0 string claiming MORE precision than it carries.

    Returns a description, or None if the value is fine.

    REWRITTEN 2026-08-15, twice, after review. Both earlier versions compared
    STRINGS, and string comparison is the wrong instrument here. The failures,
    in the order they were found:

    1. `repr(float)` emits **17** significant digits, so ordinary f64
       renderings tripped a `>16` test; and being 18 characters they could
       never match a fixed 20-character prefix, so they were structurally
       unable to clear. 79 files carrying the CANONICAL value at f64
       precision were reported as "origin UNKNOWN, no investigation".

    2. Widening the comparison to the full overlap fixed that and broke the
       other end: a serializer that ROUNDS its last digit rather than
       truncating produces `...0878015` -> `...087802`, which shares no
       prefix past the rounded digit. 145 witnesses carrying the known stale
       constant at 50 digits, plus ~80 more carrying the canonical one, were
       moved into "origin genuinely unknown" -- the bucket went UP, which is
       how the defect was caught.

    Both are the same mistake: the question is whether two DECIMALS agree to
    the precision the shorter one claims, and that is arithmetic, not text.
    So compare numerically, with the tolerance set by whichever of the two
    strings offers fewer significant digits -- one unit in its last place.
    Decimal, not float: the whole point is digits past f64's 17.
    """
    if not isinstance(raw, str):
        return None
    digits = raw.replace(".", "").replace("-", "").lstrip("0")
    # f64 round-trips at 17 significant digits. At or below that, the string
    # is a legitimate f64 rendering and asserts nothing it cannot back up --
    # whatever value it holds is a question for the anchor buckets, not here.
    if len(digits) <= 17:
        return None
    try:
        v = float(raw)
    except ValueError:
        return None
    if abs(v - Q_MUON) / Q_MUON > 1e-9:
        return None  # not a muon-pin value; out of scope for this check

    if _agrees_to_stated_precision(raw, Q_MUON_50):
        return None  # canonical, at whatever precision it was written
    if _agrees_to_stated_precision(raw, Q_MUON_50_WRONG):
        return (f"{len(digits)}-digit muon string that q_muon_at() does not "
                f"reproduce (diverges at digit 13) -- not recomputable from "
                f"the stated inputs")
    return (f"{len(digits)}-digit muon string matching NEITHER the canonical "
            f"value nor the known stale one -- origin genuinely unknown")


def anchors_in(doc) -> list[tuple[str, object, str, float]]:
    """Every substrate anchor recorded anywhere in a witness."""
    found: list[tuple[str, object, str, float]] = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if is_anchor_key(k):
                    hit = classify(v)
                    if hit:
                        found.append((k, v, hit[0], hit[1]))
                    fp = false_precision(v)
                    if fp:
                        # Keep the two classes DISTINCT. Collapsing them to a
                        # single "FALSE-PRECISION" label made the report
                        # attribute every flagged file to the known stale
                        # string and print that string verbatim -- wrong for
                        # ~96 files carrying some OTHER non-canonical value,
                        # which need a different investigation (the stale one
                        # has a known origin; these do not).
                        kind = ("FP-known-stale" if "does not reproduce" in fp
                                else "FP-unknown")
                        found.append((k, v, kind, 0.0))
                walk(v)
        elif isinstance(o, list):
            for i in o:
                walk(i)

    walk(doc)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--list-other", action="store_true",
                    help="print every file in the 'other' bucket")
    ap.add_argument("--list-truncated", action="store_true",
                    help="print every file on the 5-digit truncated anchor")
    ap.add_argument("--json", action="store_true",
                    help="emit the census as JSON and nothing else")
    args = ap.parse_args()

    buckets = collections.Counter()
    canonical = collections.Counter()
    mixed = []
    per_bucket_files = collections.defaultdict(list)
    total = 0
    unreadable = 0

    for p in sorted(pathlib.Path(args.root).rglob("*.witness.json")):
        if ".git" in str(p):
            continue
        total += 1
        try:
            doc = json.loads(p.read_text())
        except Exception:
            unreadable += 1
            continue
        canonical[("q0Anchor" in doc, "q0Value" in doc)] += 1
        hits = anchors_in(doc)
        if not hits:
            buckets["NOT RECORDED"] += 1
            continue
        kinds = {h[2] for h in hits}
        for k in kinds:
            buckets[k] += 1
            per_bucket_files[k].append(str(p))
        # FALSE-PRECISION is a QUALITY flag, not an anchor. It must not enter
        # the straddle test: a file recording the muon pin plus a
        # false-precision rendering of that same pin is one anchor with a
        # serialization defect, not two anchors. (Including it inflated the
        # straddle count 18 -> 257 in an earlier revision of this script.)
        kinds = kinds - {"FP-known-stale", "FP-unknown"}
        # A single witness carrying TWO different anchors MAY be the
        # layer-straddle AGENTS.md calls a defect regardless of size. It may
        # equally be correct by construction: a q-sweep or a pin-sensitivity
        # map has to carry both (`mu-p-pin-sensitivity-map` is exactly that).
        # So this is a high-recall CANDIDATE list for agent triage, not a
        # defect list — the tool flags, a human or agent adjudicates.
        if len(kinds) > 1:
            mixed.append((str(p), sorted(kinds)))

    rec = total - buckets["NOT RECORDED"] - unreadable

    if args.json:
        # One machine-readable output, so a count is quoted from a run rather
        # than hand-copied. Three mutually-contradictory generations of these
        # numbers were live at once across two beans and this script -- each
        # correct when written, none marked superseded, and the differences
        # were caused by fixes to the key pattern rather than by the corpus
        # moving. Anything that cites a count should cite this.
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload = {
            "scanned": total,
            "unreadable": unreadable,
            "records_an_anchor": rec,
            "records_none": buckets["NOT RECORDED"],
            "canonical_pair": {
                "both": canonical[(True, True)],
                "anchor_only": canonical[(True, False)],
                "neither": (canonical[(False, False)]
                            + canonical[(False, True)]),
            },
            "anchor_buckets": {
                k: buckets[k]
                for k in ("proton", "muon", "truncated-5-digit", "other")
            },
            "false_precision": {
                "known_stale": buckets["FP-known-stale"],
                "unknown": buckets["FP-unknown"],
            },
            "multi_anchor_candidates": len(mixed),
        }
        _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(_prov_payload, sys.stdout, indent=2)
        print()
        return 0

    print(f"  witnesses scanned  : {total}")
    if unreadable:
        print(f"  unreadable         : {unreadable}")
    print(f"  record an anchor   : {rec}  ({rec / total * 100:.1f}%)")
    print(f"  record NONE        : {buckets['NOT RECORDED']}  "
          f"({buckets['NOT RECORDED'] / total * 100:.1f}%)  "
          f"<- AGENTS.md requires new witnesses to record q0")
    print()
    both = canonical[(True, True)]
    anchor_only = canonical[(True, False)]
    neither = canonical[(False, False)] + canonical[(False, True)]
    print("  CANONICAL provenance pair (q0Anchor / q0Value), written by")
    print("  stamp_staleness_metadata and auto-stamped by build():")
    print(f"    {both:5d}  both fields")
    print(f"    {anchor_only:5d}  q0Anchor only")
    print(f"    {neither:5d}  NEITHER  ({neither / total * 100:.1f}%)  "
          f"<- the real provenance gap")
    print()
    for name in ("proton", "muon", "truncated-5-digit", "other"):
        if buckets[name]:
            print(f"  {buckets[name]:5d}  {name}")

    n_stale = buckets["FP-known-stale"]
    n_unknown = buckets["FP-unknown"]
    if n_stale or n_unknown:
        print()
        print(f"  ** {n_stale + n_unknown} witness(es) carry a 50-dps muon q0 "
              f"that q_muon_at() does not reproduce.")
        print("     Two DIFFERENT defects, reported separately because they "
              "need different work:")
        print()
        print(f"     {n_stale:5d}  the KNOWN stale string — origin understood")
        print(f"            canonical  {Q_MUON_50}")
        print(f"            in corpus  {Q_MUON_50_WRONG}")
        print("            Circular: its producer reads, via q_at, the witness")
        print("            it writes, so it has never been derived from a")
        print("            closed form. That is why q_muon_at() misses it.")
        print()
        print(f"     {n_unknown:5d}  some OTHER non-canonical value — origin UNKNOWN")
        print("            Not the stale string and not canonical. These have")
        print("            had no investigation at all; do not assume they")
        print("            share the circularity above.")
        print()
        print("     SCOPE — reproducibility, NOT accuracy. CODATA m_mu/m_e is")
        print("     known to ~7 sig figs, capping q_muon at ~8; the stale gap")
        print("     is 431x SMALLER than that uncertainty. No derived physical")
        print("     quantity moves. Do not report this as a precision problem.")

    if mixed:
        print(f"\n  ** {len(mixed)} witness(es) record MORE THAN ONE anchor "
              f"-- CANDIDATES for a layer straddle, needing triage:")
        print("     (a q-sweep or pin-sensitivity map carries both by design "
              "and is NOT a defect)")
        for path, kinds in mixed[:10]:
            print(f"       {'+'.join(kinds):22s} {path}")

    if args.list_other:
        print("\n  'other' bucket (neither pin):")
        for f in per_bucket_files["other"]:
            print(f"    {f}")
    if args.list_truncated:
        print("\n  5-digit truncated anchor:")
        for f in per_bucket_files["truncated-5-digit"]:
            print(f"    {f}")

    print("\n  Scope note: this measures what each witness RECORDS, which is")
    print("  not the same as what its producer used. A witness in 'NOT")
    print("  RECORDED' may well be on the proton pin -- it simply does not say,")
    print("  which is the reportable defect.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
