# The mixed multi-bond interface (¹¹B / ¹⁴N / ¹⁹F) — derive-or-refute

**Date:** 2026-07-14 · **Task:** R8 (follows R6-a / Model G) · **Branch:** `claude/mass-binding-errors-9zqpal`
**Probe:** [`computations/deltalambda/mixed_multibond_interface_probe.py`](../../computations/deltalambda/mixed_multibond_interface_probe.py)
· **Witness:** [`mixed-multibond-interface.witness.json`](../../computations/deltalambda/mixed-multibond-interface.witness.json)
(allPassed: true, 11/11 assertions; witness-fed — deficits and $b$ from the
committed R5-a/R6-a witnesses, AME values from the vendored AME2020;
nothing recomputed, nothing tuned, all candidates pre-registered)
**Discipline:** formalize-first (`compute-author.md` §3.3) — the cone prune
in §2 was stated *before* the candidate evaluations and excludes the entire
additive class; the three candidate rules and the closed-six regression were
pre-registered in the task.

## 1. Characterization — the Model-G ledger and what the miss correlates with

Model G ([consolidated record](2026-07-14-model-g-consolidated-record.md))
closes six isotopes to < 0.5% of $B$ with zero new constants but leaves the
mixed multi-bond trio open. Exact ledgers (committed witnesses; miss
$=$ deficit $-$ pred; $b = 0.78192$ MeV/nucleon; $m$ = number of α's the
light cluster contacts):

| iso | pieces | deficit | pred$_G$ (terms) | miss | miss/$b$ | per (α,α,X) triple | per α·X bond | per nucleon-bond | of deficit |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|
| ¹¹B | 2α+t | 11.132 | 4.692 (αα off + 2 α·t) | 6.440 | 8.24 | 6.440 | 3.220 | 1.073 | −57.9% |
| ¹⁴N | 3α+d | 17.547 | 11.729 (3 αα on + 3 α·d) | 5.818 | 7.44 | 1.939 | 1.939 | 0.970 | −33.2% |
| ¹⁹F | 4α+t | 26.137 | 23.458 (6 αα on + 4 α·t) | 2.679 | 3.43 | 0.447 | 0.670 | 0.223 | −10.3% |

What the residual correlates with:

1. **The trio selector is exact:** the open isotopes are precisely those
   with $A_{light} \ge 2$ **and** $m \ge 2$. ⁹Be ($A_{light}=1$, $m=2$)
   closes at −0.02%; ⁶Li/⁷Li ($m=1$) close. The missing object is a
   **multi-nucleon light cluster shared between multiple α's**.
2. **The miss is non-flat under every per-unit reading** — per bridged
   triple ×14.4, per bond ×4.8, per nucleon-bond ×4.8 across the trio —
   so no single per-unit quantum exists.
3. **The smooth −58 → −33 → −10 trend is partly an artifact of mixing d
   and t.** The natural fourth member ¹⁵N (3α+t; not in the committed
   witness set; deficit 22.123 from vendored AME) has Model-G miss
   **8.049 MeV (−36.4%)**: the t-series miss vs $k$ is 6.440 (k=2) →
   8.049 (k=3) → 2.679 (k=4) — **non-monotone**.

## 2. Formalize-first cone prune — the additive class is excluded before any scan

¹¹B and ¹⁹F carry the **same** light cluster (t, $A_{light}=3$) at $k=2$
vs $k=4$. Every counting available from the cluster graph is
coordinatewise non-decreasing from ¹¹B to ¹⁹F:

| counting | ¹¹B | ¹⁹F |
|---|--:|--:|
| per α·X bond ($m$) | 2 | 4 |
| per bridged triple ($C(m,2)$) | 1 | 6 |
| per nucleon-bond ($m \cdot A_{light}$) | 6 | 12 |
| per light cluster (1) | 1 | 1 |
| per light nucleon ($A_{light}$) | 3 | 3 |

Any non-negative combination $V$ of these countings therefore satisfies
$V(¹⁹F) \ge V(¹¹B)$. The measured miss goes the other way: **6.440 →
2.679 MeV (a ×2.40 decrease)**. Hence no non-negative combination of
graph countings — for *any* choice of constants, zero-new or otherwise —
matches both, and the entire class of additive non-negative
graph-counting extensions of Model G is excluded on the committed data.

**Classification of this exclusion:** structural (a proved cone/
monotonicity obstruction, invariant cited), but **conditional** on the
all-α decompositions (candidate (c) changes them and is adjudicated
separately in §3) and on the committed AME deficits. It excludes the
additive *class*, not any *ingredient*: non-additive, saturating,
shared-channel, or sign-changing closures remain admissible (permanence
principle).

## 3. Rule table — the three pre-registered candidates

| rule | trio result | closed-six regression | verdict |
|---|---|---|---|
| **(a1)** channel per bond, complete graph ($m$ copies) | this **is** committed Model G — the trio miss above | closed (it is the baseline) | already open |
| **(a2)** bridge copies: extra $b \cdot A_{light}(m-1)$ | miss/extra = 2.75 / 1.86 / 0.38 — **×7.2 non-flat** | **breaks ⁹Be**: pred $3b$ vs deficit 1.573 → **+1.33% of B** (was −0.02%) | **refuted both ways** |
| **(b)** gate = 3 *clusters* (light activates the α·α pair) | ¹¹B gains one pair (3b = 2.346 or $g$ = 2.4155): miss 6.440 → 4.095 / 4.025 — **still −36% of deficit** | **breaks ⁹Be**: pred $5b = 3.910$ vs 1.573 → **+4.02% of B** | **refuted twice over** |
| **(c)** sub-cluster promotion: max-$B_{add}$ decomposition (AME values) + Model-G cross interface | ¹¹B = ⁷Li+α: **−72.9%** of deficit (−8.29% of B); ¹⁴N = ¹³C+p: **−68.9%** (−4.97%); ¹⁹F = ¹⁵N+α: **flips sign, +133.8%** (+3.63%) | **survives** — six stay < 0.5% of B; ¹⁶O switches to ¹²C+α and closes at **−0.10%** | **refuted for the trio** (safe but insufficient) |

Named-example splits also fail: ¹¹B = ⁸Be+t −58.2% (−8.57% of B),
¹⁴N = ¹²C+d −54.3% (−5.33%), ¹⁹F = ¹⁶O+t −19.8% (−1.57% of B — the
best single variant anywhere, still ×3 outside closure). The
pre-registered best 2-part splits were verified against a full
enumeration over the vendored AME2020 table (they match).

## 4. The discriminating ¹¹B result

¹¹B (2α+t) is exactly the case that separates "gate = 3 clusters" from
"gate = 3 α's" (the round-6 I3 Milnor-indeterminacy derivation adjudicated
only ⁹Be, a *single-nucleon* spectator). Result:

- **Granting the t the power to activate the α·α pair does not close
  ¹¹B** — the gated value (2.35–2.42 MeV) is only ⅓ of the 6.44 MeV
  miss; −36% of the deficit remains.
- **The same rule breaks ⁹Be** (+4.02% of B, a ×200 degradation) — the
  identical sign-inconsistency that refuted gate=any in R6-a.

So the α-only gate (I3) is now confirmed at the discriminating
**multi-nucleon**-spectator case, not just at ⁹Be: a Hopf-linked light
cluster of any size fails to activate the pair, *and* even a
counterfactual activation would not explain the mixed multi-bond miss.
The ¹¹B deficit is structure of a different kind.

## 5. Closed-six regression (mandatory, decisive)

Under the only rule that changes any closed isotope — (c), which moves
¹⁶O to the ¹²C+α decomposition — all six stay closed:
⁶Li +0.28%, ⁷Li −0.31%, ⁸Be +0.16%, ⁹Be −0.02%, ¹²C −0.26%,
**¹⁶O −0.10%** (improved from −0.28%). Rules (a2) and (b) each break
⁹Be and are refuted independently of the trio.

**Coherence datum (new, positive):** ¹⁶O = ¹²C+α with the ¹²C at its AME
value + 3 gated cross pairs closes at −0.10% of B. Promotion commutes
with Model G exactly when the sub-cluster's internal pairs are already
gated **on** inside its AME value (¹²C, k=3). The mirror case fails as
Model G predicts: ¹²C = ⁸Be+α loses the ⁸Be-internal pair (frozen at
its k=2 AME value ≈ 0 instead of the activated 2.42) and lands at −2.9%
of B. The gate is contextual, and AME promotion freezes the context —
a genuine internal-consistency check of the Brunnian gate, obtained for
free.

**Sign bracket at ¹⁹F:** all-α undershoots (−2.68), ¹⁵N+α overshoots
(+5.37, because the ¹⁵N AME value already contains ¹⁵N's own mixed
interface, which Model G undershoots by 8.05). The two countings bracket
zero, so a correct interface theory exists strictly between them — but
no zero-constant rule tested lands it.

## 6. Honest classification

**REFUTED (scope-(a) for ingredients; scope-(b) for the additive class,
invariant cited).**

- **(b)-type structural exclusion:** the additive non-negative
  graph-counting class cannot close the trio — cone monotonicity
  (every counting non-decreasing ¹¹B → ¹⁹F at fixed light cluster t)
  vs the strictly decreasing measured miss (×2.40). Conditional on the
  all-α decompositions ((c) separately refuted) and the committed AME
  deficits.
- **Scope-(a) negatives:** (a2) bridge copies, (b) 3-cluster gate, and
  (c) sub-cluster promotion each fail as sole mechanisms; (a2) and (b)
  additionally break ⁹Be. No ingredient is excluded — the pair gate,
  the $b$-channel, and the promotion move all remain valid pieces
  (permanence: (c) even *improves* ¹⁶O).
- **Derived side-results (positive):** the α-only gate confirmed at the
  multi-nucleon-spectator discriminating case (§4); the
  promotion/Model-G commutation rule with its ⁸Be+α counter-case (§5);
  the exact trio selector $\{A_{light} \ge 2 \text{ and } m \ge 2\}$;
  the ¹⁵N non-monotonicity correcting the "smooth trend" reading.
- **What the miss now provably is:** a **shared / sub-additive**
  channel — its magnitude *falls* as the light cluster is shared among
  more α's (per-nucleon-bond 1.07 → 0.97 → 0.22), which no counting in
  the additive cone can produce. The missing object saturates.

Nothing wired; no tier change; no fitted constant ($b$ reused from the
committed R5-a witness; every threshold pre-registered).

## 7. Next steps (named, not run)

1. **Saturating closure.** The cone prune says the mixed channel must be
   sub-additive in $m$ — the same *shape* as the Boolean α·α gate.
   Formalize-first target: a shared-channel invariant (the light
   cluster's Hopf channels to several α's factor through one object —
   e.g. one $|\bar\mu|$-idempotent per light cluster, not per bond)
   that predicts the ¹¹B/¹⁵N/¹⁹F non-monotone profile.
2. **The ¹⁵N bracket.** ¹⁹F sits between the all-α undershoot and the
   ¹⁵N+α overshoot; the difference is exactly ¹⁵N's own mixed interface
   (8.05). Solving ¹⁵N (3α+t) solves ¹⁹F recursively — the t-series
   (⁷Li, ¹¹B, ¹⁵N, ¹⁹F) is the right ladder to attack, not the
   A-ordered trio.
3. **Odd-Z pairing physics.** All open members are odd-Z with an odd
   light cluster; the closed six are even-Z or single-bond. Check
   whether the corpus's mirror-split / EM-functional machinery
   (`mirror_split_*` probes) supplies the missing odd-channel term
   before inventing one.
4. **R5-full SDP knot-ID (#604)** remains the principled route to the
   composite interface (unchanged).

## Provenance

Inputs: committed
[`alpha-cluster-volume-additivity.witness.json`](../../computations/deltalambda/alpha-cluster-volume-additivity.witness.json)
(deficits re-verified against vendored AME2020 to 1e-9 MeV),
committed [`alpha-activation-brunnian.witness.json`](../../computations/deltalambda/alpha-activation-brunnian.witness.json)
($b$, Model-G ledger re-derived and matched to 1e-9 MeV), vendored
AME2020 (`qou-mass/src/qou_mass/data/ame2020.json` via
`codata_constants._ame_binding_mev`) for the (c) split enumeration and
the ¹⁵N diagnostic. Companions:
[Model G consolidated record](2026-07-14-model-g-consolidated-record.md),
[R6-a](2026-07-13-alpha-activation-brunnian-derive-or-refute.md),
[R5-a](2026-07-13-inter-cluster-bond-term-derive-or-refute.md).
EXPLORATORY — audit + witness only; no production wiring. Render-QA:
pipeline render unavailable in this sandbox; the manual grep battery
(balanced math delimiters, no KaTeX-rejected macros, no list-hijack
lines in display math) was run by hand — not machine-validated.
