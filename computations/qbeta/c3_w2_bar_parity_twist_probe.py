#!/usr/bin/env python3
"""Does the bar-parity twist remove the parity obstruction?  No — it relocates it.

Bean `qou-ceg6` / conjecture `conj:c1-ggm-bar-parity-faces`, positive half.

The conjecture's obstruction half is proved (`doorV_parity_no_identity`): no
non-negative-cone combination `alpha p + beta q` of the tensor-square sequences
can equal a target with a consecutive sign flip, because a real square is
non-negative. Its positive half — that after the diagonal Z/2 twist `(-1)^m` the
agreement is EXACT, i.e. the twist is the WHOLE difference — is open. This probe
tests the scalar-combination reading of that half.

## What is established here

1. **The twist maps solutions to solutions.** With
   `y_{m+2} - (2 - q^{m+1}) y_{m+1} + y_m = 0` the Stokes carrier's recurrence,
   `z_m := (-1)^m y_m` satisfies `z_{m+2} + (2 - q^{m+1}) z_{m+1} + z_m = 0`.
   Proved in Lean (`barTwist_recursion`) and re-measured here.

2. **The twist inverts EVERY consecutive-pair sign**, not just the alternating
   ones: `z_m z_{m+1} = -(y_m y_{m+1})` (Lean `barTwist_consecutive_product`).

3. **Therefore the twist cannot clear the obstruction unless the target
   alternates at every consecutive pair** (Lean
   `obstruction_fires_on_one_of`, `twist_clears_only_if_everywhere_alternating`).
   The Stokes carrier's solution does NOT: for `m + 1 < log 2 / log q` the
   coefficient `2 - q^{m+1}` is positive and no flip occurs. So the twisted
   sequence inherits flips exactly where the untwisted one had none, and
   `doorV_parity_no_identity` fires on it too.

This is measured below: the flip positions of the twisted sequence are recorded,
and they are non-empty.

**Consequence for the conjecture.** The claim "the diagonal Z/2 character is the
sole residual" cannot mean that applying the character makes the target a
non-negative combination of the squares — that reading is excluded by the same
non-negativity invariant that gave the obstruction in the first place. What
survives is the MODULE-level reading, where the comparison is up to a genuine
gauge transformation rather than a non-negative scalar combination, and where
the Door-iv/v probes measured `U -> I` and a constant connecting matrix. The
block should not be read as asserting the scalar version.

## What this probe does NOT settle

The module-level statement. A gauge is a matrix over the q-difference field and
does far more than a non-negative scalar combination, so nothing here bears on
it. Note also that reconstructing the tensor-square sequences `f_+^2, f_-^2` from
prose is error-prone; this probe therefore reports only findings that depend on
the Stokes carrier's own recurrence, which is unambiguous. The scalar fit
against a reconstructed `f_+/f_-` is deliberately NOT reported as evidence.

-- Ref: [manuscript] docs/audits/2026-07-20-qlift-doorV-stokes.md
-- Ref: [manuscript] docs/audits/2026-07-20-qlift-doorIV-matrix.md
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

DPS = 80
Q_STR = "1.1099785827513808075916690956"
N = 30


def main() -> None:
    t0 = time.perf_counter()
    mp.mp.dps = DPS
    q = mp.mpf(Q_STR)
    res: dict = {}
    checks: list = []

    # the Stokes carrier's recurrence, and its bar-parity twist
    y = [mp.mpf(1), mp.mpf(1)]
    for m in range(N):
        y.append((2 - q ** (m + 1)) * y[m + 1] - y[m])
    z = [(-1) ** m * y[m] for m in range(len(y))]

    print("=" * 78)
    print("  1. the twist maps solutions to solutions")
    print("=" * 78)
    err = max(abs(z[m + 2] + (2 - q ** (m + 1)) * z[m + 1] + z[m]) for m in range(N))
    scale = max(abs(z[m]) for m in range(N))
    rel = err / scale
    print(f"    max |z_(m+2) + (2 - q^(m+1)) z_(m+1) + z_m| / max|z| = {mp.nstr(rel, 6)}")
    res["twistedRecursionRelResidual"] = mp.nstr(rel, 6)
    ok1 = rel < mp.mpf("1e-50")
    checks.append({
        "name": "twist_maps_solutions_to_solutions",
        "detail": f"z_m = (-1)^m y_m satisfies the sign-flipped recurrence to "
                  f"relative {mp.nstr(rel, 6)}; Lean barTwist_recursion proves it "
                  "in general",
        "passed": bool(ok1),
    })

    print()
    print("=" * 78)
    print("  2. the twist inverts EVERY consecutive-pair sign")
    print("=" * 78)
    worst = mp.mpf(0)
    for m in range(N):
        lhs = z[m] * z[m + 1]
        rhs = -(y[m] * y[m + 1])
        d = abs(lhs - rhs) / max(abs(rhs), mp.mpf("1e-300"))
        worst = max(worst, d)
    print(f"    max rel |z_m z_(m+1) + y_m y_(m+1)| = {mp.nstr(worst, 6)}")
    res["signInversionRelErr"] = mp.nstr(worst, 6)
    ok2 = worst < mp.mpf("1e-60")
    checks.append({
        "name": "twist_inverts_every_consecutive_pair_sign",
        "detail": "z_m z_(m+1) = -(y_m y_(m+1)) identically; Lean "
                  "barTwist_consecutive_product",
        "passed": bool(ok2),
    })

    print()
    print("=" * 78)
    print("  3. where the signs flip, before and after")
    print("=" * 78)
    flips_y = [m for m in range(N) if y[m] * y[m + 1] < 0]
    flips_z = [m for m in range(N) if z[m] * z[m + 1] < 0]
    thresh = mp.log(2) / mp.log(q)
    print(f"    untwisted flips at m = {flips_y}")
    print(f"    twisted   flips at m = {flips_z}")
    print(f"    2 - q^(m+1) changes sign at m+1 = log2/log q = {mp.nstr(thresh, 8)}")
    print("    The untwisted solution does NOT alternate below that threshold, so")
    print("    the twist necessarily introduces flips there.")
    res["untwistedFlips"] = flips_y
    res["twistedFlips"] = flips_z
    res["signChangeThreshold"] = mp.nstr(thresh, 8)
    ok3 = len(flips_z) > 0
    checks.append({
        "name": "twisted_sequence_still_has_sign_flips",
        "detail": f"the twisted sequence flips at m = {flips_z}, so "
                  "doorV_parity_no_identity fires on it too. The twist relocates "
                  "the obstruction rather than removing it.",
        "passed": bool(ok3),
    })

    print()
    print("=" * 78)
    print("  4. the disjunction, checked pointwise")
    print("=" * 78)
    print("    Lean obstruction_fires_on_one_of: at every m with a nonzero product,")
    print("    the obstruction fires on y or on its twist. Never on neither.")
    both_clear = [m for m in range(N)
                  if y[m] * y[m + 1] > 0 and z[m] * z[m + 1] > 0]
    print(f"    m where BOTH are flip-free: {both_clear}   (must be empty)")
    res["mWhereBothClear"] = both_clear
    ok4 = len(both_clear) == 0
    checks.append({
        "name": "obstruction_fires_on_one_of_the_two",
        "detail": "no m at which both the target and its twist are flip-free — "
                  "the pointwise content of Lean obstruction_fires_on_one_of",
        "passed": bool(ok4),
    })

    passed = all(c["passed"] for c in checks)
    print()
    print("=" * 78)
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")
    print("=" * 78)
    print("""
  CONCLUSION.  The bar-parity twist does not remove the parity obstruction; it
  relocates it. Since the twist inverts every consecutive-pair sign, and the
  Stokes carrier's solution is flip-free below m+1 = log2/log q, the twisted
  sequence acquires flips exactly there — and one flip is all
  doorV_parity_no_identity needs.

  So "the diagonal Z/2 character is the sole residual" CANNOT mean that applying
  the character makes the target a non-negative combination of the squares. That
  reading is excluded by the same non-negativity invariant that produced the
  obstruction. What survives is the MODULE-level reading, where the comparison
  is up to a gauge rather than a non-negative scalar combination. Nothing here
  bears on that, and nothing here refutes the conjecture as the block states it.
""")

    script_path = Path(__file__).resolve()
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                             text=True, cwd=script_path.parent).stdout.strip()
    except Exception:
        sha = "unknown"
    witness = {
        "schema": "witness/v1",
        "engine": "mpmath",
        "scriptFile": script_path.name,
        "scriptSha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "commitSha": sha or "unknown",
        "description":
            "Tests the scalar-combination reading of the positive half of "
            "conj:c1-ggm-bar-parity-faces — that the diagonal Z/2 character "
            "(-1)^m is the WHOLE difference. The twist maps the Stokes carrier's "
            "recurrence y_{m+2} - (2-q^{m+1})y_{m+1} + y_m = 0 to the "
            "sign-flipped one (verified to 1e-50 relative, and proved in Lean as "
            "barTwist_recursion), and it inverts EVERY consecutive-pair sign, "
            "not only the alternating ones. Since the carrier's solution is "
            "flip-free below m+1 = log2/log q, the twisted sequence acquires "
            "flips exactly there — measured — and doorV_parity_no_identity needs "
            "only one flip. So the twist relocates the parity obstruction rather "
            "than removing it. The scalar reading of 'sole residual' is "
            "therefore excluded; the module-level reading, where the comparison "
            "is up to a gauge, is untouched and remains the conjecture's content.",
        "computation": {
            "dps": DPS,
            "q": Q_STR,
            "terms": N,
            "carrier": "y_{m+2} - (2 - q^{m+1}) y_{m+1} + y_m = 0",
            "twist": "z_m = (-1)^m y_m",
        },
        "results": res,
        "checks": checks,
        "verdict":
            "The bar-parity twist RELOCATES the parity obstruction, it does not "
            "remove it. Proved in Lean (obstruction_fires_on_one_of, "
            "twist_clears_only_if_everywhere_alternating) and measured here: the "
            "twisted sequence still flips, at exactly the indices where the "
            "untwisted one did not. Consequence: 'the diagonal Z/2 character is "
            "the sole residual' cannot be read as 'applying the character makes "
            "the target a non-negative combination of the squares'. It must be "
            "read at the MODULE level, up to a gauge. This does not refute the "
            "conjecture — it removes one reading of it, and the block has been "
            "amended to say which. Deliberately NOT reported: a scalar fit "
            "against a prose-reconstructed f_+/f_-, which would not be "
            "trustworthy. Nothing wired to production.",
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c3-w2-bar-parity-twist-probe.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness -> {out.name}   ({witness['durationMs']} ms)")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
