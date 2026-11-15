#!/usr/bin/env python3
"""Audit decimal literals against the canonical constants they claim to be.

WHY THIS IS VALUE-BASED, NOT STRING-BASED
-----------------------------------------
Bean `qou-jgew` found SEVEN wrong hand-typed Vol(4_1) values in one session; the
2026-06-21 audit fixed one more; and on 2026-08-30 `VOL_4_1_decimal` -- the corpus's
own designated approximation carrier -- was still wrong from its 21st significant
figure. Every one of those drains was a grep for a specific digit string, and every one
missed the sites spelling the same wrong number differently:

    Lean carrier          2.029883212819307250011597804990
    computations/ variant 2.0298832128193072500115970029

A grep for either misses the other. This script does not grep for known-bad strings.
It finds EVERY sufficiently-long decimal literal, asks which canonical constant it is
closest to, and then checks whether its own digits are right.

THE DISTINCTION THAT MATTERS
----------------------------
  TRUNCATED : the literal is a correct prefix (or correct rounding) of the constant.
              Correct but short. Fine, and often deliberate.
  WRONG     : the literal's own digits disagree with the constant before the literal
              runs out. Incorrect AND long -- worse, because the extra digits invite
              trust a short value would not get.

A coarse certified bound does NOT protect against the second kind: the corpus's
`abs_VOL_4_1_sub_decimal_lt` bounds the gap by 1/10 and held fine while the decimal was
wrong by 3e-20. Bounds guard magnitudes; only digit comparison guards digits.

Usage:
    python3 scripts/known-constant-literal-audit.py [--min-digits N] [--all] [PATH ...]
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

try:
    import mpmath as mp
except ImportError:
    print("known-constant-literal-audit: mpmath required", file=sys.stderr)
    raise SystemExit(2)

mp.mp.dps = 60

def _constants() -> dict[str, "mp.mpf"]:
    """Canonical values, each COMPUTED here rather than transcribed.

    Transcribing is the defect this script exists to catch; a hard-coded table would
    reproduce it one level up.
    """
    cl2_pi3 = mp.clsin(2, mp.pi / 3)
    return {
        "Cl_2(pi/3)":        cl2_pi3,
        "Vol(4_1)=2Cl2(pi/3)": 2 * cl2_pi3,
        "Catalan_G":         mp.catalan,
        "Vol(Borromean)=8G": 8 * mp.catalan,
        "Vol(5_2)":          _vol_5_2(),
        "pi":                mp.pi,
    }

def _vol_5_2() -> "mp.mpf":
    """3*D(y1), y1 the non-real root of X^3-2X^2+3X-1, via Bloch-Wigner."""
    rts = mp.polyroots([1, -2, 3, -1], maxsteps=200, extraprec=200)
    y1 = next(r for r in rts if mp.im(r) > 1e-30)
    return 3 * (mp.im(mp.polylog(2, y1)) + mp.arg(1 - y1) * mp.log(abs(y1)))

# a decimal literal with a fractional part; require enough digits to be identifiable
LIT = re.compile(r"(?<![\w.])(\d+\.\d{6,})(?![\w.])")

SKIP_DIRS = {".git", ".lake", "node_modules", "_deprecated", "fsh-guts", "beans/defs"}

# JSON keys that DECLARE a constant (as opposed to reporting a computed number)
KEY_NAMES_CONSTANT = re.compile(
    r'"[^"]*(vol[_-]?\d|vol[_-]?4|vol[_-]?5|volume|catalan|cl_?2|clausen|lobachevsky)'
    r'[^"]*"\s*:', re.I)

def sig_digits(s: str) -> int:
    return len(s.replace(".", "").lstrip("0"))

def classify(lit: str, const: "mp.mpf") -> tuple[str, int | None]:
    """Return (verdict, first_wrong_significant_figure)."""
    n = sig_digits(lit)
    # correctly rounded OR truncated to the literal's own length are both acceptable
    rounded = mp.nstr(const, n, strip_zeros=False).rstrip("0").rstrip(".")
    full = mp.nstr(const, n + 12, strip_zeros=False)
    truncated = full[: len(lit)]
    if lit.rstrip("0") == rounded.rstrip("0") or lit == truncated:
        return ("truncated", None)
    a = lit.replace(".", "")
    b = full.replace(".", "")
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return ("WRONG", i + 1)
    return ("truncated", None)

def selftest() -> int:
    """Assert the detector still catches what it was built for.

    Every detector in this corpus has a blind-spot story, and several were found blind
    by the detector written to replace them. The cases below are the REAL values this
    script was built from -- if a future narrowing stops catching them, this fails
    loudly instead of reporting a clean tree.

    Needs no repo, no files, no Lean.
    """
    consts = _constants()
    v41 = consts["Vol(4_1)=2Cl2(pi/3)"]
    v8g = consts["Vol(Borromean)=8G"]
    cases = [
        # (literal, constant, expected verdict, expected first-wrong sig fig)
        ("2.029883212819307250011597804990", v41, "WRONG", 21),   # was VOL_4_1_decimal
        ("2.0298832128193072500115970029",  v41, "WRONG", 21),    # computations/ variant
        ("2.029883212819307250042408",      v41, "WRONG", 25),    # false "24 dps verified"
        ("7.327724753846269",               v8g, "WRONG", 11),    # live in a mass formula
        # correct values must NOT fire -- a detector that flags everything is useless
        ("2.029883212819307250042405108549", v41, "truncated", None),
        ("2.0298832128193072",               v41, "truncated", None),
        ("2.029883212819307",                v41, "truncated", None),
        ("7.32772475341775",                 v8g, "truncated", None),
        ("7.327724753417752120",             v8g, "truncated", None),
    ]
    bad = 0
    for lit, const, want_v, want_p in cases:
        got_v, got_p = classify(lit, const)
        ok = (got_v == want_v) and (want_p is None or got_p == want_p)
        print(f"  [{'ok  ' if ok else 'FAIL'}] {lit:34} -> {got_v}"
              + (f" @ sig fig {got_p}" if got_p else ""))
        if not ok:
            bad += 1
            print(f"         expected {want_v}" + (f" @ {want_p}" if want_p else ""))
    print("selftest: " + ("PASS" if not bad else f"FAIL ({bad})"))
    return 0 if not bad else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=["folio", "computations", "scripts", "docs"])
    ap.add_argument("--min-digits", type=int, default=12,
                    help="ignore literals with fewer significant digits (default 12)")
    ap.add_argument("--all", action="store_true", help="also list correctly-truncated hits")
    ap.add_argument("--selftest", action="store_true",
                    help="check the detector against its own founding cases; needs no repo")
    ap.add_argument("--rel-tol", type=float, default=1e-6,
                    help="how close a literal must be to be considered a claim about a constant")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    consts = _constants()
    roots = [Path(p) for p in (args.paths or ["folio", "computations", "scripts", "docs"])]
    wrong, ok = [], []

    for root in roots:
        if not root.exists():
            continue
        for f in root.rglob("*"):
            if not f.is_file() or f.suffix not in {".lean", ".py", ".md", ".json", ".ts"}:
                continue
            if any(part in SKIP_DIRS for part in f.parts):
                continue
            if f.resolve() == Path(__file__).resolve():
                continue  # this file quotes known-bad values in its own docstring
            try:
                text = f.read_text(errors="ignore")
            except Exception:
                continue
            for ln, line in enumerate(text.splitlines(), 1):
                for m in LIT.finditer(line):
                    lit = m.group(1)
                    if sig_digits(lit) < args.min_digits:
                        continue
                    # A COMPUTED probe output that approximates a constant is not a
                    # transcription defect -- it is the measurement. Measured: 123 of
                    # 191 raw hits were witness.json numeric outputs, i.e. 64 % false
                    # positives by design. So inside JSON, require the key to NAME the
                    # constant; a transcribed `"vol_4_1": "..."` still gets caught.
                    if f.suffix == ".json" and not KEY_NAMES_CONSTANT.search(line):
                        continue
                    val = mp.mpf(lit)
                    for name, c in consts.items():
                        if c == 0:
                            continue
                        if abs(val - c) / abs(c) < args.rel_tol:
                            verdict, pos = classify(lit, c)
                            rec = (str(f), ln, lit, name, pos, mp.nstr(abs(val - c), 4))
                            (wrong if verdict == "WRONG" else ok).append(rec)
                            break

    if wrong:
        print("CANDIDATES -- the literal's own digits disagree with the constant.")
        print("HIGH RECALL, agent-confirmed: these are candidates, NOT verdicts.")
        print("Known legitimate classes that still land here:")
        print("  * a HISTORICAL record of a known-bad value (audit docs, bean bodies)")
        print("  * a float64 repr recorded deliberately (…5517578125-style tails)")
        print("  * a probe's converging numerical estimate quoted in prose")
        print("Triage each before changing anything.\n")
        for f, ln, lit, name, pos, err in sorted(wrong):
            print(f"  {f}:{ln}")
            print(f"      {lit}   claims {name}")
            print(f"      first wrong significant figure: {pos}   abs err {err}\n")
    if args.all and ok:
        print(f"correctly truncated/rounded ({len(ok)}):\n")
        for f, ln, lit, name, _, err in sorted(ok):
            print(f"  {f}:{ln}  {lit}  ({name}, err {err})")

    print(f"summary: {len(wrong)} candidates, {len(ok)} correctly truncated/rounded")
    return 1 if wrong else 0

if __name__ == "__main__":
    raise SystemExit(main())
