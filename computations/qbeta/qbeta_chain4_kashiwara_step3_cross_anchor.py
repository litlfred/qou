"""qbeta_chain4_kashiwara_step3_cross_anchor — Step 3 of Chain 4.

Cross-anchor validation of Step 2's `cocharge_(1,1,1,1) = 6` NEAR-1PCT
candidate at q_proton (0.991805 ratio).  Per AGENTS.md anti-pattern
guards + the c_3 4-session flip-flop history, single-anchor near-
matches must cross-anchor at q_muon BEFORE any structural claim.

THE KEY OBSERVATION:

  cocharge_(1,1,1,1) = 6 is a COMBINATORIAL invariant — anchor-
  INDEPENDENT.  But the TARGET prefactor A / ℏ_q^15 is anchor-
  DEPENDENT (A is anchor-independent per PR #1727 simple-pole, but
  ℏ_q^15 differs between anchors).

  - If A / ℏ_q^15 at q_muon also ≈ 6, the candidate cocharge-of-(1,1,1,1)
    is a true structural hit (modulo categorical rationale).
  - If A / ℏ_q^15 at q_muon ≠ 6, the candidate is a single-anchor
    coincidence (the 4-session flip-flop pattern).

This script computes ℏ_q at BOTH proton-pin and muon-pin anchors,
divides A by each ℏ_q^15, and compares the resulting prefactors.

ANCHORS (50-dps):
  q_proton ≈ 1.10997858275138080759166909561
  q_muon   ≈ 1.10997859555418057528159407961
  (Cross-anchor difference: 1.28e-8 in q itself)

Canonical: ℏ_q = (q - 1) / q
   per computations/qbeta/qbeta_residue_categorical_id_probe.py
   line 48: `hbar_q = (q - 1) / q`

EXPECTED OUTCOME if cocharge-of-(1,1,1,1) is a true hit:
  Both prefactors within near-match tolerance of 6, and both ratios
  close to 1.

EXPECTED OUTCOME if single-anchor coincidence:
  Wildly different prefactors at the two anchors; cocharge=6 only
  matches one.

OUTPUT: qbeta-chain4-kashiwara-step3-cross-anchor.witness.json
"""

from __future__ import annotations

from pathlib import Path
import mpmath as mp

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

# Residue A (anchor-independent per PR #1727 simple-pole verdict)
RESIDUE_A = mp.mpf("1.804e-15")

# Anchors (50-dps each)
Q_PROTON = mp.mpf("1.10997858275138080759166909561")
Q_MUON = mp.mpf("1.10997859555418057528159407961")

# Step 2 candidate: cocharge of the column tableau (1,1,1,1) = 0+1+2+3
COCHARGE_1111 = mp.mpf(6)


def hbar_q(q: mp.mpf) -> mp.mpf:
    """Canonical ℏ_q = (q - 1) / q  (per qbeta_residue_categorical_id_probe)."""
    return (q - 1) / q


def main() -> None:
    import sys
    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here.parent))
    import _path_bridge as _pb  # noqa: F401

    sys.path.insert(0, str(Path(__file__).resolve().parents[3]
                           / "tools" / "qou-substrate" / "python"))
    from qou_substrate.witness import WitnessBuilder

    print("=" * 78)
    print("Q_β Chain 4 Step 3 — CROSS-ANCHOR validation of cocharge=6")
    print("=" * 78)
    print()

    hb_p = hbar_q(Q_PROTON)
    hb_m = hbar_q(Q_MUON)

    print(f"ℏ_q(q_proton) = {mp.nstr(hb_p, 18)}")
    print(f"ℏ_q(q_muon)   = {mp.nstr(hb_m, 18)}")
    print(f"Δ_relative    = {mp.nstr(abs(hb_p - hb_m) / hb_p, 6)}")
    print()

    hb_p_15 = hb_p ** 15
    hb_m_15 = hb_m ** 15
    print(f"ℏ_q(q_proton)^15 = {mp.nstr(hb_p_15, 6)}")
    print(f"ℏ_q(q_muon)^15   = {mp.nstr(hb_m_15, 6)}")
    print(f"Δ^15_relative    = {mp.nstr(abs(hb_p_15 - hb_m_15) / hb_p_15, 6)}")
    print()

    target_p = RESIDUE_A / hb_p_15
    target_m = RESIDUE_A / hb_m_15

    # The cross-anchor spread, and the same spread predicted analytically.
    # A is anchor-INDEPENDENT, so the whole spread has to come from ℏ_q^15:
    # d(A/ℏ^15)/(A/ℏ^15) = −15·dℏ/ℏ, and dℏ/ℏ = dq/(q(q−1)) for ℏ=(q−1)/q.
    # Neither expression looks at the other.
    spread_direct = abs(target_p - target_m) / target_p
    spread_analytic = 15 * abs(Q_PROTON - Q_MUON) / (Q_PROTON * (Q_PROTON - 1))

    print("TARGETS:")
    print(f"  A / ℏ_q(q_proton)^15 = {mp.nstr(target_p, 8)}")
    print(f"  A / ℏ_q(q_muon)^15   = {mp.nstr(target_m, 8)}")
    print(f"  Δ relative          = {mp.nstr(spread_direct, 6)}")
    print(f"  15·Δq/(q(q−1))      = {mp.nstr(spread_analytic, 6)}  "
          f"(first-order prediction; gap "
          f"{mp.nstr(abs(spread_direct - spread_analytic), 4)} is the "
          f"second-order term)")
    print()

    ratio_p = COCHARGE_1111 / target_p
    ratio_m = COCHARGE_1111 / target_m

    print(f"Candidate: cocharge_(1,1,1,1) = {COCHARGE_1111} (anchor-INDEPENDENT)")
    print()
    print(f"  Ratio at q_proton: {mp.nstr(ratio_p, 8)}")
    print(f"  Ratio at q_muon:   {mp.nstr(ratio_m, 8)}")
    print()

    err_p = abs(ratio_p - 1)
    err_m = abs(ratio_m - 1)

    def tier(rel_err: mp.mpf) -> str:
        if rel_err < mp.mpf("1e-9"): return "PROVED-1PPB"
        if rel_err < mp.mpf("1e-6"): return "NEAR-1PPM"
        if rel_err < mp.mpf("1e-3"): return "NEAR-1PPT"
        if rel_err < mp.mpf("0.01"): return "NEAR-1PCT"
        if rel_err < mp.mpf("0.1"): return "NEAR-FUZZY"
        return "MISS"

    tier_p = tier(err_p)
    tier_m = tier(err_m)

    print(f"  Tier at q_proton: {tier_p} (rel_err {mp.nstr(err_p, 4)})")
    print(f"  Tier at q_muon:   {tier_m} (rel_err {mp.nstr(err_m, 4)})")
    print()

    # CROSS-ANCHOR DISCRIMINATOR
    if tier_p in ("PROVED-1PPB", "NEAR-1PPM", "NEAR-1PPT") and \
       tier_m in ("PROVED-1PPB", "NEAR-1PPM", "NEAR-1PPT"):
        verdict = "STRUCTURAL HIT — both anchors pass tight tier"
    elif tier_p == "NEAR-1PCT" and tier_m == "NEAR-1PCT":
        verdict = "BOTH-ANCHOR NEAR-MATCH — survives discriminator"
    elif tier_p in ("NEAR-1PCT", "NEAR-1PPT") and tier_m == "MISS":
        verdict = "FLIP-FLOP — proton matches, muon misses"
    elif tier_m in ("NEAR-1PCT", "NEAR-1PPT") and tier_p == "MISS":
        verdict = "FLIP-FLOP — muon matches, proton misses"
    else:
        verdict = "WIDE MISS — candidate refuted at cross-anchor"

    print(f"VERDICT: {verdict}")
    print()

    # Implication
    if "STRUCTURAL HIT" in verdict or "BOTH-ANCHOR NEAR-MATCH" in verdict:
        print("→ The cocharge_(1,1,1,1) = 6 candidate SURVIVES cross-anchor.")
        print("  Step 4: identify categorical rationale (why this particular")
        print("  cocharge value?), and document tier in the audit doc.")
        print("  Do NOT propose closure until rationale is verified.")
    else:
        print("→ The cocharge_(1,1,1,1) = 6 candidate is REFUTED.")
        print("  HONEST CORRECTION: Step 2 used a NON-CANONICAL ℏ_q value")
        print("  (hard-coded 0.0922502; canonical ℏ_q = (q-1)/q ≈ 0.09908)")
        # This line used to read "a wrong target ~6.47 instead of correct
        # ~2.07". The 2.07 is right; the 6.47 was never computed — A/ℏ^15 at
        # ℏ=0.0922502 is 6.0496. Printed live now so it cannot drift again;
        # the discrepancy is recorded as a witness caveat.
        _target_step2 = RESIDUE_A / mp.mpf("0.0922502") ** 15
        print(f"  which gave a wrong target ~{mp.nstr(_target_step2, 4)} "
              f"instead of correct ~{mp.nstr(target_p, 4)}.")
        print("  The 'NEAR-1PCT' at q_proton was a Step-2 BUG ARTIFACT,")
        print("  not a flip-flop.")
        print()
        print("RE-CHECK against CORRECT target (~2.07) using Step 2 values:")
        print("-" * 78)
        # Candidates from Step 2 evaluated at CORRECT target
        # (anchor-independent invariants ratio against target_proton)
        step2_recheck = {
            "f^(3,1)": mp.mpf(3),
            "f^(2,1,1)": mp.mpf(3),
            "q-dim_(2,2)~": mp.mpf("2.04371"),  # from Step 2 output
            "q-dim_(3,1)~": mp.mpf("3.04371"),
            "cocharge_(1,1,1,1)": mp.mpf(6),
            "Σ f^λ (n=4)": mp.mpf(10),
            "cocharge_(2,2)": mp.mpf(2),
            "f^(2,2)": mp.mpf(2),
            "f^(4) = 1": mp.mpf(1),
        }
        for name, val in step2_recheck.items():
            ratio = val / target_p
            t = tier(abs(ratio - 1))
            mark = " ← NEAR" if t in ("NEAR-1PPM", "NEAR-1PPT", "NEAR-1PCT") else ""
            print(f"  {name:30s} = {mp.nstr(val, 5):8s} → "
                  f"ratio {mp.nstr(ratio, 5)} [{t}]{mark}")
        print()

    print()

    # Emit witness
    wb = WitnessBuilder(
        name="qbeta-chain4-kashiwara-step3-cross-anchor",
        engine="mpmath",
        output_dir=here,
    )
    wb.set_description(
        f"Step 3 of PR #1772 Chain 4 — cross-anchor validation of "
        f"Step 2's NEAR-1PCT candidate cocharge_(1,1,1,1) = 6 at "
        f"q_proton. The candidate is anchor-INDEPENDENT (combinatorial), "
        f"but the target A / ℏ_q^15 differs between q_proton and q_muon "
        f"by {mp.nstr(abs(target_p - target_m) / target_p, 4)} relative. "
        f"Verdict: {verdict}."
    )
    # ── Was `step3_cross_anchor_verdict_recorded`, computed=True/expected=True ──
    # Its source line said "diagnostic completed". It could not fail, and it
    # made allPassed look like a two-assertion verdict when only one
    # assertion here was ever a claim.
    #
    # The discriminator's premise is that the candidate is anchor-INDEPENDENT
    # while the target is anchor-DEPENDENT *through ℏ_q^15 alone* (A is
    # anchor-independent per PR #1727). That premise is what makes a
    # flip-flop meaningful, and it is testable:
    #   Route A: |target_p − target_m| / target_p, evaluated by building both
    #            targets from their own 50-dps anchors and dividing.
    #   Route B: 15 · Δq / (q(q−1)) — first-order propagation of the anchor
    #            gap through ℏ = (q−1)/q and the 15th power. No target, no
    #            residue A, no division of one target by the other.
    # They agree to 1.34e-12, which is the second-order term 120·(Δℏ/ℏ)² =
    # 1.32e-12. A wrong exponent (14 or 16), a non-canonical ℏ_q, or a
    # mistyped anchor digit moves Route A off Route B by orders of magnitude.
    wb.add_assertion(
        name="cross_anchor_spread_matches_15th_power_propagation",
        computed=mp.nstr(spread_direct, 20),
        expected=mp.nstr(spread_analytic, 20),
        tolerance="5e-12",
        unit="relative spread of A/ℏ_q^15 between the proton and muon anchors",
        source=("Route A: |target_p − target_m|/target_p from the two 50-dps "
                "anchors. Route B: 15·Δq/(q(q−1)), the first-order propagation "
                "of Δq through ℏ=(q−1)/q and the 15th power. Tolerance 5e-12 "
                "sits just above the second-order term 120·(Δℏ/ℏ)² = 1.32e-12 "
                "and ~3e6 below the quantity itself."),
    )
    wb.add_assertion(
        name="step3_proton_anchor_tier",
        computed=tier_p in ("NEAR-1PCT", "NEAR-1PPT", "NEAR-1PPM", "PROVED-1PPB"),
        expected=True,
        source=f"Proton-anchor tier: {tier_p} (Step 2 found NEAR-1PCT here)",
    )
    wb.add_data("residue_A", str(RESIDUE_A))
    wb.add_data("q_proton", str(Q_PROTON))
    wb.add_data("q_muon", str(Q_MUON))
    wb.add_data("hbar_q_proton", mp.nstr(hb_p, 16))
    wb.add_data("hbar_q_muon", mp.nstr(hb_m, 16))
    wb.add_data("target_proton", mp.nstr(target_p, 16))
    wb.add_data("target_muon", mp.nstr(target_m, 16))
    wb.add_data("candidate_value", str(COCHARGE_1111))
    wb.add_data("ratio_proton", mp.nstr(ratio_p, 12))
    wb.add_data("ratio_muon", mp.nstr(ratio_m, 12))
    wb.add_data("tier_proton", tier_p)
    wb.add_data("tier_muon", tier_m)
    wb.add_data("verdict", verdict)
    wb.add_data("cross_anchor_spread_direct", mp.nstr(spread_direct, 20))
    wb.add_data("cross_anchor_spread_analytic", mp.nstr(spread_analytic, 20))
    wb.add_data("step2_noncanonical_hbar_target",
                mp.nstr(RESIDUE_A / mp.mpf("0.0922502") ** 15, 12))
    wb.add_caveat(
        "step3_proton_anchor_tier is RED and belongs red: cocharge_(1,1,1,1)=6 "
        "against the canonical target 2.0717 gives ratio 2.896, tier MISS, "
        "while the assertion encodes Step 2's NEAR-1PCT claim. The script's own "
        "else-branch says the same thing in prose — Step 2's NEAR-1PCT was a "
        "bug artifact from a non-canonical ℏ_q. Left failing rather than "
        "rewritten green; it is the refutation, recorded."
    )
    wb.add_caveat(
        "The else-branch used to print 'a wrong target ~6.47'. A/ℏ^15 at "
        "Step 2's hard-coded ℏ=0.0922502 is 6.0496, not 6.47 — the 6.47 was "
        "never computed by anything. Now printed live from RESIDUE_A so it "
        "cannot drift again; the ~2.07 in the same sentence was correct."
    )
    out_path = wb.save()
    print(f"  Witness: {out_path.name}")


if __name__ == "__main__":
    main()
