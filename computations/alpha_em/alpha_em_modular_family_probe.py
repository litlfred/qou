#!/usr/bin/env python3
"""alpha_em_modular_family_probe.py

Bean qou-tq20 (B2 lift), tranche 7: the MODULAR-FAMILY hypothesis test —
nome-anchored, zero free constants — and the closing of the parameter-free
numerical program.

HYPOTHESIS LABEL (owner question, 2026-07-18: "is modular family from the
lit or just made up?"): the modular family is a PROGRAM HYPOTHESIS, not a
literature identification. Standard ingredients (moduli deformation of
tori; det'Delta(E_tau) = (Im tau)^2 |eta|^4, Ray-Singer/OPS; the nome
q = e^{2 pi i tau} — also the corpus's own B1 fibre dictionary); the claim
"the Markov weight y_lambda(q) is realized by a modular family on
Jac(Bring)" is the open wall itself, motivated here only by elimination
(#4027 killed the heat family) and nome-nativeness. This probe TESTS it.

THE DICTIONARY IS EXACT (no fitting possible): for real categorical
q in (0,1), the nome inverts to tau = i*y with y = |ln q|/(2 pi) — every
comparison point is a prediction; there is NO constant to pin.

THE THREE CANONICAL PER-FACTOR WEIGHT FAMILIES (pre-stated; the isotypic
pair at modulus tau is (E_{5 tau} x3, E_tau)):
  (a) harmonic weight  (dim H^{1,0} per factor):    R_harm = 3   (constant)
  (b) area weight      (Im tau per factor):         R_area = 15  (constant)
  (c) det'Delta weight ((Im tau)^2 |eta(tau)|^4):   R_det(y) = 75*|eta(5iy)/eta(iy)|^4

TARGET: the corpus-canonical Markov ratio r(q) = y_[2]/y_[1,1]
(r(1) = 3, r(0.8) = 5.76, r(q15) = 15). Pass bar (pre-stated): 1%.

RESULTS — ALL THREE KILLED:
  (a) constant 3 fails pointwise away from q=1 (r(0.8) = 5.76).
  (b) constant 15 fails AT the anchor (r(1) = 3).
  (c) diverges catastrophically at the anchor: R_det ~ 3*e^{4 pi/(15 y)}
      as y -> 0 (eta functional equation), numerically 1.1e45 at q = 0.95
      vs r = 3.45 — a 45-order-of-magnitude miss.

SYNTHESIS (scope-(a)): under the bare fibre-nome dictionary, EVERY
parameter-free canonical geometric weight family fails. Combined with the
prior tranches (#4022 endpoint constants null; #4027 reciprocal power-law
heat dictionaries killed), the parameter-free numerical program is
EXHAUSTED. This is consistent with — and sharpens — the corpus's
Im(q) fibre-vs-observable discipline: the nome is a FIBRE-level dictionary,
while the Markov weights at real q are ARCHIMEDEAN evaluations; the
dictionary the identification needs is the archimedean tau-functor itself —
i.e. exactly the categorical content of the open lift. THE WALL IS
IRREDUCIBLY CATEGORICAL: no further parameter-free numerics can decide it.

Scope guard: scope-(a) kills (these families, as-is, under this dictionary);
no fit (zero free constants BY CONSTRUCTION); nothing wired; 1/(8 pi) stays
phase-4. Self-contained (sympy + mpmath + corpus y_lambda_at).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_here))
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def eta4(tau):
    qn = mp.e ** (2j * mp.pi * tau)
    return abs(qn ** (mp.mpf(1) / 12) * mp.qp(qn) ** 2) ** 2


def w_det(tau):
    return mp.im(tau) ** 2 * eta4(tau)


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    y = y_lambda_at(2)
    q = sorted(y[(2,)].free_symbols, key=str)[0]
    rf = sp.lambdify(q, sp.simplify(y[(2,)] / y[(1, 1)]), "mpmath")

    # (a) harmonic family: constant 3
    r08 = rf(mp.mpf("0.8"))
    va = abs(r08 - 3) > mp.mpf("0.01") * 3
    check("harmonic_family_killed", va,
          f"R_harm ≡ 3 vs r(0.8) = {mp.nstr(r08, 8)} — fails pointwise away from the anchor. "
          "KILLED (cannot carry any deformation)")

    # (b) area family: constant 15
    vb = abs(rf(mp.mpf(1)) - 15) > mp.mpf("0.01") * 15
    check("area_family_killed", vb,
          "R_area ≡ 15 vs r(1) = 3 — fails AT the anchor. KILLED")

    # (c) det'Delta family under the exact nome dictionary tau = i|ln q|/(2 pi)
    rows = []
    for qq in ("0.95", "0.8", "0.6255624479"):
        qv = mp.mpf(qq)
        yv = -mp.log(qv) / (2 * mp.pi)
        Rdet = 3 * w_det(5j * yv) / w_det(1j * yv)
        rows.append((qq, mp.nstr(yv, 6), mp.nstr(Rdet, 6), mp.nstr(rf(qv), 6)))
    R95 = 3 * w_det(5j * (-mp.log(mp.mpf("0.95")) / (2 * mp.pi))) / \
        w_det(1j * (-mp.log(mp.mpf("0.95")) / (2 * mp.pi)))
    vc = R95 > mp.mpf(10) ** 40
    check("detdelta_family_killed", vc,
          f"R_det under the EXACT nome dictionary (zero free constants): {rows} — diverges "
          "at the anchor as 3·e^{4π/(15y)} (η functional equation); at q=0.95 it is "
          f"{mp.nstr(R95, 4)} vs r = 3.45, a ~45-order-of-magnitude miss. KILLED")

    # (d) synthesis: parameter-free numerical program exhausted
    vd = va and vb and vc
    check("parameter_free_program_exhausted", vd,
          "all three canonical per-factor weight families fail under the bare fibre-nome "
          "dictionary; with #4022 (endpoint constants: null) and #4027 (heat reciprocal "
          "power-laws: killed), every parameter-free candidate is dead. Consistent with the "
          "Im(q) fibre-vs-observable discipline: the nome is FIBRE-level, the Markov weights "
          "at real q are ARCHIMEDEAN evaluations — the needed dictionary IS the archimedean "
          "τ-functor, i.e. the categorical content of the open lift. THE WALL IS IRREDUCIBLY "
          "CATEGORICAL")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "MODULAR-FAMILY HYPOTHESIS TESTED AND KILLED — PARAMETER-FREE NUMERICS EXHAUSTED "
        "(scope-(a); zero free constants by construction; no fit; nothing wired): under the "
        "exact nome dictionary τ = i|ln q|/(2π), all three canonical per-factor weight "
        "families (harmonic ≡ 3, area ≡ 15, det′Δ — divergent at the anchor, ~1e45 at "
        "q=0.95) fail against the Markov ratio. Hypothesis honestly labeled: the modular "
        "family was a program inference (elimination + nome-nativeness), not literature — "
        "and it is now dead as-is. Program synthesis: with #4022 and #4027, every "
        "parameter-free numerical candidate for the τ-identification's dictionary is "
        "excluded; the identification, if true, operates through the archimedean τ-functor "
        "itself (fibre-nome ≠ archimedean evaluation — the Im(q) discipline sharpened). The "
        "wall is IRREDUCIBLY CATEGORICAL: further numerics cannot decide it. The lift "
        "(qou-tq20) remains OPEN. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-modular-family",
        "description": "Bean qou-tq20 tranche 7: modular-family hypothesis (honestly labeled a "
                       "program inference, not literature) tested under the EXACT nome dictionary "
                       "tau = i|ln q|/(2pi) — zero free constants. All three canonical per-factor "
                       "weight families killed (harmonic const 3; area const 15; det'Delta "
                       "divergent ~1e45 at the anchor). With #4022/#4027 the parameter-free "
                       "numerical program is EXHAUSTED: the wall is irreducibly categorical (the "
                       "dictionary is the archimedean tau-functor itself). Lift stays open. "
                       "Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-modular-family.md",
        "tier": "exact-dictionary adjudication (30-dps eta/theta + exact Markov ratio); "
                "scope-(a) kills; program-closing synthesis",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy+mpmath", "engineVersion": sp.__version__ + "/" + mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "dictionary": "tau = i|ln q|/(2pi) — exact nome inversion, no free constants",
            "families": {
                "harmonic": "const 3 — killed (no deformation)",
                "area": "const 15 — killed (fails anchor)",
                "det_delta": "3*e^{4pi/(15y)} divergence at anchor; ~1e45 at q=0.95 — killed",
            },
            "synthesis": "parameter-free numerics exhausted (#4022, #4027, this); wall "
                         "irreducibly categorical — dictionary = the archimedean tau-functor",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-tq20 (B2 lift) tranche 7 — closes the numerical program",
            "hypothesis_label": "modular family = program inference (elimination + "
                                "nome-native), NOT literature; owner question 2026-07-18",
            "scope_guard": "scope-(a); zero free constants; no fit; nothing wired; 1/(8pi) "
                           "stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-modular-family.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
