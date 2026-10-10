#!/usr/bin/env python3
"""qou-cds3: re-run the remaining muon-fingerprint producers at the canonical pin.

Owner directive (2026-08-07, reaffirmed as R2 on 2026-08-15): production compute
defaults to the experimental PROTON pin. Owner authorisation for the bulk sweep
is recorded in AGENTS.md (2026-08-19): *"we want proton unless for an explicit
reason (like comparison on proton vs muon results). otherwise pin proton" /
"fix all, even if not visible."*

THE BEAN'S POPULATION FIGURE IS STALE, BY A LOT. `qou-cds3` records 870 muon
witnesses measured 2026-08-15. Re-measured on `main` 2026-08-29: **222**. Most
of the class was drained by sibling work (`qou-1c4y`, `qou-4un2`) and by the
Q0_FLIP tranche. Partitioned:

    muon-only, NOT on the legitimate ledger      107   <- actionable
    carries BOTH pins                             93   <- actionable (triage)
    legitimate muon (18-row ledger, PR #5500)     12   <- LEAVE
    declared ambiguous / comparison / independent 10   <- LEAVE

THE FOUR CONSTRAINTS from the recorded authorisation, all implemented:

  1. NEVER re-pin an anchor-DEFINING witness. `q-pinning-50-digit.witness.json`
     is what `_q0_value_for_anchor("muon")` READS; re-pinning it redefines what
     "muon" MEANS and hard-fails every ideal_muon producer. Excluded by name.
  2. The muon anchor keeps its definition -- "proton everywhere" governs what
     NEW compute pins to, not whether the muon layer still has a value.
  3. A comparison producer needs BOTH pins and is NOT a straddle. Anything on
     the legitimate-muon ledger, or declaring ambiguous/comparison/independent,
     is left alone.
  4. Do not split the change. Manifest reclassification and the witnesses it
     re-pins land together, or not at all. This script re-runs only; it makes no
     manifest edit, so there is nothing to split.

Producer resolution goes through a BASENAME INDEX: `scriptFile` is stored as a
bare basename in most witnesses and a repo-relative path in a few, so
`os.path.exists()` reports ~96% unrunnable (measured; see PR #5921).
"""
from __future__ import annotations

import argparse
import ast
import collections
import glob
import json
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MU, PR_ = "1.109978595", "1.1099785827"
ANCHOR_DEFINING = {"q_pinning_50_digit"}          # constraint 1
LEAVE_ANCHORS = {"independent", "ambiguous", "comparison"}
CORPUS_GUARDS = {"AmDifferenceInvalid", "PrecisionError", "AnchorCorruption",
                 "WitnessPrecisionError", "FreeParameterError"}


def env():
    e = dict(os.environ)
    e["PYTHONPATH"] = os.pathsep.join([
        os.path.join(REPO, "tools/qou-substrate/python"),
        os.path.join(REPO, "tools/pyhecke/python"),
        os.path.join(REPO, "computations"),
        e.get("PYTHONPATH", ""),
    ])
    return e


def ledger_stems() -> set[str]:
    p = os.path.join(REPO, "computations/audits/q0-muon-legitimate-producers.json")
    out: set[str] = set()
    try:
        d = json.load(open(p))
    except Exception:
        return out

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("stem", "producer", "script") and isinstance(v, str):
                    out.add(os.path.splitext(os.path.basename(v))[0])
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(d)
    return out


def needs_positional(path: str) -> bool:
    try:
        tree = ast.parse(open(path, encoding="utf-8").read())
    except Exception:
        return False
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "add_argument"
                and n.args and isinstance(n.args[0], ast.Constant)
                and isinstance(n.args[0].value, str)
                and not n.args[0].value.startswith("-")
                and not any(k.arg in ("nargs", "default") for k in n.keywords)):
            return True
    return False


def dirty() -> list[str]:
    r = subprocess.run(["git", "status", "--porcelain", "computations"],
                       cwd=REPO, capture_output=True, text=True)
    return [l[3:] for l in r.stdout.splitlines() if l.strip()]


def classify(out: str, rc: int, wrote: bool):
    """A non-zero exit that WROTE a witness is a completed run, not a refusal.

    Measured in PR #5927: all four "REFUSED" in the first flip drain had run to
    completion and written their witness, exiting 1 only on a failed assertion.
    Reverting them discarded four correct re-pins.
    """
    if "Traceback (most recent call last)" in out:
        last = [l for l in out.strip().splitlines() if l and not l.startswith(" ")]
        exc = last[-1].split(":")[0].strip() if last else "?"
        if exc.split(".")[-1] in CORPUS_GUARDS:
            return "GUARD", exc
        return "CRASH", exc
    if rc != 0:
        return ("OK-ASSERT-FAIL", f"exit {rc}, wrote") if wrote else ("REFUSED", f"exit {rc}")
    return "OK", ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=240)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--survey", action="store_true", help="classify only, run nothing")
    ap.add_argument("--out", default="/tmp/cds3-drain.json")
    a = ap.parse_args()

    led = ledger_stems()
    pidx: dict[str, list[str]] = {}
    for p in glob.glob(os.path.join(REPO, "computations/**/*.py"), recursive=True):
        pidx.setdefault(os.path.basename(p), []).append(p)

    cat = collections.Counter()
    producers: dict[str, list[str]] = collections.defaultdict(list)
    for p in glob.glob(os.path.join(REPO, "computations/**/*.witness.json"), recursive=True):
        if ("_deprecated" in p or "fsh-guts" in p):
            continue
        t = open(p, encoding="utf-8", errors="ignore").read()
        if MU not in t:
            continue
        try:
            d = json.loads(t)
        except Exception:
            cat["unparseable"] += 1
            continue
        sf = d.get("scriptFile") or ""
        stem = os.path.splitext(os.path.basename(sf))[0] if sf else ""
        if stem in ANCHOR_DEFINING:
            cat["anchor-defining (EXCLUDED, constraint 1)"] += 1
            continue
        if stem and stem in led:
            cat["legitimate muon (ledger, LEAVE)"] += 1
            continue
        if d.get("q0Anchor") in LEAVE_ANCHORS:
            cat[f"declared {d.get('q0Anchor')} (LEAVE)"] += 1
            continue
        if not sf:
            cat["no scriptFile — cannot re-run"] += 1
            continue
        c = pidx.get(os.path.basename(sf), [])
        if not c:
            cat["producer gone"] += 1
            continue
        cat["ACTIONABLE"] += 1
        producers[c[0]].append(p)

    print("qou-cds3 population, re-measured\n")
    for k, v in cat.most_common():
        print(f"  {k:<44} {v}")
    todo = sorted(producers)
    print(f"\n  unique producers to re-run: {len(todo)}")
    if a.survey:
        return 0
    if a.limit:
        todo = todo[:a.limit]

    verd = collections.Counter()
    rows = []
    t0 = time.time()
    for i, prod in enumerate(todo, 1):
        rel = os.path.relpath(prod, REPO)
        if needs_positional(prod):
            verd["SKIP-positional"] += 1
            continue
        before = set(dirty())
        best = None
        for cwd in (os.path.dirname(prod), REPO):
            try:
                r = subprocess.run([sys.executable, "-u", prod], cwd=cwd, env=env(),
                                   capture_output=True, text=True, timeout=a.timeout)
                out = (r.stdout or "") + (r.stderr or "")
                wrote = bool([f for f in dirty() if f not in before])
                v, det = classify(out, r.returncode, wrote)
            except subprocess.TimeoutExpired:
                v, det = "TIMEOUT", f">{a.timeout}s"
            if best is None or v.startswith("OK"):
                best = (v, det, [f for f in dirty() if f not in before])
            if v.startswith("OK"):
                break
        v, det, changed = best
        verd[v] += 1
        rows.append({"producer": rel, "verdict": v, "detail": det, "n_changed": len(changed)})
        el = time.time() - t0
        print(f"[{i}/{len(todo)}] {v:<15} {rel[:54]:<56} {len(changed)}f "
              f"[{el/60:.1f}m eta {el/i*(len(todo)-i)/60:.1f}m]", flush=True)
        if not v.startswith("OK"):
            stray = [f for f in dirty() if f not in before]
            if stray:
                subprocess.run(["git", "checkout", "--"] + stray, cwd=REPO, capture_output=True)

    json.dump({"verdicts": dict(verd), "rows": rows}, open(a.out, "w"), indent=2)
    print("\n" + "=" * 60)
    for k, n in verd.most_common():
        print(f"  {k:<18} {n}")
    print(f"  wall {(time.time()-t0)/60:.1f} min  -> {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
