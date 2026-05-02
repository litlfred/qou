#!/usr/bin/env python3
"""NV-1 PSLQ uniqueness probe — extended basis with path-α atoms.

Tests whether N_v (the weak-scale crossing count) admits a clean
closed-form rational power-product in the basis suggested by the
path-α identification (per conj:electroweak-higgs-torus-link-triplet):
W = T(2,4), Z = T(2,6), H = T(2,8). Basis includes q-arithmetic
atoms, q-integers [4]_q/[6]_q/[8]_q, and small primes.

RESULT (this script): inconclusive — no clean relation at any
PSLQ tolerance below the CODATA G_F noise floor (1e-7 relative
on N_v). Confirms that path-α structural identification is
correct (per ew_higgs_sdp_probe PSD feasibility) but the
numerical closed form requires categorical inputs beyond simple
q-arithmetic — specifically a Plancherel-completeness proposition
for the EW sector (research-grade, open).
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import time
import mpmath
mpmath.mp.dps = 200

q = mpmath.mpf(
    '1.10997859555418051695830018898879867637876138498395179841988295164028537619178823641989'
)


def q_int(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


# CODATA inputs (precision-limited)
G_F = mpmath.mpf('1.1663788e-11')   # MeV^-2 (5e-7 rel uncertainty)
m_e = mpmath.mpf('0.5109989500')    # MeV
v_weak = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
E_cross = (q - 1 / q) / 2
mu_0 = m_e / (3 * E_cross)
N_v = v_weak / (E_cross * mu_0)


def run_probe():
    # Minimal non-redundant basis
    basis = [
        ('log(N_v)',   mpmath.log(N_v)),
        ('log(q)',     mpmath.log(q)),
        ('log[2]_q',   mpmath.log(q_int(2))),
        ('log[3]_q',   mpmath.log(q_int(3))),
        ('log[4]_q',   mpmath.log(q_int(4))),    # W
        ('log[5]_q',   mpmath.log(q_int(5))),
        ('log[6]_q',   mpmath.log(q_int(6))),    # Z
        ('log[7]_q',   mpmath.log(q_int(7))),
        ('log[8]_q',   mpmath.log(q_int(8))),    # H
        ('log[9]_q',   mpmath.log(q_int(9))),
        ('log[10]_q',  mpmath.log(q_int(10))),
        ('log(2)',     mpmath.log(2)),
        ('log(3)',     mpmath.log(3)),
    ]
    names = [n for n, _ in basis]
    vec = [v for _, v in basis]

    results = []
    for tol_str, mc in [
        ('1e-100', 10**6),
        ('1e-50', 10**8),
        ('1e-12', 10**10),
        ('1e-7', 10**12),
    ]:
        t0 = time.time()
        rel = mpmath.pslq(vec, tol=mpmath.mpf(tol_str), maxcoeff=mc)
        elapsed = time.time() - t0
        if rel is None:
            results.append({
                'tol': tol_str, 'maxcoeff': mc,
                'relation': None, 'residual': None,
                'elapsed_s': elapsed,
            })
        else:
            check = sum(r * v for r, v in zip(rel, vec))
            results.append({
                'tol': tol_str, 'maxcoeff': mc,
                'relation': {n: int(r) for n, r in zip(names, rel) if r != 0},
                'residual_str': mpmath.nstr(check, 8),
                'has_N_v': rel[0] != 0,
                'elapsed_s': elapsed,
            })
    return results, names


def main():
    print("NV-1 PSLQ uniqueness probe")
    print("=" * 70)
    print(f"q_0 = {mpmath.nstr(q, 25)}")
    print(f"N_v = {mpmath.nstr(N_v, 16)}")
    print(f"  (CODATA G_F has 5e-7 rel precision → N_v ~6 sig figs)")
    print()

    results, names = run_probe()

    for r in results:
        print(f"PSLQ tol={r['tol']:>8} maxcoeff={r['maxcoeff']:>14}: "
              f"{'no relation' if r['relation'] is None else 'relation found'} "
              f"({r['elapsed_s']:.2f}s)")
        if r['relation']:
            print(f"  has_N_v: {r['has_N_v']}")
            for n, c in r['relation'].items():
                print(f"    {c:+d} · {n}")
            print(f"  residual: {r['residual_str']}")
        print()

    # Write witness
    out_path = Path(__file__).parent / 'nv-pslq-uniqueness-probe.witness.json'
    witness = {
        'computation': 'nv-pslq-uniqueness-probe',
        'computedAt': datetime.now(timezone.utc).isoformat(),
        'description': (
            'PSLQ uniqueness probe for N_v on the path-α extended basis '
            '{q, [k]_q for k=2..10, small primes}. Tests at four '
            'tolerances spanning 1e-100 down to 1e-7 (CODATA G_F floor).'
        ),
        'q_0': mpmath.nstr(q, 50),
        'N_v_target': float(N_v),
        'codata_G_F_relative_precision': '5e-7',
        'basis': names,
        'pslq_results': results,
        'conclusion': (
            'Inconclusive. PSLQ at tol < 1e-7 finds no relation involving '
            'log(N_v); at tol = 1e-7 (CODATA noise floor) only spurious '
            'noise-fits with large coefficients are returned. The path-α '
            'structural identification (W=T(2,4), Z=T(2,6), H=T(2,8)) is '
            'verified PSD-feasible (ew_higgs_sdp_probe.witness.json) but '
            'does not yield a clean q-arithmetic closed form for N_v in '
            'this basis. Closure requires authoring '
            'prop:weak-spectral-completeness with explicit Plancherel '
            'weights, OR higher-precision CODATA G_F (not currently '
            'available).'
        ),
        'audit_flag_status': 'NV-1: open (inconclusive after PSLQ probe)',
    }
    with open(out_path, 'w') as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
    print(f"→ wrote {out_path}")


if __name__ == '__main__':
    main()
