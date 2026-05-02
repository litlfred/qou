#!/usr/bin/env python3
"""
Pair production: γγ → e⁻ + e⁺

Computes Gröbner--Shirshov normal forms in H₃(q) for:

  γ   = σ₀           (photon  = single Hopf crossing)
  γγ  = σ₀²          → (q−q⁻¹)σ₀ + 𝟏  via Hecke relation
  e⁻  = σ₀σ₁σ₀       (electron = trefoil = Garside Δ₃)
  e⁺  = σ₀⁻¹σ₁⁻¹σ₀⁻¹  (positron = mirror trefoil = Δ₃⁻¹)

Using σᵢ⁻¹ = σᵢ − (q−q⁻¹)  (exact from the Hecke relation).

The pair-creation threshold (PDG: 1.022 MeV = 2mₑ) is recovered as:

  Δ(pair) = NF_net(e⁻) + NF_net(e⁺) − NF_net(γγ)
  E_threshold = Δ(pair) × E₀

Energy scale E₀ is imported from beta-decay-energy-scale.witness.json.

Usage:
    python3 pair-production-nf.py
"""

import math, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
q_sym = sp.Symbol('q', positive=True)

from q_parameter import Q as q0, Q_INV as qi0, HA as HA0, E_CROSS, HBAR_Q
from experimental_constants import M_E_MEV

try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    SHA = "unknown"

# ── Energy scale from free-neutron-decay calibration ────────────
_esc_path = Path(__file__).parent / "beta-decay-energy-scale.witness.json"
with _esc_path.open() as _f:
    _esc = json.load(_f)
E0 = _esc["energy_scales"]["E0_from_net_MeV"]

# ── Iwahori--Hecke algebra symbols ─────────────────────────────────────
HA_sym  = q_sym - 1 / q_sym          # q − q⁻¹  (symbolic)
HA_num  = HA0                         # numeric at q₀

PARTICLE_KNOT = {
    ():        ("ν",  "𝟏",      "unknot (0₁)"),
    (0,):      ("σ₀", "σ₀",     "virtual (ℓ=1)"),
    (1,):      ("σ₁", "σ₁",     "virtual (ℓ=1)"),
    (0, 1):    ("L₊", "σ₀σ₁",   "Hopf link"),
    (1, 0):    ("L₋", "σ₁σ₀",   "Hopf link"),
    (0, 1, 0): ("e⁻", "σ₀σ₁σ₀", "trefoil (3₁)"),
}

def ws(w):
    if not w:
        return "𝟏"
    parts = []
    for g in w:
        if g >= 0:
            parts.append(f"σ_{g}")
        else:
            parts.append(f"σ_{-g-1}⁻¹")
    return "·".join(parts)

def pn(w):
    return PARTICLE_KNOT.get(w, ("?", "?", "?"))[0]

def eval_q0(c):
    if isinstance(c, (int, float)):
        return float(c)
    return float(c.subs(q_sym, q0))


# ══════════════════════════════════════════════════════════════
#  GRÖBNER REDUCTION (same rules as free-neutron-decay.py)
# ══════════════════════════════════════════════════════════════

def reduce_verbose(terms_dict, label=""):
    """
    Reduce a Hecke element using the three Gröbner--Shirshov relations.
    Negative generator index encodes σᵢ⁻¹ via pre-substitution
    (caller expands inverses first).
    Returns (reduced_terms, step_counts).
    """
    terms = {w: sp.expand(c) for w, c in terms_dict.items() if c != 0}
    hecke = yb = fc = 0
    step = 0

    print(f"\n  ┌─ REDUCTION of {label}")
    print(f"  │  Input: {len(terms)} terms")
    for w, c in sorted(terms.items(), key=lambda x: (len(x[0]), x[0])):
        print(f"  │    {eval_q0(c):+.8f} · {ws(w)}")
    print("  │")

    changed = True
    while changed:
        changed = False
        new_terms = {}

        for word, coeff in terms.items():
            if coeff == 0:
                continue
            done = False

            # R1: Hecke  σᵢ² → (q−q⁻¹)σᵢ + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos+1] and word[pos] >= 0:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos+2:]
                    w1 = pre + (i,) + suf
                    w2 = pre + suf
                    c1 = sp.expand(coeff * HA_sym)
                    c2 = sp.expand(coeff)
                    new_terms[w1] = sp.expand(new_terms.get(w1, 0) + c1)
                    new_terms[w2] = sp.expand(new_terms.get(w2, 0) + c2)
                    step += 1; hecke += 1
                    print(f"  │  R1 Hecke #{step:3d}:  "
                          f"{eval_q0(coeff):+.6f}·{ws(word)}  →  "
                          f"{eval_q0(c1):+.6f}·{ws(w1)} + {eval_q0(c2):+.6f}·{ws(w2)}")
                    done = changed = True; break

            if done:
                continue

            # R3: Yang-Baxter  σᵢσᵢ₊₁σᵢ → σᵢ₊₁σᵢσᵢ₊₁  (orient to lex-smaller)
            for pos in range(len(word) - 2):
                a, b, c_g = word[pos], word[pos+1], word[pos+2]
                if (a == c_g and a >= 0 and b >= 0 and abs(a - b) == 1):
                    new_trip = (b, a, b)
                    old_trip = (a, b, a)
                    if new_trip < old_trip:
                        nw = word[:pos] + new_trip + word[pos+3:]
                        new_terms[nw] = sp.expand(new_terms.get(nw, 0) + coeff)
                        step += 1; yb += 1
                        print(f"  │  R3 YB    #{step:3d}:  "
                              f"{eval_q0(coeff):+.6f}·{ws(word)}  →  "
                              f"{eval_q0(coeff):+.6f}·{ws(nw)}")
                        done = changed = True; break

            if not done:
                new_terms[word] = sp.expand(new_terms.get(word, 0) + coeff)

        terms = {w: sp.expand(c) for w, c in new_terms.items() if c != 0}

    print("  │")
    print(f"  │  NF ({hecke} Hecke + {yb} YB = {step} steps):")
    net = 0.0
    results = []
    for w, c in sorted(terms.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        net += v
        name = pn(w)
        tag = f"  [{name}]" if name else ""
        print(f"  │    {v:+.10f} · {ws(w)}{tag}")
    print(f"  │  net = {net:+.10f}")
    print("  └─")
    return terms, net, {"hecke": hecke, "yb": yb, "total": step}


# ══════════════════════════════════════════════════════════════
#  EXPAND INVERSES  σᵢ⁻¹ → σᵢ − (q−q⁻¹)
# ══════════════════════════════════════════════════════════════

def expand_inverse_word(word):
    """
    Given a word with negative indices encoding σᵢ⁻¹ (index = −i−1),
    expand each σᵢ⁻¹ → σᵢ − (q−q⁻¹) and return a terms dict.
    """
    terms = {(): sp.Integer(1)}   # start with identity

    for g in word:
        new_terms = {}
        if g >= 0:
            # positive generator: left-multiply all existing words by σ_g
            for w, c in terms.items():
                nw = w + (g,)
                new_terms[nw] = sp.expand(new_terms.get(nw, 0) + c)
        else:
            # negative generator σᵢ⁻¹ = σᵢ − (q−q⁻¹)
            i = -g - 1
            for w, c in terms.items():
                # +σᵢ part
                nw1 = w + (i,)
                new_terms[nw1] = sp.expand(new_terms.get(nw1, 0) + c)
                # −(q−q⁻¹) part
                nw2 = w
                new_terms[nw2] = sp.expand(
                    new_terms.get(nw2, 0) - c * HA_sym)
        terms = {w: sp.expand(c) for w, c in new_terms.items() if c != 0}

    return terms


# ══════════════════════════════════════════════════════════════
#  MAIN COMPUTATION
# ══════════════════════════════════════════════════════════════

print("=" * 65)
print("  PAIR PRODUCTION NF:  γγ → e⁻ + e⁺")
print("=" * 65)
print(f"\n  q₀  = {q0:.10f}")
print(f"  HA  = q−q⁻¹ = {HA_num:.10f}")
print(f"  E₀  = {E0:.6f} MeV  (calibrated on n→p beta decay)")
print(f"  mₑ  = {M_E_MEV:.6f} MeV  (CODATA 2022)")
print(f"  2mₑ = {2*M_E_MEV:.6f} MeV  (pair threshold)")

# ── (1) Photon  γ = σ₀ ───────────────────────────────────────
print("\n─── (1) γ = σ₀  (single photon / Hopf generator) ───")
gamma_terms = {(0,): sp.Integer(1)}
_, net_gamma, steps_gamma = reduce_verbose(gamma_terms, "γ = σ₀")

# ── (2) Two photons  γγ = σ₀² ────────────────────────────────
print("\n─── (2) γγ = σ₀²  (two-photon vertex) ───")
gamma2_terms = {(0, 0): sp.Integer(1)}
nf_gamma2, net_gamma2, steps_gamma2 = reduce_verbose(
    gamma2_terms, "γγ = σ₀²")

# ── (3) Electron  e⁻ = σ₀σ₁σ₀ ───────────────────────────────
print("\n─── (3) e⁻ = σ₀σ₁σ₀  (trefoil = Garside Δ₃) ───")
eminus_terms = {(0, 1, 0): sp.Integer(1)}
nf_eminus, net_eminus, steps_eminus = reduce_verbose(
    eminus_terms, "e⁻ = σ₀σ₁σ₀")

# ── (4) Positron  e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ ─────────────────────────
# Encode inverses as negative indices: σ₀⁻¹ = index -1, σ₁⁻¹ = index -2
print("\n─── (4) e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹  (mirror trefoil = Δ₃⁻¹) ───")
print("  Expanding inverses: σᵢ⁻¹ = σᵢ − (q−q⁻¹)")
eplus_raw = expand_inverse_word((-1, -2, -1))   # σ₀⁻¹σ₁⁻¹σ₀⁻¹
print(f"  After inverse expansion: {len(eplus_raw)} unreduced terms")
for w, c in sorted(eplus_raw.items(), key=lambda x: (len(x[0]), x[0])):
    print(f"    {eval_q0(c):+.8f} · {ws(w)}")

nf_eplus, net_eplus, steps_eplus = reduce_verbose(
    eplus_raw, "e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹")

# ── (5) Energy budget ─────────────────────────────────────────
print("\n" + "=" * 65)
print("  ENERGY BUDGET")
print("=" * 65)

delta_pair = net_eminus + net_eplus - net_gamma2
E_pair_MeV = delta_pair * E0
E_threshold = 2.0 * M_E_MEV

print(f"\n  NF_net(e⁻)   = {net_eminus:+.10f}")
print(f"  NF_net(e⁺)   = {net_eplus:+.10f}")
print(f"  NF_net(γγ)   = {net_gamma2:+.10f}")
print()
print(f"  Δ(pair) = NF(e⁻) + NF(e⁺) − NF(γγ)")
print(f"          = {net_eminus:+.6f} + {net_eplus:+.6f} − ({net_gamma2:+.6f})")
print(f"          = {delta_pair:+.10f}")
print()
print(f"  E_threshold = Δ(pair) × E₀")
print(f"              = {delta_pair:.8f} × {E0:.6f} MeV")
print(f"              = {E_pair_MeV:.6f} MeV")
print()
print(f"  Observed 2mₑ = {E_threshold:.6f} MeV")
print(f"  Ratio (predicted / observed) = {E_pair_MeV / E_threshold:.6f}")
print(f"  Residual = {abs(E_pair_MeV - E_threshold):.6f} MeV  "
      f"({abs(E_pair_MeV - E_threshold)/E_threshold*100:.3f}%)")

# ── (6) Per-term NF comparison table ─────────────────────────
print("\n─── NF term-by-term comparison ───")
header = f"  {'Term':6s} | {'e⁻':>14s} | {'e⁺':>14s} | {'Δ(e⁻+e⁺)':>14s} | {'γγ':>14s}"
print(header)
print("  " + "-" * (len(header) - 2))

all_words = sorted(
    set(nf_eminus) | set(nf_eplus) | set(nf_gamma2),
    key=lambda x: (len(x), x)
)
for w in all_words:
    ve = eval_q0(nf_eminus.get(w, 0))
    vp = eval_q0(nf_eplus.get(w, 0))
    vg = eval_q0(nf_gamma2.get(w, 0))
    name = pn(w)
    print(f"  {name:6s} | {ve:+14.8f} | {vp:+14.8f} | "
          f"{ve+vp:+14.8f} | {vg:+14.8f}")


# ══════════════════════════════════════════════════════════════
#  WITNESS JSON
# ══════════════════════════════════════════════════════════════

def nf_to_json(nf_dict, net):
    out = {}
    for w, c in sorted(nf_dict.items(), key=lambda x: (len(x[0]), x[0])):
        key = "identity" if not w else "".join(f"s{g}" for g in w)
        out[key] = {
            "word": ws(w),
            "particle": pn(w),
            "at_q0": eval_q0(c),
        }
    out["_net"] = net
    return out


def nf_to_symbolic_q_form(nf_dict):
    """Capture symbolic ℚ(q) coefficients of NF terms (P2.5).

    Each Gröbner--Shirshov NF term carries a sympy expression in
    q_sym; this returns the simplified algebraic-side polynomials
    in q alongside the numerical at-q_0 values exposed elsewhere.
    """
    out = {}
    for w, c in sorted(nf_dict.items(), key=lambda x: (len(x[0]), x[0])):
        key = "identity" if not w else "".join(f"s{g}" for g in w)
        out[key] = {
            "word": ws(w),
            "particle": pn(w),
            "coefficient_polynomial_q": str(sp.simplify(c)),
        }
    return out

witness = {
    "name": "pair-production-nf",
    "description": (
        "Gröbner--Shirshov NF for γγ → e⁻ + e⁺ pair production in H₃(q). "
        "Photon γ = σ₀, e⁻ = σ₀σ₁σ₀ (trefoil), "
        "e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror trefoil). "
        "Threshold energy Δ(pair) × E₀ compared to 2mₑ = 1.022 MeV."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q0": q0,
        "HA": HA_num,
        "E0_MeV": E0,
        "m_e_MeV": M_E_MEV,
        "threshold_MeV": E_threshold,
    },
    "particle_braid_words": {
        "gamma":   "σ₀",
        "gamma2":  "σ₀²",
        "e_minus": "σ₀σ₁σ₀  (trefoil, Garside Δ₃)",
        "e_plus":  "σ₀⁻¹σ₁⁻¹σ₀⁻¹  (mirror trefoil, Δ₃⁻¹)",
    },
    "nf_gamma":  nf_to_json(gamma_terms, net_gamma),
    "nf_gamma2": nf_to_json(nf_gamma2,   net_gamma2),
    "nf_eminus": nf_to_json(nf_eminus,   net_eminus),
    "nf_eplus":  nf_to_json(nf_eplus,    net_eplus),
    # P2.5: symbolic ℚ(q) forms of the Gröbner--Shirshov NF
    # coefficients.  Each NF term is a sympy expression in
    # q_sym = sp.Symbol('q', positive=True); the at_q0 values
    # above are obtained by .subs(q, q_0) on these symbolic
    # forms.  The symbolic form is the algebraic truth; the
    # numerical value is its specialisation.  Sample particle
    # is e⁻ (trefoil σ₀σ₁σ₀) — the same reduce_verbose path
    # generates the symbolic NF for γ, γγ, e⁺ as well.
    "symbolic_q_form": {
        "engine": "sympy",
        "q_symbol": "q (sp.Symbol('q', positive=True))",
        "h_symbol_definition": "h = q - 1/q  (Hecke parameter)",
        "sample_particle": "e_plus",
        "nf_eplus_polynomials_q": nf_to_symbolic_q_form(nf_eplus),
        "nf_gamma2_polynomials_q": nf_to_symbolic_q_form(nf_gamma2),
        "note": (
            "Symbolic ℚ(q) NF coefficients after Gröbner--Shirshov "
            "reduction.  e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror trefoil) and "
            "γγ = σ₀² are exposed because their NFs carry "
            "non-trivial Laurent polynomial coefficients in q "
            "(via σᵢ⁻¹ → σᵢ − (q−q⁻¹) and σᵢ² → (q−q⁻¹)σᵢ + 1).  "
            "e⁻ = σ₀σ₁σ₀ is already in NF (coefficient 1) and is "
            "available numerically in nf_eminus.  Numerical values "
            "at q_0 for every term are in nf_gamma / nf_gamma2 / "
            "nf_eminus / nf_eplus above."
        ),
    },
    "energy_budget": {
        "net_eminus":          net_eminus,
        "net_eplus":           net_eplus,
        "net_gamma2":          net_gamma2,
        "delta_pair":          delta_pair,
        "E_pair_predicted_MeV": E_pair_MeV,
        "E_threshold_2me_MeV": E_threshold,
        "ratio":               E_pair_MeV / E_threshold,
        "residual_MeV":        abs(E_pair_MeV - E_threshold),
        "residual_percent":    abs(E_pair_MeV - E_threshold) / E_threshold * 100,
    },
    "reduction_steps": {
        "gamma":  steps_gamma,
        "gamma2": steps_gamma2,
        "eminus": steps_eminus,
        "eplus":  steps_eplus,
    },
}

out_path = Path(__file__).with_suffix(".witness.json")
out_path.write_text(json.dumps(witness, indent=2))
print(f"\n  Witness written to {out_path.name}")
