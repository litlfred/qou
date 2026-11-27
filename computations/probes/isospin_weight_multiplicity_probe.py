#!/usr/bin/env python3
"""
isospin_weight_multiplicity_probe.py -- size of the isospin multiplicity term.

Bean qou-o8lo (ledger gap G2), epic qou-myts.  Diagnostic only; nothing is wired and
no producer number changes.  AME enters ONLY as a comparison.

WHAT IS DERIVED (Lean, QOU/Nuclear/IsospinWeightMultiplicity.lean)
------------------------------------------------------------------
On N = 3A quark strands with n_u up and n_d down quarks (n_u = 2Z + N_n,
n_d = Z + 2N_n), the number of states at fixed T_z = (n_u - n_d)/2 is the weight
count C(3A, n_d), and it is the sum of the two-row block dimensions
d(N,k) = C(N,k) - C(N,k-1) over the blocks with T >= |T_z| (sum_twoRowDim).
The weight count falls off Gaussian-like with scale sqrt(N) (weight_le):
C(2M, M-s)/C(2M, M) <= 1/(1 + s^2/(M+s)).

WHAT IS ASSUMED HERE (not derived)
---------------------------------
The energy map: B gets + alpha * ln(count), alpha = 8 G m_e (the proxy scale of
#9706 and the writhe probe), i.e. a larger count binds more.  The sign and the
log are the assumption.  Two counts are compared:
  weight : C(3A, n_d)                  (what fixed (Z, N_n) selects)
  block  : d(3A, min(n_u, n_d))         (the lowest isospin block alone)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))

from _precision import set_compute_dps  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

set_compute_dps()

M_E = mp.mpf("0.51099895069")


def ln_weight(z: int, n: int) -> mp.mpf:
    A = z + n
    return mp.log(mp.binomial(3 * A, z + 2 * n))


def ln_block(z: int, n: int) -> mp.mpf:
    A = z + n
    N = 3 * A
    k = min(2 * z + n, z + 2 * n)
    d = mp.binomial(N, k) - (mp.binomial(N, k - 1) if k > 0 else 0)
    return mp.log(d)


def median(xs):
    s = sorted(xs)
    L = len(s)
    return s[L // 2] if L % 2 else (s[L // 2 - 1] + s[L // 2]) / 2


def main() -> int:
    alpha = M_E * 8 * mp.catalan

    wit = json.loads((COMP / "mass-table-comprehensive.witness.json").read_text())
    by = {(r["Z"], r["N"]): r for r in wit["data"]["rows"]}
    ame = json.loads((COMP / "data" / "ame2020.json").read_text())
    ame = ame if isinstance(ame, list) else next(v for v in ame.values() if isinstance(v, list))

    rows = []  # same filter as generate-accuracy-scorecard.py Table 3.4b
    for e in ame:
        z, n = int(e["Z"]), int(e["N"])
        if e.get("beta_decay_energy_estimated") or e.get("beta_decay_energy_keV") is None:
            continue
        q_exp = mp.mpf(str(e["beta_decay_energy_keV"])) / 1000
        if q_exp <= mp.mpf("0.01"):
            continue
        a, b = by.get((z, n)), by.get((z + 1, n - 1))
        if not a or not b:
            continue
        mk = "m_ruled_MeV" if a.get("m_ruled_MeV") else "m_symbolic_MeV"
        if not b.get(mk):
            continue
        q0 = mp.mpf(a[mk]) - mp.mpf(b[mk]) - M_E
        rows.append((z, n, q0, q_exp))

    report = {}
    for name, f in [("no_term", None), ("weight", ln_weight), ("block", ln_block)]:
        rels = []
        for z, n, q0, q_exp in rows:
            dq = mp.mpf(0)
            if f is not None:
                # mass = -B, B = +alpha ln count; Q = M(parent) - M(daughter)
                dq = alpha * (f(z + 1, n - 1) - f(z, n))
            rels.append(abs(q0 + dq - q_exp) / q_exp)
        report[name] = mp.nstr(100 * median(rels), 6)

    samples = {}
    for nm, (z, n) in {"48Ca": (20, 28), "56Fe": (26, 30), "132Sn": (50, 82), "208Pb": (82, 126)}.items():
        A = z + n
        # share relative to the balanced count at the same A (n_d = floor(3A/2))
        zb = None
        w0 = mp.log(mp.binomial(3 * A, (3 * A) // 2))
        samples[nm] = {
            "weight_share_MeV": mp.nstr(alpha * (ln_weight(z, n) - w0), 6),
            "gaussian_-alpha*2Tz^2/N_MeV": mp.nstr(-alpha * 2 * (mp.mpf(n - z) / 2) ** 2 / (3 * A), 6),
            "classical_23*(N-Z)^2/A_MeV": mp.nstr(-23 * mp.mpf(n - z) ** 2 / A, 6),
        }

    lean_check = all(
        mp.binomial(2 * M, M - s) * (M + s + s * s) <= mp.binomial(2 * M, M) * (M + s)
        for M in range(1, 60) for s in range(0, M + 1)
    )
    checks = {
        "n_rows": (len(rows), 1010),
        "no_term_median_92.68": (report["no_term"][:5], "92.68"),
        "weight_le_rechecked_M<60": (lean_check, True),
    }
    ok = all(a == b for a, b in checks.values())

    print(f"alpha = {mp.nstr(alpha, 10)} MeV; Table 3.4b rows {len(rows)}")
    for k, v in report.items():
        print(f"  {k:8s} median |dQ|/Q = {v} %")
    for k, v in samples.items():
        print(f"  {k:6s} {v}")
    for k, (a, b) in checks.items():
        print(f"  [{'PASS' if a == b else 'FAIL'}] {k}: {a}")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("isospin-weight-multiplicity", engine="mpmath")
        wb.set_description(
            "Size of the isospin multiplicity term: weight count C(3A, n_d) and lowest block "
            "dimension, energy map B += alpha ln(count) ASSUMED; Table 3.4b Q_beta medians as "
            "a comparison only (Lean QOU.Nuclear.IsospinWeightMultiplicity)."
        )
        for k, (a, b) in checks.items():
            wb.add_assertion(k, computed=str(a), expected=str(b), tolerance="0")
        wb.add_data("alpha_MeV", mp.nstr(alpha, 15))
        wb.add_data("table_3_4b_median_rel_pct", report)
        wb.add_data("samples", samples)
        wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
