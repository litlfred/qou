# Alien calculus ↔ surreal number integration review (2026-07-13)

**Status: COMPLETE — all six options EXECUTED on this branch (owner: "do all"), no production wiring.**

Execution record (2026-07-14):

| Option | Landed as |
|---|---|
| A (wiring + notation) | `st` + `ord_ω` rows in notation Table 10; new block `rem:st-is-median-resummation` (interprets `def:ecalle-borel-resummation`); cross-`uses[]` edges |
| B (median = st proposition) | `conj:surreal-limit-transfer` + `QOU/AppendixSurreals/SurrealLimitTransfer.lean` — content-bearing class, **no instance, no sorry**; two derived theorems fully proved (`standardPart_evalOmega_of_tendstoReal`, `tendstoReal_le_of_eventuallyLE`); verified `lean`-direct exit 0 |
| C (QM upgrade of 4₁) | `kashaev-surreal`: 4₁ instance now `=` (MM2001 + transfer equivalence), new §"Figure-eight discharge and quantum-modularity refinement" (GZ exact cocycle, GGM integer Stokes counts, Fantini–Rella template); bib entries `garoufalidis-gu-marino2021`, `fantini-rella2024` added; status authorNote |
| D (modular-resurgence probe) | `computations/probes/qbeta_modular_resurgence_stokes_probe.py` + audit-only witness. **Result (scope-(a)):** action consistent with Vol(4₁)/π within spread (rel. dev. 5.2%, Richardson over 5 exact triples); the naive β = 3/2 modular-weight reading of the as-normalized rung ladder **fails** (β_inf ≈ 0.44, raw trend ≈ 0.21–0.26; normalisation-sensitive, so this constrains the ladder normalisation, not the template); Stokes constant not identifiable at 7 rungs (best structured-grid candidate √(3/(2π)) at 0.15% — recorded under the 1/210 entropy bar, **not** claimed); L-function tower blocked. A_ω derivation route remains the GGM state-integral / 3d-index face (G3). |
| E (§7ab surreal-equality form) | AGENTS.md §7ab optional `X = Y + δ` (`ord_ω`-graded) recording form, explicitly L-tier |
| F (guardrail) | [`docs/surreal-analysis-guardrail.md`](../surreal-analysis-guardrail.md) — licensed vs forbidden analytic → surreal moves |

Validation note: the folio-assistant content pipeline is unavailable in
this sandbox; all `.md` edits passed the manual render-QA grep battery
but were **not machine-validated**. Lean changes verified via
`lean`-direct (exit 0) after lake-cache restore.

Scope: find linkage points between the alien-calculus/resurgence thread
(Borel–Écalle machinery, dilogarithm/transcendental data such as
Vol(4₁) = 2Λ(π/3)) and the surreal-number infrastructure
(`content/quantum-observable-universe/appendix-surreals/`); assess whether
transcendental arguments (inequalities, limits) can be recast as surreal
equalities; identify gaps a surreal reformulation could close or simplify.
Per the owner's mid-review directive, the **quantum-modularity** angle is
maximised (§4, Options C/D).

Method: two full corpus sweeps (alien-calculus thread; surreal
infrastructure) + literature verification. Companion PR: #3788.

---

## 1. Corpus state — alien-calculus / transcendental thread (summary)

Full inventory gathered in-session; load-bearing facts only:

- **Framework home is already inside the surreal appendix.** The Écalle
  machinery definition block `def:ecalle-borel-resummation` (Borel
  transform 𝓑, lateral/median Laplace sums, Stokes rays, alien derivative
  Δ_ω, bridge equation) lives in
  `content/quantum-observable-universe/appendix-surreals-archimedean/ecalle-borel-resummation.md`.
  The two threads are not "unintegrated" so much as **one-directionally
  integrated**: the surreal chapter reaches into resurgence; the
  resurgence/compute thread almost never cites the surreal home back.
- **Even face (mass/4₁):** C6 saddle-fluctuation transseries derived
  κ₁..κ₇ exactly (symbolic, e.g. κ₆ = (207892/295245)π⁶); Borel action
  A ≈ 0.646–0.657 consistent-within-spread with Vol(4₁)/π ≈ 0.6461
  (1.7%) but **not identified** (`docs/audits/2026-07-12-*`).
- **Odd face (Q_β/Φ_b):** the monodromy-datum gap **G3** — deriving the
  Stokes constant A_ω via Δ_ω — is the open keystone
  (`docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`);
  the dladder singularity is unresolved at k = 21 and no instanton action
  is claimed.
- **Lean-proved:** binding period is Gevrey-1/2 exactly
  (`QOU/Mass/BindingGevreyHalf.lean`, sorry-free integer sandwich);
  `BorelResummation.lean` proves the Gevrey-1 ⇒ Borel-disc-convergence
  half; Watson/Nevanlinna–Sokal **uniqueness** half is a documented
  Mathlib gap (`BorelWatsonUniqueness.lean` 1 sorry; sector/transport
  files in progress).
- **Refuted (scope-(a)):** deuteron full level-1/2 median Borel–Laplace
  undershoots B_D ~37× (`2026-07-13-deuteron-wall-full-transseries-negative.md`);
  full higher-instanton transseries route closed.
- **Transcendence is decorative, not load-bearing.**
  `predicted-spectra/hyperbolic-volume-transcendence.md` states
  explicitly that mass predictions depend only on proved numerical
  **distinctness** of the volumes, not on transcendence/irrationality;
  irrationality of Vol(4₁) = 2Cl₂(π/3) (an L(2,χ₋₃) value) is an open
  problem in the literature and is carried as honest conjecture blocks.
- **The one existing precise cross-link:** `appendix-surreals/kashaev-surreal.md`
  identifies the standard-part map with **Écalle median resummation** of
  the Kashaev transseries at a root of unity, and rewrites the volume
  conjecture as `Vol(S³∖K) =? st(2π·log|J_K(ζ_ω,ω)|/ω)` with n = ω,
  ζ_ω = e^{2πi/ω} via Berarducci–Mantova exp.

## 2. Corpus state — surreal infrastructure (summary)

- **Sorry-free kernel** (`lean/QOU/AppendixSurreals/`): `SurrealField`
  typeclass (axiomatised — Mathlib exposes no real-closed-field surreal
  witness), `StandardPart.lean` (st as ring hom + order-preserving, the
  most substantial artifact), `SignSequence.lean` (braid → No via Hecke
  eigenspaces, Gonshor map, birthday ≤ ω), `BirthdayGrading.lean`,
  `Blowup(Calculus).lean` (ε·ω = 1, `renormalise X C := st(X−C)`),
  `HoefsmitBridge.lean` (n ≤ 2), archimedean `ecalle-borel-resummation.lean`
  (`borelCoeff` over generic char-0 field).
- **Conjectural scaffolding** (§3b-cond classes with sorry-as-conjecture):
  `classical-limit-stpart` (cl_top ≅ St∘ev_{1+ε}), ε-relaxed axioms
  (`infinitesimal-observability`, `vacuum-epsilon`), millennium-bound
  blocks, `b1-hyperbolic-rows-theorem` (explicit `axiom`, reduces to the
  Volume Conjecture).
- **Standing owner ruling to respect:** the transcendental-surreal
  narrowing ledger (`docs/coordination/2026-06-08-transcendental-surreal-narrowing-ledger.md`)
  resolved **every** surreal narrowing as **L (language), not E
  (essential)** — "the corpus carries no surreal-necessary narrowing";
  `conj:hahn-substrate` was retired to `_deprecated/` as an internal
  negative (higher-order α_k are free parameters, not predictions). Any
  new linkage must not silently re-inflate surreal content from L to E.
- **Known missing analytic counterparts on No:** general integration
  (Costin–Ehrlich–Friedman: impossible for smooth-class in NBG−; exists
  for the semi-algebraic/analytic/**transserial** germ class), general
  limits (replaced piecewise by st∘ev, functoriality unproven), exp/log
  (only via Berarducci–Mantova, unformalized), hyperbolic geometry /
  metric completions, Hilbert-space machinery.

## 3. Literature verification (key bridges)

- **Surreals ↔ transseries.** Berarducci–Mantova, *Surreal numbers,
  derivations and transseries*, JEMS 20 (2018) — No with Gonshor exp IS
  a field of transseries with a Hardy-type derivation
  ([arXiv:1503.00315](https://arxiv.org/abs/1503.00315)).
  Aschenbrenner–van den Hoeven–van der Hoeven, *The surreal numbers as a
  universal H-field*, JEMS ([arXiv:1512.02267](https://arxiv.org/abs/1512.02267)) —
  every Hardy field embeds; BM embedding of transseries is elementary.
  Bagayoko–van der Hoeven, *The hyperserial field of surreal numbers*
  ([arXiv:2310.14873](https://arxiv.org/abs/2310.14873)) — E_{ω^α}, L_{ω^α}
  defined on No⁺∞; No is hyperserial. **Consequence: "evaluate a
  (trans)series at ω or at 1/ε" is a rigorous, published operation for
  precisely the transserial class — which is exactly the class median
  resummation produces.** The analytic → surreal highway exists in the
  literature and matches the corpus's st-median identification.
- **Surreal integration.** Costin–Ehrlich(–Friedman),
  [arXiv:1505.02478](https://arxiv.org/abs/1505.02478) and *Integration
  on the Surreals* ([arXiv:2208.14331](https://arxiv.org/abs/2208.14331),
  Adv. Math. 2024): genuine impossibility for general smooth classes;
  positive theory for Hardy-germ/transserial functions. Bounds ambition
  (Option F).
- **Quantum modularity (maximised per owner directive).**
  Garoufalidis–Zagier, *Knots, Perturbative Series and Quantum
  Modularity* ([arXiv:2111.06645](https://arxiv.org/abs/2111.06645)):
  matrix-valued SL₂(ℤ)-cocycle W_γ on ℚ extending to **holomorphic
  functions on cut planes** — the factorially divergent perturbative
  series Φ lifts to an **exact functional equation** (asymptotic
  inequality → equality), worked in detail for 4₁; companion *Knots and
  their related q-series* ([arXiv:2304.09377](https://arxiv.org/abs/2304.09377)).
  Garoufalidis–Gu–Mariño(–Wheeler): complete resurgent structure of the
  4₁ Kashaev series; **Stokes constants are integer counts tied to the
  3d-index / DGG data**
  ([arXiv:2111.04763](https://arxiv.org/abs/2111.04763);
  *The Resurgent Structure of Quantum Knot Invariants*, CMP 2021).
  Fantini–Rella, *Modular resurgent structures*
  ([arXiv:2404.11550](https://arxiv.org/abs/2404.11550)) and the
  q-Pochhammer sequel ([arXiv:2506.08265](https://arxiv.org/abs/2506.08265)):
  for modular resurgent series the Stokes constants are coefficients of
  an **L-function**; survey *Quantum modular forms and resurgence*
  ([arXiv:2505.00799](https://arxiv.org/abs/2505.00799)). Closed
  3-manifold case: [arXiv:2308.03265](https://arxiv.org/abs/2308.03265).
- **Formalization.** Mathlib has `SetTheory/Surreal/Basic` +
  `Surreal/Multiplication` (linear ordered comm **ring**; no field
  inverse, no exp, no sign-expansion API)
  ([docs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Surreal/Basic.html));
  Conway-normal-form formalization program:
  [arXiv:2410.00065](https://arxiv.org/abs/2410.00065). The appendix's
  axiomatised `SurrealField` remains the right call; a Mathlib-witness
  swap is not currently possible.

## 4. Synthesis — where the two threads actually meet

The meeting point is sharper than "both mention Écalle":

1. **st = median resummation** (`kashaev-surreal.md`) is the corpus's
   own bridge, already stated in prose with the right citation, but
   never promoted to a block-level identification, never registered in
   notation, and never cited from the compute-side thread.
2. **Quantum modularity is the inequality→equality machine.** Every
   transcendental *argument* in the corpus that uses a limit or an
   asymptotic estimate (Kashaev N→∞, saddle asymptotics, growth-class
   dichotomies) has, for 4₁ specifically, an **exact** counterpart in
   the GZ cocycle: W_γ satisfies a functional equation on the nose, with
   Vol(4₁) entering through e^{V/2πℏ} prefactors and the q ↔ q̃ modular
   pair. The corpus's `borel-zagier-qou-volumes`, `modular-s-transform-q-q-tilde`
   and `phi-q-aj-machinery-identification` blocks already gesture here.
3. **The surreal evaluation point is where the two become one
   statement**: a quantum-modular exact identity, evaluated at the
   surreal argument x = ω (BM/hyperserial exp makes ζ_ω = e^{2πi/ω}
   legal), with st extracting the real observable = median resummation
   selecting the real single-valued sum. Limits disappear from the
   *statement*; they survive only inside the cited literature theorem.
4. **What surreals cannot do:** fix magnitude-refuted routes (deuteron
   37× undershoot is representation-independent), prove irrationality of
   Vol(4₁), or supply a general integral (CEF). Any option claiming
   otherwise would be laundering.

## 5. Option menu

Tier legend: cost = agent-days scale; risk = chance of dead end or
policy conflict; all options honour the anti-fit rules and the all-L
narrowing ledger unless explicitly stated.

**A. Wiring + notation pass (cheap, do-first).** Register `st` and
`ord_ω` in the notation register (utilization-audit items E2/G5, already
proposed, never executed); add `uses[]` edges so the resurgence blocks
(`def:ecalle-borel-resummation`, `rem:dilog-saddle-regime`, Borel/alien
witnesses) and the surreal blocks (`kashaev-surreal`, blow-up calculus)
cite each other; promote "st = median resummation" from prose inside
`kashaev-surreal.md` to its own `remark` block with `interprets:
def:ecalle-borel-resummation`. Cost: hours. Risk: nil. Payoff: the two
threads become discoverable from each other; fixes the one-directional
citation graph.

**B. "Median sum = standard part" as a conditional proposition (the
theorem-shaped bridge).** New block + Lean: for a Gevrey-1 series
Borel-summable along ℝ⁺, the median Laplace–Borel value equals
st(evaluation of the BM-transseries at ε = 1/ω). States the analytic →
surreal move once, as a §3b-cond conditional class layered on the
existing sorry-free `BorelResummation.lean` + `SurrealField` +
`StandardPart.lean`. First concrete instance: the Lean-proved
Gevrey-1/2 binding period. Cost: days. Risk: low-medium (BM exp is not
formalized; keep it class-level). Payoff: every future "lim/≲/O(·)"
statement in the resurgence thread can be restated as a surreal
equality by citing one block.

**C. Quantum-modularity upgrade of the 4₁ row (highest gap-closing
value).** The surreal appendix's `b1-hyperbolic-rows-theorem` carries an
explicit `axiom` because it reduces to the general Volume Conjecture.
But the mass anchor only needs the **4₁ row**, and for 4₁ the
asymptotics is covered by the Garoufalidis–Zagier quantum-modularity
results (exact cocycle, worked 4₁ case). Split the 4₁ row out and
discharge it as a cited-literature class instance (same pattern as
`volumeConjecture41_of_literature`), demoting the axiom to the genuinely
open non-4₁ rows. Simultaneously restate the Kashaev-surreal identity
for 4₁ with `=` instead of `=?`, conditional on the GZ class. Cost:
days. Risk: low (literature-citation discipline already exists). Payoff:
the muon-anchor chain's conditionality weakens from "full KVC" to
"published 4₁ quantum modularity" — a real epistemic upgrade, and the
first place a transcendental *limit* argument becomes a cited *equality*.

**D. G3 keystone attack via modular resurgence (research-grade).** Test
Fantini–Rella modular-resurgence predictions on the corpus's own data:
are the κ-tower / dladder Stokes constants the coefficients of an
L-function / 3d-index integer counts (GGM) for 4₁? A probe comparing the
measured alien datum (`lever1-bridge-alien-datum.witness.json`,
A_ω ≈ 3.8884) and the unresolved odd-face Stokes constant against
DGG/3d-index counts would, on success, turn A_ω into a **derived integer
count** — exactly the "derivation, not fit" the G3 monodromy gap needs.
Surreal tie-in: the q̃-side lives at the ω-scale; birthday grading is
the natural filtration of the (q, q̃) bimodular pair. Cost: 1-2 weeks.
Risk: medium-high (may be scope-(a) negative). Payoff: the single
biggest open item in the alien thread.

**E. Approximation-convention lift (language-level, cheap).** Extend the
§7ab convention: every "X ≈ Y" derived-value statement may optionally be
recorded as the surreal equality X = Y + δ with an `ord_ω`-graded
remainder δ, using the existing blow-up calculus. Honest framing: this
is bookkeeping (per the all-L ruling), not new math — but it makes the
"calculus up to ε" arc uniform and machine-checkable. Cost: hours-days.
Risk: nil if framed as L.

**F. Surreal-analysis guardrail doc (defensive, cheap).** A short
`docs/` guardrail (pattern: `canonical-mass-formula-guardrail.md`)
recording which analytic → surreal moves are *licensed* (transserial/
Hardy-germ class: BM/ADH/Bagayoko–vdH; st; median resummation) and which
are *forbidden or open* (general surreal integration per CEF, spectral
theory, generic limits) — so future agents don't chase surreal
integration rainbows. Cost: hours. Risk: nil.

**Recommended sequencing:** A + C first (cheap wiring + the one genuine
gap-closing move), then B (makes the pattern reusable), D as the
research bet, E/F opportunistic.

## 6. Corpus-grep checklist compliance

Prior art checked: `docs/audits/2026-07-12-borel-alien-calculus-utilization-audit.md`
(proposed E2/G5 = option A's notation half; never executed),
`2026-06-08-transcendental-surreal-narrowing-ledger.md` (all-L ruling —
options E is explicitly L; C/D add *quantum-modularity* content hosted
at the surreal evaluation point, not a claim that surreals are
physically necessary), `kashaev-surreal.md` (st = median resummation
already present as prose). No option above re-opens a refuted route
(deuteron transseries, full higher-instanton tower, hahn-substrate).
