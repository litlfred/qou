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

  UNRESOLVED   the source matches but no committed witness could be found. This
               is a limit of THIS TOOL, not a verdict about the corpus, and it
               is reported separately for that reason — two of the eight the
               first version filed under "not a producer" were really this
               (`qbeta_habiro_p8_deep_probe` writes a witness that is not
               committed; `knot_volumes` writes to `substrate/`, which the
               stem convention does not reach).

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
    for m in re.finditer(r'["\']([A-Za-z0-9_./-]+\.witness\.json)["\']', text):
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
    args = ap.parse_args()

    src_sites: dict[Path, list[tuple[int, object]]] = {}
    for p in sorted(COMPUTATIONS.rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        sites = _source_would_change(p)
        if sites:
            src_sites[p] = sites
    sources = list(src_sites)

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
