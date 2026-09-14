#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical audit; validates encodings.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Comprehensive audit: braid encodings + knot-operation classification +
γγ tracking, per the user directive

    "validate braid encodings of p and n, check all knot operations
     are SDP solved.  track all braids invoiced in γγ for each
     particle.  follow all the way through.  see where differences
     really are."

Phase 1.8 of the 1ppb plan.

Sections:
  A. Particle braid encoding inventory — literal σ-words for
     electron, proton, neutron, deuteron, triton, ³He, ⁴He.  Each
     reported as (c, d, gen_idx) triple list + symbolic σ-word.
  B. Knot-operation classification — for each operator in the
     Strategy-3 chain, classify as SDP-derived / Lean-proven /
     fitted / fallback / placeholder.
  C. γγ pair-production tracking — for each particle, list every
     σ_i² site that reduces under the Hecke quadratic
     (γγ = σ_i² → h·σ_i + 𝟏).
  D. Cross-check: independent |tr_M| paths — verify trace values
     via the symbolic axiomatic chain (Phase 1.6) and the
     Strategy-3 atomic-braid chain.
  E. Structural finding cross-reference — the framework's own
     `fresh_derivation_pn_true_sdp.py` documents that absolute
     m_p and m_n are NOT directly derivable; only differences
     project to observables.  Strategy-3 violates this.

Output: braid-encoding-audit.witness.json
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from collections import Counter
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from witness_base import WitnessBuilder, record_upstream

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_50_DIGIT_STR


# ─────────────────────────────────────────────────────────────────
# A. Particle braid encoding inventory
# ─────────────────────────────────────────────────────────────────

# (c, d) triple semantic — per markov_peel.crossing_from_cd:
#   (1, 0)        →  σ_i               positive crossing
#   (1, −h)       →  σ_i⁻¹             negative crossing
#   (1, −h/2)     →  ½(σ_i + σ_i⁻¹)    averaged (Markov-symmetric)
#   (0, 1)        →  𝟏                 no-interaction


def crossing_label(c: float, d: float, h: float) -> str:
    eps = 1e-6
    if abs(c - 1.0) < eps and abs(d) < eps:
        return "σ"
    if abs(c - 1.0) < eps and abs(d + h) < eps:
        return "σ⁻¹"
    if abs(c - 1.0) < eps and abs(d + h / 2) < eps:
        return "½(σ+σ⁻¹)"
    if abs(c) < eps and abs(d - 1.0) < eps:
        return "𝟏"
    # DISPLAY ONLY. `c`/`d` arrive as mpmath.mpf since the exact-word
    # change (PR #5745); mpf has no __format__ for ".4f". The comparisons
    # above stay in mpf — only the fallback label is coerced, which is a
    # string, not a computed quantity.
    return f"({float(c):.4f}σ+{float(d):.4f}𝟏)"


def particle_braid_inventory() -> dict:
    """Build an inventory of every relevant particle's braid encoding."""
    from hecke_core import (_PROTON_G0, _PROTON_G1,
                              _NEUTRON_G0, _NEUTRON_G1,
                              h as h_num)
    from mass_at_3A_proper import atom_braid_word_3A

    inventory = {}

    # Electron: σ₁³ ∈ H_2 (trefoil T_{2,3})
    e_word_cd = [(1.0, 0.0, 0)] * 3
    inventory["electron"] = {
        "particle": "e⁻ (trefoil T_{2,3})",
        "Hecke": "H_2",
        "n_strands": 2,
        "n_generators": 1,
        "word_cd": e_word_cd,
        "word_str": " · ".join(crossing_label(c, d, float(h_num)) + f"_{g}"
                                 for (c, d, g) in e_word_cd),
        "writhe": sum(1 if abs(d) < 1e-6 else (-1 if abs(d + float(h_num)) < 1e-6 else 0)
                       for (_c, d, _g) in e_word_cd),
        "n_gamma_gamma_sites": 1,    # σ₁² appears once (3 = 2+1)
    }

    # Proton: derived from nucleon_gen_chains(['u','u','d'])
    proton_word_cd = atom_braid_word_3A(1, 0)
    inventory["proton"] = _build_record(
        "proton (uud, B_3 + 2 gluon)", proton_word_cd, h_num,
        gens=[_PROTON_G0, _PROTON_G1])

    # Neutron: derived from nucleon_gen_chains(['u','d','d'])
    neutron_word_cd = atom_braid_word_3A(0, 1)
    inventory["neutron"] = _build_record(
        "neutron (udd, B_3 + 2 gluon)", neutron_word_cd, h_num,
        gens=[_NEUTRON_G0, _NEUTRON_G1])

    # Deuteron, T, ³He, ⁴He
    for label, (Z, N) in [
        ("deuteron", (1, 1)),
        ("triton",   (1, 2)),
        ("3He",      (2, 1)),
        ("4He",      (2, 2)),
    ]:
        word_cd = atom_braid_word_3A(Z, N)
        inventory[label] = _build_record(
            f"{label} (Z={Z}, N={N})", word_cd, h_num)

    return inventory


def _build_record(name, word_cd, h_num, gens=None):
    """Helper: build a braid-record dict from a (c, d, gen) triple list."""
    h = float(h_num)
    labels = [crossing_label(c, d, h) for (c, d, _g) in word_cd]
    gen_counts = Counter((g, lab) for ((_, _, g), lab) in zip(word_cd, labels))
    n_strands = max((g for (_, _, g) in word_cd), default=0) + 2
    writhe = sum(
        1 if lab == "σ" else (-1 if lab == "σ⁻¹" else 0)
        for lab in labels
    )
    sigma_squared_sites = _count_sigma_squared(word_cd)
    return {
        "particle": name,
        "Hecke": f"H_{n_strands}",
        "n_strands": n_strands,
        "n_generators": n_strands - 1,
        # c, d arrive as 50-digit mpf (PR #5745); serialize at full precision
        # via _precision.fmt rather than downcasting to float64 (qou-6sts).
        "word_cd": [(fmt(c), fmt(d), int(g)) for (c, d, g) in word_cd],
        "word_str": " · ".join(f"{lab}_{g}" for ((_, _, g), lab) in zip(word_cd, labels)),
        "word_length": len(word_cd),
        "writhe": writhe,
        "crossing_breakdown": {f"gen_{g}_{lab}": n for ((g, lab), n) in gen_counts.items()},
        "n_gamma_gamma_sites": sigma_squared_sites,
    }


def _count_sigma_squared(word_cd) -> int:
    """Count **disjoint** consecutive σ_i · σ_i pairs (γγ insertion sites).

    Per Gemini review on PR #621 (consistency with the hardcoded electron
    record `n_gamma_gamma_sites = 1` for σ_1^3): pairs are taken
    disjointly, so σ_i^k contributes ⌊k/2⌋ sites at most. After detecting
    a pair at index k, advance by 2 (skip the consumed second factor).
    """
    count = 0
    k = 0
    while k < len(word_cd) - 1:
        c1, d1, g1 = word_cd[k]
        c2, d2, g2 = word_cd[k + 1]
        if g1 == g2 and abs(c1 - 1.0) < 1e-6 and abs(d1) < 1e-6 and \
           abs(c2 - 1.0) < 1e-6 and abs(d2) < 1e-6:
            count += 1
            k += 2  # disjoint: consume both factors
        else:
            k += 1
    return count


# ─────────────────────────────────────────────────────────────────
# B. Knot-operation classification
# ─────────────────────────────────────────────────────────────────


def classify_knot_operations() -> list[dict]:
    """Classify every knot operator in the Strategy-3 chain."""
    return [
        {
            "operator": "T1: |tr_M_atomic|",
            "role": "Markov trace of the per-particle braid",
            "source": "atomic_braid_mass_table.t1_atomic_with_coupling",
            "classification": "DERIVED (closed-form via Markov axioms + Hecke quadratic)",
            "evidence": (
                "markov-trace-axiomatic-closed-form.md (proton σ₁⁷σ₂⁴); "
                "verified by option_b_proton_mass_full_chain.py to 14 digits "
                "(Phase 1.6, commit ac88823)"
            ),
            "concerns": (
                "The encoding `|tr_M(p)|^Z · |tr_M(n)|^N · a(Z,N) · Δ_n²` "
                "treats compounds as disjoint products with all interaction "
                "structure factored into a single multiplicative `a(Z,N)`. "
                "For Z+N≥3 this requires substantial canonical_a_k input; "
                "see below."
            ),
        },
        {
            "operator": "Δ_I: knot-operator quotient-braid Jones factor a(Z,N)",
            "role": "Multiplicative coupling between nucleon carriers",
            "source": "atomic_braid_mass_table.jones_quotient_factor",
            "classification": "MIXED — fallback for A≤2; canonical for A≥3 from witness with method:unknown",
            "evidence": (
                "fallback (A=1: 1; A=2: 1; A=3: 1−h²; A=4: (1−h²)²; A≥5: extrapolation); "
                "canonical: jet-knot-invariants.witness.json (³H, ³He, ⁴He, ⁶Li, ⁷Li, ⁹Be, ¹²C, ¹⁶O) "
                "with `method: unknown` per inspection"
            ),
            "concerns": (
                "FLAGGED: the canonical_a_k witness has `method: unknown`. "
                "The values 0.06484 (³H), 0.20479 (³He), 0.67676 (⁴He) are loaded "
                "as numbers without documented derivation. These are precisely the "
                "values driving the −54%, −50%, −40% errors at A=3, 4. "
                "Need to audit jet_knot_invariants.py for SDP/derivation provenance."
            ),
        },
        {
            "operator": "Δ_n²: full-twist saturated-shell scalar",
            "role": "Categorical-neutrality coupling at magic shells",
            "source": "atomic_braid_mass_table.full_twist_scalar",
            "classification": "PLACEHOLDER (always returns 1.0)",
            "evidence": (
                "full_twist_scalar(A) returns 1 unconditionally — both magic "
                "shells AND non-magic. Per docstring: "
                "'corrections via T2-T3' — but T2/T3 are identical p/n "
                "(verified in neutron_error_diagnostic.py)."
            ),
            "concerns": (
                "FLAGGED: Δ_n² is structurally trivial in the current code. "
                "The full_twist_delta_n2_verification.py witness records "
                "q^{c(λ)} eigenvalues per Wedderburn block, but these are NOT "
                "consumed by the mass-table assembly. The placeholder elides "
                "any non-trivial Δ_n² action, including at non-magic shells "
                "where the action SHOULD be q^{c(λ)} ≠ 1."
            ),
        },
        {
            "operator": "T2: brane-tower single (z² · Σ Φ_q(|V_i|))",
            "role": "Single-generator brane-tower contribution",
            "source": "atomic_braid_mass_table.t2_markov",
            "classification": "DERIVED (closed-form Markov trace at z²)",
            "evidence": (
                "Numerically identical between p and n at A=1 (0.4986). "
                "T2 = z² for any A=1 atomic-braid (no per-quark-flavor "
                "dependence beyond the trace value, which is wrapped in T1)."
            ),
            "concerns": (
                "T2 doesn't carry quark-flavor information — it's a generic "
                "brane-tower scalar. Doesn't help discriminate p from n."
            ),
        },
        {
            "operator": "T3: brane-tower pair (z⁴ · Σ Φ_q(|V_i V_j|))",
            "role": "Pair-generator brane-tower contribution",
            "source": "atomic_braid_mass_table.t3_markov",
            "classification": "DERIVED (closed-form at z⁴)",
            "evidence": "Identical p vs n (0.0622). Same comment as T2.",
            "concerns": "(same as T2)",
        },
        {
            "operator": "T4: Frobenius co-Casimir (m_e · Σ 1/dim_q(λ))",
            "role": "Wedderburn-block dimension sum",
            "source": "atomic_braid_mass_terms.t4_raw, then ·m_e",
            "classification": "DERIVED (q-hook-length explicit; Lean-closed n=2..7)",
            "evidence": (
                "frobenius-codim-universal.lean closes n=2..5; my Phase 2 / T1 "
                "extends to n=6, n=7 (commit 4e876b6). Mathematical content "
                "verified at q=1 against S_n character-degree sums."
            ),
            "concerns": (
                "Identical p vs n (2.4973) — Frobenius co-Casimir depends only "
                "on n=3A, not on quark flavor. Doesn't discriminate p from n."
            ),
        },
        {
            "operator": "T5: chirality factor (a_K · B_bulk)",
            "role": "Multiplicative chirality on T1",
            "source": "atomic_braid_mass_table (uses bw_chirality_isotopes)",
            "classification": "PARTIAL — a_K from chirality_map literal; B_bulk from bw_chirality formula",
            "evidence": (
                "chirality_map = {chiral+, chiral-, amphichiral, borromean, none} "
                "→ literal mp.mpf values per knot type. For proton: a_K = 1 "
                "(none) ⇒ T5 = 0 in Strategy-3."
            ),
            "concerns": (
                "FLAGGED: 'amphichiral' for triton + ³He, 'chiral+' for "
                "deuteron, 'borromean' for ⁴He+ — these knot-type labels are "
                "hardcoded per atom in atomic_braid_mass_table.py. Need audit "
                "of where these labels come from (knot-type identification "
                "should be SDP-driven per conj:canonical-knot-id-sdp)."
            ),
        },
        {
            "operator": "T6: cyclotomic residue tail",
            "role": "Habiro residue at roots of unity",
            "source": "atomic_braid_mass_terms.t6_canonical_MeV (in MeV)",
            "classification": "DERIVED — Habiro residue per A from witness",
            "evidence": (
                "term6-habiro-residue-mpfr-50dps.witness.json. Identical p vs n "
                "(0.6807 MeV) since T6 depends on A=1 only."
            ),
            "concerns": "(same — A-only, no quark-flavor)",
        },
        {
            "operator": "E_0: cat-unit → MeV calibration",
            "role": "Single-parameter dimensional fit",
            "source": "atomic_braid_mass_table.main: E_0 = (M_p − T6_p) / total_hecke_p",
            "classification": "FITTED (1 parameter against CODATA m_p)",
            "evidence": (
                "By construction M_pred[p] = M_p_codata = 938.272 MeV. "
                "E_0 = 199.86 MeV/cat-unit."
            ),
            "concerns": (
                "Single-parameter fit. With proton anchor fixed, neutron and "
                "compound predictions are 'genuine' (no further fits) — but "
                "the proton anchor itself is a calibration, not a derivation."
            ),
        },
    ]


# ─────────────────────────────────────────────────────────────────
# C. γγ pair-production tracking per particle
# ─────────────────────────────────────────────────────────────────


def gamma_gamma_tracking(inventory: dict) -> dict:
    """For each particle, enumerate σ²-sites (γγ candidates) and the
    per-generator σ count.

    Per content block markov-trace-axiomatic-closed-form.md:
      σ_i² = h·σ_i + 𝟏  (Hecke quadratic)
      γγ = σ_i² → h·σ_i + 𝟏 (pair-production reduction)
    """
    out = {}
    for label, rec in inventory.items():
        # per-generator σ-count, plus disjoint γγ-site count via the
        # canonical _count_sigma_squared (matches the hardcoded electron
        # record and the rec["n_gamma_gamma_sites"] field).
        sigma_per_gen: Counter = Counter()
        for ((_c, d, g), lab) in zip(rec["word_cd"],
                                       [_l for _l in rec["word_str"].split(" · ")]):
            if "σ" in lab and "σ⁻¹" not in lab and "+" not in lab:
                sigma_per_gen[g] += 1
        out[label] = {
            "particle": rec["particle"],
            "n_sigma_per_gen": dict(sigma_per_gen),
            "n_gamma_gamma_sites": rec["n_gamma_gamma_sites"],
            "n_sigma_inverse": sum(1 for lab in rec["word_str"].split(" · ") if "σ⁻¹" in lab),
            "n_averaged": sum(1 for lab in rec["word_str"].split(" · ") if "½" in lab),
            "writhe": rec["writhe"],
        }
    return out


# ─────────────────────────────────────────────────────────────────
# D. Cross-check |tr_M| via independent paths
# ─────────────────────────────────────────────────────────────────


def cross_check_tr_M() -> dict:
    """Compare Strategy-3's |tr_M| values to the closed-form derivation
    (Phase 1.6 / option_b_proton_mass_full_chain.py)."""
    out = {}
    # Strategy-3 (atomic-braid-mass-table.witness.json)
    s3_path = _pb.witness_path("atomic-braid-mass-table.witness.json", HERE)
    s3 = record_upstream(s3_path, _UPSTREAM_RECORDS) if s3_path.exists() else {"data": {"rows": []}}
    s3_rows = {r["atom"]: r for r in s3.get("data", {}).get("rows", [])}

    # Phase 1.6 closed-form (option-b-proton-mass-full-chain.witness.json)
    ob_path = _pb.witness_path("option-b-proton-mass-full-chain.witness.json", HERE)
    ob = record_upstream(ob_path, _UPSTREAM_RECORDS) if ob_path.exists() else {}
    ob_at_q0 = ob.get("data", {}).get("tr_M_at_q0", {})

    # Markov-trace assembly chain (markov-trace-assembly-proton.derivation.json)
    chain_path = _pb.witness_path("markov-trace-assembly-proton.derivation.json", HERE)
    chain_value = None
    if chain_path.exists():
        chain = json.loads(chain_path.read_text())
        chain_value = chain.get("target_value")

    def _s3(key):
        """Strategy-3 tr_M for one nucleon, or None if the upstream row lacks it.

        This used to be `float(row.get("term1_atomic_total", "nan"))` — the
        DEFAULT was the string "nan", so a missing upstream key turned silently
        into a NaN float, which json.dump then wrote as a bare NaN token. That
        made this witness invalid JSON and presented "upstream did not supply
        this" as though it were a computed number.
        """
        raw = s3_rows.get(key, {}).get("term1_atomic_total")
        if raw is None:
            return None
        try:
            return float(raw)
        except (TypeError, ValueError):
            return None

    out["proton"] = {
        "strategy_3_tr_M": _s3("p"),
        "strategy_3_tr_M_missing": s3_rows.get("p", {}).get(
            "term1_atomic_total") is None,
        "phase_1_6_closed_form": ob_at_q0.get("proton"),
        "markov_trace_assembly_chain": chain_value,
        # markov-trace-axiomatic-closed-form.md line 29 quotes
        #   tr_M(σ_1^7 σ_2^4)(q_0) ≈ 1.88432  (convention D, proton pin).
        # The prior 1.63315 here was the convention-C / muon-pin value and
        # disagreed with this audit's own upstream (phase_1_6_closed_form) by
        # 15%. Carried as the content block's VERBATIM 6-sig-fig string — this
        # is a `\approx` quote, not a truncation of a stored full-precision
        # value, so padding it out with fmt() would fabricate digits the source
        # does not carry (qou-btqh; see draining-raw-float64 decision procedure).
        "axiomatic_content_block": "1.88432",
    }
    out["neutron"] = {
        "strategy_3_tr_M": _s3("n"),
        "strategy_3_tr_M_missing": s3_rows.get("n", {}).get(
            "term1_atomic_total") is None,
        "phase_1_6_closed_form": None,        # not computed there
        "axiomatic_content_block": "(σ₁⁷σ₂⁴ used for proton; udd encoding differs — needs separate closed form)",
    }
    out["electron"] = {
        "strategy_3_tr_M": "(not in Strategy-3 mass table — uses bare nucleon braids only)",
        "phase_1_6_closed_form": ob_at_q0.get("electron"),
    }
    return out


# ─────────────────────────────────────────────────────────────────
# E. Structural finding cross-reference
# ─────────────────────────────────────────────────────────────────


STRUCTURAL_FINDING = {
    "source": "computations/fresh_derivation_pn_true_sdp.py:1-26",
    "claim": (
        "Per the framework's own SDP audit (commit history pre-dates "
        "this audit): 'Absolute m_p and m_n are NOT directly derivable "
        "from γγ → target Hecke-energy distance because entanglement "
        "energy (pre-observable complex-q sector) is gauged away. Only "
        "DIFFERENCES/RATIOS project to observables. The clean prior "
        "result is: m_n − m_p = S_dd − S_uu = "
        "((q+q⁻¹)/(q^{1/2}+q^{-1/2})) · (μ_d − μ_u), giving < 1 ppm on "
        "Δm across isotopes once μ_d − μ_u is calibrated from CODATA.'"
    ),
    "implication": (
        "Strategy-3 (atomic_braid_mass_table.py) computes |tr_M(p)| and "
        "|tr_M(n)| separately and combines via E_0 calibration. This "
        "violates the framework's own claim — the bare absolute traces "
        "are not observables. The −8.3% neutron error is a direct "
        "consequence: the σ↔σ⁻¹ asymmetry between uud and udd is real "
        "in the Hecke algebra but does NOT correspond to a physical "
        "absolute-mass observable in the framework's stated semantics."
    ),
    "actionable_path": (
        "The framework predicts m_n − m_p (an observable) via the "
        "(q+q⁻¹)/(q^{1/2}+q^{-1/2})·(μ_d − μ_u) formula at < 1 ppm. "
        "Strategy-3 should consume this difference formula directly "
        "rather than deriving m_n independently from |tr_M(n)|. A "
        "two-step calibration: (a) anchor m_p via CODATA (or via a "
        "different absolute-mass channel), (b) derive m_n = m_p + "
        "(q+q⁻¹)/(q^{1/2}+q^{-1/2})·(μ_d − μ_u)."
    ),
}


# ─────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────


def main() -> int:
    print("=" * 100)
    print("BRAID-ENCODING + KNOT-OPERATION AUDIT (Phase 1.8)")
    print("=" * 100)

    print("\n── Section A: braid encodings ──")
    inventory = particle_braid_inventory()
    for label, rec in inventory.items():
        print(f"  {label:<10} ({rec['Hecke']}, {rec['n_strands']} strands, len={rec.get('word_length', len(rec['word_cd']))}):")
        print(f"    word: {rec['word_str'][:140]}")
        print(f"    writhe: {rec['writhe']:+d}, γγ-sites: {rec['n_gamma_gamma_sites']}")

    print("\n── Section B: knot-operation classification ──")
    classifications = classify_knot_operations()
    print(f"  {'operator':<45} {'classification':<40}")
    for c in classifications:
        print(f"  {c['operator'][:45]:<45} {c['classification'][:40]:<40}")

    print("\n── Section C: γγ tracking per particle ──")
    gg = gamma_gamma_tracking(inventory)
    print(f"  {'particle':<12} {'σ-per-gen':<25} {'γγ-sites':<10} {'σ⁻¹':<6} {'avg':<6} {'writhe':<7}")
    for label, info in gg.items():
        print(f"  {label:<12} {str(info['n_sigma_per_gen'])[:25]:<25} "
              f"{info['n_gamma_gamma_sites']:<10} "
              f"{info['n_sigma_inverse']:<6} {info['n_averaged']:<6} "
              f"{info['writhe']:<+7d}")

    print("\n── Section D: cross-check |tr_M| via independent paths ──")
    xc = cross_check_tr_M()
    for atom, vals in xc.items():
        print(f"  {atom}:")
        for k, v in vals.items():
            print(f"    {k}: {v}")

    print("\n── Section E: structural finding ──")
    print(f"  Source: {STRUCTURAL_FINDING['source']}")
    print(f"  Claim: {STRUCTURAL_FINDING['claim'][:200]}…")
    print(f"  Implication: {STRUCTURAL_FINDING['implication'][:300]}…")

    # Witness
    w = WitnessBuilder("braid-encoding-audit", engine="python")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Phase 1.8 audit per user directive: validate braid encodings of p "
        "and n, classify all knot operations (SDP / Lean / fitted / fallback "
        "/ placeholder), track γγ pair-production per particle, and identify "
        "where the structural differences really are.  Findings: "
        "(1) Δ_n² is a placeholder (returns 1.0 always); "
        "(2) canonical_a_k for ³H/³He/⁴He has method:unknown in source witness; "
        "(3) framework's own fresh_derivation_pn_true_sdp.py documents that "
        "absolute m_p / m_n are NOT directly derivable — only differences "
        "project to observables — but Strategy-3 ignores this and predicts "
        "m_n directly, hence the −8.3% error."
    )
    w.set_content_block("prop:atomic-mass-gb-nf")
    # Carry the anchor at its 50-digit source rather than the float64 alias
    # Q/HA; h = q - 1/q recomputed at compute precision (qou-6sts).
    _q0_mp = mp.mpf(Q_50_DIGIT_STR)
    w.add_parameter("q_0", fmt(_q0_mp))
    w.add_parameter("h", fmt(_q0_mp - 1 / _q0_mp))
    w.add_data("braid_inventory", inventory)
    w.add_data("knot_operation_classifications", classifications)
    w.add_data("gamma_gamma_per_particle", gg)
    w.add_data("tr_M_cross_check", xc)
    w.add_data("structural_finding", STRUCTURAL_FINDING)

    # ── ROUTE 1: give this audit assertions it can actually FAIL ───────────
    #
    # Until now this script emitted ZERO assertions and `allPassed: true`, so
    # it could not fail. That state was deliberate and half-right: bean
    # `qou-26f2` removed three `add_assertion(computed=True, expected=True)`
    # checks *because* they passed by construction, and recorded them as
    # findings instead. Correct as far as it went -- but it left the audit with
    # nothing checkable, while `tr_M_cross_check` above was already computing a
    # genuine three-way comparison of the SAME quantity, tr_M(p, q_0), and
    # asserting nothing about it. These assert on that.
    #
    # They are NOT tuned to pass. Assertion 2 FAILS on the current corpus, and
    # that failure is the point: two independent routes to tr_M(p, q_0)
    # disagree far outside either one's stated tolerance, and the disagreement
    # has been sitting in this witness unremarked.
    _p = xc.get("proton", {})
    # Upstream tr_M values now arrive as full-precision STRINGS (the producers
    # were drained to carry mpmath.mpf end to end -- qou-btqh), and
    # axiomatic_content_block is the content block's verbatim 6-sig-fig string.
    # Convert to mpf for the comparison arithmetic and serialize each `computed`
    # via fmt, so this audit's own assertions are exact-arithmetic, not float64.
    _ob_raw = _p.get("phase_1_6_closed_form")
    _ax_raw = _p.get("axiomatic_content_block")
    _ch_raw = _p.get("markov_trace_assembly_chain")

    def _to_mpf(x):
        if x is None:
            return None
        try:
            return mp.mpf(str(x))
        except (TypeError, ValueError):
            return None

    _ob = _to_mpf(_ob_raw)
    _ax = _to_mpf(_ax_raw)
    _ch = _to_mpf(_ch_raw)

    # (1) The hardcoded content-block value must track the live upstream.
    #     This is the check whose ABSENCE let the block sit at the
    #     convention-C/muon value (1.63315, 15% off) until someone noticed by
    #     eye -- see the comment on `axiomatic_content_block` above. Tolerance
    #     is 1e-5 relative: the block carries 6 significant figures, so it
    #     cannot track the upstream more tightly than that.
    if _ob is not None and _ax is not None:
        w.add_assertion(
            "axiomatic content block tracks the phase-1.6 closed form",
            computed=fmt(abs(_ax - _ob) / abs(_ob)), expected="0.0",
            tolerance="1e-5",
            source=f"axiomatic_content_block={_ax_raw}, phase_1_6_closed_form={_ob_raw}; "
                   "the content block quotes 6 sig figs")

    # (2) The two INDEPENDENT derivations of tr_M(p, q_0) must agree.
    #     `markov-trace-assembly-proton.derivation.json` declares
    #     `target = "tr_M(p, q_0) [canonical Wenzl-bridge]"` with
    #     `target_tolerance = 1e-09`; the option-b chain computes the same
    #     quantity. They differ by 43.46% (normalised by the option-b value;
    #     76.88% the other way round -- ONE gap under two normalisations, not
    #     two findings). Asserted at 1e-3, four orders looser than the
    #     derivation's own claimed tolerance, so this is not a tight-tolerance
    #     artifact.
    # UPDATE 2026-09-13 (bean qou-4383). The assembly-chain side of this
    # comparison moved from the grouped-era 1.145759692457300869689081 to the
    # canonical 0.629328402202922, because
    # markov-trace-assembly-proton.derivation.json now has a live builder on
    # the canonical 11-letter element (bean qou-nhkv). It was an ORPHAN before,
    # frozen in the pre-ruling frame.
    #
    # THIS ASSERTION STILL FAILS, AND THE GAP WIDENED — 43.46% -> ~67%. That is
    # not a regression, and the fix is not to loosen it. The OTHER side,
    # `phase_1_6_closed_form` = 1.884319467…, is computed on the ALL-POSITIVE
    # sigma^7 sigma^4 word, which `trm_proton_five_values_census` (bean
    # qou-soj6) established is a DIFFERENT element of H_3(q) from the canonical
    # one — {sigma: 6, sigma_inv: 3, averaged: 2}. So the two sides were never
    # computing the same object, and the assembly side simply stopped sharing
    # the other's error. Closing this needs the option-b side recomputed on the
    # canonical word, not a tolerance.
    if _ob is not None and _ch is not None:
        w.add_assertion(
            "the two independent tr_M(p,q0) derivations agree",
            computed=fmt(abs(_ch - _ob) / abs(_ob)), expected="0.0",
            tolerance="1e-3",
            source=f"markov_trace_assembly_chain={_ch_raw} (Wenzl-bridge, its own "
                   f"target_tolerance=1e-9) vs phase_1_6_closed_form={_ob_raw} "
                   "(option-b full chain). EXPECTED TO FAIL -- see bean qou-soj6")

    # (3) Records the deleted Strategy-3 upstream as absent, and FAILS if it
    #     ever silently returns. It was removed 2026-05-19 (commit
    #     7f30a57924d, owner directive) for carrying 24-54% errors, so its
    #     reappearance is a regression, not a repair.
    w.add_assertion(
        "the retired Strategy-3 mass table has not returned",
        computed=1 if _p.get("strategy_3_tr_M_missing") else 0,
        expected=1, tolerance=0,
        source="atomic-braid-mass-table.witness.json was deleted by owner "
               "directive (7f30a57924d); this audit must not start consuming "
               "it again")
    # These three were `add_assertion(computed=True, expected=True)` — they
    # passed by construction and contributed to `allPassed` without checking
    # anything (bean `qou-26f2`). Each *documents* a finding this audit made by
    # reading; none of the three is a computation this script performs, so the
    # remedy is to record them as findings rather than dress them as checks.
    #
    # Two are worse than vacuous, and re-checking them is how that surfaced:
    #
    #   * `full_twist_scalar` lived in `atomic_braid_mass_table`, which no
    #     longer exists anywhere in the repo. The name now survives only as a
    #     string in this file and in `delta_n2_placeholder_audit.py`, which
    #     reads the *legacy witness* rather than the module and says so.
    #   * `jet-knot-invariants.witness.json` carries no `method` field at all
    #     — no `canonical_a_k` key either. The witness was rebuilt since (it
    #     has `q0Anchor`/`q0Value`), and the provenance gap this recorded is
    #     no longer stated where it was found.
    #
    # So both are claims about subjects that have moved, and as assertions
    # they would have gone on reporting green forever. Recorded here with
    # their verification status attached, which is the part that was missing.
    w.add_data("audit_findings", {
        "delta_n_squared_is_placeholder": {
            "finding": "full_twist_scalar(A) returned mp.mpf(1) unconditionally",
            "source": "atomic_braid_mass_table.full_twist_scalar",
            "verifiable_here": False,
            "note": "defining module no longer present in the repo; the "
                    "legacy record is atomic-braid-mass-table.witness.json, "
                    "which delta_n2_placeholder_audit.py reads by design",
        },
        "canonical_a_k_method_unknown": {
            "finding": "canonical_a_k for 3H/3He/4He had method: 'unknown'",
            "source": "jet-knot-invariants.witness.json",
            "verifiable_here": False,
            "note": "that witness now carries neither a `method` field nor a "
                    "`canonical_a_k` key; re-check against the current "
                    "producer before citing this finding",
        },
        "neutron_error_localised_to_T1_trace_asymmetry": {
            "finding": "the neutron error localises to the T1 trace asymmetry",
            "source": "neutron_error_diagnostic.py",
            "verifiable_here": False,
            "note": "asserted from a sibling script's output, not recomputed "
                    "here; that script is still present",
        },
    })
    w.save()
    print(f"\n✓ Witness: braid-encoding-audit.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
