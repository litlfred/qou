#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to folio-assistant/computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Atom mass via universal branching rule (prop:universal-braid-branching).

For each nucleon K_i ∈ H_3(q), compute 3 channel characters
(χ^sym, χ^std, χ^alt).  Then for any λ ⊢ 3A:

    χ_atom(λ) = Σ_{(μ_1,...,μ_A)} f^{λ/(μ_1⊔...⊔μ_A)}
                                  · Π_i χ^{μ_i}(K_i)

where μ_i ⊢ 3, i.e. μ_i ∈ {[3], [2,1], [1,1,1]}.

This is the ASYMMETRIC-WEIGHTED approach (user's "color tubes"),
not averaging.  Each partition λ gets 3^A terms, each weighted by
a skew-SYT count f^{λ/μ}.

Free baseline: nucleons disconnected tensor — direct branching.
Atom with inter-nucleon crossings: add correction terms from
inter-nucleon σ_j generators acting on adjacent H_3 blocks.

Markov trace / tower mass:
    m_tower = Σ_λ w_λ(q) · χ_atom(λ) / d_λ
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone
from itertools import product as iproduct
from functools import lru_cache

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, qi0 as qi, z_mark, HA as h,
    proton_cross, neutron_cross,
)


# ── q-integers and q-factorial ──────────────────────────────────────

def q_int(k):
    return (q0 ** k - qi ** k) / (q0 - qi) if k != 0 else 0.0

def q_fact(n):
    r = 1.0
    for k in range(1, n + 1):
        r *= q_int(k)
    return r

def q_dim(partition, n):
    """Quantum dimension of partition λ ⊢ n (hook-length formula)."""
    hooks = []
    for i, rl in enumerate(partition):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(partition)) if partition[r2] > j)
            hooks.append(arm + leg + 1)
    num = q_fact(n)
    den = 1.0
    for hook in hooks:
        den *= q_int(hook)
    return num / den if abs(den) > 1e-30 else 0


def classical_dim(partition, n):
    """Classical dimension d_λ via hook-length formula."""
    hooks = []
    for i, rl in enumerate(partition):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(partition)) if partition[r2] > j)
            hooks.append(arm + leg + 1)
    num = math.factorial(n)
    den = 1
    for hook in hooks:
        den *= hook
    return num // den if den > 0 else 0


# ── Per-nucleon H_3 channel characters ──────────────────────────────

def nucleon_h3_characters(crossings_per_gen):
    """Compute (χ^sym, χ^std, χ^alt) for a nucleon K ∈ H_3(q).

    Sym rep: σ_i acts as q on both generators → 1-dim.
    Alt rep: σ_i acts as -q⁻¹ on both → 1-dim.
    Std rep: 2-dim Hoefsmit seminormal form.
    """
    # Sym/alt: products of scalar eigenvalues
    chi_sym = 1.0
    chi_alt = 1.0
    for gen in [0, 1]:
        for c, d in crossings_per_gen.get(gen, []):
            chi_sym *= c * q0 + d            # σ_sym = q
            chi_alt *= -c * qi + d           # σ_alt = -q⁻¹
    # Std: 2×2 Hoefsmit matrices for H_3 at partition (2,1):
    # σ_1 = diag(q, -q⁻¹), σ_2 with specific off-diagonal structure.
    # Using the Hoefsmit formula:
    sigma_1 = np.array([[q0, 0.0], [0.0, -qi]])
    # σ_2 matrix from universal-braid-branching.md: α = -1/(q³+q), γ = q³/(q²+1)
    alpha = -1.0 / (q0 ** 3 + q0)
    gamma = q0 ** 3 / (q0 ** 2 + 1.0)
    # sigma_2 has entries determined by axial distances and Hoefsmit rules.
    # Using: σ_2 = [[α, β], [β*, γ]] with α + γ = h and αγ + ββ* = -1
    off = math.sqrt(max(0.0, -1.0 - alpha * gamma))
    sigma_2 = np.array([[alpha, off], [off, gamma]])
    # Build std character
    M = np.eye(2)
    for gen in [0, 1]:
        sig = sigma_1 if gen == 0 else sigma_2
        for c, d in crossings_per_gen.get(gen, []):
            op = c * sig + d * np.eye(2)
            M = M @ op
    chi_std = float(np.trace(M))
    return {'sym': chi_sym, 'std': chi_std, 'alt': chi_alt}


# ── Skew-SYT count via hook formula (Aitken-Frobenius) ──────────────

def fits_inside(mu, lam):
    """Check that μ fits inside λ (Young diagram containment)."""
    if len(mu) > len(lam):
        return False
    for i, m in enumerate(mu):
        if m > lam[i]:
            return False
    return True


def skew_syt_count(lam, mu):
    """|SYT(λ/μ)| via Aitken's determinant formula:
       f^{λ/μ} = n! · det(1 / (λ_i - μ_j - i + j)!)
    where n = |λ| - |μ|, and 1/k! = 0 for k < 0.
    """
    if not fits_inside(mu, lam):
        return 0
    n_lam = sum(lam)
    n_mu = sum(mu)
    n = n_lam - n_mu
    if n < 0:
        return 0
    L = len(lam)
    # Pad μ with zeros to length L
    mu_p = list(mu) + [0] * (L - len(mu))
    # Build matrix
    M = [[0.0] * L for _ in range(L)]
    for i in range(L):
        for j in range(L):
            k = lam[i] - mu_p[j] - i + j
            if k >= 0:
                M[i][j] = 1.0 / math.factorial(k)
    # Compute det via numpy
    Mnp = np.array(M)
    det = float(np.linalg.det(Mnp))
    result = math.factorial(n) * det
    return int(round(result))


def concat_partitions(parts):
    """Concatenate a sequence of partitions (row-stacked, then sorted)."""
    all_rows = []
    for p in parts:
        all_rows.extend(p)
    return tuple(sorted(all_rows, reverse=True))


# ── Partition enumeration ───────────────────────────────────────────

def partitions_of(n, max_parts=None):
    """All partitions of n."""
    if n == 0:
        return [()]
    results = []
    def rec(remaining, max_part, current):
        if remaining == 0:
            results.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 0, -1):
            rec(remaining - p, p, current + [p])
    rec(n, n, [])
    if max_parts:
        results = [p for p in results if len(p) <= max_parts]
    return results


# ── Atom character via branching (free baseline) ────────────────────

H3_MUS = [(3,), (2, 1), (1, 1, 1)]
H3_CHANNELS = ['sym', 'std', 'alt']

# Precompute proton/neutron channel characters
CHI_PROTON  = nucleon_h3_characters(proton_cross)
CHI_NEUTRON = nucleon_h3_characters(neutron_cross)


def chi_of_nucleon(ntype, mu):
    """χ^μ(K_i) for nucleon type ∈ {'p', 'n'} and μ ∈ H3_MUS."""
    chi_dict = CHI_PROTON if ntype == 'p' else CHI_NEUTRON
    for m, ch in zip(H3_MUS, H3_CHANNELS):
        if m == mu:
            return chi_dict[ch]
    return 0.0


def atom_character_free_branching(Z, N, lam):
    """χ_free(λ) via universal branching rule — disconnected tensor."""
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    total = 0.0
    for mu_seq in iproduct(H3_MUS, repeat=A):
        mu_concat = concat_partitions(mu_seq)
        if not fits_inside(mu_concat, lam):
            continue
        f = skew_syt_count(lam, mu_concat)
        if f == 0:
            continue
        prod = 1.0
        for i, mu in enumerate(mu_seq):
            prod *= chi_of_nucleon(nucleon_types[i], mu)
        total += f * prod
    return total


def atom_character_with_inter(Z, N, lam, m_pp, m_pn, m_nn):
    """χ_atom(λ) with inter-nucleon crossing corrections.

    Approximation: inter-nucleon σ_j on adjacent nucleons (k, k+1)
    modifies the μ_k and μ_{k+1} characters by multiplying by
    (c σ + d) in the appropriate channel.  For now, treat the
    inter-nucleon contribution as a multiplicative factor on the
    free baseline — proportional to the Markov weight z^{A-1}
    times a pair-type-dependent phase.
    """
    free_chi = atom_character_free_branching(Z, N, lam)
    # Inter-nucleon phase factor: product over pairs
    n_pp = max(0, Z - 1)
    n_pn = 1 if Z > 0 and N > 0 else 0
    n_nn = max(0, N - 1)
    # Each pair contributes a Markov-weighted phase
    # pp: m_pp crossings with (c=1, d=0) → factor (q^{m_pp}·z)^?
    # Simplification: use Markov trace of pair crossing:
    # tr_M(σ^m) = z · q^m + (1-z)·(-q⁻¹)^m  [approximate]
    pair_factor = 1.0
    for _ in range(n_pp):
        pair_factor *= (z_mark * q0 ** m_pp + (1 - z_mark) * (-qi) ** m_pp)
    for _ in range(n_pn):
        # pn: σ with d=-h/2 effective
        pair_factor *= (z_mark * (q0 - h/2) ** m_pn
                        + (1 - z_mark) * (-qi - h/2) ** m_pn)
    for _ in range(n_nn):
        # nn: σ⁻¹ with d=-h
        pair_factor *= (z_mark * (q0 - h) ** m_nn
                        + (1 - z_mark) * (-qi - h) ** m_nn)
    return free_chi * pair_factor


# ── Atom tower mass via Wedderburn sum ──────────────────────────────

def atom_tower_mass_branching(Z, N, m_pp=1, m_pn=1, m_nn=1, include_inter=True):
    """m_tower = Σ_λ w_λ(q) · χ_atom(λ) / d_λ, summed over λ ⊢ 3A."""
    A = Z + N
    if A < 1:
        return 0.0
    n_strands = 3 * A
    lams = partitions_of(n_strands, max_parts=n_strands)
    # Wedderburn weights at H_{3A}
    nfA = q_fact(n_strands)
    total = 0.0
    for lam in lams:
        dq = q_dim(lam, n_strands)
        dcl = classical_dim(lam, n_strands)
        if dcl == 0:
            continue
        w_lam = dq ** 2 / nfA
        if include_inter:
            chi = atom_character_with_inter(Z, N, lam, m_pp, m_pn, m_nn)
        else:
            chi = atom_character_free_branching(Z, N, lam)
        total += w_lam * chi / dcl
    return total


# ── Calibration and test ────────────────────────────────────────────

# Per CAL-3 (`prop:three-calibration-inputs`), E_0 must trace back
# to Q_β(n), not proton mass — proton-mass-anchoring is a forbidden
# second pinning of the hadronic scale. Use the canonical
# E_0_CALIBRATION_MEV from hecke_core (= experimental_constants.
# Q_NEUTRON_MEV = 0.78233341 MeV). The proton-tower mass is retained
# only as a per-block intermediate for diagnostic comparison.
_m_proton_branching = atom_tower_mass_branching(1, 0, include_inter=False)
from hecke_core import E_0_CALIBRATION_MEV  # noqa: E402
E_0_BRANCH = E_0_CALIBRATION_MEV  # 0.78233341 MeV (CODATA Q_β(n))


def binding_branching(Z, N, m_pp, m_pn, m_nn):
    """Binding via branching: B = E_0 · (m_free - m_atom)."""
    m_atom = atom_tower_mass_branching(Z, N, m_pp, m_pn, m_nn, include_inter=True)
    m_free = atom_tower_mass_branching(Z, N, include_inter=False)
    B = E_0_BRANCH * (m_free - m_atom)
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_atom": m_atom, "m_free": m_free,
        "B_MeV": B,
    }


if __name__ == "__main__":
    print("ATOM MASS via UNIVERSAL BRANCHING RULE")
    print("=" * 88)
    print(f"q₀ = {q0}")
    print(f"E_0 (branching) = {E_0_BRANCH:.4e} MeV/cat.unit")
    print(f"  (from single-nucleon m_proton = {_m_proton_branching:.4e} cat.units)")
    print()
    print(f"Per-nucleon H_3 characters:")
    print(f"  proton:  sym={CHI_PROTON['sym']:+.4f}, "
          f"std={CHI_PROTON['std']:+.4f}, alt={CHI_PROTON['alt']:+.4f}")
    print(f"  neutron: sym={CHI_NEUTRON['sym']:+.4f}, "
          f"std={CHI_NEUTRON['std']:+.4f}, alt={CHI_NEUTRON['alt']:+.4f}")
    print()

    # Small atoms only (A ≤ 6) because partition count p(3A) explodes
    # and 3^A compositions for each
    ATOMS_SMALL = [
        ("D",   1, 1,   2.22),
        ("T",   1, 2,   8.48),
        ("3He", 2, 1,   7.72),
        ("4He", 2, 2,  28.30),
    ]

    print(f"  {'Atom':>6} {'A':>3} {'m_free':>14} {'m_atom':>14} "
          f"{'B_pred':>10} {'B_AME':>8} {'|ΔM/M|%':>10}")
    print("  " + "-" * 80)

    # Load ILP ground states from level walk witness
    witness = Path(__file__).parent / "confinement-level-walk.witness.json"
    ilp_ground = {}
    if witness.exists():
        w = json.loads(witness.read_text())
        for atom_key, data in w["levels"].get("3", {}).get("atoms", {}).items():
            if not data.get("unstable"):
                ilp_ground[atom_key] = data["ground_state"]

    results = []
    for atom, Z, N, B_AME in ATOMS_SMALL:
        gs = ilp_ground.get(atom, {"m_pp": 1, "m_pn": 1, "m_nn": 1})
        try:
            r = binding_branching(Z, N, gs["m_pp"], gs["m_pn"], gs["m_nn"])
            # |ΔM/M| % — using total mass-energy scale (atom mass ~ A·m_nucleon)
            M_AME = (Z + N) * 938.272  # rough atom mass in MeV
            dM_over_M = abs(r["B_MeV"] - B_AME) / M_AME * 100
            print(f"  {atom:>6} {Z+N:>3d} {r['m_free']:>14.4e} "
                  f"{r['m_atom']:>14.4e} {r['B_MeV']:>10.4f} "
                  f"{B_AME:>8.2f} {dM_over_M:>9.4f}%")
            results.append({
                "atom": atom, **r,
                "ilp_ground_state": gs,
                "B_AME_MeV": B_AME, "M_AME_MeV": M_AME,
                "delta_M_over_M_pct": dM_over_M,
            })
        except Exception as e:
            print(f"  {atom:>6} ERROR: {e}")

    witness_out = {
        "computation": "atom-mass-branching",
        "description": (
            "Atom tower mass via universal branching rule per "
            "prop:universal-braid-branching: χ_atom(λ) = Σ f^{λ/μ} · Π χ^{μ_i}(K_i). "
            "Free baseline: direct branching (disconnected tensor). "
            "Atom: free × Markov-weighted inter-nucleon phase from ILP "
            "ground state. ΔM/M computed against atom rest mass ≈ A·938.272 MeV."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": q0, "E_0_tower_MeV": E_0_BRANCH,
            "chi_proton": CHI_PROTON, "chi_neutron": CHI_NEUTRON,
        },
        "results": results,
    }
    out = Path(__file__).parent / "atom-mass-branching.witness.json"
    out.write_text(json.dumps(witness_out, indent=2, default=str))
    print(f"\nWitness: {out}")
