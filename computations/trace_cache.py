"""Persistent, incremental cache of exact `pyhecke_native` trace values.

WHAT IT STORES. `(n, signed word w, suffix s) -> the decimal string the
producer returns`, exactly as returned: no float ever touches a value. The
producer is named by `function`:
  * `tr-m-atomic-mpfr`           tr_m_atomic_mpfr(w), with s = ""
  * `tr-m-atomic-mpfr-suffixes`  tr_m_atomic_mpfr_suffixes([w], [s])[0][0]
Each function is its own branch member: the two routes give the same exact
number but may round its last MPFR digits differently, and a cache must
return what its producer returns. A probe that
evaluates thousands of expanded words (at 4He, hours of reduction) asks this
module first, computes only the misses, and appends them to a local journal
after every chunk, so an interrupted run resumes where it stopped.

WHERE IT LIVES. Locally under `$QOU_TRACE_CACHE_DIR` (default
`~/.cache/qou/trace-cache/<member>/`), and durably in the `trace-cache` family
of orphan branches declared in qou.json, through `scripts/trace-cache.sh`
(restore at start, seed a new shard at checkpoints). See that script for the
member key.

WHY A STALE VALUE CANNOT BE SERVED.
  * The member key hashes the git trees of tools/hecke-engine and
    tools/pyhecke-native, the q0 STRING and the dps. A dirty engine tree has no
    key: the cache is then off for the whole run (no restore, no write).
  * The installed binary may have been built from other sources than HEAD.
    Before any loaded entry is served, a sample of them (`QOU_TRACE_CACHE_VERIFY`,
    default 4, shortest words first plus one at random) is recomputed with the
    live binary and compared as strings. One mismatch and the cache is refused.
  * Two stored values for one key that differ are a refusal too.

ENVIRONMENT
  QOU_TRACE_CACHE=0          off entirely
  QOU_TRACE_CACHE_DIR=<dir>  local root
  QOU_TRACE_CACHE_PUSH=0     never seed the branch store (restore still runs)
  QOU_TRACE_CACHE_RESTORE=0  never restore from the branch store
  QOU_TRACE_CACHE_VERIFY=<k> number of loaded entries re-checked (default 4)
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "trace-cache.sh"


def word_key(word) -> str:
    """Canonical text for a signed word: `s:g,s:g,...`."""
    return ",".join(f"{int(s)}:{int(g)}" for (s, g) in word)


def suffix_key(suffix) -> str:
    """Canonical text for a positive suffix (generator indices): `g,g,...`."""
    return ",".join(str(int(g)) for g in suffix)


def _parse_word(text: str):
    if not text:
        return []
    return [tuple(int(x) for x in p.split(":")) for p in text.split(",")]


class TraceCache:
    """Cache for one producer `function` at one (q0, dps)."""

    def __init__(self, function: str, q0_str: str, dps: int, *, log=print):
        self.function = function
        self.q0 = q0_str
        self.dps = int(dps)
        self.log = log
        self.values: dict[tuple[int, str, str], str] = {}
        self.remote_keys: set[tuple[int, str, str]] = set()
        self.unpublished: dict[tuple[int, str, str], str] = {}
        self.hits = 0
        self.misses = 0
        self.enabled = os.environ.get("QOU_TRACE_CACHE", "1") != "0"
        self.push = os.environ.get("QOU_TRACE_CACHE_PUSH", "1") != "0"
        self.member = None
        self.journal = None
        self.last_publish = time.monotonic_ns()
        if not self.enabled:
            self.log("  trace-cache: off (QOU_TRACE_CACHE=0)")
            return
        r = subprocess.run(["bash", str(SCRIPT), "key", function, q0_str, str(self.dps)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            self.log(f"  trace-cache: off — {r.stdout.strip() or r.stderr.strip()}")
            self.enabled = False
            return
        self.member = r.stdout.strip()
        base = Path(os.environ.get("QOU_TRACE_CACHE_DIR",
                                   Path.home() / ".cache" / "qou" / "trace-cache"))
        self.dir = base / self.member
        (self.dir / "local").mkdir(parents=True, exist_ok=True)
        if os.environ.get("QOU_TRACE_CACHE_RESTORE", "1") != "0":
            t0 = time.monotonic_ns()
            r = subprocess.run(["bash", str(SCRIPT), "restore", function, q0_str, str(self.dps),
                                str(self.dir / "remote")], capture_output=True, text=True)
            msg = (r.stderr.strip().splitlines() or [""])[-1]
            self.log(f"  trace-cache: restore exit {r.returncode} ({msg}) "
                     f"in {(time.monotonic_ns() - t0) // 10**8 / 10}s")
        n_remote = self._load_dir(self.dir / "remote" / "shards", remote=True)
        n_local = self._load_dir(self.dir / "local", remote=False)
        # Local journal entries the branch store does not hold yet.
        for k, v in self.values.items():
            if k not in self.remote_keys:
                self.unpublished[k] = v
        self.log(f"  trace-cache: member {self.member}: {len(self.values)} entries "
                 f"({n_remote} from branch shards, {n_local} from local journals, "
                 f"{len(self.unpublished)} not yet on the branch)")
        stamp = time.strftime("%Y%m%dT%H%M%S", time.gmtime())
        self.journal_path = self.dir / "local" / f"journal-{stamp}-{os.getpid()}.jsonl"

    # ── loading and verification ─────────────────────────────────────
    def _load_dir(self, d: Path, *, remote: bool) -> int:
        count = 0
        if not d.is_dir():
            return 0
        for f in sorted(d.glob("*.jsonl")):
            for line in f.read_text().splitlines():
                if not line.strip():
                    continue
                rec = json.loads(line)
                if "v" not in rec:
                    continue
                k = (int(rec["n"]), rec["w"], rec.get("s", ""))
                old = self.values.get(k)
                if old is not None and old != rec["v"]:
                    raise RuntimeError(f"trace-cache: two different stored values for "
                                       f"{k!r} in {self.dir}; refusing")
                self.values[k] = rec["v"]
                if remote:
                    self.remote_keys.add(k)
                count += 1
        return count

    def verify(self, compute) -> None:
        """Recompute a sample with `compute(n, word, suffix) -> str` (the producer)."""
        if not self.enabled or not self.values:
            return
        k = int(os.environ.get("QOU_TRACE_CACHE_VERIFY", "4"))
        if k <= 0:
            self.log("  trace-cache: verification sample DISABLED (QOU_TRACE_CACHE_VERIFY=0)")
            return
        keys = sorted(self.values, key=lambda t: (t[0], len(t[1]), t))
        sample = keys[:max(k - 1, 1)]
        rest = keys[len(sample):]
        if rest:
            sample.append(random.Random(0).choice(rest))
        t0 = time.monotonic_ns()
        for (n, w, sfx) in sample:
            got = compute(n, _parse_word(w), [int(g) for g in sfx.split(",")] if sfx else [])
            stored = self.values[(n, w, sfx)]
            if got != stored:
                self.enabled = False
                self.values.clear()
                raise RuntimeError(
                    f"trace-cache: stored value for n={n} word={w!r} suffix={sfx!r} disagrees with the "
                    f"installed pyhecke_native ({got!r} vs {stored!r}); "
                    "the binary was not built from the keyed sources. Refusing the cache.")
        self.log(f"  trace-cache: verified {len(sample)} stored entries against the live "
                 f"binary in {(time.monotonic_ns() - t0) // 10**8 / 10}s — all byte-identical")

    # ── lookups and writes ───────────────────────────────────────────
    def lookup(self, n: int, pairs):
        """pairs = [(signed word, positive suffix)] -> (found {index: str}, missing [index])."""
        found, missing = {}, []
        for i, (w, sfx) in enumerate(pairs):
            v = self.values.get((n, word_key(w), suffix_key(sfx))) if self.enabled else None
            if v is None:
                missing.append(i)
            else:
                found[i] = v
        self.hits += len(found)
        self.misses += len(missing)
        return found, missing

    def store(self, n: int, pairs, values) -> None:
        if not self.enabled:
            return
        lines = []
        for (w, sfx), v in zip(pairs, values):
            k = (n, word_key(w), suffix_key(sfx))
            if k in self.values:
                continue
            self.values[k] = v
            self.unpublished[k] = v
            lines.append(json.dumps({"n": n, "w": k[1], "s": k[2], "v": v}))
        if lines:
            with open(self.journal_path, "a") as f:
                f.write("\n".join(lines) + "\n")
                f.flush()
                os.fsync(f.fileno())

    def maybe_publish(self, every_s: int = 600) -> None:
        if time.monotonic_ns() - self.last_publish >= every_s * 10**9:
            self.publish()

    def publish(self) -> None:
        """Seed the unpublished entries as one content-addressed shard."""
        self.last_publish = time.monotonic_ns()
        if not (self.enabled and self.push and self.unpublished):
            return
        body = "".join(json.dumps({"n": n, "w": w, "s": sfx, "v": v}) + "\n"
                       for (n, w, sfx), v in sorted(self.unpublished.items()))
        sha = hashlib.sha256(body.encode()).hexdigest()
        p = self.dir / "local" / f"shard-{sha[:16]}.pending"
        p.write_text(body)
        t0 = time.monotonic_ns()
        r = subprocess.run(["bash", str(SCRIPT), "seed", self.function, self.q0,
                            str(self.dps), str(p)],
                           capture_output=True, text=True)
        msg = (r.stderr.strip().splitlines() or [""])[-1]
        self.log(f"  trace-cache: seed {len(self.unpublished)} entries: exit "
                 f"{r.returncode} ({msg}) in {(time.monotonic_ns() - t0) // 10**8 / 10}s")
        p.unlink(missing_ok=True)
        if r.returncode == 0:
            self.remote_keys.update(self.unpublished)
            self.unpublished.clear()

    def stats(self) -> str:
        tot = self.hits + self.misses
        rate = f"{100 * self.hits // tot}%" if tot else "n/a"
        return (f"trace-cache: {self.hits} hits / {self.misses} misses "
                f"(hit rate {rate}), {len(self.values)} entries held")
