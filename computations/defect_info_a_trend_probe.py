"""A-trend probe: does the defect-weighted channel-information energy converge to the residual?

Audit-only decisive probe (2026-07-04 audit sec 6; owner-approved follow-up to the
twice-measured 4He near-match, PRs #3271/#3275). The defect-weighted channel-information
energy E_defect_info was within ~10% of the raw binding residual at 4He (ratio 0.904)
but wrong-signed at A <= 3. The decisive question is the A-TREND: if the ratio

    rho(A) = E_defect_info(A) / r_raw(A),   r_raw = B_AME - B(q0)

approaches 1 as A grows (6Li, 7Li), the channel-information energy is the ASYMPTOTIC
missing binding term (an extensivity statement — cf. the jet-filtration extensive
mechanism, prop:jet-filtration-binding-extensive); if it drifts away, the 4He agreement
is recorded as coincidence and the candidate closes scope-(a).

All ingredients fit-free and canonical: B(q0) = E0*ln(trM_free/trM_atom) from the
production transfer path (tr_m_atom_zn); B_AME from the vendored AME2020 witness;
defect channel weights w_lam = y_lam*(chi_free - chi_atom); E0 = m_e/(q0(q0-1)).
Tier: shape-probe; nothing wired.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from phase5_n8_dim_q_table import hook_lengths  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from chi_free_via_lr import chi_free_lr  # noqa: E402
# Frobenius route: identical values (agree to 1.3e-67 per
# chi-free-via-frobenius.witness.json) and far faster as A grows —
# 31x at 6Li, 104x at 7Li — because it needs O(A^2) cycle types where
# the LR route enumerates O(3^A) tuples.
from chi_free_via_frobenius import chi_free_frobenius  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0, Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

COMPUTE_DPS = 70
DPS = 50
AME_WITNESS = Path(__file__).with_name("ame-2020-binding-energies.witness.json")
# iso -> (Z, N, AME key); the A-trend extension points beyond the committed 4-isotope set
ISOTOPES = {
    "2H": (1, 1, "B_deuteron_MeV"), "3H": (1, 2, "B_tritium_MeV"),
    "3He": (2, 1, "B_he3_MeV"), "4He": (2, 2, "B_he4_MeV"),
    "6Li": (3, 3, "B_li6_MeV"), "7Li": (3, 4, "B_li7_MeV"),
}


def dim_q_numeric(lam: tuple[int, ...], q0: mp.mpf) -> mp.mpf:
    """Symmetric-convention q-hook quantum dimension at q0 (normalization cancels)."""
    def b(h: int) -> mp.mpf:
        return q0**h - q0**(-h)
    val = mp.mpf(1)
    for k in range(1, sum(lam) + 1):
        val *= b(k)
    for h in hook_lengths(lam):
        val /= b(h)
    return val


def main() -> int:
    start = time.monotonic()
    mp.mp.dps = COMPUTE_DPS
    ame = json.loads(AME_WITNESS.read_text())["data"]
    q0 = Q_MP  # high-precision q0 (Q is the f64 shim)
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0 = _qbeta_e0.order_zero_scaled(m_e, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    rows = {}
    ratios_by_a: list[tuple[int, mp.mpf]] = []
    print("  iso |  A |  B(q0)      B_AME    r_raw   |  E_defect_info |  ratio")
    for iso, (z, nn, key) in ISOTOPES.items():
        tr_atom, tr_free, chi_atom, _ = tr_m_atom_zn(z, nn, dps=COMPUTE_DPS)
        chi_free = chi_free_frobenius(z, nn, dps=COMPUTE_DPS)
        n = 3 * (z + nn)
        b_q0 = e0 * mp.log(tr_free / tr_atom)
        b_ame = mp.mpf(ame[key])
        r_raw = b_ame - b_q0
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
        w = {lam: y[lam] * (chi_free.get(lam, mp.mpf(0)) - chi_atom.get(lam, mp.mpf(0)))
             for lam in y}
        zabs = mp.fsum(abs(v) for v in w.values())
        e_def = (e0 / 2) * mp.fsum(
            abs(v) / zabs * mp.log(dim_q_numeric(lam, q0)) for lam, v in w.items())
        ratio = e_def / r_raw if r_raw != 0 else None
        if ratio is not None:
            ratios_by_a.append((z + nn, ratio))
        rows[iso] = {
            "Z": z, "N": nn, "A": z + nn, "strands": n,
            "B_q0_MeV": mp.nstr(b_q0, DPS), "B_AME_MeV": mp.nstr(b_ame, DPS),
            "residual_raw_MeV": mp.nstr(r_raw, DPS),
            "E_defect_info_MeV": mp.nstr(e_def, DPS),
            "ratio": mp.nstr(ratio, DPS) if ratio is not None else None,
        }
        ratio_str = f"{float(ratio):8.3f}" if ratio is not None else "     n/a"
        print(f"  {iso:4s}| {z+nn:2d} | {float(b_q0):8.3f}  {float(b_ame):8.3f}  "
              f"{float(r_raw):8.3f} |   {float(e_def):10.3f}   |  {ratio_str}")

    # decisive trend: |ratio - 1| at the largest three A values, non-increasing?
    tail = sorted(ratios_by_a)[-3:]
    devs = [abs(r - 1) for _, r in tail]
    converging = bool(all(devs[i + 1] <= devs[i] for i in range(len(devs) - 1)))
    print(f"\n  |ratio-1| at largest A {[a for a, _ in tail]}: "
          f"{[float(d) for d in devs]}  -> converging: {converging}")

    witness = {
        "description": ("A-trend of the defect-weighted channel-information energy vs "
                        "raw binding residual, extended to 6Li/7Li: decisive test of "
                        "whether the twice-measured 4He near-match (0.904) is the onset "
                        "of an asymptotic (extensive) identification or a coincidence."),
        "audit_only": True,
        "tier": "shape-probe (fit-free; production channel weights; nothing wired)",
        "precision_dps": {"compute": COMPUTE_DPS, "serialized": DPS},
        "source_witness": AME_WITNESS.name,
        "constants": {"q_0": mp.nstr(q0, DPS), "E0_MeV": mp.nstr(e0, DPS)},
        "isotopes": rows,
        "verdict": {"deviation_from_1_nonincreasing_at_top3_A": converging},
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "defect-info-a-trend-probe", witness,
        script_path=__file__, engine="mpmath", start_time=start,
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
