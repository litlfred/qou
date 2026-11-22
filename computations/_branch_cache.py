"""Python twin of scripts/lib/branch-cache.sh: a local journal plus a sharded
branch-cache member, for any qou cache whose entries are `key -> exact value`.

ONE IMPLEMENTATION. Everything about the branch store — the family prefix read
from qou.json, the git-tree source key (a dirty tree has none), the private
bare repository, sha256-checked restore, no-force seeding — is done by the
shell library through `scripts/branch-cache.sh` (or a cache's own wrapper
script, such as `scripts/trace-cache.sh`). This module only holds what is
naturally Python: an in-memory table, an append-only local journal fsync'd
after every write so an interrupted run resumes, and the bookkeeping of which
entries the branch does not hold yet.

VALUES ARE STORED AS GIVEN. A record is a JSON object built by the cache's
`rec_of(key, value)` and must end with the field "v" (the shell seed counts
entries by it). Exact values stay exact strings; nothing here converts a value
to a float, and two stored values for one key that differ are a refusal.

Users: computations/trace_cache.py (kind `trace-cache`),
computations/derived_chi_catalogue_mn_disk_cache.py (kind `mn-chi-cache`).
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLI = ROOT / "scripts" / "branch-cache.sh"


def prefix(kind: str) -> str | None:
    """The declared branchPrefix of a family, or None if qou.json declares none."""
    r = subprocess.run(["bash", str(CLI), "prefix", kind], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def source_key(label: str, dirs) -> tuple[str | None, str]:
    """(12-hex key, "") or (None, "undetermined: ...") for a dirty or unreadable tree."""
    r = subprocess.run(["bash", str(CLI), "source-key", label, *dirs],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        return None, (r.stdout.strip() or r.stderr.strip())
    return r.stdout.strip(), ""


def source_trees(dirs) -> dict:
    r = subprocess.run(["bash", str(CLI), "source-trees", *dirs],
                       capture_output=True, text=True, check=True, cwd=ROOT)
    return json.loads(r.stdout)


class ShardedCache:
    """A `key -> value` table backed by a local journal and a branch member.

    member_fn()            -> (member name, "") or (None, why the cache is off)
    restore_argv(m, dir)   -> argv that restores member m into dir
    seed_argv(m, shard)    -> argv that seeds one shard file into member m
    key_of(rec) -> tuple   rec_of(key, value) -> dict ending with "v"
    env                    environment-variable prefix: <env>=0 off,
                           <env>_DIR local root, <env>_PUSH=0, <env>_RESTORE=0
    """

    def __init__(self, kind: str, *, member_fn, restore_argv, seed_argv,
                 key_of, rec_of, env: str, log=print):
        self.kind = kind
        self.log = log
        self._seed_argv = seed_argv
        self._key_of = key_of
        self._rec_of = rec_of
        self.values: dict[tuple, object] = {}
        self.remote_keys: set[tuple] = set()
        self.unpublished: dict[tuple, object] = {}
        self.hits = 0
        self.misses = 0
        self.enabled = os.environ.get(env, "1") != "0"
        self.push = os.environ.get(f"{env}_PUSH", "1") != "0"
        self.member = None
        self.last_publish = time.monotonic_ns()
        if not self.enabled:
            self.log(f"  {kind}: off ({env}=0)")
            return
        member, why = member_fn()
        if member is None:
            self.log(f"  {kind}: off — {why}")
            self.enabled = False
            return
        self.member = member
        base = Path(os.environ.get(f"{env}_DIR", Path.home() / ".cache" / "qou" / kind))
        self.dir = base / self.member
        (self.dir / "local").mkdir(parents=True, exist_ok=True)
        if os.environ.get(f"{env}_RESTORE", "1") != "0":
            t0 = time.monotonic_ns()
            r = subprocess.run(restore_argv(member, str(self.dir / "remote")),
                               capture_output=True, text=True, cwd=ROOT)
            msg = (r.stderr.strip().splitlines() or [""])[-1]
            self.log(f"  {kind}: restore exit {r.returncode} ({msg}) "
                     f"in {(time.monotonic_ns() - t0) // 10**8 / 10}s")
        n_remote = self._load_dir(self.dir / "remote" / "shards", remote=True)
        n_local = self._load_dir(self.dir / "local", remote=False)
        # Local journal entries the branch store does not hold yet.
        for k, v in self.values.items():
            if k not in self.remote_keys:
                self.unpublished[k] = v
        self.log(f"  {kind}: member {self.member}: {len(self.values)} entries "
                 f"({n_remote} from branch shards, {n_local} from local journals, "
                 f"{len(self.unpublished)} not yet on the branch)")
        stamp = time.strftime("%Y%m%dT%H%M%S", time.gmtime())
        self.journal_path = self.dir / "local" / f"journal-{stamp}-{os.getpid()}.jsonl"

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
                k = self._key_of(rec)
                old = self.values.get(k)
                if old is not None and old != rec["v"]:
                    raise RuntimeError(f"{self.kind}: two different stored values for "
                                       f"{k!r} in {self.dir}; refusing")
                self.values[k] = rec["v"]
                if remote:
                    self.remote_keys.add(k)
                count += 1
        return count

    def refuse(self) -> None:
        self.enabled = False
        self.values.clear()

    def get(self, k):
        return self.values.get(k) if self.enabled else None

    def put_many(self, items) -> None:
        """Record (key, value) pairs not held yet, in the journal, fsync'd."""
        if not self.enabled:
            return
        lines = []
        for k, v in items:
            if k in self.values:
                continue
            self.values[k] = v
            self.unpublished[k] = v
            lines.append(json.dumps(self._rec_of(k, v)))
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
        body = "".join(json.dumps(self._rec_of(k, v)) + "\n"
                       for k, v in sorted(self.unpublished.items()))
        sha = hashlib.sha256(body.encode()).hexdigest()
        p = self.dir / "local" / f"shard-{sha[:16]}.pending"
        p.write_text(body)
        t0 = time.monotonic_ns()
        r = subprocess.run(self._seed_argv(self.member, str(p)),
                           capture_output=True, text=True, cwd=ROOT)
        msg = (r.stderr.strip().splitlines() or [""])[-1]
        self.log(f"  {self.kind}: seed {len(self.unpublished)} entries: exit "
                 f"{r.returncode} ({msg}) in {(time.monotonic_ns() - t0) // 10**8 / 10}s")
        p.unlink(missing_ok=True)
        if r.returncode == 0:
            self.remote_keys.update(self.unpublished)
            self.unpublished.clear()

    def stats(self) -> str:
        tot = self.hits + self.misses
        rate = f"{100 * self.hits // tot}%" if tot else "n/a"
        return (f"{self.kind}: {self.hits} hits / {self.misses} misses "
                f"(hit rate {rate}), {len(self.values)} entries held")


def generic_seed_argv(kind: str, meta: dict, readme: str, workdir: Path):
    """seed_argv for a cache with no wrapper script: writes meta/readme files
    beside the shard and calls `branch-cache.sh shard-seed`."""
    def argv(member: str, shard: str):
        mp_ = workdir / "seed-meta.json"
        rp = workdir / "seed-readme.md"
        mp_.write_text(json.dumps(meta))
        rp.write_text(readme)
        return ["bash", str(CLI), "shard-seed", kind, member, shard, str(mp_), str(rp)]
    return argv
