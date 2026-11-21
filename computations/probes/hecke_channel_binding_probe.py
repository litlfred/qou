#!/usr/bin/env python3
"""
Hecke-channel (chirality) binding probe (EXPLORATORY).

The canonical binding kernel uses ONE channel of each inter-nucleon
crossing — the standard channel V_std = z·c + d — for every bond type
(pp, pn, nn). That construction has no chirality: it binds the
*unbound* channels. Experimentally the diproton (pp) and dineutron (nn)
have NO bound state; only the deuteron (pn, spin-triplet) binds. So a
correct kernel must distinguish the symmetric (triplet, bound) channel
from the antisymmetric (singlet, Pauli, unbound) channel.

Each Hecke crossing (c, d) carries THREE Wedderburn channels:
    symmetric    s = c·q + d        (eigenvalue +q  channel)
    standard     V_std = z·c + d    (the one the kernel currently uses)
    alternating  a = -c·q^{-1} + d  (eigenvalue -q^{-1} channel)
with substrate weights
    w_sym = q^2/(q^4+4q^2+1),  w_std = (q^2+1)^2/(q^4+4q^2+1),
    w_alt = q^2/(q^4+4q^2+1),   V_full = w_sym·s + w_std·V_std + w_alt·a.

Inter-nucleon crossing coefficients (atom_gen_chains):
    pp = (1, 0),   nn = (1, -h),   pn = (1, -h/2),    h = q - q^{-1}.

Binding per bond:  E_0 · log(1/f),  f<1 binds, f>=1 unbound/repulsive,
E_0 = m_e/(q_0(q_0-1)) ≈ 4.186 MeV.

This probe tabulates every channel per bond type, flags whether pp/nn
come out UNBOUND (the physical requirement) in each channel, and tests
whether any Pauli-style channel assignment (pp,nn → antisymmetric;
pn → symmetric) lands the deuteron at AME 2.224 MeV. Exact mpmath,
zero free parameters.

Output: hecke-channel-binding.witness.json
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import markov_z  # noqa: E402 — canonical convention-D z
from q_parameter import Q_MP  # noqa: E402 — experimental (proton) pin

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention: it is
# the bar-symmetriser of z and averages the two flavours 50/50, so it cannot
# see the substrate flavour split. Imported rather than open-coded so there is
# one definition; the import is hard on purpose, because a fallback would
# silently compute the blind convention while reporting success.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

set_compute_dps()
HERE = Path(__file__).resolve().parent

# Proton pin per the standing 2026-08-07 directive: any probe that is
# WRITTEN OR MODIFIED defaults to the experimental layer.  This was a
# hardcoded MUON literal (…9555573347…), i.e. the ideal/CAL-2 layer.
Q0 = Q_MP
M_E = mp.mpf("0.51099895069")
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
qi = 1 / Q0
h = Q0 - qi
# Convention D via the canonical helper.  This was `mp.sqrt(Q0)/(Q0+1)`
# — convention C, excised by the 2026-08-09 ruling.  Note the witness
# `_provenance` already CLAIMED `z=q^3/(q^2+1)`, so the file documented D
# while computing C.  Calling `markov_z` rather than re-spelling z inline
# is deliberate: every convention detector keys on how z is WRITTEN, and
# an inline spelling is how a site goes blind (this one was missed by two
# independent detectors).
z = markov_z(Q0)

q2 = Q0 ** 2
denom = Q0 ** 4 + 4 * q2 + 1
w_sym = q2 / denom
w_std = (q2 + 1) ** 2 / denom
w_alt = q2 / denom

# bond (c, d)
BONDS = {"pp": (mp.mpf(1), mp.mpf(0)),
         "nn": (mp.mpf(1), -h),
         "pn": (mp.mpf(1), _pn_d(h))}   # colour-weighted

AME_D = AME_B_DEUTERON_MEV_VALIDATION   # only the deuteron is a bound 2-nucleon system


def channels(c, d):
    s = c * Q0 + d
    v = z * c + d
    a = -c * qi + d
    vfull = w_sym * s + w_std * v + w_alt * a
    return {"sym": s, "std": v, "alt": a, "Vfull": vfull}


def E_of(f):
    """Binding from a channel value f: E_0·log(1/f) (signed; >0 binds)."""
    if f <= 0:
        return None  # negative channel value: |f| used for magnitude separately
    return E0 * mp.log(1 / f)


def main() -> int:
    print("=" * 92)
    print("  Hecke-channel (chirality) binding probe")
    print(f"  E_0={mp.nstr(E0,7)} MeV  z={mp.nstr(z,6)}  h={mp.nstr(h,6)}  "
          f"w_sym={mp.nstr(w_sym,4)} w_std={mp.nstr(w_std,4)} w_alt={mp.nstr(w_alt,4)}")
    print("=" * 92)
    print(f"\n  {'bond':>4} | {'channel':>7} {'f':>12} {'E=E0 ln(1/f) MeV':>18} {'bound?':>7}")
    print("  " + "-" * 60)

    rows = []
    chvals = {}
    for bond, (c, d) in BONDS.items():
        ch = channels(c, d)
        chvals[bond] = ch
        for name, f in ch.items():
            bound = (0 < f < 1)
            # physical expectation: pp,nn should be UNBOUND; pn bound.
            E = E_of(f)
            Estr = (mp.nstr(E, 7) if E is not None else f"(|f|={mp.nstr(abs(f),5)}, f<0)")
            print(f"  {bond:>4} | {name:>7} {mp.nstr(f,8):>12} {Estr:>18} {str(bound):>7}")
            rows.append({"bond": bond, "channel": name, "f": str(f),
                         "E_MeV": (str(E) if E is not None else None),
                         "bound": bool(bound)})
        print("  " + "-" * 60)

    # ── Physical check: which channel makes BOTH pp and nn unbound? ──
    print("\n  Physical requirement: pp AND nn UNBOUND (f>=1), pn BOUND (f<1).")
    for name in ("sym", "std", "alt", "Vfull"):
        pp = chvals["pp"][name]; nn = chvals["nn"][name]; pn = chvals["pn"][name]
        pp_unbound = not (0 < pp < 1)
        nn_unbound = not (0 < nn < 1)
        pn_bound = (0 < pn < 1)
        ok = pp_unbound and nn_unbound and pn_bound
        print(f"    {name:>6}: pp_unbound={pp_unbound!s:>5}  nn_unbound={nn_unbound!s:>5}  "
              f"pn_bound={pn_bound!s:>5}   -> physical={ok}")

    # ── Deuteron landing under each pn channel ──────────────────────
    print(f"\n  Deuteron (single pn bond) vs AME {mp.nstr(AME_D,7)} MeV:")
    d_best = None
    for name in ("sym", "std", "alt", "Vfull"):
        f = chvals["pn"][name]
        E = E_of(f)
        if E is None:
            continue
        miss = abs(E - AME_D) / AME_D * 100
        print(f"    pn[{name:>5}]: E={mp.nstr(E,7)} MeV   miss={mp.nstr(miss,4)}%")
        if d_best is None or miss < d_best[0]:
            d_best = (miss, name, E)

    # ── Per-nucleus channel-binding dashboard (B_sym-ch / m_sym-ch) ──
    from math import comb
    M_P = mp.mpf("938.27208943")
    M_N = mp.mpf("939.56542194")
    NUC = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
    AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
             "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}

    def bond_E(channel, bond):
        """Per-bond binding magnitude in a channel; |f| for f<0; 0 if f>=1."""
        f = chvals[bond][channel]
        if f <= 0:
            f = abs(f)
        return E0 * mp.log(1 / f) if f < 1 else mp.mpf(0)  # unbound channel -> 0

    def B_channel(channel, Z, N):
        cnt = {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)}
        return sum(cnt[b] * bond_E(channel, b) for b in cnt)

    print("\n  Per-nucleus binding dashboard by channel  "
          "(B_sym-ch = symmetric channel; m_*-ch = Z·m_p+N·m_n−B):")
    print(f"\n  {'nuc':>4} {'AME_B':>9} | {'B_std':>8} {'B_sym-ch':>9} "
          f"{'B_alt-ch':>9} {'B_Vfull':>9} | {'m_sym-ch':>11} {'m_meas':>11}")
    print("  " + "-" * 86)
    dash = []
    for nuc, (Z, N) in NUC.items():
        bvals = {c: B_channel(c, Z, N) for c in ("std", "sym", "alt", "Vfull")}
        m_sym = Z * M_P + N * M_N - bvals["sym"]
        m_meas = Z * M_P + N * M_N - AME_B[nuc]
        print(f"  {nuc:>4} {mp.nstr(AME_B[nuc],6):>9} | "
              f"{mp.nstr(bvals['std'],5):>8} {mp.nstr(bvals['sym'],5):>9} "
              f"{mp.nstr(bvals['alt'],5):>9} {mp.nstr(bvals['Vfull'],5):>9} | "
              f"{mp.nstr(m_sym,9):>11} {mp.nstr(m_meas,9):>11}")
        dash.append({
            "nucleus": nuc, "Z": Z, "N": N,
            "AME_B_MeV": str(AME_B[nuc]),
            "B_std_MeV": str(bvals["std"]),
            "B_sym_ch_MeV": str(bvals["sym"]),
            "B_alt_ch_MeV": str(bvals["alt"]),
            "B_Vfull_MeV": str(bvals["Vfull"]),
            "m_sym_ch_MeV": str(m_sym),
            "m_measured_MeV": str(m_meas),
        })

    print("\n" + "=" * 92)
    # Verdict
    any_physical = any(
        (not (0 < chvals['pp'][n] < 1)) and (not (0 < chvals['nn'][n] < 1))
        and (0 < chvals['pn'][n] < 1) for n in ("sym", "std", "alt", "Vfull"))
    print(f"  Any single channel gives pp,nn UNBOUND + pn BOUND simultaneously: {any_physical}")
    print(f"  Best deuteron channel: pn[{d_best[1]}] miss {mp.nstr(d_best[0],4)}% "
          f"(need f_pn={mp.nstr(1/mp.e**(AME_D/E0),6)} for exact AME)")
    print("=" * 92)

    w = {
        "computation": "hecke-channel-binding",
        "kind": "exploratory-probe",
        "content_block": "step-9 binding / inter-nucleon channel",
        "engine": "mpmath-exact",
        "constants": {"q0": str(Q0), "E0_MeV": str(E0),
                      "w_sym": str(w_sym), "w_std": str(w_std), "w_alt": str(w_alt)},
        "channels_by_bond": {b: {k: str(v) for k, v in ch.items()}
                             for b, ch in chvals.items()},
        "rows": rows,
        "dashboard_by_nucleus": dash,
        "result": {
            "current_kernel_channel": "std",
            "any_channel_makes_pp_nn_unbound_pn_bound": bool(any_physical),
            "deuteron_best_channel": d_best[1],
            "deuteron_best_miss_pct": str(d_best[0]),
            "f_pn_needed_for_exact_AME": str(1 / mp.e ** (AME_D / E0)),
            "physical_red_flag": ("current std channel binds the UNBOUND pp/nn "
                                  "channels (diproton/dineutron have no bound state) "
                                  "— a genuine defect; the Hecke channel structure is "
                                  "tested here as the candidate fix."),
        },
        "_provenance": {
            "channels": "sym=c*q+d, std=z*c+d, alt=-c/q+d; Vfull=w_sym*sym+w_std*std+w_alt*alt",
            "weights": "w_sym=w_alt=q^2/(q^4+4q^2+1), w_std=(q^2+1)^2/(q^4+4q^2+1)",
            "bonds": "pp=(1,0), nn=(1,-h), pn=(1,-h/2), h=q-1/q",
            "refs": ["hecke_core_symbolic.py (atom_gen_chains_sym, _vertex_channels_sym)",
                     "prearchimedean_bond_factor.py", "derived_bond_graph_binding.py"],
        },
    }
    out = HERE.parent / "hecke-channel-binding.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(w, script_path=__file__, engine="mpmath")
    w["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(w, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
