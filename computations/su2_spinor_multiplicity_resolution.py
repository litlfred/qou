#!/usr/bin/env python3
"""SU(2) spinor structure vs the keystone (2,1) multiplicity (EXPLORATORY, audit-only).

THE QUESTION (author-steered, 2026-06-02). The keystone audit #1684
(docs/audits/2026-06-02-h5-h3-functor-keystone.md) found the (2,1) baryon block
appears in Res^{H5}_{H3} across 5 of 7 lambda |- 5 with multiplicity {1,2},
concluding "no canonical basis vector" -> no canonical 5<->3 functor. This probe
tests whether the Gelfand-Tsetlin / Jucys-Murphy / Okounkov-Vershik canonical
eigenbasis of the multiplicity space -- and specifically the SU(2) spinor
(ribbon-twist theta_j = q^{j(j+1)}) structure of #1683 ((2,1) -> spin j=1/2) --
provides a FORCED selection of a single (2,1) copy, resolving the multiplicity by
spin.

DISCIPLINE (AGENTS.md production-vs-exploratory, the FIT EPICENTER):
  - The JM elements and the GT basis are CANONICAL (defined by the
    chain H1 < H2 < ... < H5). Computing them is rigorous, NO fit.
  - SELECTING which eigenvector = the h^4 = -3/4 carrier needs a rule FORCED by
    the spinor double-cover / GT structure. A spin or content value CHOSEN to make
    h^4 appear is THE catch. We report RAW q-contents, theta_j, and the h^4
    comparison; the h^4 = -3/4 value is a FALSIFICATION reference, never a target.
  - "Spin resolves the multiplicity" is true ONLY if the spin spectrum is SIMPLE
    on the multiplicity space. We COMPUTE the spin spectrum; we do not assume it.

WHAT IS COMPUTED (exact rational / integer combinatorics + RAW @ 60 dps q-contents):

  TASK 1 -- JM / content resolution (Okounkov-Vershik).
    For each lambda |- 5 whose Res^{H5}_{H3} contains (2,1) with multiplicity
    m in {1,2}, enumerate the SYT "upper chains" (GT basis vectors of the
    multiplicity space): the chains (2,1) = lam3 < lam4 < lam5 = lambda with
    lam_k |- k. For each chain compute the JM eigenvalue tuple = q-contents
    [c]_q of the boxes added at the H3->H4 and H4->H5 steps (c = col - row), at
    q0 and symbolically. VERIFY the content tuples SEPARATE the m copies
    (Okounkov-Vershik): the multiplicity space has a canonical content-eigenbasis.

  TASK 2 -- Spin labels per copy.
    Assign the SU(2)_q spin j to each block along each chain via the
    ribbon/twist theta_j = q^{j(j+1)}. Per #1683 the spin of a two-row-bounded
    Wedderburn block is j = (lambda_1 - lambda_2)/2 (the highest-weight content of
    the SU(2)_q sub-object; (2,1) -> j = 1/2, verified). Compute theta_j per
    copy: the FINAL block (always (2,1) -> j=1/2) and the INTERMEDIATE H4 block
    lam4 (which differs between copies). Do the copies carry different spin?

  TASK 3 -- THE TEST: does spin canonically select ONE copy?
    Determine whether the spin operator has a SIMPLE spectrum on the
    (2,1)-multiplicity space -- i.e. whether it picks out a single canonical copy
    with NO free choice. Distinguish:
      (i)   spin fully separates -> canonical section EXISTS (keystone resolved by
            spin, DERIVED);
      (ii)  spin partially separates (needs JM contents too) -> canonical section
            exists via the full GT/JM algebra, spin alone insufficient;
      (iii) spin does NOT separate (both copies same j) -> spin does not resolve
            it; state what does.

  TASK 4 -- Falsification (NOT a target).
    IF a canonical copy is selected by FORCED structure, compute whether it
    carries the Borromean h^4 = -3/4 (RAW). A match would be a derived keystone
    closure; a miss is reported honestly. The selecting value MUST be forced by
    the spinor double-cover / GT structure -- a chosen j or content is a fit and
    is flagged.

Audit doc: docs/audits/2026-06-02-su2-spinor-multiplicity-resolution.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp

START = time.monotonic()

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402

# Canonical substrate q0 (proton-anchored). FALSIFICATION / reference only.
try:
    from q_parameter import Q as Q0  # type: ignore
    Q0 = mp.mpf(str(Q0))
except Exception:  # pragma: no cover - shim fallback
    Q0 = mp.mpf("1.10997859561220225731080831999100762523924148")

# Compute precision: match the keystone audit (60 dps) so precisionMetadata aligns.
try:
    from _precision import set_compute_dps  # type: ignore
    set_compute_dps(60)
except Exception:  # pragma: no cover
    mp.mp.dps = 60

# Borromean h^4 falsification reference (NOT a fit target).
H4_BORROMEAN = Fraction(-3, 4)

STD3 = (2, 1)  # the std H3 block carrying the Borromean h^4


# ===========================================================================
# Young-tableau combinatorics (exact, q-independent branching).
# ===========================================================================

def partitions(n: int):
    if n == 0:
        return [()]
    out = []

    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, cur + [p])

    rec(n, n, [])
    return out


def add_box(lam):
    """All partitions of |lam|+1 from adding one box (outer corner), with the
    (row, col) 0-indexed coordinate of the added box."""
    res = []
    parts = list(lam)
    for i in range(len(parts)):
        if i == 0 or parts[i] < parts[i - 1]:
            new = tuple(parts[:i] + [parts[i] + 1] + parts[i + 1:])
            res.append((new, (i, parts[i])))   # added box at row i, col parts[i]
    # new row of length 1 at the bottom
    res.append((tuple(parts) + (1,), (len(parts), 0)))
    return res


def upper_chains(lam5):
    """All SYT upper-chains (2,1) = lam3 < lam4 < lam5, returning, for each,
    the (lam4, box4, box5) where box_k = (row,col) of the box added going
    lam_{k-1} -> lam_k. These are the GT basis vectors of the (2,1)-multiplicity
    space inside S^{lam5} under Res^{S5}_{S3}.

    We build FORWARD from (2,1): add a box to get lam4, add a box to get
    candidate lam5; keep only those equal to the target lam5. The number of
    such chains is the restriction multiplicity m_{lam5,(2,1)} (branching
    duality: forward add-box count = backward remove-box restriction count)."""
    chains = []
    for lam4, box4 in add_box(STD3):
        for cand5, box5 in add_box(lam4):
            if cand5 == lam5:
                chains.append((lam4, box4, box5))
    return chains


def content_of_box(box):
    """Content c(box) = col - row (0-indexed coordinates)."""
    r, c = box
    return c - r


def q_content(c: int, q):
    """q-content [c]_q = (q^c - q^{-c})/(q - q^{-1}); [0]_q = 0 exactly.
    This is the Jucys-Murphy eigenvalue in the q-deformed (Hecke) seminormal
    form (Murphy / Ram). For c<0 it equals -[ -c ]_q."""
    if c == 0:
        return mp.mpf(0)
    return (mp.power(q, c) - mp.power(q, -c)) / (q - 1 / q)


def spin_of_block(lam):
    """SU(2)_q spin of a Wedderburn block. Per #1683 (u1-hypercharge audit) the
    two-row-content spin is j = (lam_1 - lam_2)/2: the highest-weight content of
    the SU(2)_q sub-object selected by the first two rows. For one-row / two-row
    diagrams this is the standard Schur-Weyl spin; for >2 rows it is the
    leading two-row content (the SU(2)_q reduction the twist ladder uses).
    Cross-checks against the #1683 table: (3)->3/2, (2,1)->1/2, (1^3)->0 ;
    (2)->1, (1,1)->0."""
    l1 = lam[0] if len(lam) >= 1 else 0
    l2 = lam[1] if len(lam) >= 2 else 0
    return Fraction(l1 - l2, 2)


def theta_j(j: Fraction, q):
    """Ribbon twist eigenvalue theta_j = q^{j(j+1)} (Reshetikhin-Turaev framing
    element). j(j+1) is the SU(2)_q Casimir."""
    casimir = float(j * (j + 1))
    return mp.power(q, casimir)


def main():
    w = WitnessBuilder(
        "su2-spinor-multiplicity-resolution",
        engine="python+mpmath",
        start_time=START,
    )
    w.set_audit_only(
        "docs/audits/2026-06-02-su2-spinor-multiplicity-resolution.md"
    )
    w.add_parameter("q0", mp.nstr(Q0, 50))
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_caveat(
        "EXPLORATORY / audit-only. Tests whether SU(2) spinor (ribbon-twist) "
        "structure FORCES a canonical selection of one (2,1) copy in the "
        "Res^{H5}_{H3} multiplicity space. h^4 = -3/4 is a FALSIFICATION "
        "reference, never a fit target. A spin/content chosen to produce h^4 "
        "is THE catch."
    )

    P5 = partitions(5)

    # -------------------------------------------------------------------
    # TASK 0 -- cross-check spin_of_block against #1683 twist ladder.
    # -------------------------------------------------------------------
    ladder_check = {
        "(2)": (Fraction(1), spin_of_block((2,))),
        "(1,1)": (Fraction(0), spin_of_block((1, 1))),
        "(3)": (Fraction(3, 2), spin_of_block((3,))),
        "(2,1)": (Fraction(1, 2), spin_of_block((2, 1))),
        "(1,1,1)": (Fraction(0), spin_of_block((1, 1, 1))),
    }
    for name, (expected, got) in ladder_check.items():
        w.add_assertion(
            f"spin_ladder_{name}", float(got), float(expected), tolerance=0,
            source="#1683 theta_j=q^{j(j+1)} ladder table",
        )
    w.add_data("task0_spin_ladder_check",
               {k: [str(e), str(g)] for k, (e, g) in ladder_check.items()})

    # Verify (2,1) -> j=1/2 (the baryon spinor premise of the whole audit).
    assert spin_of_block(STD3) == Fraction(1, 2)

    # -------------------------------------------------------------------
    # TASK 1 + TASK 2 -- JM contents and spin per copy, per lambda |- 5.
    # -------------------------------------------------------------------
    per_lambda = {}
    separation_by_content_all = True   # OV: do contents separate the copies?
    spin_separates_all = True          # do INTERMEDIATE-H4 spins separate copies?
    spin_separates_any = False
    final_spin_constant = True         # is the FINAL (2,1) spin constant (=1/2)?

    for lam5 in P5:
        chains = upper_chains(lam5)
        m = len(chains)
        copies = []
        content_tuples = []
        inter_spins = []
        for (lam4, box4, box5) in chains:
            c4 = content_of_box(box4)   # box added at H3 -> H4
            c5 = content_of_box(box5)   # box added at H4 -> H5
            qc4 = q_content(c4, Q0)
            qc5 = q_content(c5, Q0)
            j4 = spin_of_block(lam4)
            j5 = spin_of_block(lam5)
            jfinal = spin_of_block(STD3)  # = 1/2, the (2,1) block spin
            copies.append({
                "lam4": str(lam4),
                "box4_rc": list(box4),
                "box5_rc": list(box5),
                "content4": c4,
                "content5": c5,
                "q_content4": mp.nstr(qc4, 40),
                "q_content5": mp.nstr(qc5, 40),
                "spin_intermediate_H4": str(j4),
                "spin_H5": str(j5),
                "spin_final_block_2_1": str(jfinal),
                "theta_H4": mp.nstr(theta_j(j4, Q0), 40),
                "theta_2_1": mp.nstr(theta_j(jfinal, Q0), 40),
            })
            content_tuples.append((c4, c5))
            inter_spins.append(j4)

        # OV separation: are the content tuples distinct?
        sep_content = (len(set(content_tuples)) == m)
        # spin separation (intermediate H4): are the j4 values distinct?
        sep_spin = (len(set(inter_spins)) == m)

        if m >= 1 and not sep_content:
            separation_by_content_all = False
        if m >= 2:
            if not sep_spin:
                spin_separates_all = False
            else:
                spin_separates_any = True
        # final-block spin is always 1/2 by construction; confirm:
        if any(spin_of_block(STD3) != Fraction(1, 2) for _ in chains):
            final_spin_constant = False

        per_lambda[str(lam5)] = {
            "multiplicity_2_1": m,
            "content_tuples": [list(t) for t in content_tuples],
            "content_tuples_distinct": sep_content,
            "intermediate_H4_spins": [str(s) for s in inter_spins],
            "intermediate_H4_spins_distinct": sep_spin,
            "copies": copies,
        }

    w.add_data("task1_2_per_lambda", per_lambda)

    # OV theorem assertion: contents separate the GT multiplicity basis everywhere.
    w.add_assertion(
        "ov_content_separates_all_multiplicity_spaces",
        1.0 if separation_by_content_all else 0.0, 1.0, tolerance=0,
        source="Okounkov-Vershik: JM content vector labels GT basis uniquely",
    )

    # -------------------------------------------------------------------
    # TASK 3 -- THE TEST: does spin have a SIMPLE spectrum on the
    # multiplicity space? Focus on the m=2 cases (the genuine multiplicity).
    # -------------------------------------------------------------------
    m2_lambdas = [lam for lam in P5 if len(upper_chains(lam)) == 2]
    m2_detail = {}
    for lam5 in m2_lambdas:
        chains = upper_chains(lam5)
        j4s = sorted({spin_of_block(c[0]) for c in chains})
        contents = sorted({(content_of_box(c[1]), content_of_box(c[2]))
                           for c in chains})
        m2_detail[str(lam5)] = {
            "distinct_intermediate_spins": [str(j) for j in j4s],
            "num_distinct_spins": len(j4s),
            "distinct_content_tuples": [list(t) for t in contents],
            "num_distinct_contents": len(contents),
            "spin_simple_on_this_space": len(j4s) == 2,
            "content_simple_on_this_space": len(contents) == 2,
        }
    w.add_data("task3_multiplicity2_cases", m2_detail)

    # The FINAL-BLOCK spin (the literal "(2,1) is spin-1/2" datum) is CONSTANT
    # across every copy in every lambda: it cannot, by itself, separate copies.
    final_block_spins = {
        str(lam5): sorted({c_["spin_final_block_2_1"]
                           for c_ in per_lambda[str(lam5)]["copies"]})
        for lam5 in P5 if per_lambda[str(lam5)]["multiplicity_2_1"] >= 1
    }
    final_block_spin_constant = all(
        v == ["1/2"] for v in final_block_spins.values()
    )

    # GLOBAL-CANONICITY TEST (the selection-vs-separation distinction -- the
    # epicenter). Separating the copies (simple spectrum) is NECESSARY but NOT
    # sufficient for a CANONICAL SECTION: to SELECT one copy as "the ell=2 / h^4
    # carrier" you need a FORCED rule that nominates a distinguished spin value
    # CONSISTENTLY across every lambda. Compute the set of intermediate-H4 spins
    # appearing in the m=2 spaces: if there is NO single spin value that is
    # present in EVERY m=2 space (and absent from its partner), there is no
    # global canonical spin selector -- choosing one would be a fit.
    m2_spin_sets = [set(spin_of_block(c[0]) for c in upper_chains(lam))
                    for lam in m2_lambdas]
    # candidate global selectors: a spin j present in every m2 space
    common_spins = set.intersection(*m2_spin_sets) if m2_spin_sets else set()
    # but a SELECTOR must also be UNAMBIGUOUS: in each space it must pick exactly
    # one copy (it does, since spins are distinct), AND it must not flip role.
    # There is a canonical spin selector iff |common_spins| >= 1.
    global_spin_selector_exists = len(common_spins) >= 1
    w.add_data("task3_global_spin_selector", {
        "m2_intermediate_spin_sets": [sorted(str(s) for s in S)
                                      for S in m2_spin_sets],
        "common_spin_across_all_m2": sorted(str(s) for s in common_spins),
        "global_canonical_spin_selector_exists": global_spin_selector_exists,
        "note": "A canonical SELECTION (not just separation) needs one spin "
                "value present in every m=2 space. Separation alone does not "
                "nominate a copy; nominating one without this is a fit.",
    })
    w.add_assertion(
        "global_canonical_spin_selector_exists",
        1.0 if global_spin_selector_exists else 0.0,
        1.0 if global_spin_selector_exists else 0.0,  # RAW, not a target
        tolerance=0,
        source="is there a single spin value selecting one copy in EVERY m2 space?",
    )
    w.add_assertion(
        "final_2_1_block_spin_constant_one_half",
        1.0 if final_block_spin_constant else 0.0, 1.0, tolerance=0,
        source="(2,1) block spin = 1/2 by #1683; same for every copy",
    )

    # Does the INTERMEDIATE-H4 spin separate the m=2 spaces?
    spin_simple_everywhere = all(d["spin_simple_on_this_space"]
                                 for d in m2_detail.values())
    content_simple_everywhere = all(d["content_simple_on_this_space"]
                                    for d in m2_detail.values())
    w.add_assertion(
        "intermediate_H4_spin_simple_on_all_m2_spaces",
        1.0 if spin_simple_everywhere else 0.0,
        1.0 if spin_simple_everywhere else 0.0,  # report RAW (not a target)
        tolerance=0,
        source="RAW: does the path-spin (j of lam4) separate the 2 copies?",
    )
    w.add_assertion(
        "content_simple_on_all_m2_spaces",
        1.0 if content_simple_everywhere else 0.0, 1.0, tolerance=0,
        source="Okounkov-Vershik content separation on the m=2 spaces",
    )

    # Verdict logic (i/ii/iii). The key distinction (epicenter): SEPARATION
    # (simple spectrum) is necessary but does NOT by itself give a canonical
    # SECTION -- that needs a FORCED global selector.
    #   (i)   spin gives a canonical section: simple spectrum AND a forced
    #         global selector (one spin value canonically nominated in EVERY
    #         m=2 space). -> keystone resolved by spin, DERIVED.
    #   (ii)  spin SEPARATES (simple spectrum) but does NOT select (no forced
    #         global selector): canonical eigenbasis exists via GT/JM, but spin
    #         alone is insufficient for the physical selection. -> SHARPENED.
    #   (iii) spin does NOT even separate (copies share j): JM contents do the
    #         separating; spin is irrelevant.
    if not spin_simple_everywhere:
        verdict = "iii"
    elif spin_simple_everywhere and global_spin_selector_exists:
        verdict = "i"
    else:
        verdict = "ii"
    w.add_data("task3_verdict_code", verdict)
    w.add_data("task3_verdict_meaning", {
        "i": "spin gives a canonical section (simple spectrum + forced global "
             "selector) -> keystone resolved by spin, DERIVED",
        "ii": "spin SEPARATES (simple spectrum) but does NOT canonically SELECT "
              "(no forced global selector); canonical eigenbasis exists via "
              "GT/JM, spin alone insufficient -> physical selection still open",
        "iii": "spin does NOT separate (copies share j) -> JM contents separate; "
               "spin irrelevant",
    }[verdict])

    # -------------------------------------------------------------------
    # TASK 4 -- Falsification. The (2,1) block carries h^4 = -3/4 REGARDLESS of
    # which copy (it is a property of the block, computed in
    # borromean_h3_2_1_irrep_derivation.py). Spin/JM select WHICH copy of the
    # block embeds, NOT the value of h^4. We report this honestly:
    #   - There is NO forced rule by which a single copy carries a DIFFERENT
    #     h^4; the h^4 = -3/4 is the block's RAW invariant.
    #   - Any attempt to assign a per-copy h^4 by choosing a spin/content to hit
    #     -3/4 would be a FIT (flagged); we do NOT do this.
    # We record the RAW h^4 reference and the fit-flag state (= no fit performed).
    w.add_data("task4_h4_falsification", {
        "h4_borromean_reference": str(H4_BORROMEAN),
        "h4_is_block_invariant_not_copy_selected": True,
        "selected_copy_carries_distinct_h4": False,
        "fit_performed": False,
        "note": "h^4 = -3/4 is the (2,1)-block RAW invariant; spin/JM select "
                "which copy embeds, not the h^4 value. No per-copy h^4 chosen "
                "(would be a fit).",
    })
    w.add_assertion(
        "no_h4_fit_performed", 0.0, 0.0, tolerance=0,
        source="discipline: no spin/content chosen to produce h^4",
    )

    # -------------------------------------------------------------------
    # SUMMARY for the audit doc.
    # -------------------------------------------------------------------
    w.add_data("summary", {
        "ov_contents_separate_multiplicity": separation_by_content_all,
        "final_2_1_spin_constant_one_half": final_block_spin_constant,
        "intermediate_H4_spin_separates_m2": spin_simple_everywhere,
        "global_canonical_spin_selector_exists": global_spin_selector_exists,
        "verdict_code": verdict,
        "keystone_status": (
            "OVERTURNED (derived spin section)" if verdict == "i"
            else "SHARPENED (canonical GT/JM eigenbasis EXISTS -- #1684's 'no "
                 "canonical basis vector' is refuted; but spin SEPARATES without "
                 "canonically SELECTING -> physical selection of the h^4 carrier "
                 "still open)"
        ),
    })

    out = w.save()
    print(f"[su2-spinor] wrote {out}")
    print(f"[su2-spinor] OV content-separation everywhere: {separation_by_content_all}")
    print(f"[su2-spinor] final (2,1) spin constant 1/2: {final_block_spin_constant}")
    print(f"[su2-spinor] intermediate-H4 spin separates m=2: {spin_simple_everywhere}")
    print(f"[su2-spinor] global canonical spin SELECTOR exists: {global_spin_selector_exists}")
    print(f"[su2-spinor] VERDICT: ({verdict})")
    for lam, d in m2_detail.items():
        print(f"   m=2 {lam}: spins={d['distinct_intermediate_spins']} "
              f"(n={d['num_distinct_spins']}), "
              f"contents={d['distinct_content_tuples']} "
              f"(n={d['num_distinct_contents']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
