#!/usr/bin/env python3
"""`prop:frobenius-gram-matrix` published a convention-D eigenvalue that **no
registered `q0` produces** — a transcription error, not a pin difference.

WHY THIS EXISTS
---------------
`scripts/witness-block-agreement.py` flagged this block 5/6. Four of the five are
a false-positive class the checker did not yet name: the block publishes the
**convention-C** spectrum deliberately, side by side with D and explicitly
labelled "under the excised convention C", so a producer computing D correctly
carries none of them. The block is doing the right thing and the checker was
counting it as a defect.

The fifth was real.

THE FINDING
-----------
The largest **D** eigenvalue was published as `+4.23033920`. The block's own
declared witness (`frobenius-gram-matrix-probe.witness.json`, `q0Anchor: proton`)
computes `4.230339225030225`, which rounds to `4.23033923` — five half-ulps away
at the published precision. Close enough to look like a pin difference: the
proton/muon gap is `1.15e-8` relative, which moves this eigenvalue by about
`4e-8`, the same order as the `2.5e-8` discrepancy. So magnitude alone cannot
tell a typo from a pin, and it had to be computed.

Rebuilding the whole `6 x 6` Gram matrix from this block's own symbolic entries
and substituting each registered pin:

    pin          largest D eigenvalue     to 8 dp
    proton       4.230339225030226        4.23033923
    muon (live)  4.230339401101782        4.23033940
    retired      4.230339399892241        4.23033940
    -----------------------------------------------
    published                             4.23033920   <- NO PIN

**No registered `q0` produces it.** The other five D entries
(`-0.75270211`, `0`, `+0.75270211` x3) are correct at the proton pin and
unchanged. Corrected in the block to `4.23033923`.

THIS IS A REGRESSION GUARD, NOT A DEFECT ASSERTION
---------------------------------------------------
The checks below assert the CORRECTED state. A probe that asserts the defect goes
red the moment the fix lands — the `muon_pin_three_values_probe.py` failure
`qou-i229` already records.

WHAT IS NOT CLAIMED
-------------------
Nothing about the **C** column, which remains unverified against an independent
computation because convention C is excised and none exists. It does pass the one
check its own numbers permit — the six published C eigenvalues multiply to
`-0.189205215` against the published `det G = -0.189205219144`, a `2.0e-8`
agreement, which is what six figures rounded to 8 decimals should give. That is
internal consistency, **not** verification, and it is recorded as such.

Nothing about the signature reading, which this block already settled and
withdrew its earlier claim on (commit `748ba9b1`). Nothing about which pin the
block should use; the D column is proton throughout and that is not questioned
here.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

mp.mp.dps = 40

BLOCK = ROOT / ("folio/quantum-observable-universe/mass-theory/"
                "frobenius-gram-matrix.md")
DECLARED_WITNESS = COMP / "probes/frobenius-gram-matrix-probe.witness.json"

PINS = {
    "proton": "1.1099785827513808075916690956107688798744991218736",
    "muon_live": ("1.109978595642739046681795129380001752700065561029011"
                  "556974045769999095"),
    "retired": "1.1099785955541805752815940796095093779932822799587",
}

#: What the block published before this correction, and what it says now.
WAS = "4.23033920"
NOW = "4.23033923"

#: The convention-C column, published deliberately as a labelled comparison.
C_EIGENVALUES = ["-0.85506726", "0.10179667", "0.85506726", "0.85506726",
                 "0.85506726", "3.47694980"]
C_DET = "-0.18920521914403668"


def gram_spectrum(q_str: str):
    """Rebuild the 6x6 Gram matrix from the block's own symbolic entries."""
    spec = importlib.util.spec_from_file_location(
        "fg", COMP / "probes/frobenius_gram_matrix_probe.py")
    fg = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(fg)
    except SystemExit:
        pass
    basis = fg.NF_BASIS_WORDS
    n = len(basis)
    qv = sp.Float(q_str, 50)
    G = mp.matrix(
        [[mp.mpf(str(sp.N(fg.markov_trace_of_word(
            3, list(basis[i][1]) + list(basis[j][1])).subs(fg.Q_SYM, qv), 40)))
          for j in range(n)] for i in range(n)])
    return sorted(mp.re(e) for e in mp.eig(G)[0])


def to_dp(x, k: int = 8) -> str:
    """Round to k decimals as a decimal string. No float64."""
    return mp.nstr(mp.mpf(x), 20, strip_zeros=False) if k is None else \
        f"{mp.mpf(x):.{k}f}"


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])

    print("\n" + "=" * 78)
    print("§1  THE LARGEST D EIGENVALUE, AT EVERY REGISTERED PIN")
    print("=" * 78)
    spectra = {}
    for name, s in PINS.items():
        ev = gram_spectrum(s)
        spectra[name] = ev
        print(f"    {name:<11} {mp.nstr(ev[-1], 17):>22}   -> {to_dp(ev[-1])}")
    print(f"    {'PUBLISHED':<11} {'':>22}   -> {WAS}   (before correction)")

    produced = {to_dp(ev[-1]) for ev in spectra.values()}
    check("no registered q0 produces the published 4.23033920 — so it is a "
          "transcription error, not a pin difference", WAS not in produced)
    check("the proton pin gives 4.23033923, which is the corrected value",
          to_dp(spectra["proton"][-1]) == NOW)

    print("\n    (the proton/muon gap moves this eigenvalue by ~4e-8 and the")
    print("     discrepancy was 2.5e-8, so magnitude alone could not tell a")
    print("     typo from a pin — it had to be computed)")

    print("\n" + "=" * 78)
    print("§2  THE OTHER FIVE D ENTRIES ARE CORRECT AND UNCHANGED")
    print("=" * 78)
    ev = spectra["proton"]
    print(f"    computed  " + ",  ".join(mp.nstr(e, 9) for e in ev))
    print(f"    published -0.75270211, 0, +0.75270211 x3, +{NOW}")
    small = [e for e in ev if abs(e) < mp.mpf("1e-30")]
    wplus = [e for e in ev if abs(abs(e) - mp.mpf("0.752702113")) < mp.mpf("5e-9")]
    check("one exact null direction (the (1^3) Wedderburn block, y = 0 under D)",
          len(small) == 1)
    check("four entries at +-0.75270211, three positive and one negative",
          len(wplus) == 4 and sum(1 for e in wplus if e < 0) == 1)

    print("\n" + "=" * 78)
    print("§3  THE BLOCK NOW AGREES WITH ITS OWN DECLARED WITNESS")
    print("=" * 78)
    wit = json.loads(DECLARED_WITNESS.read_text(encoding="utf-8",
                                                errors="replace"))
    wev = sorted(mp.mpf(str(x)) for x in wit["data"]["gram_matrix_eigenvalues"])
    print(f"    witness q0Anchor            {wit.get('q0Anchor')}")
    print(f"    witness largest eigenvalue  {mp.nstr(wev[-1], 17)}")
    text = BLOCK.read_text(encoding="utf-8", errors="replace")
    check("the witness agrees with the proton recomputation to 1e-14",
          abs(wev[-1] - spectra["proton"][-1]) < mp.mpf("1e-14"))
    check(f"the block now publishes {NOW} and no longer {WAS}",
          NOW in text and WAS not in text.split("Digit corrected")[0])

    print("\n" + "=" * 78)
    print("§4  THE C COLUMN — INTERNAL CONSISTENCY ONLY, SAID AS SUCH")
    print("=" * 78)
    prod = mp.mpf(1)
    for e in C_EIGENVALUES:
        prod *= mp.mpf(e)
    det = mp.mpf(C_DET)
    rel = abs(prod - det) / abs(det)
    print(f"    product of the 6 published C eigenvalues  {mp.nstr(prod, 12)}")
    print(f"    published det G under C                   {mp.nstr(det, 12)}")
    print(f"    relative agreement                        {mp.nstr(rel, 4)}")
    check("the C column is internally consistent to 2e-8 — what six figures "
          "rounded to 8 decimals should give. This is CONSISTENCY, not "
          "verification: convention C is excised and no independent computation "
          "of it exists", rel < mp.mpf("1e-7"))

    print("\n" + "=" * 78)
    print("§S  VERDICT")
    print("=" * 78)
    print("  Four of the checker's five flags are the deliberately-labelled C")
    print("  comparison — a legitimate publication class, now named in the")
    print("  checker. The fifth was a real digit error in the D column, caught")
    print("  because the block disagreed with the witness it declares. Fixed.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python+sympy+mpmath")
        wb.set_content_block("prop:frobenius-gram-matrix")
        wb.set_description(
            "prop:frobenius-gram-matrix published its largest convention-D Gram "
            "eigenvalue as 4.23033920. Its own declared witness "
            "(frobenius-gram-matrix-probe, q0Anchor proton) computes "
            "4.230339225030225, which rounds to 4.23033923 -- five half-ulps away. "
            "The proton/muon pin gap moves this eigenvalue by ~4e-8 against a 2.5e-8 "
            "discrepancy, so magnitude alone could not distinguish a typo from a pin "
            "and it had to be computed. Rebuilding the whole 6x6 from the block's own "
            "symbolic entries at every registered pin gives 4.23033923 (proton), "
            "4.23033940 (muon live) and 4.23033940 (retired): NO registered q0 "
            "produces 4.23033920, so it is a transcription error. Corrected in the "
            "block; the other five D entries (-0.75270211, 0, +0.75270211 x3) are "
            "right at the proton pin and unchanged. Four of the checker's five flags "
            "on this block are the convention-C spectrum, published deliberately as a "
            "labelled side-by-side comparison against the production convention D -- "
            "a legitimate publication class, not a defect. The C column is left "
            "untouched and remains unverified against an independent computation "
            "because convention C is excised and none exists; it does pass the one "
            "check its own numbers permit, its six eigenvalues multiplying to "
            "-0.189205215 against the published det G = -0.189205219144, a 2.0e-8 "
            "agreement consistent with six 8-decimal roundings. That is internal "
            "consistency, not verification. qou-i229.")
        for name, evs in spectra.items():
            wb.add_data(f"D_spectrum_at_{name}", {
                "q0": PINS[name],
                "eigenvalues": [mp.nstr(e, 16) for e in evs],
                "largest_to_8dp": to_dp(evs[-1]),
            })
        wb.add_data("correction", {
            "block": "prop:frobenius-gram-matrix",
            "was": WAS,
            "now": NOW,
            "half_ulps_off_at_8dp": mp.nstr(
                abs(mp.mpf(WAS) - spectra["proton"][-1]) / mp.mpf("5e-9"), 4),
            "produced_by_any_registered_pin": "no",
        })
        # DELIBERATELY records only the RESULT of the C check, not the C figures
        # themselves. Listing them here would make a witness that declares this
        # block "carry" them, which closes the checker's row without producing
        # anything -- the aggregator weakness described in the script's docstring.
        # Those four figures genuinely have no producer (convention C is excised)
        # and the checker should keep saying so.
        wb.add_data("convention_C_column_internal_check", {
            "relative_agreement_of_eigenvalue_product_with_det": mp.nstr(rel, 6),
            "status": ("internal consistency only -- NOT verified, and the C "
                       "figures are deliberately NOT transcribed into this "
                       "witness; see the probe docstring"),
        })
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "The C column is NOT verified. Convention C is excised, so no independent "
            "computation of it exists in the corpus. The 2.0e-8 figure recorded here "
            "is the published eigenvalues multiplied against the published "
            "determinant -- internal consistency, which a set of wrong-but-consistent "
            "numbers would also pass.")
        wb.add_caveat(
            "Asserts the CORRECTED state, not the defect. A probe that asserts a "
            "defect goes red the moment the fix lands -- the muon_pin_three_values "
            "failure qou-i229 already records.")
        wb.add_caveat(
            "Says nothing about the signature reading; this block already settled "
            "that and withdrew its earlier indefinite/Lorentzian claim in 748ba9b1.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": (
            "comparison by design: evaluates the published Gram D-eigenvalue at every registered pin (proton, live CODATA-2022 muon, retired CODATA-2018 muon) to show none of them produces it")})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
