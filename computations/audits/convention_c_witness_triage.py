#!/usr/bin/env python3
"""Triage the committed convention-C witnesses into the three classes that
have different work orders.

PR #5510 measured 58 committed witnesses carrying the convention-C Markov
parameter ``z_C = 0.4993203340...`` and recorded, correctly, that the number is
**not a work order**: only one of the three classes it can decompose into is
mechanical.

    1. stale output of a now-D producer   -> re-run the producer   (mechanical)
    2. deliberate C-vs-D comparison       -> LEAVE IT              (that is the point)
    3. live C producer the detector missed -> real source migration (not mechanical)

Sweeping class 2 is not a cleanup, it is a regression: the excision has to stay
measurable, and `schur_principal_mpmath._wenzl_constants_convention_C_HISTORICAL`
says so in its own docstring -- left unpreserved, the D-vs-C comparison it feeds
"silently degrades to D-vs-D and reports C's y_(13)/y_(3) as 0 with a spurious
*integral* N* = 2 -- the exact opposite of the finding it exists to display."

METHOD.  Two independent signals per witness, neither of which is a `z` grep of
the kind AGENTS.md documents thirteen blind spots for:

  * **Producer drift.**  Compare the witness's recorded ``scriptHash`` against a
    freshly computed hash of the producer on disk (same function the witness
    writer uses, `qou_substrate.witness.file_content_hash`).  A producer that
    has changed since it emitted a C value is a class-1 candidate; one that is
    byte-identical is a class-3 candidate, because the code that wrote C is the
    code that is still there.
  * **Quarantine markers.**  A C spelling inside a function whose name or
    docstring marks it historical / comparison-only is class 2 by construction.

NEITHER SIGNAL IS A VERDICT, and this script does not pretend otherwise -- it
emits high-recall *candidates* in the repo's usual sense.  Producer drift cannot
see import-cone drift (a producer can be byte-stable while a module it calls
changed), and a hash match cannot distinguish "still computes C" from "computes
D now but the committed witness predates a rename".  The decisive test is
re-running the producer, which is exactly what this triage exists to *scope*:
re-running all 58 is what the measurement said not to do.

Usage:
    python3 -u computations/audits/convention_c_witness_triage.py
    python3 -u computations/audits/convention_c_witness_triage.py --json out.json
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys

# The two conventions, as committed decimal values.
Z_C = '0.4993203340'
Z_D = '0.6126880505'

# Markers that put a C spelling out of production by intent, not by accident.
QUARANTINE = re.compile(
    r'HISTORICAL|convention[_ -]?C[_ -]?(?:only|historical|dead)|'
    r'DEAD FOR PRODUCTION|do not call this|C-vs-D|D-vs-C|'
    r'excised|comparison only|retained because',
    re.IGNORECASE,
)

# High-recall C spellings.  Deliberately algebraic rather than name-based --
# AGENTS.md catalogues thirteen name-based blind spots for exactly this class.
C_SPELLINGS = [
    # z_C = 1/(sqrt(q) + 1/sqrt(q)) -- the reciprocal-sum spelling.
    re.compile(r'1(?:\.0)?\s*/\s*\(\s*sq\s*\+\s*1(?:\.0)?\s*/\s*sq\s*\)'),
    re.compile(r'1(?:\.0)?\s*/\s*\(\s*(?:mp\.|np\.|sp\.)?sqrt\(\s*q\w*\s*\)\s*\+\s*'
               r'1(?:\.0)?\s*/\s*(?:mp\.|np\.|sp\.)?sqrt\(\s*q\w*\s*\)\s*\)'),
    # the **0.5 / **(1/2) spelling of the same reciprocal sum
    re.compile(r'1(?:\.0)?\s*/\s*\(\s*\w+\s*\*\*\s*0?\.5\s*\+\s*\w+\s*\*\*\s*0?\.5\s*\)'),
    # z_C = sqrt(q)/(q + 1) -- the closed spelling.  The sqrt argument must be
    # q itself and the denominator exactly (q + 1): sqrt(q**4 + q**2 + 1)
    # over (q**2 + 1) is a DIFFERENT quantity and matching it is a false
    # positive (this detector over-fired on exactly that, twice, before the
    # arguments were pinned).
    re.compile(r'(?:mp\.|np\.|sp\.)?sqrt\(\s*q\w*\s*\)\s*/\s*\(\s*q\w*\s*\+\s*1\s*\)'),
    re.compile(r'\bq\w*\s*\*\*\s*0?\.5\s*/\s*\(\s*q\w*\s*\+\s*1\s*\)'),
    re.compile(r'\bq\w*\s*\*\*\s*\(\s*1\s*/\s*2\s*\)\s*/\s*\(\s*q\w*\s*\+\s*1\s*\)'),
]


def file_content_hash(path: str, length: int = 12) -> str:
    """Matches qou_substrate.witness.file_content_hash."""
    with open(path, 'r', encoding='utf-8') as fh:
        return hashlib.sha256(fh.read().encode('utf-8')).hexdigest()[:length]


def find_producer(script_file: str | None) -> str | None:
    """Resolve a witness's scriptFile to a live path, ignoring _deprecated."""
    if not script_file:
        return None
    base = os.path.basename(script_file)
    if not base.endswith('.py'):
        base += '.py'
    hits = [p for p in glob.glob(f'**/{base}', recursive=True)
            if '_deprecated' not in p and '/_internal/' not in p
            and '.lake' not in p]
    if not hits:
        return None
    hits.sort(key=lambda p: (not p.startswith('computations/'), len(p)))
    return hits[0]


def scan_source(path: str) -> tuple[list[str], bool]:
    """Return (matched C spellings, whether every match looks quarantined)."""
    try:
        src = open(path, 'r', encoding='utf-8').read()
    except Exception:
        return [], False
    lines = src.splitlines()
    found, quarantined = [], True
    for rx in C_SPELLINGS:
        for m in rx.finditer(src):
            lineno = src[:m.start()].count('\n')
            found.append(f'{os.path.basename(path)}:{lineno + 1}: {m.group(0).strip()}')
            # Context window: the enclosing 40 lines above, where a docstring
            # or def name marking the site historical would live.
            ctx = '\n'.join(lines[max(0, lineno - 40):lineno + 3])
            if not QUARANTINE.search(ctx):
                quarantined = False
    return found, (quarantined and bool(found))


def classify(rec: dict) -> tuple[str, str]:
    if rec['carries_D']:
        return 'deliberate-comparison', 'witness carries both z_C and z_D'
    if rec['producer'] is None:
        return 'unresolved', 'producer not resolvable from scriptFile'
    if rec['c_spellings'] and rec['all_quarantined']:
        return 'deliberate-comparison', 'C spelling present but marked historical/comparison-only'
    if rec['c_spellings']:
        return 'live-C-producer', f"live C spelling: {rec['c_spellings'][0]}"
    if rec['hash_recorded'] and rec['hash_now'] and rec['hash_recorded'] != rec['hash_now']:
        return 'stale-output', 'no live C spelling; producer changed since the witness was written'
    if rec['hash_recorded'] and rec['hash_recorded'] == rec['hash_now']:
        return 'unresolved', 'producer byte-identical to when it emitted C, but no C spelling found — import-cone drift or a blind spelling'
    return 'unresolved', 'no C spelling found and producer drift not determinable'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', help='write the full triage to this path')
    args = ap.parse_args()

    records = []
    for path in sorted(glob.glob('computations/**/*.witness.json', recursive=True)):
        if '_deprecated' in path:
            continue
        try:
            txt = open(path, encoding='utf-8').read()
        except Exception:
            continue
        if Z_C not in txt:
            continue
        try:
            data = json.loads(txt)
        except Exception:
            data = {}
        producer = find_producer(data.get('scriptFile'))
        spellings, all_q = scan_source(producer) if producer else ([], False)
        rec = {
            'witness': path,
            'scriptFile': data.get('scriptFile'),
            'producer': producer,
            'carries_D': Z_D in txt,
            'hash_recorded': data.get('scriptHash'),
            'hash_now': file_content_hash(producer) if producer else None,
            'c_spellings': spellings,
            'all_quarantined': all_q,
        }
        rec['klass'], rec['why'] = classify(rec)
        records.append(rec)

    order = ['live-C-producer', 'deliberate-comparison', 'stale-output', 'unresolved']
    print(f'convention-C witnesses found: {len(records)}\n')
    for k in order:
        group = [r for r in records if r['klass'] == k]
        print(f'{"=" * 70}\n{k.upper()}  ({len(group)})\n{"=" * 70}')
        for r in group:
            print(f'  {os.path.basename(r["witness"])}')
            print(f'      producer : {r["producer"] or "(unresolved) " + str(r["scriptFile"])}')
            print(f'      why      : {r["why"]}')
        print()

    print('SUMMARY')
    for k in order:
        print(f'  {k:<24} {sum(1 for r in records if r["klass"] == k):>4}')
    print()
    print('  mechanical (re-run the producer)  : '
          f'{sum(1 for r in records if r["klass"] == "stale-output")}')
    print('  MUST NOT be swept                 : '
          f'{sum(1 for r in records if r["klass"] == "deliberate-comparison")}')
    print('  needs a source migration          : '
          f'{sum(1 for r in records if r["klass"] == "live-C-producer")}')
    print('  needs an agent to look            : '
          f'{sum(1 for r in records if r["klass"] == "unresolved")}')

    if args.json:
        with open(args.json, 'w', encoding='utf-8') as fh:
            json.dump({'schema': 'convention-c-witness-triage/v1',
                       'records': records}, fh, indent=2)
        print(f'\nwrote {args.json}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
