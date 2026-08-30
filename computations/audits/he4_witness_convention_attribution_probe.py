#!/usr/bin/env python3
"""Settle WHY `atomic-tr-m-helium4.witness.json` is 7.55% off: it is convention C.

THE QUESTION.  The committed downstream witness records
`abs_tr_p_50dps = 1.06530622861316705936…` where the live producer computes
`1.14575978228…` — a **7.55 %** gap. The muon-vs-proton pin difference on the
same quantity is **78 ppb**, five orders too small, so the straddle fixed in
PR #6104 does not explain it and must not be reported as doing so.

WHY COMMIT ARCHAEOLOGY COULD NOT ANSWER IT.  The upstream
`atomic-tr-m-mpfr-50dps.witness.json` held the old value until `bd45adff92`
(2026-08-16) and the new one after — but that commit's subject is an unrelated
bean closure touching dozens of files, and it documents no regeneration. And
the producer's own diff across the window is **entirely timing-format**
(`float(t)` → `f"{t:.4f}"`, the float64 drain), i.e. provably math-neutral, so
the change arrived through the **import cone** rather than the producer. That
narrows the cause without naming it: the absence of a commit-message account is
not evidence of a cause.

THE TEST.  `tr_M = Σ_λ y_λ · χ^λ`. The χ are convention-independent; only the
weights `y_λ` change between conventions. So contract the committed symbolic χ
cache against BOTH weight sets at the pin the old witness itself recorded, and
see which one reproduces the recorded number. Convention C is still present as
`schur_principal_mpmath.y_lambda_at_q0_mpmath_convention_C_HISTORICAL`.

RESULT (2026-08-30) — exact, to every digit carried:

    C-frame |tr_M(proton)|   1.0653062286131670594
    recorded pre-2026-08-16  1.0653062286131670594   <- MATCH
    D-frame |tr_M(proton)|   1.1457597822878355047
    current producer         1.1457597823            <- MATCH

So the downstream witness is a **convention-C-era value that was never
regenerated after its upstream moved to D**. Bean `qou-5ll9`.

TWO METHOD NOTES, both of which cost a wrong answer first:

* **Do not read `Q_50_DIGIT_STR` from an ad-hoc script.** It resolves by the
  *running producer's stem*, so a `-c` invocation gets an arbitrary answer.
  This probe takes q from the OLD WITNESS'S OWN `q_0` field, which is the
  value the recorded number was computed at and needs no stem.
* **`Symbol('q', positive=True)` is not the `q` that `sympify` creates.**
  Different assumptions make different symbols, so `.subs()` silently does
  nothing and leaves a polynomial. Substitute the expression's own free symbol.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import _path_bridge  # noqa: F401, E402

import mpmath as mp                                        # noqa: E402
import sympy as sp                                         # noqa: E402
from schur_principal_mpmath import (                       # noqa: E402
    y_lambda_at_q0_mpmath as y_D,
    y_lambda_at_q0_mpmath_convention_C_HISTORICAL as y_C,
)

#: Fallbacks only. Both are READ FROM THE COMMITTED ARTIFACTS at run time by
#: `_q_old()` / `_recorded()` below; these literals are used only when the
#: artifact has moved on, and the run says so when it falls back.
#:
#: Copilot (PR #6104) was right that the docstring claimed these were "taken
#: from the artifact" while they were hardcoded — the claim described the
#: METHOD I used to obtain them, not what the code did, and a probe whose
#: whole subject is values drifting out of sync with their source should not
#: itself be able to drift out of sync with its source.
Q_OLD_FALLBACK = "1.1099785955573347198997632204832250266562084087802"
RECORDED_FALLBACK = "1.06530622861316705936528454643137255765066167413520000000000"


def _q_old() -> tuple[str, str]:
    """The pin recorded by THE SAME ARTIFACT the value under test comes from.

    Taking q from a different witness is a straddle, and this probe committed
    one: reading q from the muon `y-lambda-mpfr-witness.json` while reading
    the value from the (now proton-pinned) He-4 witness left a 7.84e-8
    residual — the μ–p pin gap — in a comparison meant to resolve a 7.55%
    convention gap. Two artifacts, one quantity, and the smaller error hides
    inside the larger one until the larger is fixed. Both now come from the
    same file.
    """
    import json, re                                        # noqa: PLC0415
    f = ROOT / "atomic-tr-m-helium4.witness.json"
    try:
        txt = f.read_text()
        m = re.search(r'"(?:q_0_50dps|q_0|q0Value)":\s*"?(1\.10997[0-9]*)', txt)
        if m:
            return m.group(1), f.name
    except Exception:                                      # noqa: BLE001
        pass
    return Q_OLD_FALLBACK, "FALLBACK LITERAL (artifact unreadable)"


def _recorded() -> tuple[str, str]:
    """The value under test, from the He-4 witness that records it.

    Read live so the probe tracks the corpus. Once that witness is
    regenerated under D this returns the D value and the verdict flips to
    "NOT convention C" — which is the correct report at that point, not a
    failure, and is why the exit code keys on reproduction rather than on C.
    """
    import json, re                                        # noqa: PLC0415
    f = ROOT / "atomic-tr-m-helium4.witness.json"
    try:
        m = re.search(r'"abs_tr_p_50dps":\s*"([0-9.]+)"', f.read_text())
        if m:
            return m.group(1), f.name
    except Exception:                                      # noqa: BLE001
        pass
    return RECORDED_FALLBACK, "FALLBACK LITERAL (artifact unreadable)"


def chi_at(path: Path, q: mp.mpf) -> dict[tuple, mp.mpf]:
    """Committed symbolic χ^λ, evaluated at `q`.

    The cached coefficients are dyadic (0.25, 0.5), so the float spellings in
    the JSON are exact binary fractions and carry no error into this; the
    agreement below is to every digit either side supplies.
    """
    d = json.loads(path.read_text())
    w = d.get("witness", d)
    rows = w.get("chi_lambda_symbolic") or d.get("chi_lambda_symbolic") or []
    qs = sp.Float(str(q), 60)
    out: dict[tuple, mp.mpf] = {}
    for r in rows:
        ex = sp.sympify(r["chi_q_symbolic"])
        fs = list(ex.free_symbols)
        val = ex if not fs else ex.subs(fs[0], qs)
        out[tuple(r["partition"])] = mp.mpf(str(sp.N(val, 55)))
    return out


def main() -> int:
    mp.mp.dps = 60
    q_str, q_src = _q_old()
    rec_str, rec_src = _recorded()
    q = mp.mpf(q_str)
    chi = chi_at(ROOT / "chi-proton-h3.witness.json", q)

    print("=" * 70)
    print("atomic-tr-m-helium4 7.55% gap — convention attribution")
    print("=" * 70)
    print(f"  q        {q_str[:26]}…  <- {q_src}")
    print(f"  recorded {rec_str[:26]}…  <- {rec_src}")
    print(f"  chi: {({k: mp.nstr(v, 10) for k, v in chi.items()})}")

    got: dict[str, mp.mpf] = {}
    for name, fn in (("C", y_C), ("D", y_D)):
        y = fn(3, q)
        tot = sum((mp.mpf(str(y.get(lam, 0))) * v for lam, v in chi.items()),
                  mp.mpf(0))
        got[name] = abs(tot)
        print(f"  {name}-frame |tr_M(proton)| = {mp.nstr(got[name], 20)}")

    rec = mp.mpf(rec_str)
    rel_c = abs(got["C"] - rec) / rec
    rel_d = abs(got["D"] - rec) / rec
    print(f"  recorded                 = {mp.nstr(rec, 20)}")
    print(f"    |C - recorded| / rec   = {mp.nstr(rel_c, 6)}")
    print(f"    |D - recorded| / rec   = {mp.nstr(rel_d, 6)}")

    # Three outcomes, not two. The corpus moves under this probe by design:
    # once the He-4 witness is regenerated under D, "not C" is the CORRECT
    # report, not a failure — so the exit code keys on whether the recorded
    # value is EXPLAINED by one of the two frames, never on it being C.
    TOL = mp.mpf("1e-30")
    if rel_c < TOL:
        print("\n  VERDICT: the recorded value is CONVENTION C"
              "\n           (the artifact is still the stale one)")
        ok = True
    elif rel_d < TOL:
        print("\n  VERDICT: the recorded value is CONVENTION D — the artifact has"
              "\n           been regenerated. The C attribution stands as history:"
              "\n           it is what the value WAS, and this run confirms the"
              "\n           frames are correctly separated at this pin.")
        ok = True
    else:
        print("\n  VERDICT: matches NEITHER frame — do not cite an attribution."
              "\n           A residual this size usually means q and the recorded"
              "\n           value came from DIFFERENT artifacts (a pin straddle in"
              "\n           the probe itself), so check that first.")
        ok = False
    print("=" * 70)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
