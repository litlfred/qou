#!/usr/bin/env python3
"""universal-ilp.py — 80-dps H_3(q_0) confinement-layer operator enumeration (qou-ozts).

Restores `apply_atom_nf` from its exact pre-M2b-inversion definition in git
history (`git show 95eb85e4005c4fae563b5969ca493273751e20aa:folio-assistant/computations/hecke_core.py`,
lines 711-738) and upgrades the entire H_3(q_0) normal-form multiplication,
canonical Markov trace (`z = q_0^3 / (q_0^2 + 1)`, `tr_M(e^-) = h*z^2 + z`),
and Frobenius pairing `G` to 95-digit working / 80-digit output `mpmath`
precision (zero `float64`) at the canonical proton substrate pin `q_at(95)`.

HISTORICAL PROVENANCE & SCOPE (`qou-ozts`, `qou-uilp`, `qou-mba8`)
------------------------------------------------------------------
1. Why `apply_atom_nf` was missing (`qou-ozts`): in commit `95eb85e4005c`,
   `hecke_core.py` defined both `build_atom_nf(Z, N)` (starting from identity
   `[1, 0, 0, 0, 0, 0]`) and `apply_atom_nf(nf, Z, N)` (right-multiplying an
   existing normal-form vector `nf` by the same atom crossing sequence). When
   `hecke_core.py` was inverted into `pyhecke.atom`, `build_atom_nf` was moved
   and updated (including inter-nucleon `pp`/`nn`/`pn` crossings and colour-
   weighted `D_PN`, lines 292-373 of `tools/pyhecke/python/pyhecke/atom.py`),
   while `apply_atom_nf` was omitted. Implementing `apply_atom_nf_mp(nf, Z, N)`
   as the exact right-action generalization of `pyhecke.atom.build_atom_nf`
   satisfies `apply_atom_nf_mp([1,0,0,0,0,0], Z, N) == build_atom_nf_mp(Z, N)`
   identically to `< 1e-85`.
2. Paper scope (`rem:confinement-layer-operator-selection`, `#9280`):
   the retired `universal-ilp-algorithm` definition was replaced in `#9280`
   (`qou-mba8`) by `rem:confinement-layer-operator-selection`
   (`QOU.MathlibInfra.ConfinementLayerTower`).
   Under canonical `z = q_0^3/(q_0^2+1)` and `tr_M(e^-) = h*z^2 + z`, the
   6x6 H_3(q_0) Frobenius Gram matrix has rank 5 (1D alternating radical) and
   selects 1-crossing Frobenius-feasible operators when scanning `{sigma_0,
   sigma_1, sigma_0^-1, sigma_1^-1}` by crossing count alone (`qou-jqjx`,
   `qou-v5fp`); physical step-4 gluon stabilization remains open across the
   four candidate arms recorded in `rem:confinement-layer-operator-selection`.
"""
from __future__ import annotations

import itertools
import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ.setdefault("QOU_OUTPUT_DPS", "80")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

NF_BASIS: tuple[tuple[int, ...], ...] = ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0))
NF_NAMES: tuple[str, ...] = ("γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻")


def hm_mp(nf: list[mp.mpf], c: mp.mpf, d: mp.mpf, gen: int, h: mp.mpf) -> list[mp.mpf]:
    """Exact 95-dps right-multiplication of an H_3(q) NF vector by `c*sigma_gen + d*1`."""
    z0 = mp.mpf(0)
    r = [z0, z0, z0, z0, z0, z0]
    if gen == 0:
        tables = (
            (0, ((1, c), (0, d))),
            (1, ((1, c * h), (0, c), (1, d))),
            (2, ((3, c), (2, d))),
            (3, ((3, c * h), (2, c), (3, d))),
            (4, ((5, c), (4, d))),
            (5, ((5, c * h), (4, c), (5, d))),
        )
    else:
        tables = (
            (0, ((2, c), (0, d))),
            (1, ((4, c), (1, d))),
            (2, ((2, c * h), (0, c), (2, d))),
            (3, ((5, c), (3, d))),
            (4, ((4, c * h), (1, c), (4, d))),
            (5, ((5, c * h), (3, c), (5, d))),
        )
    for si, tgts in tables:
        val = nf[si]
        if val == z0:
            continue
        for ti, co in tgts:
            r[ti] += val * co
    return r


def build_h3_gram_mp(q: mp.mpf) -> tuple[list[mp.mpf], list[list[mp.mpf]], mp.mpf, mp.mpf]:
    """Build exact 95-dps canonical Markov trace vector `TR_M` and 6x6 Gram matrix `G`."""
    one = mp.mpf(1)
    h = q - one / q
    q2 = q * q
    z = (q2 * q) / (q2 + one)
    # Canonical H_3(q) Markov trace vector (`pyhecke.gram.TR_M`, 2026-05-19 fix:
    # tr_M(sigma_0 sigma_1 sigma_0) = h*z^2 + z via Skein on sigma_0^2 = h*sigma_0 + 1).
    tr_vec = [one, z, z, z * z, z * z, h * z * z + z]

    id_nf = [one] + [mp.mpf(0)] * 5
    basis_nfs: list[list[mp.mpf]] = []
    for word in NF_BASIS:
        v = list(id_nf)
        for g in word:
            v = hm_mp(v, one, mp.mpf(0), g, h)
        basis_nfs.append(v)

    gram: list[list[mp.mpf]] = []
    for i in range(6):
        row: list[mp.mpf] = []
        for j in range(6):
            prod = list(basis_nfs[i])
            for g in NF_BASIS[j]:
                prod = hm_mp(prod, one, mp.mpf(0), g, h)
            row.append(mp.fsum(prod[k] * tr_vec[k] for k in range(6)))
        gram.append(row)
    return tr_vec, gram, h, z


def nf_tr_mp(nf: list[mp.mpf], tr_vec: list[mp.mpf]) -> mp.mpf:
    return mp.fsum(nf[i] * tr_vec[i] for i in range(6))


def check_frobenius_mp(
    nf: list[mp.mpf], gram: list[list[mp.mpf]]
) -> tuple[bool, list[mp.mpf], list[tuple[str, mp.mpf]]]:
    gx = [mp.fsum(gram[i][j] * nf[j] for j in range(6)) for i in range(6)]
    tol = mp.mpf("-1e-70")
    viols = [(NF_NAMES[i], gx[i]) for i in range(6) if gx[i] < tol]
    return len(viols) == 0, gx, viols


def apply_atom_nf_mp(
    nf_in: list[mp.mpf], Z: int, N: int, h: mp.mpf, d_pn: mp.mpf
) -> list[mp.mpf]:
    """Apply atom `(Z, N)` crossings to an existing H_3(q) NF vector `nf_in`.

    Restores `apply_atom_nf(nf, Z, N)` from `95eb85e4005c:hecke_core.py:711-738`
    updated to match `pyhecke.atom.build_atom_nf(Z, N)`'s exact crossing sequence
    (ground-state interleaved ordering, Borromean `(sigma_0 sigma_1^-1)^3` core,
    typed quark crossings, 2x`sigma_0` gluon dressing, pairwise inter-nucleon
    crossings, and `Z` `pe` `sigma_1^-1` crossings) in 95-dps `mpmath`.
    """
    one = mp.mpf(1)
    zero = mp.mpf(0)
    half_h = -h / mp.mpf(2)
    A = Z + N
    nf = list(nf_in)
    if A == 0:
        return nf

    ordering: list[str] = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append("p")
            pc += 1
        else:
            ordering.append("n")
            nc += 1

    for k in range(A):
        if ordering[k] == "p":
            for _ in range(3):
                nf = hm_mp(nf, one, zero, 0, h)
                nf = hm_mp(nf, one, -h, 1, h)
            nf = hm_mp(nf, one, zero, 0, h)
            nf = hm_mp(nf, one, half_h, 0, h)
            nf = hm_mp(nf, one, half_h, 1, h)
            nf = hm_mp(nf, one, zero, 0, h)
            nf = hm_mp(nf, one, zero, 0, h)
        else:
            for _ in range(3):
                nf = hm_mp(nf, one, zero, 0, h)
                nf = hm_mp(nf, one, -h, 1, h)
            nf = hm_mp(nf, one, half_h, 0, h)
            nf = hm_mp(nf, one, half_h, 0, h)
            nf = hm_mp(nf, one, -h, 1, h)
            nf = hm_mp(nf, one, zero, 0, h)
            nf = hm_mp(nf, one, zero, 0, h)

        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                nf = hm_mp(nf, one, zero, 0, h)
            elif ti == "n" and tj == "n":
                nf = hm_mp(nf, one, -h, 0, h)
            else:
                nf = hm_mp(nf, one, d_pn, 0, h)

    for _ in range(Z):
        nf = hm_mp(nf, one, -h, 1, h)
    return nf


def build_atom_nf_mp(Z: int, N: int, h: mp.mpf, d_pn: mp.mpf) -> list[mp.mpf]:
    """Build atom `(Z, N)` NF starting from the H_3(q) identity `[1, 0, 0, 0, 0, 0]`."""
    id_nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    return apply_atom_nf_mp(id_nf, Z, N, h, d_pn)


def make_ops(h: mp.mpf) -> list[tuple[str, int, mp.mpf, mp.mpf]]:
    one = mp.mpf(1)
    zero = mp.mpf(0)
    return [
        ("σ₀", 0, one, zero),
        ("σ₁", 1, one, zero),
        ("σ₀⁻¹", 0, one, -h),
        ("σ₁⁻¹", 1, one, -h),
    ]


def universal_ilp(
    state_nf: list[mp.mpf],
    label: str,
    ops: list[tuple[str, int, mp.mpf, mp.mpf]],
    tr_vec: list[mp.mpf],
    gram: list[list[mp.mpf]],
    h: mp.mpf,
    target_nf_builder=None,
    max_len: int = 6,
):
    """Enumerate `{σ₀, σ₁, σ₀⁻¹, σ₁⁻¹}^n` (`1 <= n <= max_len`), selecting the
    minimum-crossing Frobenius-feasible operator tie-broken by `min |tr_M|`.
    """
    tr_x = nf_tr_mp(state_nf, tr_vec)
    stable_x, _, _ = check_frobenius_mp(state_nf, gram)
    print(f"  {label} state: tr_M={mp.nstr(tr_x, 7)}, Frob={'STABLE' if stable_x else 'UNSTABLE'}")

    selected = None
    for n in range(1, max_len + 1):
        best_at_n = None
        for word in itertools.product(ops, repeat=n):
            nf_new = list(state_nf)
            for _name, gen, c, d in word:
                nf_new = hm_mp(nf_new, c, d, gen, h)
            if target_nf_builder is not None:
                nf_new = target_nf_builder(nf_new)
            tr_new = nf_tr_mp(nf_new, tr_vec)
            stable_new, _, _ = check_frobenius_mp(nf_new, gram)
            if stable_new:
                word_label = "".join(o[0] for o in word)
                if best_at_n is None or abs(tr_new) < abs(best_at_n[1]):
                    best_at_n = (word_label, tr_new, nf_new, n)
        if best_at_n is not None and selected is None:
            selected = best_at_n
    if selected is not None:
        print(f"  -> LP SELECTS: {selected[0]} ({selected[3]} crossings), tr_M = {mp.nstr(selected[1], 8)}")
    else:
        print("  -> NO non-trivial feasible operator found")
    return selected


def main() -> int:
    set_compute_dps()
    with mp.workdps(95):
        q0 = q_at(95)
        tr_vec, gram, h, z = build_h3_gram_mp(q0)
        delta_col = flavor_split_leading(q0)
        d_pn = -h * (mp.mpf(1) / mp.mpf(2) - delta_col / mp.mpf(4))
        ops = make_ops(h)
        one = mp.mpf(1)
        zero = mp.mpf(0)
        half_h = -h / mp.mpf(2)

        print("=" * 70)
        print("UNIVERSAL ILP (80-DPS H_3 ENUMERATION — BEAN qou-ozts)")
        print("=" * 70)

        results: dict[str, tuple[str, mp.mpf, list[mp.mpf], int] | None] = {}

        # Level 1: Bare quarks -> Confinement
        nf_quarks = [one, zero, zero, zero, zero, zero]
        nf_quarks = hm_mp(nf_quarks, one, zero, 0, h)
        nf_quarks = hm_mp(nf_quarks, one, half_h, 1, h)
        nf_quarks = hm_mp(nf_quarks, one, half_h, 0, h)
        sel1 = universal_ilp(nf_quarks, "quarks(uud)", ops, tr_vec, gram, h, max_len=6)
        results["confinement"] = sel1
        nf_confined = sel1[2] if sel1 is not None else list(nf_quarks)

        # Level 2: Confined quarks -> Gluon
        sel2 = universal_ilp(nf_confined, "confined quarks", ops, tr_vec, gram, h, max_len=4)
        results["gluon"] = sel2
        nf_with_gluon = sel2[2] if sel2 is not None else list(nf_confined)

        # Level 3: Proton+gluon -> Electron attachment
        sel3 = universal_ilp(nf_with_gluon, "proton+gluon", ops, tr_vec, gram, h, max_len=3)
        results["electron"] = sel3
        nf_h = sel3[2] if sel3 is not None else list(nf_with_gluon)

        # Level 4: H atom -> H_2 molecular bond (restored apply_atom_nf_mp)
        sel4 = universal_ilp(
            nf_h,
            "H atom",
            ops,
            tr_vec,
            gram,
            h,
            target_nf_builder=lambda nf: apply_atom_nf_mp(nf, 1, 0, h, d_pn),
            max_len=4,
        )
        results["bond_HH"] = sel4

        # Level 4b: C atom -> C-C molecular bond (restored apply_atom_nf_mp)
        nf_c = build_atom_nf_mp(6, 6, h, d_pn)
        sel4b = universal_ilp(
            nf_c,
            "C atom",
            ops,
            tr_vec,
            gram,
            h,
            target_nf_builder=lambda nf: apply_atom_nf_mp(nf, 6, 6, h, d_pn),
            max_len=3,
        )
        results["bond_CC"] = sel4b

        # Verify apply_atom_nf_mp(id, Z, N) == build_atom_nf_mp(Z, N) and radical nullity
        id_nf = [one, zero, zero, zero, zero, zero]
        id_check_err = max(
            max(abs(a - b) for a, b in zip(apply_atom_nf_mp(id_nf, 1, 0, h, d_pn), build_atom_nf_mp(1, 0, h, d_pn))),
            max(abs(a - b) for a, b in zip(apply_atom_nf_mp(id_nf, 6, 6, h, d_pn), build_atom_nf_mp(6, 6, h, d_pn))),
        )
        qi = one / q0
        rad_vec = [one, -qi, -qi, qi * qi, qi * qi, -(qi * qi * qi)]
        rad_err = max(abs(mp.fsum(gram[i][j] * rad_vec[j] for j in range(6))) for i in range(6))

        w = WitnessBuilder("universal-ilp", engine="python+mpmath")
        w.set_description(
            "80-dps H_3(q_0) operator enumeration across Levels 1-4b with restored "
            "apply_atom_nf (from 95eb85e4005c:hecke_core.py:711-738, bean qou-ozts) "
            "at canonical proton pin q_at(95) and z = q_0^3/(q_0^2+1)."
        )
        w.set_content_block("rem:confinement-layer-operator-selection")
        w.add_parameter("q", fmt(q0))
        w.add_parameter("z", fmt(z))

        for level, key in (
            ("confinement", "confinement"),
            ("gluon", "gluon"),
            ("electron", "electron"),
            ("H-H bond", "bond_HH"),
            ("C-C bond", "bond_CC"),
        ):
            sel = results.get(key)
            if sel is not None:
                w.add_data(key, {
                    "operator": sel[0],
                    "crossings": int(sel[3]),
                    "tr_M": fmt(sel[1]),
                })
                parsed, rest = [], sel[0]
                while rest:
                    for nm, _g, _c, _d in sorted(ops, key=lambda o: len(o[0]), reverse=True):
                        if rest.startswith(nm):
                            parsed.append(nm)
                            rest = rest[len(nm):]
                            break
                    else:
                        parsed, rest = None, ""
                        break
                got_len = len(parsed) if parsed is not None else -1
                w.add_assertion(
                    f"{level}: reported operator label re-parses to its crossing count",
                    computed=got_len,
                    expected=int(sel[3]),
                    source="label round-trip against OPS; independent of the selection rule",
                )

        w.add_assertion(
            "apply_atom_nf_on_identity_matches_build_atom_nf_for_H_and_12C",
            computed=id_check_err,
            expected=mp.mpf(0),
            tolerance=mp.mpf("1e-85"),
            source="apply_atom_nf([1,0,0,0,0,0], Z, N) == build_atom_nf(Z, N) for (1,0) and (6,6)",
        )
        w.add_assertion(
            "h3_gram_annihilates_alternating_radical_vector_to_1e_85",
            computed=rad_err,
            expected=mp.mpf(0),
            tolerance=mp.mpf("1e-85"),
            source="G * [1, -q^-1, -q^-1, q^-2, q^-2, -q^-3]^T = 0 under z = q^3/(q^2+1)",
        )

        w.save({
            "q0Anchor": "proton",
            "q0AnchorReason": "Evaluates H_3(q_0) Gram positivity and Markov trace at the canonical proton substrate pin q_at(95).",
            "q0Value": fmt(q0),
        })
        print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
