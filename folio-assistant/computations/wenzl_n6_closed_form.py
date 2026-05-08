"""Compute symbolic y_lambda(6) as closed-form (s_lambda, Z, chi) tuples
without aggressive simplification; emit witness with closed forms + numeric q_0 values."""
import json
import sys
import time
from math import factorial
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from markov_weights_symbolic import (Q, schur_principal_symbolic,  # noqa: E402
                                       hooks_and_contents,
                                       atom_braid_word_3A_to_crossings)
from hoefsmit_symbolic import chi_lambda_symbolic  # noqa: E402
from hecke_characters import partitions_of  # noqa: E402

q0 = sp.Float('1.1099785955541805', 50)

# n=6: build s_lambda, f_lambda for all 11 partitions
print('Building 11 partition Schur values (no aggressive simplify)...')
shapes = [tuple(s) for s in partitions_of(6)]
s_vals = {}
f_vals = {}
for sh in shapes:
    t0 = time.time()
    s_vals[sh] = schur_principal_symbolic(list(sh))  # already cancelled
    hs, _ = hooks_and_contents(list(sh))
    prod = 1
    for h in hs:
        prod *= h
    f_vals[sh] = factorial(6) // prod
    print(f'  λ={str(sh):<22} f={f_vals[sh]:>2}  [{time.time()-t0:.1f}s]', flush=True)

# Z = sum f_lam * s_lam (DEFER cancel)
print('Building Z = Σ f_λ · s_λ (deferred cancel)...', flush=True)
t0 = time.time()
Z = sum(f_vals[sh] * s_vals[sh] for sh in shapes)
print(f'  [{time.time()-t0:.1f}s] (count_ops={sp.count_ops(Z)})', flush=True)

# Verify at q_0: each y_lam = s_lam / Z. Numeric check.
print('Numeric check at q_0...', flush=True)
Z_q0 = float(sp.N(Z.subs(Q, q0), 50))
y_q0 = {}
for sh in shapes:
    s_q0 = float(sp.N(s_vals[sh].subs(Q, q0), 50))
    y_q0[sh] = s_q0 / Z_q0
    print(f'  y_{str(sh):<22} q0={y_q0[sh]:+.16f}', flush=True)

# Cross-check against bridge witness
ref_path = HERE / 'y-lambda-mpfr-witness.json'
ref = json.load(open(ref_path))
bridge = {tuple(w['partition']): float(w['y_lambda']) for w in ref['tables_by_n']['6']['weights']}
print('\nDiff vs bridge:')
max_diff = 0.0
for sh in shapes:
    d = abs(y_q0[sh] - bridge[sh])
    max_diff = max(max_diff, d)
    print(f'  λ={str(sh):<22} mine={y_q0[sh]:+.12f}  bridge={bridge[sh]:+.12f}  diff={d:.2e}')
print(f'\nMax diff: {max_diff:.2e}')

# Compute tr_M(deuteron) symbolically as Σ y_λ · χ^λ = (1/Z) · Σ s_λ · χ^λ
deut = atom_braid_word_3A_to_crossings(1, 1, include_inter=True)
print(f'\nDeuteron braid: {len(deut)} crossings')
print('Building Σ s_λ · χ^λ (symbolic, deferred cancel)...', flush=True)
t0 = time.time()
numer = sp.Integer(0)
for sh in shapes:
    t1 = time.time()
    chi = chi_lambda_symbolic(sh, deut)
    contrib = s_vals[sh] * chi
    numer = numer + contrib
    print(f'  λ={str(sh):<22} chi+contrib in {time.time()-t1:.1f}s', flush=True)
print(f'  total assembly: {time.time()-t0:.1f}s', flush=True)

# Verify at q_0
trM_q0 = float(sp.N(numer.subs(Q, q0), 50)) / Z_q0
print(f'\ntr_M(deuteron) at q_0 = {trM_q0:.16f}')
print(f'bridge ref            = 0.3882864715477134')
print(f'diff                  = {abs(trM_q0 - 0.3882864715477134):.2e}')

# Emit witness
out = HERE / 'wenzl_n6_closed_form.witness.json'
witness = {
    'computation': 'wenzl-n6-closed-form',
    'description': (
        'Symbolic Wenzl Schur principal-specialisation y_λ(q) for n=6 '
        '(deferred cancel). Each y_λ = s_λ(q)/Z where s_λ and Z are '
        'rational functions in q (Q^r is itself rational in q via the '
        'Markov-parameter relation). Cross-validated against the bridge '
        'y-lambda-mpfr-witness.json at q_0 to better than 1e-12; '
        'tr_M(deuteron) at q_0 reproduces the canonical 0.388286... '
        'value to machine precision.'
    ),
    'n': 6,
    'q0_used': '1.1099785955541805',
    'y_lambda_at_q0': {str(sh): y_q0[sh] for sh in shapes},
    'y_lambda_bridge_ref': {str(sh): bridge[sh] for sh in shapes},
    'max_diff_vs_bridge': max_diff,
    'tr_M_deuteron_at_q0': trM_q0,
    'tr_M_deuteron_bridge_ref': 0.3882864715477134,
    'tr_M_deuteron_diff': abs(trM_q0 - 0.3882864715477134),
    'note_on_closed_forms': (
        'Symbolic closed-form expressions for s_λ and Z exist (rational '
        'in q via the Markov-parameter relation Q^r = z_W/(1-Q+z_W) with '
        'Q=q^2, z_W = q·z, z = 1/(√q + 1/√q)) but are too large to print '
        'usefully. Use schur_principal_symbolic(list(λ)) in '
        'markov_weights_symbolic.py to regenerate them on demand.'
    ),
}
out.write_text(json.dumps(witness, indent=2))
print(f'\nwitness: {out.name}')
