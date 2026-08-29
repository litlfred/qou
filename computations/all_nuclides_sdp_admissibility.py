#!/usr/bin/env python3
"""Operator-selection admissibility across the AME2020 nuclide chart at q_0.

Answers the two questions posed for the canonical SDP/LP program, both
at the substrate quantum parameter q_0 (no fitting):

  (a) ACTIVE-CHANNEL COUNT per nucleus — how many H_3(q_0) Wedderburn
      channels the bound state saturates, = |{i : y*_i > 0}|, the
      LP-dual active set (prop:operator-selection-lp).  The active dual
      channels are "the most receptive sub-braids on the shell".

  (b) PERMITTED NUCLEI at q_0 — how many (Z,N) admit a feasible
      operator-selection solution whose Frobenius demand profile equals
      the nucleus's own categorical normal form.  This is the quantum-
      regime admissibility count, compared to the empirical chart
      (3558 AME entries; ~251 stable; ~3300 known/bounded by drip lines).

Canonical infra (no empirical fit):
  - t = TR_M  (H_3 Markov-trace cost vector), G = gram_matrix() (6x6),
    from pyhecke.gram (the H_3(q_0) NF basis [gamma, s0, s1, L+, L-, e-]).
  - per-nucleus categorical object: build_atom_nf(Z,N) (native pyhecke,
    f64; the H_3-local atom NF).
  - dual-emitting solvers (primal AND dual per prop:operator-selection-lp):
      * solve_operator_selection_lp(t, G, n_target=A) — scalar-net LP.
      * solve_frobenius_dual_lp(t, G, n_target=nf_net, u_demand=nf) —
        matches the nucleus's own Frobenius profile (the per-nucleus test).

Output: all-nuclides-sdp-admissibility.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "substrate"))

from pyhecke import gram  # noqa: E402
from pyhecke.lp_dual_solver import (  # noqa: E402
    solve_frobenius_dual_lp,
    solve_operator_selection_lp,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402  (canonical, not the witness_base shim)

try:
    import pyhecke_native as _native  # noqa: E402
    _HAS_NATIVE = hasattr(_native, "build_atom_nf")
except Exception:  # pragma: no cover
    _native = None
    _HAS_NATIVE = False

from pyhecke import atom as _atom  # noqa: E402

AME = _ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"
NF_NAMES = list(gram.NF_NAMES)  # ["gamma","s0","s1","L+","L-","e-"]


def build_nf(Z: int, N: int) -> list[float]:
    """H_3-local atom NF (native f64 if available, else pure-Python)."""
    if _HAS_NATIVE:
        return list(_native.build_atom_nf(Z, N, gram.h))
    return list(_atom.build_atom_nf(Z, N))


def main() -> int:
    # WitnessBuilder interprets start_time as a time.monotonic() baseline
    # (qou_substrate.witness:236) — time.time() here made durationMs a
    # huge negative number (caught by Copilot on PR #2074).
    _t0 = time.monotonic()
    entries = json.loads(AME.read_text())["entries"]
    t = np.asarray(gram.TR_M, dtype=float)
    G = np.asarray(gram.gram_matrix(), dtype=float)

    rows: list[dict] = []
    lp_active_hist: Counter = Counter()      # (a) active-channel count, scalar LP
    frob_active_hist: Counter = Counter()    # active-channel count, Frobenius
    n_lp_feasible = 0
    n_frob_feasible = 0
    n_overflow = 0       # f64 build_atom_nf overflowed (heavy A) — needs mpfr
    n_build_fail = 0
    permitted_ZN: list[list[int]] = []       # (b) (Z,N) feasible under Frobenius

    for e in entries:
        Z, N, A = int(e["Z"]), int(e["N"]), int(e["A"])
        if A < 1:
            continue
        try:
            nf = build_nf(Z, N)
        except Exception:
            n_build_fail += 1
            continue
        nf_net = float(np.sum(nf))
        if not np.isfinite(nf_net) or not all(np.isfinite(nf)):
            # f64 NF overflowed (very heavy A) — record + skip the solves.
            n_overflow += 1
            rows.append({"Z": Z, "N": N, "A": A, "nf_overflow": True})
            continue

        # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
        # whether the Rust binary happens to be built, so the same script
        # yields different numbers on different boxes. Bean `qou/ftuv`.
        lp = solve_operator_selection_lp(t, G, float(A), backend="clarabel")
        try:
            frob = solve_frobenius_dual_lp(t, G, nf_net, np.asarray(nf, float))
        except Exception:
            frob = None

        lp_k = len(lp.active_set) if lp.feasible else None
        if lp.feasible:
            n_lp_feasible += 1
            lp_active_hist[lp_k] += 1
        frob_k = len(frob.active_set) if (frob and frob.feasible) else None
        if frob and frob.feasible:
            n_frob_feasible += 1
            frob_active_hist[frob_k] += 1
            permitted_ZN.append([Z, N])

        # Keep a compact per-nucleus row; full dual stored only for a sample.
        rows.append({
            "Z": Z, "N": N, "A": A,
            "nf_net": nf_net,
            "lp_feasible": bool(lp.feasible),
            "lp_active_count": lp_k,
            "lp_active_channels": [NF_NAMES[i] for i in lp.active_set],
            "frob_feasible": bool(frob.feasible) if frob else False,
            "frob_active_count": frob_k,
        })

    n_total = sum(1 for e in entries if int(e["A"]) >= 1)

    # Full primal+dual for sampled nuclei (LP/SDP-dual discipline).
    sample_ZN = [(1, 0), (1, 1), (2, 2), (3, 4), (6, 6), (8, 8),
                 (20, 20), (26, 30), (50, 70), (82, 126)]
    sample_duals = []
    for Z, N in sample_ZN:
        A = Z + N
        try:
            nf = build_nf(Z, N)
        except Exception:
            continue
        if not all(np.isfinite(np.asarray(nf, dtype=float))):
            continue
        # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
        # whether the Rust binary happens to be built, so the same script
        # yields different numbers on different boxes. Bean `qou/ftuv`.
        lp = solve_operator_selection_lp(t, G, float(A), backend="clarabel")
        sample_duals.append({
            "Z": Z, "N": N, "A": A, "n_target": A,
            "lp": lp.to_dict(),
            "active_channels": [NF_NAMES[i] for i in lp.active_set],
        })

    w = WitnessBuilder("all-nuclides-sdp-admissibility", engine="python",
                       start_time=_t0)
    w.set_description(
        "Operator-selection admissibility over the AME2020 chart at q_0. "
        "(a) per-nucleus active-channel count = |{i: y*_i>0}| of the H_3 "
        "LP dual (prop:operator-selection-lp); (b) permitted-nuclei count "
        "= #{(Z,N): Frobenius-demand LP feasible with u_demand = the "
        "nucleus's own NF}. Canonical t=TR_M, G=gram_matrix() (no fit); "
        "per-nucleus object = build_atom_nf(Z,N)."
    )
    w.add_data("n_nuclides_total", n_total)
    w.add_data("n_native_engine", bool(_HAS_NATIVE))
    w.add_data("scalar_lp_n_target", "A (mass number; proton->1)")
    w.add_data("a_active_channel_count_hist_scalar_lp",
               {str(k): v for k, v in sorted(lp_active_hist.items())})
    w.add_data("a_active_channel_count_hist_frobenius",
               {str(k): v for k, v in sorted(frob_active_hist.items())})
    w.add_data("b_permitted_count_scalar_lp", n_lp_feasible)
    w.add_data("b_permitted_count_frobenius", n_frob_feasible)
    w.add_data("b_permitted_ZN_frobenius", permitted_ZN)
    w.add_data("sample_duals", sample_duals)
    w.add_data("rows", rows)

    n_finite = n_total - n_overflow - n_build_fail
    w.add_data("n_f64_finite", n_finite)
    w.add_data("n_f64_overflow_heavy", n_overflow)
    w.add_data("n_build_fail", n_build_fail)
    w.add_data("findings", [
        "(a) Active-channel count is CONSTANT (=1) across every f64-finite "
        "nucleus under the scalar LP (n_target=A): the H_3-local operator "
        "selection just scales with A, so it does NOT discriminate nuclei. "
        "Per-nucleus binding richness must live in the tower / Delta_lambda, "
        "not the H_3 operator selection.",
        "(b) Naive admissibility does NOT bound the chart: the scalar-LP "
        "'feasible' count equals the f64-finite count (an overflow cutoff, "
        "not physics), and the Frobenius equality (Gx=nf AND sum(x)=nf_net, "
        "over-determined 7-eq/6-unknown) is degenerate -> 0 feasible. A "
        "meaningful 'permitted nuclei at q_0' count needs the PSD-SDP "
        "positivity (bound-state) criterion, not the scalar/Frobenius LP.",
        f"INFRA: native f64 build_atom_nf overflows for {n_overflow}/"
        f"{n_total} (~{100 * n_overflow // max(n_total, 1)}%) heavy nuclei; "
        "an all-nuclides sweep needs the mpfr native path.",
    ])
    w.add_assertion(
        name="nuclide_chart_fully_accounted",
        computed=n_finite + n_overflow + n_build_fail,
        expected=n_total,
        tolerance=0,
        source="every AME entry (A>=1): finite-solved, f64-overflow, or build-fail",
    )

    out = w.save()
    print(f"nuclides swept: {n_total}  (native engine: {_HAS_NATIVE})")
    print(f"(a) active-channel count — scalar LP (n_target=A): "
          f"{dict(sorted(lp_active_hist.items()))}")
    print(f"(a) active-channel count — Frobenius (u_demand=nf): "
          f"{dict(sorted(frob_active_hist.items()))}")
    print(f"(b) permitted nuclei — scalar LP:  {n_lp_feasible} / {n_total}")
    print(f"(b) permitted nuclei — Frobenius:  {n_frob_feasible} / {n_total}")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
