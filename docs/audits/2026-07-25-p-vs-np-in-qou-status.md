# P ≠ NP in the QOU — status audit (2026-07-25)

Branch: `claude/p-not-equal-np-status-dfdq41` (PR #4141).
Scope: the `conj:qou-p-neq-np` cluster and the Hecke-semisimplicity
infrastructure built to support it. Every Lean file cited below is
**verified sorry-free** via `scripts/lean-verify.sh` (lean-direct against
the restored `lake-cache/qou-v4-24-0` oleans).

## 1. Executive summary (the honest status)

The QOU's `P ≠ NP` claim is a **fully-assembled conditional**: every
mechanical/structural step is proven sorry-free; the whole open content
rests on **two named inputs**, and the framework is genuinely positioned
to prove a **weaker, *derived* statement** (physical intractability) that
sidesteps the harder of the two.

- **P ≠ NP is NOT proved and (honestly) cannot be here.** It is a Clay
  problem; per AGENTS.md §"Axiomatization is NOT a Proof", the compiling
  Lean does not constitute a proof.
- What *is* done: the claim is **stated conditionally** ("Given a QOU,
  then P ≠ NP *in that QOU*"), the **non-vanishing leg is derived**
  (`χ(A) = −6`), the semisimplicity ingredient is **nearly fully built**
  (reduced to one Gram identity), and the **wall is precisely located and
  named** — it is a single missing implication wearing three costumes.
- The **honest derived result** the QOU *can* prove: a
  **physical-intractability** theorem (no bandwidth-limited device
  decides the boundary problem in poly time) — strictly weaker than
  abstract `P ≠ NP`, but a real lower bound, not a fiat.

## 2. What is proved (sorry-free)

### Conditional framing + non-vanishing leg
- `QOU/Information/QouPNeqNp.lean` — `qou_implies_p_neq_np`: "Given a QOU
  (a `QouPNeqNp` instance), `PNeqNPInQOU`." Opaque QOU-scoped target;
  never a bare `P ≠ NP`. Lone `sorry`-carrier is `faithful` (the conjecture).
- `QOU/Information/ChiMinusSix.lean` — `chi_eq_neg_six` / `chi_ne_zero`:
  from the QOU cohomology (`HH⁰=0`, `HH²≅k`) + Bring genus 4,
  `χ(A) = 2 − 2·4 = −6 ≠ 0`. The non-vanishing leg is an **axiom
  consequence**, not a conjecture.

### Hecke-semisimplicity engine (the WenzlCriterion discharge)
- `QOU/MathlibExt/QIntegerFactorial.lean` — `[n]_q`, `[n]_q!`, genericity
  iff (`[n]_q!≠0 ⟺ QGeneric`), positivity, recursions.
- `QOU/MathlibExt/TraceNilpotent.lean` — `regTraceForm` (regular-rep trace;
  Mathlib's `Algebra.traceForm` is commutative-only, a real obstruction),
  and it kills nilpotents.
- `QOU/MathlibExt/TraceFormSemisimple.lean` — **the keystone**:
  `isSemisimpleRing_of_regTraceForm_nondegenerate` (nondegenerate regular
  trace form ⟹ `IsSemisimpleRing`; via trace cyclicity, sidesteps the
  two-sided-ideal issue).
- `QOU/MathlibExt/HeckeGenericSemisimple.lean` — `isSemisimpleRing_of_qGeneric`:
  composes B1+keystone; reduces WenzlCriterion to one Gram identity.
- `QOU/MathlibExt/RegTraceGram.lean` — packages the trace form as a
  `BilinForm`, so `nondegenerate_iff_det_ne_zero` applies: semisimple ⟸
  `det(Gram) ≠ 0`.
- `QOU/MathlibExt/SubstrateRegime.lean` — the golden-ratio window
  `1 < q < φ` (φ = root of `q²−q−1` = the S₅/Bring resonance) ⟹ generic.
- `QOU/Hecke/IwahoriHecke.lean` — **constructs `H_n(q)`** (RingQuot of the
  free algebra by the Hecke relations; all three relations proven; the
  generators are units).
- `QOU/Hecke/H2GramArithmetic.lean` — the **n=2 Gram identity**, concrete:
  `det !![2, q−1; q−1, q²+1] = (q+1)² = [2]_q²`, `≠0 ⟺ [2]_q!≠0`.
- `QOU/Hecke/H2CompanionRep.lean` — the n=2 Gram **derived from the regular
  representation** (companion matrix `!![0,q;1,q−1]` satisfies the Hecke
  relation `C²=(q−1)C+q`), not asserted.
- `QOU/MathlibExt/HeckeGramFactorial.lean` — the **end-to-end hook**
  `isSemisimpleRing_of_gram_det_eq_qFactorial`: `det(Gram)=c·[n]_q!` (unit
  `c`) + generic ⟹ semisimple. Supply a basis + the determinant value and
  semisimplicity follows with no further Hecke input.
- `QOU/Hecke/H2AlgebraDimension.lean` — `H_2(q)=AdjoinRoot(X²−(q−1)X−q)` is a
  genuine **2-dim K-algebra** with the `{1,σ}` power basis (`lrz1` at n=2).
- `QOU/Hecke/H2TraceForm.lean` — **the first fully axiom-free
  `WenzlCriterion` discharge**: computes the actual `Algebra.trace` Gram of
  `H_2(q)` (`tr1=2, trσ=q−1, trσ²=q²+1`), `det=[2]_q²`, and proves
  `h2_isSemisimpleRing_of_generic` / `_of_one_lt` (substrate `q>1`) — no
  cited class, no `sorry`. The n=2 case of the whole
  `det(Gram)=[n]_q! ⟹ semisimple` chain, realised concretely.
- `QOU/Hecke/H3GramArithmetic.lean` — the n=3 arithmetic anchor:
  `[3]_q!=(1+q)(1+q+q²)`, `≠0 ⟺ q≠−1 ∧ q²+q+1≠0` (the target the 6-dim
  H₃ Gram must reproduce).

### The wall, located and analysed
- `QOU/Information/JetHorizonTransfer.lean` + `JetHorizonScaffold.lean` —
  the corpus jet-horizon mechanism (degree-0 answer blocked, degree-≥1
  witnesses leak) as a **named §3b-cond class with no instance**.
- `QOU/Information/ComplexityDictionaryOptions.lean` — **soundness is
  provable** (`trace_notInFP_of_sep`: P≠NP ⟹ Jones∉FP via JVW+Toda);
  **faithfulness is the wall** (`TraceFaithfulness`, no instance). Four
  dictionary options, each provable-but-insufficient or off-axis, except
  the one that assumes faithfulness.
- `QOU/Information/OptionBCountingTransfer.lean` — **`generic_transfer_false`**:
  counting-hard ⇏ decision-hard (perfect matching: #P-hard count,
  poly-time decision). The generic transfer is *refuted*, not merely open.

### The honest derived result (physical intractability)
- `QOU/Information/PhysicalIntractability.lean` —
  `qou_physical_intractability`: derives `info(n)=3^{3n}` from the skein
  resolution tree (non-torsion ⟹ no cancellation, full `3^c` survives),
  and concludes **no bandwidth-limited device decides the boundary problem
  in poly time**. A pigeonhole information lower bound on the Bekenstein
  bandwidth bound — *derived*, not fiat. Now **unconditional**
  (`qou_physical_intractability_unconditional`; `superPoly_two_pow`
  discharged from Mathlib little-o). Its **query-model sibling** is
  `SkeinHorizonLowerBound`/`SkeinInfoLowerBound` (on main); both carry the
  shared **algebrization caveat** (`no_horizon_cost_of_polyObservable`: a
  poly algebraic shortcut refutes the full-tree-read hypothesis, so neither
  crosses to abstract P≠NP — Aaronson–Wigderson).

## 3. The wall — one implication, three costumes

**Precision (not yet Lean-proved).** `TraceFaithfulness.faithful`
(`Jones∉FP ⟹ P≠NP`), `JetHorizonTransfer.transfer`
(`Γ(𝓗,A₀)=0 ⟹ P≠NP`), and `ComplexityDictionary.separation_of_blocked`
are **structurally analogous** — all of the shape "horizon-opacity
antecedent ⟹ the QOU separation" — but they are **formally distinct
classes over different opaque `Prop`s** (`PeqNP` vs `PNeqNPInQOU`;
antecedents `ExactTraceInFP` / `degreeZeroBlocked` / `answerBlocked`).
The claim "discharging one discharges all" is a **structural
observation, NOT a Lean theorem**: making it a theorem would require
bridging identifications (`degreeZeroBlocked ↔ ¬ExactTraceInFP`,
`PNeqNPInQOU ↔ ¬PeqNP`), which are *themselves* part of the conjectural
dictionary. (Follow-up: a conditional inter-derivability lemma given
those explicit bridges — bean `qou-*`.) What is honestly shared: each is
instance-free because it *is* the counting→decision transfer, which is:

1. **refuted as a generic law** (`generic_transfer_false`, matchings);
2. **blocked as a uniform argument** (Razborov–Rudich natural proofs — and
   "works at every non-torsion q₀" is uniform);
3. **unstatable as a Lean proof** (no formal P/NP in Mathlib; an instance
   would be axiom-laundering).

## 4. The provable / open map

| Target | Needs the transfer? | Status |
|---|---|---|
| non-vanishing `χ(A)=−6≠0` | no | **proved** (axiom consequence) |
| `H_n(q)` semisimple ⟺ `[n]_q!≠0` | no | **n=2, n=3, n=4 discharged as theorems** (`h2_isSemisimpleRing_of_generic`, `HeckeH3Semisimple`, `HeckeH4Semisimple` — the last det-free); general `n` is reachable via the **Schur route**, not the `T_w` basis — see the 🛑 note below |
| soundness `P≠NP ⟹ Jones∉FP` | no | **proved** (JVW+Toda) |
| **abstract P≠NP** | **yes** (the wall) | open; provably not-by-fiat |
| physical intractability | **no** | **derived** (mod exp-domination) |

> **🛑 CORRECTED 2026-08-29 — the row above and §5 item 1 were stale, and in a
> way that sends an agent to build the wrong thing.** Re-measured on `main` at
> `df81b22be4`:
>
> - **The rank ladder went past n=2.** `QOU/Machinery/HeckeH3Semisimple.lean` and
>   `QOU/Machinery/HeckeH4Semisimple.lean` both prove `IsSemisimpleRing` at their
>   rank by transport along an explicit Wedderburn isomorphism. H₄ is explicitly
>   **det-free** — the 24×24 Gram determinant is sympy-verified but
>   Lean-out-of-reach — so that rung was reached *without* the determinant §5
>   item 1 says to go and get.
> - **The general-`n` gap is no longer the `T_w` basis.**
>   `QOU/MathlibExt/WenzlSchurElement.lean` `semisimple_of_substrate` gives
>   semisimplicity **at every rank** for `Q > 1`, `X ≤ 0`, and its Schur-element
>   leg is *computed*: `schurElement_ne_zero` is a sorry-free theorem whose only
>   hypotheses are `1 < Q` and `X ≤ 0` — no class, no `sorry`.
> - **This is NOT a discharge.** `semisimple_of_substrate` carries
>   `[SchurElementCriterion Q X ss]`, itself instance-free, and per the 2026-08-21
>   audit that class and `WenzlCriterion` *"state the same literature theorem from
>   two equivalent angles"*. The citation **count** did not improve. What improved
>   is that one feeding leg is proved for all `n`, so the residual is a single
>   named theorem (Geck–Pfeiffer Thm 7.2.6, bean `qou-0y6h`) rather than a missing
>   basis theory.
>
> The `T_w` basis remains the honest Mathlib gap for the *determinant* route and
> is worth doing on its own merits — it is simply **not** on the critical path to
> all-`n` semisimplicity. Full re-measurement:
> [2026-08-29 gap inventory refresh](2026-08-29-pneqnp-gap-inventory-refresh.md).

## 5. Next steps (prioritized)

**Done since the 2026-07-25 snapshot** (all sorry-free, lean-direct):
`SuperPolynomial(2^n)` discharged (`superPoly_two_pow`) so
`qou_physical_intractability_unconditional` is self-contained (was #1);
the n=2 Gram wired to the **real** `AdjoinRoot` algebra and the whole
n=2 `WenzlCriterion` discharged as an **axiom-free theorem**
(`H2TraceForm`, was #2, now exceeds it); the `info(n)=3^{3n}` requirement
derived from the resolution tree and reconciled with the query-model
lower bound + algebrization caveat (`SkeinInfoLowerBound` on main +
`PhysicalIntractability` cross-ref, was #5); the headline reframed to
foreground the derived result (was #6).

**Remaining (in priority order):**

1. **[large — Mathlib wall] The general `T_w` basis / `dim = n!`** (beans
   `qou-lrz1`/`qou-twwf`, Bott–Samelson) and the symmetrizing-trace Gram
   `det(Gram)=[n]_q!` (bean `qou-0y6h`, Geck–Pfeiffer `det=∏ Schur`). This
   is the honest **Mathlib gap**: `Equiv.Perm` has no length/inversions,
   there is no Mahonian/Gaussian-binomial generating function, and the
   symmetrizing-trace / Hecke-radical theory is absent. The n=2 case is the
   proved anchor; the interface a future contribution plugs into is
   `HeckeGramFactorial.isSemisimpleRing_of_gram_det_eq_qFactorial`. Assess
   closeable-vs-wall per bean `qou-5hul` before a large build.

   > **🛑 The `T_w` half of item 1 is CLOSED over a field (2026-08-30, PR
   > #6053).** `QOU.Hecke.TwBasis.basisTwOfField` is a
   > `Module.Basis (Equiv.Perm (Fin (n+1))) K (IwahoriHecke K q n)` with
   > `coe = Tw`, and `finrank_eq_factorial` gives `dim_K H_n(q) = (n+1)!` —
   > sorry-free at general `n`, `#print axioms` clean.
   >
   > **Exactly ONE of the three "honest Mathlib gap" claims above is now
   > false.** `Equiv.Perm` *does* now have length and inversions
   > (`QOU.Hecke.PermLength.length_eq_invCount`), because `permCoxeterSystem`
   > makes `Sₙ₊₁` a Coxeter system of type `Aₙ` — which Mathlib does not have
   > for **any** concrete group. The other two stand as written: there is
   > still **no Mahonian / Gaussian-binomial generating function**, and the
   > **symmetrizing-trace / Hecke-radical theory is still absent**. Neither was
   > needed for the basis, and neither has been built.
   >
   > Two further corrections to the framing, not to the gap list.
   > **Bott–Samelson** is named in the bean but is not the route taken and is
   > not needed. **Matsumoto's theorem** — still an open Mathlib TODO at
   > `Coxeter/Basic.lean:78` — is **never used**: `T_w` is built from *some*
   > reduced word and well-definedness is never invoked, because along any
   > reduced word the operators merely walk the basis.
   >
   > What remains of item 1 is the **symmetrizing-trace Gram side** (bean
   > `qou-0y6h`, Geck–Pfeiffer `det = ∏ Schur`), which is now unblocked rather
   > than gated. And the basis itself is a *field* statement: everything
   > upstream of `QOU/Hecke/TwBasisField.lean` holds over an arbitrary
   > commutative ring, so a `ℤ[q,q⁻¹]` version needs that one file redone.
2. **[medium] NP→Jones encoding** — **already on main** as
   `QOU/Information/SkeinNPEncoding.lean` (`NPSkeinReduction`,
   `decisionBudget`, `accepts_of_observed`). Not open; do not re-derive.
3. **[permanent wall] The counting→decision transfer** (`TraceFaithfulness`
   / `qou-iv9f`) — abstract P≠NP itself; refuted-as-generic, blocked-as-
   uniform, unstatable-in-Lean. **Never fabricate an instance.**

## 6. What NOT to do (guardrails for future agents)

- **Do not fabricate an instance** of `TraceFaithfulness` /
  `JetHorizonTransfer` / `ComplexityDictionary` — that is claiming P≠NP
  (audit-dodge, AGENTS.md §anti-laundering).
- **Do not re-derive** the settled pieces (χ=−6, the semisimplicity
  engine, the Gram criterion, `generic_transfer_false`) — corpus-grep
  first.
- **Do not conflate** the physical-intractability theorem with abstract
  P≠NP; the former is real and weaker, the latter is the open wall.

## 7. Bean index

Epic `qou-yi7h` (close the two open inputs) + `qou-hnhg` (Hecke infra).
Key open beans: `qou-t2pm` (exp-domination), `qou-eedq` (H₂ trace wiring),
`qou-twwf`/`qou-lrz1` (T_w basis), `qou-iv9f`/`TraceFaithfulness` (the wall
— do not fabricate).
