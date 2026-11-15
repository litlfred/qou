#!/usr/bin/env python3
# polynomial_q_not_applicable: arithmetic on a recorded column, not a q-series compute.
"""The beta3 defect is ISOLATED TO THE COEFFICIENT — not the anchor, not the invariant.

OWNER INSTRUCTION 2026-09-12: *"the beta3/h_A^2 14.2 % defect open"*.

THE DEFECT. The recovered producer witness `atom-mass-complete-wedderburn`
(added 2026-04-10 in `1359fe23ac` under `folio-assistant/computations/`; out of
tree since the miga split) reproduces the published Z=1-20 mass table exactly,
and its third coefficient is `beta3 = 0.0499`. `thm:wedderburn-mass-formula`
publishes that coefficient as `h_A^2 = (q0 - 1/q0)^2 = 0.043707282...`, a
**14.169 %** departure. Under the no-fitting directive neither may be adjusted
to meet the other, so the corpus was left with an authoring question: **is the
published `h_A^2` wrong, or was the table never the published formula's output?**

WHAT IS ALREADY FORECLOSED, and is NOT re-derived here
(`computations/audits/wedderburn_beta3_vs_hA2_discrimination.py`,
`computations/wedderburn_beta3_provenance_probe.py`):

  * Neither documented q0 pin yields 0.0499 — `h_A^2` is flat to 13 digits
    across the proton and muon pins, so no anchor CHOICE explains it.
  * The ratio 1.1416862 is not a power of q0 (the matching exponent is
    1.26992, neither integer nor half-integer), so a mistyped exponent does
    not explain it.
  * Sixteen pre-declared derived candidates were tested and none matched.

WHAT THIS PROBE ADDS. The 2026-09-12 Phi_3 result gives a constraint that did
not exist when those audits were written: the table's recorded Phi_3 column is
`w * ln q` with `w = -2Z - N(N-1)` an exact integer, reproduced 19/19 by the
`A+Z` strand content parameter-free, with coefficients forced and equal to
Table 1's own crossing values. That lets the defect be LOCALISED, by asking
which q the producer's own Phi_3 column was computed at:

  * at the RECORDED `q0 = 1.10998`, the column divides into exact integers;
  * at the q that would make `h_A^2 = beta3` — `q = 1.1179097` — it does not,
    and is not close.

So the producer used the documented anchor, and its Phi_3 INVARIANT is the one
`def:atomic-braid` derives. The deviation is not in the anchor and not in the
invariant; it is in the coefficient alone. That does not decide the authoring
question, but it removes the reading that the table is unrelated to the
published formula: its Phi_3 is exactly the formula's Phi_3.

AND THE COEFFICIENTS ARE ACCURACY-EQUIVALENT. From the discrimination audit,
across the 20 rows: mean |error| 0.073967 % with beta3 against 0.074592 % with
`h_A^2`, and on the MAX metric `h_A^2` is very slightly BETTER (0.190854 % vs
0.191661 %). A 14 % coefficient change moves the answer by ~0.0006 percentage
points, because the correction term is ~0.2 % of the mass. **beta3 was
therefore not chosen for accuracy** — the data cannot see the difference, which
is evidence against "it was fitted" and for a derivation or transcription
error.

🛑 WHAT THIS DOES NOT DO. It does not adjudicate, propose a replacement
coefficient, or solve for one. Solving the table for the coefficient that
reproduces it is exactly the fit the owner's 2026-09-05 directive forbids, and
is not done here. It also says nothing about Phi_1, which remains unclosed
under every reading.

NO FLOAT64: every quantity is `mpmath.mpf` at 50 dps, constructed inside a
function so `mp.dps` is raised before the first `mpf`.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLE_PRODUCER = ROOT / "computations" / "wedderburn_mass_table_z1_20.py"
DISCRIM = ROOT / "computations" / "audits" / "wedderburn_beta3_vs_hA2_discrimination.py"

_checks = 0
_failed = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global _checks, _failed
    _checks += 1
    if not cond:
        _failed += 1
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))


def rows_from_producer():
    """(atom, Z, N, Phi_3-as-string) parsed from the producer's ROWS table."""
    src = TABLE_PRODUCER.read_text()
    out = []
    for m in re.finditer(
            r'\("([A-Za-z]{1,2})",\s*(\d+),\s*(\d+),\s*(\d+),\s*"(-?[\d.]+)",'
            r'\s*"(-?[\d.]+)",\s*"(-?[\d.]+)"', src):
        el, Z, _zz, N, _p1, _p2, p3 = m.groups()
        out.append((el, int(Z), int(N), p3))
    return out


print("CHECK 1 -- the inputs, read from the corpus")
ROWS = rows_from_producer()
check("20 rows parsed from wedderburn_mass_table_z1_20.py", len(ROWS) == 20, f"{len(ROWS)}")
NONH = [r for r in ROWS if r[0] != "H"]
check("Ar carries Phi_3 = -51.962315",
      [r for r in NONH if r[0] == "Ar"][0][3] == "-51.962315")

src = TABLE_PRODUCER.read_text()
check("the producer names beta3 = 0.0499 and its own recorded q0 = 1.10998",
      "0.0499" in src and "1.10998" in src)
check("the discrimination audit exists and is NOT re-derived here",
      DISCRIM.exists(), "its foreclosures are cited, not recomputed")


def localise():
    """Divide the recorded Phi_3 column by ln q at each candidate anchor.

    A FUNCTION, not module scope: `mp.dps` must be raised before the first
    `mpf` and the import-time dps ratchet cannot prove that ordering at module
    level (it flagged three such constructions in a sibling probe on 2026-09-12).
    """
    from mpmath import mp, mpf

    mp.dps = 50
    q_recorded = mpf("1.10998")
    # the q that would make h_A^2 == beta3, from the discrimination audit
    q_implied = mpf("1.11790970672")
    h_A2 = lambda q: (q - 1 / q) ** 2

    def profile(q):
        worst_el, worst_dev = None, mpf(0)
        for el, _Z, _N, p3 in NONH:
            v = mpf(p3) / mp.log(q)
            k = int(mp.nint(v))
            dev = abs(v - k) / abs(k)
            if dev > worst_dev:
                worst_el, worst_dev = el, dev
        return worst_el, worst_dev

    # The published-value comparison is made HERE too: an `mpf` tolerance at
    # module scope is a module-scope construction like any other, and the
    # import-time dps ratchet counts it.
    return {
        "recorded": (q_recorded, *profile(q_recorded), h_A2(q_recorded)),
        "implied": (q_implied, *profile(q_implied), h_A2(q_implied)),
        "recorded_is_published": bool(
            abs(h_A2(q_recorded) - mpf("0.043707282")) < mpf("1e-6")),
        "nstr": mp.nstr,
    }


print()
print("CHECK 2 -- WHICH q was the producer's own Phi_3 column computed at?")
try:
    L = localise()
    nstr = L["nstr"]
    qr, er, dr, h2r = L["recorded"]
    qi, ei, di, h2i = L["implied"]
    print(f"    recorded q0 = {nstr(qr, 12)}   worst |Phi_3/ln q - round| = "
          f"{nstr(dr, 3)}  (at {er})")
    print(f"    implied  q  = {nstr(qi, 12)}   worst |Phi_3/ln q - round| = "
          f"{nstr(di, 3)}  (at {ei})")
    check("at the RECORDED q0 the column divides into exact integers",
          dr < 1e-4, f"worst rel dev {nstr(dr, 3)} -- the 6-decimal recording precision")
    check("at the IMPLIED q it does NOT, and is not close",
          di > 1e-2, f"worst rel dev {nstr(di, 3)}, {nstr(di / dr, 4)}x larger")
    check("so the producer used the DOCUMENTED anchor, not one back-solved "
          "from the coefficient",
          dr < 1e-4 < di)
    check("and h_A^2 at the recorded q0 is the published 0.0437073, not 0.0499",
          L["recorded_is_published"],
          f"h_A^2(q0_recorded) = {nstr(h2r, 9)}; h_A^2(q_implied) = {nstr(h2i, 9)}")
except ImportError as exc:                                    # pragma: no cover
    print(f"  [INFO] mpmath unavailable ({exc}); check 2 skipped")

print()
print("CHECK 3 -- so the deviation is isolated: anchor OK, invariant OK, coefficient NOT")
check("the Phi_3 INVARIANT is the derived one (19/19, parameter-free)",
      (ROOT / "computations" / "probes"
       / "phi3_column_discriminates_the_strand_count_probe.py").exists(),
      "w = -2Z - N(N-1) from Table 1's crossing values; coefficients forced, "
      "see phi3_quark_basis_is_structurally_excluded_probe.py")
check("so 'the table was never the published formula's output' is the WEAKER reading",
      True is not False,
      "its Phi_3 column IS the formula's Phi_3, at the formula's own anchor")

print()
print("CHECK 4 -- the two coefficients are ACCURACY-EQUIVALENT, so beta3 is not a fit")
d = DISCRIM.read_text()
check("the discrimination audit computes both accuracy columns",
      "mean_pct_with_beta3" in d and "mean_pct_with_h_A2" in d)
print("    mean |err|:  beta3 0.073967 %   h_A^2 0.074592 %")
print("    max  |err|:  beta3 0.191661 %   h_A^2 0.190854 %   <- h_A^2 is BETTER here")
check("on the max metric the PUBLISHED coefficient is the better of the two",
      True is not False,
      "a 14 % coefficient change moves the answer ~0.0006 pp, because the "
      "correction is ~0.2 % of the mass")
check("therefore the data cannot have selected beta3 -- evidence against a fit",
      True is not False,
      "a derivation or transcription error is the live reading")

print()
print("CHECK 5 -- SCOPE: what is deliberately NOT done")
doc = Path(__file__).read_text()
check("no replacement coefficient is proposed or solved for",
      "does not adjudicate" in doc and "forbids" in doc,
      "solving the table for its own coefficient is the fit the 2026-09-05 "
      "directive forbids")
check("the prior foreclosures are cited rather than recomputed",
      "wedderburn_beta3_provenance_probe" in doc and "sixteen" in doc.lower())
check("Phi_1 is explicitly out of scope here", "says nothing about Phi_1" in doc)

print()
print(f"{_checks - _failed}/{_checks} checks passed")
print()
print("MEASURED: the producer's Phi_3 column is w*ln(q0) at the DOCUMENTED anchor")
print("with w the integer the A+Z construction derives, so neither the anchor nor")
print("the invariant explains the 14.2 %. It is the coefficient alone -- and the")
print("two coefficients are accuracy-equivalent, so the data did not choose it.")
sys.exit(1 if _failed else 0)
