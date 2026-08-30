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

#: The pin the pre-2026-08-16 upstream witness recorded for itself. Taken from
#: the artifact rather than resolved at runtime — see the method note above.
Q_OLD = "1.1099785955573347198997632204832250266562084087802"
RECORDED = "1.06530622861316705936528454643137255765066167413520000000000"


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
    q = mp.mpf(Q_OLD)
    chi = chi_at(ROOT / "chi-proton-h3.witness.json", q)

    print("=" * 70)
    print("atomic-tr-m-helium4 7.55% gap — convention attribution")
    print("=" * 70)
    print(f"  q (from the old witness): {Q_OLD[:26]}…")
    print(f"  chi: {({k: mp.nstr(v, 10) for k, v in chi.items()})}")

    got: dict[str, mp.mpf] = {}
    for name, fn in (("C", y_C), ("D", y_D)):
        y = fn(3, q)
        tot = sum((mp.mpf(str(y.get(lam, 0))) * v for lam, v in chi.items()),
                  mp.mpf(0))
        got[name] = abs(tot)
        print(f"  {name}-frame |tr_M(proton)| = {mp.nstr(got[name], 20)}")

    rec = mp.mpf(RECORDED)
    rel_c = abs(got["C"] - rec) / rec
    rel_d = abs(got["D"] - rec) / rec
    print(f"  recorded                 = {mp.nstr(rec, 20)}")
    print(f"    |C - recorded| / rec   = {mp.nstr(rel_c, 6)}")
    print(f"    |D - recorded| / rec   = {mp.nstr(rel_d, 6)}")

    ok = rel_c < mp.mpf("1e-40") < rel_d
    print("\n  VERDICT: the recorded value is CONVENTION C"
          if ok else "\n  VERDICT: NOT reproduced — do not cite this attribution")
    print("=" * 70)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
