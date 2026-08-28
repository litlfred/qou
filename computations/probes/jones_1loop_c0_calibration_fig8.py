#!/usr/bin/env python3
"""Calibrate the c₀ (1-loop) extraction on the figure-eight 4₁ — a KNOWN case.

Companion to borromean_jones_1loop_torsion.py (PR #4238).  The Borromean c₀
extraction there is only a *measurement* until the pipeline is validated on a
case whose 1-loop constant is known in closed form.  4₁ is that case.

Ohtsuki's rigorous asymptotic expansion of the figure-eight Kashaev invariant
(T. Ohtsuki, Quantum Topol. 7 (2016) 669; Andersen–Hansen 2006) gives, with
log⟨4₁⟩_N = (N/2π)Vol + p·logN + c₀ + O(1/N), for the corpus real-form
(un-normalized) Kashaev sum:

  • p       = 3/2                     (exact, 1-cusp knot)
  • Vol(4₁) = 2·Cl₂(π/3) = 2.0298832… (exact)
  • c₀      = −¼ log 3 = −0.27465     (exact, in THIS normalization; the
              literature 1/(2·3^{1/4}) constant is a different, normalized,
              convention — the extra log 2 is the normalization offset)

and crucially the 1-loop conjecture (Dimofte–Garoufalidis) makes c₀ a torsion:

  exp(2 c₀) = 3^{−1/2} = |τ_adj(4₁)| = 1/√3,

the adjoint Reidemeister torsion of the figure-eight at the complete structure
(τ_adj = ±1/√(−3), |τ_adj| = 1/√3).

If the SAME least-squares pipeline used on the Borromean tower reproduces
c₀(4₁) = −0.2747, p = 3/2, Vol = 2.02988, AND |τ_adj| = 1/√3 (all a priori
known), the extraction and the c₀→torsion relation are pinned on a known case,
and the Borromean c₀ = −1.417 becomes a trustworthy measured invariant.  The figure-eight Kashaev sum is cheap
(N up to 1200), so its c₀ carries far smaller extraction error than the
Habiro-triple-product Borromean tower — this is the clean calibration anchor.

NORMALIZATION NOTE (2026-08-08, bean qou-fl4t).  Nothing here is superseded —
this file is the anchor the later work calibrates on — but be explicit about
which τ it means.  The `|τ_adj(4₁)| = 1/√3` above is `1/T` with `T = √3`, and
`T = 2·|τ_DG|` where `|τ_DG(4₁)| = √3/2` is Dimofte–Garoufalidis' own worked
value (their eq. 3.2), computed at any cusp number by
`computations/one_loop_torsion.py`.  So this file's relation reads, in DG's
normalization,

    exp(2 c₀) = 1 / (2 |τ_DG|)     equivalently     c_σ = 2^{−1/2} |τ_DG|^{−1/2}

and that form carries NO per-cusp factor: the constant `2^{−1/2}` measured here
at c = 1 is the same one measured at c = 2 on the Whitehead link, to 17 digits,
so the c = 1 calibration in this file predicts c_σ(L5a1) = 2^{−3/4} with nothing
adjustable.  See `docs/audits/2026-08-08-per-cusp-factor-dissolves.md`.  The
`2^{(c−1)/2}` factor that once stood between them is proved to cancel in
`QOU.OneLoopEdgeLattice.percusp_factor_absorbs`.

Discipline: audit-only; scope-(a); NO fit (every 4₁ constant is known a priori
and only CHECKED, never tuned); nothing wired; L2 unchanged.  Reuses the
corpus's own figure-eight Kashaev sum
(computations/figure_eight_kashaev_volume.py).

-- Ref: [manuscript] docs/audits/2026-07-25-borromean-jones-asymptotics-volume-and-1loop.md
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80

VOL_4_1 = 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))   # 2·Cl₂(π/3) = 2.0298832…
# In THIS Kashaev normalization (corpus real form, ⟨4₁⟩ un-normalized) the
# 1-loop prefactor is 1/3^{1/4} (no factor of 2 — that "2" is a different
# normalization convention), so c₀ = −log(3^{1/4}) = −¼ log 3 = −0.27465,
# and exp(2c₀) = 3^{−1/2} = |τ_adj(4₁)| = 1/√3 (the known adjoint torsion).
C0_EXACT = -mp.log(3) / 4                                       # −¼ log 3 = −0.27465
TAU_ADJ_4_1 = 1 / mp.sqrt(3)                                    # |τ_adj(4₁)| = 1/√3


def kashaev_4_1_log(N: int) -> mp.mpf:
    """log ⟨4₁⟩_N = log Σ_{k=0}^{N-1} ∏_{j=1}^k (2 − 2cos(2πj/N)).
    Corpus real form (figure_eight_kashaev_volume.py). Positive, exact."""
    total = mp.mpf(0)
    prod = mp.mpf(1)  # k=0 empty product
    total += prod
    two_pi = 2 * mp.pi
    for k in range(1, N):
        prod *= (2 - 2 * mp.cos(two_pi * k / N))
        total += prod
    return mp.log(total)


def lstsq(rows_phi, ys):
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
    Ns = [200, 300, 400, 600, 800, 1200, 1600, 2200, 3000, 4000, 5000, 6000]
    logs = [kashaev_4_1_log(N) for N in Ns]

    print(f"Vol(4₁) = 2·Cl₂(π/3) = {mp.nstr(VOL_4_1, 12)}")
    print(f"c₀ exact = −¼log3 = {mp.nstr(C0_EXACT, 10)}  ⇒ |τ_adj|=exp(2c₀)=1/√3")
    print(f"\n{'N':>5} {'log⟨4₁⟩':>16} {'(2π/N)log':>14}")
    for i, N in enumerate(Ns):
        print(f"{N:>5} {float(logs[i]):>16.5f} {float((2*mp.pi/mp.mpf(N))*logs[i]):>14.7f}")

    # Vol-fixed fit  r = log⟨4₁⟩ − (N/2π)Vol = p·logN + c₀ + Σ_{m≥1} d_m/N^m.
    # The Ohtsuki expansion is a FULL asymptotic series in 1/N, so the
    # residual is set by the highest 1/N power modelled, NOT the (exact,
    # 60-dps) arithmetic. Modelling through 1/N⁴ + N up to 6000 drives the
    # c₀ (hence τ) error from ~1e-4 (one-term) to ~1e-9.
    KMAX = 4  # number of 1/N^m correction terms
    tail_lo = 200
    idx = [i for i, N in enumerate(Ns) if N >= tail_lo]
    resid = [logs[i] - (mp.mpf(Ns[i]) / (2 * mp.pi)) * VOL_4_1 for i in idx]

    def invpows(N):
        return [1 / mp.mpf(N) ** m for m in range(1, KMAX + 1)]

    phi = [[mp.log(mp.mpf(Ns[i])), mp.mpf(1)] + invpows(Ns[i]) for i in idx]
    sol = lstsq(phi, resid)
    p_fit, c0_fit = sol[0], sol[1]

    # free-slope cross-check (also frees the volume slope)
    phi4 = [[mp.mpf(Ns[i]), mp.log(mp.mpf(Ns[i])), mp.mpf(1)] + invpows(Ns[i]) for i in idx]
    sol4 = lstsq(phi4, [logs[i] for i in idx])
    a4, p4, c04 = sol4[0], sol4[1], sol4[2]

    c0_err = abs(float(c0_fit) - float(C0_EXACT))
    vol_err = abs(float(a4 * 2 * mp.pi) - float(VOL_4_1)) / float(VOL_4_1)
    print(f"\n── Vol-fixed fit, {KMAX} × 1/N terms (tail N≥{tail_lo}, N_max={Ns[-1]}) ──")
    print(f"  power p   = {mp.nstr(p_fit, 12)}   (exact 3/2)")
    print(f"  c₀        = {mp.nstr(c0_fit, 12)}   (exact {mp.nstr(C0_EXACT,12)}, err {c0_err:.2e})")
    print(f"── free-slope cross-check ──")
    print(f"  a·2π      = {mp.nstr(a4*2*mp.pi, 14)} (Vol {mp.nstr(VOL_4_1,14)}, rel {vol_err:.2e})")
    print(f"  power p   = {mp.nstr(p4, 12)}")
    print(f"  c₀        = {mp.nstr(c04, 12)}")

    # torsion readout on the KNOWN case: |τ_adj| = exp(2·c₀)  (this normalization)
    tau_measured = mp.e ** (2 * c0_fit)
    tau_err = abs(float(tau_measured) - float(TAU_ADJ_4_1))
    print(f"\n  |τ_adj(4₁)| = exp(2c₀) = {mp.nstr(tau_measured, 12)}")
    print(f"              1/√3      = {mp.nstr(TAU_ADJ_4_1, 12)}   (err {tau_err:.2e})")

    validated = (c0_err < 1e-6 and abs(float(p_fit) - 1.5) < 1e-5
                 and vol_err < 1e-8 and tau_err < 1e-6)
    print(f"\nVERDICT: pipeline {'VALIDATED' if validated else 'NOT validated'} on 4₁ "
          f"(c₀ err {c0_err:.1e}, p−3/2 {abs(float(p_fit)-1.5):.1e}, Vol rel {vol_err:.1e}, "
          f"τ err {tau_err:.1e}) — "
          f"{'Borromean c₀ extraction trustworthy' if validated else 'investigate'}.")

    script_path = Path(__file__).resolve()
    src = script_path.read_text()
    try:
        commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(script_path)],
            cwd=script_path.parent, text=True).strip()
    except Exception:
        commit = ""
    witness = {
        "engine": "mpmath", "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(), "commitSha": commit,
        "scriptFile": "computations/probes/jones_1loop_c0_calibration_fig8.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12], "scriptCommitSha": commit,
        "description": "Calibrate the c₀ (1-loop) extraction pipeline on the "
                       "figure-eight 4₁, whose Vol, power 3/2, c₀=−¼log3, and adjoint "
                       "torsion |τ|=1/√3 are known in closed form. Validates the Borromean "
                       "c₀ extraction. Audit-only; no fit; nothing wired.",
        "auditOnly": True,
        "parameters": {"Ns": Ns, "tail_lo": tail_lo, "KMAX_invN_terms": KMAX},
        "data": {
            "vol_4_1_exact": mp.nstr(VOL_4_1, 16),
            "c0_exact_neg_quarter_log3": mp.nstr(C0_EXACT, 16),
            "fit_vol_fixed": {"power_p": mp.nstr(p_fit,16), "c0": mp.nstr(c0_fit,16)},
            "fit_free_slope": {"vol_from_slope": mp.nstr(a4*2*mp.pi,16),
                                "power_p": mp.nstr(p4,16), "c0": mp.nstr(c04,16)},
            "c0_abs_err": c0_err, "vol_rel_err": vol_err,
            "tau_adj_measured": mp.nstr(tau_measured,16), "tau_adj_exact_1_over_sqrt3": mp.nstr(TAU_ADJ_4_1,16), "tau_abs_err": tau_err,
            "pipeline_validated": bool(validated),
        },
    }
    out = script_path.with_name("jones-1loop-c0-calibration-fig8.witness.json")
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
