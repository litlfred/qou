#!/usr/bin/env python3
"""channel_binding — three-channel inter-nucleon binding **library**.

A robust, importable library for downstream use (other consumers, not
just the dashboard). It composes the *canonical derived infra* — it does
NOT re-derive channels, constants, or the crossing map:

  * **Channel evaluator** — the canonical symbolic Wedderburn evaluator
    ``hecke_core_symbolic._vertex_channels_sym`` returns the three Hecke
    channels ``(symmetric, standard, alternating)`` of a crossing chain.
    Everything here is driven from it (single source of truth), so the
    **symbolic route is exact** and the numeric route is its evaluation
    at the substrate ``q₀``.
  * **Constants** — ``q_parameter.Q`` (substrate ``q₀``) and the canonical
    electron mass; ``E₀ = m_e/(q₀(q₀−1))`` is the derived binding scale.
  * **Crossing map** — the canonical inter-nucleon ``(c, d)`` per bond
    type from ``hecke_core_symbolic.atom_gen_chains_sym`` (pp=(1,0),
    nn=(1,−h), pn=(1,−h/2)); reproduced here as ``BOND_CROSSING`` and
    cross-checked against the source in :func:`self_test`.

THREE ROUTES, all preserved (owner directive):

  ============  ================================================
  ``"symbolic"``  exact sympy expressions in ℚ(√q)
  ``"numeric"``   mpmath evaluation at ``q₀`` (default dps from _precision)
  qCLT            :func:`qclt_binding` — the q-CLT forms (uniform +
                  p↔n colour-weighted), preserved alongside the channel
                  forms for downstream comparison
  ============  ================================================

PHYSICS — the "each channel its own treatment" rule. Each crossing
carries the two eigenvalues of ``(σ−q)(σ+q⁻¹)=0`` (symmetric ``+q``,
alternating ``−q⁻¹``) plus the standard traced channel ``z·c+d``. Bond
types live in the channel their spin/isospin dictates:

  * **pp, nn** (identical nucleons, T=1) — Pauli-antisymmetric →
    **ALTERNATING** channel; at ``q₀`` their alt value is negative / |·|≥1
    → **unbound** (the diproton and dineutron have no bound state).
  * **pn** — the bound deuteron channel → **STANDARD**.

Binding (per a bond→channel assignment ``channel_map``):

    B(K) = E₀ · Σ_bonds n_bond · bond_E(channel_value(bond, channel_map[bond]))
    bond_E(f) = log(1/f)  if  0 < f < 1  else  0   (unbound channel → 0)

The bond graph is the **complete graph** (n_pp=C(Z,2), n_pn=Z·N,
n_nn=C(N,2)) — exact for light nuclei; it **overbinds at scale** (Z·N
grows ~A²) and needs a saturation/shell edge rule for A ≳ 4. The library
exposes the bond counts so a downstream edge rule can replace the
complete graph.

Public API (stable):
    q0(dps) -> mpf
    E0(dps) -> mpf
    bond_crossing(bond) -> list[(c, d)]            (sympy)
    bond_channels(bond, route, dps) -> dict        sym/std/alt
    bond_energy(bond, channel, route, dps)         per-bond E [MeV]
    bond_counts(Z, N) -> dict
    channel_binding(Z, N, channel_map, route, dps) -> B [MeV]
    B_pauli_ch(Z, N, route, dps) -> B [MeV]         the canonical Pauli form
    qclt_binding(Z, N, colour_weighted, route, dps) -> B [MeV]  (qCLT route)
    binding_summary(Z, N, dps) -> dict             all forms, downstream-ready
    self_test() -> None                            cross-check vs canonical source

Exploratory infra — no production rewire.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
from math import comb
from typing import Iterable, Literal

import _path_bridge  # noqa: F401  — cluster path bridge (puts substrate/ on path)
import sympy as sp
import mpmath as mp

# ── Canonical infra (reused, never re-derived) ───────────────────────
from hecke_core_symbolic import (          # the canonical symbolic core
    _vertex_channels_sym,                  # (sym, std, alt) channel evaluator
    q as _Q_SYM,                           # sp.Symbol("q", positive=True)
    h as _H_SYM,                           # q − q⁻¹  (symbolic)
)
from q_parameter import Q as _Q0           # canonical substrate q₀
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)
try:
    from experimental_constants import M_E_MEV as _ME   # CAL-1 electron mass
except Exception:                           # pragma: no cover
    from codata_constants import M_E_MEV as _ME
try:
    from _precision import COMPUTE_DPS as _DEFAULT_DPS
except Exception:                           # pragma: no cover
    _DEFAULT_DPS = 50

Route = Literal["symbolic", "numeric"]
Channel = Literal["sym", "std", "alt"]

#: Canonical inter-nucleon crossing (c, d) per bond type — single source
#: of truth is ``hecke_core_symbolic.atom_gen_chains_sym``; cross-checked
#: in :func:`self_test`.
BOND_CROSSING: dict[str, list[tuple[sp.Expr, sp.Expr]]] = {
    "pp": [(sp.Integer(1), sp.Integer(0))],
    "nn": [(sp.Integer(1), -_H_SYM)],
    "pn": [(sp.Integer(1), -_H_SYM / 2)],
}

CHANNELS: tuple[Channel, ...] = ("sym", "std", "alt")

#: The canonical Pauli channel assignment: same-isospin → alternating
#: (unbound); different-isospin pn → standard (bound).
PAULI_MAP: dict[str, Channel] = {"pp": "alt", "nn": "alt", "pn": "std"}

#: The trivial "all-standard" assignment = the current production kernel.
STANDARD_MAP: dict[str, Channel] = {"pp": "std", "nn": "std", "pn": "std"}


# ── Substrate constants ───────────────────────────────────────────────

def q0(dps: int = _DEFAULT_DPS) -> mp.mpf:
    """Canonical substrate q₀ as an mpf at ``dps`` precision."""
    with mp.workdps(dps):
        return mp.mpf(str(_Q0() if callable(_Q0) else _Q0))


def E0(dps: int = _DEFAULT_DPS) -> mp.mpf:
    """Derived binding scale E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV."""
    with mp.workdps(dps):
        q = q0(dps)
        return mp.mpf(str(_ME)) / (q * (q - 1))


# ── Channels (driven from the canonical symbolic evaluator) ───────────

def bond_crossing(bond: str) -> list[tuple[sp.Expr, sp.Expr]]:
    """Canonical (c, d) crossing chain for a bond type ('pp'|'pn'|'nn')."""
    return BOND_CROSSING[bond]


def _channels_sym(chain: Iterable[tuple[sp.Expr, sp.Expr]],
                  simplify: bool = True) -> dict:
    """The three raw Hecke channels of a crossing chain.

    ``simplify=True`` (default, back-compat) returns ``sp.simplify``-d
    expressions — wanted for the exact ``route="symbolic"`` output and
    any human-readable display. Pass ``simplify=False`` (P16) when the
    result is fed straight into ``sp.N`` at ``q₀`` (the numeric route):
    the cosmetic ``sp.simplify`` on the un-reduced channel expression is
    pure overhead before a numerical evaluation. Ref: 2834792d.
    """
    sym, std, alt = _vertex_channels_sym(list(chain))
    if not simplify:
        return {"sym": sym, "std": std, "alt": alt}
    return {"sym": sp.simplify(sym), "std": sp.simplify(std), "alt": sp.simplify(alt)}


def bond_channels(bond: str, route: Route = "numeric",
                  dps: int = _DEFAULT_DPS) -> dict:
    """The three Hecke-channel values {sym, std, alt} of a bond type.

    ``route="symbolic"`` → exact sympy expressions in ℚ(√q).
    ``route="numeric"``  → mpf values at q₀.
    """
    # Numeric route evaluates at q₀ immediately, so skip the cosmetic
    # symbolic simplify (P16); the symbolic route keeps the exact form.
    chans = _channels_sym(bond_crossing(bond), simplify=(route == "symbolic"))
    if route == "symbolic":
        return chans
    with mp.workdps(dps):
        q = q0(dps)
        return {k: mp.mpf(str(sp.N(v.subs(_Q_SYM, sp.Rational(mp.nstr(q, dps + 5))),
                                   dps + 5))) for k, v in chans.items()}


def bond_energy(bond: str, channel: Channel, route: Route = "numeric",
                dps: int = _DEFAULT_DPS):
    """Per-bond binding magnitude E₀·log(1/f) in MeV (numeric), or the
    symbolic ``log(1/f)`` factor. Unbound channels (f≤0 or f≥1) → 0."""
    if route == "symbolic":
        f = _channels_sym(bond_crossing(bond))[channel]
        return sp.log(1 / f)   # caller interprets domain; symbolic form
    with mp.workdps(dps):
        f = bond_channels(bond, "numeric", dps)[channel]
        e0 = E0(dps)
        return e0 * mp.log(1 / f) if (0 < f < 1) else mp.mpf(0)


# ── Bond graph + binding ──────────────────────────────────────────────

def bond_counts(Z: int, N: int) -> dict:
    """Complete-graph inter-nucleon bond multiplicities (the open edge
    rule is downstream; this is the saturating upper bound)."""
    return {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)}


def channel_binding(Z: int, N: int, channel_map: dict | None = None,
                    route: Route = "numeric", dps: int = _DEFAULT_DPS):
    """B(K) [MeV] under a per-bond-type channel assignment.

    ``route="symbolic"`` returns the exact ``E₀·Σ n_bond·log(1/f)`` with
    unbound channels (f not in (0,1) at q₀) dropped — domain decided
    numerically, coefficients kept symbolic.
    """
    cmap = channel_map or PAULI_MAP
    cnt = bond_counts(Z, N)
    if route == "symbolic":
        num = bond_channels  # to test domain
        terms = []
        for b in ("pp", "pn", "nn"):
            if cnt[b] == 0:
                continue
            fnum = num(b, "numeric", dps)[cmap[b]]
            if 0 < fnum < 1:
                fsym = _channels_sym(bond_crossing(b))[cmap[b]]
                terms.append(cnt[b] * sp.log(1 / fsym))
        m_e = sp.Rational(mp.nstr(mp.mpf(str(_ME)), dps))
        import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
        E0_sym = _qbeta_e0.order_zero_scaled(m_e, _Q_SYM)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
        return sp.simplify(E0_sym * sum(terms)) if terms else sp.Integer(0)
    with mp.workdps(dps):
        return sum(cnt[b] * bond_energy(b, cmap[b], "numeric", dps)
                   for b in ("pp", "pn", "nn"))


def B_pauli_ch(Z: int, N: int, route: Route = "numeric",
               dps: int = _DEFAULT_DPS):
    """Canonical Pauli-mixed binding: pp,nn → alt (unbound), pn → std."""
    return channel_binding(Z, N, PAULI_MAP, route, dps)


# ── Generalization: per-channel WEIGHTS, and the k-body → λ lift ───────
#
# The pick-one channel assignment (``channel_map``) is the degenerate
# case of a per-bond WEIGHTING over the three channels.  More generally a
# bond carries a weight on each Hecke channel set by its spin-isospin
# Young symmetry (Pauli):
#
#     B(K) = E₀ · Σ_bonds n_bond · Σ_ch w(bond, ch) · bond_E_factor(ch)
#
# **This is the n=2 special case of the framework's per-isotope formula.**
# The two 2-nucleon Hecke channels (symmetric ``+q``, alternating
# ``−q⁻¹``) ARE the two irreps of S₂.  For a k-nucleon cluster they
# generalize to the partitions ``λ ⊢ k`` — the Wedderburn blocks of
# H_k(q) — and the weighted sum becomes
#
#     B(K) = m_e · Σ_{λ ⊢ 3A} y_λ · χ^λ(β_K) · Δ_λ(K)        (per-isotope)
#
# i.e. ``Δ_λ`` is the k-body generalization of the per-channel weight
# ``w(bond, ch)``.  The Pauli–Young structural claim is that ``Δ_λ`` is
# the spin-isospin Young-symmetry (Pauli) projection onto λ.  Filling in
# those weights for k ≥ 3 IS the open Δ_λ problem (gated; see
# CLAUDE.md §"Δ_λ gate").  This library generalizes the STRUCTURE
# (arbitrary per-bond/per-λ channel weights); the specific Pauli–Young
# weights for k ≥ 3 are research-grade and NOT asserted here.

#: A weighting over the three channels, per bond type.  ``ChannelWeights``
#: maps bond -> {channel: weight}.  Missing channels default to 0.
ChannelWeights = dict  # dict[str, dict[Channel, float | sp.Expr]]

#: The Pauli pick-one assignment expressed as weights (B_pauli_ch).
PAULI_WEIGHTS: ChannelWeights = {
    "pp": {"alt": 1}, "nn": {"alt": 1}, "pn": {"std": 1},
}

#: The current production kernel as weights (all-standard).
STANDARD_WEIGHTS: ChannelWeights = {
    "pp": {"std": 1}, "nn": {"std": 1}, "pn": {"std": 1},
}


def weighted_channel_binding(Z: int, N: int, weights: ChannelWeights | None = None,
                             route: Route = "numeric", dps: int = _DEFAULT_DPS):
    """B(K) [MeV] for an arbitrary per-bond-type channel **weighting**
    (the generalization of :func:`channel_binding`'s pick-one map).

    ``weights[bond][channel]`` weights that channel's binding factor; the
    per-channel factor is ``log(1/f)`` when the channel binds (0<f<1 at
    q₀) and 0 otherwise.  :data:`PAULI_WEIGHTS` reproduces
    :func:`B_pauli_ch`; :data:`STANDARD_WEIGHTS` the production kernel.
    Downstream consumers supply their own (e.g. a Pauli–Young projection)
    — this is the n=2 hook for the general ``Δ_λ`` weighting.
    """
    w = weights or PAULI_WEIGHTS
    cnt = bond_counts(Z, N)
    with mp.workdps(dps):
        e0 = E0(dps)
        total = mp.mpf(0)
        for bond in ("pp", "pn", "nn"):
            if cnt[bond] == 0:
                continue
            fch = bond_channels(bond, "numeric", dps)
            bond_sum = mp.mpf(0)
            for ch, wt in (w.get(bond, {}) or {}).items():
                f = fch[ch]
                factor = mp.log(1 / f) if (0 < f < 1) else mp.mpf(0)
                bond_sum += mp.mpf(str(wt)) * factor
            total += cnt[bond] * bond_sum
        return e0 * total


# ── qCLT route (preserved) ────────────────────────────────────────────

def qclt_binding(Z: int, N: int, colour_weighted: bool = True,
                 route: Route = "numeric", dps: int = _DEFAULT_DPS):
    """The q-CLT binding form (standard-part-functor.md), preserved here
    for downstream comparison alongside the channel forms.

    ``colour_weighted=False`` → B_qCLT = E₀·(A−1)·L_pn  (uniform, no p↔n).
    ``colour_weighted=True``  → B_qCLT_fac = E₀·(A−1)·⟨bond-type L⟩
        (p↔n colour-weighted mean of the standard-channel log over the
        complete graph).
    """
    A = Z + N
    if A < 2:
        return sp.Integer(0) if route == "symbolic" else mp.mpf(0)
    if route == "symbolic":
        Lpn = sp.log(1 / _channels_sym(bond_crossing("pn"))["std"])
        if not colour_weighted:
            m_e = sp.Rational(mp.nstr(mp.mpf(str(_ME)), dps))
            return sp.simplify(_qbeta_e0.order_zero_scaled(m_e, _Q_SYM) * (A - 1) * Lpn)
        # colour-weighted mean of std-channel L over the complete graph
        cnt = bond_counts(Z, N)
        Ls = {b: sp.log(1 / _channels_sym(bond_crossing(b))["std"])
              for b in ("pp", "pn", "nn")}
        tot = sum(cnt.values())
        mean = sum(cnt[b] * Ls[b] for b in cnt) / tot
        m_e = sp.Rational(mp.nstr(mp.mpf(str(_ME)), dps))
        return sp.simplify(_qbeta_e0.order_zero_scaled(m_e, _Q_SYM) * (A - 1) * mean)
    with mp.workdps(dps):
        e0 = E0(dps)
        Lpn = mp.log(1 / bond_channels("pn", "numeric", dps)["std"])
        if not colour_weighted:
            return e0 * (A - 1) * Lpn
        cnt = bond_counts(Z, N)
        Ls = {b: mp.log(1 / bond_channels(b, "numeric", dps)["std"])
              for b in ("pp", "pn", "nn")}
        tot = sum(cnt.values())
        mean = sum(cnt[b] * Ls[b] for b in cnt) / tot
        return e0 * (A - 1) * mean


# ── Downstream-ready summary ──────────────────────────────────────────

def binding_summary(Z: int, N: int, dps: int = _DEFAULT_DPS) -> dict:
    """All binding forms for (Z,N) in one dict — for downstream consumers.

    Numeric (MeV): B_std, B_pauli_ch, B_qCLT, B_qCLT_fac + bond counts.
    """
    cnt = bond_counts(Z, N)
    return {
        "Z": Z, "N": N, "A": Z + N, "bond_counts": cnt,
        "B_std": float(channel_binding(Z, N, STANDARD_MAP, "numeric", dps)),
        "B_pauli_ch": float(B_pauli_ch(Z, N, "numeric", dps)),
        "B_qCLT": float(qclt_binding(Z, N, False, "numeric", dps)),
        "B_qCLT_fac": float(qclt_binding(Z, N, True, "numeric", dps)),
    }


def self_test() -> None:
    """Cross-check the reproduced BOND_CROSSING against the canonical
    source ``atom_gen_chains_sym`` and the known per-bond channel values."""
    from hecke_core_symbolic import atom_gen_chains_sym
    # pp from atom (2,0): the single inter-nucleon crossing is the last g0 entry
    for bond, (zc, nc) in {"pp": (2, 0), "nn": (0, 2), "pn": (1, 1)}.items():
        g0, _ = atom_gen_chains_sym(zc, nc)
        canonical = g0[-1]   # the inter-nucleon crossing appended last
        mine = BOND_CROSSING[bond][0]
        assert sp.simplify(canonical[0] - mine[0]) == 0, (bond, canonical, mine)
        assert sp.simplify(canonical[1] - mine[1]) == 0, (bond, canonical, mine)
    # numeric sanity: f_pn(std) ≈ 0.5082, f_pp(alt) < 0 (unbound)
    #
    # 0.5082 is the **convention D** value (z = q³/(q²+1)).  This constant read
    # 0.3948 until 2026-08-24, which was convention C (z = √q/(q+1)); the
    # channel is linear in z -- fitting the two runs gives std = z - 0.10452 to
    # 1e-4 -- so the whole move is the z shift and nothing else.  The
    # structural half of this self-test (BOND_CROSSING vs atom_gen_chains_sym)
    # is convention-independent and passed unchanged through the migration.
    ch = bond_channels("pn", "numeric")
    assert abs(ch["std"] - mp.mpf("0.5082")) < mp.mpf("1e-3"), ch
    assert bond_channels("pp", "numeric")["alt"] < 0
    print("self_test: OK (BOND_CROSSING matches atom_gen_chains_sym; "
          "f_pn(std)≈0.508; pp(alt)<0 unbound)")


# ── CLI dashboard ─────────────────────────────────────────────────────

_LADDER = [
    ("2H", 1, 1, _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)), ("3H", 1, 2, _ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)),
    ("3He", 2, 1, _ame_nstr(AME_B_HE3_MEV_VALIDATION, 30)), ("4He", 2, 2, _ame_nstr(AME_B_HE4_MEV_VALIDATION, 30)),
    ("6Li", 3, 3, "31.99463"), ("7Li", 3, 4, "39.24454"),
    ("9Be", 4, 5, "58.16498"), ("12C", 6, 6, "92.16175"),
    ("16O", 8, 8, "127.6193"), ("40Ca", 20, 20, "342.0521"),
    ("56Fe", 26, 30, "492.2540"),
]


def main() -> int:
    self_test()
    print("\n" + "=" * 84)
    print("  channel_binding library — forms via canonical _vertex_channels_sym")
    print(f"  E₀ = {mp.nstr(E0(), 7)} MeV   (symbolic + numeric + qCLT routes)")
    print("=" * 84)
    print("\n  Per-bond channels (numeric) + Pauli assignment:")
    print(f"  {'bond':>4} | {'sym':>10} {'std':>10} {'alt':>10} | "
          f"{'Pauli ch':>8} {'E[MeV]':>9}")
    for b in ("pp", "pn", "nn"):
        c = bond_channels(b, "numeric")
        E = bond_energy(b, PAULI_MAP[b], "numeric")
        print(f"  {b:>4} | {mp.nstr(c['sym'],6):>10} {mp.nstr(c['std'],6):>10} "
              f"{mp.nstr(c['alt'],6):>10} | {PAULI_MAP[b]:>8} {mp.nstr(E,5):>9}")

    print("\n  Binding forms across the nuclide ladder [MeV]:")
    print(f"  {'iso':>5} {'A':>3} {'AME':>9} {'B_std':>9} {'B_pauli-ch':>11} "
          f"{'B_qCLT':>9} {'B_qCLT_fac':>11} {'err_pauli':>10}")
    print("  " + "-" * 80)
    for iso, Z, N, ame in _LADDER:
        s = binding_summary(Z, N)
        amev = float(ame)
        err = amev / s["B_pauli_ch"] if s["B_pauli_ch"] else float("inf")
        flag = "  <- complete-graph overbinds" if (Z + N > 8 and err < 0.5) else ""
        print(f"  {iso:>5} {Z+N:>3} {amev:>9.3f} {s['B_std']:>9.3f} "
              f"{s['B_pauli_ch']:>11.3f} {s['B_qCLT']:>9.3f} "
              f"{s['B_qCLT_fac']:>11.3f} {err:>10.4f}{flag}")
    print("\n  Symbolic route example — B_pauli_ch(³He) exact:")
    print("   ", sp.nsimplify(channel_binding(2, 1, PAULI_MAP, "symbolic"), rational=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
