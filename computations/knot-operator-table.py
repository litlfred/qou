#!/usr/bin/env python3
"""
Knot operator action table — computes K₁ · β(T_{m,n}) · K₂ for all
NF basis elements and all torus knot operators in H₃(q).

NF basis: {𝟏, σ₀, σ₁, L₊=σ₀σ₁, L₋=σ₁σ₀, e⁻=σ₀σ₁σ₀}

Knot operators (braid words):
  T_{1,0}: 𝟏  (identity/trivial)
  T_{2,1}: σ₀  (single crossing)
  T_{2,2}: σ₀² = hσ₀ + 𝟏  (Hopf link)
  T_{2,2}^{(3)}: σ₀σ₁σ₀  (= e⁻ basis word; closure is the HOPF LINK, see below)
  T_{2,4}^{(3)}: (σ₀σ₁)²σ₀  (closure is the T(2,4) torus link, see below; was mislabelled T_{2,5})

Closure of σ₀σ₁σ₀ ∈ B_3 (relabelled 2026-11-21, owner ruling (C)): the
permutation is a transposition, so the closure has 2 components; σ₀σ₁σ₀ is
conjugate to σ₀²σ₁, which Markov-destabilises to σ₀² ∈ B_2, the Hopf link.
Checked three ways: component count; Jones polynomial by Kauffman bracket
(−t^{5/2} − t^{1/2}, equal to that of σ₀² ∈ B_2 and not to the trefoil's
−t⁴ + t³ + t); and the convention-D Markov trace, tr_M(σ₀σ₁σ₀) =
z·tr_M(σ₀²) ≠ z·tr_M(σ₀³). This entry was labelled T_{2,3} (trefoil) until
2026-11-21. The trefoil braid is σ₀³ ∈ B_2; it is NOT added here, because
lp-duality-check.py reads this table's "T_{2,3}" key for its e⁻-universality
claim, and putting σ₀³ under that key would change what that claim tests.

Same check on (σ₀σ₁)²σ₀ ∈ B_3: 2 components, Jones
−t^{11/2} + t^{9/2} − t^{7/2} − t^{3/2} = that of σ₀⁴ ∈ B_2, i.e. the
T(2,4) torus link, not the cinquefoil T(2,5) = σ₀⁵. Relabelled 2026-11-21
T_{2,5} -> T_{2,4}^{(3)}, following the T_{2,2}^{(3)} pattern above (the
superscript records that the word lives in B_3). Re-verified independently
in computations/probes/electron_word_gs_interactions_probe.py's Kauffman
bracket: 2 components, Jones equal to that of σ₀⁴ ∈ B_2 and not to that of
σ₀⁵. The cinquefoil braid σ₀⁵ is NOT added here; no consumer reads this
key (no witness of this producer has ever been committed).

Output: JSON witness + markdown table for inclusion in content.

Usage:
    cd computations && python3 knot-operator-table.py
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp

# ── q parameter (canonical source) ───────────────────────────
# `mp` here is the mpmath CONTEXT (`from mpmath import mp`), so `mp.dps`
# is the correct spelling. Raised before the fallback below: that branch
# reconstructs q0 from a 16-digit literal and binds module-level q0/qi0/HA
# used throughout, so at the default 15 dps the whole module would run
# off a 53-bit q0 whenever q_parameter is unavailable.
mp.dps = 50

try:
    from q_parameter import Q as q0, Q_INV as qi0, HA
except ImportError:
    # Fallback: derive from CODATA (Vol(4₁)/m_μ/m_e)
    _V = mp.mpf("2.029883212819307"); _R = mp.mpf("206.768283")  # noqa: P31 — display-only q_0 reconstruction in __main__ block; live value from q_parameter.Q
    _h = mp.sqrt(_V / _R); q0 = mp.mpf(1) / (mp.mpf(1) - _h)
    qi0 = mp.mpf(1) / q0; HA = q0 - qi0

# ── Hecke algebra H₃(q) engine ──────────────────────────────
# Elements are dicts: {word_tuple: float_coefficient}
# word = tuple of generator indices (0 or 1)
# Empty tuple = identity 𝟏

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
NF_LATEX = [r"\gamma", r"\sigma_0", r"\sigma_1", r"L_+", r"L_-", r"e^-"]

def hecke_mul(terms1, terms2):
    """Multiply two H₃(q) elements (concatenate words)."""
    result = {}
    for w1, c1 in terms1.items():
        for w2, c2 in terms2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    """Reduce to Gröbner-Shirshov normal form in H₃(q)."""
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False

            # R1: Hecke σᵢ² → (q−q⁻¹)σᵢ + 𝟏
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    w1 = pre + (i,) + suf
                    w2 = pre + suf
                    new_terms[w1] = new_terms.get(w1, 0.0) + coeff * HA
                    new_terms[w2] = new_terms.get(w2, 0.0) + coeff
                    done = changed = True
                    break

            if done:
                continue

            # R2: Far commutativity — not needed for 2 generators
            # (|0−1| = 1 < 2, so no far commutativity applies)

            # R3: Yang-Baxter σᵢσⱼσᵢ → σⱼσᵢσⱼ (orient to lex-smaller)
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    old_trip = (a, b, a)
                    if new_trip < old_trip:
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break

            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff

        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}

    return terms


def to_nf_vector(terms):
    """Extract NF coefficients as a 6-element list."""
    return [terms.get(b, 0.0) for b in NF_BASIS]


def nf_net(vec):
    return sum(vec)


def basis_element(idx):
    """Return H₃(q) element for the idx-th NF basis element."""
    return {NF_BASIS[idx]: 1.0}


# ── Knot operators as braid words ────────────────────────────

KNOT_OPERATORS = {
    "T_{1,0}": (),                    # identity
    "T_{2,1}": (0,),                  # σ₀
    "T_{2,2}": (0, 0),               # σ₀² (reduces to hσ₀ + 𝟏)
    "T_{2,2}^{(3)}": (0, 1, 0),      # σ₀σ₁σ₀: closure is the Hopf link (was mislabelled T_{2,3})
    "T_{2,4}^{(3)}": (0, 1, 0, 1, 0),  # (σ₀σ₁)²σ₀: closure is the T(2,4) link (was mislabelled T_{2,5})
}

KNOT_LATEX = {
    "T_{1,0}": r"T_{1,0}",
    "T_{2,1}": r"T_{2,1}",
    "T_{2,2}": r"T_{2,2}",
    "T_{2,2}^{(3)}": r"T_{2,2}^{(3)}",
    "T_{2,4}^{(3)}": r"T_{2,4}^{(3)}",
}

KNOT_PHYS = {
    "T_{1,0}": "trivial (identity)",
    "T_{2,1}": "single crossing",
    "T_{2,2}": "Hopf link (gluon)",
    "T_{2,2}^{(3)}": "Hopf link (closure of σ₀σ₁σ₀ ∈ B_3; e⁻ basis word; not the trefoil)",
    "T_{2,4}^{(3)}": "T(2,4) torus link (closure of (σ₀σ₁)²σ₀ ∈ B_3; not the cinquefoil)",
}


def apply_operator(K1_idx, op_word, K2_idx):
    """Compute NF(b_{K1} · β(T) · b_{K2}) in H₃(q)."""
    elem1 = basis_element(K1_idx)
    op = {op_word: 1.0} if op_word else {(): 1.0}
    elem2 = basis_element(K2_idx)

    product = hecke_mul(hecke_mul(elem1, op), elem2)
    reduced = reduce_nf(product)
    return to_nf_vector(reduced)


# ══════════════════════════════════════════════════════════════
#  MAIN COMPUTATION
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 72)
    print("  KNOT OPERATOR ACTION TABLE")
    print(f"  q₀ = {q0:.10f},  HA = q−q⁻¹ = {HA:.10f}")
    print("=" * 72)

    results = {}

    # For each knot operator
    for op_name, op_word in KNOT_OPERATORS.items():
        print(f"\n{'─' * 72}")
        print(f"  Operator: {op_name}  ({KNOT_PHYS[op_name]})")
        print(f"  Braid word: {'𝟏' if not op_word else '·'.join(f'σ_{g}' for g in op_word)}")
        print(f"{'─' * 72}")

        op_results = {}

        # Header
        hdr = f"  {'K₁·T·K₂':12s}"
        for name in NF_NAMES:
            hdr += f" | {name:>8s}"
        hdr += f" | {'net':>8s}"
        print(hdr)
        print("  " + "-" * (len(hdr) - 2))

        # For each pair of basis elements
        for i in range(6):
            for j in range(6):
                vec = apply_operator(i, op_word, j)
                net = nf_net(vec)
                pair_name = f"{NF_NAMES[i]}·{NF_NAMES[j]}"
                line = f"  {pair_name:12s}"
                for v in vec:
                    line += f" | {v:>8.3f}"
                line += f" | {net:>8.3f}"
                print(line)

                op_results[f"{NF_NAMES[i]}*{NF_NAMES[j]}"] = {
                    "nf": vec,
                    "net": net,
                    "has_electron": abs(vec[5]) > 1e-10,
                    "has_negative": any(v < -1e-10 for v in vec),
                    "demand": [NF_NAMES[k] for k in range(6) if vec[k] < -1e-10],
                    "supply": [NF_NAMES[k] for k in range(6) if vec[k] > 1e-10],
                }

        results[op_name] = op_results

    # ── Summary: which pairs produce e⁻ channel ────────────────
    print(f"\n\n{'=' * 72}")
    print("  SUMMARY: e⁻ channel presence by operator and pair")
    print("=" * 72)

    for op_name in KNOT_OPERATORS:
        pairs_with_e = []
        for pair_key, data in results[op_name].items():
            if data["has_electron"]:
                pairs_with_e.append((pair_key, data["nf"][5]))
        print(f"\n  {op_name} ({KNOT_PHYS[op_name]}):")
        if not pairs_with_e:
            print("    No pairs produce e⁻ channel")
        else:
            print(f"    {len(pairs_with_e)} / 36 pairs produce e⁻:")
            for pk, ev in sorted(pairs_with_e, key=lambda x: -abs(x[1]))[:10]:
                print(f"      {pk:12s}  e⁻ coeff = {ev:+.6f}")
            if len(pairs_with_e) > 10:
                print(f"      ... and {len(pairs_with_e) - 10} more")

    # ── Summary: demand profiles ──────────────────────────────
    print(f"\n\n{'=' * 72}")
    print("  DEMAND PROFILES: pairs with negative NF coefficients")
    print("=" * 72)

    for op_name in KNOT_OPERATORS:
        pairs_with_demand = []
        for pair_key, data in results[op_name].items():
            if data["has_negative"]:
                pairs_with_demand.append((pair_key, data["demand"], data["nf"]))
        print(f"\n  {op_name} ({KNOT_PHYS[op_name]}):")
        if not pairs_with_demand:
            print("    No pairs have negative coefficients (no demand)")
        else:
            print(f"    {len(pairs_with_demand)} / 36 pairs have demand:")
            for pk, dem, nf in pairs_with_demand[:8]:
                neg_str = ", ".join(f"{NF_NAMES[k]}={nf[k]:+.3f}"
                                   for k in range(6) if nf[k] < -1e-10)
                print(f"      {pk:12s}  demand: [{neg_str}]")
            if len(pairs_with_demand) > 8:
                print(f"      ... and {len(pairs_with_demand) - 8} more")

    # ── Key table: σ₀·T·σ₀ for all operators ───
    # Scope note (2026-11-20): this table is the single-crossing σ₀ TERM on both sides, not a
    # photon pair. Under def:photon (fourth term σ₀σ₁⁻¹, owner ruling bean qou-99qc) the photon-pair
    # table is probes/photon_chiral/photon_chiral_ports_probe.py §A (exact, eigenvalue-pair weights).
    print(f"\n\n{'=' * 72}")
    print("  KEY TABLE: σ₀·T·σ₀ (single-crossing term; four-term photon: probes/photon_chiral §A)")
    print("=" * 72)

    hdr = f"  {'Operator':10s}"
    for name in NF_NAMES:
        hdr += f" | {name:>8s}"
    hdr += f" | {'net':>8s} | {'e⁻?':>4s}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))

    for op_name, op_word in KNOT_OPERATORS.items():
        # Compute σ₀ · T · σ₀ (single-crossing term; not a photon under def:photon)
        vec = apply_operator(1, op_word, 1)
        net = nf_net(vec)
        has_e = "YES" if abs(vec[5]) > 1e-10 else "no"
        line = f"  {op_name:10s}"
        for v in vec:
            line += f" | {v:>8.3f}"
        line += f" | {net:>8.3f} | {has_e:>4s}"
        print(line)

    # ── Write witness ─────────────────────────────────────────
    witness = {
        "name": "knot-operator-table",
        "description": (
            "NF decomposition of K₁·β(T_{m,n})·K₂ for all NF basis pairs "
            "and all torus knot operators in H₃(q). "
            "Demonstrates multi-channel pair production and demand profiles."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "HA": HA},
        "nf_basis": NF_NAMES,
        "operators": list(KNOT_OPERATORS.keys()),
        "results": results,
    }

    from witness_base import WitnessBuilder  # noqa: E402 — P30 staleness triple
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__)  # scriptHash/scriptCommitSha
    witness["scriptFile"] = Path(__file__).name
    out_path = Path(__file__).with_suffix(".witness.json")
    out_path.write_text(json.dumps(witness, indent=2, default=float))
    print(f"\n  Witness written to {out_path.name}")
