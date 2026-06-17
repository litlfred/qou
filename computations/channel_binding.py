#!/usr/bin/env python3
"""
channel_binding — three-channel inter-nucleon binding kernel (INFRA).

Each inter-nucleon crossing (c, d) carries THREE Hecke/Wedderburn
channels (the two eigenvalues of (σ−q)(σ+q⁻¹)=0 plus the standard
traced channel):

    symmetric    s(c,d) = c·q + d          (eigenvalue +q)
    standard     V(c,d) = z·c + d          (z = √q/(q+1))
    alternating  a(c,d) = −c·q⁻¹ + d       (eigenvalue −q⁻¹)

Inter-nucleon crossing coefficients (canonical, from
hecke_core_symbolic.atom_gen_chains_sym):

    pp = (1, 0),   nn = (1, −h),   pn = (1, −h/2),    h = q − q⁻¹.

**Per-bond-type channel assignment (the "each channel its own
treatment" rule).** The three channels are NOT interchangeable; each
bond type lives in the channel its spin/isospin dictates:

  - **pp, nn** (identical nucleons, T=1) are Pauli-antisymmetric →
    **ALTERNATING** channel.  At q₀ their alt value is negative /
    |·|≥1 → **unbound** (contribute 0).  This is correct: the diproton
    and dineutron have NO bound state.
  - **pn** (T can be 0) — the bound deuteron channel → **STANDARD**.

Binding:  B(K) = E₀ · Σ_{bonds} bond_E(channel(bond)),
          bond_E(f) = log(1/f) if 0<f<1 else 0  (unbound channel → 0),
          E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV.

The bond graph is the **complete graph** (n_pp=C(Z,2), n_pn=Z·N,
n_nn=C(N,2)) — exact for light nuclei; **it overbinds at scale**
(Z·N grows ~A²) and must be replaced by a saturation/shell edge rule
for A ≳ 4.  This module reports that breakdown honestly rather than
hiding it.

Public API:
    bond_counts(Z, N) -> dict           complete-graph bond multiplicities
    channel_value(bond, channel) -> mpf  s/V/a for a bond type
    bond_E(f) -> mpf                     per-bond binding magnitude
    channel_binding(Z, N, channel_map=PAULI_MAP) -> mpf   B in MeV
    B_pauli_ch(Z, N) -> mpf              the canonical Pauli-mixed form

CLI: prints the per-bond channel table + a B_pauli-ch dashboard across
a nuclide range (default light→mid), flagging the complete-graph
breakdown.  Exploratory infra — no production rewire.
"""
from __future__ import annotations

import sys
from math import comb
from pathlib import Path

import _path_bridge  # noqa: F401, E402 — cluster path bridge
import mpmath as mp  # noqa: E402

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Canonical substrate constants (fall back to literals if imports fail).
try:
    from q_parameter import Q as _Q                       # noqa: E402
    from experimental_constants import M_E_MEV as _ME     # noqa: E402
    Q0 = mp.mpf(str(_Q))
    M_E = mp.mpf(str(_ME))
except Exception:  # pragma: no cover - standalone fallback
    Q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
    M_E = mp.mpf("0.51099895069")

E0 = M_E / (Q0 * (Q0 - 1))
_QI = 1 / Q0
_H = Q0 - _QI
_Z = mp.sqrt(Q0) / (Q0 + 1)

# bond type -> crossing (c, d)
BOND_CD = {"pp": (mp.mpf(1), mp.mpf(0)),
           "nn": (mp.mpf(1), -_H),
           "pn": (mp.mpf(1), -_H / 2)}

# the canonical per-bond-type channel assignment (Pauli)
PAULI_MAP = {"pp": "alt", "nn": "alt", "pn": "std"}


def channel_value(bond: str, channel: str) -> mp.mpf:
    """The s/V/a Hecke-channel value of one inter-nucleon crossing."""
    c, d = BOND_CD[bond]
    if channel == "sym":
        return c * Q0 + d
    if channel == "std":
        return _Z * c + d
    if channel == "alt":
        return -c * _QI + d
    raise ValueError(f"unknown channel {channel!r}")


def bond_E(f) -> mp.mpf:
    """Per-bond binding magnitude in log units: log(1/f) if the channel
    binds (0<f<1), else 0 (unbound: f≤0 antisymmetric, or f≥1)."""
    return mp.log(1 / f) if (0 < f < 1) else mp.mpf(0)


def bond_counts(Z: int, N: int) -> dict:
    """Complete-graph inter-nucleon bond multiplicities."""
    return {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)}


def channel_binding(Z: int, N: int, channel_map=None) -> mp.mpf:
    """B(K) in MeV under a per-bond-type channel assignment."""
    cmap = channel_map or PAULI_MAP
    cnt = bond_counts(Z, N)
    return E0 * sum(cnt[b] * bond_E(channel_value(b, cmap[b])) for b in cnt)


def B_pauli_ch(Z: int, N: int) -> mp.mpf:
    """The canonical Pauli-mixed binding: pp,nn → alt (unbound),
    pn → std.  Equivalently E₀·(Z·N)·log(1/f_pn)."""
    return channel_binding(Z, N, PAULI_MAP)


# ── CLI / dashboard ───────────────────────────────────────────────────

# A light→mid nuclide ladder (Z, N, AME binding MeV).  AME2020.
_LADDER = [
    ("2H", 1, 1, "2.224566"), ("3H", 1, 2, "8.481798"),
    ("3He", 2, 1, "7.718043"), ("4He", 2, 2, "28.295673"),
    ("6Li", 3, 3, "31.99463"), ("7Li", 3, 4, "39.24454"),
    ("9Be", 4, 5, "58.16498"), ("12C", 6, 6, "92.16175"),
    ("16O", 8, 8, "127.6193"), ("40Ca", 20, 20, "342.0521"),
    ("56Fe", 26, 30, "492.2540"),
]


def main() -> int:
    print("=" * 80)
    print("  channel_binding — three-channel inter-nucleon kernel")
    print(f"  E₀ = {mp.nstr(E0,7)} MeV   z = {mp.nstr(_Z,6)}   h = {mp.nstr(_H,6)}")
    print("=" * 80)
    print("\n  Per-bond Hecke-channel values f and bond_E = E₀·log(1/f) [MeV]:")
    print(f"  {'bond':>4} | {'sym':>10} {'std':>10} {'alt':>10} | "
          f"{'assigned':>8} {'E[MeV]':>9} {'bound?':>7}")
    for b in ("pp", "pn", "nn"):
        s, v, a = (channel_value(b, c) for c in ("sym", "std", "alt"))
        ch = PAULI_MAP[b]
        f = channel_value(b, ch)
        E = E0 * bond_E(f)
        print(f"  {b:>4} | {mp.nstr(s,6):>10} {mp.nstr(v,6):>10} "
              f"{mp.nstr(a,6):>10} | {ch:>8} {mp.nstr(E,5):>9} "
              f"{str(0 < f < 1):>7}")

    print("\n  B_pauli-ch dashboard (pp,nn → alt[unbound], pn → std):")
    print(f"  {'iso':>5} {'A':>3} {'bonds pp/pn/nn':>15} {'AME_B':>9} "
          f"{'B_pauli-ch':>11} {'err(AME/B)':>11}")
    print("  " + "-" * 64)
    for iso, Z, N, ame in _LADDER:
        cnt = bond_counts(Z, N)
        B = B_pauli_ch(Z, N)
        ame_b = mp.mpf(ame)
        err = ame_b / B if B != 0 else mp.inf
        flag = ""
        if Z + N > 4 and err < mp.mpf("0.5"):
            flag = "  <- complete-graph OVERBINDS (needs saturation rule)"
        print(f"  {iso:>5} {Z+N:>3} "
              f"{str((cnt['pp'],cnt['pn'],cnt['nn'])):>15} "
              f"{mp.nstr(ame_b,6):>9} {mp.nstr(B,6):>11} "
              f"{mp.nstr(err,4):>11}{flag}")

    print("\n  Reading: B_pauli-ch removes the spurious pp/nn binding "
          "(Pauli/alt channel).\n  Valid for light nuclei (D/T/³He/⁴He); "
          "the complete-graph Z·N pn count\n  overbinds past A≈4 — the open "
          "saturation/shell edge rule (not this module).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
