#!/usr/bin/env python3
"""tnjb_stale_stamp_migrate.py — regenerate the witnesses whose recorded q₀ pin
their producer can no longer reproduce, with guards against a degraded rerun.

SCOPE — the narrow, defensible slice of bean `tnjb`
    NOT the ~840-witness sweep. This targets only producers where:

      * the producer resolves to **proton** today (not in `ideal_muon`, no muon
        accessor such as `q_muon_at`, no muon artifact read), AND
      * its committed witness records **muon**.

    Those witnesses are **unreproducible**: running the producer now does not
    yield the committed value. That is a staleness defect independent of any
    anchor policy question — the witness asserts a q₀ the code no longer uses.
    Regenerating corrects a live mislabel; it does not decide anything about
    which layer a quantity *ought* to live in.

    Producers that deliberately read both layers (cross-anchor comparison
    probes importing `q_at, q_muon_at`) are NOT in scope — their muon stamp may
    be entirely correct. Excluding them is why the classifier learned to treat
    `q_muon_at` as muon evidence; without that, ~8 such probes would have been
    swept into this batch.

🛑 THE DEGRADED-RERUN HAZARD (why this script has guards at all)
    A regeneration is only trustworthy if the rerun environment can do
    everything the original could. This container is missing `scipy`,
    `pyhecke_native`, `clarabel` and `snappy`. A producer depending on any of
    them either fails loudly or — worse — takes a silent fallback path and
    writes different numbers for reasons that have nothing to do with q₀.

    So every candidate is checked BEFORE and AFTER:

      SKIP    the producer imports a missing optional dependency
      REVERT  the run failed
      REVERT  any non-environment key disappeared (data loss)
      REVERT  the `environment` block lost entries (provenance degraded)
      REVERT  `q0Anchor` did not actually flip muon -> proton
      ACCEPT  otherwise

    Reverts restore the committed file exactly. A skipped or reverted candidate
    is reported, never silently dropped.

Usage:
    python3 tnjb_stale_stamp_migrate.py --dry-run     # classify only
    python3 tnjb_stale_stamp_migrate.py --apply       # regenerate with guards
"""
from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

OPTIONAL_DEPS = ("scipy", "pyhecke_native", "pyhecke", "clarabel", "snappy",
                 "spherogram", "sage", "torch")

# Producers held out by an explicit decision, not by a guard. A held-out stem
# stays UNDETERMINED rather than becoming a DECL_MISMATCH, because its manifest
# entry is withheld too.
HOLD_OUT = {
    # Regeneration moves LP dual coordinates from exactly 0.0 to 0.0207 etc.
    # An ~11.5 ppb q0 change cannot do that -- it is a degenerate LP whose
    # optimal dual vertex is solver-dependent, and this producer only became
    # runnable here after pyhecke/clarabel/pyhecke-native were installed, so the
    # committed witness came from a different solver stack. AGENTS.md treats
    # LP/SDP duals as first-class infra; folding a changed dual vertex into an
    # ANCHOR migration would bury a substantive change inside a bookkeeping one.
    # Bean qou-pin3.
    "alpha_5_lp_dual_crystal",
}


def missing_deps() -> set[str]:
    out = set()
    for m in OPTIONAL_DEPS:
        try:
            __import__(m)
        except Exception:  # noqa: BLE001
            out.add(m)
    return out


def imports_of(path: Path) -> set[str]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return set()
    names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                names.add(a.name.split(".")[0])
        elif isinstance(n, ast.ImportFrom):
            if n.module:
                names.add(n.module.split(".")[0])
    return names


def all_keys(o, p=""):
    s = set()
    if isinstance(o, dict):
        for k, v in o.items():
            s.add(p + k)
            s |= all_keys(v, p + k + ".")
    return s


def git_show(rel: str) -> dict | None:
    try:
        raw = subprocess.check_output(["git", "show", f"HEAD:{rel}"],
                                      cwd=str(REPO), stderr=subprocess.DEVNULL)
        return json.loads(raw)
    except Exception:  # noqa: BLE001
        return None


def git_restore(rel: str) -> None:
    subprocess.run(["git", "checkout", "HEAD", "--", rel], cwd=str(REPO),
                   check=False, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


def candidates() -> list[tuple[str, Path]]:
    """(witness_rel, producer_path) for stale-stamp cases.

    Gated on the CLASSIFIER's verdict, not merely on "not declared muon".
    Without this the batch also swept in producers carrying muon evidence in
    their code -- including `y_lambda_at_q0_cache.py`, which *is* the muon cache
    AGENTS.md names as the ideal-layer source. Regenerating that one at the
    proton pin would have corrupted the artifact the whole muon layer reads
    from. Only a clean `proton` verdict (no muon accessor, no muon artifact, no
    hardcoded muon literal) is eligible.
    """
    from qou_substrate.witness import q0_anchor_is_declared, resolve_q0_anchor
    sys.path.insert(0, str(HERE))
    from q0_producer_pin_classifier import classify
    out = []
    for w in REPO.rglob("*.witness.json"):
        if ".git" in w.parts:
            continue
        try:
            b = json.loads(w.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(b, dict) or b.get("q0Anchor") != "muon":
            continue
        script = b.get("scriptFile") or b.get("script")
        if not script:
            continue
        sp = Path(str(script))
        if q0_anchor_is_declared(sp) and resolve_q0_anchor(sp)[0] == "muon":
            continue  # legitimately declared muon
        # See q0_producer_pin_classifier.find_producer: the same
        # (computations-first, fewest-parts) tie-break resolves 3 of the 7
        # colliding `.py` names to `_deprecated/`. This tool then classifies
        # the retired copy's pin and migrates a stamp on that basis.
        hits = [p for p in REPO.rglob(sp.name)
                if ".git" not in p.parts and "_deprecated" not in p.parts
                and ".claude" not in p.parts and p.is_file()]
        if not hits:
            continue
        hits.sort(key=lambda p: (0 if "computations" in p.parts else 1,
                                 len(p.parts)))
        if hits[0].stem in HOLD_OUT:
            continue  # explicit decision, see HOLD_OUT
        verdict, _ev = classify(hits[0])
        if verdict != "proton":
            continue  # muon evidence, both-layer, or symbolic -> not eligible
        out.append((str(w.relative_to(REPO)), hits[0]))
    return sorted(set(out))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args(argv)

    miss = missing_deps()
    cands = candidates()
    if args.limit:
        cands = cands[:args.limit]

    print("=" * 72)
    print("tnjb — stale-stamp migration (narrow slice)")
    print("=" * 72)
    print(f"  missing optional deps here : {sorted(miss) or 'none'}")
    print(f"  candidates                 : {len(cands)}")

    counts = {"ACCEPT": 0, "SKIP-dep": 0, "REVERT-fail": 0,
              "REVERT-dataloss": 0, "REVERT-env": 0, "REVERT-noflip": 0}
    detail: list[str] = []

    for rel, prod in cands:
        deps = imports_of(prod) & miss
        if deps:
            counts["SKIP-dep"] += 1
            detail.append(f"  SKIP-dep        {prod.name} needs {sorted(deps)}")
            continue
        if not args.apply:
            counts["ACCEPT"] += 1
            detail.append(f"  would-run       {prod.name}")
            continue

        before = git_show(rel)
        r = subprocess.run([sys.executable, "-u", prod.name], cwd=str(prod.parent),
                           capture_output=True, timeout=900)
        if r.returncode != 0:
            git_restore(rel)
            counts["REVERT-fail"] += 1
            tail = (r.stderr or b"").decode()[-90:].replace("\n", " ")
            detail.append(f"  REVERT-fail     {prod.name}: {tail}")
            continue
        try:
            after = json.loads((REPO / rel).read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            git_restore(rel)
            counts["REVERT-fail"] += 1
            detail.append(f"  REVERT-fail     {prod.name}: unreadable after run")
            continue

        if before is not None:
            lost = {k for k in all_keys(before) - all_keys(after)
                    if not k.startswith("environment")}
            if lost:
                git_restore(rel)
                counts["REVERT-dataloss"] += 1
                detail.append(f"  REVERT-dataloss {prod.name}: lost {sorted(lost)[:3]}")
                continue
            env_b = set((before.get("environment") or {}))
            env_a = set((after.get("environment") or {}))
            if env_b - env_a:
                git_restore(rel)
                counts["REVERT-env"] += 1
                detail.append(f"  REVERT-env      {prod.name}: env lost "
                              f"{sorted(env_b - env_a)}")
                continue
        if after.get("q0Anchor") != "proton":
            git_restore(rel)
            counts["REVERT-noflip"] += 1
            detail.append(f"  REVERT-noflip   {prod.name}: still "
                          f"{after.get('q0Anchor')!r}")
            continue
        counts["ACCEPT"] += 1
        detail.append(f"  ACCEPT          {prod.name}")

    for line in detail:
        print(line)
    print("\n  " + "  ".join(f"{k}={v}" for k, v in counts.items() if v))
    print("=" * 72)
    if not args.apply:
        print("dry run — nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
