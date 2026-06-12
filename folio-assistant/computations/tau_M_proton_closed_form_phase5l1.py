"""
tau_M_proton_closed_form_phase5l1.py — Phase 5l.1: symbolic closed
form for the **structural** Markov trace `T(B_p, q)` of the proton
braid in H_3(q).

  NORMALIZATION CAVEAT (read this before using the output):

  This script computes the STRUCTURAL form
    T(B_p, q) := Σ_{λ ⊢ 3} y_λ(q) · χ_λ(B_p, q)
  using the symbolic Wenzl-bridge y_λ.  It is NOT the canonical
  Markov trace tr_M^3(𝓑_p, q) reported in
  rho-constit-equals-tau-M-proton-phase5l.witness.json.

  Phase 5l.2 reconciliation finding (`normalization-reconciliation-phase5l2.witness.json`):
  the relationship between T(B_p, q) and the canonical tr_M^3 is
  **NOT a simple q-independent multiplicative constant** — both
  hypotheses A (T at q, rel.spread 5.9e-2) and B (T at q^2,
  rel.spread 8.1e-1) were FALSIFIED across the 5-point substrate
  window.  The Wenzl-bridge symbolic implementation uses a deeper
  convention mismatch (likely a different y_λ normalization that
  depends on partition structure as well as q).  Full reconciliation
  is queued as a research task.

Phase 5l identified ρ_Z^constit(q) = tr_M^3(𝓑_p, q) as the
structural identity for the constit-side per-Z step factor in the
canonical-atom Markov trace.  Phase 5l.1 extracts T(B_p, q) — the
un-normalised structural variant — as a closed-form Laurent
rational in q.

The proton braid B_p in H_3(q) — built from the canonical
intra-nucleon chains _PROTON_G0 / _PROTON_G1 in hecke_core.py — is
a specific 11-generator Hecke word.  Each partition contributes:

- (3): trivial rep, χ_(3)(σ_i) = q, so χ_(3)(B_p) = q^writhe(B_p)
- (1,1,1): sign rep, χ_(1,1,1)(σ_i) = -q^{-1}
- (2,1): 2-dimensional Hoefsmit seminormal rep — symbolic matrix
  product through hecke_character_symbolic.q_character_on_braid_word

y_λ(q) via y_lambda_wenzl_bridge.y_lambda_wenzl_bridge_symbolic.

Output: a sympy expression for the STRUCTURAL T(B_p, q) — a
Laurent rational in q.

  Ref: prop:constit-factor-tau-M-proton-identity.md (Phase 5l)
  Ref: hecke_character_symbolic.py (symbolic Hoefsmit matrices)
  Ref: y_lambda_wenzl_bridge.py (Wenzl y_λ closed form)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from hecke_character_symbolic import q_character_on_braid_word  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic  # noqa: E402
from canonical_braid_marshalling import marshal_to_symbolic_braid  # noqa: E402

# h(q_0) value used to canonical-marshal the f64 atom braid word into
# the symbolic (gen_idx, cross_type) format below.
from q_parameter import Q as _Q_F64  # noqa: E402
_H_F64 = float(_Q_F64 - 1 / _Q_F64)


def proton_braid_word_symbolic():
    """H_3 proton braid as [(gen_0idx, cross_type), ...] matching
    `hecke_character_symbolic.q_character_on_braid_word` format.

    Derived from `mass_at_3A_proper.atom_braid_word_3A(1, 0,
    include_inter=False)` (the canonical f64 word for a single
    proton block); marshalling is delegated to the shared
    `canonical_braid_marshalling.marshal_to_symbolic_braid` utility
    so the convention (d ≈ 0 → "sigma", d ≈ -h → "sigma_inv",
    d ≈ -h/2 → "averaged") lives in exactly one place.

    Per Copilot PR #863 review: previously this function re-implemented
    the marshalling inline, risking convention drift if
    `atom_braid_word_3A` ever changed.
    """
    raw = atom_braid_word_3A(1, 0, include_inter=False)
    return marshal_to_symbolic_braid(raw, _H_F64)


def _cross_to_cd(cross_type: str, q: sp.Symbol):
    """Map cross_type string to (c, d) Hecke coefficients."""
    h = q - 1 / q
    if cross_type == "sigma":
        return sp.Integer(1), sp.Integer(0)
    if cross_type == "sigma_inv":
        return sp.Integer(1), -h
    if cross_type == "averaged":
        return sp.Integer(1), -h / 2
    raise ValueError(f"Unknown cross_type: {cross_type}")


def chi_lambda_trivial_symbolic(braid_word, q: sp.Symbol) -> sp.Expr:
    """χ^(n)(w) for trivial rep: each σ_i ↦ q, so c·σ + d·1 ↦ c·q + d."""
    val = sp.Integer(1)
    for _gen, cross_type in braid_word:
        c, d = _cross_to_cd(cross_type, q)
        val = val * (c * q + d)
    return sp.expand(val)


def chi_lambda_sign_symbolic(braid_word, q: sp.Symbol) -> sp.Expr:
    """χ^(1^n)(w) for sign rep: each σ_i ↦ -q^{-1}, so c·σ + d·1 ↦ -c/q + d."""
    val = sp.Integer(1)
    for _gen, cross_type in braid_word:
        c, d = _cross_to_cd(cross_type, q)
        val = val * (-c / q + d)
    return sp.expand(val)


def main() -> int:
    builder = WitnessBuilder(
        "tau-M-proton-closed-form-phase5l1", engine="sympy"
    )
    # Per user direction "don't do full infra yet" — this script is
    # probe-style with no content-block wiring (the symbolic tr_M
    # awaits Phase 5l.2 normalization reconciliation before promotion).
    # Mark audit-only so the manifest-wiring audit doesn't flag this
    # witness as an orphan claim.
    builder.set_audit_only("docs/audits/2026-05-20-constit-factor-closure-chain.md")

    q = sp.Symbol("q", positive=True, real=True)
    print(f"=== Phase 5l.1: symbolic T(B_p, q) [structural form; see header for normalization caveat] ===\n")

    # Build proton braid word symbolically
    braid_word = proton_braid_word_symbolic()
    print(f"Proton braid word (H_3): {len(braid_word)} crossings")

    # χ^λ for each partition.  Lighter normalization (sp.together)
    # used inline; final cancel only on the assembled tr_M below.
    chi_results = {}
    for lam_tuple, fn in [
        ((3,), chi_lambda_trivial_symbolic),
        ((1, 1, 1), chi_lambda_sign_symbolic),
    ]:
        t0 = time.time()
        chi = fn(braid_word, q)
        chi_results[lam_tuple] = chi
        print(f"  χ^{lam_tuple}(B_p, q) = {chi}   "
              f"[{time.time()-t0:.2f}s]")

    # (2,1) via Hoefsmit (symbolic 2x2 matrix product).
    # q_character_on_braid_word expects [(gen_idx, cross_type), ...]
    # where cross_type ∈ {"sigma", "sigma_inv", "averaged"}.
    t0 = time.time()
    chi_21 = q_character_on_braid_word(
        [2, 1], braid_word, q,
    )
    chi_results[(2, 1)] = chi_21
    print(f"  χ^(2,1)(B_p, q) ... [{time.time()-t0:.2f}s]")
    print(f"  χ^(2,1)(B_p, q) = {chi_21}")

    # Symbolic y_λ via the canonical Wenzl-bridge implementation —
    # the repo's authoritative symbolic source for Wenzl-Markov
    # weights (matches numeric `y_lambda_wenzl_bridge_numeric` modulo
    # a Q = q^2 substitution convention; see Phase 5l.2 queue).
    print(f"\nComputing y_λ(q) symbolically via Wenzl-bridge:")
    y_results = {}
    for lam in [(3,), (2, 1), (1, 1, 1)]:
        t0 = time.time()
        y_sym = y_lambda_wenzl_bridge_symbolic(list(lam))
        # The symbolic implementation uses its own q symbol — substitute
        # any free symbol named other than "q" with ours.  Iterate over
        # sorted free symbols for determinism (set iteration order in
        # CPython is insertion-order but sympy may reorder; sort by name
        # so the substitution result does not depend on hash randomization
        # — Gemini PR #854 review).
        for sym in sorted(y_sym.free_symbols, key=lambda s: s.name):
            if sym.name != "q":
                y_sym = y_sym.subs(sym, q)
        # Skip per-term simplification (expensive on degree-80+
        # expressions); the assembled tr_M sum below is normalised
        # via sp.together — a §6 escalation outcome on PR #854: an
        # earlier Copilot review flagged sp.cancel as a P15 hotspot
        # on full y_λ·χ_λ sums.  sp.together brings to a common
        # denominator without invoking full GCD reduction, which
        # keeps the probe runnable in CI.
        y_results[lam] = y_sym
        print(f"  y^{lam}(q) computed [{time.time()-t0:.2f}s]")
    print()

    # Sum: T(B_p, q) [structural form; see header for normalization caveat] = Σ y_λ · χ_λ
    tau_M_sym = sp.together(sum(
        y_results[lam] * chi_results[lam] for lam in [(3,), (2, 1), (1, 1, 1)]
    ))
    print(f"\nT(B_p, q) [structural form; see header for normalization caveat] (symbolic structural form) =")
    print(f"  {tau_M_sym}")

    # Numerical check at q_0 — use canonical 50-digit pin from
    # q_parameter (not float-derived) so the substituted value is
    # at full precision, not f64-quantized + zero-padded.
    q0_sympy = sp.Float(Q_50_DIGIT_STR, 50)
    tau_M_at_q0 = sp.N(tau_M_sym.subs(q, q0_sympy), 30)
    print(f"\nT(B_p, q_0) symbolic → numeric = {tau_M_at_q0}")
    # Load the canonical Phase 5l empirical value from its witness
    # (Copilot PR #863 review: do not hardcode — the prior 5-digit
    # truncation didn't match the witness's mpfr-50-dps value).
    p5l_witness_path = HERE / "rho-constit-equals-tau-M-proton-phase5l.witness.json"
    canonical_empirical_str = "unavailable"
    try:
        with p5l_witness_path.open() as f_witness:
            p5l_data = json.load(f_witness)
        for row in p5l_data["data"]["per_q_results"]:
            if abs(float(row["q"]) - float(q0_sympy)) < 1e-6:
                canonical_empirical_str = row["tau_M_proton_H3_str"]
                break
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass
    print(f"Canonical tr_M^3(𝓑_p, q_0) empirical (Phase 5l) = {canonical_empirical_str}")
    print(f"(differ by a non-trivial convention mismatch — see header + Phase 5l.2)")

    # See module docstring's NORMALIZATION CAVEAT: T(B_p, q) is the
    # structural variant and may differ from the canonical tr_M^3(𝓑_p, q)
    # by a q-independent constant.  The IMPORTANT result is the
    # q-DEPENDENCE: T(B_p, q) is a specific Laurent rational in q,
    # derivable in closed form from the H_3 character formulas.

    # Witness
    builder.add_parameter("q_symbol", "q")
    builder.set_description(
        "Phase 5l.1: symbolic closed-form derivation of T(B_p, q) [structural form; see header for normalization caveat] "
        "as a Laurent rational in q.  Decomposes the Markov trace as "
        "Σ_λ y_λ(q) · χ_λ(B_p, q) over partitions of 3.  Uses "
        "trivial / sign reps directly (scalar Hecke values) and "
        "Hoefsmit symbolic 2x2 matrices for (2,1).  y_λ(q) given by "
        "the Wenzl-bridge structural form (∝ q-hook-content)."
    )
    builder.add_data("chi_lambda", {
        str(lam): sp.sstr(chi) for lam, chi in chi_results.items()
    })
    builder.add_data("y_lambda_structural", {
        str(lam): sp.sstr(y) for lam, y in y_results.items()
    })
    # Field name reflects the structural-form caveat from the
    # module docstring (Copilot PR #854 review): T(B_p, q) is the
    # un-normalised symbolic variant, NOT the canonical tr_M^3.
    builder.add_data("T_proton_structural_symbolic", sp.sstr(tau_M_sym))
    builder.add_data("T_proton_structural_at_q0_eval",
                     str(tau_M_at_q0))
    builder.add_data("normalization_note",
                     "T(B_p, q) is the structural symbolic form (∝ Wenzl "
                     "y_λ).  Differs from canonical tr_M^3(𝓑_p, q) "
                     "[Phase 5l witness] by a q-independent constant.  "
                     "Phase 5l.2 reconciles the normalization.")
    builder.add_data("lean_uniqueness_ref", {
        "nucleus": "proton",
        "theorem": "qou:QOU.BraidKnot.NucleusEmptySDPUniqueness.nucleus_uniqueness_closed (parameterised by crossing count n)",
        "framework_doc": "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "T_w uniqueness at the abstract empty-constraint SDP level (PR #1537/#1542 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    builder.save()
    print(f"\nWitness written: tau-M-proton-closed-form-phase5l1.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
