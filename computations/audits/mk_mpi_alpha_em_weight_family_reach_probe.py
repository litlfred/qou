#!/usr/bin/env python3
"""Does the Molien ruling reach `m_K/m_pi` -- the corpus's ONE scoreable L2 win?

Bean `qou-oots`, whose remaining scope after the 2026-09-05 owner ruling
('molien. do the two arm reporting', re-affirmed 2026-09-08) is the alpha_EM
axis triage.

THE QUESTION, and it is not mine.  `alpha_em_b2_weight_family_triage_probe.py`
-- the existing triage, which measured the B2 scalar-c numerator moving
-42.2331 % under Molien -- states its own motivation as:

    "the corpus's ONE scoreable L2 result (m_K/m_pi) is alpha_em-conditional,
     so a weight-family change on this axis reaches the only sub-100x number
     the framework currently reports."

That is a reachability claim about the dashboard, and it was asserted as a
premise rather than measured.  This probe measures it.

THE ANSWER IS NO, because "the alpha_EM axis" is TWO constructions.
`m_K/m_pi = sqrt([3]_q[4]_q + (alpha_em/pi)(1 + log(1 + hbar_q)))`, and the
dashboard takes its alpha_em from `meson_em_sinh_closed_form
.alpha_em_inv_derived(q0)` -- the CS / sinh closed form.  The -42.2 % lives in
`alpha_em_b2_scalar_c_probe`, the B2 scalar c.  The two share the name of an
axis and do not share a call graph.

HOW IT IS MEASURED, and why a file-local grep would not settle it.  The
documented trap here is IMPORT-CONE DRIFT: a producer's own source can be
weight-free while a module it CALLS builds the weight (`binding_canonical.py`
is source-stable across its drift window while `tr_M_atom` moved 48 %, because
`tr_m_atom_via_transfer.py` changed).  So §2 walks the TRANSITIVE cone of every
in-repo module reachable from the producer, rather than stopping at the file or
at one hop, and §2 also checks for a cached-witness route, which a grep for
`dim_q` structurally cannot see.

🛑 §0 EXISTS BECAUSE THIS PROBE'S PREDECESSOR DIED OF A HARDCODED PATH.
The 2026-10-04 reorg moved `content/` -> `folio/` and `.beans/` ->
`beans/defs/`.  `bond_order_jbullet_citation_probe.py` hardcoded
`ROOT / "content"`, and run unrepathed against the moved tree it did not crash
and did not warn -- it reported `21 check(s) FAILED, 10 passed`, where all 21
were the absent directory and NOTHING was wrong in the corpus (PR #7742).
A detector confidently reporting about a tree it cannot see is the same class
as everything else in the blindness taxonomy, and it fails in the most
misleading possible way: as findings.

So §0 resolves every path this probe reads and asserts it was found.  If the
tree moves again, §0 fails with one check naming the repath and STOPS -- it
does not manufacture findings about files that are merely elsewhere.

AND THE SHARPER HALF OF THAT LESSON, learned by making the mistake here.  The
first version of §0 also gated on the CONTENT tree, discovered as `folio/` or
`content/`.  The predicate was wrong (blocks sit three levels deep, not two),
so §0 went red -- correctly refusing to continue, on a path this probe never
reads.  That is #7406's defect with the sign flipped: a probe red for a reason
that cannot affect its conclusion is as misleading as one green for one.
**Gate on what you read, and nothing else.**  This probe reads three files,
all under `computations/`; there is no content-tree dependency to break.

WHAT A NEGATIVE HERE DOES AND DOES NOT MEAN.

  DOES:  no module reachable from the alpha_em that `m_K/m_pi` consumes builds
         a partition weight, and none reads a witness, so there is no path --
         direct or transitive, by call or by cached value -- for the
         weight-family choice to move that number.
  DOES NOT:  say the B2 measurement is wrong (it is not; -42.2331 % is real),
         say `m_K/m_pi` is parameter-free (it is NOT -- see §4), or say the
         ruling moves nothing (it moves all three producers the bean names).

This narrows a stated worry.  It does not close the bean, whose subject is a
weight family with consumers still untriaged; §13a keeps it open regardless.

No arithmetic: every check is a static measurement over committed source.
No witness written, no producer re-run, nothing recomputed.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMP = ROOT / "computations"

DASHBOARD = COMP / "per_observable_100x_status.py"
PRODUCER = COMP / "meson_em_sinh_closed_form.py"
B2 = COMP / "alpha_em_b2_scalar_c_probe.py"
TRIAGE = COMP / "probes" / "alpha_em_b2_weight_family_triage_probe.py"

# Deliberately over-broad: a false positive costs a look, a false negative
# would make the whole negative worthless.
WEIGHT = re.compile(
    r"\bdim_q\w*|\bd_q\w*|q_dimension|q_factorial|wedderburn|plancherel|"
    r"molien|y_lambda|\bw_lambda\b",
    re.IGNORECASE,
)
_passed = 0
_failed = 0


def read(p: Path | None) -> str:
    if p is None or not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


def check(cond: bool, label: str, detail: str = "") -> None:
    global _passed, _failed
    mark = "✓" if cond else "✗"
    if cond:
        _passed += 1
    else:
        _failed += 1
    print(f"  {mark} {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"      {line}")


def _code_only(src: str) -> str:
    """Source with comments AND docstrings removed.

    `ast.unparse` drops comments but KEEPS docstrings -- they are ordinary
    string-literal statements.  `_precision.py` names `y_lambda_su_n` inside a
    docstring about a dps side effect, so an unparse-only filter still counts
    it as a weight.  Strip both or the filter is half a filter.
    """
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return src
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        body = getattr(node, "body", None)
        if (
            body
            and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)
        ):
            body.pop(0)
    try:
        return ast.unparse(tree)
    except ValueError:
        return src


def _reads(src: str) -> list[str]:
    """Filenames this module reads, from CODE only (not comments/docstrings)."""
    code = _code_only(src)
    return sorted(set(re.findall(r"[\w.\-]+\.json", code)))


def resolve(name: str) -> Path | None:

    """Find an in-repo module by bare name, as the corpus's sys.path shims do."""
    for base in (COMP, COMP / "substrate", ROOT / "tools" / "qou-substrate" / "python"):
        for cand in (base / f"{name}.py", base / name / "__init__.py"):
            if cand.exists():
                return cand
    hits = list(COMP.rglob(f"{name}.py"))
    return hits[0] if len(hits) == 1 else None


def imports_of(path: Path) -> list[str]:
    try:
        tree = ast.parse(read(path))
    except SyntaxError:
        return []
    out: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            out += [a.name.split(".")[0] for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            out.append(node.module.split(".")[0])
    return out


def cone(start: Path) -> dict[str, Path]:
    """Transitive in-repo import cone, by module name."""
    seen: dict[str, Path] = {}
    stack = [start]
    while stack:
        cur = stack.pop()
        for name in imports_of(cur):
            if name in seen:
                continue
            p = resolve(name)
            if p is None:          # stdlib / third-party — not ours to audit
                continue
            seen[name] = p
            stack.append(p)
    return seen


def section0() -> bool:
    print("\n=== 0. 🛑 every path this probe READS resolves ===\n")
    ok = True
    for p, why in (
        (DASHBOARD, "the L2 dashboard (§1)"),
        (PRODUCER, "the alpha_em producer (§2)"),
        (B2, "the B2 scalar-c probe (§3)"),
        (TRIAGE, "the existing alpha_EM triage (§3)"),
    ):
        here = p.exists()
        check(here, f"{why}: {p.relative_to(ROOT)}")
        ok = ok and here
    if not ok:
        print(
            "\n      A path moved.  Repath the constants above and re-run.  Do NOT\n"
            "      read the rest of this output: a probe that cannot see its inputs\n"
            "      reports findings about absence, which is how #7406 came to report\n"
            "      21 red about a corpus that was fine."
        )
    return ok


def section1() -> None:
    print("\n=== 1. which alpha_em does the m_K/m_pi dashboard row use ===\n")
    d = read(DASHBOARD)
    check(
        "from meson_em_sinh_closed_form import alpha_em_inv_derived" in d,
        "the row imports `alpha_em_inv_derived` from `meson_em_sinh_closed_form`",
        "and the next line is `_alpha_em_inv = alpha_em_inv_derived(q0)`, so the\n"
        "dashboard CALLS the derivation rather than copying a value -- which the\n"
        "producer's own docstring says is deliberate: \"A value copied across\n"
        "module boundaries cannot follow a re-pin; a call can.\"",
    )
    check(
        "alpha_em_b2" not in d,
        "🛑 and the dashboard never mentions `alpha_em_b2` at all",
        "so the B2 scalar-c route -- where the -42.2331 % Molien shift lives --\n"
        "is not on the path to any dashboard row.",
    )
    check(
        "CLASS-A acknowledged anchor" in d,
        "the row's own note calls its alpha_em a CLASS-A acknowledged anchor",
        "conditional on the open Witten-κ `sorry`.  A DIFFERENT epistemic\n"
        "caveat from the weight family, and untouched here.",
    )


def section2() -> None:
    print("\n=== 2. the TRANSITIVE cone of that producer — no weight anywhere ===\n")
    src = read(PRODUCER)
    own = [m.group(0) for m in WEIGHT.finditer(src)]
    check(
        not own,
        "the producer's own source builds NO partition weight",
        f"matches for dim_q / d_q / q_dimension / q_factorial / wedderburn /\n"
        f"plancherel / molien / y_lambda / w_lambda: {len(own)}",
    )
    check(
        not _reads(src),
        "and the producer itself reads no JSON artifact at all",
        "so a weight cannot arrive as a cached VALUE either -- the route a\n"
        "grep for `dim_q` structurally cannot see.",
    )

    c = cone(PRODUCER)
    print(f"    transitive in-repo cone: {len(c)} module(s)")
    dirty_w: list[str] = []
    all_reads: dict[str, list[str]] = {}
    for name in sorted(c):
        s = read(c[name])
        # Comments AND docstrings stripped: prose naming a weight is not a
        # weight being built.
        w = bool(WEIGHT.search(_code_only(s)))
        rd = _reads(s)
        if rd:
            all_reads[name] = rd
        flag = "  <-- WEIGHT" if w else (f"  reads {','.join(rd)}" if rd else "")
        print(f"      {name:24s} {c[name].relative_to(ROOT)}{flag}")
        if w:
            dirty_w.append(name)
    check(
        not dirty_w,
        "🛑 NOT ONE module in the transitive cone builds a partition weight",
        "measured transitively, with comments AND docstrings stripped.  Both\n"
        "matter: `_precision.py` names `y_lambda_su_n` in a DOCSTRING about a\n"
        "dps side effect, and `ast.unparse` alone keeps docstrings, so an\n"
        "unparse-only filter still reports it as a weight.",
    )

    # The OTHER route a weight could arrive by is a cached artifact.  Reading
    # JSON is not itself that route -- this cone reads CODATA tables and the
    # q0 anchor manifest, which are experimental inputs and pin configuration.
    # So classify the reads rather than assert there are none.
    weighty = {f for rs in all_reads.values() for f in rs
               if re.search(r"y[-_]lambda|wedderburn|plancherel|molien|delta[-_]lambda|dim[-_]q", f, re.I)}
    check(
        not weighty,
        "and no module reads a weight-bearing artifact",
        "what the cone DOES read: "
        + "; ".join(f"{k} -> {','.join(v)}" for k, v in sorted(all_reads.items()))
        + "\nCODATA tables and `q0_anchor_manifest.json` (which pin a producer\n"
        "reads) are experimental input and configuration, not partition data.\n"
        "An earlier version of this check asserted the cone reads NO json at\n"
        "all and went red on exactly those -- conflating 'reads a file' with\n"
        "'could import a weight'.  Classify the reads; do not forbid them.",
    )


def section3() -> None:
    print("\n=== 3. the -42.2 % is real — it is on the other construction ===\n")
    b2 = read(B2)
    check(
        "_wedderburn_weight" in b2 and "_q_dimension" in b2,
        "`alpha_em_b2_scalar_c_probe` DOES build `d_q(λ)² / [n]_q!`",
        "so the weight-family question genuinely bites there.  This probe does\n"
        "not dispute that measurement, only its reach.",
    )
    t = read(TRIAGE)
    # Whitespace-tolerant: the phrase WRAPS across a line break in the source
    # ("...ONE scoreable L2\nresult (m_K/m_pi)..."), so a single-line literal
    # returns False on text plainly there.  🛑 This is the SECOND time I have
    # made this exact mistake -- the first was the `the same $J^\bullet$` match
    # in `bond_order_jbullet_citation_probe.py`, fixed 2026-09-14 and written up
    # in that probe's own docstring as a lesson.  I then wrote this probe while
    # citing that lesson and reproduced the defect anyway.  Match across
    # whitespace by default; a literal containing a space is a latent bug.
    motive = re.search(r"ONE\s+scoreable\s+L2\s+result\s+\(m_K/m_pi\)", t)
    check(
        motive is not None,
        "and the existing triage names m_K/m_pi as its motivation",
        "which is the reachability claim §1 and §2 measure.  A reasonable worry\n"
        "stated as a premise; it is now measured false.",
    )
    check(
        "not currently a delivered number" in t or "NOT yet supplied" in t,
        "that triage also records the B2 scalar c is not a delivered number",
        "its Hodge denominator (the Braden-Northover period polarization of\n"
        "Jac(Bring)) is unsupplied.  So the -42.2 % moves the NUMERATOR of a\n"
        "quantity the corpus does not publish -- a second, independent reason\n"
        "it reaches no scored row.",
    )


def section4() -> None:
    print("\n=== 4. what this does NOT rehabilitate ===\n")
    print(
        """    m_K/m_pi is STILL not a parameter-free prediction.  AGENTS.md's
    red-team entry stands: the derived core sqrt([3]_q·[4]_q) misses this
    observable's own (unusually loose, 263.6 ppb) 100x target by ~385x on its
    own; the sub-100x result is manufactured by an EM correction whose
    alpha_em is conditional on the open Witten-κ `sorry`, and whose (3,4) pair
    is scan-selected.  The canonical statement is "1/6 scoreable -- and that 1
    is truncation-fitted + alpha_em-sorry-conditional => 0/6 unconditional".

    So quote this finding narrowly: the WEIGHT-FAMILY ruling does not reach it.
    Three other things still do.

    AND THE RULING DOES MOVE THINGS -- just not this.  All three producers the
    bean names build `dim_q²`:
      * `alpha_em_b2_scalar_c_probe` -- a single-partition absolute
        normalisation, so it moves directly (-42.2331 %, measured).
      * `alpha_5_jucys_murphy_central` -- Σ dim_q² c_5 / Σ dim_q², a same-n
        weighted average.  The [n]_q! cancels but f^λ q^{-κ} dim_q vs dim_q²
        differ PER λ, so it is invariant under the d_q²/D² comparison arm and
        NOT under Molien.  Untriaged.
      * `alpha_em_b2_canonical_scale_ratio_probe` -- an explicit two-arm
        y_(4,1) vs w_(4,1) comparison with Molien absent as a third arm.
        Untriaged.

    WHAT WOULD OVERTURN THIS: a consumer edge the cone walk cannot see -- a
    subprocess call, an importlib/`__import__` by computed name, or a value
    hand-copied into the dashboard rather than imported.  The third is the
    realistic one, and the producer's own docstring records that it has
    happened before ("Two of them were carrying the literal 137.035944").
    §1 checks the live edge is a CALL, which excludes it here."""
    )


def main() -> int:
    print("=" * 72)
    print("does the Molien ruling reach m_K/m_pi, the one scoreable L2 win?")
    print("=" * 72)
    if not section0():
        print("\n" + "=" * 72)
        print("§0 FAILED — paths unresolved.  Repath before reading further.")
        return 1
    for s in (section1, section2, section3):
        s()
    section4()
    print()
    print("=" * 72)
    if _failed:
        print(f"{_failed} check(s) FAILED, {_passed} passed")
        return 1
    print(f"all {_passed} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
