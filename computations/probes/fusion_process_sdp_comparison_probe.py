#!/usr/bin/env python3
"""
Fusion-process SDP comparison probe — D + T vs 4He + n (bean qou-dpy1).

Reads the four committed per-isotope real-SDP witnesses
(nucleus-real-sdp-{deuteron,tritium,he4,neutron}.witness.json) and compares
the two SIDES of the D + T -> 4He + n fusion process at the level the SDP
actually prices: dual variables (y0_star), active Wedderburn channels, and
bar-fold structure. No new SDP is solved; this is a cross-witness read.

Scope discipline
----------------
- The four solves live in DIFFERENT algebras (H_6, H_9, H_12, H_3), so
  active-block sets are compared as bar-fold summary statistics (counts,
  fractions, self-conjugate activity, y0_star signs), never partition-by-
  partition across levels.
- Witness numerics are float64 BY CONSTRUCTION (bean qou-ftuv: LP-dual
  witnesses carry raw float64). All arithmetic here is mpmath over
  mpf(str(.)) of those values, but conclusions are stated at float64
  resolution — nothing here is "exact".
- This probe emits no witness and wires nothing to production; its
  conclusions live in docs/audits/2026-08-29-mass-provenance-breakdown-
  and-gap-map.md §4 and bean qou-dpy1.
- ADJUDICATED (2026-08-30, beans qou-nnu3 + qou-lzgv, two rounds): the
  deuteron n_target != tr_M gap was first explained as the positive-norm
  restriction over 3 negative-norm blocks — but those blocks were an
  artifact of the STALE deuteron solve (tr_M 0.38836, pre-import-cone
  drift). The witness was regenerated from the live trace (tr_M 0.57517):
  the live deuteron has ZERO negative-norm blocks and n_target = tr_M
  bit-identical, like the other three subjects. Both sides of the process
  are split-multiplicative.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from mpmath import mp, mpf  # noqa: E402

mp.dps = 30  # inputs are f64-resolution; mp only to avoid f64 arithmetic

SIDES = {
    "initial": ["deuteron", "tritium"],
    "final": ["he4", "neutron"],
}


def load(atom):
    p = os.path.join(ROOT, f"nucleus-real-sdp-{atom}.witness.json")
    w = json.load(open(p))
    d = w.get("data", w)
    s = d.get("positive_norm_subspace_solve", {})
    return {
        "atom": atom,
        "n_strands": d["n_strands"],
        "n_blocks": d["n_blocks"],
        "tr_M": mpf(str(d["tr_M"])),
        "self_conj": d.get("self_conjugate_blocks", []),
        "reps": d.get("barfold_representatives", []),
        "n_target": mpf(str(s["n_target"])) if "n_target" in s else None,
        "y0_star": mpf(str(s["y0_star"])) if "y0_star" in s else None,
        "active": s.get("active_blocks", []),
        "y_star": [mpf(str(y)) for y in s.get("y_star", [])],
        "gap": mpf(str(s["duality_gap"])) if "duality_gap" in s else None,
        "strong": s.get("strong_duality_holds"),
        "bounded": s.get("bounded"),
    }


def main() -> int:
    subjects = {a: load(a) for side in SIDES.values() for a in side}
    ok = True

    print("FUSION-PROCESS SDP COMPARISON — D + T -> 4He + n  (cross-witness read)")
    print("| subject | H_n | blocks | tr_M | n_target | y0* | active/reps | self-conj active? | gap |")
    print("|---|--:|--:|--:|--:|--:|:--|:--|--:|")
    for a, s in subjects.items():
        sc_active = [b for b in s["self_conj"] if b in s["active"]]
        print(f"| {a} | H_{s['n_strands']} | {s['n_blocks']} | {mp.nstr(s['tr_M'], 10)} | "
              f"{mp.nstr(s['n_target'], 10) if s['n_target'] is not None else '—'} | "
              f"{mp.nstr(s['y0_star'], 6) if s['y0_star'] is not None else '—'} | "
              f"{len(s['active'])}/{len(s['reps'])} | "
              f"{sc_active if sc_active else 'NO'} | "
              f"{mp.nstr(s['gap'], 3) if s['gap'] is not None else '—'} |")

    # 1. Strand conservation across the channel
    n_init = sum(subjects[a]["n_strands"] for a in SIDES["initial"])
    n_fin = sum(subjects[a]["n_strands"] for a in SIDES["final"])
    print(f"\nstrand bookkeeping: initial {n_init} (6+9) vs final {n_fin} (12+3)"
          f" -> {'CONSERVED' if n_init == n_fin else 'MISMATCH'}")
    ok &= (n_init == n_fin)

    # 2. Certificates present on all four
    for a, s in subjects.items():
        good = bool(s["bounded"]) and bool(s["strong"]) and s["gap"] is not None and s["gap"] < mpf("1e-30")
        print(f"certificate[{a}]: bounded={s['bounded']} strong_duality={s['strong']} "
              f"gap<1e-30={'True' if good else 'FALSE'}")
        ok &= good

    # 3. Dual price (y0_star) across the channel — the SDP's own "price" of the
    #    net constraint per subject. Signs and channel sums are descriptive.
    y_init = sum(subjects[a]["y0_star"] for a in SIDES["initial"])
    y_fin = sum(subjects[a]["y0_star"] for a in SIDES["final"])
    print(f"\ny0* sums: initial {mp.nstr(y_init, 8)}  final {mp.nstr(y_fin, 8)}  "
          f"delta(final-initial) {mp.nstr(y_fin - y_init, 8)}")

    # 4. tr_M bookkeeping (descriptive; traces are per-word, not additive
    #    across a channel — recorded to show the magnitude landscape only)
    t = {a: subjects[a]["tr_M"] for a in subjects}
    print(f"tr_M: 2H {mp.nstr(t['deuteron'], 10)} 3H {mp.nstr(t['tritium'], 10)} "
          f"4He {mp.nstr(t['he4'], 10)} n {mp.nstr(t['neutron'], 10)}")
    print(f"  products: initial {mp.nstr(t['deuteron']*t['tritium'], 10)} "
          f"final {mp.nstr(t['he4']*t['neutron'], 10)}")

    print(f"\nRESULT: {'PASS' if ok else 'FAIL'} (structural checks; conclusions at f64 resolution)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
