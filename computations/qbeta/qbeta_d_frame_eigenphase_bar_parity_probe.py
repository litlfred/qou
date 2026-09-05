#!/usr/bin/env python3
"""
The D-frame ladder eigenphase is not bar-odd — the defect is exactly h²/2.

Formalize-first step for bean `qou-cds1` (S1: re-derive the Q_β `c_k` ladder
under convention D). Per that bean's discipline note: *state the structural
constraint the D-frame ladder must satisfy and check whether it prunes the
class, BEFORE any wide numerical re-fit.* This probe is that step. It runs no
search and fits nothing.

THE CONSTRAINT (symbolically exact; Lean `QOU.QBeta`
`eigenphase_barOdd_of_barEven` / `eigenphase_bar_defect_of_fullBar`,
sorry-free, `MarkovZFullBarCondition.lean`)
-----------------------------------------------------------------------
The ladder's N=1 factor is `cos(α − b·ℏ_q²/2)` with the single-wrap eigenphase
`α = (z − 1)·h/2` (`QBetaCategoricalPrecisionLadder.alpha`). Every bar-parity
statement in the `c_k` record — (H1) `c₃^even = −Vol(4₁)`, the `S_leak`
program, `q*_S`, KC13's prune — sits downstream of `eigenphase_bar_involution`,
i.e. of `α` being bar-ODD.

Since `bar(h) = −h` always, the eigenphase's bar parity is decided entirely by
`z`:

  * `bar(z) = z`      (bar-EVEN — convention C's `z_C`)   ⟹  `bar(α) + α = 0`
  * `bar(z) = z − h`  (full-bar — convention D's `z_D`)   ⟹  `bar(α) + α = h²/2`

So under D the eigenphase is not bar-odd, and the failure is not a small
perturbation: it is an exact, `z`-independent remainder. EVERY parameter
satisfying the full-bar condition carries the same defect, so no choice inside
that family restores bar-oddness. `eigenphase_bar_involution` is a
CONVENTION-C statement.

THE DERIVED CORRECTION, AND WHAT IT DOES NOT DO
-----------------------------------------------
Because the defect is exact, the bar-odd projection of the D-frame eigenphase
is forced with no free parameter: `bar(α) = h²/2 − α`, so

    α_odd = (α − bar(α))/2 = α − h²/4.

Measured below, that correction moves the D-frame extraction a long way toward
the C-frame numbers — implied `c₂` from −9.30 to −1.73 against the proved −1,
`c₃` from −974 to −86, rung gain 1.12× to 2.36× — but it does NOT reach them
(C: −1.018, −2.069, 57.7×).

**Scope-(a).** The bar-odd projection is a NECESSARY correction and it is
derived, but it is not sufficient: it does not by itself reconstruct the
D-frame ladder. Nothing here is wired, no `c_k` value changes, and no tier
changes. In particular this does NOT license searching for further corrections
until something lands near −1 — that would be a fit, and the anti-laundering
rule applies unchanged.

WHAT REMAINS OPEN (named, not hand-waved)
-----------------------------------------
The Wenzl weight-vanishing lemma landed 2026-08-16 (`WenzlWeightVanishing.lean`,
sorry-free for all `n`; `z_D` is Wenzl level `r = 2` exactly) supplies the
two-row cap that
`qbeta_c3_ladder_trace_convention_sensitivity_probe` named as its own open
item: under D the `≥3`-row blocks are annihilated, so `χ_(1,1,1)` drops from
the `H₃(q)` decomposition. That change is NOT folded in here — the ladder as
written exposes `z` only through `α`, not through the per-block characters, so
folding it in means going back to where the `(z−1)h/2` form is derived. That is
the remaining piece of `qou-cds1`.

Usage:
    python3 computations/qbeta/qbeta_d_frame_eigenphase_bar_parity_probe.py

Output:
    computations/qbeta/qbeta-d-frame-eigenphase-bar-parity.witness.json
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))


def _repo_head_sha() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE),
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return "unknown"


# ── The structural claim, symbolically exact ─────────────────────────────

def bar_parity_defects() -> dict:
    """`bar(α) + α` for the C and D parameters. Zero iff `α` is bar-odd."""
    q = sp.Symbol("q", positive=True)
    h = q - 1 / q

    def bar(e):
        return sp.simplify(e.subs(q, 1 / q))

    z_c = sp.sqrt(q) / (1 + q)
    z_d = q ** 3 / (q ** 2 + 1)

    out = {
        "bar_h_plus_h": str(sp.simplify(bar(h) + h)),
        "bar_zC_minus_zC": str(sp.simplify(bar(z_c) - z_c)),
        "bar_zD_minus_fullbar": str(sp.simplify(bar(z_d) - (z_d - h))),
    }
    for lab, z in (("C", z_c), ("D", z_d)):
        alpha = (z - 1) * h / 2
        out[f"bar_alpha_plus_alpha_{lab}"] = str(
            sp.factor(sp.simplify(bar(alpha) + alpha))
        )
    out["h_squared_over_2"] = str(sp.factor(sp.simplify(h ** 2 / 2)))
    return out


# ── The measured consequence for the ladder ──────────────────────────────

def ladder(q: mp.mpf, alpha: mp.mpf) -> dict:
    """Implied `c₂`, `c₃` and rung gain for a given eigenphase.

    Mirrors `qbeta_utils.substrate_ladder_quantities` + `c3_target_at`, with
    the eigenphase passed in rather than built from a hardwired `z`.
    """
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    q_a = ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    q_n1 = q_a * mp.cos(alpha - b * hbar ** 2 / 2)
    q_n2 = q_n1 * (1 - u ** 2)
    r1 = QCOD / q_n1 - 1
    r2 = QCOD / q_n2 - 1
    return {
        "c2_implied": r1 / u ** 2,
        "c3": r2 / u ** 3,
        "rung_gain": mp.fabs(r1 / r2),
    }


def frames(q: mp.mpf) -> dict:
    h = q - 1 / q
    z_c = mp.sqrt(q) / (1 + q)
    z_d = q ** 3 / (q ** 2 + 1)
    return {
        "C_alpha_C": (z_c - 1) * h / 2,
        "D_z_swap": (z_d - 1) * h / 2,
        "D_bar_odd_projection": (z_d - 1) * h / 2 - h ** 2 / 4,
    }


def main() -> int:
    t0 = time.monotonic()

    sym = bar_parity_defects()
    defect_is_exact = (
        sp.simplify(sp.sympify(sym["bar_alpha_plus_alpha_D"])
                    - sp.sympify(sym["h_squared_over_2"])) == 0
    )
    c_is_bar_odd = sp.sympify(sym["bar_alpha_plus_alpha_C"]) == 0

    print("=== D-frame ladder eigenphase: bar parity ===")
    print(f"  bar(h) + h                 = {sym['bar_h_plus_h']}")
    print(f"  bar(z_C) - z_C             = {sym['bar_zC_minus_zC']}   (C bar-EVEN)")
    print(f"  bar(z_D) - (z_D - h)       = {sym['bar_zD_minus_fullbar']}   (D full-bar)")
    print(f"  C:  bar(alpha) + alpha     = {sym['bar_alpha_plus_alpha_C']}")
    print(f"  D:  bar(alpha) + alpha     = {sym['bar_alpha_plus_alpha_D']}")
    print(f"      h^2/2                  = {sym['h_squared_over_2']}")
    print()

    measured = {}
    for anchor_label, q_val in (("proton", q_at()), ("muon", q_muon_at())):
        q = mp.mpf(str(q_val))
        print(f"=== {anchor_label} anchor, q0 = {mp.nstr(q, 16)}")
        print(f"  {'frame':32s} {'implied c2':>13s} {'c3':>13s} {'rung gain':>11s}")
        rows = {}
        for lab, alpha in frames(q).items():
            r = ladder(q, alpha)
            rows[lab] = {k: mp.nstr(v, 12) for k, v in r.items()}
            print(f"  {lab:32s} {mp.nstr(r['c2_implied'], 7):>13s} "
                  f"{mp.nstr(r['c3'], 7):>13s} {mp.nstr(r['rung_gain'], 5):>11s}")
        measured[anchor_label] = rows
        print()

    assertions = [
        {
            "name": "1_C_eigenphase_is_bar_odd",
            "passed": bool(c_is_bar_odd),
            "detail": "bar(alpha)+alpha = 0 under convention C "
                      "(z_C bar-even) — eigenphase_bar_involution holds",
        },
        {
            "name": "2_D_eigenphase_defect_is_exactly_h_squared_over_2",
            "passed": bool(defect_is_exact),
            "detail": f"bar(alpha)+alpha = {sym['bar_alpha_plus_alpha_D']} "
                      "under convention D — not bar-odd",
        },
    ]
    all_passed = all(a["passed"] for a in assertions)

    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-d-frame-eigenphase-bar-parity",
        "description": "The Q_beta ladder eigenphase alpha = (z-1)h/2 is bar-odd "
                       "exactly when z is bar-even. Under convention C it is; under "
                       "convention D (full-bar, bar(z) = z - h) it is not, with an "
                       "exact z-independent defect bar(alpha)+alpha = h^2/2. So "
                       "eigenphase_bar_involution — which every bar-parity fact in "
                       "the c_k record sits downstream of — is a convention-C "
                       "statement. The forced bar-odd projection alpha - h^2/4 "
                       "improves the D-frame extraction substantially but does NOT "
                       "restore the C-frame numbers: necessary, not sufficient.",
        "audit_only": True,
        "tier": "symbolic-exact (structural claim) + numeric (measured consequence)",
        "scope": "scope-(a). Nothing wired; no c_k value or tier changes. This does "
                 "NOT license searching for further corrections until one lands near "
                 "the proved c_2 = -1 — that would be a fit.",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _repo_head_sha(),
        "engine": "sympy+mpmath",
        "engineVersion": f"sympy {sp.__version__}, mpmath {mp.__version__}",
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "symbolic": sym,
            "measured_ladder": measured,
            "derived_correction": "alpha_odd = alpha - h^2/4 (bar-odd projection; "
                                  "no free parameter)",
            "verdict": "The C->D move cannot be a z-substitution: swapping z into "
                       "the C-frame alpha keeps the formula while breaking the bar "
                       "parity its downstream consumers assume. The bar-odd "
                       "projection is the forced correction and is insufficient "
                       "alone; the two-row (Wenzl level r=2) cap is not folded in "
                       "here and is the remaining piece of qou-cds1.",
        },
        "context": {
            "lean": "QOU.QBeta.eigenphase_barOdd_of_barEven, "
                    "QOU.QBeta.eigenphase_bar_defect_of_fullBar "
                    "(MarkovZFullBarCondition.lean, sorry-free)",
            "bean": "qou-cds1",
            "open_input_now_available": "WenzlWeightVanishing.lean (2026-08-16) — "
                                        "z_D is Wenzl level r=2, >=3-row blocks "
                                        "annihilated for all n",
            "flip_flop_guard": "registry section 8 — no c_k wired",
        },
    }

    out = os.path.join(HERE, "qbeta-d-frame-eigenphase-bar-parity.witness.json")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w", encoding="utf-8") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"witness -> {out}")
    print(f"allPassed: {all_passed}  ({int((time.monotonic() - t0) * 1000)} ms)")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
