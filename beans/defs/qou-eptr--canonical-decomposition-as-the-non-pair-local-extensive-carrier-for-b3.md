---
# qou-eptr
title: EP/canonical decomposition as the non-pair-local extensive carrier for b_3 — aim, and the hard blocker at the light end
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T10:56:11Z
updated_at: 2026-11-16T18:04:00Z
parent: qou-10v9
---

WHY IT IS WELL-AIMED at the ONE open piece of the binding gap
(qou-brng; audit 2026-09-05-binding-gap-groupoids-derived-categories-full-tower
§1.2 row 4: measured b_3 = +1.4262 MeV, model exactly 0):
  * EXTENSIVE by construction — a sum over cells, not a per-block lambda weight,
    so it is not blocked by exchangeDet_pow_two_le_four (intensive -/-> extensive).
  * NOT PAIR-LOCAL — a tetrahedron couples FOUR vertices, and
    CrossingModelPairLocality.b3_eq_zero_of_pairLocal says pair-locality is
    exactly what forces the model's zero. A 2-3 Pachner move is literally a
    body-order-changing move.
  * CANONICAL, so no selection-against-the-target: EP is unique, no census
    search, no fitted cutoff. Satisfies the NO-FITTING directive.
  * BOUNDED DEGREE is the regime CoordinationSaturation forces, and a
    triangulation supplies a bond graph rather than assuming one.

CANDIDATE OBSERVABLE (proposal, NOT a result): Pachner distance between the
layered triangulation derived from the braid word (2026-09-06 audit: #tetrahedra
= #letters of the LR word) and the CANONICAL EP triangulation. Both the log law
(B = E_0 x #Markov reduction steps) and the layered functor are word-length
counts; their difference is a Pachner-graph distance, which is global, not
pair-local.

HARD BLOCKER, stated up front: EP requires a COMPLETE FINITE-VOLUME HYPERBOLIC
structure. The owner's 2026-08-29 deuteron ruling puts the deuteron on the
canonical braid closure (trefoil / Hopf) with Vol = 0 — Seifert-fibred and
T^2 x I respectively, neither hyperbolic — so NO EP decomposition exists for
^2H. The route cannot reach the light end where the data is best. Whether it
reaches B_3 (hyperbolic, Vol 7.3277) and the A>=3 chain is the first thing to
measure. Do NOT read "Pachner count" as "volume": the 2026-08-29 Bloch-volume
leg proved 0 kills a VOLUME term, not a combinatorial count.

## MEASURED 2026-09-06 — the route reaches the atoms and cannot separate them

STAYS OPEN. The subject is the binding gap's irreducibly many-body term, which
is open (qou-brng). Per AGENTS.md 13a this bean is not closeable by having
measured something about it.

ep_decomposition_reachability_probe (9/9), commit 43d6ddd46:
  * 15 of 16 atoms with non-zero binding ARE hyperbolic -- the route is not
    blocked by hyperbolicity above the deuteron. My earlier framing that "the
    light end is unreachable" over-generalised from the deuteron; A>=3 is fine.
  * BUT the dictionary uses only 2 distinct manifolds, and 13 atoms share L6a4
    with binding spanning 1.667e9. An EP invariant is a function of the
    manifold, so it is constant on that class. Scope-(b).
  * deuteron excluded twice over: labelled SATELLITE, and Thurston's trichotomy
    makes a satellite complement non-hyperbolic. Agrees with the 2026-08-29
    ruling without depending on it.
  * classify_nuclear_knot factors through A (30x34 grid), discards the braid
    word, one consumer, in hecke_core_legacy.py.

canonical_cell_structure_probe (7/7):
  * the Pachner-distance candidate is 0 on 4_1 -- the derived Floyd-Hatcher
    layering IS the canonical decomposition (both 2 regular ideal tetrahedra).
  * Vol(L6a4)/V_oct = 2.0 exactly, Vol(L6a4)/V_tet = 7.2198 not an integer, so
    the principal manifold's canonical decomposition is not a triangulation.

WHAT IS STILL LIVE. The exclusion is of EP-of-the-DICTIONARY-knot. EP of the
actual per-atom braid closure is untested and needs that closure identified
first -- the same modelling decision qou-imkb records as blocked for Model B.
Attacking a better invariant of a collapsed knot cannot help.

## 2026-09-06 SELF-CORRECTION — the per-atom closure EXISTS; this was NOT blocked

I wrote that identifying the per-atom closure is something "the corpus does not
currently do" and framed it as an owner decision blocked on qou-imkb. Both wrong.

MEASURED (per_atom_braid_closure_probe, 5/5):
  canonical_braid_crossings.atom_canonical_crossings(Z, N) computes a per-atom
  canonical braid word LIVE for any (Z, N). Over a 10-atom sample the words are
  pairwise distinct 10/10. Sharp case: tritium (1,2) vs he3 (2,1) -- same A,
  same 35 crossings -- differ at 4 positions with different crossing TYPES and
  exponent sums 4 vs 8. Word LENGTH factors through A (12 crossings/nucleon),
  the word does not.

qou-imkb governs Model B's T1 registry, a different question.

ALSO CORRECTED, on owner challenge ("are you saying that you can't distinguish
atoms with A >= 4?????"): NO. Over the 13 atoms with A >= 4, exactly ONE field
is constant -- knot_type, 1/13. net, ln|tr_M|, B_MeV and V_per_gen are all
13/13 distinct. The framework distinguishes them completely; only the LOOKUP
LABEL collapses. My phrasing "collapses every atom with A >= 4 onto one knot"
was true of classify_nuclear_knot and read as a claim about the framework.

THREE OPEN QUESTIONS, in dependency order, none needing a ruling:
  1. are the per-atom closures distinct LINKS? (distinct words need not close
     to distinct links -- Markov moves, conjugation). Cheapest killer.
  2. are they hyperbolic?
  3. does the canonical decomposition then vary across atoms? (the original
     route, downstream of both)


---

## 2026-09-07 CORRECTION — `atom_canonical_crossings` is NOT a braid word either, so all three open questions are ill-posed

The 2026-09-06 self-correction above says:

  "canonical_braid_crossings.atom_canonical_crossings(Z, N) computes a per-atom
   canonical BRAID WORD live for any (Z, N)."

**The distinctness half stands. The phrase "braid word" is wrong, and I wrote it.**

That function's own docstring names its source of truth as
`mass_at_3A_proper.atom_braid_word_3A` -- the object PR #6952 established is a
HECKE ELEMENT. Deriving `(gen_idx, ctype)` pairs from it does not launder the
Hecke letters away.

MEASURED (`atom_canonical_crossings_not_a_braid_probe`, 12/12):

  atom        A   len  braid  averaged  avg_wtd
  protium     1    11      9         2        0
  deuteron    2    23     18         4        1
  tritium     3    35     28         6        1
  he3         3    35     28         6        1
  he4         4    47     38         8        1
  li6         6    71     58        12        1
  c12        12   143    118        24        1
  fe56       56   671    558       112        1

  * EVERY atom carries `averaged` letters -- 0 of 11 are clean.
  * The count GROWS with A (2 -> 112), so it is not a boundary artifact.
  * EVERY BOUND atom carries exactly one `averaged_weighted`; protium, unbound,
    carries none.
  * ctype alphabet is {averaged, averaged_weighted, sigma, sigma_inv} --
    strictly larger than the braid alphabet {sigma, sigma_inv}.

### Why this voids the three open questions

An `averaged` letter is `(sigma + sigma^-1)/2`: a proper linear combination in
`H_n(q)`, NOT in the image of `B_n -> H_n(q)`, which is generated by products
of `sigma_i^{+-1}`. Alexander/Markov closure is defined for BRAIDS. A linear
combination has no closure.

So question 1 ("are the per-atom closures distinct LINKS?") -- flagged above as
the cheapest killer -- **cannot be asked**, and 2 and 3 are moot. There is no
link to test for distinctness, hyperbolicity, or canonical decomposition.

### How the error happened, since the pattern is the reusable part

PR #6942's `canonical_word_is_not_a_braid_probe` measured `atom_braid_word_3A`
and found 0 of 14 atoms free of averaged letters. The bean then asserted
`atom_canonical_crossings` was a braid word **without re-running that test on
it** -- treating a derived function as inheriting a property its source does
not have. Running the same test on the derived function is all this took.

### WHAT IS NOT CLAIMED

This bounds the EP ROUTE, not the framework. `tr_M` of a Hecke element is a
well-defined NUMBER and is exactly what the corpus computes; the per-atom
distinctness (10/10, and tritium vs he3 differing at 4 of 35 positions) is
real and unaffected. What has no definition is `Hecke element -> 3-manifold`,
and Epstein-Penner needs a manifold.

Scope (a) with a proved obstruction to the specific route: the reason is that
the object is not in the image of `B_n -> H_n(q)`, not a failed search. It says
nothing about reaching `qou-brng`'s extensive term by some other route.

### THE BEAN STAYS OPEN (AGENTS.md 13a)

Its subject is the binding gap's irreducibly many-body term (`b_3 = +1.4262`
MeV measured, model exactly 0), which is open. What is now closed is one route
to it, for a stated structural reason.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Verified on `main` and cross-linked with `qou-sgv5` / `qou-dx1t` (PR #8145)

- Re-verified `computations/probes/atom_canonical_crossings_not_a_braid_probe.py` on `main` (12/12 checks pass, `computations/probes/atom-canonical-crossings-not-a-braid-probe.witness.json`), confirming that every atom carries non-braid `averaged` letters (`2*A` per atom) and every bound atom (`A >= 2`) carries `1` `averaged_weighted` letter, while tritium and helium-3 differ at 4 of 35 positions (`[11, 18, 20, 23]`).
- Cross-verified in `computations/probes/chi_matrix_m_isospin_degeneracy_diagnostic_probe.py` (`qou-sgv5`, PR #8145 at `ed78b60a0ffe233f132df45a37bb1456ec237832`) how dropping the `d` field in `(c, d, gen) -> (sign, gen)` collapses the 4 differing tritium/helium-3 positions and all `averaged`/`averaged_weighted` letters to `+1`, whereas the exact-triple Hoefsmit / closed-form Wenzl bridge routes preserve them.
- Status stays `in-progress` per §"THE BEAN STAYS OPEN (AGENTS.md 13a)".
