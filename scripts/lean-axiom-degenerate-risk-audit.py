#!/usr/bin/env python3
"""Rank Lean `axiom` declarations by degenerate-instance refutation risk.

Motivation
----------
On 2026-09-05 all five SDP uniqueness axioms in `QOU/MathlibExt/` were shown
to be **false** — each one alone derives `False` (bean `qou-i6u4`).  Two prior
audits of that exact family (2026-08-26, 2026-09-03) had cleared them, because
both asked *is the citation real* and *can Mathlib close it*.  Neither asked the
third question:

    is the Lean statement the theorem that citation names?

An axiom with an impeccable citation to a true published theorem can still be a
false Lean proposition, when the formalisation drops a hypothesis the paper
requires.  Here the missing hypothesis was dual nondegeneracy, and the five
axioms fell to a one-dimensional zero-cost SDP.

What this flags
---------------
The shared signature of all five: a **collapsing conclusion** — an equality, a
`= 0`, or a uniqueness claim — reached from hypotheses that a *degenerate*
instance of the axiom's own structures satisfies vacuously.  Concretely the
counterexample worked because `S = 0` makes `S * (X - Y) = 0` hold for every
`X`, `Y`: the hypothesis looks like a guard and constrains nothing.

So this ranks by:

  * `collapsing`   the conclusion is `a = b`, `... = 0`, `Unique ...`,
                   `Subsingleton ...`, or `-> v = 0`.
  * `vacuous_risk` a hypothesis is an equation whose left side is a product or
                   an application involving a bound variable — the shape that
                   goes vacuous when a factor degenerates.
  * `unconstrained` the axiom quantifies over a structure but constrains none
                   of its components with a positivity / definiteness /
                   nondegeneracy / rank hypothesis.

This is a **triage aid, not a decision**.  A high score means "write the
degenerate instance and try to refute it"; it is not evidence of falsity, and a
low score is not evidence of soundness.  The only proof either way is a Lean
term.

Self-test
---------
`--selftest` reconstructs the five known-false axioms from git history and
requires all five to score in the flagged band.  The audit aborts if they do
not, so a future narrowing cannot silently report a clean tree.
"""
from __future__ import annotations
import argparse, pathlib, re, subprocess, sys

DECL_START = re.compile(r"^(axiom|theorem|lemma|def|abbrev|instance|structure|class|example|opaque|noncomputable|@\[|/--|/-!|namespace|end|section|variable|open|import|universe|set_option)\b")
AXIOM_RE = re.compile(r"^axiom\s+([A-Za-z_][A-Za-z0-9_.'!?]*)")

# Identifiers here are Unicode -- `Φ'`, `sc.Φstar`, `y_λ`. An ASCII-only
# character class silently fails to see the very conclusion shape this audit
# exists to find; the self-test caught exactly that on the first run.
IDENT = r"[^\s(),:=]+"
COLLAPSING = re.compile(
    r"(=\s*0\s*$|=\s*" + IDENT + r"\s*$|\bUnique\b|\bSubsingleton\b)")
PRODUCT_HYP = re.compile(r"\([_A-Za-z][A-Za-z0-9_']*\s*:[^)]*[*·]\s*\(?[^)]*\)?\s*=\s*0")
GUARD = re.compile(r"\b(PosDef|PosSemidef|nondegener|Nondegener|0\s*<|rank|Rank|Injective|IsUnit|Invertible|≠\s*0|Function\.Bijective)\b")


def strip_block_comments(text: str) -> str:
    """Blank out `/- ... -/`, `/-! ... -/` and `/-- ... -/` regions, preserving
    line structure so reported line numbers stay correct.

    Load-bearing, and it was missing on the first run. Two things live inside
    Lean block comments here and both were being parsed as live declarations:

      * A documented POST-MORTEM. `LpDualityHypothesisClass.lean` records two
        axioms it deleted for being inconsistent, quoting them in a ```lean
        fence. The audit flagged `schrijver_strong_duality` as an unexamined
        candidate when it had already been found, refuted and removed.
      * ORDINARY ENGLISH. A prose line wrapping onto "axiom is consumed only
        via ..." starts with the word `axiom`, and there are fourteen such:
        `it`, `of`, `and`, `with`, `in`, `is`, `for`, `that`, `can`, `to`,
        `beyond`, `standing`, `audit`, `report`.

    Together those were 26 of 163 matches -- a 19 % overcount.
    """
    out = []
    i = 0
    depth = 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1; i += 2; continue
        if text.startswith("-/", i) and depth:
            depth -= 1; i += 2; continue
        if depth == 0:
            out.append(text[i])
        else:
            out.append("\n" if text[i] == "\n" else " ")
        i += 1
    return "".join(out)


def axioms_in(text: str, path: str):
    """Yield (name, line, full declaration text) for each top-level axiom."""
    lines = strip_block_comments(text).split("\n")
    out = []
    i = 0
    while i < len(lines):
        m = AXIOM_RE.match(lines[i])
        if not m:
            i += 1
            continue
        body = [lines[i]]
        j = i + 1
        # A declaration continues while lines are indented or blank-then-indented.
        while j < len(lines):
            nxt = lines[j]
            if nxt.strip() == "":
                # peek: a blank line ends the decl unless the next non-blank is indented
                k = j
                while k < len(lines) and lines[k].strip() == "":
                    k += 1
                if k < len(lines) and lines[k].startswith((" ", "\t")) and not DECL_START.match(lines[k].lstrip()):
                    body.extend(lines[j:k + 1]); j = k + 1; continue
                break
            if not nxt.startswith((" ", "\t")):
                break
            body.append(nxt)
            j += 1
        out.append((m.group(1), i + 1, "\n".join(body), path))
        i = j
    return out


def score(decl: str):
    """Return (score, reasons). Higher = more worth attempting to refute."""
    # Split hypotheses from conclusion at the final top-level ':' of the binder list.
    flat = decl
    reasons = []
    s = 0
    # conclusion = text after the last ',\n' or the final ':' at depth 0
    tail = flat.strip().split("\n")
    concl = ""
    for ln in reversed(tail):
        if ln.strip():
            concl = ln.strip()
            break
    if COLLAPSING.search(concl):
        s += 3; reasons.append("collapsing-conclusion")
    if PRODUCT_HYP.search(flat):
        s += 2; reasons.append("product-equation-hypothesis(vacuous-when-a-factor-is-0)")
    if not GUARD.search(flat):
        s += 2; reasons.append("no-positivity/rank/nondegeneracy-guard")
    if re.search(r"∀|\{[^}]*:\s*Type", flat) and "Empty" not in flat:
        s += 1; reasons.append("universally-quantified-over-an-index-type")
    oq_s, oq_r = overquantification_signals(decl)
    s += oq_s; reasons.extend(oq_r)
    return s, reasons


# --- Over-quantification: the root cause shared by all eleven known-false axioms ---
#
# Worked against the five documented incidents, TWO crisp rules are needed and they
# are disjoint -- 4/5 and 1/5. Do not collapse them into one; a single rule that
# "covers" all five would only do so by being vague enough to fire on everything.
#
#   rule A  the conclusion RELATES two binders that no hypothesis mentions together
#           -> B1 (`3 <= n` for a quantified n), Schrijver x2 (no hypotheses at all),
#              dressed-mass (F and M_N never tied), macroscopic x2 (psi and zeta
#              independent, joined only by the concluded iff)
#   rule B  the conclusion asserts `X = Y` while the hypotheses supply only
#           `f X = f Y` -- concluding the first from the second needs f injective,
#           which nothing asserts
#           -> the SDP five (`objAt Phi' = objAt sc.Phistar |- Phi' = sc.Phistar`)
#
# MEASURED on the live corpus after the SDP five were deleted: rule A fires on 38 of
# 137 (28 %), rule B on ZERO. So neither improves the live queue -- A is too broad to
# act on, B finds the shape genuinely absent elsewhere. A clean zero from a rule whose
# self-test proves it CAN fire is a result; a zero from an untested rule would not be,
# which is why the SDP five are reconstructed from git as fixtures rather than assumed.
#
# Reported this way rather than dropped: the flagged count stays 22, and rule A rides
# along as context on entries a primary signal already flagged.

BINDER_RE = re.compile(r"[({\[]\s*([^:()\[\]{}]+?)\s*:\s*([^()\[\]{}]*(?:\([^()]*\)[^()\[\]{}]*)*)\s*[)}\]]")
RELATIONAL = re.compile(r"(=|↔|≤|<|≥|>|∈|∉|≠)")


def _split_binders(decl: str):
    """Return (data_binders, hypothesis_binder_types, conclusion)."""
    body = decl.split("\n", 1)[1] if "\n" in decl else decl
    concl = ""
    for ln in reversed(body.split("\n")):
        if ln.strip():
            concl = ln.strip().rstrip(",")
            break
    # A binder whose TYPE is relational is a hypothesis; otherwise it names data.
    binders = [(names, ty) for names, ty in BINDER_RE.findall(body)
               if names.strip() and ty.strip()]
    data = [(n, ty) for names, ty in binders
            if not RELATIONAL.search(ty) for n in names.split()]
    hyps = [ty for _, ty in binders if RELATIONAL.search(ty)]
    return data, hyps, concl


def _mentions(text: str, name: str) -> bool:
    return re.search(r"(?<![A-Za-z0-9_'])" + re.escape(name) + r"(?![A-Za-z0-9_'])", text) is not None


def overquantification_signals(decl: str):
    """Return (extra_score, reasons) for the two over-quantification rules."""
    data, hyps, concl = _split_binders(decl)
    reasons = []
    extra = 0

    # rule A -- the conclusion relates binders nothing ties together
    in_concl = [n for n, _ in data if _mentions(concl, n)]
    if len(in_concl) >= 2:
        tied = any(sum(1 for n in in_concl if _mentions(h, n)) >= 2 for h in hyps)
        if not tied:
            # WEIGHT 0 ON PURPOSE -- annotation, not evidence. MEASURED on the live
            # corpus: this fires on 38 of 137 axioms (28 %), because "the conclusion
            # relates binders nothing else ties" is a description of what an axiom is
            # FOR. `QCasimir_comm_E_axiom` says the Casimir commutes with E: two
            # structurally connected objects, no hypothesis tying them, and the axiom
            # IS the tie. Scoring it +3 took the flagged list 22 -> 48, over a third
            # of the corpus, which is not triage.
            #
            # It stays because it is the signal that separates the four historical
            # incidents (a free ℕ under an inequality, an ℝ forced by an unrelated
            # factor, an iff between properties of independent objects) from the
            # SDP shape -- but it is only meaningful ALONGSIDE a primary signal.
            reasons.append("overquantified:conclusion-relates-binders-no-hypothesis-ties (weight 0 -- fires on 28 % of axioms; read only with a primary signal)")

    # rule B -- concludes X = Y from f X = f Y, with no injectivity anywhere
    m = re.match(r"^(.+?)\s*=\s*(.+?)$", concl)
    if m and "Injective" not in decl and "injective" not in decl:
        lhs, rhs = m.group(1).strip(), m.group(2).strip()
        for h in hyps:
            hm = re.match(r"^(.+?)\s*=\s*(.+?)$", h.strip())
            if not hm:
                continue
            hl, hr = hm.group(1), hm.group(2)
            # both sides of the conclusion occur INSIDE the hypothesis's sides,
            # i.e. under some application -- and the hypothesis is not the
            # conclusion itself.
            if (lhs in hl and rhs in hr and h.strip() != concl
                    and (hl.strip() != lhs or hr.strip() != rhs)):
                extra += 3
                reasons.append("overquantified:concludes-X=Y-from-fX=fY-without-injectivity")
                break
    return extra, reasons


# Verbatim axiom texts from the four prior post-mortems, used as self-test fixtures.
# Their axioms are deleted, so they cannot be recovered from git like the SDP five.
OVERQUANT_FIXTURES = [
    ("b1_hyperbolic_rows", """axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : ℕ)
    (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified"""),
    ("dressed_mass_split_substrate_closed_form", """axiom dressed_mass_split_substrate_closed_form
    (F : FlavorDressingFunctor) (M_N q : ℝ) (_hM : 0 < M_N) (_hq : 1 < q) :
    F.μ Flavor.down - F.μ Flavor.up = M_N * substrate_split_factor q"""),
]


KNOWN_FALSE_TEXT = [
    # The five SDP axioms refuted in PR #6882.  Their text is EMBEDDED, not read
    # from git, because they no longer exist anywhere on `main` -- the merge that
    # deleted them is what broke the previous `git show origin/main` self-test the
    # first time it ran after landing.  A guard whose reference point is the thing
    # it guards against cannot survive its own success.
    ("strict_complementarity_unique_axiom", """axiom strict_complementarity_unique_axiom :
    ∀ {n : ℕ} {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] [StarRing R] {ι : Type*}
      {sdp : SDPPrimal n R ι}
      (sc : StrictComplementarityPair sdp)
      {Φ' : Matrix (Fin n) (Fin n) R}
      (_h_feas : sdp.IsFeasible Φ')
      (_h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar),
        Φ' = sc.Φstar"""),
    ("slater_strict_complementarity_kernel_axiom", """axiom slater_strict_complementarity_kernel_axiom :
    ∀ {n : ℕ} {ι : Type*} [Fintype ι] {sdp : SDPPrimal n ℝ ι}
      (sc : RealStrictComplementarityPair sdp)
      {Φ' : Matrix (Fin n) (Fin n) ℝ}
      (_h_feas : sdp.IsFeasible Φ')
      (_h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar)
      (_h_constraint_diff :
        ∀ i : ι, Matrix.trace (sdp.constraint i * (Φ' - sc.Φstar)) = 0)
      (_h_S_diff : sdp.dualSlack sc.ystar * (Φ' - sc.Φstar) = 0)
      (_h_diff_S : (Φ' - sc.Φstar) * sdp.dualSlack sc.ystar = 0),
        Φ' = sc.Φstar"""),
    ("SDPRankUniqueness", """axiom SDPRankUniqueness
    {n : ℕ} {ι : Type*} [Fintype ι]
    (sdp : SDPPrimal n ℝ ι) (sc : RealStrictComplementarityPair sdp)
    (h_slater : sdp.IsStrictlyFeasible)
    {Φ' : Matrix (Fin n) (Fin n) ℝ}
    (h_feas : sdp.IsFeasible Φ')
    (_h_S_diff : sdp.dualSlack sc.ystar * (Φ' - sc.Φstar) = 0)
    (_h_constraint_diff :
      ∀ i : ι, Matrix.trace (sdp.constraint i * (Φ' - sc.Φstar)) = 0) :
    Φ' = sc.Φstar"""),
    ("strict_complementarity_kernel_disjoint", """axiom strict_complementarity_kernel_disjoint
    {ι : Type*} [Fintype ι]
    {sdp : SDPPrimal n ℝ ι} (sc : RealStrictComplementarityPair sdp)
    (h_slater : sdp.IsStrictlyFeasible) :
    ∀ v : Fin n → ℝ,
      sc.Φstar.mulVec v = 0 →
      (sdp.dualSlack sc.ystar).mulVec v = 0 →
      v = 0"""),
    ("affine_slater_rigidity", """axiom affine_slater_rigidity
    {n : ℕ} {ι : Type*} [Fintype ι]
    {sdp : SDPPrimal n ℝ ι} (sc : RealStrictComplementarityPair sdp)
    (_h_slater : sdp.IsStrictlyFeasible)
    (_h_rank_eq : sc.Φstar.rank + (sdp.dualSlack sc.ystar).rank = n)
    {D : Matrix (Fin n) (Fin n) ℝ}
    (_h_D_sym : D.IsHermitian)
    (_h_S_D : sdp.dualSlack sc.ystar * D = 0)
    (_h_constraint_D : ∀ i : ι, Matrix.trace (sdp.constraint i * D) = 0) :
    D = 0"""),
]
BASE = "folio/quantum-observable-universe/lean/QOU/MathlibExt/"
THRESHOLD = 5


def selftest(rev: str) -> bool:
    """Score the five refuted SDP axioms from embedded text.

    `rev` is accepted and ignored; it remains only so an older invocation does
    not fail on an unknown flag.  The fixtures are embedded precisely because
    reading them from a revision is what broke this self-test the day the
    refutation merged.
    """
    del rev
    ok = True
    for name, text in KNOWN_FALSE_TEXT:
        found = [a for a in axioms_in(text, f"{name}.fixture") if a[0] == name]
        if not found:
            print(f"  SELFTEST FAIL: parser did not find `{name}` in its own fixture",
                  file=sys.stderr)
            ok = False
            continue
        sc, reasons = score(found[0][2])
        mark = "ok " if sc >= THRESHOLD else "FAIL"
        if sc < THRESHOLD:
            ok = False
        print(f"  {mark} {name:<46} score={sc}  {','.join(reasons)}", file=sys.stderr)

    print("  -- over-quantification fixtures (axioms deleted; text from their"
          " post-mortems) --", file=sys.stderr)
    for name, text in OVERQUANT_FIXTURES:
        _, reasons = overquantification_signals(text)
        fired = [r for r in reasons if r.startswith("overquantified:")]
        if not fired:
            print(f"  FAIL {name:<46} no over-quantification signal fired", file=sys.stderr)
            ok = False
        else:
            print(f"  ok  {name:<46} {','.join(fired)}", file=sys.stderr)
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--rev", default="",
                    help="accepted and ignored; the known-false axioms are embedded fixtures")
    ap.add_argument("--root", default="folio")
    ap.add_argument("--top", type=int, default=25)
    args = ap.parse_args()

    print("self-test against the five known-false SDP axioms (embedded fixtures):",
          file=sys.stderr)
    if not selftest(args.rev):
        print("\nSELF-TEST FAILED — the detector no longer flags axioms it is known to need "
              "to flag. Its verdicts are about itself, not the corpus. Aborting.", file=sys.stderr)
        return 2
    print("self-test passed\n", file=sys.stderr)
    if args.selftest:
        return 0

    rows = []
    for p in sorted(pathlib.Path(args.root).rglob("*.lean")):
        # `.lake/packages/` holds vendored Mathlib/Aesop, including their own
        # TEST files, which declare axioms freely. Counting those inflates the
        # corpus total several-fold -- the first run of this audit reported 364
        # axioms and ~40 of the flagged rows were Mathlib test fixtures.
        if ".lake" in p.parts or "SDPUniquenessCounterexamples" in str(p):
            continue
        for name, line, decl, path in axioms_in(p.read_text(errors="replace"), str(p)):
            sc, reasons = score(decl)
            rows.append((sc, path, line, name, reasons))
    rows.sort(key=lambda r: (-r[0], r[1], r[2]))
    flagged = [r for r in rows if r[0] >= THRESHOLD]
    print(f"axioms scanned : {len(rows)}")
    print(f"flagged (>= {THRESHOLD}) : {len(flagged)}")
    print()
    print("These are candidates for a degenerate-instance refutation attempt.")
    print("A high score is NOT evidence of falsity; only a Lean term settles it.")
    print()
    for sc, path, line, name, reasons in flagged[:args.top]:
        print(f"  [{sc}] {name}")
        print(f"       {path}:{line}")
        print(f"       {', '.join(reasons)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
