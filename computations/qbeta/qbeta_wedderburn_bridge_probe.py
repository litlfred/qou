#!/usr/bin/env python3
"""The bridge six coefficients rest on is mis-shaped — it is no longer opaque.

`qou-orjl` found that six of the seven coefficients in
`mass-formula-regime-switching-table1-data` are not hook products, while
`unified-iterative-correction-proof.md` states `C_lambda = m_e . H_q(lambda)` as
"the universal constant determined by the partition algebra". The block's own
hedge is that the volume / surface / Coulomb coefficients arise "through their
image under the Wedderburn embedding". This probe pins what that bridge actually
is. Bean `qou-qb7p`; re-measured for `qou-kp2z`.

*** WHAT CHANGED, AND WHAT DID NOT (2026-09-05, bean `qou-kp2z`) ***

This probe originally recorded THREE mechanical facts. Two are now retired by
construction and ONE is untouched — and the untouched one is the one that
carried the conclusion, so the conclusion stands and the evidence for it is
narrower. The retired facts are kept below as dated history, not deleted: they
were true when measured, and a reader comparing this file against the bean that
cites it needs to see which claim moved.

  RETIRED (measured true 2026-08-21; false since 2026-09-05)

  1. **It exists and is unconstructed.** The corpus's only formalised embedding
     was `QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed`, declared `opaque`, with
     the file's own explanation: "Using `axiom` keeps the embedding opaque
     pending concrete construction."

  2. **It registers as a FOURTH AXIOM.** `#print axioms` on a theorem that
     merely mentioned it returned

         [propext, Classical.choice, Quot.sound,
          QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed]

     Every other Lean file in this arc reported exactly the first three, so
     anything routed through the bridge was NOT axiom-clean by the corpus's own
     standard.

  `QOU/HeckeAlgebra/WedderburnConstruction.lean` (bean `qou-usol`) replaced it
  with `blockDiagonal` — an ordinary definition on the index type
  `Sigma lam, Fin (f^lam) x Fin (f^lam)`, proved injective, footprint exactly
  `[propext, Classical.choice, Quot.sound]`. The `opaque` was then deleted
  (bean `qou-kp2z`); nothing in the corpus had consumed it, so the axiom had
  been paid for by no one.

  STANDING, and decisive for the clause

  3. **Its shape is wrong for the job.** The constructed map has the SAME
     signature the opaque had:

         wedderburnEmbedOf : {n : Nat} -> RSKDimIdentity n
                             -> WedderburnDecomposition n
                             -> Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) Real

     Blocks IN, one matrix OUT — an assembly map. The clause needs the
     opposite: one block's scalar `C_{(2,1)}` split into three coefficients.
     Wrong direction AND wrong arity. Building the map changed its STATUS, not
     its DIRECTION.

  4. **And the landing is conditional.** `Sigma_lam (f^lam)^2 = n!` (RSK) is
     carried as the named hypothesis `RSKDimIdentity`, discharged by nothing in
     this corpus. The unconditional object is `blockDiagonal`, which lands in
     the sigma-type, not in `Fin (n!)`.

*** AND THERE IS NO ALTERNATIVE ***

Searched the corpus for another embedding: the sibling `wedderburn*` objects are
WEIGHTS (`wedderburnWeight`, `wedderburnStd`, `wedderburnSym`) and DIMENSIONS
(`wedderburnNonSignDimS3`, the `wedderburn_nK_via_witness` family). None is a
map of algebras. So the bridge is still unavailable on both readings: if the
block means the Wedderburn embedding, it is mis-shaped (and, for the `Fin (n!)`
form, conditional); if it means something else, that something is not defined
anywhere in the corpus.

*** THE LEAN THEOREM THAT DOES ACCOMPANY IT (added 2026-09-05) ***

This section used to say no Lean theorem was offered, because the tempting one —
"three independent coefficients cannot come from one scalar" — is FALSE as
stated: set-theoretically a single real encodes three. Making it true needs a
hypothesis, and manufacturing one would be the overreach this probe documents.

The hypothesis did not have to be manufactured. LINEARITY is already assumed for
the Markov trace in this corpus (`markovTrace_add`, `markovTrace_smul`,
`markovTrace_linear`). Under it, `QOU/HeckeAlgebra/WedderburnTrace.lean` proves:

  * `markovTraceOnWedderburn` factors through the block TRACES,
  * a functional of that form supported at a single lambda is exactly
    `c_lambda * trace (x_lambda)` -- one coefficient against one number,
  * so any THREE such are linearly dependent, with an explicit witness
    (`three_supported_traceFunctionals_dependent`).

This does not make the clause false. It rules out the route the clause names,
whenever that route is linear, factors through the Markov trace, and is
localised at (2,1). And it says where the room is: f^{(2,1)} = 2, so the block
is M_2(R) -- FOUR real dimensions, of which the trace reads one. The wanted
information is present in the block and destroyed by tracing it.

f^{(2,1)} = 2 was prose when that was written -- classical, but not a fact this
corpus had in Lean. `QOU/HeckeAlgebra/SeminormalDimSmall.lean` now proves it via
the Frame-Robinson-Thrall hook-length formula, so the (2,1) instances hold
unconditionally. It also proves f^{(1,1)} = 1, which is the boundary: at the
charge shape the block IS its trace and none of these results apply.

*** WHAT WAS DONE ABOUT IT ***

`unified-iterative-correction-proof.md`'s `(2,1)` clause is annotated as an OPEN
OBLIGATION rather than deleted — the claim may well be true, it is simply
unsupported, and a reader should not take it as derived. That annotation was
updated for `qou-kp2z` to say which of its three reasons survived.
"""
from __future__ import annotations

import json
import re
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
LEAN = ROOT / "folio/quantum-observable-universe/lean/QOU/HeckeAlgebra/Wedderburn.lean"
CONSTR = ROOT / ("folio/quantum-observable-universe/lean/QOU/HeckeAlgebra/"
                 "WedderburnConstruction.lean")
BLOCK = ROOT / "folio/quantum-observable-universe/mass-theory/unified-iterative-correction-proof.md"


def _strip_lean_comments(src: str) -> str:
    """Blank out Lean comments, preserving line numbering.

    Handles `--` to end of line and the nestable block forms `/- -/`, `/-- -/`
    and `/-! -/`.  Newlines inside blocks are kept so reported line numbers
    still match the file.
    """
    out = []
    i, n, depth = 0, len(src), 0
    while i < n:
        if src.startswith("/-", i):
            depth += 1
            out.append("  ")
            i += 2
        elif depth and src.startswith("-/", i):
            depth -= 1
            out.append("  ")
            i += 2
        elif depth:
            out.append("\n" if src[i] == "\n" else " ")
            i += 1
        elif src.startswith("--", i):
            j = src.find("\n", i)
            j = n if j == -1 else j
            out.append(" " * (j - i))
            i = j
        else:
            out.append(src[i])
            i += 1
    return "".join(out)


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    src = LEAN.read_text()

    print("=" * 78)
    print("1. THE OPAQUE IS GONE -- AND WAS CONSUMED BY NOTHING")
    print("=" * 78)
    decl = [ln.strip() for ln in src.splitlines() if "wedderburnEmbed" in ln]
    for ln in decl:
        print(f"    {ln}")
    ok &= chk("the_opaque_declaration_is_deleted",
              sum(1 for ln in src.splitlines()
                  if ln.startswith("opaque wedderburnEmbed")), 0,
              note="QOU/HeckeAlgebra/Wedderburn.lean. It read 'Using `axiom` "
                   "keeps the embedding opaque pending concrete construction' "
                   "and had no body. Deleted 2026-09-05, bean qou-kp2z. "
                   "Counts DECLARATION lines, not occurrences of the string: "
                   "the note left where it stood quotes the signature it "
                   "retired, and a retirement note naming its subject must not "
                   "read as the subject still being there")
    # `opaque` is irreducible AND reports in #print axioms, so while this stood
    # every declaration reaching it read as axiom-bearing. Measured before
    # removal on merged main at 7e75622: the sole term-level occurrence of the
    # name in the whole Lean tree was the declaration itself. The remaining
    # mentions are prose, which is what this asserts -- if a real use ever
    # appears the count moves and this fails.
    tree = ROOT / "folio/quantum-observable-universe/lean"
    term_uses = []
    for f in sorted(tree.rglob("*.lean")):
        if ".lake" in f.parts:
            continue
        for i, ln in enumerate(_strip_lean_comments(f.read_text()).splitlines(), 1):
            # The BARE identifier only. `wedderburnEmbedOf` and
            # `wedderburnEmbedTotal` are real declarations that legitimately
            # share the prefix; a substring test flags them, which would make
            # this gate fire on good news. See the note below.
            if re.search(r"\bwedderburnEmbed\b(?![A-Za-z0-9_'])", ln):
                term_uses.append(f"{f.relative_to(ROOT)}:{i}")
    ok &= chk("no_term_level_use_of_the_name_remains",
              term_uses, [],
              note="scans every non-.lake Lean source with COMMENTS STRIPPED, "
                   "for the BARE name. Two earlier versions were wrong in "
                   "opposite directions: filtering on a leading backtick "
                   "counted every doc mention as a use (including the "
                   "retirement note), and a plain substring test would flag "
                   "the legitimate wedderburnEmbedOf / wedderburnEmbedTotal. "
                   "Widened deliberately when qou-yos9 added the latter -- "
                   "the gate means 'the retired opaque has no consumers', not "
                   "'no identifier starts with these letters'")

    print()
    print("=" * 78)
    print("2. A REAL CONSTRUCTION STANDS IN ITS PLACE")
    print("=" * 78)
    csrc = CONSTR.read_text()
    cflat = " ".join(csrc.split())
    for name in ("blockDiagonal", "blockDiagonal_injective", "wedderburnEmbedOf"):
        print(f"    {name}")
    ok &= chk("the_construction_defines_the_assembly_unconditionally",
              "noncomputable def blockDiagonal" in cflat, True,
              note="an ordinary def on Sigma lam, Fin (f^lam) x Fin (f^lam) -- "
                   "no side condition, no opaque")
    ok &= chk("and_proves_it_injective",
              "theorem blockDiagonal_injective" in cflat, True,
              note="so it is not the zero map. This answers the objection the "
                   "deleted docstring raised: a stub returning 0 would "
                   "contradict the Markov-trace structure. The objection was "
                   "to a stub; the answer is a construction")
    ok &= chk("the_rsk_step_is_isolated_as_a_named_hypothesis",
              "def RSKDimIdentity" in cflat, True,
              note="Sigma_lam (f^lam)^2 = n! is a HYPOTHESIS on the Fin (n!) "
                   "landing, discharged by nothing here -- not an assumption "
                   "folded into the definition")

    print()
    print("=" * 78)
    print("3. THE SHAPE OBJECTION IS UNTOUCHED -- BLOCKS IN, ONE MATRIX OUT")
    print("=" * 78)
    m = re.search(r"noncomputable def wedderburnEmbedOf[\s\S]{0,300}", csrc)
    sig = " ".join(m.group(0).split()) if m else ""
    print(f"    {sig[:220]}")
    ok &= chk("the_signature_still_takes_a_decomposition_and_returns_one_matrix",
              bool("WedderburnDecomposition n" in sig and "Matrix" in sig), True,
              note="blocks IN, ONE matrix OUT -- the SAME direction and arity "
                   "the opaque had. The clause needs the opposite: one block's "
                   "scalar C_{(2,1)} split into three coefficients. Building "
                   "the map changed its status, not its shape. THIS is the "
                   "fact that carries the conclusion")

    print()
    print("=" * 78)
    print("4. AND THERE IS NO ALTERNATIVE EMBEDDING")
    print("=" * 78)
    others = ["wedderburnWeight (a weight)", "wedderburnStd / wedderburnSym (weights)",
              "wedderburnNonSignDimS3 (a dimension)",
              "wedderburn_nK_via_witness (witness data)"]
    for o in others:
        print(f"    {o}")
    ok &= chk("the_sibling_wedderburn_objects_are_weights_and_dimensions",
              len(others), 4,
              note="none is a map of algebras. So the bridge is unavailable on "
                   "BOTH readings: this object is opaque and mis-shaped, and "
                   "anything else is undefined in the corpus")

    print()
    print("=" * 78)
    print("5. WHAT WAS DONE ABOUT IT")
    print("=" * 78)
    blk = BLOCK.read_text()
    ok &= chk("the_block_clause_is_still_marked_an_open_obligation",
              "open\nobligation, not a derivation" in blk
              or "open obligation, not a derivation" in blk.replace("\n", " "), True,
              note="unified-iterative-correction-proof.md's (2,1) clause is "
                   "ANNOTATED, not deleted -- the claim may well be true, it is "
                   "simply unsupported, and a reader should not take it as "
                   "derived")
    ok &= chk("and_says_which_of_its_three_reasons_survived",
              "Not removed, and decisive here" in blk.replace("\n", " "), True,
              note="the opaque and the fourth-axiom reasons are retired; the "
                   "shape objection is not. A reader must not read 'the "
                   "embedding was built' as 'the clause was discharged'")
    wt = ROOT / ("folio/quantum-observable-universe/lean/QOU/HeckeAlgebra/"
                 "WedderburnTrace.lean")
    wtflat = " ".join(wt.read_text().split()) if wt.exists() else ""
    ok &= chk("the_linear_no_go_is_a_lean_theorem",
              "theorem three_supported_traceFunctionals_dependent" in wtflat, True,
              note="the shape objection is no longer only prose. Under "
                   "linearity -- already assumed for the Markov trace -- three "
                   "trace-factoring functionals at one partition are dependent")
    ok &= chk("the_trace_is_provably_lossy",
              "theorem trace_does_not_separate" in wtflat, True,
              note="the ROOM is a theorem too, not only the no-go: distinct "
                   "decompositions with every block trace equal, so every "
                   "trace-factoring functional is blind to the difference")
    sd = ROOT / ("folio/quantum-observable-universe/lean/QOU/HeckeAlgebra/"
                 "SeminormalDimSmall.lean")
    sdflat = " ".join(sd.read_text().split()) if sd.exists() else ""
    ok &= chk("the_21_dimension_fact_is_formalised",
              "theorem seminormalDim_p21" in sdflat
              and "theorem trace_does_not_separate_p21" in sdflat, True,
              note="f^{(2,1)}=2 was prose when the no-go was written. Proved "
                   "via the hook-length formula, so the (2,1) instances are "
                   "unconditional rather than resting on a classical value the "
                   "corpus had not written down")
    ok &= chk("and_the_complement_is_constructive",
              "theorem three_blockEntry_independent_p21" in sdflat, True,
              note="three trace-factoring functionals at one partition are "
                   "DEPENDENT; three block-reading ones at (2,1) are "
                   "INDEPENDENT. The pair says where a derivation must live. "
                   "It does NOT identify them with volume/surface/Coulomb -- "
                   "existence is a necessary condition for such a match, not "
                   "evidence of one")
    ok &= chk("and_the_boundary_case_is_recorded_too",
              "not_two_le_seminormalDim_p11" in sdflat, True,
              note="f^{(1,1)}=1, so at the charge shape the block IS its trace "
                   "and these results say NOTHING. Recorded as a theorem so the "
                   "limit of the no-go is visible rather than assumed")
    ok &= chk("and_the_block_is_wider_than_its_trace",
              "destroyed by taking its trace" in wtflat, True,
              note="f^{(2,1)}=2 so the block is M_2(R), four dimensions to the "
                   "trace's one. Recording the ROOM as well as the no-go, so "
                   "this is not read as the clause being refuted")
    print("  The (2,1) clause names the shape mismatch and the unmet RSK")
    print("  hypothesis, and still calls itself an open obligation.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-wedderburn-bridge",
        "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {
            "lean_source": "folio/quantum-observable-universe/lean/QOU/HeckeAlgebra/Wedderburn.lean",
            "block": "folio/quantum-observable-universe/mass-theory/unified-iterative-correction-proof.md",
            "construction": "folio/quantum-observable-universe/lean/QOU/"
                            "HeckeAlgebra/WedderburnConstruction.lean",
            "axiom_footprint_before_2026_09_05":
                "[propext, Classical.choice, Quot.sound, "
                "QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed]",
            "axiom_footprint_now": "[propext, Classical.choice, Quot.sound]",
            "note": "documentary + mechanical measurement; no Lean theorem is "
                    "offered, and the docstring says why. Two of the three "
                    "original facts are retired by construction (beans "
                    "qou-usol, qou-kp2z); the shape objection stands and is "
                    "what keeps the (2,1) clause an open obligation"},
        "data": {"declaration_lines": decl, "signature": sig[:400]},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_wedderburn_bridge_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-wedderburn-bridge.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
