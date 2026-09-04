#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Δ_λ magnitude — the A-dependent DAMPING route is WALLED (formalize-first companion).

Context (corpus, already established — NOT re-derived here):
  * #4300 (QOU.MassTheory.JetFiltrationTwoAnchorNoGo, sorry-free) proved the single-knob
    q-scaled coinvariant graded dimension [A]_q! cannot land both light-nucleus anchors,
    and read §4 of the jet-filtration audit as calling for a DAMPED graded dimension.
  * The two damping routes proposed to follow it are BOTH factors D(A) ≤ 1 on
        ρ_grad(A) = [A]_q!/[2]_q!  (ρ_grad(3)=[3]_q, ρ_grad(4)=[3]_q·[4]_q):
      (a) an A-locked parabolic/skew QUOTIENT of [A]_q! (graded dim of a quotient ≤ full);
      (b) a DEMAZURE sub-crystal (a Bruhat-prefix SUB-SUM of [A]_q! ≤ full sum —
          DemazureSubcrystalGradedDim.lean already proved the A=3 Demazure obstruction).

This probe is the FORMALIZE-FIRST companion to QOU.MassTheory.DampingNonMonotoneWall.
It verifies, at the production mpmath floor, that at the FIXED canonical substrate q0 the
residual ρ_strong(A) − ρ_grad(A) CHANGES SIGN between A=3 and A=4, so the correction the
data requires is NOT a damping (which only ever subtracts). Facts (mirroring the Lean):

  (U)  A=3 undershoot / damping wall:  ρ_grad(3)(q0)=[3]_q0 < ρ_strong(3)
       ⇒ for any damping 0≤d≤1, d·[3]_q0 ≤ [3]_q0 < ρ_strong(3): NO damping closes A=3.
  (O)  A=4 overshoot:  ρ_grad(4)(q0)=[3]_q0·[4]_q0 > ρ_strong(4).
  (SIGN) residual r(3)=ρ_strong(3)−ρ_grad(3) > 0 while r(4)=ρ_strong(4)−ρ_grad(4) < 0:
       required correction is + at A=3, − at A=4 — non-monotone in A, cannot be a damping.
  (ROBUST) the sign change holds for BOTH the isospin-corrected targets AND the raw AME
       ratios B(3H)/B(2H)=3.814, B(4He)/B(2H)=12.72 — insensitive to the anchor values.
  (ENDPTS) the rational substrate window [1.109, 1.11] used by the Lean brackets both
       anchors: [3]_1.11 < ρ_strong(3) < ρ_strong(4) < [3][4]_1.109.

STRICT anti-fit: ρ_strong(3), ρ_strong(4) are DERIVED-ELSEWHERE targets (jet-filtration
witness / #3986/#3990), consumed ONLY as comparison bounds. No q, no damping d is solved
from the anchors; nothing is wired; no AME point is inverted.
"""
import json
import subprocess
import sys
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

# --- substrate q0 + DERIVED-ELSEWHERE targets (same numbers the escape/no-go Lean used) ---
JET_WITNESS = HERE / "deltalambda-jet-filtration-magnitude.witness.json"
jw = json.loads(JET_WITNESS.read_text())
# The q0 read used to end in a SILENT FALLBACK to the literal
# "1.10997859555733471" -- the RETIRED self-certified muon pin A (superseded
# 2026-08-22, fca08de7d2). The upstream witness has carried the PROTON pin
# since the jet-filtration producer was migrated, so the fallback was dead --
# but a dead cross-layer fallback is still a fallback: had the upstream ever
# stopped recording q0, this probe would have silently computed at a retired
# muon pin while its own witness stamped "proton". A pin that cannot be
# established is an error, not a default (bean qou-9ugp).
_q0_raw = jw.get("data", {}).get("q0") or jw.get("parameters", {}).get("q0")
if not _q0_raw:
    raise SystemExit(
        f"q0 not found in {JET_WITNESS.name}: neither data.q0 nor parameters.q0. "
        "Re-run deltalambda_jet_filtration_magnitude_probe.py first. Refusing to "
        "fall back to a literal pin.")
q0 = mp.mpf(str(_q0_raw))
RHO3 = mp.mpf("3.8128")     # ρ_strong(3)  isospin/Coulomb-corrected (#3986/#3990)
RHO4 = mp.mpf("13.0316")    # ρ_strong(4)  isospin/Coulomb-corrected
# raw AME total-binding ratios (uncorrected) — used only for the robustness cross-check
RHO3_RAW = mp.mpf("8.482") / mp.mpf("2.224")    # B(3H)/B(2H) ≈ 3.814
RHO4_RAW = mp.mpf("28.296") / mp.mpf("2.224")   # B(4He)/B(2H) ≈ 12.72


def qbr(k, q):
    """[k]_q = 1+q+...+q^{k-1} (coinvariant Poincaré factor)."""
    return sum(q ** j for j in range(k))


def approx(x):
    return mp.nstr(x, 12)


assertions = []


def check(name, computed, expected, source):
    passed = bool(computed == expected)
    assertions.append(
        {"name": name, "computed": str(computed), "expected": str(expected),
         "passed": passed, "source": source})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}: {source}")


rg3 = qbr(3, q0)             # ρ_grad(3)(q0) = [3]_q0
rg4 = qbr(3, q0) * qbr(4, q0)  # ρ_grad(4)(q0) = [3]_q0·[4]_q0
r3 = RHO3 - rg3              # residual at A=3
r4 = RHO4 - rg4              # residual at A=4

# --- (U) A=3 undershoot / damping wall -------------------------------------------------
# ρ_grad(3)(q0) < ρ_strong(3); a damping d∈[0,1] only decreases it. Sample d densely.
damping_wall_ok = bool(rg3 < RHO3)
for i in range(0, 101):
    d = mp.mpf(i) / 100
    if not (d * rg3 < RHO3):
        damping_wall_ok = False
        break
check("A3_undershoot_no_damping_closes_it", damping_wall_ok, True,
      f"ρ_grad(3)(q0)=[3]_q0={approx(rg3)} < ρ_strong(3)={approx(RHO3)}; ∀ d∈[0,1]: "
      f"d·[3]_q0 ≤ [3]_q0 < ρ_strong(3). A damping ONLY decreases ρ(3) — it cannot close "
      f"an anchor that already UNDERSHOOTS. (needed D(3)={approx(RHO3 / rg3)} > 1: amplify)")

# --- (O) A=4 overshoot -----------------------------------------------------------------
check("A4_overshoot_at_q0", bool(rg4 > RHO4), True,
      f"ρ_grad(4)(q0)=[3]_q0·[4]_q0={approx(rg4)} > ρ_strong(4)={approx(RHO4)}; at the same "
      f"substrate the A=4 ratio OVERshoots (needed D(4)={approx(RHO4 / rg4)} < 1: damp). "
      f"So damping is the RIGHT sign for A=4, the WRONG sign for A=3.")

# --- (SIGN) residual changes sign between A=3 and A=4 ----------------------------------
check("residual_sign_change_A3_pos_A4_neg", bool(r3 > 0 and r4 < 0), True,
      f"r(3)=ρ_strong(3)−ρ_grad(3)={approx(r3)} > 0 (graded undershoots A=3) while "
      f"r(4)=ρ_strong(4)−ρ_grad(4)={approx(r4)} < 0 (graded overshoots A=4): the required "
      f"correction is + at A=3, − at A=4. A multiplicative damping D(A)≤1 supplies a "
      f"NON-positive correction at every A ⇒ cannot realise a sign change. Damping is WALLED.")

# --- (ROBUST) sign change holds for the RAW AME ratios too -----------------------------
r3_raw = RHO3_RAW - rg3
r4_raw = RHO4_RAW - rg4
check("sign_change_robust_to_raw_ame", bool(r3_raw > 0 and r4_raw < 0), True,
      f"with RAW AME ratios B(3H)/B(2H)={approx(RHO3_RAW)}, B(4He)/B(2H)={approx(RHO4_RAW)}: "
      f"r_raw(3)={approx(r3_raw)} > 0 and r_raw(4)={approx(r4_raw)} < 0 — same sign pattern. "
      f"The wall does NOT depend on the isospin/Coulomb correction (anchors are bounds only).")

# --- (ENDPTS) rational substrate window brackets both anchors (matches Lean rationals) --
q_hi = mp.mpf("1.11"); q_lo = mp.mpf("1.109")
endpt_ok = bool(qbr(3, q_hi) < RHO3 and qbr(3, q_lo) * qbr(4, q_lo) > RHO4)
check("rational_window_brackets_both_anchors", endpt_ok, True,
      f"[3]_1.11={approx(qbr(3, q_hi))} < ρ_strong(3)={approx(RHO3)} (undershoot upper-endpoint) "
      f"and [3][4]_1.109={approx(qbr(3, q_lo) * qbr(4, q_lo))} > ρ_strong(4)={approx(RHO4)} "
      f"(overshoot lower-endpoint): the Lean rational window [1.109,1.11] certifies both.")

# --- context (audit table; not assertions) --------------------------------------------
ctx = {
    "q0": mp.nstr(q0, 20),
    "qbr3_q0": approx(qbr(3, q0)),
    "qbr4_q0": approx(qbr(4, q0)),
    "rho_grad3_q0": approx(rg3),
    "rho_grad4_q0": approx(rg4),
    "rho_strong3": mp.nstr(RHO3, 8),
    "rho_strong4": mp.nstr(RHO4, 8),
    "residual_A3": approx(r3),
    "residual_A4": approx(r4),
    "needed_D3_amplify": approx(RHO3 / rg3),
    "needed_D4_damp": approx(RHO4 / rg4),
    "rho_strong3_raw_ame": mp.nstr(RHO3_RAW, 8),
    "rho_strong4_raw_ame": mp.nstr(RHO4_RAW, 8),
}
print("\ncontext:", json.dumps(ctx, indent=1))

all_passed = all(a["passed"] for a in assertions)


def git_sha():
    try:
        return subprocess.check_output(["git", "log", "-1", "--format=%H"],
                                       cwd=ROOT).decode().strip()
    except Exception:
        return "unknown"


witness = {
    "engine": "mpmath",
    "engineVersion": f"mpmath {mp.__version__}",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "commitSha": git_sha(),
    "scriptFile": str(Path(__file__).relative_to(ROOT)),
    "scriptHash": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12],
    "assertions": assertions,
    "allPassed": all_passed,
    "description": "Δ_λ magnitude: the A-dependent DAMPING route is WALLED. At the fixed "
                   "canonical substrate q0 the residual ρ_strong−ρ_grad changes sign between "
                   "A=3 (+, graded undershoots) and A=4 (−, graded overshoots), so the required "
                   "correction is non-monotone in A and CANNOT be a multiplicative damping "
                   "D(A)≤1 (parabolic/skew quotient OR Demazure sub-crystal alike). Companion to "
                   "Lean QOU.MassTheory.DampingNonMonotoneWall (sorry-free). Robust to raw-vs-"
                   "corrected AME anchors. scope-(b) structural exclusion of the damping class; "
                   "nothing wired.",
    "parameters": {"q0": mp.nstr(q0, 20), "rho_strong3": str(RHO3), "rho_strong4": str(RHO4)},
    "data": ctx,
    "precisionMetadata": {"dps": 60},
    "caveats": [
        "ρ_strong(3), ρ_strong(4) are DERIVED-ELSEWHERE comparison targets (jet-filtration "
        "witness / #3986/#3990); consumed as one-sided bounds, never inverted. No fit; nothing wired.",
        "The exclusion is scope-(b) STRUCTURAL, cited invariant = monotone-≤1 action of a damping "
        "together with the q0 A=3 undershoot. It excludes the pure-DAMPING class only; per the "
        "permanence principle [A]_q! remains a valid ingredient — an additive many-body TERM that "
        "re-weights it (sign-changing in A) is NOT excluded and is the remaining open target.",
        "Fixed canonical q0, read from the jet-filtration witness, which carries the PROTON "
        "pin (label corrected from 'muon-canonical', bean qou-9ugp). Setting q≈1.26 to reach A=3 "
        "with free q is NOT admissible: q0 is pinned by the 3 calibrations, not a free knob.",
    ],
    "auditOnly": "docs/audits/2026-07-26-deltalambda-A-dependent-damping.md",
}

OUT = HERE / "deltalambda-damping-nonmonotone-wall.witness.json"
# Provenance stamp (bean qou-4un2): this producer writes its
# witness directly, so nothing else records which script made
# it -- and a re-run of an unstamped producer DELETES the
# scriptFile a downstream pass had added. This producer DOES read q0 (from
# the jet-filtration witness), so the anchor is resolved and stamped.
from qou_substrate.witness import WitnessBuilder as _WB
import os as _os  # noqa: E402 -- provenance stamp
witness.setdefault("scriptFile", _os.path.basename(__file__))
# q0_anchor was `False`, i.e. "this witness carries no q0-dependent field".
# Untrue: q0 is read from the jet-filtration witness at module scope and every
# q-integer below is a function of it. The false declaration DELETED the anchor
# stamp on every run, converting a visible Q0_FLIP into a silent
# Q0_ANCHOR_MISSING (bean qou-1c4y).
_WB.stamp_staleness_metadata(
    witness, script_path=__file__, engine=None)
OUT.write_text(json.dumps(witness, indent=1, ensure_ascii=False))
print(f"\nwrote {OUT.relative_to(ROOT)}  allPassed={all_passed}")
sys.exit(0 if all_passed else 1)
