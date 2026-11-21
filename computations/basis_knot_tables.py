#!/usr/bin/env python3
"""
Basis knot multiplication tables for all 6 elements of H₃(q).

For each basis knot K ∈ {γ, σ₀, σ₁, L₊, L₋, e⁻}, computes the
6×6 table of b_i · K · b_j → NF.  This is the fundamental structure
of the Hecke algebra: every physical process (pair production, decay,
scattering) decomposes into products of these tables.

Key results:
  - γ (identity): 19/36 pairs produce e⁻
  - σ₀, σ₁ (single crossing): 24/36 pairs produce e⁻
  - L₊, L₋ (Hopf link): 32/36 pairs produce e⁻
  - e⁻ (σ₀σ₁σ₀, closure Hopf link): 36/36 pairs produce e⁻ (universal)

The progression 19 → 24 → 32 → 36 shows that higher-crossing
knots progressively open more channels, with σ₀σ₁σ₀ being
the unique minimum-crossing universal pair-production operator.

Usage:
    python3 basis_knot_tables.py

Content block: rem:hecke-operations
"""

import mpmath as mp

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_MP as q0, Q_INV_MP as qi0, HA_MP as HA

# NO-FLOAT64: same shape as photon_operator_table (shared NF engine) --
# `Q` the float seeded `z`, `TR_M` opened with `1.0`, the reduction passes
# pruned on 1e-15 and `to_nf` serialized `round(..., 12)`.  Coefficients are
# O(1) polynomials in q at q0, so 1e-15 was killing float64 NOISE; 1e-50 is
# strictly weaker, so every term the float64 version kept is still kept.
set_compute_dps()
_ZERO = mp.mpf(0)
_ONE = mp.mpf(1)
_EPS = mp.mpf(10) ** -50
from witness_base import WitnessBuilder

# ── H₃(q) NF engine ─────────────────────────────────────────────

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]

z = q0**3 / (q0**2 + 1)
h = q0 - _ONE / q0
# TR_M[5] = tr_M(sigma_0 sigma_1 sigma_0) = h*z^2 + z, NOT z^3. The Markov
# axioms give tr(s0 s1 s0) = tr(s1 s0^2) = tr(s1 (h s0 + 1)) = h*tr(s1 s0)
# + tr(s1) = h*z^2 + z. docs/audits/2026-05-19-trm5-markov-bug.md fixed this
# in pyhecke.gram on 2026-05-19; it never propagated here (bean qou-ssex).
TR_M = [_ONE, z, z, z**2, z**2, h * z**2 + z]


def hecke_mul(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, _ZERO) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > _EPS}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < _EPS:
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
        terms = {w: c for w, c in new.items() if abs(c) > _EPS}
    return terms


def to_nf(terms):
    # Was `round(..., 12)` -- a float64 exit that also capped the table.
    return [terms.get(b, _ZERO) for b in NF_BASIS]


def basis_elem(i):
    return {NF_BASIS[i]: _ONE}


# ── Basis knots as operators ─────────────────────────────────────

BASIS_KNOTS = [
    ("γ",  (),       "vacuum / photon (empty knot)"),
    ("σ₀", (0,),     "single crossing (up quark channel)"),
    ("σ₁", (1,),     "single crossing (color channel)"),
    ("L₊", (0, 1),   "Hopf link (gluon +)"),
    ("L₋", (1, 0),   "Hopf link (gluon −)"),
    ("e⁻", (0, 1, 0), "Hopf link (closure in B₃; electron)"),
]


# ── Compute ──────────────────────────────────────────────────────

print(f"Basis knot multiplication tables for H₃(q)")
print(f"q₀ = {mp.nstr(q0, 11)}, h = {mp.nstr(HA, 11)}")  # display only
print()

all_tables = {}

for op_name, op_word, op_phys in BASIS_KNOTS:
    matrix = []
    e_count = 0

    for i in range(6):
        row = []
        for j in range(6):
            elem1 = basis_elem(i)
            op = {op_word: _ONE} if op_word else {(): _ONE}
            elem2 = basis_elem(j)
            product = hecke_mul(hecke_mul(elem1, op), elem2)
            nf = to_nf(reduce_nf(product))
            row.append(nf)
            if abs(nf[5]) > 1e-10:
                e_count += 1
        matrix.append(row)

    all_tables[op_name] = {
        "phys": op_phys,
        "word": list(op_word),
        "matrix": matrix,
        "e_minus_pairs": e_count,
    }

    print(f"  {op_name:3s} ({op_phys:40s}): e⁻ in {e_count}/36 pairs")

# ── Channel progression ──────────────────────────────────────────

print(f"\nChannel progression (crossings → e⁻ universality):")
print(f"  {'Knot':>4s} {'crossings':>9s} {'e⁻ pairs':>8s}")
for op_name, op_word, _ in BASIS_KNOTS:
    n_cross = len(op_word)
    e_count = all_tables[op_name]["e_minus_pairs"]
    bar = "█" * (e_count * 40 // 36)
    print(f"  {op_name:>4s} {n_cross:>9d} {e_count:>5d}/36  {bar}")

# ── Witness ──────────────────────────────────────────────────────

w = WitnessBuilder("basis-knot-tables", engine="python")
w.set_description(
    "Complete multiplication tables for all 6 basis knots of H₃(q). "
    "Each table is a 6×6 matrix of 6-element NF vectors showing "
    "b_i · K · b_j for basis knot K. The e⁻ channel count progression "
    "19 → 24 → 24 → 32 → 32 → 36 demonstrates that σ₀σ₁σ₀ "
    "is the unique minimum-crossing universal pair-production operator."
)
w.set_content_block("rem:hecke-operations")

w.add_parameter("q", q0)
w.add_parameter("h", HA)
w.add_parameter("z", z)
w.add_parameter("basis", NF_NAMES)

# Expected e⁻ pair counts out of the 36 (b_i, b_j) pairs, pinned.
#
# This read `computed=all_tables[...], expected=all_tables[...]` — the same
# expression on both sides, so it passed whatever the table held and
# `allPassed` said nothing about it (bean `qou-26f2`).
#
# REGRESSION PINS, not an independent derivation: values from the H₃(q)
# multiplication table as of 2026-08-25, recorded so a change in the table,
# the basis order or the NF reduction is caught rather than silently
# re-blessed.
#
# Cross-check worth knowing: `photon_operator_table.py` computes the same
# quantity over the same basis by a different route and agrees on γ (19),
# σ₀/σ₁ (24) and e⁻ (36) — it names its operators `T_{n,k}` rather than by
# basis word, and covers the cinquefoil instead of the two Hopf links.
EXPECTED_E_MINUS_PAIRS = {
    "γ":  19,   # vacuum / photon (empty knot)
    "σ₀": 24,   # single crossing (up quark channel)
    "σ₁": 24,   # single crossing (color channel)
    "L₊": 32,   # Hopf link (gluon +)
    "L₋": 32,   # Hopf link (gluon −)
    "e⁻": 36,   # σ₀σ₁σ₀ (electron) — universally opens the channel
}

for op_name, _, _ in BASIS_KNOTS:
    w.add_assertion(
        f"{op_name} e⁻ pair count",
        computed=all_tables[op_name]["e_minus_pairs"],
        expected=EXPECTED_E_MINUS_PAIRS[op_name],
        tolerance=0,
        source="H₃(q) basis multiplication; expected pinned 2026-08-25",
    )

# The key result
w.add_assertion(
    "e⁻ (σ₀σ₁σ₀) universally produces e⁻ channel",
    computed=all_tables["e⁻"]["e_minus_pairs"],
    expected=36,
    tolerance=0,
    source="e⁻ · b_i · b_j always has e⁻ ≠ 0 for all i,j",
)

w.add_assertion(
    "γ (identity) does NOT universally produce e⁻",
    computed=all_tables["γ"]["e_minus_pairs"],
    expected=19,
    tolerance=0,
    source="Only 19/36 basis products have e⁻ ≠ 0 under identity",
)

w.add_data("tables", all_tables)

witness_path = w.save()
print(f"\nWitness: {witness_path.name}")
