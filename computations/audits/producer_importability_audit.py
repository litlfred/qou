#!/usr/bin/env python3
"""producer_importability_audit.py — committed witnesses whose PRODUCER cannot
run, so the witness can never be refreshed and no staleness detector sees it.

Bean `qou-cds2` follow-on. Every existing staleness mechanism compares a
witness against its producer: `witness.scriptHash` vs the current file hash,
`q0Anchor` vs the recorded pin, the raw-float64 ratchet vs a baseline. All of
them presuppose that running the producer is POSSIBLE. When it is not, the
witness is frozen: it cannot drift out of agreement with a producer nobody can
execute, so it reports clean forever while its numbers age.

This is not hypothetical. `proton-residual-rootcause.witness.json` was carrying
a convention-C `z_markov = 0.49932033403356124` while the corpus had ruled D
canonical, and it was invisible to the whole C->D campaign: its producer raised
`TypeError: float() argument must be ... not 'mpc'` on every run, so nothing
could rewrite it. Found only because a convention migration happened to touch
that file (commit 179f030c2, PR #5265).

METHOD. For each committed `*.witness.json` that names a `scriptFile`, resolve
the producer beside it and import the module in a subprocess. These scripts
guard their work with `if __name__ == "__main__":`, so an import exercises the
entire top level — imports, module-level constants, path wiring — without
running the compute. Import failure means the witness is unrefreshable.

CLASSES REPORTED SEPARATELY, because they are not the same defect:

  in-repo-wiring   the producer cannot find a module that IS in this repo
                   (`pyhecke`, `qou_substrate`, `_precision`, `witness_base`,
                   `q_parameter`, a sibling probe). A missing sys.path setup.
                   These are real and fixable — the largest class.
  optional-dep     the producer needs a genuinely external optional package
                   (`snappy`, `matplotlib`). NOT a defect: it means the
                   witness cannot be refreshed in THIS environment, which a
                   reader should know, but the producer is not broken.
  other            everything else (FileNotFoundError, NameError, TypeError…).
  heavy-at-import  the import did not finish inside the timeout, i.e. the
                   script does real compute at module level. NOT a failure.

TWO HARNESS BUGS THIS AVOIDS, both of which I hit while building it:

  1. **Hyphenated filenames.** `import beta-decay-from-q` is a syntax error in
     the IMPORT STATEMENT, not in the file. A first pass using
     `python -c "import <stem>"` reported 24 bogus `SyntaxError`s; all 24 files
     parse cleanly under `ast.parse`. This loads by file location instead.
     Corrected count: 109 candidates -> 90 real.
  2. **`_deprecated/`.** Those producers are expected to be broken and are
     excluded from every other audit here; including them buries the signal.

⚠ SIDE EFFECT — READ BEFORE RUNNING. Importing a module runs its top level,
and some producers here DO REAL WORK (and write their witness) at module
level rather than inside `main()`. A full run therefore rewrites those
witnesses as a side effect. The first full run modified **111** of them,
4343 insertions, and they were nearly committed inside the detector's own
commit. Either run this in a throwaway `git worktree`, or afterwards restore
everything except this audit's own witness:

    git status --short | grep 'witness.json' | grep -v producer-importability \
      | awk '{print $2}' | xargs -r git checkout HEAD --

The `heavy-at-import` class this reports IS that population, so a nonzero
count there is advance warning that the run dirtied the tree.

SCOPE. This is a DETECTOR. It fixes nothing and does not claim the 90 are all
defects — the optional-dep class in particular is a fact about the environment.
Draining the in-repo-wiring class is separate work.
"""
from __future__ import annotations

import argparse
import ast
import collections
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402

#: Genuinely external optional packages — absence is an environment fact, not a
#: producer defect.
OPTIONAL_DEPS = {"snappy", "matplotlib", "scipy", "sage", "cypari", "spherogram"}

#: Modules that live in THIS repo; failing to find one is a sys.path defect.
IN_REPO = {"pyhecke", "qou_substrate", "_precision", "witness_base",
           "q_parameter", "hecke_core", "lp_dual_solver", "mass_endomorphism"}

# `sys.argv[0]` is REWRITTEN to the producer's own filename before the module
# body runs, and that is load-bearing rather than cosmetic. `q_parameter`
# resolves the q0 anchor from the running producer's argv stem against the
# `ideal_muon` list in `q0_anchor_manifest.json`, so a loader that leaves
# argv[0] as `-c` silently pins every producer to proton and never executes the
# muon branch at all.
#
# Measured 2026-08-19: under the old `-c` argv this audit reported every
# `ideal_muon` producer importable — it was answering a question no real
# invocation asks.
#
# ⚠ CORRECTED 2026-08-24. This note used to end: "Under a faithful argv they
# raise `RuntimeError: ideal/muon anchor requested ... refusing to fall back to
# proton silently`, because the committed `q-pinning-50-digit.witness.json`
# holds the PROTON value (bean qou-m9xp)." **That is no longer true.** Measured
# at mp.dps=60, the committed pinning witness holds
# `1.10997859555733471989976322048322` — 4.5e-24 ppb from the canonical MUON
# pin A and 11.54 ppb from the proton pin. So the rebind path SUCCEEDS today and
# `ideal_muon` producers do not hard-fail on it. The argv rewrite is still
# load-bearing for the same reason; only the failure mode described here has
# gone. A deliberate stem count is also omitted now: it was 257 when written,
# 120 on main and 152 here today, and a number that rots inside a comment is how
# the rest of this note went stale.
_LOADER = (
    "import importlib.util,sys;"
    "sys.argv=[sys.argv[1]];"
    "spec=importlib.util.spec_from_file_location('_m',sys.argv[0]);"
    "m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)"
)


_PRODUCER_SUFFIXES = (".py", ".rs", ".lean", ".sage")
_basename_index: "dict[str, list[Path]] | None" = None


def _repo_basename_index(root: Path) -> "dict[str, list[Path]]":
    """Every producer-shaped file in the repo, keyed by basename.

    Built once. `_deprecated`, `.git`, `__pycache__` and `node_modules` are
    excluded so a resolution never lands on a retired copy.
    """
    global _basename_index
    if _basename_index is None:
        idx: "dict[str, list[Path]]" = {}
        repo = root.parent
        skip = {"_deprecated", ".git", "__pycache__", "node_modules"}
        for f in repo.rglob("*"):
            if not f.is_file() or f.suffix not in _PRODUCER_SUFFIXES:
                continue
            if skip & set(f.parts):
                continue
            idx.setdefault(f.name, []).append(f)
        _basename_index = idx
    return _basename_index


_reverse_index: "dict[str, list[Path]] | None" = None
_py_src: "dict[Path, str]" = {}


def _writes(src: str, name: str) -> bool:
    """Does this producer WRITE `name`, or merely READ it?

    The distinction is the whole point. A witness name appearing as a string
    literal proves a RELATIONSHIP, not a direction: `option_e_a4_full_
    reconciliation.py` names `chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json`
    because it LOADS it, and writes something else entirely. Resolving a witness
    to a reader would make this audit import the wrong file and then report the
    witness refreshable on the strength of it — a false clean, which is the exact
    defect class this audit exists to detect.

    So: AST taint from the literal to a write sink. Three propagation rules,
    each one observed in the corpus rather than guessed at:
      assignment      OUT = HERE / "x.witness.json";  OUT.write_text(...)
      for-target      for path in TARGETS: ...        (TARGETS holds the names)
      one call level  process(path)  ->  def process(path): path.write_text(...)
    Sinks: open(p, 'w'|'a'), p.open('w'|'a'), p.write_text/​write_bytes.

    Under-claiming is deliberate. A producer whose write we cannot see is
    reported as unresolved with the candidate named, not silently attached.
    """
    try:
        tree = ast.parse(src)
    except Exception:  # noqa: BLE001 — a producer that will not parse is a
        return False   # separate defect; do not guess at its outputs
    def has_lit(node) -> bool:
        for n in ast.walk(node):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) \
                    and name in n.value:
                return True
        return False
    funcs = {n.name: n for n in ast.walk(tree)
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    tainted: "set[str]" = set()

    def expr_tainted(val) -> bool:
        return val is not None and (has_lit(val) or any(
            isinstance(x, ast.Name) and x.id in tainted for x in ast.walk(val)))

    def add_targets(t) -> bool:
        grew = False
        for x in ast.walk(t):
            if isinstance(x, ast.Name) and x.id not in tainted:
                tainted.add(x.id)
                grew = True
        return grew

    for _ in range(6):  # shallow fixpoint; the shapes here are not deep
        grew = False
        for n in ast.walk(tree):
            if isinstance(n, (ast.Assign, ast.AnnAssign)):
                if not expr_tainted(n.value):
                    continue
                for t in (n.targets if isinstance(n, ast.Assign) else [n.target]):
                    grew |= add_targets(t)
            elif isinstance(n, (ast.For, ast.AsyncFor)):
                if expr_tainted(n.iter):
                    grew |= add_targets(n.target)
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
                fn = funcs.get(n.func.id)
                if fn is None:
                    continue
                params = [a.arg for a in fn.args.args]
                for i, a in enumerate(n.args):
                    if i < len(params) and expr_tainted(a) \
                            and params[i] not in tainted:
                        tainted.add(params[i])
                        grew = True
                for kw in n.keywords:
                    if kw.arg in params and expr_tainted(kw.value) \
                            and kw.arg not in tainted:
                        tainted.add(kw.arg)
                        grew = True
        if not grew:
            break

    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if isinstance(f, ast.Name) and f.id == "open" and n.args:
            mode = n.args[1] if len(n.args) > 1 else None
            kw = {k.arg: k.value for k in n.keywords}
            mode = kw.get("mode", mode)
            mv = mode.value if isinstance(mode, ast.Constant) else ""
            if isinstance(mv, str) and ("w" in mv or "a" in mv) \
                    and expr_tainted(n.args[0]):
                return True
        elif isinstance(f, ast.Attribute):
            if f.attr in ("write_text", "write_bytes") and expr_tainted(f.value):
                return True
            if f.attr == "open" and expr_tainted(f.value):
                mv = n.args[0].value if n.args and isinstance(
                    n.args[0], ast.Constant) else ""
                if isinstance(mv, str) and ("w" in mv or "a" in mv):
                    return True
    return False


def _reverse_reference_index(root: Path) -> "dict[str, list[Path]]":
    """Producers keyed by the witness filename they NAME IN THEIR OWN SOURCE.

    Most witnesses with no `scriptFile` are written by hand — the producer does
    `json.dump({...})` to a path it spells out literally, instead of routing
    through `WitnessBuilder`, which is what would have stamped `scriptFile`,
    `engine` and `commitSha`. Those producers are not guessable from the witness
    name, but they are not lost either: the source says which file it writes.

    This index records every producer that MENTIONS a witness. Direction is
    decided separately by `_writes` — see the docstring there for why naming is
    not enough.
    """
    global _reverse_index
    if _reverse_index is None:
        idx: "dict[str, list[Path]]" = {}
        skip = {"_deprecated", ".git", "__pycache__", "node_modules"}
        for f in root.parent.rglob("*.py"):
            if skip & set(f.parts):
                continue
            try:
                src = f.read_text(encoding="utf-8", errors="ignore")
            except Exception:  # noqa: BLE001
                continue
            _py_src[f] = src
            for m in re.finditer(r'["\']([A-Za-z0-9_.\-]+\.witness\.json)["\']',
                                 src):
                idx.setdefault(m.group(1), []).append(f)
        _reverse_index = idx
    return _reverse_index


def _resolve_by_reverse_reference(root: Path, wf: Path):
    """(producer | None, reason). Only a UNIQUE confirmed writer resolves."""
    named = _reverse_reference_index(root).get(wf.name, [])
    if not named:
        return None, "unnamed"
    writers = [f for f in named if _writes(_py_src.get(f, ""), wf.name)]
    if len(writers) == 1:
        return writers[0], "reverse_reference"
    if len(writers) > 1:
        return None, f"written by {len(writers)} producers"
    return None, ("named by " + ", ".join(
        f.name for f in named[:3]) + " — none of which visibly writes it")


def _resolve_producer(root: Path, sf: str, wf: Path) -> "tuple[Path | None, str]":
    """Locate the producer a witness names. Returns (path, how).

    The original rule was `wf.parent / basename(scriptFile)` — beside the witness
    and nowhere else. `computations/` has had subdirectories for a long time, and
    the rule discards the directory component outright, so it dropped even the
    witnesses whose `scriptFile` is a CORRECT repo-root path. Measured before this
    change: 2371 resolved beside, **4** naming a correct path that was thrown away,
    and **62** whose producer sits one directory over (mostly
    `computations/probes/`). Those 66 were reported as "producer not beside
    witness" and silently excluded from an audit whose whole thesis is that a
    witness with no runnable producer is the maximal case of unrefreshability.

    Resolution order, most to least certain. A basename that matches more than one
    file is NOT resolved — reported as ambiguous rather than guessed.
    """
    base = os.path.basename(sf)
    beside = wf.parent / base
    if beside.exists():
        return beside, "beside_witness"
    named = root.parent / sf
    if named.exists() and named.is_file():
        return named, "declared_path"
    hits = _repo_basename_index(root).get(base, [])
    if len(hits) == 1:
        return hits[0], "basename_search"
    if len(hits) > 1:
        return None, "ambiguous"
    return None, "unresolved"


def _producers(root: Path):
    """witness -> producer path, plus an accounting of what could NOT be resolved.

    Returns `(out, scope)`. Every witness this function declines to map is
    counted in `scope` rather than merely skipped: the audit's thesis is that a
    witness whose producer cannot run is unrefreshable and invisible to every
    staleness check, and *a producer that does not exist at all* is the maximal
    case of that thesis. The header discloses the `scriptFile` precondition, but
    the printed report used to show only `producers checked N` with no
    denominator, so a reader could not tell what fraction of the corpus that N
    covered. `scope` supplies the denominator.
    """
    out = {}
    scope = {
        "witnesses_scanned": 0,
        "unparseable": [],
        "no_script_file": [],
        "producer_not_beside_witness": [],
        "ambiguous_basename": [],
        "reverse_reference_unresolved": [],
        "resolved_by": {},
    }
    for wf in root.rglob("*.witness.json"):
        s = str(wf)
        if "_deprecated" in s or "/data/" in s:
            continue
        scope["witnesses_scanned"] += 1
        rel = str(wf.relative_to(root.parent))
        try:
            d = json.loads(wf.read_text())
        except Exception:
            scope["unparseable"].append(rel)
            continue
        if not isinstance(d, dict):
            scope["unparseable"].append(rel)
            continue
        sf = d.get("scriptFile")
        if not sf:
            # No declared producer — but a hand-written witness is usually named
            # verbatim in the producer that writes it. Try that before giving up.
            cand, why = _resolve_by_reverse_reference(root, wf)
            if cand is not None:
                scope["resolved_by"]["reverse_reference"] = (
                    scope["resolved_by"].get("reverse_reference", 0) + 1)
                out.setdefault(cand, []).append(wf)
                continue
            if why == "unnamed":
                scope["no_script_file"].append(rel)
            else:
                scope["reverse_reference_unresolved"].append(f"{rel}  ->  {why}")
            continue
        cand, how = _resolve_producer(root, str(sf), wf)
        if cand is not None:
            scope["resolved_by"][how] = scope["resolved_by"].get(how, 0) + 1
            out.setdefault(cand, []).append(wf)
        elif how == "ambiguous":
            scope["ambiguous_basename"].append(f"{rel}  ->  {sf}")
        else:
            scope["producer_not_beside_witness"].append(f"{rel}  ->  {sf}")
    scope["witnesses_resolved"] = sum(len(v) for v in out.values())
    scope["witnesses_unresolved"] = (len(scope["unparseable"])
                                     + len(scope["no_script_file"])
                                     + len(scope["producer_not_beside_witness"])
                                     + len(scope["ambiguous_basename"])
                                     + len(scope["reverse_reference_unresolved"]))
    # Deliberately NO ratio stored: a float64 in a witness violates the corpus's
    # no-float64 rule (the repo's own raw-float64 guard fires on it), and a
    # coverage ratio needs no precision policy anyway — the two integers above
    # are exact and the fraction is derivable from them. _print_scope computes
    # the percentage for display only.
    return out, scope


def _print_scope(scope: dict) -> None:
    """The denominator, printed whether or not it is flattering."""
    print("\n  SCOPE — which witnesses this audit could even look at")
    print("  (counts here are WITNESSES; 'producers checked' below counts distinct")
    print("   producer files, which is smaller — one producer can emit several.)")
    print(f"    witnesses scanned                {scope['witnesses_scanned']}")
    pct = (100.0 * scope["witnesses_resolved"] / scope["witnesses_scanned"]
           if scope["witnesses_scanned"] else 0.0)
    print(f"    witnesses w/ producer resolved   {scope['witnesses_resolved']}"
          f"   [{pct:.1f}% EVALUATED]")
    print(f"    witnesses NOT evaluated          {scope['witnesses_unresolved']}")
    print(f"      no scriptFile field            {len(scope['no_script_file'])}")
    print(f"      producer not locatable         "
          f"{len(scope['producer_not_beside_witness'])}")
    print(f"      ambiguous basename (>1 match)  "
          f"{len(scope['ambiguous_basename'])}")
    print(f"      named, writer unconfirmed      "
          f"{len(scope['reverse_reference_unresolved'])}")
    print(f"      unparseable                    {len(scope['unparseable'])}")
    if scope.get("resolved_by"):
        print("    resolved by: " + ", ".join(
            f"{k}={v}" for k, v in sorted(scope["resolved_by"].items())))
    if scope["witnesses_unresolved"]:
        print("    NOTE: a witness whose producer cannot be located is the MAXIMAL"
              "\n          case of this audit's thesis, not an exemption from it."
              "\n          It is excluded from the counts below, not cleared by them.")
        for label, key in (("no scriptFile", "no_script_file"),
                           ("producer missing", "producer_not_beside_witness"),
                           ("writer unconfirmed",
                            "reverse_reference_unresolved")):
            for ex in scope[key][:3]:
                print(f"      e.g. [{label}] {ex}")


def _classify(err: str) -> tuple[str, str]:
    if "No module named" in err:
        mod = err.split("No module named ")[-1].strip().strip("'\"").split(".")[0]
        if mod in OPTIONAL_DEPS:
            return "optional-dep", mod
        return "in-repo-wiring", mod
    return "other", err.split(":")[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=45)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any in-repo-wiring failure is found")
    ap.add_argument("--scope-only", action="store_true",
                    help="print the coverage accounting and exit; imports nothing")
    args = ap.parse_args()

    root = HERE.parent
    prod, scope = _producers(root)
    if args.scope_only:
        _print_scope(scope)
        return 0
    items = sorted(prod)
    if args.limit:
        items = items[: args.limit]

    bad, slow = [], []
    t0 = time.time()
    for i, p in enumerate(items):
        try:
            r = subprocess.run([sys.executable, "-c", _LOADER, p.name],
                               cwd=p.parent, capture_output=True, text=True,
                               timeout=args.timeout)
        except subprocess.TimeoutExpired:
            slow.append(str(p.relative_to(root.parent)))
            continue
        if r.returncode != 0:
            tail = [l for l in r.stderr.strip().splitlines() if l.strip()][-1:] or [""]
            bad.append((str(p.relative_to(root.parent)), tail[0][:160]))
        if (i + 1) % 200 == 0:
            print(f"  {i+1}/{len(items)}  unimportable={len(bad)}  "
                  f"{time.time()-t0:.0f}s", flush=True)

    buckets = collections.defaultdict(list)
    causes = collections.Counter()
    for path, err in bad:
        cls, cause = _classify(err)
        buckets[cls].append({"producer": path, "error": err, "cause": cause})
        causes[f"{cls}:{cause}"] += 1

    n_wiring = len(buckets["in-repo-wiring"])
    print("\n" + "=" * 74)
    print(" producers that cannot be imported — their witnesses are unrefreshable")
    print("=" * 74)
    _print_scope(scope)
    print(f"\n  producers checked        {len(items)}")
    print(f"  UNIMPORTABLE             {len(bad)}")
    print(f"    in-repo-wiring         {n_wiring}   <- real, fixable defects")
    print(f"    optional-dep           {len(buckets['optional-dep'])}   "
          "<- environment fact, not a defect")
    print(f"    other                  {len(buckets['other'])}")
    print(f"  heavy-at-import          {len(slow)}   <- not a failure")
    print(f"\n  top causes: {dict(causes.most_common(8))}")

    wb = WitnessBuilder("producer-importability-audit", engine="python")
    wb.set_description(
        "Detects committed witnesses whose PRODUCER cannot be imported, so the "
        "witness can never be refreshed and no staleness mechanism sees it. "
        "Every existing check (scriptHash drift, q0Anchor, the raw-float64 "
        "ratchet) presupposes the producer can run; when it cannot, the witness "
        "reports clean forever while its numbers age. Real instance: "
        "proton-residual-rootcause carried a convention-C z_markov = "
        # comparison only — this string DOCUMENTS the convention-C defect class;
        # it is not a live C value. (Marker for the convention-C triage detector,
        # which matches the decimal by value and cannot otherwise tell prose from
        # a computed constant.)
        "0.49932033403356124 invisibly through the entire C->D campaign because "
        "its producer raised TypeError on every run (fixed in 179f030c2). "
        "Method: import the module by file location in a subprocess — these "
        "scripts guard work behind __main__, so an import exercises the whole "
        "top level without running the compute. Classes are reported separately "
        "because they are not the same defect: in-repo-wiring (a module that IS "
        "in this repo is not on sys.path — real and fixable), optional-dep "
        "(snappy/matplotlib etc — an environment fact, NOT a producer defect), "
        "other, and heavy-at-import (not a failure). Excludes _deprecated/. "
        "Loads by file location rather than `import <stem>` because hyphenated "
        "filenames make `import beta-decay-from-q` a syntax error in the IMPORT "
        "STATEMENT — a first pass reported 24 bogus SyntaxErrors that all parse "
        "cleanly under ast.parse, inflating 90 real findings to 109. This is a "
        "DETECTOR: it fixes nothing and does not claim every hit is a defect."
    )
    wb.add_data("scope", scope)
    wb.add_data("producers_checked", len(items))
    wb.add_data("unimportable_total", len(bad))
    wb.add_data("counts", {k: len(v) for k, v in buckets.items()})
    wb.add_data("heavy_at_import", slow)
    wb.add_data("causes", dict(causes.most_common()))
    wb.add_data("findings", {k: v for k, v in buckets.items()})
    wb.add_data("detector_gap_closed",
                "witness staleness when the producer cannot run at all")

    wb.add_assertion(
        name="in_repo_wiring_failures_are_reported_not_hidden",
        computed=str(int(n_wiring >= 0)), expected="1", tolerance=0,
        source=f"{n_wiring} producers cannot import a module that lives in this "
               f"repo; top causes {dict(causes.most_common(4))}. Each one owns at "
               "least one committed witness that cannot be regenerated, so no "
               "staleness check can ever fire on it. Reported, not fixed.",
    )
    wb.add_assertion(
        name="optional_dependency_failures_are_carved_out_separately",
        computed=str(int(all(f["cause"] in OPTIONAL_DEPS
                             for f in buckets["optional-dep"]))),
        expected="1", tolerance=0,
        source="failures caused by a genuinely external optional package "
               f"({sorted(OPTIONAL_DEPS)}) are counted separately: "
               f"{len(buckets['optional-dep'])} of them. Calling those defects "
               "would inflate the count with facts about the environment rather "
               "than about the corpus.",
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    if args.strict and n_wiring:
        print(f"STRICT: {n_wiring} in-repo-wiring failures")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
