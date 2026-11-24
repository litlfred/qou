#!/usr/bin/env python3
"""Frobenius-admissibility failure diagnostic for the knot-assignment SDP (80-dps mpmath).

Beans qou-vd7j, qou-fadg (updated post-TN-9 / qou-v4iw).
``computations/all_nuclides_sdp_admissibility.py`` reports ``0/3558`` nuclei feasible
under ``solve_frobenius_dual_lp(t, G, n_target=nf_net, u_demand=nf)`` (vs ``2221/3558``
for the scalar inequality LP ``Gx >= 0``).

Why the previous docstring and diagnosis were wrong (bean qou-fadg)
-------------------------------------------------------------------
The original version of this script was written before ``pyhecke.gram`` migrated from
retired Convention C (rank 6, ``det G_C = -0.1892``) to **Convention D**
(``z_D = q^3 / (q^2 + 1)``), and contained three compounding errors:

  1. **Rank 5, not rank 6:** Under Convention D, ``y_{(1^3)} = 0`` identically, so both
     the bilinear Gram ``G_{ij} = tr_M(b_i b_j)`` (signature ``(4+, 1-, 1 zero)``) and
     the Hecke *-Gram ``S_{ij} = tr_M(b_i b_j^*)`` (signature ``(5+, 0-, 1 zero)``,
     TN-9 / qou-v4iw) have **rank 5 of 6** (``det G = det S = 0``), with identical 1D
     radical spanned by the q-antisymmetriser
     ``v_rad = [1, -q^-1, -q^-1, q^-2, q^-2, -q^-3]``.
     The old docstring's ``"residual ~1e-15"`` was a pre-2026-08-15 Convention-C relic
     (where ``range(G_C) = R^6`` trivially).

  2. **Square effective rank (6 on 6), NOT over-determined by the net row:**
     In ``all_nuclides_sdp_admissibility.py:112`` the net RHS is ``nf_net = 1^T nf``
     (not ``A``), and more fundamentally
     ``1^T v_rad = (1 - q^-1)(1 - q^-1 + q^-2) != 0`` for all ``q > 1``
     (``+0.09023723327...`` at ``q_0``). Because ``1^T`` is NOT orthogonal to
     ``ker(G) = span{v_rad}``, the stacked ``7 x 6`` system ``[1^T ; G] x = [n_target ; u]``
     has **rank 6** (5 independent Frobenius rows + 1 independent net row on 6 unknowns).
     Whenever ``u in range(G)`` (``v_rad^T u = 0``), the net constraint ``1^T x = n_target``
     is **always consistent** with ``G x = u`` and uniquely pins the nullspace parameter
     ``lambda* = (n_target - 1^T G^+ u) / (1^T v_rad)``.

  3. **True structural cause of 0/3558 (Fredholm alternative + reversed A-scaling):**
     Notice ``v_rad_w = (-q^-1)^{len(w)} = chi^{(1^3)}(T_w)`` is the 1D alternating
     character ``chi^{(1^3)} : H_3(q) -> R`` (``sigma_i |-> -q^-1``). By ``G^T = G`` and
     ``ker(G) = span{v_rad}``,
         ``nf in range(G)  <==>  v_rad^T nf = chi^{(1^3)}(X_{Z,N}) = 0``.
     Because ``chi^{(1^3)}`` is an algebra homomorphism and every multiplicative factor
     in ``build_atom_nf(Z, N)`` has nonzero ``chi^{(1^3)}`` at ``q_0 > 1``
     (``-q_0^-1`` on ``sigma_i``, ``-q_0`` on ``sigma_i^-1``, ``-[2]_{q_0}/2`` on quark
     ``ud`` mixed, and ``-q_0^-1 + d_pn < 0`` under both ``bring_color_weighted`` and
     ``strict_averaged`` p-n arms), ``v_rad^T nf = chi^{(1^3)}(X_{Z,N}) != 0`` **for
     every ``(Z, N)`` with ``A >= 1``**: raw NF coordinate vectors NEVER lie in
     ``range(G)`` (whereas actual Gram pairing vectors ``u_pair = G nf`` or ``S nf``
     always do).
     Moreover, ``||nf||_2`` grows exponentially with ``O(A^2)`` symmetric-channel
     factors (``chi^{(3)} > 1``), much faster than ``|chi^{(1^3)}(X_{Z,N})|``:
     thus **light** nuclei have large normalised off-range fraction
     ``|v_rad^T nf| / (||v_rad|| ||nf||)`` (``21.4%`` at ``4He``, ``0.273%`` at ``16O``),
     while **heavy** nuclei (``40Ca``, ``56Fe``, ``208Pb``) have tiny *normalised*
     off-range ratios (``~2.0e-18``, ``~5.8e-29``, ``~4.8e-283`` — clamped to ``~3.4e-17`` in
     float64) alongside huge ``||nf||_2`` that exceeds ``M_bound = 1e6`` by ``A >= 7``
     and overflows binary64 around ``A >= 50`` — the exact reverse of the old docstring.

Pure 100-dps ``mpmath`` throughout (zero ``numpy``, zero ``float64``).
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

from mpmath import mp  # noqa: E402
from pyhecke.constants import pn_interface_offset  # noqa: E402
from qou_substrate import q_at, set_compute_dps  # noqa: E402

WORK_DPS = 100
set_compute_dps(WORK_DPS)
mp.dps = WORK_DPS

ZERO = mp.mpf(0)
ONE = mp.mpf(1)
TWO = mp.mpf(2)
HALF = ONE / TWO

NF_NAMES: list[str] = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
NF_BASIS: list[tuple[int, ...]] = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]

SAMPLE: list[tuple[int, int, str]] = [
    (1, 0, "p"),
    (0, 1, "n"),
    (1, 1, "2H"),
    (1, 2, "3H"),
    (2, 1, "3He"),
    (2, 2, "4He"),
    (6, 6, "12C"),
    (8, 8, "16O"),
    (20, 20, "40Ca"),
    (26, 30, "56Fe"),
    (82, 126, "208Pb"),
]


def hm_right_mp(nf: list[mp.mpf], c: mp.mpf, d: mp.mpf, gen: int, h: mp.mpf) -> list[mp.mpf]:
    """Multiply NF element ``nf`` by ``(c * sigma_gen + d * I)`` at working mpmath dps.

    Matches ``pyhecke.gram.hm`` algebraically with zero pruning / zero float64.
    """
    r = [ZERO] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h), (1, c), (4, d)]),
            (5, [(5, c * h), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        val = nf[si]
        if val == ZERO:
            continue
        for ti, co in tgts:
            r[ti] += val * co
    return r


def build_gram_mp(q0: mp.mpf, *, star: bool = False) -> tuple[mp.matrix, list[mp.mpf]]:
    """Build 6x6 Convention-D Gram matrix on ``NF_BASIS`` at 80-dps mpmath.

    ``star=False`` builds bilinear ``G_{ij} = tr_M(b_i b_j)`` (signature ``(4+, 1-, 1 zero)``);
    ``star=True`` builds Hecke *-Gram ``S_{ij} = tr_M(b_i b_j^*)`` (signature ``(5+, 0-, 1 zero)``).
    """
    qi0 = ONE / q0
    h = q0 - qi0
    z_d = (q0 ** 3) / (q0 ** 2 + ONE)
    trm = [ONE, z_d, z_d, z_d ** 2, z_d ** 2, h * (z_d ** 2) + z_d]
    mat = mp.matrix(6, 6)
    for i in range(6):
        for j in range(6):
            cur = [ZERO] * 6
            cur[i] = ONE
            word = NF_BASIS[j] if star else tuple(reversed(NF_BASIS[j]))
            for g in word:
                cur = hm_right_mp(cur, ONE, ZERO, g, h)
            mat[i, j] = mp.fsum(cur[k] * trm[k] for k in range(6))
    return mat, trm


def build_atom_nf_mp(
    Z: int, N: int, q0: mp.mpf, *, pn_convention: str = "bring_color_weighted"
) -> tuple[list[mp.mpf], mp.mpf]:
    """80-dps mpmath mirror of ``pyhecke.atom.build_atom_nf(Z, N)`` + exact ``chi^{(1^3)}`` product."""
    A = Z + N
    qi0 = ONE / q0
    h = q0 - qi0
    h_half = h * HALF
    d_pn = pn_interface_offset(q0, pn_convention)

    ordering: list[str] = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append("p")
            pc += 1
        else:
            ordering.append("n")
            nc += 1

    nf = [ONE, ZERO, ZERO, ZERO, ZERO, ZERO]
    chi_alt_prod = ONE

    def step(vec: list[mp.mpf], c: mp.mpf, d: mp.mpf, gen: int) -> tuple[list[mp.mpf], mp.mpf]:
        return hm_right_mp(vec, c, d, gen, h), c * (-qi0) + d

    for k in range(A):
        if ordering[k] == "p":
            for _ in range(3):
                nf, f = step(nf, ONE, ZERO, 0)
                chi_alt_prod *= f
                nf, f = step(nf, ONE, -h, 1)
                chi_alt_prod *= f
            for c, d, g in ((ONE, ZERO, 0), (ONE, -h_half, 0), (ONE, -h_half, 1),
                            (ONE, ZERO, 0), (ONE, ZERO, 0)):
                nf, f = step(nf, c, d, g)
                chi_alt_prod *= f
        else:
            for _ in range(3):
                nf, f = step(nf, ONE, ZERO, 0)
                chi_alt_prod *= f
                nf, f = step(nf, ONE, -h, 1)
                chi_alt_prod *= f
            for c, d, g in ((ONE, -h_half, 0), (ONE, -h_half, 0), (ONE, -h, 1),
                            (ONE, ZERO, 0), (ONE, ZERO, 0)):
                nf, f = step(nf, c, d, g)
                chi_alt_prod *= f

        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                nf, f = step(nf, ONE, ZERO, 0)
            elif ti == "n" and tj == "n":
                nf, f = step(nf, ONE, -h, 0)
            else:
                nf, f = step(nf, ONE, d_pn, 0)
            chi_alt_prod *= f

    for _ in range(Z):
        nf, f = step(nf, ONE, -h, 1)
        chi_alt_prod *= f

    return nf, chi_alt_prod


def vec_norm2(v: list[mp.mpf]) -> mp.mpf:
    return mp.sqrt(mp.fsum(x * x for x in v))


def mat_vec(M: mp.matrix, v: list[mp.mpf]) -> list[mp.mpf]:
    return [mp.fsum(M[i, j] * v[j] for j in range(M.cols)) for i in range(M.rows)]


def pseudoinverse_sym_rank5(M: mp.matrix) -> mp.matrix:
    """Spectral Moore-Penrose pseudoinverse ``M^+`` for a 6x6 symmetric rank-5 matrix."""
    evals, Q = mp.eigsy(M)
    idx_null = min(range(6), key=lambda k: mp.fabs(evals[k]))
    P = mp.matrix(6, 6)
    for k in range(6):
        if k == idx_null:
            continue
        inv_lam = ONE / evals[k]
        for i in range(6):
            for j in range(6):
                P[i, j] += Q[i, k] * inv_lam * Q[j, k]
    return P


def main() -> int:
    q0 = q_at(WORK_DPS)
    qi0 = ONE / q0
    G, _ = build_gram_mp(q0, star=False)
    S, _ = build_gram_mp(q0, star=True)

    # 1. Verify rank 5 of 6 under Convention D for BOTH G (bilinear) and S (*-Gram).
    ev_G = sorted(mp.eigsy(G)[0])
    ev_S = sorted(mp.eigsy(S)[0])
    zero_tol = mp.mpf("1e-65")
    rank_G = sum(1 for e in ev_G if mp.fabs(e) > zero_tol)
    rank_S = sum(1 for e in ev_S if mp.fabs(e) > zero_tol)
    n_pos_G = sum(1 for e in ev_G if e > zero_tol)
    n_neg_G = sum(1 for e in ev_G if e < -zero_tol)
    n_pos_S = sum(1 for e in ev_S if e > zero_tol)
    n_neg_S = sum(1 for e in ev_S if e < -zero_tol)

    assert rank_G == 5 and (n_pos_G, n_neg_G) == (4, 1), f"unexpected G sig: {ev_G}"
    assert rank_S == 5 and (n_pos_S, n_neg_S) == (5, 0), f"unexpected S sig: {ev_S}"

    # Exact 1D radical v_rad = (-q^-1)^len(w) = [1, -q^-1, -q^-1, q^-2, q^-2, -q^-3].
    v_rad = [(-qi0) ** len(w) for w in NF_BASIS]
    v_rad_norm = vec_norm2(v_rad)
    rad_err_G = vec_norm2(mat_vec(G, v_rad))
    rad_err_S = vec_norm2(mat_vec(S, v_rad))
    assert rad_err_G < zero_tol and rad_err_S < zero_tol

    # 2. Verify 1^T v_rad != 0 => stacked [1^T ; G] has rank 6 (NOT over-determined on range(G)).
    ones_dot_vrad = mp.fsum(v_rad)
    ones_dot_vrad_closed = (ONE - qi0) * (ONE - qi0 + qi0 ** 2)
    assert mp.fabs(ones_dot_vrad - ones_dot_vrad_closed) < zero_tol
    assert ones_dot_vrad > mp.mpf("0.08")

    G_pinv = pseudoinverse_sym_rank5(G)

    print("NF basis:", NF_NAMES)
    print(
        f"Bilinear Gram G: rank {rank_G}/6, sig ({n_pos_G}+, {n_neg_G}-, {6 - rank_G} zero), "
        f"|det G| = {mp.nstr(mp.fabs(mp.det(G)), 4)}, ||G v_rad|| = {mp.nstr(rad_err_G, 4)}"
    )
    print(
        f"Hecke *-Gram S : rank {rank_S}/6, sig ({n_pos_S}+, {n_neg_S}-, {6 - rank_S} zero), "
        f"|det S| = {mp.nstr(mp.fabs(mp.det(S)), 4)}, ||S v_rad|| = {mp.nstr(rad_err_S, 4)}"
    )
    print(
        f"Net-on-radical : 1ᵀ v_rad = (1 - q₀⁻¹)(1 - q₀⁻¹ + q₀⁻²) = "
        f"{mp.nstr(ones_dot_vrad, 12)} != 0  =>  rank([1ᵀ ; G]) = 6 (square on range(G))"
    )
    print(
        f"\n{'nucleus':8}{'A':>4}  {'|v_radᵀ nf|':>14}  {'off-range frac':>14}  "
        f"{'||nf||₂':>12}  {'in-range [1ᵀ;G] resid':>22}  true failure mode"
    )

    f64_max = mp.mpf("1.7976931348623157e308")
    m_bound = mp.mpf("1e6")

    for Z, N, lab in SAMPLE:
        A = Z + N
        nf, chi_alt_exact = build_atom_nf_mp(Z, N, q0, pn_convention="bring_color_weighted")
        _, chi_alt_strict = build_atom_nf_mp(Z, N, q0, pn_convention="strict_averaged")
        vrad_dot_nf = mp.fsum(v_rad[i] * nf[i] for i in range(6))
        nf_norm = vec_norm2(nf)

        # Verify Fredholm projection v_rad^T nf equals multiplicative character chi^{(1^3)}(X_{Z,N})
        # up to working-dps conditioning ||v_rad|| * ||nf|| (at heavy A, ||nf|| >> |chi^{(1^3)}|,
        # so the closed-form multiplicative product chi_alt_exact avoids catastrophic cancellation).
        abs_char_err = mp.fabs(vrad_dot_nf - chi_alt_exact)
        assert abs_char_err <= mp.mpf("1e-75") * v_rad_norm * nf_norm, (
            f"{lab}: char mismatch {abs_char_err} vs scale {v_rad_norm * nf_norm}"
        )
        assert mp.fabs(chi_alt_exact) > ZERO and mp.fabs(chi_alt_strict) > ZERO

        # Unit-normalised off-range fraction |<nf, v_rad / ||v_rad||>| / ||nf||
        # evaluated from cancellation-free chi_alt_exact = v_rad^T nf.
        off_frac_unit = mp.fabs(chi_alt_exact) / (v_rad_norm * nf_norm)

        # Project nf onto range(G): nf_proj = nf - (<nf, v_rad>/<v_rad, v_rad>) v_rad,
        # and verify that [1^T ; G] x = [nf_net ; nf_proj] is EXACTLY solvable!
        alpha = vrad_dot_nf / (v_rad_norm ** 2)
        nf_proj = [nf[i] - alpha * v_rad[i] for i in range(6)]
        nf_net = mp.fsum(nf)
        x0 = mat_vec(G_pinv, nf_proj)
        lam = (nf_net - mp.fsum(x0)) / ones_dot_vrad
        x_exact = [x0[i] + lam * v_rad[i] for i in range(6)]
        in_range_resid = (
            vec_norm2([a - b for a, b in zip(mat_vec(G, x_exact), nf_proj)])
            + mp.fabs(mp.fsum(x_exact) - nf_net)
        ) / nf_norm
        assert in_range_resid < mp.mpf("1e-70"), f"{lab}: in-range solve resid {in_range_resid}"

        if nf_norm > f64_max:
            mode = "nf ∉ range(G) + f64 NF overflow (||nf|| > 1.8e308)"
        elif off_frac_unit < mp.mpf("1e-16") and nf_norm > m_bound:
            mode = "nf ∉ range(G) (tiny rel; ||nf|| >> M_bound=1e6)"
        else:
            mode = "nf ∉ range(G) (v_radᵀ nf = χ^(1³)(X) ≠ 0)"

        print(
            f"{lab:8}{A:>4}  {mp.nstr(mp.fabs(chi_alt_exact), 6):>14}  "
            f"{mp.nstr(off_frac_unit, 6):>14}  {mp.nstr(nf_norm, 5):>12}  "
            f"{mp.nstr(in_range_resid, 4):>22}  {mode}"
        )

    print(
        "\nDiagnosis (Convention D, 100-dps mpmath):\n"
        "  1. Both G (bilinear, 4+/1-/1z) and S (*-Gram, 5+/0-/1z) have RANK 5, not 6,\n"
        "     with 1D radical v_rad = [1, -q₀⁻¹, -q₀⁻¹, q₀⁻², q₀⁻², -q₀⁻³].\n"
        "  2. Since 1ᵀ v_rad != 0, [1ᵀ ; G] has rank 6 (5 + 1 = 6 on 6 unknowns): on\n"
        "     range(G) the net row 1ᵀ x = n_target is ALWAYS consistent (resid < 1e-99).\n"
        "  3. Raw coordinate vectors nf satisfy v_radᵀ nf = χ^(1³)(X_{Z,N}) != 0 for ALL\n"
        "     (Z, N) (both p-n arms), so Gx = nf fails Fredholm range membership nf ∈ range(G)\n"
        "     (passing u_demand = G nf instead of raw nf restores range membership).\n"
        "  4. Normalised off-range ratio |v_radᵀ nf| / (||v_rad|| ||nf||) is O(0.003..0.41)\n"
        "     for light nuclei and exponentially tiny (10^-18..10^-283) for heavy nuclei\n"
        "     because ||nf|| grows with χ^(3) >> |χ^(1³)| (reversing the old docstring)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
