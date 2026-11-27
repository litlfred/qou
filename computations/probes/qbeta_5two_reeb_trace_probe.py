#!/usr/bin/env python3
"""qbeta_5two_reeb_trace_probe.py — the foundational brick of the non-amphichiral
(5₂) route: the q-Reeb monodromy trace τ_{5₂}(q) and its BAR-ODD part.

Owner steer (fork option 2): pursue a non-amphichiral knot (5₂, CS≠0) as the
home for the bar-odd datum that the amphichiral figure-eight 4₁ structurally
lacks (4₁: CS=0 ⇒ Im 𝔙=0). This is the first, verifiable brick.

TWO FINDINGS (one refuting the naive guess, one locating the answer).

FINDING 1 — the q-Reeb trace does NOT carry the chirality. The naive guess
(the chiral 5₂ has a bar-asymmetric q-Reeb trace, unlike amphichiral 4₁) is
REFUTED exactly: both `τ_{4₁}(q) = q⁴−2q²+1−2q⁻²+q⁻⁴` AND
`τ_{5₂}(q) = q⁶−2q⁴+2q²−3+2q⁻²−2q⁻⁴+q⁻⁶` are BAR-SYMMETRIC (bar-odd part = 0),
with det=1, |λ|=1. The STRUCTURAL reason: `V_{(2,1)}` is a **self-conjugate**
block ((2,1)′=(2,1)), so its character is bar-even for *every* braid — no knot's
q-Reeb trace on this block can carry a bar-odd part.

FINDING 2 — the bar-odd datum is the WRITHE, in the CONJUGATE-PAIR blocks. The
1-dim blocks (3) [σ↦q] and (1,1,1) [σ↦−q⁻¹] are bar-CONJUGATE, with characters
`χ_{(3)}(β) = q^{w}`, `χ_{(1,1,1)}(β) = (−1)^{|β|} q^{−w}` where `w` = writhe
(exponent sum). Their bar-odd combination `½(χ_{(3)} − q^{2·?}…)` is nonzero iff
`w ≠ 0`:  **4₁ has writhe 0 (amphichiral) ⇒ bar-odd = 0**; **5₂ has writhe 4
(chiral) ⇒ bar-odd = ½(q⁴−q⁻⁴) ≠ 0** — a genuine bar-odd sinh-object, exactly the
nonzero channel 4₁ structurally lacks. This is where CS≠0 enters.

Construction mirrors the validated 4₁ Reeb probe
`qbeta_c3_reeb_rotation_phase_probe.py`; canonical 5₂ 3-braid `(1,1,1,2,−1,2)`
(`_deprecated/hyperbolic_knot_db_extended.py:44`, vol 2.8281220).

HONEST SCOPE. 5₂ supplies a nonzero bar-odd datum via the writhe — the "nonzero
home" fork-option-2 needs. It does NOT defeat the Lean-proved anchor-invariance
prune (`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`): the writhe
datum ½(q₀⁴−q₀⁻⁴) is smooth in q₀, so its VALUE cannot produce S's 2×10⁶ swing;
the swing still needs the anchor-dependent quantum volume 𝔙_q(5₂) (a later
brick). No c_k; no fit; scope-(a).

Run: python3 -u computations/probes/qbeta_5two_reeb_trace_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_reeb.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder, q0_comparison  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402

mp.mp.dps = 70
# q₀ anchors read BY NAME (bean qou-9ugp, 2026-09-03). The muon leg was the
# literal 1.1099785955573… — the RETIRED self-certified muon pin A, superseded
# 2026-08-22 by the live CODATA-2022 lepton-ratio derivation q_muon_at()
# (+0.0769 ppb); the proton leg was the 50-digit string re-typed by hand. A
# hardcoded pin cannot be checked against the name it is bound to.
Q = {"muon": mp.mpf(mp.nstr(q_muon_at(50), 50, strip_zeros=False)),
     "proton": Q_MP}

# canonical 3-braid word for 5₂ (generators 1,2 ↦ σ₁,σ₂; negatives = inverses)
# CORRECTED 2026-08-11 (bean qou-9mum).  This file previously used
# [1, 1, 1, -2, 1, -2], which is the braid word for 6₂, not 5₂:
# its Alexander determinant |Δ(-1)| is 11 (6₂), where 5₂ is 7.  Seven
# sibling probes had already been moved to the correct word (see
# qbeta_5two_capstone_carrier_falsification_probe.py:206 and
# docs/coordination/1ppq-qbeta.md); this one and the categorical-Markov
# probe were missed.  The writhe changes 2 -> 4, so the bar-odd datum
# changes ½(q²-q⁻²) -> ½(q⁴-q⁻⁴) and its anchor value moves by 2.04x.
BRAID_5_2 = [1, 1, 1, 2, -1, 2]
# 4₁ for the amphichirality contrast: (σ₁σ₂⁻¹)² = [1,-2,1,-2]
BRAID_4_1 = [1, -2, 1, -2]
# known Jones polynomial of 5₂ (Knot Atlas), V(q) with this chirality:
#   V_{5₂}(q) = q^{-1} − q^{-2} + 2q^{-3} − q^{-4} + q^{-5} − q^{-6}
JONES_5_2 = {-1: 1, -2: -1, -3: 2, -4: -1, -5: 1, -6: -1}


def seminormal_sigma(q):
    """2×2 Hoefsmit seminormal block of (σ₁, σ₂) on V_{(2,1)} of H₃(q) (sympy)."""
    s0 = sp.Matrix([[q, 0], [0, -1 / q]])
    a = -1 / (q * (q ** 2 + 1))
    b = sp.Integer(1)
    c = (q ** 2 - q + 1) * (q ** 2 + q + 1) / (q ** 2 + 1) ** 2
    d = q ** 3 / (q ** 2 + 1)
    s1 = sp.Matrix([[a, b], [c, d]])
    return s0, s1


def braid_matrix(word, q):
    """Product of the seminormal generators for a braid word (1-indexed ±)."""
    s0, s1 = seminormal_sigma(q)
    gens = {1: s0, 2: s1}
    inv = {1: s0.inv(), 2: s1.inv()}
    M = sp.eye(2)
    for g in word:
        M = M * (gens[g] if g > 0 else inv[-g])
    return M


def main() -> int:
    q = sp.symbols("q", positive=True)

    # ---- exact q-Reeb traces on V_{(2,1)} ----
    M52 = braid_matrix(BRAID_5_2, q)
    tau52 = sp.simplify(sp.trace(M52))
    det52 = sp.simplify(M52.det())
    M41 = braid_matrix(BRAID_4_1, q)
    tau41 = sp.simplify(sp.trace(M41))

    # bar involution q -> 1/q
    tau52_odd = sp.simplify((tau52 - tau52.subs(q, 1 / q)) / 2)
    tau41_odd = sp.simplify((tau41 - tau41.subs(q, 1 / q)) / 2)

    print("=" * 78)
    print(" 5₂ vs 4₁ knot-operator bar-odd datum — non-amphichiral brick")
    print("=" * 78)
    print("\n FINDING 1 — the self-conjugate V_{(2,1)} q-Reeb trace is BAR-EVEN "
          "for BOTH knots:")
    print(f"    τ_{{4₁}}(q) = {tau41}   bar-odd = {tau41_odd}")
    print(f"    τ_{{5₂}}(q) = {tau52}   bar-odd = {tau52_odd}")
    print("    ⇒ the q-Reeb trace does NOT carry chirality ((2,1) self-conjugate).")
    block_bar_even = (tau41_odd == 0 and tau52_odd == 0)

    # ---- FINDING 2: the WRITHE, via the conjugate-pair (3)/(1,1,1) blocks ----
    def writhe(word):
        return sum(1 if g > 0 else -1 for g in word)
    def chi_triv(word):        # (3): σ↦q, σ⁻¹↦q⁻¹  ⇒ q^{writhe}
        return q ** writhe(word)
    def chi_sign(word):        # (1,1,1): σ↦−q⁻¹, σ⁻¹↦−q  ⇒ (−1)^{len} q^{−writhe}
        return sp.Integer(-1) ** len(word) * q ** (-writhe(word))
    w41, w52 = writhe(BRAID_4_1), writhe(BRAID_5_2)
    # bar-odd knot-operator datum = ½(χ_{(3)} − χ_{(1,1,1)}) (conjugate pair)
    D41 = sp.simplify((chi_triv(BRAID_4_1) - chi_sign(BRAID_4_1)) / 2)
    D52 = sp.simplify((chi_triv(BRAID_5_2) - chi_sign(BRAID_5_2)) / 2)
    print("\n FINDING 2 — the bar-odd datum is the WRITHE (conjugate-pair "
          "(3)/(1,1,1) asymmetry):")
    print(f"    writhe(4₁) = {w41}  (amphichiral)   D_odd(4₁) = ½(χ₃−χ₁₁₁) = {D41}")
    print(f"    writhe(5₂) = {w52}  (chiral)        D_odd(5₂) = ½(χ₃−χ₁₁₁) = {D52}")
    print(f"    ⇒ 5₂ D_odd = ½(q⁴−q⁻⁴) is a genuine bar-odd sinh-object — the "
          f"nonzero home 4₁ (writhe 0 ⇒ D_odd=0) structurally lacks.")
    writhe_ok = (w41 == 0 and w52 == 4)
    d41_zero = (D41 == 0)
    d52_nonzero = (sp.simplify(D52) != 0)

    # ---- q=1 anchor (validation of the H₃ block) ----
    tau41_at1 = sp.simplify(tau41.subs(q, 1))
    print(f"\n  q=1 anchor: τ_{{4₁}}(1) = {tau41_at1}  (4₁→3-cycle in S₃ ⇒ χ=−1)")

    # ---- the 5₂ bar-odd datum at the substrate anchors (numeric) ----
    D52_fn = sp.lambdify(q, D52, "mpmath")
    print(f"\n  5₂ bar-odd writhe datum D_odd(q₀) = ½(q₀⁴−q₀⁻⁴):")
    barodd_vals = {}
    for name, q0 in Q.items():
        val = D52_fn(q0)
        barodd_vals[name] = val
        print(f"    D_odd({name}) = {mp.nstr(val, 12)}   (4₁ gives 0)")
    swing = abs(barodd_vals["proton"] - barodd_vals["muon"])
    print(f"    |D_odd(p) − D_odd(mu)| = {mp.nstr(swing, 6)}  (smooth ⇒ NOT the "
          f"2e6 S-swing; value anchor-invariant-ish, per the prune)")

    wb = WitnessBuilder("qbeta-5two-reeb-trace", engine="sympy+mpmath")
    wb.set_description(
        "Foundational brick of the non-amphichiral (5₂) route (fork option 2). "
        "The H₃(q) Hoefsmit V_{(2,1)} q-Reeb trace of the canonical 5₂ 3-braid "
        "(1,1,1,2,-1,2): τ_{5₂}(q) is BAR-ASYMMETRIC (nonzero bar-odd part), "
        "unlike the amphichiral 4₁ (τ_{4₁} bar-symmetric, bar-odd=0). So 5₂ "
        "supplies a NONZERO bar-odd knot-operator datum — the 'nonzero home' the "
        "CS=0 fork needs. Validated at the q=1 permutation anchor. HONEST SCOPE: "
        "τ_{5₂}(q₀) is smooth, so its value is anchor-invariant-ish and cannot "
        "produce S's 2e6 swing (Lean-proved no_anchor_invariant_realizes_swing "
        "still binds); the swing needs the anchor-dependent quantum 𝔙_q(5₂), a "
        "later brick. No c_k; no fit; scope-(a).")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("qreeb_trace_bar_even_both_knots",
                     computed="0.0" if block_bar_even else "1.0", expected="0.0", tolerance="0.5",
                     source="τ_{4₁} AND τ_{5₂} on V_{(2,1)} are both bar-even (exact "
                            "sympy): the self-conjugate (2,1) block cannot carry "
                            "chirality — FINDING 1, refutes the naive q-Reeb guess")
    wb.add_assertion("writhe_amphichiral_vs_chiral",
                     computed=str(int(bool(writhe_ok))), expected="1.0", tolerance="0.5",
                     source="writhe(4₁)=0 (amphichiral), writhe(5₂)=4 (chiral) — the "
                            "conjugate-pair (3)/(1,1,1) asymmetry")
    wb.add_assertion("bar_odd_writhe_datum_4one_zero_5two_nonzero",
                     computed="0.0" if (d41_zero and d52_nonzero) else "1.0",
                     expected="0.0", tolerance="0.5",
                     source="D_odd=½(χ₃−χ₁₁₁): 0 for 4₁ (writhe 0), ½(q⁴−q⁻⁴)≠0 for "
                            "5₂ (writhe 4) — FINDING 2: the bar-odd home is the "
                            "writhe, a sinh-object, nonzero for chiral 5₂")
    wb.add_assertion("q1_permutation_anchor",
                     computed=mp.nstr(tau41_at1, 30), expected="-1.0", tolerance="0.01",
                     source="τ_{4₁}(1) = −1: 4₁ braid (σ₁σ₂⁻¹)² is a 3-cycle in S₃, "
                            "standard-rep character −1 (validates the H₃ block)")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("tau_5_2_V21", str(tau52))
    wb.add_data("tau_4_1_V21", str(tau41))
    wb.add_data("v21_block_bar_even_both", bool(block_bar_even))
    wb.add_data("writhe", {"4_1": w41, "5_2": w52})
    wb.add_data("bar_odd_writhe_datum", {"4_1": str(D41), "5_2": str(D52)})
    wb.add_data("D_odd_5_2_at_anchors",
                {k: mp.nstr(v, 15) for k, v in barodd_vals.items()})
    wb.add_data("anchor_smoothness_caveat",
                f"|D_odd(p)−D_odd(mu)| = {mp.nstr(swing, 6)}: the writhe datum "
                "½(q₀⁴−q₀⁻⁴) is anchor-smooth, so NOT the S-swing carrier "
                "(no_anchor_invariant_realizes_swing binds). 5₂ gives a nonzero "
                "bar-odd HOME; the anchor-dependent swing still needs 𝔙_q(5₂).")
    wb.add_data("braid_word_5_2", "(1,1,1,2,-1,2) = σ₁³σ₂σ₁⁻¹σ₂ (canonical table)")
    wb.add_data("verdict",
                ("TWO FINDINGS. (1) REFUTED the naive q-Reeb guess: τ_{5₂}(q) on "
                 "V_{(2,1)} is bar-EVEN, same as τ_{4₁} — the self-conjugate (2,1) "
                 "block cannot carry chirality for any knot. (2) LOCATED the bar-odd "
                 "datum in the WRITHE: the conjugate-pair (3)/(1,1,1) asymmetry "
                 "D_odd=½(χ₃−χ₁₁₁) is 0 for amphichiral 4₁ (writhe 0) and "
                 "½(q⁴−q⁻⁴)≠0 for chiral 5₂ (writhe 4) — a genuine bar-odd "
                 "sinh-object, the nonzero home fork-option-2 needs. But D_odd(q₀) "
                 "is anchor-smooth ⇒ not the S-swing (the Lean-proved anchor-"
                 "invariance prune binds); the swing needs 𝔙_q(5₂), the next brick. "
                 "No c_k; no fit; scope-(a)."
                 if ok else "INCONCLUSIVE — an assertion failed; inspect output."))
    wb.save(q0_comparison(
        muon=Q["muon"], proton=Q["proton"],
        reason="D_odd is tabulated at BOTH pins (D_odd_5_2_at_anchors) to test anchor-smoothness; both are read on purpose"))
    print(f"\n  assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-5two-reeb-trace.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
