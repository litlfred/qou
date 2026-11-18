---
# qou-gl58
title: 30 files use the CLASSICAL q-integer (q^n-1)/(q-1) under names q_int/qint — check each consumer expects it, not the symmetric one; several are in deltalambda/ (Track A)
status: in-progress
type: task
priority: normal
tags:
    - needs-owner
    - reorg-2026-10-04
created_at: 2026-09-07T14:02:18Z
updated_at: 2026-11-18T08:30:27Z
parent: qou-4cu3
---

WORKED 2026-09-07 (audit sec 22). 0 of 363 files carry BOTH conventions — no internal inconsistency anywhere. My 'the word hecke appears' classifier is NOISE: tw_gram_determinant_probe.py is CORRECT (its q_int is the Gaussian bracket and its docstring says the conventions match QOU/Hecke/TwMul.lean, whose rule sigma_i T_v = (q-1)T_v + q T_{v s_i} is the T_w basis, where classical IS right); deltalambda_jet_filtration_magnitude_probe.py DECLARES the convention in its docstring ('Coxeter-length / coinvariant Poincare convention, NOT the balanced'). THE REAL DISCRIMINATOR IS THE BASIS: T_w / Iwahori unnormalised -> classical; normalised / quantum-dimension -> symmetric. Defensible figures: at most 28 unclassified, 1 confirmed ambiguous (helium_four_body_cluster_probe.py, sum(q**k), undeclared, Borromean cluster context), 2 confirmed fine. term7_chi5_basis.py stays OPEN: it feeds a q-hook-length dim_q, and my attempt to settle it against y_lambda_at was the WRONG TEST — y_lambda_at is the SU(2)-restricted Markov weight (zero on height>2 partitions), term7 computes Plancherel dim_q^2/[n]_q! over all partitions.

2026-09-13 — the TEN classical definitions surfaced by qou-b8vx are all resolved.
SCOPE FIRST, because these are NOT this bean's original 30: the duplication
audit's 30 are q-PARAMETRIC (2-arg) definitions; qou-b8vx's global-resolution
audit measures the q0-PINNED (1-arg) population, which that audit skips
entirely. Different sets. This append closes the 10, and this bean's own 30
are untouched.

FIVE SELF-DECLARE IN THE FUNCTION NAME — no determination needed:
   probes/c1_kernel_door_v_residual_probe.py::qint_geo
   probes/c1_kernel_level_reading_probe.py::qint_geo
   probes/derivative_only_dq_vs_c1_kernel_probe.py::qint_geo
   probes/ramified_shift_calculus_prune_probe.py::qint_geo
   substrate/lever1_qinvolution_kernel_test.py::qint_asym
"geo" IS the geometric sum 1+q+...+q^(n-1), which IS the classical bracket;
"asym" says the same thing the other way. The name states the convention.

FIVE UNDER AMBIGUOUS NAMES, each DETERMINED BY ITS OWN BASIS — all five
CORRECT AS WRITTEN. None is a defect.

1. hecke/tw_gram_square_class_crosscheck.py::q_int — CORRECT, and decisively.
   A T_w Gram file (twGram, QOU.Hecke.TwBasis), where audit sec 22 rules the
   classical bracket correct. But the file settles it without needing that
   rule: it MEASURES det = q^22 (q+1)^48 (q^2+1)^20 (q^2+q+1)^6, and the
   published form [2]^28 [3]^6 [4]^20 reconstructs that ONLY classically,
   since [4]_clas = (1+q)(1+q^2). Ran it: exit 0, "all ranks confirm both
   predictions".

2. gs_tower_jet_degree_body_order_probe.py::q_int — CORRECT. The subject is
   the GS/jet filtration's GRADED DIMENSION. A Poincare grading is exactly
   where sec 22 puts the classical bracket. Ran it: exit 0.

3. lever1_kernel_maj_involution_identification.py::qint_u — CORRECT. The
   subject is the MAJOR INDEX (maj) over involutions in S_n -- a
   Coxeter-length statistic, whose generating function is the classical
   [n]_q!. sec 22 again. Used in a q-factorial hook ratio, num/den.

4. deltalambda/binding_weight_markov_pinning_probe.py::qint — CORRECT, and
   this is the one whose NAME most suggests otherwise. "Markov" implies the
   symmetric bracket, so I expected a defect. Ran it: the Markov weights come
   from the CANONICAL MODULE ("y_lambda source: canonical-module"), and qint
   feeds only W_lambda = d_q^2/[n]!, the Schur-Weyl/Plancherel weight this
   probe EXCLUDES. Built via the hook-length formula, which is a principal
   specialization -- classical. The file's own check that W_lambda is
   conjugation-symmetric HOLDS THROUGH n=7, and that symmetry fails for a
   wrong-convention hook formula. Its own test verifies its own bracket.

5. qbeta/qbessel_mu_lambda_vs_qlommel_zeros.py::q_int — SELF-DECLARED. Its
   docstring is literally "[n]_q = (q^n - 1)/(q - 1), valid for negative n
   too" and the body implements exactly that, so no reader is misled. Used in
   the content-Casimir sum total += q_int(c)*q_int(c+1). NOT ESTABLISHED, and
   deliberately not guessed: whether classical is the RIGHT convention for a
   q-Casimir belongs to whoever owns prop:q-heat-kernel-peter-weyl. That is a
   question about the mathematics, not about whether the file says what it
   does.

SO: 0 defects in 10. The lesson for this bean's remaining 30 is the useful
part -- the discriminator that worked was never the NAME, it was:
  (a) does the file publish a figure its bracket must reproduce? (case 1)
  (b) does the file's own internal check verify the bracket? (case 4)
  (c) does the subject name a grading/statistic sec 22 already rules on? (2,3)
  (d) does the docstring declare it? (case 5 and the five _geo/_asym)
Only when none of (a)-(d) applies is a per-file basis determination actually
needed. On this sample that was ZERO of 10, which suggests the 30 may be far
cheaper than "a per-file determination, not a sweep" implies.


---

## 2026-09-13 — this bean's OWN 29 (not the 10 above): all classified, 0 defects

The count is **29, not 30** — re-measured from `q_integer_duplication_audit`
rather than quoted. New artifact:
`computations/audits/classical_q_integer_basis_triage.py`, which recomputes the
list rather than hardcoding it.

**RESULT, and quote it as two numbers, never one:**

| | |
|---|---|
| STRONG (DECLARED 18 + BASIS 4) | **22 / 29** |
| WEAK (FAMILY) | **7** |
| needs human reading | **0** |
| **defects** | **0** |

**Do NOT quote 29/29.** The 7 FAMILY files declare nothing at all; they are
merely near a file with an identical definition. The script refuses to print a
combined figure for this reason.

### The finding is about THE DETECTOR, not the corpus

The residue needing a human went **20 -> 15 -> 10 -> 7 -> 0 without a single
file being read**, purely by fixing four blind spots in my own script. Four
spellings of one function, each defeating an ASCII-shaped regex:

1. `(1 - q^n)/(1 - q)` — the same function with both signs flipped. Hid 7 of
   the 9 `qlift_*` probes, 5 of which declare in their own function docstring.
2. `1 + q + ... + q^(n-1)` — the geometric-sum spelling.
3. **U+2212 MINUS SIGN** in `q^{k-1}`. This hid the three files whose
   docstrings cite **a Lean declaration** (`QOU.Mass.QDifferenceConfluent
   Obstruction.qint`) as the corpus convention — the strongest evidence in the
   whole set, invisible on one non-ASCII character.
4. **The USE SITE.** `q_int(hook_length(...), q)` in a running product IS the
   q-hook-length formula — a principal specialisation, classical by
   construction — whether or not any docstring says so. Found because three
   `chirality_avg_content*` files compute the identical thing and only the one
   that MENTIONED hook lengths was being classified.

**The ordering lesson for the next auditor: exhaust the detector before reading
files.** I was one step from hand-reading 20 files, 19 of which the corpus
already answers in writing.

### FAMILY is weak and the script says so in its own output

Both halves of its evidence are near-vacuous here, measured rather than felt:
body-identity restates how a file got into the CLASSICAL bucket (symbolic
signature) in the first place, and `computations/probes/` holds **~1200
files**, so two probes sharing that directory are not siblings in any
meaningful sense.

What FAMILY genuinely is: **an authoring-hygiene queue** — 7 files that do not
say which bracket they use, each paired with the nearby file to copy one
docstring line from. A statement about documentation, not about mathematics.

The 7: `a4_h12_brunnian_deficit_measure_probe`,
`helium_four_body_cluster_probe` (both -> `deltalambda_additive_signchanging
_term_probe`); `ksel2id_friedrichs_selection_probe`,
`ksel2id_u1_promotion_probe` (-> `fvk_selection_probe`);
`qlift_doorIV_matrix_crossterm_probe`, `qlift_doorV_stokes_automorphism_probe`
(-> `qlift_doorIII_followup_twist_crossterm_probe`);
`qlift_routeC_homogenized_factor_probe` (-> `qlift_ggm_diagonal_gauge_prune
_probe`).

`helium_four_body_cluster_probe` was this bean's **"1 confirmed ambiguous"**.
It is no longer unmeasured — but it is FAMILY, i.e. still undeclared in its own
file, so the earlier note was right about the file and only wrong about
whether anything nearby settles it.

### What is NOT established

* **That the classical bracket is mathematically RIGHT for each subject.** A
  DECLARED verdict says the file is HONEST about which bracket it uses. Those
  are different claims and the script makes only the first. It says so in its
  own output rather than only here.
* **`term7_chi5_basis.py` is untouched** and stays open. It is not in this 29
  (`term7_height6_partition_enum.py` is, and resolves BASIS on `T_w`). Note
  for whoever takes it: AGENTS.md's notation-register section now records that
  `sum_lambda w_lambda(q) != 1` (measured 0.987 / 0.982 / 0.982 / 0.991 /
  1.111 / 1.517 at n = 3/4/5/6/9/12), and that whether `dim_q^2` is even the
  right numerator — against the Molien `f^lambda dim_q(lambda)`, which sums to
  `[n]_q!` exactly — is **open as bean qou-oots**. term7 computes exactly that
  `dim_q^2/[n]_q!`, so its convention question is entangled with `qou-oots`
  and should not be settled independently of it.

Running total across both appends: **0 defects in 39 classical definitions**
(10 from `qou-b8vx` + these 29).


2026-09-13 (later) — THE AUTHORING-HYGIENE HALF IS CLOSED: 29/29 STRONG,
0 FAMILY, 0 READ. Seven files that used no convention-declaring words at all
now carry a one-line docstring each. Branch
claude/gl58-declare-bracket-convention-2026-09-13.

WHAT "FAMILY" WAS, because the verdict name understates it. The triage
assigns FAMILY when a file's `qint` body is byte-identical to a sibling's
whose docstring DOES declare the bracket. That is a statement about the
neighbourhood, not about the file: a reader opening
ksel2id_u1_promotion_probe.py sees `def qint(qv, k)` with a bare loop and
has nothing in front of them that says which bracket it is. The two
brackets differ by q^{(n-1)/2}, silently, on every value returned. FAMILY is
the audit reporting that it could not answer the question from the file and
went looking elsewhere.

THE SEVEN, with the wording taken from each one's own declaring sibling so
the file now says what the family already said:

  deltalambda/a4_h12_brunnian_deficit_measure_probe.py::qint
  deltalambda/helium_four_body_cluster_probe.py::qint
      "[n]_q = 1 + q + ... + q^{n-1} = (q^n - 1)/(q - 1)"

  probes/ksel2id_friedrichs_selection_probe.py::qint
  probes/ksel2id_u1_promotion_probe.py::qint
      "[k]_q = 1 + q + ... + q^{k-1}, field-agnostic.  NOTE the argument
       order: the MODULUS comes first, the index second."
      -- this pair takes (q, k), the OPPOSITE order to every other qint in
      the corpus. That is a second, independent foot-gun that the triage
      does not measure and that nothing else in the tree stated; it is
      stated now.

  probes/qlift_doorIV_matrix_crossterm_probe.py::q_int
  probes/qlift_doorV_stokes_automorphism_probe.py::q_int
      "[n]_q = (q^n - 1)/(q - 1), n at q = 1"

  probes/qlift_routeC_homogenized_factor_probe.py::qint
      "[k]_q = (1 - q^k)/(1 - q) -- the unbalanced bracket, sign-flipped
       spelling"

RUNTIME-INERT, and verified rather than asserted. The diff is 9 insertions,
0 non-docstring added lines, 0 removed lines. qlift_routeC re-runs with its
VERDICT line unchanged ("NEITHER EMBEDS ... Scope-(a)") and a witness diff
that is provenance-only (generated / scriptHash / scriptCommitSha /
commitSha / computedAt / durationMs / q0Anchor); no numeric field moved.
raw-float64 ratchet NEW 0, REGRESSED 0. Triage re-run after merging
origin/main (17 commits): still 29/29.

SECOND COMMIT, and it is the more interesting defect. The triage's own
closing warning hardcoded the number it was warning about:

    Do NOT quote a single combined figure.  'STRONG + WEAK' would read as
    29/29 resolved, and 7 of those are files that say nothing at all.

The 7 was a literal. With FAMILY drained it printed that line directly
beneath its own computed "WEAK (FAMILY) : 0" -- a footer contradicting its
own measurement, in the one script whose entire subject is files asserting
something a neighbour measured. Now derived (n_fam + n_read), and when both
are zero the warning is replaced rather than printed falsely.

WHAT THIS DOES NOT CLAIM. A DECLARED verdict says a file is HONEST about
which bracket it uses. It says nothing about whether that bracket is the
mathematically right one for the file's subject. Those are different claims
and the triage only makes the first. The bean's ORIGINAL 30 -- the
q-PARAMETRIC (2-arg) definitions from the duplication audit -- are a
different population from the q0-PINNED (1-arg) set this triage measures,
and are untouched by this append, as by the previous one.

STILL OPEN in this bean: term7_chi5_basis.py (feeds a q-hook-length dim_q;
the y_lambda_at test was the wrong test and it has not been re-settled), and
the original 30's per-consumer correctness question.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

Same axis as `qou-b8vx`/`qou-qint`: classical q-integer under `q_int`/`qint`
names. The bean's own worked note says 0 of 363 files carry both conventions,
i.e. no internal inconsistency. Keep open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## Round 86 Progress (PR #8398)
- Branch: `feat/round86-irrcubic-resolvent3-dimsum5-tau1-satdiff-43c1`
- Commit 1 (code + probe): `b5de63778dc1a1dd5f06089955f845fb94bba20f`
- Commit 2 (witness): `cda43c1b21fb03c917cb1d6c4ebc184aeff1e706` (`scriptSha256 = d48339de07d62c85bc2a014c14ff39ca61b8c6091d44dbc01d9abdb15245ae18`)
