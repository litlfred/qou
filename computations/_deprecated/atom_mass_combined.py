#!/usr/bin/env python3
"""
COMBINED MASS: atomic Φ + F_Pauli corrections.

Three methods compared:
  M1: atomic Φ only (0.199% baseline)
  M2: atomic Φ + nuclear F_Pauli (from certificates)
  M3: atomic Φ + atomic F_Pauli (from Rust NF, small atoms only)

The atomic Φ captures electron binding. The F_Pauli captures
Gram character (alternating trace / net) from the full NF.

Usage:
    python3 folio-assistant/computations/atom_mass_combined.py
"""

import math, sys, json, time, subprocess
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q_SQ
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder

HA = q0 - 1.0 / q0
z_m = 1.0 / (q0**0.5 + q0**(-0.5))
RUST_BIN = Path(__file__).parent.parent.parent / "tools" / "hecke-engine" / "target" / "release" / "hecke-atomic"
CERT_DIR = Path(__file__).parent.parent.parent / "tools" / "hecke-engine"


def crossing_coeff(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    if ti == 'n' and tj == 'n': return 1.0, -HA
    if (ti, tj) in [('p','n'),('n','p')]: return 1.0, -HA/2
    if (ti, tj) in [('p','e'),('e','p')]: return 1.0, -HA
    if (ti, tj) in [('n','e'),('e','n')]: return 0.0, 1.0
    if ti == 'e' and tj == 'e': return 1.0, 0.0
    return 0.0, 1.0


def compute_Phi(ordering):
    n = len(ordering)
    if n <= 1: return 0.0
    Phi = 0.0
    for gen in range(n - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, n):
            c, d = crossing_coeff(ordering[gen], ordering[j])
            if c == 0.0 and d == 1.0: continue
            a, b = a * c * HA + a * d + b * c, a * c + b * d
        V = z_m * a + b
        if abs(V) < 1e-300: return float('inf')
        Phi += math.log(abs(V))
    return Phi


def find_nuclear_gs(Z, N):
    A = Z + N
    if A <= 1: return list('p' * Z + 'n' * N)
    total = math.comb(A, Z)
    if total <= 50000:
        best_Phi, best_o = float('inf'), None
        for pos in combinations(range(A), Z):
            o = ['n'] * A
            for p in pos: o[p] = 'p'
            Phi = compute_Phi(o)
            if Phi < best_Phi: best_Phi, best_o = Phi, list(o)
        return best_o
    o = list('p' * Z + 'n' * N)
    Phi = compute_Phi(o)
    improved = True
    while improved:
        improved = False
        for pi in [i for i in range(A) if o[i] == 'p']:
            for ni in [i for i in range(A) if o[i] == 'n']:
                o[pi], o[ni] = 'n', 'p'
                new_Phi = compute_Phi(o)
                if new_Phi < Phi - 1e-12:
                    Phi = new_Phi; improved = True; break
                o[pi], o[ni] = 'p', 'n'
            if improved: break
    return o


def insert_electrons(nuclear_ordering, Z):
    current = list(nuclear_ordering)
    for _ in range(Z):
        best_pos, best_Phi = 0, float('inf')
        for pos in range(len(current) + 1):
            candidate = list(current)
            candidate.insert(pos, 'e')
            Phi = compute_Phi(candidate)
            if Phi < best_Phi:
                best_Phi = Phi
                best_pos = pos
        current.insert(best_pos, 'e')
    return current


def load_nuclear_fp(Z, N):
    names = {1:'h',2:'he',3:'li',4:'be',5:'b',6:'c',7:'n',8:'o',
             9:'f',10:'ne',11:'na',12:'mg',13:'al',14:'si',15:'p',
             16:'s',17:'cl',18:'ar',19:'k',20:'ca'}
    sym = names.get(Z, f'z{Z}')
    A = Z + N
    for pat in [f"certificate-{A}{sym}.json"]:
        fpath = CERT_DIR / pat
        if fpath.exists():
            try:
                d = json.load(open(fpath))
                return d.get('f_pauli_f64', None)
            except: pass
    return None


def run_atomic_nf(ordering, timeout_s=120):
    """Run Rust hecke-atomic for exact NF. Returns (f_pauli, nf_words) or None."""
    if not RUST_BIN.exists(): return None
    z_count = ordering.count('p')
    n_count = ordering.count('n')
    try:
        result = subprocess.run(
            [str(RUST_BIN), str(z_count), str(n_count), ordering],
            capture_output=True, text=True, timeout=timeout_s)
        fp, nw = None, None
        for line in result.stdout.split('\n'):
            if 'f_pauli' in line and '=' in line:
                fp = float(line.split('=')[1].strip())
            if 'NF words' in line:
                parts = line.split()
                for i, p in enumerate(parts):
                    if p == 'NF': nw = int(parts[i-1])
        return (fp, nw) if fp is not None else None
    except: return None


# ══════════════════════════════════════════════════════════════

ATOMS = [
    (1, 0, "H",  938.783),
    (2, 2, "He", 3728.401),
    (3, 4, "Li", 6535.367),
    (4, 5, "Be", 8394.794),
    (5, 6, "B",  10255.103),
    (6, 6, "C",  11177.930),
    (7, 7, "N",  13043.781),
    (8, 8, "O",  14899.169),
    (9, 10,"F",  17696.901),
    (10,10,"Ne", 18622.835),
    (11,12,"Na", 21414.830),
    (12,12,"Mg", 22341.908),
    (13,14,"Al", 25133.143),
    (14,14,"Si", 26060.344),
    (15,16,"P",  28851.873),
    (16,16,"S",  29781.800),
    (17,18,"Cl", 32573.283),
    (18,22,"Ar", 37224.719),
    (19,20,"K",  36294.464),
    (20,20,"Ca", 37213.777),
]

# Atomic orderings where exact NF is feasible (≤12 strands)
ATOMIC_NF_FEASIBLE = {
    'H':  'ep',
    'He': 'epepnn',       # 6 strands
    'Li': 'epenpenpnn',   # 10 strands
    'Be': 'eepepppnnnnn', # 12 strands (3e version)
}

print("=" * 120)
print("COMBINED MASS: atomic Φ + F_Pauli corrections")
print(f"q₀ = {q0:.10f}   HA = {HA:.10f}")
print("=" * 120)

# Phase 1: Compute all Φ values and load certificates
results = []
for Z, N, sym, M_obs in ATOMS:
    A = Z + N
    t0 = time.time()

    nuc_ord = find_nuclear_gs(Z, N)
    Phi_nuc = compute_Phi(nuc_ord)

    atom_ord = insert_electrons(nuc_ord, Z)
    Phi_atom = compute_Phi(atom_ord)
    atom_str = ''.join(atom_ord)

    F_nuc = load_nuclear_fp(Z, N)
    elapsed = time.time() - t0

    r = {
        'Z': Z, 'N': N, 'A': A, 'sym': sym, 'M_obs': M_obs,
        'Phi_nuc': Phi_nuc, 'Phi_atom': Phi_atom,
        'atom_ord': atom_str,
        'F_nuc': F_nuc, 'F_atom': None, 'nf_atom': None,
    }
    results.append(r)
    fp_str = f"F_nuc={F_nuc:.4f}" if F_nuc else "no cert"
    print(f"  {A:>2d}{sym:>3s}: Φ_atom={Phi_atom:>+10.4f}  {fp_str:>20s}  [{elapsed:.1f}s]")

# Phase 2: Compute atomic F_Pauli for small atoms
print(f"\nComputing atomic F_Pauli (exact NF, no stripping)...")
for r in results:
    if r['sym'] in ATOMIC_NF_FEASIBLE:
        ordering = ATOMIC_NF_FEASIBLE[r['sym']]
        timeout_s = 30 if len(ordering) <= 10 else 120
        print(f"  {r['sym']}: {ordering} ({len(ordering)} strands)...", end=" ", flush=True)
        nf = run_atomic_nf(ordering, timeout_s)
        if nf:
            r['F_atom'] = nf[0]
            r['nf_atom'] = nf[1]
            print(f"F_atom={nf[0]:.4f}, {nf[1]} NF words")
        else:
            print("timeout/error")

# Phase 3: Mass predictions
print("\n" + "=" * 120)
print("MASS PREDICTIONS (calibration: H + C)")
print("=" * 120)

def predict_masses(method_name, phi_func, correction_func=None, cal_atoms=['H', 'C']):
    """Compute mass predictions with optional correction term."""
    r_cal = {sym: r for r in results for sym in cal_atoms if r['sym'] == sym}

    # Simple case: M = M_free + α·Φ + β·correction
    # Calibrate α from cal_atoms
    from numpy import array, linalg
    cal_rows = []
    cal_rhs = []
    for sym in cal_atoms:
        r = r_cal[sym]
        M_free = r['Z'] * M_P_MEV + r['N'] * M_N_MEV + r['Z'] * M_E_MEV
        phi = phi_func(r)
        corr = correction_func(r) if correction_func else 0.0
        if phi is None or corr is None: return None
        cal_rows.append([phi, corr] if correction_func else [phi])
        cal_rhs.append(r['M_obs'] - M_free)

    A_mat = array(cal_rows)
    b_vec = array(cal_rhs)
    try:
        if correction_func:
            params = linalg.lstsq(A_mat, b_vec, rcond=None)[0]
            alpha, beta = params[0], params[1]
        else:
            # Single parameter
            alpha = sum(b_vec) / sum(A_mat[:, 0])
            beta = 0.0
    except: return None

    print(f"\n  {method_name}: α={alpha:.4f}" + (f", β={beta:.4f}" if correction_func else ""))
    print(f"  {'Atom':>6s} | {'M_pred':>12s} | {'M_obs':>12s} | {'Δ%':>8s} | {'Φ':>10s}" +
          (f" | {'corr':>10s}" if correction_func else ""))
    print(f"  {'─'*70}")

    errors = []
    for r in results:
        M_free = r['Z'] * M_P_MEV + r['N'] * M_N_MEV + r['Z'] * M_E_MEV
        phi = phi_func(r)
        corr = correction_func(r) if correction_func else 0.0
        if phi is None: phi = 0.0
        if corr is None: corr = 0.0
        M_pred = M_free + alpha * phi + beta * corr
        delta_pct = (M_pred - r['M_obs']) / r['M_obs'] * 100
        is_cal = " CAL" if r['sym'] in cal_atoms else ""
        corr_str = f" | {corr:>+10.4f}" if correction_func else ""
        print(f"  {r['A']:>2d}{r['sym']:>4s} | {M_pred:>12.3f} | {r['M_obs']:>12.3f} | {delta_pct:>+7.3f}% | {phi:>+10.4f}{corr_str}{is_cal}")
        if r['sym'] not in cal_atoms:
            errors.append(abs(delta_pct))

    if errors:
        mean_err = sum(errors) / len(errors)
        max_err = max(errors)
        print(f"  {len(errors)} predictions: mean = {mean_err:.4f}%, max = {max_err:.4f}%")
        return mean_err
    return None

# M1: Atomic Φ only
predict_masses("Atomic Φ", lambda r: r['Phi_atom'])

# M2: Nuclear Φ + ln(F_nuc) (previous best)
def ln_F_nuc(r):
    f = r.get('F_nuc')
    if f and f > 0: return math.log(f)
    return 0.0
predict_masses("Nuclear Φ + ln(F_nuc)", lambda r: r['Phi_nuc'], ln_F_nuc)

# M3: Atomic Φ + ln(F_nuc)
predict_masses("Atomic Φ + ln(F_nuc)", lambda r: r['Phi_atom'], ln_F_nuc)

# M4: Atomic Φ + F_nuc directly
def F_nuc_direct(r):
    f = r.get('F_nuc')
    return f if f else 1.0
predict_masses("Atomic Φ + F_nuc", lambda r: r['Phi_atom'], F_nuc_direct)

# M5: Atomic Φ + ln(F_atom) for small atoms (He calibration)
def ln_F_atom(r):
    f = r.get('F_atom')
    if f and f > 0: return math.log(f)
    return None

has_atom_fp = [r for r in results if r['F_atom'] is not None and r['sym'] not in ['H']]
if len(has_atom_fp) >= 2:
    # Use He and Li as calibration (both have atomic F_Pauli)
    predict_masses("Atomic Φ + ln(F_atom)", lambda r: r['Phi_atom'], ln_F_atom,
                   cal_atoms=['He', 'C'])

# Summary table
print("\n" + "=" * 120)
print("ATOMIC NF SUMMARY")
print("=" * 120)
print(f"  {'Atom':>6s} | {'NF_nuc':>8s} | {'F_nuc':>10s} | {'NF_atom':>8s} | {'F_atom':>10s} | {'atom_ordering'}")
print(f"  {'─'*90}")
for r in results:
    nf_nuc = "—"
    nf_atom = str(r['nf_atom']) if r['nf_atom'] else "—"
    f_nuc = f"{r['F_nuc']:.4f}" if r['F_nuc'] else "—"
    f_atom = f"{r['F_atom']:.4f}" if r['F_atom'] else "—"
    atom_str = r['atom_ord'][:40]
    print(f"  {r['A']:>2d}{r['sym']:>4s} | {nf_nuc:>8s} | {f_nuc:>10s} | {nf_atom:>8s} | {f_atom:>10s} | {atom_str}")

# Witness
w = WitnessBuilder("atom-mass-combined", engine="v12-atomic+v11-nuclear")
w.set_description("Combined atomic Φ + F_Pauli mass prediction")
w.save()
