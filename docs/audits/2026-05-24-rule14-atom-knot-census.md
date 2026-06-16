# Rule-14 escalation — atom → knot census assignments (D ↔ 6₂, T ↔ 8₁₁, ³He ↔ L6a4)

**Date:** 2026-05-24
**Branch:** `claude/post-1089-followups-2026-05-24` → PR [#1111](https://github.com/litlfred/qou/pull/1111)
**Status:** ⏸️ **DEFERRED 2026-05-24** — owner decision: **wait for R5-full SDP solver** (option 3 of the §5 menu). The current census-derived assignments (D ↔ 6₂, T ↔ 8₁₁, ³He ↔ L6a4) are retained as **EXPLORATORY scaffolding** in [`mass_table_ppb.py`](../../computations/mass_table_ppb.py) ATOM_ASSIGN; origin tags now carry the explicit `"hyp: census-assigned (EXPLORATORY pending R5-full SDP)"` marker. No `prop:` block authored — categorical derivation of the canonical (Z, N) → K functor deferred to the R5-full SDP solver landing.

Rule-14 escalation per [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md §"Rule 14 — Author-escalation for off-menu coefficients"`](2026-05-23-lambda-scale-canonical-unification.md).
**Parent audit:** [`docs/audits/2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md) (item #1, 🔴 HIGH risk).

## §1. The issue

The atom → knot map in [`computations/mass_table_ppb.py:86-93`](../../computations/mass_table_ppb.py) hardcodes three census-derived pairings:

```python
"2H":   {"rule": "kashaev", "knot": "6_2",  "rho_factor": 1, "origin": "hyp: census-assigned"},
"3H":   {"rule": "kashaev", "knot": "8_11", "rho_factor": 2, "origin": "hyp: census-assigned"},
"3He":  {"rule": "kashaev", "knot": "L6a4", "rho_factor": 2, "origin": "hyp: census-assigned"},
```

The script's own docstring ([`mass_table_ppb.py:18-21`](../../computations/mass_table_ppb.py)) admits:

> *"The atom→knot assignments for D, T, ³He were obtained by census search in `jsj_verification.py` — that IS a form of AME-driven fitting (we picked the knot whose volume is closest to B_AME/ρ)."*

The selection procedure (see [`delta_lambda_jsj_phase3.py:14-21`](../../computations/delta_lambda_jsj_phase3.py)) closes the canonical atomic braid word into a link, calls `snappy.simplify`, reads the hyperbolic volume, and accepts the knot whose `Vol_hyp(K)` minimises `|B_AME − ρ_F · m_e · Vol(K)|` across the SnapPy `HTLinkExteriors` / `OrientableCuspedCensus` enumeration. The choice of `ρ_F ∈ {m_e, 2m_e}` is itself a free binary picked to match. **This is empirical fitting** in the CLAUDE.md production-vs-exploratory sense: a coefficient selected by minimising a CODATA residual, with no substrate-derived rule producing the same answer.

Per CLAUDE.md §production-vs-exploratory and the Rule-14 escalation protocol (§"Rule 14 — Author-escalation for off-menu coefficients" of the 2026-05-23 canonical-unification audit), this cannot remain in the production mass-prediction pipeline without either (a) a derivation from one of the 13 categorical drivers, or (b) explicit owner authorisation under conjecture-conditional status (analogous to PR #895's canonical-Wedderburn adoption — see [`docs/audits/2026-05-24-family-a-gap-audit.md`](2026-05-24-family-a-gap-audit.md) for that precedent).

## §2. Trace through the 13 categorical drivers

| # | Driver | Does it give a substrate-pure (Z, N) → K rule? | Verdict |
|---|--------|------------------------------------------------|---------|
| (i)   | Faddeev recursion Φ_q(qz) = (1−z)⁻¹·Φ_q(z) | Constrains q-deformation coefficients on a fixed link; does not select the link from (Z, N). | ❌ |
| (ii)  | Φ_q power-series log Φ_q(z) = Σ z^n / (n·(1−q^{2n})) | Same as (i) — coefficient machinery on a fixed object. | ❌ |
| (iii) | Rogers Li_2^q pentagon | 5-term relation between Li_2^q values; no topology-selection content. | ❌ |
| (iv)  | Yang-Baxter R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂ | Constrains braid-group representations; does not pick which braid the atom maps to. | ❌ |
| (v)   | Hexagon equations | Braiding ↔ fusion compatibility on the chosen category. Indifferent to (Z, N). | ❌ |
| (vi)  | Frobenius reciprocity / pairing | Duality of h^k coefficients on a fixed Hecke element. | ❌ |
| (vii) | Quantum 6j-symbols (Racah-Wigner) | Closed forms for partition-character products on H_n(q). Gives an atom → **partition** menu (Wedderburn block selection), **but not an atom → knot topology** — different partitions can share the same closed braid; same partition can host distinct closures. | 🟡 partial — Wedderburn side only |
| (viii)| Modular dual / S-transformation | Constrains asymptotics of Φ_q, Li_2^q at large h; not topology-selection. | ❌ |
| (ix)  | KLR positivity (canonical-basis non-negativity) | Filters which coefficients on a chosen basis can be observables. Constrains the **coefficient** of a knot-operator's contribution, not the **identity** of the knot. | 🟡 indirect — constrains coefficients, not topology |
| (x)   | MacMahon partition-algebra identities | h-expansions for partition-algebra weighted sums; no link-selection rule. | ❌ |
| (xi)  | Lobachevsky / Catalan-G identities | Transcendental ties between Vol values once a knot is chosen. | ❌ |
| (xii) | Chern-Simons / Ohtsuki perturbative series (WRT TQFT) | Atom-as-WRT-state interpretation: each WRT state on a 3-manifold M is labelled by a coloured link in M. **Potential canonical home** — the (Z, N) → WRT state-labelling could canonically select a representative link. Needs explicit construction; not yet in framework. | 🟡 **candidate categorical home** |
| (xiii)| Crystal-graph / Kashiwara q→0 | Atoms-as-crystal-paths: nucleus represented by a path in a Kashiwara crystal. The crystal graph is combinatorial and admits a canonical functor to braid words via the affine Schubert / Demazure machinery. Selecting the closed knot then becomes a Schubert-cell choice. | 🟡 **candidate categorical home** |

**Summary.** Eleven of the 13 drivers are categorically off-topic — they constrain *coefficients on a chosen topological object*, not the choice of object. Two plausible candidate categorical homes exist:

- **(xii) Chern-Simons / WRT.** An atom built as a WRT-coloured state on a punctured 3-manifold naturally carries a coloured-link representative; the (Z, N) → state-labelling would canonically pick the closure. Concrete construction is missing.
- **(xiii) Kashiwara crystal → Demazure → Schubert.** A nucleus path in the crystal could lift to a Bruhat element whose Schubert cell selects a closed braid. The CLAUDE.md §7b Demazure-subcrystal-for-resonances hint suggests this is on-framework for unstable resonances; the stable-atom version is not yet articulated.

Neither candidate currently delivers a rule mapping (Z, N) ↦ K. Both would require new content blocks.

## §3. Categorical question — is there a canonical `nucleus → knot` functor?

Existing content blocks under [`content/quantum-observable-universe/braids-and-knots/`](../../content/quantum-observable-universe/braids-and-knots/) define:

- [`atom-knot-exists.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-exists.md) — proves an atom-knot **exists** as a closed braid in H_{3(Z+N)}(q): it constructs `T_w = T_{w_qZ} · T_{w_q̄N} · T_{w_inter}` and Markov-closes. This proves existence; it does **not** pin the resulting knot to a specific census representative such as 6₂ / 8₁₁ / L6a4.
- [`isotope-knot-equivalence.md`](../../content/quantum-observable-universe/braids-and-knots/isotope-knot-equivalence.md) — proves the isotope equivalence relation respects the (Z, N) parameterisation. The equivalence-class machinery is canonical; the *representative* of each class is not.
- [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) — §"Where the gaps actually are" item 1 lists "Joint mass-tower confinement SDP — solver mode (R5-full)" as the open structural item. Item §"PSD-cone α* ranking" shows ³He ↔ L6a4 ranks PSD-feasible and is in the top 17 % of canonical-basis classes at L_max = 8 — **structural plausibility, not derivation**. ²H ↔ 6₂ is not PSD-feasible on its own (`α* = 0.89`) and ranks in the top 45 % — i.e. the census assignment is *not* the SDP-optimal canonical T_w for the deuteron.

**Conclusion:** the framework has a canonical *existence* theorem and an equivalence-class structure, but **no canonical `(Z, N) ↦ K_census` functor**. The R5-full SDP solver, when it lands, would supply the canonical T_w per atom; the resulting knot is then derived (Markov closure of the SDP solution), not census-fitted. Until R5-full lands, the census assignments are scaffolding.

## §4. What closure would unlock

If a canonical (Z, N) → K functor lands:

- Removes the highest-load-bearing 🔴 hidden-fitting candidate from the production mass-prediction chain (per the parent audit's ranked list).
- Decouples the +2.89 % / +1.09 % / −0.16 % / −2.97 % / +5.87 % low-isotope error pattern from any selection-bias contamination — current sign-flip diagnostic ([`docs/audits/2026-05-24-low-isotope-mass-error-anatomy.md §"Inter-nucleon channel counts vs error signs"`](2026-05-24-low-isotope-mass-error-anatomy.md)) cannot exclude that the census choice for D, T, ³He was already absorbing part of the channel-weight miscalibration.
- Closes the structural item §"Where the gaps actually are" #1 in [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md).

## §5. Recommended next step (owner decision required)

🟡 Awaiting owner pick — multi-select OK.

| # | Option | Cost | Scope | Trade-off |
|---|--------|------|-------|-----------|
| 1 | **Conjecture-conditional adoption** — accept the three census assignments as production with explicit owner authorisation (analogous to PR #895's canonical-Wedderburn move). Add a `conj:atom-knot-census-D-T-He3` block axiomatising the three pairings; mark `mass_table_ppb.py` rows as `conditional-on-conj`. | Low (1 content block + 1 commit). | Leaves the 🔴 risk visible in `conjectural-propagation-audit` output. | Unblocks Track-A downstream computations but does not solve the hidden-fitting concern; just makes it auditable. |
| 2 | **Author a new content block proposing a canonical `(Z, N) → K` functor** along one of: (xii) Chern-Simons/WRT atom-as-state, (xiii) Kashiwara-crystal-to-Schubert-cell, or the R5-full SDP solver output once it lands. | Medium-high (new prop block + Lean stub + canonical justification). | Genuine categorical closure; supersedes the census. | Requires substantial mathematical R&D; (xii) and (xiii) are 🟡-candidate homes only — neither delivers a rule out-of-the-box. |
| 3 | **Defer to R5-full SDP solver** ([`r5_full_canonical_knot_solver.py`](../../computations/r5_full_canonical_knot_solver.py) Python prototype, Rust port pending). When R5-full lands per-atom canonical T_w, derive K as `Markov.close(T_w)` and replace the census table. | Low (waiting cost only); R5-full is already in the workplan. | Cleanest categorical path. The current PSD-cone ranking shows ³He ↔ L6a4 is already plausible; ²H ↔ 6₂ may *change* under R5-full. | Wait time uncertain; current Python prototype defers H_5+ atoms (T at H_9, ⁴He at H_12) to Rust. |
| 4 | **Defer to PR #1081's Task 3 (S_5 ↔ SO(3))** if the structural source of the per-isotope knot is the S_5 fibre action on Bring's surface (per [`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md §3`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md)). The atom → knot would then be `(Z, N) → SO(3)-orbit → fibre-bundle-classifying knot`. | Low (waiting cost). | Could be the categorical home for the entire chain (matches (xii) WRT framing). | Speculative — needs an explicit construction Task 3 has not yet produced. |

**Recommended pick (default if no other input): combine option 1 + option 3** — adopt as conjecture-conditional now (cheap, restores auditability), explicitly tagged to be superseded by R5-full output. This matches the PR #895 precedent (production adoption under conjecture status, with a named replacement path).

## §6. Cross-references

- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md §"Rule 14"`](2026-05-23-lambda-scale-canonical-unification.md) — escalation protocol + 13-driver menu (parent rule).
- [`docs/audits/2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md) — parent audit, ranks this as 🔴 HIGH risk item #1.
- [`docs/audits/2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md`](2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md) — L1/L2/L3 three-layer framing; this audit addresses the **L1** atom→knot selection.
- [`docs/audits/2026-05-24-a5-a7-knot-census-candidates.md`](2026-05-24-a5-a7-knot-census-candidates.md) — sibling exploratory shape-probe for A ∈ {5, 6, 7}; explicitly flagged as "extends the hidden-fitting surface, owner-direction required".
- [`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md) — S_3 ⊂ SO(3) gap; relevant to option 4.
- [`docs/audits/2026-05-24-family-a-gap-audit.md`](2026-05-24-family-a-gap-audit.md) — PR #895 conjecture-conditional precedent.
- [`computations/mass_table_ppb.py`](../../computations/mass_table_ppb.py) — production script carrying the assignments (lines 18-21 docstring admission, lines 86-93 hardcoded table).
- [`computations/delta_lambda_jsj_phase3.py`](../../computations/delta_lambda_jsj_phase3.py) — JSJ verification / census-search implementation.
- [`content/quantum-observable-universe/braids-and-knots/atom-knot-exists.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-exists.md) — canonical existence; does not pin K.
- [`content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) §"Where the gaps actually are" #1 — R5-full SDP solver as the missing categorical step.
- [`computations/r5_full_canonical_knot_solver.py`](../../computations/r5_full_canonical_knot_solver.py) — Python R5-full prototype.
