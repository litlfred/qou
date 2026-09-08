# Two research fronts, two initial plans — route C step 3 (the log-trace question) and the KZ-level construction

**Date:** 2026-09-07. **Owner instruction (verbatim):** *"Merge. And both research. Dispatch agents for initial plans. Then coordinate on foreground."* **Beans:** `qou-8uxw` (route C), `qou-d0qq` (Step-2 option C). **PR:** #7035.

Two planning agents were dispatched under the dispatch-agent progress contract, read-only on the
tree, with the NO-FITTING rule, the six-path corpus-grep, the scope-(a)/(b) discipline and the
substrate-`q₀` forever-gate written into their briefs. Their plans are reproduced **verbatim** in
§A and §B; §0 is the parent's verification of their corpus claims and the coordination decision.

## 0. Parent verification and the execution queue

**Verification (the DONE line is a claim; these were re-read against the tree).**

- Route C plan: all thirteen `file:line` citations resolve to the declarations named
  (`MarkovBondRuleForcesPairwise.lean:148/178/185/195`, `FormalityBridgeF1.lean:84/94/108`,
  `MarkovBondFactor.lean:46/76/87`, `CrossTermOrderZeroComponentCount.lean:46/83`,
  `AmeBindingNotPairwise.lean:24`, `RouteCPivotalVsCount.lean:91`). Two small corrections:
  `chi_general_word` is the module `computations/chi_general_word.py` (not a function inside
  `atom_bond_product_closed_form_probe.py`); the canonical word `[0,1,0,1,0,1,0,0,1,0,0]` sits at
  `.beans/qou-wdij…:275` (and `chi_general_word.py:24`), line 272 is the section heading. The
  S2 arithmetic checks: `E₀·ln 2 = 4.186 × 0.6931 = 2.902` MeV and `1.4262/2.902 = 0.491`, not an
  integer. BHW held at `library/arxiv-0908.4305v3`; Leinster absent from `library/INDEX.md` (0 hits).
- KZ plan: `KZUnitModulusPrune.lean:30`, `HeckeMonodromy.lean:52`, `FourTermRelation.lean:18/93`,
  `NaStokesKeystone.lean:24`, both probes, and `trace-convention-registry.md:432-446`
  (`loop_reciprocal`) all resolve. The three prose sites are real — `lifted-crossing-locality.md:15`
  ("guaranteed at the generic physical substrate $q_0$ where the KZ connection is flat"),
  `q-holonomy-locality-derivation.md:36` ("At the pinned parameter $q_0 ≈ 1.11$, the KZ connection is
  flat"), `vertex-operator-dictionary.md:1`. One correction: the registry key is `drinfeld1985`
  (`references.ts:8623`), not "Drinfeld 1990"; `kohno1987` and `kassel1995` are cited and not held, as
  the plan says. The P2 identity `z_D = (q[3]_q − q⁻¹)/[2]_q²` is the same computation this session
  made in `RouteCPivotalVsCount` (§7h of the survey), so it is doubly confirmed.

**Coordination decision (judgement, parent).** The two fronts share no files and no beans, so they
run in parallel. Ordered queue, cheapest decisive step first on each:

| # | front | step | why first | cost |
|---|---|---|---|---|
| A1 | route C | **S3** — exact-in-`q` bond factorisation of the canonical non-monotone word at `n = 9` (`ppn`, `pnn`, each interface) | the only undecided fact on the front; either closes route C on the production word (scope-(b), invariant = the identity) or exhibits the first many-body term with its `q`-adic order | 3–5 h |
| A2 | route C | **S2** Lean — the classical part of any route-C `b₃` is `E₀·ln 2·m`, `m ∈ ℤ` | one hour; kills the census-word reading at `E₀` without choosing a word | 1–2 h |
| B1 | KZ | **P5** probe — the braid word of each of the six lassos of `colour_cubic_branch_monodromy_probe.py`, conjugate to `σ_i^{±1}` or not | the one genuine unknown on the front | 2 h |
| B2 | KZ | **P2** Lean — `z_D` is the `U_q(sl₂)` fundamental quantum trace; `z_3 ≠ z_D` | exact, `q₀`-free, registers where convention D comes from | 2 h |
| B3 | KZ | **P3** Lean + prose — flatness is level-independent; reword the three "flat at `q₀`" sites | corrects a false claim in two content blocks | 1 h + render-QA |
| A3/B4 | both | S1 convolution lemma; P1 six-distinct-roots lemma | cheap, closes the two "is the base/union hiding it" worries | 1 h each |
| B5 | KZ | rewrite the conjecture's open remainder; retitle `qou-d0qq` (its title still says *"does any level reproduce q₀"*, gate-violating wording) | bean hygiene | 1 h |

Not queued: any literature acquisition (Leinster; Kohno 1987 / Drinfeld 1985 ingestion is a §8-style
chore, bean-worthy, not blocking).

**What nobody acting would mean.** Both beans stay in-progress with plans attached; no number
moves; the three prose sites keep asserting level-dependent flatness.

## 0b. Execution results, same day (parent-verified: every probe re-run by the parent, every Lean file lean-direct by the parent)

| step | result | evidence |
|---|---|---|
| **A1** exact bond factorisation, `n = 9` | **Holds identically** — `C(β₁₂₃)·C(β_free) = C(β₁₂)·C(β₂₃)` as Laurent polynomials in `q` for all four compositions `ppn, pnn, ppp, nnn`; `(q−1)`-adic order ∞, no leading coefficient. Stronger: each bond contributes exactly the Markov scalar of its interface letter, `C(β₁₂)/C(β_free) = q·(z_D + d_bond)` (`pp → q⁴/(q²+1)`, `nn → 1/(q²+1)`, `pn → q·(z_D − h(½ − δ/4))`), the same factor whether the other interface is on or off. The ε²-order series of `atom_bond_product_closed_form_probe.py` is the truncation of these exact factors (4/4). | `computations/probes/route_c_step3_bond_factorisation_exact_probe.py` (536 lines, big-integer evaluation on weight sectors + Newton interpolation over `Fraction`, verified at three unused `q`), witness `route-c-step3-bond-factorisation-exact.witness.json`, **76/76**, parent re-run exit 0 in 31 s. Words from `canonical_braid_crossings.atom_canonical_crossings` → `mass_at_3A_proper.atom_braid_word_3A` (`bring_color_weighted`), nothing re-typed. |
| **A2/S2** classical quantisation | Folded into A1's diagnostic: with `Δ ≡ 0` there is no classical term to quantise on the chain word; the arithmetic `E₀·ln 2 = 2.902` MeV, `1.4262/2.902 = 0.491 ∉ ℤ` stands as recorded in §A. No Lean file: `log₂ 2^{c−n} = c − n` is definitional (Strict Lean Discipline rule 8), not a theorem. | — |
| **S1/A3** convolution | `QOU/Mass/WeightedCountConvolution.lean`: `weighted (P*Q) (n₁+n₂) x = weighted P n₁ x · weighted Q n₂ x`, `weighted_pow`. Sorry-free, generic field. | commit `68301ad0d6` |
| **B1/P5** lasso braid words | **All six lassos are positive half-twists**, conjugacy to `σ_i^{+1}` **established** (explicit ≤ 2-letter conjugators, verified in a hand-rolled `B₃` left-normal form and in the faithful Burau representation; super-summit set `{σ₁, σ₂}` for every lasso). Product of the six in departure order `= Δ²` = the independently continued loop at infinity. 50 dps continuation, 0 bisections, min root separation ≥ 0.45. | `computations/probes/colour_cubic_braid_monodromy_probe.py` (675 lines), witness `colour-cubic-braid-monodromy.witness.json`, **13/13**, `q0Anchor: independent`; parent re-run exit 0 in 17.5 s; parent grep: zero `float(`/`math`/`numpy`, zero `q_parameter` reads. |
| **B2/P2** `z_D` is `𝔰𝔩₂` | `QOU/Mass/SL2QuantumTraceIsZD.lean`: `zSL2 = q³/(q²+1) = z_D`; `zSL3 = q⁵/(q⁴+q²+1)`; `zSL3 ≠ zD` over **every** field (equality forces `q³ = 0`) — no archimedean inequality needed. | commit `1e9962b189`, axioms standard |
| **B3/P3** flatness level-independent | `QOU/Mass/KZFlatnessLevelIndependent.lean`: `InfinitesimalBraidRelations t → InfinitesimalBraidRelations (c • t)`; the two "flat at `q₀`" prose sites reworded to semisimplicity. | commit `7bfa2bc9d5`, axioms `propext, Quot.sound` |
| **B5** bean hygiene | `qou-d0qq` retitled to the gate-clean question. | commit `68301ad0d6` |

**What the two fronts now say, in physics-and-paper terms.**

*Route C.* On the production chain word the fixed-point groupoid factors over bonds exactly, at every
order in `q`, at `A = 3`: `b₃ ≡ 0` there is now a scope-(b) statement with the polynomial identity as
its invariant (general `A` still wants the disjoint-block Lean lemma, `MarkovBondFactor` general
case, bean `qou-g8i1`). So the measured `b₃ = 1.4262` MeV cannot come from the chain word's trace at
any `q`-adic order — a route-C many-body term needs a **non-chain word class** (the Brunnian /
component-changing classes of §7g) or something **outside the trace**. This closes route C on the
production word honestly rather than by fatigue, exactly as the plan's recommendation anticipated.

*KZ front.* Every prune passed in the positive direction: the target algebra is `𝔰𝔩₂` (and not
`𝔰𝔩₃`, over any field), flatness cannot single out a level, and every monodromy generator of the
`𝔰𝔩₂` KZ connection pulled back along the root map is a conjugate of `ϱ(σ_i)`, so by Kohno–Drinfeld
(cited, `kohno1987`, not held) the Hecke quadratic `(σ − q)(σ + q⁻¹) = 0` follows with the level's `q`.
The identification question of `qou-d0qq` is therefore reduced to a **conditional class with one
named hypothesis** — that the substrate connection *is* that pulled-back KZ connection at the level
`k + 2 = iπ/ln q₀` (Kohno's convention) — and `q₀` enters only as that label. What is *not* done: the
content block `conj:hecke-monodromy-step-two` does not yet carry that hypothesis as a field (plan
step 5), and Kohno 1987 / Drinfeld 1985 are not in `library/` (plan step 6).

**Gates.** `precision-gates.sh --changed` (run four times on this branch): the red list is
`main`'s standing set; the only mention of either new probe in any log is the branch name.
Gate-regenerated audit witnesses were reverted by explicit lists excluding this branch's files.

---

## A. Route C step 3 — plan (agent `routec-log`, verbatim)

# Route C step 3 — plan

**Constraints repeated.** NO FITTING: no parameter, cutoff, word or partition chosen because it reproduces a binding; each step ends in a derived statement or an honest negative. Substrate-`q₀` derivation is FOREVER GATED; nothing below routes through it (all statements are Laurent-polynomial identities in formal `q`, evaluated at the proton pin only as a diagnostic). No seventh fit-based ansatz for the Δ_λ magnitude. Scope-(a) vs (b) marked, (b) only with the invariant named.

## 0. The decision, in one paragraph

The "log of a cardinality is not a cardinality" framing is **not a new invariant** — it is the statement `log` is a monoid homomorphism, which the corpus already proved forces `b₃ = 0` from any bond product (`QOU.Mass.MarkovBondRuleForcesPairwise.b3_eq_zero_of_bondRule`, L178; composed with the ordering hypothesis in `QOU.Mass.FormalityBridgeF1.f_tr_stabWord_eq_sum`, L84). What the groupoid picture of §7h actually sharpens is *which sets must biject*: with `C(w) := q^{l(w)}[2]_q^n tr_D(w) = |⊔_k Fix_k(w) × A_k|` (weighted fixed-colouring count over `𝔽_{q²}`), "the fixed-point groupoid factors over bonds" means the polynomial identity `C(atom)·C(free) = ∏ C(one-bond words)`-shape, i.e. at every prime power a weight-preserving bijection of colouring sets. The decision is therefore: (1) prove two cheap prunes in Lean that dispose of the disjoint-union-over-`k` worry and quantise the classical part of `b₃`; then (2) run one exact computation the corpus does not have — whether the **canonical, non-monotone** nucleon word (`[0,1,0,1,0,1,0,0,1,0,0]`, bean `qou-wdij` L272) satisfies bond factorisation **exactly in `q`** at `n = 9` (`A = 3`), not merely to `ε²` as currently measured. Its outcome either closes route C on the production word (scope-(b), invariant = the identity) or exhibits the first genuine many-body term on the production word with its `q`-adic order.

## 1. What the corpus already holds

- Bond product ⇒ `b₃ = b₄ = 0` for *any* `f(xy) = f x + f y` (no continuity): `QOU/Mass/MarkovBondRuleForcesPairwise.lean:148,178,185`; the converse-shaped `no_traceFunctional_of_b3_ne_zero` L195.
- Monotone word ⇒ letter product; interleaved `n = 4` word ⇒ not a bond sum (exact cross term `z(z²−hz−1)`): `QOU/Mass/FormalityBridgeF1.lean:84,94,108`; `QOU/MathlibExt/MonotoneWordTraceFactorizes.lean`.
- Per-bond and two-bond trace factorisation, sorry-free; general `A`-bond case **open** ("needs the cross-level Markov axiom"): `QOU/Hecke/MarkovBondFactor.lean:46,76,87`. Bean `qou-g8i1`: gap-multiplicativity is "mechanism, NOT a Lean proof".
- Order-zero cross term = component-count difference, vanishing iff `c(w) = c(w′)`: `QOU/Mass/CrossTermOrderZeroComponentCount.lean:46`; Brunnian 3-body deficit `≤ h⁴` L83 (audit §7g: 78× too small at `E₀`).
- Convention-D trace is a BHW weighted groupoid cardinality for every `n`: audit §7h; probe witness `route-c-step2-pivotal-vs-count.witness.json` (26/26); `QOU/Mass/RouteCPivotalVsCount.lean:91`.
- Canonical nucleon word is non-monotone; block-and-bond product measured only to `ε²`, `A ≤ 5`, sorted orderings; "disjoint-block Lean gap" named: `.beans/qou-wdij…md:272–300`, `computations/probes/atom_bond_product_closed_form_probe.py`.
- Measured target: `b₃ = 2852445/2000000 = 1.4262225` MeV, `QOU/MassTheory/AmeBindingNotPairwise.lean:24`. (A second, different figure `μ₃ ≈ 0.4708` MeV lives in the Δ_λ audit; §7g compares against that one — the two targets are not reconciled anywhere I found.)
- Library (paths 5, all four tiers; 661 dirs / 614 index rows): **held** BHW `library/arxiv-0908.4305v3` (§4.2 Hecke algebras — over `𝔽_q`, no Markov trace, no pivotal weight), Baez–Dolan `arxiv-math-0004133v1`, Morton `arxiv-0810.2361v2`, `arxiv-math-0601458v1`. **Not held**: Leinster "Euler characteristic of a category" (cited only in the references of 0908.4305v3 and 0801.0083v4); anything on *weighted/graded* groupoid cardinality or on *logs* of cardinalities (Baez–Fritz–Leinster entropy characterisation) — zero hits in `sections/` and `ocr/`.
- Six-path grep for "log of cardinality", "fixed-point groupoid", "product groupoid binding", "factorisation of the fixed-point set": **empty** outside the route-C files (scratch `corpus-grep.txt`). "Bond factorisation" hits are all the trace-level results above.

## 2. Candidate statements

**S1 (prune, Lean-provable, cheap): the disjoint union over `k` forces neither factorisation nor non-factorisation.** Claim: for disjoint juxtaposition `w₁ ⊔ w₂` (tensor product), `N_k(w₁⊔w₂) = Σ_{k₁+k₂=k} N_{k₁}(w₁) N_{k₂}(w₂)` and the weight `q^{n−2k}` is multiplicative, hence `C(w₁⊔w₂) = C(w₁)C(w₂)` — a convolution identity over `CommRing R` (Mathlib `Finset.sum_mul_sum` / antidiagonal). Expected: holds. Consequence: `log C` is additive over *blocks* by construction; the `k`-union is a red herring, and non-factorisation over *bonds* is decided by word topology alone — exactly F1's ordering hypothesis. Kills the hypothesis "the `⊔_k` structure is where `b₃` hides".

**S2 (prune, Lean-provable, cheap): the classical part of any route-C `b₃` is quantised.** At `q = 1`, `B = E₀·log 2·(c_free − c_atom)` (`componentTrace`), so the order-zero connected 3-body cumulant of *any* word assignment is `E₀·log 2·m`, `m ∈ ℤ`; for a bond chain whose bonds merge cycles independently, `m = 0`. Expected: holds (integer arithmetic on `c`). Diagnostic at the comparison boundary (not a fit): `E₀·log 2 = 4.186 × 0.6931 = 2.902` MeV, and `1.4262/2.902 = 0.49` is not an integer — so **scope-(a)**: no classical fixed-point-count difference on any word reproduces the measured `b₃` at scale `E₀`; a route-C `b₃` must be of `q`-adic order ≥ 1 (first-order unit `E₀·h ≈ 0.87` MeV at the pin). This forecloses the component-changing "census word" reading of §7g without touching any word choice.

**S3 (the survivor, computational): exact bond factorisation of the canonical non-monotone word.** Claim: with `β_free` = three disjoint nucleon blocks (`n = 9`), `β_{12}`, `β_{23}` = one interface on, `β_{123}` = both, `C(β_{123})·C(β_free) = C(β_{12})·C(β_{23})` **as Laurent polynomials in `q`** (equivalently `tr_D` identity), for `ppn` and `pnn`, each interface type. Two outcomes, both derived: (i) holds identically ⇒ the production word's fixed-point groupoid factors over bonds; `b₃ ≡ 0` on it at every order in `q` at `A = 3` (scope-(b) at `n = 9`, invariant = the identity; general `A` then wants the disjoint-block Lean lemma that `qou-wdij` names) ⇒ route C cannot reach `b₃` on the production word, the term must come from a non-chain word class or from outside the trace; (ii) fails at order `ε^m`, `m ≥ 3` ⇒ first genuine many-body term on the production word, with its `q`-adic order and exact coefficient — reportable as `E₀·h^m·(rational)` against `1.4262` MeV without fitting.

**Not a candidate: "weighted groupoid cardinality" as a literature gap.** §7h already realised the weight as `|𝔽_q^{n−2k}|` / `|B(𝔽_q^{2k−n})|`; nothing further is needed from the library for S1–S3.

## 3. Ordered steps

| # | step | cost | risk | forecloses | produces |
|---|---|---|---|---|---|
| 1 | **S2 in Lean**: `classicalB3_eq_int_mul` over `ℚ` in `CrossTermOrderZeroComponentCount` style; chain instance `m = 0` | 1–2 h | low (integer arithmetic) | classical route-C `b₃` at `E₀`; census-word reading | `QOU/Mass/RouteCLogCardinalityClassical.lean`, `lean -DautoImplicit=false -s 65536` exit 0 |
| 2 | **S3 compute**: extend `atom_bond_product_closed_form_probe.py` to exact-in-`q`: integer `T_i = qσ_i` (entries `q², q²−1, q`) acting sparsely on the 512 basis vectors of `V^{⊗9}`, evaluated at ≥ `2·l(w)+10` integer `q`, exact Lagrange interpolation over `Fraction`, verified at extra prime powers; report `C(123)C(free) − C(12)C(23)` and its `(q−1)`-adic order | 3–5 h; runtime minutes | medium: getting the canonical word/ordering exactly as `chi_general_word` does (reuse its generator; do not re-type the word) | either route C on the production word (outcome i) or the "no many-body term on the chain" assumption (ii) | `computations/probes/route_c_step3_bond_factorisation_exact_probe.py` + witness (`q0Anchor: independent`; pin only for a diagnostic line) |
| 3 | **S1 in Lean**: convolution identity `Σ_k x^{-2k}(a∗b)_k = (Σ x^{-2i}a_i)(Σ x^{-2j}b_j)` | 1 h | low | the "`⊔_k` hides `b₃`" hypothesis | `QOU/Mass/WeightedCountConvolution.lean` |
| 4 | If S3 outcome (i): formalise gap-multiplicativity for **disjoint blocks with interior bond crossings** (the `MarkovBondFactor` general-`A` gap, `qou-g8i1`) — this is what turns (i) into scope-(b) for all `A` | 4–8 h | high (needs the cross-level Markov axiom the class lacks) | — | extension of `QOU/Hecke/MarkovBondFactor.lean` |
| 5 | Write audit §7i + bean updates (`qou-8uxw`, `qou-wdij`, `qou-brng`) | 1 h | — | — | audit section, beans |

Skip: any literature acquisition (Leinster; Baez–Fritz–Leinster) — nothing in S1–S3 depends on it; log a low-priority bean at most.

## 4. Default if nobody acts

Nothing changes. `qou-8uxw` stays in-progress at step 2; the production word's bond factorisation stays "measured to `ε²`"; `b₃` stays unlocated. No production number moves either way.

## 5. Recommendation (judgement)

Do steps 1 → 2 → 5 in that order (≈ 6–8 h total). Step 2 is the only genuinely undecided fact on this front and it is cheap and exact; step 1 costs an hour and removes an entire class of word-hunting before it starts. Step 3 is a nice-to-have; step 4 only if step 2 returns outcome (i). My expectation is outcome (i) — `qou-g8i1`'s gap-multiplicativity argument (commuting subalgebras across an unused generator) does not use monotonicity inside the blocks — which would close route C on the production word honestly rather than by fatigue.

---

## B. Bean `qou-d0qq`, Step-2 option C — plan (agent `kz-level`, verbatim)

# Plan — bean `qou-d0qq`, Step-2 option C (KZ-type connection, imaginary level)

**Hard constraints, repeated.** NO FITTING. `q₀`-derivation is FOREVER GATED — `q₀` is an *input* that fixes the level; no step below outputs a value of `q₀`. Every negative is scope-(a) unless a proved invariant licenses (b). Every Lean proposal states a falsifiable proposition; no `True` placeholders; no `sorry` without `-- Ref:`.

## 0. The decision in one paragraph

The bean's stated next step — "write the KZ connection on the configuration space of the six branch points and compute its monodromy exactly" — is **ill-posed as written and should be replaced** by a two-line identification that is already mostly a theorem. The six branch points of the colour cubic are *fixed* numbers (roots of `D(z) = 16z⁶+…+16`), so the base is `ℂ ∖ {6 points}` with fundamental group the free group `F₆`, not a braid group; a Knizhnik–Zamolodchikov (KZ) connection lives on `Conf_n(ℂ)` (the corpus's own base, `q-holonomy-locality-derivation.md:7`), so the only construction that makes the bean meaningful is the **pullback of the sl₂ KZ connection on `Conf₃(ℂ)` along the root map** `z ↦ {X₁,X₂,X₃}(z)`, i.e. the composite `F₆ → B₃ → H₃(q)`. Once stated that way, Kohno–Drinfeld makes the Hecke quadratic automatic, and the framework's convention-D Markov parameter `z_D = q³/(q²+1)` turns out to be *exactly* the U_q(sl₂) fundamental-representation quantum trace of the R-matrix — measured this session at 30 dps (diff 5e-31) and already recorded in another guise (`trace-convention-registry.md:432-446`, `loop_reciprocal`). The imaginary level is not an obstacle: it is only the relabelling `ħ = ln q₀/(iπ)` of a formal-`ħ` identity. What remains genuinely open is one thing — whether each lasso's lift to `B₃` is a half-twist — and that is a cheap exact computation, not research.

## 1. What the corpus already holds

| item | where |
|---|---|
| Real-level prune (unit-modulus ≠ real `q₀`) | `QOU/Mass/KZUnitModulusPrune.lean:30-45` (2 theorems) |
| Step 2 as §3b class, 4 content fields; `q=1` shadow is Coxeter | `QOU/Mass/HeckeMonodromy.lean:52-67`, `:75-144` |
| Discriminant reciprocal / sum-of-squares / no real root | `QOU/Mass/ColourCubicDiscriminant.lean:40-77`, `…Real.lean:24-37`; **duplicated** by `QOU.Brings.ColourCubicBranchLocus` (noted at `Brings/ColourCubicDiscriminant.lean:12-20`) |
| Kohno–Drinfeld infinitesimal braid relation `[t_ij, t_ik+t_jk]=0` | `QOU/KnotTheory/Vassiliev/FourTermRelation.lean:18,93` |
| Probe: six simple branch points, each local monodromy a transposition, group `S₃`, 11/11, mpmath 50 dps | `computations/probes/colour_cubic_branch_monodromy_probe.py` |
| KZ ↔ Hecke eigenvalue matching already forces `ħ = 2 ln q`, `det A = −(ln q)²` (hyperbolic at real `q₀`, elliptic iff `|q|=1`) — the same "imaginary level" fact | `computations/qbeta/qbeta_fibre_unit_circle_opens_route5_probe.py` §1 |
| `z_D` ↔ Temperley–Lieb loop `δ=[2]_q`, `tr_M(e_i)=1/δ` exact | `docs/coordination/trace-convention-registry.md:432-446`; `QOU/QBeta/TemperleyLiebTower.lean` `loop_reciprocal` |
| Prose saying KZ is "flat at `q₀`", `q = e^{2πi/(k+2)}` | `mass-theory/lifted-crossing-locality.md:15`, `vertex-operator-dictionary.md:1-3`, `nuclear-interactions/q-holonomy-locality-derivation.md:36` |
| Library: GGOR KZ-functor (`library/hdr/sections/sec-018…:181-206`), WZW/KZ monodromy (`library/monodromyhitchiny/sections/sec-019…:35`), quantum KZ / R-matrices (`library/arxiv-math-0203003v2/sections/sec-000…:19-28`), hypergeometric monodromy (`deligne-mostow-1986`). **Not held:** Kohno 1987, Drinfeld 1990 (associator), Kassel 1995 — cited only, `content/schema/references.ts:6111,8623,3133`. |
| Six-path grep: "imaginary/non-unitary level" exists only in the 2026-09-06 arc (3 files); "KZ/Kohno" in 11 beans, ~20 audits, 30 content files (mostly `QBeta/*Eigenphase*`), 10 probes — none constructs a connection. |

## 2. What "the framework's connection" currently IS

Nothing but the conjecture class. `NaStokesKeystone.lean:20-24` now says the abelianised Cartan connection on `S_c` is *conjectured* to have curvature `F(σ)`; cheat-sheet §2a (`docs/canonical-derivation-cheat-sheet.md:212-238`) records no form, no connection, no surface. The class `HeckeMonodromy` (`HeckeMonodromy.lean:52-67`) is a *property of a representation* `ϱ: B_n → H_n(q)`, not a connection. So the bean's question "is the framework's connection this KZ one?" is empty as posed. **For it to be well-posed** the framework side must supply the same kind of object as Kohno–Drinfeld's input: a flat connection on a configuration space with values in `End(V^{⊗n})` for a named `𝔤` and `V`. The only candidate in the corpus is the prose's "KZ on `X_n`" with `𝔤 = sl₂` (`vertex-operator-dictionary.md:1`: "R-matrix of `U_q(su₂)`"), so the identification question collapses to: *does the sl₂ KZ connection on `Conf₃(ℂ)`, pulled back along the colour cubic's root map, have monodromy generators satisfying the framework's quadratic and trace conventions?*

## 3. Candidate prunes (formalize-first)

**P1 — base is not a braid group (Lean-provable, expected: the bean's base is wrong).** Claim: the six branch points are fixed; `ℂ∖Δ` has `π₁ = F₆`; the braid group `B₃` enters only via the root map. Lean: `colourDiscriminant` has six distinct roots (`Polynomial.natDegree = 6`, separable — `discriminant ≠ 0` of `D`, exact integer) — falsifiable, cheap. Consequence: replace "Conf of the six branch points" by "pullback along `z ↦ roots(P(·,z))`".

**P2 — target algebra is sl₂, not sl₃ (exact, Lean-provable, expected PASS).** Claim: with the framework's normalisation (eigenvalue `q` on Sym², `−q⁻¹` on Λ²), the quantum-trace Markov parameter of `U_q(sl_N)` fundamental is `z_N = (q·dim_q Sym²V − q⁻¹·dim_q Λ²V)/[N]_q²`; for `N=2` this is `(q[3]_q − q⁻¹)/[2]_q² = q³/(q²+1) = z_D` (measured: diff 5e-31 at the proton pin), for `N=3` it is `0.4493 ≠ 0.6127`. Lean: the `N=2` identity is a `field_simp; ring` over a generic field; the `N=3` inequality at any `q>1` is archimedean (its own file). This is the *positive* identification check and it is `q₀`-free. Note it strengthens, not duplicates, `loop_reciprocal`.

**P3 — flatness is level-independent (Lean-provable, expected PASS ⇒ prose correction).** Claim: if `t_ij` satisfy the infinitesimal braid relations then so do `ħ·t_ij` for every scalar `ħ`, so KZ is flat at every level; "flat at `q₀`, fails at roots of unity" (`lifted-crossing-locality.md:15`, `q-holonomy-locality-derivation.md:36`) conflates flatness with semisimplicity of `H_n(q)`. Builds on `FourTermRelation.lean`. Scope: corrects two content blocks; nothing numerical moves.

**P4 — imaginary level makes nothing less exact (not Lean; a reading).** Drinfeld's theorem is for formal `ħ`; the R-matrix eigenvalues `e^{±iπħ·c}` are exact for any complex `ħ`; only the associator (multiple zeta values) is transcendental, at real and imaginary level alike. So "compute the monodromy exactly" means: exact in `ℚ(q)` for the generator eigenvalues and `z`, never a numerical solve.

**P5 — the lasso lifts are half-twists (exact compute, expected PASS; the only real unknown).** Claim: each of the six lassos of the probe lifts from a transposition in `S₃` to a conjugate of `σ_i^{±1}` in `B₃` (a simple branch point gives a half-twist). Then the monodromy generator of the pulled-back KZ connection is `ϱ(σ_i^{±1})` up to conjugacy, whose eigenvalues are `{q, −q⁻¹}` (or inverses) by Kohno–Drinfeld — the quadratic follows. Falsifiable: a full twist or a longer word would fail.

## 4. Ordered steps

1. **Probe extension** (2 h, risk low): extend `colour_cubic_branch_monodromy_probe.py` to record the *braid word* of each lasso (crossing sequence from ordering `Re X_j` along the path, mpmath 50 dps, no float64), assert each is conjugate to `σ_i^{±1}`, record signs and the product word. Output: `computations/probes/colour-cubic-braid-monodromy.witness.json`. Forecloses: nothing; a non-half-twist result is a scope-(a) finding.
2. **Lean P2** (2 h): `QOU/Mass/SL2QuantumTraceIsZD.lean` — `z_D = (q[3]−q⁻¹)/[2]²` generic; `QOU/Mass/SL3QuantumTraceNeZD.lean` — `z_3 ≠ z_D` for `1<q` (archimedean). `lean -DautoImplicit=false -s 65536` exit 0 both. Register `z_D` origin in `trace-convention-registry.md`.
3. **Lean P3** (1 h): `KZFlatnessLevelIndependent.lean` — scalar-multiple stability of the infinitesimal braid relations; then reword the three prose sites (P3) in the same PR, render-QA'd.
4. **Lean P1** (1 h): six distinct roots of `D` (exact discriminant of the sextic, `norm_num`/`decide` on an integer — genuinely finite, not laundering).
5. **Rewrite the conjecture's open remainder** (1 h): `hecke-monodromy-step-two.md` §"What remains conjectural" becomes: *the substrate connection is the sl₂ KZ connection on `Conf₃(ℂ)` pulled back along the root map, at level `k+2 = iπ/ln q₀` (Kohno convention `q=e^{iπ/(k+2)}`; `2πi/ln q₀` in the block's convention — state one), with `q₀` an input.* Add a `HeckeMonodromy` sub-hypothesis naming that connection so option C is a conditional class, not prose. Bean `qou-d0qq` body-append; retitle it (its title still says "does any level reproduce q₀" — gate-violating wording).
6. **Library** (30 min): ingest Kohno 1987 and Drinfeld 1990 into `library/` (they are cited, not held); otherwise every "Kohno–Drinfeld gives…" sentence in the corpus is unverifiable by path 5.

Total ≈ 8 h, one PR. Nothing here is a fit: `q₀` enters only at step 5 as the level label.

## 5. Default if nobody acts

`qou-d0qq` stays `in-progress` with a next-step that cannot be executed as written; the three prose sites keep asserting a level-dependent flatness that is false; `z_D`'s sl₂ origin stays implicit; the gate-violating bean title stays. No number moves.

## 6. Recommendation (judgement)

Do steps 1–3 first, in that order — they convert option C from "research-scale, unknown" to a **conditional identification with two exact checks already passing** (P2) and one cheap decisive compute (P5). I would *not* build a KZ connection on `ℂ∖{6 points}` at all; the bean's phrasing is the error, not the mathematics. Blast radius: two `mass-theory` blocks and one `nuclear-interactions` block reword; `HeckeMonodromy.lean` gains a field; no witness or dashboard changes.

---

## B′. Correction to §B and to the KZ-level docstring (2026-09-07, after the `qou-99qc` review on #7088)

Two points from the sibling review, both accepted. (1) **Scope.** The relation `q² = e^{iπħ}` is
read off the §7a Skein normalisation (H); the corpus's other live normalisation (J) (bean
`qou-8bxv`) has generator eigenvalue ratio `−q`, so under it `e^{iπħ} = q` and `ħ` halves. The
relation is invariant under generator rescaling and `ħ`-vs-`k` bookkeeping, **not** under a change
of Skein normalisation; (H) is canonical by AGENTS.md, so the number stands, the scope sentence
was wrong. (2) **Level bookkeeping.** With `ħ = (2/iπ) ln q₀`: `ħ = 1/(k+2) ⇒ k+2 ≈ 15.05 i`,
`ħ = 2/(k+2) ⇒ 30.1 i` (`q = e^{iπ/(k+2)}`), `ħ = 4/(k+2) ⇒ 60.2 i` (`q = e^{2πi/(k+2)}`). §B's
plan text and the merged docstring mapped `60.2 i / 30.1 i` onto `ħ = 2/(k+2)` and `1/(k+2)`,
off by two; the probe's computed values were correct. Fixed in the docstring and the probe on #7088.

## C. The framework-side connection — plan (agent `fw-conn`, verbatim) and the two steps executed the same day

**Parent verification.** Every Lean and audit citation re-read: `KZUnitModulusPrune.lean:30` (`unit_modulus_ne_real_gt_one`), `mi_sw_cartan_reduction.lean:103/142` (the class and theorem, no instance), `reeb-bundle.lean:29` (`structure ReebBundle (M) (q : ℝ)`), the two June audits and `2026-08-02-moc-gauss-manin-not-derivable.md` exist, `library/deligne-mostow-1986` is held, and `ColorSpectralCubicGeometry.lean:35-36` carries the zero-residue statement (`Res(X dz) = 0` at every finite branch point, PR #2755). One path correction: `TrBIntegerTracePrune.lean` lives under `QOU/BraidKnot/`, not `QOU/Mass/`. The §3 amendment table (the library holds 53 Gauss–Manin and 37 vanishing-cycle section files that `INDEX.md` does not show) is recorded as delivered.

**Executed (parent, same day):**

- **Step 1 — `QOU/Mass/UntwistedMonodromyPrune.lean`** (sorry-free, axioms `propext/Classical.choice/Quot.sound`, generic linearly ordered field): a finite-order eigenvalue is never `> 1`; quasi-unipotence `(l^k − 1)^m = 0` forces `l^k = 1` in a field, so the same; and the negative Hecke eigenvalue `−q⁻¹` is not of finite order either. Candidates C1/C2 (any untwisted geometric monodromy) are dead by this invariant — scope-(b).
- **Step 2 — `computations/probes/colour_cubic_abelian_twist_holonomy_probe.py`** (8/8, mpmath 50 dps, anchor independent, nothing reads `q₀`): the push-down of the abelianised Cartan connection `A⁰ = X dz` is `Σ_j X_j dz = −(z+1) dz`, exact; around every one of the six branch points the fixed sheet's circle integral and the exchanged pair's sum both vanish to `10⁻⁵¹`, so the closed loop on the curve (lasso twice) has zero integral on every sheet and `exp(∮A⁰) = 1`. **The framework's only connection supplies no twist** — candidate C3 is dead, scope-(b) (invariant: holomorphy of the fixed sheet inside the circle, plus Vieta). C3′ — an external exponent `μ` with `e^{2πiμ} = −q₀²` — is the survivor, and it is the KZ level in geometric clothing.

**What this settles, stated without softening.** No framework geometry in the corpus produces the deformation `1 ↦ q₀`: untwisted monodromy is finite-order, the abelian connection is holonomy-trivial, and the twist exponent is therefore an input. Under the forever-gate it can only ever be an input. Step 2 of the canonical chain is thus honestly: *the substrate connection is the twisted Gauss–Manin connection of the root-map family with exponent `μ(q₀)`* — the class `KZPullbackGenerators` names it — and "constructing the connection" is not a derivation target. Plan steps 3–5 (the hypergeometric model, the `Im μ ≠ 0` Lean, the prose rewrite) remain.

# Plan — framework-side connection for Step 2 (bean `qou-d0qq`, pick "2")

**Hard constraints, repeated.** NO FITTING: no object is chosen because its number matches; each candidate below is tested by a *proved invariant* or an *exact* computation, never by residual. **`q₀` is INPUT only** — the connection's level/twist is fixed *from* `q₀`; any step whose output would be a value of `q₀` is forbidden (forever-gate 2026-08-02). Every negative is scope-(a) unless the invariant is named. Every Lean statement is falsifiable; no `True`, no `sorry` without `-- Ref:`.

## 0. The decision in one paragraph

The natural candidate — *the Gauss–Manin connection of the colour cubic family is the framework connection and its q-deformation is where the substrate enters* — is **dead as stated, by two proved invariants the corpus already holds, and the corpus knew this in June**: (1) the colour-cubic fibre is three points, so its Gauss–Manin local system is the S₃ permutation representation, finite order, eigenvalues roots of unity — never the real pin (`KZUnitModulusPrune.lean:30-45`); (2) any *untwisted* Gauss–Manin monodromy of an algebraic family is quasi-unipotent, and for the genus-1 case lands in SL₂(ℤ) with integer trace (`TrBIntegerTracePrune.lean:132`; audit `2026-06-24-lever1-color-eq-monodromy-integrality.md:26-47`, which already concluded *"B is the holonomy of the abelianised λ_SW connection, not the topological monodromy"*). The only connection on `ℂ∖Δ` (Δ = the six branch points) whose lasso monodromies can have eigenvalue ratio `−q₀²` with real `q₀ > 1` is a **twisted** Gauss–Manin connection — cohomology with coefficients in a rank-1 local system `L_μ` with local exponents `μ`, `e^{2πiμ} = −q₀²` (Deligne–Mostow (2.11), held). That is *exactly* the hypergeometric-integral realisation of the KZ connection (Schechtman–Varchenko; not held), so "constructing the framework connection" reduces to: **does any framework object supply the twist `L_μ`, or must `μ` be put in by hand from `q₀`?** Measured below: every rank-1 system the framework's own geometry produces on `ℂ∖Δ` is trivial (zero residues, polynomial 1-forms are exact). So the twist is the level, the level is `q₀`, and the honest deliverable is the explicit twisted-period realisation with `μ(q₀)` as input — a *re-description* of `KZPullbackGenerators` in geometric terms with one new exact check, not a derivation of the deformation.

## 1. Which framework objects could carry a connection (file:line, not prose)

| object | where it exists | can it carry a connection? |
|---|---|---|
| Colour cubic `P(X,z)` over `z = √q − 1/√q` | `QOU/Mass/ColorSpectralCubicGeometry.lean:8-11`; `ColourCubicDiscriminant.lean:6-25` | It is **one** plane cubic (genus 1 by Riemann–Hurwitz: `2g−2 = 3·(−2)+6 = 0`); `z` is a coordinate *on* it, and `q` is a **point** `z₀(q₀) = 0.10439` on the base, not a family parameter. `ColorCubicPowerSums.lean` (cited at `:21-24`): the spectral data is **q-free**. |
| The 3-sheeted root map `z ↦ {X_j(z)}` | `computations/probes/colour_cubic_branch_monodromy_probe.py:1-70`; lifts in `colour_cubic_braid_monodromy_probe.py` | Yes — its Gauss–Manin (H⁰ of the fibre) is the S₃ permutation local system: finite. |
| The abelianised Cartan connection `A⁰ = X dz = λ_SW` on the exceptional divisor `S_c ≅ P¹` | `brings-surface/mi-sw-abelianisation-cartan.md:1-20`; Lean class `MiSwCartanReductionHypotheses` at `QOU/ArchimedeanUniverse/mi_sw_cartan_reduction.lean:103`, theorem `:142`, **no instance** | The only framework-side *connection* that exists as a content block + Lean. Rank 1, abelian. |
| Reeb bundle `R_p → S_p` with connection from `ξ_q` | `mass-theory/reeb-bundle.lean:29` (`structure ReebBundle (M) (q : ℝ)`, ℝ-only, header says "NOT part of the formal proof chain") | Named, but no connection form, no holonomy is defined anywhere in Lean. |
| Yekutieli multiplicative integral | `QOU/MathlibExt/YekutieliIntegration.lean:55-162` (discrete holonomy layer only; continuum MI∫ and surface Stokes explicitly *not* formalised, `:22-30`) | Provides the algebra of holonomy, no connection. Library: `arxiv-1007.1250v4` held but `sections/` is intro + references only, no `ocr/` — its (α, β) setup is not greppable. |
| Brane tower `⊕Aₙ`, vertex-operator worldsheet | `mass-theory/vertex-operator-dictionary.md:1-3` (prose only) | No Lean carrier. |

## 2. Candidate identifications and their prunes

**C1 — untwisted Gauss–Manin of the root map (rank 3 / reduced rank 2).** Claim: lasso monodromies are the transpositions the probe measured. Prune (scope-(b), invariant: finite order): `g^k = 1` in a field forces every eigenvalue `λ` to satisfy `λ^k = 1`, impossible for real `λ = q₀ > 1`. This *is* the `q = 1` shadow already held (`HeckeQuadraticClassicalShadow.lean`); it supplies no deformation. **Dead as sole mechanism.**

**C2 — untwisted Gauss–Manin of a genus-1 family (`H¹`, rank 2).** No such family over `ℂ∖Δ` exists in the corpus (§1 row 1). Granting the descartes/Bring `E_q` family over the `q`-plane instead, the corpus proved its topological monodromy is SL₂(ℤ) with integer trace (`TrBIntegerTracePrune.no_SL2Z_realizes_trB`, `:132`); generally the local-monodromy theorem gives quasi-unipotence, eigenvalues roots of unity. **Dead by proved invariant; a step-1 Lean lemma makes the general form explicit.**

**C3 — twisted Gauss–Manin, twist supplied by the framework's own abelian connection `A⁰ = λ_SW`.** Claim: `L := exp(∮ A⁰)` around each lasso has holonomy `q₀^{±2}`, and the twisted cohomology of the root-map family then carries the Hecke pseudo-reflections. Prune (scope-(b), invariant: residue theorem / `H¹_dR(ℂ) = 0`): `Res(X dz) = 0` at every finite branch point (`ColorSpectralCubicGeometry.lean:30-33`, PR #2755), so on the curve the loop holonomy of `exp(∮ λ_SW)` is `1`; and any push-down of `λ_SW` to `ℂ∖Δ` is a symmetric function of the roots, hence a polynomial 1-form (`p₁ = −(z+1)`, `ColorCubicPowerSums.lean`), hence exact, holonomy `1`. **The framework's abelian connection supplies no twist.** (The jets `λ_SW^{(n)} ~ (z−z_k)^{1/2−n}` have √-branch monodromy `−1` — a root of unity again, `NaStokesKeystone.lean:46-48`.)

**C3′ — twisted Gauss–Manin with the twist as input (the survivor).** `L_μ` on `ℂ∖Δ` with the *same* exponent `μ` at all six points (forced: all six lassos are conjugate positive half-twists, probe 13/13, so one parameter — **no freedom to fit**), `e^{2πiμ} = −q₀²`, i.e. `μ = ½ − i·ln q₀/π`. Then `H¹(P¹ ∖ {X₁,X₂,X₃,∞}, L_μ)` is rank 2, its local monodromy at a collision `X_i = X_j` is a pseudo-reflection with special eigenvalue `e^{2πi·2μ'}`-type (Deligne–Mostow (2.11)/(3.4), `library/deligne-mostow-1986/sections/sec-004…, sec-005…`), and the eigenvalue pair is `{q, −q⁻¹}` up to the scalar `KZLevelFromHeckeNormalisation` already proves is invisible to the ratio. Falsifiable: *the twisted-period local monodromy has eigenvalue ratio `−q₀²` iff `e^{2πiμ} = −q₀²`; for real `q₀ > 1` this forces `Im μ ≠ 0` (non-unitary twist), the imaginary level in geometric clothing.* **What it is not:** a derivation of `q`. The twist is `q₀`, entered once, as input.

**C4 — q-difference (Birkhoff/qKZ) connection.** Since the colour data is q-free the corpus already forced a q-difference operator (`ColorSpectralCubicGeometry.lean:21-24`; `QDifferenceConfluentObstruction.lean:1-30`); q-difference connection matrices are R-matrices with real-`q` eigenvalues, no imaginary level needed (library: q-Stokes `arxiv-2412.02281v1`, quantum KZ `arxiv-math-0203003v2` held). Prune before any compute: Frenkel–Reshetikhin's connection matrices are *elliptic* R-matrices, so the Hecke quadratic holds only in a trigonometric limit — and the framework's kernel `R(q,x) = x² − τx + 1` is an **effective fit to three anchors** (`NaStokesKeystone.lean:55,93`), so nothing numerical from it may be used. Bean it; do not run it.

## 3. Six-path corpus-grep (library, `.beans`, `.lake` excluded unless stated)

- **Gauss–Manin**: 80 occurrences / 38 files (`docs/audits` 6 by the timed-out loop; ripgrep full count). Decisive prior holds: `2026-06-24-lever1-color-eq-monodromy-integrality.md:26-47` (integer-trace exclusion; "B = abelianised λ_SW holonomy"), `2026-06-24-lever1-binding-monodromy-hyperbolicity.md:35-60` (`τ = 2.6424 > 2`, hyperbolic — **but τ is the fitted depth-2 kernel; do not reuse it**), `2026-08-02-moc-gauss-manin-not-derivable.md:1-60` (period map is an irreducible input), `2026-06-25-z2bn-tau-gauss-manin-sage-probe-spec.md` (spec only). Bean `qou-i5yp` (todo) asks a related depth-8 Bring GM question.
- **Picard–Fuchs**: 35 files, all in the same Lever-1 arc (`computations/substrate/bring_picard_fuchs_kernel.py`, `lever1_color_eq_monodromy_integrality.py`, `z2bn_pf_monodromy_synthesis.py`).
- **vanishing cycle**: 8 files, none about the colour cubic (`colour_sign_line_pure_braid_probe.py`, `TorusKnotPages.lean`, two beans).
- **Cartan connection**: 9 occurrences / 8 files — the cheat-sheet, the two Step-2 plans, `categorical-connection-su2.md` (Maurer–Cartan form, flat by MC equation — a connection on `SU(2)` itself, not on `ℂ∖Δ`).
- **Reeb connection**: 6 files, prose/QA only + `reeb-bundle.lean` (no connection form).
- **Yekutieli**: hundreds of hits, dominated by the `.lake` build mirror; live Lean carriers `MathlibExt/YekutieliIntegration.lean`, `Archimedean/yekutieli_leading_coefficient.lean` (axiomatised `YekutieliStokesNormalisation` class).
- **Library**: Deligne–Mostow held (local monodromy `α_s = exp(2πiμ_s)`); Yekutieli surfaces held as PDF only; Kohno, Drinfeld, Schechtman–Varchenko, Aomoto, Frenkel–Reshetikhin **not held** (`library/INDEX.md`: 0 hits).

Nothing in the corpus constructs a connection on `ℂ∖Δ`; nothing contradicts C3′.

## 4. Ordered steps

| # | step | cost | risk | forecloses | produces |
|---|---|---|---|---|---|
| 1 | **Lean prune (C1/C2)**: `finite_order_eigen_ne_real_gt_one` — in a field, `λ^k = 1`, `k ≥ 1`, and `1 < λ` (ordered field) contradict; corollary for quasi-unipotent `(λ^k − 1)^m = 0`. Falsifiable, generic. | 1 h | low | any untwisted geometric (finite/quasi-unipotent) monodromy as the substrate connection — scope-(b) | `QOU/Mass/UntwistedMonodromyPrune.lean`, `lean -DautoImplicit=false -s 65536` exit 0 |
| 2 | **Exact computation (C3, smallest)**: extend the branch probe to integrate `X_j dz` along each of the six lassos on the curve (loop = lasso twice), mpmath 50 dps, assert `|∮| < 10⁻⁴⁰`, and symbolically that `Σ_j X_j dz` is exact. | 1–2 h | low; expected zero | the framework-supplied twist | `computations/probes/colour_cubic_abelian_twist_holonomy_probe.py` + witness (q₀-independent) |
| 3 | **Exact computation (C3′)**: Gauss hypergeometric model — local monodromy of `∫ t^{a}(t−1)^{b}(t−x)^{c} dt` at `x = 0, 1` via Deligne–Mostow (2.11); closed-form eigenvalues in `e^{2πi(·)}`; verify with `a = b = c = μ − 1` that the ratio is `−q²` with `q² = e^{iπħ}` — exact in `ℚ(e^{2πiμ})`, then evaluated at the proton pin as a diagnostic only. | 2–3 h | medium: the exponent bookkeeping (SV vs Kohno) must be stated, not guessed | — | `computations/probes/twisted_period_pseudoreflection_probe.py` + witness |
| 4 | **Lean (C3′)**: `TwistedPeriodEigenvalueRatio.lean` — for `μ : ℂ`, `Complex.exp (2πiμ) = −q²` with real `q > 1` forces `Im μ = −ln q/π ≠ 0`; and the pseudo-reflection pair `{1, e^{2πiμ}}` rescales to `{q, −q⁻¹}` (reuse `KZLevelFromHeckeNormalisation.eigen_sq_of_product_ratio`). | 2 h | low | — | `QOU/Mass/TwistedPeriodEigenvalueRatio.lean` |
| 5 | Rewrite `hecke-monodromy-step-two.md` §"What remains conjectural": the substrate connection = twisted Gauss–Manin of the root-map family with exponent `μ(q₀)`; `A⁰ = λ_SW` proved *not* to be the twist; render-QA. Beans: `qou-d0qq` body; new bean for C4 (qKZ, blocked on Frenkel–Reshetikhin not held). | 1 h | — | — | content block + beans |

Total ≈ 8 h, one PR, no witness moves.

## 5. Default if nobody acts

`qou-d0qq` keeps "construct the connection" as an open next step that reads as a derivation target; the corpus continues to carry two unreconciled framings (§2a stipulation; June's "B is the abelianised holonomy" without the zero-residue consequence drawn); no number moves.

## 6. Recommendation (judgement)

Do 1 → 2 → 4 → 5, skip 3 unless the owner wants the hypergeometric model made explicit — step 2 is the load-bearing negative (the framework's only connection contributes no twist), and once it lands the honest statement of Step 2 is: *the deformation `1 ↦ q` is not produced by any framework geometry in the corpus; it is the twist exponent, and under the forever-gate it can only ever be an input.* That converts option C from "research-scale construction" into a closed scope-(b) negative plus a named, falsifiable input — which is more valuable to the paper than a connection that would have carried `q₀` in by hand and called it geometry. Blast radius: `hecke-monodromy-step-two.md`, the cheat-sheet §2a row, bean `qou-d0qq`; nothing downstream computes from the geometry, so no mass or binding number changes.
