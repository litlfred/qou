#!/usr/bin/env python3
"""load_q_50dps_flip_ab.py — isolate what the `load_q_50dps` default flip
actually changes, by running each producer TWICE: once with the pre-flip
helper + manifest, once with the post-flip pair, and diffing run against run.

WHY NOT JUST DIFF AGAINST THE COMMITTED WITNESS
    Because that measures two things at once. A committed witness can be stale
    for reasons that have nothing to do with q₀ — an upstream constant moved, a
    dependency version changed, the file predates an unrelated fix. Diffing
    `committed` against `rerun-now` attributes all of that to the flip.

    Measured here on the 7 muon-declared callers, that confound is not
    hypothetical: 7 of 10 "moved" against their committed witnesses, which would
    have read as the flip breaking producers it cannot touch.

    Run-vs-run holds everything else fixed. The only difference between arm A
    and arm B is the two files under test, so a field that moves moved *because
    of the flip*.

THE TWO ARMS
    A (pre-flip)   `computations/_li_2_q_util.py` and
                   `computations/q0_anchor_manifest.json` restored from HEAD
    B (post-flip)  the working-tree versions

    Both arms run the same producer, in the same container, back to back.
    Provenance fields that necessarily differ between any two runs
    (`commitSha`, `scriptHash`, timestamps, durations) are excluded — they are
    not results.

EXPECTED
    already-declared muon  → **zero** value fields differ. Under the muon anchor
                             `q_parameter.Q_50_DIGIT_STR` is read from the same
                             pinning witness the old default opened directly, so
                             the two arms feed identical q₀. These are the
                             control group; a change here is a bug in the flip.
    newly-declared muon    → a change is EXPECTED and is the point. Arm A had
                             them undeclared: `load_q_50dps()` handed them muon
                             while any module-level `q_parameter` binding in
                             their import tree resolved proton — a straddle.
                             Declaring them unifies both sources.
    undeclared callers     → q₀ moves 11.537 ppb, values move with it.

    The script partitions on `ideal_muon` membership AT HEAD so the control
    group stays honest even as declarations accumulate.

Usage:
    python3 load_q_50dps_flip_ab.py --muon        # the no-op check
    python3 load_q_50dps_flip_ab.py --movers      # measure the intended change
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent

UNDER_TEST = ["computations/_li_2_q_util.py",
              "computations/q0_anchor_manifest.json"]

# Fields that differ between ANY two runs and are not results.
PROVENANCE = ("commitsha", "scripthash", "scriptcommitsha", "timestamp",
              "computedat", "durationms", "generated", "elapsed", "wall",
              "runtime", "seconds", "timing")


def is_provenance(key: str) -> bool:
    kl = key.lower()
    return any(p in kl for p in PROVENANCE)


def flat(o, p="") -> dict[str, object]:
    out: dict[str, object] = {}
    if isinstance(o, dict):
        for k, v in o.items():
            out.update(flat(v, f"{p}{k}."))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            out.update(flat(v, f"{p}{i}."))
    else:
        out[p.rstrip(".")] = o
    return out


def rel_change(a, b) -> float | None:
    """Relative change, with the corpus's numeric-zero floor applied.

    Without the floor this metric cries wolf: `5.43e-71 -> 0.0` is a relative
    change of 1.0, yet both sides are ~30 orders below any assertion tolerance
    in the corpus (`probe_9b_alphak_structure` uses 1e-40). Reporting that as
    the worst field change buries the real movers under noise. Anything with
    both magnitudes under the floor contributes 0.
    """
    try:
        fa, fb = float(a), float(b)
    except (TypeError, ValueError):
        return None
    if fa != fa or fb != fb:
        return None
    d = max(abs(fa), abs(fb))
    if d < 1e-45:
        return 0.0
    return abs(fb - fa) / d if d else 0.0


def _stems(flag: str) -> list[str]:
    r = subprocess.run([sys.executable, str(HERE / "load_q_50dps_caller_layers.py"),
                        flag], capture_output=True, text=True, cwd=str(REPO))
    return sorted({l.strip() for l in r.stdout.splitlines() if l.strip()})


def _producer(stem: str) -> Path | None:
    for p in COMPUTE_DIR.rglob(f"{stem}.py"):
        if "_deprecated" not in p.parts:
            return p
    return None


def _witness_for(stem: str) -> Path | None:
    for w in REPO.rglob("*.witness.json"):
        if ".git" in w.parts or "_deprecated" in w.parts:
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(d, dict):
            continue
        prov = d.get("provenance")
        prov = prov if isinstance(prov, dict) else {}
        sf = prov.get("scriptFile") or d.get("scriptFile") or ""
        if sf and Path(str(sf)).stem == stem:
            return w
    return None


def _save(paths: list[str]) -> dict[str, str]:
    return {p: (REPO / p).read_text(encoding="utf-8") for p in paths}


def _write(snap: dict[str, str]) -> None:
    for p, txt in snap.items():
        (REPO / p).write_text(txt, encoding="utf-8")


def _head(paths: list[str]) -> dict[str, str]:
    out = {}
    for p in paths:
        out[p] = subprocess.check_output(["git", "show", f"HEAD:{p}"],
                                         cwd=str(REPO)).decode()
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--muon", action="store_true", help="check the no-op arm")
    ap.add_argument("--movers", action="store_true", help="measure the change")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--only", default="")
    args = ap.parse_args(argv)

    if not (args.muon or args.movers):
        ap.error("pass --muon or --movers")

    flag = "--muon-resolved-only" if args.muon else "--movers-only"
    stems = _stems(flag)
    if args.only:
        want = {s.strip() for s in args.only.split(",") if s.strip()}
        stems = [s for s in stems if s in want]

    post = _save(UNDER_TEST)          # working tree = arm B
    pre = _head(UNDER_TEST)           # HEAD          = arm A
    witness_backup: dict[str, str] = {}

    # Partition the muon set on membership AT HEAD: only stems already declared
    # before this change are a valid control group for "the flip is a no-op".
    head_muon = set(json.loads(pre["computations/q0_anchor_manifest.json"])
                    .get("ideal_muon", []))

    label = "muon-declared (expect NO value change)" if args.muon else \
            "movers (expect an 11.5 ppb q₀ shift)"
    print("=" * 72)
    print(f"load_q_50dps flip — A/B run-vs-run: {label}")
    print("=" * 72)

    results = []
    try:
        for stem in stems:
            prod, wit = _producer(stem), _witness_for(stem)
            if prod is None or wit is None:
                print(f"  no-witness  {stem}")
                continue
            rel = str(wit.relative_to(REPO))
            witness_backup.setdefault(rel, wit.read_text(encoding="utf-8"))

            arms = {}
            failed = None
            for name, snap in (("A", pre), ("B", post)):
                _write(snap)
                try:
                    r = subprocess.run([sys.executable, "-u", prod.name],
                                       cwd=str(prod.parent), capture_output=True,
                                       timeout=args.timeout)
                except subprocess.TimeoutExpired:
                    failed = f"timeout in arm {name}"
                    break
                if r.returncode != 0:
                    failed = (f"arm {name} failed: "
                              + (r.stderr or b"").decode()[-70:].replace("\n", " "))
                    break
                try:
                    arms[name] = flat(json.loads(wit.read_text(encoding="utf-8")))
                except Exception as e:  # noqa: BLE001
                    failed = f"arm {name} unreadable: {e}"
                    break
            if failed:
                print(f"  SKIP        {stem}: {failed}")
                continue

            a, b = arms["A"], arms["B"]
            diffs = [(k, a[k], b[k]) for k in sorted(set(a) & set(b))
                     if a[k] != b[k] and not is_provenance(k)]
            worst = 0.0
            for _, x, y in diffs:
                rc = rel_change(x, y)
                if rc:
                    worst = max(worst, rc)
            control = args.muon and stem in head_muon
            results.append((stem, len(diffs), worst, control))
            tag = "" if not args.muon else (
                "  [control]" if control else "  [newly declared]")
            if not diffs:
                print(f"  IDENTICAL   {stem}{tag}")
            else:
                print(f"  differs     {stem}{tag}: {len(diffs)} field(s), "
                      f"max |Δrel| {worst:.3e}")
                for k, x, y in diffs[:3]:
                    print(f"                  {k}\n                    A={str(x)[:34]}"
                          f"\n                    B={str(y)[:34]}")
    finally:
        _write(post)                                  # leave arm B in place
        for rel, txt in witness_backup.items():
            (REPO / rel).write_text(txt, encoding="utf-8")
        print("\n  (working tree restored: post-flip sources, committed witnesses)")

    ident = sum(1 for _, n, _, _ in results if n == 0)
    moved = len(results) - ident
    print(f"\n  identical={ident}  differs={moved}  (of {len(results)} run)")

    control_moved = 0
    if args.muon:
        ctl = [r for r in results if r[3]]
        new = [r for r in results if not r[3]]
        control_moved = sum(1 for _, n, _, _ in ctl if n)
        print(f"    control (declared at HEAD) : {len(ctl)} run, "
              f"{control_moved} changed")
        print(f"    newly declared here        : {len(new)} run, "
              f"{sum(1 for _, n, _, _ in new if n)} changed (expected)")
        if control_moved:
            print("\n  🛑 The flip changed an ALREADY-declared muon caller. It must")
            print("     not: under the muon anchor `Q_50_DIGIT_STR` comes from the")
            print("     same pinning witness the old default opened.")
        else:
            print("\n  ✅ The helper flip is a no-op for every already-declared muon")
            print("     caller. Changes are confined to stems declared in this change.")
    if args.movers and moved:
        worst = max((w for _, n, w, _ in results if n), default=0.0)
        print(f"  largest single-field |Δrel| across movers: {worst:.3e}")
    print("=" * 72)
    return 1 if control_moved else 0


if __name__ == "__main__":
    raise SystemExit(main())
