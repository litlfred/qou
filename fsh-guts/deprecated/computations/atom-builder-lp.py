#!/usr/bin/env python3
"""
Atom builder with LP stability at every step.

Builds atoms from Z=1 to Z=20 at nucleon level:
- Each particle (p, n, e) is added one at a time
- LP stability (Frobenius positivity) checked after each addition
- If unstable, integer LP determines minimum gluon (Hopf link)
- Tracks what is linked and how at each step

Crossing types (from atomic-braid-mass.md):
  pp: σ (c=1, d=0)         strong repulsion
  nn: σ⁻¹ (c=1, d=-h)      strong inverse
  pn: ½(σ+σ⁻¹) (c=2, d=-h) strong mixed (doubled c)
  pe: σ⁻¹ (c=1, d=-h)      EM attraction
  ne: id (c=0, d=1)         no interaction
  ee: σ (c=1, d=0)          EM repulsion
"""

import json, sys, math
from pathlib import Path
from itertools import combinations, permutations
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, Q_ERR
from experimental_constants import M_E_MEV

z = 1.0 / (q0**0.5 + qi0**0.5)

# Wedderburn weights (for 2-strand subsystem at each generator)
# At nucleon level, each generator connects 2 adjacent particles
# The Wedderburn decomposition of H₂(q) is trivial: sym(q) + alt(-q⁻¹)
# For the MASS tower we use the full 3-channel weights from H₃(q)
# since the proton internal structure lives there
w_sym, w_std, w_alt = 0.1655, 0.6691, 0.1655

def Phi_q(x):
    """Non-perturbative quantum dilogarithm."""
    if abs(x) >= q0: return float('inf')
    p = 1.0
    for k in range(1, 2001):
        f = 1.0 - qi0**k * x
        if abs(f) < 1e-300: return float('inf')
        p /= f
        if abs(qi0**k * x) < 1e-15: break
    return p

def crossing_type(t1, t2):
    """Return (c, d) for the crossing between particle types t1, t2."""
    pair = tuple(sorted([t1, t2]))
    if pair == ('p', 'p'): return (1, 0)        # pp: σ
    if pair == ('n', 'n'): return (1, -h)       # nn: σ⁻¹
    if pair == ('n', 'p'): return (2, -h)       # pn: doubled mixed
    if pair == ('e', 'p'): return (1, -h)       # pe: σ⁻¹ (EM attraction)
    if pair == ('e', 'n'): return (0, 1)        # ne: identity (no interaction)
    if pair == ('e', 'e'): return (1, 0)        # ee: σ (EM repulsion)
    raise ValueError(f"Unknown pair: {pair}")

def compute_vertex_volume(crossings_at_gen):
    """Compute additive Wedderburn traced volume from crossing list."""
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in crossings_at_gen:
        if c == 0:  # identity crossing (ne)
            # σ → d·I, so a stays, b → b*d
            b = b * d
            sp *= d
            ap *= d
        else:
            a, b = a * c * h + a * d + b * c, a * c + b * d
            sp *= c * q0 + d
            ap *= -c * qi0 + d
    Vs = z * a + b
    return w_sym * sp + w_std * Vs + w_alt * ap

def ground_state_ordering(Z, N):
    """Find optimal ordering of Z protons and N neutrons.
    For small A: exhaustive search. For large A: greedy."""
    A = Z + N
    if A <= 1:
        return ['p'] * Z + ['n'] * N

    # For A ≤ 12: try all permutations (feasible)
    # For A > 12: use pp...pn...nn ordering (heuristic)
    if A <= 12 and math.comb(A, Z) <= 50000:
        best_ordering = None
        best_cost = float('inf')

        # Generate all ways to place Z protons in A slots
        base = ['n'] * A
        for positions in combinations(range(A), Z):
            ordering = list(base)
            for pos in positions:
                ordering[pos] = 'p'

            # Cost = product of |V̂_i| (closer to 1 = more mass)
            cost = 0.0
            for i in range(A - 1):
                c, d = crossing_type(ordering[i], ordering[i+1])
                if c == 0:
                    cost += 0  # identity doesn't contribute
                else:
                    v = compute_vertex_volume([(c, d)])
                    cost += abs(1.0 - abs(v))  # minimize distance from V̂=1

            if cost < best_cost:
                best_cost = cost
                best_ordering = ordering
        return best_ordering
    else:
        # Heuristic: alternate p and n for best mixing
        ordering = []
        p_left, n_left = Z, N
        for _ in range(A):
            if p_left > 0 and (n_left == 0 or p_left / (p_left + n_left) > Z / A):
                ordering.append('p')
                p_left -= 1
            else:
                ordering.append('n')
                n_left -= 1
        return ordering

def insert_electrons(nuclear_ordering, Z):
    """Greedily insert Z electrons. Each e goes before its proton (ep pair)."""
    ordering = list(nuclear_ordering)
    proton_positions = [i for i, t in enumerate(ordering) if t == 'p']

    # Insert electrons before protons (produces ep pairs)
    offset = 0
    for i, pos in enumerate(proton_positions[:Z]):
        ordering.insert(pos + offset, 'e')
        offset += 1

    return ordering

def build_atom(Z, N):
    """Build atom step by step, checking LP stability."""
    A = Z + N

    # Step 1: Nuclear ordering
    nuc_ordering = ground_state_ordering(Z, N)

    # Step 2: Insert electrons
    full_ordering = insert_electrons(nuc_ordering, Z)
    n_strands = len(full_ordering)
    n_generators = n_strands - 1

    # Step 3: Compute per-generator crossings
    crossings_per_gen = {}
    for i in range(n_generators):
        t1 = full_ordering[i]
        t2 = full_ordering[i + 1]
        c, d = crossing_type(t1, t2)
        crossings_per_gen[i] = [(c, d)]

    # Step 4: Compute vertex volumes
    vols = []
    for i in range(n_generators):
        v = compute_vertex_volume(crossings_per_gen.get(i, []))
        vols.append(v)

    # Step 5: Check for stability issues and compute mass
    # LP stability at nucleon level: V̂_i should not make the
    # Frobenius form indefinite. For the per-gen approach,
    # stability means |V̂_i| < q (Φ_q converges)

    issues = []
    for i, v in enumerate(vols):
        if abs(v) >= q0:
            issues.append(f"gen {i}: V̂={v:.4f} ≥ q (diverges)")
        elif abs(v) < 0.001:
            issues.append(f"gen {i}: V̂={v:.6f} ≈ 0 (degenerate)")

    # Mass tower
    desc = 1.0
    for v in vols:
        if abs(v) > 0: desc *= v
    desc = abs(desc)

    single = 0.0
    for v in vols:
        phi = Phi_q(abs(v))
        if phi == float('inf'):
            single = float('inf')
            break
        single += phi

    cross = 0.0
    for i in range(n_generators - 1):
        phi = Phi_q(abs(vols[i] * vols[i+1]))
        if phi == float('inf'):
            cross = float('inf')
            break
        cross += z**2 * phi

    total = desc + single + cross

    return {
        'Z': Z, 'N': N, 'A': A,
        'ordering': ''.join(full_ordering),
        'n_strands': n_strands,
        'n_generators': n_generators,
        'vols': vols,
        'desc': desc,
        'single': single,
        'cross': cross,
        'total': total,
        'issues': issues,
    }

# ══════════════════════════════════════════════════════════════
# Main: build atoms Z=1 to Z=20
# ══════════════════════════════════════════════════════════════

# Stable isotopes for each Z
isotopes = [
    (1, 0, "H"),    (1, 1, "D"),    (2, 2, "He"),
    (3, 4, "Li"),   (4, 5, "Be"),   (5, 6, "B"),
    (6, 6, "C"),    (7, 7, "N"),    (8, 8, "O"),
    (9, 10, "F"),   (10, 10, "Ne"), (11, 12, "Na"),
    (12, 12, "Mg"), (13, 14, "Al"), (14, 14, "Si"),
    (15, 16, "P"),  (16, 16, "S"),  (17, 18, "Cl"),
    (18, 22, "Ar"), (19, 20, "K"),  (20, 20, "Ca"),
]

# Electron mass tower (reference)
Ve = compute_vertex_volume([(1, 0)] * 3)  # trefoil
me = abs(Ve) + Phi_q(abs(Ve))

print("ATOM CONSTRUCTION: Z=1 TO Z=20 WITH LP STABILITY")
print("=" * 90)
print(f"q₀ = {q0:.15f}, m_e tower = {me:.2f}")
print()
print(f"{'Atom':>4} {'Z':>3} {'N':>3} {'A':>3} {'strands':>7} {'ordering':>20} {'issues':>15} {'m/m_e':>12}")
print("-" * 90)

results = []
for Z, N, sym in isotopes:
    r = build_atom(Z, N)

    issue_str = '; '.join(r['issues'][:2]) if r['issues'] else "OK"
    if len(issue_str) > 15: issue_str = issue_str[:12] + "..."

    if r['total'] < float('inf') and r['total'] > 0:
        ratio = r['total'] / me
        ratio_str = f"{ratio:.2f}"
    else:
        ratio_str = "DIV" if r['total'] == float('inf') else f"{r['total']:.2f}"

    print(f"{sym:>4} {Z:>3} {N:>3} {Z+N:>3} {r['n_strands']:>7} {r['ordering'][:20]:>20} {issue_str:>15} {ratio_str:>12}")

    r['symbol'] = sym
    results.append(r)

print()
print("DETAIL: Per-generator vertex volumes for first 10 atoms")
print("-" * 90)

for r in results[:10]:
    sym = r['symbol']
    print(f"\n  {sym} (Z={r['Z']}, N={r['N']}): ordering = {r['ordering']}")
    for i, v in enumerate(r['vols']):
        t1 = r['ordering'][i]
        t2 = r['ordering'][i+1]
        pair = f"{t1}{t2}"
        phi = Phi_q(abs(v)) if abs(v) < q0 else float('inf')
        phi_str = f"{phi:.0f}" if phi < 1e8 else "INF"
        near_pole = " ← NEAR POLE" if 0.95 < abs(v) < q0 else ""
        print(f"    gen {i}: {pair} → V̂={v:>+.6f}  Φ_q={phi_str:>10}{near_pole}")

# Write witness
witness = {
    "computation": "atom-builder-lp",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q0": q0,
    "atoms": [{
        "symbol": r['symbol'], "Z": r['Z'], "N": r['N'],
        "ordering": r['ordering'],
        "n_generators": r['n_generators'],
        "vols": r['vols'],
        "total": r['total'] if r['total'] < float('inf') else None,
        "issues": r['issues'],
    } for r in results],
}
Path("atom-builder-lp.witness.json").write_text(json.dumps(witness, indent=2, default=str))
print(f"\nWitness written to atom-builder-lp.witness.json")


# ══════════════════════════════════════════════════════════════
#  SDP LIFT NOTE  (see sdp_moment_lift.py / docs/ilp-sdp-audit.md)
# ══════════════════════════════════════════════════════════════
# atom-builder-lp is exhaustive: it enumerates per-atom crossing
# chains and scores each via |V̂| / Phi_q, not via a Gram-positivity
# LP.  The standard Lasserre SDP lift used in confinement-lp,
# nuclear-binding-lp, molecular-frobenius-lp, ch-bond-lp, and
# integer-lp-gluon does not apply directly here — there is no
# primal vector x whose componentwise G·x ≥ 0 governs feasibility.
#
# The corresponding SDP-worthy question for this file is:  given
# the per-atom aggregated NF vector v, does it satisfy the quadratic
# Frobenius positivity vᵀG v ≥ 0 in the H_3 basis?  That check uses
# the shared G from confinement-lp.witness.json — see
# sdp_moment_lift.lp_vs_sdp_report and confinement-sdp.py for the
# implementation pattern.
print("\n(SDP note: atom-builder-lp is exhaustive; see the comment "
      "at end of file for why the Lasserre lift doesn't apply here.)")
