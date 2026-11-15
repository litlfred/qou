# Word-dependent "isospin" maps on the Q_β nucleon words: an exhaustive search, and what literature says isospin is

Owner requests, relayed by the coordinator (session_01M5GA1LmsEf8tSMxFjMkmnn) on 2026-11-15:
*"Search for word-dependent maps."* and *"try Derive the right isospin involution --- need lit?"*.
The owner's reading of #7862 was that bar acts on every letter uniformly, whereas isospin
should flip flavour only.

* Beans: `qou-z08b` (stream 12's gap; appended) and `qou-hlx8`. Epic `qou-qs0e`.
* Stacked on stream 12's branch `claude/bar-parity-split-close-gap-2026-11-15` (draft #7860),
  because `qou-z08b` exists only there.
* Probe (analysis only, writes **no** witness, computes **no** Q_β value, touches no
  dashboard): `computations/qbeta/qbeta_word_dependent_isospin_maps_probe.py`, 6/6 checks.
  It uses exact sympy throughout. The meet-in-the-middle step runs mod two primes, and every
  candidate it produces is then re-verified exactly.
* Every map was enumerated before any value was computed. Nothing was selected by closeness
  to anything.

## 0. Result

| family | maps tested | φ(n) = p as element | tr^{z_D}(φ n) = tr^{z_D}(p) | descends to H₃ |
|---|---|---|---|---|
| F1: flavour-only, core + gluon fixed, 6 actions per tail slot | 216 | **0** | **0** | — |
| F2: slot-dependent over all 11 slots, 6 actions per slot | 362,797,056 (= 6¹¹) | **0** | **1,296** (256 distinct image words) | **0 of 1,296** |
| F2 restricted to the 5 involutive actions | 48,828,125 (= 5¹¹) | **0** | 384 | 0 |
| F3: inner conjugation x n x⁻¹, x a reduced group word of length ≤ 3 | 53 | **0** | 0, by invariance | (inner by definition) |
| (iii) module map on the (2,1) block | the unique left multiplier | does not commute with the core or the gluon | — | — |

**Verdict: no derived isospin involution maps the neutron word to the proton word in any of
the formulations tested.**

* The 1,296 trace hits are word-level coincidences, not isospin. Every one rewrites **10 or
  11 of the 11 letters, the core included**. None acts uniformly per generator, so **none
  descends to an algebra map on H₃**. For each of them f_φ = tr(φn) − tr(p) = 0, so
  "g_φ bar-even" holds trivially and says nothing.

## 1. The per-slot actions

A letter is c·σ_g + k·h, where u = σ, d = σ − h and ud = σ − h/2.

| action | (c, k, g) ↦ | involution as a letter map? |
|---|---|---|
| id | (c, k, g) | yes |
| flip σ ↦ σ⁻¹ | (c, k − c, g) | **no**: flip² shifts k by −2c |
| bar | (c, −k − c, g) | yes |
| swap σ ↦ −σ⁻¹ | (−c, k + c, g) | yes |
| neg σ ↦ −σ | (−c, k, g) | yes |
| relabel | (c, k, 1 − g) | yes |

**Pruning.** None was needed. The meet-in-the-middle step covers all 6¹¹ maps, and family 2's
"involutions only" restriction is reported as the 5¹¹ subset.
* Element test: the first 6 slots are hash-joined against p·(last 5)⁻¹. All letters are
  invertible, with inverse (aσ + b)⁻¹ = (−aσ + ah + b)/((ah + b)b − a²).
* Trace test: the bilinear trace form tr(L·R) = Lᵀ B R, solved blockwise.
* Both tests run mod 1000003 and mod 999983. **A mod-p equality is necessary for an exact one,
  so the step cannot produce false negatives.** Every mod-p candidate (0 element, 1,296
  trace) was re-verified in exact sympy.

## 2. Family 1, flavour-only: zero hits

Keeping the core and gluon fixed and applying any of the 6 actions to each of the three tail
slots gives **0 of 216** element hits and **0 of 216** trace hits.

The obstruction can be seen at the letter level: no single action sends the neutron's slot-6
letter ud₀ = σ₀ − h/2 to the proton's u₀ = σ₀.
* bar fixes ud (#7862).
* flip gives σ − 3h/2.
* swap and neg give −(σ − h/2) up to a shift.
* relabel moves it to σ₁.

**Scope (a)**: the map set is these 6 actions per slot. An action outside the set (for example
a letter replacement that is not one of these involutions) is not tested.

## 3. Family 2, slot-dependent: 0 element hits, 1,296 trace hits that do not descend

Per-slot histogram of the trace hits, listing which actions occur:
* slots 0, 2 (u₀ in the core): {flip, bar, swap};
* slots 1, 3, 5 (d₁ in the core): {bar, swap};
* slot 10 (the last gluon letter): relabel in **all** 1,296.

**Never `id` on the core's d₁ letters or on the last gluon letter**, so every trace hit
rewrites the "flavour-neutral" core.

* **They do not descend.** An algebra map is determined by the images of σ₀ and σ₁, so a
  per-slot map can descend only if every slot carrying the same generator receives the same
  action. That necessary condition fails for **all 1,296**.
* **They are not isospin.** "Isospin" has to be at least a map on H₃, or a module map (§5). A
  map on words that does not descend is neither.
* **Element level, scope (b)** within the 6¹¹ set: **no** slot-dependent map of these actions
  sends n to p. The invariant is the exhaustive exact check.

## 4. Family 3, inner conjugation: impossible at trace level

The Markov trace is a class function, so tr(x n x⁻¹) = tr(n). Exactly,

  tr^{z_D}(n) − tr^{z_D}(p) = (q² − 1)(q⁴ + 1)·P₁₂(q)/(4q⁷(q² + 1)²) ≠ 0,

so **no inner automorphism of H₃ can map n to p.**
* Scope (b): the invariant is trace class-invariance together with this nonzero difference.
  It covers every x, not only the 53 words tested.
* The 53-word element check (0 hits) is a redundant confirmation.
* The same argument excludes **every trace-preserving algebra automorphism**, which is what an
  "isospin symmetry" of the decay functional would be.

## 5. Literature: what isospin is, and what Aut(H_n(q)) is

**Held, and read at the passages cited:**
* **Geck, "Hecke algebras of finite type are cellular"** (`library/arxiv-math-0611941v3`). It
  cites Lusztig 2003 §3.4–3.5 for three maps:
  * the A-linear **anti-involution** ♭ (Geck writes it as *): T_w ↦ T_{w⁻¹} (our *rev*);
  * the A-algebra **involution** †: T_s ↦ −T_s⁻¹ (our *swap*, the eigenline swap χ).
* **`library/hdr`** (Hecke algebras habilitation): the ring involution ι with ι(q) = q⁻¹ and
  ι(T_s) = T_s⁻¹, i.e. our **bar**.
* **`library/black-samson-phd2010sp`**: conjugation by an invertible element defines an
  automorphism, i.e. **inner** automorphisms.
* All of these act **uniformly on the generators T_s**. None is slot- or role-dependent.

**Not held, and not asserted: a classification of Aut(H_n(q)).** I found no held source
that classifies the automorphism group, so I do not claim that the list above is complete.
Candidates for stream 13 to fetch:
* G. Lusztig, *Hecke algebras with unequal parameters* (CRM Monograph Series 18, 2003),
  Ch. 3;
* M. Geck and G. Pfeiffer, *Characters of finite Coxeter groups and Iwahori–Hecke algebras*
  (LMS Monographs 21, 2000);
* a targeted search for "automorphisms of Iwahori–Hecke algebras".

**How the cited physics literature realises isospin:**
* **Furey's thesis, held** (`library/arxiv-1611.09182v1`, §7.3, pp. 65–66).
  * The SU(2)_L generators are **T_i = τ_i·ε↑↑**: quaternion units times an **idempotent**
    ε↑↑.
  * The "MTIS" symmetries act on the generating space as **e^{iφg} · e^{−iφg}**, which is
    conjugation by a unitary element, i.e. an **inner** automorphism.
  * The states form a **minimal right ideal** on which the group acts as a **module**: ν_R and
    e_R are singlets, (ν_L, e_L) is a doublet.
  * **The left-only action comes from the idempotent factor in the generator, not from a
    non-uniform map on letters.**
  * Furey 1806.00612 is **not held** (it is in neither `library/` nor `uploads/`).
* **Gresnigt**, held as `library/arxiv-1901.01312v1`, "Braided fermions from Hurwitz
  algebras", and `library/arxiv-2106.01332v4`, at the level of a grep read. Following the
  Bilson-Thompson helon model, electroweak interactions are **topological braid composition**,
  i.e. gluing or multiplication by a braid, which is again **not** an automorphism.
* **Günaydin–Gürsey**: not held.

## 6. Which of (i)–(iii) is admissible as "isospin"

* **(i) A map on words that does not descend: not admissible.** It is not a map on the
  algebra, so it is not a symmetry of anything. §3 shows that every word-level trace hit is of
  this kind.
* **(ii) An inner conjugation: admissible as a symmetry, and Furey's isospin is of this type
  at the algebra level.** But it is **trace-preserving**, so it cannot relate n to p in a
  trace functional (§4, scope (b)). Any effect it has must appear through a **state**, not a
  trace.
* **(iii) A module map on a state: the admissible class for "isospin acts on the nucleon".**
  This is exactly Furey's realisation: an inner symmetry acting on an ideal, made one-sided by
  an idempotent factor.

**Test of (iii) on the (2,1) block** (exact, seminormal 2-dimensional irrep ρ of H₃):
* ρ(p) is invertible, so an operator T with T·ρ(p) = ρ(n) is **forced**: T = ρ(n)ρ(p)⁻¹.
  It is not chosen.
* Result: T is not scalar, and it commutes with **neither** ρ(core) **nor** ρ(gluon).
* The tail-only operator T_t = ρ(n_tail)ρ(p_tail)⁻¹ has det T_t = 1 and
  tr T_t = (3q⁴ + 2q² + 3)/(q² + 1)². It also commutes with neither ρ(core) nor ρ(gluon).
* **So no (2,1)-block operator maps the p-state to the n-state while commuting with the
  core/gluon action.**
* Scope:
  * **(b)** for the left-multiplication-on-the-block formulation, because the operator is
    unique;
  * **(a)** for state-vector formulations, i.e. T v_p = v_n for a chosen vector, which need a
    choice of v and are not tested. The ideal formulation of D-I1 below is also untested.

## 7. Side question: does "bar breaks in three places" survive at trace level?

* tr^{z_D}(core) = −(q¹² − 3q¹⁰ + 2q⁸ − 4q⁶ + 2q⁴ − 3q² + 1)/(q⁴(q² + 1)²) is **bar-even**
  (exact).
* tr^{z_D}(gluon) = (q⁴ + 1)/(q² + 1) is **not** bar-even.
* So at trace level the core is bar-even even though its letters are not bar-fixed.
* The trace is not multiplicative, so isolated-segment parities do not combine into a
  statement about g. They are a lead for `qou-z08b`, not a decomposition.

## 8. Lean

Not formalised. The results are exhaustive NF and trace computations over 11-letter words;
a sorry-free Lean version would mean encoding the census multiplication table and
re-running the enumeration, which is not "small". The structural facts used (trace class
invariance, uniqueness of a left multiplier by an invertible matrix) are standard.

## 9. Owner decision

### D-I1: should "isospin" be formulated as a module map on a chirality ideal (Furey's shape), and tested?

* **(A) Yes, as a working hypothesis.**
  * *Means:* put the nucleon in a right ideal of H₃ (or of End V^{⊗3}) cut out by the
    chirality idempotent P₊. The idempotent is already derived: the one-sided vertex is
    W_L = s − h·P₊, #7844. Take isospin to be left multiplication by a derived element. Then
    test whether it maps the p-state to the n-state.
  * *Costs:* a probe plus small Lean; hours.
  * *Risks:* the state vector inside the ideal is a choice. If it is chosen to make p ↦ n
    work, that is selection against the target. The vector must be fixed first, e.g. by the
    γγ construction (`qou-ales`).
  * *Commits to:* treating isospin as acting on states rather than on the Q_β trace word.
* **(B) No.**
  * *Means:* record this search as the answer: no derived isospin on words or algebra maps
    n ↦ p.
  * *Costs:* none.

**Default if nothing is said: (B).** **Recommendation (judgement): (A).** It is the only
admissible class left (§6), and it reuses the derived P₊ rather than inventing a map.

## 10. HANDOFF: D-I1 = (A) received, work NOT started beyond the rule read (WIP, 2026-11-15)

The owner answered D-I1 with (A): test isospin as a module map on the chirality ideal H·P₊
(Furey-style). The stream was stood down before any computation, so **nothing below is a
result**. It records what was read and the planned test.

**State rule (step 1, read and not yet coded).** Two rules are on record, and neither fixes the
slot order uniquely, so the whole family must be tested:
* **D2**, `QOU/QuarkState/PhotonPairNormalForm.lean`, `nucleonState q c1 c2 c3`:
  * the word is ρ_{(2,1)}((σ₀σ₁⁻¹)³ · ℓ₀(c₁) ℓ₀(c₂) ℓ₁(c₃)), **with no gluon**;
  * cᵢ = flavourShift εᵢ, so u ↦ 0 and d ↦ −1 (`nucleonStateOfQuarks`);
  * the quark-to-slot order is not fixed, giving p ∈ perms of (0,0,−1) and n ∈ perms of (0,−1,−1), i.e. 3 × 3 pairs.
* **The census AVG pair rule** (`nuc11_interleaved`, the ruled Q_β element): p = (0, −½, −½), n = (−½, −½, −1), followed by the gluon σ₀².
  The docstring of `nucleonState` says the AVG c = −½ "is a pair AVERAGE and NOT a single letter".
* **The γγ rule** (bean `qou-ales`; `GammaGammaSelectorH3.lean`) fixes only the core (σ₀σ₁⁻¹)^k inside H₃. It does not fix the quark letters.
* So the planned family is {AVG, D2 × 9 orders} × {with gluon, without gluon} = **20 (p, n) state pairs**.
  The chirality idempotent is P₊(σ_g) with g ∈ {0, 1}, giving 40 settings.
  The state is ψ = N·P₊(σ_g) in H₃ (6-dim NF over ℚ(q)).
* The word must not change. The gluon σ₀² is census-picked and carries the bar obstruction (#7860).

**Candidates (step 2, enumerated in advance and drawn only from existing structure):**
* for g ∈ {0, 1}: σ_g, σ_g⁻¹, P₊,g, P₋,g, J_g, W_L = q⁻¹J_g and W_R = qJ_g (#7844);
* the centraliser of {core, gluon} in H₃: compute it, then test whether a **unique** element maps ψ_p to ψ_n. A forced element is a result; a choice from a family is not.

**Structural point to verify first.** At n = 3 the corner P₊(σ₀)H₃P₊(σ₀) should be **2-dim and
commutative**: rank 1 in each of the (3) and (2,1) blocks, 0 in (1³). If that holds, the
corner carries no τ_j / sl₂ at n = 3, and the Furey-type corner sl₂ (stream 11, #7867) needs
n ≥ 4, i.e. a word outside H₃. Measure this before relying on it. It is a candidate for a
small Lean lemma.

**Tests (step 3)** for each (state pair, idempotent, candidate):
* X·ψ_p = ψ_n exactly, and separately up to a scalar;
* X² = 1 or X² scalar;
* [X, core] = 0 and [X, gluon] = 0.

Report every hit and miss. Arithmetic is exact in ℚ(q): census `hm` right-multiplication and
mulNF via the basis words [], [0], [1], [1,0], [0,1], [0,1,0].

**Next step for whoever picks this up:** write
`computations/qbeta/qbeta_isospin_module_map_probe.py` to the plan above, starting with the
corner-dimension check.

## 11. RESULT: D-I1 = (A), isospin as a module map on H₃·P₊ (2026-11-15, thread "Test isospin as a module map")

Probe: [`computations/qbeta/qbeta_isospin_module_map_probe.py`](../../computations/qbeta/qbeta_isospin_module_map_probe.py),
**11/11 checks PASS**, exact over ℚ(q) (sympy `DomainMatrix` over `QQ(q)`), every product
through the corpus table `hecke_core_symbolic.hm_sym`. No witness, no Q_β value, no word
changed. States and candidates are exactly the §10 lists, enumerated before any test.

**Verdict.** At n = 3, no module map on the chirality ideal that commutes with the core and the
gluon turns the proton state into the neutron state, except in 4 degenerate settings where the
two states are already the same up to the number q⁻². No candidate from the fixed list does
it at all. This is an H₃ result; the Furey-type question moves to n ≥ 4.

**0. Structure (measured, then explained).**
* P₊(σ_g) H₃ P₊(σ_g) is **2-dimensional and commutative** for g = 0, 1 (the §10 hypothesis holds).
  Reason (Wedderburn, generic q): H₃ ≅ ℚ(q) ⊕ M₂(ℚ(q)) ⊕ ℚ(q) over the blocks (3), (2,1), (1³);
  P₊ is 1 on (3), rank 1 on (2,1), 0 on (1³). So the corner is ℚ(q) ⊕ ℚ(q), and there is
  **no τ_j / sl₂ in the corner at n = 3**. Scope (b), invariant = the block decomposition.
* The left ideal H₃·P₊ is **3-dimensional**: the (3) line plus one column V ≅ ℚ(q)² of the (2,1) block.
* The centre of H₃ is 3-dimensional, and **the centraliser of {core, gluon} equals the centre**
  (dim 3). Alone, each of core and gluon has a 4-dim centraliser; together they generate all of M₂
  on the (2,1) block. So any operator commuting with both acts on H₃·P₊ by one scalar on the (3)
  line and one scalar on V. It cannot rotate inside V. Scope (b) for "commutes with core and gluon".

**1–3. State family × idempotent × candidate = 20 × 2 × 14 = 560 settings.**

| test | result |
|---|---|
| X ψ_p = ψ_n exactly, X in the fixed list | **0 of 560** |
| X ψ_p ∥ ψ_n (up to a scalar) | **0 of 560** |
| X² scalar (J, W_L, W_R) | 6 of 14 candidates; none commutes with the core |
| [X, core] = 0 | **0 of 14** |
| [X, gluon] = 0 | 7 of 14 (the σ₀ family: the gluon is σ₀²) |
| some x in the centraliser with x ψ_p = ψ_n | **4 of 40** settings; 36 none |
| some x anywhere in H₃ with x ψ_p = ψ_n | 40 of 40, always a 3-dim affine family (context: the ideal is cyclic, so this carries no information) |

**The 4 centraliser hits are degenerate.** They are the D2 orders p ∈ {(d,u,u), (u,d,u)},
n ∈ {(d,u,d), (u,d,d)}, no gluon, idempotent g = 1. In each, ψ_n = **q⁻² ψ_p** exactly, for
two reasons that are identities, not findings about isospin:
* the two σ₀ letters are u and d, and σ₀⁻¹σ₀ = σ₀σ₀⁻¹ = 1, so their order is invisible;
* the last letter is on σ₁, and P₊(σ₁) absorbs it as an eigenvalue: σ₁P₊ = qP₊, σ₁⁻¹P₊ = q⁻¹P₊.

So the p ↦ n "map" there is the number q⁻², not an operator. The chirality projector erases the
flavour of the letter next to it. This is the letter-level statement "flavour = orientation of
the letter" seen from the ideal, and it does not survive the census gluon (σ₀² between the tail and
P₊(σ₁)): all 20 gluon settings miss.

**What this does and does not say.**
* Scope (b): at n = 3, no isospin on H₃·P₊ commuting with core and gluon is more than a scalar. Invariant: the centraliser equals the centre (measured exactly), plus Wedderburn.
* Scope (a): the 14 fixed candidates do not work. A different state rule, or dropping the
  commutation requirement, is not excluded. Without the commutation requirement, existence is trivial and the operator is not fixed, which is the fitting this test was set up to avoid.
* Not touched: n ≥ 4. Stream 11's n = 4 corner sl₂ (#7867, not one-sided from n = 5, bias [3]_q : 1) is the only place a Furey-type su(2) can live. The Stream 11 thread is checking whether that corner's multiplicity space is flavour (σ₃ ↦ σ₃⁻¹); that result decides whether an H₄ version of this test is worth building.
* No Lean was written. The corner fact is Wedderburn at generic q and the rest are finite exact
  linear algebra; a Lean lemma "centraliser of {core, gluon} in H₃ is the centre" is a possible
  follow-up.

**Side note (not changed: the ask-first rule).** `hecke_core_symbolic.NF_BASIS` lists index 3 as
(0,1) and index 4 as (1,0), but the `hm_sym` table it ships with sends 1·σ₁·σ₀ to index 3 and
1·σ₀·σ₁ to index 4. Measured here: with the table's order the basis words reduce to unit vectors;
with `NF_BASIS` order they do not. Both have length 2, so trace weights (z² for both) are unaffected.
Only a reader taking the `NF_NAMES` labels L₊ / L₋ literally is affected.
