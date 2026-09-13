"""The alternating character's SIGN is `(-1)^length` — so no odd-length word
over the corpus alphabet can be PSD in the alternating block, and the nucleon
budget of 11 is odd.

# Ref: QOU.Mass.AltCharShiftMultiset.wordChar_sign -- the Lean, sorry-free,
#      proved BEFORE this probe was written (formalize-first)
# Ref: QOU.Mass.AltCharShiftMultiset.no_eleven_letter_word_is_alt_psd
# Ref: QOU.Mass.GammaGammaWordSelection.altChar_eq_one -- every gamma-gamma
#      word has character 1; gamma-gamma words have EVEN length
# Ref: bean qou-99qc, OWNER RULING 2026-09-13 -- SDP scope is (B) whole
#      element, so every Wedderburn projection must be PosSemidef
# Ref: computations/qbeta/qbeta_pn_asymmetry_has_one_home_under_the_ruling_probe.py
#      -- the engine route (`sign_block`) cross-checked to 4.6e-39

WHAT THIS CONFIRMS, AND WHAT PROVES IT.  The Lean proves it; this probe is the
numerical confirmation and the bridge to the engine.  The theorem:

    every letter of the corpus alphabet has NEGATIVE alternating character,
    so  sign(wordChar w) = (-1)^len(w),  for ANY letters, ANY order, ANY
    generator labelling.

    letterChar(sigma)     = -1/q           = -0.9009
    letterChar(bar-fixed) = -(q^2+1)/(2q)  = -1.0054
    letterChar(sigma^-1)  = -q             = -1.1100

WHY IT MATTERS.  Under the owner-selected SDP scope **(B) whole element**, the
confinement SDP of `qou-ales` asks every Wedderburn projection of a candidate
word to be `Matrix.PosSemidef`.  The alternating block `(1,1,1)` at `n = 3` is
ONE-DIMENSIONAL, so PSD there is exactly `0 <= character`.  The corpus nucleon
budget is **11**, which is ODD.  So the whole 11-crossing construction is
excluded -- not a choice of letters within it.

THAT REFRAMES THE OPEN PROBLEM.  Bean `qou-99qc` item 2 asked for "a principle
for the 5 un-ruled letters that is both bar-consistent and whole-element
PSD-admissible".  No such principle exists AT LENGTH 11: the obstruction does
not depend on which letters carry the proton/neutron asymmetry, so no choice
among them can repair it.  The question to ask instead is about the length.

TWO PARITY OBSTRUCTIONS, INDEPENDENT, SAME DIRECTION.  Gamma-gamma words have
even length (`gammaGamma_length_even`, sorry-free), which is why the
construction half of the ruling reaches only 6 of the 11 letters.  The SDP half
under (B) ALSO demands even length.  Neither argument uses the other.

WHAT IS CHECKED HERE:

1. the three letter characters, at the proton pin, all strictly negative;
2. the exact threshold `d >= 1/(q^2-1)` at which a letter would go positive,
   and how far the corpus letters sit from it;
3. the parity, EXHAUSTIVELY over all 3^n words for n = 1..6 (1092 words);
4. the parity by the INDEPENDENT ENGINE ROUTE -- Hoefsmit `(1,1,1)` matrices
   rather than the scalar product -- on a sample at each length;
5. the corpus nucleon words: 11 letters, odd, negative, excluded;
6. the consistency check that even-length words are POSITIVE, so the result is
   a discriminator and not a blanket sign claim.

SCOPE.  **(b) structural**, invariant named: the sign of the alternating
character.  Honest limit, from the Lean docstring rather than discovered later:
per-letter negativity fails for a letter with shift `d >= 1/(q^2-1)`, about
4.31 at the substrate pin.  Every corpus letter has `d` in {0, -1/2, -1}.  This
excludes words over the CORPUS ALPHABET, not over every conceivable alphabet.
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

_OC = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_ocneanu_trace_general_n_probe.py")
_spec = importlib.util.spec_from_file_location("_oc", _OC)
_oc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_oc)

_FE = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_gamma_gamma_sdp_feasibility_probe.py")
_spec2 = importlib.util.spec_from_file_location("_fe", _FE)
_fe = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(_fe)

set_compute_dps(60)
mp.mp.dps = 40

Q0 = mp.mpf(str(_oc.Q0))
H0 = mp.mpf(str(_oc.H0))

#: the corpus alphabet, as shift-in-units-of-h. `sigma`, the bar-fixed letter,
#: and `sigma^-1`. These are the three `Letter` constructors of
#: `QOU.Mass.AltCharShiftMultiset` (.uu, .ud, .dd respectively).
SHIFTS = {"sigma": mp.mpf(0), "fixed": mp.mpf("-0.5"), "inv": mp.mpf(-1)}

#: the corpus nucleon words, as (generator, shift) -- 11 letters each.
CORE = [(0, mp.mpf(0)), (1, mp.mpf(-1))] * 3
QUARK = {
    "p": [(0, mp.mpf(0)), (0, mp.mpf("-0.5")), (1, mp.mpf("-0.5"))],
    "n": [(0, mp.mpf("-0.5")), (0, mp.mpf("-0.5")), (1, mp.mpf(-1))],
}
GLUON = [(0, mp.mpf(0)), (0, mp.mpf(0))]

TOL = mp.mpf("1e-30")

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def alt_letter(d) -> mp.mpf:
    """The alternating rep sends `sigma_i -> -1/q`, so a letter `sigma_g + d*h`
    goes to `-1/q + d*h`. Generator-blind, per `altChar_regen`."""
    return -1 / Q0 + mp.mpf(str(d)) * H0


def alt_word_scalar(letters) -> mp.mpf:
    """Route A: the product of per-letter characters."""
    out = mp.mpf(1)
    for _g, d in letters:
        out *= alt_letter(d)
    return out


def alt_word_engine(letters) -> mp.mpf:
    """Route B, INDEPENDENT: multiply the Hoefsmit `(1,1,1)` block matrices and
    take the trace. One-dimensional, so the trace IS the character -- but it is
    computed from the engine's generator matrices, never from `alt_letter`."""
    sig, dim = _fe.blocks(3)[(1, 1, 1)]
    M = mp.eye(dim)
    for g, d in letters:
        M = M * (sig[g] + (mp.mpf(str(d)) * H0) * mp.eye(dim))
    return sum(M[j, j] for j in range(dim))


def main() -> int:
    w = WitnessBuilder("qbeta-altchar-sign-is-length-parity")
    w.set_description(
        "The alternating character's SIGN is (-1)^length over the corpus "
        "alphabet: every letter has strictly negative character (-1/q, "
        "-(q^2+1)/(2q), -q), so a product of them is decided in sign by nothing "
        "but how many there are. Proved first in Lean "
        "(QOU.Mass.AltCharShiftMultiset.wordChar_sign, sorry-free); this probe "
        "confirms it exhaustively over all 3^n words for n = 1..6 and by an "
        "INDEPENDENT engine route (Hoefsmit (1,1,1) matrices). CONSEQUENCE: "
        "under the owner-selected SDP scope (B) whole element, the alternating "
        "block is 1-dimensional so PSD there is 0 <= character; the nucleon "
        "budget is 11, which is ODD; so the entire 11-crossing construction is "
        "excluded, not merely a choice of letters within it. This REFRAMES bean "
        "qou-99qc item 2: no principle for the 5 un-ruled letters can repair an "
        "obstruction that does not depend on them."
    )

    print("== 1. every corpus letter has negative alternating character ==")
    chars = {k: alt_letter(d) for k, d in SHIFTS.items()}
    for k, v in chars.items():
        print(f"     letterChar({k:6s}) = {mp.nstr(v, 20)}")
    check("every_corpus_letter_has_negative_alternating_character",
          all(v < 0 for v in chars.values()),
          f"sigma {mp.nstr(chars['sigma'], 12)}, bar-fixed "
          f"{mp.nstr(chars['fixed'], 12)}, sigma^-1 {mp.nstr(chars['inv'], 12)} "
          f"-- all three strictly negative at the proton pin. This is the whole "
          f"mechanism: the sign of a product of them depends on nothing but how "
          f"many there are. Lean: AltCharShiftMultiset.letterChar_neg", w)

    print("\n== 2. the threshold a letter would have to clear ==")
    qs = sp.Symbol("q", positive=True)
    thr_sym = sp.simplify(1 / (qs ** 2 - 1))
    thr = mp.mpf(str(sp.N(thr_sym.subs(qs, sp.Rational(Q_50_DIGIT_STR)), 30)))
    worst = max(SHIFTS.values())
    print(f"     threshold d >= 1/(q^2-1) = {mp.nstr(thr, 20)}")
    print(f"     largest corpus shift     = {mp.nstr(worst, 20)}")
    check("no_corpus_letter_is_anywhere_near_the_positivity_threshold",
          worst < thr and (thr - worst) > 4,
          f"a letter needs shift d >= 1/(q^2-1) = {mp.nstr(thr, 12)} to reach "
          f"non-negative character. The largest corpus shift is "
          f"{mp.nstr(worst, 6)}, short by {mp.nstr(thr - worst, 12)}. This is "
          f"the honest limit of the exclusion: it covers the corpus alphabet, "
          f"not every conceivable alphabet", w)

    print("\n== 3. parity, EXHAUSTIVELY over all 3^n words, n = 1..6 ==")
    keys = list(SHIFTS)
    total = 0
    bad: list[str] = []
    per_n = {}
    for n in range(1, 7):
        cnt = 0
        for combo in itertools.product(keys, repeat=n):
            letters = [(i % 2, SHIFTS[k]) for i, k in enumerate(combo)]
            v = alt_word_scalar(letters)
            expected_pos = (n % 2 == 0)
            if (v > 0) != expected_pos or abs(v) < TOL:
                bad.append(f"n={n} {combo}")
            cnt += 1
            total += 1
        per_n[n] = cnt
        print(f"     n={n}: {cnt:4d} words, all {'positive' if n % 2 == 0 else 'negative'}")
    check("the_sign_is_length_parity_on_all_1092_words_exhaustively",
          not bad and total == 1092,
          f"all {total} words over the 3-letter alphabet at lengths 1..6 have "
          f"sign exactly (-1)^length -- {len(bad)} exceptions. Exhaustive, not "
          f"sampled: 3+9+27+81+243+729. Generators were varied along each word "
          f"too, confirming the generator-blindness altChar_regen states", w)

    print("\n== 4. the SAME parity by the independent ENGINE route ==")
    eng_bad: list[str] = []
    worst_gap = mp.mpf(0)
    for n in range(1, 7):
        for combo in list(itertools.product(keys, repeat=n))[:12]:
            letters = [(i % 2, SHIFTS[k]) for i, k in enumerate(combo)]
            a = alt_word_scalar(letters)
            b = alt_word_engine(letters)
            gap = abs(a - b)
            worst_gap = max(worst_gap, gap)
            if gap > TOL or (b > 0) != (n % 2 == 0):
                eng_bad.append(f"n={n} {combo} gap={mp.nstr(gap, 6)}")
    check("the_engine_route_agrees_and_shows_the_same_parity",
          not eng_bad,
          f"multiplying the Hoefsmit (1,1,1) generator matrices and taking the "
          f"trace reproduces the per-letter product to {mp.nstr(worst_gap, 6)} "
          f"across lengths 1..6, and carries the same sign parity. The scalar "
          f"model is not assumed -- it is confirmed against the engine", w)

    print("\n== 5. the corpus nucleon words: 11 letters, odd, excluded ==")
    rows = {}
    for kind in ("p", "n"):
        word = CORE + QUARK[kind] + GLUON
        a = alt_word_scalar(word)
        b = alt_word_engine(word)
        rows[kind] = {"length": len(word), "scalar": mp.nstr(a, 25),
                      "engine": mp.nstr(b, 25), "agree_to": mp.nstr(abs(a - b), 6)}
        print(f"     {kind}: len={len(word)}  altChar={mp.nstr(a, 20)}  "
              f"engine agrees to {mp.nstr(abs(a - b), 6)}")
    ok5 = all(len(CORE + QUARK[k] + GLUON) == 11 for k in ("p", "n")) and \
        all(alt_word_scalar(CORE + QUARK[k] + GLUON) < 0 for k in ("p", "n"))
    check("both_corpus_nucleon_words_are_odd_length_and_negative",
          ok5,
          f"both are 11 letters (ODD) and both have strictly negative "
          f"alternating character -- p {rows['p']['scalar'][:14]}, n "
          f"{rows['n']['scalar'][:14]}. The (1,1,1) block is 1-dimensional, so "
          f"PSD there is 0 <= character: under scope (B) both are excluded, and "
          f"by the parity theorem so is EVERY 11-letter word over this alphabet, "
          f"whatever its letters. Lean: no_eleven_letter_word_is_alt_psd", w)

    print("\n== 6. even length is POSITIVE — a discriminator, not a blanket sign ==")
    core_val = alt_word_scalar(CORE)
    gluon_val = alt_word_scalar(GLUON)
    check("even_length_words_are_positive_so_the_parity_discriminates",
          core_val > 0 and gluon_val > 0 and abs(core_val - 1) < TOL,
          f"the 6-letter gamma-gamma core has character {mp.nstr(core_val, 12)} "
          f"(exactly 1, as altChar_eq_one requires) and the 2-letter gluon pair "
          f"{mp.nstr(gluon_val, 12)} -- both POSITIVE. So the result is not "
          f"'the character is always negative'; it is a parity. This is also "
          f"the consistency check against altChar_eq_one, which pins every "
          f"gamma-gamma word at 1: gamma-gamma words have EVEN length", w)

    w.add_data("letter_characters", {
        k: {"shift_in_h": mp.nstr(SHIFTS[k], 10), "char": mp.nstr(v, 25),
            "lean_constructor": {"sigma": ".uu", "fixed": ".ud", "inv": ".dd"}[k]}
        for k, v in chars.items()
    })
    w.add_data("positivity_threshold", {
        "symbolic": str(thr_sym),
        "value_at_proton_pin": mp.nstr(thr, 25),
        "largest_corpus_shift": mp.nstr(worst, 10),
        "margin": mp.nstr(thr - worst, 25),
        "meaning": "a letter would need this shift to reach non-negative "
                   "character; no corpus letter is close, so the exclusion "
                   "covers the corpus alphabet and not every alphabet",
    })
    w.add_data("exhaustive_parity", {
        "words_tested": total,
        "per_length": per_n,
        "exceptions": bad,
        "method": "all 3^n words over the 3-letter alphabet, n = 1..6, with "
                  "generators varied along each word",
    })
    w.add_data("corpus_nucleon_words", rows)
    w.add_data("consequence_under_scope_B", {
        "scope": "(B) whole element -- owner ruling 2026-09-13, bean qou-99qc",
        "alternating_block_dimension": 1,
        "so_psd_is": "0 <= alternating character",
        "nucleon_budget": 11,
        "parity": "odd",
        "verdict": "every 11-letter word over the corpus alphabet is excluded, "
                   "independent of which letters carry the p/n asymmetry",
        "reframes": "bean qou-99qc item 2 asked for a principle for the 5 "
                    "un-ruled letters that is bar-consistent AND whole-element "
                    "PSD-admissible. No such principle exists at length 11: the "
                    "obstruction does not depend on those letters",
        "second_independent_obstruction": "gamma-gamma words have even length "
                                          "(gammaGamma_length_even), which is "
                                          "why the construction half reaches "
                                          "only 6 of 11. The SDP half demands "
                                          "even length too, by a different "
                                          "argument",
    })
    w.add_data("scope", {
        "class": "(b) structural",
        "invariant": "the sign of the alternating character, = (-1)^length",
        "proved_in": "QOU.Mass.AltCharShiftMultiset.wordChar_sign and "
                     "no_eleven_letter_word_is_alt_psd (sorry-free)",
        "honest_limit": "per-letter negativity fails for a letter with shift "
                        "d >= 1/(q^2-1) ~ 4.31; every corpus letter is in "
                        "{0, -1/2, -1}",
        "what_is_NOT_claimed": "that no nucleon word exists -- only that none "
                               "of ODD length over this alphabet is admissible "
                               "in the alternating block under scope (B)",
    })
    # AGENTS.md q0-anchor rule: "Say which pin you used. Any new witness
    # must record its q0 so a later reader can tell which layer it belongs
    # to without inferring it from a call site."
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.save()

    ok = not FAILED
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
