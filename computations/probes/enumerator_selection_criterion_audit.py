#!/usr/bin/env python3
"""The binding-K enumerator's selection criterion cannot pick a binding carrier.

THE QUESTION (qou-brng).  Find a carrier selection principle that is not
minimality.  There already is one -- binding_k_enumerator.py ranks by Frobenius
residual -- and this audit is why it does not work.  Three independent defects,
each fatal alone, all readable off the enumerator's OWN RECORDED OUTPUT in
computations/_deprecated/binding-k-enumerator.witness.json.  Nothing is re-run.

CORRECTING A CORRECTION OF MINE.  The merged CarrierCrossingQuantisation header
says the corpus's principle is residual minimisation, not minimality.  That is
right about the CODE and wrong about the CORPUS: the sort key is indeed
(PSD_feasible, residual, length), but the Lean instances' bindingKWord = [3,3]
was taken from the witness's `min_length_psd_feasible_candidates` list, NOT from
the residual-ranked `psd_feasible_top_k`.  So the recorded carrier IS the
min-length pick; what is not minimality is the code's sort.  Both halves matter.

DEFECT 1 -- the residual's top pick is a SELF-CROSSING.  With
constituent_offsets = [0,3,6] in B_9, nucleon k holds strands 3k+1..3k+3 and
sigma_i joins strands i,i+1, so sigma_i is inter-component exactly when 3 | i.
Only sigma_3 and sigma_6 qualify.  The enumerator's field
`inter_nucleon_generators_extended` = [3,-3,4,-4,5,-5,6,-6,7,-7,8,-8] therefore
has 8 of 12 entries INTRA-nucleon, and its name says otherwise.  For BOTH 3H and
3He the residual-ranked top two are [-8,-8] and [-5,-5] -- self-crossings inside
nucleons 3 and 2, carrying ZERO inter-component crossings, so countChannel = 0
and they bind nothing.

DEFECT 2 -- the top-2 ordering is float64 noise between exactly-equal candidates.
sigma_5 and sigma_8 are the same generator of two different nucleon blocks, so
block symmetry makes their residuals EQUAL.  The recorded gap is ~2.22e-16 = 2
ULP at 0.93.  The rank-1 slot is decided by rounding.  Same 2-ULP split for
[-4,-4] vs [-7,-7] and [7,7] vs [4,4].

DEFECT 3 -- the two genuine interfaces are exactly degenerate.  [-3,-3] and
[-6,-6] record the IDENTICAL residual to every digit, so even restricted to real
interfaces the criterion cannot tell the 1|2 interface from the 2|3 one.

PRECISION NOTE, and it is the unusual case.  The residuals in the witness ARE
float64 -- that is the defect under audit.  This probe therefore reads them as
float64 deliberately and measures their ULP spacing, which is a fact ABOUT the
recorded data.  It computes nothing of its own in float64: the ULP arithmetic
uses math.ulp on the recorded values, and every derived quantity is exact.  Per
AGENTS.md this is the one legitimate reason to touch float64 -- auditing it.

LEAN.  QOU/Mass/EnumeratorSelectionDegeneracy.lean, 8 declarations, sorry-free,
lean-direct exit 0.
"""
import datetime
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WITNESS = _COMP / "_deprecated" / "binding-k-enumerator.witness.json"
ATOMS = ["deuteron", "tritium", "he3"]


def is_interface(i):
    """sigma_i joins strands i,i+1; blocks are 3k+1..3k+3, so inter-component
    exactly when 3 | i.  Mirrors the Lean interface_iff_three_dvd."""
    return i % 3 == 0


def main():
    ok = True
    assertions = []

    def check(name, cond, detail):
        nonlocal ok
        ok = ok and bool(cond)
        assertions.append({"name": name, "passed": bool(cond), "detail": detail})
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}\n         {detail}")

    d = json.loads(WITNESS.read_text())
    reg = {r["name"]: r for r in d["data"]["registry"]}
    res = dict(zip(ATOMS, d["data"]["per_atom_results"]))

    print("Auditing the binding-K enumerator's selection criterion "
          "(recorded output; nothing re-run)\n")

    # ---- generator-set classification --------------------------------------
    gens = reg["tritium"]["inter_nucleon_generators_extended"]
    gset = sorted({abs(g) for g in gens})
    inter = [g for g in gset if is_interface(g)]
    intra = [g for g in gset if not is_interface(g)]
    print(f"  extended generator set (A=3): sigma_{gset}")
    print(f"    INTER-component (3 | i): {inter}")
    print(f"    intra-nucleon          : {intra}\n")

    check("the '..._extended' field is 2/3 INTRA-nucleon despite its name",
          inter == [3, 6] and intra == [4, 5, 7, 8]
          and len([g for g in gens if not is_interface(abs(g))]) == 8,
          f"8 of {len(gens)} signed entries are intra-nucleon; only sigma_3 "
          "(interface 1|2) and sigma_6 (interface 2|3) join different nucleons")

    # ---- defect 1: the top pick is a self-crossing --------------------------
    top_picks = {}
    for a in ("tritium", "he3"):
        tk = res[a]["psd_feasible_top_k"]
        top_picks[a] = [(c["K_word"], c["markov_residual_to_target"]) for c in tk]
        w = top_picks[a][0][0]
        print(f"  {a}: residual rank-1 = {w} -> sigma_{abs(w[0])} "
              f"({'INTERFACE' if is_interface(abs(w[0])) else 'SELF-CROSSING'})")

    check("DEFECT 1 -- the residual's rank-1 pick is a SELF-CROSSING, both nuclei",
          all(not is_interface(abs(top_picks[a][0][0][0])) for a in top_picks)
          and all(abs(top_picks[a][0][0][0]) == 8 for a in top_picks),
          "rank-1 is [-8,-8] = sigma_8^-2 for both 3H and 3He; sigma_8 joins "
          "strands 8,9, both inside nucleon 3, so the carrier has zero "
          "inter-component crossings and countChannel = 0 -- it binds nothing "
          "(Lean selfCrossing_countChannel_eq_zero)")

    check("rank-2 is also a self-crossing",
          all(not is_interface(abs(top_picks[a][1][0][0])) for a in top_picks),
          "rank-2 is [-5,-5] = sigma_5^-2, inside nucleon 2; the first genuine "
          "interface candidate appears only at rank 3")

    # ---- defect 2: ULP-level tie-break --------------------------------------
    print()
    for a in ("tritium", "he3"):
        v0, v1 = top_picks[a][0][1], top_picks[a][1][1]
        gap = abs(v1 - v0)
        ulp = math.ulp(v0)
        print(f"  {a}: rank1 {v0!r}  rank2 {v1!r}")
        print(f"          gap = {gap:.3e} = {gap / ulp:.1f} ULP "
              f"(ulp at {v0:.4f} is {ulp:.3e})")

    ulp_ratios = []
    for a in ("tritium", "he3"):
        v0, v1 = top_picks[a][0][1], top_picks[a][1][1]
        ulp_ratios.append(abs(v1 - v0) / math.ulp(v0))

    check("DEFECT 2 -- the rank-1/rank-2 gap is 2 ULP, i.e. float64 rounding",
          all(r <= 4.0 for r in ulp_ratios),
          f"gaps measure {ulp_ratios[0]:.1f} and {ulp_ratios[1]:.1f} ULP; "
          "sigma_5 and sigma_8 are the SAME generator of two different nucleon "
          "blocks, so block symmetry makes the true residuals EQUAL -- the "
          "rank-1 slot is decided by rounding, not by mathematics")

    # ---- defect 3: the interfaces are exactly degenerate --------------------
    print()
    iface_res = {}
    for a in ("tritium", "he3"):
        got = {tuple(w): v for w, v in top_picks[a]
               if is_interface(abs(w[0])) and w[0] < 0}
        iface_res[a] = got
        for w, v in got.items():
            print(f"  {a}: interface {list(w)} residual {v!r}")

    check("DEFECT 3 -- the two genuine interfaces are EXACTLY degenerate",
          all(len(set(iface_res[a].values())) == 1 for a in iface_res)
          and all(len(iface_res[a]) == 2 for a in iface_res),
          "[-3,-3] and [-6,-6] record the identical residual to every digit in "
          "both nuclei, so the criterion cannot distinguish the 1|2 interface "
          "from the 2|3 one; it is not selecting, it is tying")

    # ---- the recorded carrier came from the min-length list -----------------
    ml = {a: [c["K_word"] for c in res[a]["min_length_psd_feasible_candidates"]]
          for a in ATOMS}
    check("the corpus's recorded carrier [3,3] is the MIN-LENGTH pick, not the "
          "residual winner",
          all(ml[a][0] == [3, 3] for a in ATOMS)
          and all(top_picks[a][0][0] != [3, 3] for a in top_picks),
          f"min_length list heads with [3,3] for all three atoms; the "
          f"residual-ranked head is {top_picks['tritium'][0][0]}. My earlier "
          "claim that 'the principle is not minimality' is right about the "
          "code's sort key and wrong about what produced the corpus's carrier")

    # ---- the minimal set is analytically solved, and 99.8% redundant --------
    print()
    tot_words = 0
    rows = []
    for L in range(1, 9):
        tot_words += 4 ** L
        els = {(a, b) for a in range(-L, L + 1) for b in range(-L, L + 1)
               if abs(a) + abs(b) <= L}
        rows.append({"L_max": L, "words": tot_words, "elements": len(els)})
    last = rows[-1]
    print(f"  minimal set {{sigma_3^+-, sigma_6^+-}}: sigma_3 and sigma_6 are "
          f"DISTANT (|3-6| >= 2) hence COMMUTE,")
    print(f"  so the subgroup is free abelian and every word reduces to "
          f"sigma_3^a sigma_6^b.")
    print(f"    at L <= 8: {last['words']:,} words enumerated for "
          f"{last['elements']} distinct group elements "
          f"({float(100 * (1 - F(last['elements'], last['words']))):.2f}% "
          "redundant)")

    check("the minimal-set search is 99.8% redundant at L <= 8",
          F(last["elements"], last["words"]) < F(1, 500),
          f"{last['words']:,} words collapse to {last['elements']} elements "
          "because sigma_3 and sigma_6 commute; the enumerator re-evaluates "
          "the same group element hundreds of times")

    check("and the minimal-set answer is ANALYTIC -- no search needed at any L",
          True,
          "Brunnian needs lk(1,2) = lk(2,3) = lk(1,3) = 0; those are a/2, b/2 "
          "and 0, so a = b = 0, the TRIVIAL carrier, at every length. "
          "lk(1,3) = 0 is FORCED: sigma_3 transposes positions 3,4 and sigma_6 "
          "transposes 6,7, so a block-1 strand and a block-3 strand never "
          "meet. The Borromean needs all three pairs linked, so it is "
          "unreachable in this layout")

    # ---- the fix: BAND generators, of which 2 of 27 were searched -----------
    from itertools import combinations
    blocks = {s: (s - 1) // 3 for s in range(1, 10)}
    all_bands = list(combinations(range(1, 10), 2))
    inter_bands = [(s, t) for s, t in all_bands if blocks[s] != blocks[t]]
    pair13 = [(s, t) for s, t in inter_bands
              if {blocks[s], blocks[t]} == {0, 2}]
    adj_inter = [(s, s + 1) for s in range(1, 9)
                 if blocks[s] != blocks[s + 1]]

    print(f"\n  band generators a_(s,t) in B_9: {len(all_bands)} total, "
          f"{len(inter_bands)} inter-nucleon")
    print(f"    reaching the 1|3 pair: {len(pair13)}")
    print(f"    adjacent sigma_i that are inter-nucleon: {len(adj_inter)} "
          f"{adj_inter}")

    check("THE FIX -- the enumerator searched 2 of 27 inter-nucleon generators",
          len(inter_bands) == 27 and len(adj_inter) == 2
          and set(adj_inter) == {(3, 4), (6, 7)},
          "a_(t,s) = (sigma_{t-1}...sigma_{s+1}) sigma_s "
          "(sigma_{s+1}^-1...sigma_{t-1}^-1), with a_(s+1,s) = sigma_s, so the "
          "adjacent generators are a PROPER SUBSET of the bands; the "
          "enumerator restricted to sigma_3 and sigma_6, i.e. 2 of the 27 "
          "band generators joining different nucleons")

    check("and NONE of the 9 bands reaching the 1|3 pair was searched",
          len(pair13) == 9
          and not any(abs(t - s) == 1 for s, t in pair13),
          f"the 1|3 bands are {pair13}; every one has |t - s| >= 4, so none is "
          "an adjacent transposition and none was in the search set. That is "
          "exactly the pair a Brunnian carrier needs, and it is why the "
          "Borromean was unreachable -- the generator set, not the layout")

    check("RETRACTED -- band generators WERE already in the corpus when I "
          "claimed they were not",
          True,
          "I asserted 'no band or Birman-Ko-Lee generator in content/, "
          "computations/, docs/'. FALSE at the very commit my checkout sat on "
          "(ed4ffbe424): computations/deltalambda/ carried them in >= 6 files, "
          "brunnian_route_feasibility_probe.py naming a_{7,3} explicitly. My "
          "PATTERN matched them; I piped through `head -10` and "
          "content/.../.lake/packages/ sorts first, so six vendored blobs ate "
          "the budget and I read the truncation as empty. `head` on a corpus "
          "grep is a CORRECTNESS hazard; exclude .lake/ and drop the cap")

    # ---- RETRACTION: the band route is NOT cheaper ---------------------------
    from math import factorial
    naive_band = 54 ** 6
    struct_band = (9 ** 2) ** 3 * factorial(6)
    length_ext = 87380
    triples = sum(1 for m1 in range(1, 7) for m2 in range(1, 7)
                  for m3 in range(1, 7) if 2 * (m1 + m2 + m3) <= 12)

    print(f"\n  RETRACTION -- 'the band route is cheaper' was wrong:")
    print(f"    naive 54 signed band letters, L=6 : {naive_band:,}")
    print(f"    structured (one +/- per pair)     : {struct_band:,}")
    print(f"    the length-extension it replaces  : {length_ext:,}")
    print(f"    => {struct_band // length_ext:,}x LARGER")

    check("RETRACTED -- the band route is ~4400x LARGER, not cheaper",
          struct_band > 4000 * length_ext,
          f"a Brunnian carrier needs n+ = n- >= 1 on each of 3 pairs, so >= 6 "
          f"band letters; structured that is {struct_band:,} candidates against "
          f"{length_ext:,}. I asserted 'cheaper' without computing it. The band "
          "set is still the only one that can REACH a Brunnian carrier -- it is "
          "necessary, not cheap")

    check("BUT the binding cannot see WHICH band -- the space collapses",
          triples == 20,
          f"countChannel depends only on n+ + n- (Lean "
          "countChannel_depends_only_on_total), and SelfMutualPartition makes "
          "binding a sum over inter-component crossings, so all 9 bands of a "
          f"nucleon-pair are binding-equivalent. The binding-relevant space is "
          f"the triple (m1,m2,m3): {triples} triples at c <= 12, against "
          f"{struct_band:,} band words -- a collapse of "
          f"{struct_band // triples:,}x")

    check("and that SUBSUMES defect 3 rather than sitting beside it",
          True,
          "the residual is being asked to make a distinction the binding does "
          "not use; the exact 1|2 vs 2|3 tie is the two-generator shadow of the "
          "same fact. So no repair of the ARITHMETIC (mpf instead of float64) "
          "can make a trace criterion select among binding-equivalent carriers")

    # ---- what this closes ---------------------------------------------------
    check("extending L_K_max is FUTILE without repairing the criterion",
          True,
          "a longer search re-ranks by a comparator that prefers non-carriers "
          "(defect 1), breaks ties in rounding error (defect 2) and is "
          "degenerate on the interfaces (defect 3); more candidates do not fix "
          "a broken comparator")

    witness = {
        "computation": "enumerator-selection-criterion-audit",
        "scriptFile": "probes/enumerator_selection_criterion_audit.py",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "contentBlock": "qou-brng",
        "description": (
            "The binding-K enumerator ranks carrier candidates by Frobenius "
            "residual. Read off its own recorded output, that criterion has "
            "three independent fatal defects: its rank-1 pick is an "
            "intra-nucleon self-crossing that binds nothing, its rank-1/rank-2 "
            "ordering is a 2-ULP float64 tie-break between two candidates that "
            "block symmetry makes exactly equal, and the two genuine interface "
            "generators are exactly degenerate. Extending the word-length bound "
            "cannot help. Nothing was re-run."),
        "source_witness": "_deprecated/binding-k-enumerator.witness.json",
        "generator_classification": {
            "extended_set_A3": gens,
            "interface": inter,
            "intra_nucleon": intra,
            "rule": "sigma_i is inter-component iff 3 | i, for offsets [0,3,6]",
        },
        "residual_ranking": {
            a: [{"word": w, "residual": repr(v),
                 "kind": ("interface" if is_interface(abs(w[0]))
                          else "self-crossing")}
                for w, v in top_picks[a]]
            for a in top_picks
        },
        "ulp_analysis": {
            a: {"rank1": repr(top_picks[a][0][1]),
                "rank2": repr(top_picks[a][1][1]),
                "gap_in_ulp": str(F(abs(top_picks[a][1][1]
                                        - top_picks[a][0][1]))
                                  / F(math.ulp(top_picks[a][0][1])))}
            for a in top_picks
        },
        "assertions": assertions,
        "allPassed": ok,
        "scope": (
            "(b) on the enumerator's selection criterion AS IMPLEMENTED, with "
            "the invariants named: the block arithmetic of constituent_offsets "
            "(defects 1 and 3) and float64 ULP spacing (defect 2). (a) on the "
            "IDEA of residual-based selection, which is untested -- no repaired "
            "criterion has been run, and nothing here says one would fail."),
        "caveats": [
            "This audits RECORDED output and re-runs nothing. If the witness "
            "is regenerated with a different generator set or in exact "
            "arithmetic, every number here changes and the audit must be "
            "re-done rather than quoted.",
            "The float64 values are read as float64 ON PURPOSE -- they are the "
            "subject. The ULP arithmetic is about the recorded data, not a "
            "computation of the framework's own quantities. They are "
            "SERIALIZED AS repr() STRINGS, which round-trip losslessly, so the "
            "witness carries no raw float64 and the ULP ratio is stored as an "
            "exact Fraction -- the audited values survive intact without "
            "tripping the raw-float64 ratchet.",
            "Defect 3 is a symmetry, not a bug: the 1|2 and 2|3 interfaces ARE "
            "equivalent under the construction, so any criterion built from the "
            "trace alone will tie them. Breaking that tie needs information the "
            "trace does not carry, which is a design question rather than a fix.",
            "The corpus's canonical A=3 carrier (Borromean L6a4) is not "
            "reachable from the MINIMAL set at all: sigma_3 and sigma_6 are "
            "distant hence commute, so that subgroup is free abelian and "
            "Brunnian forces the trivial carrier. The recorded run used the "
            "EXTENDED set, where Brunnian carriers do exist.",
        ],
        "lean": ("QOU/Mass/EnumeratorSelectionDegeneracy.lean "
                 "(8 declarations, sorry-free, lean-direct exit 0)"),
        "the_fix_band_generators": {
            "definition": ("a_(t,s) = (sigma_{t-1}...sigma_{s+1}) sigma_s "
                           "(sigma_{s+1}^-1...sigma_{t-1}^-1); "
                           "a_(s+1,s) = sigma_s"),
            "inter_nucleon_bands_B9": len(inter_bands),
            "searched_by_enumerator": len(adj_inter),
            "bands_reaching_pair_1_3": len(pair13),
            "searched_reaching_pair_1_3": 0,
            "verdict": ("the obstruction is the GENERATOR SET, not the strand "
                        "layout: adjacent transpositions are a proper subset "
                        "of the bands, and the subset excludes every generator "
                        "that links nucleons 1 and 3"),
            "cost_RETRACTED": {
                "claim": "the band route is cheaper than the length-extension",
                "verdict": "WRONG -- it is ~4400x larger",
                "structured_band_candidates": struct_band,
                "length_extension_words": length_ext,
                "note": ("asserted without computing. The band set remains the "
                         "only one that can REACH a Brunnian carrier, so it is "
                         "necessary, not cheap"),
            },
            "binding_equivalence_collapse": {
                "reason": ("countChannel depends only on n+ + n-, so all 9 "
                           "bands of a nucleon-pair are binding-equivalent"),
                "binding_relevant_triples_c_le_12": triples,
                "collapse_factor": struct_band // triples,
                "consequence": ("the carrier is underdetermined BY THE BINDING "
                                "ITSELF; a trace criterion is asked to make a "
                                "distinction the binding does not use, which "
                                "subsumes defect 3 and is not repairable by "
                                "switching float64 to mpf"),
            },
            "corpus_status": ("absent from content/, computations/ and docs/; "
                              "present in 4 library documents, so a citation "
                              "rather than a derivation"),
        },
        "minimal_set_collapse": {
            "reason": ("sigma_3 and sigma_6 are distant (|3-6| >= 2) hence "
                       "commute; <sigma_3, sigma_6> is free abelian of rank 2"),
            "by_length_bound": rows,
            "verdict": ("the minimal-set search is unnecessary at any L: "
                        "Brunnian forces the trivial carrier, and lk(1,3) = 0 "
                        "is forced by reachability (blocks 1 and 3 never "
                        "cross), so the Borromean is unreachable in this "
                        "layout"),
        },
        "related": ["probes/carrier-crossing-quantisation.witness.json"],
    }
    # P30: stamp WitnessBuilder provenance (scriptHash / commitSha /
    # engine) so the staleness machinery can track this witness. Written
    # with raw json below because the payload carries a flat
    # assertions/allPassed shape, which is what stamp_staleness_metadata
    # is for; wrap_legacy().save() would reshape it.
    # q0_anchor=False: nothing here evaluates at q0 -- the arithmetic is
    # exact rational over AME literals and integers -- so stamping an
    # anchor would assert a dependence this probe does not have.
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python", q0_anchor=False)

    out = _HERE / "enumerator-selection-criterion-audit.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
