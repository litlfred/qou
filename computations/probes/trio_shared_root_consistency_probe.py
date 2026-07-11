#!/usr/bin/env python3
"""
trio_shared_root_consistency_probe.py — is the Q_β / m_n / Δ_pn L2 residual trio
consistent with a SINGLE shared-root (Path C) structure, and which observable is
the bottleneck?

Path C (per-observable-100x-status.witness.json):
    m_n  = m_p + Q_β + m_e
    Δ_pn = m_n − m_p = Q_β + m_e         (m_e is exact, CAL-1)

If the shared root holds, the residuals must satisfy
    residual(Δ_pn) = residual(Q_β)            (+ residual(m_e) ≈ 0)
    residual(m_n)  = residual(m_p) + residual(Q_β)
which this probe checks against the committed dashboard values.

Finding: consistent to ~1e-9 MeV; the bottleneck is Q_β (+1248 ppb), NOT the
observations-level traced-volume α·|ΔΦ| formula (0.63%, a separate object).

Companion audit: docs/audits/2026-07-11-trio-shared-root-qbeta-bottleneck.md.
Values from computations/per-observable-100x-status.witness.json (Path C rows).
"""
from __future__ import annotations

# (pred_MeV, codata_MeV, err_ppb) from per-observable-100x-status.witness.json
ROWS = {
    "m_p":    (938.272089427, 938.272088160, 1.351),
    "m_mu":   (105.658397811, 105.658375649, 209.8),
    "Q_beta": (0.782334386518, 0.782333410, 1248.0),
    "m_n":    (939.565422765, 939.565420520, 2.389),
    "Delta_pn": (1.29333333721, 1.29333236, 755.6),
}
M_E_MEV = 0.51099895069  # exact CAL-1 (residual ≈ 0)


def residual(obs: str) -> float:
    pred, cod, _ = ROWS[obs]
    return pred - cod


def main() -> None:
    print("residual = pred − codata  (MeV):")
    for o in ("m_p", "Q_beta", "m_n", "Delta_pn"):
        print(f"  {o:9s} {residual(o):+.4e}   ({ROWS[o][2]:.0f} ppb)")

    print("\nshared-root (Path C) consistency:")
    d_dpn = abs(residual("Delta_pn") - residual("Q_beta"))
    d_mn = abs(residual("m_n") - (residual("m_p") + residual("Q_beta")))
    print(f"  Δ_pn residual  vs  Q_β residual        : Δ = {d_dpn:.1e} MeV")
    print(f"  m_n residual   vs  m_p + Q_β residual  : Δ = {d_mn:.1e} MeV")
    ok = d_dpn < 1e-8 and d_mn < 1e-8
    print(f"  ⇒ shared-root {'CONSISTENT' if ok else 'INCONSISTENT'} (both < 1e-8 MeV)")

    print("\nbottleneck: Q_β (+1248 ppb) drives Δ_pn (756 ppb) directly and, with")
    print("m_p (1.35 ppb), drives m_n (2.39 ppb). Closing the trio ⇒ close Q_β,")
    print("which is the c_k-truncation / Habiro-element problem — NOT the")
    print("observations traced-volume α·|ΔΦ| residual (0.63%, a separate object).")


if __name__ == "__main__":
    main()
