#!/usr/bin/env python3
"""
Shell correction λ_shell from alpha-particle sub-link binding.

The alpha particle N(2,2) is the fundamental closed sub-link.
Its extra binding energy (beyond the sum of 2 protons + 2 neutrons)
gives the shell correction scale λ_shell.

λ_shell = Φ_q(N(2,2)) - 2·Φ_q(p) - 2·Φ_q(n)

where Φ_q = Σ log|V̂_i| is the quantum dilogarithm volume.

Run from repo root:
    python3 folio-assistant/computations/shell-correction-lambda.py

Output:
    folio-assistant/computations/shell-correction-lambda.witness.json
"""

import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from computations.hecke_engine import HeckeEngine

from q_parameter import Q_RAT_NUM, Q_RAT_DEN, Q, HBAR_Q, HBAR_Q_SQ
engine = HeckeEngine(q_num=Q_RAT_NUM, q_den=Q_RAT_DEN)
qr = engine.qr

q = Q
hbar_q = HBAR_Q
hbar_q_sq = HBAR_Q_SQ

print("=" * 60)
print("Shell correction λ_shell from alpha-particle sub-link")
print("=" * 60)
print(f"q = {q}")
print(f"ℏ_q = {hbar_q:.6f}")
print(f"ℏ_q² = {hbar_q_sq:.6f}")
print()

# ── Compute quantum dilogarithm volumes ──────────────────────────

def phi_q(p, n, force_exact=False):
    """Quantum dilogarithm volume Φ_q(N(p,n)) = Σ log|V̂_i|.

    force_exact: if True, uses exact ground-state search even for
    large A (up to 15000 orderings). Essential for magic nuclei
    where the heuristic ordering misses the alpha-cluster structure.
    """
    A = p + n
    if A <= 1:
        return 0.0  # single nucleon has no crossings

    # Use exact search for A <= 20 (binom(20,10) = 184,756 — feasible)
    max_ord = 200000 if (force_exact or A <= 20) else 5000
    ordering, method = engine.ground_state_ordering(p, n, max_orderings=max_ord)

    # Sum log|V̂_i| for all generators
    phi = 0.0
    for i in range(A - 1):
        v = float(qr.traced_volume(i, ordering))
        if v != 0:
            phi += math.log(abs(v))
    return phi, ordering, method

# ── Individual nucleon volumes ───────────────────────────────────

print("Individual nucleon volumes:")
# Single proton: trivial (no crossings)
phi_proton = 0.0
phi_neutron = 0.0
print(f"  Φ_q(p) = {phi_proton:.6f}  (single strand, no crossings)")
print(f"  Φ_q(n) = {phi_neutron:.6f}  (single strand, no crossings)")
print()

# ── Light nuclei ─────────────────────────────────────────────────

print("Light nucleus volumes:")
light_nuclei = [
    (1, 1, "²H (deuteron)"),
    (1, 2, "³H (tritium)"),
    (2, 1, "³He"),
    (2, 2, "⁴He (alpha)"),
    (2, 4, "⁶He"),
    (3, 3, "⁶Li"),
    (4, 4, "⁸Be"),
    (8, 8, "¹⁶O (doubly magic)"),
    (10, 10, "²⁰Ne"),
    (10, 20, "⁵⁰Ca (magic n=20)"),
]

# Remove duplicates
seen = set()
unique_nuclei = []
for p, n, name in light_nuclei:
    key = (p, n)
    if key not in seen:
        seen.add(key)
        unique_nuclei.append((p, n, name))

phi_values = {}
orderings = {}
for p, n, name in unique_nuclei:
    A = p + n
    t0 = time.time()
    phi, ordering, method = phi_q(p, n)
    elapsed = time.time() - t0
    phi_values[(p, n)] = phi
    orderings[(p, n)] = (ordering, method)

    # Binding energy in ℏ_q² units
    E_bind = phi / hbar_q_sq if hbar_q_sq != 0 else 0

    print(f"  {name:20s} ({p},{n}): Φ_q = {phi:+.6f}, "
          f"E_bind/ℏ_q² = {E_bind:+.2f}, {method}, {elapsed:.1f}s")

print()

# ── Alpha-particle shell correction ─────────────────────────────

phi_alpha = phi_values.get((2, 2), 0)
phi_deuteron = phi_values.get((1, 1), 0)

# λ_shell = extra binding of alpha beyond 2p + 2n
# Since individual nucleons have Φ = 0, λ_shell = Φ_q(alpha)
lambda_shell = phi_alpha / hbar_q_sq

# Alternatively: compare alpha to 2 deuterons
# 2 deuterons have Φ = 2 * Φ(deuteron)
lambda_vs_deuterons = (phi_alpha - 2 * phi_deuteron) / hbar_q_sq

print("Shell correction energy scale:")
print(f"  Φ_q(⁴He) = {phi_alpha:.6f}")
print(f"  λ_shell = Φ_q(⁴He)/ℏ_q² = {lambda_shell:.4f} (Skein units)")
print(f"  λ_shell vs 2 deuterons = {lambda_vs_deuterons:.4f} (Skein units)")
print()

# ── Magic number verification ────────────────────────────────────
# Check whether Skein polynomial factorizes at magic nuclei

print("Factorization test at magic numbers:")
magic_nuclei = [
    (2, 2, "⁴He", "doubly magic"),
    (8, 8, "¹⁶O", "doubly magic"),
]

for p, n, name, mtype in magic_nuclei:
    if (p, n) not in phi_values:
        continue
    A = p + n
    phi_nucleus = phi_values[(p, n)]
    n_alpha = min(p // 2, n // 2)  # max alpha clusters

    # If the nucleus factorizes into alpha clusters:
    # Φ(nucleus) ≈ n_alpha * Φ(alpha) + linking corrections
    phi_alpha_clusters = n_alpha * phi_alpha
    residual = phi_nucleus - phi_alpha_clusters

    print(f"  {name} ({p},{n}): {n_alpha} alpha clusters")
    print(f"    Φ_nucleus = {phi_nucleus:.6f}")
    print(f"    {n_alpha} × Φ_alpha = {phi_alpha_clusters:.6f}")
    print(f"    Residual = {residual:.6f} ({residual/phi_nucleus*100:.1f}%)")
    print()

# ── Assemble witness ─────────────────────────────────────────────

witness = {
    "computation": "shell-correction-lambda",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q": q,
    "hbar_q": hbar_q,
    "hbar_q_sq": hbar_q_sq,
    "phi_values": {f"N({p},{n})": {"name": name, "phi_q": phi_values[(p,n)],
                                    "E_bind_skein": phi_values[(p,n)]/hbar_q_sq,
                                    "ordering": orderings[(p,n)][0],
                                    "method": orderings[(p,n)][1]}
                   for p, n, name in unique_nuclei if (p,n) in phi_values},
    "lambda_shell": {
        "from_alpha": lambda_shell,
        "vs_deuterons": lambda_vs_deuterons,
        "unit": "Skein units (multiply by μ₀ for MeV)",
    },
}

out_path = Path(__file__).parent / "shell-correction-lambda.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)

print(f"Witness written to {out_path}")
