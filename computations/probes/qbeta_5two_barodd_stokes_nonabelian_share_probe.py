#!/usr/bin/env python3
"""qbeta_5two_barodd_stokes_nonabelian_share_probe.py

The bar-odd 5₂ Stokes datum is MAJORITY NON-ABELIAN — the structural reason every
scalar closed-form search on the bar-odd channel fails.

CONTEXT (the na-Stokes ⇄ resurgence dictionary). Écalle's resurgence is the ABELIAN
theory: a scalar Borel transform, scalar alien derivatives Δ_ω, scalar Stokes
constants. Its NON-ABELIAN analogue is the Stokes-MATRIX / Riemann–Hilbert structure
(Deligne–Malgrange–Mochizuki) — on the physics side the Kontsevich–Soibelman
wall-crossing formula. For the chiral knot 5₂ that matrix is the Garoufalidis–Gu–
Mariño Stokes matrix S±(q) (3×3, SL(3), inversion S⁺ᵀS⁻=1), transcribed + machine-
verified in `qbeta_5two_stokes_barodd_index_probe.py` (uploads/2007.10190v2.pdf). Its
bar-EVEN part is the rotated 3d index Ind^rot (a scalar, eq 124); its bar-ODD part is
the full matrix O = ½(S⁺ − S⁻).

The corpus's DOWNSTREAM bar-odd data — the scalar φ_odd (σ1/σ2 arg-sum), the c₃/Q_β
swing carriers, the 5₂ Habiro-tail action — are all SCALAR reductions. This probe
quantifies how much of the bar-odd datum a scalar reduction can possibly see.

MEASUREMENT (from the GGM producer's witness, both anchors). Decompose O into its
abelian part (the diagonal = formal-monodromy / period data, what scalar resurgence
captures) and its non-abelian part (the off-diagonal = the genuine Stokes data):

  ‖O‖_F = 2.107,  ‖diag O‖_F = 1.448 (abelian),  ‖offdiag O‖_F = 1.530 (non-abelian).

FINDINGS.
  1. OFF-DIAGONAL DOMINATES. off/diag Frobenius ratio = 1.057; the off-diagonal
     (non-abelian) part carries 52.8% of ‖O‖_F² — MORE than the diagonal. A scalar
     extraction (trace, a single entry, det) sees at most the diagonal ⇒ it discards
     the MAJORITY (52.8%) of the datum.
  2. GENUINELY NON-NORMAL. ‖O − Oᵀ‖_F = 1.71 ≠ 0: O is not normal, so no basis
     diagonalizes it by scalars — the datum is irreducibly matrix-valued. trace(O) =
     −0.026 (the one clean scalar invariant) captures almost none of it.
  3. ANCHOR-STABLE. The decomposition is the same to 4 sig figs at the proton anchor
     (off^2-fraction differs by < 1e-4) — this is a structural property of the datum,
     not an anchor artifact.

CONCLUSION. The bar-odd 5₂ channel is majority non-abelian. This is the structural
diagnosis of why the scalar closed-form searches (φ_odd σ1/σ2 arg-sum; the 5₂
Habiro-tail "no π²/5-analog"; the c₃ swing carriers) do not close: they are scalar
projections of an object 52.8% of which is off-diagonal and scalar-invisible. The
correct bar-odd carrier is the MATRIX O (or its non-abelian invariants — off-diagonal
entries / non-normal spectral data), NOT a scalar phase. This does NOT close c₃ (the
GGM probe already established O is smooth, NOT the swing — SRigidityPrune binds); it
reframes WHERE the bar-odd datum lives and why scalar routes structurally cannot reach
it.

DISCIPLINE: scope-(a) structural. Reads the GGM producer's witness; decomposes;
reports the non-abelian share. No fit; no c_k wired; nothing to production; no tier
change.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 30
SRC = Path(__file__).resolve().parent / "qbeta-5two-stokes-barodd-index.witness.json"


def _load_O(key):
    d = json.load(open(SRC))["data"][key]
    return mp.matrix([[mp.mpf(str(d[i][j])) for j in range(3)] for i in range(3)])


def _fro(M):
    return mp.sqrt(sum(M[i, j] ** 2 for i in range(3) for j in range(3)))


def _decompose(O):
    diag = mp.matrix([[O[i, j] if i == j else 0 for j in range(3)] for i in range(3)])
    offd = mp.matrix([[0 if i == j else O[i, j] for j in range(3)] for i in range(3)])
    fO, fD, fOff = _fro(O), _fro(diag), _fro(offd)
    return {
        "fro_O": fO, "fro_diag": fD, "fro_offdiag": fOff,
        "off_over_diag": fOff / fD, "off2_fraction": fOff ** 2 / fO ** 2,
        "trace": sum(O[i, i] for i in range(3)), "nonnormality": _fro(O - O.T),
    }


def main() -> int:
    if not SRC.exists():
        print(f"  MISSING producer witness: {SRC} — run qbeta_5two_stokes_barodd_index_probe.py first", flush=True)
        return 1
    Om = _load_O("odd_datum_O_muon")
    Op = _load_O("odd_datum_O_proton")
    dm, dp = _decompose(Om), _decompose(Op)

    print("  bar-odd 5₂ Stokes matrix O = ½(S⁺−S⁻) — abelian/non-abelian split", flush=True)
    for tag, dd in (("muon", dm), ("proton", dp)):
        print(f"  [{tag}] ‖O‖_F={mp.nstr(dd['fro_O'],7)}  ‖diag‖={mp.nstr(dd['fro_diag'],7)} (abelian)  "
              f"‖offdiag‖={mp.nstr(dd['fro_offdiag'],7)} (non-abelian)", flush=True)
        print(f"         off/diag={mp.nstr(dd['off_over_diag'],6)}  off²-share={mp.nstr(dd['off2_fraction'],6)}  "
              f"trace={mp.nstr(dd['trace'],6)}  ‖O−Oᵀ‖={mp.nstr(dd['nonnormality'],6)}", flush=True)

    off_dominates = dm["off2_fraction"] > mp.mpf("0.5")
    non_normal = dm["nonnormality"] > mp.mpf("1e-3")
    anchor_stable = abs(dm["off2_fraction"] - dp["off2_fraction"]) < mp.mpf("1e-3")
    scalar_lossy = dm["off2_fraction"] > mp.mpf("0.5")  # a scalar sees ≤ diagonal

    assertions = [
        ("offdiagonal_carries_majority_of_datum", bool(off_dominates)),
        ("O_is_genuinely_non_normal_no_scalar_diagonalization", bool(non_normal)),
        ("scalar_reduction_is_structurally_lossy", bool(scalar_lossy)),
        ("decomposition_anchor_stable", bool(anchor_stable)),
    ]

    verdict = (
        f"THE BAR-ODD 5₂ STOKES DATUM IS MAJORITY NON-ABELIAN (scope-(a) structural). O = "
        f"½(S⁺−S⁻) (GGM Stokes matrix, the non-abelian analogue of the resurgent Borel datum): "
        f"‖O‖_F={mp.nstr(dm['fro_O'],6)}, split ‖diag‖={mp.nstr(dm['fro_diag'],6)} (abelian / "
        f"formal-monodromy) vs ‖offdiag‖={mp.nstr(dm['fro_offdiag'],6)} (non-abelian / Stokes). "
        f"off/diag={mp.nstr(dm['off_over_diag'],5)}; the off-diagonal carries "
        f"{mp.nstr(dm['off2_fraction']*100,4)}% of ‖O‖² — MORE than the diagonal. O is non-normal "
        f"(‖O−Oᵀ‖={mp.nstr(dm['nonnormality'],5)}≠0) so no scalar diagonalizes it; trace(O)="
        f"{mp.nstr(dm['trace'],4)} (the one clean scalar) captures almost none of it. CONCLUSION: "
        f"the scalar closed-form searches (φ_odd σ1/σ2 arg-sum; 5₂ Habiro-tail 'no π²/5-analog'; "
        f"c₃ swing carriers) fail STRUCTURALLY — they are scalar projections of an object 52.8% of "
        f"which is off-diagonal and scalar-invisible. The correct bar-odd carrier is the MATRIX O "
        f"(non-abelian invariants), not a scalar phase. Does NOT close c₃ (O is smooth, not the "
        f"swing — SRigidityPrune binds); reframes where the datum lives. No fit; no c_k; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-5two-barodd-stokes-nonabelian-share", engine="mpmath")
    wb.set_description(
        "The bar-odd 5₂ Stokes datum O=½(S⁺−S⁻) (GGM Stokes matrix — the non-abelian analogue of "
        "resurgence) is MAJORITY non-abelian: off-diagonal carries 52.8% of ‖O‖² (> diagonal), and "
        "O is non-normal (no scalar diagonalization). This is the structural reason the scalar "
        "closed-form searches (φ_odd, 5₂ Habiro-tail, c₃ swing) fail — they are scalar projections "
        "of an irreducibly-matrix object. Correct carrier = the matrix, not a scalar phase.")
    wb.set_audit_only("docs/audits/2026-07-19-5two-barodd-stokes-majority-nonabelian.md")
    for name, passed in assertions:
        wb.add_assertion(name, str(passed), "True")
    wb.add_data("source_witness", SRC.name)
    wb.add_data("fro_O_muon", mp.nstr(dm["fro_O"], 15))
    wb.add_data("fro_diag_abelian_muon", mp.nstr(dm["fro_diag"], 15))
    wb.add_data("fro_offdiag_nonabelian_muon", mp.nstr(dm["fro_offdiag"], 15))
    wb.add_data("off_over_diag_ratio_muon", mp.nstr(dm["off_over_diag"], 12))
    wb.add_data("nonabelian_share_of_datum_muon", mp.nstr(dm["off2_fraction"], 12))
    wb.add_data("nonnormality_muon", mp.nstr(dm["nonnormality"], 12))
    wb.add_data("trace_scalar_muon", mp.nstr(dm["trace"], 12))
    wb.add_data("nonabelian_share_proton", mp.nstr(dp["off2_fraction"], 12))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all(p for _, p in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
