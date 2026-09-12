#!/usr/bin/env python3
"""Every long digit-string quoted in the bean must be a TRUNCATION or a correct
ROUNDING of a witness value.

Catches the 2026-09-12 defect: a full-precision-LOOKING figure written from a
rounded console display. Truncation gives a prefix; correct rounding gives the
nearest value at that many places; fabrication gives neither.

A prefix-only test is NOT enough -- it flags correct roundings (`...82989` ->
`...83`) as fabrications, which is the same detector-blindness class the defect
belongs to. Both spellings are accepted here.

Strings inside a section headed `CORRECTION` are quoted deliberately as
superseded and are exempt; they are reported so the exemption stays visible.

USAGE
    python3 computations/audits/quoted_figure_provenance_audit.py [BEAN.md] [WITNESS.json]

Defaults to the `qou-za3q` bean and the Magnus-Omega2 weight-family witness,
which is where the defect was found.

LIMITS, stated rather than discovered later:
  * It compares against ONE witness. A bean legitimately quoting a figure from a
    sibling witness is reported UNEXPLAINED -- pass that witness instead, or
    extend `truth`. It is a provenance check, not an oracle.
  * `>= 10` decimal places is the trigger. A fabricated SHORT figure
    (`-6.92125065` say) is below it and is not caught; the defect class this
    targets is a figure dressed up as full precision.
  * The exempt zone is the whole file from the first `CORRECTION` heading
    onward. A new fabrication appended after that heading would be exempt.
    Keep corrections at the end and new claims above them.
"""
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 120   # witness values run to ~60 digits; default 28 raises InvalidOperation
import json, pathlib, re, sys

BEAN = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.beans/qou-za3q--magnus-omega2-probes-call-the-plancherel-weight-y.md')
WIT  = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else 'computations/deltalambda/magnus-omega2-weight-family-robustness.witness.json')

truth = []
for r in json.loads(WIT.read_text())['data']['per_atom']:
    for k in ('P_total_plancherel', 'P_total_wenzl'):
        truth.append(Decimal(str(r[k])).copy_abs())

def explains(q: str) -> str | None:
    """Return 'truncation' / 'rounding' if some witness value explains q."""
    places = len(q.split('.')[1])
    qd = Decimal(q)
    for t in truth:
        ts = str(t)
        if ts.startswith(q):
            return 'truncation'
        if t.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP) == qd:
            return 'rounding'
    return None

text = BEAN.read_text()
# byte offset where the correction section starts (exempt zone)
m = re.search(r'^#+ .*CORRECTION', text, re.M)
exempt_from = m.start() if m else len(text)

rows, bad = [], []
for mm in re.finditer(r'(?<![\d.])\d{1,3}\.\d{10,}', text):
    q, off = mm.group(0), mm.start()
    how = explains(q)
    exempt = off >= exempt_from
    rows.append((q, how, exempt))
    if how is None and not exempt:
        bad.append(q)

seen = set()
print(f"witness values : {len(truth)}")
for q, how, exempt in rows:
    if (q, how, exempt) in seen:
        continue
    seen.add((q, how, exempt))
    tag = how or ('SUPERSEDED-QUOTE' if exempt else 'UNEXPLAINED')
    print(f"  {'EXEMPT' if exempt and how is None else 'OK    '} {q:62s} {tag}")
if bad:
    print(f"\nFAIL — {len(bad)} figure(s) outside the correction section match no witness value:")
    for q in bad:
        print(f"  {q}")
    sys.exit(1)
print("\nPASS — every live figure is a truncation or a correct rounding of a witness value.")
