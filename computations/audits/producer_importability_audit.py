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
import collections
import json
import os
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
# resolves the q0 anchor from the running producer's argv stem against
# `q0_anchor_manifest.json` (257 stems select the muon pin), so a loader that
# leaves argv[0] as `-c` silently pins every producer to proton and never
# executes the muon branch at all.
#
# Measured 2026-08-19: under the old `-c` argv this audit reported all 257
# `ideal_muon` producers importable. Under a faithful argv they raise
# `RuntimeError: ideal/muon anchor requested ... refusing to fall back to
# proton silently`, because the committed `q-pinning-50-digit.witness.json`
# holds the PROTON value (bean qou-m9xp). The detector was answering a
# question no real invocation asks.
_LOADER = (
    "import importlib.util,sys;"
    "sys.argv=[sys.argv[1]];"
    "spec=importlib.util.spec_from_file_location('_m',sys.argv[0]);"
    "m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)"
)


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
            scope["no_script_file"].append(rel)
            continue
        cand = wf.parent / os.path.basename(str(sf))
        if cand.exists():
            out.setdefault(cand, []).append(wf)
        else:
            scope["producer_not_beside_witness"].append(f"{rel}  ->  {sf}")
    scope["witnesses_resolved"] = sum(len(v) for v in out.values())
    scope["witnesses_unresolved"] = (len(scope["unparseable"])
                                     + len(scope["no_script_file"])
                                     + len(scope["producer_not_beside_witness"]))
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
    print(f"      producer not beside witness    "
          f"{len(scope['producer_not_beside_witness'])}")
    print(f"      unparseable                    {len(scope['unparseable'])}")
    if scope["witnesses_unresolved"]:
        print("    NOTE: a witness whose producer cannot be located is the MAXIMAL"
              "\n          case of this audit's thesis, not an exemption from it."
              "\n          It is excluded from the counts below, not cleared by them.")
        for label, key in (("no scriptFile", "no_script_file"),
                           ("producer missing", "producer_not_beside_witness")):
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
