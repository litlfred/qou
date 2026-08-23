# L2 closure — attack options, and the non-EM terms we are missing

**Date:** 2026-08-07 · **Branch:** `claude/1ppq-l2-closure-attacks-ufrfun`
**Tier:** analysis / coordination. **No fit, no AME inversion, nothing wired to production.**

Answers the owner's question: *what are the attack options to close L2; how can the
Standard Model / eightfold way give new hints at getting binding correct; are we
missing the non-EM terms?*

Owner constraints governing every option below:

> **"where/why would you add? what gaps will that close?"**
> **"no fitting. only derivable from QOU axioms."**

So each option states its **insertion point in the canonical derivation chain**, the
**axiom/driver it comes from**, and the **gap it closes**. Nuclear data (SEMF, IMME,
hypernuclei, Tjon, Nolen–Schiffer) appears **only as a falsification target**, never
as an input. Any option whose only justification is "it fits" is marked dead on
arrival.

---

## 0. TL;DR

1. **Yes — the missing terms are the non-EM ones, and that is now a structural
   statement, not an intuition.** The proved pairwise cap `ρ_A ≤ C(A,2) = A(A−1)/2`
   is *exactly* the Coulomb combinatorics `Z(Z−1)/2`. The framework has derived the
   **2-body / EM-like sector to its proved ceiling** and is missing precisely the
   terms that are not 2-body: volume (extensive), symmetry (isospin Casimir),
   pairing (parity). §2.
2. **The answer to "where would you add" is: nowhere — stop discarding.** The Markov
   trace is *normalized* to make it an isotopy invariant. That normalization is
   exponential in strand count, so its logarithm is **linear in A** — an extensive
   term. Knot invariants are *designed* to be intensive; the framework inherited a
   normalization built for topology and is using it for physics. The extensive term
   the corpus has been hunting is the factor we divide out. §3, **A1**.
3. **The eightfold way's concrete gift to binding is the Ocneanu parameter
   `a = q^{N−1}`.** The T3f audit (2026-08-04, three days old) rules it **GENUINELY
   OPEN** — binding runs on the Jones specialization `N = 2`, while the eightfold-way
   chapter independently wants `N = 3`. This is not a new knob; it is an *existing
   undetermined* one, and it is the same parameter that sets the normalization in (2).
   §4, **A2**.
4. **A coincidence that deserves exactly one careful probe, flagged with its own
   tension:** the `N = 2 → N = 3` change multiplies the extensive normalization
   exponent by `ln[3]_q / ln[2]_q ≈ 1.5871`, and the missing A=3 magnitude is
   `r* ≈ 1.5852` (0.12 %). **But the q-correction moves the wrong way** — classical
   `log₂3 = 1.58496` matches `r*` *better* (0.015 %) than the q-deformed ratio does.
   Read §4.3 before getting excited; this is suggestive, **not** a closure.
5. **Genuinely new levers with zero corpus footprint:** hypernuclei (0 hits),
   chiral-EFT power counting (0), seniority (0), IMME (0 in `docs/`). Tjon,
   Nolen–Schiffer and mirror nuclei are **already** in the corpus — those are
   re-aiming targets, not new directions. §6.

---

## 1. Where the L2 misses actually live

From `computations/per-observable-100x-status.witness.json` (2/7 met):

| obs | err (ppb) | target (ppb) | miss | class |
|---|---:|---:|---:|---|
| `m_p` | 1.351 | 0.003091 | **437×** | pin round-trip (de-fitted 2026-07-04) |
| `m_μ` | 209.8 | 0.2177 | **963.6×** | μ–p substrate tension |
| `m_n` | 2.389 | 0.005747 | **415.7×** | Path C — no flavor split |
| `Q_β` | 1248 | 7.797 | **160.1×** | Q_β chain |
| `Δ_pn` | 755.6 | 4.739 | **159.4×** | Path C — no flavor split |

Three **independent** classes, not one:

- **Class I — μ–p tension** (`m_μ`). A single ~11.5 ppb structural residual between
  the muon anchor `Vol(4₁)/ℏ_q²` and the Borromean `F_Bor`. Not a binding problem;
  §7.
- **Class II — pin round-trip** (`m_p`). §7.
- **Class III — no flavor split** (`m_n`, `Δ_pn`, and through the chain `Q_β`). The
  gating witness literally says *"Path C: no flavor-split."* **This is a p/n isospin
  problem — i.e. a non-EM term** — and it is the class the eightfold way is
  positioned to attack. §5.

Per-isotope binding (the `Δ_λ` magnitude wall, `r* ≈ 1.585`) is Subgoal-1 and sits
underneath Class III: a derived isospin splitting would serve both.

> 🛑 **CORRECTION (ROAST §R0.2, bean `qou-40r8`).** An earlier draft of this section
> claimed non-EM attacks hit Class III *and* Subgoal-1 binding. **That is wrong — a
> scale conflation.** Closing `Δ_pn` at L2 requires the categorical p/n split (a
> 1.29 MeV quantity) to **0.0061 eV**; nuclear symmetry energy is a ~20 MeV/nucleon
> effect — **≈9.1 orders of magnitude apart**. A binding fix accurate to 1 % is
> still ~10⁹ too coarse to move Class III. Class III's "no flavor-split" and nuclear
> isospin share the word "isospin" and nothing else.
>
> **Correct position: every option A1–A7 below serves Subgoal-1 binding only. None
> of them closes an L2 dashboard miss.** "Close L2" and "get binding correct" are
> two different programs; this memo answers the second.

---

## 2. The term-accounting argument — why "non-EM" is now structural

Two proved results bracket the missing object:

- **Intensive/extensive** (`2026-06-02-binding-intensive-vs-extensive-derivation.md`):
  the trace binding saturates; *no per-block weight `Δ_λ` converts an intensive
  quantity into an extensive one*.
- **Pairwise cap** (`2026-07-18-deltalambda-saturation-det-ceiling.md`): the
  isospin-even log-det cumulant obeys `ρ_A ≤ C(A,2) = A(A−1)/2` for all `m`; strong
  targets exceed it ⇒ the missing term is irreducibly **≥3-body**.

Now line the five Bethe–Weizsäcker terms up against body-order and algebraic character:

| BW term | scaling | body-order / algebraic character | QOU status |
|---|---|---|---|
| Volume `+a_V·A` | `A` | 1-body additive; needs an **unnormalized** trace | **missing** — the extensive object |
| Surface `−a_S·A^{2/3}` | `A^{2/3}` | boundary / genus of the closure | missing |
| Coulomb `−a_C·Z(Z−1)/A^{1/3}` | `C(Z,2)` | **2-body** | **derived, at its proved ceiling** |
| Symmetry `−a_A·(N−Z)²/A` | `T₃²` | **isospin Casimir** (rank-2 isotensor) | half-built (Wigner SU(4) gate) |
| Pairing `±a_P·A^{−1/2}` | parity(N), parity(Z) | **ℤ/2 valuation parity** | possibly *already proved* (Δ_λ sign) |

The cap `C(A,2)` and the Coulomb combinatorics `Z(Z−1)/2` are the same object. The
framework built the 2-body sector, proved its ceiling, and the ceiling is the EM
term. **The owner's read is correct.**

### 2.1 A corpus stance that should be amended

`observations/bw-mass-decomposition-dictionary.md` declines term-mapping as
*"a numerological exercise."*

That is **right about coefficients and wrong about exponents.** Fitting `a_V ≈ 15.6`
is numerology. Reading the **A-scaling exponent of the residual** is not a fit — it
is a *measurement of the tensor body-order* of the missing operator, and it is
exactly the diagnostic the `C(A,2)` cap proof already used successfully. The block
should be amended to permit exponent-fingerprinting while keeping the ban on
coefficient-fitting. (Recommendation only; not done in this doc.)

---

## 3. The normalization-discard argument

**Where:** the `𝐇_n(q) → tr_M = Σ_λ y_λ χ_λ` step of the canonical chain — *before*
normalization, not after.

**Why.** The Ocneanu/Markov trace becomes a **link invariant** only after multiplying
by a factor of the form `N(q)^{\,n−1}` (the Jones/HOMFLY stabilization factor fixed by
the Markov moves). Then

```
log( unnormalized ) − log( normalized )  =  (n − 1) · log N(q)
```

— **linear in the strand count `n`**, i.e. **extensive**. Isotopy-invariance is
precisely the property that kills extensivity: a knot invariant must not care how
many strands you wrote the braid on, so the normalization is *designed* to cancel the
`∝ n` piece. The framework inherited a normalization engineered for topology and is
using it for physics, where the `∝ A` piece is the volume term — the single largest
contribution to nuclear binding.

**Gap closed.** The additive, non-normalized, extensive term that both proved
constraints (intensive/extensive, pairwise-cap) say is missing. This is the object
the option-e ledger lists as the surviving candidate *"non-normalized extensive
generating kernel."*

**Axiom source.** The Markov moves + the Ocneanu parameter `z` — both part of the
Hecke data already in `HnMarkovTrace.lean`. **Nothing is added and nothing is fitted:**
the claim is that a factor already present in the pipeline is being divided out, and
that its logarithm is the extensive term. Whether the resulting coefficient matches
`a_V` is then a *prediction*, free to fail.

> **Structure formalized (2026-08-22).** The extensivity itself — the part that is
> purely algebraic and independent of the magnitude — is now Lean-proved sorry-free
> in `QOU/Mass/MarkovStabFactorExtensive.lean`: the stabilisation factor
> `markovStabFactor Nq n = N(q)^{n-1}` accrues one constant factor of `N(q)` per
> strand (`markovStabFactor_succ`), the merge law
> `stab(m)·stab(n)·N(q) = stab(m+n)` (`markovStabFactor_merge`), and it is
> extensive-not-intensive for `N(q) ≠ 1` (`markovStabFactor_not_intensive`;
> exponent affine with unit slope). The **`A`-constituent** form is proved too
> (`markovStabFactor_merge_parts`): merging `A` parts gives
> `stab(Σ nᵢ) = (∏ stab nᵢ)·N(q)^{A-1}`, so the normalisation that does **not**
> cancel in a binding difference is exactly `N(q)^{A-1}` — extensive in the
> constituent count `A`, the precise `∝ A` volume-term shape. This proves *only*
> that the discarded normalisation is extensive — the coefficient/`a_V` question
> (is `(A-1)·log N(q) = a_V·(A-1)`?) and the strand↔`A` identification are
> deliberately left as the open prediction below.

**Honest caveat.** `E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV` and `log[2]_q ≈ 0.6945`, so the
naive `N = 2` reading gives `≈ 2.91 MeV` per strand against `a_V ≈ 15.6 MeV` —
**5.4× short.** So the *structure* is right and the *magnitude* is not, in the Jones
specialization. Which leads directly to §4.

---

## 4. The eightfold way's actual entry point: the Ocneanu parameter

### 4.1 The parameter is open, and it is the same parameter

`docs/audits/2026-08-04-ocneanu-trace-parameter-audit.md` (T3f, three days old):

> The Ocneanu trace on `H_•(q)` carries a **free parameter** `s` (equivalently
> `a = q^{N−1}`) that selects the gauge group rank `N`. QOU's mass/binding pipeline
> uses the **Jones specialization** (`N = 2`). This specialization is **not forced**
> by the Descartes condition. **Status: GENUINELY OPEN.**

and

> `a = q` → Jones (`gl₂`) · `a = q²` → `gl₃` invariant (**eightfold way!**)

`HnMarkovTrace.lean` confirms `z` is a **class field**, not a `def` computed from `q`
— constrained only by `z_pos`.

This is the answer to *"how can the eightfold way give hints at binding."* Not by
adding flavor structure on top of binding, but because **`N` is the same parameter
that sets the extensive normalization in §3**, it is **currently undetermined**, and
the flavor chapter independently argues for `N = 3` while binding silently runs on
`N = 2`.

### 4.2 Why this is not a fit

`N = 3` is **not tuned to binding.** It is argued for independently in the
eightfold-way chapter (`a2-from-three-strands`, `color-su3-from-g2`, GMO). Testing
whether the binding pipeline should use the same `N` as the flavor sector is a
**consistency requirement between two parts of the framework**, which is the
opposite of a fit: it has exactly one admissible answer and the data does not get a
vote.

### 4.3 The coincidence — and why to distrust it

Changing `N = 2 → N = 3` scales the extensive exponent of §3 by `ln[3]_q / ln[2]_q`:

| convention | `ln[3]_q / ln[2]_q` at `q₀` | vs `r* = 1.5852` |
|---|---:|---:|
| symmetric `[2]_q = q^{1/2}+q^{−1/2}`, `[3]_q = q+1+q^{−1}` | 1.5870788 | **0.12 %** |
| unsymmetrized `[n]_q = (qⁿ−1)/(q−1)` | 1.6159296 | **2.0 %** |
| classical `log₂3` (q→1) | 1.5849625 | 0.015 % |

**Four reasons to distrust it, stated up front:**

0. **The convention was shopped.** Both rows above were computed; an earlier draft
   of this memo reported only the flattering one. The agreement is a **function of
   an arbitrary convention choice** and therefore currently means nothing. The
   normalization factor must be *derived from the Markov moves first* and evaluated
   as it comes out — never selected afterwards. See the ROAST companion §R0.1.

1. **The q-correction moves the wrong way.** Classical `log₂3` (1.58496) is
   *0.015 %* from `r*` — **8× closer** than the q-deformed ratio. If the mechanism
   were genuinely the q-deformed normalization ratio, the q-deformed value should fit
   *better*, not worse. This is the single strongest argument that the agreement is
   accidental.
2. **The corpus already dismissed `r* ≈ log₂3` as numerology** (option-e.md:782,
   Lean `two_pow_ne_three_pow`).
3. **Scratch arithmetic only** — float64, and the repo's NO-FLOAT64 rule means no
   number above may enter a witness. Any real probe runs at ≥65 dps.

**But note the dismissal is scope-limited.** `two_pow_ne_three_pow` ("`2^a` even
≠ `3^b` odd") proves `r*` is not realized as a **ratio of integer Vassiliev weights**.
It says nothing about `log₂3` arising as a **ratio of logarithms of normalization
factors**, which is a different mechanism entirely. Per AGENTS.md §"Before declaring
refuted", that existing refutation is scope-(a) with respect to this route and does
**not** exclude it. Re-scoping the ledger row is warranted regardless of how the
probe turns out.

---

## 5. The non-EM terms, one by one — insertion point, axiom source, gap closed

### A1 — Volume term ← unnormalized Ocneanu trace  *(highest value; §3)*
- **Where:** Hecke → trace step, before the Markov normalization.
- **Axiom source:** Markov moves + Ocneanu `z` (already in `HnMarkovTrace.lean`).
- **Gap closed:** the additive extensive term; the `∝A` growth the trace binding
  cannot produce (1.65× vs 12.72× needed).
- **Falsifies if:** `E₀ · log N(q₀)` misses `a_V` at the chosen `N` and no `N`
  consistent with the flavor sector fixes it.

### A2 — Ocneanu `N` consistency with the flavor sector  *(§4)*
- **Where:** the trace parameter `a = q^{N−1}`.
- **Axiom source:** T3f open question + the eightfold-way chapter's independent
  `N = 3`. Determined by *internal consistency*, not by data.
- **Gap closed:** simultaneously the extensive magnitude (A1) and the flavor/binding
  coherence; potentially `r*`.
- **Falsifies if:** the Descartes condition forces `N = 2` in the mass pipeline (the
  T3f audit's §3a branch) — in which case A1 must find its magnitude elsewhere.

### A3 — Symmetry energy ← isospin/SU(4) Casimir on the Wedderburn partition
- **Where:** the Wedderburn decomposition step (`λ ⊢ n`).
- **Axiom source:** the SU(4) Casimir is a **known polynomial in the partition**
  (`C₂ = Σλᵢ(λᵢ+n+1−2i)`), and `Δ_λ = (−1)^{n(λ)}·dim V_λ` is **proved sorry-free**.
- 🛑 **Blocked — check first (ROAST §R1/A3):** the Descartes condition forces
  `dim V = 2`, so Schur–Weyl on `V^{⊗n}` gives the **`GL(2)`** commutant, *not*
  `GL(4)`. Whether `λ ⊢ n` can carry spin-isospin content **at all** is an open
  structural question. Resolve before any work.
- **Gap closed:** the `(N−Z)²` asymmetry *numerator* only. ⚠️ **Correction:** an
  earlier draft claimed the Casimir supplies the `(N−Z)²/A` shape and closes
  Class III. Both are wrong. The `1/A` is Fermi-gas level density, a separate
  dynamical input; and closing `Δ_pn` at L2 needs **6 meV** precision on a 1.29 MeV
  split, ~9.1 orders below the nuclear scale — **no binding attack touches the L2
  dashboard.** Binding is Subgoal-1 only. See ROAST §R0.2, bean `qou-40r8`.
- **Existing footing:** `SU4SupermultipletGate.lean` proves the `[1⁴]` trace is
  `C(4,A)`, zero for `A>4` (⁴He locality). The corpus stopped at locality and never
  took the Casimir eigenvalue.
- **Falsifies if:** the Casimir's leading term does not reproduce the `(N−Z)²/A`
  shape (shape first — coefficient is a *prediction*, never a fit).

### A4 — Pairing term ← the already-proved Δ_λ chirality sign  *(cheapest)*
- **Where:** nowhere — it may already be proved.
- **Axiom source:** the proved sign `(−1)^{n(λ)}`, `n(λ) = Σ(i−1)λᵢ` — a **ℤ/2
  valuation parity**. The BW pairing term is *also* a pure parity object
  (even-even `+`, odd-odd `−`, odd-A `0`).
- **Gap closed:** even-odd staggering; the one BW term the framework may already own
  and not have noticed.
- **Test:** does `n(λ)` parity track `(−1)^N + (−1)^Z` under the atomic-braid
  partition assignment? **One afternoon, pure bookkeeping, no new math.**
- **Falsifies if:** the parities decorrelate on the light isotopes. A clean negative
  is still worth having.

### A5 — IMME rank-≤2 as a body-order meter  *(prunes before searching)*
- **Where:** a constraint on the missing operator, applied *before* any search.
- **Why:** the isobaric multiplet mass equation `M(T₃) = a + b·T₃ + c·T₃²` is
  quadratic **because a two-body charge-dependent interaction carries isospin tensors
  of rank ≤ 2 only**; a genuine 3-body force generates rank 3, i.e. a `d·T₃³` term.
  Measured `d` is ≲ keV — `d/a ~ 10⁻⁷`.
- **Gap closed:** none directly — it **narrows the search**, which is the
  formalize-first discipline. The missing extensive term is a ~58 % effect (`r*`) yet
  must be **isoscalar to ~10⁻⁷**. That kills every candidate 3-body operator built
  on p/n asymmetry — in particular it says the derived color-tube weight `W_{c₁c₂}`
  (which fixes the p/n sign) **cannot** be the extensive magnitude, independently
  confirming what the option-e ledger concluded by another route.
- **Scope:** empirical ⇒ scope-(a) constraint, strong but not a proof. Label
  accordingly.
- **Corpus footprint:** IMME appears **nowhere** in `docs/`. Genuinely new.

### A6 — Hypernuclei: the eightfold way's parameter-free binding test
- **Where:** the color-tube weight `W_{c₁c₂}` (derived, 8→0 free params, 2026-08-01).
- **Why:** a Λ-hypernucleus is the *same nuclear geometry with one strand's flavor
  changed*. Under a derived flavor-dependent weight this is a **pure representation
  change with no new parameters**. The textbook result — the Λ well depth is ≈ 2/3
  of the nucleon's, from simple light-quark counting (Λ has 2 non-strange quarks
  vs the nucleon's 3) — is exactly a **strand-counting** statement, which is the
  natural language of the Borromean 3-strand picture.
- **Gap closed:** validates or refutes the derived flavor weight against an
  **entirely independent data set that never touched `q₀`**. If QOU reproduces 2/3
  from strand counting, that is a genuine parameter-free prediction in the flavor
  sector.
- **Corpus footprint: 0 hits.** The single most under-exploited eightfold-way lever.

### A7 — Chiral-EFT power counting as a magnitude budget
- **Where:** a sanity bound on the missing 3-body term, not an ingredient.
- **Why:** chiral EFT places 3N forces at N²LO with a known suppression; the Tjon
  line (a model-independent `B(³H)`–`B(⁴He)` correlation) says where any 2N-only
  theory must land, and how far the 3N force must move it.
- **Gap closed:** tells us whether `r* ≈ 1.585` is *the size a genuine 3-body term
  should be* or is anomalously large — i.e. whether we are hunting a 3-body force or
  a missing normalization (A1). **These two attacks are mutually diagnostic**: if the
  deficit is normalization, it is `∝A` and Tjon-line placement will show it.
- **Corpus footprint:** chiral EFT 0 hits; "Tjon" appears once, undeveloped
  (`2026-07-11-jones-nuclear-quotient-infra.md`), with no "Tjon line" analysis.

### A8 — Mirror nuclei / Nolen–Schiffer  *(re-aim, not new)*
- Already in the corpus (Nolen 13 files, mirror nuclei 25). Re-aimed: mirror pairs
  isolate the p/n-asymmetric sector with the extensive part **cancelling**, making
  them the cleanest test of the derived `W_{c₁c₂}` — and the ~7 % Nolen–Schiffer
  anomaly is a standing unexplained discrepancy in mainstream nuclear physics that a
  correct categorical charge-symmetry-breaking term would address.

---

## 6. Dead on arrival (stated so nobody re-pitches them)

- **Any seventh `Δ_λ` magnitude ansatz.** Banned by AGENTS.md and structurally
  hopeless: no per-block weight converts intensive → extensive (proved).
- **Fitting any BW coefficient.** Explicitly excluded by the owner's constraint.
- **Charm / heavy flavor for the extensive term.** A category error
  (`2026-08-02` audit §4). The higher-representation instinct is right; the correct
  object is nuclear spin-isospin SU(4), not quark flavor.
- **Sign-only re-derivations.** ℓ¹-ceiling prune: `‖c‖₁/|target| < 1` for all four
  light isotopes ⇒ no sign reassignment closes the deficit.

---

## 7. Classes I and II (not binding — listed for completeness)

`m_μ` (963.6×) and `m_p` (437×) are **not** non-EM-term problems and should not be
bundled into this arc. `m_μ` is the μ–p substrate tension (one ~11.5 ppb residual
between `Vol(4₁)/ℏ_q²` and `F_Bor`); `m_p` is the post-de-fit pin round-trip. Note
that **A1/A2 touch the trace normalization that feeds `F_Bor`**, so a change there
would propagate into Class I — this must be checked as a *regression risk*, not
claimed as a bonus. Note also the standing gate: **substrate-`q₀` derivation is
permanently forbidden** (owner ruling 2026-08-02, bean `qou-eic1`); no option above
routes through it.

---

## 8. Recommended order

| # | Attack | Cost | Payoff | Type |
|---|---|---|---|---|
| 1 | **A4** pairing = proved Δ_λ sign | hours | may already own a BW term | bookkeeping |
| 2 | **A5** IMME rank-≤2 prune | ~1 day | narrows before searching | formalize-first |
| 3 | **A1+A2** unnormalized trace + Ocneanu `N` | days | the extensive term; possibly `r*` | structural |
| 4 | **A3** isospin Casimir | ~week | Class III (3 of 5 L2 misses) | structural |
| 5 | **A6** hypernuclei | ~week | independent flavor test | validation |
| 6 | **A7/A8** Tjon / mirror | ~week | diagnostic placement | validation |

A4 and A5 are cheap and can run in parallel; both are pure pruning/bookkeeping and
neither can produce a fit. A1+A2 is the structurally deepest and should be attacked
with the §4.3 skepticism in hand: **the probe must be built to kill the coincidence,
not to confirm it.**
