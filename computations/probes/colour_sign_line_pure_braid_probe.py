#!/usr/bin/env python3
"""The two colour sign lines are isomorphic but NOT the same section.

`docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md` §7.4
left one question open, and
`docs/audits/2026-08-30-statement-b-brunnian-isotype-exclusion.md` then
made it the single surviving premise of the whole statement-B argument:

    are the Milnor sign line (Borromean side, mu-bar_123 under permutation
    of the three components) and the monodromy sign line (Bring side,
    Lambda^3 of the colour coordinates under the fibre monodromy) the SAME
    line, or two sections of isomorphic lines?

**They are isomorphic, and the identification is NOT canonical.** The
separating invariant is the kernel of `B_3 -> S_3` — the pure braid group
`P_3` — on which the sign character is constant and Milnor's invariant is
not.

The argument, in one line: the monodromy sign character **factors through
`S_3`**, while the baryon's own braid is **pure**, so the sign character
takes the same value on the Borromean rings as on the unlink — which
`mu-bar_123` separates. Two functions with different level sets are not
the same function, however isomorphic their targets.

FACTS ESTABLISHED HERE, all exact (permutations and free-group words; no
floating point anywhere, and no numerical anchor):

  F1. The corpus's stated Borromean braid word is wrong, by a count that
      needs no convention. `binding-knots-visual-inventory` gives
      `B_3 = sigma_0 sigma_1 sigma_2 sigma_0 sigma_1 sigma_2` in `B_4`.
      Its closure has **2 components**. The Borromean rings have 3. Two
      further entries in the same table miss their component count; only
      the figure-eight is right.

  F2. The standard representative `(sigma_1 sigma_2^-1)^3` lies in **B_3**
      — the same braid group as the colour fibre's monodromy — closes to
      3 components, and is a **pure** braid: its image in `S_3` is the
      identity.

  F3. `beta` is nontrivial *as a braid*, so `P_3` is not collapsed by the
      quotient. Checked through the **Artin representation**
      `B_3 -> Aut(F_3)`, which is faithful (Artin 1947): `beta` acts
      non-identically on the free group.

  F4. THE SEPARATION. `beta` and the trivial braid have the **same image
      in `S_3`** (both the identity), hence the same sign character. Their
      closures are the Borromean rings and the 3-component unlink, which
      `mu-bar_123` separates: `+/-1` against `0`. So `mu-bar` does not
      factor through `S_3`, and the sign character does not see the link.

The `mu-bar` values in F4 are **cited, not computed here** — the corpus's
own `borromean-quark` ("all three pairwise linking numbers vanish while
the triple Milnor invariant `mu-bar_123 = +/-1` encodes confinement") and
Mellor-Melvin (`library/0110001v3`) for total antisymmetry. What this
script contributes is the exact braid-theoretic half: that the two
configurations are genuinely indistinguishable to the sign character.

**Scope, per the (a)/(b) discipline.** F4 is a scope-**(b)** structural
exclusion: the named invariant is the kernel of `B_3 -> S_3`, and it
forbids *any* function that factors through `S_3` from separating two
pure-braid closures. It excludes the canonical identification, not the
isomorphism — the two lines remain isomorphic as `S_3`-representations,
which is what B-i and the Milnor route each need on their own side.

**What this does NOT do.** It does not refute statement B, and it does
not weaken the Brunnian isotype exclusion: that argument runs entirely on
the Milnor side and never needs the monodromy line. What it removes is
the hope that the two routes could be fused into one — and, with it, my
own earlier claim (dg07 §7.4) that the corpus carries "one route with two
derivations of its key step". That was too strong; see the CORRECTION
section of the audit.

Cross-references:
  - `docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md` §7.4
  - `docs/audits/2026-08-30-statement-b-brunnian-isotype-exclusion.md`
  - `computations/probes/bring_cubic_monodromy_probe.py`  (A6/A7: the sheets
    ARE the colour tubes; the monodromy is the full S_3)
  - `content/.../knots-particles-confinement/binding-knots-visual-inventory.md`
"""

from __future__ import annotations

import itertools
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# Path bridge (subdirectory refactor): keeps flat-namespace imports
# resolving from the `probes/` cluster. Must follow the sys.path
# bootstrap above, per _path_bridge's documented USAGE — importing it
# earlier fails without PYTHONPATH and is the defect class AGENTS.md
# records as masked by a PYTHONPATH-equipped runner.
import _path_bridge as _bridge  # noqa: E402, F401

WITNESS_OUT = HERE / "colour-sign-line-pure-braid-probe.witness.json"


# ── Braid words: permutation image and closure component count ────


def perm_image(word, n):
    """Image in S_n of a braid word, as a tuple. `word` is a list of
    generator indices (1-based, sign irrelevant to the permutation:
    sigma_i and sigma_i^-1 induce the same transposition)."""
    p = list(range(n))
    for i in word:
        k = abs(i)
        p[k - 1], p[k] = p[k], p[k - 1]
    return tuple(p)


def n_components(p):
    """Number of cycles of a permutation = number of components of the
    braid's Markov closure."""
    seen, count = set(), 0
    for i in range(len(p)):
        if i in seen:
            continue
        count += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = p[j]
    return count


def is_pure(p):
    return p == tuple(range(len(p)))


# ── Artin representation B_n -> Aut(F_n): exact, and faithful ─────
#
# Free-group words are tuples of nonzero ints: k = generator x_k,
# -k = its inverse. `reduce` cancels adjacent inverse pairs, which is a
# normal form for the free group, so equality of reduced words IS
# equality in F_n. Artin's theorem (1947) gives that this action is
# faithful, so a braid acting as the identity automorphism IS trivial.


def reduce_word(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def inv_word(w):
    return tuple(-g for g in reversed(w))


def artin_gen(i, n, inverse=False):
    """The automorphism of F_n induced by sigma_i (1-based), as a map
    generator-index -> reduced word.

      sigma_i   : x_i -> x_i x_{i+1} x_i^-1,      x_{i+1} -> x_i
      sigma_i^-1: x_i -> x_{i+1},                 x_{i+1} -> x_{i+1}^-1 x_i x_{i+1}
    """
    img = {k: (k,) for k in range(1, n + 1)}
    if not inverse:
        img[i] = reduce_word((i, i + 1, -i))
        img[i + 1] = (i,)
    else:
        img[i] = (i + 1,)
        img[i + 1] = reduce_word((-(i + 1), i, i + 1))
    return img


def apply_auto(img, w):
    """Apply an automorphism (given by generator images) to a word."""
    out = []
    for g in w:
        piece = img[abs(g)]
        out.extend(piece if g > 0 else inv_word(piece))
    return reduce_word(out)


def compose(first, second, n):
    """Automorphism applying `first` then `second`."""
    return {k: apply_auto(second, first[k]) for k in range(1, n + 1)}


def braid_automorphism(word, n):
    """Artin image of a signed braid word (entries +/- generator index)."""
    auto = {k: (k,) for k in range(1, n + 1)}
    for g in word:
        auto = compose(auto, artin_gen(abs(g), n, inverse=(g < 0)), n)
    return auto


def is_identity_auto(auto, n):
    return all(auto[k] == (k,) for k in range(1, n + 1))


# ── The four facts ────────────────────────────────────────────────

# `binding-knots-visual-inventory` is 0-indexed (sigma_0 is the first
# generator); these are its words shifted to the 1-based convention used
# above. Component counts are convention-independent either way.
INVENTORY = [
    ("gluon / Hopf link L2a1 = T(2,2)", "sigma_0 sigma_1 in B_3", [1, 2], 3, 2),
    ("electron / trefoil 3_1", "sigma_0 sigma_1 sigma_0 in B_3", [1, 2, 1], 3, 1),
    ("Higgs / figure-eight 4_1", "(sigma_0 sigma_1^-1)^2 in B_3", [1, -2, 1, -2], 3, 1),
    ("proton / Borromean B_3", "sigma_0 sigma_1 sigma_2 sigma_0 sigma_1 sigma_2 in B_4",
     [1, 2, 3, 1, 2, 3], 4, 3),
]

BORROMEAN = [1, -2] * 3          # (sigma_1 sigma_2^-1)^3 in B_3
TRIVIAL: list[int] = []          # the identity braid in B_3


def fact_1():
    rows = []
    for name, stated, word, n, need in INVENTORY:
        p = perm_image(word, n)
        got = n_components(p)
        rows.append({
            "block_entry": name, "stated_word": stated,
            "strands": n, "closure_components": got,
            "components_required": need, "matches": got == need,
        })
    return {
        "rows": rows,
        "n_mismatched": sum(1 for r in rows if not r["matches"]),
        "borromean_row_wrong": next(
            not r["matches"] for r in rows if "Borromean" in r["block_entry"]),
        "note": ("component count is a braid-word invariant needing no "
                 "convention beyond which generator swaps which strands; "
                 "both natural readings of the 0-indexing give these counts"),
    }


def fact_2():
    p = perm_image(BORROMEAN, 3)
    return {
        "word": "(sigma_1 sigma_2^-1)^3",
        "braid_group": "B_3",
        "permutation_image": list(p),
        "closure_components": n_components(p),
        "is_pure": is_pure(p),
        "same_braid_group_as_colour_monodromy": True,
        "note": ("B_3 is the braid group of the colour fibre's monodromy "
                 "(rem:holonomy-trefoil; bring_cubic_monodromy_probe A6/A7)"),
    }


def fact_3():
    auto = braid_automorphism(BORROMEAN, 3)
    return {
        "representation": "Artin B_3 -> Aut(F_3), faithful (Artin 1947)",
        "images": {f"x_{k}": list(auto[k]) for k in (1, 2, 3)},
        "acts_as_identity": is_identity_auto(auto, 3),
        "braid_is_nontrivial": not is_identity_auto(auto, 3),
    }


def fact_4():
    pb, pt = perm_image(BORROMEAN, 3), perm_image(TRIVIAL, 3)
    ab = braid_automorphism(BORROMEAN, 3)
    at = braid_automorphism(TRIVIAL, 3)
    same_s3 = pb == pt
    diff_braid = not all(ab[k] == at[k] for k in (1, 2, 3))
    return {
        "left": "closure of (sigma_1 sigma_2^-1)^3  =  Borromean rings",
        "right": "closure of the trivial braid      =  3-component unlink",
        "same_image_in_S3": same_s3,
        "shared_S3_image": list(pb),
        "sign_character_value_on_both": "+1  (sgn of the identity)",
        "distinct_as_braids": diff_braid,
        "mu_bar_123_left": "+/-1  (CITED: borromean-quark; Mellor-Melvin)",
        "mu_bar_123_right": "0     (CITED: the unlink carries no triple invariant)",
        "mu_bar_separates_them": True,
        "sign_character_separates_them": False,
        "conclusion": ("the sign character factors through S_3 and is "
                       "therefore constant on pure-braid closures; mu-bar "
                       "is not, so the two are different functions of the "
                       "configuration"),
    }


def fact_5_residual():
    """The scoping this argument must NOT skip — an arity check.

    The two "sections" do not start on a common domain. The monodromy
    sign character is a function of a LOOP in the base; mu-bar is a
    function of a LINK. They become comparable only by pulling both back
    along `loop -> braid traced by the three sheets -> its closure`, and
    F4 lives on that common domain, `B_3`.

    On `B_3` the conclusion is unconditional: sgn factors through `S_3`,
    mu-bar does not, and F4 exhibits the witnessing pair.

    What is NOT established is that this fibration's monodromy image
    CONTAINS such a pair. Each local monodromy is a half-twist (the
    branch points are simple, per bring_cubic_monodromy_probe A1/A3), so
    the image is generated by six conjugates of band generators; whether
    that subgroup meets `P_3` in two braids of different mu-bar is a
    further question this script does not answer.
    """
    return {
        "arity_check": (
            "the monodromy sign character is a function of a LOOP; mu-bar "
            "is a function of a LINK; F4 compares them only after pulling "
            "both back to B_3, which is a genuine common domain"),
        "unconditional_on_B3": True,
        "monodromy_image_contains_witnessing_pair": "NOT ESTABLISHED",
        "why_open": (
            "the six local monodromies are half-twists, but the existing "
            "probe records them as PERMUTATIONS only — their braid lifts "
            "are not computed, so the subgroup they generate is unknown"),
        "consequence_if_image_pure_part_is_trivial": (
            "the two sections would agree VACUOUSLY on the realised image "
            "without being the same function; that would not restore a "
            "canonical identification, but it would weaken the practical "
            "force of the separation"),
        "next_step": (
            "lift the six local monodromies from S_3 to B_3 (each a "
            "half-twist about a vanishing cycle) and compute the subgroup"),
    }


# ── Main ──────────────────────────────────────────────────────────


def main() -> int:
    f1, f2, f3, f4 = fact_1(), fact_2(), fact_3(), fact_4()
    f5 = fact_5_residual()

    print("F1  the inventory's braid words vs their named links")
    for r in f1["rows"]:
        mark = "ok " if r["matches"] else "*** MISMATCH"
        print(f"      {r['block_entry']:34s} closure {r['closure_components']} "
              f"/ needs {r['components_required']}   {mark}")
    print(f"      -> {f1['n_mismatched']} of {len(f1['rows'])} miss their "
          f"component count; the Borromean row is wrong: "
          f"{f1['borromean_row_wrong']}")

    print(f"\nF2  standard representative {f2['word']} in {f2['braid_group']}")
    print(f"      permutation {tuple(f2['permutation_image'])}, "
          f"{f2['closure_components']} components, PURE: {f2['is_pure']}")

    print("\nF3  Artin image (faithful), generator images:")
    for k, v in f3["images"].items():
        print(f"      {k} -> {tuple(v)}")
    print(f"      acts as identity: {f3['acts_as_identity']}  "
          f"=> braid nontrivial: {f3['braid_is_nontrivial']}")

    print("\nF4  THE SEPARATION")
    print(f"      {f4['left']}")
    print(f"      {f4['right']}")
    print(f"      same image in S_3            : {f4['same_image_in_S3']}  "
          f"{tuple(f4['shared_S3_image'])}")
    print(f"      distinct as braids            : {f4['distinct_as_braids']}")
    print(f"      sign character separates them : {f4['sign_character_separates_them']}")
    print(f"      mu-bar_123 separates them     : {f4['mu_bar_separates_them']}  "
          f"({f4['mu_bar_123_left']} vs {f4['mu_bar_123_right']})")

    print("\nF5  the arity check, and what stays open")
    print(f"      {f5['arity_check']}")
    print(f"      unconditional on B_3                 : {f5['unconditional_on_B3']}")
    print(f"      monodromy image contains such a pair : "
          f"{f5['monodromy_image_contains_witnessing_pair']}")

    established = bool(
        f2["is_pure"] and f3["braid_is_nontrivial"]
        and f4["same_image_in_S3"] and f4["distinct_as_braids"]
        and not f4["sign_character_separates_them"]
    )

    print("\nVERDICT")
    print(f"   the two sign lines are ISOMORPHIC but NOT the same section: "
          f"{established}")
    print("   separating invariant: the kernel of B_3 -> S_3 (the pure braid")
    print("   group P_3), on which sgn is constant and mu-bar is not.")
    print("   NOT refuted: statement B, nor the Brunnian isotype exclusion —")
    print("   that argument runs on the Milnor side and never needs this line.")
    print("   STILL OPEN (F5): whether THIS fibration's monodromy image")
    print("   realises the witnessing pair, or agrees with mu-bar vacuously.")

    out = {
        "schemaVersion": "1.0.0",
        "description": (
            "The Milnor sign line and the Bring-monodromy sign line are "
            "isomorphic as S_3-representations but are not the same section: "
            "the monodromy sign character factors through S_3 and is constant "
            "on pure-braid closures, while mu-bar_123 separates the Borromean "
            "rings from the unlink. Also records that the corpus's stated "
            "Borromean braid word closes to 2 components, not 3."
        ),
        "computation": {
            "script": "computations/probes/colour_sign_line_pure_braid_probe.py",
            "arithmetic": (
                "exact: permutations of finite sets and reduced free-group "
                "words (tuples of ints). No floating point, no numerical "
                "anchor, no q dependence."
            ),
        },
        "facts": {
            "F1_inventory_braid_words": f1,
            "F2_borromean_is_a_pure_B3_braid": f2,
            "F3_nontrivial_via_faithful_artin": f3,
            "F4_separation": f4,
            "F5_arity_check_and_residual": f5,
        },
        "summary": {
            "canonical_identification_excluded": established,
            "lines_remain_isomorphic": True,
            "separating_invariant": "ker(B_3 -> S_3) = P_3, the pure braid group",
            "scope": (
                "(b) structural exclusion of the CANONICAL identification, "
                "backed by a named invariant; not an exclusion of the "
                "isomorphism, which each route still has on its own side"
            ),
            "corrects": (
                "dg07 §7.4's 'the two routes are one route with two "
                "derivations of its key step' — too strong; same group and "
                "same three objects, but different sections"
            ),
            "residual": (
                "F5 — the separation is unconditional on B_3, but whether "
                "this fibration's monodromy image realises a witnessing "
                "pair is NOT established: the local monodromies are "
                "recorded as permutations, not braid lifts"),
            "does_not_touch": [
                "statement B (2026-08-30 Brunnian isotype exclusion) — runs "
                "entirely on the Milnor side",
                "B-i (Alt^3 is a non-trivial line) — a fact about the "
                "monodromy alone",
            ],
            "corpus_defect_flagged": (
                "binding-knots-visual-inventory states the Borromean braid "
                "word as sigma_0 sigma_1 sigma_2 sigma_0 sigma_1 sigma_2 in "
                "B_4, whose closure has 2 components; two further rows in the "
                "same table also miss their component count"
            ),
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote: {WITNESS_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
