#!/usr/bin/env sage
"""
Nuclear braid witness computation in SageMath.

Computes EXACT symbolic Markov traces for nuclear braid words
in the Iwahori-Hecke algebra H_A(q) over Q(q).

For each nucleus:
  1. Build the nuclear braid word in H_A(q)
  2. Gröbner-reduce (automatic in Sage's T-basis)
  3. Compute the Markov trace (exact, symbolic)
  4. Evaluate at q = 1.110
  5. Compute Q-value as ground-state energy difference

Run:
    sage computations/sage-nuclear-braid.sage

Output:
    computations/sage-nuclear-braid.witness.json

Time estimate:
    A <= 6:  seconds
    A = 14:  minutes (3003 orderings for ground state search)
    A > 20:  may need hours
"""

import json
import time
from datetime import datetime, timezone
from itertools import combinations

print("SageMath nuclear braid computation")
print(f"Sage version: {version()}")
print()

# ── Parameters ───────────────────────────────────────────────────

q_num = 1.110  # numerical substrate parameter

# ── Helper: build nuclear braid and compute trace ────────────────

def nuclear_trace_sage(p, n, ordering=None):
    """Build nuclear braid in H_A(q) and compute Markov trace.

    ordering: list of 'p' and 'n' specifying nucleon positions.
              If None, uses block ordering ['p']*p + ['n']*n.

    Returns: (trace_symbolic, trace_numerical, n_terms)
    """
    A = p + n

    if ordering is None:
        ordering = ['p']*p + ['n']*n

    # Create Hecke algebra H_A(q) with parameter q
    # Sage's IwahoriHeckeAlgebra uses type A_{A-1} for A strands
    R = QQ['q']
    q = R.gen()

    # The Iwahori-Hecke algebra with T-basis
    # Parameters: q1 = q, q2 = -1 (so T_i^2 = (q-1)T_i + q)
    H = IwahoriHeckeAlgebra(['A', A-1], q, -1, R)
    T = H.T()

    # Build the braid word
    braid = T.one()

    for i in range(A):
        for j in range(i+1, A):
            ti, tj = ordering[i], ordering[j]
            # T[s] where s is the simple reflection s_i (1-indexed in Sage)
            s = H.coxeter_group().simple_reflections()[i+1]

            if ti == 'p' and tj == 'p':
                # Positive crossing: T_i
                braid = braid * T[s]
            elif ti == 'n' and tj == 'n':
                # Negative crossing: T_i^{-1}
                # In the T-basis: T_i^{-1} = q^{-1} T_i + (q^{-1} - 1)
                braid = braid * T[s].inverse()
            else:
                # Mixed crossing: (T_i + T_i^{-1}) / 2
                braid = braid * (T[s] + T[s].inverse()) / 2

    # Number of terms in the reduced expression
    n_terms = len(braid.coefficients())

    # Markov trace
    markov = H.markov_trace()
    trace_sym = markov(braid)

    # Evaluate numerically
    trace_num = float(trace_sym.subs({q: q_num}))

    return trace_sym, trace_num, n_terms


def ground_state_search(p, n, max_orderings=None):
    """Find the minimum-energy ordering for N(p,n).

    Enumerates all C(A, p) orderings and returns the one with
    minimum Φ_q = log|tr|.

    For large A, set max_orderings to limit the search.
    """
    A = p + n
    n_total = binomial(A, p)

    if max_orderings and n_total > max_orderings:
        print(f"  Too many orderings ({n_total}), sampling {max_orderings}")
        # TODO: implement random sampling or optimization
        return None, None, None

    best_phi = Infinity
    best_ordering = None
    best_trace = None

    count = 0
    for proton_positions in combinations(range(A), p):
        ordering = ['n'] * A
        for pos in proton_positions:
            ordering[pos] = 'p'

        _, trace_num, _ = nuclear_trace_sage(p, n, ordering)
        phi = log(abs(trace_num)).n() if abs(trace_num) > 1e-300 else -999

        if phi < best_phi:
            best_phi = phi
            best_ordering = ordering
            best_trace = trace_num

        count += 1
        if count % 500 == 0:
            print(f"    {count}/{n_total} orderings checked...")

    return best_phi, best_ordering, best_trace


# ── Main computation ─────────────────────────────────────────────

nuclei = [
    # (name, p, n, Q_exp_MeV, t_obs_yr_or_d, unit)
    ("3H",    1,  2, 0.01861, 12.32,   "yr"),
    ("3He",   2,  1, None,    None,    None),
    ("4He",   2,  2, None,    None,    None),
    ("6Li",   3,  3, None,    None,    None),
    ("14C",   6,  8, 0.156,   5730,    "yr"),
    ("14N",   7,  7, None,    None,    None),
]

results = []

for name, p, n, Q_exp, t_obs, unit in nuclei:
    A = p + n
    print(f"{'='*60}")
    print(f"{name}: N({p},{n}), A={A}")
    t0 = time.time()

    # Block ordering trace (fast)
    print(f"  Block ordering...")
    tr_sym, tr_num, n_terms = nuclear_trace_sage(p, n)
    elapsed = time.time() - t0

    print(f"  Trace (symbolic): {tr_sym}")
    print(f"  Trace (q=1.110):  {tr_num:.10f}")
    print(f"  Reduced terms:    {n_terms}")
    print(f"  Time:             {elapsed:.1f}s")

    result = {
        'nucleus': name,
        'p': int(p), 'n': int(n), 'A': int(A),
        'trace_symbolic': str(tr_sym),
        'trace_numerical': float(tr_num),
        'n_terms': int(n_terms),
        'elapsed_s': float(elapsed),
    }

    # Ground state search (for small A)
    n_orderings = int(binomial(A, p))
    if n_orderings <= 5000:
        print(f"  Ground state search ({n_orderings} orderings)...")
        t1 = time.time()
        gs_phi, gs_ordering, gs_trace = ground_state_search(p, n)
        gs_elapsed = time.time() - t1

        if gs_phi is not None:
            ordering_str = ''.join('●' if t=='p' else '○' for t in gs_ordering)
            print(f"  Ground state Φ_q = {gs_phi:.6f}")
            print(f"  Ordering: {ordering_str}")
            print(f"  Search time: {gs_elapsed:.1f}s")

            result['ground_state'] = {
                'phi_q': float(gs_phi),
                'ordering': gs_ordering,
                'ordering_visual': ordering_str,
                'trace': float(gs_trace),
                'search_time_s': float(gs_elapsed),
                'n_orderings': n_orderings,
            }

    # Daughter trace (for Q-value)
    if n >= 1:
        print(f"  Daughter N({p+1},{n-1})...")
        tr_dau_sym, tr_dau_num, _ = nuclear_trace_sage(p+1, n-1)
        result['daughter_trace_numerical'] = float(tr_dau_num)
        result['daughter_trace_symbolic'] = str(tr_dau_sym)

        # Q from block ordering
        phi_par = log(abs(tr_num)).n()
        phi_dau = log(abs(tr_dau_num)).n()
        Q_hecke = float(phi_par - phi_dau)
        result['Q_hecke_block'] = Q_hecke

        if Q_exp:
            result['Q_exp'] = Q_exp
            result['Q_ratio_block'] = Q_hecke / Q_exp

    if Q_exp:
        print(f"  Q_hecke (block) = {result.get('Q_hecke_block', 'N/A')}")
        print(f"  Q_exp = {Q_exp} MeV")

    results.append(result)
    print()

# ── Q-value table ────────────────────────────────────────────────

print("=" * 70)
print("Q-VALUE SUMMARY")
print("=" * 70)
print()
print(f"{'Nuc':>8} | {'Q_hecke':>10} | {'Q_exp':>8} | {'ratio':>8}")
print("-" * 45)

for r in results:
    if 'Q_exp' in r and r['Q_exp']:
        Q_h = r.get('Q_hecke_block', 0)
        Q_e = r['Q_exp']
        ratio = Q_h / Q_e if Q_e else 0
        print(f"{r['nucleus']:>8} | {Q_h:10.6f} | {Q_e:8.5f} | {ratio:8.4f}")

# ── Ground state Q ───────────────────────────────────────────────

print()
print("=" * 70)
print("GROUND STATE Q-VALUES")
print("=" * 70)
print()

gs_phis = {}
for r in results:
    if 'ground_state' in r:
        key = (r['p'], r['n'])
        gs_phis[key] = r['ground_state']['phi_q']

print(f"{'transition':>20} | {'Φ_par':>10} | {'Φ_dau':>10} | {'Q_gs':>10}")
print("-" * 60)

transitions = [
    ((1,2), (2,1), "3H→3He"),
    ((2,2), (3,1), "4He→5Li"),
    ((3,3), (4,2), "6Li→6Be"),
    ((6,8), (7,7), "14C→14N"),
]

for (p1,n1), (p2,n2), label in transitions:
    if (p1,n1) in gs_phis and (p2,n2) in gs_phis:
        phi1 = gs_phis[(p1,n1)]
        phi2 = gs_phis[(p2,n2)]
        Q = phi1 - phi2
        print(f"{label:>20} | {phi1:10.6f} | {phi2:10.6f} | {Q:+10.6f}")

# ── Write witness ────────────────────────────────────────────────

witness = {
    'computation': 'sage-nuclear-braid',
    'description': 'Exact symbolic Markov traces in IwahoriHeckeAlgebra over Q(q)',
    'engine': f'SageMath {version()}',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'parameters': {
        'q_numerical': q_num,
        'hecke_type': 'A_{A-1}',
        'basis': 'T (braid generators)',
        'trace': 'Markov (Ocneanu)',
    },
    'results': results,
}

out_path = 'computations/sage-nuclear-braid.witness.json'
with open(out_path, 'w') as f:
    json.dump(witness, f, indent=2, default=str)

print(f"\nWitness written to {out_path}")
print("Done.")
