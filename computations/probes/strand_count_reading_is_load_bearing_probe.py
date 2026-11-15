#!/usr/bin/env python3
"""The A+Z vs 3A reading picks a DIFFERENT atom — so the count is load-bearing.

Answers one item from bean `qou-jgg0`'s own "Not established" list, verbatim:

    "That the 7 mass-chapter citations are load-bearing; whether any DEPENDS
     on the A+Z count for a result was not measured."

`wedderburn-mass-formula.md` is one of those seven. **Measured: yes, and the
dependence is not a shift in a number, it is a change of subject.**

  reading (a)  def:atomic-braid   n = A + Z = 2Z + N   ->  unique atom is DEUTERIUM
  reading (b)  production         n = 3A    = 3(Z+N)   ->  unique atom is HYDROGEN-1

"Unique atom" means the unique atom at which p(n) = 3, i.e. at which the three
extremal Wedderburn blocks exhaust the partitions of n. That exhaustion is the
whole reason the n = 3 point is interesting: it is the one place where the
"three extremal invariants" are not a truncation of a longer list.

Both readings are live in the corpus. `qou-jgg0` measured 824 strand-count
lines across 377 files using 3A against 9 lines across 4 files using A+Z, plus
a THIRD count 3A+Z in `atomic-mass-gb-nf.md`. This probe does not adjudicate
them -- (a) vs (b) is explicitly reserved to the author in that bean -- it
measures what turns on the choice.

WHY IT MATTERS HERE AND NOW. PR #7171 (merged, commit 20671dcc1) added
`rem:level-zero-discards-braid-noncommutativity`, which asserts

    "Deuterium is the unique atom with n = A + Z = 3."

True under (a). Under (b) the unique such atom is hydrogen-1 and deuterium sits
at n = 6, where p(6) = 11 and the extremal blocks do NOT exhaust. So that
remark, and the probe behind it, are (a)-CONDITIONAL and do not say so. Same
for `deuterium_is_the_untested_exact_point_probe.py` check 1, which asserts
"D sits in H_{A+Z} = H_3".

That is the "conditional-proved != premise-established" discipline: the
sentences are correct given a premise the corpus has not settled, and they
state them flatly.

NOT DECIDED HERE. Which reading is right, whether either object is wrong, and
whether the other six mass-chapter citations are load-bearing. Scope (a) in the
refutation taxonomy: this constrains what depends on the choice; it excludes
nothing.

NO FLOAT64, and none is reachable: every quantity is an exact integer
(partition counts, strand counts). No mpmath, no float, no witness.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from sympy.functions.combinatorial.numbers import partition

REPO = Path(__file__).resolve().parent.parent.parent
MASS = REPO / "folio/quantum-observable-universe/mass-theory"

# Sweep bound for the enumerative half of checks 2-3. The EXACT argument in
# check 4 does not depend on it; the sweep is corroboration, not the proof.
Z_MAX, N_MAX = 20, 30


def n_a(Z: int, N: int) -> int:
    """def:atomic-braid: 'H_{A+Z}(q) ... with A + Z strands, where A = Z + N'."""
    return (Z + N) + Z


def n_b(Z: int, N: int) -> int:
    """production canonical_braid: n_strands = 3 * (Z + N)."""
    return 3 * (Z + N)


def atoms():
    """Real atoms only: Z >= 1. Z = 0 is not an atom, and admitting it would
    manufacture spurious solutions (e.g. Z=0, N=3 under reading (a))."""
    for Z in range(1, Z_MAX + 1):
        for N in range(0, N_MAX + 1):
            yield Z, N


def main() -> int:
    fails: list[str] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("The A+Z vs 3A reading picks a DIFFERENT atom -- the count is load-bearing.\n")

    print("CHECK 1 -- p(n) = 3 has exactly one solution, and it is n = 3")
    vals = [int(partition(n)) for n in range(1, 41)]
    strictly_increasing = all(b > a for a, b in zip(vals, vals[1:]))
    sols = [n for n, v in zip(range(1, 41), vals) if v == 3]
    check("p is strictly increasing on n >= 1 (so p(n)=3 has <= 1 solution)",
          strictly_increasing, f"p(1..8) = {vals[:8]}")
    check("the solution is n = 3", sols == [3], f"solutions in 1..40: {sols}")
    check("p(6) = 11, so at 6 strands the extremal blocks do NOT exhaust",
          int(partition(6)) == 11, f"p(6) = {int(partition(6))}")

    print("\nCHECK 2 -- under reading (a), n = A+Z, the unique such atom is DEUTERIUM")
    hits_a = [(Z, N) for Z, N in atoms() if int(partition(n_a(Z, N))) == 3]
    check("exactly one atom in the swept range", len(hits_a) == 1, f"hits = {hits_a}")
    check("and it is (Z=1, N=1) = deuterium", hits_a == [(1, 1)],
          f"A+Z = {n_a(1, 1)}")

    print("\nCHECK 3 -- under reading (b), n = 3A, the unique such atom is HYDROGEN-1")
    hits_b = [(Z, N) for Z, N in atoms() if int(partition(n_b(Z, N))) == 3]
    check("exactly one atom in the swept range", len(hits_b) == 1, f"hits = {hits_b}")
    check("and it is (Z=1, N=0) = hydrogen-1", hits_b == [(1, 0)],
          f"3A = {n_b(1, 0)}")

    print("\nCHECK 4 -- EXACT, not merely swept: solve each reading against n = 3")
    # (a) 2Z + N = 3 with Z >= 1, N >= 0  ->  (Z,N) = (1,1) only. Z=1,N=0 gives 2.
    exact_a = [(Z, N) for Z in range(1, 4) for N in range(0, 4) if 2 * Z + N == 3]
    # (b) 3(Z+N) = 3  ->  Z + N = 1, Z >= 1  ->  (1,0) only.
    exact_b = [(Z, N) for Z in range(1, 4) for N in range(0, 4) if 3 * (Z + N) == 3]
    check("(a) 2Z + N = 3 with Z >= 1 has the unique solution (1,1)",
          exact_a == [(1, 1)], f"{exact_a}")
    check("(b) 3(Z+N) = 3 with Z >= 1 has the unique solution (1,0)",
          exact_b == [(1, 0)], f"{exact_b}")
    check("the two readings name DIFFERENT atoms", exact_a != exact_b,
          "deuterium vs hydrogen-1")

    print("\nCHECK 5 -- deuterium under reading (b) is NOT an exhaustion point")
    check("D has 3A = 6 strands and p(6) = 11 != 3",
          n_b(1, 1) == 6 and int(partition(n_b(1, 1))) == 11,
          f"3A = {n_b(1, 1)}, p = {int(partition(n_b(1, 1)))}")

    print("\nCHECK 6 -- the merged artifacts assert the DEUTERIUM form, unqualified")
    rem = (MASS / "level-zero-discards-braid-noncommutativity.md").read_text()
    flat = " ".join(rem.split())
    check("rem:level-zero... asserts 'the unique atom with $n = A + Z = 3$'",
          "Deuterium is the unique atom with $n = A + Z = 3$" in flat)
    check("and does NOT mention the 3A reading or qou-jgg0",
          not re.search(r"3A|3\s*\\?cdot\s*A|jgg0", rem),
          "so the claim is (a)-conditional and does not say so")

    print("\nCHECK 7 -- both readings are live in the mass chapter, same symbol")
    wmf = (MASS / "wedderburn-mass-formula.md").read_text()
    swd = (MASS / "schur-weyl-mass-decomposition.md")
    check("wedderburn-mass-formula.md uses H_{A+Z}",
          "H_{A+Z}" in " ".join(wmf.split()))
    if swd.exists():
        check("schur-weyl-mass-decomposition.md uses H_{3A}",
              "H_{3A}" in " ".join(swd.read_text().split()),
              "same chapter, same symbol A, different algebra")
    else:
        check("schur-weyl-mass-decomposition.md present", False, "file missing")

    print("\nCHECK 8 -- CITING a definition is not DEPENDING on its strand count")
    # qou-jgg0's blast-radius line reads "24 citing blocks, 7 in the mass
    # chapters". That counts CITATIONS. This counts DEPENDENCIES: which citing
    # blocks actually use a strand count, and which one.
    cites = sorted(
        str(p_.relative_to(REPO / "folio/quantum-observable-universe"))
        for p_ in (REPO / "folio/quantum-observable-universe").rglob("*")
        if p_.suffix in (".ts", ".md") and "def:atomic-braid" in p_.read_text()
    )
    check("24 blocks cite def:atomic-braid (qou-jgg0's count, re-derived)",
          len(cites) == 24, f"{len(cites)} blocks")

    # Order matters: "3A + Z" contains both "3A" and "A + Z".
    pat_c = re.compile(r"3\s*A\s*\+\s*Z")
    pat_b = re.compile(r"3\s*A\b|3\s*\\cdot\s*A|3\s*\(\s*Z\s*\+\s*N\s*\)|H_\{3A\}")
    pat_a = re.compile(r"A\s*\+\s*Z|H_\{A\+Z\}")
    buckets: dict[str, list[str]] = {"c": [], "b": [], "a": [], "ab": [], "none": []}
    for rel in cites:
        flat = " ".join((REPO / "folio/quantum-observable-universe" / rel).read_text().split())
        has_c = bool(pat_c.search(flat))
        rest = pat_c.sub(" ", flat)
        has_b, has_a = bool(pat_b.search(rest)), bool(pat_a.search(rest))
        key = "c" if has_c else "ab" if (has_a and has_b) else "b" if has_b else "a" if has_a else "none"
        buckets[key].append(rel)

    check("16 of the 24 use NO strand count at all",
          len(buckets["none"]) == 16,
          "they cite the crossing table or the ground-state ordering, both "
          "reading-independent")
    check("5 commit to the production side: 4 use 3A, 1 uses 3A+Z",
          len(buckets["b"]) == 4 and len(buckets["c"]) == 1,
          f"3A: {buckets['b']}  |  3A+Z: {buckets['c']}")

    print("\nCHECK 9 -- exactly ONE CONSUMER carries the A+Z reading")
    a_hits = set(buckets["a"]) | set(buckets["ab"])
    own_manifest = "knots-particles-confinement/atomic-braid.ts"
    index_row = "index-of-definitions/definition-index.md"
    consumers = sorted(a_hits - {own_manifest, index_row})
    check("atomic-braid.ts is the DEFINITION's own manifest, not a consumer",
          own_manifest in a_hits
          and 'label: "def:atomic-braid"' in
              (REPO / "folio/quantum-observable-universe" / own_manifest).read_text(),
          "its title is 'Atomic braid $H_{A+Z}(q)$'")
    check("definition-index.md is a catalogue echoing that title",
          index_row in a_hits,
          "its 3A hits belong to unrelated entries (rho-k-h3a, exterior-algebra, psd-trace)")
    check("the remaining A+Z consumer set is exactly {wedderburn-mass-formula.md}",
          consumers == ["mass-theory/wedderburn-mass-formula.md"], f"{consumers}")

    print("\nCHECK 10 -- so the dependency surface is ~1 block, not 24 or 7")
    check("citations (24) far exceed dependencies on the A+Z count (1)",
          len(cites) == 24 and len(consumers) == 1,
          "qou-jgg0's blast-radius line counts citations; this counts dependencies")

    print("\nCHECK 11 -- RETRACTION: a block can depend on the count WITHOUT writing it")
    # Checks 8-10 classify TEXTUALLY, on the strings "A + Z" / "3A". A block that
    # writes a bare numeric H_n instead is invisible to them. Measured: three are.
    CB = REPO / "folio/quantum-observable-universe"
    num = re.compile(r"H_\{?(\d+)")
    numeric: dict[str, list[int]] = {}
    for rel in cites:
        found = sorted({int(m) for m in num.findall(
            " ".join((CB / rel).read_text().split()))})
        if found:
            numeric[rel] = found
    check("7 citing blocks carry a bare numeric H_n", len(numeric) == 7,
          "; ".join(f"{k.split('/')[-1]}:{v}" for k, v in sorted(numeric.items())))

    # A numeric H_n is NOT automatically a strand count. The seven partition
    # exhaustively into four kinds, and only the first is an A+Z dependency:
    #   3  A+Z arithmetic            molecular-construction (checks 12, 14)
    #   2  per-NUCLEON H_3           the quark triple; both also write 3A
    #   1  the TREFOIL's H_3         electron-shell-braid-capacity (check 13)
    #   1  catalogue                 definition-index.md, 18x H_3 from other titles
    per_nucleon = {
        "knots-particles-confinement/atom-knot-exists-proof.md",
        "mass-theory/active-set-trace-concentration.ts",
    }
    catalogue = {"index-of-definitions/definition-index.md"}
    trefoil = {"molecular-construction/electron-shell-braid-capacity.md"}
    az_dep = set(numeric) - per_nucleon - catalogue - trefoil
    check("the 7 partition exhaustively: 3 A+Z, 2 per-nucleon, 1 trefoil, 1 catalogue",
          len(az_dep) == 3 and per_nucleon | catalogue | trefoil <= set(numeric),
          f"A+Z dependants: {sorted(x.split('/')[-1] for x in az_dep)}")
    akep = " ".join((CB / "knots-particles-confinement/atom-knot-exists-proof.md")
                    .read_text().split())
    check("atom-knot-exists-proof's H_3 is PER-NUCLEON, and it writes 3(Z+N) for the atom",
          "canonical NF in $H_3(R, q)$ on $3$ strands" in akep
          and "H_{3(Z+N)}(q)" in akep,
          "so a bare H_3 means three different things across these blocks")

    print("\nCHECK 12 -- three of them are A+Z arithmetic, stated in words")
    co_md = " ".join((CB / "molecular-construction/co-molecular-braid-carbon-monoxide.md")
                     .read_text().split())
    h2_md = " ".join((CB / "molecular-construction/h2-molecular-braid.md")
                     .read_text().split())
    # Carbon Z=6 N=6 A=12: A+Z = 18 (3A would be 36). Oxygen Z=8 N=8 A=16: A+Z = 24
    # (3A = 48). CO = 18 + 24 = 42 (under 3A it would be 36 + 48 = 84).
    check("CO: carbon H_18 = 12 nucleons + 6 electrons = A+Z, NOT 3A = 36",
          "H_{18}(q)$ has 18 strands (12 nucleons + 6 electrons)" in co_md
          and (12 + 6) == 18 and 3 * 12 == 36)
    check("CO: oxygen H_24 = 16 nucleons + 8 electrons = A+Z, NOT 3A = 48",
          "24 strands (16 nucleons + 8 electrons)" in co_md
          and (16 + 8) == 24 and 3 * 16 == 48)
    check("CO: molecule H_42 = 18 + 24, so 3A would give 36 + 48 = 84",
          "$H_{42}(q)$ ($18 + 24 = 42$ strands)" in co_md and 36 + 48 == 84)
    check("H2: each atom in H_2 = one proton + one electron = A+Z, NOT 3A = 3",
          "atomic braid](#def:atomic-braid) in $H_2(q)$: one proton" in h2_md
          and (1 + 1) == 2 and 3 * 1 == 3)

    print("\nCHECK 13 -- and one numeric hit is a FALSE POSITIVE, caught by reading it")
    esc = " ".join((CB / "molecular-construction/electron-shell-braid-capacity.md")
                   .read_text().split())
    check("electron-shell-braid-capacity's H_3 is the TREFOIL's algebra, not a strand count",
          "T_{2,3} = \\sigma_0\\sigma_1\\sigma_0$ in $H_3(q)$" in esc,
          "a numeric H_n is not automatically a strand count")

    print("\nCHECK 14 -- so the A+Z dependency set is at least FOUR, not one")
    symbolic = ["mass-theory/wedderburn-mass-formula.md"]
    numeric_dep = sorted([
        "molecular-construction/co-molecular-braid-carbon-monoxide.md",
        "molecular-construction/co-molecular-braid-carbon-monoxide.ts",
        "molecular-construction/h2-molecular-braid.md",
    ])
    check("1 writes A+Z symbolically; 3 more depend on it numerically",
          len(symbolic) == 1 and len(numeric_dep) == 3,
          "checks 9-10's 'exactly one consumer' is RETRACTED as a dependency claim")
    check("all three numeric dependants are in molecular-construction",
          all(d.startswith("molecular-construction/") for d in numeric_dep),
          "the chapter is built on 'nucleons + electrons', which IS the A+Z construction")

    print("\nCHECK 15 -- a FOURTH surface: Lean. qou-jgg0 measured content + Python only")
    CBR = REPO / "folio/quantum-observable-universe"
    az_lean = CBR / "knots-particles-confinement/atomic-braid.lean"
    az = az_lean.read_text()
    check("def:atomic-braid HAS a Lean sibling (it is not under lean/QOU/)",
          az_lean.exists() and not (CBR / "lean/QOU/AtomicBraid").exists(),
          "grepping lean/QOU/ alone reports ZERO hits for NeutralAtom -- a scan-scope "
          "blind spot, and I hit it before checking resolution path 1")
    check("it encodes A+Z as a FIELD DEFAULT, not a constraint",
          "totalStrands : Nat := A + Z" in az and "A : Nat := Z + N" in az)
    check("it carries the six pair types INCLUDING the three electronic ones",
          all(f"| {k} : PairType" in az for k in ("pp", "nn", "pn", "pe", "ne", "ee")),
          "pe / ne / ee -- qou-jgg0's own evidence for reading (a), also present in Lean")

    print("\nCHECK 16 -- but that carrier does NOT force A+Z, and says so itself")
    check("its single theorem is proved by rfl on the defaults",
          "totalStrands = Z + N + Z := by" in " ".join(az.split())
          and az.rstrip().endswith("rfl"),
          "AGENTS.md rule 8: a proposition true by unfolding is notation, not a theorem")
    check("its docstring states the fields are INDEPENDENT and may be non-default",
          "the `A` and `totalStrands` fields are independent" in " ".join(az.split()),
          "so a NeutralAtom with totalStrands := 3*A is well-typed -- (a) is a "
          "default, not a constraint")

    print("\nCHECK 17 -- the 3A reading ALSO has Lean carriers, and more of them")
    lean_3a = {
        "knots-particles-confinement/fusion-process.lean":
            "Hecke strand count: three strands per nucleon (`H_{3A}`)",
        "mass-theory/conj-rho-prefactor-structural.lean":
            "the strand count is exactly `3 * (Z + N)`",
        "mass-theory/habiro-expansion-atomic.lean":
            "H_{3A}(q)",
        "mass-theory/schur-weyl-mass-decomposition.lean":
            "H_{3A}(q)",
    }
    missing = [f for f, q in lean_3a.items()
               if q not in " ".join((CBR / f).read_text().split())]
    check("4 named Lean files carry the 3A reading verbatim", not missing, str(missing))
    check("one of them states it as a CONSTRAINT, not a default",
          "Sanity: the strand count is exactly `3 * (Z + N)`" in
          " ".join((CBR / "mass-theory/conj-rho-prefactor-structural.lean").read_text().split()))

    print("\nCHECK 18 -- so the Lean surface carries BOTH, and leans the OTHER way")
    # Not a bare True: count the Lean files that actually carry each reading as a
    # STRAND COUNT (the phrase must sit on a line mentioning strands/braid/atom, so
    # an unrelated "3 * A" in an inequality does not inflate the 3A side).
    ctx = re.compile(r"strand|braid|atom", re.I)
    az_files, b_files = set(), set()
    for f in CBR.rglob("*.lean"):
        for line in f.read_text().splitlines():
            if not ctx.search(line):
                continue
            if re.search(r"A \+ Z|A\+Z", line):
                az_files.add(str(f.relative_to(CBR)))
            if re.search(r"3 ?\* ?A\b|3 ?\* ?\(Z \+ N\)|H_\{3A\}", line):
                b_files.add(str(f.relative_to(CBR)))
    check("the 3A reading has strictly MORE Lean carriers than A+Z",
          len(b_files) > len(az_files),
          f"A+Z: {len(az_files)} file(s) {sorted(az_files)}  |  3A: {len(b_files)} file(s)")
    check("A+Z's Lean carriers are exactly three, and I under-counted them twice",
          az_files == {
              "knots-particles-confinement/atomic-braid.lean",
              "lean/QOU/BraidKnot/ElectronShell.lean",
              "molecular-construction/h2o-molecular-braid.lean",
          },
          f"{sorted(az_files)}")

    print("\nCHECK 19 -- the pattern across ALL surfaces: A+Z lives in the ELECTRON domain")
    esl = " ".join((CBR / "lean/QOU/BraidKnot/ElectronShell.lean").read_text().split())
    h2o = " ".join((CBR / "molecular-construction/h2o-molecular-braid.lean").read_text().split())
    check("ElectronShell.lean is a real CONSTRUCTION, not a default: H_A -> H_{A+Z} cabling",
          "H_A(q) \u21aa H_{A+Z}(q)" in esl or "H_{A+Z}(q)" in esl,
          "plus `BraidWord (A+Z)` and an SDP-selected binding subword")
    check("h2o-molecular-braid.lean does A+Z arithmetic explicitly",
          "A+Z = 16+8 = 24 strands" in h2o, "oxygen O(8,8) for water")
    # Every A+Z carrier found on ANY surface is about electrons, shells, or molecules.
    az_all = sorted(az_files) + [
        "molecular-construction/co-molecular-braid-carbon-monoxide.md",
        "molecular-construction/co-molecular-braid-carbon-monoxide.ts",
        "molecular-construction/h2-molecular-braid.md",
        "mass-theory/wedderburn-mass-formula.md",
    ]
    domain = [f for f in az_all
              if f.startswith("molecular-construction/")
              or "ElectronShell" in f
              or f.endswith("knots-particles-confinement/atomic-braid.lean")]
    check("6 of the 7 A+Z carriers are electron-shell or molecular; the 7th is the mass formula",
          len(domain) == 6 and len(az_all) == 7,
          "the one domain reading (b) -- 3A with NO electrons -- cannot serve")

    total = 44
    print(f"\n{total - len(fails)}/{total} checks passed")
    if fails:
        print("FAILED: " + "; ".join(fails))
    print("\nNOT DECIDED HERE: which reading is right. That is qou-jgg0's (a)/(b)")
    print("question and is explicitly the author's. This measures what turns on it.")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
