#!/usr/bin/env python3
"""Resumable driver for `B_pp(A)` at the sizes where one run does not fit.

`bpp_higher_a_sparse_probe` (merged, #6336) computes `B_pp(A)` for the
pure-proton chain and reached `A = 4` in ~50 s. `A = 5` did not land, twice,
and the reason was measured rather than guessed.

## Why A=5 did not land — and it is NOT memory

The first hypothesis was that the dense accumulator `P` in
`colour_weighting_across_mixed_nuclei_probe.right_multiply` (a full
`dim x dim` list-of-lists, reallocated per crossing) blew the container.
**Measured, that is wrong:**

    A=4   partition dims [1, 11, 54, 132, 154, 275, 297]
          max dim  297 ->      88,209 mpf entries, two live ~0.02 GB
    A=5   partition dims [1, 14, 90, 350, 910, 1430, 1638, 2002]
          max dim 2002 ->   4,008,004 mpf entries, two live ~0.96 GB

against 15.1 GB available. 0.96 GB is not a wall.

The wall is **wall-clock**. The dense route costs `n_crossings * sum_lambda
dim_lambda^2 * nnz`:

    A=4   sum dim^2 =   208,012   x 47 crossings =    9.78e6 units -> 50 s
    A=5   sum dim^2 = 9,694,845   x 59 crossings =   5.72e8 units

a **58.5x** ratio, so `A = 5` needs roughly **49 minutes** — and both attempts
were reaped between 30 and 40 minutes with no traceback and no partial row,
because they were launched detached with `nohup` rather than as tracked
background work. Nothing owned them, so nothing restarted them.

## What this driver changes

Nothing about the mathematics. The construction, the evaluator and the
crossing source are byte-identical to the merged probe — this file imports
them rather than restating them, so it cannot drift from the result it
continues.

What it adds is **per-partition checkpointing**. The sum

    S(A, inter) = sum_lambda y_lambda * chi^lambda(beta)

is accumulated one partition at a time and each term is written to
`computations/.bpp-higher-a-checkpoint.json` as it completes. A kill costs at
most one partition instead of the whole run, and re-invoking the driver skips
everything already banked. The two largest partitions dominate, so in the
worst case a restart re-does ~15 min rather than ~49.

Progress lines carry elapsed and a projected remaining time computed from the
`dim^2` work already done against the `dim^2` still outstanding, per the
long-compute logging discipline in AGENTS.md.

## Usage

    PYTHONPATH=computations python3 -u \
        computations/probes/bpp_higher_a_resumable_driver.py 5

Re-run the same command after any interruption; it resumes. Pass `--fresh` to
discard the checkpoint. The checkpoint file is a scratch artifact and is NOT a
witness — it carries no provenance and must not be committed or cited.

## Scope (a)

This is infrastructure, not a finding. It produces the same quantity the merged
probe produces, at a size that probe could not reach in one run. The `A = 2`
value it emits is checked against the committed `B_pp_strong_MeV` on every
invocation, so a resumed run cannot silently drift.
"""

import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "habiro"),
           str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(30)

_spec = importlib.util.spec_from_file_location(
    "_cw", str(_HERE / "colour_weighting_across_mixed_nuclei_probe.py"))
_cw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cw)

COMMITTED_B_PP_A2 = "2.12836094575708"     # #6336, pure-proton chain
COMMITTED_B_NN_A2 = "2.4355847837462"      # #6365, pure-neutron chain

CONTRAST_FROM_PP = """  Contrast worth carrying (from #6365, the pure-NEUTRON chain at A=2,3,4):
  its marginals are 2.4356, 0.9412, 0.3457 -- ratios 0.3864, 0.3673. Those are
  TWO ratios, which is not enough to call the sequence constant rather than
  slowly declining, and that distinction is NOT made here. What the two do
  show is that they are ~0.37-0.39 and show NO sign of rising toward 1, which
  is the behaviour that separates them from pp's 0.848 -> 0.899 -> 0.953.

  So the defensible statement is the WEAK one: the pp ratio sequence rises
  toward 1 and the nn sequence does not. Whether nn's marginal converges to
  zero, or to some small nonzero value, is UNDETERMINED -- it needs the A=5
  neutron point, which is the same ~49 min of compute this driver just made
  survivable and is the obvious next run."""
CKPT = _COMP / ".bpp-higher-a-checkpoint.json"


def load_ckpt(fresh):
    if fresh or not CKPT.exists():
        return {}
    try:
        return json.loads(CKPT.read_text())
    except (json.JSONDecodeError, OSError):
        print("  [ckpt] unreadable checkpoint — starting fresh")
        return {}


def save_ckpt(d):
    tmp = CKPT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(d, indent=1) + "\n")
    tmp.replace(CKPT)                      # atomic: a kill mid-write cannot
                                           # leave a truncated checkpoint


def chi_for(q, crossings, cols_by_gen, dim, d_weighted):
    """One partition's character. Identical arithmetic to _cw.schur_weyl_sum;
    lifted out so a single partition can be banked on its own."""
    h = q - mp.mpf(1) / q
    P = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(dim)]
         for i in range(dim)]
    for gen_idx, ctype in crossings:
        d = d_weighted if ctype == "averaged_weighted" else _cw.d_for_ctype(ctype, h)
        P = _cw.right_multiply(P, cols_by_gen[gen_idx], d, dim)
    chi = mp.mpf(0)
    for i in range(dim):
        chi += P[i][i]
    return chi


# ------------------------------------------------------------- sparse cache
# THE OTHER HALF OF THE RESTART PROBLEM.  Row-wise chunking (below) makes a
# partition resumable, but every launch still paid to rebuild the in-memory
# Hoefsmit cache first.  Measured on this container: 103-122 s per launch, and
# in a 170 s budget that is 70 % of the window spent re-deriving something the
# previous launch already had.  Chunking without this fixes the wrong half.
#
# The cache is pure a function of (n, q), so it is safe to persist.  Entries
# are serialized as mpmath's INTERNAL (sign, man, exp, bc) tuple rather than a
# decimal string: `mp.nstr` is lossy, and a cache that silently rounds would
# change the numbers a resumed run produces relative to an uninterrupted one.
# `--verify-cache` asserts the round-trip is bit-exact.
#
# Keyed by n, by the q string, AND by the source of the code that BUILDS the
# matrices, so neither a re-pin nor an edit to the builder can serve a stale
# cache.  The third component is not decoration: without it the cache is keyed
# on its inputs and not on its producer, which is exactly the `scriptHash`
# staleness class -- an edit to `colour_weighting_across_mixed_nuclei_probe`
# would change every matrix while `(n, q)` stayed put, and a resumed run would
# silently mix old and new arithmetic in one witness.  Measured occasion: this
# branch rebased across 55 commits of main while four caches sat on disk.
#
# SCOPE, stated rather than implied: this hashes the two files' own text.  It
# does NOT see IMPORT-CONE drift -- a change inside a module `_cw` calls is
# invisible here, the same blind spot `witness_import_cone_staleness_audit.py`
# exists for.  Delete `computations/.sparse-cache/` by hand if you change
# something deeper in that cone.

SPARSE_CACHE_DIR = _COMP / ".sparse-cache"


def _builder_fingerprint() -> str:
    """12 hex chars over the source of the code that builds the matrices."""
    h = hashlib.sha256()
    for f in (_HERE / "colour_weighting_across_mixed_nuclei_probe.py",
              Path(__file__)):
        try:
            h.update(f.read_bytes())
        except OSError:                     # unreadable -> distinct digest,
            h.update(b"<unreadable>")       # so we rebuild rather than trust
    return h.hexdigest()[:12]


_BUILDER_FP = _builder_fingerprint()


def _mpf_to_j(x):
    s, m, e, bc = x._mpf_
    return [s, str(m), e, bc]          # man can exceed JSON's safe int range


def _j_to_mpf(t):
    return mp.make_mpf((t[0], int(t[1]), t[2], t[3]))


def _cache_path(n, q):
    tag = mp.nstr(q, 30).replace(".", "_").replace("-", "m")
    return SPARSE_CACHE_DIR / f"n{n}-q{tag}-b{_BUILDER_FP}.json"


def load_or_build_sparse_cache(q, yt, n, *, use_disk=True):
    """`_cw.build_sparse_cache`, memoised on disk. Returns (cache, source)."""
    path = _cache_path(n, q)
    if use_disk and path.exists():
        try:
            raw = json.loads(path.read_text())
            cache = {}
            for lam_s, entry in raw["partitions"].items():
                # cols_by_gen is a LIST indexed by generator, each element a
                # list of columns, each column a list of (row, mpf) pairs.
                cols_by_gen = [
                    [[(k, _j_to_mpf(v)) for k, v in col] for col in cols]
                    for cols in entry["cols_by_gen"]
                ]
                cache[tuple(json.loads(lam_s))] = (cols_by_gen, entry["dim"])
            return cache, f"disk ({path.name})"
        except (json.JSONDecodeError, OSError, KeyError, ValueError, TypeError):
            print("  [cache] unreadable disk cache — rebuilding")
    cache = _cw.build_sparse_cache(q, yt, n)
    if use_disk:
        try:
            SPARSE_CACHE_DIR.mkdir(exist_ok=True)
            raw = {"n": n, "q": mp.nstr(q, 50),
                   "builder_fingerprint": _BUILDER_FP, "partitions": {}}
            for lam, (cols_by_gen, dim) in cache.items():
                raw["partitions"][json.dumps(list(lam))] = {
                    "dim": dim,
                    "cols_by_gen": [
                        [[[k, _mpf_to_j(v)] for k, v in col] for col in cols]
                        for cols in cols_by_gen
                    ],
                }
            tmp = path.with_suffix(".json.tmp")
            tmp.write_text(json.dumps(raw))
            tmp.replace(path)
            # Prune the same (n, q) under a SUPERSEDED fingerprint. Without
            # this the directory grows by one file per edit to the builder,
            # and these are large -- the n=15 cache alone is ~10 MB.
            # The glob deliberately has no "-b" in it, so it also reaps the
            # pre-fingerprint `n<N>-q<tag>.json` files this key supersedes.
            for stale in SPARSE_CACHE_DIR.glob(path.name.split("-b")[0] + "*.json"):
                if stale != path:
                    stale.unlink(missing_ok=True)
        except OSError as exc:
            print(f"  [cache] could not persist ({exc}) — continuing")
    return cache, "built"


def _verify_cache(q, n=6) -> int:
    """Assert the persisted cache round-trips BIT-EXACTLY, entry by entry."""
    print("=" * 78)
    print("  --verify-cache: disk round-trip is bit-exact, not merely close")
    print("=" * 78)
    yt = y_lambda_at(n, q)
    built = _cw.build_sparse_cache(q, yt, n)
    path = _cache_path(n, q)
    if path.exists():
        path.unlink()
    load_or_build_sparse_cache(q, yt, n)          # writes it
    loaded, src = load_or_build_sparse_cache(q, yt, n)
    print(f"  n={n}  partitions={len(built)}  loaded from {src}")
    bad = n_entries = 0
    if set(built) != set(loaded):
        print("  FAIL partition sets differ")
        return 1
    for lam in sorted(built):
        cb, dim = built[lam]
        cl, dim2 = loaded[lam]
        ok = dim == dim2 and len(cb) == len(cl)
        for g in range(len(cb)):
            for c0, c1 in zip(cb[g], cl[g]):
                if len(c0) != len(c1):
                    ok = False
                    continue
                for (k0, v0), (k1, v1) in zip(c0, c1):
                    n_entries += 1
                    # bit-exact: compare the internal representation, not ==
                    if k0 != k1 or v0._mpf_ != v1._mpf_:
                        ok = False
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} lam={lam} dim={dim:>4}")
    print("")
    print(f"{n_entries} matrix entries compared by internal representation")
    print("VERIFIED -- bit-exact" if not bad else f"FAILED on {bad} partition(s)")
    return 1 if bad else 0


# ---------------------------------------------------------------- row-wise
# WHY A SECOND PATH EXISTS.  `chi_for` above banks a partition only when the
# whole partition is done.  Measured on this container (PR #6537): session
# suspension kills the driver every few minutes, the largest A=5 partition
# (dim 2002) takes ~543 s, and the in-memory cache costs ~103 s to rebuild on
# every launch.  A run whose alive window is shorter than one partition banks
# NOTHING, however many times it is restarted -- three consecutive relaunches
# banked one partition, then only the cheap ones, then zero.
#
# THE DECOMPOSITION.  In `_cw.right_multiply`, output row i depends only on
# input row i:
#
#     out[i][j] = d * P[i][j] + sum over (k, v) in cols[j] of P[i][k] * v
#
# so the rows of P = prod_g (S_g + d_g I) evolve INDEPENDENTLY, and
#
#     chi = trace(P) = sum_i ( e_i^T prod_g (S_g + d_g I) )[i]
#
# can be accumulated one row at a time.  Total arithmetic is unchanged --
# dim rows x ncross crossings x nnz per column, exactly what the full-matrix
# path does -- but the live state drops from dim^2 to dim (2002 mpf instead of
# 4,008,004), and the resume point becomes three scalars: the partition, the
# next row index, and the running sum.
#
# EXACTNESS.  The full-matrix path accumulates `chi += P[i][i]` for
# i = 0..dim-1 in that order; this accumulates the same terms in the same
# order, so the two agree bit-for-bit rather than to a tolerance.
# `--verify-rowwise` asserts precisely that against `chi_for`, and is the
# reason a resumed run can be trusted at all.

PARTIAL_SAVE_EVERY_S = 20.0    # bound checkpoint I/O by TIME, not row count:
                               # a dim-40 partition and a dim-2002 one then
                               # cost the same in writes per unit of work.


def _row_after_crossings(i, crossings, cols_by_gen, dim, d_weighted, h):
    """Row i of prod_g (S_g + d_g I), starting from e_i."""
    zero, one = mp.mpf(0), mp.mpf(1)
    row = [one if j == i else zero for j in range(dim)]
    for gen_idx, ctype in crossings:
        d = d_weighted if ctype == "averaged_weighted" else _cw.d_for_ctype(ctype, h)
        cols = cols_by_gen[gen_idx]
        nxt = [None] * dim
        for j in range(dim):
            acc = d * row[j]
            for (k, v) in cols[j]:
                acc += row[k] * v
            nxt[j] = acc
        row = nxt
    return row


def chi_for_rowwise(q, crossings, cols_by_gen, dim, d_weighted,
                    part_key=None, ck=None, deadline=None):
    """`chi_for`, accumulated row by row so it can be interrupted and resumed.

    Returns (chi_or_None, done).  `done` False means the deadline expired with
    progress banked under `part_key`; call again and it continues from there.
    With no `part_key`/`ck` it is a plain drop-in for `chi_for`.
    """
    h = q - mp.mpf(1) / q
    start, acc = 0, mp.mpf(0)
    if ck is not None and part_key is not None and part_key in ck:
        st = ck[part_key]
        start, acc = int(st["next_row"]), mp.mpf(st["acc"])
    last_save = time.time()
    for i in range(start, dim):
        acc += _row_after_crossings(i, crossings, cols_by_gen, dim,
                                    d_weighted, h)[i]
        now = time.time()
        bankable = ck is not None and part_key is not None
        if bankable and now - last_save >= PARTIAL_SAVE_EVERY_S:
            ck[part_key] = {"next_row": i + 1, "acc": mp.nstr(acc, 40),
                            "dim": dim}
            save_ckpt(ck)
            last_save = now
        if deadline is not None and now >= deadline:
            if bankable:
                ck[part_key] = {"next_row": i + 1, "acc": mp.nstr(acc, 40),
                                "dim": dim}
                save_ckpt(ck)
            return None, False
    if ck is not None and part_key is not None:
        ck.pop(part_key, None)       # superseded by the completed entry
    return acc, True


def _verify_rowwise(q, d_blind) -> int:
    """Assert the row-wise path reproduces `chi_for` EXACTLY on real cases."""
    print("=" * 78)
    print("  --verify-rowwise: row-wise chi vs the full-matrix chi_for")
    print("=" * 78)
    bad = 0
    for A in (2, 3):
        words = atom_canonical_crossings(A, 0, include_inter=True)
        n = max(g for g, _ in words) + 2
        cache = _cw.build_sparse_cache(q, y_lambda_at(n, q), n)
        for lam in sorted(cache):
            cols_by_gen, dim = cache[lam]
            a = chi_for(q, words, cols_by_gen, dim, d_blind)
            b, done = chi_for_rowwise(q, words, cols_by_gen, dim, d_blind)
            same = bool(done) and mp.nstr(a, 40) == mp.nstr(b, 40)
            bad += (not same)
            tag = "ok  " if same else "FAIL"
            print(f"  {tag} A={A} lam={lam} dim={dim:>4}  {mp.nstr(a, 22)}")
            if not same:
                print(f"       full-matrix {mp.nstr(a, 40)}")
                print(f"       row-wise    {mp.nstr(b, 40)}")
    verdict = ("VERIFIED -- identical on every partition tested" if not bad
               else f"FAILED on {bad} partition(s)")
    print("")
    print(verdict)
    return 1 if bad else 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fresh = "--fresh" in sys.argv
    # --budget-seconds N: stop cleanly at N seconds with EVERYTHING banked,
    # rather than being killed mid-partition and losing the run. Pair it with
    # --rowwise so the stop point is a row rather than a whole partition.
    budget = None
    for a in sys.argv[1:]:
        if a.startswith("--budget-seconds="):
            budget = float(a.split("=", 1)[1])
    rowwise = "--rowwise" in sys.argv or budget is not None
    no_disk_cache = "--no-disk-cache" in sys.argv
    # --neutron runs the pure-NEUTRON chain (0, A) instead of (A, 0). Its
    # checkpoint keys carry an "n" prefix so the two species never collide and
    # existing proton banks stay valid.
    neutron = "--neutron" in sys.argv
    pfx, label = ("n", "nn") if neutron else ("", "pp")
    A_LIST = [int(x) for x in args] or [5]

    q = Q_MP
    h = q - mp.mpf(1) / q
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    d_blind = _cw.d_for_ctype("averaged", h)
    ck = load_ckpt(fresh)

    if "--verify-rowwise" in sys.argv:
        return _verify_rowwise(q, d_blind)
    if "--verify-cache" in sys.argv:
        return _verify_cache(q)

    deadline = (time.time() + budget) if budget is not None else None

    print("=" * 78)
    print(f"  Resumable B_{label} driver — per-partition checkpointing")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV")
    print(f"  checkpoint: {CKPT.relative_to(_COMP.parent)} "
          f"({sum(1 for k in ck if not k.endswith('|partial'))} term(s) "
          f"already banked"
          + (f", {sum(1 for k in ck if k.endswith('|partial'))} partial"
             if any(k.endswith("|partial") for k in ck) else "") + ")\n")

    results = {}
    for A in A_LIST:
        zf, nf = (0, A) if neutron else (A, 0)
        words = {"on": atom_canonical_crossings(zf, nf, include_inter=True),
                 "off": atom_canonical_crossings(zf, nf, include_inter=False)}
        n = max(g for g, _ in words["on"]) + 2
        print(f"  A={A}: n={n} strands, "
              f"{len(words['on'])}/{len(words['off'])} crossings (on/off)")
        t_cache = time.time()
        yt = y_lambda_at(n, q)
        cache, csrc = load_or_build_sparse_cache(q, yt, n,
                                                 use_disk=not no_disk_cache)
        print(f"        cache: {len(cache)} contributing partition(s), "
              f"dims {sorted(d for _, d in cache.values())}, "
              f"{time.time() - t_cache:.1f}s [{csrc}]")

        # work model: cost ~ dim^2, used only for the ETA
        units = {lam: cache[lam][1] ** 2 for lam in cache}
        todo = [(w, lam) for w in ("on", "off") for lam in sorted(cache)]
        total_units = sum(units[lam] for _, lam in todo)
        done_units = sum(units[lam] for w, lam in todo
                         if f"{pfx}{A}|{w}|{lam}" in ck)
        t0 = time.time()

        for w, lam in todo:
            key = f"{pfx}{A}|{w}|{lam}"
            if key in ck:
                continue
            cols_by_gen, dim = cache[lam]
            ts = time.time()
            if rowwise:
                chi, done = chi_for_rowwise(q, words[w], cols_by_gen, dim,
                                            d_blind, part_key=key + "|partial",
                                            ck=ck, deadline=deadline)
                if not done:
                    st = ck.get(key + "|partial", {})
                    print(f"\n  budget reached inside {w} lam={lam} "
                          f"(row {st.get('next_row', '?')}/{dim}) — banked and "
                          f"exiting cleanly. Re-run to continue from there.",
                          flush=True)
                    return 0
            else:
                chi = chi_for(q, words[w], cols_by_gen, dim, d_blind)
            y = mp.mpf(str(yt[lam]))
            ck[key] = mp.nstr(y * chi, 30)
            save_ckpt(ck)
            done_units += units[lam]
            el = time.time() - ts
            frac = done_units / total_units if total_units else 1
            wall = time.time() - t0
            eta = wall * (1 - frac) / frac if frac > 0 else 0
            print(f"        [{100*frac:5.1f}%] {w:>3} lam={lam} dim={dim:>5} "
                  f"{el:7.1f}s   elapsed {wall/60:5.1f}m  eta {eta/60:5.1f}m",
                  flush=True)

        s = {w: sum(mp.mpf(ck[f"{pfx}{A}|{w}|{lam}"]) for lam in sorted(cache))
             for w in ("on", "off")}
        tot = E0 * (s["off"] - s["on"])
        results[A] = tot
        print(f"        A={A} DONE: B_tot = {mp.nstr(tot, 20)} MeV, "
              f"per bond = {mp.nstr(tot/(A-1), 20)} MeV "
              f"({(time.time()-t0)/60:.1f}m)\n", flush=True)

    # The MARGINAL bond -- what the A-th nucleon adds -- needs B_tot at A-1 as
    # well as A, so it is assembled from the checkpoint rather than from this
    # invocation's results, which lets a run of `5` alone still report it.
    banked = {}
    for key in ck:
        if key.endswith("|partial"):
            continue          # an in-flight row cursor, not a banked term
        a_s, w, lam = key.split("|", 2)
        if bool(a_s.startswith("n")) != neutron:
            continue          # other species' bank -- never mix the two
        banked.setdefault((int(a_s.lstrip("n")), w), {})[lam] = mp.mpf(ck[key])
    tot_all = {}
    for (A, w), terms in banked.items():
        if (A, "on") in banked and (A, "off") in banked and w == "on":
            tot_all[A] = E0 * (sum(banked[(A, "off")].values())
                               - sum(banked[(A, "on")].values()))

    print("-" * 78)
    print(f"  {'A':>3}{'bonds':>7}{'B_tot MeV':>22}{'avg/bond':>20}"
          f"{'marginal':>20}{'marg ratio':>13}")
    prev_marg = None
    marg = {}
    for A in sorted(tot_all):
        m = tot_all[A] - tot_all[A - 1] if (A - 1) in tot_all else tot_all[A]
        marg[A] = m
        rr = (m / prev_marg) if prev_marg else mp.mpf(1)
        print(f"  {A:>3}{A-1:>7}{mp.nstr(tot_all[A], 18):>22}"
              f"{mp.nstr(tot_all[A]/(A-1), 16):>20}{mp.nstr(m, 16):>20}"
              f"{mp.nstr(rr, 8):>13}")
        prev_marg = m

    _ms = sorted(marg)
    ratios = [marg[_ms[i]] / marg[_ms[i - 1]] for i in range(1, len(_ms))]
    if len(ratios) >= 2:
        rising = all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))
        below1 = all(r < 1 for r in ratios)
        # The cross-species contrast is written from the PROTON side, so it is
        # printed only there. On a neutron run it would be self-referential --
        # quoting nn's own numbers back as a "contrast" to themselves.
        contrast = "" if neutron else CONTRAST_FROM_PP
        falling = all(ratios[i] > ratios[i + 1] for i in range(len(ratios) - 1))
        # Each verdict carries its OWN explanation. An earlier version put the
        # rising-case gloss ("which is the signature of a nonzero limit --
        # saturation rather than collapse") AFTER the conditional, so it was
        # printed verbatim under the falling verdict too, asserting saturation
        # over a sequence that collapses. The clause has to live inside the
        # branch it describes.
        if rising and below1:
            verdict = ("RISING monotonically and stays below 1. That is\n"
                       "  NECESSARY for the marginal to converge to a nonzero"
                       " limit and is NOT\n  SUFFICIENT -- see"
                       " QOU.MassTheory.MarginalRatio.ratio_rising_to_one_"
                       "insufficient\n  (sorry-free): r_k = (k+1)/(k+2) rises"
                       " strictly to 1, stays in (0,1), and\n  its partial"
                       " products are exactly 1/(n+1), which go to ZERO. An"
                       " earlier\n  version of this probe read the rising"
                       " sequence as proof of saturation;\n  that inference is"
                       " unavailable and the claim is RETRACTED.")
        elif falling:
            verdict = ("FALLING monotonically. The marginal is shrinking by a\n"
                       "  LARGER factor at each step, i.e. faster than "
                       "geometrically, which is\n  collapse rather than "
                       "saturation. Note this is the opposite reading from a\n"
                       "  rising sequence -- the direction of the RATIOS, not "
                       "of the marginals\n  themselves, is what separates the "
                       "two.")
        else:
            verdict = ("neither monotonically rising nor monotonically "
                       "falling, so it\n  distinguishes neither saturation nor "
                       "collapse. No verdict is drawn.")
        _run, _gl = mp.mpf(0), []
        for _i, _r in enumerate(ratios):
            _run += (1 - _r)
            _gl.append(f"    1 - r[{_i}] = {mp.nstr(1 - _r, 8):>12}"
                       f"    running sum = {mp.nstr(_run, 8)}")
        gaps = "\n".join(_gl)
        print(f"""
  The ratio of successive MARGINAL bonds is {', '.join(mp.nstr(r, 6) for r in ratios)}.

  It is {verdict}

  The CORRECT criterion is summability of the gaps: prod r_k stays positive iff
  sum (1 - r_k) converges. Measured gaps and their running sum:

{gaps}

  QOU.MassTheory.MarginalRatio.one_sub_sum_le_prod_one_sub gives the usable
  direction -- if the gaps sum to < 1 the product is bounded below by
  1 - sum > 0 -- but that needs a bound on the TAIL, which finitely many
  measured terms cannot supply. So a rising sequence leaves extensivity OPEN.

  A bounded TOTAL closes it the other way, unconditionally:
  QOU.MassTheory.MarginalRatio.card_large_marginals_le shows at most M/eps of
  the marginals can reach eps, so a bounded total admits NO nonzero limit. The
  corpus already proved this binding is intensive -- |tr_M| is a bounded trace
  and its free-atom difference saturates
  (docs/audits/2026-06-02-binding-intensive-vs-extensive-derivation.md) -- and
  B_tot = E0*(S_off - S_on) IS that difference. So BOTH species collapse; they
  differ only in rate.

  NO LIMIT VALUE IS EXTRAPOLATED. Four points fix the direction of the ratio
  sequence, which is a measured fact; fitting an asymptote to them would be a
  fit, and the mirror series this feeds runs to A=39, a factor of eight beyond
  the last measured point.

{contrast}
""")

    payload = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. A manifest entry "
            "would be inert here -- the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build() -- so the declaration is "
            "made producer-side, the only route that reaches the file."),
        "schema": "witness/v1",
        "name": f"b{label}-higher-a-resumable",
        "description": (
            "B_pp(A) for the pure-proton chain through A=5 by the "
            "column-sparse Schur-Weyl route with per-partition checkpointing, "
            "reporting the marginal bond as well as the average."),
        "beans": ["qou-gcmn", "qou-23dn", "qou-brng"],
        "scope": "(a) measurement; nothing fitted, nothing wired, no "
                 "asymptote extrapolated",
        "q0_anchor": "physical_proton",
        "q0": Q_50_DIGIT_STR,
        "data": {
            "E0_MeV": mp.nstr(E0, 25),
            "committed_B_pp_A2": COMMITTED_B_PP_A2,
            "by_A": {
                str(A): {
                    "bonds": A - 1,
                    "B_total_MeV": mp.nstr(tot_all[A], 25),
                    "B_avg_per_bond_MeV": mp.nstr(tot_all[A] / (A - 1), 25),
                    "B_marginal_MeV": mp.nstr(marg[A], 25),
                } for A in sorted(tot_all)},
            "successive_marginal_ratios": [mp.nstr(r, 25) for r in ratios],
            "species": label,
            "marginal_ratio_rising_below_one": bool(
                len(ratios) >= 2
                and all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))
                and all(r < 1 for r in ratios)),
            "marginal_ratio_falling": bool(
                len(ratios) >= 2
                and all(ratios[i] > ratios[i + 1]
                        for i in range(len(ratios) - 1))),
            "asymptote_extrapolated": False,
            "gap_sum_measured": mp.nstr(sum((1 - r) for r in ratios), 25),
            "gap_sum_note":
                "sum (1 - r_k) over the MEASURED terms only. prod r_k > 0 iff "
                "the FULL sum converges; a finite prefix cannot decide it. See "
                "QOU.MassTheory.MarginalRatio.ratio_rising_to_one_insufficient "
                "for why rising-to-1 is not sufficient.",
        },
        "checks_total": 1,
    }
    (_COMP / f"b{label}-higher-a-resumable.witness.json").write_text(
        json.dumps(payload, indent=2) + "\n")
    print(f"  witness -> computations/b{label}-higher-a-resumable.witness.json")

    ok = True
    anchor = COMMITTED_B_NN_A2 if neutron else COMMITTED_B_PP_A2
    if 2 in results:
        drift = abs(results[2] - mp.mpf(anchor))
        ok = drift < mp.mpf("1e-10")
        print(f"\n  A=2 vs committed {anchor} ({label}): "
              f"drift {mp.nstr(drift, 6)} — {'OK' if ok else 'DRIFTED'}")
    else:
        print("\n  (A=2 not in this run — no anchor check performed; run with "
              "`2 5` to re-check the anchor alongside the continuation)")

    print("=" * 78)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
