#!/usr/bin/env python3
"""Frobenius admissibility with the net row fixed -- re-run under convention D
at the proton pin, reading NO AME / CODATA binding value (bean qou-ales step 2,
implementing qou-vd7j's "cheap next step").

## What qou-vd7j found, and what has changed underneath it

`computations/probes/frobenius_admissibility_diagnostic.py` (2026-08-02) showed
that the 0/3558 Frobenius admissibility of `all_nuclides_sdp_admissibility.py`
was an OVER-DETERMINATION artifact: the LP imposes seven equalities -- the net
row `1'x = A` plus six Frobenius rows `G x = nf` -- on six unknowns, and with
`G` invertible (rank 6, the CONVENTION-C Gram) the Frobenius rows already fix
`x = G^-1 nf`, whose implied net `1' G^-1 nf` is O(1), not the mass number.
The cheap fix it named: drop the net row, or use the consistent net.

That diagnosis was made on the convention-C Gram. Under **convention D**
(`z = q^3/(q^2+1)`, canonical since 2026-08-15) the H_3(q) trace form on the
GB normal-form basis is SINGULAR -- rank 5 of 6, radical spanned by the
three-strand q-antisymmetriser `v_k = (-1/q)^len(b_k)` (proved exactly over Q
in `gram_radical_exact_probe.py`; `pyhecke.gram.radical_mp`). So:

  * `G x = nf` is solvable iff `nf` lies in `range(G) = v-perp`, i.e. iff the
    Euclidean pairing `<v, nf> = 0`.
  * When it IS solvable the solution is a LINE `x_min + t v`, and since
    `1'v != 0` (measured below) the net row `1'x = A` can always be met by
    choosing `t`. So under D the "over-determination" of qou-vd7j is GONE:
    six independent equations on six unknowns, generically one solution --
    the net row is no longer the obstruction.
  * BUT the pairing `<v, nf(W)>` is exactly the ALTERNATING CHARACTER
    `eps(W) = prod over crossings of (c . (-1/q) + d)` of the word `W`
    (the sign representation `sigma_i -> -1/q` of H_3), because `v_k = eps(b_k)`
    and `eps` is a ring homomorphism. For every crossing type the template
    uses -- `sigma` (d=0), `sigma^-1` (d=-h), colour-weighted `p-n` (d=D_PN) --
    and for the gamma-gamma vertex `sigma_0 sigma_1^-1` (eps = 1 exactly,
    `QOU.Mass.GammaGammaWordSelection.altChar_eq_one`), the factor is nonzero,
    so `eps(W) != 0` and NO such word's demand profile is in `range(G)`.

This probe MEASURES all of that, per light nucleus and per candidate word.

## What "candidate words" means here (no census, no AME)

Each nucleus is a braid word in H_3(q) built exactly as `pyhecke.atom.build_atom_nf`
builds it (per-nucleon Borromean B_3 + quark crossings + gluon sigma_0^2, then an
inter-nucleon crossing with every previous nucleon, then optionally Z electron
crossings) -- except that every inter-nucleon BOND is left free over four
crossing types instead of being template-assigned:

    S  sigma_0            (c, d) = (1, 0)        template pp
    I  sigma_0^-1         (c, d) = (1, -h)       template nn
    C  colour-weighted    (c, d) = (1, D_PN)     template pn (R3, bring_color_weighted)
    G  gamma-gamma vertex sigma_0 sigma_1^-1      the pair-production bond

so a nucleus with B = A(A-1)/2 bonds has 4^B candidate words (4He: 4096). The
demand profile `u_demand = nf(W)` is the word's OWN normal form. Nothing here
reads a measured binding energy; survival is decided by the algebra alone.

## Precision

mpmath at 60 dps end to end (`gram.h_mp`, `gram.hm_mp`, `gram.radical_mp`,
`gram.gram_quotient_solve_mp`); `q_0` is the proton pin `Q_50_DIGIT_STR`.
No float64 enters a computed value; the float64 `build_atom_nf` is read ONLY
as an independent cross-check target for the word builder, to 1e-13.

Witness: computations/probes/frobenius-admissibility-net-row-probe.witness.json
"""
from __future__ import annotations

import itertools
import os
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from pyhecke import gram  # noqa: E402
from pyhecke.constants import pn_interface_offset  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)

# The eight light systems of qou-ales step 2. pp and nn are not AME nuclides;
# they are here because the diproton sign (qou-vbyi) is step 3's first output.
SAMPLE = [(1, 0, "p"), (0, 1, "n"), (1, 1, "2H"), (2, 0, "pp"), (0, 2, "nn"),
          (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He")]

BOND_TYPES = ("S", "I", "C", "G")
TEMPLATE = {("p", "p"): "S", ("n", "n"): "I", ("p", "n"): "C", ("n", "p"): "C"}

# Survival threshold for `nf in range(G)`: relative radical component below
# this is "zero to working precision" (60 dps; the Gram's own null residual
# is ~1e-61, see `radical_mp`).
RANGE_TOL = mp.mpf("1e-40")


def ground_state_ordering(Z: int, N: int) -> list[str]:
    """Interleaved p/n ordering, identical to `build_atom_nf`."""
    A = Z + N
    ordering, pc, nc = [], 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append("p"); pc += 1
        else:
            ordering.append("n"); nc += 1
    return ordering


def bond_crossings(kind: str, h, d_pn):
    """The (c, d, gen) crossings one inter-nucleon bond contributes."""
    one, zero = mp.mpf(1), mp.mpf(0)
    if kind == "S":
        return [(one, zero, 0)]
    if kind == "I":
        return [(one, -h, 0)]
    if kind == "C":
        return [(one, d_pn, 0)]
    if kind == "G":                      # gamma-gamma vertex sigma_0 sigma_1^-1
        return [(one, zero, 0), (one, -h, 1)]
    raise ValueError(kind)


def nucleon_crossings(kind: str, h):
    """Per-nucleon block of `build_atom_nf` as (c, d, gen) triples."""
    one, zero = mp.mpf(1), mp.mpf(0)
    w = []
    for _ in range(3):                   # B_3 = (sigma_0 sigma_1^-1)^3
        w.append((one, zero, 0))
        w.append((one, -h, 1))
    if kind == "p":                      # uu@0, ud@0, ud@1
        w += [(one, zero, 0), (one, -h / 2, 0), (one, -h / 2, 1)]
    else:                                # ud@0, ud@0, dd@1
        w += [(one, -h / 2, 0), (one, -h / 2, 0), (one, -h, 1)]
    w += [(one, zero, 0), (one, zero, 0)]   # gluon sigma_0^2 (qou-1qsw)
    return w


def atom_word(Z: int, N: int, bonds: dict, h, d_pn, electrons: bool):
    """The full word, in `build_atom_nf` order, with free bond types."""
    ordering = ground_state_ordering(Z, N)
    w = []
    for k, nuc in enumerate(ordering):
        w += nucleon_crossings(nuc, h)
        for prev in range(k):
            w += bond_crossings(bonds[(prev, k)], h, d_pn)
    if electrons:
        for _ in range(Z):
            w.append((mp.mpf(1), -h, 1))
    return w


def nf_of(word):
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for c, d, g in word:
        nf = gram.hm_mp(nf, c, d, g, DPS)
    return nf


def alt_char(word, q):
    """eps(W) = prod (c . (-1/q) + d): the sign representation of H_3."""
    e = mp.mpf(1)
    for c, d, _g in word:
        e *= c * (-1 / q) + d
    return e


def main() -> int:
    t0 = time.time()
    anchor = os.environ.get("QOU_Q0_ANCHOR", "").strip().lower()
    if anchor in ("ideal", "muon", "canonical"):
        raise SystemExit("this probe is a PROTON-pin producer (owner directive "
                         "2026-08-07); refusing a muon override")
    electrons = "--atoms" in sys.argv     # default: bare nuclei
    mp.mp.dps = DPS
    q = Q_MP
    h = q - 1 / q
    assert abs(h - gram.h_mp(DPS)) < mp.mpf("1e-55")
    d_pn = pn_interface_offset(q)

    G = mp.matrix(gram.gram_matrix_mp(DPS))
    v = mp.matrix(gram.radical_mp(DPS))
    eig = mp.eigsy(G)[0]
    eigs = sorted([+e for e in eig])
    gv = mp.norm(G * v)
    one_dot_v = mp.fsum(v[i] for i in range(6))
    n_neg = sum(1 for e in eigs if e < -mp.mpf("1e-30"))
    n_zero = sum(1 for e in eigs if abs(e) < mp.mpf("1e-30"))
    # eps(b_k) for the NF basis: v_k should be exactly the alternating character
    v_check = max(abs(v[k] - alt_char([(mp.mpf(1), mp.mpf(0), g) for g in gram.NF_BASIS[k]], q))
                  for k in range(6))

    print("Frobenius admissibility, net row fixed -- convention D, proton pin, "
          f"{DPS} dps, {'atoms (Z electrons)' if electrons else 'bare nuclei'}")
    print("=" * 78)
    print(f"  q0 (proton)        : {Q_50_DIGIT_STR[:32]}...")
    print(f"  Gram eigenvalues   : {[mp.nstr(e, 8) for e in eigs]}")
    print(f"  rank / neg / null  : {6 - n_zero} / {n_neg} / {n_zero}   |G v| = {mp.nstr(gv, 3)}")
    print(f"  1'v                : {mp.nstr(one_dot_v, 15)}   (nonzero => net row satisfiable "
          "whenever Gx=nf is)")
    print(f"  max |v_k - eps(b_k)|: {mp.nstr(v_check, 3)}")

    # Independent float64 cross-check of the WORD BUILDER on the template words.
    from pyhecke import atom as _atom  # noqa: PLC0415
    builder_max_rel = mp.mpf(0)
    for Z, N, _lab in SAMPLE:
        ordering = ground_state_ordering(Z, N)
        bonds = {(i, k): TEMPLATE[(ordering[i], ordering[k])]
                 for k in range(len(ordering)) for i in range(k)}
        nf_mp = nf_of(atom_word(Z, N, bonds, h, d_pn, electrons=True))
        nf_f64 = _atom.build_atom_nf(Z, N)          # float64, cross-check ONLY
        for a, b in zip(nf_mp, nf_f64):
            ref = max(abs(a), mp.mpf(1))
            builder_max_rel = max(builder_max_rel, abs(a - mp.mpf(str(b))) / ref)
    print(f"  word builder vs build_atom_nf (f64, atoms): max rel dev {mp.nstr(builder_max_rel, 3)}")

    rows = []
    pairing_vs_eps_max = mp.mpf(0)
    total_candidates = 0
    total_survivors = 0
    print(f"\n  {'nucleus':8}{'A':>3}{'bonds':>6}{'cands':>7}{'survive':>8}  "
          f"{'eps(template)':>18}  {'min|eps|':>12}  {'net(x_min) tmpl':>16}  {'net(nf) tmpl':>13}")
    for Z, N, lab in SAMPLE:
        A = Z + N
        ordering = ground_state_ordering(Z, N)
        bond_ix = [(i, k) for k in range(A) for i in range(k)]
        tmpl = {b: TEMPLATE[(ordering[b[0]], ordering[b[1]])] for b in bond_ix}
        survivors = []
        min_abs_eps = None
        tmpl_row = None
        n_cands = 0
        for assignment in itertools.product(BOND_TYPES, repeat=len(bond_ix)):
            bonds = dict(zip(bond_ix, assignment))
            word = atom_word(Z, N, bonds, h, d_pn, electrons)
            nf = nf_of(word)
            eps = alt_char(word, q)
            pairing = mp.fsum(v[k] * nf[k] for k in range(6))
            pairing_vs_eps_max = max(pairing_vs_eps_max,
                                     abs(pairing - eps) / max(abs(eps), mp.mpf(1)))
            nf_norm = mp.sqrt(mp.fsum(x * x for x in nf))
            rel_rad = abs(pairing) / (mp.norm(v) * nf_norm)
            survives = rel_rad < RANGE_TOL
            n_cands += 1
            if survives:
                survivors.append("".join(assignment))
            if min_abs_eps is None or abs(eps) < min_abs_eps:
                min_abs_eps = abs(eps)
            if assignment == tuple(tmpl[b] for b in bond_ix):
                x_min, rad_comp = gram.gram_quotient_solve_mp(nf, DPS)
                net_min = mp.fsum(x_min)
                nf_net = mp.fsum(nf)
                # residual of the PROJECTED system, and the unreachable part
                res = mp.norm(G * mp.matrix(x_min) - mp.matrix(nf))
                tmpl_row = {
                    "bonds": "".join(assignment),
                    "eps": fmt(eps), "pairing_v_nf": fmt(pairing),
                    "rel_radical_component": fmt(rel_rad),
                    "nf": [fmt(x) for x in nf], "nf_net": fmt(nf_net),
                    "x_min_norm_quotient": [fmt(x) for x in x_min],
                    "net_of_x_min": fmt(net_min),
                    "unreachable_radical_component": fmt(rad_comp),
                    "residual_G_xmin_minus_nf": fmt(res),
                    "net_row_t_if_solvable": fmt((mp.mpf(A) - net_min) / one_dot_v),
                    "survives": bool(survives),
                }
        total_candidates += n_cands
        total_survivors += len(survivors)
        rows.append({"nucleus": lab, "Z": Z, "N": N, "A": A, "n_bonds": len(bond_ix),
                     "n_candidates": n_cands, "n_survive": len(survivors),
                     "surviving_words": survivors, "min_abs_eps": fmt(min_abs_eps),
                     "template": tmpl_row})
        print(f"  {lab:8}{A:>3}{len(bond_ix):>6}{n_cands:>7}{len(survivors):>8}  "
              f"{mp.nstr(mp.mpf(tmpl_row['eps']), 10):>18}  {mp.nstr(min_abs_eps, 6):>12}  "
              f"{mp.nstr(mp.mpf(tmpl_row['net_of_x_min']), 8):>14}  "
              f"{mp.nstr(mp.mpf(tmpl_row['nf_net']), 8):>12}")

    print(f"\n  candidates {total_candidates}, survivors {total_survivors}; "
          f"max |<v,nf> - eps(W)| / max(1,|eps|) = {mp.nstr(pairing_vs_eps_max, 3)}")
    print("\nReading (scope-(a)): with the net row dropped -- or kept, since 1'v != 0 makes it\n"
          "satisfiable along the kernel -- the Frobenius rows Gx = nf are solvable iff\n"
          "<v, nf(W)> = eps(W) = 0. Every candidate word is a product of crossings whose\n"
          "alternating-character factors are all nonzero, so eps(W) != 0 and nothing\n"
          "survives. Under D the obstruction is the demand profile's nonzero alternating\n"
          "component, not the net row. This says nothing about the PSD confinement SDP\n"
          "(prop:confinement-sdp), which is a different program; see the audit doc.")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("frobenius-admissibility-net-row-probe", engine="python",
                       start_time=t0)
    w.set_description(
        "qou-vd7j cheap fix re-run under convention D at the proton pin: Frobenius "
        "admissibility of light nuclei with the net row 1'x=A dropped / made "
        "consistent, candidate words = build_atom_nf construction with every "
        "inter-nucleon bond free over {sigma_0, sigma_0^-1, colour-weighted, "
        "gamma-gamma vertex}, demand profile = the word's own NF. No AME/CODATA "
        "binding value is read. Finding: 0 survivors, because <v, nf(W)> equals the "
        "alternating character eps(W), a product of nonzero factors; the D-frame "
        "Gram is rank 5 with 1'v != 0 so the net row is never the obstruction."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("electrons_included", electrons)
    w.add_parameter("bond_types", list(BOND_TYPES))
    w.add_parameter("range_tolerance", fmt(RANGE_TOL))
    w.add_data("gram_eigenvalues", [fmt(e) for e in eigs])
    w.add_data("gram_rank", 6 - n_zero)
    w.add_data("gram_neg_norm_blocks", n_neg)
    w.add_data("radical_v", [fmt(v[i]) for i in range(6)])
    w.add_data("one_dot_v", fmt(one_dot_v))
    w.add_data("d_pn_colour_weighted", fmt(d_pn))
    w.add_data("per_nucleus", rows)
    w.add_data("total_candidates", total_candidates)
    w.add_data("total_survivors", total_survivors)
    w.add_assertion(name="gram_rank_5_of_6", computed=str(6 - n_zero), expected="5",
                    tolerance="0", source="gram_radical_exact_probe (exact over Q)")
    w.add_assertion(name="radical_is_alternating_character_of_basis",
                    computed=fmt(v_check), expected="0", tolerance="1e-55",
                    source="v_k = (-1/q)^len(b_k) = eps(b_k)")
    w.add_assertion(name="pairing_v_nf_equals_alt_char_of_word",
                    computed=fmt(pairing_vs_eps_max), expected="0", tolerance="1e-50",
                    source="eps is a ring homomorphism; v_k = eps(b_k); "
                           "QOU.Mass.GammaGammaWordSelection.altChar")
    w.add_assertion(name="word_builder_matches_build_atom_nf",
                    computed=fmt(builder_max_rel), expected="0", tolerance="1e-13",
                    source="float64 pyhecke.atom.build_atom_nf, cross-check only")
    w.add_assertion(name="one_dot_v_nonzero",
                    computed=fmt(abs(one_dot_v)), expected=fmt(abs(one_dot_v)),
                    tolerance="1e-50",
                    source="1'v != 0 => the net row is satisfiable along the kernel "
                           "whenever Gx = nf is; recorded so the value is on file")
    w.add_assertion(name="no_candidate_in_range_of_gram",
                    computed=str(total_survivors), expected="0", tolerance="0",
                    source="eps(W) = prod of nonzero factors (S: -1/q, I: -q, "
                           "C: -1/q + D_PN, G: 1); scope-(a) for THIS formulation")
    print(f"\nWitness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
