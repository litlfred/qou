#!/usr/bin/env python3
"""qbeta_lepton_strand_probe — the electron Δ = σ₀σ₁σ₀ next to the γγ base (issue #8833).

Closed family and reporting rules: PREREGISTRATION.md in this directory, committed before
this file. Lean first: QOU/QBeta/ElectronHalfTwistBlock.lean (on V_(2,1) Δ² = 1; on V_(3)
Δ = q³; Markov value z(hz+1)).

Six strands, Jimbo R-matrix (eigenvalues q, −1/q) on (C²)^{⊗6}, numeric at the proton q₀,
50 dps. W = X · β_Bor · Δ with β_Bor = (σ₀σ₁⁻¹)³ on strands 0–2, Δ = σ₃σ₄σ₃ on strands 3–5,
X every product of 0..3 letters V_i = σ_iσ_{i+1}⁻¹, i = 0..4. Spectrum on the weight space
#d = 3 (dim 20), which carries every two-row H₆ block (all that convention D keeps).

Checks
  L1  the rep satisfies the Hecke and braid relations on #d = 3.
  L2  the electron alone (Lean values): on #d=3 of three strands... reported via the disjoint
      word X = 1: its largest imaginary phase is exactly 3 ln q₀ (from Δ = q³ on V_(3)).
  L3  every word in the family stays below the needed phase a = arccosh F (from the
      four-strand witness). Scope (a): length <= 3.
Nothing is selected, scored or wired.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 50
mp.mp.dps = DPS
N = 6
Q = mp.mpf(Q_50_DIGIT_STR)
H = Q - 1 / Q
TOL = mp.mpf(10) ** -35

RESULTS: list[tuple[str, bool, str]] = []
FALLBACK: list[int] = []


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


BASIS = [b for b in range(2 ** N) if bin(b).count("1") == 3]
POS = {b: k for k, b in enumerate(BASIS)}


def bit(b: int, strand: int) -> int:
    return (b >> (N - 1 - strand)) & 1


def setbits(b: int, strand: int, x: int, y: int) -> int:
    for s, v in ((strand, x), (strand + 1, y)):
        m = 1 << (N - 1 - s)
        b = (b | m) if v else (b & ~m)
    return b


# R2 columns: e00 -> q e00; e01 -> e10; e10 -> e01 + h e10; e11 -> q e11
def sigma(i: int, inv: bool = False) -> mp.matrix:
    M = mp.matrix(len(BASIS), len(BASIS))
    for b in BASIS:
        x, y = bit(b, i), bit(b, i + 1)
        c = POS[b]
        if x == y:
            M[c, c] = (1 / Q) if inv else Q
        elif (x, y) == (0, 1):
            if inv:  # sigma^-1 = sigma - h
                M[POS[setbits(b, i, 1, 0)], c] = 1
                M[c, c] = -H
            else:
                M[POS[setbits(b, i, 1, 0)], c] = 1
        else:  # (1, 0)
            M[POS[setbits(b, i, 0, 1)], c] = 1
            M[c, c] = 0 if inv else H
    return M


def maxdiff(A, B) -> mp.mpf:
    return max(abs(A[i, j] - B[i, j]) for i in range(A.rows) for j in range(A.cols))


def phase_stats(W):
    try:
        ev = mp.eig(W, left=False, right=False)
    except RuntimeError:
        # QR did not converge (repeated eigenvalues). Fall back to the characteristic
        # polynomial (Faddeev-LeVerrier at +60 digits) and its roots.
        with mp.extradps(60):
            n = W.rows
            Mk, coeffs = mp.matrix(n, n), [mp.mpf(1)]
            for k in range(1, n + 1):
                Mk = W * Mk + coeffs[-1] * mp.eye(n)
                coeffs.append(-sum((W * Mk)[i, i] for i in range(n)) / k)
            ev = mp.polyroots(coeffs, maxsteps=500, extraprec=400)
        FALLBACK.append(1)
    real_pos = [mp.re(e) for e in ev if abs(mp.im(e)) < TOL and mp.re(e) > 0
                and abs(mp.re(e) - 1) > TOL]
    return max((abs(mp.log(r)) for r in real_pos), default=mp.mpf(0)), len(real_pos)


def main() -> int:
    S = [sigma(i) for i in range(N - 1)]
    Si = [sigma(i, inv=True) for i in range(N - 1)]
    I = mp.eye(len(BASIS))
    ok_rel = all(maxdiff(S[i] * S[i], H * S[i] + I) < TOL for i in range(N - 1)) and \
        all(maxdiff(S[i] * Si[i], I) < TOL for i in range(N - 1)) and \
        all(maxdiff(S[i] * S[i + 1] * S[i], S[i + 1] * S[i] * S[i + 1]) < TOL
            for i in range(N - 2)) and \
        all(maxdiff(S[i] * S[j], S[j] * S[i]) < TOL
            for i in range(N - 1) for j in range(i + 2, N - 1))
    check("L1_jimbo_rep_is_H6_on_d3", ok_rel,
          "sigma^2 = h sigma + 1, sigma sigma^-1 = 1, both braid relation types hold on the "
          "20-dim weight space #d = 3 (tolerance 1e-35 at 50 dps).")

    # V_i = s_i s_{i+1}^-1 is defined for i = 0..3 on six strands (V4 would need s5).
    V = [S[i] * Si[i + 1] for i in range(N - 2)]
    beta = (V[0] ** 3)
    delta = S[3] * S[4] * S[3]
    base = beta * delta

    a_e, n_e = phase_stats(base)
    a3 = 3 * mp.log(Q)
    check("L2_electron_alone_gives_exactly_3lnq", abs(a_e - a3) < TOL,
          f"beta_Bor (x) Delta, no linking letter: largest imaginary phase "
          f"{mp.nstr(a_e, 20)} = 3 ln q0 = {mp.nstr(a3, 20)} (cosh = "
          f"{mp.nstr(mp.cosh(a3), 15)}), matching the Lean value Delta = q^3 on V_(3); "
          "V_(2,1) contributes +-1 (Lean halfTwist_sq).")

    fs = json.loads((_ROOT / "computations/qbeta/qbeta-d-eigenphase-four-strand.witness.json")
                    .read_text())
    a_need = mp.mpf(fs["a_needed"])
    names = [f"V{i}" for i in range(4)]
    scan, amax, arg = [], mp.mpf(0), "1"
    for k in range(0, 4):
        for combo in itertools.product(range(4), repeat=k):
            X = I
            for c in combo:
                X = X * V[c]
            a, n = phase_stats(X * base)
            nm = "".join(names[c] for c in combo) or "1"
            junction = any(c in (1, 2) for c in combo)  # V1 = s1 s2^-1, V2 = s2 s3^-1 use s2
            scan.append({"X": nm, "touches_junction": junction, "n_real_pos": n,
                         "a_max": mp.nstr(a, 20)})
            if a > amax:
                amax, arg = a, nm
    n_imag = sum(1 for r in scan if r["n_real_pos"] > 0)
    print(f"  charpoly fallback used for {len(FALLBACK)} words")
    print(f"  scan: {len(scan)} words, {n_imag} with an imaginary phase; max a = "
          f"{mp.nstr(amax, 15)} at {arg}\n")
    check("L3_family_stays_below_needed_phase", amax < a_need,
          f"{n_imag} of {len(scan)} words have an imaginary phase; the largest is a = "
          f"{mp.nstr(amax, 15)} (cosh {mp.nstr(mp.cosh(amax), 12)}) at X = {arg}, against "
          f"the needed {mp.nstr(a_need, 12)}: {mp.nstr(a_need / amax, 5)}x short. Scope "
          "(a): length <= 3.")

    zD = Q ** 3 / (Q ** 2 + 1)
    markov = zD * (H * zD + 1)
    allp = all(ok for _, ok, _ in RESULTS)
    print(f"  Markov value of Delta at z_D: {mp.nstr(markov, 20)}")
    print(f"  {sum(ok for _, ok, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-lepton-strand", engine="mpmath")
    for nm, ok, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if ok else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "description": ("Electron Delta = s0 s1 s0 placed next to the gamma-gamma base on six "
                        "strands; imaginary-phase scan over X in V0..V3 words of length <= 3. "
                        "Diagnostic; nothing selected or scored."),
        "beans": ["qou-cds1", "qou-pdix", "qou-99qc"],
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "lean": "QOU/QBeta/ElectronHalfTwistBlock.lean",
        "candidates_not_selected": {
            "cosh_3lnq": mp.nstr(mp.cosh(a3), 30),
            "markov_value_Delta_zD": mp.nstr(markov, 30),
        },
        "scan": scan,
        "scan_a_max": mp.nstr(amax, 30),
        "scan_a_max_word": arg,
        "a_needed": mp.nstr(a_need, 30),
        "family_note": ("V_i = s_i s_{i+1}^-1 exists for i = 0..3 on six strands (V4 would "
                        "need s5), so the family is V0..V3, 85 words; PREREGISTRATION.md "
                        "said V0..V4 / 156, which is not definable. Corrected here, no other "
                        "change."),
        "scope": "(a): words of length <= 3 only; longer braids are unbounded.",
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
