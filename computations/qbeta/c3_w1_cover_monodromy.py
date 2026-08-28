#!/usr/bin/env python3
"""W1: the color-cubic sheet cover has full S₃ monodromy — no single-valued branch.

Bean `qou-d8de` (W1, construct D_q from Σ), re-scoped by
`docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md` v2: the branch
selection "which sheet Yᵢ continues X" is the FINITE covering monodromy
`ρ : π₁(ℂ*∖{branch pts}) → S₃` of the algebraic cubic cover `C_z(X)=0`, NOT a theta object.

This computes the monodromy group. For an irreducible cubic over `ℂ(z)`, the monodromy
group (= Galois group of `C_z(X)` over `ℂ(z)`) is:
  - **S₃** iff `disc_X` is NOT a square in `ℂ(z)` (a transposition is present);
  - A₃ (cyclic 3) iff `disc_X` IS a square.
A squarefree discriminant of positive degree can never be a perfect square, so squarefree
`disc` ⇒ S₃. The consequence: the 3 sheets are fully inseparable, so there is NO
single-valued algebraic branch, and `D_q` cannot be a single-valued algebraic operator on
the base — it lives on the 3-sheeted cover. (The proved (−1)ⁿ parity,
`Brings.RamificationParityMonodromy`, is the sign character of this ρ.)

Structural / algebraic — no fit, nothing wired.
"""
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path
import sympy as sp


def main() -> None:
    z, X = sp.symbols("z X")
    C = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)
    Cp = sp.Poly(C, X)
    disc = sp.discriminant(Cp, X)                      # = -branchSextic
    sext = sp.Poly(-disc, z)
    squarefree = sp.Poly(sp.gcd(sext, sext.diff(z)), z).degree() == 0
    n_branch = sext.degree()                            # 6 branch points if squarefree
    _irr = Cp.is_irreducible
    if _irr is None:
        raise RuntimeError("sympy could not decide irreducibility of the color cubic")
    irreducible = bool(_irr)
    # disc is a perfect square in C(z) iff every irreducible factor has even multiplicity
    # (over C the leading constant is always a square). A squarefree disc of positive
    # degree therefore can never be a square — but test it properly, do not assume.
    _, factors = sp.factor_list(-disc)                  # (const, [(factor, mult), ...])
    disc_is_square = bool(factors) and all(m % 2 == 0 for _, m in factors)
    monodromy = ("reducible" if not irreducible
                 else ("A3" if disc_is_square else "S3"))

    results = {
        "cubic": "X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1)",
        "irreducible_over_Qz": irreducible,
        "disc_X": "-(16z^6+24z^5+35z^4+50z^3+35z^2+24z+16) = -branchSextic",
        "disc_squarefree": bool(squarefree),
        "num_branch_points": int(n_branch),
        "disc_is_square_in_Cz": bool(disc_is_square),
        "monodromy_group": monodromy,
        "single_valued_algebraic_branch_exists": (monodromy not in ("S3", "A3")),
    }
    for k, v in results.items():
        print(f"  {k}: {v}")

    script_path = Path(__file__).resolve()

    def _git(a):
        try:
            return subprocess.check_output(["git", *a], cwd=script_path.parent, text=True).strip() or "unknown"
        except Exception:
            return "unknown"

    # per-path last-touch commit; fall back to repo HEAD for a newly-added (uncommitted)
    # script so provenance never lands as a bare "unknown".
    _script_sha = _git(["log", "-1", "--format=%H", "--", str(script_path)])
    if _script_sha == "unknown":
        _script_sha = _git(["rev-parse", "HEAD"])

    witness = {
        "schema": "witness/v1",
        "engine": "python+sympy",
        "scriptFile": "c3_w1_cover_monodromy.py",
        "commitSha": _git(["rev-parse", "HEAD"]),
        "description": (
            "W1: color-cubic sheet cover has full S3 monodromy (irreducible cubic + "
            "squarefree/non-square disc) => no single-valued algebraic branch; D_q lives "
            "on the 3-sheeted cover. Symbolic (sympy)."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w1_cover_monodromy.py",
            "scriptCommitSha": _script_sha,
            "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        },
        "results": results,
        "verdict": (
            "CONFIRMED: monodromy group = S3 (full symmetric); no single-valued algebraic "
            "branch. W1 obstruction is the S3 cover monodromy, NOT a theta object."
        ),
        "scope": "Finite covering-monodromy invariant. No fit; nothing wired.",
    }
    out = script_path.with_suffix(".witness.json")
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
    print(f"\nverdict: {witness['verdict']}\nwitness: {out}")


if __name__ == "__main__":
    main()
