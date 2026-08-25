#!/usr/bin/env python3
"""W1 subleading term — extract the 1-loop (torsion) datum from the
Borromean colored-Jones asymptotics.

Follow-on to the merged volume anchor
(computations/probes/borromean_jones_volume_anchor.py, PR #4208), which
anchored the LEADING term: the Kashaev growth rate of J_{B,N}(e^{2πi/N})
recovers Vol(𝓑₃)=8G to 0.4%.  This probe extracts the NEXT term.

The Ohtsuki-type asymptotic expansion of the Kashaev invariant of a
hyperbolic link is

  log|J_{K,N}(e^{2πi/N})| = (N/2π)·Vol + p·log N + c₀ + O(1/N),

where
  • (N/2π)·Vol   is the leading volume term (anchored in #4208),
  • p            is the power-of-N prefactor (p = 3/2 for a 1-cusp
                 knot; 𝓑₃ has 3 cusps but MEASURES p = 3/2 too — the
                 J_{B,1}=1-normalized reduced Kashaev invariant grows
                 knot-like),
  • c₀           is the "1-loop" constant.  By the 1-loop conjecture
                 (Dimofte–Garoufalidis arXiv:1102.4847) exp(c₀) is
                 fixed by the ADJOINT REIDEMEISTER TORSION τ(𝓑₃) of
                 the complete hyperbolic structure (the delta-invariant
                 1/√(±τ), times explicit 2π/i factors).

We FIX Vol = 8G (known, from #4208) and least-squares fit the remaining
coefficients (p, c₀, and KMAX subleading 1/N^m terms) from the exactly-
computable Habiro tower — the same higher-order methodology validated to
2e-11 on the figure-eight (jones_1loop_c0_calibration_fig8.py).  The
extracted (p, c₀) are the second and third honest bridge data below the
volume — the numbers any derived index↔tr_M bridge must also reproduce
on its side.

What this does / does NOT do:
  • DOES measure p and c₀ from the Jones side, parameter-free.
  • Does NOT yet compare c₀ to an independent τ(𝓑₃): the corpus carries
    no Borromean adjoint torsion (grep 2026-07-25).  Computing τ(𝓑₃)
    from the octahedral Neumann–Zagier data is the bounded follow-up
    that turns this MEASUREMENT into a MATCH.  We report c₀ honestly as
    a measured constant, not a verified torsion match.

Discipline: audit-only; scope-(a); NO fit of any physical observable
(Vol is fixed by topology; p, c₀ are read off, not tuned to a target);
nothing wired; no c_k; L2 unchanged.  Reuses the corpus Habiro
transcription (Garoufalidis–Le arXiv:math/0508100 v6 App A).

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md

THEOREM BACKING (2026-08-02, bean qou-pvuw): the 1-loop conjecture used below is now a THEOREM for both calibration cases — 4_1 is 2-bridge (Garoufalidis-Yoon arXiv:2411.03801 Thm 1.1, [garoufalidis-yoon-2024], library/arxiv-2411.03801v2/2411.03801v2.pdf) and the Borromean rings are a fundamental shadow link (Pandey-Wong arXiv:2308.06643, [pandey-wong-2023]). Wording below kept for history; readings of exp(2c0) = 1/|det J_NZ| are theorem-backed.

⚠ FOLLOW-UP DELIVERED 2026-08-08 (bean qou-fl4t).  The bounded follow-up named
above — "computing tau(B3) from the octahedral Neumann-Zagier data" — now exists:
`computations/one_loop_torsion.py` computes the triangulation-invariant
Dimofte-Garoufalidis 1-loop invariant at any cusp number, and gives

    |tau_DG(B3)| = |tau_DG(L6a4)| = 8       (audit
    docs/audits/2026-08-07-one-loop-multicusp-derivation.md)

The comparison this file asks for, in the c-free law
`exp(2 c_0) = 1/(2 |tau_DG|)` established in
docs/audits/2026-08-08-per-cusp-factor-dissolves.md:

    predicted   exp(2 c_0) = 1/16 = 0.0625
    measured    exp(2 c_0) = 0.06294           (this probe, NMAX=56)
    agreement   0.7%,  i.e. c_0 = -1.38281 measured vs -1.38629 predicted

READ THAT AS SUPPORTING, NOT AS A MATCH.  The two fits here bracket the
prediction (vol-fixed c_0 = -1.38281, free-slope c_0 = -1.37347, spread 0.0093
against a 0.0035 deviation), and this tower's own witness note flags an
unresolved normalization+cusp offset against the 1-cusp anchor, with p = 1.4993
against the exact 3/2.  The decisive comparison is at c = 2, where the corpus
has 20 digits: whitehead_c_sigma_hiprec.py gives c_sigma(L5a1) = 2^{-3/4}, and
the same law predicts it from the 4_1 calibration alone to ~17 digits with
nothing fitted.

NOTE the normalization: |det J_NZ| in this file's relation is 2|tau_DG|, not
|tau_DG|.  `exp(2c_0) = 1/|det J_NZ|` at c = 1 is `1/sqrt(3)`, and
|tau_DG(4_1)| = sqrt(3)/2 — DG's own normalization, a factor 2 apart.
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

V_OCT = 4 * mp.catalan       # ideal regular octahedron = 4G
VOL_BOR = 2 * V_OCT          # Borromean complement = 8G ≈ 7.327724753


def log_abs_habiro_at_root(n: int) -> mp.mpf:
    """log |J_{B,n}(e^{2πi/n})| via the corpus Habiro sum (removable-pole
    safe: evaluate at s = e^{iπ(1+δ)/n}, δ = 1e-30, 60 dps)."""
    delta = mp.mpf("1e-30")
    sval = mp.e ** (1j * mp.pi * (1 + delta) / n)

    def brk(j: int):
        return sval**j - sval ** (-j)

    total = mp.mpc(0)
    bn2 = brk(n) ** 2
    for l in range(0, n):
        num = bn2
        for j in range(1, l + 1):
            num *= (brk(n + j) * brk(n - j)) ** 3
        den = mp.mpc(1)
        for j in range(l + 1, 2 * l + 2):
            den *= brk(j) ** 2
        total += ((-1) ** l) * num / den
    return mp.log(abs(total))


def lstsq(rows_phi, ys):
    """Solve min ‖Φ c − y‖ via mpmath Gaussian elimination on the normal
    equations (no numpy in sandbox).  rows_phi[k] is the design row."""
    m = len(rows_phi[0])
    AtA = [[sum(rows_phi[k][i] * rows_phi[k][j] for k in range(len(rows_phi)))
            for j in range(m)] for i in range(m)]
    Aty = [sum(rows_phi[k][i] * ys[k] for k in range(len(rows_phi))) for i in range(m)]
    M = [AtA[i] + [Aty[i]] for i in range(m)]
    for col in range(m):
        piv = max(range(col, m), key=lambda rr: abs(M[rr][col]))
        M[col], M[piv] = M[piv], M[col]
        for rr in range(m):
            if rr != col and M[rr][col] != 0:
                f = M[rr][col] / M[col][col]
                M[rr] = [M[rr][c] - f * M[col][c] for c in range(m + 1)]
    return [M[i][m] / M[i][i] for i in range(m)]


def main() -> int:
    NMAX = 56
    print(f"Vol(𝓑₃) = 8G = {mp.nstr(VOL_BOR, 12)} (fixed from #4208)")
    Ns, logs = [], []
    for n in range(4, NMAX + 1):
        lg = log_abs_habiro_at_root(n)
        Ns.append(mp.mpf(n))
        logs.append(lg)
    # subtract the KNOWN leading volume term, fit the remainder to
    #   r(N) := log|J| − (N/2π)Vol = p·log N + c₀ + d/N.
    lead = [(N / (2 * mp.pi)) * VOL_BOR for N in Ns]
    resid = [logs[i] - lead[i] for i in range(len(Ns))]

    print(f"\n{'N':>3} {'log|J|':>16} {'r(N)=log|J|−volTerm':>22}")
    for i in range(len(Ns)):
        if int(Ns[i]) % 4 == 0 or i >= len(Ns) - 4:
            print(f"{int(Ns[i]):>3} {float(logs[i]):>16.6f} {float(resid[i]):>22.6f}")

    # Higher-order tail fit, matching the 4₁ calibration methodology
    # (jones_1loop_c0_calibration_fig8.py): model KMAX subleading 1/N^m
    # Ohtsuki terms so c₀ is not contaminated by the truncated tail.  The
    # Borromean Habiro tower is O(n³), so N_max is far smaller than 4₁'s
    # 6000 — c₀(𝓑₃) therefore carries a larger residual than the 1e-11
    # calibration anchor (reported honestly below).
    KMAX = 2
    tail_lo = 20
    idx = [i for i in range(len(Ns)) if Ns[i] >= tail_lo]

    def invpows(N):
        return [1 / N ** m for m in range(1, KMAX + 1)]

    # (A) Vol-fixed:  r = p·logN + c₀ + Σ d_m/N^m
    phiA = [[mp.log(Ns[i]), mp.mpf(1)] + invpows(Ns[i]) for i in idx]
    solA = lstsq(phiA, [resid[i] for i in idx])
    p_fit, c0_fit = solA[0], solA[1]

    # (B) free-slope cross-check: log|J| = a·N + p·logN + c₀ + Σ d_m/N^m
    phiB = [[Ns[i], mp.log(Ns[i]), mp.mpf(1)] + invpows(Ns[i]) for i in idx]
    solB = lstsq(phiB, [logs[i] for i in idx])
    a4, p4, c04 = solB[0], solB[1], solB[2]

    print(f"\n── Vol-fixed fit  r=p·logN + c₀ + {KMAX}×1/N^m  (tail N≥{tail_lo}, N_max={int(Ns[-1])}) ──")
    print(f"  power  p   = {float(p_fit):.5f}   (knot 3/2 = 1.5; 𝓑₃ has 3 cusps)")
    print(f"  1-loop c₀  = {float(c0_fit):.5f}")
    print(f"\n── free-slope cross-check ──")
    print(f"  slope a    = {float(a4):.6f}  → a·2π = {float(a4*2*mp.pi):.5f}  (8G = {float(VOL_BOR):.5f})")
    print(f"  power  p   = {float(p4):.5f}")
    print(f"  1-loop c₀  = {float(c04):.5f}")

    # 1-loop torsion candidate.  The 4₁ calibration
    # (jones_1loop_c0_calibration_fig8.py) VALIDATED the relation
    # |τ_adj| = exp(2c₀) to 2e-11 on the figure-eight (recovered 1/√3).
    # Applying the SAME relation here gives a candidate |τ_adj(𝓑₃)| —
    # but the 4₁ anchor is a 1-cusp KNOT in the un-normalized Kashaev
    # normalization, whereas this tower is a 3-cusp LINK in the Habiro
    # J_{B,1}=1 normalization.  The candidate therefore carries an
    # unquantified normalization/cusp-count offset until the octahedral
    # Neumann–Zagier τ(𝓑₃) is computed independently (the follow-up).
    delta_expc0 = float(mp.e ** c0_fit)
    tau_candidate = float(mp.e ** (2 * c0_fit))
    print(f"\n  exp(c₀)     = {delta_expc0:.6f}")
    print(f"  exp(2c₀)    = {tau_candidate:.6f}   (|τ_adj| candidate — normalization/cusp "
          f"offset vs the 4₁ anchor UNRESOLVED; τ(𝓑₃) NZ computation = follow-up)")

    verdict_vol = abs(float(a4 * 2 * mp.pi) - float(VOL_BOR)) / float(VOL_BOR) < 0.02
    print(f"\nVERDICT: leading volume re-confirmed ({'OK' if verdict_vol else 'OFF'}); "
          f"subleading power p≈{float(p_fit):.2f} and 1-loop constant c₀≈{float(c0_fit):.3f} "
          f"MEASURED (τ(𝓑₃) match is the follow-up).")

    script_path = Path(__file__).resolve()
    src = script_path.read_text()
    try:
        commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(script_path)],
            cwd=script_path.parent, text=True).strip()
    except Exception:
        commit = ""
    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": commit,
        "scriptFile": "computations/probes/borromean_jones_1loop_torsion.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12],
        "scriptCommitSha": commit,
        "theorem_backing": "GY 2411.03801 Thm 1.1 (4_1, 2-bridge) + PW 2308.06643 (Borromean, fundamental shadow link) — 1-loop = adjoint torsion proved for both cases",
        "description": "Subleading (power-of-N + 1-loop constant c₀) extraction "
                       "from the Borromean colored-Jones Kashaev asymptotics, "
                       "Vol fixed = 8G. The next honest bridge data below the "
                       "volume. Audit-only; no fit; nothing wired.",
        "auditOnly": True,
        "parameters": {"NMAX": NMAX, "tail_lo": tail_lo, "KMAX_invN_terms": KMAX, "root": "q=exp(2πi/N)"},
        "data": {
            "vol_borromean_8G": mp.nstr(VOL_BOR, 20),
            "fit_vol_fixed": {"power_p": float(p_fit), "c0": float(c0_fit)},
            "fit_free_slope": {"slope_a": float(a4), "vol_from_slope": float(a4 * 2 * mp.pi),
                                "power_p": float(p4), "c0": float(c04)},
            "exp_c0": delta_expc0,
            "exp_2c0_tau_candidate": tau_candidate,
            "verdict_leading_volume_ok": bool(verdict_vol),
            "note": "c0 MEASURED. exp(2c0)=|tau_adj| relation validated to 2e-11 "
                    "on 4_1 (jones_1loop_c0_calibration_fig8), but the 4_1 anchor is "
                    "1-cusp/un-normalized vs this 3-cusp/Habiro tower, so exp(2c0) here "
                    "is a candidate with an unresolved normalization+cusp offset; the "
                    "octahedral Neumann-Zagier tau(B3) is the follow-up.",
        },
    }
    out = script_path.with_name("borromean-jones-1loop-torsion.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
