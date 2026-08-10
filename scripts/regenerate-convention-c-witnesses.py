#!/usr/bin/env python3
"""Regenerate every witness still carrying a convention-C fingerprint.

The producers are all convention D (`convention-c-producer-audit.py` reports 0
actionable sites); their committed outputs are not. This closes that gap by
re-running each producer and recording exactly how far every number moved.

## Constraints this is built around

**Strictly serial.** Standing owner directive: never two producers concurrently
in one checkout. They share caches, witness paths and sys.path mutations.

**Resumable.** The container is ephemeral and has died mid-task twice at roughly
an hour each. One JSONL line is appended after *every* producer, and a resume
skips whatever is already recorded. A restart costs one producer, not the run.

**Nothing hand-edited.** Every number that lands in a witness comes from a
producer run. This script never writes into a witness itself.

## Reading the deltas

Three kinds of change come out of this and conflating them would make the report
meaningless:

* **structural zero** — a value that becomes exactly `0`. Under convention D
  every `y_λ` with `ℓ(λ) ≥ 3` vanishes identically; that is what the convention
  *is*, not a numerical shift, and reporting it as "−100 %" would be noise.
* **shift** — a genuine relative move. Reported in ppm. This is the physics.
* **q0-refresh** — a move at roughly the 9th significant digit with no
  convention content, from a witness that was simply stale against its q₀.
  Classified separately because a witness regenerated *before* its producer was
  migrated moves only this much and looks superficially like a result.

## Usage

    python3 scripts/regenerate-convention-c-witnesses.py --plan
    python3 scripts/regenerate-convention-c-witnesses.py --run [--timeout 900]
    python3 scripts/regenerate-convention-c-witnesses.py --report
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pathlib
import re
import signal
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
LOG = REPO / ".work" / "convention-c-regen.jsonl"

#: Convention-C fingerprints, from the registry.
C_FINGERPRINTS = ["0.49932033418369", "0.41539579536", "0.2809296", "0.02274491"]

#: Fields that churn on every run and carry no numeric meaning.
VOLATILE = {"computedAt", "durationMs", "scriptHash", "commitSha",
            "scriptCommitSha", "engineVersion", "hostname", "elapsed",
            "elapsedMs", "timestamp", "generatedAt"}

NUM = re.compile(r"-?\d+\.\d{6,}(?:[eE][+-]?\d+)?")

#: sys.path additions producers expect. ABSOLUTE, deliberately.
#:
#: These were relative on the first run ("..", "../tools/pyhecke/python"), which
#: is correct only for a producer sitting directly in `computations/`. Each
#: producer runs from its OWN directory, so for `computations/alpha/foo.py` the
#: entry `../tools/pyhecke/python` resolved to `computations/tools/...` and the
#: producer died with `ModuleNotFoundError: No module named 'pyhecke'`. Four
#: failures were the harness's fault, not the producer's — which is exactly the
#: kind of thing that would otherwise be written up as "pre-existing breakage".
SYS_PATHS = [str(REPO / "computations" / d) if d else str(REPO / "computations")
             for d in ("", "substrate", "hecke", "markov", "alpha", "probes",
                       "qbeta", "deltalambda", "phase5", "sweeps", "audits")] + [
    str(REPO / "tools" / "pyhecke" / "python"),
    str(REPO / "tools" / "qou-substrate" / "python"),
    str(REPO / "qou-mass" / "src"),
]


def numeric_fields(obj, out=None, path=""):
    """Flatten every high-precision number in a witness, keyed by JSON path."""
    out = {} if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in VOLATILE:
                continue
            numeric_fields(v, out, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            numeric_fields(v, out, f"{path}[{i}]")
    elif isinstance(obj, str):
        for m in NUM.findall(obj):
            out.setdefault(path, []).append(m)
    elif isinstance(obj, float):
        out.setdefault(path, []).append(repr(obj))
    elif isinstance(obj, int) and obj == 0:
        out.setdefault(path, []).append("0")
    return out


def snapshot(witness: pathlib.Path):
    try:
        raw = witness.read_text()
    except OSError:
        return {"exists": False}
    try:
        doc = json.loads(raw)
    except json.JSONDecodeError:
        doc = {}
    return {
        "exists": True,
        "sha256": hashlib.sha256(raw.encode()).hexdigest()[:16],
        "c_fingerprint": any(c in raw for c in C_FINGERPRINTS),
        "numbers": numeric_fields(doc),
    }


#: Below this a value is numerically indistinguishable from zero, so a RELATIVE
#: change against it is meaningless — dividing by something at the level of
#: machine noise manufactures astronomical ppm. The first draft of this report
#: led with "1.3e20 ppm" for 3.47e-18 -> 4.6e-4, which is not a physics result,
#: it is a division by epsilon.
NOISE_FLOOR = 1e-12


def classify(before: str, after: str):
    """Return (kind, relative_change) for one value.

    Kinds, and why each is kept separate:

    ``structural_zero``  became exactly 0. Convention D sends every ``y_lambda``
                         with ``ell(lambda) >= 3`` to zero identically; that is
                         the convention working, not a shift, and rendering it
                         as "-100%" would drown the real numbers.
    ``emerged``          was at or below the noise floor, now is not. A
                         quantity that was numerically zero acquiring a value is
                         a qualitative change and no ppm describes it.
    ``vanished``         the reverse: was real, now at the noise floor without
                         being exactly zero.
    ``noise``            both sides at the floor. Nothing happened.
    ``q0_refresh``       moved by less than 1e-7 relative, roughly the ninth
                         digit. No convention content -- a witness simply stale
                         against its q0. Kept separate because a witness
                         regenerated BEFORE its producer was migrated moves
                         exactly this much and looks like a result.
    ``shift``            a genuine relative move, reported in ppm. The physics.
    """
    try:
        b, a = float(before), float(after)
    except ValueError:
        return ("unparseable", None)
    if b == a:
        return ("same", 0.0)
    if a == 0.0:
        return ("structural_zero", None)
    if abs(b) <= NOISE_FLOOR < abs(a):
        return ("emerged", None)
    if abs(a) <= NOISE_FLOOR < abs(b):
        return ("vanished", None)
    if abs(b) <= NOISE_FLOOR and abs(a) <= NOISE_FLOOR:
        return ("noise", None)
    rel = abs(a - b) / abs(b)
    if rel < 1e-7:                      # ~digit 8 and below
        return ("q0_refresh", rel)
    return ("shift", rel)


def diff(before: dict, after: dict):
    nb = before.get("numbers", {}) or {}
    na = after.get("numbers", {}) or {}
    rows = []
    for key in sorted(set(nb) | set(na)):
        xs, ys = nb.get(key, []), na.get(key, [])
        for i in range(max(len(xs), len(ys))):
            x = xs[i] if i < len(xs) else None
            y = ys[i] if i < len(ys) else None
            if x is None or y is None or x == y:
                continue
            kind, rel = classify(x, y)
            if kind == "same":
                continue
            rows.append({"field": key, "before": x, "after": y,
                         "kind": kind, "rel": rel})
    return rows


def _is_convention_c(raw: str, doc) -> bool:
    """Is this witness convention C?

    TWO tests, because the first one is not sufficient and I shipped a campaign
    that assumed it was.

    1. **Fingerprint** — the witness contains a known convention-C decimal.
       Those constants are the `n = 3` values (`z_C` and the three `y_λ` at
       three strands), so this catches nothing computed at `n = 6`, `9` or `12`.

    2. **Structural** — the witness records a nonzero `y_λ` on a partition with
       three or more rows. Under convention D every such weight is *exactly*
       zero (Schur-Weyl on a two-dimensional fibre), so a nonzero one is
       convention C at any `n`, whatever numbers it happens to contain.

    Measured when test 2 was added: 46 witnesses matched test 1, 53 matched
    test 2, and only 12 matched both — the first work list missed 41, the whole
    nuclear layer among them. Test 2 is a property of the physics rather than of
    a decimal expansion, which is why it does not need a maintained list.
    """
    if any(c in raw for c in C_FINGERPRINTS):
        return True
    if "partition" not in raw:
        return False
    return bool(_structural_hits(doc))


def _structural_hits(doc, tol: float = 1e-30):
    """Nonzero y_lambda on a 3+ row block. Mirrors convention-c-witness-audit.py."""
    found = []

    def part_of(node):
        part = node.get("partition")
        if part is None:
            return None
        if isinstance(part, (list, tuple)):
            cleaned = [x for x in part if x not in ("_", "", None)]
            try:
                return tuple(int(x) for x in cleaned)
            except (TypeError, ValueError):
                return None
        return None

    def walk(node):
        if found:
            return
        if isinstance(node, dict):
            p = part_of(node)
            if p is not None and len(p) >= 3:
                for k, v in node.items():
                    if "y_lambda" in k or "y_lam" in k:
                        try:
                            if abs(float(v)) > tol:
                                found.append(True)
                                return
                        except (TypeError, ValueError):
                            pass
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return found


def _resolve_producer(doc, witness: pathlib.Path, index, stems):
    """Find the .py that writes this witness, over three keys and a slug.

    `scriptFile` alone leaves 23 witnesses unowned, 11 of them wrongly: the
    corpus records a producer under three different keys and sometimes not at
    all. Resolution order, weakest assumption last:

    1. ``scriptFile`` / ``script`` / ``producer`` — a path or a bare filename.
       ``producer`` is the one that was being skipped, and it is not a rare
       spelling: it owns the whole `chi_at_q0_via_hoefsmit_mpfr` family.
    2. **slug match** on the witness basename, `-` to `_`. `e0-lambda-tryall`
       to `e0_lambda_tryall.py`. Only accepted on an exact stem hit, so it
       cannot silently bind a witness to a near-neighbour script.

    A `producer` naming a **Rust binary** (`rust-chi-q-via-gp-lossless`,
    `matrix-m-chi-q-via-gp`) resolves to nothing here by design — that layer
    needs the hecke-engine CLI, and is where `qou-j6il` found a binary
    returning convention C while its source read D. Better unowned and visible
    than bound to a Python script that does not produce it.

    `_deprecated/` is never a resolution: a witness whose producer was retired
    is history, and history may stay convention C provided it says so.
    """
    for key in ("scriptFile", "script", "producer"):
        val = doc.get(key) or ""
        if not isinstance(val, str) or not val:
            continue
        hit = index.get(pathlib.Path(val).name)
        if hit and "_deprecated" not in str(hit):
            return hit
    base = witness.name
    for suffix in (".witness.json", "-witness.json", ".json"):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
            break
    hit = stems.get(base.replace("-", "_"))
    if hit and "_deprecated" not in str(hit):
        return hit
    return None


def work_list():
    """[(witness, producer)] for every convention-C witness."""
    index = {p.name: p for p in (REPO / "computations").rglob("*.py")}
    stems = {p.stem: p for p in (REPO / "computations").rglob("*.py")}
    items, orphans = [], []
    for w in sorted((REPO / "computations").rglob("*.json")):
        if "_deprecated" in str(w):
            continue
        try:
            raw = w.read_text()
        except OSError:
            continue
        try:
            _doc = json.loads(raw)
        except json.JSONDecodeError:
            _doc = {}
        if not _is_convention_c(raw, _doc):
            continue
        try:
            doc = json.loads(raw)
        except json.JSONDecodeError:
            doc = {}
        src = _resolve_producer(doc, w, index, stems)
        (items if src else orphans).append(
            (str(w.relative_to(REPO)), str(src.relative_to(REPO)) if src else None))
    return items, orphans


def done_set():
    if not LOG.exists():
        return set()
    out = set()
    for line in LOG.read_text().splitlines():
        try:
            out.add(json.loads(line)["producer"])
        except Exception:
            pass
    return out


#: Live producer subprocesses, so signal handlers can take them down with us.
_CHILDREN: list = []


def _kill_group(proc):
    """SIGTERM then SIGKILL the producer's whole process group."""
    if proc is None or proc.poll() is not None:
        return
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(os.getpgid(proc.pid), sig)
        except (ProcessLookupError, PermissionError, OSError):
            return
        try:
            proc.wait(timeout=10)
            return
        except subprocess.TimeoutExpired:
            continue


def _on_signal(signum, _frame):
    """Never leave a producer running after the harness dies."""
    print(f"\nreceived signal {signum} — terminating producer(s) before exit", flush=True)
    for proc in list(_CHILDREN):
        _kill_group(proc)
    try:
        (REPO / ".work" / "convention-c-regen.lock").unlink(missing_ok=True)
    except OSError:
        pass
    sys.exit(128 + signum)


for _sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
    signal.signal(_sig, _on_signal)


class SerialLock:
    """Refuse to start if another instance is already running.

    Not paranoia: on 2026-08-10 two instances of this script were launched
    within a minute of each other and both began stepping through the producer
    list. Nothing was corrupted — they were killed before either finished a
    shared producer — but the standing directive is *never two producers
    concurrently in one checkout*, and "I was careful" is not a mechanism.

    Uses O_EXCL plus a liveness check, so a lock left behind by a container
    death (which has happened twice in this arc) does not wedge the next run.
    """

    def __init__(self, path: pathlib.Path):
        self.path = path

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                pid = int(self.path.read_text().strip())
            except (ValueError, OSError):
                pid = None
            alive = False
            if pid is not None:
                try:
                    os.kill(pid, 0)
                    alive = True
                except OSError:
                    alive = False
            if alive:
                sys.exit(f"REFUSING TO START: another run holds {self.path} (pid {pid}).\n"
                         f"Producers must run strictly serially in one checkout.")
            print(f"note: clearing stale lock from dead pid {pid}", flush=True)
            self.path.unlink(missing_ok=True)
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return self

    def __exit__(self, *exc):
        self.path.unlink(missing_ok=True)
        return False


def run_all(timeout: int):
    items, orphans = work_list()
    # One producer may own several witnesses; run it once.
    by_producer = {}
    for w, p in items:
        by_producer.setdefault(p, []).append(w)

    already = done_set()
    todo = [(p, ws) for p, ws in sorted(by_producer.items()) if p not in already]
    LOG.parent.mkdir(parents=True, exist_ok=True)

    print(f"producers: {len(by_producer)}   already done: {len(already)}   to run: {len(todo)}")
    print(f"orphan witnesses (no scriptFile): {len(orphans)}")
    print(f"log: {LOG}\n", flush=True)

    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join(SYS_PATHS) + os.pathsep + env.get("PYTHONPATH", "")

    for n, (producer, witnesses) in enumerate(todo, 1):
        before = {w: snapshot(REPO / w) for w in witnesses}
        t0 = time.time()
        # Own process group, so a kill of this harness takes the producer with
        # it. Killing the harness alone used to ORPHAN the producer: it kept
        # running, reparented to init, and the next harness happily started the
        # same script again. Three concurrent copies of binding_k_enumerator.py
        # were writing one witness before this was noticed. The SerialLock
        # guards harness instances; only this guards their children.
        proc = None
        try:
            proc = subprocess.Popen(
                [sys.executable, str(pathlib.Path(producer).name)],
                cwd=str((REPO / producer).parent), env=env,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                start_new_session=True)
            _CHILDREN.append(proc)
            out, err = proc.communicate(timeout=timeout)
            status = "ok" if proc.returncode == 0 else f"exit{proc.returncode}"
            tail = (err or out or "").strip().splitlines()[-3:]
        except subprocess.TimeoutExpired:
            _kill_group(proc)
            try:
                out, err = proc.communicate(timeout=15)
            except Exception:                                    # noqa: BLE001
                out = err = ""
            status, tail = "timeout", (err or out or "").strip().splitlines()[-2:]
        except Exception as e:                                   # noqa: BLE001
            _kill_group(proc)
            status, tail = f"error:{type(e).__name__}", [str(e)[:200]]
        finally:
            if proc in _CHILDREN:
                _CHILDREN.remove(proc)
        secs = round(time.time() - t0, 1)
        after = {w: snapshot(REPO / w) for w in witnesses}

        rec = {
            "producer": producer, "status": status, "seconds": secs,
            "witnesses": [
                {"path": w,
                 "c_before": before[w].get("c_fingerprint"),
                 "c_after": after[w].get("c_fingerprint"),
                 "changed": before[w].get("sha256") != after[w].get("sha256"),
                 "deltas": diff(before[w], after[w])}
                for w in witnesses],
            "tail": tail,
        }
        with LOG.open("a") as fh:
            fh.write(json.dumps(rec) + "\n")

        cleared = sum(1 for w in witnesses
                      if before[w].get("c_fingerprint") and not after[w].get("c_fingerprint"))
        print(f"[{n:3d}/{len(todo)}] {status:>9} {secs:7.1f}s  "
              f"cleared {cleared}/{len(witnesses)}  {producer}", flush=True)

    print("\nrun complete", flush=True)


def report():
    if not LOG.exists():
        print("no log yet")
        return
    recs = [json.loads(l) for l in LOG.read_text().splitlines() if l.strip()]
    ok = [r for r in recs if r["status"] == "ok"]
    bad = [r for r in recs if r["status"] != "ok"]
    total_secs = sum(r["seconds"] for r in recs)

    kinds, shifts, zeros = {}, [], 0
    cleared = still_c = 0
    for r in recs:
        for w in r["witnesses"]:
            if w["c_before"] and not w["c_after"]:
                cleared += 1
            elif w["c_after"]:
                still_c += 1
            for d in w["deltas"]:
                # RECLASSIFY from the raw values rather than trusting the stored
                # `kind`: records written before the noise-floor rule existed
                # carry the old labels, and a report that mixes the two is worse
                # than one that is merely wrong.
                kind, rel = classify(d["before"], d["after"])
                kinds[kind] = kinds.get(kind, 0) + 1
                if kind == "shift":
                    shifts.append((rel, r["producer"], w["path"], d))
                elif kind == "structural_zero":
                    zeros += 1

    print(f"producers run : {len(recs)}   ok {len(ok)}   failed {len(bad)}")
    print(f"wall time     : {total_secs/60:.1f} min")
    print(f"witnesses     : C cleared {cleared}   still C {still_c}")
    print(f"\ndelta kinds   : " + ", ".join(f"{k}={v}" for k, v in sorted(kinds.items())))
    # `structural_zero` requires the value to land on exactly 0.0. Producers
    # that carry the weight through mpmath arithmetic instead land it at ~1e-40,
    # which classify() calls `vanished`. Both are the convention-D collapse;
    # reporting only the first prints "structural zeros: 0" next to
    # "vanished=70" and reads as though nothing collapsed at all.
    vanished = kinds.get("vanished", 0)
    print(f"convention-D collapse: {zeros + vanished}"
          f"   (exactly 0: {zeros}, below noise floor {NOISE_FLOOR:g}: {vanished})")

    # Key on the magnitude only: two shifts can tie on `rel`, and the
    # tuple comparison then falls through to comparing dicts, which raises.
    # Magnitude distribution first. A list of extremes answers "what moved
    # most"; only the distribution answers "how much of the corpus moved", and
    # that is the question "total impact" is actually asking.
    buckets = [("< 1 ppm", 0), ("1 ppm - 100 ppm", 0), ("100 ppm - 1%", 0),
               ("1% - 10%", 0), ("10% - 100%", 0), ("> 100% (order-of-magnitude)", 0)]
    counts = [0] * 6
    for rel, *_ in shifts:
        if   rel < 1e-6:  counts[0] += 1
        elif rel < 1e-4:  counts[1] += 1
        elif rel < 1e-2:  counts[2] += 1
        elif rel < 1e-1:  counts[3] += 1
        elif rel < 1.0:   counts[4] += 1
        else:             counts[5] += 1
    print("\nshift magnitude distribution:")
    for (label, _), n in zip(buckets, counts):
        bar = "#" * min(40, n // max(1, max(counts) // 40 or 1))
        print(f"  {label:<30} {n:5d}  {bar}")

    # Per-quantity rollup. The extremes lists answer "which single number moved
    # most"; they cannot answer "did quantity X move by the order the registry
    # predicts", because one quantity appears under many JSON paths and at many
    # array indices. Group by the leaf field name, with array indices and the
    # enclosing path stripped, and report the spread.
    #
    # A tight spread within a group is the signal worth having: the registry
    # records the migration as ~195.8 ppm on beta_Bor and ~-197 ppm on m_p, so a
    # group whose median lands there and whose max is close to its median has
    # moved coherently. A group spanning orders of magnitude has not, and is
    # either mixing two quantities under one name or is not a convention effect.
    groups: dict[str, list[float]] = {}
    for rel, _prod, _wpath, d in shifts:
        leaf = re.sub(r"\[\d+\]", "", d["field"]).split(".")[-1].strip()
        groups.setdefault(leaf or "(unnamed)", []).append(rel)
    if groups:
        print("\nper-quantity rollup (leaf field, indices stripped):")
        print(f"  {'quantity':<34} {'n':>5} {'median ppm':>14} {'max ppm':>14}  spread")
        ranked = sorted(groups.items(), key=lambda kv: max(kv[1]), reverse=True)
        for name, rels in ranked[:20]:
            rs = sorted(rels)
            med = rs[len(rs) // 2]
            mx = rs[-1]
            # Orders of magnitude between the smallest and largest move in the
            # group. 0 means every member moved together.
            span = ""
            if rs[0] > 0:
                decades = math.log10(mx / rs[0])
                span = "coherent" if decades < 1 else f"{decades:.0f} decades"
            print(f"  {name[:34]:<34} {len(rs):5d} {med*1e6:14.1f} {mx*1e6:14.1f}  {span}")

    shifts.sort(key=lambda t: t[0], reverse=True)
    print(f"\nlargest RELATIVE shifts:")
    for rel, prod, wpath, d in shifts[:12]:
        print(f"  {rel*1e6:16.1f} ppm  {wpath.split('/')[-1]}")
        print(f"        {d['field']}")
        print(f"        {d['before'][:26]} -> {d['after'][:26]}")

    def absdelta(t):
        try:
            return abs(float(t[3]["after"]) - float(t[3]["before"]))
        except ValueError:
            return 0.0
    shifts.sort(key=absdelta, reverse=True)
    print(f"\nlargest ABSOLUTE shifts (what actually moved in magnitude):")
    for rel, prod, wpath, d in shifts[:12]:
        print(f"  {absdelta((rel,prod,wpath,d)):18.9g}  ({rel*1e6:.1f} ppm)  {wpath.split('/')[-1]}")
        print(f"        {d['field']}")
        print(f"        {d['before'][:26]} -> {d['after'][:26]}")

    if bad:
        print(f"\nFAILURES ({len(bad)}):")
        for r in bad:
            print(f"  {r['status']:>10}  {r['producer']}")
            for t in r["tail"][-1:]:
                print(f"              {t[:150]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--timeout", type=int, default=900)
    a = ap.parse_args()
    if a.plan:
        items, orphans = work_list()
        by = {}
        for w, p in items:
            by.setdefault(p, []).append(w)
        print(f"{len(items)} witnesses / {len(by)} producers; {len(orphans)} orphan witnesses")
        for p, ws in sorted(by.items()):
            print(f"  {p}  ->  {len(ws)} witness(es)")
        for w, _ in orphans:
            print(f"  ORPHAN  {w}")
        return 0
    if a.run:
        with SerialLock(REPO / ".work" / "convention-c-regen.lock"):
            run_all(a.timeout)
        return 0
    if a.report:
        report()
        return 0
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
