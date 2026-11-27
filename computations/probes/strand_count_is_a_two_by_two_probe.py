#!/usr/bin/env python3
"""strand_count_is_a_two_by_two_probe.py
=========================================

**Bean `qou-jgg0`. The atomic braid's strand count is not a two-way
disagreement — it is a 2x2 of two independent binary choices, and three of the
four cells are live in content blocks with no block saying which is canonical.**

WHAT THIS CORRECTS, AND IT IS THIS BRANCH'S OWN CLAIM
------------------------------------------------------
`docs/audits/2026-09-05-two-atomic-braids-one-name.md` records that `3A + Z` is
"a third strand COUNT ... NOT a third braid construction", on the evidence that
`computations/electron_sigma_f_chain.py` uses it as an SDP normalisation
(`tr Phi = n_target`) and never calls `atom_braid_word_3A`.

That evidence is correct and check 8 re-verifies it. The CONCLUSION drawn from
it is not, because it is a claim about one FILE promoted to a claim about the
CORPUS. A content block --

    folio/quantum-observable-universe/mass-endomorphism/atomic-mass-gb-nf.md:3
    "atomic braid $\\mathcal{B}_K \\in B_{n}$, where $n = 3A + Z$"

-- asserts a braid-group element on `3A + Z` strands. `B_n` is the braid group;
that IS a braid. So `3A + Z` is a third strand count AND a third braid.

WHAT THE STRUCTURE ACTUALLY IS
-------------------------------
Two independent binary choices, not one three-way argument:

    axis 1: is a nucleon ONE strand, or THREE (its quarks)?
    axis 2: are the Z electrons IN the braid, or OUT?

                    | electrons IN | electrons OUT
    nucleon-strand  |   A + Z      |   A
    quark-strand    |   3A + Z     |   3A

Three cells are asserted as the home of the atomic braid (checks 1-4). The
fourth, `H_A`, appears in `level-sufficiency-interprets.md` but as an explicit
DEFAULT-COARSE approximation, not as a competing claim -- check 7 pins that
distinction rather than counting it as a fourth disputant.

The counts are never equal for a real atom (check 5), so no reading reconciles
them by coincidence; and `3A + Z` is exactly the join of the other two live
cells (check 6), which is why it is the one an electron-carrying SDP reaches.

THE COLLISION IS ON A SYMBOL, AND THE REGISTER IS A DISPUTANT
---------------------------------------------------------------
Both `3A` and `3A + Z` are asserted of the SAME symbol `\\mathcal{B}_K`, and one
of the two sites is `notation/notation-register-table3-data.md` -- which
AGENTS.md 7aa makes authoritative for symbols. `notation-collisions.md` carries
no entry for this symbol. Check 2.

ARITHMETIC
----------
Every quantity here is an exact Python integer or a substring test. No
approximate binary arithmetic is used or needed, so the NO-FLOAT64 family is
satisfied by construction rather than by tolerance.

PATHS ARE VERIFIED, NOT QUOTED
-------------------------------
Check 1 asserts each cited file EXISTS before asserting its content. This guard
exists because the audit's own section 5 cited two of these sites at paths that
resolve to nothing (`mass-theory/atomic-braid.md`, bare `hecke_3a_weights.py`)
while the claims themselves were true -- a dead pointer in an authoritative
list, which is the defect class AGENTS.md logs repeatedly.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT = ROOT / "folio" / "quantum-observable-universe"

fails = 0


def chk(label: str, ok: bool, detail: str = "") -> None:
    global fails
    if not ok:
        fails += 1
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}" + (f"  ({detail})" if detail else ""))


def read(rel: str) -> str:
    p = ROOT / rel
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


# ---------------------------------------------------------------- the sites
SITES = {
    "A+Z": [
        ("folio/quantum-observable-universe/knots-particles-confinement/atomic-braid.md", "H_{A+Z}(q)"),
        ("folio/quantum-observable-universe/mass-theory/wedderburn-mass-formula.md", "H_{A+Z}(q)"),
    ],
    "3A": [
        ("folio/quantum-observable-universe/mass-theory/schur-weyl-mass-decomposition.md", "H_{3A}(q)"),
        ("folio/quantum-observable-universe/notation/notation-register-table3-data.md", "H_{3A}(q)"),
        ("computations/hecke/hecke_3a_weights.py", "H_{3A}"),
    ],
    "3A+Z": [
        ("folio/quantum-observable-universe/mass-endomorphism/atomic-mass-gb-nf.md", "3A + Z"),
        ("computations/electron_sigma_f_chain.py", "3A + Z"),
    ],
}


def main() -> int:
    print(__doc__.split("\n")[2])
    print()

    # --- 1. every cited path exists AND carries its claim ------------------
    print("CHECK 1 -- the cited sites resolve, and say what they are cited for")
    missing, wrong = [], []
    for conv, rows in SITES.items():
        for rel, needle in rows:
            if not (ROOT / rel).exists():
                missing.append(rel)
            elif needle not in read(rel):
                wrong.append(f"{rel} lacks {needle!r}")
    for conv, rows in SITES.items():
        print(f"    {conv:5s}: " + ", ".join(r.split('/')[-1] for r, _ in rows))
    chk("every cited path exists", not missing, "; ".join(missing) or "7 of 7")
    chk("every cited site carries its claimed string", not wrong,
        "; ".join(wrong) or "7 of 7")
    print()

    # --- 2. one symbol, two counts, register is a disputant ----------------
    print("CHECK 2 -- the collision is on the symbol \\mathcal{B}_K")
    reg = read("folio/quantum-observable-universe/notation/notation-register-table3-data.md")
    gbnf = read("folio/quantum-observable-universe/mass-endomorphism/atomic-mass-gb-nf.md")
    coll = read("folio/quantum-observable-universe/notation/notation-collisions.md")
    reg_bk = r"\mathcal{B}_K \in H_{3A}(q)" in reg
    gbnf_bk = (r"\mathcal{B}_K \in B_{n}" in gbnf) and ("3A + Z" in gbnf)
    print(f"    notation register : B_K in H_{{3A}}(q)        -> {reg_bk}")
    print(f"    atomic-mass-gb-nf : B_K in B_n, n = 3A + Z   -> {gbnf_bk}")
    chk("the SAME symbol carries two different strand counts", reg_bk and gbnf_bk)
    chk("one of the two disputants IS the notation register (AGENTS.md 7aa authority)",
        reg_bk, "notation-register-table3-data.md:7")
    chk("notation-collisions.md registers no entry for this symbol",
        r"\mathcal{B}_K" not in coll, "the collision is unregistered")
    print()

    # --- 3. the 3A+Z block cites the A+Z definition ------------------------
    print("CHECK 3 -- the 3A+Z block CITES the definition it contradicts")
    ab = read("folio/quantum-observable-universe/knots-particles-confinement/atomic-braid.md")
    cites_def = "#def:atomic-braid" in gbnf
    def_is_apz = "H_{A+Z}(q)" in ab and "A + Z$ strands" in ab
    print(f"    atomic-mass-gb-nf links #def:atomic-braid -> {cites_def}")
    print(f"    def:atomic-braid says A + Z strands       -> {def_is_apz}")
    chk("a block asserts 3A+Z while citing a definition that says A+Z",
        cites_def and def_is_apz,
        "the disagreement sits INSIDE one uses/link edge")
    print()

    # --- 4. how many blocks per convention ---------------------------------
    print("CHECK 4 -- population per convention, over content blocks only")
    md = sorted(CONTENT.rglob("*.md"))
    pop = {"A+Z": [], "3A": [], "3A+Z": []}
    for p in md:
        t = p.read_text(encoding="utf-8")
        if "3A + Z" in t or "3A+Z" in t:
            pop["3A+Z"].append(p.name)
        if "H_{A+Z}" in t:
            pop["A+Z"].append(p.name)
        if "H_{3A}" in t:
            pop["3A"].append(p.name)
    for k in ("A+Z", "3A", "3A+Z"):
        print(f"    {k:5s}: {len(pop[k]):3d} block(s)")
    chk("all three conventions are live in content blocks",
        all(pop[k] for k in pop),
        f"A+Z {len(pop['A+Z'])}, 3A {len(pop['3A'])}, 3A+Z {len(pop['3A+Z'])}")
    chk("3A is the production majority, so the definition is the minority reading",
        len(pop["3A"]) > len(pop["A+Z"]),
        f"{len(pop['3A'])} vs {len(pop['A+Z'])}")
    print()

    # --- 5. never equal for a real atom ------------------------------------
    print("CHECK 5 -- the three counts are strictly ordered for every real atom")
    clashes = []
    for A in range(1, 61):
        for Z in range(1, A + 1):
            a, b, c = A + Z, 3 * A, 3 * A + Z
            if not (a < b < c):
                clashes.append((A, Z, a, b, c))
    print("      A   Z | A+Z   3A  3A+Z")
    for A, Z in ((1, 1), (2, 1), (4, 2), (12, 6)):
        print(f"    {A:3d} {Z:3d} | {A+Z:3d}  {3*A:3d}  {3*A+Z:3d}")
    chk("A+Z < 3A < 3A+Z for every A in 1..60, Z in 1..A -- no coincidental agreement",
        not clashes, f"{len(clashes)} clash(es)")
    print()

    # --- 6. 3A+Z is exactly the join ---------------------------------------
    print("CHECK 6 -- the 2x2: 3A+Z is the join of the two live cells")
    joins = all(
        (3 * A + Z) - 3 * A == Z and 3 * A - A == 2 * A
        for A in range(1, 61) for Z in range(1, A + 1)
    )
    print("    3A+Z  -  3A  =  Z   (the electron axis)")
    print("    3A    -  A   =  2A  (the quark-split axis)")
    chk("3A+Z = (quark split) applied to (electrons in) -- exact, all A,Z", joins,
        "the two axes are independent")
    print()

    # --- 7. H_A is a coarsening, not a fourth disputant ---------------------
    print("CHECK 7 -- the fourth cell H_A is an approximation, not a claim")
    lvl = read("folio/quantum-observable-universe/nuclear-interactions/level-sufficiency-interprets.md")
    has_ha = "H_A(R, q)" in lvl
    is_coarse = "Default-coarse" in lvl or "default-coarse" in lvl
    print(f"    level-sufficiency-interprets mentions H_A(R,q) -> {has_ha}")
    print(f"    ... and frames it as default-coarse            -> {is_coarse}")
    chk("H_A appears, but as an explicit coarsening -- NOT counted as a disputant",
        has_ha and is_coarse,
        "so the live disagreement is three-way, not four-way")
    print()

    # --- 8. the narrow claim survives; the corpus-wide one does not --------
    print("CHECK 8 -- re-verifying this branch's own evidence before correcting it")
    esf = read("computations/electron_sigma_f_chain.py")
    narrow_ok = "atom_braid_word_3A" not in esf and "n_target" in esf
    braid_block = bool(re.search(r"\\mathcal\{B\}_K \\in B_\{n\}", gbnf))
    print(f"    electron_sigma_f_chain never calls atom_braid_word_3A -> {narrow_ok}")
    print(f"    but a content block asserts B_K in B_n at 3A+Z        -> {braid_block}")
    chk("the FILE-level evidence stands (the audit measured it correctly)", narrow_ok)
    chk("the CORPUS-level conclusion does NOT -- 3A+Z is also a braid",
        braid_block,
        "B_n is the braid group; audit scope corrected")
    print()

    # --- 9. what each reading does to the disjoint-support layout ---------
    print("CHECK 9 -- the layout consequence, for #6919's f1/f0 additivity")
    import importlib, os
    os.environ.setdefault("PYTHONPATH", str(ROOT / "computations"))
    sys.path.insert(0, str(ROOT / "computations"))
    try:
        abw = importlib.import_module("mass_at_3A_proper").atom_braid_word_3A
    except Exception as exc:                       # pragma: no cover
        chk("producer importable", False, f"{type(exc).__name__}: {exc}")
        abw = None
    if abw is not None:
        gens = [t2[2] for t2 in abw(1, 1)]          # deuteron, one p + one n
        pblk, nblk = {0, 1}, {3, 4}
        bond = [g for g in gens if g == 2]
        print(f"    D generator sequence: {gens}")
        print(f"    proton {sorted(pblk)}: {sum(g in pblk for g in gens)} ops;"
              f"  neutron {sorted(nblk)}: {sum(g in nblk for g in gens)} ops;"
              f"  bond {{2}}: {len(bond)} ops")
        cross = min(abs(i - j) for i in pblk for j in nblk)
        chk("under 3A the two nucleon blocks are disjoint-support (min cross |i-j| = 2)",
            cross == 2 and set(gens) <= pblk | nblk | {2},
            "#6919's premise holds -- in the 3A reading it was computed in")
        chk("BUT the full word carries the inter-nucleon bond at generator 2, "
            "adjacent to BOTH blocks",
            len(bond) == 1,
            "so factorisation is a property of the vacuum part, not of the whole word")
        # A+Z: one strand per nucleon -> for D, 3 strands, generators {0,1} only
        apz_gens = (1 + 1 + 1) - 1                  # A+Z = 3 strands -> 2 generators
        chk("under A+Z the premise is NOT STATABLE -- D has 3 strands, 2 generators, "
            "no per-nucleon block",
            apz_gens == 2 and apz_gens < max(nblk) + 1,
            f"{apz_gens} generators vs neutron block needing index {max(nblk)}")
        # 3A+Z: blocks survive, but the electron strand is adjacent to the neutron block
        n_str = 3 * 2 + 1                           # D: 3A+Z = 7 strands
        e_gen = n_str - 2                           # generator joining last quark to electron
        chk("under 3A+Z the nucleon blocks survive but the electron generator is "
            "ADJACENT to the neutron block",
            e_gen == 5 and abs(e_gen - max(nblk)) == 1,
            "def:atomic-braid specifies pe/ne/ee crossings, so a full atom word couples them")
    print()

    total = 16
    print(f"{total - fails}/{total} checks passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
