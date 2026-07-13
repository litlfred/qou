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

import json
from pathlib import Path

# Load the Path-C rows straight from the committed witness (source of truth), so
# the probe never drifts from the dashboard.  It reads each observable's OWN
# pred/codata pair from the same witness, so it still tests that witness's
# *internal* shared-root consistency (not live codata_constants).
# m_e is exact (CAL-1, residual ≈ 0), so it drops out of the residual identities.
_WITNESS = (Path(__file__).resolve().parent.parent
            / "per-observable-100x-status.witness.json")


def _load_rows() -> dict:
    rows = json.loads(_WITNESS.read_text())["data"]["rows"]
    return {r["obs"]: (float(r["pred_MeV"]), float(r["codata_MeV"]), float(r["err_ppb"]))
            for r in rows}


ROWS = _load_rows()


def residual(obs: str) -> float:
    pred, cod, _ = ROWS[obs]
    return pred - cod


def main() -> None:
    print(f"witness: {_WITNESS.name}")
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
