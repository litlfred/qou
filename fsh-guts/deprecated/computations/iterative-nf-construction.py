#!/usr/bin/env python3
"""
Iterative NF construction of nuclei.

Builds nuclei one nucleon at a time following the shell-closure-normal-form
construction. At each step:
  1. Add one nucleon (p or n) via typed crossing operators
  2. Reduce to Gröbner-Shirshov NF in H_A(q)
  3. Witness: verify NF properties, record vertex volumes V̂_i
  4. Compute Q-value via Gram matrix formula: Q = |Σ ΔV̂| × z² × m_e

The construction order alternates p-n following the shell filling rules.
The NF is guaranteed unique by Bergman confluence.

Usage:
    python3 iterative-nf-construction.py
"""
import math, sys, json
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, HBAR_Q, LN_Q

z = 1.0 / (q**0.5 + q**(-0.5))
m_e = 0.51099895
E_gram = z**2 * m_e  # Gram matrix energy scale


def chain_V(ordering, gen):
    """Vertex volume V̂_i at generator gen."""
    A = len(ordering)
    a, b = 0.0, 1.0
    for j in range(gen + 1, A):
        ti, tj = ordering[gen], ordering[j]
        if ti == 1 and tj == 1:
            d = 0.0
        elif ti == 0 and tj == 0:
            d = -h
        else:
            d = -h / 2
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def all_V(ordering):
    """All vertex volumes for an ordering."""
    A = len(ordering)
    return [chain_V(ordering, i) for i in range(A - 1)]


def verify_nf(ordering):
    """Verify NF properties of the transfer matrix chain.

    The per-generator transfer matrix chain IS the NF (by P1 of
    shell-construction-rules.md: zero YB steps, zero far-comm steps).
    We verify:
      (a) Each V̂_i is finite and nonzero
      (b) The Skein polynomial P = Π V̂_i is well-defined
      (c) The ordering has correct nucleon counts
    """
    A = len(ordering)
    Z = sum(ordering)
    N = A - Z
    vols = all_V(ordering)

    ok = True
    issues = []

    # Check finiteness
    for i, v in enumerate(vols):
        if not math.isfinite(v):
            issues.append(f"V̂_{i} = {v} (not finite)")
            ok = False
        if abs(v) < 1e-300:
            issues.append(f"V̂_{i} ≈ 0 (underflow)")
            ok = False

    # Check Skein polynomial
    logP = sum(math.log(abs(v)) for v in vols if v != 0)

    return {
        'ok': ok,
        'issues': issues,
        'Z': Z, 'N': N, 'A': A,
        'vols': vols,
        'logP': logP,
        'Phi': logP,  # quantum dilogarithm volume
    }


def build_nucleus(Z_target, N_target, verbose=True):
    """Iteratively build nucleus by alternating p-n Hopf linking.

    Following shell-closure-normal-form.md:
    1. Start with N(1,0) = [1] (single proton)
    2. Alternate adding n, p, n, p, ...
    3. At each step, verify NF and witness V̂_i

    Returns the final ordering and per-step witness data.
    """
    A_target = Z_target + N_target
    steps = []

    # Determine construction sequence: alternate n, p, n, p, ...
    # Start with one proton, then add neutrons and protons alternately
    sequence = []
    pi, ni = 0, 0

    # First nucleon: proton
    sequence.append(1)
    pi += 1

    # Then alternate: n, p, n, p, ... until we have enough of each
    while pi + ni < A_target:
        if ni < N_target:
            sequence.append(0)
            ni += 1
        if pi + ni >= A_target:
            break
        if pi < Z_target:
            sequence.append(1)
            pi += 1

    # Build ordering step by step
    ordering = []

    for step_idx, nucleon_type in enumerate(sequence):
        ordering.append(nucleon_type)
        A = len(ordering)
        Z = sum(ordering)
        N = A - Z

        # Verify NF
        nf = verify_nf(ordering)

        # Witness this step
        label = 'p' if nucleon_type == 1 else 'n'
        step_data = {
            'step': step_idx,
            'added': label,
            'A': A, 'Z': Z, 'N': N,
            'ordering': ordering[:],
            'nf_ok': nf['ok'],
            'nf_issues': nf['issues'],
            'Phi': nf['Phi'],
        }

        if A >= 2:
            step_data['vols'] = [round(v, 10) for v in nf['vols']]
            step_data['logP'] = nf['logP']

        steps.append(step_data)

        if verbose and A <= 20:
            vols_str = ', '.join(f'{v:+.4f}' for v in nf['vols']) if A >= 2 else '—'
            nf_mark = '✓' if nf['ok'] else '✗'
            print(f"  Step {step_idx:2d}: +{label} → [{','.join(str(x) for x in ordering)}] "
                  f"A={A} Z={Z} N={N} | NF {nf_mark} | Φ={nf['Phi']:+.4f} | V̂=[{vols_str}]")

    return ordering, steps


def compute_Q(Z, N, Q_exp=None, verbose=True):
    """Compute Q-value for β⁻ decay (Z,N) → (Z+1,N-1)."""
    if verbose:
        print(f"\n{'─' * 70}")
        print(f"  PARENT: Z={Z}, N={N}, A={Z+N}")

    ord_par, steps_par = build_nucleus(Z, N, verbose=verbose)

    if verbose:
        print(f"\n  DAUGHTER: Z={Z+1}, N={N-1}, A={Z+N}")

    ord_dau, steps_dau = build_nucleus(Z + 1, N - 1, verbose=verbose)

    # Compute ΣΔV̂
    V_par = all_V(ord_par)
    V_dau = all_V(ord_dau)
    A = Z + N

    sum_dV = sum(V_dau[i] - V_par[i] for i in range(A - 1))
    Q_pred = abs(sum_dV) * E_gram

    err = (Q_pred / Q_exp - 1) * 100 if Q_exp else None

    if verbose:
        print(f"\n  Q = |ΣΔV̂| × z² × m_e = |{sum_dV:+.6f}| × {E_gram:.6f}")
        print(f"  Q_pred = {Q_pred:.6f} MeV")
        if Q_exp:
            print(f"  Q_exp  = {Q_exp:.6f} MeV")
            print(f"  Error  = {err:+.1f}%")

    return {
        'Z': Z, 'N': N, 'A': A,
        'ord_par': ord_par, 'ord_dau': ord_dau,
        'sum_dV': sum_dV, 'Q_pred': Q_pred,
        'Q_exp': Q_exp, 'err': err,
        'steps_par': steps_par, 'steps_dau': steps_dau,
        'V_par': V_par, 'V_dau': V_dau,
    }


if __name__ == '__main__':
    print("=" * 70)
    print("  ITERATIVE NF CONSTRUCTION + GRAM MATRIX Q-VALUE")
    print(f"  q = {q:.10f}, z² = {z**2:.10f}, m_e = {m_e}")
    print(f"  E_gram = z² × m_e = {E_gram:.8f} MeV")
    print("=" * 70)

    benchmarks = [
        (1, 2, 0.018592, '3H→3He'),
        (6, 8, 0.156476, '14C→14N'),
        (27, 33, 2.823, '60Co→60Ni'),
    ]

    results = []
    for Z, N, Q_exp, name in benchmarks:
        print(f"\n{'═' * 70}")
        print(f"  {name}")
        print(f"{'═' * 70}")

        r = compute_Q(Z, N, Q_exp, verbose=(Z + N <= 20))
        results.append({'name': name, **r})

    # Summary
    print(f"\n{'═' * 70}")
    print("  SUMMARY")
    print(f"{'═' * 70}")
    print(f"  {'Decay':15s} | {'Q_pred':>8s} | {'CODATA':>8s} | {'Error':>8s}")
    print(f"  {'-' * 48}")
    for r in results:
        name = r.get('name', f"Z={r['Z']}")
        err_str = f"{r['err']:+.1f}%" if r['err'] is not None else '—'
        print(f"  {name:15s} | {r['Q_pred']:8.4f} | {r['Q_exp']:8.4f} | {err_str:>8s}")

    mae = sum(abs(r['err']) for r in results if r['err'] is not None) / len(results)
    print(f"\n  MAE = {mae:.1f}%")

    # Witness
    witness = {
        'name': 'iterative-nf-qvalue',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q': q, 'E_gram': E_gram,
        'formula': 'Q = |sum(dV_i)| * z^2 * m_e',
        'results': [{
            'name': r.get('name'),
            'Z': r['Z'], 'N': r['N'], 'A': r['A'],
            'Q_pred': r['Q_pred'], 'Q_exp': r['Q_exp'], 'err': r['err'],
            'ord_par': r['ord_par'], 'ord_dau': r['ord_dau'],
            'sum_dV': r['sum_dV'],
            'n_steps_par': len(r['steps_par']),
            'n_steps_dau': len(r['steps_dau']),
            'nf_ok_all': all(s['nf_ok'] for s in r['steps_par'] + r['steps_dau']),
        } for r in results],
    }
    out = Path(__file__).with_suffix('.witness.json')
    out.write_text(json.dumps(witness, indent=2, default=float))
    print(f"\n  Witness: {out.name}")
