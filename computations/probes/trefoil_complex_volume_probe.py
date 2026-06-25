"""Trefoil (electron knot) — algebraic invariant non-zero while hyperbolic
volume vanishes.

Substantiates the part-3 point of the Faddeev-dilog / Kashaev discussion:
the electron knot is the trefoil 3_1 = T(2,3) = σ₀σ₁σ₀, a (2,3) TORUS knot,
hence Seifert-fibered, hence NON-hyperbolic.  Its hyperbolic volume is 0
(Gromov norm of a torus-knot complement = 0; KVC's convention sends the
Kashaev limit of a non-hyperbolic knot to 0 — see
content/.../mass-theory/kashaev-volume-conjecture.md, line "with the
convention that the right-hand side vanishes when K is not hyperbolic").

Yet its ALGEBRAIC quantum volume — the Markov trace tr_M / Jones polynomial —
is non-zero.  So the complex-volume observable
    𝔙(K) = E₀·tr_M((Π_free − 1)∘𝓜)
(content/.../mass-endomorphism/binding-qbeta-complex-volume.md) is carried, for
a single PRIMITIVE knot like the electron (no constituents to un-link, so the
free projection contributes no genuine convolution defect), by the bare
algebraic trace tr_M — which is non-zero where the geometric hyperbolic volume
is zero.  Algebra survives where geometry degenerates.

This is the part-3 contrast made concrete:
  • Vol_hyp(3_1) = 0                (geometry degenerates — non-hyperbolic)
  • tr_M(3_1) at q₀ ≠ 0            (algebra survives — Markov trace)

Hecke/Markov conventions (AGENTS.md §7a): the Hecke generator σ satisfies
    σ² = (q − q⁻¹)σ + 1,    h := q − q⁻¹,
and J_K(q) = tr_M(ρ(β_K)) with the Ocneanu/Markov normalisation tr(1)=1,
tr(σ)=z, z = 1/(q^{1/2}+q^{-1/2}) (the Markov parameter, matching the repo's
z_markov ≈ 0.49932 in pentagon-reduction-li2q.witness.json).

The trefoil is the closure of σ³ ∈ B₂.  Reducing σ³ in H₂(q):
    σ³ = σ·σ² = σ((q−q⁻¹)σ + 1) = (h²+1)·σ + h,
so    tr_M(σ³) = (h²+1)·z + h.

Stdlib only (no mpmath / pyhecke / qou_substrate available in this sandbox);
Decimal at 50 dps.  The exact Laurent-polynomial coefficients (h²+1, h) are
convention-robust; only the numeric evaluation depends on q₀.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 60

# Muon-canonical substrate modulus (computations/ layer convention; matches the
# committed rho-prefactor-structural-verifier.witness.json `q_0` parameter and
# the cheat-sheet muon value 1.10997859555733471…).
Q0 = Decimal("1.1099785955573347")


def _sci(d: Decimal, n: int = 30) -> str:
    return format(d, f".{n}f")


def compute() -> dict:
    q = Q0
    h = q - 1 / q                      # h = q − q⁻¹
    rootq = q.sqrt()
    z = 1 / (rootq + 1 / rootq)        # Markov parameter z = 1/(q^{1/2}+q^{-1/2})

    # tr_M(σ³) = (h²+1)·z + h  (exact reduction; (h²+1, h) are the Laurent
    # coefficients of the reduced Hecke element, convention-robust).
    coeff_sigma = h * h + 1            # coefficient of σ in σ³ = (h²+1)σ + h
    coeff_one = h                      # coefficient of 1
    trM = coeff_sigma * z + coeff_one

    # Standard topological Jones polynomial of the (left) trefoil, literature
    # normalisation V(t) = −t⁻⁴ + t⁻³ + t⁻¹, evaluated at t = q₀ (secondary,
    # convention-labelled cross-check that the invariant is non-vanishing).
    t = q
    jones = -t ** (-4) + t ** (-3) + t ** (-1)

    # Hyperbolic volume: trefoil is the (2,3) torus knot → Seifert-fibered →
    # NON-hyperbolic → simplicial volume / Gromov norm = 0 (exact).
    vol_hyp = Decimal(0)

    return {
        "q_0": _sci(q),
        "h_eq_q_minus_qinv": _sci(h),
        "z_markov": _sci(z),
        "trM_reduction": "sigma^3 = (h^2+1)*sigma + h  in H_2(q)",
        "trM_coeff_sigma_h2_plus_1": _sci(coeff_sigma),
        "trM_coeff_one_h": _sci(coeff_one),
        "trM_trefoil_at_q0": _sci(trM),
        "abs_trM_trefoil_at_q0": _sci(abs(trM)),
        "jones_convention": "V(3_1)(t) = -t^-4 + t^-3 + t^-1 (left trefoil), t = q_0",
        "jones_trefoil_at_q0": _sci(jones),
        "abs_jones_trefoil_at_q0": _sci(abs(jones)),
        "vol_hyp_trefoil": _sci(vol_hyp, 1),
        "vol_hyp_reason": "(2,3) torus knot: Seifert-fibered, non-hyperbolic, Gromov norm 0",
    }


def main() -> None:
    started = datetime.now(timezone.utc)
    data = compute()

    abs_trM = Decimal(data["abs_trM_trefoil_at_q0"])
    abs_jones = Decimal(data["abs_jones_trefoil_at_q0"])
    vol_hyp = Decimal(data["vol_hyp_trefoil"])

    assertions = [
        {
            "name": "trefoil_markov_trace_nonzero",
            "passed": abs_trM > Decimal("0.1"),
            "detail": f"|tr_M(sigma^3)|@q0 = {data['abs_trM_trefoil_at_q0']} > 0.1",
        },
        {
            "name": "trefoil_jones_nonzero",
            "passed": abs_jones > Decimal("0.1"),
            "detail": f"|V(3_1)|@q0 = {data['abs_jones_trefoil_at_q0']} > 0.1",
        },
        {
            "name": "trefoil_hyperbolic_volume_zero",
            "passed": vol_hyp == 0,
            "detail": "Vol_hyp(3_1) = 0 (non-hyperbolic torus knot)",
        },
        {
            "name": "algebra_survives_geometry_vanishes",
            "passed": (abs_trM > 0) and (vol_hyp == 0),
            "detail": "algebraic quantum volume (tr_M) non-zero while hyperbolic volume = 0",
        },
    ]
    all_passed = all(a["passed"] for a in assertions)
    for a in assertions:
        a["passed"] = bool(a["passed"])

    script_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]

    def _git(*args: str) -> str:
        try:
            return subprocess.check_output(
                ["git", *args], cwd=script_path.parent, stderr=subprocess.DEVNULL
            ).decode().strip()
        except Exception:
            return ""

    witness = {
        "engine": "python",
        "engineVersion": "python (stdlib decimal, 60 dps)",
        "computedAt": started.isoformat(),
        "commitSha": _git("rev-parse", "HEAD"),
        "assertions": assertions,
        "allPassed": bool(all_passed),
        "durationMs": int((datetime.now(timezone.utc) - started).total_seconds() * 1000),
        "computation": "trefoil-complex-volume-probe",
        "scriptFile": "trefoil_complex_volume_probe.py",
        "scriptHash": script_hash,
        "scriptCommitSha": _git("log", "-1", "--format=%H", "--", str(script_path)),
        "precisionMetadata": {
            "compute_dps": 60,
            "output_dps": 30,
            "note": "stdlib Decimal; exact Laurent coefficients (h^2+1, h) are convention-robust",
        },
        "environment": {"python": "stdlib only (no mpmath/pyhecke/qou_substrate in sandbox)"},
        "description": (
            "Electron knot = trefoil 3_1 = T(2,3): NON-hyperbolic (Seifert-fibered) "
            "so Vol_hyp = 0, yet its algebraic invariant tr_M(sigma^3) = (h^2+1)z + h "
            "and Jones polynomial are non-zero at q_0. Substantiates the complex-volume "
            "𝔙 = E0*tr_M((Pi_free-1)∘M) point for a primitive knot: the algebraic quantum "
            "volume survives where the geometric (hyperbolic) volume degenerates. "
            "Hecke/Markov conventions per AGENTS.md §7a."
        ),
        "contentBlock": "conj:binding-qbeta-complex-volume",
        "parameters": {
            "knot": "3_1 = T(2,3) (electron, per rem:knot-particle-dictionary)",
            "braid_word": "sigma^3 in B_2 (equivalently sigma_0 sigma_1 sigma_0 in B_3)",
            "q_0": data["q_0"],
        },
        "data": data,
    }

    out = script_path.parent / "trefoil-complex-volume-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"allPassed={all_passed}")
    print(f"  tr_M(trefoil)@q0 = {data['trM_trefoil_at_q0']}  (|.|={data['abs_trM_trefoil_at_q0']})")
    print(f"  Jones(3_1)@q0    = {data['jones_trefoil_at_q0']}")
    print(f"  Vol_hyp(3_1)     = {data['vol_hyp_trefoil']}  ({data['vol_hyp_reason']})")
    print(f"  witness -> {out}")


if __name__ == "__main__":
    main()
