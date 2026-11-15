#!/usr/bin/env python3
"""Every long digit-string quoted in a bean must be a TRUNCATION or a correct
ROUNDING of a value in one of its witnesses.

Catches the 2026-09-12 defect: a full-precision-LOOKING figure written from a
rounded console display. Truncation gives a prefix; correct rounding gives the
nearest value at that many places; fabrication gives neither.

TWO DESIGN POINTS, each of which the FIRST version of this script got wrong.
Both failures are recorded because each is the same class the script exists to
catch -- a detector blind to a legitimate spelling, and a detector that reports
clean over ground it never examined.

1. A PREFIX-ONLY TEST IS NOT ENOUGH. It flags correct roundings
   (`...82989` -> `...83`) as fabrications. v1 reported 4 problems of which 2
   were its own false positives. Rounding is accepted alongside truncation.

2. EXEMPTION MUST BE EXPLICIT, NEVER POSITIONAL. v1 exempted "everything from
   the first `CORRECTION` heading onward", so that superseded values quoted in
   a correction would not self-report. Measured consequences on the qou-za3q
   bean:
     * the first CORRECTION heading is at line 188 of 436, so **57 % of the
       file was never examined** while the script printed PASS;
     * a blatant fabrication (`-99.123456789012345678`) appended at the end was
       classified `SUPERSEDED-QUOTE` and the script exited 0;
     * beans grow by `beans update --body-append`, which appends to the END, so
       EVERY future append landed in the exempt zone. v1's own advice -- "keep
       corrections at the end and new claims above them" -- is unfollowable
       with the tool that actually writes beans.
   So a superseded figure must now carry the literal token `SUPERSEDED` on its
   own line or within the 3 lines above it. Explicit, greppable, and immune to
   where it sits in the file.

USAGE
    quoted_figure_provenance_audit.py [BEAN.md] [WITNESS.json ...]
    quoted_figure_provenance_audit.py --selftest

Defaults to the `qou-za3q` bean and all four Magnus-Omega2 witnesses, so a
figure legitimately quoted from a sibling witness resolves instead of being
reported unexplained (v1 knew one witness and mis-reported the he4 sign value).

REMAINING LIMITS, stated rather than left to be discovered:
  * `>= 10` decimal places is the trigger. A fabricated SHORTER figure is not
    caught. The real defect was caught at exactly 10, so the margin is thin;
    the target class is a figure dressed up as full precision.
  * It knows only the witnesses passed to it. An unexplained figure may be a
    correct quote from a witness not on the command line -- the report says
    UNEXPLAINED, which means "not justified by what I was given", not "wrong".
  * It checks digit provenance only. A figure can be a true copy of a witness
    value and still be the wrong quantity for the sentence around it.
"""
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 200   # witness values run to ~60 digits; default 28 raises InvalidOperation
import json, pathlib, re, subprocess, sys, tempfile

DEFAULT_BEAN = 'beans/defs/qou-za3q--magnus-omega2-probes-call-the-plancherel-weight-y.md'
DEFAULT_WITNESSES = [
    'computations/deltalambda/magnus-omega2-weight-family-robustness.witness.json',
    'computations/deltalambda/deuteron-magnus-omega2-sign.witness.json',
    'computations/deltalambda/triton-magnus-omega2-sign.witness.json',
    'computations/deltalambda/he4-magnus-omega2-sign.witness.json',
]
FIGURE_RX = re.compile(r'(?<![\d.])\d{1,4}\.\d{10,}')
MARKER = 'SUPERSEDED'
MARKER_LOOKBACK = 3          # lines above the figure that may carry the marker


def _numbers(obj, out):
    """Every numeric-looking scalar anywhere in the witness, as abs Decimal."""
    if isinstance(obj, dict):
        for v in obj.values():
            _numbers(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _numbers(v, out)
    elif isinstance(obj, str):
        if re.fullmatch(r'[+-]?\d+(\.\d+)?([eE][+-]?\d+)?', obj.strip()):
            try:
                out.append(Decimal(obj.strip()).copy_abs())
            except Exception:
                pass
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        try:
            out.append(Decimal(str(obj)).copy_abs())
        except Exception:
            pass


def load_truth(paths):
    truth = []
    for p in paths:
        p = pathlib.Path(p)
        if p.exists():
            _numbers(json.loads(p.read_text()), truth)
    return truth


def explains(q, truth):
    """'truncation' / 'rounding' if some witness value explains q, else None."""
    places = len(q.split('.')[1])
    qd = Decimal(q)
    unit = Decimal(1).scaleb(-places)
    for t in truth:
        if str(t).startswith(q):
            return 'truncation'
        try:
            if t.quantize(unit, rounding=ROUND_HALF_UP) == qd:
                return 'rounding'
        except Exception:
            continue
    return None


def audit(bean_path, witness_paths, quiet=False):
    truth = load_truth(witness_paths)
    lines = pathlib.Path(bean_path).read_text().splitlines()

    rows, bad = [], []
    for i, line in enumerate(lines):
        if not FIGURE_RX.search(line):
            continue
        window = '\n'.join(lines[max(0, i - MARKER_LOOKBACK):i + 1])
        marked = MARKER in window
        for q in FIGURE_RX.findall(line):
            how = explains(q, truth)
            rows.append((i + 1, q, how, marked))
            if how is None and not marked:
                bad.append((i + 1, q))

    if not quiet:
        print(f"bean           : {bean_path}")
        print(f"witnesses      : {len(witness_paths)}  ({len(truth)} numeric values)")
        print(f"figures >= 10dp: {len(rows)}")
        for ln, q, how, marked in rows:
            if how:
                tag = how
            elif marked:
                tag = f'{MARKER}-QUOTE (explicitly marked)'
            else:
                tag = 'UNEXPLAINED'
            flag = 'OK    ' if how else ('EXEMPT' if marked else '** BAD')
            print(f"  {flag} L{ln:<5} {q:62s} {tag}")
        if bad:
            print(f"\nFAIL — {len(bad)} figure(s) justified by no witness and not marked {MARKER}:")
            for ln, q in bad:
                print(f"  line {ln}: {q}")
        else:
            print(f"\nPASS — every figure is witness-justified or explicitly marked {MARKER}.")
    return 1 if bad else 0


def selftest():
    """The check v1 failed: an appended fabrication must be DETECTED."""
    print("SELFTEST — is an appended fabrication caught?\n")
    src = pathlib.Path(DEFAULT_BEAN).read_text()
    fake = '99.123456789012345678'
    ok = True

    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as fh:
        fh.write(src + f"\n## A later append\n\nP_total = -{fake}\n")
        appended = fh.name
    rc = audit(appended, DEFAULT_WITNESSES, quiet=True)
    print(f"  fabrication appended at END        -> {'DETECTED' if rc else 'MISSED'}"
          f"   (v1: MISSED, exit 0)")
    ok &= rc == 1

    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as fh:
        fh.write(src + f"\n## A later append\n\n{MARKER}: P_total = -{fake}\n")
        marked = fh.name
    rc2 = audit(marked, DEFAULT_WITNESSES, quiet=True)
    print(f"  same figure, explicitly {MARKER}  -> {'exempt' if rc2 == 0 else 'still flagged'}")
    ok &= rc2 == 0

    rc3 = audit(DEFAULT_BEAN, DEFAULT_WITNESSES, quiet=True)
    print(f"  the real bean, unmodified          -> {'clean' if rc3 == 0 else 'FLAGGED'}")
    ok &= rc3 == 0

    print(f"\n{'PASS' if ok else 'FAIL'} — detection is positional-independent"
          f" and the marker still exempts.")
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    sys.exit(audit(args[0] if args else DEFAULT_BEAN,
                   args[1:] if len(args) > 1 else DEFAULT_WITNESSES))
