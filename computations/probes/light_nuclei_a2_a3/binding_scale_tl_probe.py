#!/usr/bin/env python3
"""γγ binding past ⁴He on the ruled inputs, with the Temperley–Lieb sweep engine (bean qou-sv7h).

What this makes computable. The ruled γγ bond (photon vertex σ_iσ_{i+1}⁻¹, V³ on the bond
strand and the first two strands of the newer nucleon, right-hand closure), convention D
(z_D = q³/(q²+1)), the proton pin (50-digit q₀) and the log law B = E₀·ln(tr_free/tr_atom).
`hecke_flint` (permutation basis, n! terms) needed ~25 min on 4 cores for the nine ⁴He
all-pairs cells and cannot reach A = 5. `hecke_tl` computes the same trace through the TL
quotient (exact at z_D) in a re-laid-out sweep whose width is A + 2, not 3A.

Checks, all before any new number:
  C1  hecke_tl == hecke_flint exactly in ℚ at q = 3/2: ²H, every ³H / ³He order, chain and
      all-pairs routes in several placements, both transport variants.
  C2  the nine ⁴He all-pairs cells of he4-all-pairs-exact.witness.json reproduced at the pin
      to 1e-28 (certified balls).
  C3  the braid identity W = Π·M·Π⁻¹ behind atom_program, in the free group (Artin
      representation, faithful), A = 3 and 4, random block braids, both variants.

New rows (comparison with AME2020 is a comparison field only; nothing is chosen against it):
  nucleon order Z protons then N neutrons (the production order, as for ⁴He's p p n n; the
  owner ruled that order must be derived, 2026-11-21, and this probe does not derive it);
  routes "gg chain" (j−1, j) and "sequential capture" (each new nucleon J bonds to J−1, …, 0,
  which is the ⁴He "3He+n" route); variants over and under.

Arithmetic: python-flint arb balls at 768 bits (certified enclosures, the radius is printed);
exact fmpq for C1. No float anywhere. Long-compute discipline: run with
`python3 -u binding_scale_tl_probe.py 2>&1 | tee /tmp/binding_scale_tl.log`.
Usage: binding_scale_tl_probe.py [A_MAX] [--workers K]   (defaults 12, 2)
"""
from __future__ import annotations

import json
import multiprocessing as mp_pool
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "qou-substrate", "python"))
sys.path.insert(0, os.path.join(ROOT, "computations", "substrate"))

import flint  # noqa: E402
import mpmath as mp  # noqa: E402

import hecke_flint as F  # noqa: E402
import hecke_tl as T  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

PREC = 768
mp.mp.dps = 60
T0 = time.time()
E0_STR = "4.227483355629030550268056026587211153615"  # he4-gg-all-pairs.witness.json (scale only)
NUCLEI = [  # (name, Z, N), ground-state isotopes A = 2..12
    ("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("5He", 2, 3), ("6Li", 3, 3),
    ("7Li", 3, 4), ("8Be", 4, 4), ("9Be", 4, 5), ("10B", 5, 5), ("11B", 5, 6), ("12C", 6, 6),
]
HE4_ROUTES = {  # ../he4_all_pairs_formation (copied in he4_all_pairs_exact_probe.py)
    "gg chain": [(0, 1), (1, 2), (2, 3)],
    "D+D pairing a": [(0, 2), (1, 3), (0, 1), (2, 3), (1, 2), (0, 3)],
    "D+D pairing b": [(1, 2), (0, 3), (0, 1), (2, 3), (0, 2), (1, 3)],
    "3H+p": [(1, 2), (2, 3), (1, 3), (0, 1), (0, 2), (0, 3)],
    "3He+n": [(0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3)],
}


def log(m):
    print(f"[{time.time() - T0:8.1f}s] {m}", flush=True)


def chain(A):
    return [(j - 1, j) for j in range(1, A)]


def sequential(A):
    return [(i, j) for j in range(1, A) for i in range(j - 1, -1, -1)]


# ---- C3: the braid identity, in the free group ------------------------------------------------

def _fg_red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def _fg_inv(w):
    return tuple(-x for x in reversed(w))


def artin(n, letters):
    """Artin action of a braid word (list of (±1, i)) on the free group F_n, as generator images."""
    phi = {g: (g,) for g in range(1, n + 1)}
    for s, i in letters:
        a, b = i + 1, i + 2
        g = {a: (a, b, -a), b: (a,)} if s > 0 else {a: (b,), b: (-b, a, b)}
        new = {}
        for x in range(1, n + 1):
            r = []
            for y in g.get(x, (x,)):
                r.extend(phi[y] if y > 0 else _fg_inv(phi[-y]))
            new[x] = _fg_red(r)
        phi = new
    return phi


def artin_identity(A, bonds, variant, rng):
    """W (original layout, blocks = random B₃ words) == Π · atom_program body · Π⁻¹."""
    sg = {"S": 1, "I": -1}
    blocks = [[(rng.choice("SI"), rng.choice((0, 1))) for _ in range(4)] for _ in range(A)]
    order = "".join("x" for _ in range(A))
    W = []
    after = T._route(bonds)
    for k in range(A):
        W += [(sg[s], i + 3 * k) for s, i in blocks[k]]
        for i, j in after.get(k, []):
            W += [(sg[t], g) for t, g in F.bond(i, j, variant)]
    prog = T.atom_program(order, bonds, variant, fixed_width=True,
                          block_fn=lambda J, base: [(s, i + base) for s, i in blocks[J]])
    M = [(sg[k], i) for k, i in prog]
    # Π: slide every c to the left, over the a/b strands for "over", under for "under"
    lay = [(s, k) for k in range(A) for s in "abc"]
    Pi = []
    for J in range(A):
        p = lay.index(("c", J))
        while p > J:
            Pi.append((-1 if variant == "over" else 1, p - 1))
            lay[p], lay[p - 1] = lay[p - 1], lay[p]
            p -= 1
    Pinv = [(-s, i) for s, i in reversed(Pi)]
    n = 3 * A
    return artin(n, W) == artin(n, Pi + M + Pinv)


# ---- main ---------------------------------------------------------------------------------------

def _pin(prec=PREC):
    flint.ctx.prec = prec
    R = T.Ring(flint.arb(Q_50_DIGIT_STR), flint.arb)
    tb = {k: T.sweep_trace(T.word_program(3, F.atom_word(k, [], "over")), R)[0] for k in "pn"}
    return tb, R, flint.arb(E0_STR)


def _cell(tb, R, order, bonds, variant, progress=False):
    t = time.time()
    atom, st = T.sweep_trace(T.atom_program(order, bonds, variant), R,
                             log=log if progress else None, every=2000)
    free = flint.arb(1)
    for k in order:
        free *= tb[k]
    st["seconds"] = round(time.time() - t, 2)
    return atom / free, st


def _job(job):
    name, Z, N, route, v = job
    A = Z + N
    order = "p" * Z + "n" * N
    bonds = chain(A) if route == "gg chain" else sequential(A)
    # The sequential sweep cancels heavily: at 768 bits the ball loses ~220 decimal digits at
    # A = 8 and all of them by A = 9. Start where the measured loss says, and double until the
    # certified relative radius is below 1e-40. The radius is checked, never assumed.
    prec = PREC if route == "gg chain" or A <= 8 else (2048 if A <= 10 else 3072)
    while True:
        tb, R, E0 = _pin(prec)
        ratio, st = _cell(tb, R, order, bonds, "over" if v == "-" else v, progress=A >= 10)
        if ratio.mid() != 0 and ratio.rad() < abs(ratio.mid()) * flint.arb("1e-40"):
            break
        log(f"{name} {route} {v}: radius {ratio.rad().str(3)} at {prec} bits, doubling")
        prec *= 2
    Bd = E0 * 1000 * (1 - ratio)
    Bl = E0 * 1000 * (-ratio.log())
    return {"nucleus": name, "Z": Z, "N": N, "order": order, "route": route, "variant": v,
            "bonds": len(bonds), "ratio_atom_over_free": ratio.str(40, radius=False),
            "ratio_radius": ratio.rad().str(3), "B_diff_over_trfree_keV": Bd.str(20, radius=False),
            "B_log_keV": Bl.str(20, radius=False), "peak_width": st["peak_width"],
            "peak_terms": st["peak_terms"], "prec_bits": prec, "letters": st["steps"], "seconds": st["seconds"]}


def _write(checks, rows):
    names = [n for n, _, _ in NUCLEI]
    rows = sorted(rows, key=lambda r: (names.index(r["nucleus"]), r["route"] != "gg chain", r["variant"]))
    out = {"q0Anchor": "proton",
           "q0AnchorReason": "arb balls (768 bits, more where the sweep cancels; see prec_bits) around the 50-digit proton pin",
           "bean": "qou-sv7h",
           "rulings": ["γγ bond: photon vertex σ_iσ_{i+1}⁻¹, right-hand closure (owner-rulings 2026-11-22)",
                       "convention D: z = q³/(q²+1)",
                       "log law B = E₀·ln(tr_free/tr_atom) (owner-rulings 2026-11-25)"],
           "notChosen": ["nucleon order Z p then N n is the production order, not derived "
                         "(owner-rulings 2026-11-21)",
                         "routes and variants are all reported; none is selected"],
           "E0_MeV": E0_STR, "checks": checks, "rows": rows,
           "note": "PROBE, adopts nothing. AME values are comparison fields only. "
                   "B_diff_over_trfree = E0(1 - tr_atom/tr_free) is the retired linear form, kept "
                   "for comparison with he4-all-pairs-exact (which reports E0(tr_free - tr_atom))."}
    with open(os.path.join(HERE, "binding-scale-tl.witness.json"), "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)


def main():
    a_max = int(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else 12
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    checks = {}

    # C1
    q = flint.fmpq(3, 2)
    Rq = T.Ring(q, flint.fmpq)
    ok, n = True, 0
    cells = [("pn", [(0, 1)])]
    for order in ("pnn", "npn", "nnp", "ppn", "pnp", "npp"):
        cells += [(order, [(0, 1), (1, 2), (0, 2)]), (order, [(0, 2), (0, 1), (1, 2)]),
                  (order, [(1, 2), (0, 1), (0, 2)]), (order, [(0, 1), (1, 2)])]
    for order, b in cells:
        for v in ("over", "under"):
            ref = F.evalq(F.tr(3 * len(order), F.atom_word(order, b, v)), q)
            val, _ = T.sweep_trace(T.atom_program(order, b, v), Rq)
            ok &= val == ref
            n += 1
    checks["C1_tl_equals_flint_exact_q3/2"] = bool(ok)
    log(f"C1 {n} cells exact: {ok}")

    # C3
    rng = random.Random(20261127)
    ok, n = True, 0
    for A, routes in ((3, [[(0, 1), (1, 2), (0, 2)], [(0, 2), (0, 1), (1, 2)], [(1, 2), (0, 1)]]),
                      (4, list(HE4_ROUTES.values()))):
        for b in routes:
            for v in ("over", "under"):
                ok &= artin_identity(A, b, v, rng)
                n += 1
    checks["C3_braid_identity_artin"] = bool(ok)
    log(f"C3 {n} braid identities in the free group: {ok}")

    tb, R, E0 = _pin()
    # C2
    W = json.load(open(os.path.join(HERE, "he4-all-pairs-exact.witness.json")))
    ok = True
    for r in W["rows"]:
        v = "over" if r["variant"] == "-" else r["variant"]
        ratio, _ = _cell(tb, R, "ppnn", HE4_ROUTES[r["route"]], v)
        ok &= bool(abs(ratio - flint.arb(r["ratio_atom_over_free"])) < flint.arb("1e-28"))
    checks["C2_he4_all_pairs_witness_1e-28"] = bool(ok)
    log(f"C2 nine ⁴He cells reproduced: {ok}")
    assert all(checks.values()), checks

    from codata_constants import _ame_binding_mev  # comparison only
    jobs = []
    for name, Z, N in NUCLEI:
        A = Z + N
        if A > a_max:
            break
        # the chain has no transports, so "over" and "under" are the same word: computed once
        jobs.append((name, Z, N, "gg chain", "-"))
        for v in ("over", "under"):
            jobs.append((name, Z, N, "sequential capture", v))
    rows = []
    if "--only" in sys.argv:  # rerun named nuclei, keep the other rows of the existing witness
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
        jobs = [j for j in jobs if j[0] in only]
        prev = json.load(open(os.path.join(HERE, "binding-scale-tl.witness.json")))["rows"]
        rows = [r for r in prev if r["nucleus"] not in only]
    with mp_pool.Pool(workers) as pool:
        for row in pool.imap_unordered(_job, jobs):
            row["AME_keV_comparison_only"] = mp.nstr(_ame_binding_mev(row["Z"], row["Z"] + row["N"]) * 1000, 12)
            rows.append(row)
            log(f"{row['nucleus']:4s} {row['route']:18s} {row['variant']:5s} B_log={row['B_log_keV'][:16]:>17s} keV "
                f"(AME {row['AME_keV_comparison_only'][:9]}) width {row['peak_width']} terms {row['peak_terms']} "
                f"{row['seconds']}s")
            _write(checks, rows)
    log("done")


if __name__ == "__main__":
    main()
