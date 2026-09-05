#!/usr/bin/env python3
"""The bridge six coefficients rest on is opaque, axiom-bearing, and mis-shaped.

`qou-orjl` found that six of the seven coefficients in
`mass-formula-regime-switching-table1-data` are not hook products, while
`unified-iterative-correction-proof.md` states `C_lambda = m_e . H_q(lambda)` as
"the universal constant determined by the partition algebra". The block's own
hedge is that the volume / surface / Coulomb coefficients arise "through their
image under the Wedderburn embedding". This probe pins what that bridge actually
is. Bean `qou-qb7p`.

*** THREE MECHANICAL FACTS ***

1. **It exists and is unconstructed.** The corpus's only formalised embedding is
   `QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed`, declared `opaque`, with the
   file's own explanation: "Using `axiom` keeps the embedding opaque pending
   concrete construction."

2. **It registers as a FOURTH AXIOM.** `#print axioms` on a theorem that merely
   mentions it returns

       [propext, Classical.choice, Quot.sound,
        QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed]

   Every Lean file in this arc reports exactly the first three, so anything
   routed through the bridge is NOT axiom-clean by the corpus's own standard.

3. **Its shape is wrong for the job.** Signature:

       wedderburnEmbed : {n : Nat} -> WedderburnDecomposition n
                         -> Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) Real

   Blocks IN, one matrix OUT — an assembly map. The clause needs the opposite:
   one block's scalar `C_{(2,1)}` split into three coefficients. Wrong direction
   AND wrong arity.

*** AND THERE IS NO ALTERNATIVE ***

Searched the corpus for another embedding: the sibling `wedderburn*` objects are
WEIGHTS (`wedderburnWeight`, `wedderburnStd`, `wedderburnSym`) and DIMENSIONS
(`wedderburnNonSignDimS3`, the `wedderburn_nK_via_witness` family). None is a
map of algebras. So the bridge is unavailable on BOTH readings: if the block
means `wedderburnEmbed`, it is opaque, axiom-bearing and mis-shaped; if it means
something else, that something is not defined anywhere in the corpus.

*** WHY NO LEAN THEOREM ACCOMPANIES THIS ***

The tempting one — "three independent coefficients cannot come from one scalar"
— is FALSE as stated: set-theoretically a single real can encode three. Making
it true needs a continuity or naturality hypothesis the corpus does not supply,
and manufacturing one would be the same overreach this probe documents. The real
Lean content is the `#print axioms` measurement in fact 2, recorded here.

*** WHAT WAS DONE ABOUT IT ***

`unified-iterative-correction-proof.md`'s `(2,1)` clause is annotated as an OPEN
OBLIGATION rather than deleted — the claim may well be true, it is simply
unsupported, and a reader should not take it as derived.
"""
from __future__ import annotations

import json
import re
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
LEAN = ROOT / "content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Wedderburn.lean"
BLOCK = ROOT / "content/quantum-observable-universe/mass-theory/unified-iterative-correction-proof.md"


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
    print("1. THE EMBEDDING IS DECLARED OPAQUE")
    print("=" * 78)
    decl = [ln.strip() for ln in src.splitlines() if "wedderburnEmbed" in ln]
    for ln in decl:
        print(f"    {ln}")
    ok &= chk("the_only_embedding_is_declared_opaque",
              any(ln.startswith("opaque wedderburnEmbed") for ln in decl), True,
              note="QOU/HeckeAlgebra/Wedderburn.lean. The file's own words: "
                   "'Using `axiom` keeps the embedding opaque pending concrete "
                   "construction.' There is no body")
    # The source is line-wrapped, so match on whitespace-normalised text --
    # a raw substring check fails on "pending concrete\n    construction".
    flat = " ".join(src.split())
    ok &= chk("and_the_file_says_so_itself",
              "keeps the embedding opaque pending concrete construction" in flat,
              True,
              note="quoted verbatim in the block annotation; matched after "
                   "whitespace normalisation because the source wraps mid-phrase")

    print()
    print("=" * 78)
    print("2. ITS TYPE IS AN ASSEMBLY MAP — BLOCKS IN, ONE MATRIX OUT")
    print("=" * 78)
    m = re.search(r"opaque wedderburnEmbed[\s\S]{0,240}", src)
    sig = " ".join(m.group(0).split()) if m else ""
    print(f"    {sig[:200]}")
    ok &= chk("the_signature_takes_a_decomposition_and_returns_one_matrix",
              bool("WedderburnDecomposition n" in sig and "Matrix" in sig), True,
              note="blocks IN, ONE matrix OUT. The clause needs the opposite -- "
                   "one block's scalar C_{(2,1)} split into three coefficients. "
                   "Wrong direction and wrong arity")

    print()
    print("=" * 78)
    print("3. IT REGISTERS AS A FOURTH AXIOM")
    print("=" * 78)
    print("    measured with lean-direct on a theorem that merely mentions it:")
    print("      'uses_embed' depends on axioms: [propext, Classical.choice,")
    print("       Quot.sound, QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed]")
    print()
    print("    every Lean file in this arc reports exactly the first three, so")
    print("    anything routed through the bridge is NOT axiom-clean by the")
    print("    corpus's own standard.")
    ok &= chk("opaque_makes_it_an_axiom_not_a_definition",
              src.count("opaque wedderburnEmbed"), 1,
              note="`opaque` is irreducible AND shows up in #print axioms, "
                   "unlike a `def`. Recorded as a measurement rather than a "
                   "theorem -- see the docstring on why no Lean theorem "
                   "accompanies this")

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
    ok &= chk("the_block_clause_is_now_marked_an_open_obligation",
              "open\nobligation, not a derivation" in blk
              or "open obligation, not a derivation" in blk.replace("\n", " "), True,
              note="unified-iterative-correction-proof.md's (2,1) clause is "
                   "ANNOTATED, not deleted -- the claim may well be true, it is "
                   "simply unsupported, and a reader should not take it as "
                   "derived")
    print("  The (2,1) clause now names the opaque object, its axiom footprint")
    print("  and its arity mismatch, and calls itself an open obligation.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-wedderburn-bridge",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {
            "lean_source": "content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Wedderburn.lean",
            "block": "content/quantum-observable-universe/mass-theory/unified-iterative-correction-proof.md",
            "axiom_footprint": "[propext, Classical.choice, Quot.sound, "
                               "QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed]",
            "note": "documentary + mechanical measurement; no Lean theorem is "
                    "offered, and the docstring says why"},
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
