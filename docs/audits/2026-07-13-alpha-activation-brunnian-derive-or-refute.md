# The k ≥ 3 activation of the α·α pair term — Brunnian/Milnor derive-or-refute

**Date:** 2026-07-13 · **Task:** R6-a (follows R5-a) · **Branch:** `claude/mass-binding-errors-9zqpal`
**Probe:** [`computations/deltalambda/alpha_activation_brunnian_probe.py`](../../computations/deltalambda/alpha_activation_brunnian_probe.py)
· **Witness:** [`alpha-activation-brunnian.witness.json`](../../computations/deltalambda/alpha-activation-brunnian.witness.json)
(allPassed: true, 9/9 assertions; witness-fed — deficits from the committed
additivity witness, `b` from the committed R5-a witness; nothing recomputed,
nothing tuned, all candidates pre-registered)
**Discipline:** formalize-first (`compute-author.md` §3.3) — the invariants
(I1)–(I3) below were stated *before* the numerical checks; the ⁹Be gate
adjudication and the counting-rule adjudication were pre-registered both ways.

## 1. The datum (R5-a) and the hypothesis

R5-a ([inter-cluster bond term](2026-07-13-inter-cluster-bond-term-derive-or-refute.md))
left one crisp structural target: the α·α inter-cluster pair term is ≈ 0 at
k = 2 (⁸Be, −0.092 MeV; additivity +0.16%) but pairwise-flat ≈ 2.41 MeV/pair
at k ≥ 3 under complete-graph $C(k,2)$ counting (¹²C 2.425 vs ¹⁶O 2.406 —
0.8%), while the same 2.41 forces a *negative* α·n term at ⁹Be. Separately,
the one-bond deficits are ~linear at $b = 0.782$ MeV per light-cluster
nucleon (3 points, guarded).

**Hypothesis (Brunnian arrangement).** If the k α-clusters form a
Brunnian-type arrangement — pairwise unlinked, triple-linked, the corpus's
own Borromean pattern at the nucleon level (`binding_mn_milnor_linking.py`,
validated: Borromean $lk_{ij} = 0$, $\bar\mu(123) = \pm 1$; Hopf-chain
$\bar\mu = 0$) — then:

- **(I1) k = 2 zero.** All pairwise linkings vanish, so the α·α *pair*
  channel is structurally zero. This derives the ⁸Be anomaly (2α unbound)
  from topology, where standard nuclear physics gives an energetic
  near-cancellation.
- **(I2) k ≥ 3 activation.** The triple channel $\bar\mu(\alpha\beta\gamma) = \pm 1$
  opens only when a third component exists.
- **(I3) Milnor-indeterminacy gate (new).** $\bar\mu(ijs)$ is well-defined
  only modulo $\gcd$ of the pairwise linking numbers of $\{i,j,s\}$
  (Milnor 1954). A *light* spectator (n/d/t) is pairwise Hopf-linked to the
  αs — that pairwise linking **is** the always-on $0.78 \cdot A_{light}$
  channel — so $\gcd = 1$ and the triple invariant carries no content.
  **Only a third α (pairwise-unlinked, $\gcd = 0$) can activate an α·α
  pair.** This is a genuine structural derivation of the "α-only gate",
  stated before the ⁹Be check below, and it makes the two R5-a findings
  mutually consistent: mixed α·X channels are pairwise (Hopf-type,
  active at k = 2 — ⁶Li/⁷Li have nonzero deficits with only two clusters),
  α·α channels are pairwise-absent and only triple-activated.

All three are conditional on the Brunnian cluster-arrangement **model
input** (the same status as the per-isotope $\mathcal{B}_K$ assignment in
`binding_mn_milnor_linking.py`); C5 of the
[a5plus constraints](2026-07-13-atom-knot-rule-a5plus-constraints.md)
(4-component Brunnian L8n8 non-hyperbolic) is consistent — the triple level
is where the content lives.

## 2. Counting-rule adjudication — what makes both ¹²C and ¹⁶O flat AND ⁸Be zero

Three pre-registered counting rules for the pure-α family, adjudicated on
the committed ¹²C (k = 3) / ¹⁶O (k = 4) deficits:

| rule | ¹²C per unit | ¹⁶O per unit | ratio | verdict |
|---|--:|--:|--:|---|
| C-a triple-sum $C(k,3)$ | 7.275 | 3.609 | 2.02 | **refuted** (2× non-flat) |
| C-b spectator-additive $3\,C(k,3)$ (pair value grows with $k-2$) | 2.425 | 1.203 | 2.02 | **refuted** (2× non-flat) |
| C-c Boolean-gated pairs $C(k,2)$, $k \ge 3$ | 2.425 | 2.406 | 1.01 | **selected** (flat to 0.8%) |

Reconciliation of the task's ¹²C-per-triple 7.28 vs ¹⁶O 3.61: correct — the
naive Brunnian *triple-sum* reading is refuted by the very flatness the
round-5 data show. What survives is the **gate**: each α·α pair is activated
by the *existence* of an activating spectator, with a value independent of
how many spectators exist (¹²C has 1 per pair, ¹⁶O has 2 — same 2.41).
So the Brunnian mechanism naturally produces the on/off (I1/I2) and the
α-only gate (I3); the **saturation** (Boolean OR over spectators rather than
a sum) is *data-selected*, not derived. A consistent structural reading:
the Lean-proved D2 sign-rep obstruction
([`QOU/Mass/MilnorSignRepObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/MilnorSignRepObstruction.lean))
forces any equivariant coupling to enter through $|\bar\mu|$
(equivalently $\bar\mu^2 \in \{0,1\}$ — an idempotent), and an idempotent
gate saturates; but OR-vs-SUM over distinct spectator triples is not proved
by that lemma. Recorded as consistent-not-derived.

**⁸Be check (task item 1).** The mechanism predicts exactly 0; measured
−0.092 MeV = 0.16% of $B_{AME}$, a factor ×26 below the 2.42 MeV a universal
pair quantum would force. Consistent — with one honesty note: the *sign* of
the −92 keV threshold residual (⁸Be slightly unbound) is **not** derived;
the topology gives 0, the small negative is separate (Coulomb-scale) physics.

## 3. ⁹Be gate adjudication (pre-registered both ways)

⁹Be = α + α + n. Does the neutron count as an activating spectator?

- **gate = any:** α·α carries $3b = 2.346$ ⇒ forced α·n term
  $= (1.573 - 2.346)/2 = -0.387$ MeV each — negative, sign-inconsistent
  (the same inconsistency that killed the universal-pair reading in R5-a).
  **Refuted.**
- **gate = α-only (the I3 prediction):** α·α stays off; prediction
  $2b = 1.564$ vs deficit 1.573 — **−0.56%**. Passes.

I3 *predicted* the α-only rule from Milnor indeterminacy before this check;
⁹Be confirms it. This upgrades the gate from a data patch to a
(model-conditional) derivation.

## 4. The 3 × 0.78 unification check (task item 3)

Flat per-pair value (mean of ¹²C/¹⁶O): **2.4155 MeV**. Three
light-cluster-nucleon channels: $3b = 3 \times 0.78192 = 2.3458$ MeV.

- Deviation: **−2.89%**, inside the one-bond family's own 5.8% scatter band.
- Ratio direction: per-pair$/b = 3.089$ vs 3 (+3.0%).
- **Genuinely out-of-sample:** $b$ is calibrated on the *mixed* one-bond
  family (⁶Li/⁷Li/⁹Be) only; ¹²C and ¹⁶O are pure-α predictions with zero
  new constants (¹²C −3.3% deficit-level = −0.26% of B; ¹⁶O −2.5% = −0.28%
  of B).

This unifies the two round-5 data (the 0.78/nucleon one-bond linearity and
the 2.41 flat pair value) under **one quantum** $b$ with counting
{$A_{light}$ per α·X pair; 3 per gated α·α pair}. **Guard (stated
plainly):** the count "3" is a post-hoc reading — "one 0.78-channel per
cluster of the mediating triple" is suggestive (the activated interaction is
a 3-cluster object) but not a derivation; an α read as the light side of a
*pairwise* bond would give 4 channels, not 3. What is derived vs read:
the *existence* of a common quantum and the flatness are data; the channel
counts are the hypothesis. Do not wire; do not treat 3 as established.

## 5. Model G — per-isotope table (zero new constants)

$\text{deficit}_{pred} = \sum_{\text{pairs}} \big[\, 3b \cdot [\alpha\alpha,\ \#\alpha \ge 3] \;+\; A_{light}\, b \cdot [\alpha X] \,\big]$
(complete-graph pairs; $b = 0.78192$ from the committed R5-a witness):

| iso | terms | pred | deficit | resid | deficit-level | of B | additivity of B |
|---|---|--:|--:|--:|--:|--:|--:|
| ⁶Li | 1 α·d | 1.564 | +1.474 | +0.090 | +6.1% | +0.28% | −4.61% |
| ⁷Li | 1 α·t | 2.346 | +2.468 | −0.122 | −4.9% | −0.31% | −6.29% |
| ⁸Be | 1 αα (off) | 0 | −0.092 | +0.092 | — | +0.16% | +0.16% |
| ⁹Be | 1 αα (off) + 2 α·n | 1.564 | +1.573 | −0.009 | −0.6% | −0.02% | −2.70% |
| ¹¹B | 1 αα (off) + 2 α·t | 4.692 | +11.132 | −6.440 | **−57.9%** | −8.45% | −14.61% |
| ¹²C | 3 αα (on) | 7.037 | +7.275 | −0.237 | −3.3% | −0.26% | −7.89% |
| ¹⁴N | 3 αα (on) + 3 α·d | 11.729 | +17.547 | −5.818 | **−33.2%** | −5.56% | −16.77% |
| ¹⁶O | 6 αα (on) | 14.075 | +14.437 | −0.362 | −2.5% | −0.28% | −11.31% |
| ¹⁹F | 6 αα (on) + 4 α·t | 23.458 | +26.137 | −2.679 | −10.3% | −1.81% | −17.68% |

- **Closed to < 0.5% of B:** ⁶Li, ⁷Li, ⁸Be, ⁹Be, ¹²C, ¹⁶O. In-sample
  caveat: ⁶Li/⁷Li/⁹Be calibrate $b$ (their residuals are scatter about their
  own mean); the out-of-sample closures are ⁸Be, ¹²C, ¹⁶O.
- **NOT closed:** ¹¹B (−57.9% deficit-level), ¹⁴N (−33.2%), ¹⁹F (−10.3%,
  −1.81% of B — marginal). All three *improve* on pure additivity
  (−14.6/−16.8/−17.7% → −8.5/−5.6/−1.8% of B), but the gated rule + linear
  term is **not** the whole interface theory for mixed multi-bond
  composites. Scope-(a): this constrains Model G as sole mechanism there;
  candidate explanations (not adjudicated here): additional mixed-triple
  structure below the Milnor gate, or wrong decompositions (2α+t / 3α+d)
  for exactly these odd/odd-odd isotopes.

## 6. Magnitude candidates for the flat 2.4155 MeV (pre-registered)

| candidate | MeV | dev |
|---|--:|--:|
| **3b (unification)** | 2.3458 | **−2.9%** |
| B_D (AME) | 2.2246 | −7.9% |
| deuteron rotor $\mu_0 \hbar_q J_q^2(3)$ | 2.0196 | −16.4% |
| $m_e \cdot Vol(L6a4)$ | 3.7445 | +55.0% |
| $m_e \cdot Vol(4_1)$ | 1.0373 | −57.1% |
| $m_e \cdot Vol(8_{11})/2$ | 2.1171 | −12.4% |
| $m_\pi \hbar_q^2$ | 1.3702 | −43.3% |
| $\alpha_{der} \cdot m_\pi$ | 1.0201 | −57.8% |

Only 3b lands within 5%. B_D and the rotor were quarantined in R5-a and stay
quarantined; no $m_e \cdot Vol$ candidate is close.

## 7. Honest classification

**PARTIAL DERIVATION.**

- **Derived (conditional on the Brunnian cluster-arrangement model input):**
  (I1) the k = 2 zero — the ⁸Be anomaly from topology (×26 discrimination
  vs a universal pair quantum; the −92 keV sign not derived); (I2) the
  k ≥ 3 activation; (I3) the α-only gate via Milnor indeterminacy —
  *predicted* the ⁹Be resolution (−0.56%), where gate=any is
  sign-inconsistent.
- **Data-selected (not derived):** the saturation — Boolean-gated $C(k,2)$
  is flat to 0.8% while triple-sum and spectator-additive counting are 2×
  non-flat; idempotent $|\bar\mu|$ coupling (Lean D2) is a consistent
  reading only.
- **Consistent within scatter, guarded:** the 3 × 0.78 unification (−2.9%
  vs 5.8% band; out-of-sample at ¹²C/¹⁶O); the channel count "3" is
  post-hoc.
- **Negative (scope-(a)):** mixed multi-bond composites ¹¹B/¹⁴N (and ¹⁹F
  marginally) are not closed by Model G — the mixed-cluster multi-bond
  interface has additional structure.

Nothing wired; no tier change; no fitted constant ($b$ reused from the
committed R5-a characterization, not re-fit).

## 8. Next steps (named, not run)

1. **Derive the saturation.** Find the invariant that forces the Boolean
   (idempotent) gate — e.g. show the pair's activated interface energy is a
   property of the pair's 2-component sublink class *given* activation
   (spectator-independent), or that multiple-spectator triples share one
   channel. The Lean D2 $|\bar\mu|$ route is the natural starting point.
2. **Derive the channel count 3** (or refute it: at −2.9% with a 5.8% band,
   a 4-channel reading at $4b = 3.128$ is −29.5% and already excluded; the
   discrimination is real, the derivation is missing).
3. **The mixed multi-bond interface** (¹¹B, ¹⁴N): test alternative
   decompositions and sub-α-cluster triples; this is the same missing
   object as the a5plus C8 carrier-saturation line.
4. **Lean target:** the I3 gate (triple invariant killed by unit pairwise
   linking) is a finite Magnus computation — formalizable in the style of
   `MilnorSignRepObstruction.lean`.

## Provenance

Inputs: committed [`alpha-cluster-volume-additivity.witness.json`](../../computations/deltalambda/alpha-cluster-volume-additivity.witness.json)
(deficits re-verified against vendored AME2020 to 1e-9 MeV),
committed [`inter-cluster-bond-term.witness.json`](../../computations/deltalambda/inter-cluster-bond-term.witness.json)
($b$, per-pair values), validated Magnus $\bar\mu$ machinery imported from
[`binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py),
`m_e` (CODATA 2022, CAL-1), q₀ (`q_parameter.Q_50_DIGIT_STR`), `m_π` (CAL-3,
candidates only), link volumes from the additivity witness (deprecated
volume-search IDs, stated as such). Milnor indeterminacy: Milnor 1954
(μ̄ defined mod gcd of lower-order invariants). Companions:
[R5-a](2026-07-13-inter-cluster-bond-term-derive-or-refute.md),
[a5plus constraints](2026-07-13-atom-knot-rule-a5plus-constraints.md),
[D2 sign-rep](2026-07-13-mirror-split-s3-em-functional-attempt.md) +
[`MilnorSignRepObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/MilnorSignRepObstruction.lean),
[GAP-2 triple count](2026-07-11-gap2-borromean-triple-count.md) (the
3-clique overshoot — consistent: reducible triples don't count there,
non-Brunnian triples don't activate here).
EXPLORATORY — audit + witness only. Render-QA: pipeline render unavailable
in this sandbox; the manual grep battery (balanced math delimiters, no
KaTeX-rejected macros, no list-hijack lines in display math) was run by
hand — not machine-validated.
