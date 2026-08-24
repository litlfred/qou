---
# qou-omiu
title: 'check-sidecars JUST regex: bare ≤/≥ make ℕ index comparisons read as archimedean (§7c false positive)'
status: todo
type: bug
priority: normal
created_at: 2026-08-23T21:56:07Z
updated_at: 2026-08-24T13:21:54Z
---

FOUND while my own new Lean file took a §7c MIXED advisory it does not deserve.

    content/quantum-observable-universe/lean/QOU/MathlibExt/MarkovUnusedGenerator.lean
      [WARN §7c MIXED generic + archimedean -> split into two files per §7c]
         25:  far_comm : forall i j : N, i + 2 <= j -> sigma i * sigma j = sigma j * sigma i
         85:      by_cases hfar : g + 2 <= m

Both are orderings on N -- GENERATOR INDICES in a Hecke tower. The file has no
R anywhere, its base is a generic [CommRing R], and #print axioms is clean on
every declaration. AGENTS.md 7c is about the BASE RING ("ordering predicates
(0 < q, q < 1)"); N index order is not archimedean content and cannot be
removed -- a tower indexed by N needs it.

THE CAUSE IS AN INTERNAL INCONSISTENCY IN THE REGEX, not a judgement call.
scripts/check-sidecars.sh, the JUST marker:

    ...|0\s*<|<\s*1|<=|>=|\blinarith\b|...
           ^^^^^^^^^^^^^  ^^^^^
           < only in its   <= and >= listed BARE
           typed shapes

So `<` counts only as `0 <` or `< 1` -- a bound on a ring element -- while any
`<=` at all counts. That is the same class as the `norm_num` false positive the
file's own NOTE (bean qou-akb4, class 1) already removed: "a token that does
not cross the substrate->archimedean wall listed as a marker that it does".

I TRIED THE OBVIOUS FIX AND BACKED IT OUT. Narrowing `<=`/`>=` to `0 <=`,
`<= 1`, `0 >=`, `>= 1` -- matching how `<` is already handled -- does fix my
file, and I verified it in both directions on a constructed test (genuine
`0 <= q` + Real.sqrt still caught; ring bounds `0 <= q` and `q <= 1` still
caught; my N-indexed file clean).

THEN I MEASURED THE BLAST RADIUS, AND IT IS TOO BIG:

    library Lean files scanned            2086
    reclassified archimedean -> generic    252
      ...of which still mention R/Real.     98   <-- the risky ones

Spot-checked one: QOU/Infra/DirichletL.lean is
`noncomputable def lValueAxiomatic (K : N) (chi : N -> R) (_n : N) : R` --
genuinely real-valued, and my narrowing moves it out of the archimedean class.
Reverted. A 252-file reclassification is not a side-effect to land while fixing
one advisory on my own file, and 98 R-touching files is too many to reason
about loosely.

WHAT THE OWNER OF THIS CHECKER SHOULD DECIDE. The narrowing is probably right in
principle -- it is what the regex evidently intended, since `<` is already
handled that way -- but it needs the 98 adjudicated, not a spot check. Possible
routes: (a) narrow as above and walk the 98; (b) keep `<=`/`>=` bare but skip
them when both operands are N-typed (hard for a grep-based checker); (c) leave
it and accept the false positives on N-indexed files.

MEANWHILE, for anyone who hits this: a §7c MIXED advisory on a file whose only
`<=` are over N is a FALSE POSITIVE. Check the base ring before splitting a
file on its say-so -- the prescribed remedy ("split into two files") would be
actively wrong here.

A SECOND, SEPARATE GAP found in the same pass (this one belongs to
canonical_mass_status_guard, not check-sidecars): it excludes probe-class files
by DIRECTORY (probes/, audits/, sweeps/) and by NAME PREFIX (probe_, audit_,
sweep_), but 226 top-level computations/*.py carry those words as a SUFFIX
(*_probe.py, *_test.py) and escape both rules. Only 1 trips the guard today, so
the class is latent rather than live -- but it is luck, not design. Which
suffixes to exclude is that guard's owner's call: `_probe.py` is unambiguously
the excluded class, `_test.py` is not (a real unit test SHOULD be guarded).


§7c HALF CLOSED 2026-08-24 -- FIXED ON MAIN BY A SIBLING, AND THEIR FIX IS
STRICTLY BETTER THAN THE ONE I REVERTED.

main's 31fc4481cd "fix(check-sidecars): §7c was flagging the files that comply
with it" solves it at the LOGIC level rather than the regex level:

    STRONG = Real.(sqrt|rpow|...)|linarith|positivity|nlinarith|LinearOrdered|CODATA|MeV
    WEAK   = 0\s*<|<\s*1|≤|≥
    RTYPE  = :\s*ℝ|\(ℝ\)|→\s*ℝ|ℝ\s*\)
    hasJ = hasS OR (hasW AND hasR)

i.e. a WEAK marker counts as archimedean ONLY IF the file actually uses ℝ as a
type. That is exactly the distinction my measurement said was missing, and it is
the right rule: `≤` on a ring element is archimedean, `≤` on a ℕ index is not,
and the presence of ℝ is what separates them.

MEASURED THEIR FIX AGAINST MINE over 2129 library Lean files:

    classified archimedean, OLD logic : 1381   (over-broad; the false positives)
    classified archimedean, MAIN's fix:  943
    classified archimedean, MY revert  : 1119

MY APPROACH WAS WRONG IN BOTH DIRECTIONS, and the numbers say so:

  * 45 files main correctly KEEPS archimedean would have been DROPPED by mine
    -- including Infra/DirichletL.lean, the exact file I spot-checked before
    reverting. My spot check found the problem; the full count shows it was 45
    files, not one.
  * mine also KEPT 438 files main correctly drops -- files with `0 <` or `< 1`
    on a ℕ and no ℝ anywhere. My regex kept those two shapes unconditionally.

So reverting was right, and not merely cautious: the fix I nearly shipped was a
regex-level approximation that both over- and under-classified. The lesson
stands and is sharper than I first wrote it -- MEASURE THE RECLASSIFICATION,
and prefer fixing the LOGIC over narrowing a PATTERN when the pattern's meaning
depends on context the pattern cannot see.

Verified live: my own MarkovUnusedGenerator.lean (ℕ-indexed, generic
[CommRing R], no ℝ) now reports "[library Lean — no ℝ, generic OK]" under
main's rule, and check-sidecars reports no §7c flags.

STILL OPEN in this bean: the SECOND finding, untouched by 31fc4481cd --
canonical_mass_status_guard excludes probe-class files by DIRECTORY (probes/,
audits/, sweeps/) and by NAME PREFIX (probe_, audit_, sweep_), but 226
top-level computations/*.py carry those words as a SUFFIX (*_probe.py,
*_test.py) and escape both rules. Only 1 tripped when measured, so the class is
latent rather than live. Which suffixes to exclude is that guard owner's call:
`_probe.py` is unambiguously the excluded class, `_test.py` is not -- a real
unit test SHOULD be guarded.


## 2026-08-24 — the suffix half is MEASURED, and the implied fix is WRONG. Do not widen the exclusion.

I recorded this as "226 top-level `computations/*.py` carry probe/audit/sweep words
as a SUFFIX and escape both rules", with the implied fix being to add the suffixes
to `PY_EXCLUDED_NAME_PREFIXES`' mirror. **Measured, that fix is a bad trade.**

### The count was low, and that makes it worse, not better

226 was top-level only. Across the guard's real recursive scan surface:

    currently SCANNED                : 2790
    excluded by directory            :  829
    excluded by name prefix          :   64
    of the SCANNED, suffix-class     :  742   <- 26.6% of the scanned surface

So widening would drop **26.6% of everything the guard looks at**.

### What that 26.6% would buy: nothing. Measured.

The decisive test is not "how many files escape" but "is the exclusion mechanism
load-bearing". Ran the guard with `PY_EXCLUDED_DIR_PARTS` and
`PY_EXCLUDED_NAME_PREFIXES` neutralised. **11 hits appear, and every single one is
in an ALREADY-EXCLUDED location:**

    computations/audit_delta_S_chain.py:26,27          <- audit_ prefix
    computations/probes/gap_a4_T4_..._perknot_rerun.py:17    <- probes/ dir
    computations/probes/per_knot_density_borromean_q_locality_probe.py:7,116,117
    computations/probes/rho_k_h3a_co_casimir_perknot_rerun.py:24
    computations/probes/vol_density_borromean_q_locality_probe.py:7,91,92
    computations/sweeps/mass_table_bring_phi_q_h4_sweep.py:9 <- sweeps/ dir

**Zero** are suffix-named files in the scanned surface. The existing exclusions ARE
load-bearing — they suppress 11 genuine would-be false positives — but the 742
suffix-class files cite no deprecated figure at all.

Note the sharpening: several of those hits DO end in `_probe.py`
(`..._q_locality_probe.py`). They are already excluded **by directory**, so a suffix
rule adds nothing for them. It would only remove coverage from top-level files,
none of which cite anything.

### Verdict

**Recommend NOT widening.** 26.6% coverage lost, 0 measured false positives
prevented. The finding stands as a *consistency* observation — the repo names by
suffix (167 `_probe`, 31 `_audit`, 12 `_sweep`) while the guard knows only prefixes
(57 files) — but consistency of naming is not a reason to blind a guard.

This is the same lesson as the §7c half of this bean, one level up: **measure the
reclassification before shipping it.** There I nearly shipped a regex that
mis-classified in both directions; here I nearly shipped an exclusion that costs a
quarter of the scan surface to prevent nothing.

`_test.py` (17 files) was never a candidate anyway — a real unit test SHOULD be
guarded, as recorded above.

### Not duplicated here

`--strict` is off by default (`return 1 if args.strict else 0`), so the guard is
warn-only and nothing in CI invokes it. That is **by design, not a defect**, and
wiring it is already owned by bean `qou-8plu` ("reach strict green and wire it").
Left alone.

**This half of qou-omiu closes as measured-and-declined, not as work.**
