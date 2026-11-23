#!/usr/bin/env python3
"""Chain walk, steps 7-8: the cheat sheet's chain is not the corpus's
dependency graph.

CONTEXT.  The canonical-derivation cheat sheet draws steps 1 -> 11 as a single
descending chain, each arrow reading like the others:

    step 7-8. GB-NF / jet  ->  E_inf = (+)_lambda M_{d_lambda}(Q(q))
    step  9.  Archimedean realization  ->  tau : C -> Vec_R at q = q_0
    step 10.  Confinement SDP  ->  selects canonical T_w
    step 11.  beta-decay Q  ->  Q_beta = |Delta(net(T_w))| . E_0

and its own step table flags step 8's carrier as `conj:jet-convergence-
classical-limit` -- "(conjecture, not prop -- corpus kind)".  That flag is
honest and is not the finding here.

THE QUESTION THE WALK ASKS.  If steps 9-11 are downstream of a conjecture,
AGENTS.md §3b (conjectural propagation) says they cannot be `proposition`
kind unless they satisfy §3b-cond: the conjecture axiomatised as a Lean class,
carried as an explicit `[Instance]` hypothesis, with a banner and an explicit
`uses[]` entry.  So: DO they declare it?

WHAT IS MEASURED.  The transitive `uses[]` cone of each chain carrier, read
from the `.ts` manifests -- the corpus's own formal dependency graph, which is
what the propagation audit and the pipeline actually walk.  No arithmetic;
this probe reads manifests and does graph reachability, so no precision
question arises.

THE RESULT, narrowly.  None of steps 9, 10, 11 reaches -- through `uses[]` --
any of the three carriers the step table NAMES for steps 7 and 8.  But step
9's cone DOES reach `conj:jet-prefix-gb-filtration`, i.e. the same GB/jet
machinery under a different label.

So the claim is about LABELS, not about dependence: the diagram's arrow is not
a `uses[]` edge, and the blocks it names for steps 7-8 are not the blocks the
dependency graph routes through.  An agent tracing the chain formally, by the
manifests, will not find what the cheat sheet sends it to.

I first wrote this as "steps 9-11 stand independently of the GB/jet
machinery".  That was TOO STRONG and section 4 is the measurement that
corrected it -- the same *grep the claim shape, not the topic* failure
AGENTS.md warns about, one label over.

PRIOR ART, checked first and cited rather than re-derived.  Two things this
probe's data would otherwise invite re-reporting, and both are already known:

  - `prop:atom-knot-mass-derivation` is an ALREADY-ADJUDICATED §3b-cond item-5
    violation (bean `qou-tmmt`, 2026-09-04, 8 confirmed of 9, still `todo`):
    its class field IS the theorem's conclusion, discharged by a bare
    projection.
  - `MassIdentity` reducing to a 25 % tolerance against AME is reported in
    `docs/audits/2026-06-07-proof-rater-baseline-audit.md`.

This probe does NOT claim a §3b propagation violation and does NOT re-report
either of the above.

Run:  python3 computations/audits/chain_uses_graph_vs_diagram_probe.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PAPER = REPO / "folio" / "quantum-observable-universe"

FAILURES: list[str] = []
CHECKS = 0

LABEL_RE = re.compile(r'label:\s*"([^"]+)"')
USES_RE = re.compile(r"uses:\s*\[(.*?)\]", re.S)
KIND_RE = re.compile(r"export default (\w+)\(")
STR_RE = re.compile(r'"([^"]+)"')


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


def load_graph() -> tuple[dict[str, list[str]], dict[str, str], dict[str, Path]]:
    """label -> uses, label -> kind, label -> path.  Bare labels only.

    A `uses` entry may be qualified (`paper-dir:label`) or a URL; those are
    cross-paper and are deliberately not followed -- the pipeline's own
    `uses-resolve` constraint skips them for the same reason.
    """
    uses: dict[str, list[str]] = {}
    kind: dict[str, str] = {}
    where: dict[str, Path] = {}
    for p in PAPER.rglob("*.ts"):
        if "/lean/" in str(p) or p.name.endswith(".d.ts"):
            continue
        try:
            txt = p.read_text(encoding="utf-8")
        except Exception:                                   # pragma: no cover
            continue
        m = LABEL_RE.search(txt)
        if not m:
            continue
        lab = m.group(1)
        k = KIND_RE.search(txt)
        kind[lab] = k.group(1) if k else "?"
        where[lab] = p.relative_to(REPO)
        u = USES_RE.search(txt)
        uses[lab] = (
            [s for s in STR_RE.findall(u.group(1)) if ":" in s and not s.startswith("http")]
            if u else []
        )
    return uses, kind, where


def cone(start: str, uses: dict[str, list[str]]) -> set[str]:
    seen: set[str] = set()
    stack = [start]
    while stack:
        n = stack.pop()
        for d in uses.get(n, []):
            # a qualified cross-paper ref has a paper-dir prefix, not a kind
            # prefix; those are not in this graph and are skipped.
            if d in uses and d not in seen:
                seen.add(d)
                stack.append(d)
    return seen


STEPS = [
    ("7  GB filtration", "prop:gb-spectral-sequence"),
    ("7  SS collapse", "prop:spectral-sequence-collapse"),
    ("8  jet order", "conj:jet-convergence-classical-limit"),
    ("9  mass identity", "prop:atom-knot-mass-derivation"),
    ("10 confinement SDP", "prop:confinement-sdp"),
    ("11 beta-decay Q", "prop:neutron-qvalue-symbolic"),
]


def main() -> int:
    print("chain uses-graph vs diagram probe")
    print("=" * 72)

    uses, kind, where = load_graph()
    print(f"\n    parsed {len(uses)} labelled blocks from {PAPER.relative_to(REPO)}\n")

    print("\n=== 1. the chain carriers exist and carry the kinds the table says ===\n")
    for name, lab in STEPS:
        check(lab in kind, f"step {name:20s} {lab}",
              f"kind={kind.get(lab, '(absent)')}  {where.get(lab, '')}")
    check(
        kind.get("conj:jet-convergence-classical-limit") == "conjecture",
        "step 8's carrier IS a conjecture, as the step table says",
        "the cheat sheet flags this itself -- honest, and not the finding here",
    )
    check(
        "conj:jet-filtered-knot-factor" in uses.get(
            "conj:jet-convergence-classical-limit", []),
        "and it is a DEPENDENT conjecture: it uses conj:jet-filtered-knot-factor",
        "so step 8 is not a root -- it sits on a second conjecture beneath it",
    )

    print("\n=== 2. do steps 9-11 reach steps 7-8 through uses[]? ===\n")
    upstream = {
        "prop:gb-spectral-sequence",
        "prop:spectral-sequence-collapse",
        "conj:jet-convergence-classical-limit",
    }
    for name, lab in STEPS[3:]:
        c = cone(lab, uses)
        hit = sorted(upstream & c)
        print(f"    step {name:20s} cone = {len(c):3d} blocks;  reaches 7/8: "
              f"{hit if hit else 'NONE'}")
    print()
    for name, lab in STEPS[3:]:
        check(
            not (upstream & cone(lab, uses)),
            f"step {name} does NOT reach step 7 or 8",
        )

    print("\n=== 3. does any of them reach ANY conjecture? ===\n")
    for name, lab in STEPS[3:]:
        c = cone(lab, uses)
        conjs = sorted(x for x in c if kind.get(x) == "conjecture")
        print(f"    step {name:20s} conjectures in cone: "
              f"{len(conjs)}  {conjs[:3] if conjs else ''}")
    print()
    print("    A `proposition` whose cone reaches a conjecture is a §3b matter")
    print("    (demote, or satisfy §3b-cond).  A cone that reaches NONE is not a")
    print("    propagation violation -- it is evidence the diagram's arrow is not")
    print("    a dependency edge.\n")

    print("\n=== 4. BUT the machinery is in the cone under a DIFFERENT label ===\n")
    c9 = cone("prop:atom-knot-mass-derivation", uses)
    check(
        "conj:jet-prefix-gb-filtration" in c9,
        "step 9's cone DOES reach conj:jet-prefix-gb-filtration",
        "so 'step 9 does not reach step 7 or 8' is a statement about the\n"
        "CHEAT SHEET'S NAMED CARRIERS, not about the GB/jet machinery.  The\n"
        "machinery is there; the diagram points at different labels for it.\n"
        "Reading (a) below is therefore TOO STRONG and is not asserted.",
    )

    print("\n=== 5. the disagreement, stated with its limits ===\n")
    print("""    The cheat sheet draws 7 -> 8 -> 9 -> 10 -> 11 as one descending
    chain.  The corpus's uses[] graph has no edge from 9, 10 or 11 to any of
    the three carriers the step table NAMES for steps 7 and 8 -- while step
    9's cone does reach `conj:jet-prefix-gb-filtration`, which is the same
    machinery under another label.

    So the honest statement is narrow: **the diagram's arrow is not a uses[]
    edge, and the labels it names for steps 7-8 are not the labels the
    dependency graph uses.**  An agent tracing the chain formally, by the
    manifests, will not find the blocks the cheat sheet sends it to.

    This probe does NOT claim steps 9-11 are independent of the GB/jet
    machinery (they are not -- see section 4), and does NOT claim a §3b
    propagation violation.

    PRIOR ART, checked before writing any of this and cited rather than
    re-derived:

      - `prop:atom-knot-mass-derivation` is an ALREADY-ADJUDICATED §3b-cond
        item-5 violation: its class field `AtomKnotMassDerivationConjecture.
        atom_knot_mass_derivation` IS the theorem's conclusion, discharged by
        a bare projection.  Bean `qou-tmmt` (2026-09-04), 8 confirmed of 9
        candidates, still `todo`.  Do not re-report it.
      - `MassIdentity` reducing to `B_pred >= 0 AND |B_pred - B_AME| <=
        B_AME/4` -- a 25 % tolerance against AME -- is reported in
        `docs/audits/2026-06-07-proof-rater-baseline-audit.md`.

    What survives as new here is only the graph measurement above.\n""")

    print("=" * 72)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
