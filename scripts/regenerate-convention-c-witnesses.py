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


#: Producers that take required positional arguments.
#:
#: The harness invokes every producer bare, which is right for the ~50 that
#: write their witness on import-and-run. A few instead take the object to
#: compute as argv and exit 2 on argparse before doing anything. That reads in
#: the journal as a producer failure, which it is not — the atom is simply not
#: recoverable from the witness path by the resolver.
#:
#: Keyed by producer path, valued by the argv that regenerates exactly the
#: in-scope witnesses. For `per_irrep_pole_atom` those are
#: `per-irrep-pole-proton-h3` and `per-irrep-pole-deuteron-h6`, so the atoms
#: are `proton` and `deuteron` and no others — passing the full ATOMS list
#: would rewrite six witnesses this campaign has not audited.
PRODUCER_ARGV = {
    "computations/per_irrep_pole_atom.py": ["proton", "deuteron"],
}


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

    THREE tests now — test 2 has the same shape of blind spot test 1 had.

    3. **Symbolic** — a weight held as an EXPRESSION carrying a half-integer
       power of `q`. Test 2 calls `float(v)` and skips what does not parse, so
       a sympy-valued weight is invisible to it. C is
       `z = 1/(q^{1/2} + q^{-1/2})`; D is `z = q^3/(q^2 + 1)`, rational and
       sqrt-free — so `q^{k/2}` in a weight expression is C at any `n`.

    Test 3 finds two witnesses the other two miss, and they are not inert:
    `y-lambda-wenzl-bridge-symbolic-witness.json` evaluates to nonzero `y_λ`
    on 3-, 4-, 5- and 6-row partitions at q₀ and feeds
    `rho_k_h3a_refinement`, whose Schur-Weyl check fails at 4.75e-8 and which
    is itself the upstream of five more producers.
    """
    if any(c in raw for c in C_FINGERPRINTS):
        return True
    if ("**" in raw or "sqrt" in raw) and _symbolic_hits(doc):
        return True
    if "partition" not in raw:
        return False
    return bool(_structural_hits(doc))


#: Half-integer power of q — see test 3 above.
_SQRT_Q = re.compile(r"q\s*\*\*\s*\(?\s*-?\d+\s*/\s*2\s*\)?"
                     r"|sqrt\(\s*q\s*\)"
                     r"|q\s*\*\*\s*-?0\.5")

_SYMBOLIC_WEIGHT_KEYS = ("y_lambda", "y_lam", "y_at_q0", "weight_lambda")


def _symbolic_hits(doc) -> bool:
    """A weight expression built under convention C. Mirrors the audit's test 3."""
    hit = False

    def walk(node):
        nonlocal hit
        if hit:
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str) and any(w in k for w in _SYMBOLIC_WEIGHT_KEYS):
                    try:
                        float(v)
                        continue
                    except (TypeError, ValueError):
                        pass
                    if _SQRT_Q.search(v):
                        hit = True
                        return
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return hit


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


def work_list():
    """[(witness, producer)] for every convention-C witness."""
    index = {p.name: p for p in (REPO / "computations").rglob("*.py")}
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
        sf = doc.get("scriptFile") or doc.get("script") or ""
        src = index.get(pathlib.Path(sf).name) if sf else None
        (items if src else orphans).append(
            (str(w.relative_to(REPO)), str(src.relative_to(REPO)) if src else None))
    return items, orphans


#: Witness basenames referenced in a producer's source.
_WITNESS_REF = re.compile(r"[A-Za-z0-9._-]+\.witness\.json")


def dependency_order(by_producer: dict) -> list:
    """Order producers so an upstream witness is rewritten before its readers.

    Producers read each other's witnesses. Alphabetical order therefore
    regenerates downstream producers against *stale* upstream data and the
    output looks clean — nothing in the run reports it, because each producer
    individually succeeded.

    This is not hypothetical. `rho-k-h3a-refinement.witness.json` is read by
    five producers (`rho_k_co_casimir_extended`, `rho_k_h3a_co_casimir`,
    `rho_k_h3a_crystal`, `rho_k_h3a_frobenius_pairing`, `rho_k_h3a_lp_dual`)
    and written by `rho_k_h3a_refinement`, which sorts **last**. Every one of
    the five read convention-C weights while being counted as migrated. It is
    also how the campaign's first work list came to be wrong: a freshly
    migrated co-Casimir producer printed `live channels = 11 of 11`, impossible
    under convention D at n = 6, because its weights came from a stale upstream.

    Edges come from the source text (which witness names a producer mentions),
    not from a maintained list, so a new dependency orders itself.

    A cycle cannot be ordered; those producers are emitted in the original
    order with a warning rather than dropped, since a mutually-referential pair
    still needs running — it just needs running twice, which is a judgement for
    the operator, not something to silently paper over.
    """
    writes = {p: {pathlib.Path(w).name for w in ws} for p, ws in by_producer.items()}
    reads = {}
    for p in by_producer:
        try:
            src = (REPO / p).read_text()
        except OSError:
            src = ""
        reads[p] = set(_WITNESS_REF.findall(src)) - writes[p]

    # owner[witness] = the producer that writes it (within this run).
    owner = {w: p for p, ws in writes.items() for w in ws}
    deps = {p: {owner[w] for w in reads[p] if w in owner and owner[w] != p}
            for p in by_producer}

    ordered, placed = [], set()
    while True:
        ready = sorted(p for p in by_producer
                       if p not in placed and deps[p] <= placed)
        if not ready:
            break
        ordered.extend(ready)
        placed.update(ready)

    stuck = sorted(p for p in by_producer if p not in placed)
    if stuck:
        print(f"  ! {len(stuck)} producer(s) in a witness-dependency cycle; "
              f"running in name order: {', '.join(pathlib.Path(s).name for s in stuck)}",
              flush=True)
        ordered.extend(stuck)
    return ordered


def stale_readers():
    """Producers that ran BEFORE an upstream witness they read was rewritten.

    `dependency_order` fixes the order of work still pending. It cannot fix
    what already ran: a producer recorded early in the journal may have read a
    witness that a later producer then rewrote, so its committed output is
    against data that no longer exists.

    The journal is append-ordered, which is the only clock available — records
    carry no timestamp — and it is sufficient: if Q writes a witness P reads,
    and Q appears after P, then P read Q's pre-run value.

    Returns [(reader, [upstreams])] in journal order. An empty list is the
    campaign's real convergence criterion, and it is stronger than "every
    producer ran": a run can be 52-for-52 green and still be internally
    inconsistent.
    """
    items, _ = work_list()
    by_producer = {}
    for w, p in items:
        by_producer.setdefault(p, []).append(w)
    writes = {p: {pathlib.Path(w).name for w in ws} for p, ws in by_producer.items()}
    owner = {w: p for p, ws in writes.items() for w in ws}

    # The LAST record is the one that matters: a producer's committed witness
    # comes from its most recent run, so P is stale iff last(Q) > last(P).
    # Keying on the first record would flag a producer that was re-run after
    # its upstream — a false positive, and precisely the case a drain creates.
    # Today a second record only exists after a purge removes the first (the
    # harness skips producers already in the journal), so first and last
    # coincide; this keeps the check correct once that stops being true.
    pos = {}
    for i, line in enumerate(LOG.read_text().splitlines() if LOG.exists() else []):
        try:
            pos[json.loads(line)["producer"]] = i
        except Exception:                                        # noqa: BLE001
            continue
    order = sorted(pos, key=pos.get)

    out = []
    for p in order:
        if p not in by_producer:
            continue
        try:
            src = (REPO / p).read_text()
        except OSError:
            continue
        late = sorted({
            owner[w] for w in set(_WITNESS_REF.findall(src))
            if w in owner and owner[w] != p
            and (owner[w] not in pos or pos[owner[w]] > pos[p])
        })
        if late:
            out.append((p, late))
    return out


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
    todo = [(p, by_producer[p]) for p in dependency_order(by_producer)
            if p not in already]
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
                [sys.executable, str(pathlib.Path(producer).name)]
                + PRODUCER_ARGV.get(producer, []),
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
    print(f"structural zeros (y_lambda -> 0, ell(lambda)>=3): {zeros}")

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
    ap.add_argument("--stale", action="store_true",
                    help="list producers that ran before an upstream witness "
                         "they read was rewritten (exit 1 if any)")
    a = ap.parse_args()
    if a.stale:
        rows = stale_readers()
        if not rows:
            print("no stale readers — every producer ran after its upstreams")
            return 0
        print(f"{len(rows)} producer(s) ran against an upstream that changed after:")
        for p, ups in rows:
            print(f"  {p}")
            for u in ups:
                print(f"      reads a witness written later by  {u}")
        return 1
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
