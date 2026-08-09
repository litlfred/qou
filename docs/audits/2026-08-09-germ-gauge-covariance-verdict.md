# `Ω₂` is NOT gauge-covariant: the germ is a connection, and the covariant order-2 object is zero

**Date:** 2026-08-09
**Bean:** `qou-prjo` (deuteron `Δ_λ` magnitude) — stays **OPEN**
**Branch:** `claude/germ-gauge-covariance-2026-08-09` · **PR** [#4856](https://github.com/litlfred/qou/pull/4856)
**Predecessors:** [#4850](https://github.com/litlfred/qou/pull/4850) (orbit symmetry forced but
vacuous), [#4849](https://github.com/litlfred/qou/pull/4849) (multi-generator super-pairwise;
the §2.3 red-team note this audit runs), [#4848](https://github.com/litlfred/qou/pull/4848)
(single-generator scope-(b)), [#4818](https://github.com/litlfred/qou/pull/4818),
[#4798](https://github.com/litlfred/qou/pull/4798), [#4619](https://github.com/litlfred/qou/pull/4619).

---

## 0. The verdict, in four lines

1. **`Ω₂` is NOT gauge-covariant.** The germ `δq = q(∂_qρ)ρ⁻¹` is a **1-cocycle**, not a
   tensor; the curvature `F_q = ⟦δq_i, δq_j⟧` picks up a surviving inhomogeneous defect
   `Δ ≠ 0` (exhibited exactly below), and `Ω₂` inherits it exactly.
2. **So the observer-pair question is VOID, not open.** #4849 asked which of the `n−2`
   admissible adjacent germ observer pairs is right, given a `16.4×` spread. There is
   nothing to choose *between*: `Ω₂` has **no** basis-independent value, and `‖Ω₂‖` is not
   even invariant for a genuine tensor (the basis change is not unitary).
3. **A covariant object does exist, and it is zero.** The gauge-invariant content of the
   germ is its class `[α] ∈ H¹(B_n; 𝔤𝔩_{Ad ρ})`. The canonical second-order object built
   from it — the bracket **cup square** `[α]∪[α] ∈ H²` — is **identically a coboundary**,
   with the explicit primitive `β = q∂_q α`. The surviving invariant *linear* functional is
   `τ(α(w)) = q∂_q log det ρ(w)`: pure writhe/framing, the datum already walled by
   `no_writhe_only_framing`.
4. **Retro-narrowing of #4848.** Its `Ω₂ = 0` on `σ₁³` is itself **gauge-dependent** —
   correct within a `q`-*independent* change of basis, false under the full connection
   freedom. Its algebra is right; its "gauge-independent" quantification (every `J`, every
   handle exponent) simply did not range over `q`-dependent regaugings.

**Scope:** **(b)** for item 1 (a proved algebraic obstruction, invariant cited);
**(b)** for the cup-square vanishing (an exact identity, primitive exhibited);
**(a)** for "no *other* nonzero covariant functional exists" — not attempted, stays open.
`free_parameters = 0`; no AME quantity, no `g₂`, no binding number appears anywhere in the
compute. Bean **OPEN**.

---

## 1. Phase 0 — corpus grep (mandatory)

Per AGENTS.md §"Before declaring open math". Searched `content/`, `computations/`,
`docs/audits/`, `docs/coordination/` for germ gauge/basis conventions, connection
transformation laws, cocycle/coboundary/`H¹` treatments of the `q`-deformation, and
intertwiner conventions between Hoefsmit seminormal and reduced Burau.

**Result: the corpus records the *observation* but has never run it.** #4849 §2.3 states the
transformation law and explicitly declines to draw the consequence
(*"Recorded here so a later agent does not read a germ-derived magnitude as canonical"*).
Nothing in `content/`, `computations/`, or the coordination ledgers treats the germ as a
cocycle, computes its class, or tests covariance of any germ-derived quantity. So the
question was genuinely open, and the answer below is new.

**Negative Phase-0 findings** (recorded so a later agent does not re-search): there is no
corpus block fixing the representation gauge of the germ; no intertwiner convention between
the Hoefsmit seminormal and reduced-Burau realizations; and no prior use of `H¹`/`H²` of the
braid group with adjoint coefficients anywhere in the tree.

---

## 2. The algebra (formalize-first — Lean was written before any sweep)

[`QOU/MassTheory/GermConnectionGaugeCovariance.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/GermConnectionGaugeCovariance.lean)
— **sorry-free**, generic non-commutative `Ring R`, `scripts/lean-verify.sh` **exit 0**,
`#print axioms` clean on **all 48** declarations (`propext` / `Classical.choice` /
`Quot.sound` only; no `sorryAx`, no `axiom`, no `native_decide`, no `: True`).

Everything is stated for a bare **derivation** `D` of a ring and **units** of that ring. The
substrate reading is `D = q∂_q`, `R` = the matrix algebra of a Hecke representation,
`u = ρ(σ_i)`, `b = B(q)` a `q`-dependent basis change — but no such reading is needed.

### 2.1 The germ is a 1-cocycle

`germ_mul`:  `α(uv) = α(u) + Ad(u) α(v)`, where `α(u) = (Du)u⁻¹`.

This is the whole story in one line. A **cocycle** is a section of an affine bundle, not a
vector: it is well-defined only modulo **coboundaries**, and §2.2 shows the gauge freedom is
exactly the coboundary.

### 2.2 The connection law

`germ_conj`:

$$
  \alpha(u) \;\longmapsto\; \mathrm{Ad}(b)\Bigl(\alpha(u) + \bigl(1 - \mathrm{Ad}(u)\bigr)\Theta\Bigr),
  \qquad \Theta \;=\; b^{-1}\,(D b).
$$

The shift `(1 − Ad u)Θ` is precisely `−(∂Θ)(u)`, the coboundary of the 0-cochain `Θ`. It
vanishes iff `Db = 0`, i.e. iff the basis change is `q`-independent. **The Hoefsmit
seminormal basis is `q`-dependent** (through `b = √(1 − 1/[ρ]²)`), and the reduced-Burau
basis is a *different* `q`-dependent gauge — so this freedom is live, not hypothetical.

### 2.3 The curvature is not a tensor

`germCurvature_conj`:  `F ↦ Ad(b)(F + Δ)` with

$$
  \Delta \;=\; \bigl\llbracket \alpha(u),\, X_v \bigr\rrbracket +
    \bigl\llbracket X_u,\, \alpha(v) \bigr\rrbracket +
    \bigl\llbracket X_u,\, X_v \bigr\rrbracket ,
  \qquad X_w = (1 - \mathrm{Ad}\,w)\Theta .
$$

`germCurvature_covariant_iff`: covariance holds **iff** `Δ = 0`. And `gaugeDefect_ne_zero`
exhibits a concrete ring / derivation / unit triple where it does not — `R = M₂(ℚ[X])`,
`D = d/dX` entrywise, `u = !![1,X;0,1]`, `v = !![1,0;X,1]`, `b = u`, giving

$$
  \Delta \;=\; \begin{pmatrix} X^2 & -2X \\ 0 & -X^2 \end{pmatrix} \;\neq\; 0 .
$$

### 2.4 The pairing inherits the failure *exactly* — none of it is the transport's fault

`listPairing_map_adAct`:  `Ω(map (Ad b) l) = Ad b (Ω l)`.

The transports `U_k` are ordered products of `ρ`'s, hence genuinely tensorial; the pairing
itself is covariant **given** covariant inputs. So every bit of the failure sits in `F_q`.
Combined with `transversePairing_covariant_iff`, this closes the chain from "the germ is a
connection" to "`Ω₂` has no invariant value".

### 2.5 The covariant second-order object — and its vanishing

The canonical object attached to a 1-cocycle at second order is not `⟦α(u), α(v)⟧` (which
is not even a cochain) but the **bracket cup square**

$$
  (\alpha \cup \alpha)(u,v) \;=\; \bigl\llbracket \alpha(u),\, \mathrm{Ad}(u)\,\alpha(v) \bigr\rrbracket ,
$$

which descends to cohomology classes. `cupSq_eq_neg_coboundary` proves

$$
  \alpha \cup \alpha \;=\; -\,\partial\beta, \qquad \beta \;=\; D \circ \alpha \;=\; q\,\partial_q\,\alpha .
$$

So `[α]∪[α] = 0` in `H²(B_n; 𝔤𝔩_{Ad ρ})` — **in every gauge, for every representation, with
an explicit primitive.** The single lemma that makes it work is `D_adAct`:
`D(Ad_u x) = Ad_u(Dx) + ⟦α(u), Ad_u x⟧`.

> **Why this had to happen.** `D` differentiates in **one** direction (`q`). A curvature is a
> 2-form and needs two independent base directions. `⟦δq_i, δq_j⟧` borrows the *generator
> indices* `i, j` as if they were directions — but they are **group elements**, not
> directions in the base. The commutator of a cocycle's values at two group elements is
> neither a tensor nor a cocycle; the object that *is* both is the cup square, and on a
> one-dimensional base it is exact. **The "transverse surface curvature" was never a
> curvature.**

### 2.6 What *is* gauge-invariant

`trace_germ_conj`: for any cyclic trace `τ`, `τ(α(b u b⁻¹)) = τ(α(u))` — the inhomogeneous
term is trace-annihilated. Substrate reading: `τ(δq(w)) = q∂_q log det ρ(w)`, which sees only
`det ρ`, i.e. the **abelianisation** of `B_n`, i.e. the **writhe / framing** — exactly the
datum already walled (`no_writhe_only_framing`, bean history). So the surviving invariant
linear functional carries no new information.

---

## 3. The measurement

[`computations/probes/nastokes_germ_gauge_covariance_probe.py`](../../computations/probes/nastokes_germ_gauge_covariance_probe.py)
→ `nastokes-germ-gauge-covariance.witness.json`. **15/15 assertions pass**, 4.4 s wall.

### 3.1 Part A — exact over `ℚ(q)`, the 2-dimensional Hecke rep of `H₃` (#4848's rep)

Certified first: braid, Hecke, and #4848's germs reproduced exactly
(`δq₁ = H − 2E`, `δq₂ = −H`, `F_q = −4E`).

Gauge `B(q) = diag(1, q)` — a legitimate `q`-dependent change of basis (conjugation preserves
braid + Hecke, so `BρB⁻¹` is the *same* abstract representation in a different frame),
`Θ = q B⁻¹∂_q B = diag(0,1)`.

| check | result |
|---|---|
| **A2** `germ(BρB⁻¹) = B(germ ρ + (1−Ad ρ)Θ)B⁻¹` — both sides computed independently | **True**, both generators |
| shift at `σ₁` | `X₁ = −E` |
| shift at `σ₂` | `X₂ = q²F` |
| **A3** `Δ = ⟦α₁,X₂⟧ + ⟦X₁,α₂⟧ + ⟦X₁,X₂⟧` | `!![−3q², −2; −2q², 3q²] = −3q²H − 2E − 2q²F` |
| `F' = B(F + Δ)B⁻¹` | **True** |
| `Δ ≠ 0` ⇒ `F_q` is not a tensor | **True** |
| **A5** `(α∪α)(u,v) = −(∂β)(u,v)`, `β = q∂_qα`, all **25** word pairs | **True**, exactly |
| **A6** `τ(α(w))` gauge-invariant and `= q∂_q log det ρ(w)` | **True**, all words |

### 3.2 A4 — the retro-check on #4848

`F_q = −4E` is an `Ad(ρ(σ₁))`-eigenvector **in the base gauge** (verified), which is why
#4848's `Ω₂` on `σ₁³` vanishes for every `J` and every handle exponent. In the gauge
`B = diag(1,q)`:

| | base gauge | gauge `diag(1,q)` |
|---|---|---|
| `F` is an `Ad(σ₁)`-eigenvector? | **yes** | **no** |
| `Ω₂` on `σ₁³` | `0` (#4848 reproduced) | `!![24q⁴ − 20q² − 16 + 12q⁻², …; q⁵(24q⁴ − 16q² − 8), …] ≠ 0` |

So **#4848's zero is gauge-dependent.** This is a *narrowing*, not a refutation: #4848's
algebra is correct and its stated quantification (every intersection form, every handle
exponent) is honoured. What it did not range over is a `q`-**dependent** change of
representation basis — the very freedom #4849 §2.3 later identified. Correspondingly,
#4849 §2.3's parenthetical *"the answer there was `0` in every gauge, which is exactly why
the gauge did not have to be fixed"* is **too strong** and should be read as "`0` in every
gauge #4848 quantified over".

### 3.3 Part B — the real `⁴He` atom word, two genuinely different gauges

Word: the corpus `atom_braid_word_3A(2,2)` — 12 strands, 47 letters, generators `σ₀…σ₁₀`.
`q₀` = **experimental proton anchor**, `1.1099785827513808`.

**B1 — gauge (a): `B(q) = diag(1, q, …, q^{d−1})` on the Hoefsmit seminormal basis.** `B` is
known explicitly, so the covariance defect is measured **directly**: covariance means
`Ad(B)⁻¹Ω₂′ = Ω₂`.

| `λ` | germ pair | `‖Ω₂‖` | `‖Ω₂′‖` | **covariance defect** `‖Ad(B)⁻¹Ω₂′ − Ω₂‖/‖Ω₂‖` |
|---|---|---|---|---|
| `(11,1)` | `(0,1)` | 4.948e3 | 1.163e3 | **0.781** |
| `(11,1)` | `(3,4)` | 2.342e3 | 3.021e3 | **1.254** |
| `(10,1,1)` | `(0,1)` | 1.485e4 | 1.199e6 | **13.378** |
| `(10,1,1)` | `(3,4)` | 7.025e3 | 6.901e5 | **14.427** |

`0` would mean covariant. The observed defect is `O(1)`–`O(10)`. The Lean connection law is
reproduced numerically to `≤ 4.9e-15` relative on every germ, and every representation
(base and gauged) is certified on braid + Hecke + far-commutation to `≤ 3.7e-15`.

**B2 — gauge (b): the reduced-Burau realization, i.e. the #4798/#4848 gauge.** Reduced Burau
at `t = q^{-2}` scaled by `q` has eigenvalues `q` (mult `n−2`) and `−q⁻¹` (mult 1), so it is
the **same** `λ = (n−1,1)` representation of `H_n(q)` in a different, `q`-dependent basis.
Certified by **character equality** on 40 random words: worst relative difference `1.7e-15`.

The comparison uses only **conjugation-invariant** readouts `tr(Ω₂^k)`, so it needs no
intertwiner and is readout-independent: *conjugate operators have equal trace powers, full
stop.*

| germ pair | readout | seminormal | reduced Burau | rel diff |
|---|---|---|---|---|
| `(0,1)` | `tr Ω₂` | `+3.4e-13` | `+1.2e-12` | — (both `0`) |
| | `tr Ω₂²` | `+3.555e6` | `+4.395e7` | **11.4×** |
| | `tr Ω₂³` | `−1.296e9` | `−9.320e9` | **6.2×** |
| | `tr Ω₂⁴` | `+6.567e12` | `+9.687e14` | **146×** |
| `(3,4)` | `tr Ω₂²` | `−1.212e6` | `+6.333e5` | **sign flip** |
| | `tr Ω₂³` | `+8.779e8` | `+2.316e8` | 0.74 |
| | `tr Ω₂⁴` | `−3.671e11` | `+2.085e11` | **sign flip** |

`tr Ω₂²` changes **sign** between two bases of the same representation. That is not a
precision artefact and not a choice of norm — it is a basis-independent scalar of a
conjugacy class disagreeing across two realizations of one representation, which is possible
only if the operator is not a tensor.

**Trace control:** `|tr Ω₂| / ‖Ω₂‖ = 9.1e-17` — the arithmetic reproduces
`listPairing_trace_zero` (#4818, #4619) to machine epsilon, exactly as that theorem requires.

---

## 4. Scope classification

Per AGENTS.md §"Before declaring refuted / ruled out / dead end".

- **(b) STRUCTURAL EXCLUSION — `Ω₂` (equivalently `F_q`) has no basis-independent value.**
  **Cited invariant:** the germ is the right logarithmic derivative of a `q`-family, hence a
  **1-cocycle**, defined only modulo the coboundary `(1 − Ad u)Θ`
  (`germ_mul`, `germ_conj`, sorry-free); the induced defect on `⟦δq_i, δq_j⟧` is nonzero
  (`gaugeDefect_ne_zero`, plus the exact `ℚ(q)` computation in §3.1); the pairing is
  covariant *given* covariant inputs (`listPairing_map_adAct`), so the failure transfers
  unchanged; and the conjugation-invariant `tr(Ω₂^k)` demonstrably differ between two
  realizations of the *same* representation (§3.3). This is a proved algebraic obstruction
  plus a readout-independent measurement, not a failed numerical search — which is what
  licenses (b) rather than (a).
- **(b) — the canonical covariant second-order object is identically zero.** `α∪α = −∂β`
  with the explicit primitive `β = q∂_qα` (`cupSq_eq_neg_coboundary`, plus 25/25 exact
  symbolic pairs). An exhibited primitive is a proof, not a probe.
- **(a) — "no *other* nonzero gauge-invariant functional of the germ exists".** **Not
  claimed.** §2.6 exhibits one (the abelian `τ(α(w)) = q∂_q log det ρ(w)`, already walled).
  A full classification of gauge-invariant functionals of `[α] ∈ H¹` is not attempted and
  stays open.
- **(a) retro-narrowing of #4848**, not a refutation — see §3.2.

**What is NOT shown:**

- Not that the `Δ_λ` **value** is wrong. It is proved
  (`dtEuler_eq_deltaLambda_unconditional`) and untouched here.
- Not that #4849's super-pairwise *measurement* is wrong. It stands as a measurement; what
  this audit removes is the possibility of reading a **number** off the object.
- Not a `Δ_λ`, not a binding energy, not a wiring. **`sorry-free ≠ derived`**: nothing here
  enters production, and the bean's `≥3`-body magnitude gate is untouched.

---

## 5. What this does to the transverse NA-Stokes route

| object on the atom words | status |
|---|---|
| **Longitudinal** inter-crossing Magnus tower on a single-generator word | `= 0` identically (#4848 predecessor, `eunit_magnus_order2_probe` N2) |
| Scalar-trace visibility of any pairing | `tr⟦A,B⟧ = 0` — `listPairing_trace_zero` (#4818, #4619) |
| Diagonal / Betti-count reading | exactly linear in link count ⇒ pairwise-capped (#4818) |
| **Transverse** pairing, single-generator `σ₁³` | `= 0` **in a fixed germ trivialisation** (#4848; gauge-dependent, §3.2) |
| **Transverse** pairing, multi-generator atom words | nonzero and super-pairwise (#4849) — but **not a gauge-invariant object** (**this audit**) |
| Nucleon-ordering symmetry | forced but vacuous (#4850) |
| **The covariant order-2 object** (`[α]∪[α] ∈ H²`) | **`= 0` identically, explicit primitive** (**this audit**) |

> **The transverse NA-Stokes route is closed, and closed at the level of the observable
> rather than of its value.** The question was never "which germ observer pair"; it was
> whether the object being observed exists basis-independently. It does not. The one
> covariant construction the germ genuinely supports at second order — the cup square — is
> exact for a structural reason that will not go away: `q` is one direction, and a curvature
> needs two.

**Do NOT redo:** any transverse-pairing / surface-curvature magnitude extraction under any
germ normalisation, handle-holonomy convention, intersection form, observer-pair selection
rule, or representation basis. There is no invariant to extract. **Do not run another
discretization or observer sweep** — a sweep cannot recover an object that has no
basis-independent value.

**What a future attempt must use instead.** If the `q`-deformation's second-order structure
is to carry physics, it must be built from the **cohomology class** `[α] ∈ H¹(B_n; 𝔤𝔩_{Adρ})`
— the actual gauge-invariant content — not from matrix commutators of germ *values*. Two
honest observations for whoever picks this up:

1. The cup square of that class vanishes (§2.5), so the *quadratic* invariant of the class
   is empty; any nonzero invariant must be of a different type (e.g. a pairing of `[α]`
   against a **homology** class of `B_n`, or a non-quadratic invariant).
2. The invariant *linear* functional `τ(α(w))` is abelian (writhe/framing) and already
   walled. So the interesting content, if any, is in the **non-abelian** part of `[α]` — and
   nothing in the corpus currently extracts it.

---

## 6. Discipline record

- `free_parameters = 0`. **No AME quantity, no `g₂`, and no binding number appears anywhere
  in this audit's compute** — not even as a post-hoc comparison, because there is no
  determined value to compare. The forbidden seventh ansatz (selecting an observer pair
  because its value looks right) is not merely avoided: the audit removes the selection
  problem entirely.
- `q₀` = **experimental proton anchor** (`qou_substrate.constants.Q_50_DIGIT_STR`, owner
  directive 2026-08-07); no muon-serving cache is touched anywhere in the probe; layer-pure.
  The `A ≥ 3` germ is `q`-dependent (#4849 §2.2), unlike #4848's, so the pin is **material**
  and is recorded in the witness. Part A's symbolic results are `q`-general (they hold as
  identities in `ℚ(q)`), so no anchor enters them.
- Arithmetic: exact `sympy` over `ℚ(q)` in Part A. `float64` in Part B, where the verdict is
  a `0`-vs-`O(1)` question (covariance defect) and a sign-flip / order-of-magnitude question
  (invariants), not a 1-ppQ question; every representation is certified on braid + Hecke +
  far-commutation to `≤ 3.7e-15` and the connection law reproduces to `≤ 4.9e-15`.
- Run cost: 4.4 s wall, single process. No long-compute logging discipline needed.
- Lean sorry-free; `#print axioms` clean on all **48** declarations; generic `Ring R`
  throughout (§7c) with a `Matrix (Fin 2) (Fin 2) (Polynomial ℚ)` witness ring — no `ℝ`, no
  ordering, no `Real.*`. **Registered in the `QOU` umbrella**, along with #4848's
  `GermRootVectorGaugeFixing` and #4849's `TransversePairingClusterDecomposition`, both of
  which landed unregistered and were therefore built by nothing.
- Bean `qou-prjo` stays **OPEN**. This closes a route by showing its observable does not
  exist; it does not close the magnitude.
