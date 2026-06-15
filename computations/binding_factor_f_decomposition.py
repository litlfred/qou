#!/usr/bin/env python3
"""Barrier-1 attack: the binding link is B₃ (8G) scaled by a factor f(Z,N).

The deuteron binding is B(D) = m_e · Vol(B₃) · Δtr with Vol(B₃)=8G
(Borromean, +0.19%). Testing whether the SAME 8G volume works for T/³He
shows it does NOT (−64%, −59%): each nuclide needs its own Vol(K_bind).

But the required volumes are NOT exotic per-atom census knots — they
factor as Vol(K_bind) = 8G · f(Z,N):

    f(Z,N) = B_AME / (m_e · 8G · Δtr)        [extracted from AME]

This script computes f for D/T/³He from the canonical Δtr (binding-
canonical, H_{3A} Wedderburn sum). The result f = {D:1.00, T:2.82,
³He:2.45} matches the per-magic-closure factors found independently in
#1417, and the T↔³He difference is the Coulomb energy of ³He's two
protons (mirror-nucleus split) — i.e. the #1417 sinh(ln q) ≈ α_EM
channel.

A consistent 4th point (⁴He, Z=2 N=2, same binding-canonical producer)
then tests the pairwise-bond hypothesis f = A(A−1)/2 − κ·Z(Z−1)/2 with
κ fixed from the A=3 mirror. ⁴He is OUT-OF-SAMPLE and FALSIFIES it:
f(⁴He)=8.29 vs predicted 5.63 (+47%). Doubly-magic ⁴He binds
collectively, not pairwise — so f is a magic-SHELL-closure quantity
(exactly #1417's "per-magic-closure f"), to be derived from the
Demazure crystal closure level (CLAUDE.md §7b), NOT inter-nucleon bonds.

STATUS: f is EXTRACTED from AME (not derived). The findings here are
(i) the *factorisation* Vol(K_bind)=8G·f·Δtr — the census-free derived
part is 8G·Δtr; (ii) the Coulomb structure of f (A=3 mirror split); and
(iii) the *falsification* of the pairwise-bond model. f is NOT fittable
from 4 points (forbidden ansatz); deriving it from crystal-closure is
the open Barrier-1 research. Discipline: structural probe, f labelled
AME-extracted; no fitted coefficient is wired to production.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, catalan

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

# canonical tr_M (free constituents, bound atom) from binding-canonical
# (H_{3A} Wedderburn sum); AME binding energies.
ATOMS = {
    # name: (Z, N, tr_M_free, tr_M_atom, B_AME_MeV) — all from binding-canonical
    "D":   (1, 1, "0.9835261819186453", "0.38828647154771295", "2.224566"),
    "T":   (1, 2, "0.9080241197853626", "0.10405211867552604", "8.481798"),
    "3He": (2, 1, "1.0477565675816238", "0.20654085856226245", "7.718043"),
    "4He": (2, 2, "0.9673237505194684", "0.05534834587669799", "28.295673"),
}


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("binding-factor-f-decomposition", engine="mpmath")
    me = mpf(str(M_E_MEV))
    vol_b3 = 8 * catalan
    scale = me * vol_b3

    print("=" * 72)
    print("Binding factor f(Z,N): Vol(K_bind) = 8G · f  (Barrier-1 reframe)")
    print("=" * 72)
    print(f"  m_e·8G = {mp.nstr(scale, 8)} MeV   (8G = Vol(Borromean) = {mp.nstr(vol_b3, 8)})")
    print(f"  {'atom':5}{'Z,N':>6}{'Δtr':>10}{'B_AME':>9}{'f=B/(m_e·8G·Δtr)':>20}")
    rows = []
    fvals = {}
    for name, (Z, N, free, atomtr, bame) in ATOMS.items():
        dtr = mpf(free) - mpf(atomtr)
        B = mpf(bame)
        f = B / (scale * dtr)
        print(f"  {name:5}{f'{Z},{N}':>6}{mp.nstr(dtr, 6):>10}{mp.nstr(B, 6):>9}{mp.nstr(f, 8):>20}")
        fvals[name] = f
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "delta_tr": mp.nstr(dtr, 30),
            "B_AME_MeV": str(bame),
            "f_AME_extracted": mp.nstr(f, 30),
        })
    # Coulomb structure: T and ³He are A=3 mirror nuclei; f(T) > f(³He)
    df = fvals["T"] - fvals["3He"]  # κ: Coulomb per proton-pair, from A=3 mirror
    print()
    print(f"  f(T) − f(³He) = {mp.nstr(df, 6)}  (mirror split; ³He's 2 protons → Coulomb, #1417)")

    # ── Pairwise-bond hypothesis test: f = pairs(A) − κ·proton-pairs(Z) ──
    # κ fixed from the A=3 mirror; deuteron fixes the bond unit. ⁴He (Z=2,N=2)
    # is then a TRUE out-of-sample test of the pairwise-bond model.
    print()
    print("  Pairwise-bond test  f_pred = A(A−1)/2 − κ·Z(Z−1)/2 :")
    print(f"  {'atom':5}{'A':>3}{'Z':>3}{'pairs':>6}{'f_pred':>9}{'f_ext':>9}{'err%':>9}")
    bond_rows = []
    for name, (Z, N, free, atomtr, bame) in ATOMS.items():
        A = Z + N
        pairs = A * (A - 1) // 2
        ppair = Z * (Z - 1) // 2
        f_pred = pairs - df * ppair
        f_ext = fvals[name]
        err = (f_ext / f_pred - 1) * 100
        print(f"  {name:5}{A:>3}{Z:>3}{pairs:>6}{mp.nstr(f_pred, 5):>9}"
              f"{mp.nstr(f_ext, 5):>9}{mp.nstr(err, 4):>9}")
        bond_rows.append({"atom": name, "A": A, "pairs": pairs,
                          "f_pred_bondcount": mp.nstr(f_pred, 20),
                          "f_extracted": mp.nstr(f_ext, 20),
                          "err_pct": float(err)})
    he4_err = bond_rows[-1]["err_pct"]
    print()
    print(f"  D fits a single bond (−0.19%); ⁴He misses by {mp.nstr(mpf(he4_err), 4)}% "
          f"(f(⁴He)≫pairs).")
    print("  ⇒ pairwise-bond model FALSIFIED; f is a magic-shell-closure quantity")
    print("    (#1417 per-magic-closure), to derive from Demazure crystal closure,")
    print("    NOT pairwise bonds. f NOT fittable from 4 points (forbidden ansatz).")

    wb.add_data("scale_m_e_8G_MeV", mp.nstr(scale, 30))
    wb.add_data("rows", rows)
    wb.add_data("mirror_split_T_minus_He3", mp.nstr(df, 30))
    wb.add_data("bondcount_test", {
        "model": "f = A(A-1)/2 - kappa*Z(Z-1)/2, kappa from A=3 mirror",
        "rows": bond_rows,
        "verdict": "FALSIFIED at 4He (+47%); f tracks magic-shell closure, "
                   "not pairwise bonds",
    })
    wb.add_data("finding", (
        "Vol(K_bind) = 8G·f(Z,N); f={D:1.00,T:2.82,3He:2.45,4He:8.29} "
        "(AME-extracted). Pairwise-bond model f=pairs−κ·pp fits D (−0.19%) "
        "but FAILS 4He (+47%): doubly-magic 4He binds collectively. f is a "
        "magic-shell-closure quantity (#1417 per-magic-closure), to derive "
        "from Demazure crystal closure — NOT pairwise bonds. f NOT yet "
        "derived; not fittable from 4 points — open Barrier-1."))
    wb.add_assertion(
        "deuteron_f_is_unity",
        computed=float(rows[0]["f_AME_extracted"]), expected=1.0,
        tolerance=0.01,
        source="B(D) = m_e·8G·Δtr → f(D)=1 (Borromean volume, +0.19%)")
    wb.save()
    print("\n  Witness: binding-factor-f-decomposition.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
