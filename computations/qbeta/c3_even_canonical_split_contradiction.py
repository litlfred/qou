#!/usr/bin/env python3
"""
c3_even_canonical_split_contradiction.py — settle bean `qou-qb8f`.

QUESTION.  `SLeakZeroCrossing.lean:11` defines

    S_leak(q0) := c_3(q0) + Vol(4_1)

and reads it as "the bar-ODD residual of c_3 after removing the bar-EVEN
amphichiral -Vol(4_1) face".  That reading requires

    c_3^even = -Vol(4_1) ~ -2.0299                                       (H1)

Is (H1) DERIVED, or is it an assumed structural form?

METHOD.  Do not attempt the bar-split from anchor data — it is not accessible
(it needs c_3 at q ~ 0.901; both anchors sit at q ~ 1.10998).  Instead test (H1)
against the corpus's OTHER, independently-derived decomposition and check
whether the two can both hold.

THE CANONICAL SPLIT (docs/audits/2026-07-07-c3-even-solved-s-complex-volume-
rigidity.md §2, tier structural-exact):

    c_3^odd = kappa_(2,1)(q) * S,     kappa_(2,1)(q) = (q-1)^3 (q+1) / q^2

with `kappa_(2,1)` the DERIVED pure-q bar-odd carrier and `S = Q_beta/E_0` the
single archimedean scalar, quoted there as S_proton ~ 908.4, S_muon ~ 886.8
(S_p/S_mu ~ 1.024).

Those S values are stated INDEPENDENTLY of anything in the S_leak framing, so
they are a free cross-check: invert `c_3 = -kappa*S` at each anchor under the
hypothesis `c_3^even = 0` and see whether the audit's S values come back.

RESULT (assertions below).  They come back to 4.1e-5 / 1.1e-5 relative.  So the
corpus's canonical decomposition has c_3 essentially PURELY BAR-ODD — its
bar-even part is ~0, not -2.03.  (H1) is therefore not merely underived: it is
INCOMPATIBLE with the canonical split.

WHAT `S_leak` ACTUALLY IS.  Adding +2.0299 to a number in [-2.069, -2.020] does
not remove a bar-even face; it CANCELS ~98% of the bar-ODD part.  `S_leak` is a
near-total cancellation residual.  That is the mechanical origin of its
hypersensitivity: c_3's own anchor swing is 2.4%, while S_leak's is ~500% — an
amplification of ~200x, purely from the cancellation.

SCOPE.  (a) scope-limited, and deliberately so.  What is refuted is the
IDENTIFICATION (H1), not `Vol(4_1)` as an ingredient anywhere else, and not any
theorem in SLeakZeroCrossing.lean / SLeakMagnitude*.lean — those are stated for
a GENERIC function with the anchor signs (or a simple zero) as HYPOTHESES and
are unaffected.  What is refuted is the interpretive sentence that names S_leak
"c_3's bar-odd residual".

NO FIT.  Every number is either a corpus-committed anchor value or an exact
evaluation of the derived carrier kappa_(2,1).  Nothing is tuned; nothing is
wired to production.

-- Ref: [manuscript] docs/audits/2026-07-07-c3-even-solved-s-complex-volume-rigidity.md
-- Ref: [manuscript] docs/audits/2026-07-03-9fnm-c3even-exact-rational-measurement.md
-- Ref: [manuscript] AGENTS.md "Defined residual != derived decomposition (STRICT, 2026-08-08)"
"""

from mpmath import mp, mpf

mp.dps = 50

# ---------------------------------------------------------------- corpus data
# Substrate anchors.  Proton = the experimental/Physical-Observations pin
# (AGENTS.md owner directive 2026-08-07); muon = the ideal CAL-2 proxy pin.
Q_PROTON = mpf("1.1099785827513808")
Q_MUON = mpf("1.10997859555733471")

# c_3 at each anchor (ck-dk canonical registry; the same pair the S_leak
# framing and the 2026-07-07 audit both quote).
C3_PROTON = mpf("-2.06934258")
C3_MUON = mpf("-2.02020024")

# Vol(4_1) = 2*Lobachevsky(pi/3), the figure-eight hyperbolic volume.
VOL_41 = mpf("2.029883212819307")

# S values quoted INDEPENDENTLY by the 2026-07-07 audit §2.  These are the
# cross-check targets — they are not inputs to the reconstruction below.
S_PROTON_AUDIT = mpf("908.4")
S_MUON_AUDIT = mpf("886.8")


def kappa_21(q):
    """The derived pure-q bar-odd carrier kappa_(2,1)(q) = (q-1)^3 (q+1)/q^2.

    Bar-odd: kappa(1/q) = -kappa(q), verified symbolically in `check_kappa_odd`.
    """
    return (q - 1) ** 3 * (q + 1) / q**2


def check_kappa_bar_odd():
    """kappa_(2,1) is genuinely bar-ODD: kappa(1/q) = -kappa(q)."""
    for q in (mpf("1.3"), mpf("2"), Q_PROTON, mpf("1.05")):
        lhs = kappa_21(1 / q)
        rhs = -kappa_21(q)
        assert abs(lhs - rhs) < mpf("1e-40"), (q, lhs, rhs)
    return True


def reconstruct_S(q, c3):
    """Invert c_3 = -kappa_(2,1)(q) * S under the hypothesis c_3^even = 0."""
    return -c3 / kappa_21(q)


def main():
    print("=" * 74)
    print("c_3^even: is it -Vol(4_1)?  Testing (H1) against the canonical split")
    print("=" * 74)

    assert check_kappa_bar_odd()
    print("\n[0] carrier check: kappa_(2,1)(1/q) = -kappa_(2,1)(q)  -> bar-ODD  OK")

    print("\n[1] The canonical split (2026-07-07 audit §2), tested at both anchors.")
    print("    Hypothesis: c_3 is purely bar-ODD, c_3 = -kappa_(2,1)(q)*S.")
    print("    Invert for S and compare to the audit's INDEPENDENT S values.\n")

    rows = []
    for name, q, c3, s_audit in (
        ("proton", Q_PROTON, C3_PROTON, S_PROTON_AUDIT),
        ("muon", Q_MUON, C3_MUON, S_MUON_AUDIT),
    ):
        k = kappa_21(q)
        s = reconstruct_S(q, c3)
        rel = abs(s - s_audit) / s_audit
        rows.append((name, q, c3, k, s, s_audit, rel))
        print(
            f"    {name:7s} kappa = {mp.nstr(k, 10):>14s}   "
            f"S_recon = {mp.nstr(s, 10):>12s}   audit = {s_audit}   "
            f"rel dev = {mp.nstr(rel, 3)}"
        )

    for _, _, _, _, s, s_audit, rel in rows:
        assert rel < mpf("1e-4"), f"S reconstruction missed the audit value: {s} vs {s_audit}"

    ratio = rows[0][4] / rows[1][4]
    print(f"\n    S_p/S_mu = {mp.nstr(ratio, 10)}   (audit quotes ~1.024)")
    assert abs(ratio - mpf("1.024")) < mpf("5e-4"), ratio

    print(
        "\n    => Assuming c_3^even = 0 REPRODUCES both independently-quoted S\n"
        "       values to ~1e-5.  The canonical decomposition therefore has\n"
        "       c_3 essentially PURELY BAR-ODD."
    )

    print("\n[2] The contradiction with (H1).\n")
    print(f"    (H1) claims        c_3^even = -Vol(4_1) = {mp.nstr(-VOL_41, 10)}")
    print("    canonical split    c_3^even ~ 0")
    print(
        f"    separation         {mp.nstr(VOL_41, 10)}  "
        f"-- ~{mp.nstr(VOL_41 / abs(C3_PROTON) * 100, 4)}% of |c_3| itself"
    )
    assert abs(VOL_41) > mpf("2"), "sanity"

    print("\n[3] What S_leak actually is: a near-total cancellation.\n")
    for name, _, c3, _, _, _, _ in rows:
        leak = c3 + VOL_41
        cancel = (1 - abs(leak) / abs(c3)) * 100
        print(
            f"    {name:7s} c_3 = {mp.nstr(c3, 10):>13s}  + Vol(4_1)  ->  "
            f"S_leak = {mp.nstr(leak, 8):>12s}   ({mp.nstr(cancel, 5)}% cancelled)"
        )

    swing_c3 = abs(C3_PROTON - C3_MUON) / abs(C3_MUON) * 100
    leak_mu = C3_MUON + VOL_41
    leak_p = C3_PROTON + VOL_41
    swing_leak = abs(leak_p - leak_mu) / abs(leak_mu) * 100
    amp = swing_leak / swing_c3

    print(f"\n    anchor swing of c_3    : {mp.nstr(swing_c3, 5)}%")
    print(f"    anchor swing of S_leak : {mp.nstr(swing_leak, 5)}%")
    print(f"    amplification          : {mp.nstr(amp, 5)}x  <- cancellation artifact")
    assert amp > 100, amp

    print(
        "\n    The 'hypersensitivity of S_leak' is therefore ~200x cancellation\n"
        "    amplification on top of c_3's own (real, 2.4%) anchor swing."
    )

    print("\n[4] Why the anchors cannot settle the bar-split directly.\n")
    print(
        "    c_3^even(q) = (c_3(q) + c_3(1/q))/2 needs c_3 at q ~ 0.901.\n"
        "    Both anchors sit at q ~ 1.10998, so NO anchor data determines the\n"
        "    split; it must come from an assumed structural form.  That is why\n"
        "    this probe tests (H1) for CONSISTENCY against a derived split\n"
        "    rather than trying to measure the split."
    )
    print(f"    bar-partner of q_proton would be 1/q = {mp.nstr(1 / Q_PROTON, 12)}")

    print("\n" + "=" * 74)
    print("VERDICT (scope-(a)): (H1) c_3^even = -Vol(4_1) is NOT derived, and is")
    print("INCOMPATIBLE with the canonical kappa_(2,1)*S split, which reproduces")
    print("two independently-quoted S values to ~1e-5 with c_3^even ~ 0.")
    print("Unaffected: every theorem in SLeakZeroCrossing/SLeakMagnitude*.lean")
    print("(generic, hypothesis-carrying).  Affected: the interpretive sentence")
    print("naming S_leak 'c_3's bar-odd residual'.")
    print("=" * 74)
    print("\n7/7 assertions passed.")


if __name__ == "__main__":
    main()
