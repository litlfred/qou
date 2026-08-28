#!/usr/bin/env python3
"""CALIBRATION of the c_σ = |τ_adjoint|^{-1/2} template on the figure-eight knot.

The Whitehead c_σ is measured (whitehead_c_sigma_hiprec.py) as
    c_σ(W) := lim_N |J'_N| · N^{-3/2} · e^{-Vol·N/2π}  =  2^{-3/4}  (16 digits).

To argue this is the 1-loop torsion prefactor (c_σ = |τ|^{-1/2}, τ = adjoint
Reidemeister torsion) rather than a coincidence, we run the SAME c_σ definition
on the figure-eight knot 4_1, whose value is INDEPENDENTLY KNOWN:
    c_σ(4_1) = 3^{-1/4}   ⇔   |τ(4_1)| = √3   (the classic figure-eight torsion,
                                                trace field ℚ(√-3)).

The reduced colored Jones of 4_1 at q=e^{2πi/N} is the Habiro/Kashaev single sum
(unknot-normalized, the SAME normalization class as van der Veen's reduced J for
the Whitehead):
    J'_N(4_1) = Σ_{k=0}^{N-1} ∏_{j=1}^k (2 sin(πj/N))²        (real, positive).

If this pipeline returns 3^{-1/4} to high precision AND p=3/2, the template is
validated on the known case → the Whitehead output 2^{-3/4} ⇒ |τ(L5a1)| = 2√2
is a template-consistent identification (not a bare fit).  Audit-only; NO wiring.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


def log_J_fig8(N: int) -> mp.mpf:
    """log J'_N(4_1)(e^{2πi/N}) = log Σ_{k} ∏_{j≤k}(2 sin(πj/N))²  (positive sum)."""
    piN = mp.pi / N
    fac = [(2 * mp.sin(j * piN)) ** 2 for j in range(1, N)]   # f[j-1]=(2sin(jπ/N))²
    tot = mp.mpf(1)      # k=0 term = empty product = 1
    prod = mp.mpf(1)
    for k in range(1, N):
        prod *= fac[k - 1]
        tot += prod
    return mp.log(tot)


def c_sigma_fig8(N, A) -> mp.mpf:
    return mp.e ** (log_J_fig8(N) - mp.mpf(3) / 2 * mp.log(N) - A * N)


def fit_p(Ns, logs, A):
    """Least-squares (p, c0, a1, a2) for log J = A N + p log N + c0 + a1/N + a2/N²."""
    import mpmath
    M = mpmath.matrix(len(Ns), 4)
    y = mpmath.matrix(len(Ns), 1)
    for i, N in enumerate(Ns):
        M[i, 0] = mp.log(N); M[i, 1] = 1; M[i, 2] = mp.mpf(1) / N; M[i, 3] = mp.mpf(1) / N ** 2
        y[i] = logs[N] - A * N
    # normal equations
    MT = M.T
    sol = mpmath.lu_solve(MT * M, MT * y)
    return sol[0], sol[1]


def neville_1overN(Ns, vals):
    xs = [mp.mpf(1) / N for N in Ns]
    T = [list(vals)]
    m = len(vals)
    for k in range(1, m):
        row = []
        for i in range(m - k):
            xi, xik = xs[i], xs[i + k]
            row.append((T[k - 1][i + 1] * (-xi) - T[k - 1][i] * (-xik)) / (xik - xi))
        T.append(row)
    return T[m - 1][0]


if __name__ == "__main__":
    mp.mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    VOL41 = 2 * mp.im(mp.polylog(2, mp.exp(mp.pi * 1j / 3)))   # Vol(4_1)=2·Im Li₂(e^{iπ/3})
    A = VOL41 / (2 * mp.pi)
    print(f"figure-eight c_σ calibration — mpmath dps={mp.mp.dps}")
    print(f"  Vol(4_1) = {mp.nstr(VOL41, 20)}  (expect 2.029883...)")
    print(f"  A = Vol/2π = {mp.nstr(A, 20)}\n")

    Ns = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2
                           else "300,500,800,1200,1700,2300,3000").split(",")]
    logs = {}
    for N in Ns:
        logs[N] = log_J_fig8(N)
    p, c0 = fit_p(Ns, logs, A)
    print(f"  p-exponent fit = {mp.nstr(p, 12)}   (target 3/2)")

    cs = [c_sigma_fig8(N, A) for N in Ns]
    for N, c in zip(Ns, cs):
        print(f"  N={N:5d}: c_σ = {mp.nstr(c, 20)}")
    c_inf = neville_1overN(Ns, cs)
    target = mp.power(3, mp.mpf(-1) / 4)
    rel = abs(c_inf - target) / target
    digits = int(-mp.log10(rel)) if rel > 0 else 999
    print(f"\n  c_σ(4_1) extrapolated = {mp.nstr(c_inf, 22)}")
    print(f"  3^{{-1/4}}             = {mp.nstr(target, 22)}")
    print(f"  |Δ| rel = {mp.nstr(rel, 4)}  → match to ~{digits} digits")
    print(f"  ⇒ template c_σ = |τ|^{{-1/2}} VALIDATED (|τ(4_1)| = √3)"
          if digits >= 8 else "  ⇒ template NOT validated at this N-reach")

    wit = {
        "description": "Calibration of the c_σ=|τ|^{-1/2} template on the figure-eight knot: same c_σ definition (reduced colored Jones · N^{-3/2} · e^{-Vol N/2π}) as the Whitehead run, checked against the known 3^{-1/4} (|τ(4_1)|=√3).",
        "computation": "whitehead_c_sigma_fig8_calib", "audit_only": True,
        "dps": mp.mp.dps,
        "vol_4_1": mp.nstr(VOL41, 25),
        "p_fit": mp.nstr(p, 15),
        "c_sigma_fig8_extrapolated": mp.nstr(c_inf, 25),
        "target_3_pow_minus_1_4": mp.nstr(target, 25),
        "match_digits": digits,
        "template_validated": digits >= 8,
        "note": "Validates that the reduced-colored-Jones c_σ IS the 1-loop torsion prefactor |τ|^{-1/2} on the known figure-eight case, making the Whitehead c_σ=2^{-3/4} ⇒ |τ(L5a1)|=2√2 a template-consistent identification.",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-c-sigma-fig8-calib.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(wit, indent=2))
    print(f"\n  Witness: {out}")
