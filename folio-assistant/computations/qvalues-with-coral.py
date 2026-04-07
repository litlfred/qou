"""
Q-values with coral content: using the full Gröbner NF, not just
the transfer matrix (observable) part.

Key finding: for A ≥ 5, the observable (degree 0+1) is negligible
compared to coral (degree ≥ 2). The binding energy is dominated by
multi-body correlations. The current Q-value formula uses only the
observable — this is the source of the structural error.

The full NF net = observable + coral gives:
  P_full(q) = exp(net) ≈ exp(coral) for large A

So the Q-value should use net (not observable) in the log ratio.

For the benchmark nuclei, we don't have the full NF (A ≤ 12 only).
But we can compute the CORAL CORRECTION FACTOR:
  R_coral = |net(daughter)| / |net(parent)|
          ÷ |obs(daughter)| / |obs(parent)|

This ratio measures how much the coral changes the Q-value prediction
relative to the transfer-matrix-only formula.
"""

import json, glob, math, sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q
from experimental_constants import M_E_MEV

q0 = 1.10998
t0 = q0**0.5

def eval_sparse(terms, t):
    return sum(int(coeff) * t**exp for exp, coeff in terms) if terms else 0.0

def load_checkpoint(z, n):
    """Load checkpoint for nucleus (Z, N) if it exists."""
    a = z + n
    # Try various naming conventions
    syms = {1:'h',2:'he',3:'li',4:'be',5:'b',6:'c',7:'n',8:'o',9:'f',10:'ne'}
    sym = syms.get(z, '?')
    for pattern in [f'checkpoint-{a}{sym}.json', f'checkpoint-{a}{sym.upper()}.json']:
        try:
            c = json.load(open(pattern))
            if c['Z'] == z and c['N'] == n:
                return c
        except: pass
    # Search all checkpoints
    for f in glob.glob('checkpoint-*.json'):
        try:
            c = json.load(open(f))
            if c['Z'] == z and c['N'] == n:
                return c
        except: pass
    return None


def get_nf_values(z, n):
    """Get observable, coral, net values at q0 for nucleus (Z,N)."""
    c = load_checkpoint(z, n)
    if c is None:
        return None
    pn = c['pn_count']
    denom = 2.0**pn
    obs = eval_sparse(c.get('observable_coeffs', []), t0) / denom
    cor = eval_sparse(c.get('coral_coeffs', []), t0) / denom
    net = eval_sparse(c.get('net_coeffs', []), t0) / denom
    tr_alt = eval_sparse(c.get('tr_alt_coeffs', []), t0) / denom
    return {'obs': obs, 'coral': cor, 'net': net, 'tr_alt': tr_alt, 'a': c['A']}


# Check which beta-decay pairs we have data for
# β⁻: (Z,N) → (Z+1, N-1)
print("=" * 80)
print("Q-VALUES WITH CORAL CONTENT")
print("=" * 80)

# For light nuclei where we have both parent AND daughter witnesses:
print(f"\n{'Parent':>10} {'Daughter':>10} {'obs_par':>10} {'net_par':>10} {'obs_dau':>10} {'net_dau':>10} {'net_ratio':>10}")
print("-" * 80)

pairs_found = []
for z in range(1, 8):
    for n in range(z, 13 - z):
        par = get_nf_values(z, n)
        dau = get_nf_values(z + 1, n - 1)
        if par is not None and dau is not None:
            a = z + n
            # Q from observable only (current formula approximation)
            if abs(par['obs']) > 1e-30 and abs(dau['obs']) > 1e-30:
                log_obs = math.log(abs(dau['obs'])) - math.log(abs(par['obs']))
            else:
                log_obs = 0.0
            # Q from full net (observable + coral)
            if abs(par['net']) > 1e-30 and abs(dau['net']) > 1e-30:
                log_net = math.log(abs(dau['net'])) - math.log(abs(par['net']))
            else:
                log_net = 0.0

            kappa = M_E_MEV / 3.0
            q_obs = abs(log_obs) * kappa
            q_net = abs(log_net) * kappa

            syms = {1:'H',2:'He',3:'Li',4:'Be',5:'B',6:'C',7:'N',8:'O'}
            par_name = f"{a}{syms.get(z,'?')}({z},{n})"
            dau_name = f"{a}{syms.get(z+1,'?')}({z+1},{n-1})"

            pairs_found.append((z, n, par_name, dau_name, par, dau, q_obs, q_net))

            print(f"{par_name:>10} {dau_name:>10} {par['obs']:>+10.6f} {par['net']:>+10.6f} "
                  f"{dau['obs']:>+10.6f} {dau['net']:>+10.6f} "
                  f"{abs(dau['net']/par['net']) if abs(par['net'])>1e-30 else 0:>10.4f}")

# Now compare Q-values
print(f"\n{'Decay':>22} {'Q(obs)':>10} {'Q(net)':>10} {'Ratio':>8} {'Note':>20}")
print("-" * 75)
for z, n, pn, dn, par, dau, q_obs, q_net in pairs_found:
    ratio = q_net / q_obs if abs(q_obs) > 1e-30 else 0
    note = ""
    if abs(ratio - 1.0) > 0.1:
        note = f"coral shifts by {(ratio-1)*100:+.0f}%"
    print(f"{pn:>10} → {dn:>10} {q_obs:>10.5f} {q_net:>10.5f} {ratio:>8.4f} {note:>20}")

print(f"\n  Q(obs) = |ln(obs_dau/obs_par)| × κ  (transfer matrix only)")
print(f"  Q(net) = |ln(net_dau/net_par)| × κ  (full NF: observable + coral)")
print(f"  κ = m_e/3 ≈ {M_E_MEV/3:.6f} MeV")
print(f"\n  The ratio Q(net)/Q(obs) shows how much the coral content")
print(f"  changes the Q-value prediction. For A ≥ 5, the observable")
print(f"  is negligible — the Q-value is dominated by coral physics.")
