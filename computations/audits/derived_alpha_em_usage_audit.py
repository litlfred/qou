#!/usr/bin/env python3
"""derived_alpha_em_usage_audit.py — flag CODATA α_EM used as a production INPUT.

The framework DERIVES α_EM from q₀ (`pyhecke.constants.ALPHA_EM_INV_DERIVED`,
the Bring zero-mode / `q[9]_q[10]_q` form) and already uses the derived value in
the meson EM sector (`meson_em_sinh_closed_form._alpha_em_inv_derived`). But
`coulomb_energy.py` — the whole nuclear EM sector — hard-codes the CODATA value
as `ALPHA_HBAR_C_MEV_FM = 1.43996`, so every Coulomb energy in the binding
dashboard is built on an experimental input where a derived one exists.

That is a PROVENANCE defect, not primarily a numerical one: derived and CODATA
α_EM agree closely, so the number barely moves. What moves is the claim. A
prediction that silently consumes CODATA α_EM is not parameter-free, and the
framework's headline is that it is.

## The distinction this audit exists to make

Not every CODATA α_EM literal is a bug. Two legitimate uses:

  * VALIDATION — `alpha_em_*_probe.py` and friends compare the DERIVED value
    against CODATA. That is the whole point of those probes; the CODATA literal
    is the target, not an input.
  * DISPLAY — printing CODATA alongside a derived number for the reader.

The defect is CODATA feeding a COMPUTATION whose output is a predicted
observable.

## HONEST LIMITS — the INPUT bucket is a REVIEW QUEUE, not a defect list

This is a triage tool and it OVER-REPORTS. It classifies by file and by whether
the literal is consumed on its line, which still admits false positives:
comparator assignments like `codata_inv = mpf("137.035999084")` in a file that
is not name-matched to the alpha cluster, and docstring prose that happens to
contain an `=` or an operator. Do not quote the INPUT count as a defect count.

CONFIRMED defects, hand-checked, in order of consequence:

  1. `coulomb_energy.py:38` — ALPHA_HBAR_C_MEV_FM = 1.43996. THE one that
     matters: it feeds every Coulomb energy in the binding dashboard, i.e. a
     predicted observable, and the derived alpha_EM already exists and is
     already used in the meson sector. Also float64.
  2. `b_over_a_evaluator.py:126` — ALPHA_EM = 1.0 / 137.035999084. A bare
     Python float AND CODATA, in an evaluator.
  3. `audits/m_k_m_pi_closure_pattern_audit.py:114` — alpha_em_codata used
     alongside the derived closure. Check which one reaches the result.

Everything else in the INPUT bucket needs a human read before being called a
defect. The point of the tool is to bound the search, not to settle it.

Read-only: writes no witness, runs no producer.

Usage:
    python3 computations/audits/derived_alpha_em_usage_audit.py
    python3 computations/audits/derived_alpha_em_usage_audit.py --self-test
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent          # computations/
sys.path.insert(0, str(HERE))
from _source_normalise import code_and_numeric_strings_only, code_only  # noqa: E402

# CODATA α_EM in its usual spellings: 1/α, α, and α·ℏc in MeV·fm.
CODATA_PAT = re.compile(
    r"137\.03[0-9]*|1\.43996|0\.0072973525|7\.2973525[0-9]*e-3", re.I)

# The right discriminator is NOT the line's wording -- a first pass tried that
# and failed its own self-test: a trailing `#` comment made
# `ALPHA_HBAR_C_MEV_FM = 1.43996  # CODATA` read as "validation", hiding the one
# defect the audit exists to find, while 54 alpha_EM-derivation probes were
# reported as false flags.
#
# The discriminator is WHICH FILE the literal is in. A file whose job IS alpha_EM
# (deriving it, or validating the derivation against CODATA) must hold the CODATA
# value -- that is its reference target. Any OTHER file consuming CODATA alpha_EM
# is consuming an experimental input where a derived one exists.
ALPHA_HOME = re.compile(r"alpha_em|alpha_k|(^|/)alpha/|fine_structure|photon_ir",
                        re.I)

# Within a non-alpha file, the literal must actually be consumed, not just named
# in prose. Strip comments and docstring-ish lines first.
CONSUMED = re.compile(r"=\s*[^=]|return\s|[*/+-]")


def _strip_comment(line: str) -> str:
    """Drop a trailing # comment, respecting simple quoting."""
    out, q = [], None
    for ch in line:
        if q:
            out.append(ch)
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            out.append(ch)
        elif ch == "#":
            break
        else:
            out.append(ch)
    return "".join(out)


def live_py_files() -> list[Path]:
    """Every live .py under computations/, skipping deprecated trees."""
    return [p for p in sorted(ROOT.rglob("*.py"))
            if ("_deprecated" not in p.parts and "fsh-guts" not in p.parts) and "__pycache__" not in p.parts]


def classify(line: str, path: str = "") -> str:
    """VALIDATION | INPUT | UNCLEAR for one matching line.

    `path` decides: inside the alpha_EM cluster the CODATA literal is the
    reference target and is legitimate; outside it, a consumed literal is an
    experimental input standing in for a derived one.
    """
    if ALPHA_HOME.search(path):
        return "VALIDATION"
    code = code_and_numeric_strings_only(_strip_comment(line))
    if not CODATA_PAT.search(code):
        return "VALIDATION"          # literal lives only in a comment/docstring/prose string
    if CONSUMED.search(code):
        return "INPUT"
    return "UNCLEAR"


def scan() -> dict[str, list[tuple[str, int, str]]]:
    out: dict[str, list[tuple[str, int, str]]] = {
        "INPUT": [], "VALIDATION": [], "UNCLEAR": []}
    for p in live_py_files():
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # Skip the audit itself and the shared normaliser — their own regexes
        # and selftests contain the literals.
        if p.name in (Path(__file__).name, "_source_normalise.py"):
            continue
        code_lines = code_only(text).splitlines()
        norm_lines = code_and_numeric_strings_only(text).splitlines()
        for i, (orig_line, code_line, norm_line) in enumerate(
            zip(text.splitlines(), code_lines, norm_lines), 1
        ):
            # Skip docstring/comment regions via `code_only` so multi-line
            # strings and inline comments cannot look like assignments.
            if not CODATA_PAT.search(code_line):
                continue
            rel = str(p.relative_to(ROOT))
            out[classify(norm_line, rel)].append(
                (rel, i, orig_line.strip()[:104]))
    return out


def report() -> int:
    res = scan()
    print("=" * 78)
    print(" CODATA alpha_EM usage — is it an INPUT (flag) or a TARGET (fine)?")
    print("=" * 78)
    print(f"  INPUT (FLAG)  {len(res['INPUT']):>4}   CODATA feeding a computation")
    print(f"  VALIDATION    {len(res['VALIDATION']):>4}   compared against / printed — legitimate")
    print(f"  UNCLEAR       {len(res['UNCLEAR']):>4}   needs a human read")
    for bucket in ("INPUT", "UNCLEAR"):
        if not res[bucket]:
            continue
        print(f"\n--- {bucket} ---")
        for rel, ln, src in res[bucket]:
            print(f"  {rel}:{ln}")
            print(f"      {src}")
    print("\nNOTE. The derived and CODATA values agree closely, so flagging a site")
    print("is a PROVENANCE claim, not a numerical one: a prediction that consumes")
    print("CODATA alpha_EM is not parameter-free, however small the difference.")
    return 1 if res["INPUT"] else 0


def self_test() -> int:
    fails = 0

    def chk(name: str, ok: bool) -> None:
        nonlocal fails
        if not ok:
            fails += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}")

    chk("detects 1/alpha literal", bool(CODATA_PAT.search("137.035999084")))
    chk("detects alpha*hbar c literal", bool(CODATA_PAT.search("1.43996")))
    chk("no false positive on a plain year",
        not CODATA_PAT.search("published in 1969"))
    chk("assignment classifies INPUT",
        classify("ALPHA_HBAR_C_MEV_FM = 1.43996", "coulomb_energy.py") == "INPUT")
    chk("alpha_EM-cluster file classifies VALIDATION",
        classify('CODATA = mp.mpf("137.035999084")',
                 "alpha_em_schwinger_ladder_probe.py") == "VALIDATION")
    chk("literal only in a trailing comment is NOT a flag",
        classify("R0_FM = 1.2   # unrelated 137.036 mention", "x.py")
        == "VALIDATION")
    chk("trailing comment does not mask a real assignment",
        classify("ALPHA_HBAR_C_MEV_FM = 1.43996   # CODATA",
                 "coulomb_energy.py") == "INPUT")
    # Synthetic, not live-tree. The original asserted the coulomb_energy defect
    # was still PRESENT, so it went vacuous the moment that defect was fixed —
    # it kept passing by matching the docstring prose describing the old
    # behaviour, which is exactly the failure the docstring-skip above prevents.
    chk("the coulomb_energy defect shape is caught",
        classify("ALPHA_HBAR_C_MEV_FM = 1.43996", "coulomb_energy.py") == "INPUT")
    chk("prose string announcing derivation is NOT a flag",
        classify('"(was CODATA 1.43996) and R0 = lambda_bar_pi"', "probe.py") == "VALIDATION")
    chk("f-string prose with operator is NOT a flag",
        classify('f"(3/5) Z(Z-1) e^2 / R, with e^2 = 1.43996 MeV.fm: {x}"', "probe.py") == "VALIDATION")
    chk("mpf numeric string assignment IS caught",
        classify('alpha_em = mp.mpf(1) / mp.mpf("137.035999084")', "probe.py") == "INPUT")
    chk("live tree: coulomb_energy is now CLEAN",
        not any("coulomb_energy" in r for r, _, _ in scan()["INPUT"]))
    print(f"\n{'PASS' if not fails else 'FAIL'} — {fails} failure(s)")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    return self_test() if a.self_test else report()


if __name__ == "__main__":
    sys.exit(main())
