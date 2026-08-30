#!/usr/bin/env python3
"""Selftest for `lean_decl_scan`.  Every case here is a regression that was
actually hit while unifying the two detectors (bean `qou-rfq9`), not a
hypothetical.  Run: python3 scripts/lib/test_lean_decl_scan.py

Exit 0 = all pass.  Exit 1 = a primitive regressed; DO NOT re-measure detector
counts until this is green, because each failure below silently moves them.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lean_decl_scan import (  # noqa: E402
    blank_comments, split_statement, decl_spans, docstring_before,
    binder_names, assumption_binders, discharges_via_binder_field,
    local_def_names, line_comments_before, line_comments_inside, comment_cone,
)

FAIL = []


def check(name, got, want):
    if got != want:
        FAIL.append(f"{name}\n     got:  {got!r}\n     want: {want!r}")


# --- 1. `end` must close a body -------------------------------------------
# Cost of getting this wrong: 163 findings vanished from one detector and 22
# never appeared in the other, because `:= rfl` read as `rfl\n\nend Foo`.
SRC_END = """\
@[simp] theorem degree_conj (D : Chord n) (g : Perm) :
    (D.conj g).degree = D.degree := rfl

end ChordDiagram

/-! ## next section -/
def later : Nat := 0
"""
spans = list(decl_spans(blank_comments(SRC_END)))
_, _, _, body = spans[0]
check("end closes a body", split_statement(body)[1].strip(), "rfl")

# --- 2. `omit ... in` must close a body ------------------------------------
# Lean 4 per-decl instance suppression sits at column 0 immediately BEFORE the
# declaration it modifies, so it lands inside the PRECEDING decl's body.
SRC_OMIT = """\
@[simp] theorem gram_apply (tau : A) (b : I) (i j : I) :
    gram tau b i j = tau (b i * b j) := rfl

omit [IsDomain R] [Fintype I] in
@[simp] theorem other : True := trivial
"""
_, _, _, body = list(decl_spans(blank_comments(SRC_OMIT)))[0]
check("omit-in closes a body", split_statement(body)[1].strip(), "rfl")

# --- 3. a decl quoted inside a docstring is NOT a decl ----------------------
# Real instance: `blochWignerD_real_pos` is quoted in a module docstring
# recording that it was REMOVED for being a banned tautology.  Unblanked, the
# detector flagged a theorem that no longer exists.
SRC_QUOTED = '''\
/-! ## Removed 2026-08-07

    theorem blochWignerD_real_pos (q n) : blochWignerD q n = 0 := rfl

which is the banned tautology pattern. -/
def real_one : Nat := 1
'''
names = [n for k, n, _, _ in decl_spans(blank_comments(SRC_QUOTED))]
check("docstring-quoted decl is skipped", names, ["real_one"])

# --- 4. comments between a name and its statement -------------------------
# `b3_nf_wedderburn_uniqueness` carries three comment lines inside the
# declaration; without blanking the collapse test cannot see `:= ...`.
SRC_INLINE = """\
theorem b3_nf_wedderburn_uniqueness :
    -- Stated as: the NF basis reconstruction matches our coefficients.
    -- Full proof requires Wedderburn-Artin over R_q.
    b3_nf_coefficients 5 = 0 :=
  -- e- = 0 follows as the key consequence.
  rfl
"""
_, _, _, body = list(decl_spans(blank_comments(SRC_INLINE)))[0]
check("inline comments blanked", split_statement(body)[1].strip(), "rfl")

# --- 5. binder forms ------------------------------------------------------
# NOTE an ANONYMOUS instance binder `[Field R]` has no `name :` and so
# contributes NO binder name -- `Field` is the class, `R` its argument.  Only a
# NAMED instance binder `[inst : Field R]` yields one.  That is correct and not
# a gap: with an anonymous instance a proof writes `Field.rule`, a foreign
# constant, which the borrowed-name detector's LOCAL-ONLY signal already
# handles.  (This test asserted `Field` was a binder name and was wrong.)
STMT = "theorem t (a b : R) {A : Nat} [Field R] (hA : A < 4) : foo a A "
check("binder_names covers named binders in all brackets",
      binder_names(STMT), {"a", "b", "A", "hA"})
check("anonymous instance binder yields no name",
      binder_names("theorem t [Field R] : True "), set())
check("named instance binder yields its name",
      binder_names("theorem t [inst : Field R] : True "), {"inst"})

# --- 6. the exclusion must not fire on dot-notation over a VALUE binder ----
# `mu4_unconstrained_below_four` has `{A : Nat}` and uses `A.choose 4`.  With
# every binder in scope the exclusion suppressed it -- the right outcome for
# the wrong reason, and over-suppression everywhere else.
check("assumption_binders excludes value binders",
      assumption_binders(STMT), {"hA"})
check("no false exclusion on A.choose",
      discharges_via_binder_field("by simp [A.choose 4]", assumption_binders(STMT)),
      False)
check("real exclusion fires on a named instance's field",
      discharges_via_binder_field(
          "by exact inst.rule x",
          assumption_binders("theorem t [inst : Field R] (hA : 0 < n) : True ")),
      True)
check("real exclusion fires on a hypothesis's field",
      discharges_via_binder_field("by exact hA.left", assumption_binders(STMT)),
      True)

# --- 7. split_statement is bracket-aware ----------------------------------
# A naive split at the first `:=` breaks on a structure literal in the
# STATEMENT.  `helium4_lp_reduction`'s neighbours in that file have this shape.
check("split_statement ignores := inside brackets",
      split_statement("theorem t : f { x := 1 } = g := rfl")[1].strip(), "rfl")

# --- 8. opaque/axiom are not local defs -----------------------------------
check("local_def_names takes def/abbrev only",
      local_def_names("def a : Nat := 0\nopaque b : Nat\naxiom c : True\nabbrev d := a\n"),
      {"a", "d"})

# --- 9. docstring lookup survives a `-- Ref:` line -------------------------
SRC_REF = """\
/-- **A theorem.** Does a thing. -/
-- Ref: [manuscript] prop:foo
theorem t : True := trivial
"""
lines = SRC_REF.split("\n")
kind, name, line_no, _ = list(decl_spans(blank_comments(SRC_REF)))[0]
check("docstring found across a Ref line",
      "**A theorem.**" in docstring_before(lines, line_no), True)

# --- 10-12. the comment cone (bean `qou-rfq9`, 2026-08-30) ------------------
# `docstring_before` deliberately SKIPS `--` lines, so prose written there is
# invisible to it.  Modelled on `b3_nf_wedderburn_uniqueness`, whose docstring
# says "PROVED CORRECT" while its own `--` comments say the proof is not there.
SRC_CONE = """\
/-- The coefficients are PROVED CORRECT. -/
-- Ref: [jones1987]
-- The formal proof needs: Wedderburn for finite-dim algebras.
theorem b3_uniqueness :
    -- Full proof requires Wedderburn-Artin over R_q.
    coeffs 5 = 0 :=
  rfl
"""
lines = SRC_CONE.split("\n")
kind, name, line_no, chunk = list(decl_spans(blank_comments(SRC_CONE)))[0]
span = chunk.count("\n") + 1

check("docstring alone does NOT see the -- admission",
      "formal proof needs" in docstring_before(lines, line_no), False)
check("line_comments_before reads the -- block above",
      "formal proof needs" in line_comments_before(lines, line_no), True)
check("line_comments_inside reads -- inside the statement",
      "Full proof requires" in line_comments_inside(lines, line_no, span), True)

cone = comment_cone(lines, line_no, span)
check("cone carries all three sources",
      ("PROVED CORRECT" in cone, "formal proof needs" in cone,
       "Full proof requires" in cone), (True, True, True))

# The walk upward must stop at a preceding declaration, never reach over it.
SRC_STOP = """\
def earlier : Nat := 0
-- a comment about `later`
theorem later : True := trivial
"""
lines2 = SRC_STOP.split("\n")
_, _, ln2, _ = [d for d in decl_spans(blank_comments(SRC_STOP)) if d[1] == "later"][0]
check("comment walk stops at the previous decl",
      "earlier" in line_comments_before(lines2, ln2), False)


if FAIL:
    print(f"FAIL ({len(FAIL)}):")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("lean_decl_scan selftest OK (17 regression cases, incl. the comment cone)")
