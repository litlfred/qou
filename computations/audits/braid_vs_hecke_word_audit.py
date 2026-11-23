#!/usr/bin/env python3
"""
Which "braid word" claims about the ATOMIC object are wrong as mathematics.

Issue #6952 (this tranche); root finding in #6941 §10.

The atomic object the mass law traces is NOT a braid. `atom_braid_word_3A`
returns `(c, d, gen_idx)` triples and `d` takes FOUR values at the proton `q0`:

    d = 0                    ->  sigma          a positive crossing      BRAID
    d = -h  = -0.2090602988  ->  sigma_inv      a negative crossing      BRAID
    d = -h/2 = -0.1045301494 ->  averaged       (sigma + sigma^-1)/2     NOT
    d = -0.1044582478        ->  averaged_wt    colour-weighted          NOT

so the object lives in `H_n(q)` and not in the image of `B_n`. Measured across
protium -> iron-56: 0 of 14 atoms has a word free of the last two.

NONE OF THAT IS NEW, AND THIS AUDIT MUST NOT CLAIM IT IS. The producer's own
docstring has carried the correction since **2026-08-25 (PR #5765)**:

    NAME IS A MISNOMER - this does NOT return a braid word (2026-08-25, PR #5765).
    A rename was considered and rejected: 685 call sites across 382 files. So the
    name stays and this docstring carries the correction.
    Each triple (c, d, g) denotes the HECKE ELEMENT c*sigma_g + d*1, not a braid
    generator. The letters OUTSIDE the image of rho are exactly the AVERAGED ones

So the corpus already knows, the rename was already weighed with a count (685 /
382) close to this audit's independent 672, and it was already REJECTED. PR
#6359 acted on the same note, correcting "the closure" out of its PR body, its
probe and a Lean docstring. This audit's own arrival at "a rename is the wrong
instrument" is a re-derivation, not a finding, and is recorded as agreement.

WHAT IS ACTUALLY UNDRAINED, and is this audit's only real contribution: the
docstring fixed the PRODUCER. The CONTENT BLOCKS still assert the atomic object
lives in a braid group. Those are false as mathematics, not merely misnamed, and
nobody has drained them.

WHAT IT FLAGS. A line is a DEFECT when it asserts membership in a BRAID GROUP
(`\\in B_n`) for the atomic / canonical-atom object. That is wrong as
mathematics, not merely as naming: `B_n -> H_n(q)` is a proper inclusion and the
object is outside the image. A line is CORRECT when it asserts `\\in B_n` for a
named knot given by an explicit sigma-word, or when it distinguishes the two
(e.g. "a braid `beta in B_n` with Hecke representative `T_w in H_n(q)`").

The verified-correct sites are listed explicitly rather than inferred, so a
future reader can check the adjudication instead of trusting a regex.

SCOPE. Flagging a line as a defect is a claim about that line's mathematics, and
each flagged line was read. This audit does NOT claim the 672-file identifier
surface is fine — it claims a rename is the wrong first instrument, and that the
mathematically false statements are a much smaller, reviewable set.

-- Ref: [manuscript] docs/audits/2026-09-06-universal-triangulation-ep-route-assessment.md §10
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Sites asserting `\in B_...` that are CORRECT — each read and adjudicated.
# Keyed by (path suffix, why).
VERIFIED_CORRECT = {
    "knots-particles-confinement/binding-knots-visual-inventory.md":
        "trefoil sigma_0^3 in B_2 and Borromean (sigma_0 sigma_1^-1)^3 in B_3 — "
        "explicit sigma-words, genuinely braids",
    "knots-particles-confinement/binding-knots-visual-inventory-table1-data.md":
        "same, in table form",
    "mass-theory/binding-scale-catalan.md":
        "B_3 = sigma_0 sigma_1 sigma_2 sigma_0 sigma_1 sigma_2 in B_4 — explicit",
    "mass-theory/six-canonical-knot-operators.md":
        "beta_w in B_3 for w in S_3 — the six knot operators are genuine braids",
    "climax-volume-mass/q-momentum.md":
        "restricts to generators sigma^eps with eps = +-1 IN THE SAME SENTENCE, "
        "so it is explicitly about braid words",
    "mass-theory/markov-axiom-recursive-ascent.md":
        "distinguishes correctly: 'a braid beta in B_n with Hecke representative "
        "T_w in H_n(q)'",
    "appendix-knot-periodic-table/recursive-atom-knot-atlas.md":
        "distinguishes correctly: 'T_w in H_{n_0}(q_0), w in B_{n_0}'",
    "mass-theory/conj-canonical-knot-id-sdp.lean":
        "explicit braid words for NAMED links (Hopf sigma_3^2 in B_6, L6a4 in B_9)",
    "mass-theory/graded-hecke-energy-truncation-bound.md":
        "CORRECTED 2026-09-06 by this tranche. The premise now reads 'let "
        "B_K in B_n be a braid' and carries a scoping note saying the atomic "
        "Hecke word does NOT satisfy it and has no closure. Still matches the "
        "ATOMIC_SUBJECT regex because it keeps the symbol \\mathcal{B}_K -- "
        "that symbol collision is real and is PR #6821's to adjudicate, so it "
        "is deliberately NOT renamed here. Listed as correct on the strength of "
        "the scoping note, not the symbol.",
    "notation/notation-collisions.md":
        "the A vs B_K register entry: states B_K in H_{3A}(q) and quotes the "
        "superseded 'B_K in B_{3A+Z}' only as history (adjudicated 2026-11-21)",
    "notation/notation-collisions.ts":
        "relocated history note for the same register entry (2026-11-21)",
}

# Owned by sibling PR #6821 until it merged (2026-10-10, owner choice B1:
# B_K on 3A strands). No site is sibling-owned now; atomic-mass-gb-nf.md is
# scanned like any other block.
SIBLING_OWNED: dict[str, str] = {}

# The atomic object is named EITHER in words OR by its symbol. Keying on the
# word "atom" alone was a false-negative blind spot of this audit's first
# version: `graded-hecke-energy-truncation-bound.md` says "the closure of
# $\mathcal{B}_K \in B_n$" and never says "atom", so it was missed. The
# notation register gives `\mathcal{B}_K` and `\mathcal{A}` as the atomic
# braid's symbols (and #6821 records that BOTH are used for it), so they are
# atomic subjects in their own right.
ATOMIC_SUBJECT = re.compile(
    r"atom(ic)?[- ]braid|atomic braid|canonical atom|atom-braid|"
    r"atomic\s+\w*\s*braid|braid word.*atom|atom.*braid word|"
    r"\\mathcal\{B\}_K|\\mathcal\{A\}", re.I)
BRAID_GROUP = re.compile(r"\\in\s*B_")


def scan() -> tuple[list, list, list]:
    out = subprocess.run(
        ["grep", "-rn", "-E", r"\\in\s*B_", "--include=*.md", "--include=*.lean",
         "--include=*.ts", "folio/"],
        cwd=ROOT, capture_output=True, text=True)
    defects, correct, sibling = [], [], []
    for line in out.stdout.splitlines():
        try:
            path, lno, text = line.split(":", 2)
        except ValueError:
            continue
        if "/schema/" in path:
            continue
        hit_correct = next((k for k in VERIFIED_CORRECT if path.endswith(k)), None)
        hit_sibling = next((k for k in SIBLING_OWNED if path.endswith(k)), None)
        if hit_sibling:
            sibling.append((path, lno, text.strip()[:110], SIBLING_OWNED[hit_sibling]))
        elif hit_correct:
            correct.append((path, lno, VERIFIED_CORRECT[hit_correct]))
        elif ATOMIC_SUBJECT.search(text):
            defects.append((path, lno, text.strip()[:150]))
    return defects, correct, sibling


def main() -> int:
    defects, correct, sibling = scan()

    print("=== DEFECTS: the atomic object asserted to live in a BRAID GROUP ===")
    for p, l, t in defects:
        print(f"  {p}:{l}\n      {t}")
    print(f"\n  {len(defects)} defect line(s)")

    print("\n=== OWNED BY SIBLING PR #6821 — not touched here ===")
    for p, l, t, why in sibling:
        print(f"  {p}:{l}  ({why})")

    print(f"\n=== VERIFIED CORRECT (adjudicated, left alone): {len(correct)} line(s) ===")
    seen = set()
    for p, l, why in correct:
        if p not in seen:
            print(f"  {p}\n      {why}")
            seen.add(p)

    checks = [
        # A GATE, not a snapshot. This asserted `0 < len(defects) <= 12` while
        # the defects existed, which made it fail the moment they were drained —
        # a snapshot masquerading as a check. Clean is zero.
        ("no_atomic_object_asserted_in_a_braid_group", len(defects) == 0,
         f"{len(defects)} line(s) assert the atomic object lives in a braid "
         "group; clean is 0. Drained from 5 by this tranche"),
        ("correct_uses_exist_and_are_adjudicated", len(correct) > 0,
         f"{len(seen)} files assert `in B_n` correctly (explicit sigma-words, "
         "or correctly distinguishing braid from Hecke) and are left alone"),
        ("sibling_owned_sites_excluded", len(sibling) == len(SIBLING_OWNED),
         "every sibling-owned site is flagged, not touched (none since "
         "PR #6821 merged)"),
    ]
    print()
    ok = 0
    for name, cond, desc in checks:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}: {desc}")
        ok += 1 if cond else 0
    print(f"\n{ok}/{len(checks)} assertions")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
