#!/usr/bin/env python3
# polynomial_q_not_applicable: static value audit; emits no numeric physics.
"""float64-padding audit — catch fake precision in committed witnesses.

Owner directive: "NO FLOAT64".

**The defect.** A value that enters a producer as a Python `float` carries at
most ~17 significant digits. Serializing it at 50 dps does not add
information — it writes out the *binary64 expansion*, i.e. 30+ digits of
rounding garbage that reads as exact. Example, from a live witness:

    "B_AME_MeV": "8.4817962000000015621026250300928950309753417968750000000000"

The experimental datum is `8.4817962` — eight significant figures. Everything
after `...962` is an artifact of binary representation, and it is presented
with the same authority as the real digits.

This is worse than staleness. A stale value is *wrong*; a float64-padded
value is *wrong about how well it is known*, which is harder to notice and
defeats every precision check downstream.

**The discriminator.** For a decimal string `s`:

| quantity | genuine 50-dps value | float64-padded |
|---|---|---|
| relative distance to the nearest binary64 | ~1e-17 | **~1e-50** |

A genuine high-precision value carries information a double cannot hold, so
it sits ~1e-17 away from the nearest double. A padded one *is* a double's
expansion, so the distance is pure truncation (~1e-50).

**Honest padding is not flagged.** `1.000...0` is exactly 1: a short exact
value written with trailing ZEROS carries no false claim. Only a non-zero
tail beyond ~17 significant digits — binary garbage — is flagged.

**Ratchet.** The existing backlog is large (283 distinct values / 458
occurrences at introduction), so it is recorded in
`float64-padding-baseline.json` and tolerated; anything NOT in the baseline
fails `--strict`. Fake precision can shrink but never grow.

**The fix is at the producer, not the witness.** Do not hand-edit a padded
number. Either carry the value as a string/`mpf` from its source, or
serialize it at its true precision. Re-run the producer afterwards.

Output: `witness-float64-padding-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402

from decimal import Decimal, InvalidOperation, localcontext

from mpmath import mp, mpf

mp.dps = 90

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASELINE = HERE / "float64-padding-baseline.json"

# Only strings *claiming* high precision are candidates.
NUMSTR = re.compile(r"^-?\d+\.\d{20,}$")

# Below this many significant fractional digits (after stripping trailing
# zeros) a value makes no high-precision claim at all.
MIN_SIG_FRAC = 17

# Cheap pre-filter only. A value further than this from the nearest binary64
# cannot be that double's expansion, so it is rejected without the exact test
# below. It is NOT the discriminator — see `is_double_expansion`.
F64_GAP = mpf("1e-30")


def is_double_expansion(t: str) -> bool:
    """Is `t` the correctly-rounded rendering of its nearest binary64, at the
    precision `t` actually shows?

    This is what padding *literally is*: a value carrying 53 bits, printed at
    50 dps, emits the double's dyadic tail. So the question is not "how close
    is this to a double" but "are these the double's own digits".

    The distinction matters because proximity alone cannot decide it. Class B
    of the 2026-08-07 sweep is 9 producers whose flagged values are genuine
    computations of quantities that are exactly integers — `tr_M(1)` landing
    1.4e-51 short of 1 by rounding. That is *nearer* to a double than a real
    padding case truncated at 50 dps (1.6e-50), so no threshold can order
    them:

        mpf(0.1) printed at 50 dps   rel. distance 1.56e-50   IS padding
        tr_M(1), genuinely computed  rel. distance 1.37e-51   is NOT

    Digits settle it where distance cannot. `mpf(0.1)` at 50 dps reproduces
    0.10000000000000000555111512312578270211815834045410 — the double's exact
    expansion, truncated. `tr_M(1)` prints 0.999…99863, and the nearest double
    is 1.0, whose expansion is "1". Those are not the same digits, and no
    amount of closeness makes them so.

    Tolerance is exactly one half-ulp *of the shown precision*, so a value
    whose last digit mpmath rounded still matches. The place value comes from
    `Decimal.as_tuple().exponent` rather than from counting characters after
    the ".", so exponent-notation strings get the right ulp too.
    """
    try:
        d = float(mpf(t))
    except Exception:
        return False
    if d == 0 or d != d or abs(d) == float("inf"):
        return False
    try:
        dec = Decimal(t)
    except InvalidOperation:
        return False
    exp = dec.as_tuple().exponent
    if not isinstance(exp, int):
        return False                  # NaN/Inf sentinels
    with localcontext() as ctx:
        ctx.prec = abs(exp) + 60
        # Decimal(<float>) is the double's EXACT value, not a re-rounding.
        return abs(dec - Decimal(d)) <= Decimal(1).scaleb(exp) / 2


def is_f64_padded(s: str) -> bool:
    t = s.strip()
    if "." not in t:
        return False
    sig = t.split(".")[1].rstrip("0")
    if len(sig) <= MIN_SIG_FRAC:
        return False              # short exact value + honest zero padding
    try:
        x = mpf(t)
    except Exception:
        return False
    if x == 0:
        return False
    # Cheap reject first: nowhere near a double, so not its expansion.
    if abs(x - mpf(float(x))) / abs(x) >= F64_GAP:
        return False
    # Then the exact question, which proximity cannot answer.
    return is_double_expansion(t)


def real_digits(s: str) -> str:
    """The information actually present: the shortest round-tripping repr."""
    return repr(float(mpf(s.strip())))


def _walk(obj, path: str, fname: str, out: list) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            _walk(v, f"{path}.{k}" if path else k, fname, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _walk(v, f"{path}[{i}]", fname, out)
    elif isinstance(obj, str) and NUMSTR.match(obj.strip()):
        try:
            if is_f64_padded(obj):
                out.append({"file": fname, "field": path,
                            "value": obj.strip(),
                            "real_value": real_digits(obj)})
        except Exception:
            pass


# Witnesses that QUOTE numbers rather than compute them.
#
# The detector is sound on all of these — the strings really are doubles
# rendered past their precision. What it cannot see is that the witness is
# reporting a number found elsewhere, not publishing one of its own, so the
# finding belongs to the quoted source and re-reporting it here is noise. This
# audit's own witness is the obvious case (it records every offender it finds),
# but it was never the only one: the q0-drift and no-free-parameter witnesses
# were already here for the same reason, which is why the old name
# `SELF_OUTPUTS` described a narrower set than it held.
#
# `hardcoded-literal-audit` joins them, and it is the clearest instance of the
# class: its whole job is finding over-padded literals in SOURCE files, so its
# `rows[].hits[].literal` fields are the evidence. One such field
# (`8.481796200000000156210262503009…`, `matches_constant:
# AME_B_TRITIUM_MEV_VALIDATION`) was the last NEW entry in this audit — an
# audit flagging another audit's citation of the thing they both exist to
# catch.
#
# A LIST, not a heuristic, and deliberately: "does this field look quoted?"
# is exactly the inference that would let a producer's real padding hide
# behind an evidence-shaped path. Add a witness here only when its numbers
# come from somewhere else and that somewhere is itself audited.
QUOTED_EVIDENCE_WITNESSES = {
    "witness-float64-padding-audit.witness.json",
    "q0-value-drift-audit.witness.json",
    "no-free-parameter-certificate.witness.json",
    "hardcoded-literal-audit.witness.json",
}


def scan(skipped: list[str] | None = None) -> list[dict]:
    rows: list[dict] = []
    for p in sorted(HERE.rglob("*.witness.json")):
        if p.name in QUOTED_EVIDENCE_WITNESSES:
            # Recorded, not silently dropped. An exclusion nobody can see is
            # indistinguishable from a hole in the audit — the same rule the
            # raw-float64 carve-outs follow, where every excused field is
            # counted and reported apart from the total.
            if skipped is not None:
                skipped.append(p.relative_to(ROOT).as_posix())
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        _walk(d, "", p.relative_to(ROOT).as_posix(), rows)
    return rows


def self_test() -> int:
    cases = [
        # (string, expected is_f64_padded)
        ("8.4817962000000015621026250300928950309753417968750000000000", True),
        ("1.1097090248999998962631252652499824762344360351563", True),
        ("1.10997859555733471989976322048322502665620840878015368660798114614493", False),
        ("1.1099785827513808075916690956107688798744991218736", False),
        ("1.00000000000000000000000000000000000000000000000000000000000", False),
        ("-1.00000000000000000000000000000000000000000000000000000000000", False),
        ("2.00000000000000000000000000000000000000000000000000000000000", False),
        # --- Class B: genuine computations of exactly-integer quantities.
        # Each sits CLOSER to a double than a real 50-dps padding case does,
        # so no distance threshold can reject them; only the digits can. These
        # are the values three of the nine Class B producers actually emit.
        ("0.99999999999999999999999999999999999999999999999863", False),   # tr_M(1)
        ("-0.99999999999999999999999999999999999999999999999863", False),  # H_leading_ratio
        ("1.0000000000000000000000000000000000000000000000001", False),    # f_leading_ratio
        ("10.000000000000000000000000000000000000000000000323", False),    # h2, truth 10
        # --- and the padding that must still be caught, including the shape
        # the first (string-equality) draft of the discriminator wrongly
        # cleared: mpmath rounds the last shown digit, so the tolerance has to
        # be a half-ulp, not an exact match.
        ("3477.23000000000001818989403545856475830078125", True),          # mpf built at 15 dps
        ("0.000000001000000000000000062281591457779856418897068692786", True),
        ("0.10000000000000000555111512312578270211815834045410", True),    # mpf(0.1) @50 dps
    ]
    bad = [(s, e, is_f64_padded(s)) for s, e in cases if is_f64_padded(s) != e]
    if bad:
        print("SELF-TEST FAILED:")
        for s, e, g in bad:
            print(f"   {s[:44]}... expected {e}, got {g}")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases: float64-padded values detected, "
          "genuine 50-dps values and honest zero-padding not flagged.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on padded values NOT already in the baseline")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (draining only — count must go DOWN)")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    skipped: list[str] = []
    rows = scan(skipped)
    key = lambda r: f"{r['file']}::{r['field']}"
    prior = set()
    if BASELINE.exists():
        prior = set(json.loads(BASELINE.read_text())["padded_keys"])
    new = [r for r in rows if key(r) not in prior]

    files = sorted({r["file"] for r in rows})
    live = [f for f in files if ("_deprecated" not in f and "fsh-guts" not in f)]
    distinct = sorted({r["value"] for r in rows})

    print("=" * 74)
    print("FLOAT64-PADDING AUDIT — fake precision in committed witnesses")
    print("=" * 74)
    print(f"  padded occurrences : {len(rows)}")
    print(f"  distinct values    : {len(distinct)}")
    print(f"  files              : {len(files)}  ({len(live)} live)")
    if skipped:
        print(f"  quoted-evidence  : {len(skipped)} witness(es) NOT scanned "
              f"— they cite numbers found elsewhere rather than computing them")
        for _s in skipped:
            print(f"      {_s}")
    print(f"  baseline           : {len(prior)}")
    print(f"  NEW (not baselined): {len(new)}")

    if new:
        print("\n  NEW fake precision — fix AT THE PRODUCER (carry the value as a")
        print("  string/mpf, or serialize at its true precision), then re-run it.")
        print("  Never hand-edit the number.")
        for r in new[:25]:
            print(f"    {r['file']}  {r['field']}")
            print(f"        claims {r['value'][:52]}...")
            print(f"        really {r['real_value']}")
        if len(new) > 25:
            print(f"    ... and {len(new) - 25} more")

    if args.rebaseline:
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload_1 = {"note": "Known float64-padded witness fields. Regenerate ONLY when "
                     "draining; the count must go DOWN. Not a way to silence a "
                     "new failure. Fix at the producer, never by hand-editing.",
             "count": len(rows),
             "padded_keys": sorted(key(r) for r in rows)}
        _prov_payload_1.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload_1, script_path=__file__, engine=None, q0_anchor=False)
        BASELINE.write_text(json.dumps(
            _prov_payload_1, indent=2) + "\n")
        print(f"\nRebaselined: {len(rows)} padded keys recorded.")

    out = HERE / "witness-float64-padding-audit.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload_2 = {
        "schema": "witness/v1",
        "name": "witness-float64-padding-audit",
        "description": "Values serialized at high precision that are really "
                       "float64 expansions — fake precision. Honest zero-padding "
                       "of exact short values is not flagged.",
        "data": {"occurrences": len(rows), "distinct_values": len(distinct),
                 "files": len(files), "live_files": len(live),
                 "new_not_baselined": len(new), "rows": rows},
    }
    _prov_payload_2.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload_2, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(_prov_payload_2, indent=2) + "\n")
    print(f"\nWrote {out.name}")
    return 1 if (args.strict and new) else 0


if __name__ == "__main__":
    sys.exit(main())
