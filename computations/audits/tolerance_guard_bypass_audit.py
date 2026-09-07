#!/usr/bin/env python3
"""Which producers can UNDO the declared-tolerance drain, decided by the answer
rather than by the shape of the source.

*** WHAT THIS IS FOR ***

PR #5910 (`bc8131bd58`) converted 1232 declared assertion tolerances from JSON
floats to strings across 499 witnesses, by editing the ARTIFACTS
(`normalize_assertion_tolerance.py --apply`). The guard that would make that
permanent — `qou_substrate.witness._tolerance_literal` — runs at
`Assertion.to_dict`, i.e. only for a producer that constructs an `Assertion`.
A producer that hand-builds its payload and `json.dump`s it never reaches the
guard, so its next re-run re-emits the float and undoes the drain for that
file, one file at a time, invisibly.

Bean `qou-9tqx`.

*** WHY NOT JUST GREP THE SOURCE ***

The bean's own method is a source grep:

    grep -rln '"tolerance":[[:space:]]*[0-9]' --include=*.py computations/
      | grep -v _deprecated                                  # 33 files
    # of those, json.dump AND no add_assertion               # -> 26

That 26 is a count of *files whose text matches a shape*, and this corpus has a
long record of such counts being wrong in both directions (see
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`). Measured here, **at
least two of the 26 are not producers at all**:

  - `normalize_assertion_tolerance.py:13` — the drain script's own DOCSTRING,
    showing the before/after of the transformation it performs.
  - `witness_raw_float64_audit.py:682` — the ratchet's own SELF-TEST FIXTURE,
    an inline dict with an asserted expected count.

Both are tools that *mention* the key; neither emits a witness. A shape audit
that counts its own detectors as offenders is the taxonomy's own failure mode.

*** WHAT THIS DECIDES INSTEAD ***

For every candidate producer, resolve its committed witness(es) and read what
is actually on disk. Three verdicts, and only the first two are work:

  LIVE-DIRTY   the committed witness carries a float `tolerance` NOW that the
               guard WOULD have stringified. The drain was reverted here (by a
               stale-branch merge, or by a re-run) and the artifact is dirty
               today.

*** THE VERDICT IMPORTS THE GUARD; IT DOES NOT REIMPLEMENT IT ***

"Carries a float" is NOT the question, and asking it that way is how the first
version of this script reported **28 LIVE-DIRTY against a true 6**. Most of
what it flagged was `0` and `0.0`, which `_tolerance_literal` returns `None`
for on purpose — integral values are exact in binary64, the ratchet already
excuses them, and converting them would churn ~200 committed values for no
gate benefit. It also flags nothing for a COMPUTED tolerance (more than 5
significant digits, e.g. `1025.6028557082007`): those genuinely lost precision,
are real findings, and stringifying one would hide a defect behind a
convention.

So this script imports `qou_substrate.witness._tolerance_literal` and asks the
guard's own question — *would adoption have changed this value?* A float the
guard would leave alone is not this bean's business, and counting it inflates
the number the bean exists to keep honest. Importing rather than restating also
means the audit cannot drift from the rule it audits: change the guard and this
follows, with no second edit.

That correction is the same class as the two false positives above — a detector
measuring its own assumptions instead of the corpus — caught here in its own
first run.

  LATENT       the committed witness carries string tolerances (drained, clean)
               but the producer source still holds a float literal THE GUARD
               WOULD CHANGE. The next re-run of this producer re-dirties the
               file. This is the population the bean is about, and it is
               invisible to any check that reads only artifacts.

               The capitalised clause is load-bearing and was absent from the
               first version: this pass used the bean's shape match while pass 1
               imported the guard, and reported **24 where the guard would
               change 8**. Fifteen of the 24 were `0`/`0.0` or values already
               serialized as strings — two of them producers that had *already
               been fixed at source*. See `_source_would_change`.

  NO-TOLERANCE the witness resolves and carries no `tolerance` key at all. The
               source match is a docstring, a self-test fixture, or a dict that
               never reaches the payload.

*** PASS 2 IS BLIND TO A TOLERANCE PASSED AS A VARIABLE — MEASURED, LIVE ***

`_source_would_change` runs `ast.literal_eval` on the token after `"tolerance":`
and skips anything that is not a literal. So a producer whose assertion helper
takes `tolerance` as a PARAMETER is invisible to pass 2 no matter how many
floats reach it.

This is not hypothetical and it was not caught by prediction. On 2026-09-05,
`3277607d39` ("guard qbeta_ck_qholonomic probe against null extracted c_k")
re-ran `qbeta_ck_qholonomic_recurrence_test.py` on `main`, and its
`gate(name, passed, computed, expected, tolerance, source)` helper re-emitted
`1e-45`, `1e-12` and `1.1` as floats — undoing PR #5910's drain for that file.
Pass 2 had reported the corpus LATENT-free at the time. **Pass 1 caught it**
(LIVE-DIRTY 1, and the ratchet independently as REGRESSED 65 -> 67), which is
why the two passes exist: the artifact check is the guarantee, the source check
is only the early warning.

Measured surface of the gap: **16** hand-building files pass a non-literal
tolerance, but most are already safe — `mp.nstr(TOL, …)`, an f-string, and
`str(t)` all yield strings, and two hits are these audits' own docstrings.
About **five** pass a bare name that could be a float
(`m_tau_complex_volume_search`, `lw2_c2_independent_hopf_test_attempt`,
`he4_binding_k_presentation_correction_probe`,
`qbeta_habiro_integrality_kill_test`, `aoperator_a5_crosscheck`); pass 1
reports all of them clean today. Closing the gap needs a detector that keys on
the helper's call sites rather than on the literal — deliberately NOT built
here, because a hasty one would add false positives to the very count this
audit exists to keep honest.

**CLOSED — the tier below is that detector** (`_source_unguarded_param`, bean
`qou-zq7b`). It resolves a parameter to its call sites instead of matching the
token, excludes the stringified / integral / f-string forms, and carries a
`--selftest` because it reports ZERO on the corpus: zero hits is not the same
as verified sound. Calibrated against the pre-fix
`qbeta_ck_qholonomic_recurrence_test.py`, where it finds 4 sites; 0 after the
fix.

  UNRESOLVED   the source matches but no committed witness could be found. This
               is a limit of THIS TOOL, not a verdict about the corpus, and it
               is reported separately for that reason — two of the eight the
               first version filed under "not a producer" were really this
               (`qbeta_habiro_p8_deep_probe` writes a witness that is not
               committed; `knot_volumes` writes to `substrate/`, which the
               stem convention does not reach).

               `knot-volumes.py` has since been RESOLVED and fixed: it names
               its output only in its docstring, unquoted, so the path match
               missed it — a real latent producer (11 sites) filed under a
               tool limit. That is what this verdict is for, and it is why it
               must never be read as a clean bill.

               The four that remain are triaged and are NOT work:
                 - `witness_integer_field_audit.py` and
                   `test_q0_migration_tolerance_triage.py` — self-test
                   fixtures whose floats are the thing under test;
                   stringifying one would delete the case it asserts.
                 - `witness_constant_staleness.py` — the same, inside
                   `_selftest()`.
                 - `q0_migration_tolerance_triage.py` — writes its payload to
                   STDOUT, never to a file, so there is no artifact to
                   re-dirty.

*** TWO PASSES, BECAUSE THEY ANSWER DIFFERENT QUESTIONS ***

Pass 1 scans EVERY committed witness, not only those reachable from a matched
source. That is the decisive measure of *"is the corpus dirty today"*, and it
is the population the bean's own list of ten came from. It is also the only
pass that can see an offender whose producer does not match the source pattern
at all — which is exactly what it found.

Pass 2 scans sources for the latent hazard, which no artifact check can see.

*** WHAT IT DELIBERATELY DOES NOT DO ***

It does not run any producer. A re-run is the only way to prove a LATENT
verdict end-to-end, and re-running is exactly the act that dirties the file —
so proving the claim would perform the damage it predicts. The end-to-end
confirmation already exists and is recorded in the bean: one producer
(`qbeta_ck_basis_constrained_pslq`) was re-run after the drain and the float
came back. That is the calibration; this audit generalises from it by reading,
not by repeating it 26 times.

Consequently a LATENT verdict is a *hazard*, not a proof, and this script says
so in its own output rather than claiming more than it measured.

*** USAGE ***

    PYTHONPATH=computations:tools/qou-substrate/python \
      python3 computations/audits/tolerance_guard_bypass_audit.py [--strict]

`--strict` exits 1 when any LIVE-DIRTY witness is found. LATENT is reported but
never fails: it is a statement about a future run, and failing on it would make
the gate red on a tree that is clean.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
COMPUTATIONS = ROOT / "computations"

# The audit's verdict IS the guard's verdict. Imported, never restated: a
# reimplementation drifts, and the first version of this script proved it by
# reporting 28 against a true 6 (see the module docstring).
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
try:
    from qou_substrate.witness import _tolerance_literal
except ImportError as exc:  # pragma: no cover - environment, not logic
    print(f"cannot import the guard being audited: {exc}\n"
          f"  run with PYTHONPATH including tools/qou-substrate/python",
          file=sys.stderr)
    raise SystemExit(2) from exc

# The literal token following a `"tolerance":` key in Python source. NOT the
# bean's `\s*[0-9]` shape test — see `_source_would_change` for why that test
# over-counts by 3x, and why this script committed that very error in this pass
# while fixing it in the other.
SRC_TOL = re.compile(r'"tolerance":\s*([^,}\n]+)')


def _source_would_change(py: Path) -> list[tuple[int, object]]:
    """Sites in `py` where adopting the guard WOULD change the emitted value.

    Pass 1 imports `_tolerance_literal` and asks the guard's own question. This
    pass did not, and used the bean's `"tolerance":\\s*[0-9]` shape match — so
    it counted every site whose text starts with a digit, including the two
    populations the guard deliberately leaves alone:

      - `0`, `0.0` — integral, exact in binary64, ~200 committed values that
        would churn for no gate benefit;
      - a value already serialized as a string (`"1e-08"`, `mp.nstr(TOL, 5)`).

    Measured on the 24 this pass reported: **8** would change, 15 were already
    guard-clean and 1 was a non-literal expression that evaluates to a string.
    Two of the 15 (`qbeta_ck_basis_constrained_pslq`, `wlambda_q0_continuation`)
    had *already been fixed at source*, and this pass was still reporting them.

    A shape match and the guard's predicate are different questions; asking the
    first and reporting the second is the same defect the module docstring
    records for pass 1, arrived at independently in the half that was not
    rewritten. Both halves now import the guard.
    """
    try:
        text = py.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    hits: list[tuple[int, object]] = []
    for m in SRC_TOL.finditer(text):
        try:
            value = ast.literal_eval(m.group(1).strip())
        except (ValueError, SyntaxError):
            continue  # an expression, not a literal — pass 1 sees its output
        if isinstance(value, (int, float)) and _tolerance_literal(value) is not None:
            hits.append((text.count("\n", 0, m.start()) + 1, value))
    return hits


# Callables whose result is a STRING, so a tolerance routed through one is
# already safe and must not be flagged. Measured: of the 16 hand-building files
# passing a non-literal tolerance, 11 are safe for exactly this reason, and a
# detector that ignored it would report eleven false positives against one true
# one — the failure `docs/audits/2026-08-15-detector-blindness-taxonomy.md`
# catalogues. `mp.nstr` is the corpus's usual spelling.
_STRINGIFIERS = {"str", "repr", "format", "nstr", "mp.nstr"}


def _call_name(node: ast.AST) -> str:
    """Dotted name of a call target, or '' — `mp.nstr(x, 5)` -> 'mp.nstr'."""
    if not isinstance(node, ast.Call):
        return ""
    f = node.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        base = f.value.id if isinstance(f.value, ast.Name) else ""
        return f"{base}.{f.attr}" if base else f.attr
    return ""


def _guard_would_change(value) -> bool:
    return isinstance(value, (int, float)) and _tolerance_literal(value) is not None


def _source_unguarded_param(py: Path) -> list[tuple[int, str, object]]:
    """Sites where a tolerance reaches the payload through a VARIABLE.

    THE GAP THIS CLOSES, and it is not hypothetical. `_source_would_change`
    above literal-evals the token after `"tolerance":`, so a producer whose
    assertion helper takes `tolerance` as a PARAMETER is invisible to it. On
    2026-09-05 `3277607d39` re-ran exactly such a producer on `main` and undid
    PR #5910's drain for one file while this pass reported the corpus
    LATENT-free. Bean `qou-zq7b`.

    It resolves rather than pattern-matches, in three steps:

      1. A value that is an f-string, or a call to a STRINGIFIER, is SAFE — it
         is already a string. This is what keeps the count honest: 11 of the 16
         non-literal sites in the corpus are safe for this reason alone.
      2. A value that is a PARAMETER of the enclosing function is resolved to
         that function's call sites, and each argument (positional or keyword)
         is literal-eval'd. A site is flagged only when a call site actually
         passes a value the guard would change.
      3. A value that is a plain name assigned a literal in the same function
         or at module level is resolved to that literal.

    Anything else — a computed expression, a name bound from a call — is left
    UNREPORTED rather than guessed at. This audit's whole purpose is a count
    that can be trusted, so a site it cannot decide is not a finding.
    """
    try:
        src = py.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(src)
    except (OSError, SyntaxError):
        return []

    # name -> literal, for module-level and function-local `name = <literal>`
    bindings: dict[str, object] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                bindings[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, SyntaxError):
                pass

    # function -> its call sites' arguments, keyed by parameter name
    funcs: dict[str, ast.FunctionDef] = {
        n.name: n for n in ast.walk(tree)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    calls: dict[str, list[ast.Call]] = {}
    for node in ast.walk(tree):
        name = _call_name(node)
        if name in funcs:
            calls.setdefault(name, []).append(node)

    def enclosing(lineno: int):
        cands = [f for f in funcs.values() if f.lineno <= lineno <= (f.end_lineno or f.lineno)]
        return min(cands, key=lambda f: (f.end_lineno or f.lineno) - f.lineno) if cands else None

    hits: list[tuple[int, str, object]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if not (isinstance(k, ast.Constant) and k.value == "tolerance"):
                continue
            if isinstance(v, ast.Constant):
                continue                      # the literal path already has it
            if isinstance(v, ast.JoinedStr) or _call_name(v) in _STRINGIFIERS:
                continue                      # already a string
            if not isinstance(v, ast.Name):
                continue                      # computed — not decidable here
            fn = enclosing(v.lineno)
            if fn and v.id in [a.arg for a in fn.args.args]:
                idx = [a.arg for a in fn.args.args].index(v.id)
                for call in calls.get(fn.name, []):
                    passed = None
                    if len(call.args) > idx:
                        passed = call.args[idx]
                    for kw in call.keywords:
                        if kw.arg == v.id:
                            passed = kw.value
                    if passed is None or isinstance(passed, ast.JoinedStr) \
                            or _call_name(passed) in _STRINGIFIERS:
                        continue
                    try:
                        val = ast.literal_eval(passed)
                    except (ValueError, SyntaxError):
                        continue
                    if _guard_would_change(val):
                        hits.append((passed.lineno, f"{fn.name}({v.id}=)", val))
            elif v.id in bindings and _guard_would_change(bindings[v.id]):
                hits.append((v.lineno, v.id, bindings[v.id]))
    return hits


# A fixture in the SHAPE of the real defect: a helper taking `tolerance` as a
# parameter, called with a guard-changing float, a stringified one, and an
# integral one. `--selftest` fails unless the detector separates all three.
#
# This exists because the detector reports ZERO on the corpus, and zero hits is
# not the same as verified sound — taxonomy row 34, where a tier that had fired
# on nothing was asserted correct having measured only that. A future narrowing
# that broke this detector would otherwise look like a clean tree.
_SELFTEST_SRC = '''
def gate(name, passed, computed, expected, tolerance, source):
    rows.append({"name": name, "computed": computed, "expected": expected,
                 "tolerance": tolerance, "source": source})

gate("a", True, 1, 1, 1e-45, "flag: the guard would stringify this")
gate("b", True, 1, 1, mp.nstr(TOL, 5), "safe: already a string")
gate("c", True, 1, 1, 0.0, "safe: integral, the guard declines")
gate("d", True, 1, 1, f"1e-{n}", "safe: f-string")
'''


def _selftest() -> int:
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
        fh.write(_SELFTEST_SRC)
        path = Path(fh.name)
    try:
        hits = _source_unguarded_param(path)
    finally:
        path.unlink(missing_ok=True)
    vals = sorted(repr(v) for _, _, v in hits)
    if vals != ["1e-45"]:
        print(f"SELFTEST FAIL: expected exactly the 1e-45 site, got {vals}")
        return 1
    print("SELFTEST OK: flags the parameter-passed float; ignores the "
          "stringified, integral and f-string forms.")
    return 0


def _iter_tolerances(obj):
    """Yield every value stored under a `tolerance` key, at any depth."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "tolerance":
                yield v
            yield from _iter_tolerances(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _iter_tolerances(v)


def _candidate_witnesses(py: Path) -> list[Path]:
    """Witnesses a producer plausibly writes.

    Two routes, because producers name their output both ways:
      1. the stem convention — `foo_bar_probe.py` -> `foo-bar-probe.witness.json`
         (and without the `_probe` suffix), in the producer's own directory;
      2. any `*.witness.json` path spelled literally in the source.

    Route 2 is what catches a producer whose output name does not follow from
    its own filename, which several here do not.
    """
    found: list[Path] = []
    stem = py.stem
    for cand in {stem, stem.removesuffix("_probe")}:
        p = py.parent / f"{cand.replace('_', '-')}.witness.json"
        if p.is_file():
            found.append(p)
    try:
        text = py.read_text(encoding="utf-8", errors="replace")
    except OSError:
        text = ""
    # Unquoted too: `knot-volumes.py` names its output only in its DOCSTRING
    # ("computations/substrate/knot-volumes.witness.json"), so a quote-requiring
    # match filed a real latent producer under UNRESOLVED — its witness lives in
    # a sibling directory the stem convention also cannot reach. The path must
    # still exist on disk, so relaxing this cannot invent a candidate.
    for m in re.finditer(r'([A-Za-z0-9_./-]+\.witness\.json)', text):
        rel = m.group(1)
        for base in (py.parent, COMPUTATIONS, ROOT):
            p = (base / rel).resolve()
            if p.is_file() and p not in found:
                found.append(p)
                break
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any committed witness carries a float tolerance")
    ap.add_argument("--selftest", action="store_true",
                    help="check the parameter-resolving detector against a known-shape fixture")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    src_sites: dict[Path, list[tuple[int, object]]] = {}
    for p in sorted(COMPUTATIONS.rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        sites = _source_would_change(p)
        if sites:
            src_sites[p] = sites
    sources = list(src_sites)

    # The parameter-resolving tier (bean qou-zq7b). Separate from `sources`
    # because it answers a different question: not "is the literal here wrong"
    # but "does a float reach the payload through a variable".
    param_sites: dict[Path, list[tuple[int, str, object]]] = {}
    for p in sorted(COMPUTATIONS.rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        h = _source_unguarded_param(p)
        if h:
            param_sites[p] = h

    rel = lambda p: p.relative_to(ROOT)  # noqa: E731

    # ---- Pass 1: every committed witness. The decisive measure. -------------
    scanned = 0
    live_dirty: list[tuple[Path, list]] = []
    for w in sorted(COMPUTATIONS.rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        scanned += 1
        try:
            data = json.loads(w.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        bad = [t for t in _iter_tolerances(data) if _tolerance_literal(t) is not None]
        if bad:
            live_dirty.append((w, bad))

    # ---- Pass 2: sources, for the latent hazard artifacts cannot show. ------
    latent: list[tuple[Path, list[Path]]] = []
    no_tolerance: list[Path] = []
    unresolved: list[Path] = []
    dirty_paths = {w for w, _ in live_dirty}
    for py in sources:
        witnesses = _candidate_witnesses(py)
        if not witnesses:
            unresolved.append(py)
            continue
        if any(w in dirty_paths for w in witnesses):
            continue  # already reported by pass 1
        saw = False
        for w in witnesses:
            try:
                data = json.loads(w.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if list(_iter_tolerances(data)):
                saw = True
        (latent if saw else no_tolerance).append((py, witnesses) if saw else py)

    print("=" * 78)
    print("DECLARED-TOLERANCE GUARD BYPASS — the guard's own predicate, imported")
    print("=" * 78)
    print(f"  PASS 1  committed witnesses scanned          : {scanned}")
    print(f"          LIVE-DIRTY (guard WOULD stringify)   : {len(live_dirty)}")
    print(f"  PASS 2  sources the guard WOULD change       : {len(sources)}")
    print(f"          LATENT (clean now; a re-run re-dirties): {len(latent)}")
    print(f"          NO-TOLERANCE (docstring/fixture)     : {len(no_tolerance)}")
    print(f"          UNRESOLVED (tool limit, not a verdict): {len(unresolved)}")
    print(f"  PASS 2b VARIABLE-PASSED (resolved to call sites)  : {len(param_sites)}")

    if live_dirty:
        print("\n--- LIVE-DIRTY: the drain is undone in these committed witnesses ---")
        for w, floats in live_dirty:
            shown = ", ".join(repr(f) for f in floats[:4])
            more = f" (+{len(floats) - 4} more)" if len(floats) > 4 else ""
            print(f"  {rel(w)}\n      would-be literals: {shown}{more}")

    if latent:
        print("\n--- LATENT: artifact is clean; the SOURCE still holds a float literal ---")
        print("    (a hazard about a future run, not a defect on disk today —")
        print("     never fails --strict, and must not be reported as one)")
        for py, ws in latent:
            sites = ", ".join(f"L{ln}={v!r}" for ln, v in src_sites[py])
            print(f"  {rel(py)}  ->  {', '.join(str(rel(w)) for w in ws)}")
            print(f"      {sites}")

    if param_sites:
        print("\n--- VARIABLE-PASSED: a float reaches the payload through a name ---")
        print("    (resolved to the call site, not guessed from the token; the")
        print("     stringified / integral / f-string forms are excluded)")
        for py, hs in param_sites.items():
            for ln, via, val in hs:
                print(f"  {rel(py)}:{ln}  via {via}  -> {val!r}")

    if unresolved:
        print("\n--- UNRESOLVED: no committed witness found. NOT a clean bill. ---")
        for py in unresolved:
            print(f"  {rel(py)}")

    if no_tolerance:
        print("\n--- NO-TOLERANCE: witness resolves, carries no tolerance key ---")
        for py in no_tolerance:
            print(f"  {rel(py)}")

    print("\nNOTE: no producer was run. A LATENT verdict generalises from the one")
    print("end-to-end confirmation recorded in bean qou-9tqx; re-running to prove")
    print("it here would perform the damage it predicts.")

    if args.strict and live_dirty:
        print(f"\nFAIL (--strict): {len(live_dirty)} witness(es) carry a float tolerance.")
        return 1
    print("\nOK" + (" (LATENT hazards reported, not failed)" if latent else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
