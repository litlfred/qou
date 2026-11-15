#!/usr/bin/env python3
"""molecular_junction_window_probe.py — how deep must a window at a molecular junction reach to tell CO from N2?

Owner 2026-10-12 (bean `qou-a1hh`): "measure window depth at a molecular junction (C+O -> CO scale), using the
composition law". Companion: `QOU/MassTheory/SegmentCollisionDatum.lean` Parts E and G (`window_factor`,
`window_factor_below`, `junction_window_above`, `junction_window_below`, `junction_cannot_separate_above`).

WHAT IS MISSING, FIRST. The corpus has NO junction-letter rule for the production nucleon chain.
`molecular-construction/molecular-braid.md` names a "molecular crossing table" and never specifies it, and its atoms
carry A+Z strands (electrons included); `mass_at_3A_proper.atom_braid_word_3A` is a 3A-strand NUCLEUS word with no
electron strands. `unified-mass-molecular.py` / `co_bond_order_active_set.py` are scalar Phi_1 models (float), not
Hecke words. So no molecule word is built here and no junction letter is invented. Part G is what makes that
unnecessary for every window that does NOT contain the junction generator: such a window sees one atom only,
whatever the junction letter is. A window that DOES contain the junction generator is undetermined here.

THE MOLECULE. A diatomic word is `a * J * b`: lower atom `a` (its top strands next to the junction), junction `J`
on one generator, upper atom `b` (its bottom strands next to the junction). Atoms are the production words
`atom_braid_word_3A(Z, N, include_inter=True)` at their defaults (inter-nucleon ordering sorted p...p n...n, chain
topology, colour-weighted p-n letter). Note D1 in that builder's docstring: the chain topology is refuted and the
sorted ordering is a convention, not a derivation, so the depths below are statements about THAT word.

THE MEASUREMENT.
  V  Validate the builder on every atom with committed characters (d, t, 3He, 4He; two-row blocks).
     C, N, O have no committed characters, so their words are validated LETTER BY LETTER: every nucleon block and
     every bond letter must equal (exact mpf ==) the corresponding letter of the validated 4He word, which carries
     all five letter kinds (p block, n block, pp, pn, nn bonds).
  S  Exact word comparison outward from the junction on each side. By Part G plus Part E (top windows, lower side)
     and its mirror (bottom windows, upper side), a window that stops short of the first differing letter cannot
     separate. The first differing letter fixes the candidate depth k* (strands, counted from the junction).
  L  Separation at k* is measured on the 6-strand local chain [block][first differing bond][block], sliced out of the
     production words. The cut is legitimate by window_factor / window_factor_below (each side is cut at the next
     single-generator bond outward and inward); checked numerically on 9-strand chains extended both ways.
     phi(x) = tr(w x) / tr(w), convention-D weights from `y-lambda-at-q0.witness.json` (two-row blocks only).

mpmath 60 dps throughout; no float arithmetic. Nothing fitted, selected or wired.
-- Ref: [manuscript] bean qou-a1hh, qou-jfx8
"""
from __future__ import annotations

import json
import sys
import time
from itertools import permutations
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
mp.mp.dps = 60
import composition_feasibility_a2_probe as cf  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
C = HERE.parent
TOL = mp.mpf("1e-40")
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def to_word(triples):
    return [(mp.mpf(c), mp.mpf(d), int(g)) for c, d, g in triples]


_COLS: dict = {}


def chi(shape, word):
    """chi_lambda of a word, same seminormal matrices as cf.chi, multiplied using their sparsity (each column of a
    seminormal sigma has at most two nonzeros). Cross-checked against cf.chi in main()."""
    key = tuple(shape)
    if key not in _COLS:
        mats, dim = cf.sigmas(shape)
        _COLS[key] = ([[[(k, S[k][j]) for k in range(dim) if S[k][j] != 0] for j in range(dim)] for S in mats], dim)
    cols, dim = _COLS[key]
    M = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(dim)] for i in range(dim)]
    for c, d, g in word:
        cg = cols[g]
        M = [[c * mp.fsum(row[k] * v for k, v in cg[j]) + d * row[j] for j in range(dim)] for row in M]
    return mp.fsum(M[i][i] for i in range(dim))


def two_row(n):
    return [l for l in cf.partitions_of(n) if len(l) <= 2]


def trace(word, n, y):
    return mp.fsum(y[l] * chi(l, word) for l in two_row(n) if y[l] != 0)


def reduced_words(gens):
    k = len(gens) + 1
    out = []
    for perm in permutations(range(k)):
        p, w = list(perm), []
        changed = True
        while changed:
            changed = False
            for i in range(k - 1):
                if p[i] > p[i + 1]:
                    p[i], p[i + 1] = p[i + 1], p[i]
                    w.append(gens[i])
                    changed = True
        out.append(list(reversed(w)))
    return out


def tokens(Z, N):
    """Split the production word into per-nucleon blocks (offsets 0,1 within the nucleon) and bond letters."""
    A = Z + N
    w = to_word(atom_braid_word_3A(Z, N, include_inter=True))
    blocks = [[] for _ in range(A)]
    bonds = [[] for _ in range(A - 1)]
    for c, d, g in w:
        k, off = divmod(g, 3)
        (bonds[k] if off == 2 else blocks[k]).append((c, d, off))
    return w, blocks, bonds


def slice_chain(blocks, bonds, k0, count):
    """Letters of nucleons k0..k0+count-1 and the bonds between them, generators shifted to start at 0."""
    out = []
    for i in range(count):
        out += [(c, d, 3 * i + off) for c, d, off in blocks[k0 + i]]
        if i < count - 1:
            out += [(c, d, 3 * i + 2) for c, d, _ in bonds[k0 + i]]
    return out


def side_stream(blocks, bonds, side):
    """Tokens read outward from the junction: lower atom top-down ('lower'), upper atom bottom-up ('upper')."""
    A = len(blocks)
    order = list(range(A - 1, -1, -1)) if side == "lower" else list(range(A))
    s = []
    for i, k in enumerate(order):
        s.append(("block", tuple(blocks[k])))
        if i < A - 1:
            nb = order[i + 1]
            s.append(("bond", tuple(bonds[min(k, nb)])))
    return s, order


def first_difference(s1, s2):
    for j in range(min(len(s1), len(s2))):
        if s1[j] != s2[j]:
            return j
    return None


def phi_rows(chain, n, y, gens):
    tr_w = trace(chain, n, y)
    rows = []
    for x in reduced_words(gens):
        xw = [(mp.mpf(1), mp.mpf(0), g) for g in x]
        rows.append((tuple(x), trace(chain + xw, n, y) / tr_w))
    return rows


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}")

    y = {n: cf.load_y(n) for n in (6, 9, 12)}
    for n in (6, 9, 12):
        supp = sorted(l for l in cf.partitions_of(n) if y[n][l] != 0)
        check(f"convention_D_support_n{n}_is_two_row", supp == sorted(two_row(n)), "y-lambda-at-q0")

    wd = to_word(atom_braid_word_3A(1, 1, include_inter=True))
    dfast = max(abs(chi(l, wd) - cf.chi(l, wd)) for l in two_row(6))
    check("sparse_chi_matches_cf_chi_on_the_deuteron_word", dfast < TOL, "composition_feasibility_a2_probe.chi")

    # ── V: validation on every atom with committed characters ──
    validation = {}
    for tag, (Z, N) in (("d", (1, 1)), ("t", (1, 2)), ("3he", (2, 1)), ("4he", (2, 2))):
        n = 3 * (Z + N)
        w = to_word(atom_braid_word_3A(Z, N, include_inter=True))
        com = json.loads((C / f"atom-chi-rust-{tag}.witness.json").read_text(encoding="utf-8"))["data"]["atom"]
        cmap = {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in com["by_partition"]}
        dev = max(abs(chi(l, w) - cmap[l]) for l in two_row(n))
        validation[tag] = mp.nstr(dev, 5)
        log(f"{tag}: worst |chi - chi_committed| on two-row blocks = {mp.nstr(dev, 5)}")
        check(f"{tag}_word_reproduces_committed_atom_characters_two_row", dev < TOL, f"atom-chi-rust-{tag}")

    _, b4, d4 = tokens(2, 2)        # 4He: p p n n -> blocks p,p,n,n ; bonds pp, pn, nn
    ref = {"p": b4[0], "n": b4[3], "pp": d4[0], "pn": d4[1], "nn": d4[2]}
    check("4He_carries_two_distinct_blocks_and_three_distinct_bonds",
          b4[0] == b4[1] and b4[2] == b4[3] and b4[0] != b4[2] and len({tuple(v) for v in d4}) == 3, "builder")

    atoms = {"12C": (6, 6), "14N": (7, 7), "16O": (8, 8), "13C": (6, 7), "13N": (7, 6)}
    tok = {}
    for name, (Z, N) in atoms.items():
        w, blocks, bonds = tokens(Z, N)
        kinds = ["p"] * Z + ["n"] * N
        ok = all(blocks[k] == ref[kinds[k]] for k in range(Z + N))
        ok &= all(bonds[k] == ref["".join(sorted(kinds[k] + kinds[k + 1], reverse=True))] for k in range(Z + N - 1))
        check(f"{name}_every_letter_equals_a_validated_4He_letter", ok, "atom-chi-rust-4he via letter identity")
        tok[name] = (blocks, bonds, kinds)

    # ── S + L: each molecule pair, each side ──
    pairs = {
        "CO_vs_N2 (C below junction, O above)": (("12C", "16O"), ("14N", "14N")),
        "OC_vs_N2 (O below junction, C above)": (("16O", "12C"), ("14N", "14N")),
        "13C2_vs_13N2 (mirror nuclei, 26 nucleons each)": (("13C", "13C"), ("13N", "13N")),
    }
    results = {}
    for label, (m1, m2) in pairs.items():
        log(f"== {label}")
        res = {}
        for side, idx in (("lower", 0), ("upper", 1)):
            a1, a2 = m1[idx], m2[idx]
            bl1, bd1, k1 = tok[a1]
            bl2, bd2, k2 = tok[a2]
            s1, o1 = side_stream(bl1, bd1, side)
            s2, o2 = side_stream(bl2, bd2, side)
            j = first_difference(s1, s2)
            entry = {"atoms": [a1, a2]}
            if j is None:
                entry["verdict"] = "identical until one atom ends: no off-junction window separates"
                res[side] = entry
                log(f"  {side}: {a1} vs {a2} identical over the shorter atom")
                continue
            kind = s1[j][0]
            nb = j // 2                               # nucleons fully inside before the difference
            if kind == "bond":
                kstar = 3 * (nb + 1) + 1               # window must contain the bond generator
            else:
                kstar = 3 * nb + 2                     # window must contain one intra generator of block nb
            entry.update({"first_difference_token": kind, "nucleons_identical_from_junction": nb + (1 if kind == "bond" else 0),
                          "k_star_strands": kstar})
            log(f"  {side}: {a1} vs {a2}: identical over {entry['nucleons_identical_from_junction']} nucleon(s) "
                f"from the junction; first difference is a {kind}; candidate k* = {kstar} strands")
            if kind == "bond":
                # the bond is between outward-ordered nucleons nb and nb+1
                for t, (bl, bd, kk, order) in (("m1", (bl1, bd1, k1, o1)), ("m2", (bl2, bd2, k2, o2))):
                    lo = min(order[nb], order[nb + 1])
                    entry[f"{t}_bond_kind"] = "".join(sorted(kk[lo] + kk[lo + 1], reverse=True))
                # local 6-strand chains; junction side is local top (lower atom) or local bottom (upper atom)
                short = [3, 4] if side == "lower" else [0, 1]
                reach = [2, 3, 4] if side == "lower" else [0, 1, 2]
                chains = {}
                for t, (bl, bd, order) in (("m1", (bl1, bd1, o1)), ("m2", (bl2, bd2, o2))):
                    lo = min(order[nb], order[nb + 1])
                    chains[t] = (bl, bd, lo, slice_chain(bl, bd, lo, 2))
                phis = {}
                for wname, gens in (("short", short), ("reach", reach)):
                    t1 = time.time()
                    r1 = phi_rows(chains["m1"][3], 6, y[6], gens)
                    r2 = phi_rows(chains["m2"][3], 6, y[6], gens)
                    worst = max(abs(p1 - p2) for (_, p1), (_, p2) in zip(r1, r2))
                    phis[wname] = (worst, r1, r2)
                    log(f"    window {wname} gens {gens}: {len(r1)} basis words, worst |phi1 - phi2| = "
                        f"{mp.nstr(worst, 8)}  ({time.time() - t1:.1f}s)")
                entry["short_window_worst_sep"] = mp.nstr(phis["short"][0], 12)
                entry["reach_window_worst_sep"] = mp.nstr(phis["reach"][0], 20)
                entry["reach_window_rows"] = [{"x": list(x), "phi_m1": mp.nstr(p1, 25), "phi_m2": mp.nstr(p2, 25)}
                                              for (x, p1), (_, p2) in zip(phis["reach"][1], phis["reach"][2])]
                check(f"{label}|{side}: window short of the first differing bond does not separate",
                      phis["short"][0] < TOL, "Lean window_cannot_separate(_below) + junction lemmas")
                check(f"{label}|{side}: window reaching the first differing bond separates (k* = {kstar})",
                      phis["reach"][0] > mp.mpf("1e-6"), "measured on the 6-strand local chain")
                # cut validation: extend the local chain one nucleon outward and one inward; same phi on 'reach'
                bl, bd, lo, ch6 = chains["m1"]
                ext = []
                for direction in ("down", "up"):
                    k0, shift = (lo - 1, 3) if direction == "down" else (lo, 0)
                    if k0 < 0 or k0 + 3 > len(bl):
                        continue
                    ch9 = slice_chain(bl, bd, k0, 3)
                    t1 = time.time()
                    r9 = phi_rows(ch9, 9, y[9], [g + shift for g in reach])
                    dev = max(abs(p9 - p6) for (_, p9), (_, p6) in zip(r9, phis["reach"][1]))
                    ext.append((direction, dev))
                    log(f"    cut check ({direction}, H_9 vs H_6): worst |phi9 - phi6| = {mp.nstr(dev, 5)} "
                        f"({time.time() - t1:.1f}s)")
                entry["cut_checks"] = {d: mp.nstr(v, 5) for d, v in ext}
                check(f"{label}|{side}: 6-strand cut agrees with 9-strand chains (window_factor)",
                      ext and all(v < TOL for _, v in ext), "Lean window_factor / window_factor_below")
            res[side] = entry
        ks = [res[s]["k_star_strands"] for s in res if "k_star_strands" in res[s]]
        res["minimal_separating_k_off_junction"] = min(ks) if ks else None
        log(f"  => minimal separating off-junction window: {res['minimal_separating_k_off_junction']} strands")
        results[label] = res

    co = results["CO_vs_N2 (C below junction, O above)"]
    check("CO_vs_N2_minimal_off_junction_window_is_19_strands_on_the_carbon_side",
          co["minimal_separating_k_off_junction"] == 19 and co["lower"]["k_star_strands"] == 19
          and co["upper"]["k_star_strands"] == 22, "S + L above")

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("molecular-junction-window", engine="mpmath")
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": ("q0 enters only through the committed y-lambda-at-q0 witness and the production atom words "
                           "(proton pin); atom words validated against committed atom-chi-rust characters"),
        "description": ("PROBE (bean qou-a1hh): window depth at a molecular junction on the production nucleon chain. "
                        "Windows off the junction generator see one atom only (Lean Part G), so CO vs N2 is decided by "
                        "how far the atoms' words agree outward from the junction. The corpus has no junction-letter "
                        "rule; windows containing the junction generator are not measured. Nothing fitted, selected "
                        "or wired."),
        "weight_family": "markov_y_lambda_convention_D",
        "builder": "mass_at_3A_proper.atom_braid_word_3A(Z, N, include_inter=True), default sorted ordering",
        "missing_in_corpus": ("junction-letter rule ('molecular crossing table') for the production nucleon chain; "
                              "electron strands in atom_braid_word_3A"),
        "validation_worst_dev": validation,
        "pairs": results,
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
