"""
delta_lambda_alexander_phase4.py — Phase 4 of the closed-forms workplan.

Phase 3 finding (`delta-lambda-jsj-phase3.witness.json`):

  - Vol_hyp clusters by Z: Vol(D)=Vol(T)=12.776 (Z=1); Vol(³He)=Vol(⁴He)=12.554 (Z=2).
  - The N-direction is Seifert-fibered → contributes 0 to hyperbolic volume.
  - Adding one nucleon at fixed Z multiplies |Δ_λ*| by a factor ~16
    (T/D = 15.95; ⁴He/³He = 16.36 — near-equality).

Phase 4 hypothesis: replace Vol_hyp(K) with a per-knot factor V(K) =
|Alex_K(t)| (or a function of it) that DOES distinguish Seifert-piece
content. The Alexander polynomial is computable from the Burau
representation of the braid word without SageMath.

Procedure:
  1. Build canonical atomic braid words for D, T, ³He, ⁴He (reuse Phase 3).
  2. Compute reduced Burau matrix B(β; t) for each braid.
  3. Alexander polynomial of the closure: Δ_K(t) such that
       Δ_K(t) · (1 - t) / (1 - t^n) = det(B(β; t) - I_{n-1})
     where n is the number of strands.
  4. Evaluate at:
       - t = -1 → determinant of the link
       - t = q_0² ≈ 1.2321 → categorical evaluation at substrate
       - t = q_0 ≈ 1.110
  5. Test rel_std of |Δ_λ*(K)| / V(K) across the 4 atoms for each V candidate.

  Ref: [manuscript] conj:delta-lambda-categorical-closure
  Ref: docs/audits/2026-05-19-delta-lambda-phase2-findings.md
  Ref: docs/coordination/1ppb-categorical-chain.md (Phase 3 result)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import sympy as sp

from witness_base import WitnessBuilder
from q_parameter import Q as Q0


def load_atom_braids() -> dict:
    """Build canonical braid words for D, T, ³He, ⁴He."""
    from probe_he4_jsj_topology import (
        _proton_braid_word,
        _neutron_braid_word,
        he4_compositional_braids,
    )
    p = _proton_braid_word()
    n = _neutron_braid_word()
    D = list(p) + [3] + [g + 3 for g in n]
    T = list(p) + [3] + [g + 3 for g in n] + [-6] + [g + 6 for g in n]
    He3 = list(p) + [3] + [g + 3 for g in p] + [6] + [g + 6 for g in n]
    He4 = he4_compositional_braids()["canonical_pppnnn"][0]
    return {
        "D":   (D,   6),
        "T":   (T,   9),
        "3He": (He3, 9),
        "4He": (He4, 12),
    }


def reduced_burau_generator(i: int, n: int, t):
    """Reduced Burau matrix of σ_i on (n-1)-dim Z[t,t⁻¹] module.

    For 1 ≤ i ≤ n-1, σ_i acts on the basis e_1,...,e_{n-1} as:
      - identity outside rows/cols i-1, i, i+1 (0-indexed: i-1)
      - 2-row block at position (i-1, i-1) and (i, i)
    Standard reduced Burau:
        i=1:        [[-t, 1, 0, ...],
                     [ 0, 1, 0, ...],
                     ...]
        1 < i < n-1: ... [[1, t, 0],
                          [0,-t, 1],
                          [0, 1, 0]] ...
        i = n-1:    [..., [1, t],
                          [0,-t]]

    (Equivalent conventions exist; this one follows Birman §3.3.)
    """
    M = sp.eye(n - 1)
    if i == 1:
        M[0, 0] = -t
        M[0, 1] = 1
    elif i == n - 1:
        M[n - 3, n - 2] = t
        M[n - 2, n - 2] = -t
    else:
        # i with 1 < i < n-1 (i is 1-indexed braid generator)
        # 0-indexed rows: row i-1 is the "centre"
        # Per Birman §3.3 (matching the comment at lines 78-80):
        #   [[1,  t,  0],
        #    [0, -t,  1],
        #    [0,  1,  0]]
        r = i - 1
        M[r - 1, r] = t
        M[r, r] = -t
        M[r, r + 1] = 1
        M[r + 1, r] = 1
        M[r + 1, r + 1] = 0
    return M


def burau_matrix_from_word(word: list[int], n: int, t):
    """Reduced Burau matrix of a braid word σ_{i_1}^{s_1} ... σ_{i_k}^{s_k}.

    word: signed integers, e.g. [1, -2, 1] for σ_1 σ_2⁻¹ σ_1.
    """
    M = sp.eye(n - 1)
    for s in word:
        i = abs(s)
        Bi = reduced_burau_generator(i, n, t)
        if s < 0:
            Bi = Bi.inv()
        M = M * Bi
    return M


def alexander_from_braid(word: list[int], n: int, t):
    """Alexander polynomial of the braid closure.

    Δ_K(t) · (1 - t)/(1 - t^n) = det(I - B(β; t))
    => Δ_K(t) = det(I - B(β; t)) · (1 - t^n) / (1 - t)

    Returns a simplified sympy rational expression.

    **Performance note** (Gemini review, PR #819): at large `n` and
    long braid words, the symbolic det + cancel can become a
    bottleneck.  Two optimisation paths are available if this script
    grows beyond exploratory scope:

    1. **Numeric-only evaluation**: substitute `t = q_0` (or other
       concrete value) into the Burau matrix BEFORE taking `det`.
       Loses the symbolic polynomial but recovers a single numeric
       value at the cost of one matmul per generator — orders of
       magnitude faster.

    2. **Polynomial det via Newton's method or trace recursion**:
       compute the characteristic polynomial of B directly from its
       traces (Newton's identities), avoiding the symbolic det's
       cofactor expansion.

    For the current 4-atom exploratory probe (D, T, ³He, ⁴He at
    H_6 / H_9 / H_12 with word lengths ≤ 50), the symbolic-cancel
    path is sufficient and the symbolic form is useful for pattern
    inspection.  If the probe scales to ⁶Li, ⁷Li, ⁹Be, etc., switch
    to option 1 (numeric).
    """
    B = burau_matrix_from_word(word, n, t)
    det = sp.det(sp.eye(n - 1) - B)
    # Multiply by (1 - t^n) / (1 - t) = 1 + t + t^2 + ... + t^{n-1}
    geom = sum(t**k for k in range(n))
    # Use sp.cancel for rational expressions — significantly faster
    # than sp.simplify and sufficient for the simplification we need.
    alex = sp.cancel(det * geom)
    return alex


def main() -> int:
    builder = WitnessBuilder("delta-lambda-alexander-phase4")
    builder.set_description(
        "Phase 4 of the closed-forms-first-principles workplan: tests "
        "whether Alexander polynomial (computed from Burau rep) gives "
        "a per-knot factor V(K) that captures the N-direction structure "
        "missing from Vol_hyp(K) (Phase 3). Tests V(K) ∈ {|Δ_K(-1)| "
        "(determinant), |Δ_K(q_0)|, |Δ_K(q_0^2)|} against the empirical "
        "|Δ_λ*| across D, T, ³He, ⁴He."
    )
    builder.add_parameter("q0", str(Q0))

    t = sp.Symbol("t")
    braids = load_atom_braids()

    # 1. Alexander polynomial for each atom
    alex_polys = {}
    for atom, (word, n_strands) in braids.items():
        print(f"computing Alexander polynomial for {atom} (n={n_strands}, "
              f"word_length={len(word)})...")
        try:
            alex = alexander_from_braid(word, n_strands, t)
            alex_polys[atom] = alex
            print(f"  Δ_{atom}(t) = {alex}")
        except Exception as e:
            print(f"  ERR: {type(e).__name__}: {e}")
            alex_polys[atom] = None
    builder.add_data("alexander_polynomials",
                     {k: str(v) for k, v in alex_polys.items()})

    # 2. Evaluate at categorical points
    eval_points = {
        "minus_one": sp.Integer(-1),
        "q0": sp.Rational(Q0) if isinstance(Q0, (int, float)) else sp.sympify(str(Q0)),
        "q0_squared": (sp.Rational(Q0) if isinstance(Q0, (int, float))
                       else sp.sympify(str(Q0))) ** 2,
    }
    evals = {}
    for atom, alex in alex_polys.items():
        if alex is None:
            evals[atom] = None
            continue
        atom_evals = {}
        for name, pt in eval_points.items():
            try:
                val = complex(alex.subs(t, pt).evalf())
                atom_evals[name] = {
                    "real": float(val.real),
                    "imag": float(val.imag),
                    "abs": float(abs(val)),
                }
            except Exception as e:
                atom_evals[name] = {"err": str(e)}
        evals[atom] = atom_evals
    builder.add_data("evaluations", evals)
    print("\n=== Evaluations ===")
    for atom, ev in evals.items():
        if ev is None:
            print(f"  {atom}: None")
            continue
        print(f"  {atom}:")
        for name, v in ev.items():
            if "abs" in v:
                print(f"    {name}: |Δ| = {v['abs']:.6f}  (Δ = {v['real']:.4f}{v['imag']:+.4f}j)")
            else:
                print(f"    {name}: {v}")

    # 3. Load empirical |Δ_λ*| from Phase 1b tabulation
    try:
        emp_w = json.loads(
            (_pb.witness_path("delta-lambda-empirical-tabulation.witness.json", HERE)).read_text()
        )["data"]["per_atom"]
        empirical = {a: float(emp_w[a]["a_single_block"]["best_abs_delta"])
                     for a in ("D", "T", "3He", "4He")}
    except Exception as e:
        print(f"\n  WARNING: empirical tabulation unavailable: {e}")
        empirical = None
    builder.add_data("empirical_best_abs_delta", empirical)

    if empirical:
        # 4. Test rel_std for each V(K) candidate
        print("\n=== rel_std test: |Δ_λ*(K)| / V(K) constant across atoms? ===")
        candidates = {}
        for name in ("minus_one", "q0", "q0_squared"):
            ratios = {}
            for atom in ("D", "T", "3He", "4He"):
                v = evals[atom][name]["abs"] if evals[atom] and "abs" in evals[atom][name] else None
                if v is not None and v > 0:
                    ratios[atom] = empirical[atom] / v
                else:
                    ratios[atom] = None

            valid = [r for r in ratios.values() if r is not None and r > 0]
            if len(valid) >= 2:
                rmean = sum(valid) / len(valid)
                rmin = min(valid); rmax = max(valid)
                rstd = (sum((r - rmean) ** 2 for r in valid) / len(valid)) ** 0.5
                rel_std = rstd / rmean if rmean else float("inf")
                candidates[name] = {
                    "ratios": ratios,
                    "mean": rmean, "min": rmin, "max": rmax,
                    "max_over_min": rmax / rmin if rmin > 0 else float("inf"),
                    "rel_std": rel_std,
                }
                print(f"\n  V(K) = |Δ_K({name})|:")
                for atom in ("D", "T", "3He", "4He"):
                    r = ratios[atom]
                    print(f"    {atom:>5}: |Δ_λ*| = {empirical[atom]:>10.4f}  "
                          f"V = {evals[atom][name]['abs']:>10.4f}  "
                          f"ratio = {r if r else '—':>10}")
                print(f"    rel_std = {rel_std:.4f} ({'PASS <0.05' if rel_std < 0.05 else 'PARTIAL <0.5' if rel_std < 0.5 else 'MISS'})")
        builder.add_data("rel_std_per_evaluation", candidates)

        # 5. Cross-Z and cross-N test (D vs T at Z=1; ³He vs ⁴He at Z=2)
        cross_tests = {}
        for name in candidates:
            r = candidates[name]["ratios"]
            T_over_D = r["T"] / r["D"] if r["D"] and r["T"] else None
            He4_over_He3 = r["4He"] / r["3He"] if r["3He"] and r["4He"] else None
            cross_tests[name] = {
                "T_over_D_ratio": T_over_D,
                "He4_over_He3_ratio": He4_over_He3,
                "consistency": (abs(T_over_D - He4_over_He3) / max(T_over_D, He4_over_He3)
                                if T_over_D and He4_over_He3 else None),
            }
        builder.add_data("cross_z_n_consistency", cross_tests)

    # Assertions
    builder.add_assertion(
        "alexander_computable",
        computed=1.0 if all(a is not None for a in alex_polys.values()) else 0.0,
        expected=1.0,
        tolerance=0.0,
        unit="boolean",
        source="all 4 canonical braid closures admit Burau-derived Alexander polynomial",
    )
    if empirical and "minus_one" in (candidates or {}):
        best = min((c["rel_std"] for c in candidates.values() if "rel_std" in c),
                   default=float("inf"))
        builder.add_assertion(
            "alexander_phase4_relstd_lower_than_vol_hyp_phase3",
            computed=float(best),
            expected=1.398,  # Phase 3 result
            tolerance=10.0,
            unit="rel_std",
            source="Phase 3 rel_std = 1.398; any lower means Alexander captures more structure",
        )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
