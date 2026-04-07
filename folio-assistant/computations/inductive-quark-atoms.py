#!/usr/bin/env python3
"""
Inductive atom construction at the quark level with full
Gröbner--Shirshov witness — knot particle tables with signed coefficients.

Builds atoms one particle at a time from vacuum:
  1. Start with identity (vacuum)
  2. Add quarks/electrons one at a time
  3. Gröbner--Shirshov-reduce at each step
  4. Track all inputs/outputs with knot identification
  5. Write witness JSON with commit SHA

Negative coefficients = prior interaction inputs (causal history)
Positive coefficients = observable outputs (the atom/particle)

Usage:
    cd folio-assistant/computations
    python3 inductive-quark-atoms.py

    # For specific atom only:
    python3 inductive-quark-atoms.py protium

    # For all atoms up to tritium:
    python3 inductive-quark-atoms.py all

Output:
    inductive-quark-atoms.witness.json
    inductive-quark-atoms.lean.txt
"""

import math
import json
import sys
import time
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from hecke_division import HeckeDivision, HeckeElement
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import *

# ══════════════════════════════════════════════════════════════
# SETUP
# ══════════════════════════════════════════════════════════════

div = HeckeDivision(q_val=q)
HA = q - qi
s_skein = q**0.5 - qi**0.5
z_markov = 1.0 / (q**0.5 + qi**0.5)
kappa = M_E_MEV / 3  # = E_CROSS * M_E_MEV / (3 * E_CROSS), simplified

# Commit SHA for provenance
try:
    COMMIT_SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    COMMIT_SHA = "unknown"


# ══════════════════════════════════════════════════════════════
# CROSSING COEFFICIENTS
# ══════════════════════════════════════════════════════════════

# Crossing coefficients (c, d) for T(c,d) = c·σ + d·𝟙.
# From the Hecke inverse relation σ⁻¹ = σ − (q − q⁻¹):
#   uu (pp) → c = 1,  d = 0
#   dd (nn) → c = 1,  d = −HA
#   ud (pn) → c = 1,  d = −HA/2
c_dd = 1.0
d_dd = -HA
c_ud = 1.0
d_ud = -HA / 2.0

def sigma(i):
    return HeckeElement({(i,): 1.0})

def crossing_element(type_i, type_j, gen):
    """Crossing between quark/particle types at generator sigma_gen.

    From the Hecke inverse relation σ⁻¹ = σ − (q − q⁻¹):
      u–u: σ (positive crossing, c=1, d=0)
      d–d: σ⁻¹ (negative crossing, c=1, d=−HA)
      u–d: ½(σ+σ⁻¹) (mixed crossing, c=1, d=−HA/2)
      any–electron: σ (Hopf link)
    """
    if type_i == type_j == 'u':
        return sigma(gen)
    elif type_i == type_j == 'd':
        return HeckeElement({(gen,): c_dd, (): d_dd})
    elif set([type_i, type_j]) == set(['u', 'd']):
        return HeckeElement({(gen,): c_ud, (): d_ud})
    else:
        return sigma(gen)  # Hopf link


# ══════════════════════════════════════════════════════════════
# KNOT IDENTIFICATION
# ══════════════════════════════════════════════════════════════

def word_paper(w):
    """Convert word tuple to paper notation."""
    if not w:
        return "1 (identity)"
    return " . ".join(f"sigma_{i}" for i in w)

def knot_type(w):
    """Identify the knot/link type of a reduced word."""
    n = len(w)
    if n == 0:
        return "unknot"
    if n == 1:
        return f"T_{{2,1}} at sigma_{w[0]}"
    if len(set(w)) == 1:
        return f"T_{{2,{n}}} at sigma_{w[0]}"
    if n % 2 == 0:
        pair = w[:2]
        if all(w[2*j:2*j+2] == pair for j in range(n // 2)):
            if abs(pair[0] - pair[1]) == 1:
                return f"T_{{3,{n//2}}} at sigma_{pair[0]}.sigma_{pair[1]}"
    return f"degree-{n} reduced braid"


# ══════════════════════════════════════════════════════════════
# ATOM DEFINITIONS
# ══════════════════════════════════════════════════════════════

ATOMS = {
    "proton": {
        "strands": ["u_r", "u_g", "d_b"],
        "types":   ["u",   "u",   "d"],
        "label":   "proton = B_3(u, u, d)",
        "paper":   "def:categorical-proton",
    },
    "neutron": {
        "strands": ["u_r", "d_g", "d_b"],
        "types":   ["u",   "d",   "d"],
        "label":   "neutron = B_3(u, d, d)",
        "paper":   "def:categorical-neutron",
    },
    "protium": {
        "strands": ["u_r", "u_g", "d_b", "e-"],
        "types":   ["u",   "u",   "d",   "e"],
        "label":   "protium = B_3(u,u,d) + e-",
        "paper":   "rem:hydrogen-knot-structure",
    },
    "deuterium": {
        "strands": ["u_r", "u_g", "d_b", "u_r2", "d_g2", "d_b2", "e-"],
        "types":   ["u",   "u",   "d",   "u",    "d",    "d",    "e"],
        "label":   "deuterium = B_3(u,u,d) + B_3(u,d,d) + e-",
        "paper":   "def:stable-nucleus",
    },
    "tritium": {
        "strands": ["u_r", "u_g", "d_b", "u_r2", "d_g2", "d_b2",
                     "u_r3", "d_g3", "d_b3", "e-"],
        "types":   ["u",   "u",   "d",   "u",    "d",    "d",
                     "u",   "d",   "d",   "e"],
        "label":   "tritium = B_3(u,u,d) + 2*B_3(u,d,d) + e-",
        "paper":   "def:stable-nucleus",
    },
    "he3_nucleus": {
        "strands": ["u_r", "u_g", "d_b", "u_r2", "u_g2", "d_b2",
                     "u_r3", "d_g3", "d_b3"],
        "types":   ["u",   "u",   "d",   "u",    "u",    "d",
                     "u",   "d",   "d"],
        "label":   "He-3 nucleus = 2*B_3(u,u,d) + B_3(u,d,d)",
        "paper":   "def:stable-nucleus",
    },
}


# ══════════════════════════════════════════════════════════════
# BUILD ATOM WITH FULL WITNESS
# ══════════════════════════════════════════════════════════════

def build_atom(name):
    """Build atom inductively with complete witness."""
    spec = ATOMS[name]
    strands = spec["strands"]
    types = spec["types"]
    A = len(strands)

    print(f"\n{'='*70}")
    print(f"  {spec['label']}")
    print(f"  Paper: {spec['paper']}")
    print(f"  Strands: {A}, Algebra: H_{A}(q)")
    print(f"{'='*70}\n")

    elem = HeckeElement.identity()
    total_E = 0.0
    total_H = 0
    total_YB = 0
    steps = []
    t0 = time.time()

    for k in range(1, A):
        print(f"  Step {k}: add {strands[k]} ({types[k]}) at position {k}")
        step_crossings = []

        for i in range(k):
            pair = f"{types[i]}-{types[k]}"
            cx = crossing_element(types[i], types[k], i)

            # Multiply and reduce
            product = elem * cx
            product_red, log = div.reduce(product)
            summary = div.summarize_log(log)
            E = summary.get('hecke_energy_change', 0)
            total_E += E
            total_H += summary['hecke_steps']
            total_YB += summary['yang_baxter_steps']

            if summary['hecke_steps'] > 0 or summary['yang_baxter_steps'] > 0:
                print(f"    ({i},{k}) {strands[i]}-{strands[k]} ({pair}): "
                      f"{summary['hecke_steps']}H+{summary['yang_baxter_steps']}YB, E={E:.6f}")
            else:
                print(f"    ({i},{k}) {strands[i]}-{strands[k]} ({pair}): NF (no reduction)")

            elem = product_red
            step_crossings.append({
                "pair": f"({i},{k})", "types": pair,
                "hecke": summary['hecke_steps'],
                "yb": summary['yang_baxter_steps'],
                "energy": E,
            })

        steps.append({"k": k, "strand": strands[k], "crossings": step_crossings})

    elapsed = time.time() - t0
    tr = div.markov_trace(elem, A)

    # Build knot particle table
    table = []
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        if abs(c) < 1e-10:
            continue
        table.append({
            "sign": "INPUT" if c < 0 else "OUTPUT",
            "coefficient": c,
            "word": word_paper(w),
            "knot": knot_type(w),
            "degree": len(w),
        })

    # Print table
    print(f"\n  KNOT PARTICLE TABLE:")
    print(f"  {'Sign':>8} {'Coeff':>12} {'Knot':>30} {'Word':>40}")
    print(f"  {'-'*95}")
    for row in table:
        if abs(row['coefficient']) > 0.001:
            print(f"  {row['sign']:>8} {row['coefficient']:>+12.6f} "
                  f"{row['knot']:>30} {row['word']:>40}")

    net = sum(c for c in elem.terms.values())
    print(f"\n  Net coefficient: {net:+.6f}")
    print(f"  Markov trace ({A}-strand): {tr:.10f}")
    print(f"  Hecke energy: {total_E:.6f}")
    print(f"  Time: {elapsed:.1f}s")

    return {
        "name": name,
        "label": spec["label"],
        "paper": spec["paper"],
        "strands": strands,
        "types": types,
        "A": A,
        "steps": steps,
        "knot_table": table,
        "n_terms": elem.n_terms(),
        "total_hecke_energy": total_E,
        "total_hecke_steps": total_H,
        "total_yb_steps": total_YB,
        "markov_trace": tr,
        "ln_markov_trace": math.log(abs(tr)) if tr != 0 else None,
        "net_coefficient": net,
        "elapsed_s": elapsed,
    }, elem


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "all"

    if target == "all":
        names = list(ATOMS.keys())
    elif target in ATOMS:
        names = [target]
    else:
        print(f"Unknown atom: {target}")
        print(f"Available: {', '.join(ATOMS.keys())}")
        sys.exit(1)

    print(f"Inductive quark-level atom construction")
    print(f"Commit: {COMMIT_SHA[:8]}")
    print(f"q = {q:.10f}")

    results = {}
    elements = {}
    for name in names:
        data, elem = build_atom(name)
        results[name] = data
        elements[name] = elem

    # Q-values
    if "neutron" in results and "proton" in results:
        print(f"\n{'='*70}")
        print(f"  FREE NEUTRON Q-VALUE")
        print(f"{'='*70}")
        net_n = results["neutron"]["net_coefficient"]
        net_p = results["proton"]["net_coefficient"]
        Q_net = abs(net_n - net_p) * kappa
        print(f"  |net_n - net_p| x kappa = {Q_net:.5f} MeV  (exp: 0.782)")
        print(f"  error: {(Q_net - 0.782) / 0.782 * 100:+.1f}%")

    if "tritium" in results and "he3_nucleus" in results:
        print(f"\n{'='*70}")
        print(f"  TRITIUM BETA DECAY Q-VALUE")
        print(f"{'='*70}")
        net_3H = results["tritium"]["net_coefficient"]
        net_3He = results["he3_nucleus"]["net_coefficient"]
        Q_net = abs(net_3H - net_3He) * kappa
        E_3H = results["tritium"]["total_hecke_energy"]
        E_3He = results["he3_nucleus"]["total_hecke_energy"]
        Q_lnE = abs(math.log(E_3H / E_3He)) * kappa if E_3He > 0 else 0
        print(f"  |net_3H - net_3He| x kappa = {Q_net:.5f} MeV")
        print(f"  |ln(E_3H/E_3He)| x kappa  = {Q_lnE:.5f} MeV")
        print(f"  Q_exp = {Q_TRITIUM_MEV:.5f} MeV")

    # Witness
    witness = {
        "computation": "inductive-quark-atoms",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "commit_sha": COMMIT_SHA,
        "script": str(Path(__file__).name),
        "parameters": {
            "q": q, "q_inv": qi, "HA": HA,
            "s_skein": s_skein, "z_markov": z_markov,
            "kappa_MeV": kappa,
        },
        "ideal": {
            "R1_hecke": f"sigma_i^2 = {HA:.10f} * sigma_i + 1",
            "R2_yang_baxter": "sigma_i . sigma_{i+1} . sigma_i = sigma_{i+1} . sigma_i . sigma_{i+1}",
            "R3_far_comm": "sigma_i . sigma_j = sigma_j . sigma_i for |i-j| >= 2",
        },
        "atoms": results,
    }

    out = Path(__file__).parent / "inductive-quark-atoms.witness.json"
    with open(out, "w") as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\nWitness: {out}")
    print(f"  Commit: {COMMIT_SHA}")
