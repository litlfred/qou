#!/usr/bin/env python3
"""Detect the "∀-bound constant" vacuity class.

    axiom f : ∀ … (z : T) …, LHS = RHS

where `z` occurs on exactly one side of the equation and is otherwise
unconstrained (does not appear in any hypothesis). Such a statement forces the
*other* side to be independent of `z` — and when that side is a product
containing `z`, it forces it to zero.

Why this class needs its own detector
-------------------------------------
It is invisible to every existing audit: there is no `sorry`, no `True`
conclusion, no `native_decide`, and `#print axioms` looks completely normal.
The declaration is well-typed and reads like a real theorem. Two live instances
were found on 2026-08-08 by reading a single file:

  QOU/HeckeAlgebra/MarkovTrace.lean
    MarkovTrace_markov_axiom : ∀ … (z : ℝ), markovTrace (n+1) (heckeStab x)
                                              = z * markovTrace n x
      z := 0 and z := 1 together give `markovTrace n x = 0` for every x, i.e.
      the Markov trace — the central object of the mass chain — was pinned to
      the zero function.

    wenzlBridge : ∀ … (q : ℝ) …, markovTraceOnWedderburn x = ∑ … y_λ(q) · …
      the left side does not mention q, so the weighted block-sum was provably
      q-independent — the negation of what the Wenzl bridge exists to say.

  QOU/Archimedean/WeierstrassProjection.lean
    weierstrass_diff_eq_axiom — a variant of the same failure: an existential
      over free complex numbers that never mentions `weierstrassProjection`,
      making the "axiom" a provable triviality of ℂ.

Reading the output
------------------
This is a HIGH-RECALL candidate detector, agent-confirmed like the other
vacuity classes. Triage rules:

  * RHS-only is the dangerous direction. LHS-only is usually fine — `f n = 1`
    genuinely depends on n and equals 1 for each n.
  * A *proved* theorem cannot collapse anything: it is true. Only `axiom`s and
    `sorry`-ed theorems can assert a falsehood, so those are reported first.
  * A variable that also appears in a hypothesis is constrained and is normally
    a false positive; those are filtered out by default (--include-constrained
    to see them).

Usage:
    scripts/lean-one-sided-binder-audit.py [ROOT] [--include-constrained] [--all-kinds]
"""
from __future__ import annotations

import pathlib
import re
import sys

DEFAULT_ROOT = "content/quantum-observable-universe/lean/QOU"


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


def split_top_level_eq(body: str):
    """Split on the top-level '=', skipping '==', '=>', '<=', '>=', ':='."""
    depth = 0
    for i, c in enumerate(body):
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == "=" and depth == 0:
            if body[i - 1:i] in ("<", ">", "!", ":", "=") or body[i + 1:i + 2] in ("=", ">"):
                continue
            return body[:i], body[i + 1:]
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
    for p in sorted(root.rglob("*.lean")):
        src = p.read_text(encoding="utf-8", errors="replace")
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
            mm = re.search(r"∀([^,]*),(.*)", stmt, re.S)
            if not mm:
                continue
            binders, body = mm.group(1), mm.group(2)
            hyps, concl = split_hypotheses(body)
            eq = split_top_level_eq(concl)
            if not eq:
                continue
            lhs, rhs = eq
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
            for var, implicit in binder_names(binders):
                if implicit or len(var) > 3:
                    continue
                in_l, in_r = occurs(var, lhs), occurs(var, rhs)
                if in_l == in_r:
                    continue
                constrained = occurs(var, hyp_text)
                if constrained and not include_constrained:
                    continue
                findings.append(
                    {
                        "file": str(p),
                        "kind": kind,
                        "name": name,
                        "var": var,
                        "side": "RHS only" if in_r else "LHS only",
                        "unproved": unproved,
                        "constrained": constrained,
                    }
                )
    return findings


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
}


def self_test() -> int:
    import tempfile

    failures = []
    with tempfile.TemporaryDirectory() as td:
        for label, src in SELF_TEST.items():
            d = pathlib.Path(td) / label
            d.mkdir()
            (d / "T.lean").write_text(src, encoding="utf-8")
            hits = [f for f in scan(d, False, False) if f["side"] == "RHS only" and f["unproved"]]
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

    findings = scan(root, include_constrained, all_kinds)
    hi = [f for f in findings if f["side"] == "RHS only" and f["unproved"]]
    lo = [f for f in findings if f not in hi]

    print(f"one-sided-binder candidates: {len(findings)}  "
          f"({len(hi)} high-priority, {len(lo)} lower)\n")

    if hi:
        print("HIGH — unproved, variable on RHS only, unconstrained by hypotheses")
        print("       (this is the shape that collapsed tr_M to zero)\n")
        for f in hi:
            print(f"  {f['file']}")
            print(f"      {f['kind']} {f['name']}  --  '{f['var']}' {f['side']}")
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
