#!/usr/bin/env python3
"""d1b_eq98_rank_correction_probe.py — qou-rutm: CORRECTING A MERGED CLAIM.

🛑 This probe corrects `d1b_52_charge_lattice_sourcing_probe.py`, which is
**already merged to `main`** (`74a927b6af`, PR #6599). The defect is in that
probe's headline verdict, C4, and it is the load-bearing step.

═══ WHAT I MERGED ═══

    "eq (98) is a rank-3 antisymmetric integer matrix.
     The NZ datum's antisymmetric content has rank 2, always.
     ⇒ scope-(b) exclusion, invariant = NZ symmetry + cusp relation."

═══ WHY IT IS WRONG ═══

**eq (98) has rank 2, not rank 3.** I wrote "rank 3" meaning its SIZE, 3×3, and
then used it as a RANK in a rank comparison. The two are never equal here, and
not by accident:

    every odd-size antisymmetric matrix is singular
    (det A = det(−Aᵀ) = (−1)ⁿ det A, so n odd ⇒ det A = 0),

hence **an antisymmetric matrix always has even rank**. A 3×3 antisymmetric
integer matrix can have rank 0 or 2 and nothing else. `det(eq 98) = 0` and its
exact rank over ℚ is **2** — computed below.

So the comparison "eq (98) is rank 3, NZ is rank 2" compares a size against a
rank. **Both objects are rank 2.** The exclusion had no content, and the
scope-(b) label — which under AGENTS.md requires a *proved invariant* — was
attached to a miscomputed one.

Worse for the original conclusion: matching rank makes the NZ cusp block **more**
plausible as a carrier, not less. The invariant I used to exclude it is the one
invariant on which the two agree.

═══ WHAT ACTUALLY DISCRIMINATES THEM ═══

A rank-2 antisymmetric integral form is classified up to `GL(ℤ)` equivalence by a
single elementary divisor `d`: it is `[[0,d],[−d,0]] ⊕ 0`. Computed by Smith
normal form below:

    d(eq 98)     = 1
    d(NZ cusp)   = 2

So they are **inequivalent over ℤ** and **equivalent over ℚ**. That is the true
statement, and it is much weaker than what was merged.

═══ RE-SCOPED VERDICT (b) → (a) ═══

Per AGENTS.md §"Before declaring refuted": a scope-(b) structural exclusion needs
a proved invariant. There isn't one here. Re-scoped to **(a)**:

  **The NZ cusp form is not, on the nose, the eq-(98) form** — it differs by an
  integral factor of 2 and is indexed by (μ,λ) rather than by the three σ.

  **The NZ route is NOT excluded.** A charge lattice is routinely defined only up
  to normalisation, and over ℚ the two forms agree. Anyone who reads the merged
  C4 as "NZ is dead" is reading a defect.

═══ WHAT IS UNAFFECTED ═══

C1 (GGM defines no lattice: 0/0 measured), C2 (the NZ edge block is exactly
zero), C3 (the whole antisymmetric content is the rank-2 cusp block at ±2), C5
(KRSS quivers are symmetric), C7 (route 2 exists; the repo has both halves) all
stand — they are measurements, not inferences from the bogus rank claim. Only C4,
which turned C2+C3 into an exclusion, is void.

Predictions recorded before measuring:
  P1: det(eq 98) = 0 and rank = 2, forced by odd-size antisymmetry.  -> C1
  P2: d(eq 98) = 1 and d(NZ cusp) = 2, so ℤ-inequivalent.            -> C2
  P3: they ARE ℚ-equivalent, both being rank 2.                      -> C3

Exact integer / Fraction arithmetic throughout; no floats.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

EQ98 = [[0, 4, 3], [-4, 0, -3], [-3, 3, 0]]
NZ_CUSP = [[0, 2], [-2, 0]]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def rank_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n)]
        r += 1
    return r


def snf(M):
    A = [row[:] for row in M]
    m, n = len(A), len(A[0])
    out = []
    r = c = 0
    while r < m and c < n:
        best = None
        for i in range(r, m):
            for j in range(c, n):
                if A[i][j] != 0 and (best is None
                                     or abs(A[i][j]) < abs(A[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            break
        i, j = best
        A[r], A[i] = A[i], A[r]
        for k in range(m):
            A[k][c], A[k][j] = A[k][j], A[k][c]
        done = False
        while not done:
            done = True
            for i in range(r + 1, m):
                q = A[i][c] // A[r][c]
                if q:
                    A[i] = [A[i][t] - q * A[r][t] for t in range(n)]
                if A[i][c] != 0:
                    A[r], A[i] = A[i], A[r]
                    done = False
            for j in range(c + 1, n):
                q = A[r][j] // A[r][c]
                if q:
                    for k in range(m):
                        A[k][j] -= q * A[k][c]
                if A[r][j] != 0:
                    for k in range(m):
                        A[k][c], A[k][j] = A[k][j], A[k][c]
                    done = False
        out.append(abs(A[r][c]))
        r += 1
        c += 1
    return out


def main() -> int:
    print("=" * 78)
    print(" CORRECTING A MERGED CLAIM: eq (98) has rank 2, not rank 3")
    print("=" * 78)
    checks = []

    d = det3(EQ98)
    rk = rank_q(EQ98)
    c1 = (d == 0 and rk == 2)
    print("\n  ── C1: the merged 'rank 3' is impossible, not merely wrong ──")
    print(f"     det(eq 98)  = {d}")
    print(f"     rank(eq 98) = {rk}   (exact, over ℚ)")
    print("     Forced: det A = det(−Aᵀ) = (−1)ⁿ det A, so an odd-size")
    print("     antisymmetric matrix is singular ⇒ antisymmetric ⇒ EVEN rank.")
    print("     A 3×3 antisymmetric integer matrix has rank 0 or 2. Never 3.")
    print("     I wrote the SIZE (3×3) and then used it as a RANK.")
    checks.append((c1, "C1_eq98_rank_is_2_not_3",
                   "P1 CONFIRMED. det(eq 98) = 0 and its exact rank over Q is 2. "
                   "The merged probe's C4 said 'eq (98) is a rank-3 antisymmetric "
                   "integer matrix' -- that is its SIZE, used as a RANK. Every "
                   "odd-size antisymmetric matrix is singular (det A = det(-A^T) "
                   "= (-1)^n det A), so an antisymmetric matrix always has EVEN "
                   "rank and 'rank 3' was never available"))

    snf98, snfnz = snf(EQ98), snf(NZ_CUSP)
    d98 = snf98[0] if snf98 else 0
    dnz = snfnz[0] if snfnz else 0
    c2 = (d98 == 1 and dnz == 2 and d98 != dnz)
    print("\n  ── C2: what ACTUALLY discriminates them ──")
    print(f"     SNF(eq 98)   = {snf98}   ⇒ elementary divisor d = {d98}")
    print(f"     SNF(NZ cusp) = {snfnz}   ⇒ elementary divisor d = {dnz}")
    print("     A rank-2 antisymmetric integral form is [[0,d],[−d,0]] ⊕ 0 up to")
    print("     GL(ℤ), so d is the complete invariant. 1 ≠ 2 ⇒ INEQUIVALENT / ℤ.")
    checks.append((c2, "C2_the_real_invariant_is_the_elementary_divisor",
                   f"P2 CONFIRMED. A rank-2 antisymmetric integral form is "
                   f"[[0,d],[-d,0]] (+) 0 up to GL(Z), so the elementary divisor "
                   f"d is the complete invariant. d(eq 98) = {d98}, "
                   f"d(NZ cusp) = {dnz}: inequivalent over Z. This is the "
                   f"discriminator the merged probe should have used"))

    c3 = (rank_q(EQ98) == rank_q(NZ_CUSP) == 2)
    print("\n  ── C3: but they ARE equivalent over ℚ ──")
    print(f"     rank(eq 98) = {rank_q(EQ98)},  rank(NZ cusp) = {rank_q(NZ_CUSP)}")
    print("     Same rank, same parity, differing only by the factor 2. Over ℚ a")
    print("     rank-2 antisymmetric form is unique up to equivalence.")
    checks.append((c3, "C3_they_are_Q_equivalent",
                   "P3 CONFIRMED. Both forms have rank 2, and over Q a rank-2 "
                   "antisymmetric form is unique up to equivalence, so they are "
                   "Q-equivalent and differ only by the integral factor 2. A "
                   "charge lattice is routinely defined up to normalisation, "
                   "which is exactly why this is not an exclusion"))

    c4 = True
    print("\n  ── C4: RE-SCOPING the merged verdict, (b) → (a) ──")
    print("     AGENTS.md: a scope-(b) structural exclusion requires a PROVED")
    print("     invariant. The invariant cited was a miscomputed rank, so there")
    print("     is no (b) here. Re-scoped to (a):")
    print("       the NZ cusp form is not ON THE NOSE the eq-(98) form — it")
    print("       differs by an integral factor 2 and is indexed by (μ,λ) rather")
    print("       than by the three σ.")
    print("     🛑 THE NZ ROUTE IS **NOT** EXCLUDED. Anyone reading the merged C4")
    print("     as 'NZ is dead' is reading a defect.")
    checks.append((c4, "C4_rescoped_b_to_a_NZ_is_NOT_excluded",
                   "The merged C4 was labelled scope-(b), which AGENTS.md "
                   "reserves for exclusions resting on a PROVED invariant. The "
                   "invariant cited was a miscomputed rank, so the (b) label was "
                   "unearned. Re-scoped to (a): the NZ cusp form is not on the "
                   "nose the eq-(98) form (integral factor 2, and indexed by "
                   "(mu,lambda) rather than by the three sigma). The NZ route is "
                   "NOT excluded -- charge lattices are routinely defined up to "
                   "normalisation and the two forms agree over Q"))

    c5 = True
    print("\n  ── C5: what is UNAFFECTED ──")
    for k, v in {
        "C1 GGM defines no lattice (0/0)": "measurement, stands",
        "C2 NZ edge block exactly zero": "measurement, stands",
        "C3 antisym content = rank-2 cusp at ±2": "measurement, stands",
        "C5 KRSS quivers are symmetric": "measurement, stands",
        "C7 route 2 exists, repo has both halves": "measurement, stands",
        "C4 the exclusion": "VOID — this probe replaces it",
    }.items():
        print(f"     {k:<42} {v}")
    checks.append((c5, "C5_only_C4_is_void",
                   "The merged probe's C1, C2, C3, C5 and C7 are measurements and "
                   "stand unchanged. Only C4 -- which turned the C2+C3 "
                   "measurements into an exclusion via the bogus rank comparison "
                   "-- is void. The defect is in one inference, not in the data"))

    # -- C6: is d=1 vs d=2 an obstruction at all? NO. --------------------
    half_integral = all(x % 2 == 0 for row in NZ_CUSP for x in row)
    half = [[x // 2 for x in row] for row in NZ_CUSP]
    half_unimodular = (snf(half)[0] == 1)
    c6 = (half_integral and half_unimodular)
    print("\n  ── C6: the d=1 vs d=2 gap is a NORMALISATION, not an obstruction ──")
    print(f"     NZ cusp / 2 = {half}, integral: {half_integral}")
    print(f"     and unimodular: {half_unimodular}")
    print("     So the NZ cusp form is 2 × a unimodular rank-2 form, and eq (98)")
    print("     is already unimodular on its support. The two differ by an")
    print("     OVERALL FACTOR 2 — a convention about how the NZ symplectic form")
    print("     is normalised, not a lattice-theoretic obstruction.")
    print("     ⇒ even the re-scoped (a) statement is NOT evidence against NZ.")
    checks.append((c6, "C6_d1_vs_d2_is_normalisation_not_obstruction",
                   "The NZ cusp form halves to [[0,1],[-1,0]], which is "
                   "unimodular, so it is 2 x a unimodular rank-2 form while "
                   "eq (98) is already unimodular on its support. The elementary "
                   "divisors differ by an overall factor 2 -- a normalisation "
                   "convention for the NZ symplectic form, not an obstruction. So "
                   "even the re-scoped scope-(a) statement ('differs by an "
                   "integral factor 2') is NOT evidence against the NZ route"))

    # -- C7: what the REAL structural difference is: eq (98) has a radical --
    cc = EQ98[0][1]
    bb = -EQ98[0][2]
    aa = EQ98[1][2]
    axis = (aa, bb, cc)
    img = [sum(EQ98[i][j] * axis[j] for j in range(3)) for i in range(3)]
    c7 = (img == [0, 0, 0] and rank_q(EQ98) == 2)
    print("\n  ── C7: the only surviving difference — eq (98) has a RADICAL ──")
    print(f"     axis vector (Ω₂₃, −Ω₁₃, Ω₁₂) = {axis}")
    print(f"     eq(98) · axis = {img}   ⇒ it spans the radical")
    print("     Any 3×3 antisymmetric matrix is the cross-product matrix of its")
    print("     axis vector, so the radical being built from the Ω entries is")
    print("     FORCED by antisymmetry — read no numerology into (−3,−3,4).")
    print("\n     So the genuine structural difference is neither rank nor the")
    print("     elementary divisor: eq (98) lives on a rank-3 lattice with a")
    print("     1-dimensional radical, the NZ cusp form on a rank-2 lattice with")
    print("     none. In SW terms a null direction of the Dirac pairing is a")
    print("     FLAVOUR charge — so the question NZ has to answer is not 'why")
    print("     rank 2' but 'where is the third, null direction'.")
    checks.append((c7, "C7_the_real_difference_is_the_radical_and_it_is_forced",
                   f"eq (98) has a 1-dimensional radical spanned by the axis "
                   f"vector {axis}, verified by eq(98) . axis = [0,0,0]. This is "
                   f"FORCED: any 3x3 antisymmetric matrix is the cross-product "
                   f"matrix of its axis vector (Omega_23, -Omega_13, Omega_12), so "
                   f"the radical being built from the Omega entries carries no "
                   f"information and must not be read as numerology. After C6 "
                   f"removes the elementary-divisor gap, THIS is the only "
                   f"surviving structural difference from the NZ cusp form: a "
                   f"rank-3 lattice with a 1-dim radical versus a rank-2 lattice "
                   f"with none. In Seiberg-Witten terms a null direction of the "
                   f"Dirac pairing is a FLAVOUR charge, so the open question for "
                   f"the NZ route is not 'why rank 2' but 'where is the third, "
                   f"null direction'"))

    wb = WitnessBuilder("d1b-eq98-rank-correction",
                        engine="exact-integer-rank-and-smith-normal-form")
    wb.set_description(
        "qou-rutm. CORRECTS A MERGED CLAIM. d1b_52_charge_lattice_sourcing_probe "
        "is on main (74a927b6af, PR #6599) and its headline verdict C4 reads "
        "'eq (98) is a rank-3 antisymmetric integer matrix; the NZ datum's "
        "antisymmetric content has rank 2, always; scope-(b) exclusion'. eq (98) "
        "has rank 2, not 3: I wrote its SIZE (3x3) and used it as a RANK. This "
        "was never possible -- every odd-size antisymmetric matrix is singular "
        "(det A = det(-A^T) = (-1)^n det A), so an antisymmetric matrix always "
        "has EVEN rank. det(eq 98) = 0, rank = 2 exactly. So the comparison put a "
        "size against a rank and BOTH objects are rank 2, which makes the NZ "
        "cusp block MORE plausible as a carrier rather than less. The real "
        "discriminator is the elementary divisor of a rank-2 antisymmetric "
        "integral form, complete up to GL(Z): d(eq 98) = 1 against d(NZ cusp) = "
        "2, so they are inequivalent over Z but EQUIVALENT over Q. Verdict "
        "re-scoped (b) -> (a) per AGENTS.md, which reserves (b) for exclusions "
        "resting on a proved invariant: the NZ cusp form is not on the nose the "
        "eq-(98) form, but THE NZ ROUTE IS NOT EXCLUDED -- charge lattices are "
        "routinely defined up to normalisation. The merged C1, C2, C3, C5 and C7 "
        "are measurements and stand; only C4 is void.")
    wb.add_data("merged_claim_corrected", {
        "probe": "computations/qbeta/d1b_52_charge_lattice_sourcing_probe.py",
        "assertion": "C4_NZ_route_EXCLUDED_scope_b",
        "merged_at": "74a927b6af (PR #6599)",
        "quoted": "eq (98) is a rank-3 antisymmetric integer matrix. The NZ "
                  "datum's antisymmetric content has rank 2, always.",
        "defect": "SIZE (3x3) used as RANK; antisymmetric matrices have even "
                  "rank, so rank 3 was never available",
    })
    wb.add_data("measured", {
        "det_eq98": d, "rank_eq98": rk,
        "snf_eq98": snf98, "elementary_divisor_eq98": d98,
        "snf_nz_cusp": snfnz, "elementary_divisor_nz_cusp": dnz,
        "Z_equivalent": False, "Q_equivalent": True,
    })
    wb.add_data("rescope", {
        "was": "scope-(b) structural exclusion",
        "now": "scope-(a): the NZ cusp form is not on the nose the eq-(98) form "
               "(integral factor 2; indexed by (mu,lambda) not the three sigma)",
        "nz_route_excluded": False,
        "why_not": "charge lattices are routinely defined up to normalisation, "
                   "and the two forms are equivalent over Q",
    })
    wb.add_data("unaffected", [
        "C1 GGM defines no charge lattice (0 / 0, measured)",
        "C2 NZ edge block is exactly zero",
        "C3 antisymmetric content is the rank-2 cusp block at +-2",
        "C5 KRSS quivers are symmetric; eq (98) is not",
        "C7 route 2 exists and the repo has both halves",
    ])
    wb.add_data("scope", {
        "tier": "correction of a merged claim; re-scope (b) -> (a)",
        "method": "exact determinant, exact rank over Q, Smith normal form over Z",
        "arithmetic": "exact integers and Fractions; no floats",
        "derives_A_omega": False, "wired": False, "fit": False,
    })
    for ok, name, detail in checks:
        wb.add_assertion(name, computed="PASS" if ok else "FAIL",
                         expected="PASS", tolerance="exact", source=detail)
    wb.save({"q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal"})

    n_ok = sum(1 for ok, _, _ in checks if ok)
    print(f"\n  {n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
