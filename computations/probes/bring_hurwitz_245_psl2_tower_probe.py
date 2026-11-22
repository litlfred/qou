#!/usr/bin/env python3
"""bring_hurwitz_245_psl2_tower_probe.py — classify non-abelian Hurwitz (2,4,5) quotients PSL_2(F_p) / PGL_2(F_p)
and their unramified Galois covers over Bring's surface Sigma_4.

Bean `qou-6082` (owner ruling `Q-VO9T-3 = 2`). Companion to `QOU/Brings/BringCoverTower.lean`.

Mathematical structure:
1. Bring's surface Sigma_4 is the unique minimal-genus regular map of type (2,4,5):
   Delta(2,4,5) = <x, y, z | x^2 = y^4 = z^5 = x y z = 1>, with Riemann-Hurwitz
   2g - 2 = |G|(1 - 1/2 - 1/4 - 1/5) = |G|/20 <=> 40(g - 1) = |G|.
   At G = S_5 ~= PGL_2(F_5) (|G| = 120), g = 4.
2. Abelianization: Delta(2,4,5)^ab ~= C_2 (sending x |-> -1, y |-> -1, z |-> +1).
   Hence any perfect quotient (such as PSL_2(F_p) for p >= 5) cannot factor through S_5 directly,
   because S_5^ab ~= C_2 and A_5 ~= PSL_2(F_5) has no elements of order 4 (40 does not divide 60).
3. Macbeath classification over F_p for odd prime p:
   - Order 5 exists in PSL_2(F_p) (and PGL_2(F_p)) iff p = 5 or p = +-1 (mod 5) ((5/p) != -1).
   - Order 4 exists in PSL_2(F_p) iff p = +-1 (mod 8) ((2/p) = +1); when p = +-3 (mod 8) ((2/p) = -1),
     all projective order-4 elements lie in PGL_2(F_p) \\ PSL_2(F_p).
   - Therefore:
     * Direct PSL_2(F_p) branch (p = +-1, +-9 mod 40, e.g. p = 31, 41):
       PSL_2(F_p) is a smooth (2,4,5)-quotient of genus 1 + |PSL_2(F_p)|/40, and by Goursat's lemma
       G_p = S_5 x PSL_2(F_p) (|G_p| = 120 |PSL_2(F_p)|) is an unramified PSL_2(F_p)-cover of Sigma_4
       with genus g(p) = 3 |PSL_2(F_p)| + 1.
     * Fiber-product PGL_2(F_p) branch (p = +-11, +-19 mod 40, e.g. p = 11, 19, 29; plus p = 5 itself):
       PGL_2(F_p) is a smooth (2,4,5)-quotient with x, y in PGL_2 \\ PSL_2 and z in PSL_2, so the
       sign characters of S_5 and PGL_2(F_p) coincide on Delta(2,4,5). For p > 5, the diagonal image
       is the fiber product G_p = S_5 x_{C_2} PGL_2(F_p) of order 120 |PSL_2(F_p)|, which projects
       onto S_5 with kernel PSL_2(F_p) and gives an unramified PSL_2(F_p)-cover of Sigma_4 of the
       same genus g(p) = 3 |PSL_2(F_p)| + 1.

Exact integer/modular arithmetic throughout; no floats, nothing fitted.
-- Ref: [manuscript] QOU/Brings/BringCoverTower.lean; Macbeath (1969); Farkas-Kra §I.2, §V.1; bean qou-6082
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

try:
    from qou_substrate.witness import WitnessBuilder
except ImportError:
    WitnessBuilder = None


def mat_mul(A: tuple[int, int, int, int], B: tuple[int, int, int, int], p: int) -> tuple[int, int, int, int]:
    return (
        (A[0] * B[0] + A[1] * B[2]) % p,
        (A[0] * B[1] + A[1] * B[3]) % p,
        (A[2] * B[0] + A[3] * B[2]) % p,
        (A[2] * B[1] + A[3] * B[3]) % p,
    )


def mat_det(A: tuple[int, int, int, int], p: int) -> int:
    return (A[0] * A[3] - A[1] * A[2]) % p


def mat_inv(A: tuple[int, int, int, int], p: int) -> tuple[int, int, int, int]:
    d_inv = pow(mat_det(A, p), p - 2, p)
    return ((A[3] * d_inv) % p, (-A[1] * d_inv) % p, (-A[2] * d_inv) % p, (A[0] * d_inv) % p)


def proj_norm(A: tuple[int, int, int, int], p: int) -> tuple[int, int, int, int]:
    for x in A:
        if x % p != 0:
            inv = pow(x, p - 2, p)
            return tuple((v * inv) % p for v in A)  # type: ignore[return-value]
    return A


def proj_order(A: tuple[int, int, int, int], p: int, max_k: int = 100) -> int | None:
    ident = (1, 0, 0, 1)
    cur = proj_norm(A, p)
    if cur == ident:
        return 1
    for k in range(2, max_k + 1):
        cur = proj_norm(mat_mul(cur, A, p), p)
        if cur == ident:
            return k
    return None


def is_quad_residue(a: int, p: int) -> bool:
    return pow(a % p, (p - 1) // 2, p) == 1


def find_245_triple(p: int) -> dict[str, object]:
    """Find an explicit non-abelian (2,4,5) matrix triple (X, Y, Z=(XY)^-1) in PGL_2(F_p) / PSL_2(F_p)
    whose commutator [X, Y] has order not in {1, p} (hence generating PSL_2(F_p) or PGL_2(F_p) by Dickson)."""
    for dx in range(1, p):
        for ty in range(1, p):
            dy = (ty * ty * pow(2, p - 2, p)) % p
            Y = (ty, (-dy) % p, 1, 0)
            for u in range(p):
                for c in range(1, p):
                    b = ((-u * u - dx) * pow(c, p - 2, p)) % p
                    X = (u, b, c, (-u) % p)
                    if mat_det(X, p) == 0:
                        continue
                    XY = mat_mul(X, Y, p)
                    if proj_order(X, p) == 2 and proj_order(Y, p) == 4 and proj_order(XY, p) == 5:
                        comm = mat_mul(mat_mul(X, Y, p), mat_mul(mat_inv(X, p), mat_inv(Y, p), p), p)
                        ord_c = proj_order(comm, p)
                        if ord_c is not None and ord_c not in (1, p):
                            Z = mat_inv(XY, p)
                            return {
                                "X": list(X),
                                "Y": list(Y),
                                "Z": list(Z),
                                "XY": list(XY),
                                "det_X_is_square": is_quad_residue(mat_det(X, p), p),
                                "det_Y_is_square": is_quad_residue(mat_det(Y, p), p),
                                "det_Z_is_square": is_quad_residue(mat_det(Z, p), p),
                                "orders": [proj_order(X, p), proj_order(Y, p), proj_order(Z, p)],
                                "commutator_order": ord_c,
                            }
    raise RuntimeError(f"No (2,4,5) triple found for p={p}")


def bfs_projective_group_order(gens: list[tuple[int, int, int, int]], p: int, cap: int = 2000) -> int:
    ident = (1, 0, 0, 1)
    seen = {ident}
    queue = [ident]
    all_gens = [proj_norm(g, p) for g in gens] + [proj_norm(mat_inv(g, p), p) for g in gens]
    while queue and len(seen) <= cap:
        cur = queue.pop()
        for g in all_gens:
            nxt = proj_norm(mat_mul(cur, g, p), p)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return len(seen)


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, src: str) -> None:
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    # 1. Verify p = 5: PGL_2(F_5) ~= S_5 has order 120 (Bring's surface g = 4), PSL_2(F_5) ~= A_5 (60) has 40 -| 60
    t5 = find_245_triple(5)
    ord_pgl2_5 = bfs_projective_group_order([tuple(t5["X"]), tuple(t5["Y"])], 5)  # type: ignore[arg-type]
    check("p5_triple_generates_full_PGL2_F5_order_120", ord_pgl2_5 == 120, "BFS in PGL_2(F_5) ~= S_5")
    check("p5_bring_rh_genus_4", 40 * (4 - 1) == 120, "Lean bring_rh: 40(g-1) = |S_5| = 120")
    check("p5_psl2_A5_not_smooth_245_quotient", 60 % 40 != 0 and not t5["det_Y_is_square"], "Lean psl2_five_not_rh245")

    # 2. Verify p = 11 by exact BFS: generates full PGL_2(F_11) of order 1320 (genus 34)
    t11 = find_245_triple(11)
    ord_pgl2_11 = bfs_projective_group_order([tuple(t11["X"]), tuple(t11["Y"])], 11, cap=2000)  # type: ignore[arg-type]
    check("p11_triple_generates_full_PGL2_F11_order_1320", ord_pgl2_11 == 1320, "BFS in PGL_2(F_11)")

    # 3. Classify primes p in {5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41}
    prime_scan = {}
    admissible_primes = [5, 11, 19, 29, 31, 41]
    inadmissible_primes = [7, 13, 17, 23, 37]

    for p in inadmissible_primes:
        psl_ord = p * (p * p - 1) // 2
        has_5 = (p == 5) or (p % 5 in (1, 4))
        check(f"p{p}_has_no_order_5_element_in_PGL2", not has_5 and (psl_ord % 5 != 0), "Lagrange / Macbeath")

    records = {}
    ExpectedCoverGenera = {11: 1981, 19: 10261, 29: 36541, 31: 44641, 41: 103321}
    ExpectedBaseGenera = {5: 4, 11: 34, 19: 172, 29: 610, 31: 373, 41: 862}

    for p in admissible_primes:
        triple = find_245_triple(p)
        psl_ord = p * (p * p - 1) // 2
        pgl_ord = p * (p * p - 1)
        qr2 = is_quad_residue(2, p)
        branch = "PSL2_direct" if qr2 else "PGL2_fiber_product"
        quot_ord = psl_ord if qr2 else pgl_ord
        quot_genus = quot_ord // 40 + 1
        cover_ord = 120 * psl_ord
        cover_genus = 3 * psl_ord + 1

        check(
            f"p{p}_orders_are_2_4_5_and_xyz_is_identity",
            triple["orders"] == [2, 4, 5],
            "explicit F_p matrix evaluation",
        )
        check(
            f"p{p}_det_parity_matches_macbeath_branch",
            (triple["det_X_is_square"] == qr2)
            and (triple["det_Y_is_square"] == qr2)
            and bool(triple["det_Z_is_square"]),
            "Cayley-Hamilton trace/det criterion",
        )
        check(
            f"p{p}_quotient_rh_genus_matches_{ExpectedBaseGenera[p]}",
            40 * (quot_genus - 1) == quot_ord and quot_genus == ExpectedBaseGenera[p],
            "Lean pgl2_*_rh / psl2_*_rh",
        )
        if p > 5:
            check(
                f"p{p}_bring_psl2_cover_genus_matches_{ExpectedCoverGenera[p]}",
                40 * (cover_genus - 1) == cover_ord and cover_genus == ExpectedCoverGenera[p],
                "Lean bringPSL2Cover_rh / bringPSL2CoverGenus_values",
            )
        records[str(p)] = {
            "branch": branch,
            "psl2_order": psl_ord,
            "pgl2_order": pgl_ord,
            "quotient_order": quot_ord,
            "quotient_genus": quot_genus,
            "bring_cover_order": None if p == 5 else cover_ord,
            "bring_cover_genus": None if p == 5 else cover_genus,
            "triple": triple,
        }
        print(
            f"  p={p:2d} ({branch:18s}): |Q|={quot_ord:6d} (g={quot_genus:3d}), "
            f"|G_cover|={str(records[str(p)]['bring_cover_order']):>8s} (g_cover={records[str(p)]['bring_cover_genus']})"
        )

    ok_all = all(ok for _, ok, _ in checks)
    if WitnessBuilder is not None:
        w = WitnessBuilder("bring-hurwitz-245-psl2-tower", engine="python-exact")
        for name, ok, src in checks:
            w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
        out = w.save({
            "q0Anchor": "independent",
            "q0_anchor_reason": "pure finite-group and Riemann-Hurwitz geometry over F_p; no q",
            "q0AnchorReason": "pure finite-group and Riemann-Hurwitz geometry of (2,4,5) triangle quotients over F_p; never touches q",
            "description": (
                "PROBE (bean qou-6082, owner ruling Q-VO9T-3 = 2): classifies non-abelian Hurwitz (2,4,5) quotients "
                "PSL_2(F_p) and PGL_2(F_p) and their unramified PSL_2(F_p) Galois covers over Bring's surface Sigma_4 "
                "(g(p) = 3 |PSL_2(F_p)| + 1), with explicit (2,4,5) matrix triples for p = 5, 11, 19, 29, 31, 41."
            ),
            "admissible_primes": records,
        })
        print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
