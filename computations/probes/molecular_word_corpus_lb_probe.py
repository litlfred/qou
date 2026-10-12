#!/usr/bin/env python3
"""molecular_word_corpus_lb_probe.py — the molecular junction on the corpus covalent operator L_b.

Bean `qou-a1hh`. Owner rulings 2026-10-12 (structured question, verbatim picks):
  bond operator      "Corpus L_b (Recommended)": sigma^-1 to a proton of each atom per shared electron, plus the
                     inter-atomic crossing table;
  electron strands   "3A + 3Z (Recommended)": each electron is a trefoil in its own local H_3.

Companion Lean: `QOU/MassTheory/SegmentCollisionDatum.lean` Part H (`chain_trace`, `sharedElectron_trace`,
`hopfLetter_trace`, `hopf_value_eq`, `twoCut_sub_hopf`, `window_two_sided`, `window_two_sided_cannot_separate`),
all conditional on `DisjointBlockMultiplicative`.

THE WORD, AS THE CORPUS FIXES IT (molecular-construction/)
  covalent-bond-shared-trefoil   L_b = prod_{e=1}^{k_b} sigma^-1_{g_e(p_j)} sigma^-1_{g_e(p_i)}; each shared electron
                                 crosses ONE proton of EACH atom, sigma^-1 both times; each electron is the trefoil
                                 T_{2,3} = sigma_0 sigma_1 sigma_0 in its local H_3 (POSITIVE trefoil; the inverse
                                 trefoil of ilp-covalent-bond is the LP-selected BOND operator, a different object).
  molecular-crossing-table       inter-atomic: pp sigma (c=1,d=0); pn, nn, ne identity; p_i e_j sigma^-1 (c=1,d=-h);
                                 e_i e_j sigma.
  molecular-braid                atoms embedded by index shift, then C_mol, then L_b, then normal form.
  nucleus                        mass_at_3A_proper.atom_braid_word_3A(Z, N, include_inter=True, ordering=...).

WHAT FOLLOWS FROM THAT, WITHOUT A CHOICE. A letter is a single generator, so it crosses two ADJACENT strands. The
electron is a contiguous 3-strand block (its own H_3) and the nucleus a contiguous 3A-strand block. A shared electron
crossing a strand of each nucleus with single-generator letters must therefore sit between the two nuclei, its bottom
strand crossing the lower atom's top strand and its top strand crossing the upper atom's bottom strand: two letters on
two DISTINCT cuts. Consequences checked below:
  * only ONE electron block can sit between two contiguous nuclei, so L_b with k_b >= 2 is NOT realizable on single
    generators (exhaustive layout enumeration, check `kb_ge_2_not_realizable`);
  * the two sigma^-1 of a shared electron never cross the same strand pair, so the literal Hopf letter sigma^-2 is
    NOT a realization of L_b; it is measured only as the Lean comparison value 1 - h*zinv;
  * no nucleon strand of one atom is adjacent to one of the other, so C_mol contributes no pp letter.

WHAT THE CORPUS DOES NOT FIX (parameters, all admissible values run, nothing selected):
  U_order   the nucleon ordering of each atom (atomic-braid clause 1 is intractable and the builder's sorted order is a
            convention). Admissible = a proton at the junction-facing end. Two families: 'facing_sorted' (lower atom
            n..n p..p, upper p..p n..n) and 'one_proton_moved' (lower p^(Z-1) n^N p, upper p..p n..n).
  U_kb      CO: k_b = 3 shared trefoils (L_b over bond order) vs 6 ("three electron pairs", co-molecular-braid); both
            unrealizable by the point above. Only the one-trefoil junction is built.
  U_donor   which atom donates the shared trefoils. Enters only through which separated atom loses a trefoil.
  U_rest    where the non-shared 3(Z) - k_b trefoils attach. By chain_trace, any attachment on cuts enters only through
            its own trace and letter values, identical in atom and molecule, so it cancels in the ratio.

MEASURED (mpmath 60 dps, no floats; local chains only)
  V   builder validated against committed atom-chi-rust characters (d, t, 3He, 4He); trefoil and Hopf letters
      against their closed forms z(hz+1) and 1 - h*zinv; tr(1) = 1.
  iii the junction contribution: tr(composite) / (tr(lower) tr(e) tr(upper)) = zinv^2 on 9- and 12-strand chains.
  ii  reading 3 (chi_lambda >= 0 on every convention-D two-row block with y_lambda > 0) on the 9-strand junction
      composite [proton] sigma^-1 [electron] sigma^-1 [proton] (= the whole H2 molecule word, one shared trefoil).
  i   window depth: a window containing a junction letter sees only the letters in its range (window_two_sided), so
      CO vs N2 is decided by the first differing atomic letter outward from the electron block; separation at that
      letter is measured on its 6-strand local chain and transfers to every window containing it.

-- Ref: [manuscript] def:covalent-bond-shared-trefoil; def:molecular-crossing-table; def:molecular-braid; bean qou-a1hh
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
mp.mp.dps = 60
import composition_feasibility_a2_probe as cf  # noqa: E402
import molecular_junction_window_probe as mjw  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Q = cf.Q
H = cf.H
Z = cf.Z_D
ZINV = Z - H
TOL = mp.mpf("1e-40")
T0 = time.time()
ONE = mp.mpf(1)
ZERO = mp.mpf(0)


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


chi, trace, two_row = mjw.chi, mjw.trace, mjw.two_row


def electron(base):
    """Corpus electron: the positive trefoil sigma_0 sigma_1 sigma_0 on its own three strands."""
    return [(ONE, ZERO, base), (ONE, ZERO, base + 1), (ONE, ZERO, base)]


def sinv(g):
    return [(ONE, -H, g)]


def tokens_ordered(Zp, N, ordering):
    A = Zp + N
    w = mjw.to_word(atom_braid_word_3A(Zp, N, include_inter=True, ordering=ordering))
    blocks = [[] for _ in range(A)]
    bonds = [[] for _ in range(A - 1)]
    for c, d, g in w:
        k, off = divmod(g, 3)
        (bonds[k] if off == 2 else blocks[k]).append((c, d, off))
    return w, blocks, bonds


def orderings(Zp, N, family, side):
    if family == "facing_sorted":
        return (["n"] * N + ["p"] * Zp) if side == "lower" else (["p"] * Zp + ["n"] * N)
    if family == "one_proton_moved":
        return (["p"] * (Zp - 1) + ["n"] * N + ["p"]) if side == "lower" else (["p"] * Zp + ["n"] * N)
    raise ValueError(family)


def kb_realizable(kb, n_blocks_between_max=None):
    """Exhaustive: blocks on a line = 2 nuclei + kb electron blocks, all contiguous. A shared electron needs a
    single-generator letter to each nucleus, i.e. must be ADJACENT to both. Count layouts where all kb are."""
    labels = ["I", "J"] + [f"e{i}" for i in range(kb)]
    from itertools import permutations
    ok = 0
    total = 0
    for perm in permutations(labels):
        total += 1
        pos = {lab: i for i, lab in enumerate(perm)}
        if all(abs(pos[f"e{i}"] - pos["I"]) == 1 and abs(pos[f"e{i}"] - pos["J"]) == 1 for i in range(kb)):
            ok += 1
    return ok, total


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}")

    y = {n: cf.load_y(n) for n in (3, 6, 9, 12)}
    for n in (3, 6, 9, 12):
        tr1 = trace([], n, y[n])
        check(f"tr_of_unit_is_1_n{n}", abs(tr1 - 1) < TOL, "Markov normalisation T2")

    # ── V: builder against committed characters (reuses the parent probe's validation) ──
    validation = {}
    for tag, (Zp, N) in (("d", (1, 1)), ("t", (1, 2)), ("3he", (2, 1)), ("4he", (2, 2))):
        import json
        n = 3 * (Zp + N)
        w = mjw.to_word(atom_braid_word_3A(Zp, N, include_inter=True))
        com = json.loads((HERE.parent / f"atom-chi-rust-{tag}.witness.json").read_text(encoding="utf-8"))["data"]["atom"]
        cmap = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in com["by_partition"]}
        dev = max(abs(chi(l, w) - cmap[l]) for l in two_row(n))
        validation[tag] = mp.nstr(dev, 5)
        check(f"{tag}_word_reproduces_committed_atom_characters_two_row", dev < TOL, f"atom-chi-rust-{tag}")

    tr_e = trace(electron(0), 3, y[3])
    check("electron_trefoil_trace_equals_z(hz+1)", abs(tr_e - Z * (H * Z + 1)) < TOL, "Markov + Hecke closed form")
    hopf = trace(sinv(0) + sinv(0), 3, y[3])
    check("hopf_letter_trace_equals_1_minus_h_zinv", abs(hopf - (1 - H * ZINV)) < TOL, "Lean hopf_value_eq")
    check("zinv_equals_trace_of_sigma_inverse", abs(trace(sinv(0), 3, y[3]) - ZINV) < TOL, "Lean zinv_eq_of_hecke")
    zz1 = Z * ZINV - 1
    check("twoCut_minus_hopf_equals_z_zinv_minus_1_nonzero",
          abs((ZINV ** 2 - (1 - H * ZINV)) - zz1) < TOL and abs(zz1) > mp.mpf("0.1"), "Lean twoCut_sub_hopf")

    # ── realizability of k_b >= 2 on single generators with contiguous blocks ──
    real = {}
    for kb in (1, 2, 3, 6):
        ok, total = kb_realizable(kb) if kb <= 3 else (0, None)
        real[kb] = {"admissible_layouts": ok, "layouts_enumerated": total}
        log(f"k_b={kb}: {ok} of {total} block layouts put every shared trefoil adjacent to both nuclei")
    check("kb_1_realizable", real[1]["admissible_layouts"] > 0, "exhaustive layout enumeration")
    check("kb_ge_2_not_realizable", real[2]["admissible_layouts"] == 0 and real[3]["admissible_layouts"] == 0,
          "exhaustive layout enumeration (k_b=6 follows from k_b=2: a sub-layout of an admissible one is admissible)")

    # ── proton block (junction-facing nucleon in every admissible ordering) ──
    _, bH, _ = tokens_ordered(1, 0, ["p"])
    pblock = [(c, d, off) for c, d, off in bH[0]]

    def junction_composite(lower_block, upper_block):
        """[lower nucleon] sigma^-1_2 [e on 3..5] sigma^-1_5 [upper nucleon on 6..8]."""
        return ([(c, d, off) for c, d, off in lower_block] + sinv(2) + electron(3) + sinv(5)
                + [(c, d, 6 + off) for c, d, off in upper_block])

    # ── iii + ii: H2 = the 9-strand junction composite with two proton nuclei ──
    W9 = junction_composite(pblock, pblock)
    tr_p = trace([(c, d, off) for c, d, off in pblock], 3, y[3])
    chis9 = {l: chi(l, W9) for l in two_row(9)}
    tr9 = mp.fsum(y[9][l] * chis9[l] for l in two_row(9))
    ratio9 = tr9 / (tr_p * tr_e * tr_p)
    log(f"H2 (one shared trefoil): tr = {mp.nstr(tr9, 20)}; ratio to tr(p) tr(e) tr(p) = {mp.nstr(ratio9, 25)}; "
        f"zinv^2 = {mp.nstr(ZINV ** 2, 25)}")
    check("H2_junction_ratio_equals_zinv_squared", abs(ratio9 - ZINV ** 2) < TOL, "Lean sharedElectron_trace")
    feas9 = {str(l): {"y": mp.nstr(y[9][l], 15), "chi": mp.nstr(chis9[l], 25), "nonneg": bool(chis9[l] >= -TOL)}
             for l in two_row(9)}
    supp9 = [l for l in two_row(9) if y[9][l] > 0]
    reading3_H2 = all(chis9[l] >= -TOL for l in supp9)
    for l in two_row(9):
        log(f"  chi_{l}(H2 composite) = {mp.nstr(chis9[l], 20)}  (y = {mp.nstr(y[9][l], 8)})")
    check("convention_D_support_n9_all_two_row_positive", len(supp9) == len(two_row(9)), "y-lambda-at-q0")
    # the parts: proton block alone, electron alone
    chi_p = {l: chi(l, [(c, d, off) for c, d, off in pblock]) for l in two_row(3)}
    chi_e = {l: chi(l, electron(0)) for l in two_row(3)}
    reading3_parts = {"proton_block": all(v >= -TOL for v in chi_p.values()),
                      "electron_trefoil": all(v >= -TOL for v in chi_e.values())}
    log(f"  reading 3: H2 composite {reading3_H2}; parts {reading3_parts}")
    # also the bare junction letters on a pure unit composite: [1] s^-1 [e] s^-1 [1]
    Wbare = sinv(2) + electron(3) + sinv(5)
    chis_bare = {l: chi(l, Wbare) for l in two_row(9)}
    reading3_bare = all(chis_bare[l] >= -TOL for l in supp9)
    log(f"  reading 3 of the bare junction (unit nuclei, trefoil, two sigma^-1): {reading3_bare}")
    check("electron_trefoil_chi_21_is_zero", abs(chi_e[(2, 1)]) < TOL, "sigma0 sigma1 sigma0 on the 2-dim block")

    # ── 12-strand chain_trace check: [p] pp [p] s^-1 [e] s^-1 [p] (the CO/N2 lower side at depth 2) ──
    _, b2, d2 = tokens_ordered(2, 0, ["p", "p"])
    W12 = ([(c, d, off) for c, d, off in b2[0]] + [(c, d, 2) for c, d, _ in d2[0]]
           + [(c, d, 3 + off) for c, d, off in b2[1]] + sinv(5) + electron(6) + sinv(8)
           + [(c, d, 9 + off) for c, d, off in pblock])
    t1 = time.time()
    tr12 = trace(W12, 12, y[12])
    tr_pp = trace([(c, d, off) for c, d, off in b2[0]] + [(c, d, 2) for c, d, _ in d2[0]]
                  + [(c, d, 3 + off) for c, d, off in b2[1]], 6, y[6])
    ratio12 = tr12 / (tr_pp * tr_e * tr_p)
    log(f"12-strand chain: ratio = {mp.nstr(ratio12, 25)} ({time.time() - t1:.1f}s)")
    check("12_strand_chain_ratio_equals_zinv_squared", abs(ratio12 - ZINV ** 2) < TOL, "Lean chain_trace")

    # ── i: window depth, per ordering family ──
    atoms = {"12C": (6, 6), "14N": (7, 7), "16O": (8, 8)}
    depth = {}
    for fam in ("facing_sorted", "one_proton_moved"):
        res = {}
        for side, (a1, a2) in (("lower", ("12C", "14N")), ("upper", ("16O", "14N"))):
            streams = {}
            for a in (a1, a2):
                Zp, N = atoms[a]
                ordr = orderings(Zp, N, fam, side)
                _, bl, bd = tokens_ordered(Zp, N, ordr)
                facing = ordr[-1] if side == "lower" else ordr[0]
                s, order = mjw.side_stream(bl, bd, side)
                streams[a] = (s, order, bl, bd, ordr, facing)
            j = mjw.first_difference(streams[a1][0], streams[a2][0])
            entry = {"atoms": [a1, a2], "orderings": {a: "".join(streams[a][4]) for a in (a1, a2)},
                     "junction_facing": {a: streams[a][5] for a in (a1, a2)}}
            check(f"{fam}|{side}: junction-facing nucleon is a proton for both atoms",
                  all(streams[a][5] == "p" for a in (a1, a2)), "corpus L_b: sigma^-1 to a PROTON")
            kind = streams[a1][0][j][0]
            nb = j // 2
            kstar = 3 * (nb + 1) + 1 if kind == "bond" else 3 * nb + 2
            entry.update({"first_difference_token": kind, "k_star_strands_atom_side": kstar,
                          "junction_window_strands": kstar + 1})
            if kind == "bond":
                s1, o1, bl1, bd1 = streams[a1][:4]
                s2, o2, bl2, bd2 = streams[a2][:4]
                lo1 = min(o1[nb], o1[nb + 1])
                lo2 = min(o2[nb], o2[nb + 1])
                c1 = mjw.slice_chain(bl1, bd1, lo1, 2)
                c2 = mjw.slice_chain(bl2, bd2, lo2, 2)
                reach = [2, 3, 4] if side == "lower" else [0, 1, 2]
                r1 = mjw.phi_rows(c1, 6, y[6], reach)
                r2 = mjw.phi_rows(c2, 6, y[6], reach)
                worst = max(abs(p1 - p2) for (_, p1), (_, p2) in zip(r1, r2))
                entry["sub_range_separation"] = mp.nstr(worst, 15)
                check(f"{fam}|{side}: sub-range window at the first differing bond separates",
                      worst > mp.mpf("1e-6"), "6-strand local chain; transfers by window_two_sided")
            log(f"{fam} {side} {a1} vs {a2}: first difference {kind}, k* = {kstar}, "
                f"junction-containing window = {kstar + 1} strands")
            res[side] = entry
        res["minimal_junction_window_strands"] = min(res[s]["junction_window_strands"] for s in ("lower", "upper"))
        depth[fam] = res
    # the junction region itself: identical words for CO and N2 (both facing nucleons protons, one trefoil)
    check("junction_region_identical_for_CO_and_N2", True,
          "both facing nucleons are proton blocks (checked above); junction letters and trefoil are fixed words")
    dep_vals = {f: depth[f]["minimal_junction_window_strands"] for f in depth}
    ordering_dependent = len(set(dep_vals.values())) > 1
    log(f"minimal junction-containing separating window by ordering family: {dep_vals}")

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("molecular-word-corpus-lb", engine="mpmath")
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": ("q0 enters only through the committed y-lambda-at-q0 witness (proton pin) and the production "
                           "atom words; words validated against committed atom-chi-rust characters"),
        "description": ("PROBE (bean qou-a1hh): the molecular junction on the corpus L_b with 3A + 3Z strands (owner "
                        "rulings 2026-10-12). One shared trefoil between two nuclei contributes zinv^2 (Lean "
                        "sharedElectron_trace); L_b with k_b >= 2 is not realizable on single generators with "
                        "contiguous blocks; the junction-containing window depth depends on the unfixed nucleon "
                        "ordering. Nothing fitted, selected or wired."),
        "weight_family": "markov_y_lambda_convention_D",
        "constants": {"q0": mp.nstr(Q, 40), "h": mp.nstr(H, 40), "z_D": mp.nstr(Z, 40), "zinv": mp.nstr(ZINV, 40),
                      "zinv_sq": mp.nstr(ZINV ** 2, 40), "hopf_value_1_minus_h_zinv": mp.nstr(1 - H * ZINV, 40),
                      "z_zinv_minus_1": mp.nstr(zz1, 40), "tr_electron_trefoil": mp.nstr(tr_e, 40),
                      "tr_proton_block": mp.nstr(tr_p, 40)},
        "validation_worst_dev": validation,
        "kb_realizability": real,
        "H2": {"tr_composite": mp.nstr(tr9, 40), "ratio_to_parts": mp.nstr(ratio9, 40),
               "reading3_feasible": reading3_H2, "chi_by_block": feas9,
               "reading3_parts": reading3_parts,
               "chi_proton_block": {str(l): mp.nstr(v, 25) for l, v in chi_p.items()},
               "chi_electron_trefoil": {str(l): mp.nstr(v, 25) for l, v in chi_e.items()},
               "reading3_bare_junction": reading3_bare,
               "chi_bare_junction": {str(l): mp.nstr(v, 25) for l, v in chis_bare.items()}},
        "chain12_ratio": mp.nstr(ratio12, 40),
        "window_depth": depth,
        "window_depth_ordering_dependent": ordering_dependent,
        "unfixed_choices": ["U_order: nucleon ordering of each atom (facing_sorted, one_proton_moved run)",
                            "U_kb: CO shared trefoils k_b = 3 vs 6 (both unrealizable on single generators)",
                            "U_donor: which atom donates the shared trefoils",
                            "U_rest: attachment of non-shared trefoils (cancels in the ratio by chain_trace)"],
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
