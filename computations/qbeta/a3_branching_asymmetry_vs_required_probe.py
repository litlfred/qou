#!/usr/bin/env python3
"""a3_branching_asymmetry_vs_required_probe.py — can the H₃ branching supply the A=3 magnitude?

Companion to `QOU/QBeta/A3BranchingModulusReflection.lean`. The modulus bridge
(`BirkhoffBarOddPythagorasBridge`) composed with the `H₃(q)` Wedderburn branching
(`A3OffBlockDerivation`: `A=D=(a+b)/2`, `B=(a−b)/2`, `factor_sa = 1 − x²`, `x=(a−b)/(a+b)`)
gives the Pythagorean lift

  r* = 1 + x² = 2 − factor_sa,   (1+x²)² = (1−x²)² + (2x)².

The observed lift is r* = μ₃/c₃ ≈ 1.585, i.e. it requires x² ≈ 0.585 (x ≈ 0.765). This probe
asks — 0-fit — whether the **branching's own** bar-asymmetry x is that large.

RESULT (honest negative): it is not. The two 1-dim blocks (3), (1³) have EQUAL Borromean
characters (χ = 1 for β = (σ₁σ₂⁻¹)³), so x comes purely from the bar-asymmetric weight:
  - symmetric Wedderburn weight d_q²/[n]!  →  bar-even  →  x = 0        (r* = 1, no lift);
  - content weight q^{±c}                  →  x = tanh(c·ln q);
     c = 3 (bare H₃ content) → x² ≈ 0.09 (r* ≈ 1.09); no clean topological c gives x = 0.765
     (it would need c ≈ 9.66).
The branching supplies at most x² ≈ 0.09 — ~6× short of the required 0.585. Hence the transverse
leg 2x is NOT the branching slope; the A=3 magnitude needs a genuinely transverse
(Birkhoff/Stokes surface-curvature, qou-prjo) datum. NOTHING is fitted or wired.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from _witness_q0_stamp import stamp_q0  # noqa: E402

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 (AGENTS.md, owner directive 2026-08-18: "PROBES ARE NOT EXEMPT").
# dps raised at MODULE scope, before the first mpf below is constructed.
set_compute_dps()

# PIN: MUON (ideal CAL-2) -- 1.10997859555733471..., not the proton
# 1.1099785827513808. Recorded explicitly because this literal carried no pin
# label at all; re-pinning is bean qou-1c4y, not this drain.
# q0 RESOLVED, not frozen (2026-08-29, bean qou-1c4y). This was the literal
# 1.10997859555733471..., the SUPERSEDED muon pin A -- it stopped being the
# muon anchor when PR #5500 re-derived that anchor to CODATA-2022. A frozen
# literal cannot follow an anchor move, so the witness kept recording A under
# the label "muon" and the anchor gate scored it Q0_FLIP; re-running could not
# clear it, because the producer was the source of the stale number. It now
# resolves the PROTON pin per the owner directive of 2026-08-15 ("we want
# proton unless for an explicit reason ... otherwise pin proton").
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402 -- q0 RESOLVED, not frozen (qou-1c4y)
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

Q0_STR = _Q0_RESOLVED
Q0 = mp.mpf(Q0_STR)
LNQ = mp.log(Q0)
MU3_STR, C3_STR = "0.4708", "0.297"
MU3 = mp.mpf(MU3_STR)
C3 = mp.mpf(C3_STR)
R_STAR = MU3 / C3
X_REQ = mp.sqrt(R_STAR - 1)              # r* = 1 + x²  ⇒  x = √(r*−1)


def qint(k: int):
    return (Q0 ** k - Q0 ** (-k)) / (Q0 - 1 / Q0)


def sym_wedderburn_x():
    """Symmetric weight d_q²/[n]! : (3) and (1³) have identical hooks (3,2,1) ⇒ equal ⇒ x=0."""
    d = qint(3) * qint(2) * qint(1)           # same for (3) and (1,1,1)
    y3 = d * d
    y111 = d * d
    return (y3 - y111) / (y3 + y111)


def content_x(c):
    """Content weight y_(3)=q^{+c}, y_(1³)=q^{-c} ⇒ x = tanh(c·ln q)."""
    c = mp.mpf(c)
    a, b = Q0 ** c, Q0 ** (-c)
    return (a - b) / (a + b)


def main() -> None:
    rows = []
    for label, x in [
        ("symmetric Wedderburn d_q²/[n]!", sym_wedderburn_x()),
        ("content c=3 (bare H₃)", content_x(3)),
        ("content c=6", content_x(6)),
        ("content c=9 (≈H₉ cabling scale)", content_x(9)),
    ]:
        rows.append({
            "weight": label, "x": fmt(x), "x2": fmt(x * x),
            "r_star_1_plus_x2": fmt(1 + x * x),
            "abs_err_vs_rstar": fmt(abs((1 + x * x) - R_STAR)),
            "_x2": x * x,                      # mpf, stripped before serialization
        })

    c_needed = mp.atanh(X_REQ) / LNQ           # content that WOULD give x=0.765
    max_branching_x2 = max(r["_x2"] for r in rows)
    for r in rows:
        del r["_x2"]

    witness = {
        "computation": "a3-branching-asymmetry-vs-required",
        "scriptFile": "a3_branching_asymmetry_vs_required_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": "mpmath mpf (0 free params; structural)",
        "free_parameters": 0,
        "inputs": {
            "q0": Q0_STR, "q0_pin": "proton (experimental pin, resolved)",
            "q0_precision_note": (
                "RESOLVED from substrate.q_parameter at run time, not frozen. It was a "
                "17-digit muon literal until 2026-08-29 (bean qou-1c4y); a frozen literal "
                "cannot follow an anchor move, which is how this witness came to record "
                "the superseded muon pin under the label \"muon\"."),
            "mu3_MeV": MU3_STR, "c3_single_trace_MeV": C3_STR, "r_star": fmt(R_STAR),
            "arithmetic": f"mpmath mpf at {mp.mp.dps} dps (no float64 anywhere)",
            "borromean_braid": "(sigma_1 sigma_2^{-1})^3",
            "chi_(3)_borr": 1, "chi_(1,1,1)_borr": 1,
            "note_equal_characters": "both 1-dim characters = 1 on the Borromean braid (A3OffBlockDerivation Part 1)",
        },
        "results": {
            "x_required": fmt(X_REQ), "x2_required": fmt(R_STAR - 1),
            "branching_rows": rows,
            "max_branching_x2": fmt(max_branching_x2),
            "content_c_that_would_be_needed": fmt(c_needed),
            "branching_supplies_required": bool(
                max_branching_x2 >= (R_STAR - 1) - mp.mpf(10) ** -3),
        },
        "verdict": (
            f"scope-(a): BARE H₃ (content c=3) gives x²≈0.09, r*≈1.09 — ~6× short in x² of the "
            f"required x²={mp.nstr(R_STAR - 1, 4)}; symmetric weight gives x=0, r*=1. BUT the CABLED "
            f"content c≈9 (the H₉ strand scale at which c₃ is actually computed) gives "
            f"x²≈0.54, r*≈1.54 — only ~3% short of 1.585 (exact needs c≈{mp.nstr(c_needed, 3)}). So the "
            f"Pythagorean transverse leg 2x is NOT the bare-branching slope; it lives at the "
            f"CABLED/transverse (H₉ Birkhoff/Stokes surface-curvature, qou-prjo) level, where it "
            f"NEARLY closes. A near-miss lead, not a closure — the 9→9.66 residual is the open "
            f"fine structure."
        ),
        "scope": (
            "scope-(a): confirms the Lean Pythagorean structure (1+x²)²=(1−x²)²+(2x)² and "
            "reports that the branching's own x is too small. r*/μ₃/c₃/x never inverted to fit."
        ),
        "lean": "QOU.QBeta.A3BranchingModulusReflection",
        "wired": False,
        "notes": "Honest negative on 'derive s from the branching': the branching cannot; s is transverse.",
    }

    # Provenance stamp (bean 1j39): this producer hand-rolls json.dump and so

    # never reaches WitnessBuilder.build(), which is where q0Anchor is set.

    # Without this the witness stays unstamped permanently — re-running it

    # cannot fix that. Adds two keys; touches nothing else.

    stamp_q0(witness, __file__)

    out = os.path.join(os.path.dirname(__file__), "a3-branching-asymmetry-vs-required.witness.json")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w", encoding="utf-8") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"r* = {mp.nstr(R_STAR, 5)}  ⇒  required x = {mp.nstr(X_REQ, 5)}, x² = {mp.nstr(R_STAR - 1, 5)}")
    for r in rows:
        print(f"  {r['weight']:34s}: x²={r['x2'][:6]}  r*=1+x²={r['r_star_1_plus_x2'][:6]}")
    print(f"bare H₃ (c=3): ~6x short in x²;  cabled c≈9: r*=1.54 (~3% short);  needs c≈{mp.nstr(c_needed, 3)}")
    print(f"wrote {out}")
    assert not witness["results"]["branching_supplies_required"], "unexpected: branching supplied r*"
    assert abs(content_x(3) ** 2 - mp.mpf("0.0919")) < mp.mpf(10) ** -3, "content c=3 x² drift"
    print("ALL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
