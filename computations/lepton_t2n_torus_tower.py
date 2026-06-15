#!/usr/bin/env python3
"""lepton_t2n_torus_tower.py — group-action map of the lepton T(2,n) torus
tower (EXPLORATORY, audit-only).

Maps the 2-strand T(2,n) torus-knot tower that the framework attaches to the
charged leptons (electron=T(2,3), muon=T(2,5), tau=T(2,7), T(2,9) saturation),
following the merged census
(docs/audits/2026-06-01-knot-operator-census-group-actions.md) and the
inter-nucleon linked-channel audit
(docs/audits/2026-06-01-inter-nucleon-linked-channel.md, the H_2(q) Wenzl
Markov-trace machinery reused verbatim).

Computes, RAW (no tuning to any lepton mass ratio, charge, or any h^k):
  1. The tower group-action table per T(2,n): the H_2(q) Markov trace
     tr_M(sigma_1^n) = J_{T(2,n)}(q) symbolic in q AND at q0 @ 60 dps,
     writhe (=n), genus ((n-1)/2), cyclic Z_n symmetry, the B_2=Z -> H_2 ->
     Z_2 statistics (gcd(2,n) components: odd=knot=fermion, even=link=boson).
     The T(2,n) trace closed form is derived and cross-checked vs the census
     Hopf form tr_M(sigma_1^2) = 1 + (q-1)/sqrt(q).
  2. The S_5-equivariance selection: Z_n -> S_5 exists iff S_5 has an
     order-n element, n in {1,2,3,4,5,6}; restricting to odd n>=3 gives
     {3,5} = electron + muon (group-theoretic verification).
  3. Mass-ratio RAW comparison: the direct operator-level Markov-trace ratio
     |tr_M(T(2,n))| / |tr_M(T(2,3))| vs CODATA m_mu/m_e, m_tau/m_e --
     FALSIFICATION references reported raw with miss factors. The production
     lepton-mass path is the Skein/Kashaev-volume identity
     Vol(4_1)/hbar_q^2 (calibrated to CODATA), NOT the direct trace ratio:
     this script does NOT reproduce or wire that; it reports the RAW direct
     ratio and the known ~10^3x miss as the fit-flag check.
  4. The U(1)_framing ladder: writhe(T(2,n))=n != 0 for every lepton, so the
     framing factor q^{n.c} is a per-lepton charge-ladder candidate. Compared
     RAW to lepton electric charge (all -1) -- a constant, not a ladder.

NO FIT. Every numeric is a falsification reference reported raw.
Audit doc: docs/audits/2026-06-02-lepton-t2n-torus-tower.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from math import gcd
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402

# Canonical substrate q0 (proton-anchored, single source of truth) and CODATA
# lepton mass ratios, imported -- NOT hardcoded -- so this script tracks the
# 2026-05-28 proton-anchor re-pin and avoids the compute-audit P31 scanner.
from q_parameter import Q_MP as Q0  # noqa: E402  proton-pinned substrate
from q_parameter import VOL_4_1_MP as Vol_4_1  # noqa: E402  SnapPy Vol(4_1)
from experimental_constants import (  # noqa: E402
    MU_OVER_E as CAL2_MU_E,           # CODATA m_mu/m_e (falsification ref)
    TAU_OVER_E as CAL_TAU_E,          # CODATA m_tau/m_e (falsification ref)
)

START = time.monotonic()
mp.mp.dps = 60

# Promote the imported experimental ratios to mpmath at the working precision.
CAL2_MU_E = mp.mpf(str(CAL2_MU_E))
CAL_TAU_E = mp.mpf(str(CAL_TAU_E))


# ---------------------------------------------------------------------------
# H_2(q) Wenzl Markov trace (reused from inter_nucleon_linked_channel.py).
# Two 1-dim blocks: (2) [sigma_1 -> q] and (1,1) [sigma_1 -> -q^{-1}].
#   tr_M(sigma_1^k) = W_(2) q^k + W_(1,1) (-q^{-1})^k
# Wenzl weights fixed by the two Markov axioms (tr_M(1)=1, tr_M(b sigma)=z tr_M(b)):
#   W_(2)   = (q^{3/2} + q + 1)/(q^3 + q^2 + q + 1)
#   W_(1,1) = (q^3 + q^2 - q^{3/2})/(q^3 + q^2 + q + 1)
# ---------------------------------------------------------------------------
def z_factor(q):
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def wenzl_weights(q):
    denom = q**3 + q**2 + q + 1
    W2 = (q ** mp.mpf("1.5") + q + 1) / denom
    W11 = (q**3 + q**2 - q ** mp.mpf("1.5")) / denom
    return W2, W11


def trM_sigma1_pow(q, k):
    """tr_M(sigma_1^k) in H_2(q), Wenzl Jones-Markov normalisation."""
    W2, W11 = wenzl_weights(q)
    return W2 * q**k + W11 * (-1 / q) ** k


def trM_hopf_census_form(q):
    """Census Hopf closed form tr_M(sigma_1^2) = 1 + (q-1)/sqrt(q)."""
    return 1 + (q - 1) / mp.sqrt(q)


# Symbolic trace in q (verify the closed-form structure independent of q0).
def trM_symbolic(k):
    qs = sp.symbols("q", positive=True)
    rt = sp.sqrt(qs)
    denom = qs**3 + qs**2 + qs + 1
    W2 = (rt**3 + qs + 1) / denom
    W11 = (qs**3 + qs**2 - rt**3) / denom
    expr = W2 * qs**k + W11 * (-1 / qs) ** k
    # sp.cancel combines over the common denominator (a targeted rational
    # normal form) without the heavyweight sp.simplify the compute-audit
    # P16 rule flags; the symbolic-vs-numeric assertion cross-checks it.
    return sp.cancel(expr)


# ---------------------------------------------------------------------------
# S_5 element orders (the equivariance selection).
# Orders of elements of S_n = lcm of the parts of each partition of n.
# ---------------------------------------------------------------------------
def partitions(n):
    if n == 0:
        yield []
        return
    for first in range(n, 0, -1):
        for rest in partitions(n - first):
            if not rest or first >= rest[0]:
                yield [first] + rest


def lcm(parts):
    out = 1
    for p in parts:
        out = out * p // gcd(out, p)
    return out


def element_orders(n):
    return sorted({lcm(p) for p in partitions(n)})


# ---------------------------------------------------------------------------
LEPTON_TOWER = [
    (3, "electron", "e-"),
    (5, "muon", "mu-"),
    (7, "tau", "tau-"),
    (9, "T(2,9) ghost", "(saturation)"),
    (11, "T(2,11) ghost", "(genus 5, excluded)"),
]

w = WitnessBuilder(
    "lepton-t2n-torus-tower", engine="python+mpmath", start_time=START
)
w.set_description(
    "Engine: python+mpmath (60 dps numeric) with sympy for the symbolic q "
    "trace cross-check. "
    "EXPLORATORY group-action map of the lepton T(2,n) torus tower: H_2(q) "
    "Markov trace J_{T(2,n)}(q) (symbolic + @ q0 60dps), writhe=n, genus="
    "(n-1)/2, cyclic Z_n, B_2->H_2->Z_2 fermion/boson statistics; S_5-"
    "equivariance selection n in {3,5}; RAW direct-trace mass-ratio "
    "falsification comparison (miss factors, fit-flags); U(1)-framing ladder "
    "q^{n.c}. All RAW; no tuning to any lepton mass ratio, charge, or h^k."
)
w.set_audit_only("docs/audits/2026-06-02-lepton-t2n-torus-tower.md")
w.add_parameter("q0", str(Q0))
w.add_parameter("dps", mp.mp.dps)
w.add_parameter("Vol_4_1_ref", str(Vol_4_1))
w.add_parameter("CODATA_m_mu_over_m_e", str(CAL2_MU_E))
w.add_parameter("CODATA_m_tau_over_m_e", str(CAL_TAU_E))

# --- 1. The tower group-action table ---
z = z_factor(Q0)
w.add_data("markov_z_at_q0", str(z))

tower = {}
for n, name, sym in LEPTON_TOWER:
    components = gcd(2, n)
    tr_q0 = trM_sigma1_pow(Q0, n)
    tower[f"T(2,{n})"] = {
        "particle": name,
        "symbol": sym,
        "braid_word": f"sigma_1^{n}",
        "B_n": "B_2 = Z (one generator sigma_1)",
        "H_n": "H_2(q), blocks (2),(1,1)",
        "S_n_quotient": "S_2 = Z_2",
        "writhe": n,
        "genus": (n - 1) // 2,
        "cyclic_symmetry": f"Z_{n}",
        "gcd_2_n": components,
        "components": components,
        "knot_or_link": "knot (1-cpt)" if components == 1 else "link (2-cpt)",
        "statistics": "fermion (odd n)" if n % 2 == 1 else "boson (even n)",
        "tr_M_at_q0": str(tr_q0),
        "abs_tr_M_at_q0": str(mp.fabs(tr_q0)),
    }
w.add_data("lepton_tower_table", tower)

# Symbolic traces + symbolic vs numeric cross-check (T(2,3) and T(2,5)).
sym3 = trM_symbolic(3)
sym5 = trM_symbolic(5)
w.add_data("trM_T2_3_symbolic", str(sym3))
w.add_data("trM_T2_5_symbolic", str(sym5))
# evaluate symbolic at q0 and compare to mpmath
qs = sp.symbols("q", positive=True)
sym3_num = mp.mpf(str(sp.N(sym3.subs(qs, sp.Float(str(Q0), 60)), 55)))
w.add_assertion(
    "trM_T2_3_symbolic_eq_numeric", str(sym3_num),
    str(trM_sigma1_pow(Q0, 3)), tolerance=mp.mpf("1e-45"),
)

# Census Hopf cross-check: tr_M(sigma_1^2) Wenzl == census closed form.
hopf_wenzl = trM_sigma1_pow(Q0, 2)
hopf_census = trM_hopf_census_form(Q0)
w.add_data("trM_hopf_wenzl_at_q0", str(hopf_wenzl))
w.add_data("trM_hopf_census_at_q0", str(hopf_census))
w.add_assertion(
    "trM_hopf_wenzl_eq_census", str(hopf_wenzl), str(hopf_census),
    tolerance=mp.mpf("1e-50"),
)

# writhe = n and genus = (n-1)/2 (structural, derived).
for n, _, _ in LEPTON_TOWER:
    w.add_assertion(f"writhe_T2_{n}_eq_n", tower[f"T(2,{n})"]["writhe"], n)
    w.add_assertion(
        f"genus_T2_{n}_eq_n_minus_1_over_2",
        tower[f"T(2,{n})"]["genus"], (n - 1) // 2,
    )

# fermion (odd) / boson (even) statistics from gcd(2,n) (sanity: all leptons odd).
for n, _, _ in LEPTON_TOWER:
    w.add_assertion(
        f"components_T2_{n}_eq_gcd_2_n",
        tower[f"T(2,{n})"]["components"], gcd(2, n),
    )

# --- 2. The S_5-equivariance selection ---
orders_S5 = element_orders(5)
w.add_data("S5_element_orders", orders_S5)
w.add_assertion(
    "S5_orders_eq_1_to_6", str(orders_S5), str([1, 2, 3, 4, 5, 6])
)
# odd n>=3 admissible iff n in S5 orders -> {3,5}
admissible = [n for n in [3, 5, 7, 9, 11] if n in orders_S5]
w.add_data("S5_equivariant_odd_n", admissible)
w.add_assertion("S5_equivariant_selection_eq_3_5", str(admissible), str([3, 5]))
# n=7 (tau) explicitly NOT S5-equivariant (no order-7 element in S5)
w.add_data("tau_n7_in_S5_orders", 7 in orders_S5)
w.add_assertion("tau_n7_not_S5_equivariant", 7 in orders_S5, False)

# --- 3. Mass-ratio RAW comparison (falsification references, fit-flagged) ---
abs_tr3 = mp.fabs(trM_sigma1_pow(Q0, 3))   # electron
abs_tr5 = mp.fabs(trM_sigma1_pow(Q0, 5))   # muon (T(2,5) candidate)
abs_tr7 = mp.fabs(trM_sigma1_pow(Q0, 7))   # tau
ratio_mu_e_direct = abs_tr5 / abs_tr3
ratio_tau_e_direct = abs_tr7 / abs_tr3
miss_mu = CAL2_MU_E / ratio_mu_e_direct
miss_tau = CAL_TAU_E / ratio_tau_e_direct
mass_ratio = {
    "method": "DIRECT operator-level |tr_M(T(2,n))| / |tr_M(T(2,3))| in H_2(q)",
    "is_production_path": False,
    "production_path_note": (
        "Production reads m_mu/m_e from the Skein/Kashaev identity "
        "Vol(4_1)/hbar_q^2 (calibrated to CODATA, conj:lepton-mass-tower-"
        "canonical). The direct trace ratio below is NOT that path -- it is "
        "the RAW operator-level ratio, reported as a falsification reference."
    ),
    "ratio_mu_e_direct": str(ratio_mu_e_direct),
    "CODATA_mu_e": str(CAL2_MU_E),
    "miss_factor_mu": str(miss_mu),
    "ratio_tau_e_direct": str(ratio_tau_e_direct),
    "CODATA_tau_e": str(CAL_TAU_E),
    "miss_factor_tau": str(miss_tau),
    "fit_flag": "NONE -- no coupling tuned; both ratios miss CODATA by ~10^2-10^3x",
}
w.add_data("mass_ratio_raw_comparison", mass_ratio)
# Assert the miss is large (the operator ratio is NOT a covert fit to CODATA).
w.add_assertion(
    "direct_mu_e_ratio_misses_codata_by_gt_100x",
    bool(miss_mu > 100), True,
)

# --- 4. The U(1)_framing ladder q^{n.c} ---
# writhe(T(2,n)) = n != 0 for every lepton -> live framing factor q^{n.c}.
# At observable level Im(q0)=0 (CLAUDE.md), so q^{n.c} is a real factor.
framing_c1 = {}
for n, name, _ in LEPTON_TOWER:
    framing_c1[f"T(2,{n})"] = {
        "particle": name, "writhe": n,
        "framing_q_pow_n_c1_at_q0": str(Q0 ** n),  # c = 1 (SET, not fitted)
    }
w.add_data("u1_framing_ladder_c1", framing_c1)
w.add_data("lepton_electric_charge_all", -1)
w.add_caveat(
    "U(1)-framing ladder verdict: writhe(T(2,n)) = n is nonzero and "
    "STRICTLY INCREASING across the lepton tower (3,5,7,9), so the framing "
    "factor q^{n.c} is a per-lepton LADDER (monotone in generation), NOT a "
    "constant. But the lepton ELECTRIC CHARGE is the SAME (-1) for e, mu, "
    "tau -- a constant. So writhe -> electric charge is a CATEGORY MISMATCH "
    "(monotone ladder vs constant); the framing U(1) does NOT reproduce "
    "electric charge. The framing ladder DOES track generation number "
    "(n=2k+1 for generation k), which is the cyclic-symmetry index Z_n, NOT "
    "a gauge charge. No coupling c is tuned (c=1 set); writhe -> Y remains "
    "undefined, consistent with the inter-nucleon linked-channel audit "
    "(misses PDG split by ~305x at c=1)."
)
w.add_caveat(
    "Mass-ratio fit-flag: the DIRECT operator-level Markov-trace ratio "
    "|tr_M(T(2,5))|/|tr_M(T(2,3))| misses CODATA m_mu/m_e by ~10^3x raw "
    "(reported). The PRODUCTION lepton-mass map is the Skein/Kashaev-volume "
    "identity Vol(4_1)/hbar_q^2, which is CALIBRATED to CODATA via CAL-2 "
    "(conj:lepton-mass-tower-canonical, Phase 3 finding) -- it is a "
    "Kashaev q->1 LIMIT identity, NOT a q0 operator ratio. This script does "
    "NOT reproduce or wire that calibrated path; it reports the RAW direct "
    "ratio so the ~10^3x gap is visible as the catch (a coupling chosen to "
    "close it would be the fit the discipline review catches). No fit."
)
w.add_caveat(
    "S_5-equivariance selection: Z_n -> S_5 exists iff S_5 has an order-n "
    "element. Element orders of S_5 = {1,2,3,4,5,6} (lcm of partition parts "
    "of 5). Odd n>=3 (forced by gcd(2,n)=1, fermion sector) gives exactly "
    "{3,5} = electron + muon. n=7 (tau) is genus-3<=4 so embeds "
    "topologically but its Z_7 has no order-7 element in S_5 -> "
    "symmetry-broken. This is a GROUP-THEORETIC FACT, not a fit; the "
    "2+1 generation split (symmetry-preserving e,mu + symmetry-broken tau) "
    "is what the framework predicts (rem:symmetry-preserving-leptons), "
    "compared RAW to the 3 observed generations (falsification ref)."
)

path = w.save()
elapsed = time.monotonic() - START
print(f"[lepton-t2n-torus-tower] wrote {path} in {elapsed:.2f}s")
print(f"  q0 = {Q0}")
print(f"  z(q0) = {z}")
print(f"  S_5 element orders = {orders_S5}  -> equivariant odd n>=3 = {admissible}")
print("  tower (n, particle, writhe, genus, Z_n, stats, |tr_M|):")
for n, name, _ in LEPTON_TOWER:
    t = tower[f"T(2,{n})"]
    print(f"    n={n:2d} {name:14s} w={t['writhe']:2d} g={t['genus']} "
          f"Z_{n}  {t['statistics']:14s} |tr_M|={float(mp.fabs(trM_sigma1_pow(Q0,n))):.6f}")
print(f"  Hopf cross-check: Wenzl={float(hopf_wenzl):.10f} census={float(hopf_census):.10f}")
print(f"  RAW direct ratio m_mu/m_e = {float(ratio_mu_e_direct):.6f}  "
      f"CODATA={float(CAL2_MU_E):.4f}  miss={float(miss_mu):.1f}x")
print(f"  RAW direct ratio m_tau/m_e = {float(ratio_tau_e_direct):.6f}  "
      f"CODATA={float(CAL_TAU_E):.4f}  miss={float(miss_tau):.1f}x")
