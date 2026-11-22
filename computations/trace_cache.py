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
(restore at start; seed a new shard at checkpoints only when
QOU_TRACE_CACHE_PUSH=1, since pushing to origin is opt-in). See that script for the
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
  QOU_TRACE_CACHE_PUSH=1     seed the branch store on origin (default 0: never push;
                             new entries stay in the local journal)
  QOU_TRACE_CACHE_RESTORE=0  never restore from the branch store
  QOU_TRACE_CACHE_VERIFY=<k> number of loaded entries re-checked (default 4)
"""
from __future__ import annotations

import os
import random
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "trace-cache.sh"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _branch_cache import ShardedCache  # noqa: E402  (the shared branch-cache layer)


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


class TraceCache(ShardedCache):
    """Cache for one producer `function` at one (q0, dps).

    The journal, restore, seed and refusal rules are the shared ones in
    `_branch_cache.ShardedCache` / `scripts/lib/branch-cache.sh`; this class
    adds the member key (through `scripts/trace-cache.sh key`), the
    (n, word, suffix) entry key, and verification against the live binary.
    """

    def __init__(self, function: str, q0_str: str, dps: int, *, log=print):
        self.function = function
        self.q0 = q0_str
        self.dps = int(dps)

        def member_fn():
            r = subprocess.run(["bash", str(SCRIPT), "key", function, q0_str, str(self.dps)],
                               capture_output=True, text=True)
            if r.returncode != 0:
                return None, (r.stdout.strip() or r.stderr.strip())
            return r.stdout.strip(), ""

        super().__init__(
            "trace-cache",
            member_fn=member_fn,
            restore_argv=lambda m, d: ["bash", str(SCRIPT), "restore", function, q0_str,
                                       str(self.dps), d],
            seed_argv=lambda m, p: ["bash", str(SCRIPT), "seed", function, self.q0,
                                    str(self.dps), p],
            key_of=lambda rec: (int(rec["n"]), rec["w"], rec.get("s", "")),
            rec_of=lambda k, v: {"n": k[0], "w": k[1], "s": k[2], "v": v},
            env="QOU_TRACE_CACHE", log=log)

    # ── verification ─────────────────────────────────────────────────
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
            v = self.get((n, word_key(w), suffix_key(sfx)))
            if v is None:
                missing.append(i)
            else:
                found[i] = v
        self.hits += len(found)
        self.misses += len(missing)
        return found, missing

    def store(self, n: int, pairs, values) -> None:
        self.put_many(((n, word_key(w), suffix_key(sfx)), v) for (w, sfx), v in zip(pairs, values))
