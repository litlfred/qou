---
# qou-ix0x
title: The binding's divergent series is G, its Borel-Stokes plane is EMPTY, and the untried summation is the Habiro/cyclotomic one
status: todo
type: task
priority: normal
created_at: 2026-09-07T08:46:20Z
updated_at: 2026-09-07T08:48:33Z
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

**Closed:** [`QOU/Mass/MilnorSignRepObstructionTripleChannel.lean`](../content/quantum-observable-universe/lean/QOU/Mass/MilnorSignRepObstructionTripleChannel.lean), six declarations, **`lean -DautoImplicit=false -s 65536` exit 0**, `#print axioms` on all six showing only `propext` / `Classical.choice` / `Quot.sound` — **no `sorryAx`**.

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
