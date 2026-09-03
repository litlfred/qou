#!/usr/bin/env python3
"""Does a producer bake in a q0 pin? Decided by VALUE, not by spelling.

Why this exists
---------------
The q0-anchor triage asks one question per producer: does it read q0? The
import-cone trace answers that for q0 reached through ``q_parameter`` /
``qou_substrate.constants``, and it is the right tool for that. It has one
documented blind spot, and this audit is that blind spot's counterpart.

A producer can pin q0 **without importing anything**, by writing the value
into its own source. The cone trace looks for the literal prefix
``1.1099785``, so it sees a decimal and nothing else. It does not see:

    sp.Rational("2584370278640139188197914756009",       # = 1.1099785827513805...
                "2328306436538696289062500000000")

which is exactly how ``milnor_a4_deficit_h_form.py`` pins the proton anchor,
and which that script's own docstring records as the case it cannot catch.
Nor would it see ``Fraction(a, b)``, ``mpf("1.109...")`` reached through a
variable, or a pin assembled arithmetically.

**A hardcoded pin need not look like the pin.** So this audit parses the
source, evaluates every numeric literal and 1-/2-argument
``Rational`` / ``Fraction`` / ``mpf`` / ``Decimal`` call to an exact
``Fraction``, and compares the VALUE against the two anchors. Spelling is
irrelevant to it by construction.

Relative window is 1e-6, wide on purpose: a pin truncated to 8 significant
digits is still a pin, and the two anchors are 11.6 ppb apart, so the window
cannot confuse one for the other.

What a verdict means
--------------------
``BAKED_PIN``   the value is in the source. Whether that is legitimate is a
                separate question this audit does not answer -- a deliberate
                cross-anchor comparison bakes in both pins correctly.
                A name suffixed ``?`` matched only in the wider truncation
                window; ``ambiguous:...`` means the value is within tolerance
                of more than one anchor and is NOT attributed to either.
``clean``       no q0-valued literal. Combined with a NO_Q0 cone verdict,
                that is the evidence for declaring a producer ``independent``.
                Alone it is not: a producer that IMPORTS q0 is clean here.

The two checks are complementary and neither is sufficient. Run both.

Usage
-----
    python3 computations/audits/producer_baked_pin_audit.py <file.py>...
    python3 computations/audits/producer_baked_pin_audit.py --selftest
    python3 computations/audits/producer_baked_pin_audit.py --all

``--selftest`` exits non-zero unless both known positives are still detected,
so a future narrowing of the matcher cannot quietly report a clean tree the
way a spelling-keyed check did.
"""
import ast
import pathlib
import sys
from fractions import Fraction

# The substrate anchors, exact. FOUR values are in play, not two: the proton
# pin, and THREE numbers that have all been called "the muon q0" --- the
# retired self-certified pin, and the lepton-tower derivation at CODATA 2018
# and at CODATA 2022 (the live canonical one).
ANCHORS = {
    "proton": Fraction(
        11099785827513808075916690956107688798744991218736, 10**49),
    "muon-retired": Fraction(11099785955573347, 10**16),
    "muon-codata2018": Fraction(1109978595554180575281594079610, 10**30),
    "muon-codata2022": Fraction(
        1109978595642739046681795129380001752700065561029011556974045769999095,
        10**69),
}

# Three windows, because the anchors are separated by three very different
# distances and one tolerance cannot serve all of them:
#
#   proton vs any muon          1.16e-8   relative
#   muon-retired vs -codata2022 7.7e-11
#   muon-retired vs -codata2018 2.8e-12
#
# TOL resolves the vintage; FAMILY_TOL resolves proton-vs-muon but not the
# vintage; TRUNC_TOL is wider than the proton/muon gap, so anything matching
# only at that width is genuinely unattributable and is reported as such.
#
# An earlier draft used a single 1e-6 window --- ~100x the proton/muon gap ---
# and reported the retired MUON pin as `proton` on 21 lines of one file. The
# lesson generalises: a tolerance looser than the separation it is meant to
# resolve does not blur the answer, it silently returns the first candidate.
TOL = Fraction(1, 10**13)
FAMILY_TOL = Fraction(1, 10**9)
TRUNC_TOL = Fraction(1, 10**7)


def _within(v, tol):
    return [k for k, ref in ANCHORS.items() if abs(v - ref) < tol * ref]


# Known positives --- --selftest fails if any stops being detected.
SELFTEST = [
    # sp.Rational(num, den): the form the import-cone trace documents as
    # invisible to it.
    ("computations/deltalambda/milnor_a4_deficit_h_form.py", "proton"),
    # a decimal truncated to 9 significant digits --- inside the truncation
    # window of more than one anchor, so deliberately NOT attributed.
    ("computations/probes/alpha_scale_is_outside_the_trace_probe.py",
     "ambiguous:truncated"),
    # BOTH pins in one file, which is what a cross-anchor comparison looks
    # like. Guards the regression that motivated the tolerance: with a window
    # wider than the 11.6 ppb anchor separation, every muon value here was
    # reported `proton`.
    # BOTH pins in one file, which is what a cross-anchor comparison looks
    # like. This is the regression guard for the tolerance: with a window
    # wider than the 11.6 ppb anchor separation, every muon value here was
    # reported `proton`. Its literals are truncated to 12 digits, so the
    # vintage is correctly NOT resolved --- `muon`, not `muon-retired`.
    ("computations/audits/q0_producer_pin_classifier.py", "muon"),
    ("computations/audits/q0_producer_pin_classifier.py", "proton"),
]

_CALLS = ("Rational", "Fraction", "mpf", "Decimal", "mpmathify")


def _anchor(v):
    """-> anchor name, a family/ambiguity verdict, or None. Never guesses."""
    exact = _within(v, TOL)
    if len(exact) == 1:
        return exact[0]

    fam = _within(v, FAMILY_TOL)
    if fam:
        kinds = {k.split("-")[0] for k in fam}
        if kinds == {"muon"}:
            # digits do not reach the vintage, but proton is excluded
            return "muon" if len(fam) > 1 else fam[0]
        if kinds == {"proton"}:
            return "proton"
        return "ambiguous:" + "|".join(sorted(fam))

    loose = _within(v, TRUNC_TOL)
    if len(loose) > 1:
        return "ambiguous:truncated"
    if len(loose) == 1:
        return loose[0] + "?"
    return None


def _values(tree):
    """Yield (Fraction, how-it-was-written, lineno) for everything evaluable."""
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant):
            if isinstance(n.value, bool):
                continue
            if isinstance(n.value, (int, float)):
                try:
                    yield Fraction(n.value).limit_denominator(10**60), repr(n.value), n.lineno
                except (ValueError, OverflowError):
                    pass
            elif isinstance(n.value, str):
                try:
                    yield Fraction(n.value.strip()), n.value.strip()[:44], n.lineno
                except (ValueError, ZeroDivisionError):
                    pass
        elif isinstance(n, ast.Call):
            fn = n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, "id", "")
            if fn not in _CALLS:
                continue
            args = []
            for a in n.args:
                if isinstance(a, ast.Constant) and not isinstance(a.value, bool):
                    try:
                        args.append(Fraction(str(a.value).strip()))
                    except (ValueError, ZeroDivisionError):
                        args.append(None)
                else:
                    args.append(None)
            if len(args) == 2 and all(a is not None for a in args) and args[1] != 0:
                yield args[0] / args[1], f"{fn}(<num>, <den>)", n.lineno
            elif len(args) == 1 and args[0] is not None:
                yield args[0], f"{fn}({str(args[0])[:24]})", n.lineno


def audit(path):
    """-> [(anchor, how-written, lineno)]; empty means no q0-valued literal."""
    try:
        tree = ast.parse(pathlib.Path(path).read_text(errors="replace"))
    except (SyntaxError, OSError):
        return None
    out = []
    for v, how, ln in _values(tree):
        a = _anchor(v)
        if a:
            out.append((a, how, ln))
    return out


def _report(path, hits):
    if hits is None:
        print(f"PARSE_FAIL {path}")
        return
    print(f"{'BAKED_PIN' if hits else 'clean    '} {path}")
    for a, how, ln in hits:
        print(f"      L{ln} {a}: {how}")


# Value-level invariants: unlike the file cases above, these cannot go stale
# when a producer is edited. (written-value, expected verdict)
SELFTEST_VALUES = [
    ("1.1099785955573347", "muon-retired"),
    ("1.109978595554180575281594079610", "muon-codata2018"),
    ("1.109978595642739046681795129380", "muon-codata2022"),
    ("1.1099785827513808075916690956107688798744991218736", "proton"),
    # 12 digits: proton excluded, vintage not resolvable
    ("1.10997859555", "muon"),
    # 9 digits: a prefix of every anchor
    ("1.10997858", "ambiguous:truncated"),
    # not an anchor at all
    ("1.11", None),
]


def main(argv):
    if "--selftest" in argv:
        bad = 0
        for written, want in SELFTEST_VALUES:
            got = _anchor(Fraction(written))
            ok = got == want
            print(f"{'ok  ' if ok else 'FAIL'} value {written:52s} -> {got}"
                  + ("" if ok else f"   (expected {want})"))
            bad += not ok
        for path, want in SELFTEST:
            hits = audit(path)
            got = {a for a, _, _ in (hits or [])}
            ok = want in got
            print(f"{'ok  ' if ok else 'FAIL'} {path} -> expected {want}, got {sorted(got) or 'none'}")
            bad += not ok
        if bad:
            print(f"\nSELFTEST FAILED ({bad}) --- the matcher no longer sees a pin it "
                  f"provably used to see. Do not trust a clean sweep until this passes.")
        return 1 if bad else 0

    if "--all" in argv:
        targets = sorted(str(p) for p in pathlib.Path("computations").rglob("*.py"))
    else:
        targets = [a for a in argv if not a.startswith("--")]
    if not targets:
        print(__doc__)
        return 2

    n = 0
    for t in targets:
        hits = audit(t)
        if hits or "--quiet" not in argv:
            _report(t, hits)
        n += bool(hits)
    print(f"\n{n} of {len(targets)} bake in a q0 pin.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
