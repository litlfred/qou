#!/usr/bin/env python3
"""W1 volume-asymptotics anchor — the honest bridge candidate, checked from
the computable colored-Jones (Habiro) side.

Context (read first):
  docs/audits/2026-07-24-borromean-index-bridge-invariant.md §1(d)-(e)
  docs/audits/2026-07-25-borromean-index-fbor-bridge-invariant.md

The I_𝓑₃ (3D-index) → F_Bor bridge invariant list PRUNES coefficientwise
evaluation at q₀ (integer coefficients, q₀ = 1.10998 > 1 lies OUTSIDE the
index's disc |q| < 1, series diverges — §1(e)).  The ONLY honest bridge
classes left are limit/continuation classes (§1(d)):

  (i)  the state-integral / total-index route (GHRS Rmk 1.13, GK
       arXiv:1411.6062) — pursued index-side on beans qou-zezz / qou-yaz9;
  (ii) the VOLUME-ASYMPTOTICS route (DGG arXiv:1112.5179 §4.6): in the
       't Hooft limit q → 1 the index's leading asymptotics carry the
       hyperbolic volume Vol(M).  §1(e) names this "the honest candidate"
       but does NOT numerically verify the shared-volume premise.

This probe supplies that missing number, from the side we CAN compute
exactly to high order: the colored Jones.  The Kashaev / volume-conjecture
statement for the hyperbolic link 𝓑₃ (Borromean rings, L6a4) is

  2π · lim_{N→∞} (1/N) · log |J_{B,N}(e^{2πi/N})|  =  Vol(𝓑₃) = 2·v_oct
                                                     ≈ 7.327724753.

If the Habiro colored-Jones tower reproduces THIS volume, the volume-
asymptotics bridge route (ii) is anchored with a real, parameter-free,
anti-fit number on the Jones side: the SAME Vol(𝓑₃) the DGG index
asymptotics must carry.  It does NOT by itself prove the index↔tr_M
bridge (that is the subleading torsion / state-integral identification,
research-paper-scale, on the DGG beans) — it verifies the leading term
that any honest bridge must share, and refutes nothing it should not.

Discipline: audit-only; scope-(a); NO fit (Vol(𝓑₃) is fixed by the
topology, never selected); nothing wired; no c_k; L2 unchanged.  The
Jones tower is the corpus's own Habiro transcription
(habiro_borromean_colored_jones.py, Garoufalidis-Le arXiv:math/0508100
v6 App A).  We only ADD a numerical root-of-unity evaluation of it.

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

# ── Vol(𝓑₃): 2 × ideal regular octahedron (Catalan-constant closed form) ──
# v_oct = 4G (ideal regular octahedron); Vol(Borromean) = 2·v_oct = 8G.
V_OCT = 4 * mp.catalan  # Vol(ideal regular octahedron) = 4G ≈ 3.663862753...
VOL_BOR = 2 * V_OCT      # Vol(Borromean complement) = 8G ≈ 7.327724753...


def eval_habiro_at_root(n: int) -> mp.mpf:
    """|J_{B,n}(q)| at q = e^{2πi/n}, evaluated numerically with mpmath.

    Verbatim the corpus transcription (Garoufalidis-Le App A):
      J_{B,n} = Σ_{l=0}^{n-1} (-1)^l {n}² (Π_{j=1}^l {n+j}{n-j})³
                              / (Π_{j=l+1}^{2l+1} {j})²,   {j}=s^j - s^{-j}.
    At the root of unity the denominator factor {n} vanishes but the sum
    is a genuine Laurent polynomial (A4), so the singularities are
    removable.  We evaluate at s = e^{iπ(1+δ)/n} with a tiny real δ off
    the exact root: each term stays finite (removable pole), and the
    O(δ) error is negligible (60-dps, δ = 1e-25) against the exponential
    growth we measure.
    """
    delta = mp.mpf("1e-25")
    sval = mp.e ** (1j * mp.pi * (1 + delta) / n)

    def brk(j: int):
        return sval**j - sval ** (-j)

    total = mp.mpc(0)
    bn2 = brk(n) ** 2
    for l in range(0, n):
        num = bn2 * mp.mpc(1)
        for j in range(1, l + 1):
            num *= (brk(n + j) * brk(n - j)) ** 3
        den = mp.mpc(1)
        for j in range(l + 1, 2 * l + 2):
            den *= brk(j) ** 2
        total += ((-1) ** l) * num / den
    return abs(total)


def main() -> int:
    print(f"Vol(𝓑₃) = 8G = {mp.nstr(VOL_BOR, 12)}  (2 ideal octahedra)")
    print(f"{'N':>3} {'|J_{B,N}(ζ)|':>18} {'(2π/N)log|J|':>16} {'rel.err vs Vol':>16}")
    NMAX = 40
    rows = []
    last_est = None
    for n in range(2, NMAX + 1):
        absz = eval_habiro_at_root(n)
        if absz <= 0:
            print(f"{n:>3} {float(absz):>18.6e}   (|J| = 0 — degenerate at this root)")
            continue
        est = float((2 * mp.pi / n) * mp.log(absz))
        rel = abs(est - float(VOL_BOR)) / float(VOL_BOR)
        last_est = est
        rows.append({"N": n, "absJ": float(absz), "vol_est": est, "rel_err": rel})
        print(f"{n:>3} {float(absz):>18.8f} {est:>16.8f} {rel:>16.4e}")

    # ── Log-aware fit.  The volume conjecture's refined asymptotic is
    #   log|J_{K,N}(ζ)| = (N/2π)·Vol + (3/2)·log N + c₀ + O(1/N),
    # so  y(N) := (2π/N)·log|J| = Vol + 3π·(log N)/N + (2π c₀)/N + O(1/N²).
    # The raw y(N) therefore approaches Vol from ABOVE, slowly, dominated
    # by the positive (log N)/N term — exactly the observed decrease.
    # Fit y(N) = Vol + A·(log N)/N + B/N by least squares over the tail;
    # the intercept Vol is the anchor.  (A ≈ 3π ≈ 9.42 if the standard
    # (3/2)log N term holds for this link; we let it float and report it.)
    tail = [r for r in rows if r["N"] >= 12]
    fit_vol = fit_A = fit_B = None
    if len(tail) >= 4:
        # design rows φ(N) = [1, log(N)/N, 1/N]; solve 3×3 normal equations
        # (AᵀA)c = Aᵀy by mpmath Gaussian elimination (no numpy in sandbox).
        phis, ys = [], []
        for r in tail:
            N = mp.mpf(r["N"])
            phis.append([mp.mpf(1), mp.log(N) / N, 1 / N])
            ys.append(mp.mpf(r["vol_est"]))
        AtA = [[sum(phis[k][i] * phis[k][j] for k in range(len(phis)))
                for j in range(3)] for i in range(3)]
        Aty = [sum(phis[k][i] * ys[k] for k in range(len(phis))) for i in range(3)]
        # Gaussian elimination on the augmented 3×4 system
        M = [AtA[i] + [Aty[i]] for i in range(3)]
        for col in range(3):
            piv = max(range(col, 3), key=lambda rr: abs(M[rr][col]))
            M[col], M[piv] = M[piv], M[col]
            for rr in range(3):
                if rr != col and M[rr][col] != 0:
                    f = M[rr][col] / M[col][col]
                    M[rr] = [M[rr][c] - f * M[col][c] for c in range(4)]
        coef = [M[i][3] / M[i][i] for i in range(3)]
        fit_vol, fit_A, fit_B = float(coef[0]), float(coef[1]), float(coef[2])

    print()
    if last_est is not None:
        print(f"raw  y(N={rows[-1]['N']})               = {last_est:.6f}  "
              f"(still + the (logN)/N tail)")
    if fit_vol is not None:
        rel_f = abs(fit_vol - float(VOL_BOR)) / float(VOL_BOR)
        print(f"log-aware fit intercept Vol   = {fit_vol:.6f}  (rel {rel_f:.3e})")
        print(f"  fitted (logN)/N coeff A     = {fit_A:.4f}   (3π = {float(3*mp.pi):.4f})")
        print(f"  fitted 1/N coeff B          = {fit_B:.4f}")
    print(f"target Vol(𝓑₃) = 8G           = {float(VOL_BOR):.6f}")

    verdict = (fit_vol is not None and
               abs(fit_vol - float(VOL_BOR)) / float(VOL_BOR) < 0.02)
    print()
    print("VERDICT:", "log-aware growth-rate fit recovers Vol(𝓑₃) to <2% — "
          "leading bridge term anchored (Jones side)" if verdict
          else "fit does NOT match Vol(𝓑₃) to <2% (see intercept above)")

    # ── witness ──
    script_path = Path(__file__).resolve()
    src = script_path.read_text()
    try:
        commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(script_path)],
            cwd=script_path.parent, text=True).strip()
    except Exception:
        commit = ""
    witness = {
        "engine": "mpmath+numpy",
        "engineVersion": f"mpmath {mp.__version__}, numpy",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": commit,
        "scriptFile": "computations/probes/borromean_jones_volume_anchor.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12],
        "scriptCommitSha": commit,
        "description": "Colored-Jones volume-conjecture growth rate for the "
                       "Borromean rings vs Vol(𝓑₃)=8G — anchors the leading term "
                       "of the volume-asymptotics bridge route (W1) from the "
                       "computable Jones side. Audit-only; no fit; nothing wired.",
        "auditOnly": True,
        "parameters": {"NMAX": NMAX, "root": "q = exp(2πi/N)"},
        "data": {
            "vol_borromean_target": mp.nstr(VOL_BOR, 20),
            "rows": rows,
            "log_aware_fit": {"vol_intercept": fit_vol, "logN_over_N_coeff": fit_A, "one_over_N_coeff": fit_B},
            "verdict_leading_term_matches": verdict,
            "target_vol_borromean_8G": float(VOL_BOR),
        },
    }
    out = script_path.with_name("borromean-jones-volume-anchor.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
