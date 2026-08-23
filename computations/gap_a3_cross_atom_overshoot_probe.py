#!/usr/bin/env python3
"""
Cross-atom extension of the binding flat-baseline / overshoot analysis.

#2626 (deuteron): flat trace bar-mixed; #2631: flat baseline A(D)·tr_M overshoots
−B(D)/m_e by ~2.05×. The genuinely-informative non-fit next step (NOT a 7th
ansatz): does the SAME pattern (bar-mixed flat trace + ~2× overshoot) hold across
atoms? Atom-independence of the overshoot would be a real structural clue about
P_λ; variation constrains its atom-dependence.

For each atom K=(Z,N), n=3A:
  A(K)      = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}   (Phase-4 derived)
  tr_M(β_K) = Σ_λ y_λ(q₀) χ^λ(β_K)   (canonical: y_lambda_at q₀ hot path + chi_all_lambda)
  overshoot = A(K)·tr_M(β_K) / (−B(K)/m_e)
  bar-mix   = max_λ |w_λ − w_λᵀ| (w_λ = y_λ χ^λ)

Vol_hyp: D=12.776 (Z=1), ³He=⁴He=12.554 (Z=2)  [PR #787 Phase-3 clusters].
−B/m_e (AME / m_e=0.51099895 MeV): D=4.353, ³He=15.10, ⁴He=55.37.  # noqa: P31 — docstring; m_e in -B/m_e note

DISCIPLINE: characterises the overshoot/bar-mix ACROSS atoms; proposes NO P_λ and
fits nothing. ⁴He (H₁₂) χ may be infeasible in-session (Hoefsmit-gated) — handled
gracefully.
"""
import sys, time
sys.path.insert(0, "computations")
import mpmath as mp
from wedderburn_jones_markov import y_lambda_at
from chi_monotone_transfer import chi_all_lambda
from mass_at_3A_proper import atom_braid_word_3A
from lr_coefficients import partitions_of

# --- muon anchor: READ, never retyped ---------------------------------------
# This file used to carry the muon q0 as a string literal. A transcribed pin
# cannot be re-pinned, cannot be flipped by QOU_Q0_ANCHOR, and reports a
# q0Anchor describing its label rather than its computation. The literal here
# was B = Vol(4_1)/206.7682830, the CODATA-2018 derivation -- superseded by the
# owner ruling of 2026-08-22 (A -> CODATA 2022, PR #5500). Reading the anchor
# is correct before and after that ruling; retyping either value is not.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[1]
                        / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor as _q0_for  # noqa: E402

mp.mp.dps = 18
Q0 = mp.mpf(_q0_for("muon"))
VOL = {"D": mp.mpf("12.776"), "3He": mp.mpf("12.554"), "4He": mp.mpf("12.554")}
B_OVER_ME = {"D": mp.mpf("4.353"), "3He": mp.mpf("15.10"), "4He": mp.mpf("55.37")}
ATOMS = [("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2)]


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def A_of(Z, N, lbl):
    spin = (Q0 ** mp.mpf("0.5") + Q0 ** mp.mpf("-0.5")) ** (4 * N)
    return VOL[lbl] / qint(8) * qint(3) ** (2 * (Z - 1)) * spin


def transpose(lam):
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def main():
    print(f"q_0={Q0} dps={mp.mp.dps}\n")
    print(f"{'atom':<5}{'n':>3}{'A(K)':>12}{'tr_M':>12}{'A·tr_M':>12}"
          f"{'−B/m_e':>10}{'overshoot':>11}{'bar-mix':>10}")
    for lbl, Z, N in ATOMS:
        n = 3 * (Z + N)
        t0 = time.time()
        print(f"  [{lbl}] n={n}: computing y_λ + χ^λ ...", flush=True)
        try:
            yraw = y_lambda_at(n, Q0)
            if isinstance(yraw, dict):
                yitems = yraw.items()
            else:
                parts_n = [tuple(p) for p in partitions_of(n)]
                if len(parts_n) != len(yraw):
                    raise ValueError(
                        f"y_lambda_at returned {len(yraw)} weights but p({n})="
                        f"{len(parts_n)} partitions — mismatch (would zip-truncate).")
                yitems = zip(parts_n, yraw)
            y = {tuple(k): (v if isinstance(v, mp.mpf) else mp.mpf(str(v)))
                 for k, v in yitems}
            chi = {tuple(k): v for k, v in
                   chi_all_lambda(atom_braid_word_3A(Z, N), n, dps=mp.mp.dps).items()}
        except Exception as e:
            print(f"     [{lbl}] FAILED/INFEASIBLE: {type(e).__name__}: {e}", flush=True)
            continue
        w = {lam: y.get(lam, mp.mpf(0)) * chi.get(lam, mp.mpf(0))
             for lam in set(y) | set(chi)}
        trM = mp.fsum(w.values())
        A = A_of(Z, N, lbl)
        flat = A * trM
        over = flat / B_OVER_ME[lbl]
        barmix = mp.mpf(0)
        for lam in w:
            lt = transpose(lam)
            if lt in w and lt != lam:
                barmix = max(barmix, abs(w[lam] - w[lt]))
        dt = round(time.time() - t0, 1)
        print(f"  [{lbl}] done ({dt}s)", flush=True)
        print(f"{lbl:<5}{n:>3}{mp.nstr(A,7):>12}{mp.nstr(trM,7):>12}{mp.nstr(flat,7):>12}"
              f"{mp.nstr(B_OVER_ME[lbl],5):>10}{mp.nstr(over,6):>11}{mp.nstr(barmix,5):>10}", flush=True)
    print("\nReading: if 'overshoot' is ~constant across atoms ⇒ atom-independent")
    print("redistribution scale (structural clue); if it varies ⇒ P_λ is atom-dependent.")
    print("'bar-mix' > 0 everywhere ⇒ the bar-even-P_λ symmetrisation requirement is general.")
    print("NO P_λ proposed; nothing fitted.")
    print("\nCROSS-ATOM PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
