"""N_l = 84 has NO producer — and that reframes two failed reproductions.

Two readings of N_l were tried and both failed to reproduce 84 (lattice points
of decompositions, refuted outright by a span test; feasible gluon adjunctions,
which give 65 at cap 9 and 88 at cap 10, never 84).  Before proposing a third,
this probe asks where the number came from.

The answer is that nothing computes it.  Full corpus-grep checklist:

 1. THE BLOCK'S OWN MANIFEST.  ilp-solution-count-unwrap.ts is a bare
    `remark` -- interprets def:confinement-level, uses prop:stable-atom-
    decidable -- with NO `computation:` field.  No script, no witness.

 2. WHAT IT USES.  prop:stable-atom-decidable likewise declares no
    `computation:` field.

 3. THE ONE NAMED SOURCE, and it is a dead citation.
    docs/audits/2026-05-27-mass-formula-uniqueness-argument.md, section
    "C5. Integer LP optimality (gluon derivation)", says the gluon count is
    "the unique integer LP minimum over the 84 feasible integer solutions",
    Source: "Exhaustive enumeration + LP shadow-price analysis",
    Witness: `mass-endomorphism.witness.json`.

    That witness EXISTS -- computations/mass-endomorphism.witness.json -- and
    does not contain the number.  Zero fields equal 84.  Zero keys mention
    ilp / solution / feasible / count / gluon.  Its own description is a
    different quantity entirely: "Mass endomorphism via Phi_q tower with
    z^2-weighted cross-term.  m_p/m_e = 9310.3278 (CODATA: 1836.152, error
    407.06%)".  So the citation points at a witness that is neither about the
    enumeration nor carries its result, and which records a 407 % error.

 4. THE ONLY ILP-COUNTING CODE IN THE CORPUS is deprecated, heuristic, and
    structurally cannot return 84.
    fsh-guts/deprecated/computations/confinement_adaptive.py::
    ilp_solution_count_nucleon_level(Z, N) returns 3 (both magic), 2 (one
    magic), 1 (neither), or 0 (A < 2).  Its own docstring: "Heuristic (proxy
    for Lenstra ILP enumeration) ... This is a categorical proxy; the full ILP
    enumeration per Lenstra's algorithm would be strictly correct but
    expensive."  Its maximum is 3.  It is also ORPHANED -- no live producer
    imports it.

 5. library/ (ingested sources): nothing.
 6. .beans/: only this branch's own bean.

WHY THIS MATTERS, and it is the point of the probe.  My two reproduction
attempts were measured against a number that nothing derives.  So their
failure is NOT evidence that the readings are wrong -- there is no computation
to agree with.  The honest status of N_l = 84 is an UNSOURCED FIGURE, in the
same class as the neutron NF table (also producerless, established earlier on
this branch by testing all six basis rows).

WHAT IS NOT CLAIMED.  That the number is wrong.  An exhaustive enumeration may
well have been run and its result recorded by hand; the audit doc says
"exhaustive enumeration" and that is entirely plausible.  What is established
is only that the corpus does not now contain anything that reproduces it, so
it cannot be checked, and a mismatch against it cannot be interpreted.

TWO METHOD NOTES, both self-inflicted, both caught by running the checks.

 (a) A grep for producers containing "adjoin" returns 50 live files against 8
     for "adjoin(?!t)" -- because "adjoin" is a substring of "ADJOINT", which
     is ubiquitous here.  A 6x false-positive rate from one unnoticed
     substring.  Both counts are reported below so the gap is visible.

 (b) The orphan check greps the tree for "confinement_adaptive" -- and THIS
     FILE contains that string, so on its first run the probe counted ITSELF
     as the module's one live importer and failed its own check.  A
     provenance audit that greps for a name must exclude its own source, or
     it manufactures the dependency it is looking for.

SCOPE-(a).  Provenance only.  Adjudicates no net value, asserts no gluon
count, proposes no third reading of N_l.

-- Ref: [manuscript] folio/quantum-observable-universe/knots-particles-confinement/ilp-solution-count-unwrap.md
-- Ref: [manuscript] docs/audits/2026-05-27-mass-formula-uniqueness-argument.md
-- Ref: [manuscript] computations/qbeta/qbeta_adjunction_ilp_probe.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402

from witness_base import WitnessBuilder  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent

_FAILURES: list[str] = []


def check(name, ok, detail, w=None):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    if w is not None:
        w.add_data(name, bool(ok))
        # bean qou-srvu. Without this the witness carried ZERO assertions and
        # `save()` still emitted `allPassed: true` -- green while claiming
        # nothing, indistinguishable to a consumer from a run that checked
        # something and passed. The verdict was already computed (it prints
        # [PASS]/[FAIL] above, is tallied into _FAILURES, and drives this
        # script's exit code); it just never reached `assertions[]`. No
        # threshold is chosen here and no claim is invented: `ok` is the
        # producer's own boolean and `True` is what the exit code already
        # compares it against.
        w.add_assertion(name, computed=bool(ok), expected=True, source=detail)
    if not ok:
        _FAILURES.append(name)
    return ok


def has_computation(ts_path: Path) -> bool:
    # A `computation:` FIELD, not the word: the block's own authorNotes quote
    # "`computation:`" in prose, which a substring test read as a declared
    # producer (2026-10-10 follow-up, bean qou-v4ux).
    return ts_path.exists() and re.search(
        r"^\s*computation\s*:", ts_path.read_text(), re.M) is not None


def main() -> int:
    w = WitnessBuilder("qbeta-nl84-provenance", engine="python")
    w.set_description(
        "Provenance audit of N_l = 84: the block declares no producer, the "
        "one named witness does not contain the number, and the only "
        "ILP-counting code in the corpus is a deprecated heuristic capped at "
        "3. The figure is unsourced, so the two failed reproductions on this "
        "branch cannot be read as evidence against their readings."
    )

    kpc = ROOT / "folio/quantum-observable-universe/knots-particles-confinement"

    # 1 + 2 -- declared producers
    blk = kpc / "ilp-solution-count-unwrap.ts"
    dec = kpc / "stable-atom-decidable.ts"
    b_has, d_has = has_computation(blk), has_computation(dec)
    print(f"\n  ilp-solution-count-unwrap.ts  declares computation? {b_has}")
    print(f"  stable-atom-decidable.ts      declares computation? {d_has}")
    w.add_data("block_declares_computation", b_has)
    w.add_data("used_block_declares_computation", d_has)

    check("neither_the_block_nor_what_it_uses_declares_a_producer",
          not b_has and not d_has,
          "ilp-solution-count-unwrap.ts is a bare `remark` with no "
          "`computation:` field, and prop:stable-atom-decidable, the block it "
          "`uses`, declares none either. So nothing in the manifest layer "
          "points at code that computes N_l", w)

    # 3 -- the one named source
    wit = ROOT / "computations/mass-endomorphism.witness.json"
    d = json.loads(wit.read_text())
    txt = json.dumps(d)
    eq84 = []

    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, path + "/" + k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, f"{path}[{i}]")
        elif str(o).strip() in ("84", "84.0"):
            eq84.append(path)

    walk(d)
    keys = [k for k in re.findall(r'"([^"]*)":', txt)
            if any(t in k.lower() for t in
                   ("ilp", "solution", "feasible", "count", "gluon"))]
    print(f"\n  cited witness: {wit.name}  (exists: {wit.exists()})")
    print(f"    fields equal to 84            : {len(eq84)}")
    print(f"    keys naming ilp/solution/count: {sorted(set(keys)) or 'NONE'}")
    print(f"    its description               : {str(d.get('description'))[:96]}")
    w.add_data("cited_witness_exists", wit.exists())
    w.add_data("cited_witness_fields_equal_84", len(eq84))
    w.add_data("cited_witness_relevant_keys", sorted(set(keys)))

    check("the_ONE_named_source_is_a_DEAD_citation",
          wit.exists() and len(eq84) == 0 and not keys,
          f"the 2026-05-27 mass-formula-uniqueness audit cites "
          f"'84 feasible integer solutions' with Witness: "
          f"mass-endomorphism.witness.json. The file exists but contains ZERO "
          f"fields equal to 84 and ZERO keys naming ilp/solution/feasible/"
          f"count/gluon. Its description is a different quantity -- a Phi_q "
          f"tower mass endomorphism recording a 407.06% error against CODATA. "
          f"The citation resolves to a file, which is why it survived review, "
          f"but not to the number", w)

    # 4 -- the only counting code
    dep = ROOT / "fsh-guts/deprecated/computations/confinement_adaptive.py"
    src = dep.read_text() if dep.exists() else ""
    returns = sorted({int(m) for m in re.findall(r"return (\d+)\n", src)})
    importers = subprocess.run(
        ["grep", "-rl", "confinement_adaptive", "--include=*.py",
         str(ROOT / "computations"), str(ROOT / "tools")],
        capture_output=True, text=True).stdout.split()
    # exclude THIS file: it greps for the module name, so its own source
    # contains the string and it counted itself as a live importer.
    _self = str(Path(__file__).resolve())
    live = [p for p in importers
            if ("_deprecated" not in p and "fsh-guts" not in p) and str(Path(p).resolve()) != _self]
    print(f"\n  only ILP-counting code: {dep.relative_to(ROOT)}")
    print(f"    return values     : {returns}   (max {max(returns) if returns else 'n/a'})")
    print(f"    live importers    : {len(live)}  {live or '(orphaned)'}")
    w.add_data("counting_code_return_values", returns)
    w.add_data("counting_code_live_importers", len(live))

    check("the_only_counting_code_CANNOT_return_84_and_is_orphaned",
          bool(returns) and max(returns) <= 3 and not live,
          f"confinement_adaptive.ilp_solution_count_nucleon_level returns "
          f"{returns} -- a magic-number lookup capped at 3, whose own "
          f"docstring calls it 'a categorical proxy' for 'the full ILP "
          f"enumeration per Lenstra's algorithm'. It cannot produce 84 for "
          f"anything, and it is deprecated with {len(live)} live importers", w)

    # the method note: "adjoin" is a substring of "adjoint"
    loose = subprocess.run(
        ["grep", "-rl", "adjoin", "--include=*.py", str(ROOT / "computations")],
        capture_output=True, text=True).stdout.split()
    loose = [p for p in loose if ("_deprecated" not in p and "fsh-guts" not in p)]
    tight = [p for p in loose
             if re.search(r"adjoin(?!t)", Path(p).read_text())]
    print(f"\n  method note -- grep 'adjoin' matches ADJOINT:")
    print(f"    files matching 'adjoin'      : {len(loose)}")
    print(f"    files matching 'adjoin(?!t)' : {len(tight)}")
    w.add_data("grep_adjoin_loose", len(loose))
    w.add_data("grep_adjoin_excluding_adjoint", len(tight))

    check("N_l_eq_84_is_an_UNSOURCED_FIGURE",
          not b_has and not d_has and len(eq84) == 0 and max(returns) <= 3,
          "no manifest declares a producer, the one named witness does not "
          "carry the number, and the only counting code is a deprecated "
          "heuristic capped at 3. So the two reproduction attempts on this "
          "branch were measured against a figure nothing derives, and their "
          "failure is NOT evidence against their readings. NOT claimed: that "
          "84 is wrong -- an exhaustive enumeration may have been run and its "
          "result recorded by hand. Claimed only: the corpus contains nothing "
          "that reproduces it, so it cannot be checked and a mismatch against "
          "it cannot be interpreted. Same class as the neutron NF table", w)

    print("\n  scope")
    print("    SCOPE-(a). Provenance only. Adjudicates no net value, asserts")
    print("    no gluon count, proposes no third reading of N_l.")
    w.add_data("scope", "(a) provenance only")

    total = 4
    print(f"\n  {total - len(_FAILURES)}/{total} checks passed")
    for f in _FAILURES:
        print(f"    FAILED: {f}")
    out = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-independent: q_0 is unreachable from this producer's import cone -- it imports only stdlib and WitnessBuilder. This is provenance bookkeeping over an ILP solution count, with no substrate evaluation. It was declared `ambiguous` in the manifest, which the builder can never stamp, so the witness went out unstamped. Bean qou-fl0a."
        ),
    })
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
