#!/usr/bin/env python3
"""
bounded_degree_coordination_genericity_probe — the coordination number the plateau
"implies" is manufactured by the choice of inputs, and this measures by how much.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Follows #6332 (the channel arity gap)
and #6338 (which made the per-bond energies trustworthy past the float64 floor).

## The tempting move, and why it needs a guard before anyone makes it

`QOU.Mass.CoordinationSaturation` gives the bounded-degree law

    B/A = ε · k / 2                     (`bounded_degree_saturates`, sorry-free)

and the corpus now has *derived* per-bond energies `ε = E₀·log(1/f_bond)` — not
fitted, closed q₀ expressions, and after #6338 confirmed to 31 digits rather than 16:

    ε_pp = 2.0507…   ε_pn = 2.8332…   ε_nn = 3.7978…   MeV

So one can invert the observed nuclear plateau for `k` and ask what coordination
number the framework "implies". Do that with `ε_pn` against the bulk volume
coefficient and it lands near **11.1**, which is within 8 % of the fcc/hcp
close-packing number **12** — a result that would look like the framework
predicting close packing.

**It is not one, and this probe is the guard.** Inverting an empirical anchor for a
parameter is a FIT (AGENTS.md: "a Δ_λ obtained by inverting the AME anchors is still
a fit"). The only thing such an inversion can legitimately do is a *plausibility
check*: does the implied `k` land in the physically possible range at all, or is it
absurd? An absurd `k` would be a scope-(a) negative against the framing. A plausible
`k` is **not** evidence for it.

And the check has teeth only if the plausible range is hard to hit. So the actual
measurement here is GENERICITY, in the shape of
`computations/qbeta/sleak_offset_genericity_check.py`: over the choices a reasonable
person could make — which `ε` (three derived bond types, plus their mixtures at the
N=Z composition) and which empirical target (the observed `B/A` peak, or the
Bethe–Weizsäcker volume coefficient) — what RANGE of `k` is reachable? If the
reachable range covers the physically plausible window, then hitting 12 is a
property of the choice, not of the framework.

## Scope

Scope **(a)**, and specifically a NEGATIVE-guard probe: it proposes nothing, wires
nothing, and derives nothing. Its output is the width of a window. Nothing here says
the bounded-degree law is wrong — `bounded_degree_saturates` is correct as stated;
what is measured is that inverting it for `k` does not constrain anything.

NO FLOAT64: mpmath `mpf` at 50 dps; `float` appears nowhere. Empirical values are
read as exact decimal strings. Proton pin.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from itertools import product  # noqa: E402

import mpmath as mp  # noqa: E402

from closed_form_tau_M import markov_z, hecke_h  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50


def constants():
    """The same substrate quantities `derived_bond_graph_binding` uses, read at the
    50-digit pin (not the float64 `q_parameter.Q` — see bean qou-vsqh)."""
    from codata_constants import M_E_MEV as me
    q0 = Q_MP
    h = q0 - 1 / q0
    me = me if isinstance(me, mp.mpf) else mp.mpf(str(me))
    z = q0**3 / (q0**2 + 1)                       # convention D
    delta = flavor_split_leading(q0)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    f = {"pp": z, "nn": z - h, "pn": z - h * (mp.mpf(1) / 2 - delta / 4)}
    eps = {k: E0 * mp.log(1 / v) for k, v in f.items()}
    return q0, E0, f, eps


# Empirical targets a reasonable person might invert against. Exact decimal strings.
TARGETS = {
    "B/A peak (62Ni)": mp.mpf("8.7945"),      # 545.259126 / 62
    "B/A peak (56Fe)": mp.mpf("8.7902"),      # 492.253892 / 56
    "a_V (Bethe-Weizsacker volume coeff)": mp.mpf("15.75"),
    "a_V low bracket": mp.mpf("15.5"),
    "a_V high bracket": mp.mpf("15.8"),
}

# Physically plausible coordination numbers for a 3D packing.
K_MIN, K_MAX = mp.mpf(2), mp.mpf(12)          # chain-like .. fcc/hcp close packing


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0, E0, f, eps = constants()

    print("bounded_degree_coordination_genericity_probe")
    print("=" * 78)
    print(f"q0 (50-digit proton pin) = {fmt(q0, 20)}")
    print(f"E_0 = m_e/(q0(q0-1))     = {fmt(E0, 12)} MeV")
    print("Derived per-bond energies eps = E_0*log(1/f_bond)  [MeV], NOT fitted:")
    for k in ("pp", "pn", "nn"):
        print(f"    f_{k} = {fmt(f[k], 12):>16}    eps_{k} = {fmt(eps[k], 12)}")
    print()

    # The N=Z mixtures a complete graph or a chain would actually present, as
    # bond-count-weighted means -- these are the "reasonable" epsilon choices
    # beyond the three pure types.
    #   complete graph at N=Z:  C(Z,2) pp + Z*N pn + C(N,2) nn
    #   chain at N=Z (canonical p...pn...n): (Z-1) pp + 1 pn + (N-1) nn
    A_MIX = 20
    Z = N = A_MIX // 2
    n_pp, n_pn, n_nn = Z * (Z - 1) // 2, Z * N, N * (N - 1) // 2
    eps_complete = (n_pp * eps["pp"] + n_pn * eps["pn"] + n_nn * eps["nn"]) / (
        n_pp + n_pn + n_nn)
    c_pp, c_pn, c_nn = Z - 1, 1, N - 1
    eps_chain = (c_pp * eps["pp"] + c_pn * eps["pn"] + c_nn * eps["nn"]) / (
        c_pp + c_pn + c_nn)
    EPS_CHOICES = {
        "eps_pp (pure)": eps["pp"],
        "eps_pn (pure)": eps["pn"],
        "eps_nn (pure)": eps["nn"],
        f"complete-graph mean (A={A_MIX}, N=Z)": eps_complete,
        f"chain mean (A={A_MIX}, N=Z)": eps_chain,
        "unweighted mean of the three": (eps["pp"] + eps["pn"] + eps["nn"]) / 3,
    }
    print(f"Bond-count-weighted eps at A={A_MIX}, N=Z:")
    print(f"    complete graph ({n_pp} pp, {n_pn} pn, {n_nn} nn) -> "
          f"{fmt(eps_complete, 10)} MeV")
    print(f"    chain          ({c_pp} pp, {c_pn} pn, {c_nn} nn) -> "
          f"{fmt(eps_chain, 10)} MeV")
    print()

    print("THE INVERSION.  bounded_degree_saturates:  B/A = eps*k/2  =>  k = 2*(B/A)/eps")
    print("  This inverts an EMPIRICAL anchor for a parameter, i.e. it is a FIT.")
    print("  It is reported only as a plausibility check: is the implied k inside the")
    print(f"  physically possible window [{int(K_MIN)}, {int(K_MAX)}] for a 3D packing?")
    print()
    print(f"{'eps choice':>38} {'target':>38} {'implied k':>11} {'in window?':>11}")
    ks = []
    for (en, ev), (tn, tv) in product(EPS_CHOICES.items(), TARGETS.items()):
        k = 2 * tv / ev
        inw = K_MIN <= k <= K_MAX
        ks.append((k, en, tn, inw))
        print(f"{en:>38} {tn:>38} {fmt(k, 6):>11} {('yes' if inw else 'NO'):>11}")
    print()

    kv = [k for k, _e, _t, _i in ks]
    kmin, kmax = min(kv), max(kv)
    n_in = sum(1 for _k, _e, _t, i in ks if i)
    # How much of the plausible window does the reachable range cover?
    lo, hi = max(kmin, K_MIN), min(kmax, K_MAX)
    covered = (hi - lo) / (K_MAX - K_MIN) if hi > lo else mp.mpf(0)

    print("GENERICITY — the actual measurement")
    print("-" * 78)
    print(f"  combinations tried                    : {len(ks)}"
          f"  ({len(EPS_CHOICES)} eps x {len(TARGETS)} targets)")
    print(f"  implied k, full range                 : {fmt(kmin, 6)} .. {fmt(kmax, 6)}")
    print(f"  landing inside the plausible window   : {n_in}/{len(ks)}")
    print(f"  fraction of window [{int(K_MIN)},{int(K_MAX)}] reachable : "
          f"{fmt(covered * 100, 5)} %")
    print()

    # Named temptations, checked explicitly so nobody has to re-derive them.
    print("  The two matches someone will notice, and what they are worth:")
    for en, tn, target_k, label in [
        ("eps_pn (pure)", "a_V (Bethe-Weizsacker volume coeff)", mp.mpf(12),
         "fcc/hcp close packing"),
        ("eps_pn (pure)", "B/A peak (62Ni)", mp.mpf(6), "simple-cubic / in-plane"),
    ]:
        k = 2 * TARGETS[tn] / EPS_CHOICES[en]
        rel = abs(k - target_k) / target_k * 100
        print(f"    {en} vs {tn}")
        print(f"      k = {fmt(k, 8)}   vs {label} k = {int(target_k)}"
              f"   ({fmt(rel, 4)} % away)")
    print()

    verdict_generic = covered > mp.mpf("0.5")
    print("VERDICT")
    print("-" * 78)
    if verdict_generic:
        print(f"  The reachable k range covers {fmt(covered*100, 4)} % of the plausible")
        print("  window, so landing near ANY particular lattice coordination number --")
        print("  12 for fcc/hcp, 6 for simple cubic, 8 for bcc -- is a property of")
        print("  WHICH eps and WHICH empirical target were chosen, not of the")
        print("  framework.  The inversion does not constrain k, and a 'k = 12,")
        print("  therefore close packing' reading is NUMEROLOGY.  Guard, not a result.")
    else:
        print(f"  The reachable k range covers only {fmt(covered*100, 4)} % of the")
        print("  plausible window.  That does NOT make the inversion a derivation --")
        print("  it is still a fit -- but the narrowness is worth recording, because")
        print("  a tight window is what would make the plausibility check informative.")
    print()
    print("  What this does NOT say: bounded_degree_saturates is correct as stated,")
    print("  and nothing here argues against bounded coordination.  What is measured")
    print("  is only that INVERTING it for k is uninformative at the current inputs.")
    print()
    print("  What WOULD be informative: a k derived from the substrate -- from the")
    print("  braid word's own geometry or from a packing argument inside the")
    print("  framework -- and then COMPARED to the plateau.  That is derive-then-")
    print("  check; the above is check-then-derive, which is the forbidden direction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
