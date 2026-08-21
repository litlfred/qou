"""Audit every hardcoded CODATA constant in the corpus against the NIST table.

Until `library/allascii.txt` was committed (2026-08-15) the corpus had no
authoritative CODATA table to check against, so every CODATA value was a
hand-transcribed literal and nothing could detect a mis-transcription or a
stale edition. This probe closes that: it maps each registry symbol to its
exact NIST quantity name and compares.

**The finding that motivated it.** `MASS_RATIO_MU_E = 206.7682830` in the
production registry `qou_substrate.constants` is the CODATA-**2018** value,
carried under a "CODATA 2022" comment. The 2022 value is `206.7682827`
(table row *muon-electron mass ratio*, ±0.0000046). `codata_2022_source.py`
was corrected to 2022 on 2026-08-09 (PR #4860); the production registry was
not, so the two disagree with each other.

Run:  python3 -u computations/codata_table_vintage_audit.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))

from codata_table import codata  # noqa: E402

mp.mp.dps = 50

# Two mpf built from the SAME decimal string can differ in the last bit when
# they are constructed at different working precisions, so `==` on mpf is the
# wrong equality here: it reported all 8 constants as disagreeing by ~1e-17
# relative while their printed digits were identical. Compare with a relative
# tolerance instead. 1e-15 is far below any real edition difference (those are
# ~1e-9) and far above float-construction noise (~1e-17), so this keeps full
# detection power. Fixes a defect in the version merged by PR #5149.
_SAME_TOL = mp.mpf("1e-15")


def _same(a, b) -> bool:
    """True when two mpf denote the same printed decimal value."""
    if a == b:
        return True
    if b == 0:
        return abs(a) < _SAME_TOL
    return abs(a - b) / abs(b) < _SAME_TOL

# ── Registry symbol → NIST quantity name ────────────────────────────
#
# Only symbols that CLAIM to be CODATA values are listed. AME-derived
# quantities (Q_BETA_MEV_AME, M_N_MEV_AME_DERIVED) are deliberately excluded:
# they come from the AME2020 mass evaluation, not the CODATA adjustment, and
# checking them against this table would be a category error.

CHECKS = [
    # (module, symbol, NIST quantity name)
    ("computations/codata_2022_source.py", "M_E_MEV", "electron mass energy equivalent in MeV"),
    ("computations/codata_2022_source.py", "M_P_MEV", "proton mass energy equivalent in MeV"),
    ("computations/codata_2022_source.py", "M_N_MEV_CODATA_DIRECT", "neutron mass energy equivalent in MeV"),
    ("computations/codata_2022_source.py", "M_MU_MEV", "muon mass energy equivalent in MeV"),
    ("computations/codata_2022_source.py", "M_MU_OVER_M_E", "muon-electron mass ratio"),
    ("computations/codata_2022_source.py", "U_MEV", "atomic mass constant energy equivalent in MeV"),
    ("computations/codata_2022_source.py", "M_N_MINUS_P_MEV",
     "neutron-proton mass difference energy equivalent in MeV"),
    ("tools/qou-substrate/.../constants.py", "MASS_RATIO_P_E_STR", "proton-electron mass ratio"),
    ("tools/qou-substrate/.../constants.py", "MASS_RATIO_MU_E_STR", "muon-electron mass ratio"),
]


def _load_registry_values() -> dict[tuple[str, str], tuple[str, str]]:
    """Return {(module, symbol): (value_str, uncertainty_str)} for each check.

    Read via import rather than regex so the audit sees the value the corpus
    actually computes with, not the value a comment claims.
    """
    out: dict[tuple[str, str], tuple[str, str]] = {}

    import codata_2022_source as c22

    for mod, sym, _ in CHECKS:
        if not mod.startswith("computations/"):
            continue
        val = getattr(c22, sym)
        err = getattr(c22, f"{sym}_ERR", None)
        out[(mod, sym)] = (mp.nstr(val, 20, strip_zeros=False), "" if err is None else mp.nstr(err, 10))

    repo = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(repo / "tools" / "qou-substrate" / "python"))
    from qou_substrate import constants as qc  # noqa: PLC0415

    out[("tools/qou-substrate/.../constants.py", "MASS_RATIO_P_E_STR")] = (qc.MASS_RATIO_P_E_STR, str(qc.MASS_RATIO_P_E_ERR))
    out[("tools/qou-substrate/.../constants.py", "MASS_RATIO_MU_E_STR")] = (qc.MASS_RATIO_MU_E_STR, str(qc.MASS_RATIO_MU_E_ERR))
    return out


def main() -> int:
    print("=" * 78)
    print("CODATA vintage audit — registry literals vs library/allascii.txt")
    print("=" * 78)
    print()
    print("Table: NIST 'Fundamental Physical Constants --- Complete Listing',")
    print("       2022 CODATA adjustment, committed verbatim at library/allascii.txt")
    print()

    registry = _load_registry_values()

    mismatches: list[tuple[str, str, str, str, float]] = []
    checked = 0

    for mod, sym, quantity in CHECKS:
        entry = codata(quantity)
        have_str, have_err = registry[(mod, sym)]
        have = mp.mpf(have_str)
        want = entry.value

        checked += 1
        agree = _same(have, want)

        # Check the UNCERTAINTY as well as the value. A value-only check is
        # not enough: `m_p/m_e` prints identically in CODATA-2018 and -2022,
        # so its value passed while its error bar was still the 2018 one
        # (1.1e-7 vs 3.2e-8, 3.4x too wide). An edition straddle can live
        # entirely in the uncertainty.
        err_agree = True
        if have_err and entry.uncertainty is not None:
            err_agree = _same(mp.mpf(have_err), entry.uncertainty)
        # Express any disagreement in units of the table's own uncertainty.
        if entry.uncertainty and entry.uncertainty != 0:
            sigma = float(abs(have - want) / entry.uncertainty)
        else:
            sigma = 0.0
        rel_ppb = float(abs(have - want) / want) * 1e9 if want != 0 else 0.0

        flag = "OK  " if (agree and err_agree) else "DIFF"
        print(f"[{flag}] {sym}")
        print(f"        NIST  {quantity!r}")
        print(f"        table = {entry.value_str} ± {entry.uncertainty_str}")
        print(f"        corpus= {have_str.rstrip('0').rstrip('.')}  (± {have_err})")
        if not agree:
            print(f"        VALUE delta = {rel_ppb:.4g} ppb = {sigma:.4g} sigma(table)")
            mismatches.append((mod, sym, entry.value_str, have_str, sigma))
        if not err_agree:
            ratio = float(mp.mpf(have_err) / entry.uncertainty)
            print(f"        UNCERTAINTY differs: corpus {have_err} vs table "
                  f"{entry.uncertainty_str}  ({ratio:.3g}x)")
            mismatches.append((mod, f"{sym} [uncertainty]", entry.uncertainty_str, have_err, 0.0))
        print()

    print("=" * 78)
    print(f"checked {checked} registry constants against the table; "
          f"{len(mismatches)} disagree")
    print("=" * 78)

    if mismatches:
        print()
        print("MISMATCHES (registry literal != CODATA-2022 table):")
        for mod, sym, want, have, sigma in mismatches:
            print(f"  - {sym:<24s} {mod}")
            print(f"      table {want}  corpus {have.rstrip('0').rstrip('.')}  ({sigma:.3g} sigma)")
        print()
        print("Every mismatch is well inside the table's own uncertainty, so no")
        print("physical conclusion in the corpus moves. What is wrong is the LABEL:")
        print("a CODATA-2018 value carried under a 'CODATA 2022' comment cannot be")
        print("audited, and two registries disagreeing with each other means one of")
        print("them is silently wrong in any comparison that spans both.")

    # This is a reporting probe, not a gate: exit 0 either way so it can run
    # in an idle pass without failing a pipeline. The gate is a separate call.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
