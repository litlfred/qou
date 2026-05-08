#!/usr/bin/env python3
"""
Task 3: Tower/mass ratio investigation
Task 4: Neutrino consistency check (formerly "Neutrino mass from L₋
        channel" — see audit §2·F, P1.6, 2026-05-01)

The corrected Markov trace gives:
  tr_M(proton) ≈ -0.012
  tr_M(neutron) ≈ -0.134
  ratio |tr_M(n)|/|tr_M(p)| ≈ 11.6

CODATA: m_n/m_p = 1.00138

The tower mechanism must amplify these traces through iterated
self-interaction (Φ_q composition tower) for the proton/neutron
investigation in Task 3.

Task 4 (neutrino sector) was previously framed as deriving
m_ν via tower iteration on V̂ = z² (the L₋ channel). Per the
2026-05-01 deep audit (§2·F), that derivation is **incorrect by
construction**: the neutrino is the unknot K_{0,1}, J_ν(q) = 1,
bare-knot mass = 0. The knot-derived "predicted m_ν" appearing
below is therefore *empirical confirmation* that the L₋ channel
does NOT yield a neutrino mass; it is preserved as a diagnostic
of the unknot identity, not a prediction.

The categorical prediction for m_ν is the vacuum-drag formula:

    m_ν ∝ μ₀ · (q - 1)

reported in §"Alternative: vacuum drag formula" below.

See:
  docs/audits/2026-05-01-math-framework-deep-audit.md §2·F
  docs/audits/2026-05-01-math-framework-workplan.md P1.6
  content/quantum-observable-universe/descartes-universe/neutrino-knot.md
"""

import json
import math
from pathlib import Path
from datetime import datetime, timezone

DIR = Path(__file__).parent

from q_parameter import Q as q0, Q_INV as qi0, HA as HA0, Q_ERR, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

z = 1.0 / (math.sqrt(q0) + 1.0 / math.sqrt(q0))

# ── Load nucleon NF from beta-decay-energy-scale witness ─────────
esc_w = json.loads((DIR / "beta-decay-energy-scale.witness.json").read_text())
esc_nf = esc_w.get("nucleon_nf", {})

# NF basis traces (corrected: e⁻ = z³, not hz²+z)
TR_M = [1.0, z, z, z**2, z**2, z**3]
NF_NAMES = ["ν", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]

# Map witness keys to NF indices
KEY_MAP = {"ν": 0, "H\u2070": 1, "H\u00b9": 2, "L\u208a": 3, "L\u208b": 4, "e\u207b": 5}

def nf_to_vec(nf_dict):
    """Convert witness NF dict to 6-element vector."""
    return [nf_dict.get(k, 0.0) for k in KEY_MAP]

p_vec = nf_to_vec(esc_nf.get("proton", {}))
n_vec = nf_to_vec(esc_nf.get("neutron", {}))

tr_p = sum(c * t for c, t in zip(p_vec, TR_M))
tr_n = sum(c * t for c, t in zip(n_vec, TR_M))

print("=" * 70)
print("  TASK 3: TOWER/MASS RATIO INVESTIGATION")
print("=" * 70)

print(f"\n─── Corrected Markov traces (z³ for e⁻) ───")
print(f"  tr_M(e⁻) = z³ = {z**3:.10f}")
print(f"  z = {z:.10f}")

print(f"\n  Proton NF:  {[f'{c:+.6f}' for c in p_vec]}")
print(f"  Neutron NF: {[f'{c:+.6f}' for c in n_vec]}")
print(f"  TR_M basis: {[f'{t:.6f}' for t in TR_M]}")

print(f"\n  tr_M(proton)  = {tr_p:+.10f}")
print(f"  tr_M(neutron) = {tr_n:+.10f}")
print(f"  |tr_M(n)|/|tr_M(p)| = {abs(tr_n)/abs(tr_p):.4f}")
print(f"  CODATA m_n/m_p      = {M_N_MEV/M_P_MEV:.6f}")

# ── Decompose the trace by basis element ────────────────────────
print(f"\n─── Trace decomposition by basis element ───")
print(f"  {'Basis':<6} {'c_p':>10} {'c_n':>10} {'tr_M(b)':>10} {'c_p×tr':>12} {'c_n×tr':>12}")
print("  " + "-" * 62)
for i in range(6):
    print(f"  {NF_NAMES[i]:<6} {p_vec[i]:>+10.6f} {n_vec[i]:>+10.6f} {TR_M[i]:>10.6f} {p_vec[i]*TR_M[i]:>+12.8f} {n_vec[i]*TR_M[i]:>+12.8f}")
print(f"  {'TOTAL':<6} {'':>10} {'':>10} {'':>10} {tr_p:>+12.8f} {tr_n:>+12.8f}")

# ── Tower mechanism ──────────────────────────────────────────────
print(f"\n─── Tower mechanism analysis ───")

# The mass formula uses the tower Φ_q^(k)(V̂) where V̂ is the vertex volume
# Mass = lim_{k→∞} |Φ_q^(k)(V̂)| × μ₀
# where Φ_q(x) = (q^x - q^{-x})/(q - q^{-1}) = [x]_q evaluated at x=V̂
# and μ₀ is the Planck mass scale

# For the proton, the dominant NF term is σ₁ with coefficient ≈ +0.998
# Its vertex volume is V̂ = z × c + d where c,d come from the NF coefficient
# In the simplest case: V̂_proton ≈ z × 0.998 ≈ 0.498 (close to z)

V_hat_p = abs(tr_p)  # Single-level: mass ∝ |tr_M|
V_hat_n = abs(tr_n)

print(f"  Single-level (no tower):")
print(f"    |tr_M(p)| = {V_hat_p:.10f}")
print(f"    |tr_M(n)| = {V_hat_n:.10f}")
print(f"    ratio = {V_hat_n/V_hat_p:.4f} (need 1.0014)")

# Tower iteration: Φ_q(x) = [x]_q = (q^x - q^{-x})/(q - q^{-1})
def phi_q(x, qq=q0):
    """q-integer function: Φ_q(x) = (q^x - q^{-x})/(q - q^{-1})"""
    return (qq**x - qq**(-x)) / (qq - 1.0/qq)

# Iterate tower
print(f"\n  Tower iteration Φ_q^(k)(V̂):")
print(f"  {'k':>3} {'Φ^k(|tr_p|)':>16} {'Φ^k(|tr_n|)':>16} {'ratio':>10}")
print("  " + "-" * 48)

v_p = V_hat_p
v_n = V_hat_n
for k in range(15):
    ratio = v_n / v_p if v_p != 0 else float('inf')
    print(f"  {k:>3} {v_p:>16.10f} {v_n:>16.10f} {ratio:>10.6f}")
    if abs(v_p) > 1e10 or abs(v_n) > 1e10:
        print("  ... (diverging)")
        break
    v_p_new = phi_q(v_p)
    v_n_new = phi_q(v_n)
    v_p = v_p_new
    v_n = v_n_new

# ── Alternative: use net instead of tr_M ─────────────────────────
print(f"\n─── Alternative: tower on net (not tr_M) ───")
net_p = sum(p_vec)
net_n = sum(n_vec)
print(f"  net(p) = {net_p:.10f}")
print(f"  net(n) = {net_n:.10f}")

v_p = net_p
v_n = net_n
print(f"\n  {'k':>3} {'Φ^k(net_p)':>16} {'Φ^k(net_n)':>16} {'ratio':>10}")
print("  " + "-" * 48)
for k in range(15):
    ratio = v_n / v_p if v_p != 0 else float('inf')
    print(f"  {k:>3} {v_p:>16.10f} {v_n:>16.10f} {ratio:>10.6f}")
    if abs(v_p) > 1e10 or abs(v_n) > 1e10:
        print("  ... (diverging)")
        break
    v_p = phi_q(v_p)
    v_n = phi_q(v_n)

# ═══════════════════════════════════════════════════════════════
# TASK 4: NEUTRINO CONSISTENCY CHECK (was: "Neutrino mass from L₋ channel")
#
# Per audit §2·F (2026-05-01) and P1.6 of the math-framework workplan,
# the neutrino is the unknot K_{0,1} with J_ν(q) = 1 and bare-knot
# mass exactly 0. Any L₋-channel-tower path that emits a numerical
# m_ν is buggy by the unknot identity. This section keeps the L₋
# computation as a *diagnostic*: the resulting "predicted m_ν" is
# the empirical signature of the wrong-channel framing — it cannot
# match observation because the underlying physics says the answer
# must be 0 in the bare-knot limit.
#
# The categorical prediction for m_ν is the vacuum-drag formula
# below (§"Alternative: vacuum drag formula").
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  TASK 4: NEUTRINO CONSISTENCY CHECK (audit §2·F, P1.6)")
print("=" * 70)
print()
print("  Per audit §2·F: the neutrino is the unknot K_{0,1}.")
print("  J_ν(q) = 1, bare-knot mass = 0.")
print("  The L₋-channel-tower path below is a diagnostic, NOT a")
print("  prediction — its output is the empirical signature of")
print("  the wrong-channel framing. The categorical prediction is")
print("  the vacuum-drag formula in the next section.")

# Diagnostic: the L₋ channel does NOT correspond to the neutrino.
# V̂_L₋ = z² is preserved as the L₋ channel value (used elsewhere in
# the witness chain), but it does NOT model the neutrino, which is
# the unknot with V̂_ν = 1 (trivial vertex volume).
V_hat_Lminus = z**2  # was mislabelled V̂_ν; this is the L₋ channel
V_hat_nu_true = 1.0  # unknot K_{0,1} vertex volume (trivial)
V_hat_e = z**3       # electron vertex volume (corrected)

print(f"\n  L₋ channel:  V̂_L₋ = z² = {V_hat_Lminus:.10f} (NOT the neutrino)")
print(f"  Unknot K_{{0,1}}: V̂_ν = 1.0 (categorical neutrino value)")
print(f"  Electron:    V̂_e  = z³ = {V_hat_e:.10f}")

# L₋-channel diagnostic tower (kept for empirical-signature purposes
# only; this iteration does NOT yield m_ν per the unknot identity).
print(f"\n  L₋-channel diagnostic tower (NOT a neutrino-mass prediction):")
print(f"  {'k':>3} {'Φ^k(V̂_L₋)':>16} {'Φ^k(V̂_e)':>16} {'L₋/e ratio':>12}")
print("  " + "-" * 50)

v_Lminus = V_hat_Lminus
v_e = V_hat_e
ratio_history = []
for k in range(20):
    ratio = v_Lminus / v_e if v_e != 0 else float('inf')
    ratio_history.append(ratio)
    print(f"  {k:>3} {v_Lminus:>16.10f} {v_e:>16.10f} {ratio:>12.8f}")
    if abs(v_Lminus) > 1e10 or abs(v_e) > 1e10:
        print("  ... (diverging)")
        break
    v_Lminus = phi_q(v_Lminus)
    v_e = phi_q(v_e)

# Diagnostic readout: this is what the buggy framing would have
# called m_ν; here it is named explicitly as the L₋/e ratio so no
# downstream consumer treats it as a neutrino-mass prediction.
if len(ratio_history) > 5:
    converged_ratio = ratio_history[-1]
    print(f"\n  L₋/e converged ratio ≈ {converged_ratio:.8f}")
    print(f"  (Naïve L₋ channel \"would-be m_ν\" ≈ "
          f"{converged_ratio * M_E_MEV * 1e6:.4f} eV — diagnostic only,")
    print(f"   NOT the categorical neutrino-mass prediction.)")

# ── Categorical prediction: mass from vacuum drag ────────────────
# The correct categorical prediction: bare-knot mass is 0 (unknot),
# observed mass arises from vacuum drag on the brane substrate.
print(f"\n─── Categorical prediction: vacuum-drag formula ───")
print(f"  Bare-knot mass (unknot): 0 MeV (exact, from J_ν = 1)")
print(f"  Vacuum-drag correction: m_ν ∝ μ₀ · (q - 1)")
print(f"  ℏ_q = 1 - q⁻¹ = {HBAR_Q:.10f}")
print(f"  q - 1 = {q0 - 1:.10f}")
print(f"  Candidate vacuum-drag prefactors:")
print(f"    m_ν ≈ m_e · ℏ_q²   = {M_E_MEV * HBAR_Q**2 * 1e6:.4f} eV")
print(f"    m_ν ≈ m_e · ℏ_q³   = {M_E_MEV * HBAR_Q**3 * 1e6:.4f} eV")
print(f"    m_ν ≈ m_e · (q-1)³ = {M_E_MEV * (q0-1)**3 * 1e6:.4f} eV")
print(f"  Observed upper bound: m_ν < 0.8 eV (KATRIN 2022)")
print(f"  Cosmological bound:   Σm_ν < 0.12 eV (Planck 2018)")

# ── Write witness ────────────────────────────────────────────────
witness = {
    "computation": "tower-mass-neutrino",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q0": q0,
    "corrected_traces": {
        "tr_M_proton": tr_p,
        "tr_M_neutron": tr_n,
        "ratio_abs": abs(tr_n) / abs(tr_p),
        "codata_mn_mp": M_N_MEV / M_P_MEV,
    },
    # Neutrino sector — see audit §2·F (2026-05-01) and P1.6.
    # Bare-knot mass = 0 by the unknot identity; the L₋-channel
    # diagnostic below is preserved for empirical-signature purposes
    # only and is NOT a categorical neutrino-mass prediction.
    "neutrino": {
        "categorical_bare_mass_MeV": 0.0,
        "categorical_basis": "unknot K_{0,1}, J_nu(q) = 1, no crossings",
        "L_minus_channel_diagnostic": {
            "V_hat_L_minus": V_hat_Lminus,
            "V_hat_e": V_hat_e,
            "L_minus_over_e_ratio_history": ratio_history[:10],
            "warning": (
                "L_minus channel is NOT the neutrino sector; this "
                "tower iteration is a diagnostic of the wrong-channel "
                "framing per audit §2·F, not a m_nu prediction."
            ),
        },
        "vacuum_drag_prediction": {
            "form": "m_nu ∝ mu_0 · (q - 1)",
            "candidates_eV": {
                "m_e_times_hbar_q2": M_E_MEV * HBAR_Q**2 * 1e6,
                "m_e_times_hbar_q3": M_E_MEV * HBAR_Q**3 * 1e6,
                "m_e_times_q_minus_1_cubed": M_E_MEV * (q0 - 1)**3 * 1e6,
            },
            "katrin_upper_bound_eV": 0.8,
            "planck_cosmological_bound_eV": 0.12,
        },
    },
}
out = DIR / "tower-mass-neutrino.witness.json"
out.write_text(json.dumps(witness, indent=2))
print(f"\n  Witness written to {out.name}")
print("=" * 70)
