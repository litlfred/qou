"""Closure-b step 2g/3 — ρ_ξ⊗ρ_ν gauge alignment + H_9 universality (WIP).

Builds on the verified step-2 result (PR #2353): the analytic interface operator
A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν} reconstructs χ^λ exactly (deuteron, 1.5e-49).
This module adds the remaining pieces toward feeding the combiner / unlocking
A ≥ 3:

  2g. Express A^λ_{ξν}(I) as a (d_ξ·d_ν)×(d_ξ·d_ν) matrix in V_ξ⊗V_ν
      coordinates (gauge alignment) — a basis-change of range(Π_{ξν}).
  3.  Construct A at H_9 and reconstruct tr_M(T)/tr_M(³He) (the case the
      least-squares fit misses by 21–42 %).

## Verified building block in this file

`range_basis_and_restricted_gens` constructs, per (ξ,ν), an orthonormal basis Q
of range(Π_{ξν}) (the invariant subspace) and the restricted generators
g̃ = Qᵀ ρ_λ(g) Q. Because range(Π_{ξν}) is invariant under the inner H_3
(⟨σ_0,σ_1⟩) and block H_3 (⟨σ_3,σ_4⟩) — both commute with Π_{ξν} — the
compression Qᵀ σ Q IS the genuine restriction. Verified properties (exact, 50 dps):
  - Q orthonormal (QᵀQ = I_m, m = c·d_ξ·d_ν);
  - restricted inner/block generators satisfy the Hecke relation
    (g̃ − q)(g̃ + q⁻¹) = 0;
  - the inner class-sum acts as the scalar e_ξ on range (ξ-isotypic), the block
    class-sum as e_ν (ν-isotypic) — confirming the (ξ,ν) labelling.

## Remaining (TODO closure-b — precise spec)

The gauge-aligning isometry U_{ξν}: V_ξ⊗V_ν⊗ℂ^c → range(Π_{ξν}) must satisfy
  Uᵀ ρ_λ(g_in) U = ρ_ξ(g)⊗I_ν⊗I_c,   Uᵀ ρ_λ(g_bl) U = I_ξ⊗ρ_ν(g)⊗I_c,
with ρ_ξ, ρ_ν from `seminormal_matrices_mpfr` at H_3. Construction (exact):
  (i)  Young seminormal matrix units E^ξ_{tt'} of the inner H_3 on Q (polynomials
       in the restricted inner generators) expose the V_ξ factor;
  (ii) within a fixed inner idempotent's range, the block H_3 matrix units E^ν
       expose V_ν; the residual degeneracy is the multiplicity ℂ^c;
  (iii) A_full = Uᵀ (Π_{ξν} ρ_λ(I) Π_{ξν}) U  [(d_ξ d_ν c)²];
        A_combiner = partial-trace over ℂ^c.
Verification target: Σ_{ξν} Tr[A_combiner·(ρ_ξ(W)⊗ρ_ν(β))] = χ^λ(W·I·β) at
1e-25, with ρ_ξ(W), ρ_ν(β) evaluated at H_3 (the speedup — small dim). Internal
consistency only is needed (same seminormal source on both sides); matching the
legacy fitted extract entrywise is optional.

Design: docs/audits/2026-06-16-analytic-interface-operator-closure-b-design.md
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from lr_coefficients import partitions_of  # noqa: E402
import a_operator_analytic as aoa  # noqa: E402

EXACT_TOL = mp.mpf("1e-25")


def _orthonormal_range_basis(P: "mp.matrix", rank: int) -> "mp.matrix":
    """Orthonormal basis (dim×rank) of the column space of the idempotent P.

    P = Π_{ξν} = P_in·P_bl is an OBLIQUE (non-Hermitian) idempotent — a product
    of spectral projectors of non-normal class-sums — so a plain QR's leading
    columns need not span range(P). Use the SVD: range(P) is spanned by the left
    singular vectors with nonzero singular value (the leading `rank` columns of
    U, since the singular values are returned in descending order)."""
    U, S, _V = mp.svd(P)
    dim = P.rows
    out = mp.zeros(dim, rank)
    for i in range(dim):
        for j in range(rank):
            out[i, j] = U[i, j]
    return out


def _compress(Q: "mp.matrix", M: "mp.matrix") -> "mp.matrix":
    """Restriction Qᵀ M Q of M to the invariant subspace spanned by Q."""
    return Q.T * M * Q


def range_basis_and_restricted_gens(lam: tuple[int, ...], q_str: str,
                                    dps: int) -> dict:
    """Per (ξ,ν): orthonormal basis Q of range(Π_{ξν}) and restricted inner /
    block generators. Returns a dict keyed (ξ,ν) with verified diagnostics."""
    mp.mp.dps = dps + 10
    q = mp.mpf(q_str)
    mats, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
    if dim == 0:
        return {}
    ev = aoa._h3_class_sum_eigenvalues(q_str, dps)
    C_in = aoa._class_sum_C2(mats, 0, 1)
    C_bl = aoa._class_sum_C2(mats, 3, 4)
    P_in = aoa._lagrange_projectors(C_in, ev, dim)
    P_bl = aoa._lagrange_projectors(C_bl, ev, dim)
    I = mp.eye(dim)
    out = {}
    for xi in ev:
        for nu in ev:
            Pi = P_in[xi] * P_bl[nu]
            r = int(mp.nint(aoa._trace(Pi)).real)
            if r == 0:
                continue
            Q = _orthonormal_range_basis(Pi, r)
            inner = [_compress(Q, mats[0]), _compress(Q, mats[1])]
            block = [_compress(Q, mats[3]), _compress(Q, mats[4])]
            out[(xi, nu)] = {
                "rank": r, "Q": Q, "inner": inner, "block": block,
            }
    return out


def verify_restricted_gens(dps: int = 50) -> dict:
    """Verify (deuteron H_6, exact): Q orthonormal; restricted inner/block gens
    satisfy the Hecke relation; inner/block class-sums act as the scalars
    e_ξ / e_ν on each range (confirming the (ξ,ν) isotypic labelling)."""
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    ev = aoa._h3_class_sum_eigenvalues(q_str, dps)
    max_ortho = mp.mpf(0)
    max_hecke = mp.mpf(0)
    max_iso = mp.mpf(0)
    n_blocks = 0
    for lam in partitions_of(6):
        info = range_basis_and_restricted_gens(lam, q_str, dps)
        for (xi, nu), d in info.items():
            n_blocks += 1
            Q, r = d["Q"], d["rank"]
            Ir = mp.eye(r)
            # Orthonormality QᵀQ = I_r
            G = Q.T * Q
            max_ortho = max(max_ortho,
                            max(abs(G[i, j] - Ir[i, j])
                                for i in range(r) for j in range(r)))
            # Hecke relation on each restricted generator
            for g in d["inner"] + d["block"]:
                rel = (g - q * Ir) * (g + (1 / q) * Ir)
                max_hecke = max(max_hecke,
                                max(abs(rel[i, j])
                                    for i in range(r) for j in range(r)))
            # Isotypic: inner class-sum = e_ξ·I_r ; block class-sum = e_ν·I_r
            si0, si1 = d["inner"]
            sb0, sb1 = d["block"]
            C_in_r = si0 + si1 + si0 * si1 * si0
            C_bl_r = sb0 + sb1 + sb0 * sb1 * sb0
            max_iso = max(max_iso,
                          max(abs(C_in_r[i, j] - (ev[xi] if i == j else 0))
                              for i in range(r) for j in range(r)),
                          max(abs(C_bl_r[i, j] - (ev[nu] if i == j else 0))
                              for i in range(r) for j in range(r)))
    passed = (max_ortho < EXACT_TOL and max_hecke < EXACT_TOL
              and max_iso < EXACT_TOL)
    return {
        "n_blocks": n_blocks,
        "max_orthonormality_residual": mp.nstr(max_ortho, 6),
        "max_hecke_relation_residual": mp.nstr(max_hecke, 6),
        "max_isotypic_residual": mp.nstr(max_iso, 6),
        "tolerance": mp.nstr(EXACT_TOL, 4),
        "all_passed": passed,
    }


def verify_isotypic_multiplicity_structure(dps: int = 50) -> dict:
    """Verify (deuteron H_6, exact) that range(Π_{ξν}) decomposes as
    V_ξ ⊗ V_ν ⊗ ℂ^c with the correct multiplicity c = c^λ_{ξν}.

    Method (convention-free — no Jucys-Murphy needed): the inner factor ρ_ξ is
    irreducible, so the restricted inner algebra ⟨σ̃_0,σ̃_1⟩ is the full matrix
    algebra M_{d_ξ} acting as ρ_ξ⊗I_{c d_ν}. A *generic* inner element therefore
    has d_ξ distinct eigenvalues, each of multiplicity c·d_ν; a generic block
    element has d_ν distinct, each mult c·d_ξ. Since inner ⊥ block (commute), a
    generic M = G_in + φ·G_bl has exactly **d_ξ·d_ν distinct eigenvalues, each
    of multiplicity c** — which must equal the LR coefficient c^λ_{ξν}.
    """
    from lr_coefficients import get_lr_table
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    lr = get_lr_table(3, 3)
    # Irrational generic coefficients (avoid accidental degeneracy).
    a1, a2, b1, b2, phi = mp.sqrt(2), mp.sqrt(3), mp.pi, mp.sqrt(5), mp.e
    clust_tol = mp.mpf("1e-18")
    n_blocks = 0
    n_fail = 0
    failures = []
    for lam in partitions_of(6):
        info = range_basis_and_restricted_gens(lam, q_str, dps)
        for (xi, nu), d in info.items():
            n_blocks += 1
            si0, si1 = d["inner"]
            sb0, sb1 = d["block"]
            G_in = si0 + a1 * si1 + a2 * (si0 * si1)
            G_bl = sb0 + b1 * sb1 + b2 * (sb0 * sb1)
            M = G_in + phi * G_bl
            E, _ER = mp.eig(M)
            clusters: list[list] = []
            for e in E:
                for cl in clusters:
                    if abs(e - cl[0]) < clust_tol:
                        cl.append(e)
                        break
                else:
                    clusters.append([e])
            sizes = sorted(len(cl) for cl in clusters)
            c_lr = lr.get((xi, nu, lam), 0)
            expect_n = aoa.partition_dim(xi) * aoa.partition_dim(nu)
            ok = (len(clusters) == expect_n and sizes == [c_lr] * expect_n)
            if not ok:
                n_fail += 1
                if len(failures) < 5:
                    failures.append({
                        "lambda": list(lam), "xi": list(xi), "nu": list(nu),
                        "n_distinct": len(clusters), "expect_distinct": expect_n,
                        "cluster_sizes": sizes, "c_lr": c_lr})
    return {
        "n_blocks": n_blocks, "n_fail": n_fail,
        "all_passed": n_fail == 0, "failures": failures,
        "method": "generic inner+block eigenvalue multiplicities vs c^λ_ξν",
    }


def main() -> int:
    dps = 50
    print("=" * 78)
    print("  Closure-b step 2g/3 — gauge-alignment building blocks (WIP)")
    print("=" * 78)
    res = verify_restricted_gens(dps)
    print(f"  [a] range-basis + restricted generators (deuteron H_6, {res['n_blocks']} blocks):")
    print(f"      orthonormality   max residual = {res['max_orthonormality_residual']}")
    print(f"      Hecke relation   max residual = {res['max_hecke_relation_residual']}")
    print(f"      isotypic e_ξ/e_ν max residual = {res['max_isotypic_residual']}")
    print(f"      → {'PASS' if res['all_passed'] else 'FAIL'} (tol {res['tolerance']})")
    print()
    mres = verify_isotypic_multiplicity_structure(dps)
    print(f"  [b] V_ξ⊗V_ν⊗ℂ^c multiplicity structure ({mres['n_blocks']} blocks):")
    print(f"      joint-weight count + multiplicities vs c^λ_ξν")
    print(f"      → {'PASS' if mres['all_passed'] else 'FAIL'} ({mres['n_fail']} fail)")
    for f in mres["failures"]:
        print(f"        FAIL {f}")
    print()
    print("  TODO(closure-b): phase-aligned ladder → U → A_combiner (partial trace) → H_9.")
    return 0 if (res["all_passed"] and mres["all_passed"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
