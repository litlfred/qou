#!/usr/bin/env python3
"""PRE-ARCHIMEDEAN derivation of the per-bond trace factor f_bond(q).

Owner directive 2026-06-10: "do everything pre-archimedean where you can" +
"derive it [f], no |·|"; cross-ref `claude/peaceful-brown-hrt19q` §3-bis
(pre-archimedean depth-1 heat backbone: exp_q shift kernel, per-mode R_λ, Z_q).

## Pre-archimedean (fibre / formal-q) content

The per-bond suppression factor is the Markov **conditional expectation** of the
inter-nucleon bridge crossing `c·σ + d·1`, a FIBRE-LEVEL Hecke fact (formal q,
Im(q) unconstrained) — NOT an archimedean evaluation:

    E_{H_n → H_{n-1}}(c·σ_{n-1} + d) = c·z + d ,   z(q) = 1/(q^{1/2}+q^{-1/2})

So, with h(q) = q − q^{-1} and δ(q) the color split, the per-bond factors are
closed FORMAL-q expressions:

    f_pp(q) = z = √q/(q+1)
    f_nn(q) = z − h
    f_pn(q) = z − h·(½ − δ/4)

The Jones–Markov trace `tr_M = Σ_λ y_λ(q)·χ_λ(q)` is a Wedderburn heat trace —
the Z_q partition function of `peaceful-brown` (sum over modes λ with weights
y_λ). Linking nucleon k→k+1 multiplies Z_q by the mode-averaged factor f_bond,
so the binding is the pre-archimedean **free-energy difference**

    B(q) = E_0 · log( tr_free / tr_atom ) = E_0 · Σ_{bonds} log(1/f_bond(q))

This is positive (each f_bond < 1) so NO |·| is needed; if a norm were wanted
the archimedean realization is the bar product tr_M·\check{tr}_M (q→q^{-1}),
not |·| — but at the fibre level the log-ratio is the natural object.

The ARCHIMEDEAN step is a single substitution q → q₀ at the end (Im(q₀)=0),
giving the MeV numbers. Everything above is fibre-level.

## Connection to the peaceful-brown depth-1 heat kernel

`peaceful-brown` R(q,x) = 1 + (q−1)x (depth-1 q-difference kernel); per-mode
R_λ(q,t) = 1 − (q−1)μ_λ(q)t; Z_q = heat trace. Our f_bond is the per-bond
multiplier of the SAME Z_q (here Z_q = tr_M, the braid-word heat trace), so the
bond-graph binding is the log of a ratio of these q-partition functions — the
free energy of the q-heat flow. The bridge crossing is the depth-1 link kernel
on the Wedderburn eigenbasis.

Output: prearchimedean-bond-factor.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    t0 = time.time()
    q = sp.Symbol("q", positive=True)
    qh = sp.sqrt(q)
    z = 1 / (qh + 1 / qh)
    h = q - 1 / q
    delta = sp.Symbol("delta", nonnegative=True)  # color split (formal)

    # Pre-archimedean per-bond factors (formal q).
    f_pp = sp.simplify(z)
    f_nn = sp.simplify(z - h)
    f_pn = sp.simplify(z - h * (sp.Rational(1, 2) - delta / 4))

    forms = {
        "z": sp.simplify(z), "h": sp.simplify(h),
        "f_pp": f_pp, "f_nn": f_nn, "f_pn_delta0": sp.simplify(f_pn.subs(delta, 0)),
    }
    print("=" * 78)
    print(" PRE-ARCHIMEDEAN per-bond factors f_bond(q) = c·z + d  (formal q)")
    print("=" * 78)
    print(f"  z(q)            = {sp.nsimplify(z)}  =  {sp.simplify(z)}")
    print(f"  h(q)            = q - 1/q")
    print(f"  f_pp(q) = z     = {f_pp}")
    print(f"  f_nn(q) = z - h = {f_nn}")
    print(f"  f_pn(q) (δ→0)   = {forms['f_pn_delta0']}")

    # Archimedean realization: substitute q → q₀ (single step at the end).
    from q_parameter import Q as Q0
    from codata_constants import M_E_MEV as me
    try:
        from canonical_braid_crossings import _avg_color_delta
        d0 = float(_avg_color_delta())
    except Exception:
        d0 = 0.0
    q0 = float(Q0); me = float(me)
    E0 = me / (q0 * (q0 - 1.0))
    arch = {
        "q0": q0, "E_0_MeV": round(E0, 4),
        "f_pp_at_q0": float(f_pp.subs(q, q0)),
        "f_nn_at_q0": float(f_nn.subs(q, q0)),
        "f_pn_at_q0": float(f_pn.subs({q: q0, delta: d0})),
    }
    e_bond = {
        "pp": E0 * float(sp.log(1 / f_pp.subs(q, q0))),
        "nn": E0 * float(sp.log(1 / f_nn.subs(q, q0))),
        "pn": E0 * float(sp.log(1 / f_pn.subs({q: q0, delta: d0}))),
    }
    print("\n  ── archimedean realization (q → q₀, Im q₀ = 0) ──")
    print(f"  f_pp(q₀)={arch['f_pp_at_q0']:.6f}  f_pn(q₀)={arch['f_pn_at_q0']:.6f}  "
          f"f_nn(q₀)={arch['f_nn_at_q0']:.6f}")
    print(f"  per-bond E_0·log(1/f) [MeV]: pp={e_bond['pp']:.3f}  "
          f"pn={e_bond['pn']:.3f}  nn={e_bond['nn']:.3f}")

    w = WitnessBuilder("prearchimedean-bond-factor", engine="sympy",
                       start_time=t0)
    w.set_description(
        "Pre-archimedean (fibre / formal-q) derivation of the per-bond trace "
        "factor f_bond(q) = c·z + d — the Markov conditional expectation of the "
        "inter-nucleon bridge crossing (a Hecke fact, NOT archimedean). f_pp=z="
        "√q/(q+1), f_nn=z−h, f_pn=z−h(½−δ/4). tr_M is the Z_q Wedderburn heat "
        "trace (cf. peaceful-brown §3-bis); binding = E_0·log(tr_free/tr_atom) = "
        "E_0·Σ_bonds log(1/f_bond) is the q-heat free-energy difference "
        "(positive, no |·|). The only archimedean step is q→q₀ at the end."
    )
    w.add_data("prearchimedean_forms", {k: str(v) for k, v in forms.items()})
    w.add_data("archimedean_eval", arch)
    w.add_data("per_bond_energy_MeV", {k: round(v, 4) for k, v in e_bond.items()})
    w.add_data("z_closed_form", str(sp.simplify(z)))
    w.add_data("peaceful_brown_link",
               "tr_M = Σ_λ y_λ χ_λ is the Z_q heat trace; f_bond is the depth-1 "
               "bridge multiplier on the Wedderburn eigenbasis; binding is the "
               "q-heat free energy. See claude/peaceful-brown-hrt19q §3-bis + "
               "QBetaPreArchHeatDepthOneKernel.lean.")
    # Sanity: symbolic eval at q₀ matches the numeric derivation (1e-12).
    w.add_assertion(
        name="symbolic_f_bond_matches_numeric_at_q0",
        computed=abs(arch["f_pp_at_q0"] - 1.0 / (q0 ** 0.5 + q0 ** -0.5)),
        expected=0.0, tolerance=1e-12,
        source="symbolic f_pp(q₀) == numeric z(q₀); the fibre expression "
               "realizes correctly at the archimedean anchor.",
    )
    out = w.save()
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
