#!/usr/bin/env python3
"""Detect statements that quantify over what was meant to be a fixed constant.

Two signals, of very different severity.

UNSOUND — a whole side of an ORDER relation is a bare, unconstrained binder
----------------------------------------------------------------------------
    axiom f (n : ℕ) (p q : Prop) : p → q → 3 ≤ n

`n` is universally quantified, so this asserts `3 ≤ n` for **every** `n`.
Instantiate at `n = 0` with both `Prop`s taken to be `True` and you have
`3 ≤ 0`, hence `False`. This does not merely say nothing — it makes the whole
import cone unsound.

Live case, fixed 2026-08-08:
`QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean::b1_hyperbolic_rows`, which
was verbatim the shape above. `False` was provable anywhere downstream of
`QOU.AppendixSurreals`, with `#print axioms` naming it as the sole culprit.

COLLAPSE — a short-named binder on one side of an `=`
-----------------------------------------------------
    axiom f : ∀ … (z : T) …, LHS = RHS

with `z` on exactly one side and unconstrained elsewhere. This forces the
other side to be independent of `z` — and when that side is a product
containing `z`, it forces it to zero. Live cases, both fixed 2026-08-08 in
`QOU/HeckeAlgebra/MarkovTrace.lean`:

  MarkovTrace_markov_axiom — `markovTrace (n+1) (heckeStab x) = z * markovTrace n x`
    with `z` bound. `z := 0` and `z := 1` together give `markovTrace n x = 0`
    for every `x`: the Markov trace, the central object of the mass chain, was
    pinned to the zero function.

  wenzlBridge — the left side does not mention `q`, so the weighted block-sum
    was provably `q`-independent, which is the negation of what the Wenzl
    bridge exists to say.

Why these need their own detector
---------------------------------
They are invisible to every existing audit: no `sorry`, no `True` conclusion,
no `native_decide`, and `#print axioms` looks entirely normal. The declaration
is well-typed and reads like a real theorem.

Reading the output
------------------
HIGH-RECALL candidates, agent-confirmed like the other vacuity classes:

  * UNSOUND hits are not candidates — fix them immediately.
  * For COLLAPSE, RHS-only is the dangerous direction. LHS-only is usually
    fine: `f n = 1` genuinely depends on `n` and equals `1` for each.
  * A *proved* theorem cannot collapse anything — it is true. Only `axiom`s and
    `sorry`-ed theorems can assert a falsehood.
  * A binder appearing in a hypothesis is constrained, and normally a false
    positive; filtered out by default (`--include-constrained` to see them).

Three parsing details that each hid a real defect until fixed, worth
preserving if this is ever rewritten:

  1. Comments must be stripped first, or a docstring quoting a declaration —
     including this repo's own write-up of the B1 fix — is read as source.
  2. Both binder forms must be handled: `axiom f : ∀ (n : ℕ), …` *and*
     `axiom f (n : ℕ) : …`. B1 used the second, so a `∀`-only regex skipped
     the only unsound file in the corpus.
  3. The length cap on binder names applies to COLLAPSE only. The unsound
     binder was `n_hyperbolic_rows_verified`; a cap tuned for `z`/`q` hid it.

Usage:
    scripts/lean-one-sided-binder-audit.py [ROOT] [--include-constrained] [--all-kinds]
    scripts/lean-one-sided-binder-audit.py --self-test
"""
from __future__ import annotations

import pathlib
import re
import sys

DEFAULT_ROOT = "folio/quantum-observable-universe/lean/QOU"


def binder_names(sig: str) -> list[tuple[str, bool]]:
    """(name, is_implicit) for each binder group in a signature fragment."""
    out: list[tuple[str, bool]] = []
    for m in re.finditer(r"([(\[{])\s*([A-Za-z0-9_'’ ]+?)\s*:\s*[^)\]}]+?[)\]}]", sig):
        implicit = m.group(1) != "("
        for n in m.group(2).split():
            out.append((n, implicit))
    return out


def occurs(var: str, text: str) -> bool:
    return re.search(rf"(?<![A-Za-z0-9_'])" + re.escape(var) + r"(?![A-Za-z0-9_'])", text) is not None


# Order-relation glyphs are as dangerous as `=` here, and in a nastier way: a
# one-sided `=` collapses the other side to a constant, but a one-sided `≤`
# over an unconstrained numeric binder is outright INCONSISTENT. Live case
# (fixed 2026-08-08, `QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean`):
#
#     axiom b1_hyperbolic_rows (n : ℕ) (bloch_suslin van_der_veen : Prop) :
#         bloch_suslin → van_der_veen → 3 ≤ n
#
# `n` is universally quantified, so this asserts `3 ≤ n` for every `n`.
# Instantiating at `n = 0` with both Props `True` proves `3 ≤ 0`, hence `False`
# — the whole import cone of `QOU.AppendixSurreals` was unsound.
RELATIONS = ["≤", "≥", "<", ">", "="]


def split_top_level_eq(body: str):
    """Split on the first top-level relation, skipping '==', '=>', ':=', '<='/'>='
    written ASCII-style (those are single glyphs in Lean, handled separately)."""
    depth = 0
    for i, c in enumerate(body):
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif depth == 0 and c in RELATIONS:
            if c == "=":
                if body[i - 1:i] in ("<", ">", "!", ":", "=") or body[i + 1:i + 2] in ("=", ">"):
                    continue
            # `<`/`>` are also used in Lean for universe/instance brackets and
            # anonymous constructors; require surrounding whitespace so `⟨a, b⟩`
            # and `Foo<T>`-style noise do not split.
            elif c in ("<", ">") and not (
                body[i - 1:i].isspace() and body[i + 1:i + 2].isspace()
            ):
                continue
            return body[:i], body[i + 1:], c
    return None


def strip_comments(src: str) -> str:
    """Blank out `/- … -/` blocks and `--` line comments, preserving line count.

    Without this the scanner reads *prose* as source. Two ways that bites:
    a module docstring quoting a declaration in a ```lean fence (this file's
    own B1 write-up quotes the very axiom it documents fixing), and ordinary
    paragraph text that happens to wrap onto a line starting with `axiom`.
    Both produce confident false positives.
    """
    out, i, depth = [], 0, 0
    while i < len(src):
        if src.startswith("/-", i):
            depth += 1
            i += 2
            continue
        if src.startswith("-/", i) and depth:
            depth -= 1
            i += 2
            continue
        if depth == 0 and src.startswith("--", i):
            j = src.find("\n", i)
            i = len(src) if j < 0 else j
            continue
        ch = src[i]
        out.append(ch if depth == 0 else ("\n" if ch == "\n" else " "))
        i += 1
    return "".join(out)


def split_on_top_level_colon(stmt: str):
    """Split `(binders…) : body` on the top-level `:` (depth 0, not `:=`).

    For the binders-before-the-colon declaration form. Returns None if there
    is no top-level colon (a declaration with no explicit binders)."""
    depth = 0
    for i, c in enumerate(stmt):
        if c in "([{⦃":
            depth += 1
        elif c in ")]}⦄":
            depth -= 1
        elif c == ":" and depth == 0:
            if stmt[i + 1:i + 2] in ("=", ":") or stmt[i - 1:i] == ":":
                continue
            return stmt[:i], stmt[i + 1:]
    return None


def split_hypotheses(body: str):
    """Split a body into (hypotheses, conclusion) on top-level '→'."""
    parts, depth, cur = [], 0, ""
    i = 0
    while i < len(body):
        c = body[i]
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        if depth == 0 and body[i:i + 1] == "→":
            parts.append(cur)
            cur = ""
            i += 1
            continue
        cur += c
        i += 1
    parts.append(cur)
    return parts[:-1], parts[-1]


def scan(root: pathlib.Path, include_constrained: bool, all_kinds: bool):
    findings = []
    scanned = 0
    # A ROOT MAY BE A SINGLE FILE (see lean-self-assuming-audit.py). This one
    # was the worst of the three: it printed no scanned-file count at all, so
    # `<script> path/to/One.lean` reported "0 candidates", exited 0, and left
    # nothing in the output to reveal that nothing had been read.
    cands = [root] if (root.is_file() and root.suffix == ".lean") else root.rglob("*.lean")
    for p in sorted(cands):
        scanned += 1
        src = strip_comments(p.read_text(encoding="utf-8", errors="replace"))
        for m in re.finditer(
            r"^(axiom|theorem|lemma)\s+([A-Za-z0-9_.']+)\s*((?:[^\n]|\n[ \t]+)*)", src, re.M
        ):
            kind, name, rest = m.group(1), m.group(2), m.group(3)
            proved = ":=" in rest or re.search(r"\bby\b", rest) is not None
            has_sorry = "sorry" in rest
            if kind == "axiom":
                unproved = True
            else:
                unproved = has_sorry or not proved
            if not all_kinds and not unproved:
                continue
            stmt = rest.split(":=")[0]
            # Two binder forms, and missing the second one hid the only UNSOUND
            # case in the corpus. Lean lets you write either
            #
            #     axiom f : ∀ (n : ℕ), 3 ≤ n          -- ∀ form
            #     axiom f (n : ℕ) : 3 ≤ n             -- binders before the colon
            #
            # and `b1_hyperbolic_rows` used the latter, so a `∀`-only regex
            # skipped the file outright. Both are universally quantified and
            # both are equally dangerous.
            mm = re.search(r"∀([^,]*),(.*)", stmt, re.S)
            if mm:
                binders, body = mm.group(1), mm.group(2)
            else:
                split = split_on_top_level_colon(stmt)
                if not split:
                    continue
                binders, body = split
            hyps, concl = split_hypotheses(body)
            eq = split_top_level_eq(concl)
            if not eq:
                continue
            lhs, rhs = eq[0], eq[1]
            # A variable is "constrained" if it appears anywhere other than the
            # conclusion's two sides: in a `→` antecedent, OR in the *type* of
            # another binder (the `(_h : … sc.Φstar)` shape, which is how most
            # hypotheses are actually written and which a `→`-only split
            # misses — that omission made `strict_complementarity_unique_axiom`
            # report as a false HIGH).
            binder_types = " ".join(
                m.group(1) for m in re.finditer(r"[(\[{][^:()\[\]{}]*:([^)\]}]*)[)\]}]", binders)
            )
            hyp_text = " ".join(hyps) + " " + binder_types
            rel = eq[2] if len(eq) > 2 else "="
            for var, implicit in binder_names(binders):
                if implicit:
                    continue
                in_l, in_r = occurs(var, lhs), occurs(var, rhs)
                if in_l == in_r:
                    continue
                constrained = occurs(var, hyp_text)
                if constrained and not include_constrained:
                    continue

                # Signal B — UNSOUND. One whole side of an ORDER relation is a
                # bare unconstrained variable (`3 ≤ n`), so the statement is
                # asserted for every value of it, including ones that falsify
                # it. This proves `False`, not merely nothing. Any identifier
                # length; the live case was `n_hyperbolic_rows_verified`.
                bare_side = (rhs if in_r else lhs).strip()
                if rel in ("≤", "≥", "<", ">") and bare_side == var:
                    findings.append({
                        "file": str(p), "kind": kind, "name": name, "var": var,
                        "side": f"whole {'RHS' if in_r else 'LHS'} of `{rel}`",
                        "unproved": unproved, "constrained": constrained,
                        "signal": "unsound-order-bound",
                    })
                    continue

                # Signal C — UNCONSTRAINED PROJECTION. The conclusion relates
                # field projections of a universally-quantified structure that
                # no hypothesis constrains. If those fields are independent,
                # the statement asserts a relation between arbitrary values.
                #
                # This is how the SECOND inconsistency got in, and signal B
                # does not see it (the relation is `=`, and neither side is a
                # bare variable):
                #
                #   structure OperatorSelectionLP where
                #     primal_obj : ℝ ;  dual_obj : ℝ  -- independent, arbitrary
                #   def duality_gap lp := |lp.primal_obj - lp.dual_obj|
                #   axiom schrijver_strong_duality : ∀ lp, lp.duality_gap = 0
                #
                # i.e. "any two reals are equal". Live in
                # QOU/BraidKnot/LpDualityHypothesisClass.lean until 2026-08-08;
                # its sibling `schrijver_complementary_slackness` was
                # separately inconsistent the same way.
                #
                # Reported as ADVISORY, not UNSOUND: whether it is fatal
                # depends on whether the projected fields are genuinely
                # independent, which is a question about the structure and
                # needs a human. The signal is "an unconditional claim about
                # an arbitrary structure" — always worth a second look.
                if (
                    not hyps
                    and rel is not None
                    and occurs(var, lhs + rhs)
                    and re.search(rf"(?<![A-Za-z0-9_']){re.escape(var)}\.", lhs + rhs)
                ):
                    findings.append({
                        "file": str(p), "kind": kind, "name": name, "var": var,
                        "side": f"projections of `{var}` related by `{rel}`, no hypotheses",
                        "unproved": unproved, "constrained": constrained,
                        "signal": "unconstrained-structure-projection",
                    })
                    continue

                # Signal A — COLLAPSE. A variable on one side of an `=` forces
                # the other side to be independent of it. Restricted to short
                # names: a long descriptive identifier on one side of an
                # equation is usually the subject of a real definition, whereas
                # the collapse cases are scalar constants (`z`, `q`). Order
                # relations are handled by signal B above; `0 < f lam` is a
                # perfectly normal statement and must not be reported here.
                if rel != "=" or len(var) > 3:
                    continue
                findings.append({
                    "file": str(p), "kind": kind, "name": name, "var": var,
                    "side": "RHS only" if in_r else "LHS only",
                    "unproved": unproved, "constrained": constrained,
                    "signal": "one-sided-constant",
                })
    return findings, scanned


# The two real defects this detector was written from, plus the false positive
# that an earlier revision reported as HIGH. Guards the detector against
# silently rotting into a no-op (or back into noise).
SELF_TEST = {
    "must_flag_markov": """
axiom MarkovTrace_markov_axiom :
    ∀ {n : ℕ} (x : HeckeElement n) (z : ℝ),
    markovTrace (n + 1) (heckeStab x) = z * markovTrace n x
""",
    "must_flag_wenzl": """
axiom wenzlBridge :
    ∀ {n : ℕ} (q : ℝ) (x : WedderburnDecomposition n),
    markovTraceOnWedderburn x =
      ∑ lam ∈ partitions_as_finset n, JonesMarkovCoefficient lam q * (x lam).trace
""",
    "must_not_flag_constrained_binder": """
axiom strict_complementarity_unique_axiom :
    ∀ {n : ℕ} {sdp : SDPPrimal n R ι}
      (sc : StrictComplementarityPair sdp)
      {Φ' : Matrix (Fin n) (Fin n) R}
      (_h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar),
        Φ' = sc.Φstar
""",
    "must_not_flag_lhs_only": """
axiom JonesMarkovCoefficient_sum_eq_one :
    ∀ (n : ℕ) (q : ℝ),
    (∑ lam ∈ partitions_as_finset n, JonesMarkovCoefficient lam q) = 1
""",
    # The inconsistency case: a one-sided `≤` over an unconstrained numeric
    # binder is not merely vacuous, it proves `False`.
    "must_flag_b1_inequality": """
axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : ℕ)
    (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified
""",
    # The second inconsistency: a relation between independent projections of
    # an unconstrained structure. Signal B cannot see this one.
    "must_flag_lp_projection": """
axiom schrijver_strong_duality :
    ∀ (lp : OperatorSelectionLP), lp.duality_gap = 0
""",
}


def self_test() -> int:
    import tempfile

    failures = []
    with tempfile.TemporaryDirectory() as td:
        for label, src in SELF_TEST.items():
            d = pathlib.Path(td) / label
            d.mkdir()
            (d / "T.lean").write_text(src, encoding="utf-8")
            hits = [
                f for f in scan(d, False, False)
                if f["unproved"]
                and (f["signal"] in ("unsound-order-bound",
                                     "unconstrained-structure-projection")
                     or f["side"] == "RHS only")
            ]
            want = label.startswith("must_flag")
            got = bool(hits)
            status = "ok" if got == want else "FAIL"
            if status == "FAIL":
                failures.append(label)
            print(f"  [{status}] {label}: expected flagged={want}, got={got}")
    if failures:
        print(f"\nself-test FAILED: {', '.join(failures)}")
        return 1
    print("\nself-test passed")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:]]
    if "--self-test" in args:
        return self_test()
    include_constrained = "--include-constrained" in args
    all_kinds = "--all-kinds" in args
    positional = [a for a in args if not a.startswith("--")]
    root = pathlib.Path(positional[0] if positional else DEFAULT_ROOT)
    if not root.exists():
        print(f"error: {root} does not exist", file=sys.stderr)
        return 2

    findings, scanned = scan(root, include_constrained, all_kinds)
    print(f"scanned {scanned} .lean files")
    if scanned == 0:
        print("error: scanned 0 .lean files — this is NOT a pass. Nothing was "
              "audited; check the root given.", file=sys.stderr)
        return 2
    unsound = [f for f in findings if f["signal"] == "unsound-order-bound"]
    advisory = [f for f in findings
                if f["signal"] == "unconstrained-structure-projection"]
    hi = [f for f in findings
          if f["signal"] == "one-sided-constant" and f["side"] == "RHS only" and f["unproved"]]
    lo = [f for f in findings if f not in hi and f not in unsound and f not in advisory]

    print(f"one-sided-binder candidates: {len(findings)}  "
          f"({len(unsound)} UNSOUND, {len(advisory)} advisory, "
          f"{len(hi)} high-priority, {len(lo)} lower)\n")

    if unsound:
        print("UNSOUND — a whole side of an order relation is a bare, unconstrained")
        print("          binder. This proves False, not merely nothing. FIX IMMEDIATELY.\n")
        for f in unsound:
            print(f"  {f['file']}")
            print(f"      {f['kind']} {f['name']}  --  '{f['var']}' is the {f['side']}")
        print()

    if hi:
        print("HIGH — unproved, variable on RHS only, unconstrained by hypotheses")
        print("       (this is the shape that collapsed tr_M to zero)\n")
        for f in hi:
            print(f"  {f['file']}")
            print(f"      {f['kind']} {f['name']}  --  '{f['var']}' {f['side']}")
        print()

    if advisory:
        print("ADVISORY — unconditional claim relating projections of an arbitrary")
        print("           structure. Fatal iff those fields are independent — check.\n")
        for f in advisory:
            print(f"  {f['file']}")
            print(f"      {f['kind']} {f['name']}  --  {f['side']}")
        print()

    if lo:
        print("LOWER — LHS-only (usually fine) and/or already proved (cannot be false)\n")
        for f in lo:
            tag = "proved" if not f["unproved"] else "unproved"
            print(f"  {f['file']}")
            print(f"      {f['kind']} {f['name']}  --  '{f['var']}' {f['side']}  [{tag}]")

    # Advisory only: every hit needs an agent to read the declaration.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
