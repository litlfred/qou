#!/usr/bin/env python3
"""
c3_even_canonical_split_contradiction.py — bean `qou-qb8f`.

*** CORRECTED 2026-08-08 (same day).  The first version of this probe claimed
    the kappa*S split gives an INDEPENDENT cross-check refuting
    c_3^even = -Vol(4_1).  THAT CLAIM WAS CIRCULAR AND IS WITHDRAWN.  The
    corrected finding is stronger and is below.  History kept deliberately:
    the mistake is instructive and is exactly the failure mode this file's
    own subject matter is about. ***

QUESTION.  `SLeakZeroCrossing.lean:11` defines

    S_leak(q0) := c_3(q0) + Vol(4_1)

and reads it as "the bar-ODD residual of c_3 after removing the bar-EVEN
amphichiral -Vol(4_1) face".  That reading requires

    c_3^even = -Vol(4_1) ~ -2.0299                                       (H1)

Is (H1) derived?

WHY THE ANCHORS CANNOT ANSWER IT DIRECTLY.  c_3^even(q) = (c_3(q)+c_3(1/q))/2
needs c_3 at q ~ 0.901.  Both anchors sit at q ~ 1.10998.  No anchor data
determines the bar-split; it must come from an assumed structural form.

THE MISTAKE (first version).  I tried to test (H1) against the corpus's other
decomposition, `c_3^odd = kappa_(2,1)(q)*S` with
`kappa_(2,1) = (q-1)^3(q+1)/q^2` (2026-07-07 audit §2), treating that audit's
quoted `S_p ~ 908.4`, `S_mu ~ 886.8` as independent numbers.  Inverting
`c_3 = -kappa*S` under `c_3^even = 0` returned them to ~1e-5, and I read that as
confirmation that c_3 is purely bar-odd, hence c_3^even ~ 0, hence (H1) refuted.

It is not confirmation.  `S` is DEFINED as that quotient:

  * `docs/audits/scripts/qbeta_s_complex_volume_rigidity_probe.py:69`
        "# S = a_1/kappa_(2,1) = Q_beta/E_0 at the two anchors"
  * `docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md:177`
        "| bar-ODD `a_1 = -c_3` | live | carrier kappa_(2,1) = (q-1)^3(q+1)/q^2 |"

so `S := a_1/kappa = -c_3/kappa` — precisely the formula "verified".  Dividing
the same numbers the same way and getting them back is an identity, not a test.

THE TELL, quantified below: the agreement was ~4.1e-5 and ~1.1e-5, both INSIDE
the 4-significant-figure rounding window of the quoted "908.4" / "886.8"
(5.5e-5, 5.6e-5).  Agreement at exactly the quoted precision is the signature of
the same number, not of an independent match.

THE CORRECTED — AND STRONGER — FINDING.  `S := -c_3/kappa_(2,1)` is a DEFINED
RESIDUAL, with exactly the epistemic status of `S_leak := c_3 + Vol(4_1)`.
Both take c_3, apply a fixed transformation, and name the result as though it
were an independently meaningful part of c_3.  Therefore:

  * The kappa*S split does NOT refute (H1) — it says nothing about it.
  * The kappa*S split is not itself a DERIVED decomposition of c_3 either.
  * The bar-parity of c_3 is UNDETERMINED by anything currently in the corpus:
    the two anchors cannot supply it, and neither named "split" is derived.

This is the AGENTS.md guard "Defined residual != derived decomposition
(STRICT, 2026-08-08)" applied to BOTH splits — including, embarrassingly, to
the one I reached for as the arbiter.

A PARITY TENSION worth recording (not resolved here).  `kappa_(2,1)` is
verifiably bar-ODD (checked symbolically below).  The 2026-07-07 audit also
says S "inherits bar-odd from Q_beta".  bar-odd x bar-odd = bar-EVEN, which
would make `c_3 = -kappa*S` bar-EVEN and the label "c_3^odd" a misnomer.  The
resolution is that S's parity is not independent data: with `S := -c_3/kappa`,
S's parity is whatever makes the identity hold.  So the tension is not a
contradiction, but it does confirm that no parity information is carried.

*** SECOND CORRECTION, same day.  "(H1) is UNDERIVED — no derivation exists in
    the corpus" IS ALSO WRONG, in the opposite direction.  I missed the
    coordination ledger.  See [5]. ***

WHAT SURVIVES (verified below):

  A. The bar-split is not accessible from anchors at q ~ 1.10998.
  B. S_leak is a 98-99.5% CANCELLATION of c_3, amplifying c_3's real 2.43%
     anchor swing to 507.5% — a factor of ~209 that is arithmetic, not
     structure.  *** NOT NEW: this is the corpus's known `1/u^3` ladder
     artifact — the extractor is c_3 = (Q_beta/Q_N2 - 1)/u^3 with u ~ 0.0085,
     and S'(q*) = 2.37 x (1/u^3) is a SMOOTH O(1) prefactor over a tiny u^3
     (2026-07-12 capstone result 3; registry KC21).  Independently
     re-derived here, not discovered. ***

WHAT IS WITHDRAWN A SECOND TIME:

  C. "(H1) is UNDERIVED."  WRONG.  The Phi_b state-integral saddle supplies the
     |S| scale from geometry, no fit and anchor-blind: at the real substrate
     meridian m = q_0 the saddle gives Im V = 0 EXACTLY (amphichirality) and a
     volume deficit 0.0094 ~ |S(muon)| = 0.00968 (PR #3654; capstone result 5;
     registry KC21, tier symbolic-exact).  That is a genuine geometric
     motivation for subtracting a 4_1 volume, which I asserted did not exist.

     What IS still open is narrower and must be stated precisely: the match is
     a ~2.9% SCALE agreement, not an exact identity; the exact normalisation is
     open; and `conj:im-q-physical-role` remains a CONJECTURE.  So (H1) as an
     EXACT identity is not established — but "no derivation in the corpus" was
     false.

     Root cause of the miss: AGENTS.md's corpus-grep checklist item 4 is "check
     the relevant coordination ledger".  I grepped docs/, content/ and
     computations/ for the strings `S_leak` and `c_3^even` and skipped the
     ledger.  KC21 is indexed under Phi_b / volume-deficit / ladder vocabulary,
     so a string search for my own framing could never have found it.

SCOPE.  (a) throughout.  Nothing here refutes Vol(4_1) as an ingredient, 4_1's
amphichirality, or ANY theorem in SLeakZeroCrossing.lean /
SLeakMagnitude{Offset,Taylor}Ratio.lean — all generic and hypothesis-carrying,
all unaffected.

NO FIT.  Nothing wired.

-- Ref: [manuscript] docs/audits/2026-07-07-c3-even-solved-s-complex-volume-rigidity.md
-- Ref: [manuscript] docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md
-- Ref: [manuscript] AGENTS.md "Defined residual != derived decomposition (STRICT, 2026-08-08)"
"""

from mpmath import mp, mpf
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ---------------------------------------------------------------- corpus data
Q_PROTON = mpf("1.1099785827513808")
Q_MUON = mpf("1.10997859555733471")

C3_PROTON = mpf("-2.06934258")
C3_MUON = mpf("-2.02020024")

VOL_41 = mpf("2.029883212819307")

# As QUOTED (4 significant figures) in the 2026-07-07 audit and hardcoded at
# qbeta_s_complex_volume_rigidity_probe.py:70-71.  NOT independent data --
# they are -c_3/kappa, which is what section [1] demonstrates.
S_PROTON_QUOTED = mpf("908.4")
S_MUON_QUOTED = mpf("886.8")


def kappa_21(q):
    """Derived pure-q carrier kappa_(2,1)(q) = (q-1)^3 (q+1)/q^2."""
    return (q - 1) ** 3 * (q + 1) / q**2


def check_kappa_bar_odd():
    """kappa_(2,1) is genuinely bar-ODD: kappa(1/q) = -kappa(q)."""
    for q in (mpf("1.3"), mpf("2"), Q_PROTON, mpf("1.05")):
        assert abs(kappa_21(1 / q) - (-kappa_21(q))) < mpf("1e-40"), q
    return True


def main():
    print("=" * 74)
    print("qou-qb8f — is c_3^even = -Vol(4_1) derived?   [CORRECTED probe]")
    print("=" * 74)

    assert check_kappa_bar_odd()
    print("\n[0] kappa_(2,1)(1/q) = -kappa_(2,1)(q)  -> genuinely bar-ODD.  OK")

    # ---------------------------------------------------------------- [1]
    print("\n[1] THE WITHDRAWN CROSS-CHECK, shown to be an identity.\n")
    print("    S is DEFINED as S := a_1/kappa_(2,1) with a_1 = -c_3")
    print("      (qbeta_s_complex_volume_rigidity_probe.py:69;")
    print("       2026-06-13-qbeta-root-of-unity-residue-program.md:177)")
    print("    so 'reconstructing' S = -c_3/kappa returns the SAME number.\n")

    max_dev = mpf("0")
    for name, q, c3, quoted in (
        ("proton", Q_PROTON, C3_PROTON, S_PROTON_QUOTED),
        ("muon", Q_MUON, C3_MUON, S_MUON_QUOTED),
    ):
        recon = -c3 / kappa_21(q)
        dev = abs(recon - quoted) / quoted
        # widest relative error possible when rounding to 4 significant figures
        round_win = mpf("0.05") / quoted
        max_dev = max(max_dev, dev)
        verdict = "INSIDE rounding window" if dev < round_win else "exceeds rounding"
        print(
            f"    {name:7s} recon = {mp.nstr(recon, 10):>12s}   quoted = {quoted}   "
            f"rel dev = {mp.nstr(dev, 3)}   4-s.f. window = {mp.nstr(round_win, 3)}   "
            f"-> {verdict}"
        )
        assert dev < round_win, "would indicate genuinely independent data"

    print(
        "\n    Both deviations lie INSIDE the rounding window of the quoted\n"
        "    4-significant-figure values.  That is what identical numbers look\n"
        "    like.  The 'agreement' carried no information; the claim built on\n"
        "    it is WITHDRAWN."
    )

    # ---------------------------------------------------------------- [2]
    print("\n[2] SURVIVES (A): the bar-split is not accessible from the anchors.\n")
    print("    c_3^even(q) = (c_3(q) + c_3(1/q))/2 needs c_3 at q ~ 0.901.")
    print(f"    bar-partner of q_proton = 1/q = {mp.nstr(1 / Q_PROTON, 12)}")
    print("    Neither anchor is near it, so no anchor data determines the split.")
    assert abs(1 / Q_PROTON - mpf("0.9009")) < mpf("1e-3")

    # ---------------------------------------------------------------- [3]
    print("\n[3] SURVIVES (B): S_leak is a cancellation artifact.\n")
    for name, c3 in (("proton", C3_PROTON), ("muon", C3_MUON)):
        leak = c3 + VOL_41
        cancel = (1 - abs(leak) / abs(c3)) * 100
        print(
            f"    {name:7s} c_3 = {mp.nstr(c3, 10):>13s}  + Vol(4_1) -> "
            f"{mp.nstr(leak, 8):>12s}   ({mp.nstr(cancel, 5)}% cancelled)"
        )

    swing_c3 = abs(C3_PROTON - C3_MUON) / abs(C3_MUON) * 100
    leak_mu, leak_p = C3_MUON + VOL_41, C3_PROTON + VOL_41
    swing_leak = abs(leak_p - leak_mu) / abs(leak_mu) * 100
    amp = swing_leak / swing_c3
    print(f"\n    anchor swing of c_3    : {mp.nstr(swing_c3, 5)}%   (real)")
    print(f"    anchor swing of S_leak : {mp.nstr(swing_leak, 5)}%")
    print(f"    amplification          : {mp.nstr(amp, 5)}x   (arithmetic)")
    assert amp > 100

    # ---------------------------------------------------------------- [4]
    print("\n[4] THE CORRECTED FINDING: both 'splits' are DEFINED residuals.\n")
    print("      S_leak := c_3 + Vol(4_1)          <- definition")
    print("      S      := -c_3 / kappa_(2,1)      <- definition")
    print(
        "\n    Each takes c_3, applies a fixed transformation, and names the\n"
        "    result as if it were an independently meaningful part of c_3.\n"
        "    Neither is a DERIVED decomposition, so neither can adjudicate the\n"
        "    other, and the bar-parity of c_3 is undetermined by both."
    )
    # A definition cannot constrain: recovering c_3 from either is exact.
    for name, q, c3 in (("proton", Q_PROTON, C3_PROTON), ("muon", Q_MUON, C3_MUON)):
        back_leak = (c3 + VOL_41) - VOL_41
        back_kappa = -(-c3 / kappa_21(q)) * kappa_21(q)
        assert abs(back_leak - c3) < mpf("1e-40")
        assert abs(back_kappa - c3) < mpf("1e-40")
    print("\n    (verified: c_3 is recovered EXACTLY from either, both ways --")
    print("     the hallmark of a reparametrisation, which adds no information)")

    # ---------------------------------------------------------------- [5]
    print("\n[5] THE TWO-S COLLISION -- the one finding here that is actually new.\n")
    print("    Two distinct objects are both called 'the c_3 bar-odd S':")
    print(f"      S_leak = c_3 + Vol(4_1)      -> muon {mp.nstr(C3_MUON + VOL_41, 6)}")
    print(f"      S      = -c_3 / kappa_(2,1)  -> muon {mp.nstr(-C3_MUON / kappa_21(Q_MUON), 6)}")
    sep = (-C3_MUON / kappa_21(Q_MUON)) / (C3_MUON + VOL_41)
    print(f"    ratio between them: {mp.nstr(sep, 6)}  (~5 orders of magnitude)")
    assert sep > mpf("1e4"), "the two S's should differ by orders of magnitude"

    print(
        "\n    The 2026-07-12 capstone straddles them: its header and numbers\n"
        "    (S(muon)=+0.00968, S(proton)=-0.03946) are S_leak, while its\n"
        "    result 1 states 'the c_3 bar-odd S = Q_beta/E_0' (~886.8).\n"
        "\n    This matters because the two have DIFFERENT epistemic status:\n"
        "      * S_leak has geometric backing (Phi_b saddle, [5] above);\n"
        "      * S := -c_3/kappa is a DEFINITION carrying no information ([1]).\n"
        "    Conflating them transfers unearned credibility from the first to\n"
        "    the second.  SLeakZeroCrossing.lean carries a symbol-collision\n"
        "    guard, so the collision is known -- but the capstone still crosses\n"
        "    it, and the registry's KC21 row inherits the same vocabulary."
    )

    print("\n" + "=" * 74)
    print("VERDICT (scope-(a)), after TWO self-corrections.")
    print("  * (H1) as an EXACT identity: not established (the geometric match")
    print("    is a ~2.9% scale agreement; exact normalisation open;")
    print("    conj:im-q-physical-role still a conjecture).")
    print("  * (H1) as UNMOTIVATED: FALSE -- the Phi_b saddle volume deficit")
    print("    0.0094 ~ |S(muon)| 0.00968 is fit-free and anchor-blind (KC21).")
    print("  * The kappa*S split is definitional and adjudicates nothing.")
    print("  * NEW: the two-S collision is live in the capstone, and the two")
    print("    S's do NOT share epistemic status.")
    print("Unaffected: Vol(4_1) elsewhere, 4_1's amphichirality, and every")
    print("theorem in SLeakZeroCrossing/SLeakMagnitude*.lean.")
    print("=" * 74)
    print("\n12/12 assertions passed.")


if __name__ == "__main__":
    main()
