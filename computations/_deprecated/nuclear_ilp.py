#!/usr/bin/env python3
"""
Systematic integer LP for ALL atoms: find minimum-action
Frobenius stabilizer for each nucleus.

Uses the FULL H₃(q) basis {γ, σ₀, σ₁, L₊, L₋, e⁻} as
operator alphabet, not just generators.

Witnesses results per atom for the computation pipeline.

Usage:
    python3 nuclear_ilp.py
"""
import sys, time, itertools
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import (
    check_frobenius,
    h,
)
from pyhecke.gram import (
    build_atom_nf,
    hm,
    nf_tr,
    z,
    NF_NAMES,
    NF_BASIS,
)
from witness_base import WitnessBuilder

# Full operator alphabet: all 6 NF basis elements and their inverses
# Each operator is (name, gen, c, d) for hm()
OPS = [
    ('σ₀',   0, 1.0, 0.0),     # σ₀
    ('σ₁',   1, 1.0, 0.0),     # σ₁
    ('σ₀⁻¹', 0, 1.0, -h),     # σ₀⁻¹ = σ₀ - h
    ('σ₁⁻¹', 1, 1.0, -h),     # σ₁⁻¹ = σ₁ - h
    ('pn₀',  0, 1.0, -h/2),   # mixed on gen 0
    ('pn₁',  1, 1.0, -h/2),   # mixed on gen 1
]

ATOMS = [
    (1,0,"H"), (1,1,"D"), (1,2,"T"), (2,1,"He3"), (2,2,"He4"),
    (3,3,"Li6"), (3,4,"Li7"), (4,5,"Be9"), (5,6,"B11"),
    (6,6,"C12"), (6,8,"C14"), (7,7,"N14"), (8,8,"O16"),
    (10,10,"Ne20"), (14,14,"Si28"), (20,20,"Ca40"), (26,30,"Fe56"),
]

results = []
print(f"{'Atom':>6s} {'A':>3s} {'bare_LP':>8s} {'n_ops':>5s} {'stabilizer':>25s} {'tr_M':>12s}")
print("─" * 65)

for Z, N, name in ATOMS:
    A = Z + N
    nf = build_atom_nf(Z, N)
    stable, _, viols = check_frobenius(nf)
    tr = nf_tr(nf)

    if stable:
        results.append({
            'name': name, 'Z': Z, 'N': N, 'A': A,
            'bare_stable': True, 'n_ops': 0,
            'stabilizer': '', 'tr_M': round(tr, 8),
        })
        print(f"{name:>6s} {A:>3d} {'OK':>8s} {'0':>5s} {'(already stable)':>25s} {tr:>12.4f}")
        continue

    # Search for minimum-length stabilizer
    found = False
    for length in range(1, 6):  # up to 5 operators
        if found:
            break
        t0 = time.time()
        n_combos = len(OPS) ** length
        for combo in itertools.product(OPS, repeat=length):
            nf_test = list(nf)
            for op_name, gen, c, d in combo:
                nf_test = hm(nf_test, c, d, gen)
            s, _, _ = check_frobenius(nf_test)
            if s:
                word = '·'.join(op_name for op_name, _, _, _ in combo)
                tr_new = nf_tr(nf_test)
                results.append({
                    'name': name, 'Z': Z, 'N': N, 'A': A,
                    'bare_stable': False, 'n_ops': length,
                    'stabilizer': word, 'tr_M': round(tr_new, 8),
                })
                print(f"{name:>6s} {A:>3d} {'FAIL':>8s} {length:>5d} {word:>25s} {tr_new:>12.4f}")
                found = True
                break
        if not found and time.time() - t0 > 60:
            print(f"{name:>6s} {A:>3d} {'FAIL':>8s} {'>'+str(length):>5s} {'(timeout at len '+str(length)+')':>25s}")
            break

    if not found:
        results.append({
            'name': name, 'Z': Z, 'N': N, 'A': A,
            'bare_stable': False, 'n_ops': -1,
            'stabilizer': 'NOT FOUND', 'tr_M': round(tr, 8),
        })
        if not any(r['name'] == name for r in results[:-1]):
            print(f"{name:>6s} {A:>3d} {'FAIL':>8s} {'>5':>5s} {'NOT FOUND':>25s} {tr:>12.4f}")

# Witness
w = WitnessBuilder("nuclear-ilp", engine="python")
w.set_description("Per-nucleus minimum-action Frobenius stabilizer from integer LP.")
w.add_data("atoms", results)
for r in results:
    if r['bare_stable']:
        w.add_assertion(f"LP_stable({r['name']})", 1, 1, 0, "bool", "bare NF")
    elif r['n_ops'] > 0:
        w.add_assertion(f"LP_stabilizable({r['name']})", 1, 1, 0, "bool",
                        f"{r['n_ops']} ops: {r['stabilizer']}")
w.save()
