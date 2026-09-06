"""`bar_pairing_binding_observable`'s cache guard read three q-field names,
and the canonical at-q0 caches carry none of them.

WHAT THIS IS.  Three producers write files matching
`chi-<atom>(-free)-h<n>-at-<tag>-50dps.witness.json`, and each spells the
q value differently:

    bar_pairing_binding_observable.py   ->  q_str
    chi_at_q_inv_via_native_mpfr.py     ->  q_inv_50dps_str
    chi_at_q0_via_hoefsmit_mpfr.py      ->  q_0_50dps          <-- was missing

`_load_or_compute_chi`'s cache-key guard (added by a Copilot review on
PR #1748, correctly, to stop a q re-pin loading a stale witness) looked up
only the first two plus a `q_0_50dps_str` that no producer writes.  So on
every cache written by the Hoefsmit producer `cached_q` was `None`, the
`cached_q == q_str` hit condition could never hold, and the file was
recomputed and **overwritten with this script's schema** -- dropping
`tr_M_at_q0` and `q_0_50dps`, the two fields downstream consumers read.

WHY IT WAS SILENT.  Both diagnostic branches were guarded on
`cached_q is not None`, which is exactly the case that failed.  A miss on a
recognised schema printed a "cache miss" line; a miss on an unrecognised one
printed nothing at all and destroyed the file.

WHAT THIS PROBE ASSERTS.  Not that the bug is fixed -- that a regression
would be caught.  Section 1 reads every on-disk cache and checks the guard's
key vocabulary covers every producer present.  Section 2 exercises the real
`_load_or_compute_chi` with the compute path replaced by a raising stub, so a
cache HIT is proved by the absence of a recompute rather than asserted.
Section 3 checks the ownership refusal fires on a foreign file and does NOT
fire on one this script owns.

NO ARITHMETIC.  This probe compares strings and counts files; it computes no
q-dependent quantity, so the NO-FLOAT64 family has nothing to bind to here.
It reads witnesses and never writes one of theirs.

Bean `qou-w8rv`.  Found while the chi caches were being regenerated under
`qou-92u9`: the regeneration would have been undone by the next run of this
consumer.
"""
from __future__ import annotations

import json
import sys
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
for _p in (str(COMP), str(ROOT / "tools/qou-substrate/python"),
           str(ROOT / "tools/pyhecke/python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# The compute path must be a LOUD failure: every "HIT" below is then proved
# by nothing having been recomputed, not by a return value we chose to trust.
_SENTINEL = "COMPUTE PATH TAKEN"
if "pyhecke_native" not in sys.modules:
    _fake = types.ModuleType("pyhecke_native")

    def _boom(*_a, **_k):
        raise AssertionError(_SENTINEL)

    _fake.chi_lambda_all_partitions_mpfr = _boom
    sys.modules["pyhecke_native"] = _fake

from mpmath import mp  # noqa: E402

import bar_pairing_binding_observable as B  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

# The keys the guard looks up, in order.  Kept here so a future narrowing of
# the guard fails this probe instead of silently reinstating the bug.
GUARD_KEYS = ("q_str", "q_0_50dps_str", "q_inv_50dps_str",
              "q_0_50dps", "q0Value")

results: dict = {}
failures: list[str] = []


def check(name: str, ok: bool, detail) -> None:
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}: {detail}")
    results[name] = detail
    if not ok:
        failures.append(name)


mp.dps = 60
_q0 = mp.mpf(Q_50_DIGIT_STR)
Q_TAGS = {"q0": Q_50_DIGIT_STR,
          "qinv": mp.nstr(1 / _q0, 50, strip_zeros=False)}
ISOTOPES = dict(B.ISOTOPES)

print("=" * 74)
print("1. EVERY on-disk cache carries a key the guard looks up")
print("=" * 74)

cache_files = []
for atom, (Z, N) in ISOTOPES.items():
    n = 3 * (Z + N)
    for tag in Q_TAGS:
        for kind in ("atom", "free"):
            stem = f"chi-{atom}-h{n}" if kind == "atom" \
                else f"chi-{atom}-{kind}-h{n}"
            p = COMP / f"{stem}-at-{tag}-50dps.witness.json"
            if p.exists():
                cache_files.append((atom, n, kind, tag, p))

producers: dict[str, int] = {}
unreadable: list[str] = []
for atom, n, kind, tag, p in cache_files:
    w = json.loads(p.read_text())
    owner = w.get("producer") or w.get("scriptFile") or "<unstamped>"
    producers[owner] = producers.get(owner, 0) + 1
    if not any(w.get(k) is not None for k in GUARD_KEYS):
        unreadable.append(p.name)

for owner, cnt in sorted(producers.items()):
    print(f"  {cnt:3d}  {owner}")
check("every_cache_exposes_a_q_field_the_guard_reads",
      not unreadable, unreadable or f"{len(cache_files)} files, 0 unreadable")
check("more_than_one_producer_writes_this_filename_family",
      len(producers) > 1,
      f"{len(producers)} producers — the reason the guard needs every "
      f"vocabulary")

# The refusal in section 3 can only protect a file that NAMES its producer:
# it is keyed on `w["producer"]`, so an unstamped file is overwritable.
# Measured 2026-09-06: 6 of 16 are unstamped and ALL SIX are `free-*`, the
# kind this script owns exclusively -- so the hole is real but unoccupied.
# This asserts it stays unoccupied. An unstamped `atom`-kind cache is a
# canonical witness the refusal cannot see, which is the bug all over again.
unstamped_atom = [
    p.name for atom, n, kind, tag, p in cache_files
    if kind == "atom"
    and not (json.loads(p.read_text()).get("producer")
             or json.loads(p.read_text()).get("scriptFile"))
]
unstamped_all = [
    p.name for atom, n, kind, tag, p in cache_files
    if not (json.loads(p.read_text()).get("producer")
            or json.loads(p.read_text()).get("scriptFile"))
]
check("no_canonical_atom_cache_is_unstamped",
      not unstamped_atom,
      unstamped_atom or
      f"0 of {sum(1 for c in cache_files if c[2] == 'atom')} atom-kind "
      f"caches unstamped ({len(unstamped_all)} unstamped overall, all "
      f"free-kind — this script's own, so the refusal gap is unoccupied)")

print()
print("=" * 74)
print("2. THE REAL GUARD hits every cache — proved by no recompute")
print("=" * 74)

hits, recomputed = 0, []
for atom, n, kind, tag, p in cache_files:
    try:
        chis, path = B._load_or_compute_chi(
            atom, n, kind, Q_TAGS[tag], tag, 50, ["SENTINEL_WORD"])
        hits += 1
        print(f"  HIT   {path.name:47s} {len(chis):3d} partitions")
    except AssertionError:
        recomputed.append(p.name)
        print(f"  MISS  {p.name:47s} RECOMPUTED (would clobber)")

check("guard_hits_every_committed_cache", not recomputed,
      recomputed or f"{hits}/{len(cache_files)} hit, 0 recomputed")

print()
print("=" * 74)
print("3. OWNERSHIP REFUSAL — fires on a foreign file, not on its own")
print("=" * 74)

WRONG_Q = "1." + "2" * 49          # not any pin; forces a genuine miss
foreign = next((c for c in cache_files if c[2] == "atom"), None)
mine = next((c for c in cache_files if c[2] == "free"), None)

refused = False
if foreign is not None:
    atom, n, kind, tag, p = foreign
    try:
        B._load_or_compute_chi(atom, n, kind, WRONG_Q, tag, 50, ["S"])
    except RuntimeError as exc:
        refused = True
        print(f"  refused: {str(exc)[:110]}")
    except AssertionError:
        print(f"  !! {p.name} would have been OVERWRITTEN")
check("foreign_owned_cache_is_not_overwritten_on_a_q_mismatch",
      refused, p.name if foreign else "no atom-kind cache on disk")

own_recompute = False
if mine is not None:
    atom, n, kind, tag, p = mine
    try:
        B._load_or_compute_chi(atom, n, kind, WRONG_Q, tag, 50, ["S"])
    except AssertionError:
        own_recompute = True
    except RuntimeError as exc:
        print(f"  !! refused on its OWN file: {str(exc)[:100]}")
check("self_owned_cache_still_recomputes_on_a_q_mismatch",
      own_recompute,
      "the refusal is scoped to other producers' files, not a blanket lock")

print()
print("=" * 74)
if failures:
    print("FAILURES:", ", ".join(failures))
    sys.exit(1)
print("ALL PASSED")
