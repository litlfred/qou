"""Measure: corpus labels cited in computations/ docstrings that have NO carrier.

No existing gate reads this surface: `uses-resolve` reads MANIFEST uses[], and a
label inside a Python docstring is not a manifest edge. Bean qou-3kni item 3
("the population is unmeasured").

CALIBRATION, and it is not decoration: the first version of this script used
`[a-z0-9-]` for the label stem and silently TRUNCATED
`prop:constit-factor-tau-M-proton-identity` to `prop:constit-factor-tau-` at the
uppercase M, then reported the fragment as dead. Corpus labels carry uppercase
(`tau-M`), so the character class IS the blind spot. --selftest asserts the full
form is captured and that three known-dead and two known-live labels classify
correctly; it FAILS rather than passing quietly.
"""
import ast, pathlib, re, subprocess, collections, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent  # computations/
# uppercase and underscore are LOAD-BEARING here -- see the calibration note.
LABEL = re.compile(r'\b((?:conj|prop|def|thm|lem|cor|rem|sec|ex|sim|alg):'
                   r'[A-Za-z0-9][A-Za-z0-9_-]{2,})')

tracked = set(subprocess.run(["git","ls-files"],capture_output=True,text=True).stdout.split())

_cache = {}
def has_carrier(label: str) -> bool:
    if label in _cache: return _cache[label]
    stem = label.split(":",1)[1]
    hit = any(stem in p for p in tracked)
    if not hit:
        r = subprocess.run(["git","grep","-l","--fixed-strings",f'"{label}"',
                            "--","folio/","content/"], capture_output=True, text=True)
        hit = bool(r.stdout.strip())
    _cache[label] = hit
    return hit

def collect():
    cites = collections.defaultdict(set)
    me = pathlib.Path(__file__).resolve()
    for p in sorted(ROOT.rglob("*.py")):
        if "_deprecated" in p.parts or "__pycache__" in p.parts: continue
        # Skip THIS file. Its calibration note quotes the truncated fragment as
        # documentation, so scanning itself reports that fragment as a dead
        # label and fails its own selftest -- caught by the selftest on the
        # first run after the script moved under computations/. An audit that
        # scans itself measures its own prose.
        if p.resolve() == me: continue
        try: tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError: continue
        for node in [tree, *(n for n in ast.walk(tree)
                     if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)))]:
            d = ast.get_docstring(node)
            if not d: continue
            for m in LABEL.finditer(d):
                cites[m.group(1)].add(str(p))
    return cites

cites = collect()

# Both spellings. precision-gates.sh tries --self-test first and falls back to
# --selftest only on argparse's "unrecognized arguments"; a bare argv check emits
# no such message, so the mis-spelled flag was silently ignored, the real scan
# ran, and its honest exit 1 (25 dead labels) was reported as a self-test
# failure. Rejecting an unknown flag is the half that generalises: a flag
# matching nothing must not produce a clean-looking run (bean qou-wu38).
_FLAGS = [a for a in sys.argv[1:] if a.startswith("-")]
_UNKNOWN = [a for a in _FLAGS if a not in ("--selftest", "--self-test", "-v")]
if _UNKNOWN:
    print(f"unrecognized arguments: {' '.join(_UNKNOWN)}", file=sys.stderr)
    sys.exit(2)

if set(_FLAGS) & {"--selftest", "--self-test"}:
    ok = True
    # 1. no truncation: the uppercase-bearing label must appear in FULL
    full = "prop:constit-factor-tau-M-proton-identity"
    if full not in cites:
        print(f"SELFTEST FAIL: truncation — {full} not captured"); ok = False
    if "prop:constit-factor-tau-" in cites:
        print("SELFTEST FAIL: truncated fragment captured"); ok = False
    # 2. known DEAD must classify dead
    for l in ("conj:pl-jsj-mass-integration-equivalence",
              "conj:denominator-zeros-as-sw-critical-points"):
        if l not in cites: print(f"SELFTEST FAIL: {l} not even cited"); ok = False
        elif has_carrier(l): print(f"SELFTEST FAIL: known-dead {l} read as live"); ok = False
    # 3. known LIVE must classify live
    for l in ("conj:shared-denominator-cusp-holonomy",
              "def:q-pochhammer-partial-product"):
        if not has_carrier(l): print(f"SELFTEST FAIL: known-live {l} read as dead"); ok = False
    print("SELFTEST PASS" if ok else "SELFTEST FAILED")
    sys.exit(0 if ok else 1)

print(f"distinct labels cited in computations/ docstrings: {len(cites)}")
print(f"citing files: {len({f for fs in cites.values() for f in fs})}")
dead = {l: fs for l, fs in cites.items() if not has_carrier(l)}
print(f"DEAD (no carrier in folio/ or content/): {len(dead)}")
print(f"citations pointing at nothing: {sum(len(fs) for fs in dead.values())}\n")
for l, fs in sorted(dead.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    print(f"  {len(fs):2d}  {l}")
    if "-v" in sys.argv:
        for f in sorted(fs):
            print(f"        {f}")

if dead:
    print("\nEach label above is cited in a producer docstring and resolves to no\n"
          "block anywhere in folio/ or content/. `uses-resolve` reads MANIFEST\n"
          "uses[], so a label in a docstring is not a manifest edge and no\n"
          "existing gate sees it. A reader following one lands on nothing.")
sys.exit(1 if dead else 0)
