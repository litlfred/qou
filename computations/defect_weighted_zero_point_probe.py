"""Defect-weighted zero-point probe: channel-information energy under the ACTUAL defect measure.

Audit-only probe (2026-07-04 audit sec 5 follow-up 2). The sec-4 probe used the bare
Plancherel measure and was refuted as a sole uniform mechanism (sign flips). This probe
replaces the measure with the physical one: the convolution-defect's own per-channel
weights

    w_lam = y_lam * (chi_free^lam - chi_atom^lam)

(the per-partition object of `binding_canonical` / conj:binding-qbeta-complex-volume),
normalized by |w|, and asks whether the channel-information energy under THAT measure

    E_defect_info = (E0/2) * sum_lam |w_lam|/Z * ln dim_q(lam),   Z = sum |w_lam|

tracks the per-isotope binding residuals r_raw = B_AME - B(q0). Channel data from the
production transfer-matrix path (tr_m_atom_zn -> chi_atom; chi_free_lr -> chi_free;
y_lambda_at -> y_lam) — fit-free, but no longer measure-naive.

Tier: shape-probe; verdict scope-(a) either way; nothing wired.
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
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

COMPUTE_DPS = 70
DPS = 50
WITNESS_IN = Path(__file__).with_name("binding-bar-even-odd-probe.witness.json")
ISOTOPES = {"2H": (1, 1), "3H": (1, 2), "3He": (2, 1), "4He": (2, 2)}  # iso -> (Z, N)


def dim_q_numeric(lam: tuple[int, ...], q0: mp.mpf) -> mp.mpf:
    """Symmetric-convention q-hook quantum dimension at q0."""
    def qi(h: int) -> mp.mpf:
        return (q0**h - q0**(-h)) / (q0 - q0**(-1))
    val = mp.mpf(1)
    for k in range(1, sum(lam) + 1):
        val *= qi(k)
    for h in hook_lengths(lam):
        val /= qi(h)
    return val


def main() -> int:
    start = time.monotonic()
    mp.mp.dps = COMPUTE_DPS
    src = json.loads(WITNESS_IN.read_text())
    q0 = mp.mpf(src["constants"]["q_0"])
    e0 = mp.mpf(src["constants"]["E0_MeV"])

    rows = {}
    print("  iso |  E_defect_info  |  r_raw = B_AME-B(q0) |  ratio")
    for iso, (z, nn) in ISOTOPES.items():
        _, _, chi_atom, _ = tr_m_atom_zn(z, nn, dps=COMPUTE_DPS)
        chi_free = chi_free_lr(z, nn, dps=COMPUTE_DPS)
        n = 3 * (z + nn)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
        w = {lam: y[lam] * (chi_free.get(lam, mp.mpf(0)) - mp.mpf(str(chi_atom.get(lam, 0))))
             for lam in y}
        zabs = mp.fsum(abs(v) for v in w.values())
        e_def = (e0 / 2) * mp.fsum(
            abs(v) / zabs * mp.log(dim_q_numeric(lam, q0)) for lam, v in w.items())
        d = src["isotopes"][iso]
        r_raw = mp.mpf(d["B_AME_MeV"]) - mp.mpf(d["B_q0_MeV"])
        ratio = e_def / r_raw if r_raw != 0 else None
        rows[iso] = {
            "Z": z, "N": nn, "strands": n,
            "E_defect_info_MeV": mp.nstr(e_def, DPS),
            "residual_raw_MeV": mp.nstr(r_raw, DPS),
            "ratio": mp.nstr(ratio, 12) if ratio is not None else None,
        }
        print(f"  {iso:4s}|  {float(e_def):10.3f}     |  {float(r_raw):10.3f}          |  "
              f"{float(ratio):8.3f}" if ratio is not None else f"  {iso}: r_raw = 0")

    ratios = [mp.mpf(rows[i]["ratio"]) for i in rows if rows[i]["ratio"] is not None]
    tracks = bool(ratios and all(mp.mpf("0.5") <= r <= mp.mpf(2) for r in ratios))
    print(f"\n  defect-weighted info candidate tracks r_raw (all in [0.5,2]): {tracks}")

    witness = {
        "description": ("Defect-weighted zero-point probe: channel-information energy "
                        "(E0/2)*sum |w|/Z * ln dim_q under the actual convolution-defect "
                        "channel weights w = y*(chi_free - chi_atom) from the production "
                        "transfer path, vs per-isotope binding residuals."),
        "audit_only": True,
        "tier": "shape-probe (fit-free; production channel weights; nothing wired)",
        "precision_dps": {"compute": COMPUTE_DPS, "serialized": DPS},
        "source_witness": WITNESS_IN.name,
        "constants": {"q_0": mp.nstr(q0, 20), "E0_MeV": mp.nstr(e0, 20)},
        "isotopes": rows,
        "verdict": {"defect_weighted_info_tracks_raw_residual": tracks},
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "defect-weighted-zero-point-probe", witness,
        script_path=__file__, engine="mpmath", start_time=start,
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
