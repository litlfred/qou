#!/usr/bin/env python3
"""Nuclear quotient braid Jones values — the (2,k) torus-link Markov traces.

Compute-provenance for the Lean infrastructure
`QOU/BraidKnot/JonesNuclearQuotient.lean` (RHS of the OPEN Part-4 conjecture
`conj:jet-filtered-knot-factor`: `a(Z,N) = J_β̄(q)`).

The nuclear quotient braid collapses each nucleon to one effective inter-nucleon
crossing; its knot type by shell structure (jet-filtered-knot-factor.md) is:
  odd Z -> trefoil (2,3),  even Z -> Hopf (2,2),  double-magic -> unknot (2,1).

The Jones value of the (2,k) torus link is the Markov trace tr_M(sigma_1^k) in
H_2(q). With the Hecke relation sigma^2 = h*sigma + 1 (h = q - 1/q, AGENTS.md
Sec 7a), sigma^k = a_k*sigma + b_k with (a_0,b_0)=(0,1),
(a_{k+1},b_{k+1})=(h*a_k+b_k, a_k); and tr_M(sigma^k) = a_k*z + b_k with the
canonical Markov parameter z = q**3 / (q**2 + 1) (convention D, canonical per
the 2026-08-15 owner ruling R1). This read `1/(sqrt(q) + 1/sqrt(q))` —
convention C — while line 59 has computed the D value throughout; corrected
2026-10-10, bean `qou-u5z0`.

Assertions (all parameter-free / symbolic-exact):
  1. unknot  (2,1): tr = z                 -> the Lean `jonesUnknot`   closed form
  2. Hopf    (2,2): tr = h*z + 1           -> the Lean `jonesHopfLink` closed form
  3. trefoil (2,3): tr = (h^2+1)*z + h     -> the Lean `jonesTrefoil`  closed form
  4. the Hopf value h*z+1 EQUALS the already-verified JonesViaMarkovTrace.jonesHopf
     closed form (q^{5/2}-q^{1/2}+q^2+q)/(q^2+q)   [difference simplifies to 0]

This does NOT prove the conjecture (that a(Z,N) equals these); it verifies the
closed forms wired into the Lean infra are the correct framework-normalised
Markov traces.

Usage:
    python3 nuclear_quotient_jones_torus_link_probe.py
"""
import datetime
import hashlib
import json
import os
import platform
import subprocess

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))


def _sigma_pow_trace(h, z, k):
    """tr_M(sigma^k) = a_k*z + b_k via the Hecke recursion."""
    a, b = sp.Integer(0), sp.Integer(1)  # sigma^0 = 1 = 0*sigma + 1
    for _ in range(k):
        a, b = h * a + b, a
    return sp.simplify(a * z + b)


def main() -> int:
    q = sp.symbols("q", positive=True)
    # Convention D (canonical, owner ruling 2026-08-15 R1, re-affirmed by the
    # owner 2026-08-29). This read `1/(sq + 1/sq)` with `sq = sqrt(q)` = z_C — unannounced, and
    # invisible to scripts/convention-c-producer-audit.py, whose matcher does
    # not see the sqrt-variable spelling. Found by convention-c-value-audit.py.
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)

    tr1 = _sigma_pow_trace(h, z, 1)
    tr2 = _sigma_pow_trace(h, z, 2)
    tr3 = _sigma_pow_trace(h, z, 3)

    # Lean closed forms (in terms of h, z):
    lean_unknot = z
    lean_hopf = h * z + 1
    lean_trefoil = (h ** 2 + 1) * z + h

    # The already-verified JonesViaMarkovTrace.jonesHopf closed form.
    #
    # This read `(q^(5/2) - q^(1/2) + q^2 + q)/(q^2 + q)` -- the CONVENTION-C
    # value, and a STALE transcription: QOU/BraidKnot/JonesViaMarkovTrace.lean
    # migrated to convention D and its own docstring records the C form it
    # replaced, `J(Hopf) = (q^4 + 1)/(q^2 + 1)`. Because the probe's `z` was
    # also still C, the two stale halves agreed and this assertion PASSED while
    # checking nothing against the live Lean. Migrating `z` alone is what
    # surfaced it: got (q^4+1)/(q^2+1), want the C transcription.
    #
    # The check is not circular. The probe derives `h*z + 1` from its own `h`
    # and `z`; this is the Lean's independently STATED closed form. They agree
    # because (q - 1/q)*q^3/(q^2+1) + 1 = (q^4+1)/(q^2+1), verified symbolically.
    jones_hopf_file = (q ** 4 + 1) / (q ** 2 + 1)

    assertions = []

    def check(name, got, want):
        ok = sp.simplify(got - want) == 0
        assertions.append(
            {"name": name, "passed": bool(ok),
             "got": str(sp.simplify(got)), "want": str(sp.simplify(want))}
        )
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        return ok

    all_ok = True
    all_ok &= check("unknot_(2,1)_is_z", tr1, lean_unknot)
    all_ok &= check("hopf_(2,2)_is_hz_plus_1", tr2, lean_hopf)
    all_ok &= check("trefoil_(2,3)_is_h2p1_z_plus_h", tr3, lean_trefoil)
    all_ok &= check("hopf_matches_jonesviamarkovtrace_closed_form",
                    lean_hopf, jones_hopf_file)

    # Numeric sanity at q = 4:
    subs = {q: 4}
    numeric = {f"tr_sigma1_pow_{k}_at_q4": float(_sigma_pow_trace(h, z, k).subs(subs))
               for k in (1, 2, 3)}

    with open(os.path.abspath(__file__), "rb") as _f:
        src = _f.read()
    try:
        commit_sha = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=_HERE,
            capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        commit_sha = None
    witness = {
        "schema": "witness/v1",
        "computation": "nuclear-quotient-jones-torus-link",
        "engine": "python",
        "engineVersion": platform.python_version(),
        "scriptFile": os.path.basename(__file__),
        "commitSha": commit_sha,
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "description": (
            "(2,k) torus-link Jones values (Markov trace tr_M(sigma_1^k)) for the "
            "nuclear quotient braid: unknot/Hopf/trefoil closed forms wired into "
            "QOU/BraidKnot/JonesNuclearQuotient.lean; RHS of the OPEN Part-4 "
            "conjecture conj:jet-filtered-knot-factor (a(Z,N)=J_beta_bar(q)). "
            "Infra provenance only; does NOT prove the conjecture."
        ),
        "generated": datetime.datetime(2026, 7, 11, tzinfo=datetime.timezone.utc).isoformat(),
        "assertions": assertions,
        "allPassed": all_ok,
        "result": {
            "unknot_2_1": str(sp.simplify(tr1)),
            "hopf_2_2": str(sp.simplify(tr2)),
            "trefoil_2_3": str(sp.simplify(tr3)),
            "hopf_matches_existing_lean_jonesHopf": bool(
                sp.simplify(lean_hopf - jones_hopf_file) == 0),
            "numeric_q4": numeric,
        },
        "context": {
            "consumes": "QOU/BraidKnot/JonesNuclearQuotient.lean (jonesUnknot / jonesHopfLink / jonesTrefoil)",
            "conjecture": "conj:jet-filtered-knot-factor Part-4 (OPEN): a(Z,N) = J_beta_bar(q)",
            "hecke_relation": "sigma^2 = h*sigma + 1, h = q - q^{-1} (AGENTS.md Sec 7a)",
            # Was `z = 1/(sqrt(q) + 1/sqrt(q))` (convention C) while line 59
            # computes `z = q ** 3 / (q ** 2 + 1)` (convention D, canonical
            # per the 2026-08-15 ruling R1). Bean qou-u5z0.
            "markov_parameter": "z = q**3 / (q**2 + 1)",
            "scope": "infra RHS construction; NOT a closure of the conjecture",
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    # Payload carries a top-level `assertions` mapping → stamp preserves it.
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(_HERE, "nuclear-quotient-jones-torus-link.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
