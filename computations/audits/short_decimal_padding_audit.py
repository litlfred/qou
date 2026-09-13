#!/usr/bin/env python3
# polynomial_q_not_applicable: static value audit; emits no numeric physics.
"""short-decimal padding audit — a value the float64-padding ratchet cannot see.

**The defect.** `codata_constants._ame_binding_mev` and its siblings build
their constants inside `mp.workdps(max(50, mp.dps))`, and the module is
imported before `set_compute_dps()` has run in most producers.  So the
constant IS the 50-dps binary approximation of an EXACT short decimal.
`_precision.fmt` then renders it at `OUTPUT_DPS` (60), and a producer that
prints at 70 goes further:

    "AME_MeV": "2.22456619999999999999999999999999999999999999999999734095406"

The AME2020 datum is `2.2245662` — eight significant figures.  Sixty digits
published, eight of them real, and the other fifty-two read with the same
authority.  Same defect as float64 padding, one working precision up.

**Why the existing ratchet cannot see it.**
`witness_float64_padding_audit.py` discriminates by relative distance to the
nearest binary64: ~1e-17 means genuine, ~1e-50 means a double's expansion.  A
50-dps value sits **~1e-17** from the nearest double — it is a *genuine*
high-precision value by that test, and passes.  The test is sound; it answers
a different question.  Detector-blindness class, and this file is the
complementary detector, not a replacement.

**The discriminator here is a RECONSTRUCTION, not a threshold.**  A threshold
over-claims: `pn-alpha-lp-dual`'s
`y_star_str[0] = 1.000000000000000000000000000000000000000000000309399`
sits 3.1e-46 from `1.0` and is an SDP residual, not padding.  So instead:

    mp.nstr(mpf(short) built at B dps, printed at O dps) == recorded

for `B` in the build precisions the corpus actually uses and `O` in the output
precisions it actually prints at.  A match means the recorded digits are,
character for character, what you get by taking a short decimal into an mpf at
a lower working precision and printing it at a higher one.  There is no
information in the tail, and there is no judgement in the verdict.

**Not the source-literal class.**  `overlong_float_literal_audit.py`
(`qou-gqt5`) catches a bare Python literal spelling more digits than its parse
can keep.  That is the SOURCE side.  This is the RECORD side: the producer
writes its string correctly from an `mpf`, and the `mpf` was built short.

**Reported, not swept.**  Under the 2026-09-07 ASK-THE-OWNER directive the
disposition of the ~94 witnesses this finds is the owner's; bean `qou-rj7d`
carries the three options.  This file measures.  It is deliberately NOT wired
into `scripts/precision-gates.sh` and has no baseline — adding a gate is a
change, and this is a measurement.

Usage:
    python3 computations/audits/short_decimal_padding_audit.py [root]
    python3 computations/audits/short_decimal_padding_audit.py --selftest
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from mpmath import mp, mpf

# Numeric strings only.  An exponent form is excluded on purpose: `mp.nstr`
# switches to it below its own threshold and the reconstruction would then
# have to match formatting rather than digits.
NUM_RX = re.compile(r"^-?\d+\.\d+$")

# Working precisions the corpus builds constants at.  50 is
# `workdps(max(50, mp.dps))` in `codata_constants`; 53 is a common
# `mp.dps = 53`; 60 and 70 are OUTPUT_DPS and COMPUTE_DPS.
BUILD_DPS = (50, 53, 60, 70)
# Precisions producers print at.  60 is `_precision.fmt`; the others are
# hand-rolled `mp.nstr(x, N)` calls seen in the tree.
OUT_DPS = (60, 65, 67, 70)

# Below this, a long tail is not evidence of anything.
MIN_SIG_DIGITS = 25
# Prefilter only.  The verdict is the reconstruction, never this number.
NEAR_REL = "1e-45"


def sig_digits(s: str) -> int:
    body = re.sub(r"[-.]", "", s)
    return len(body.lstrip("0").rstrip("0")) or 0


def nearest_short(recorded: str):
    """The <=15-sig-fig decimal `recorded` is close to, or None.

    Returns None when `recorded` IS that decimal exactly — a short value
    written with trailing zeros claims nothing false and is not a finding.
    """
    mp.dps = 120
    v = mpf(recorded)
    if v == 0:
        return None
    for k in range(1, 16):
        mp.dps = 120
        cand = mp.nstr(v, k, strip_zeros=True)
        cv = mpf(cand)
        if cv == 0:
            continue
        rel = abs(v - cv) / abs(v)
        if rel == 0:
            return None
        if rel < mpf(NEAR_REL):
            return cand
    return None


def reconstruct(recorded: str, short: str):
    """(build_dps, out_dps) if `recorded` is the render of `short`, else None."""
    for bd in BUILD_DPS:
        mp.dps = bd
        cand = mpf(short)
        for od in OUT_DPS:
            mp.dps = od + 10
            for strip in (False, True):
                if mp.nstr(cand, od, strip_zeros=strip) == recorded:
                    return bd, od
    return None


def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, path + "/" + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, path + f"[{i}]")
    else:
        yield path, obj


def classify(recorded: str):
    """('confirmed', short, bd, od) | ('near', short, None, None) | None."""
    if sig_digits(recorded) < MIN_SIG_DIGITS:
        return None
    short = nearest_short(recorded)
    if short is None:
        return None
    r = reconstruct(recorded, short)
    if r is None:
        return ("near", short, None, None)
    return ("confirmed", short, r[0], r[1])


def _selftest() -> int:
    """Pin BOTH directions: the class fires, and the near-misses stay quiet."""
    mp.dps = 50
    ame_d = mp.nstr(mpf("2.2245662"), 60, strip_zeros=False)
    mp.dps = 50
    m_e = mp.nstr(mpf("0.51099895069"), 70, strip_zeros=False)
    cases = [
        # (label, recorded, expected verdict, expected short)
        ("AME deuteron at 50 dps printed at 60", ame_d, "confirmed",
         "2.2245662"),
        ("CAL-1 m_e at 50 dps printed at 70", m_e, "confirmed",
         "0.51099895069"),
        # An SDP residual near 1.0 — near, never confirmed.
        ("SDP residual near 1",
         "1.000000000000000000000000000000000000000000000309399",
         "near", "1.0"),
        # Honest short value: exactly 2.5, written short.  No finding.
        ("short exact", "2.5", None, None),
        # A genuine 60-dps quantity: no short decimal within 1e-45.
        ("genuine high precision",
         mp.nstr(mpf("1.1099785827513808075916690956107688798744991218736"),
                 60, strip_zeros=False),
         None, None),
    ]
    fails = []
    for label, rec, want_kind, want_short in cases:
        got = classify(rec)
        kind = got[0] if got else None
        short = got[1] if got else None
        if kind != want_kind or (want_short is not None and short != want_short):
            fails.append(f"{label}: got {kind!r}/{short!r}, "
                         f"want {want_kind!r}/{want_short!r}")
    for f in fails:
        print(f"SELFTEST FAILED: {f}", file=sys.stderr)
    print(f"short-decimal padding selftest: "
          f"{len(cases) - len(fails)}/{len(cases)} "
          f"{'PASS' if not fails else 'FAIL'}")
    return 1 if fails else 0


def main(argv: list[str]) -> int:
    if argv and argv[0] in ("--selftest", "--self-test"):
        return _selftest()
    root = Path(argv[0]) if argv else Path("computations")
    confirmed: dict[str, list] = {}
    near: dict[str, list] = {}
    n_files = n_conf = n_near = 0
    for f in sorted(root.rglob("*.witness.json")):
        n_files += 1
        try:
            payload = json.loads(f.read_text())
        except Exception:
            continue
        for p, v in walk(payload):
            if not isinstance(v, str) or not NUM_RX.match(v):
                continue
            got = classify(v)
            if got is None:
                continue
            kind, short, bd, od = got
            if kind == "confirmed":
                n_conf += 1
                confirmed.setdefault(str(f), []).append((p, v, short, bd, od))
            else:
                n_near += 1
                near.setdefault(str(f), []).append((p, v, short))

    print("=" * 74)
    print("SHORT-DECIMAL PADDING AUDIT — a short datum rendered at 60-70 dps")
    print("=" * 74)
    print(f"  witnesses scanned            : {n_files}")
    print(f"  CONFIRMED fields             : {n_conf} "
          f"in {len(confirmed)} witness(es)")
    print(f"  NEAR (not claimed)           : {n_near} "
          f"in {len(near)} witness(es)")
    print()
    print("  CONFIRMED means the recorded string reconstructs character for")
    print("  character from a <=15-sig-fig decimal at one of the build/output")
    print("  precisions below; there is no information in its tail.")
    print(f"    build dps tried : {BUILD_DPS}")
    print(f"    output dps tried: {OUT_DPS}")
    print()
    print("  NEAR is MIXED and is deliberately not claimed: it holds both the")
    print("  same class at a build precision not tried, and genuine solver")
    print("  output that happens to land near a short decimal.  Widen")
    print("  BUILD_DPS to separate them; do not reason about it.")
    print()
    for path, rows in sorted(confirmed.items(), key=lambda kv: -len(kv[1])):
        print(f"  {len(rows):>5}  {path}")
        for p, v, short, bd, od in rows[:2]:
            print(f"           {p}")
            print(f"             recorded = {v}")
            print(f"             == mpf('{short}') at {bd} dps, "
                  f"printed at {od}")
    print()
    print("  Reported, not swept — disposition is bean `qou-rj7d` under the")
    print("  2026-09-07 ASK-THE-OWNER directive.  No baseline, no --strict.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
