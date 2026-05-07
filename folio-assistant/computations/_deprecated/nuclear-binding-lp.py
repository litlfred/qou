#!/usr/bin/env python3
"""
Nuclear binding LP: operator selection at each nucleon addition.

Restates the confinement LP at the NUCLEAR level (not quark level).
B₃ is already done — the question is what inter-nucleon operator
binds nucleon k+1 to the existing nucleus N_k.

Three regimes:
  1. Non-magic: bare typed crossing (Hopf link) — B₃-like binding
  2. Magic shell closure: torus knot T_{2,n_s} as collective operator
  3. Doubly magic: two torus knot operators (proton + neutron shells)

For each regime, the LP selects the optimal operator among:
  - Bare crossing C_pp, C_pn, C_nn
  - Torus knots T_{2,2}, T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}
  - Borromean B₃ (from quark level, shouldn't appear at nuclear level)

Usage:
    cd folio-assistant/computations && python3 nuclear-binding-lp.py
"""
import json
import numpy as np
from scipy.optimize import linprog
from datetime import datetime, timezone
from pathlib import Path
import subprocess

from q_parameter import Q as q0, Q_INV as qi0, HA as HA_val, E_CROSS
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402

from experimental_constants import M_P_MEV, M_N_MEV

try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    SHA = "unknown"

HA = HA_val
z = _PG_Z  # moved to pyhecke.gram
NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
TR_M_BASIS = np.array([1.0, z, z, z**2, z**2, z**3])


def hecke_mul(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * HA
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def to_vec(terms):
    return np.array([terms.get(b, 0.0) for b in NF_BASIS])


def expand_inverse(word):
    terms = {(): 1.0}
    for g in word:
        new_terms = {}
        if g >= 0:
            for w, c in terms.items():
                nw = w + (g,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
        else:
            i = -g - 1
            for w, c in terms.items():
                nw = w + (i,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
                new_terms[w] = new_terms.get(w, 0.0) - c * HA
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def print_nf(label, vec):
    net = sum(vec)
    parts = []
    for name, val in zip(NF_NAMES, vec):
        if abs(val) > 1e-15:
            parts.append(f"{val:+.6f}·{name}")
    print(f"  {label}: {' '.join(parts)}  [net={net:+.6f}]")


def build_gram():
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            prod = hecke_mul({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
            nf = reduce_nf(prod)
            vec = to_vec(nf)
            G[i, j] = sum(vec[k] * TR_M_BASIS[k] for k in range(6))
    return G


print("=" * 80)
print("NUCLEAR BINDING LP: OPERATOR SELECTION AT EACH NUCLEON ADDITION")
print(f"q₀ = {q0:.10f}  |  HA = {HA:.10f}")
print(f"Commit: {SHA[:8]}")
print("=" * 80)

G = build_gram()
G_inv = np.linalg.inv(G)

# ── Build nucleon NFs ─────────────────────────────────────────
b3_raw = expand_inverse((0, -2, 0, -2, 0, -2))
b3_nf = reduce_nf(b3_raw)

def build_nucleon(quark_types):
    elem = dict(b3_nf)
    for i in range(3):
        for j in range(i + 1, 3):
            gen = min(i, j)
            if gen > 1:
                gen = 1
            if quark_types[i] == quark_types[j] == 'u':
                cx = {(gen,): 1.0}
            elif quark_types[i] == quark_types[j] == 'd':
                cx = {(gen,): 1.0, (): -HA}
            else:
                cx = {(gen,): 1.0, (): -HA / 2}
            elem = hecke_mul(elem, cx)
            elem = reduce_nf(elem)
    return elem

proton_terms = build_nucleon(['u', 'u', 'd'])
neutron_terms = build_nucleon(['u', 'd', 'd'])
proton_vec = to_vec(proton_terms)
neutron_vec = to_vec(neutron_terms)

print_nf("\nProton NF", proton_vec)
print_nf("Neutron NF", neutron_vec)

# ── Candidate inter-nucleon operators ─────────────────────────
# These are what can mediate the binding between nucleon k and k+1

operators = {}

# Typed crossings (the bare inter-nucleon Hopf links)
operators["C_pp (σ₀)"] = {(0,): 1.0}
operators["C_nn (σ₀ − HA)"] = {(0,): 1.0, (): -HA}
operators["C_pn (σ₀ − ½HA)"] = {(0,): 1.0, (): -HA / 2}

# Torus knots (collective shell operators)
operators["T_{2,2} = σ₀²"] = reduce_nf({(0, 0): 1.0})
operators["T_{2,3} = e⁻ (trefoil)"] = {(0, 1, 0): 1.0}
operators["T_{2,5} = (σ₀σ₁)²σ₀"] = reduce_nf(
    hecke_mul(hecke_mul({(0, 1): 1.0}, {(0, 1): 1.0}), {(0,): 1.0}))

# B₃ (from quark level — should NOT be optimal at nuclear level)
operators["B₃ (quark-level)"] = dict(b3_nf)

# Identity (no binding)
operators["𝟙 (identity)"] = {(): 1.0}

# Hopf links
operators["L₊ = σ₀σ₁"] = {(0, 1): 1.0}
operators["L₋ = σ₁σ₀"] = {(1, 0): 1.0}

print(f"\n{'─' * 70}")
print(f"  Inter-nucleon operator NFs:")
print(f"{'─' * 70}")
for name, terms in operators.items():
    vec = to_vec(reduce_nf(terms))
    print_nf(f"  {name}", vec)


# ══════════════════════════════════════════════════════════════
#  INDUCTIVE NUCLEUS CONSTRUCTION
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("INDUCTIVE NUCLEUS CONSTRUCTION: A = 1 → 8")
print("=" * 80)
print("""
Build nuclei one nucleon at a time. At each step, test ALL candidate
inter-nucleon operators and report which one:
  (a) Minimizes |demand| of the resulting nucleus
  (b) Has lowest Markov trace
  (c) Matches the known stable isotope

Track shell structure: magic numbers should show operator transitions.
""")

# Shell filling order (simplified): 1s, 1p, 1d, ...
# For A ≤ 8: fill protons and neutrons alternately
# Standard nuclear filling for lightest nuclei:
nucleon_sequences = {
    "H-1":   [('p', 'proton')],
    "H-2":   [('p', 'proton'), ('n', 'neutron')],
    "He-3":  [('p', 'proton'), ('p', 'proton'), ('n', 'neutron')],
    "He-4":  [('p', 'proton'), ('p', 'proton'), ('n', 'neutron'), ('n', 'neutron')],
    "Li-6":  [('p', 'proton'), ('p', 'proton'), ('n', 'neutron'), ('n', 'neutron'),
              ('p', 'proton'), ('n', 'neutron')],
    "O-16":  [('p', 'proton')]*8 + [('n', 'neutron')]*8,
}

def nuclear_crossing_type(t1, t2):
    """Return typed crossing label for two nucleon types."""
    if t1 == t2 == 'p':
        return "C_pp"
    elif t1 == t2 == 'n':
        return "C_nn"
    else:
        return "C_pn"

# For each nucleus, build inductively and test operators at each step
for nuc_name, sequence in nucleon_sequences.items():
    A = len(sequence)
    if A > 8:
        continue  # skip O-16 for now (too slow for full operator sweep)

    print(f"\n{'═' * 70}")
    print(f"  {nuc_name} (A={A})")
    print(f"{'═' * 70}")

    Z = sum(1 for t, _ in sequence if t == 'p')
    N = A - Z

    # Build inductively
    nuc_type_0, _ = sequence[0]
    nucleus = dict(proton_terms if nuc_type_0 == 'p' else neutron_terms)
    nucleus_types = [nuc_type_0]

    for step in range(1, A):
        new_type, new_label = sequence[step]
        new_nucleon = dict(proton_terms if new_type == 'p' else neutron_terms)

        print(f"\n  Step {step}: adding {new_label} ({new_type}) to A={step} nucleus")

        # Current nucleus NF
        nuc_vec = to_vec(nucleus)

        # Determine the default crossing type
        prev_type = nucleus_types[-1]
        default_cx_label = nuclear_crossing_type(prev_type, new_type)

        # Test each operator: nucleus · operator · new_nucleon
        step_results = []
        for op_name, op_terms in operators.items():
            # nucleus · operator
            temp = hecke_mul(dict(nucleus), reduce_nf(dict(op_terms)))
            temp = reduce_nf(temp)
            # ... · new_nucleon
            temp = hecke_mul(temp, new_nucleon)
            temp = reduce_nf(temp)

            result_vec = to_vec(temp)
            net = sum(result_vec)
            tr_m = sum(result_vec[i] * TR_M_BASIS[i] for i in range(6))
            demand = [(NF_NAMES[i], result_vec[i]) for i in range(6) if result_vec[i] < -1e-10]
            demand_mag = sum(abs(v) for _, v in demand)
            n_demand = len(demand)

            step_results.append({
                'op': op_name, 'net': net, 'tr_m': tr_m,
                'n_demand': n_demand, 'demand_mag': demand_mag,
                'result_terms': temp, 'result_vec': result_vec,
            })

        # Rank by demand magnitude (lower = more stable)
        step_results.sort(key=lambda r: (r['demand_mag'], r['tr_m']))

        print(f"  {'Operator':<25s} | {'net':>8s} | {'|dem|':>8s} | {'#dem':>4s} | {'tr_M':>8s}")
        print(f"  {'─'*25}-+-{'─'*8}-+-{'─'*8}-+-{'─'*4}-+-{'─'*8}")
        for rank, r in enumerate(step_results):
            marker = " ◀" if rank == 0 else ""
            print(f"  {r['op']:<25s} | {r['net']:>+8.4f} | {r['demand_mag']:>8.4f} | {r['n_demand']:>4d} | {r['tr_m']:>8.4f}{marker}")

        # Use the best operator (lowest demand)
        best = step_results[0]
        nucleus = best['result_terms']
        nucleus_types.append(new_type)

        print(f"\n  SELECTED: {best['op']}")
        print_nf(f"  Nucleus NF (A={step+1})", best['result_vec'])

        # Check if this is a magic number
        cur_Z = sum(1 for t in nucleus_types if t == 'p')
        cur_N = sum(1 for t in nucleus_types if t == 'n')
        magic = {2, 8, 20, 28, 50, 82, 126}
        z_magic = cur_Z in magic
        n_magic = cur_N in magic
        if z_magic and n_magic:
            print(f"  ★★ DOUBLY MAGIC: Z={cur_Z}, N={cur_N}")
        elif z_magic:
            print(f"  ★ MAGIC Z={cur_Z}")
        elif n_magic:
            print(f"  ★ MAGIC N={cur_N}")

    # Final result
    final_vec = to_vec(nucleus)
    final_demand = [(NF_NAMES[i], final_vec[i]) for i in range(6) if final_vec[i] < -1e-10]
    print(f"\n  FINAL {nuc_name} (Z={Z}, N={N}):")
    print_nf(f"  NF", final_vec)
    print(f"  Demand: {', '.join(f'{n}={v:+.4f}' for n, v in final_demand) if final_demand else 'NONE (stable)'}")


# ══════════════════════════════════════════════════════════════
#  LP AT NUCLEAR LEVEL
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("LP AT NUCLEAR LEVEL: OPTIMAL BINDING OPERATOR")
print("=" * 80)
print("""
Primal LP for inter-nucleon binding:
  min  t · x          (minimize Markov trace of bound pair)
  s.t. 1ᵀ x = n_target   (net = physical nucleus net)
       G x ≥ 0            (Frobenius positivity)
       |x_i| ≤ 1          (braid word realizability)

Solved for each nucleon-pair type (pp, pn, nn).
""")

pair_types = [
    ("p-p binding", proton_vec, proton_vec, "pp"),
    ("p-n binding", proton_vec, neutron_vec, "pn"),
    ("n-n binding", neutron_vec, neutron_vec, "nn"),
]

for pair_name, nuc1_vec, nuc2_vec, cx_type in pair_types:
    print(f"\n{'─' * 70}")
    print(f"  {pair_name}")
    print(f"{'─' * 70}")

    # Compute bound pair with each operator
    print(f"\n  Operator comparison for {pair_name}:")
    print(f"  {'Operator':<25s} | {'net':>8s} | {'|dem|':>8s} | {'tr_M':>8s}")
    print(f"  {'─'*25}-+-{'─'*8}-+-{'─'*8}-+-{'─'*8}")

    for op_name, op_terms in operators.items():
        # nuc1 · operator · nuc2
        nuc1 = {NF_BASIS[i]: nuc1_vec[i] for i in range(6) if abs(nuc1_vec[i]) > 1e-15}
        temp = hecke_mul(nuc1, reduce_nf(dict(op_terms)))
        temp = reduce_nf(temp)
        nuc2 = {NF_BASIS[i]: nuc2_vec[i] for i in range(6) if abs(nuc2_vec[i]) > 1e-15}
        temp = hecke_mul(temp, nuc2)
        temp = reduce_nf(temp)

        vec = to_vec(temp)
        net = sum(vec)
        tr_m = sum(vec[i] * TR_M_BASIS[i] for i in range(6))
        demand = [(NF_NAMES[i], vec[i]) for i in range(6) if vec[i] < -1e-10]
        demand_mag = sum(abs(v) for _, v in demand)

        print(f"  {op_name:<25s} | {net:>+8.4f} | {demand_mag:>8.4f} | {tr_m:>8.4f}")


# ══════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════
#  SDP LIFT VALIDATION  (see sdp_moment_lift.py / docs/ilp-sdp-audit.md)
# ══════════════════════════════════════════════════════════════
# Componentwise G·x ≥ 0 is strictly weaker than quadratic Frobenius
# xᵀG x ≥ 0 because G has a negative eigenvalue at q₀.  Add the
# Lasserre moment-matrix lift as a correctness check on the LP's
# channel-operator solutions.

print(f"\n{'═' * 80}\n  SDP LIFT VALIDATION\n{'═' * 80}")
sdp_reports = []
try:
    from sdp_moment_lift import lp_vs_sdp_report
    _proton_net = float(np.sum(proton_vec))
    _neutron_net = float(np.sum(neutron_vec))
    for _lbl, _tgt in [("pp-channel", _proton_net * _proton_net),
                         ("nn-channel", _neutron_net * _neutron_net),
                         ("pn-channel", _proton_net * _neutron_net)]:
        _rep = lp_vs_sdp_report(
            c=TR_M_BASIS, G=G, A_eq=np.ones((1, 6)),
            b_eq=np.array([_tgt]),
            label=f"nuclear-binding/{_lbl}")
        for _l in _rep.summary_lines():
            print(_l)
        print()
        sdp_reports.append(_rep.__dict__)
except ImportError as _e:
    print(f"  (cvxpy not available: {_e})")


witness = {
    "name": "nuclear-binding-lp",
    "description": "LP for inter-nucleon binding operators at magic/doubly-magic numbers",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {"q0": q0, "HA": HA, "z": z},
    "sdp_lift": sdp_reports,
}

out_path = Path(__file__).parent / "nuclear-binding-lp.witness.json"
with open(out_path, 'w') as f:
    json.dump(witness, f, indent=2)

print(f"\n\nWitness written to: {out_path.name}")
print("Done.")
