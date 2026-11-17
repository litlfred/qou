---
# qou-ix0x
title: The binding's divergent series is G, its Borel-Stokes plane is EMPTY, and the untried summation is the Habiro/cyclotomic one
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T08:46:20Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
---

Owner pointer, 2026-09-07: *"On A_infty there was a divergent series..."*, against the standing target *"ultimate target is to close gap in binding"*.

## Where the divergent series actually is

**NOT in `B(K)` for a fixed nucleus.** `conj:binding-manybody-eq-jet-filtration` writes `B(K) = Σ_{n≥2} B_n(K)` and `jet-filtration-binding-extensive` writes `B(A) = Σ_{n=2}^{A}`. These look like they disagree and **they do not**: a nucleus with `A` nucleons has no `n`-body term for `n > A`, so the sums are equal. Do not report this as an internal contradiction — I nearly did.

**It is `G(x;q) = Σ_n B_n x^n`**, the binding generating function, which is genuinely over all `n` and is the object carrying the q-difference equation. Two facts about it are already proved sorry-free:

- **`BindingGevreyHalf`** — `n! ≤ 4ⁿ I(n)² ≤ 8ⁿ n!`, so the lever-1 binding period is Gevrey-**1/2**. Divergent, and its divergence class is pinned.
- **`BindingScalarKernelParityExclusion`** — its q-difference module `L_K = (q²x−1)σ² − (q−1)σ − (q−1)` is irreducible of rank 2 and pure isoclinic of Newton slope 1/2.

## What I established this session, which closes the obvious use of that divergence

`QOU/Mass/BindingNoAlienPlane.lean` (sorry-free, lean-direct exit 0): **the divergence carries no Stokes data, on either plane.**

- classical: Gevrey-1/2 ⇒ level-1 Borel transform entire ⇒ no alien derivatives there.
- q: pure isoclinic ⇒ Ramis–Sauloy math/0611521 §2.2 verbatim, pure modules "are irregular objects **without wild monodromy**" ⇒ no q-alien derivations, no Stokes operators.

So the series diverges and the *resurgent* content of that divergence is empty.

## THE UNTRIED SUMMATION — this is the bean

Borel–Laplace is not the only way to sum a divergent q-series, and the corpus already uses the other one. **Habiro / cyclotomic summation** converges at every root of unity rather than along a ray, so purity — a statement about the slope filtration and the Stokes sheaf — says **nothing about it**.

The corpus already places the right objects there and this is prior art, not my idea:

- `full-pole-structure-mass-trace.md`: "The Markov trace of any closed braid lies **natively** within the Habiro cyclotomic completion" `\hat{ℤ[q]} = varprojlim ℤ[q]/(q;q)_n`.
- `z-Habiro ring`: `Φ_q(z) = Π(1−q^{-k}z)^{-1}` is "**ill-defined as a polynomial but exists as a formal limit within this completion**" — the exact move needed for a divergent all-orders object.
- `operator-selection-lp-interpretation.md` puts the LP's Markov traces and Gram entries in `\hat{ℤ[q]}` too.

And it is what the **owner's 2026-09-03 full-tower ruling** asks for: "all `n` of the Hecke tower *and* all orders in `q`". The Habiro ring is precisely the object holding all orders in `q` at once.

## Why this is not excluded by the b3 = 0 diagnosis

The 09-05 audit derives the model's `b3 = 0` from pair-locality (`b3_eq_zero_of_pairLocal`) and explains pair-locality by `HH^k(H_n(q), H_n(q)) = 0` at **generic** `q`. Both are level-wise statements at a fixed finite `n` and at a *generic* point. `H_n(q)` at a **root of unity** is NOT semisimple — `2026-06-04-kontsevich-soibelman` records this explicitly: cellular over `ℤ[q^{±1}]`, generic fibre semisimple, "the root-of-unity fibres are **non-semisimple**". A cyclotomic evaluation therefore lands exactly where the semisimplicity that forces `b3 = 0` fails.

## ROAST — what is wrong with this, stated by me

1. **It is a LOCATION, not a derivation.** It says where a nonzero 3-body datum could live. It does not compute `b3 = +1.4262 MeV`, and a completion is enormous. Do not write it up as progress on the number.
2. **The `A_∞` conflation I nearly committed.** `direct-limit-algebra-su2.md` defines `A_∞ = colim End(J^nO(SU(2))) ≅ U(𝔰𝔲(2))` — the SU(2) jet tower. The binding's "jet filtration" is a DIFFERENT object: `lem:bond-order-eq-jet-degree` uses the Gröbner–Shirshov Coxeter-length filtration on `H_{3A}(q)`. Both are called jet filtrations. Any argument routed through the SU(2) one is a symbol collision.
3. **`b3` is a glyph collision three ways.** A grep for `b3` in this corpus returns `B_3(ℂ)` (the Bloch group, in the α_EM fixed point), `b3ix` (the Q_β odd channel), and `B3` (a Gröbner monomial in `HeckeCompletion.lean`). None is the connected 3-body cumulant. Resolve before citing.
4. **The non-semisimplicity is at roots of unity; the substrate `q₀ ≈ 1.11` is not one.** So a cyclotomic route has to explain how root-of-unity data reaches an evaluation at a non-root-of-unity point. The Habiro ring's whole content is that it does — but that is the thing to establish, not to assume.
5. **Anti-fit gate.** Any number extracted from a cyclotomic evaluation and matched to `b3` without a derived map is a fit. `qou-brng` was already burned once by a coincidence of exactly this shape (the ≈ ℏ_q² saturated fraction, now recorded as "more likely numerology than a derived prediction").

## FIRST BRICK — cheap, no compute, falsifiable

Does the corpus's `b3 = 0` proof survive at a root of unity? `b3_eq_zero_of_pairLocal` derives `b3 = 0` from pair-locality as a **hypothesis**. So the question is not whether the theorem holds — it does — but whether **pair-locality itself** is derivable at a root of unity, where `HH^k ≠ 0`. If pair-locality is genuinely a generic-`q` fact, the theorem simply has no hypothesis to stand on there, and `b3` is unconstrained by it. That is a Lean-readable question about one hypothesis, needs no probe, and either answer is progress.

Companion: `qou-dk8a` (the global connection matrix, the other unexcluded route).


---
**FIRST BRICK RUN, SAME SESSION — and it makes the resurgence route unnecessary for this purpose. The 3-body term is ALREADY AVAILABLE inside the framework, with a closed formula.**

My brick question ("is pair-locality generic-q only?") was mis-posed and the corpus answers something better. `QOU/Mass/CrossingModelPairLocality.lean` is over a **generic `CommRing`** — `PairLocal` is not a statement about `H_n(q)` at generic `q` at all. It is a hypothesis on the crossing model: *does a pair's mutual energy depend on what else is in the assembly?*

    def PairLocal := (∀ i j k, w3 i j k = w2 i j) ∧ (∀ i j, w4 i j = w2 i j)

Three theorems already there, sorry-free:

- **`not_pairLocal_of_b3_ne_zero`** — AME2020's `b₃ = +1.4262225` (`AmeBindingNotPairwise.ame_b3_eq`) **refutes pair-locality**. The file's own docstring: "a constraint on the carrier derived from data, not a modelling choice."
- **`brunnian_not_pairLocal`** — a Brunnian carrier violates pair-locality whenever some `w3 ≠ 0`. And `qou-brng`'s 2026-08-30 update establishes the ³He/⁴He carrier **L6a4 IS Brunnian** (`QOU.Mass.BrunnianBindingChannel`).
- **`b3_eq_neg_tripleMutual_of_brunnian`** — *on a Brunnian carrier*,

      b₃(i,j,k) = − tripleMutual(i,j,k) = − ( w3 i j k + w3 i k j + w3 j k i )

  exactly. Its docstring: "**No pair contamination and no free constant**: the pair terms vanish identically, so the whole of `b₃` is the irreducibly three-body channel. **Measuring `b₃` therefore pins that channel.**"

**So `b₃ = 0` is not a shadow of semisimplicity that has to be broken.** It holds only for a **pair-local** model, and the corpus proves its own carrier is not pair-local. The 09-05 audit is not wrong — it explicitly flags the formality→pair-locality bridge as "a conjecture to prove, not a theorem" — but the nearer reading is that the framework **already permits** `b₃ ≠ 0` and does not need a non-semisimple home for it.

**The open question therefore collapses**, from *"find somewhere a 3-body datum can live"* to a concrete in-framework computation:

> **compute `w3` for L6a4** — the mutual crossing energy of a pair measured *inside the triple* — and check `−(w3 ijk + w3 ikj + w3 jki)` against `+1.4262225 MeV`.

`CrossingEnergy.decomposition` (proved, cited in `qou-brng`) already splits mutual crossing energy into a signed writhe/linking channel `(n₊−n₋ = 2·lk)` and an unsigned count channel `(n₊+n₋)`, with the signed channel **zero** on a Brunnian pair. So `w3` is the unsigned count channel measured in the triple — a crossing count, not a fitted weight.

**This is a PREDICTION, not a fit**, and that is what makes it worth doing: `w3` is determined by the carrier's crossing structure, and `b₃` is measured. Nothing is tuned. If the number misses, that is a real negative about the carrier or about `binding = −(mutual energy)`, and either is information.

**Consequence for this bean and for `qou-dk8a`:** both remain unexcluded, and both are now **lower priority than computing `w3`**. The cyclotomic-summation route is a fallback for if the direct computation fails; it should not be worked ahead of it. My resurgence excursion this session produced a real negative (`BindingNoAlienPlane`) and pointed at a gap that has a nearer route — say so rather than dressing the excursion up as the plan.


---
**THE COMPUTATION RAN — 2026-09-11. It is a scope-(a) NEGATIVE, and it fails on the SIGN, which is the cheapest possible way for it to fail.**

[`b3_brunnian_count_channel_probe.py`](../computations/deltalambda/b3_brunnian_count_channel_probe.py), 6/6 PASS, exit 0, mpmath 50 dps, proton pin.

The entry above asked for exactly this and called it "a PREDICTION, not a fit". It is, and it is falsified:

| quantity | value |
|---|---|
| `signedChannel(1,1,q₀)` | `0` exactly (Brunnian) |
| `countChannel(1,1,q₀) = w3` | `+0.209060298796` |
| `tripleMutual = 3·w3` | `+0.627180896387` |
| `b₃ = −tripleMutual` (predicted) | **`−0.627180896387`** |
| `b₃` (AME2020) | **`+1.4262225` MeV** |

**The disagreement is a sign, so no energy scale can repair it.** `q₀ > 1 ⇒ q₀ − q₀⁻¹ > 0 ⇒` every `w3 > 0 ⇒ tripleMutual > 0 ⇒ b₃ = −tripleMutual < 0`. AME measures it positive. This is scale-independent: the construction supplies no MeV scale at all (`countChannel` is dimensionless), and that second gap is on the record too — scaling by CAL-1 `m_e` gives `|b₃| = 0.32048878` MeV against `1.4262225`, **4.45× short**. Reporting both so the sign is not mistaken for the only problem.

**The obvious escape is closed, and closing it is the part worth keeping.** My first write-up said the residual gap was that I had used the *isolated pair's* crossing numbers rather than the pair *inside the triple* — which is literally what the entry above asked for. That escape does not exist. Brunnian means every pairwise linking number is zero, so `n₊ − n₋ = 2·lk = 0` forces `n₊ = n₋ = m` for **whatever** `m` an inside-the-triple count produces, and

    countChannel(m, m, q₀) = m(q₀ − q₀⁻¹) > 0   for every m ≥ 1

Swept `m ∈ {1,2,3,5,8,13,100}` (FINDING 1b): all positive, from `0.209060299` to `20.9060299`. Re-counting **rescales** the prediction; it cannot flip it. Note the direction of that sweep — it is a check that *no* value works, not a search for one that does, which is why it is not a fit.

**What this does NOT touch**, and none of it is in question: the Lean channel decomposition; `b3_eq_neg_tripleMutual_of_brunnian`; that L6a4 is Brunnian; that the signed channel is empty on it; or `countChannel` as a *term* in some other combination — a compositional object is not excluded by one term of it failing alone (AGENTS.md §"Before declaring refuted"). What is excluded is the **identification `w3 = countChannel` at `q > 1`**.

**The open question changes shape rather than closing.** What survives is narrower and sharper: the identification presumes `w3` has the **pair-energy shape** `n₊q − n₋q⁻¹` with triple-adjusted counts. If the irreducibly three-body channel is instead a genuinely 3-body object *not* of that form, nothing above applies to it and the framework's 3-body channel is simply not yet computed. **That is a question about the FORM of `w3`, not about its numbers**, and it is what `qou-ix0x` now points at.

**Consequence for priority.** The previous entry demoted the cyclotomic-summation route below "compute `w3`". That computation is now done and has failed, so the demotion lapses — but it does **not** promote resurgence by default. The nearer question is the form of `w3`, and neither this bean's Habiro route nor `qou-dk8a`'s connection-matrix route is aimed at it. Both stay unexcluded and both stay open; neither is now "the plan".

Two sign-source questions, stated as open, **not** as candidates to try until one works:
- `binding = −(mutual energy)` makes a positive `b₃` require an **attractive** (negative) mutual channel, and `countChannel` at `q > 1` is repulsive by construction. Is the sign convention in `b3_eq_neg_tripleMutual_of_brunnian` the intended one for a *binding*?
- The `q < 1` branch flips it, but the substrate pin is `q₀ > 1` and is not free (and deriving `q₀` is forever-gated). So this is not a route.


---
**CONVERGENCE WITH `qou-rwhv` — 2026-09-12, and the convergence is NARROWER than it first reads.**

A sibling session (#7198, bean `qou-rwhv`) reached the **same sign** by an entirely different vocabulary: the corpus's connected 3-body cumulant read as `−φᵀ₃` of a hard-core lattice gas on the nucleon sites, negative for every bond triple in `(0,1)` by the Jansen–Kolesnikov Ursell alternation (their Lean `UrsellPartitionFunctionB3.b3corpus_neg`, sorry-free; their Mayer coefficient `−1.23` MeV ³H / `−0.80` MeV ³He against AME `+1.81` / `+1.04`). Their framing: *"two shadows of the classical Mayer sign"*.

**It is agreement, and it is not independence.** Both routes are **pairwise-generated**. Theirs: a partition function that is a product over pair bonds. Mine: `w3` assumed to have the pair-energy shape `n₊q − n₋q⁻¹`. *Neither computes an irreducibly 3-body object* — both compute what pair data implies about one. So this is two arguments **inside one class**, not two attacks on `b₃` from outside it.

That is worth more than it sounds, in the right direction: it upgrades the negative from *"this construction fails"* to *"pairwise-generated constructions fail"*, which is a wider scope-(a) than either branch had alone. It does **not** make the negative structural, and it must not be written as two confirmations.

**The escapes coincide as well**, which is the tell that the premise is shared. My verdict's item (i) — *"a positive `b₃` needs an **attractive** (negative) mutual channel, and `countChannel` at `q > 1` is repulsive by construction"* — is their *"a positive `b₃` needs a bond factor above 1"* in the other vocabulary. **One obstruction, two spellings.**

**Where the routes genuinely differ, and this is the part that might be worth something.** The alternation theorem requires a **non-negative (purely repulsive) pair potential** *as a hypothesis*, and on their route repulsiveness arrives through a Boltzmann reading `f = e^{−βU}` that `qou-rwhv` itself marks as unmade: *"the corpus's `f` are Markov factors built from `z`, and nothing in the corpus identifies them with an exponentiated potential. That identification is the concrete next measurement."* My route needs no such reading: `countChannel(m,m,q₀) = m(q₀ − q₀⁻¹) > 0` is arithmetic at `q₀ > 1`, for every `m ≥ 1`.

So the crossing-energy result **may discharge the hypothesis the Ursell route has to assume** — modulo exactly one identification, which I am **flagging, not claiming**: that *"positive crossing energy"* and *"non-negative pair potential"* are the same predicate. Under `binding = −energy` they line up, but that convention is item (i), i.e. the open question itself, so asserting the bridge would be circular. Establishing that identification is a concrete, falsifiable next step and is more valuable than a third instance of the sign.

**Not recorded, deliberately.** Neither branch has met `qou-rwhv`'s own settling condition — *"exhibit the polymer / cluster model whose activity expansion has the corpus's `b₃` as its third Ursell coefficient — name the polymer set, the weight, and the compatibility relation"*. Until that exists, *"two shadows of the classical Mayer sign"* claims the classical theorem applies here, which is the thing `qou-rwhv` was opened to decide. Both branches support only: **two arguments within pairwise-generated models, agreeing.** Posted to #7193 and #7198.

**Net effect on this bean's open question: unchanged in content, sharper in scope.** It was *"does `w3` have the pair-energy shape at all?"*. The convergence says the whole pairwise class gives the wrong sign, so the question is now *"is the framework's 3-body channel pairwise-generated at all?"* — same question, one level up, and now with two independent-vocabulary reasons to expect the answer must be no. `qou-ix0x` stays OPEN.


---
**🛑 I MADE THE TIER-CONFLATION ERROR THE CORPUS FIXED ON 2026-09-07 — corrected 2026-09-12. The conclusion survives and gets STRONGER, which is why the correction is worth spelling out rather than quietly patching.**

**What I asserted.** Two entries above, and in PR #7193's body, its commit message, and coordination comments on #7193 and #7198: *"b₃(predicted) = −0.627180896387 against AME +1.4262225"*, citing `QOU.Mass.CrossingModelPairLocality.b3_eq_neg_tripleMutual_of_brunnian`.

**What is actually true.** That theorem's hypothesis was **renamed on 2026-09-07** from `Brunnian` to `NoIsolatedPairEnergy`, precisely because two unrelated properties shared one name. `QOU.Mass.BrunnianTierDisambiguation` lists four tiers:

| tier | condition | true of L6a4? |
|---|---|---|
| T1 true Brunnian | every proper sub-link is the UNLINK | **yes** |
| T2 linking vanishes | every pairwise Gauss linking number `= 0` | **yes** |
| T3 linking vanishes at `k` | the same, localised | yes |
| **T4 `NoIsolatedPairEnergy`** | a pair carries no mutual **ENERGY** in isolation | **NO** |

The theorem's hypothesis is **T4**. L6a4 fails it, and the corpus proves so twice over (`QOU.Mass.BrunnianHypothesisNotSatisfied`): its own `brunnian_binding_survives` gives `0 < countChannel m m q`, and the measured `b₂ = 2.2245662` MeV is a nonzero isolated-pair binding outright. That file's words: *"a correct theorem whose hypothesis L6a4 does not satisfy"*.

**So my step `b₃ = −tripleMutual` was not licensed, and the `−0.627` figure should not be quoted.** The tier file exists *because this exact mistake was made on 2026-09-07*; I repeated it four days later, on a theorem name a corpus-grep would have resolved. Recorded as a TRAP, not as a footnote.

**The fix needs no hypothesis at all.** The cumulant is defined unconditionally (`PairwiseCumulantVanishing.BindingMap.b3`) as `b₃ = triple − (pair+pair+pair)`, and `toBindingMap` sets `pair = −w₂`, `triple = −tripleMutual`. Substituting:

    b₃ = −tripleMutual + (w₂ᵢⱼ + w₂ᵢₖ + w₂ⱼₖ)

T4 is just the special case `w₂ = 0`. We do not need it, because the corpus **measures both cumulants in one witness** (`computations/probes/pair-locality-shortfall.witness.json`): `b₂ = 2.2245662`, `b₃ = 1.42622016`, and `B_AME(A=3) = 8.09991876 = b₃ + 3b₂` (CONTROL 4, exact to 0.0). Hence `w₂ = −b₂` and

> **the data REQUIRES `tripleMutual = −(b₃ + 3b₂) = −8.09991876` MeV** — a strongly **attractive** three-body mutual channel, and it says how attractive.

Nothing is fitted: both cumulants are measured and the relation is the cumulant's definition.

**The correction goes AGAINST the framework, not for it.**

| | under the (inapplicable) T4 reading | corrected, no T4 |
|---|---|---|
| target | `b₃ = 1.42622016` MeV | `tripleMutual = −8.09991876` MeV |
| count channel gives | `+0.627180896` (dimensionless) | same |
| scaled by CAL-1 `m_e` | `+0.320488780` MeV | same |
| magnitude short by | **4.45×** | **25.27×** |

So dropping the bad hypothesis **raises the target 5.68×**. The sign failure is untouched — `q₀ > 1 ⇒ countChannel > 0` is arithmetic — and the magnitude gap is nearly six times worse than I reported. I had the error in my favour and it was still a negative; correcting it makes the negative sharper.

**Probe rewritten**, [`b3_brunnian_count_channel_probe.py`](../computations/deltalambda/b3_brunnian_count_channel_probe.py), now **8/8 PASS** — four controls (decomposition identity; T2 ⇒ signed channel zero; `q₀>1 ⇒ countChannel>0`; the cumulants reconstruct `B_AME(A=3)`) and four findings, one of which (FINDING 3) records the tier refutation *inside the probe* so the conflation cannot be walked past again.

**Contamination check** (AGENTS.md: say what else the error may have reached). The `−0.627 vs +1.4262` framing reached: this bean (two entries above), PR #7193's body and commit message, and coordination comments on #7193 and #7198. All corrected. **What does NOT change**, because it never depended on T4: `countChannel(m,m,q₀) = m(q₀−q₀⁻¹) > 0` for every `m ≥ 1`; the `m` sweep; that both routes are pairwise-generated; that the escapes coincide; and the scoping of the `qou-rwhv` convergence.

**And it sharpens the requirement into something falsifiable.** Item (i) is no longer "what supplies the sign" in the abstract — the corpus now names the number: **an attractive three-body mutual channel of `−8.09991876` MeV.** The question is what supplies *attraction*, not what supplies magnitude. `qou-ix0x` stays OPEN.


---
**THE OBVIOUS NEXT IDEA — the Milnor triple linking number `μ̄₁₂₃` — IS ALREADY CLOSED, and closed precisely where I wanted it to help. Corpus-grepped 2026-09-12 BEFORE writing any of it.**

The correction above sharpened the open question to *"what supplies an attractive `−8.09991876` MeV three-body channel?"*, and the natural candidate is the invariant that is nonzero on a Brunnian link exactly because all pairwise linkings vanish — Milnor's `μ̄₁₂₃`, which is **signed**, i.e. carries the one freedom `countChannel` lacks. I ran the six-path checklist on it rather than building it. **The corpus proposed it, built it, and refuted it on 2026-08-30.**

**It is not a small prior art.** `μ̄` / Brunnian / Massey material spans ~184 `content/` files, 222 `computations/`, 114 beans, 50+ audit docs and ~20 Lean modules — including a **working producer**, `computations/binding_mn_milnor_linking.py`, whose header already reads *"`M_3(K) = triple linking μ̄_ijk` (irreducible 3-body) … Milnor DISTINGUISHES the genuine 3-body (Borromean) from a chain of pairwise bonds"*, validated on Hopf (`lk=1`), Borromean (`lk_ij=0, μ̄₁₂₃=+1`) and the 3-chain (`μ̄₁₂₃=0`).

**R1 — the type refutation.** Bean `qou-edt7` (in-progress, 1063 lines) line 355, its author correcting themselves:

> *"I proposed Milnor `μ̄₁₂₃` as the last candidate — 'three-body by construction' … **Right about the SHAPE, wrong about the TYPE** … **`μ̄` is NORMALISED. It has no size.** If `b_A = c_A·μ̄` then `|b_A| = |c_A|` — the magnitude is entirely `c_A`'s."*

Durable carrier `QOU/Mass/MilnorCarriesOrderNotMagnitude.lean` (sorry-free): `muBar_no_magnitude`, `geometric_order_forces_square` (`b₃² = b₂·b₄`, which **fails by 10.11×** isospin-averaged / 5.25× Coulomb-corrected), `not_geometric_order`. Correctly scoped **(a)**.

**R2 — and this is the one that matters for MY question, because it blocks the SIGN, not the magnitude.** Bean **`qou-lq6k`** (todo, 2026-08-01, untouched), title verbatim:

> *"`μ̄₁₂₃` is TOTALLY ANTISYMMETRIC under component permutation, but a per-pair repulsion energy is SYMMETRIC in its pair — so no symmetric pair energy can be read off the triple-linking integral directly."*

Formalised sorry-free in `QOU/Mass/MilnorSignRepObstruction.lean`: `μ̄` is the **sign rep of S₃**, and `equivariant_linearMap_eq_zero` proves every S₃-equivariant linear map from the sign rep to pair-functions is **zero**. The surviving corollary is that the coupling can enter only through `|μ̄|` or `μ̄²` — **unsigned again**. So the sign freedom that made `μ̄` attractive to me is exactly what the equivariance kills. Verified exactly (integer Magnus, all 6 permutations) by `computations/deltalambda/mirror_split_s3_em_functional_probe.py`, 5/5.

**R3 — the Massey detour is the same object.** `docs/audits/2026-08-30-helicity-ladder-cannot-supply-the-he4-surplus.md` §"Rung 3 — third-order helicity IS the Milnor `μ̄` route, in different notation". Scope (b), and correctly confined to the max-contact all-`lk=1` configuration, so it does **not** exclude low-`lk` configurations — the triton's triple is genuinely Borromean.

**So I do not pursue `μ̄`, and this entry exists so the next agent does not either.** What the corpus leaves standing is stated by the file that closed it: *"a multi-term closure in which `μ̄` fixes each term's sign and order while separate coefficients carry the sizes is untouched — and is, on this evidence, the only shape left for it."* `qou-edt7` adds the discipline line: *"Nothing tested supplies those coefficients, and I am not proposing a candidate — proposing one because it would fit is the anti-fit violation."* I hold to that.

**Independent confirmation of the correction above.** The same grep pass reached the T4 conflation on its own and called my probe's first version *"the fourth independent sighting of one conflation … a known recurring defect, not a novel slip"*. Two routes to the same correction, one of which did not know the other's conclusion.

**Two library notes worth keeping.**
- **`library/1992evansberger/` (*A Hierarchy of Linking Integrals*) is the most on-point held source and a `sections/` grep cannot see it** — `sections/` is 878 B against 20,305 B of `ocr/` (4.3 %), and the `ocr/` text carries the construction outright: *"A third order linking integral (based on the Massey product) describes the subtle interlocking of the Borromean rings"*, *"§2. Third Order Linking"*, *"for the Borromean rings, L12, L23 and L31, all vanish"*. Exactly the `ocr/`-tier blind spot AGENTS.md warns about.
- **AGENTS.md's other named `ocr/` example does NOT hold this material.** `library/procrsoclondona92/` (Moffatt & Ricca, *Helicity and the Călugăreanu invariant*) contains **0** occurrences of Milnor, Massey or "triple linking" (against 14 `Călugăreanu`, 19 `writhe`) — it is **self**-linking, 1-body data. AGENTS.md names it as "the single most on-point held source for the mass/binding self-vs-mutual linking question", which is right for *self-vs-mutual* and wrong if read as a triple-invariant source.
- **Not held**: Laurence & Stredulinsky, *Asymptotic Massey products, induced currents and Borromean torus links* (J. Math. Phys. 41 (2000) 3170) — named by `qou-hrz3` as *"the ONLY Borromean-specific energy result"*, likely paywalled. Milnor 1954/1957 are in `references.ts` and not ingested.

**Homonym warning for anyone re-running this grep**: ~45 of the 184 `content/` hits are the **Milnor–Lobachevsky function** `Л(θ)` (`QOU/Archimedean/{Lob*,IdealTet*,BlochWigner*,Orthoscheme*}`), a different Milnor object. Filter before quoting a count.

**Path 0 was NOT run**: the `paper-assistant` MCP server failed to connect this session, so `corpus_search` was unavailable and `emptyRoots` could not be checked. The vocabulary blind spot the graph exists to cover is therefore **not** ruled out — this is a grep-measured result, not a graph-measured one.


---
**THE D2 OBSTRUCTION HAD A HOLE EXACTLY WHERE `b₃` SITS — closed in Lean, sorry-free, 2026-09-12. Companion bean: `qou-lq6k`.**

Having recorded that `μ̄₁₂₃` is closed, I read `QOU/Mass/MilnorSignRepObstruction.lean` rather than taking the summary on trust — and the theorem does **not** cover the case this arc needs.

**What it proves:** any S₃-equivariant linear map from the sign rep into the **pair-channel** module `Fin 3 → R` is zero. That target is the permutation module on 3 points, *trivial ⊕ standard*, and it is the right target for a **charge-bilinear / per-pair** coupling — which is what finding D2 was about.

**What this arc needs is a different target.** `CrossingModelPairLocality.tripleMutual(i,j,k) = w3 ijk + w3 ikj + w3 jki` sums over **all three** pairs, so it is a **scalar**, invariant under relabelling the components — the **trivial** rep, not `trivial ⊕ standard`. No instance of the existing theorem has it as a target. So between the corpus's two `μ̄` refutations there was a gap: `MilnorCarriesOrderNotMagnitude` argues about **size** and is silent on sign; `MilnorSignRepObstruction` argues about **symmetry** but only into the pair channel. **Neither says a symmetric scalar channel cannot be linear in `μ̄`.**

**Closed:** [`QOU/Mass/MilnorSignRepObstructionTripleChannel.lean`](../folio/quantum-observable-universe/lean/QOU/Mass/MilnorSignRepObstructionTripleChannel.lean), six declarations, **`lean -DautoImplicit=false -s 65536` exit 0**, `#print axioms` on all six showing only `propext` / `Classical.choice` / `Quot.sound` — **no `sorryAx`**.

- `sign_equivariant_scalar_eq_zero` — a transposition has `signR = −1`, so `signR g · c = c` forces `c + c = 0`.
- `equivariant_linearMap_to_trivial_eq_zero` — the companion of `equivariant_linearMap_eq_zero` with the target changed to a scalar carrying the trivial action.
- `muBar_cannot_carry_symmetric_channel` — and this is the one that bites: the probe above establishes the data requires `tripleMutual = −8.09991876` MeV **≠ 0**, which discharges the theorem's `hne` hypothesis **from measurement**. So the required attractive channel **cannot be a linear functional of `μ̄`**, for any coefficient, over any commutative ring without 2-torsion.

This closes the linear-in-`μ̄` route from the **symmetry** side, independently of `μ̄`'s normalisation — i.e. it does not rely on the type argument at all, so the two refutations are now genuinely independent rather than adjacent.

**Anti-vacuity, both directions, because a Schur argument is easy to over-read.** `sq_functional_is_equivariant_and_nonzero` exhibits `x ↦ x²` as equivariant into the trivial rep and not identically zero — so **linearity is load-bearing**, and the surviving coupling is through `μ̄²` / `|μ̄|` exactly as `muBarFamily_sq_invariant` says (unsigned, which is why it does not rescue attraction — but that is a separate argument, not this theorem's). `exists_nonzero_equivariant_into_trivial_of_trivial_source` shows the conclusion comes from the **sign source**, not from the target being small.

**Scope (a), narrowly.** Excludes `tripleMutual = (linear functional of μ̄)`. Does **not** exclude: `μ̄` through `|μ̄|` or `μ̄²`; `μ̄` fixing sign and order in a multi-term closure whose sizes come from elsewhere (the shape `MilnorCarriesOrderNotMagnitude` explicitly leaves standing); any non-`μ̄` three-body invariant; or **a channel that is not S₃-symmetric because the components are distinguishable**.

**That last one is the live escape, and it is `qou-lq6k`'s actual subject** — an explicit antisymmetry-breaking weight. Note the physical opening: a triton is `(p,n,n)` and ³He is `(p,p,n)`, so the components are **not** interchangeable and the full S₃-equivariance this theorem assumes is stronger than the physics requires. `MilnorSignRepObstruction.coupling_vanishes_on_charge_bilinears` already closes the obvious charge-bilinear form of that idea, so the opening is narrower than it first looks. **I am not proposing a candidate weight** — proposing one because it would fit is the anti-fit violation, and `qou-edt7` says so in as many words. Recorded as where the door still is, not as a plan.


---
**🛑 I RETRACT TWO OF THE THREE THINGS I TOLD `qou-rwhv` — 2026-09-12. Both retractions go in THEIR favour, and one of them told a sibling not to record a result they had earned.**

My convergence entry above scoped #7198's result on the strength of bean `qou-rwhv` **as it stands on `main`**, not on their branch. Reading their PR body shows two of my three points were answering questions they had already closed.

**RETRACTED (1) — "neither branch has met `qou-rwhv`'s settling condition, so *two shadows of the classical Mayer sign* should not be recorded."** They met it. The bean asks to *"exhibit the polymer / cluster model whose activity expansion has the corpus's `b₃` as its third Ursell coefficient — name the polymer set, the weight, and the compatibility relation"*. Their body names all four plus the ensemble: sites = the nucleons of one fixed nucleus; activity `z_i` with hard core `z_i² = 0`; pair weight `μ_e` = the interface-letter trace; Mayer-graph compatibility; grand canonical over sub-clusters `T ⊆ S`. Matched as `Z_T = ∏_{e⊆T} μ_e = tr_M(atom T)/tr_M(free T)` to **2.5e-60** at A = 2,3,4, with `ln Ξ = Σ z^T φᵀ_T` verified symbolically through n = 4. **This is the worst of the two**: I told a sibling to withhold a claim on the grounds that a condition was unmet, when their own branch had discharged it.

**RETRACTED (2) — "your route assumes repulsiveness where mine derives it."** I took `qou-rwhv`'s flag (*"nothing in the corpus identifies them with an exponentiated potential"*) to mean the Boltzmann reading was load-bearing for them. It is not. The hypothesis their result needs is in **Mayer variables** — `g_e = μ_e − 1 ∈ (−1,0)`, i.e. `μ_e ∈ (0,1)` — and they **measured** it: pp `0.61269`, pn `0.50823`, nn `0.40363`, with `phi3_pos` proved on `(0,1)³`. The Boltzmann identification is interpretation, not premise. So there was no hypothesis of theirs for my arithmetic to discharge, and my offered bridge answered a closed question.

**STANDS (3) — the routes are not independent**, and their body says it more plainly than I did: `Z_T = ∏_{e⊆T} μ_e` is a product over pair bonds, and they write *"the log assembly is exactly pairwise"*. Class-level agreement, which is a strengthening rather than a caveat.

**The lesson is the one this corpus keeps re-learning, one level out:** a bean on `main` is a snapshot, and scoping a sibling's *live* result against it is the same error class as quoting a stale figure. AGENTS.md already says a sibling's bean is not a primary source; the branch is.

**What their measurement buys my side, which is more than I expected.** Their scope-(a) escape (*"an attractive Mayer channel — a letter with trace > 1; none in the production word, measured"*) and mine (*"a positive `b₃` needs an attractive channel; `countChannel` at `q > 1` is repulsive by construction"*) are **the same escape** — and they have **measured that the production word contains no letter that could supply it**. That is strictly stronger than my arithmetic, which only rules out `countChannel`.

**JOINT STATE, supported by neither branch alone:**

> The attraction the data requires has **no source in the production word's letters** (theirs, measured) and **no source in a symmetric channel linear in `μ̄`** (mine, proved sorry-free).

Both remaining doors are the same shape: something **not pairwise-generated**, or **not S₃-symmetric because the components are distinguishable** — which is `qou-lq6k`, open since 2026-08-01.

**Flagged, not adjudicated:** their `b₃` is per-species (³H `+1.8081`, ³He `+1.0443`) while `pair-locality-shortfall.witness.json` carries the isospin-symmetric `b₃ = 1.42622016` against `b₂ = 2.2245662`. Two decompositions, both in the corpus; not a discrepancy, and not mine to settle.


---
**I OVER-STATED MY OWN HYPOTHESIS, AND FIXING IT CLOSES THE DOOR I HAD JUST CALLED THE ONLY ONE LEFT — 2026-09-12. Then the fix needed its own scope correction.**

Two entries above I recorded the live escape as *"a channel that is not S₃-symmetric because the components are distinguishable"* — a triton is `(p,n,n)`, so full S₃-equivariance is stronger than the physics requires — and named `qou-lq6k` (an explicit antisymmetry-breaking **charge weighting**) as the sole remaining door. **Re-reading my own proof shows that escape is much smaller than I said.**

`sign_equivariant_scalar_eq_zero` invokes its equivariance hypothesis at **exactly one transposition** (`Equiv.swap 0 1`). Full S₃-equivariance was never needed. All the argument requires is **one** swap under which `μ̄` flips and the channel does not — and a nucleon triple always has one, because **there are only two species, so any three nucleons include two of the same kind** (`exists_identical_pair`, pigeonhole on `Fin 3 → Fin 2`, decided exhaustively over all 8 assignments).

Stripped of the representation theory the argument is three lines: linearity gives `T(−μ̄) = −T(μ̄)`; invariance under the swap gives `T(−μ̄) = T(μ̄)`; together `T(μ̄) + T(μ̄) = 0`. No group action, no Schur.

**This closes the form `qou-lq6k` actually proposes.** A *charge* weighting is a function of **species**, so it assigns the two like nucleons the **same** weight and leaves the swap a symmetry of the weighted channel. Charge cannot break an antisymmetry between two neutrons, because charge does not distinguish them.

Three declarations added, all sorry-free, `lean -DautoImplicit=false -s 65536` **exit 0**, `#print axioms` on all **nine** in the file clean (the two new physical ones need only `propext` / `Quot.sound` — not even `Classical.choice`): `exists_identical_pair`, `linear_in_muBar_vanishes_of_identical_pair`, `muBar_cannot_carry_nucleon_triple_channel`.

**🛑 And then I over-claimed the fix, and caught it before committing.** My first draft of the new section said the obstruction *"applies to every nucleon triple in every nucleus"*. **Species is not the only label a nucleon carries.** Two neutrons agree in species but may differ in **spin**, and two components in different states need not leave the channel invariant when exchanged — so `hflip` fails for such a triple and nothing here applies to it.

**Honest statement, now in the file:** a weighting that is a function of **species alone** cannot break the antisymmetry. A weighting distinguishing the two like nucleons by some **further quantum number** is untouched, and **spin is the obvious candidate**. That is a narrower and more specific open question than `qou-lq6k` had this morning — not a closed one. I am not proposing such a weighting; proposing one because it would fit is the anti-fit violation `qou-edt7` names.

**Correcting my own end-of-turn line from the previous turn.** I told the author `qou-lq6k` was *"the sole remaining door … derive a weight that breaks S₃ without being a charge bilinear"*. Two things were wrong: the charge-**bilinear** form was already refuted by `coupling_vanishes_on_charge_bilinears`, but so is **every** charge weighting, bilinear or not, by the argument above; and the surviving door is not "breaks S₃" but the much narrower "distinguishes two nucleons of the same species". `qou-lq6k` stays OPEN with its subject rewritten.


---
**THREE INDEPENDENT ROUTES NOW GIVE `b₃ < 0` — and that pattern, not any one of them, is the finding. 2026-09-12.**

As of this morning the corpus has three routes to the connected three-body channel, on three different branches, by three different constructions, and **all three give the wrong sign**:

| route | branch | three-body result | AME |
|---|---|---|---|
| crossing count channel (`w3 = countChannel`) | #7193 (this) | `tripleMutual = +0.627` (needs `−8.09991876` MeV) | — |
| Mayer/Ursell cluster expansion of the lattice gas | #7198 | `b₃ = −1.2277` MeV (³H), `−0.7973` (³He) | `+1.8081` / `+1.0443` |
| trace's dominant summand, Ursell-inverted | #7200 | `b₃ = +0.4829` (³H), **`−0.3907`** (³He) | `+1.8081` / `+1.0443` |

#7200's mirror pair carries **opposite signs**, which is its own defect. And its deuteron comes out **anti-bound** (`e₂ = −0.0230` MeV against AME `+2.2246`).

**The honest headline is about the model, not about any one construction:** *as it currently stands, the framework's three-body channel is systematically repulsive, across every construction anyone has tried.* That is a real negative about the physics, and it is worth more than any of the three individually — three constructions failing the same way is evidence about a shared premise, not three separate accidents. The shared premise is visible in at least two of them (pairwise generation); whether #7200's dominant-summand route shares it is **not established here**.

**🛑 RED-TEAM OF MY OWN CONTRIBUTION, since I should not let it read as bigger than it is.** The theorem I proved today is **three lines** and mathematically near-trivial: `T(−x) = −T(x)` by linearity, `T(−x) = T(x)` by invariance, done. Its value is entirely in two observations, neither deep:

1. the existing corpus theorem (`MilnorSignRepObstruction`) had the **wrong target** — the pair-channel module, not the scalar the binding channel lives in;
2. **pigeonhole**: only two species exist, so species can never supply the breaking.

And it is a **second** nail in a coffin the corpus had already closed — `MilnorCarriesOrderNotMagnitude` refuted `μ̄` on type in August. Do not cite today's work as *refuting the Milnor route*; it was refuted. What is new is that the exclusion now runs through **symmetry** as well as type, so it survives if anyone ever repairs the normalisation objection.

**The reusable part is the pigeonhole, and it generalises past `μ̄`.** Nothing in `linear_in_muBar_vanishes_of_identical_pair` is about Milnor: it applies to **any** invariant that flips under exchanging two components. So the statement worth carrying forward is *no antisymmetric-under-component-exchange invariant, coupled linearly, can carry a channel that is invariant under exchanging two same-species nucleons* — and species can never break that, only a finer label (spin) can.

**Coordination performed, recorded because it is durable work:** #7200 shipped `QOU/Mass/OneRowBlockLetterProduct.lean` marked **⚠ NOT COMPILED** (their container had 7.8 GB free against the ≥ 8 GB a cache restore needs) and asked a reviewer to verify it. I had a live olean cache, so I did: branch head `39cd170452f`, `lean -DautoImplicit=false -s 65536` **exit 0**, `#print axioms` on `map_letter` / `map_word_eq_prod` / `map_word_append` all `propext` + `Quot.sound`, **`sorryAx` 0** — not even `Classical.choice`. Their anticipated `simp`-set gap did not materialise. Verified by copying to its real path, compiling, and deleting; nothing of theirs is committed here and I did not touch their branch.


---
**THE LAST DOOR IS OPEN BUT UNBUILT — and the one route to building it is PROVED not to lift. Corpus-grepped 2026-09-12; I am stopping the arc here rather than manufacturing the missing object.**

I recorded spin as the surviving escape and greped it before touching it. Six paths (path 0 `corpus_search` **DOWN** again — `paper-assistant` `ENOENT` — so `emptyRoots` unchecked and a vocabulary blind spot is **not** ruled out; everything below is grep-derived).

**Spin IS represented — in FOUR inequivalent, unreconciled senses**: `SpinLabels`/`SU2SpinLabels` (SU(2) label `j`); `BoundedPartition.spin` (`j = (λ₁−λ₂)/2`, from a two-row Wedderburn partition); `LocalizedKnot.intrinsicAngularMomentum` (`J = c(K)/2`, crossing number over two); and the `SpinFromSo3Fiber` conjecture class. Plus `nuclear-spin-parity-proof.md`'s spin-statistics from **writhe** (`w` even ⟺ bosonic ⟺ `J ∈ ℤ`; odd ⟺ fermionic ⟺ `J ∈ ℤ+½`).

**🛑 THE TRAP, AND IT IS EXACTLY MY RESULT'S SUBJECT.** The corpus's single most spin-named object — `knots-particles-confinement/spin-involution`, 15 Lean declarations — **is not about spin**. It is a `*`-antiautomorphism whose output is **isospin**: `T₃(a) = ½·sgn_σ(a) ∈ {−½,0,+½}`, grading `A = A₊ ⊕ A₋` while calling the sectors "spin-singlet/spin-doublet". An agent grepping `spin` lands on it first, and would reach for it as the antisymmetry-breaking label.

**It cannot be that label, and my own pigeonhole is what says so.** Isospin **is** the species label — it is `p` vs `n`. `muBar_cannot_carry_nucleon_triple_channel` excludes exactly the species-dependent weighting, so the most inviting "spin" object in the corpus is precisely the one already closed. Worth stating loudly, because the name points the wrong way. (Counts confirm the naming hazard: `isospin` 313 files against `spin-singlet` 28, and `isospin` *contains* `spin`, so every non-word-boundary grep is dominated by it.)

**What genuinely exists, and it has the right SHAPE.** `qou-m896` (**completed**): the antisymmetric Hecke block carries a negative eigenvalue — T=1 (symmetric) gives `|μ| = q > 1` ⇒ UNBOUND; T=0 (antisymmetric) gives `|μ| = 1/q < 1` ⇒ BOUND, at `β = 0`, *"a pure σ crossing carrying NO FLAVOUR INFORMATION AT ALL"*. **Species-free exchange antisymmetry producing a sign** — exactly the shape the pigeonhole leaves room for. Its cap is **exactly 1**, attained only at `β = 0`, against nature's 33.7055.

**And here is why I stop.** `qou-r1yj` (**completed**) proves the Pauli forcing **does not lift to the arity my triple lives at**:

> *"AND THE IDENTIFICATION STOPS BEING FORCED. At n=2, Pauli forced it… Here exchange parity is NOT locked to magnitude — `q², q³, q⁵, q⁶` each carry BOTH signs — so the two labels no longer pick out two channels with two values."* *"Recovering the sign pattern at six strands requires choosing an unbound channel **BY HAND**, and nothing forces which."*

Three strands per nucleon is exactly where a three-body channel lives. So the route that *would* build a species-free spin antisymmetry is proved not to reach it, and the only way through is a **hand-chosen channel** — which is selection against the target, forbidden by §NO FITTING.

**The object itself is absent, not merely unused.** `qou-o43i` (in-progress), measured from field lists rather than names: *"`fIso` is available; **`fSpin` does not exist**… no other `.lean` in the tree carries one… the equal-scalars identification is **un-instantiable at present** — stronger than un-instantiated."*

**So the honest status of the last door is neither "open" nor "closed": it is UNBUILT.** Saying "spin is the remaining route" overstates it — there is no spin function to weight with, and the one construction that forced the spin↔exchange link is proved not to lift to this arity. **I am not building `fSpin` and not choosing a channel.** Doing either to get the sign would be the anti-fit violation, and `qou-r1yj` has already established that nothing forces the choice.

**Scope discipline for whoever writes this up:** the grep found **no named proved invariant** forbidding a spin-dependent weight in a triple channel. The four existing spin refutations are a 2-body magnitude degeneracy (`InterfaceScalar.separable_interface_degenerate` — different arity, and it constrains magnitude degeneracy, **not** a sign under component swap), a `Δ_λ` magnitude failure (Pauli/Wigner-SU(4) plethysm, zero free parameters, deuteron −92.69 %), an SU(4) row bound (correctly scope-(b), and **vacuous for `n ≤ 4`**), and a dimension-count coincidence. **Any refutation written here is scope-(a).** Do not write (b).

**One library note.** `arxiv-1906.12122v2` (Hammer–König–van Kolck) is held, registered and already cited by `T3WritheVsDeltaLambdaSign.lean` as the `τ₁·τ₂` exchange-symmetry template — so the literature side of this is not a gap. And Moffatt–Ricca is already used, in `fluid-dynamics/helicity-conservation.lean`, as **hypotheses** (`hCWF`, `hSelf`, cited not proved) and in the **fluid** chapter rather than the nuclear one.


---
**2026-09-13 — OPTION 1 RE-AIMED. The bean's "form of `w3`" question has been answered on `main` while this bean sat at `todo`, and the live frontier is now ONE hypothesis, not the Habiro route.**

Owner instruction this session: *"work qou-ix0x — push option 1 as far as possible. then option 2"*, against the `qou-brng` framing of 2026-09-13 (Option 1 = a further derived source of per-pair variation inside the bond/count channel; Option 2 = the channel is not where `b₃` lives).

**What landed on `main` since this bean's last entry (2026-09-11), none of it recorded here.** The 2026-09-12 Ursell arc turns the `b₃` sign into an exact algebraic condition:

- `QOU.MassTheory.B3SignOneRoot.b3corpus_chain` — `b3corpus f01 1 f12 = −((f01−1)(f12−1))` exactly. So **`b₃ > 0` iff EXACTLY ONE of the two chain bonds exceeds 1.** Not "a bond above 1" — the AGENTS.md bullet and the Ursell audit §4 both said that and it is necessary-not-sufficient; flipping *both* bonds leaves `b₃` byte-identical.
- `PnBetweennessBlocksSignMixed` (`qou-q8vl`) reduces the escape to **two hypotheses**: the pn letter's AVERAGING, and AFFINENESS of the interface law `μ = z + d`.
- The required pattern is the two-nucleon spectrum: unlike pair binds, like pairs do not.

**Option 1's live route is the γγ ruling, and it is DERIVED, not chosen.** The owner ruled 2026-09-08 (`qou-ales`) that every canonical braid word is selected by γγ pair-production + the confinement SDP. `QOU/Mass/GammaGammaEscapesSingleCrossing.lean` (sorry-free, on `main`) then establishes: no non-empty γγ word is a single crossing (`length_even`), the writhe/`T₃` grading is identically trivial on one (`writhe_eq_zero`), and step 3 MEASURED the γγ-selected bond `G³ = (σ₂σ₃⁻¹)³` **unbinding the diproton** — `tr_atom/tr_free = 1.001058 > 1`, `B_pp = −4.47` keV.

That is `μ_pp > 1` by derivation, which is the like-pair half of the required pattern, and it breaks AFFINENESS (a length-6 word is not `σ + d·1`). `qou-q8vl`'s open item is literally *"a THIRD bond family that supplies the sign-mixed pattern by derivation"*; `qou-ales` step 8's own not-claimed list names *"the dineutron side"*. **Neither arc has connected to the other.** That junction is this bean's Option-1 push.

**THE DECISIVE MEASUREMENT, and I state the failure mode BEFORE running it so the result cannot be read as a fit.** Under γγ the bond WORD is the same `G³` for every pair; only the nucleon blocks `W_free(Z,N)` differ. Step 3 records that the template ratio equals `z_D` *"by connected-sum multiplicativity"*, which suggests `μ = tr(W_free·bond)/tr(W_free)` is **independent of `W_free`**. If it is:

> a pair-type-INDEPENDENT bond word gives `μ_pp = μ_pn = μ_nn`, so the two chain bonds are equal, so they are never on opposite sides of 1, so `b₃ < 0` — and **Option 1 closes structurally**, not numerically.

The γγ route then survives only if the SELECTED WORD is itself pair-dependent (the deuteron SDP choosing some `G^m`, m ≠ 3). Step 3 solved the diproton only.

So the measurement is: compute `μ = tr_M(W_free·bond)/tr_M(W_free)` at `(Z,N) ∈ {(2,0),(1,1),(0,2)}` for the template `σ₂` bond and for `G³`, and read off whether it depends on `(Z,N)`. Nothing is tuned: the word is fixed by a ruling dated three days before this session and made for reasons unrelated to `b₃`; the sign condition is Lean-proved. **A negative here is the expected outcome and is the result** — it would convert `qou-q8vl`'s two-hypothesis disjunction into a one-line structural statement about what a bond family must do.

Branch `claude/b3-affineness-is-the-last-hypothesis-2026-09-13`.


---
**2026-09-13 — BOTH OPTIONS PUSHED TO A STRUCTURAL STOP. Neither closes the gap, and TWO of my own stated predictions were refuted along the way.**

Audit: [`2026-09-13-b3-sign-options-1-and-2-at-the-gamma-gamma-junction.md`](../docs/audits/2026-09-13-b3-sign-options-1-and-2-at-the-gamma-gamma-junction.md). PR #7287.

### Option 1 — the γγ bond IS pair-dependent, and still cannot sign-mix

Probe `gamma_gamma_bond_is_pair_independent_probe.py`, 11/11, 60 dps, proton pin.

| ordered pair | μ(template σ₂) | μ(G³) |
|---|---|---|
| pp | 0.612688037146465252 | **1.00105775254515984** |
| pn | 0.612688037146465252 | **1.00061119140688078** |
| np | 0.612688037146465252 | **1.00105775254515984** |
| nn | 0.612688037146465252 | **1.00061119140688078** |

**My stated expectation was REFUTED.** The entry above recorded, before the run, that the likely outcome was pair-INDEPENDENCE. `G³` is pair-DEPENDENT — spread `4.47e-4` against the template's `1.6e-61`.

**Option 1 closes anyway, for a sharper reason: ALL FOUR exceed 1.** So every `A=3` chain gets TWO bonds above 1, never exactly one, and `b3corpus_chain` gives `b₃ < 0` on both atoms (³He `−6.46e-7`, ³H `−3.74e-7`).

**And the dependence is ONE-SIDED.** The `np` order-reversal control gives `μ_np = μ_pp` and `μ_pn = μ_nn` to `1.6e-61`, while `μ_pn ≠ μ_np` by `4.47e-4`. So μ is not a function of the PAIR — it is a function of the SECOND nucleon, i.e. **order-dependent**, and `ChainBondOrderDependence.orderIndependent_iff` records that a nucleus has no arrangement. **Mechanism MEASURED, NOT PROVED**: `G³`'s `σ₃` is inside block 1, but `G³` also carries `σ₂`, adjacent to block 0's `σ₁`, so far-commutation does not explain it.

### Option 2 — the γγ assembly is EXACTLY AFFINE, which is the wrong side

Probe `gamma_gamma_aggregator_convexity_probe.py`, 6/6, `A=3` in `H₉`, restricted to the `y_λ>0` blocks (the 25 dropped carry `y=0` exactly — verified, a restriction not an approximation).

`δ := μ_both − μ₀·μ₁` is `0` to the 60-dps floor on all four contents — **the same floor as the template control**. So the bond product HOLDS for `G³`, the log-assembly is additive in bond count, and `qou-82mc`'s `b₃` is **0, not positive**. **My second prediction (non-affineness) was REFUTED too.**

Two by-products worth keeping:
- **`ProductionChainBondProduct`'s strand-window hypotheses are SUFFICIENT but NOT NECESSARY** — `G³` violates them and the product holds anyway. A note for `qou-qqm4`, not a defect.
- The per-content `δ` signs (`−,+,0,0`) are **round-off at the arithmetic floor, not structure**; asserted in the probe so "MIXED" is never quoted as a finding.

### What this changes for the front

`PnBetweennessBlocksSignMixed` left two escapes — break averaging, or break affineness. **The γγ family breaks BOTH and still fails.** So that disjunction is not the binding constraint; **every bond factor landing on the SAME SIDE of 1 is**, which is sharper than the two hypotheses it replaces.

**NOT claimed:** that no bond family exists; that no convex `Φ` exists; any magnitude; that the one-sidedness mechanism is understood.

**This bean's own Habiro/cyclotomic route is untouched and still unexcluded** — it was not worked here, and nothing above bears on it.


---
**2026-09-13 (later) — LEAN. Owner asked "Lean.prove assertions?". Two of the thirteen had provable content, and the first CORRECTS my own framing above.**

`QOU/MassTheory/SecondArgBondNotPairFunction.lean`, 7 decls, `lean`-direct **exit 0, ZERO errors and ZERO warnings** (`-DautoImplicit=false -s 65536`, restored cache 3480 mathlib + 2713 QOU oleans, traces present). `#print axioms`: six on `[propext]` alone, one on `[propext, Classical.choice, Quot.sound]` from `classical`. **No `sorryAx`.**

**Most assertions are NOT theorems** — they are numeric measurements at `q₀`. The structural ones were already proved on `main` (`b3corpus_chain_neg_of_same_sign`, `b3_eq_zero_ofBondFunctional`) and are cited, not re-proved. Saying so rather than manufacturing Lean around measurements.

**The correction.** The entry above says the one-sidedness makes the bond *"order-dependent, and `ChainBondOrderDependence.orderIndependent_iff` records that a nucleus has no arrangement"*. That is weaker than the truth. `bondOf` is **symmetric in its two nucleon arguments by construction** (`bondOf_comm`), so

    secondOnly_eq_bondOf_iff : (∃ Lpp Lpn Lnn, secondOnly f = bondOf …) ↔ f true = f false

— a second-argument-only bond is **not of the `bondOf` form at all** unless constant. The corpus's chain calculus is stated over `bondOf`, so the γγ bond falls **outside its domain** rather than violating its conclusion. Measured `f true = 1.00105775 ≠ 1.00061119 = f false`, so it is not any `bondOf`. Two anti-vacuity guards included (`secondOnly_const_is_bondOf`, `bondOf_ne_secondOnly_witness`).

**Second:** `weighted_diff_supported_on_multidim` formalises the cross-arc reconciliation with `qou-99qc`/#7295 — if every 1-dim block agrees on two words, the whole weighted-character difference sits on dimension `≠ 1`. The reconciliation no longer depends on `q₀`.

**NOT claimed:** that the γγ bond is wrong, that the one-sidedness mechanism is understood (still measured, not proved), or anything about γγ word selection.


---
**2026-09-13 (later still) — MY FRAMING WAS WRONG AND A SIBLING CAUGHT IT. The measurements stand; what they MEAN is better than I said.**

Five coordination comments landed on #7287 while I was working. One (from `qou-2ss0` / PR #7255, merged) corrects this bean's own framing, and I verified it against `origin/main` rather than taking the comment as primary.

**What I said:** *"`PnBetweennessBlocksSignMixed` left two escapes — break averaging, or break affineness. The γγ family breaks BOTH and still fails."*

**Both halves are wrong.** `InterfaceMonotone.between_iff_combo`: betweenness and convex-combination are the **same condition**, so averaging is not separately breakable. And `signMixed_impossible_of_monotone` holds for **any monotone law, affine or not** — its docstring: *"abandoning affineness, on its own, buys nothing: the construction is dead before any bond value is computed."* **The invariant is MONOTONICITY, not affineness.**

**The correction makes my negative STRONGER, not weaker.** `μ(x) = tr_M(W·x)/tr_M(W)` is linear in `x`, so any *affine path* is monotone-or-antitone and blocked either way. `G³` is a **power, not a sum** — not an affine path — and the power family is independently measured non-monotone. So the γγ route occupies the one structurally-permitted door, and §1's result is a measurement of a **live candidate**, not a foregone conclusion.

**And my own Lean supplies the cleaner reason.** Both hypotheses are about a *pair function* `f(d_pair)`. `secondOnly_eq_bondOf_iff` shows the γγ bond is **not a pair function at all**. It is outside the framework's domain — which is why "it breaks affineness" was the wrong thing to say.

**A conflation to avoid**, flagged before anyone makes it: the sibling's measured non-monotone family is `μ(σ^m)` — powers of ONE generator, `μ > 1` at `m = 2,4,5,6,7,8` and NOT at `m = 3`. Mine is `μ((σ₂σ₃⁻¹)^m)` at `m = 3`, where I measure `μ > 1`. **Different objects**; there is no conflict, and the coincidence of the index `3` is exactly the kind of collision AGENTS.md's notation rules exist for.

**Scope question answered** (from #7304/#7319, owner ruled SDP scope **(B) whole element**, not (A)): my Options 1/2 closure does **not** lean on PSD scope at all. `G³` is taken as GIVEN from `qou-ales` steps 6–7; I re-derive no selection. So the (A)→(B) ruling does not move anything here.

## 2026-09-14 — the FIRST BRICK is answered, and it dissolves. My own framing was wrong.

Options 1 and 2 merged (#7287, `db8d3cefd9`); #7256 merged (`20e40ba1c4`). Both replay-verified.
Then the brick, which needed no compute.

**The brick asked:** *"whether pair-locality itself is derivable at a root of unity … if
pair-locality is genuinely a generic-`q` fact, the theorem has no hypothesis to stand on there."*

**The antecedent is false.** Pair-locality is not a generic-`q` fact; it is not a corpus fact at
any `q`. Three measurements on `main` `db8d3cefd9`:

1. **`PairLocal` contains no `q`** — `(∀ i j k, w3 i j k = w2 i j) ∧ (∀ i j, w4 i j = w2 i j)`
   over a generic `{R : Type*}`. There is nothing in it for a root of unity to act on. Whether
   it holds is a fact about how a carrier populates `w2/w3/w4`, not about the fibre `H_n(q)`.
2. **The proved direction is the refutation, and it is `q`-free.** `not_pairLocal_of_b3_ne_zero`
   reaches `¬PairLocal` from the measured AME `b₃ = +1.4262225` MeV — its own file calls this
   "the load-bearing direction … from data with no unsatisfied hypothesis at all".
3. **The bridge I cited as established is flagged conjectural in the audit I cited it from.**
   `2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md` §2: *"§2 states this as a
   **conjecture to prove, not a theorem** — the bridge from 'formal' to 'pair-local' is the thing
   to formalise first."* Its §2.1 "What is proved" lists `HH^{k≥1} = 0` and both directions of the
   pair-locality implication, and does **not** list "pair-locality holds".

**So `b₃` is ALREADY unconstrained by `b3_eq_zero_of_pairLocal` at every `q`, `q₀` included**, and
a root of unity buys nothing on this lever — it was never locked. An agent proving "pair-locality
fails at roots of unity" would be negating something nobody proved, against a `q`-free predicate.

**This re-aims the Habiro route rather than weakening it.** What genuinely holds at generic `q`
and fails at a root of unity is **semisimplicity**, hence `HH^{k≥1} = 0` — the audit's "higher
structure" row, recorded as invisible to `tr_M` because `tr_M` is the Euler characteristic.

**Sharpened brick (the next one):** does `tr_M` acquire anything to see where `H_n(q)` is not
semisimple? Degree 0 of a complex does not change when higher degrees become non-zero; an Euler
characteristic does. Which is `tr_M`, and does the difference reach `q₀`? That is well-posed, is
not about `PairLocal`, and is where ROAST item 4 already pointed.

**Method note.** I asserted the `HH`→pair-local bridge as background in this bean's own body.
Checking it cost one grep, and the cited audit's next sentence said it was conjectural. **A bean
is not a primary source — including one's own.**

Write-up: `docs/audits/2026-09-14-pair-locality-is-not-a-generic-q-fact-the-brick-dissolves.md`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-10-12 — the cyclotomic route is answered, in the NEGATIVE, and this bean stays open

The ring-hom question this bean raised as item 4 is settled, sorry-free, in
`QOU/Habiro/CyclotomicEvaluationRingHom.lean` (salvaged from the unlanded PR
#7225 and repathed onto `main`; see `docs/audits/2026-09-12-cyclotomic-evaluation-is-a-ring-hom.md`).

**A dichotomy, and it shuts the door on both sides.** At a root of unity `ev_ζ`
*is* a ring homomorphism — `cyclotomicQuotientEval` is the induced `→+*` out of
`R[q]/((q;q)_N)`, the object the Habiro ring is the inverse limit of — so
#7216's `bondSum_map` transports verbatim and class D's exclusion extends
through the cyclotomic rendering. Off the roots of unity there is no rendering
at all: over a domain `(ζ;ζ)_N = 0` forces `ζ^k = 1`, so at a non-root-of-unity
point the truncations never stabilise and there is nothing to render.

**ROAST item 4 is therefore answered in the negative**: root-of-unity data does
not reach `q₀ ≈ 1.11` *by evaluating*. The "archimedean instance at the
substrate pin" the draft's own docstring promised cannot exist — a file of that
name would contradict §4 of the file promising it.

**This bean stays `todo` (§13a).** Its subject is the binding's missing
super-pairwise extensive object, which is open; what closed is one proposed
route to it, and closing a route is not closing the question. The 2026-09-14
entry above ("pair-locality is not a generic-q fact") is a *different* strand
and is untouched here — the sharpened brick it names (does `tr_M` acquire
anything to see where `H_n(q)` is not semisimple?) is still the live one.

**Caveat on the framing, not on the result.** #7216 is **not merged** —
`bondSum_map` does not exist on `main`, and the only occurrences of that name in
the tree are inside the new file's own prose. The new file is written so as not
to depend on it (`map_bondCount` / `quotientEval_bondCount` state the transport
directly), so the mathematics stands alone; but "the hinge under #7216 class D"
describes a hinge under something still on a branch.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Round 68 Formalization Progress (PR #8285)
- Formalized `QOU.Mass.MilnorCarriesOrderNotMagnitude.geometric_order_step_diff_and_hankel_zero` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/twobody_deficit_regulator_sdp_milnor_probe.py`, `scriptHash: 39a564805d3e`, Commit 1 `70bec575bb493c7f91cf1b39cb54e58ef8343777`, Commit 2 / Witness `250465c60a6cea44d9f569e88cc79ee2c8d8051b`, PR `litlfred/qou#8285`).
