"""Regression tests for O(1) slot-memoised ``atom_per_generator_volumes`` (bean qou-cbot)."""
from __future__ import annotations

import mpmath as mp

from pyhecke import atom


def _reference_atom_per_generator_volumes(
    Z: int,
    N: int,
    include_inter: bool = True,
    crossings_per_pair: int = 1,
    m_pp: int | None = None,
    m_pn: int | None = None,
    m_nn: int | None = None,
) -> list[dict]:
    """Uncached per-slot loop matching the pre-qou-cbot implementation line-for-line."""
    A = Z + N
    if A < 1:
        return []
    ordering = ["p"] * Z + ["n"] * N
    n_gens_total = (3 * A - 1) if include_inter else (2 * A)
    a_arr = [0.0] * n_gens_total
    b_arr = [1.0] * n_gens_total
    sp_arr = [1.0] * n_gens_total
    ap_arr = [1.0] * n_gens_total

    for k, nuc in enumerate(ordering):
        intra = atom._PROTON_G0 if nuc == "p" else atom._NEUTRON_G0
        intra_g1 = atom._PROTON_G1 if nuc == "p" else atom._NEUTRON_G1
        base_g0 = (3 * k) if include_inter else (2 * k)
        base_g1 = (3 * k + 1) if include_inter else (2 * k + 1)
        for c, d in intra:
            i = base_g0
            a_new = a_arr[i] * c * atom.h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i], b_arr[i] = a_new, b_new
            sp_arr[i] *= c * atom.q0 + d
            ap_arr[i] *= -c * atom.qi + d
        for c, d in intra_g1:
            i = base_g1
            a_new = a_arr[i] * c * atom.h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i], b_arr[i] = a_new, b_new
            sp_arr[i] *= c * atom.q0 + d
            ap_arr[i] *= -c * atom.qi + d
        if include_inter and k < A - 1:
            i = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == "p" and next_nuc == "p":
                base_cross = (1.0, 0.0)
                m_this = m_pp if m_pp is not None else crossings_per_pair
            elif nuc == "n" and next_nuc == "n":
                base_cross = (1.0, -atom.h)
                m_this = m_nn if m_nn is not None else crossings_per_pair
            else:
                base_cross = (1.0, atom.D_PN)
                m_this = m_pn if m_pn is not None else crossings_per_pair
            for c, d in [base_cross] * m_this:
                a_new = a_arr[i] * c * atom.h + a_arr[i] * d + b_arr[i] * c
                b_new = a_arr[i] * c + b_arr[i] * d
                a_arr[i], b_arr[i] = a_new, b_new
                sp_arr[i] *= c * atom.q0 + d
                ap_arr[i] *= -c * atom.qi + d

    vols = []
    for i in range(n_gens_total):
        vs = atom.z * a_arr[i] + b_arr[i]
        vols.append({"std": vs, "sym": sp_arr[i], "alt": ap_arr[i], "full": vs})
    return vols


def test_atom_per_generator_volumes_bit_identical_to_uncached() -> None:
    cases = [
        (0, 0),
        (1, 0),
        (0, 1),
        (2, 0),
        (0, 2),
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
        (6, 6),
        (82, 126),
    ]
    for dps in (15, 50, 80):
        with mp.workdps(dps):
            for Z, N in cases:
                for inter in (True, False):
                    got = atom.atom_per_generator_volumes(Z, N, include_inter=inter)
                    ref = _reference_atom_per_generator_volumes(Z, N, include_inter=inter)
                    assert got == ref
                    for d_got, d_ref in zip(got, ref):
                        for k in ("std", "sym", "alt", "full"):
                            assert type(d_got[k]) is type(d_ref[k])
                            assert repr(d_got[k]) == repr(d_ref[k])

            got_custom = atom.atom_per_generator_volumes(
                3, 4, include_inter=True, crossings_per_pair=2, m_pp=0, m_pn=2, m_nn=3
            )
            ref_custom = _reference_atom_per_generator_volumes(
                3, 4, include_inter=True, crossings_per_pair=2, m_pp=0, m_pn=2, m_nn=3
            )
            assert got_custom == ref_custom


def test_atom_per_generator_volumes_returns_unaliased_dicts() -> None:
    vols = atom.atom_per_generator_volumes(3, 3, include_inter=True)
    orig_first = vols[0]["full"]
    vols[0]["full"] = -999.0
    assert vols[3]["full"] == orig_first
    fresh = atom.atom_per_generator_volumes(3, 3, include_inter=True)
    assert fresh[0]["full"] == orig_first
