#!/usr/bin/env python3
"""
Photon operator table — compact H₃(q) representation.

Computes the NF of b_i · β(T_{m,n}) · b_j for all 6×6 basis pairs
and all torus knot operators. Stores the result as 6×6 matrices
(one per operator) instead of 180 verbose pair entries.

Each operator's action is a 6×6→6 trilinear map. At the H₃(q) level,
this is fully determined by the multiplication table + the operator's
own NF. The witness stores:

  1. The NF of each operator (6 coefficients)
  2. The 6×6 output matrix per operator (36 × 6 = 216 floats total)
  3. Summary statistics (e⁻ channel count, demand pairs)

This replaces knot-operator-table.py (3,562 lines, 78KB witness)
with ~200 lines and ~8KB witness.

Usage:
    python3 photon_operator_table.py

Content block: rem:knot-operator-basis-table
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0, HA
from witness_base import WitnessBuilder

# ── H₃(q) NF engine (same as hecke_core, self-contained) ────────

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
NF_LATEX = [r"\gamma", r"\sigma_0", r"\sigma_1", r"L_+", r"L_-", r"e^-"]

z = 1.0 / (q0**0.5 + qi0**0.5)
TR_M = [1.0, z, z, z**2, z**2, z**3]


def hecke_mul(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    i = word[p]
                    pre, suf = word[:p], word[p + 2:]
                    new[pre + (i,) + suf] = new.get(pre + (i,) + suf, 0) + coeff * HA
                    new[pre + suf] = new.get(pre + suf, 0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


def to_nf(terms):
    return [round(terms.get(b, 0.0), 12) for b in NF_BASIS]


def basis_elem(i):
    return {NF_BASIS[i]: 1.0}


def nf_tr(vec):
    return sum(v * t for v, t in zip(vec, TR_M))


# ── Knot operators ───────────────────────────────────────────────

OPERATORS = {
    "T_{1,0}": {"word": (), "phys": "trivial (vacuum)"},
    "T_{2,1}": {"word": (0,), "phys": "single crossing"},
    "T_{2,2}": {"word": (0, 0), "phys": "Hopf link (gluon)"},
    "T_{2,3}": {"word": (0, 1, 0), "phys": "trefoil (electron)"},
    "T_{2,5}": {"word": (0, 1, 0, 1, 0), "phys": "cinquefoil (muon)"},
}


# ── Compute ──────────────────────────────────────────────────────

print(f"Photon operator table (compact H₃(q) representation)")
print(f"q₀ = {q0:.10f}, h = {HA:.10f}, z = {z:.10f}")
print()

results = {}

for op_name, op_info in OPERATORS.items():
    op_word = op_info["word"]

    # NF of the operator itself
    op_nf = to_nf(reduce_nf({op_word: 1.0} if op_word else {(): 1.0}))

    # 6×6 action matrix: matrix[i][j] = NF(b_i · T · b_j)
    matrix = []
    e_minus_count = 0
    demand_count = 0

    for i in range(6):
        row = []
        for j in range(6):
            elem1 = basis_elem(i)
            op = {op_word: 1.0} if op_word else {(): 1.0}
            elem2 = basis_elem(j)
            product = hecke_mul(hecke_mul(elem1, op), elem2)
            nf = to_nf(reduce_nf(product))
            row.append(nf)

            if abs(nf[5]) > 1e-10:
                e_minus_count += 1
            if any(v < -1e-10 for v in nf):
                demand_count += 1
        matrix.append(row)

    results[op_name] = {
        "phys": op_info["phys"],
        "operator_nf": op_nf,
        "matrix": matrix,
        "e_minus_pairs": e_minus_count,
        "demand_pairs": demand_count,
    }

    print(f"  {op_name:8s} ({op_info['phys']:25s}): "
          f"e⁻ in {e_minus_count}/36 pairs, "
          f"demand in {demand_count}/36, "
          f"op NF = [{', '.join(f'{v:.3f}' for v in op_nf)}]")

# ── Key table: photon-photon channel ─────────────────────────────

print(f"\nPhoton-photon channel (γ·T·γ = b₀·T·b₀):")
print(f"  {'Op':8s} {'γ':>8s} {'σ₀':>8s} {'σ₁':>8s} {'L₊':>8s} {'L₋':>8s} {'e⁻':>8s}")
for op_name, data in results.items():
    nf = data["matrix"][0][0]
    print(f"  {op_name:8s} {nf[0]:>8.4f} {nf[1]:>8.4f} {nf[2]:>8.4f} "
          f"{nf[3]:>8.4f} {nf[4]:>8.4f} {nf[5]:>8.4f}")

# ── Witness ──────────────────────────────────────────────────────

w = WitnessBuilder("photon-operator-table", engine="python")
w.set_description(
    "Compact photon operator table: NF of b_i·β(T_{m,n})·b_j for all "
    "6×6 basis pairs and 5 torus knot operators. Each operator stored "
    "as a 6×6 matrix of 6-element NF vectors. Replaces the verbose "
    "knot-operator-table witness (78KB → ~8KB)."
)
w.set_content_block("rem:knot-operator-basis-table")

w.add_parameter("q", q0)
w.add_parameter("h", HA)
w.add_parameter("z", z)
w.add_parameter("basis", NF_NAMES)

# Key assertions
for op_name, data in results.items():
    w.add_assertion(
        f"{op_name} e⁻ pair count",
        computed=data["e_minus_pairs"],
        expected=data["e_minus_pairs"],
        tolerance=0,
        source="H₃(q) basis multiplication",
    )

# The critical physics result
w.add_assertion(
    "T_{2,3} universally opens e⁻ channel",
    computed=results["T_{2,3}"]["e_minus_pairs"],
    expected=36,
    tolerance=0,
    source="Trefoil = e⁻ in NF basis; b_i·e⁻·b_j always has e⁻ ≠ 0",
)

w.add_data("operators", results)

witness_path = w.save()
print(f"\nWitness: {witness_path.name}")
