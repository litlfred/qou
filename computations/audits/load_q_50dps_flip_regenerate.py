#!/usr/bin/env python3
"""load_q_50dps_flip_regenerate.py — regenerate the producers whose q₀ moved
when `load_q_50dps()`'s default flipped from the muon witness to the caller's
own resolved pin (owner decision 2026-08-08), with guards and a value audit.

WHAT MOVED
    `_li_2_q_util.load_q_50dps()` used to hand the **muon** pinning witness to
    every no-arg caller. It now resolves the caller's own pin
    (`q_parameter.Q_50_DIGIT_STR`), so a producer not declared `ideal_muon`
    computes at **proton** — an 11.537 ppb shift in q₀.

    Committed witnesses for those producers therefore record numbers their code
    no longer reproduces. This regenerates them.

    Producers declared `ideal_muon` still resolve muon and are NOT candidates:
    their values are byte-identical across the flip (verified separately by
    `--verify-muon`), because under the muon anchor `q_parameter` reads
    `Q_50_DIGIT_STR` from that same pinning witness.

GUARDS (same shape as `tnjb_stale_stamp_migrate.py`, whose hazard note applies
verbatim: a rerun is only trustworthy if this environment can do everything the
original could)

      SKIP-dep        producer imports an optional dep missing here
      REVERT-fail     the run failed, or the witness became unreadable
      REVERT-dataloss a non-`environment` key disappeared
      REVERT-env      the `environment` block lost entries
      REVERT-flip     the witness ended up stamped `muon` (it must not — these
                      producers are undeclared or `physical_proton`)
      ACCEPT          otherwise

THE VALUE AUDIT (why a diff count is not enough)
    An anchor migration is a bookkeeping change: every moved number should be
    explicable by an 11.5 ppb q₀ shift, a timing field, or a precision floor.
    A field that moves by more than that is a **substantive** change riding in
    on the migration — which is exactly how the `alpha_5_lp_dual_crystal` LP
    dual vertex change was caught during `tnjb`. Every moved numeric field is
    classified:

      timing        wall-clock and provenance keys (shas, hashes, tool versions)
      precision     both sides under the numeric-zero floor, 1e-40 — the corpus's
                    own assertion tolerances run to there, so `5.4e-71 -> 0.0`
                    is noise, not a change
      q0-scale      |Δrel| ≤ 1e-7 — the 1.15e-8 separation plus ordinary
                    arithmetic on top of it
      q0-amplified  up to 1000x the separation, with the factor PRINTED. Binding
                    energies come out of exponentials and cumulants out of
                    near-cancellations, so a few-hundred-fold gain is ordinary —
                    but the reader gets the number instead of a threshold the
                    author picked.
      UNEXPLAINED   anything else → reported loudly, and `--strict` exits 1

    Fields are compared as real OR complex (producers store complex results as
    mpmath reprs); a bare `float()` sent those to UNEXPLAINED on the first pass.

Usage:
    python3 load_q_50dps_flip_regenerate.py --dry-run
    python3 load_q_50dps_flip_regenerate.py --verify-muon
    python3 load_q_50dps_flip_regenerate.py --apply [--strict]
    python3 load_q_50dps_flip_regenerate.py --audit-only   # classify, no rerun
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent

OPTIONAL_DEPS = ("scipy", "pyhecke_native", "pyhecke", "clarabel", "snappy",
                 "spherogram", "sage", "torch")

# Fields that differ between ANY two runs and are not results: wall-clock, and
# the provenance block (commit shas, script hashes, upstream-witness hashes,
# tool versions). Classifying these as value changes buried the real movers
# under 60+ false alarms on the first pass.
TIMING_HINTS = ("durationms", "elapsed", "wall", "computedat", "seconds",
                "runtime", "timing", "commitsha", "scripthash", "sha256",
                "size_bytes", "timestamp", "generated", "engineversion",
                "environment.", "description")

# The muon/proton layer separation itself.
Q0_SEPARATION = 1.1537118e-8

# Direct q₀-scale movement: at or below the separation, plus a decade of slack
# for ordinary arithmetic on top of it.
Q0_SCALE_TOL = 1e-7

# Beyond that a field can still be the q₀ shift AMPLIFIED — binding energies
# come out of exponentials, cumulant corrections out of differences of nearly
# equal terms, so a few-hundred-fold gain is ordinary. Report the amplification
# factor rather than widening the threshold and calling it explained: a number
# the reader can check beats a tolerance the author chose.
Q0_AMPLIFY_MAX = 1000.0

# Producers held out by an explicit decision, not by a guard — the same
# discipline `tnjb_stale_stamp_migrate.HOLD_OUT` applies.
HOLD_OUT = {
    # Committed witness is stale by ~5 ORDERS OF MAGNITUDE on `T1_atom`
    # (D: 4.5283 vs 3.06e-05), and the staleness has nothing to do with q₀.
    # Proven by a three-way run: pre-flip and post-flip produce
    # BIT-IDENTICAL T1 values, and both differ from the committed witness.
    # So the producer's T1 changed at some point and the witness was never
    # regenerated. Folding a 5-order correction into an anchor-bookkeeping
    # commit would bury it exactly the way the `alpha_5_lp_dual_crystal` LP
    # dual vertex nearly rode in on `tnjb`. Bean qou-pin6.
    "pentagon_reduction_li2q",
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
        elif isinstance(n, ast.ImportFrom) and n.module:
            names.add(n.module.split(".")[0])
    return names


def all_keys(o, p=""):
    s = set()
    if isinstance(o, dict):
        for k, v in o.items():
            s.add(p + k)
            s |= all_keys(v, p + k + ".")
    return s


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


def _delta(a, b) -> tuple[float, float] | None:
    """(|b − a|, max(|a|,|b|)) for real or complex string fields."""
    for cast in (float, complex):
        try:
            xa, xb = cast(str(a).strip().strip("()").replace(" ", "")), \
                     cast(str(b).strip().strip("()").replace(" ", ""))
        except (TypeError, ValueError):
            continue
        return abs(xb - xa), max(abs(xa), abs(xb))
    return None


_NUM = re.compile(r"[-+]?\d+\.?\d*(?:[eE][-+]?\d+)?")


def _prose(a, b) -> tuple[str, float | None] | None:
    """Classify two differing PROSE strings by their embedded numerals.

    Verdict fields in this corpus quote their own results — "the proton tower
    Im = 0.656782298853 (nonzero)". A q₀ shift moves the quoted number and
    nothing else, which a numeric parser cannot see and which should not read as
    an unexplained change. But an edit to the surrounding wording IS worth
    flagging, so the two are separated: identical skeleton + numerals that moved
    at q₀ scale is explained; anything else is not.
    """
    if not (isinstance(a, str) and isinstance(b, str)):
        return None
    na, nb = _NUM.findall(a), _NUM.findall(b)
    if len(na) != len(nb) or not na:
        return None
    if _NUM.sub("#", a) != _NUM.sub("#", b):
        return None                      # the WORDS changed, not just the values
    worst = 0.0
    for x, y in zip(na, nb):
        try:
            fx, fy = float(x), float(y)
        except ValueError:
            return None
        d = max(abs(fx), abs(fy))
        if d < 1e-40:
            continue
        worst = max(worst, abs(fy - fx) / d)
    if worst <= Q0_SCALE_TOL:
        return "q0-scale", worst
    if worst <= Q0_SEPARATION * Q0_AMPLIFY_MAX:
        return "q0-amplified", worst
    return None


def classify(key: str, a, b) -> tuple[str, float | None]:
    """Classify a moved field. Returns (bucket, relative change)."""
    kl = key.lower()
    if any(h in kl for h in TIMING_HINTS):
        return "timing", None
    if isinstance(a, bool) or isinstance(b, bool):
        return ("identical", 0.0) if a == b else ("UNEXPLAINED", None)
    d = _delta(a, b)
    if d is None:
        p = _prose(a, b)
        return p if p is not None else ("UNEXPLAINED", None)
    diff, denom = d
    if diff == 0:
        return "identical", 0.0
    # Both sides under the corpus's numeric-zero floor (assertion tolerances
    # here run to 1e-40). `5.4e-71 -> 0.0` is |Δrel| = 1.0 and means nothing.
    if denom < 1e-40:
        return "precision", 0.0
    rel = diff / denom
    if rel <= Q0_SCALE_TOL:
        return "q0-scale", rel
    if rel <= Q0_SEPARATION * Q0_AMPLIFY_MAX:
        return "q0-amplified", rel
    return "UNEXPLAINED", rel


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


def _stems(flag: str) -> list[str]:
    r = subprocess.run([sys.executable, str(HERE / "load_q_50dps_caller_layers.py"),
                        flag], capture_output=True, text=True, cwd=str(REPO))
    return sorted({l.strip() for l in r.stdout.splitlines() if l.strip()})


def _producer(stem: str) -> Path | None:
    for p in COMPUTE_DIR.rglob(f"{stem}.py"):
        if "_deprecated" not in p.parts:
            return p
    return None


def _witness_for(stem: str) -> tuple[str, Path] | None:
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
            return str(w.relative_to(REPO)), w
    return None


def _run(prod: Path, timeout: int) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-u", prod.name], cwd=str(prod.parent),
                          capture_output=True, timeout=timeout)


def verify_muon(timeout: int) -> int:
    """The 7 muon-resolved callers must be byte-identical across the flip."""
    print("=" * 72)
    print("verify-muon — declared `ideal_muon` callers must not move")
    print("=" * 72)
    miss = missing_deps()
    ok = moved = skipped = 0
    for stem in _stems("--muon-resolved-only"):
        prod = _producer(stem)
        w = _witness_for(stem)
        if prod is None or w is None:
            print(f"  no-witness  {stem}")
            skipped += 1
            continue
        rel, path = w
        deps = imports_of(prod) & miss
        if deps:
            print(f"  SKIP-dep    {stem} needs {sorted(deps)}")
            skipped += 1
            continue
        before = path.read_text(encoding="utf-8")
        try:
            r = _run(prod, timeout)
        except subprocess.TimeoutExpired:
            print(f"  SKIP-slow   {stem} (> {timeout}s)")
            skipped += 1
            continue
        if r.returncode != 0:
            git_restore(rel)
            print(f"  SKIP-fail   {stem}: "
                  f"{(r.stderr or b'').decode()[-80:]!r}")
            skipped += 1
            continue
        after = path.read_text(encoding="utf-8")
        b, a = json.loads(before), json.loads(after)
        fb, fa = flat(b), flat(a)
        diff = [k for k in set(fb) & set(fa)
                if fb[k] != fa[k]
                and classify(k, fb[k], fa[k])[0] not in ("timing", "identical")]
        git_restore(rel)
        if diff:
            moved += 1
            print(f"  MOVED       {stem}: {sorted(diff)[:4]}")
        else:
            ok += 1
            print(f"  unchanged   {stem}")
    print(f"\n  unchanged={ok}  MOVED={moved}  skipped={skipped}")
    if moved:
        print("\n  🛑 A muon-declared caller moved. The flip was supposed to be")
        print("     a no-op for these — check `Q_50_DIGIT_STR` under the muon")
        print("     anchor still equals the pinning witness's `derived_50_digit.q`.")
    print("=" * 72)
    return 1 if moved else 0


def audit_only(args) -> int:
    """Classify the committed-vs-working-tree diff without re-running anything.

    This is the TOTAL diff — the q₀ flip plus whatever staleness the committed
    witness already carried. Use `load_q_50dps_flip_ab.py --movers` to isolate
    the flip's own contribution; the two answer different questions and the
    total is the one that lands in the commit.
    """
    stems = [s for s in _stems("--movers-only") if s not in HOLD_OUT]
    if args.only:
        want = {s.strip() for s in args.only.split(",") if s.strip()}
        stems = [s for s in stems if s in want]

    print("=" * 72)
    print("VALUE AUDIT — committed (HEAD) vs working tree, every moved field")
    print("=" * 72)
    for h in sorted(HOLD_OUT):
        print(f"  HELD OUT: {h}")
    unexplained = 0
    for stem in stems:
        w = _witness_for(stem)
        if w is None:
            continue
        rel, path = w
        before = git_show(rel)
        if before is None:
            continue
        try:
            after = json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        fb, fa = flat(before), flat(after)
        buckets: dict[str, int] = {}
        worst = 0.0
        bad: list[tuple[str, float | None]] = []
        for k in sorted(set(fb) & set(fa)):
            if fb[k] == fa[k]:
                continue
            bucket, relc = classify(k, fb[k], fa[k])
            if bucket in ("timing", "identical"):
                continue
            buckets[bucket] = buckets.get(bucket, 0) + 1
            if relc:
                worst = max(worst, relc)
            if bucket == "UNEXPLAINED":
                bad.append((k, relc))
        summ = " ".join(f"{k}={v}" for k, v in sorted(buckets.items())) or "no change"
        amp = f"  = {worst / Q0_SEPARATION:,.0f}x q0-sep" if worst else ""
        print(f"  {stem:<56} {summ}  (max |Δrel| {worst:.3e}{amp})")
        for k, relc in bad:
            unexplained += 1
            print(f"      🛑 {k}  |Δrel|="
                  f"{'n/a' if relc is None else f'{relc:.3e}'}")
    if unexplained:
        print(f"\n  🛑 {unexplained} field(s) moved by more than an 11.5 ppb q₀ shift")
        print("     can account for. Each needs an explanation before commit.")
    else:
        print("\n  ✅ Every moved field is explained by the q₀ shift, a timing or")
        print("     provenance field, or the numeric-zero floor.")
    print("=" * 72)
    return 1 if (args.strict and unexplained) else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify-muon", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any moved field is UNEXPLAINED")
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--only", default="", help="comma-separated stems")
    ap.add_argument("--audit-only", action="store_true",
                    help="classify HEAD vs the working tree without re-running")
    args = ap.parse_args(argv)

    if args.verify_muon:
        return verify_muon(args.timeout)
    if args.audit_only:
        return audit_only(args)

    miss = missing_deps()
    stems = [s for s in _stems("--movers-only") if s not in HOLD_OUT]
    if args.only:
        want = {s.strip() for s in args.only.split(",") if s.strip()}
        stems = [s for s in stems if s in want]

    print("=" * 72)
    print("load_q_50dps flip — guarded regeneration of the moved producers")
    print("=" * 72)
    print(f"  missing optional deps here : {sorted(miss) or 'none'}")
    print(f"  movers                     : {len(stems)}")

    counts: dict[str, int] = {}
    detail: list[str] = []
    audit: dict[str, list[tuple[str, float | None]]] = {}

    def bump(k):
        counts[k] = counts.get(k, 0) + 1

    for stem in stems:
        prod = _producer(stem)
        if prod is None:
            bump("SKIP-nofile")
            detail.append(f"  SKIP-nofile     {stem}")
            continue
        w = _witness_for(stem)
        if w is None:
            bump("SKIP-nowitness")
            detail.append(f"  SKIP-nowitness  {stem} (nothing committed to move)")
            continue
        rel, path = w
        deps = imports_of(prod) & miss
        if deps:
            bump("SKIP-dep")
            detail.append(f"  SKIP-dep        {stem} needs {sorted(deps)}")
            continue
        if not args.apply:
            bump("would-run")
            detail.append(f"  would-run       {stem}  -> {rel}")
            continue

        before = git_show(rel)
        try:
            r = _run(prod, args.timeout)
        except subprocess.TimeoutExpired:
            git_restore(rel)
            bump("REVERT-timeout")
            detail.append(f"  REVERT-timeout  {stem} (> {args.timeout}s)")
            continue
        if r.returncode != 0:
            git_restore(rel)
            bump("REVERT-fail")
            tail = (r.stderr or b"").decode()[-90:].replace("\n", " ")
            detail.append(f"  REVERT-fail     {stem}: {tail}")
            continue
        try:
            after = json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            git_restore(rel)
            bump("REVERT-fail")
            detail.append(f"  REVERT-fail     {stem}: unreadable after run")
            continue

        if before is not None:
            lost = {k for k in all_keys(before) - all_keys(after)
                    if not k.startswith("environment")}
            if lost:
                git_restore(rel)
                bump("REVERT-dataloss")
                detail.append(f"  REVERT-dataloss {stem}: lost {sorted(lost)[:3]}")
                continue
            env_b = set(before.get("environment") or {})
            env_a = set(after.get("environment") or {})
            if env_b - env_a:
                git_restore(rel)
                bump("REVERT-env")
                detail.append(f"  REVERT-env      {stem}: lost {sorted(env_b - env_a)}")
                continue

        prov = after.get("provenance") if isinstance(after.get("provenance"), dict) else {}
        pin = prov.get("q0Anchor") or after.get("q0Anchor")
        if pin == "muon":
            git_restore(rel)
            bump("REVERT-flip")
            detail.append(f"  REVERT-flip     {stem}: stamped muon, must not be")
            continue

        moved: list[tuple[str, float | None]] = []
        if before is not None:
            fb, fa = flat(before), flat(after)
            for k in sorted(set(fb) & set(fa)):
                if fb[k] == fa[k]:
                    continue
                bucket, relc = classify(k, fb[k], fa[k])
                if bucket in ("timing", "identical"):
                    continue
                moved.append((f"{bucket}:{k}", relc))
        audit[stem] = moved
        bad = [m for m in moved if m[0].startswith("UNEXPLAINED")]
        bump("ACCEPT")
        detail.append(f"  ACCEPT          {stem}: {len(moved)} field(s) moved"
                      + (f", {len(bad)} UNEXPLAINED" if bad else ""))

    for line in detail:
        print(line)
    print("\n  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))

    unexplained = 0
    if args.apply:
        print("\n" + "-" * 72)
        print("  VALUE AUDIT — every moved field, classified")
        print("-" * 72)
        for stem, moved in sorted(audit.items()):
            buckets: dict[str, int] = {}
            worst = 0.0
            for name, relc in moved:
                b = name.split(":", 1)[0]
                buckets[b] = buckets.get(b, 0) + 1
                if relc:
                    worst = max(worst, relc)
            summ = " ".join(f"{k}={v}" for k, v in sorted(buckets.items())) or "none"
            print(f"    {stem:<56} {summ}  (max |Δrel| {worst:.3e})")
            for name, relc in moved:
                if name.startswith("UNEXPLAINED"):
                    unexplained += 1
                    print(f"        🛑 {name}  |Δrel|="
                          f"{'n/a' if relc is None else f'{relc:.3e}'}")
        if unexplained:
            print(f"\n  🛑 {unexplained} UNEXPLAINED field change(s): larger than an")
            print("     11.5 ppb q₀ shift can account for. Each is a substantive")
            print("     change riding in on a bookkeeping migration — triage before")
            print("     committing, do not fold it into the anchor change.")
        else:
            print("\n  ✅ Every moved field is explained by the q₀ shift, a timing")
            print("     field, or the 50-dps precision floor.")
    print("=" * 72)
    if not args.apply:
        print("dry run — nothing written. Re-run with --apply.")
    return 1 if (args.strict and unexplained) else 0


if __name__ == "__main__":
    raise SystemExit(main())
