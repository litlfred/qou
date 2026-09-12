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
