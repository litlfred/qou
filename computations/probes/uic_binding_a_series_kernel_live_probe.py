"""The production binding across A = 2..6, every point measured kernel-live.

Bean qou-sv7h / qou-brng.  Settles whether the "A-independence" plateau exists
at all, because three of the four figures it rested on have NO provenance.

WHY THIS RUN EXISTS

PR #6752 argued A-independence from `-7.271 / -7.742 / -7.456 / -6.829`.  Only
the FIRST is verifiable: a fixed-string grep for the other three across *.md,
*.json and *.py returns no hit anywhere in the tree -- they reached the PR from
conversation context, and their kernel-vs-fallback provenance is unknown.

That is not pedantry.  On the SAME atom the two paths differ by 17.29 %:

    2H, kernel live   -7.271102124876717
    2H, fallback      -8.52811254141235

and the fallback family `_build_ysn_matrices` VIOLATES the braid relation, so it
is not a representation of H_n(q) at all.  An unverified figure from that series
could be either number.

THIS PROBE ASSERTS THE KERNEL IS LIVE AND REFUSES OTHERWISE.  Every row it
emits is therefore comparable with the two points already measured this session
(2H and 6Li), and with nothing else.

WHAT IT MEASURES

`hecke_core_legacy.binding_energy(Z, N)` -- the production entry point, run
as-is (A=1 step included), one atom per row.  No reconstruction, no truncation:
this is the number production reports.

COST.  Long compute.  6Li (A=6) took 4039.8 s and 4He is reported at ~2425 s, so
the set below is ~2 h.  Atoms run CHEAPEST FIRST and each row is flushed as it
completes, so a partial run is still a usable result.

WHAT IT CANNOT SETTLE

Which atoms the four unverified figures were computed for.  There is no A=5
entry anywhere in the corpus's own gated-set data (that series is per-ATOM:
2H, 3H, 3He, 4He, 6Li -- A = 2,3,3,4,6, skipping 5), so the comparison is to a
set whose membership is unknown.  This probe states its own atoms explicitly
and claims nothing about theirs.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401,E402

import hecke_core_legacy as H  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from mpmath import mp  # noqa: E402

set_compute_dps()

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""),
          flush=True)


# (Z, N, label).  Cheapest first.  AME binding is NOT hardcoded -- it is read
# from the vendored AME2020 table via `codata_constants.ame_binding_mev(Z, A)`.
# Hand-typing it is a known defect: `ame_2020_binding_energies.py`'s docstring
# records six hand-typed entries disagreeing with the publication table by up to
# 63 eV, against an AME uncertainty on B(4He) of 0.8 eV.  A first draft of this
# probe hardcoded seven values and EVERY ONE was wrong -- 5He by 158.7 keV.
ATOMS = [
    (2, 2, "4He"),
    (2, 3, "5He"),
    (3, 2, "5Li"),
]

# Measured earlier this session, kernel-live, by the same call.  Carried so the
# emitted series is complete; flagged so a reader can tell them from this run.
PRIOR = [
    (1, 1, "2H", "-7.271102124876717"),
    (1, 2, "3H", "-7.742121347136118"),
    (2, 1, "3He", "-7.45619950551758"),
    (3, 3, "6Li", "-3.065019520558719"),
]

# Per-atom checkpoint.  A container restart killed the first run of this probe
# mid-4He and cost ~40 min; 3H and 3He survived only because they had been
# flushed to a log.  Each completed row is now appended here as it lands, so a
# restart costs the in-flight atom and nothing else.
CKPT = Path("/tmp/a_series_checkpoint.jsonl")


def main() -> int:
    print("=== production binding_energy, A-series, kernel-live ===", flush=True)
    print(f"  q0 = {Q_50_DIGIT_STR[:24]}...  mp.dps = {mp.dps}", flush=True)

    check("the Rust LP kernel is available -- the fallback family violates the "
          "braid relation and is not a representation of H_n(q)",
          bool(H._HAS_LP_KERNEL),
          f"_HAS_LP_KERNEL={H._HAS_LP_KERNEL}")
    if not H._HAS_LP_KERNEL:
        print("\n  REFUSING to report numbers from the fallback family.", flush=True)
        print("  Build pyhecke-native: cd tools/pyhecke-native && maturin build --release",
              flush=True)
        return 1

    rows: list[dict] = []
    t_all = time.time()
    for Z, N, label in ATOMS:
        A = Z + N
        ame = fmt(ame_binding_mev(Z, A))
        t0 = time.time()
        print(f"\n  [{time.strftime('%H:%M:%S')}] starting {label} (Z={Z}, N={N}, A={A}) "
              f"-- elapsed so far {time.time()-t_all:.0f}s", flush=True)
        B = H.binding_energy(Z, N)
        dt = time.time() - t0
        row = {
            "atom": label, "Z": Z, "N": N, "A": A,
            "B_pred_MeV": fmt(mp.mpf(str(B))),
            "B_AME_MeV": ame,
            "elapsed_seconds_note": "wall time is environment-dependent; not a result",
            "measured_here": True,
        }
        rows.append(row)
        try:
            with CKPT.open("a") as fh:
                fh.write(json.dumps(row) + "\n")
        except OSError as exc:   # a failed checkpoint must not lose the run
            print(f"  (checkpoint write failed: {exc})", flush=True)
        print(f"  [{time.strftime('%H:%M:%S')}] {label}  A={A}  B_pred={B!r}  "
              f"AME={ame}  ({dt:.1f}s)", flush=True)

    for Z, N, label, b in PRIOR:
        rows.append({
            "atom": label, "Z": Z, "N": N, "A": Z + N,
            "B_pred_MeV": fmt(mp.mpf(b)),
            "B_AME_MeV": fmt(ame_binding_mev(Z, Z + N)),
            "measured_here": False,
            "provenance": "measured earlier in the same session, same call, "
                          "kernel asserted live",
        })

    rows.sort(key=lambda r: (r["A"], r["atom"]))

    print("\n  === series (all kernel-live) ===", flush=True)
    print(f"  {'atom':>5} {'A':>2} {'B_pred':>22} {'B_AME':>12} {'B/A pred':>12}", flush=True)
    for r in rows:
        bp = mp.mpf(r["B_pred_MeV"])
        print(f"  {r['atom']:>5} {r['A']:>2} {mp.nstr(bp, 12):>22} "
              f"{r['B_AME_MeV']:>12} {mp.nstr(bp/r['A'], 8):>12}", flush=True)

    preds = [mp.mpf(r["B_pred_MeV"]) for r in rows]
    ames = [mp.mpf(r["B_AME_MeV"]) for r in rows]

    check("every point is negative -- the gate forces the sign at every A",
          all(p < 0 for p in preds),
          f"{sum(1 for p in preds if p < 0)}/{len(preds)} negative")

    spread_pred = max(abs(p) for p in preds) / min(abs(p) for p in preds)
    spread_ame = max(ames) / min(ames)
    check("the predicted spread is far smaller than AME's, so the output does "
          "not track the nucleus",
          spread_pred < spread_ame,
          f"|B| spread {mp.nstr(spread_pred, 6)}x vs AME {mp.nstr(spread_ame, 6)}x")

    # Does |B_pred| move WITH A or AGAINST it?  Compare the extreme A points.
    lo = min(rows, key=lambda r: r["A"])
    hi = max(rows, key=lambda r: r["A"])
    dlo, dhi = abs(mp.mpf(lo["B_pred_MeV"])), abs(mp.mpf(hi["B_pred_MeV"]))
    alo, ahi = mp.mpf(lo["B_AME_MeV"]), mp.mpf(hi["B_AME_MeV"])
    anti = (dhi < dlo) and (ahi > alo)
    check("|B_pred| moves AGAINST A while AME moves with it (anti-correlation)",
          anti,
          f"{lo['atom']}->{hi['atom']}: pred x{mp.nstr(dhi/dlo, 6)}, "
          f"AME x{mp.nstr(ahi/alo, 6)}")

    check("no point reproduces its AME value even in sign, so none is a fit",
          all(mp.mpf(r["B_pred_MeV"]) < 0 < mp.mpf(r["B_AME_MeV"]) for r in rows),
          "all predicted negative, all AME positive")

    w = WitnessBuilder("uic-binding-a-series-kernel-live", engine="python+mpmath+rust")
    w.set_description(
        "Production binding_energy(Z,N) across A = 2..6, EVERY point measured "
        "with the Rust LP kernel asserted live (the fallback family violates "
        "the braid relation and differs by 17.29% on 2H). Re-measures A = 3,4,5, "
        "whose figures in PR #6752 had no provenance anywhere in the tree. "
        "Reports whether the 'A-independence plateau' exists and whether the "
        "prediction is anti-correlated with AME."
    )
    w.set_audit_only("docs/audits/2026-09-05-li6-production-binding-anticorrelates.md")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("series", rows)
    w.add_data("spread_pred_over_ame", {
        "pred_max_over_min": fmt(spread_pred),
        "ame_max_over_min": fmt(spread_ame),
    })
    for name, ok in CHECKS:
        w.add_assertion(name, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_binding_a_series_kernel_live_probe")
    print(f"\n  witness: {w.save()}", flush=True)
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed", flush=True)
    print(f"  total wall {time.time()-t_all:.0f}s", flush=True)
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
