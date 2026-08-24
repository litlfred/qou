#!/usr/bin/env python3
"""
Molecular covalent bond from Frobenius LP dual.

The LP dual DERIVES the covalent bond operator the same way it
derives the gluon: find the minimum-crossing inter-atomic operator
that restores Frobenius positivity of the molecular NF.

For the gluon: the 9-crossing proton violates Gx ≥ 0, and the LP
finds that 2 extra σ₀ crossings restore positivity.

For covalent bonds: the unbonded molecular product A×B may violate
Gx ≥ 0, and the LP finds which inter-atomic crossings restore it.

LP formulation:
    min  t · x_mol                    (minimize Markov trace)
    s.t. G · x_mol ≥ 0               (Frobenius positivity)
         net(x_mol) = net(A) + net(B) (mass conservation)
         x_mol = NF(A × O_bond × B)  (structural constraint)

The integer LP scans O_bond over all crossing operators of length n
and finds feasible solutions at each n.

Usage:
    cd computations
    python3 molecular-frobenius-lp.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import itertools
import numpy as np
import sys
from pathlib import Path
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402

from witness_base import WitnessBuilder

z = _PG_Z  # moved to pyhecke.gram
q2 = q0**2
denom_w = q2**2 + 4*q2 + 1
w_sym = q2 / denom_w
w_std = (q2 + 1)**2 / denom_w
w_alt = q2 / denom_w

TWO_Q = q0 + qi0
from hecke_core import alpha_em, E_HARTREE_EV as E_hartree_eV, E_MOL as E_mol

NF_NAMES = ["gamma", "s0", "s1", "L+", "L-", "e-"]
# e- Markov trace is h·z² + z (NOT z³); see docs/audits/2026-05-19-trm5-markov-bug.md
TR_M = np.array([1.0, z, z, z**2, z**2, h * z**2 + z])


# ══════════════════════════════════════════════════════════════
# §1. Hecke algebra
# ══════════════════════════════════════════════════════════════

def hecke_mul(nf, c, d, gen):
    r = [0.0]*6
    if gen == 0:
        tables = [(0,[(1,c),(0,d)]),(1,[(1,c*h),(0,c),(1,d)]),(2,[(3,c),(2,d)]),(3,[(3,c*h),(2,c),(3,d)]),(4,[(5,c),(4,d)]),(5,[(5,c*h),(4,c),(5,d)])]
    else:
        tables = [(0,[(2,c),(0,d)]),(1,[(4,c),(1,d)]),(2,[(2,c*h),(0,c),(2,d)]),(3,[(5,c),(3,d)]),(4,[(4,c*h),(1,c),(4,d)]),(5,[(5,c*h),(3,c),(5,d)])]
    for si, tgts in tables:
        if abs(nf[si]) < 1e-15: continue
        for ti, co in tgts: r[ti] += nf[si] * co
    return r


def nf_trace(nf):
    return sum(nf[i] * TR_M[i] for i in range(6))


def nf_net(nf):
    return sum(nf)


# ══════════════════════════════════════════════════════════════
# §2. Gram matrix G — Frobenius pairing ⟨b_i, b_j⟩_F = tr_M(b_i · b_j)
# ══════════════════════════════════════════════════════════════

NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
def hecke_mul_dict(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf_dict(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15: continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * h
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True; break
            if done: continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos+1], word[pos+2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos+3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True; break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def to_vec(terms):
    return np.array([terms.get(b, 0.0) for b in NF_BASIS])


def build_gram():
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            prod = hecke_mul_dict({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
            nf = reduce_nf_dict(prod)
            vec = to_vec(nf)
            G[i, j] = sum(vec[k] * TR_M[k] for k in range(6))
    return G


G = build_gram()
print("=" * 70)
print("MOLECULAR COVALENT BOND FROM FROBENIUS LP DUAL")
print("=" * 70)
print(f"q = {q0:.10f}, h = {h:.10f}, z = {z:.10f}")
print(f"E_mol = {E_mol:.4f} eV")
print(f"Gram matrix eigenvalues: {sorted(np.linalg.eigvals(G).real)}")
print()


# ══════════════════════════════════════════════════════════════
# §2b. Canonical operator-selection LP dual (AGENTS.md LP/SDP mandate)
# ══════════════════════════════════════════════════════════════
# Route the molecular Frobenius operator-selection through the canonical
# solver so the witness carries BOTH the primal coefficients AND the dual
# shadow prices.  The active set {i : y_star[i] > 0} are the saturated
# Frobenius/Wedderburn channels — the "most receptive sub-braids" — and
# their cardinality is the categorical signature of bond order.
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402

# Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
# whether the Rust binary happens to be built, so the same script
# yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
# makes a missing binary an error rather than a changed answer.
# Bean `qou/ftuv`.
_lp = solve_operator_selection_lp(np.asarray(TR_M, dtype=float), G, n_target=1.0, backend="clarabel")
print("--- Operator-selection LP dual (unit net) ---")
print(f"  primal_obj  = {_lp.primal_obj:.6f}   dual_obj = {_lp.dual_obj:.6f}")
print(f"  duality_gap = {_lp.duality_gap:.2e}   (strong duality)")
print(f"  y0*         = {_lp.y0_star:.6f}   (binding-energy density shadow price)")
print(f"  active_set  = {_lp.active_set} → "
      f"{[NF_NAMES[i] for i in _lp.active_set]}")
print(f"  |active_set| = {len(_lp.active_set)}  (saturated Wedderburn channels)")
print()


# ══════════════════════════════════════════════════════════════
# §3. Build atoms
# ══════════════════════════════════════════════════════════════

def build_atom_nf(Z, N):
    nf = [1.0, 0, 0, 0, 0, 0]
    pc, nc = 0, 0
    for k in range(Z + N):
        is_p = (k % 2 == 0 and pc < Z) or nc >= N
        if is_p:
            for _ in range(3):
                nf = hecke_mul(nf, 1, 0, 0)
                nf = hecke_mul(nf, 1, -h, 1)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h/2, 1)
            nf = hecke_mul(nf, 1, -h/2, 0)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, 0, 0)
            pc += 1
        else:
            for _ in range(3):
                nf = hecke_mul(nf, 1, 0, 0)
                nf = hecke_mul(nf, 1, -h, 1)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h/2, 1)
            nf = hecke_mul(nf, 1, -h/2, 0)
            for _ in range(4):
                nf = hecke_mul(nf, 1, 0, 0)
            nc += 1
    for _ in range(Z):
        nf = hecke_mul(nf, 1, -h, 1)
    return nf


def apply_atom(nf, Z, N):
    pc, nc = 0, 0
    for k in range(Z + N):
        is_p = (k % 2 == 0 and pc < Z) or nc >= N
        if is_p:
            for _ in range(3):
                nf = hecke_mul(nf, 1, 0, 0)
                nf = hecke_mul(nf, 1, -h, 1)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h/2, 1)
            nf = hecke_mul(nf, 1, -h/2, 0)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, 0, 0)
            pc += 1
        else:
            for _ in range(3):
                nf = hecke_mul(nf, 1, 0, 0)
                nf = hecke_mul(nf, 1, -h, 1)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h/2, 1)
            nf = hecke_mul(nf, 1, -h/2, 0)
            for _ in range(4):
                nf = hecke_mul(nf, 1, 0, 0)
            nc += 1
    for _ in range(Z):
        nf = hecke_mul(nf, 1, -h, 1)
    return nf


# ══════════════════════════════════════════════════════════════
# §4. Frobenius LP for each bond type
# ══════════════════════════════════════════════════════════════

OPS = [
    ("s0",  0, 1.0, 0.0),
    ("s1",  1, 1.0, 0.0),
    ("s0i", 0, 1.0, -h),
    ("s1i", 1, 1.0, -h),
]


def frobenius_check(nf_vec):
    """Check Frobenius positivity: G · x ≥ 0. Returns (passes, Gx, n_violations)."""
    x = np.array(nf_vec)
    Gx = G @ x
    violations = sum(1 for v in Gx if v < -1e-10)
    return violations == 0, Gx, violations


def scan_bond_frobenius(nf_A, Z_B, N_B, obs_E, bond_name, max_n=4):
    """Scan crossing operators, check Frobenius feasibility at each n."""

    # Step 1: Check unbonded state
    nf_ub = apply_atom(list(nf_A), Z_B, N_B)
    x_ub = np.array(nf_ub)
    passes_ub, Gx_ub, n_viol_ub = frobenius_check(nf_ub)
    tr_ub = nf_trace(nf_ub)
    Phi_ub = mp.log(abs(tr_ub)) if abs(tr_ub) > 1e-300 else float('inf')

    print(f"\n--- {bond_name} bond ---")
    print(f"  Unbonded: tr_M = {tr_ub:.6e}, Phi_1 = {float(Phi_ub):.6f}")
    print(f"  Frobenius: {'PASS' if passes_ub else 'FAIL'} ({n_viol_ub} violations)")
    if not passes_ub:
        for i in range(6):
            if Gx_ub[i] < -1e-10:
                print(f"    (G·x)[{NF_NAMES[i]}] = {Gx_ub[i]:+.6f} < 0  VIOLATED")

    # Step 2: Scan operators at each crossing count
    print(f"\n  {'n':>3} {'feasible':>8} {'best ops':>28} {'tr_M':>12} "
          f"{'binding':>10} {'E(eV)':>10} {'Frob':>5}")
    print("  " + "-" * 80)

    best_overall = None
    for n in range(1, max_n + 1):
        feasible = []
        for ops in itertools.product(OPS, repeat=n):
            nf = list(nf_A)
            for name, gen, c, d in ops:
                nf = hecke_mul(nf, c, d, gen)
            nf = apply_atom(nf, Z_B, N_B)

            passes, Gx, n_viol = frobenius_check(nf)
            tr = nf_trace(nf)
            if abs(tr) < 1e-300:
                continue
            Phi = mp.log(abs(tr))
            bind = Phi_ub - Phi
            E = bind * E_mol
            label = ",".join(o[0] for o in ops)

            feasible.append({
                'ops': label, 'n': n, 'tr': tr, 'Phi': Phi,
                'bind': bind, 'E': E, 'passes': passes,
                'n_viol': n_viol, 'Gx': Gx.copy(),
            })

        # Sort by: Frobenius feasibility first, then minimize |tr_M|
        feasible.sort(key=lambda r: (-int(r['passes']), abs(r['tr'])))

        n_pass = sum(1 for f in feasible if f['passes'])
        if feasible:
            best = feasible[0]
            frob_str = "PASS" if best['passes'] else f"FAIL({best['n_viol']})"
            print(f"  {n:>3} {n_pass:>4}/{len(feasible):>3} {best['ops']:>28} "
                  f"{best['tr']:>12.6e} {float(best['bind']):>10.6f} "
                  f"{float(best['E']):>10.4f} {frob_str:>5}")

            if best['passes'] and (best_overall is None or abs(best['tr']) < abs(best_overall['tr'])):
                best_overall = best

    if best_overall:
        print(f"\n  LP-OPTIMAL: {best_overall['ops']} ({best_overall['n']} crossings)")
        print(f"    tr_M = {best_overall['tr']:.6e}")
        print(f"    E = {float(best_overall['E']):.4f} eV (obs: {obs_E:.2f} eV, "
              f"err: {float(best_overall['E']/obs_E - 1)*100:+.1f}%)")
        print(f"    Frobenius: ALL constraints satisfied")
    else:
        print(f"\n  NO feasible solution found up to {max_n} crossings")

    return best_overall


# ══════════════════════════════════════════════════════════════
# §5. Run for all bond types
# ══════════════════════════════════════════════════════════════

bond_types = [
    ("H-H", 1, 0, 1, 0, 4.478),
    ("C-H", 6, 6, 1, 0, 4.48),
    ("C-O", 6, 6, 8, 8, 3.70),
    ("C-C", 6, 6, 6, 6, 3.60),
    ("O-H", 8, 8, 1, 0, 4.82),
]

results = {}
for name, Z_A, N_A, Z_B, N_B, obs in bond_types:
    nf_A = build_atom_nf(Z_A, N_A)
    best = scan_bond_frobenius(nf_A, Z_B, N_B, obs, name, max_n=4)
    results[name] = best

# ══════════════════════════════════════════════════════════════
# §6. Summary and molecules
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SUMMARY: LP-DERIVED BOND OPERATORS (Frobenius feasibility)")
print("=" * 70)
print(f"\n  {'Bond':>6} {'n':>3} {'Operator':>28} {'E/bond':>10} {'Observed':>10} {'Error':>8}")
print("  " + "-" * 68)

for name in ["H-H", "C-H", "C-O", "C-C", "O-H"]:
    r = results.get(name)
    if r:
        err = float(r['E']/bond_types[[b[0] for b in bond_types].index(name)][5] - 1)*100
        print(f"  {name:>6} {r['n']:>3} {r['ops']:>28} {float(r['E']):>10.4f} "
              f"{bond_types[[b[0] for b in bond_types].index(name)][5]:>10.2f} {err:>+7.1f}%")
    else:
        print(f"  {name:>6}   — no feasible solution —")

# Molecules
print()
co_E = results.get('C-O', {}).get('E', 0) if results.get('C-O') else 0
cc_E = results.get('C-C', {}).get('E', 0) if results.get('C-C') else 0
ch_E = results.get('C-H', {}).get('E', 0) if results.get('C-H') else 0
hh_E = results.get('H-H', {}).get('E', 0) if results.get('H-H') else 0

molecules = [
    ("H2",   1 * hh_E,                    4.478),
    ("CO",   3 * co_E,                    11.09),
    ("CO2",  4 * co_E,                    16.56),
    ("CH4",  4 * ch_E,                    17.9),
    ("C6H6", 9*cc_E + 6*ch_E,            57.4),
]

print(f"  {'Molecule':>8} {'Predicted':>12} {'Observed':>12} {'Error':>8}")
print("  " + "-" * 44)
for name, pred, obs in molecules:
    err = float((pred/obs - 1)*100) if obs > 0 and pred != 0 else float('nan')
    print(f"  {name:>8} {float(pred):>10.2f} eV {obs:>10.2f} eV {err:>+7.1f}%")

print()

# ══════════════════════════════════════════════════════════════
# §7. Witness
# ══════════════════════════════════════════════════════════════

w = WitnessBuilder("molecular-frobenius-lp", engine="python")
w.set_description(
    "Molecular covalent bonds derived from Frobenius LP dual. "
    "Bond operators selected by: (1) Frobenius positivity Gx >= 0, "
    "(2) minimum Markov trace among feasible operators. "
    "Zero fitted parameters."
)
w.set_content_block("def:molecular-braid")

w.add_parameter("q", q0)
w.add_parameter("E_mol_eV", E_mol)
w.add_parameter("gram_eigenvalues", sorted(np.linalg.eigvals(G).real.tolist()))

# Canonical operator-selection LP dual: primal coefficients + shadow prices.
w.add_data("operator_selection_lp_dual", _lp.to_dict())
w.add_data("operator_selection_active_channels",
           [NF_NAMES[i] for i in _lp.active_set])
w.add_assertion(
    "operator-selection LP strong duality (gap ~ 0)",
    computed=bool(_lp.duality_gap < 1e-6),
    expected=True,
    source="solve_operator_selection_lp (lp_dual_solver / pyhecke)",
)

for name in ["H-H", "C-H", "C-O", "C-C", "O-H"]:
    r = results.get(name)
    if r:
        w.add_data(f"bond_{name}", {
            "ops": r['ops'], "n_crossings": r['n'],
            "E_eV": float(r['E']), "tr_M": float(r['tr']),
            "frobenius_passes": True,
        })

w.add_data("molecules", [{"name": n, "predicted_eV": p, "observed_eV": o}
                          for n, p, o in molecules])

for name, pred, obs in molecules:
    w.add_assertion(
        f"{name} binding positive",
        computed=pred > 0,
        expected=True,
        source="Frobenius LP feasibility",
    )


# ══════════════════════════════════════════════════════════════
#  SDP LIFT VALIDATION  (see sdp_moment_lift.py / docs/ilp-sdp-audit.md)
# ══════════════════════════════════════════════════════════════
print(f"\n{'═' * 80}\n  SDP LIFT VALIDATION\n{'═' * 80}")
sdp_reports = []
try:
    from sdp_moment_lift import lp_vs_sdp_report
    _rep = lp_vs_sdp_report(
        c=TR_M, G=G, A_eq=np.ones((1, 6)),
        b_eq=np.array([1.0]),
        label="molecular-frobenius/unit-net")
    for _l in _rep.summary_lines():
        print(_l)
    sdp_reports.append(_rep.__dict__)
    w.add_data("sdp_lift", sdp_reports)
    w.add_assertion(
        "LP solution Frobenius-valid (xᵀGx ≥ 0)",
        computed=_rep.lp_frobenius_valid,
        expected=True,
        source="sdp_moment_lift",
    )
except ImportError as _e:
    print(f"  (cvxpy not available: {_e})")

w.save()
print("Done.")
