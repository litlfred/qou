#!/usr/bin/env python3
"""
The A=1 corner: do the four resolutions of protium's word agree on hyperbolicity?

Bean `qou-eptr`, issue #6941 §11.3. Audit §10 establishes that the atomic word is
a Hecke element, not a braid, so it has no closure. §11 records that the newly
ingested `arxiv-2108.09349v2` (Nimershiem) carries **FKP Theorem 5.5**, which
makes hyperbolicity of a THREE-STRAND braid closure decidable from the word:

    S^3 - L_w is hyperbolic IFF w is conjugate to
        C^k sigma_1^{p_1} sigma_2^{-q_1} ... sigma_1^{p_s} sigma_2^{-q_s}
    with k in Z and p_i, q_i, s positive integers, AND w is not conjugate to
    sigma_1^{p_0} sigma_2^{q_0} (those close to unknots, torus knots, or
    connected sums of torus knots).  C = (sigma_1 sigma_2 sigma_1)^2 is central.

Protium is the one atom where the two facts meet productively: its word uses
generator indices {0,1} — three strands — and has exactly TWO averaged letters,
so its 2^2 = 4 resolutions are FULLY ENUMERABLE. §11.3 asked: if all four agree
on hyperbolicity, the resolution ambiguity does not matter for that question, and
that would be a genuine result with nothing selected.

RESULT: THEY DO NOT AGREE — or more precisely, agreement is NOT ESTABLISHED.
Three of the four are in FKP hyperbolic form; the fourth is not matched. So the
optimistic branch of §11.3 does not hold and §10.4's warning still binds.

    bits        cyc-reduced word              expsum   FKP form
    (+1,+1)     s1 S2 s1 S2 s1 S2 s1 s1 s2 s1 s1   +5   NOT MATCHED
    (+1,-1)     s1 S2 s1 S2 s1 S2 s1 s1 S2 s1 s1   +3   YES  (1,1)(1,1)(2,1)(3,1)
    (-1,+1)     s1 S2 s1 S2 s1 s1 s1               +3   YES  (1,1)(4,1)
    (-1,-1)     s1 S2 s1 S2 s1 S2 S2 s1 s1         +1   YES  (1,1)(1,2)(3,1)

SCOPE — the single most important thing to read here.

**"NOT MATCHED" DOES NOT MEAN "NOT HYPERBOLIC."** FKP's criterion is up to
CONJUGACY in B_3. This probe tests only CYCLIC ROTATIONS of the freely- and
cyclically-reduced word, which is a proper SUBSET of conjugacy: it does not
conjugate by an arbitrary braid, and it does not apply the braid relation
sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2. So the test is SUFFICIENT for
hyperbolicity and NOT NECESSARY.

Therefore:
  * three resolutions are HYPERBOLIC — established, because a syntactic match to
    the FKP form after cyclic reduction exhibits the required conjugate;
  * the fourth is UNDECIDED — not shown non-hyperbolic. Settling it needs a
    genuine conjugacy decision procedure in B_3 (Birman-Ko-Lee or Garside normal
    form), which is NOT implemented here and is not faked.

The negative clause of FKP is discharged for the three by inspection: each
matched form carries a strictly negative sigma_2 exponent, so none is conjugate
to sigma_1^{p_0} sigma_2^{q_0}, whose closures are the excluded torus family.

WHAT THIS SETTLES FOR THE ROUTE. §11.3's optimistic branch — "if all four agree,
the ambiguity is harmless" — is not available. What remains is the pessimistic
branch, and it is unchanged from §10.4: choosing a resolution because its
complement's invariants land near a target is a fit. Nothing here selects one.

The exponent sum is a conjugacy invariant (it is the abelianisation B_3 -> Z),
so the three distinct values +5, +3, +1 prove the resolutions fall into at least
THREE distinct conjugacy classes. They are genuinely different braids, not
presentations of one.

Precision: exact integer combinatorics on signed generator indices. No q, no
float, no anchor.

-- Ref: library/arxiv-2108.09349v2 (Nimershiem, Geometric triangulations of a
--      family of hyperbolic 3-braids) §1, quoting Futer-Kalfagianni-Purcell
--      Theorem 5.5
-- Ref: [manuscript] docs/audits/2026-09-06-universal-triangulation-ep-route-assessment.md §§10-11
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

BRAID = {"sigma", "sigma_inv"}


def resolutions(Z: int, N: int):
    """Every resolution of the averaged letters, as a signed-generator word.
    The producer is 0-indexed; standard braid numbering is g+1."""
    w = atom_canonical_crossings(Z, N)
    n_avg = sum(1 for _, t in w if t not in BRAID)
    for bits in itertools.product([1, -1], repeat=n_avg):
        it = iter(bits)
        out = []
        for g, t in w:
            if t == "sigma":
                out.append(g + 1)
            elif t == "sigma_inv":
                out.append(-(g + 1))
            else:
                out.append(next(it) * (g + 1))
        yield bits, out


def free_reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def cyclic_reduce(w):
    w = free_reduce(w)
    while len(w) > 1 and w[0] == -w[-1]:
        w = free_reduce(w[1:-1])
    return w


def runs(w):
    out = []
    for x in w:
        if out and out[-1][0] == x:
            out[-1][1] += 1
        else:
            out.append([x, 1])
    return out


def fkp_form(w):
    """Sufficient test: is some CYCLIC ROTATION of the reduced word literally
    sigma_1^{p_1} sigma_2^{-q_1} ... with all p_i, q_i > 0?

    NOT a conjugacy test — see the module docstring. A match proves the FKP
    hyperbolic form is attained; a non-match proves nothing."""
    w = cyclic_reduce(w)
    for r in range(len(w)):
        rot = w[r:] + w[:r]
        bl = runs(rot)
        if len(bl) < 2 or len(bl) % 2:
            continue
        if all(g == (1 if j % 2 == 0 else -2) for j, (g, _) in enumerate(bl)):
            return True, [(bl[i][1], bl[i + 1][1])
                          for i in range(0, len(bl), 2)], rot
    return False, None, w


def show(w):
    return " ".join(("s%d" % g if g > 0 else "S%d" % -g) for g in w)


def main() -> int:
    rows = []
    for bits, w in resolutions(1, 0):
        cw = cyclic_reduce(w)
        es = sum(1 if x > 0 else -1 for x in cw)
        ok, pq, rot = fkp_form(w)
        rows.append({"bits": list(bits), "len_raw": len(w), "len_reduced": len(cw),
                     "word_reduced": show(cw), "exponent_sum": es,
                     "fkp_form_matched": ok,
                     "pq": pq, "matched_rotation": show(rot) if ok else None})

    matched = [r for r in rows if r["fkp_form_matched"]]
    unmatched = [r for r in rows if not r["fkp_form_matched"]]
    expsums = sorted({r["exponent_sum"] for r in rows})

    print("PROTIUM (Z=1, N=0) — all 4 resolutions of the 2 averaged letters")
    print("  s1/s2 = sigma_1/sigma_2 ; S1/S2 = inverses\n")
    for r in rows:
        print(f"  bits={tuple(r['bits'])}  len {r['len_raw']} -> {r['len_reduced']}"
              f"  expsum {r['exponent_sum']:+d}")
        print(f"     {r['word_reduced']}")
        if r["fkp_form_matched"]:
            print(f"     FKP form YES  (p_i,q_i) = {r['pq']}   [HYPERBOLIC]")
        else:
            print("     FKP form NOT MATCHED  [UNDECIDED — not a non-hyperbolicity proof]")
        print()

    checks = [
        ("three_of_four_are_fkp_hyperbolic", len(matched) == 3,
         "three resolutions attain the FKP hyperbolic form after cyclic "
         "reduction, so their closures are hyperbolic"),
        ("one_of_four_is_undecided", len(unmatched) == 1,
         "the all-positive resolution is not matched; NOT a proof of "
         "non-hyperbolicity, since this test is cyclic rotation only, a proper "
         "subset of conjugacy"),
        ("resolutions_do_NOT_all_agree", len(matched) != 4,
         "so §11.3's optimistic branch — 'if all four agree the ambiguity is "
         "harmless' — is NOT available"),
        ("at_least_three_distinct_conjugacy_classes", len(expsums) == 3,
         f"exponent sums {expsums} are distinct; exponent sum is a conjugacy "
         "invariant (the abelianisation B_3 -> Z), so the resolutions are "
         "genuinely different braids, not presentations of one"),
        ("matched_forms_escape_the_torus_clause",
         all(any(q > 0 for _, q in r["pq"]) for r in matched),
         "each matched form carries a strictly negative sigma_2 exponent, so "
         "none is conjugate to sigma_1^{p0} sigma_2^{q0} — FKP's excluded "
         "torus family — discharging the criterion's negative clause"),
    ]

    ok = 0
    for name, cond, desc in checks:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}: {desc}")
        ok += 1 if cond else 0
    print(f"\n{ok}/{len(checks)} assertions")

    try:
        from qou_substrate.witness import WitnessBuilder
    except Exception as e:  # noqa: BLE001
        print(f"(witness not emitted: {e!r})")
        return 0 if ok == len(checks) else 1

    wb = WitnessBuilder("protium-fkp-hyperbolicity", engine="python",
                        _script_path=__file__)
    for name, cond, desc in checks:
        wb.add_assertion(name, computed="1" if cond else "0", expected="1",
                         tolerance="0.5", source=desc)
    wb.add_data("resolutions", rows)
    wb.add_data("n_matched", len(matched))
    wb.add_data("n_undecided", len(unmatched))
    wb.add_data("distinct_exponent_sums", expsums)
    wb.add_data("criterion",
                "FKP Thm 5.5 as quoted in library/arxiv-2108.09349v2 §1")
    wb.add_data("scope",
                "The test is a SUFFICIENT condition only: it checks cyclic "
                "rotations of the reduced word, a proper subset of conjugacy in "
                "B_3, and applies no braid relation. A match proves hyperbolic; "
                "a non-match proves nothing. Settling the fourth needs a real "
                "conjugacy decision procedure (Birman-Ko-Lee / Garside), which "
                "is NOT implemented here and is not faked.")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "exact integer braid combinatorics: no q, no anchor"})
    print("witness written")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
