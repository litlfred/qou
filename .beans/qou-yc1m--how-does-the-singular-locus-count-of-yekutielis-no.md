---
# qou-yc1m
title: How does the singular-locus count of Yekutieli's non-abelian Stokes estimate scale with A for the nuclear braid closure's spanning surface? Affine => renormalises the volume term; sublinear => the first Stokes-derived surface term
status: completed
type: task
priority: normal
created_at: 2026-09-06T09:25:31Z
updated_at: 2026-09-06T10:13:56Z
---

## Resolved 2026-09-06 — Euler bounds the 1-skeleton below by 9A+1; whether that IS the Stokes singular locus is hypothesis (H1), and the corpus cannot discharge it

Lean `QOU/Mass/StokesSingularCountAffine.lean` (5 decls, sorry-free, axiom-clean) + probe
`computations/probes/stokes_singular_count_affine_probe.py` (11/11, exact integers/Fractions).

**Proved (scope-(b), invariant = Euler).** For ANY cell decomposition with a vertex and a face,
E = V + F - chi >= 2 - chi (edges_ge_two_sub_chi). With the canonical closure's chi = -9A + 1
(COMPUTED from n = 3A disks and c = 12A - 1 bands, both derived for all A per qou-hu1f; reproduced
from atom_braid_word_3A at six nuclei), E >= 9A + 1 — the 1-skeleton of any decomposition grows at
least linearly in A. Sharp (one-vertex polygon attains it); generalises the corpus's exact counts
(AffineCountIsNotASurfaceTerm.crossingCount, TransverseSurfaceCurvature.seifertBettiOne_extensive)
from one decomposition to all — not a new number. A boundary count bounded below by an affine
function over a bulk count bounded above by one has ratio -> 3/5, never 0: not a StokesSurfaceTerm
(not_stokesSurfaceTerm_of_bounds, stokes_canonical_not_surfaceTerm).

**THE CORRECTION (opened as qou-h7w4).** The 2026-08-30 audit — and my own HyperbolicSurfaceLaw
header, now fixed on this branch — read the bad set as "counted by the singular points of the
surface map". That is Yekutieli's 1-DIM string case (:2280). In 2-dim the kite map is linear by
definition (Def 4.1.1) and the bad set is where the connection FORMS (alpha, beta) fail to be
smooth (Def 4.4.12); a_0 = 2m for m segments covering their singular locus, a_1 = 2*sum len(Z_j) —
a LENGTH (Lemma 4.4.13). Consequences: "a_S proportional to a count" can only mean a_0; and if the
forms are smooth, a_0 = a_1 = 0 — NO Stokes surface term of any size. The corpus has no (alpha,
beta) as forms (qou-20bk: "Step 2's curvature is stipulated, not a form").

**(H1), scope-(a), NOT dischargeable now:** that the forms' singular locus runs along the 1-skeleton
of some cell decomposition. Under (H1) the Stokes route renormalises the volume coefficient exactly
as the hyperbolic ball does. Two named ways out: smooth forms (no surface term at all), or a
singular locus that is a proper sub-complex of sublinear edge count — Euler forbids that for the
whole skeleton, not for a subset, so (H1) is where the content is.

**Also found (qou-d5hn):** mu = A+1 is a HYPOTHESIS in SLq2LabelParity.lean:77 and
TorusKnotPages.lean:82 but is cited as "(exact, Lean-proved)" by total_curvature_is_the_computable_half_probe.py:43
and its witness. And YekutieliTrefoilDiscretization.lean cites bean qou-jqof, which does not exist.

## Next (my judgement)
Nothing on the Stokes route is derivable until the framework has (alpha, beta) as forms. The
hyperbolic ball's S/V >= 2 is unconditional; this is the conditional twin. Do not open a third
surface-term tranche on this arc without a connection form.
