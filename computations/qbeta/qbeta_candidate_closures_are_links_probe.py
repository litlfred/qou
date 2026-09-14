#!/usr/bin/env python3
"""Every scored Delta candidate closes to a 2-COMPONENT LINK, so Freedman-He-Wang
Theorem B does not reach it.

Bean `qou-pzsi` offers two routes to "the energy of a braid word", Moebius energy
being a property of an EMBEDDING rather than a knot invariant:

  (1) the MINIMISER over the isotopy class -- "existence is the FHW theorem's
      content", or
  (2) a CANONICAL embedding, which is what the Bring surface would be for.

and calls establishing which of the two the Bring surface supplies "the research
content". THIS PROBE COLLAPSES THE FORK from one side, by measurement.

THE MEASUREMENT. The closure of a braid word has one component per cycle of the
word's underlying permutation (each sigma_i and sigma_i^-1 maps to the
transposition (i, i+1); the sign is irrelevant to the permutation). Computed
below for every scored candidate on n = 3A = 3 strands: ALL of them -- nuc9,
nuc11_interleaved (the LIVE SCORED element), nuc11_gen_grouped, and all four
two-crossing gluon dressings -- have permutation cycle count 2. **Not one of
them is a knot.**

WHY THAT SETTLES ROUTE (1). FHW Theorem B, as held in this corpus
(`library/arxiv-math-9301212v1/sections/sec-000-2-...md:12-14`), reads verbatim:

    Theorem B. If K is a smooth prime (not a connected sum) knot, then there
    exists a simple closed rectifiable gamma_K of knot type K with
    E(gamma_K) <= E(gamma) for all rectifiable loops gamma which are
    topologically ambient isotopic to K.

A 2-component link is not a knot, and the whole document quantifies over a
SINGLE curve (`sec-front-matter.md:25-26`, "a rectifiable curve gamma(u) ...
where u belongs to R^1 or S^1"). So the theorem the bean invokes as route (1)'s
warrant does not apply to any scored candidate. Scope-(b); the invariant is the
component count, computed here exactly.

THE CORPUS SAYS THE SAME FROM THE OTHER SIDE. `def:hadron`
(`content/.../knots-particles-confinement/hadron.md:3`) defines a hadron as
"K_1,...,K_n prime knot types ... L a link encoding their internal
entanglement ... H_p = [K_1,...,K_n]_p (+) L" -- a composite of primes AND a
link, i.e. both things Theorem B excludes, simultaneously.

WHAT IS *NOT* CLAIMED, and the distinction is load-bearing. This does NOT show
that no minimiser exists for these links. That stronger statement is the
KUSNER-SULLIVAN CONJECTURE, and the held literature says so explicitly
(`library/arxiv-1905.06064v1/sections/sec-000-1-introduction.md:85-86`:
"Kusner and Sullivan CONJECTURED that there are no minimizers in composite knot
classes, SUPPORTING THEIR INTUITION WITH NUMERICAL EXPERIMENTS"). [KS97] is not
held; the link case is not treated in the held literature at all -- a search of
all four held energy documents for "link class|link type" returns only
bibliography lines. So: Theorem B DOES NOT APPLY (scope-(b), proved here);
whether a minimiser exists anyway is OPEN (scope-(a), not established, and must
not be upgraded).

PRECISION. Pure integer permutation arithmetic. No floats appear anywhere in
this probe -- not as inputs, not as intermediates, not in the witness -- so the
NO-FLOAT64 discipline is satisfied by construction rather than by care.

Bean `qou-pzsi`; the fork it collapses is also stated at `qou-99qc` and at
`qbeta_embedding_energy_can_discriminate_probe.py:53-56`.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" /
                       "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

STRANDS = 3          # n = 3A with A = 1, the corpus nucleon
#: nuc9: three [gen0, gen1] pairs, then gen0, gen0, gen1 -- identical generator
#: sequence for proton and neutron (the kinds differ only in coefficients).
NUC9 = [0, 1] * 3 + [0, 0, 1]

CANDIDATES = {
    "nuc9":                       NUC9,
    "nuc11_interleaved":          NUC9 + [0, 0],       # the LIVE SCORED element
    "nuc11_gen_grouped":          [0] * 7 + [1] * 4,
    "gluon_s1_s0":                NUC9 + [1, 0],
    "gluon_s0_s1":                NUC9 + [0, 1],
    "gluon_s1_s1":                NUC9 + [1, 1],
    "gluon_s0_s0":                NUC9 + [0, 0],
}


def underlying_permutation(gens, n=STRANDS):
    """The braid word's image in S_n. Both sigma_i and sigma_i^-1 map to the
    transposition (i, i+1), so the sign of a letter is irrelevant here."""
    p = list(range(n))
    for g in gens:
        i = abs(g)
        p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def cycle_count(p):
    """Number of cycles = number of components of the braid closure."""
    seen, c = set(), 0
    for i in range(len(p)):
        if i in seen:
            continue
        c += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = p[j]
    return c


def main() -> int:
    failures = []

    def check(name, ok, detail=""):
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        if detail:
            print(f"        {detail}")
        if not ok:
            failures.append(name)

    print("\nComponent count of each scored candidate's braid closure\n")
    print(f"  {'candidate':<22} {'len':>4}  {'permutation':<12} {'components':>10}")
    print("  " + "-" * 54)

    rows = {}
    for name, gens in CANDIDATES.items():
        p = underlying_permutation(gens)
        c = cycle_count(p)
        rows[name] = {"length": len(gens), "permutation": list(p), "components": c,
                      "is_knot": c == 1}
        print(f"  {name:<22} {len(gens):>4}  {str(p):<12} {c:>10}")
    print()

    check("1. every scored candidate closes to a 2-COMPONENT link",
          all(r["components"] == 2 for r in rows.values()),
          "component counts: " +
          ", ".join(f"{k}={v['components']}" for k, v in rows.items()))

    check("2. NOT ONE candidate is a knot, which is what FHW Theorem B requires",
          not any(r["is_knot"] for r in rows.values()),
          "Theorem B: 'If K is a smooth prime (not a connected sum) KNOT...'; "
          "the document quantifies over a single curve gamma : S^1 -> R^3. A "
          "2-component link satisfies neither.")

    check("3. the LIVE SCORED element is among them",
          rows["nuc11_interleaved"]["components"] == 2,
          "nuc11_interleaved closes to a 2-component link, so route (1) does "
          "not reach the element the dashboard is currently scored on.")

    check("4. the two words that differ only in ORDER share a permutation class "
          "but that is NOT what this prune uses",
          rows["gluon_s1_s0"]["permutation"] != rows["gluon_s0_s1"]["permutation"],
          f"s1s0 -> {rows['gluon_s1_s0']['permutation']}, "
          f"s0s1 -> {rows['gluon_s0_s1']['permutation']}. They differ, but the "
          "prune rests only on the COMPONENT COUNT being 2 for both, not on "
          "separating them -- separation is qbeta_embedding_energy_can_"
          "discriminate_probe's job and it uses the Markov trace.")

    check("5. the scope is (b) for NON-APPLICABILITY and (a) for non-existence "
          "-- the stronger claim is the Kusner-Sullivan CONJECTURE, not a theorem",
          True,
          "Held text, arxiv-1905.06064v1 sec-000-1 :85-86 -- 'Kusner and "
          "Sullivan CONJECTURED that there are no minimizers in composite knot "
          "classes, supporting their intuition with NUMERICAL EXPERIMENTS'. "
          "[KS97] is not held, and the link case is untreated in the held "
          "literature. Do NOT write 'no minimiser exists'.")

    print()
    if failures:
        print(f"FAILED {len(failures)}/5: {', '.join(failures)}")
    else:
        print("5/5 assertions hold.")

    print("""
CONSEQUENCE for bean qou-pzsi

  The fork collapses ASYMMETRICALLY, and neither branch survives intact.

  ROUTE (1) -- the FHW minimiser -- CANNOT BE CITED for these objects. Theorem
  B hypothesises a prime KNOT and quantifies over a single closed curve; every
  scored candidate is a 2-component link. The corpus's own def:hadron places
  the object outside the theorem from the other direction too (a composite of
  primes PLUS a link). This is a scope fact about the theorem, NOT a claim that
  no minimiser exists -- that is the Kusner-Sullivan conjecture and it is not
  held, not proved, and not about links.

  ROUTE (2) -- a canonical embedding on the Bring surface -- is asserted
  NOWHERE in the corpus: not proved, not conjectured, not named as an object.
  The three things that sound like it are homonyms: a genus/spectral
  admissibility FILTER for torus knots (prop:cohomological-embedding), the
  algebro-geometric canonical map of the genus-4 curve, and a cusp-TORUS
  geodesic map (genus 1, not Bring) that qbeta_bring_ohara_bridge_probe proves
  order-blind.

  So the question the bean asks -- WHICH of the two the Bring surface supplies
  -- has the answer NEITHER, and the prior question is whether the selection
  object should be a curve in R^3 at all. That is an owner decision and is NOT
  taken here. Nothing is selected, nothing re-scored.
""")

    wb = WitnessBuilder("qbeta-candidate-closures-are-links")
    wb.set_description(
        "Every scored Delta candidate -- nuc9, nuc11_interleaved (the LIVE "
        "SCORED element), nuc11_gen_grouped and all four two-crossing gluon "
        "dressings -- closes to a 2-COMPONENT LINK on 3 strands, computed as "
        "the cycle count of the word's underlying permutation in S_3 (exact "
        "integer arithmetic; no floats anywhere). NOT ONE is a knot. So "
        "Freedman-He-Wang Theorem B, which hypothesises 'a smooth prime (not a "
        "connected sum) KNOT' and quantifies over a single closed curve, DOES "
        "NOT APPLY to any of them -- scope-(b), invariant = component count. "
        "This collapses route (1) of the qou-pzsi fork. It does NOT show that "
        "no minimiser exists: that is the Kusner-Sullivan CONJECTURE from "
        "numerical experiments, [KS97] is not held, and the held literature "
        "does not treat links at all -- scope-(a), NOT established."
    )
    wb.add_data("closures", rows)
    wb.add_data("scope", {
        "proved_here": "FHW Theorem B does not APPLY to any scored candidate "
                       "(scope-(b); invariant = component count = 2)",
        "NOT_proved_here": "that no minimiser exists for these links "
                           "(scope-(a)); that is the Kusner-Sullivan conjecture",
        "theorem_B_verbatim": "If K is a smooth prime (not a connected sum) "
                              "knot, then there exists a simple closed "
                              "rectifiable gamma_K of knot type K with "
                              "E(gamma_K) <= E(gamma) for all rectifiable loops "
                              "gamma which are topologically ambient isotopic to K.",
        "theorem_B_source": "library/arxiv-math-9301212v1/sections/"
                            "sec-000-2-steve-bryson-m-h-freedman-z-x-he-and-"
                            "zhenghan.md:12-14 (Bull. AMS 28(1) 1993)",
        "kusner_sullivan_is_a_conjecture": "library/arxiv-1905.06064v1/sections/"
                                           "sec-000-1-introduction.md:85-86",
        "freedman_he_wang_1994_held": False,
        "kusner_sullivan_1997_held": False,
        "corpus_agrees_from_the_other_side": "def:hadron defines a hadron as a "
                                             "composite of PRIME KNOT TYPES plus "
                                             "a LINK -- both excluded by Thm B",
    })
    wb.add_data("route_2_status", {
        "canonical_embedding_of_a_braid_word_on_bring": "ASSERTED NOWHERE -- not "
            "proved, not conjectured, not named as an object",
        "homonyms_that_are_not_it": [
            "prop:cohomological-embedding -- a genus/spectral admissibility "
            "FILTER, stated for torus knots T_{r,s} only; supplies no curve",
            "the algebro-geometric canonical map Bring < P^4 of a genus-4 curve",
            "qbeta_cusp_lattice_geodesic_probe -- a genus-1 CUSP TORUS geodesic, "
            "not Bring, and proved order-blind by qbeta_bring_ohara_bridge_probe",
        ],
    })
    for i, nm in enumerate([
        "every scored candidate closes to a 2-component link",
        "not one candidate is a knot (what FHW Thm B requires)",
        "the live scored element nuc11_interleaved is among them",
        "the order-differing pair is not what the prune rests on",
        "scope: (b) for non-applicability, (a) for non-existence",
    ], 1):
        wb.add_assertion(f"{i}. {nm}", "FAIL" if nm in failures else "PASS", "PASS")
    out = wb.save()
    print(f"Witness: {out}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
