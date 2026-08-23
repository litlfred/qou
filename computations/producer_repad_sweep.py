#!/usr/bin/env python3
# polynomial_q_not_applicable: build-hygiene measurement, no q-dependence.
"""Measure WHICH producers regenerate float64 padding on re-run.

Owner directive: NO FLOAT64.

`witness_float64_padding_audit.py` finds fake precision sitting in a
committed witness. `strip_float64_padding.py` removes it. Neither answers
the question that decides whether the removal *holds*: a witness is a
derived artifact, so if its producer still promotes a float to `mpf`, the
padding comes back on the next run and the strip was cosmetic.

This measures that directly rather than assuming it in either direction.
Full findings: docs/audits/2026-08-07-producer-repadding-empirical-sweep.md

**Method**, per producer, inside a throwaway git worktree:

  1. reset to pristine (git checkout + git clean)
  2. content-hash every *.witness.json
  3. run the producer under a wall timeout
  4. re-hash; a witness whose content changed was WRITTEN by this producer
  5. score padded fields on each written witness
  6. reset again, so collateral never accumulates

`is_f64_padded` is imported from the audit itself, so this sweep and the
CI gate cannot drift apart.

**A producer is CLEAN only if it ran, wrote a witness, and that witness had
zero padded fields.** One that could not run is reported untested, never
clean — the distinction is the whole point of the exercise.

**Never point this at the live checkout.** Producers write witnesses;
running 50+ of them in the working tree contaminates it. The script
refuses to run anywhere that looks like the primary checkout.

Usage:
    # from a detached worktree created for the purpose
    git worktree add --detach /tmp/sweep-wt HEAD
    python3 -u computations/producer_repad_sweep.py /tmp/sweep-wt \
        --witnesses-from HEAD --out /tmp/repad.json 2>&1 | tee /tmp/repad.log
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Share the detector with the CI gate rather than re-implementing it.
from witness_float64_padding_audit import NUMSTR, is_f64_padded  # noqa: E402


def _walk(obj, path, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            _walk(v, f"{path}.{k}" if path else k, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _walk(v, f"{path}[{i}]", out)
    elif isinstance(obj, str) and NUMSTR.match(obj.strip()):
        try:
            if is_f64_padded(obj):
                out.append(path)
        except Exception:
            pass


def padded_fields(path: Path) -> list[str]:
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    out: list[str] = []
    _walk(d, "", out)
    return out


GIT_DRIVER = re.compile(r'subprocess\.run\(\s*\[\s*["\']git["\']|\bgit\(\s*["\'](?:commit|push|add)')


def is_git_driver(path: Path) -> bool:
    """True for batch drivers that commit/push — never safe to execute here."""
    try:
        return bool(GIT_DRIVER.search(path.read_text(encoding="utf-8")))
    except Exception:
        return False


def producers_for(worktree: Path, rev: str) -> dict[str, list[str]]:
    """Map producer script -> witnesses it owns, from a commit's touched set."""
    files = subprocess.run(
        ["git", "show", "--name-only", "--format=", rev],
        cwd=worktree, capture_output=True, text=True).stdout.split()
    out: dict[str, list[str]] = {}
    for f in files:
        if not f.endswith(".witness.json"):
            continue
        p = worktree / f
        if not p.exists():
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        sf = d.get("scriptFile") or d.get("witness", {}).get("scriptFile")
        if sf:
            out.setdefault(sf, []).append(f)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("worktree", help="detached worktree to run in — NOT the live checkout")
    ap.add_argument("--witnesses-from", default="HEAD",
                    help="commit whose touched witnesses define the producer set")
    ap.add_argument("--timeout", type=int, default=150)
    ap.add_argument("--out", default="/tmp/repad_result.json")
    a = ap.parse_args()

    wt = Path(a.worktree).resolve()
    if wt == Path(__file__).resolve().parent.parent:
        print("REFUSING: that is the live checkout. Use a detached worktree.",
              file=sys.stderr)
        return 2
    comp = wt / "computations"
    if not comp.is_dir():
        print(f"no computations/ under {wt}", file=sys.stderr)
        return 2

    def sh(*args):
        return subprocess.run(args, cwd=wt, capture_output=True, text=True)

    def pristine():
        sh("git", "checkout", "--", ".")
        sh("git", "clean", "-fdq", "computations")

    def hashes():
        return {p: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(comp.rglob("*.witness.json"))}

    prod_map = producers_for(wt, a.witnesses_from)
    producers = sorted(prod_map)
    print(f"[sweep] {len(producers)} producers · timeout {a.timeout}s · worktree {wt}",
          flush=True)

    results = []
    t0 = time.time()
    for i, prod in enumerate(producers, 1):
        # `prod` is a bare `scriptFile` basename lifted out of a witness, so
        # resolve it BESIDE THE WITNESS THAT NAMES IT before falling back.
        # Producers live next to the witnesses they emit, and preferring the
        # root instead picks the wrong script whenever a basename is
        # duplicated: `witness_provenance_audit.py` exists at both
        # `computations/` and `computations/audits/`, and the witness naming it
        # is `audits/witness-provenance-audit.witness.json` — so the old
        # `comp / prod` ran the ROOT copy, which per bean qou-2r42 is a
        # DIFFERENT audit (correctness vs I14 completeness), not another copy
        # of the same one.
        #
        # The rglob fallback is sorted and refuses ambiguity: `rglob` yields in
        # os.scandir order, so `hits[0]` could pick a different script per
        # machine with nothing in the output saying which ran. Bean qou-kcii.
        src = None
        for _w in sorted(prod_map.get(prod, ())):
            cand = (wt / _w).parent / prod
            if cand.exists():
                src = cand
                break
        if src is None and (comp / prod).exists():
            src = comp / prod
        if src is None:
            hits = sorted(p for p in comp.rglob(prod)
                          if "_deprecated" not in p.parts)
            if len(hits) > 1:
                rels = [p.relative_to(wt).as_posix() for p in hits]
                print(f"[{i:3}/{len(producers)}] {prod:<58} AMBIGUOUS — "
                      + " | ".join(rels), flush=True)
                results.append({"producer": prod, "verdict": "AMBIGUOUS_BASENAME",
                                "candidates": rels})
                continue
            src = hits[0] if hits else None
        el = time.time() - t0
        eta = (el / max(i - 1, 1)) * (len(producers) - i + 1) if i > 1 else 0.0
        print(f"[{i:3}/{len(producers)}] {prod:<58} {el/60:5.1f}m elapsed · eta {eta/60:4.1f}m",
              flush=True)
        if src is None:
            results.append({"producer": prod, "verdict": "NOT_FOUND"})
            continue

        # Some scripts in computations/ are batch DRIVERS, not producers: they
        # re-run other producers and commit + push per witness. Executing one
        # from a sweep makes commits and attempts a push. q0_repin_regen_batch
        # did exactly that during this tool's own development — the throwaway
        # worktree contained it, but nothing should rely on that alone.
        if is_git_driver(src):
            print("        -> SKIPPED_DRIVER (invokes git; would commit/push)",
                  flush=True)
            results.append({"producer": prod, "verdict": "SKIPPED_DRIVER"})
            continue

        pristine()
        before = hashes()
        t1 = time.time()
        try:
            r = subprocess.run([sys.executable, "-u", str(src.relative_to(wt))],
                               cwd=wt, capture_output=True, text=True,
                               timeout=a.timeout)
            rc, err = r.returncode, (r.stderr or "")[-600:]
        except subprocess.TimeoutExpired:
            rc, err = None, "TIMEOUT"
        dur = time.time() - t1

        written = [p for p, h in hashes().items() if before.get(p) != h]
        detail, total = [], 0
        for p in written:
            f = padded_fields(p)
            total += len(f)
            detail.append({"witness": p.relative_to(wt).as_posix(),
                           "padded": len(f), "fields": f[:5]})

        # Padding written is padding written — a producer that dies partway
        # through can still have emitted a padded witness first, and several
        # do. So RE_PADS outranks the failure verdicts; scoring exit status
        # first silently understates the count (it hid 73 fields across
        # rho_k_co_casimir_extended and rho_k_h3a_lp_dual).
        incomplete = rc is None or rc != 0
        if total:
            verdict = "RE_PADS"
        elif rc is None:
            verdict = "TIMEOUT"
        elif rc != 0:
            verdict = "EXIT_NONZERO"
        elif not written:
            verdict = "NO_WRITE"
        else:
            verdict = "CLEAN"

        results.append({"producer": prod, "verdict": verdict, "rc": rc,
                        "incomplete": incomplete,
                        "seconds": round(dur, 1), "written": len(written),
                        "padded_total": total, "detail": detail,
                        "stderr_tail": "" if verdict == "CLEAN" else err})
        print(f"        -> {verdict}  wrote {len(written)}  padded {total}  ({dur:.0f}s)",
              flush=True)
        pristine()

    Path(a.out).write_text(json.dumps(results, indent=1))
    print(f"\n[sweep] {(time.time()-t0)/60:.1f}m -> {a.out}")

    c = Counter(r["verdict"] for r in results)
    print("\n=== VERDICTS ===")
    for k, v in c.most_common():
        print(f"  {k:<14} {v}")
    measured = c["RE_PADS"] + c["CLEAN"]
    partial = sum(1 for r in results
                  if r["verdict"] == "RE_PADS" and r.get("incomplete"))
    if measured:
        print(f"\n{c['RE_PADS']}/{measured} measured producers re-pad "
              f"({100*c['RE_PADS']/measured:.0f}%); "
              f"{sum(r.get('padded_total',0) for r in results)} fields regenerated")
        if partial:
            print(f"  ({partial} of those re-padded then died — padding written "
                  f"before the failure still counts)")
        print(f"{len(results)-measured} untested (could not run) — NOT clean")
    print("\n=== RE-PADDERS ===")
    for r in results:
        if r["verdict"] == "RE_PADS":
            print(f"  {r['producer']}  (+{r['padded_total']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
