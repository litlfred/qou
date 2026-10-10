#!/usr/bin/env python3
"""Flag Lean class fields whose DOCSTRING claims a limit but whose
STATEMENT does not encode one.

Motivation.  `conj:critical-exponent` and `conj:ns-counterexample` each
carried a field documented as a limit ("diverges as q -> 1", "unbounded
as t -> T*-") whose statement asserted only unboundedness *somewhere*.
Both were therefore satisfiable by a counterexample to the very claim
they name -- an enstrophy regular at q = 1, a velocity tending to 0 at
T*.  Verified in
docs/audits/2026-08-29-q-ns-conjecture-statement-strength-probe.lean.

No shipped criterion catches this.  The field is neither vacuous (it can
be false) nor a self-assuming projection (nothing projects it); it is
simply weaker than its own prose.  A detector keyed on inhabitability by
zero cannot see it, because these are not inhabitable by zero.

The check is deliberately crude and HIGH-RECALL: a hit is a candidate
for an agent to read, never a verdict.  The two known true positives are
regression-tested by --selftest.

Usage:
    python3 scripts/limit-claim-encoding-audit.py [PATH ...]
    python3 scripts/limit-claim-encoding-audit.py --selftest
"""
import re, sys, glob, os

# Prose that promises a limiting/asymptotic behaviour.
LIMIT_PROSE = [
    r'\\to\s*1', r'\\to\s*0', r'\\to\s*T', r'->\s*1', r'->\s*0',
    r'\bdiverge', r'\bblow[- ]?up\b', r'\bblows up\b',
    r'\basymptot', r'\bin the limit\b', r'\btends to\b',
    r'\bunbounded as\b', r'\bapproaches\b', r'\bvanishes as\b',
    r'\bsingularity time\b', r'\bas\s+\$?[a-zA-Z]\s*\\to',
]
# Devices that actually localise a limit in a Lean statement.
LIMIT_DEVICE = [
    r'\bε\b', r'\beps\b', r'Filter\.Tendsto', r'\bTendsto\b', r'𝓝',
    r'atTop', r'nhds', r'\|\s*\w+\s*-\s*\w+\s*\|\s*<',
    r'-\s*ε\s*<', r'<\s*ε', r'Set\.Ioo', r'Set\.Ico', r'Set\.Ioi',
    r'\bLimUnder\b', r'IsLittleO', r'IsBigO',
]
LIMIT_PROSE_RE  = re.compile('|'.join(LIMIT_PROSE), re.I)
LIMIT_DEVICE_RE = re.compile('|'.join(LIMIT_DEVICE))

def fields_with_docs(path):
    """Yield (field_name, docstring, statement) for each class field."""
    lines = open(path).read().split("\n")
    out, doc, i = [], [], 0
    in_class = False
    while i < len(lines):
        l = lines[i]
        if re.match(r'(class|structure)\s', l):
            in_class = True; doc = []; i += 1; continue
        if l and not l[0].isspace() and not re.match(r'\s*$', l):
            if not re.match(r'(class|structure)\s', l):
                in_class = False
        if not in_class:
            i += 1; continue
        if re.match(r'\s*/--', l):                       # docstring start
            doc = []
            while i < len(lines):
                doc.append(lines[i])
                if '-/' in lines[i]: break
                i += 1
            i += 1; continue
        m = re.match(r'^  ([a-zA-Z_][A-Za-z0-9_\']*)\s*:(.*)$', l)
        if m and not l.strip().startswith('--'):
            stmt = [m.group(2)]
            j = i + 1
            while j < len(lines) and re.match(r'^\s{4,}\S', lines[j]) \
                    and not re.match(r'\s*/--', lines[j]):
                stmt.append(lines[j]); j += 1
            out.append((m.group(1), "\n".join(doc), "\n".join(stmt)))
            doc = []; i = j; continue
        i += 1
    return out

def audit(paths):
    hits = []
    for p in paths:
        for name, doc, stmt in fields_with_docs(p):
            if not doc:
                continue
            if LIMIT_PROSE_RE.search(doc) and not LIMIT_DEVICE_RE.search(stmt):
                # only interesting when the statement quantifies a bound
                if re.search(r'∀|∃', stmt):
                    hits.append((p, name, doc, stmt))
    return hits

def selftest():
    """The two known true positives, as they read BEFORE the 2026-08-29 fix."""
    import tempfile
    before = '''namespace T
class CriticalExponent where
  /-- The enstrophy diverges as $q \\to 1$: for every bound $M$ there
      exists $q \\neq 1$ exhibiting an enstrophy exceeding $M$. -/
  enstrophy_diverges :
    ∀ M : ℝ, ∃ q : ℝ, q ≠ 1 ∧ M < enstrophy q
class NSCounterexample where
  /-- The velocity is unbounded as $t \\to T^{*-}$. -/
  ns_counterexample_holds :
    ∀ M : ℝ, ∃ t x : ℝ, t < singularityTime ∧ M < velocityProfile t x
end T
'''
    with tempfile.NamedTemporaryFile('w', suffix='.lean', delete=False) as fh:
        fh.write(before); tmp = fh.name
    got = {n for _, n, _, _ in audit([tmp])}
    os.unlink(tmp)
    want = {'enstrophy_diverges', 'ns_counterexample_holds'}
    if not want <= got:
        print(f"SELFTEST FAIL: expected {want}, detector found {got}")
        return 1
    print(f"selftest ok: detector finds both known true positives {sorted(want)}")
    return 0

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    if not args:
        args = (glob.glob("folio/quantum-observable-universe/lean/QOU/FluidDynamics/*.lean")
                + glob.glob("folio/quantum-observable-universe/fluid-dynamics/*.lean"))
    paths = []
    for a in args:
        paths += glob.glob(os.path.join(a, "*.lean")) if os.path.isdir(a) else [a]
    hits = audit(sorted(paths))
    for p, name, doc, stmt in hits:
        print(f"\n\u2550\u2550 {p}::{name}")
        d = " ".join(re.sub(r'/--|-/', '', doc).split())
        print(f"   doc  : {d[:190]}")
        print(f"   stmt : {' '.join(stmt.split())[:190]}")
    print(f"\n{len(hits)} candidate(s) over {len(paths)} file(s) "
          f"-- candidates for an agent to read, not verdicts.")
