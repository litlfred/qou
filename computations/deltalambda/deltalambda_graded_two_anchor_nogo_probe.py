#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Δ_λ magnitude — the graded-dimension TWO-ANCHOR NO-GO (W5, formalize-first).

Context (corpus, already established — NOT re-derived here):
  * The exchange-DETERMINANT cumulant family is Lean-capped: ρ_A = b_A/b_2 ≤ C(A,2)
    (QOU.MassTheory.SaturationRhoCap, sorry-free) — undershoots the strong targets.
  * The NON-determinant jet-filtration graded dimension
        W_A(q) = [A]_q! = ∏_{k=1}^{A}[k]_q ,   ρ_grad(A) = W_A(q)/W_2(q)
    ESCAPES that cap (QOU.MassTheory.JetFiltrationGradedDimEscape:
    ρ_grad(4)=[3]_q·[4]_q ≥ 12 > 6, sorry-free), so the true magnitude sits in a
    TWO-SIDED BRACKET:  −ln det (capped, too flat)  <  true  <  [A]_q! (too steep).
  * The jet-filtration probe (deltalambda_jet_filtration_magnitude_probe.py) found,
    as PYTHON assertions only, that a single parameter-free q lands NEITHER anchor.

This probe is the FORMALIZE-FIRST companion to a new Lean no-go file
(QOU.MassTheory.JetFiltrationTwoAnchorNoGo). It verifies, at the production mpmath
floor, exactly the inequalities the Lean file proves sorry-free — turning the
"one knob cannot do both" observation into a machine-checked scope-(b) structural
statement:

  (S)  step-lock:            [4]_q ≥ 4            for all q ≥ 1   (q-independent invariant)
  (M)  single-knob monotone: q ↦ [3]_q  and  q ↦ [3]_q·[4]_q  are BOTH increasing on [1,∞)
  (N)  two-anchor no-go:     q ≥ 1 and [3]_q ≥ ρ_strong(3)  ⇒  [3]_q·[4]_q > ρ_strong(4)
                             (reaching the A=3 target FORCES an A=4 overshoot)

STRICT anti-fit: ρ_strong(3), ρ_strong(4) are consumed as DERIVED-ELSEWHERE targets
(committed jet-filtration witness) and used ONLY as comparison constants in (N). No q
is solved from the anchors; nothing is wired; no AME point is inverted. The invariants
(S)/(M) are AME-independent (scope-(b), proved); (N) uses the targets as bounds only.
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

# --- substrate q0 + DERIVED-ELSEWHERE targets; the jet-filtration witness now
# --- RESOLVES its pin (proton) instead of freezing the superseded muon literal ---
# q0 and the strong targets are read from the committed jet-filtration witness, not
# recomputed, so this probe consumes the SAME numbers the escape Lean was built on.
JET_WITNESS = HERE / "deltalambda-jet-filtration-magnitude.witness.json"
jw = json.loads(JET_WITNESS.read_text())
q0 = mp.mpf(str(jw["data"].get("q0", jw["parameters"].get("q0", "1.10997859555733471"))))
# strong targets (isospin/Coulomb-corrected; #3986/#3990) — comparison constants only
RHO3 = mp.mpf("3.8128")     # ρ_strong(3)  (jet-filtration witness)
RHO4 = mp.mpf("13.0316")    # ρ_strong(4)  (jet-filtration witness)
DATA_STEP = RHO4 / RHO3     # ≈ 3.4179  (the A=3→A=4 data growth step)


def qbr(k, q):
    """Balanced-length q-bracket [k]_q = 1+q+...+q^{k-1} (the coinvariant Poincaré factor)."""
    return sum(q ** j for j in range(k))


def rho_grad(A, q):
    """ρ_grad(A) = W_A(q)/W_2(q) = ∏_{k=3}^{A}[k]_q  (W_2 = [2]_q cancels)."""
    num = mp.mpf(1)
    for k in range(3, A + 1):
        num *= qbr(k, q)
    return num


def approx(x):
    return mp.nstr(x, 12)


assertions = []


def check(name, computed, expected, source):
    passed = bool(computed == expected)
    assertions.append(
        {"name": name, "computed": str(computed), "expected": str(expected),
         "passed": passed, "source": source}
    )
    print(f"[{'PASS' if passed else 'FAIL'}] {name}: {source}")


# --- (S) step-lock: [4]_q ≥ 4 for all q ≥ 1 (q-independent invariant) ---------------
# sampled dense on [1, 3]; the identity [4]_q - 4 = (q-1)(q^2+2q+3) makes it exact.
step_lock_ok = True
for i in range(0, 401):
    q = mp.mpf(1) + mp.mpf(i) / 100  # q in [1, 5]
    if qbr(4, q) < 4:
        step_lock_ok = False
        break
    # exact factorisation cross-check
    lhs = qbr(4, q) - 4
    rhs = (q - 1) * (q ** 2 + 2 * q + 3)
    if abs(lhs - rhs) > mp.mpf(10) ** (-40):
        step_lock_ok = False
        break
check("step_lock_q4_ge_4_all_q_ge_1", step_lock_ok, True,
      "[4]_q - 4 = (q-1)(q^2+2q+3) ≥ 0 on q≥1 (exact, 40dps); the A=3→A=4 graded step "
      "is q-locked ≥ 4 for every admissible substrate q — no q≥1 flattens it")

check("graded_step_exceeds_data_step_all_q_ge_1",
      bool(qbr(4, q0) > DATA_STEP and mp.mpf(4) > DATA_STEP), True,
      f"data step ρ_strong(4)/ρ_strong(3)={approx(DATA_STEP)} < 4 ≤ [4]_q for all q≥1 "
      f"([4]_q0={approx(qbr(4, q0))}); the graded step overshoots the data step at every q≥1")

# --- (M) single-knob monotonicity: both anchors move the SAME way under q -----------
mono_ok = True
prev3 = prev4 = None
for i in range(0, 301):
    q = mp.mpf(1) + mp.mpf(i) / 100  # q in [1, 4]
    r3 = qbr(3, q)                    # ρ_grad(3) = [3]_q
    r4 = qbr(3, q) * qbr(4, q)        # ρ_grad(4) = [3]_q[4]_q
    if prev3 is not None and (r3 < prev3 or r4 < prev4):
        mono_ok = False
        break
    prev3, prev4 = r3, r4
check("single_knob_moves_both_anchors_up", mono_ok, True,
      "q ↦ [3]_q and q ↦ [3]_q·[4]_q are BOTH strictly increasing on [1,∞) (dense sweep) — "
      "the single knob q cannot push the (under-shot) A=3 ratio up while pushing the "
      "(over-shot) A=4 ratio down: one knob cannot do both")

# --- (N) two-anchor no-go: reaching A=3 target FORCES A=4 overshoot ------------------
# For every q≥1 with [3]_q ≥ ρ_strong(3): [3]_q·[4]_q ≥ ρ_strong(3)·4 = 15.2512 > 13.0316.
nogo_ok = True
q_reach3 = None
for i in range(100, 401):
    q = mp.mpf(i) / 100  # q in [1, 4]
    if qbr(3, q) >= RHO3:
        if q_reach3 is None:
            q_reach3 = q
        if not (qbr(3, q) * qbr(4, q) > RHO4):
            nogo_ok = False
            break
bound = RHO3 * 4
check("two_anchor_nogo_reach3_forces_overshoot4", nogo_ok, True,
      f"∀ q≥1: [3]_q ≥ ρ_strong(3)={approx(RHO3)} ⇒ [3]_q·[4]_q ≥ ρ_strong(3)·4 = "
      f"{approx(bound)} > {approx(RHO4)} = ρ_strong(4). First q reaching A=3: "
      f"q={approx(q_reach3)}; there ρ_grad(4)={approx(qbr(3, q_reach3) * qbr(4, q_reach3))} "
      f"(overshoot). No single-knob graded dim lands both anchors.")

check("bound_product_exceeds_rho4", bool(bound > RHO4), True,
      f"ρ_strong(3)·4 = {approx(bound)} > {approx(RHO4)} = ρ_strong(4): the no-go margin "
      f"is {approx(bound - RHO4)} MeV-ratio, strictly positive")

# --- forward context values (for the audit table; not assertions) -------------------
ctx = {
    "q0": mp.nstr(q0, 20),
    "qbr3_q0": mp.nstr(qbr(3, q0), 12),
    "qbr4_q0": mp.nstr(qbr(4, q0), 12),
    "rho_grad3_q0": mp.nstr(rho_grad(3, q0), 12),
    "rho_grad4_q0": mp.nstr(rho_grad(4, q0), 12),
    "rho_strong3": mp.nstr(RHO3, 8),
    "rho_strong4": mp.nstr(RHO4, 8),
    "data_step_T4_over_T3": mp.nstr(DATA_STEP, 8),
    "graded_step_q4_q0": mp.nstr(qbr(4, q0), 8),
    "nogo_bound_rho3_times_4": mp.nstr(bound, 8),
}
print("\ncontext:", json.dumps(ctx, indent=1))

# --- SU(4) row-restriction is VACUOUS for A≤4 (a separate scope-(b) elimination) ----
# The natural "physical" damping candidate — restrict to ℓ(λ)≤4 (SU(4) supermultiplet
# rows) — does NOT damp the light nuclei, because every partition of A≤4 already has
# ≤4 parts. So it cannot be the A=3→A=4 damping. Verify by enumeration.
from itertools import count


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield []
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest


su4_vacuous = True
for A in (2, 3, 4):
    all_parts = list(partitions(A))
    restricted = [p for p in all_parts if len(p) <= 4]  # ℓ(λ) ≤ 4
    if restricted != all_parts:
        su4_vacuous = False
check("su4_row_restriction_vacuous_for_A_le_4", su4_vacuous, True,
      "every partition of A≤4 has ≤4 parts ⇒ the SU(4) row-restriction ℓ(λ)≤4 removes "
      "NO partition for the light nuclei; it cannot supply the A=3→A=4 damping "
      "(scope-(b) elimination of the SU(4)-locality damping candidate)")

all_passed = all(a["passed"] for a in assertions)


def git_sha():
    try:
        return subprocess.check_output(["git", "log", "-1", "--format=%H"],
                                       cwd=ROOT).decode().strip()
    except Exception:
        return "unknown"


def script_hash():
    import hashlib
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12]


witness = {
    "engine": "mpmath",
    "engineVersion": f"mpmath {mp.__version__}",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "commitSha": git_sha(),
    "scriptFile": str(Path(__file__).relative_to(ROOT)),
    "scriptHash": script_hash(),
    "assertions": assertions,
    "allPassed": all_passed,
    "description": "Δ_λ magnitude graded-dimension TWO-ANCHOR NO-GO (W5, formalize-first): "
                   "the single-knob q-scaled coinvariant graded dimension [A]_q! cannot land "
                   "both light-nucleus anchors — step-locked ≥4, monotone in q, reaching A=3 "
                   "forces A=4 overshoot. Companion to Lean JetFiltrationTwoAnchorNoGo. "
                   "scope-(b) invariants (S)/(M) AME-independent; (N) uses targets as bounds only.",
    "parameters": {"q0": mp.nstr(q0, 20), "rho_strong3": str(RHO3), "rho_strong4": str(RHO4)},
    "data": ctx,
    "precisionMetadata": {"dps": 60},
    "caveats": [
        "ρ_strong(3), ρ_strong(4) are DERIVED-ELSEWHERE comparison targets (jet-filtration "
        "witness / #3986/#3990); consumed as bounds, never inverted. No fit; nothing wired.",
        "Invariants (S) step-lock and (M) monotonicity are q-independent / AME-independent "
        "(scope-(b), proved sorry-free in the companion Lean). (N) is a comparison no-go.",
    ],
    "auditOnly": "docs/audits/2026-07-25-deltalambda-perpair-bond-scalar.md",
}

OUT = HERE / "deltalambda-graded-two-anchor-nogo.witness.json"
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
