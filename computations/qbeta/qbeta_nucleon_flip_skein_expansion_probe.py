#!/usr/bin/env python3
"""qou-99qc: the p->n flip retypes TWO crossings, and Delta is a THREE-TERM
skein expansion in the SMOOTHED proton words -- exact to 60 dps.

🛑 THIS PROBE CORRECTS ITS OWN AUTHOR'S EARLIER CLAIM, WHICH REACHED A PR TITLE,
A PR BODY, A LEAN DOCSTRING AND A COMMENT ON A SIBLING PR. That claim was that
the nucleon words `differ in exactly one letter: a single sigma becomes a single
sigma^-1'. It is wrong at the LETTER level and the corpus's own data says so.
The counts it was read off -- proton (1,2,0), neutron (0,2,1) -- were never
wrong; the reading of them was. CHECK 1 below measures the actual difference
from `_GEN_CHAINS' rather than asserting it, and CHECK 4 falsifies the
one-letter reading numerically instead of merely retracting it in prose.

# Ref: computations/qbeta/qbeta_option_e_order_dof_range_probe.py  (NF machinery, calibrated)
# Ref: computations/qbeta/qbeta_delta_candidate_census_probe.py    (_GEN_CHAINS, the models)
# Ref: content/quantum-observable-universe/lean/QOU/QBeta/NucleonFlavourIsDetermined.lean
# Ref: .beans/qou-99qc--...md  (OWNER RULING 2026-09-08: eps := tr at z_D)

WHY TWO CROSSINGS AND NOT ONE. A nucleon is three quarks, so it carries
C(3,2) = 3 pair-crossings, and each quark sits in TWO of them. Beta decay flips
ONE quark, so it retypes every pair that quark belongs to -- two of the three.
Concretely `uud -> udd' by flipping the second up:

    (u1,u2) uu -> ud          retyped
    (u2,d3) ud -> dd          retyped
    (u1,d3) ud -> ud          untouched

The `ud' COUNT is preserved by CANCELLATION, one gained against one lost, not
because the mixed crossings are untouched. That is exactly what makes the count
statement `(1,2,0) -> (0,2,1)' compatible with the false one-letter reading.
`QOU.QBeta.NucleonFlavour.flip_retypes_pairs' proves the general form
(sorry-free, lean-direct exit 0).

WHAT THAT BUYS, AND IT IS THE POINT. Each retyped letter changes by the SAME
central scalar: the typed shifts are uu = 0, ud = -h/2, dd = -h, so both
retypings add exactly s = -h/2. A word differing from another at two slots by a
common central scalar expands exactly:

    X(a+s)Y(b+s)Z - X a Y b Z  =  s(XYbZ) + s(XaYZ) + s^2(XYZ)

(`QOU.QBeta.NucleonFlavour.two_shift_expansion', over a NONCOMMUTATIVE ring with
centrality of s as an explicit hypothesis -- the braid algebra is not
commutative and a commutative-ring proof would be unsound here). So

    Delta = s*(S_A + S_B) + s^2*S_AB

with S_A, S_B the proton word with ONE of the two flavour crossings SMOOTHED and
S_AB with BOTH smoothed. `tr^z' is linear on the normal-form vector, so the same
identity holds under the ruled functional. Delta is therefore a small
combination of LOWER-CROSSING words -- 10 and 9 crossings against 11.

WHY THE TYPING TABLE IS ONE SCALAR AND NOT THREE CONVENTIONS. The Hecke relation
of AGENTS.md 7a, sigma^2 = (q - q^-1) sigma + 1, gives sigma - h = sigma^-1 on
multiplication by sigma^-1. So the dd letter IS the inverse crossing and the ud
letter is exactly (sigma + sigma^-1)/2 -- `skein_letter_inv' and
`ud_letter_is_average', both sorry-free. The whole typing is the single scalar
-h/2 applied zero, one or two times.

WHAT THIS DOES AND DOES NOT CHANGE. It does NOT move any number: the residual is
still -15.451387 %, identical to the merged Option-E witness, because this is an
exact rewriting of the same element and not a new model. What it changes is the
STRUCTURE of the open question. `Delta' is no longer an opaque 11-crossing
difference; it is a fixed rational combination of three smoothed proton words,
so the decay observable is determined by traces of words the mass channel
already has to compute. Whether that helps is not claimed here.

ARITHMETIC. mpmath mpf at 60 dps end to end, proton pin, convention D. No
float64 (probes are not exempt). The NF machinery is imported from the merged
order probe, which calibrates itself against the committed census before use.

Run: python3 -u computations/qbeta/qbeta_nucleon_flip_skein_expansion_probe.py \
       2>&1 | tee /tmp/qbeta_flip_skein.log
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402
import qbeta_delta_candidate_census_probe as _census  # noqa: E402

mp = _order.mp

# Set the working precision HERE rather than inheriting it from the imported
# order probe. Both set 60, so nothing moves -- but `never_raises_dps_audit`
# flags an inherited dps as fragile and it is right to: a later edit to the
# parent would silently drop this probe to mpmath's default 15.
set_compute_dps(60)
mp.mp.dps = 60
H0, ZD, E0, QB, TARGET = _order.H0, _order.ZD, _order.E0, _order.QB, _order.TARGET
Q_50_DIGIT_STR = _order.Q_50_DIGIT_STR

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def tr(letters):
    return _order.tr_at(_order.word_nf(letters), ZD)


def drop(word, *idx):
    return [l for i, l in enumerate(word) if i not in idx]


def main() -> int:
    print("qou-99qc — the p→n flip retypes TWO crossings; Δ is a three-term "
          "skein expansion\n")
    print(f"  z_D    = {mp.nstr(ZD, 20)}")
    print(f"  h      = {mp.nstr(H0, 20)}")
    print(f"  TARGET = {mp.nstr(TARGET, 20)}\n")

    # ---- CHECK 1: measure the difference, do not assert it ------------------
    print("CHECK 1 — how many slots actually differ, read from _GEN_CHAINS")
    gp, gn = _census._GEN_CHAINS["p"], _census._GEN_CHAINS["n"]
    diffs = []
    flat = 0
    for g in (0, 1):
        for i, (a, b) in enumerate(zip(gp[g], gn[g])):
            if a != b:
                diffs.append((g, i, flat + i, a, b))
        flat += len(gp[g])
    for g, i, fi, a, b in diffs:
        print(f"    gen{g}[{i}] (flat {fi}):  p {a}  →  n {b}")
    check("exactly_two_slots_differ", len(diffs) == 2,
          f"{len(diffs)} — NOT one; the one-letter reading is false")
    check("both_shifts_are_minus_one_half",
          all(b - a == _census.sp.Rational(-1, 2) for _, _, _, a, b in diffs),
          "each retyped letter picks up the SAME central scalar s = −h/2")

    # ---- CHECK 2: the three-term expansion is exact -------------------------
    print("\nCHECK 2 — Δ = s(S_A + S_B) + s²·S_AB, exact")
    P = _order.canonical_letters("p")
    N = _order.canonical_letters("n")
    A, B = diffs[0][2], diffs[1][2]
    s = -H0 / 2
    assert P[A][0] == N[A][0] and P[B][0] == N[B][0]

    trP, trN = tr(P), tr(N)
    delta_direct = trN - trP
    SA, SB, SAB = tr(drop(P, A)), tr(drop(P, B)), tr(drop(P, A, B))
    delta_skein = s * (SA + SB) + s * s * SAB
    gap = abs(delta_direct - delta_skein)

    print(f"    s = −h/2   = {mp.nstr(s, 25)}")
    print(f"    tr(S_A)    = {mp.nstr(SA, 25)}   (10 crossings)")
    print(f"    tr(S_B)    = {mp.nstr(SB, 25)}   (10 crossings)")
    print(f"    tr(S_AB)   = {mp.nstr(SAB, 25)}   ( 9 crossings)")
    print(f"    direct     = {mp.nstr(delta_direct, 30)}")
    print(f"    expansion  = {mp.nstr(delta_skein, 30)}")
    check("three_term_expansion_is_exact", gap < mp.mpf("1e-50"),
          f"|direct − expansion| = {mp.nstr(gap, 5)} at 60 dps")

    t1 = s * (SA + SB)
    t2 = s * s * SAB
    print(f"    s-term     = {mp.nstr(t1, 25)}")
    print(f"    s²-term    = {mp.nstr(t2, 25)}   "
          f"({mp.nstr(abs(t2 / t1) * 100, 6)} % of the s-term)")

    # ---- CHECK 3: it changes no number ------------------------------------
    print("\nCHECK 3 — the rewriting moves nothing; the residual is unchanged")
    pct = (abs(delta_direct) * E0 / QB - 1) * 100
    check("residual_still_minus_15_4514_pct",
          abs(pct - mp.mpf("-15.4514")) < mp.mpf("0.001"),
          f"{mp.nstr(pct, 8)} % — matches the merged Option-E witness exactly")

    # ---- CHECK 4: falsify the one-letter reading numerically ---------------
    print("\nCHECK 4 — the ONE-letter reading, tested rather than retracted")
    print("    Under it Δ would be ±h times ONE smoothed word. Both candidates:")
    one_A = -H0 * SA
    one_B = -H0 * SB
    for lab, v in (("−h·tr(S_A)", one_A), ("−h·tr(S_B)", one_B)):
        rel = abs(v - delta_direct) / abs(delta_direct) * 100
        print(f"      {lab} = {mp.nstr(v, 20)}   ({mp.nstr(rel, 8)} % from Δ)")
    check("one_letter_reading_is_refuted",
          min(abs(one_A - delta_direct), abs(one_B - delta_direct))
          > mp.mpf("0.1") * abs(delta_direct),
          "neither single-smoothing candidate is within 10 % of Δ; the "
          "one-letter reading is not a rounding difference, it is wrong")

    # ---- CHECK 5: the smoothed words are genuinely lower-crossing ----------
    print("\nCHECK 5 — the expansion lands on LOWER-crossing words")
    check("smoothed_words_are_shorter",
          len(drop(P, A)) == len(P) - 1 and len(drop(P, A, B)) == len(P) - 2,
          f"{len(P)} → {len(drop(P, A))} → {len(drop(P, A, B))} crossings")

    ok = all(r[1] for r in RESULTS)
    print()
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — β-decay flips ONE quark, which retypes TWO of the three")
    print("pair-crossings, each by the same central scalar −h/2. Δ is therefore")
    print("an exact three-term combination of the proton word with one and both")
    print("flavour crossings SMOOTHED, verified to 60 dps. This is a structural")
    print("rewriting, not a new model: the residual is unchanged at −15.4514 %.")
    print("What it buys is that Δ is no longer an opaque 11-crossing difference")
    print("but a fixed rational combination of 10- and 9-crossing traces. It")
    print("also REFUTES this author's earlier one-letter claim numerically")
    print("(CHECK 4), which had reached a PR title, a PR body, a Lean docstring")
    print("and a sibling comment. Scope-(a): measured on the census multisets")
    print("and the gen-grouped ordering.")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-nucleon-flip-skein-expansion")
        w.set_description(
            "beta-decay flips ONE quark, which retypes TWO of a nucleon's three "
            "pair-crossings, each by the same central scalar s = -h/2. Delta is "
            "therefore an exact three-term expansion s(S_A + S_B) + s^2 S_AB in "
            "the proton word with one and both flavour crossings smoothed, "
            "verified to 60 dps. Corrects this author's earlier one-letter "
            "claim, which CHECK 4 refutes numerically. Changes no number."
        )
        w.add_data("markov_convention", "D — the ruled functional, z_D = q^3/(q^2+1)")
        w.add_data("q0_anchor", "proton")
        w.add_data("q0_value", Q_50_DIGIT_STR)
        w.add_data("differing_slots",
                   [{"gen": g, "index": i, "flat": fi, "p": str(a), "n": str(b)}
                    for g, i, fi, a, b in diffs])
        w.add_data("central_shift_s", mp.nstr(s, 30))
        w.add_data("smoothed_traces",
                   {"S_A": mp.nstr(SA, 30), "S_B": mp.nstr(SB, 30),
                    "S_AB": mp.nstr(SAB, 30)})
        w.add_data("delta",
                   {"direct": mp.nstr(delta_direct, 30),
                    "three_term_expansion": mp.nstr(delta_skein, 30),
                    "abs_gap": mp.nstr(gap, 8),
                    "s_term": mp.nstr(t1, 30),
                    "s2_term": mp.nstr(t2, 30),
                    "s2_over_s_pct": mp.nstr(abs(t2 / t1) * 100, 10)})
        w.add_data("residual_pct_unchanged", mp.nstr(pct, 12))
        w.add_data("one_letter_reading_refuted",
                   {"minus_h_times_S_A": mp.nstr(one_A, 25),
                    "minus_h_times_S_B": mp.nstr(one_B, 25),
                    "nearest_rel_error_pct":
                        mp.nstr(min(abs(one_A - delta_direct),
                                    abs(one_B - delta_direct))
                                / abs(delta_direct) * 100, 10)})
        w.add_caveat(
            "🛑 CORRECTION OF THIS AUTHOR'S OWN EARLIER CLAIM. PR #7212's title, "
            "body, the Lean docstring and a comment on this PR all said the two "
            "nucleon words 'differ in exactly one letter: a single sigma becomes "
            "a single sigma^-1'. Wrong at the letter level. The COUNTS it was "
            "read off -- (1,2,0) vs (0,2,1) -- are correct and unchanged; the "
            "reading was wrong because the preserved ud count is a cancellation, "
            "not an absence of change. CHECK 4 refutes the one-letter reading "
            "numerically rather than merely retracting it."
        )
        w.add_caveat(
            "Changes no number. The residual is -15.451387 %, identical to the "
            "merged Option-E witness, because this is an exact rewriting of the "
            "same element rather than a new model. Nothing downstream moves."
        )
        w.add_caveat(
            "Scope-(a): measured on the census typed-crossing multisets in the "
            "gen-grouped ordering. two_shift_expansion is proved for ANY two "
            "slots carrying a common central shift; that the nucleon words are "
            "in that shape is read off _GEN_CHAINS and re-verified here, not "
            "proved."
        )
        w.add_caveat(
            "The expansion does NOT reduce the open question to a solved one. It "
            "restates Delta in terms of 10- and 9-crossing traces; whether those "
            "are more tractable, or connect to the mass channel's own words, is "
            "not claimed."
        )
        for name, passed, det in RESULTS:
            w.add_assertion(name, "1" if passed else "0", "1", "0", source=det or None)
        w.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
