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
  bandwidth bound — *derived*, not fiat. Conditional only on the standard
  exponential-domination fact (`SuperPolynomial(2^n)`, Mathlib-dischargeable).

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
| `H_n(q)` semisimple ⟺ `[n]_q!≠0` | no | reduced to `det(Gram)=[n]_q!`; n=2 done |
| soundness `P≠NP ⟹ Jones∉FP` | no | **proved** (JVW+Toda) |
| **abstract P≠NP** | **yes** (the wall) | open; provably not-by-fiat |
| physical intractability | **no** | **derived** (mod exp-domination) |

## 5. Next steps (prioritized)

1. **[small] Discharge `SuperPolynomial(2^n)`** (bean `qou-t2pm`) from
   Mathlib analysis (`isLittleO_pow_const_const_pow_of_one_lt`) — makes
   `qou_physical_intractability` self-contained.
2. **[medium] Wire H₂ to the real trace** (bean `qou-eedq`): connect
   `h2GramMatrix` entries to `AdjoinRoot`/`Algebra.discr` trace values, so
   the n=2 Gram identity is about the *actual* algebra, not hand-computed
   entries.
3. **[medium] Formalize the NP→Jones encoding** (step 1 of the non-fiat
   transfer): a link family `β_{L,n}` reducing an NP-complete `L` to
   reading `J_{β_{L,n}}(q₀)`. Real; lands `L ∈ P^#P`.
4. **[large] The `T_w` basis / `dim = n!`** (bean `qou-lrz1`/`twwf`,
   Bott–Samelson) — the deep classical piece to make `det(Gram)=[n]_q!`
   general and fully discharge `WenzlCriterion`.
5. **[research] Derive the `info(n)` super-poly requirement** rigorously
   from the horizon / `3^c`-tree argument — converts
   `qou_physical_intractability` from conditional to the QOU's
   *unconditional* physical-intractability theorem. This is the genuine
   physical content and the most valuable honest target.
6. **[content] Reframe the headline** in the `.md` blocks: state the
   **physical-intractability** theorem as the derived result and keep
   abstract `P≠NP` explicitly conjectural (the wall). Do NOT let the
   content imply the Clay problem is proved.

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
