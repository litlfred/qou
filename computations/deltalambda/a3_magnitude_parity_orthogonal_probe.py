#!/usr/bin/env python3
"""Does the conjugation-parity structure constrain the A=3 (Borromean) magnitude? NO — parity is a
RELABELING, not a rescaling; the ~1.6× coefficient gap is orthogonal to it. An honest scope-(a)
negative that closes the "use parity for the magnitude" route. Forward, no fit.

CONTEXT: GAP-1 (#4399) narrowed the Δ_λ WEIGHT class via conjugation parity (symmetric Δ_λ excluded
for even A ⇒ principal specialization survives). Natural follow-up (owner "1"): can the same parity
structure constrain the standing A=3 MAGNITUDE gap — c₃ = E₀(1−τ_Borr) = 0.63×μ₃ (μ₃=+0.4708), a
~1.6× near-miss (option-e ledger; #4364)? This probe answers it: NO.

THE n=9 (BORROMEAN, A=3) CONJUGATION STRUCTURE (exact):
  30 partitions of 9 = 14 conjugate pairs + 2 self-conjugate {(5,1,1,1,1), (3,3,3)}.
  sgn = (−1)^{n-1} = (−1)^8 = +1 (n=9) — OPPOSITE parity regime from the deuteron (n=6, sgn=−1). So at
  A=3 the self-conjugate blocks feed the bar-EVEN channel, and (unlike even A) a conjugation-symmetric
  Δ_λ is NOT excluded (bar-even total = Σ T_λ(Δ_λ+Δ_{λ'}) ≠ 0). GAP-1 gives no exclusion here.

WHY PARITY DOES NOT TOUCH THE MAGNITUDE (two independent reasons):
  R1. Parity is a RELABELING, not a rescaling. The signed parity map T_λ(q⁻¹)=(−1)^{n-1}T_{λ'}(q) sorts
      the H₉ Wedderburn terms into bar-even/bar-odd channels; each partition still contributes its FULL
      derived amount. Parity fixes WHICH channel a term lands in, never HOW BIG it is. So it supplies
      no coefficient — the ~1.6× cannot come from parity.
  R2. The A=3 gap lives at the BARE-TRACE level, not the Δ_λ-dressing level. c₃ = E₀(1−τ_Borr) is a
      SINGLE Markov trace with a proved closed form (1−τ_Borr = h⁴(3+h²)/(h²+4), magnitude 0.297); the
      Δ_λ per-partition dressing (where conjugation parity acts) is a different, downstream object. The
      c₃ vs μ₃ gap is a property of the bare trace, which the Δ_λ parity structure does not enter.

VERDICT (scope-(a), honest negative): the conjugation-parity structure is ORTHOGONAL to the A=3
magnitude. It narrows the WEIGHT class (GAP-1) but cannot supply the ~1.6× coefficient — that remains
the standing Track-A magnitude gate (the derived c₃=0.297 vs μ₃=+0.4708). This closes the "use parity
for the magnitude" route so future sessions do not re-try it.

EXPLORATORY — audit + witness only; no fit, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
from sympy.utilities.iterables import partitions

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was a hardcoded PROTON
# literal -- the right VALUE by the wrong MECHANISM: it cannot follow the
# anchor, and it is invisible to the retired-pin drain because it never
# matched. Spellings across this family ran 13 to 60 digits for one pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()


def conj(p):
    m = max(p)
    return tuple(sum(1 for x in p if x >= k) for k in range(1, m + 1))


def main() -> int:
    parts = []
    for pd in partitions(9):
        lam = []
        for part, mult in sorted(pd.items(), reverse=True):
            lam += [part] * mult
        parts.append(tuple(lam))
    self_conj = [p for p in parts if conj(p) == p]
    seen, pairs = set(), []
    for p in parts:
        if p in seen:
            continue
        seen.add(p)
        c = conj(p)
        if c != p:
            pairs.append((p, c))
            seen.add(c)

    n = 9
    sgn = (-1) ** (n - 1)

    # the bare-trace A=3 magnitude (proved closed form) — for context, at the
    # PROTON q₀. (This comment said 'muon-canonical' until 2026-09-04, one line
    # above the call that reads `Q_50_DIGIT_STR`, which for this stem — not in
    # `ideal_muon` — resolves to the proton pin; bean qou-9ugp.)
    q0 = Q_MP
    h = q0 - 1 / q0
    deficit = h ** 4 * (3 + h ** 2) / (h ** 2 + 4)          # 1 − τ_Borr (dimensionless)

    result = {
        "n9_conjugation_structure": {
            "n_partitions": len(parts),
            "n_conjugate_pairs": len(pairs),
            "self_conjugate": [list(p) for p in self_conj],
            "sgn": int(sgn),
            "meaning": "n=9 ⇒ sgn=+1 (opposite of deuteron n=6): self-conjugate feeds bar-EVEN, and "
                       "a conjugation-symmetric Δ_λ is NOT excluded (GAP-1 gives no exclusion at A=3).",
        },
        "R1_parity_is_relabeling_not_rescaling": {
            "statement": "the signed parity map sorts terms into channels; each partition contributes "
                         "its full derived amount. Parity fixes the channel, never the magnitude ⇒ no "
                         "coefficient, so the ~1.6× cannot come from parity.",
        },
        "R2_gap_is_bare_trace_level": {
            "c3": "E₀(1−τ_Borr); 1−τ_Borr = h⁴(3+h²)/(h²+4) (proved closed form)",
            "deficit_dimensionless_at_q0": mp.nstr(deficit, 8),
            "statement": "the A=3 gap (c₃=0.63×μ₃, μ₃=+0.4708) is a property of the BARE single Markov "
                         "trace; the Δ_λ per-partition dressing (where conjugation parity acts) is a "
                         "different downstream object the gap does not enter.",
        },
        "verdict": {
            "classification": "scope-(a) honest negative: conjugation parity is ORTHOGONAL to the A=3 "
                              "magnitude — it narrows the weight class (GAP-1) but supplies no "
                              "coefficient. The ~1.6× remains the standing Track-A magnitude gate.",
            "closes_route": "using parity to constrain the A=3 magnitude — do not re-try.",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "a3-magnitude-parity-orthogonal",
        "description": ("Does conjugation parity constrain the A=3 (Borromean) magnitude gap "
                        "(c₃=0.63×μ₃, ~1.6× near-miss)? NO. The n=9 structure is 30 partitions = 14 "
                        "conjugate pairs + 2 self-conjugate {(5,1,1,1,1),(3,3,3)}, sgn=+1 (opposite of "
                        "the deuteron; self-conjugate feeds bar-even, symmetric Δ_λ NOT excluded). Two "
                        "reasons parity cannot touch the magnitude: (R1) parity is a RELABELING not a "
                        "rescaling — it sorts terms into channels but each contributes its full derived "
                        "amount, so it supplies no coefficient; (R2) the gap lives at the BARE single-"
                        "trace level (1−τ_Borr=h⁴(3+h²)/(h²+4), proved) not the Δ_λ-dressing level where "
                        "parity acts. VERDICT (scope-a negative): conjugation parity is orthogonal to "
                        "the A=3 magnitude — it narrows the weight class (GAP-1) but cannot supply the "
                        "~1.6×; the magnitude stays the Track-A gate. Closes the route. scope-(a), "
                        "audit-only, nothing wired; no fit."),
        "audit_only": True,
        "tier": "scope-(a) honest negative (exact n=9 structure + two orthogonality arguments); no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — A=3 magnitude gate vs the conjugation-parity structure",
            "builds_on": "#4399 GAP-1 (weight-class exclusion), option-e ledger (A=3 magnitude, μ₃)",
            "q0_convention": "proton (experimental / Physical-Observations pin; owner directive 2026-08-07). Corrected from 'muon-canonical (computations/ layer)' on 2026-09-04, bean qou-9ugp: the label named a layer this producer does not evaluate at.",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "a3-magnitude-parity-orthogonal", payload,
        script_path=__file__, engine="sympy+mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("n9_structure_14pairs_2selfconj",
                     computed=f"{len(pairs)}pairs+{len(self_conj)}sc", expected="14pairs+2sc")
    wb.add_assertion("sgn_plus_one_at_n9", computed=str(int(sgn)), expected="1")
    out = wb.save(extra={"auditOnly": True})

    print("=== Does conjugation parity constrain the A=3 magnitude? NO (orthogonal) ===")
    print(f"n=9: {len(parts)} partitions = {len(pairs)} conjugate pairs + {len(self_conj)} self-conjugate "
          f"{[list(p) for p in self_conj]}; sgn={int(sgn)} (self-conj → bar-even; symmetric Δ NOT excluded)")
    print("R1: parity RELABELS terms into channels, does NOT rescale ⇒ supplies no coefficient (~1.6× ∉ parity).")
    print("R2: the c₃ gap is at the BARE single-trace level (1−τ_Borr closed form), not the Δ_λ-dressing level.")
    print("VERDICT (scope-a negative): conjugation parity is ORTHOGONAL to the A=3 magnitude; it narrows the")
    print("  weight class (GAP-1) but cannot supply the ~1.6×. The magnitude stays the Track-A gate. Route closed.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
