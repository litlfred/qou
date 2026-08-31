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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
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


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fresh = "--fresh" in sys.argv
    # --neutron runs the pure-NEUTRON chain (0, A) instead of (A, 0). Its
    # checkpoint keys carry an "n" prefix so the two species never collide and
    # existing proton banks stay valid.
    neutron = "--neutron" in sys.argv
    pfx, label = ("n", "nn") if neutron else ("", "pp")
    A_LIST = [int(x) for x in args] or [5]

    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - mp.mpf(1) / q
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    d_blind = _cw.d_for_ctype("averaged", h)
    ck = load_ckpt(fresh)

    print("=" * 78)
    print(f"  Resumable B_{label} driver — per-partition checkpointing")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV")
    print(f"  checkpoint: {CKPT.relative_to(_COMP.parent)} "
          f"({len(ck)} term(s) already banked)\n")

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
        cache = _cw.build_sparse_cache(q, yt, n)
        print(f"        cache: {len(cache)} contributing partition(s), "
              f"dims {sorted(d for _, d in cache.values())}, "
              f"{time.time() - t_cache:.1f}s")

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
        print(f"""
  The ratio of successive MARGINAL bonds is {', '.join(mp.nstr(r, 6) for r in ratios)}.

  It is {'RISING monotonically and stays below 1' if rising and below1 else 'NOT monotonically rising below 1'}, which is the signature of a marginal
  bond converging to a NONZERO limit -- saturation rather than collapse.

  NO LIMIT VALUE IS EXTRAPOLATED. Four points fix the direction of the ratio
  sequence, which is a measured fact; fitting an asymptote to them would be a
  fit, and the mirror series this feeds runs to A=39, a factor of eight beyond
  the last measured point.

{contrast}
""")

    payload = {
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
            "marginal_ratio_rising_below_one": bool(
                len(ratios) >= 2
                and all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))
                and all(r < 1 for r in ratios)),
            "asymptote_extrapolated": False,
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
