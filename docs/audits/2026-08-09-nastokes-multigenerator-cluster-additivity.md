# NA-Stokes transverse pairing on multi-generator words: super-pairwise, and undetermined

**Date:** 2026-08-09 · **Bean:** `qou-prjo` (deuteron Δ_λ magnitude) — stays **OPEN**
**Branch:** `claude/nastokes-multigen-additivity-2026-08-09` · **PR** [#4849](https://github.com/litlfred/qou/pull/4849)
**Predecessors:** [#4848](https://github.com/litlfred/qou/pull/4848) (single-generator scope-(b);
conventions pinned), [#4818](https://github.com/litlfred/qou/pull/4818) (Betti-additivity
scope-(b); trace-null), [#4798](https://github.com/litlfred/qou/pull/4798) (the trefoil
discretization; `0…897` spread), [#4619](https://github.com/litlfred/qou/pull/4619)
(`tr[A,B] = 0`).

---

## 0. The question, and the four-line answer

#4848 closed the transverse pairing on **single-generator** `(2,L)`-torus channels
(the deuteron `pn` word `σ₁³`) and wrote: *"Multi-generator words (`A ≥ 3` nuclei) are
untouched … that case remains scope-(a) open."* This audit runs it.

1. **The canonical `A ≥ 3` words already exist** in the corpus
   (`atom_braid_word_3A`); none had to be derived. **Every** atom word — including
   the `A = 2` deuteron, which is 6 strands on generators `σ₀…σ₄` — is
   **multi-generator**, so #4848's scope-(b) reaches none of them.
2. The determined pairing is **nonzero**, and its three- and four-body Möbius
   (cluster) residuals are **nonzero**: **SUPER-PAIRWISE**. It is not the additive,
   pairwise-capped object #4818 excluded.
3. But Lean (sorry-free) shows the pairing is an **exactly quadratic** cluster
   functional, so **all** of that super-pairwise content is attributable to
   **context-dependence of the Yekutieli transport** — not to any three-body
   property of the curvature.
4. And the **value is not determined**: it depends on which two germ observers are
   chosen, and — fatally for a many-body binding term — on the **order in which the
   nucleons are listed**, a relabelling the corpus's own scalar observables are
   invariant under. #4798's gauge problem is **live** at `A ≥ 3`; #4848 dissolved it
   only because the single-generator answer was `0` in every gauge.

**Verdict: scope-(a).** Super-pairwise is a *necessary* property of the missing
≥3-body term, not a sufficient one. This supplies at most one input. `free_parameters = 0`;
no AME number is an input anywhere; nothing is wired; the bean stays **OPEN**.

---

## 1. Phase 0 — corpus grep (mandatory)

Per AGENTS.md §"Before declaring open math". Searched `computations/`, `content/`,
`docs/audits/`, `docs/coordination/` for multi-nucleon braid words, `atom_braid_word_3A`,
`canonical_braid`, per-ordering emitters, and Seifert/transport conventions.

**Result: the words exist. #4818's "the corpus lacks the canonical multi-nucleon
Seifert braid word" is superseded.**

| Datum | Where | What it is |
|---|---|---|
| Canonical `3A`-strand word | [`computations/mass_at_3A_proper.py::atom_braid_word_3A(Z,N)`](../../computations/mass_at_3A_proper.py) | per nucleon `k`: intra chains on `σ_{3k}, σ_{3k+1}`, then the adjacency-typed inter-nucleon crossing on `σ_{3k+2}`. Letters are `c·σ_g + d·1` (pp `= σ`, nn `= σ⁻¹`, pn `= σ − h(½ − δ/4)`, colour-weighted). |
| Per-ordering emitter | [`computations/atom_orbit_reduction.py::atom_braid_word_ordered`](../../computations/atom_orbit_reduction.py) | same word for an explicit species ordering; its `OrbitRepresentative` records that `tr_M(β) = tr_M(rep)` **exactly** — the scalar trace is ordering-invariant. |
| Crossing-type map | [`computations/markov/markov_weights_symbolic.py`](../../computations/markov/markov_weights_symbolic.py) | `(c,d) ↦ {sigma, sigma_inv, averaged}` |
| Transport ordering | `QOU.MathlibExt.YekutieliIntegration` (`holonomy`, `holonomy_append`) | ordered product in path order |
| Seifert combinatorics | `QOU.MassTheory.TransverseSurfaceCurvature.seifertBettiOne` | `b₁ = c − s + 1`; discs ↔ strands, bands ↔ crossings |
| Germ | [`def:germ-commutator-q-curvature`](../../content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.md) | `[δq₁, δq₂] = F_q`, two observers' germ-level `q`-increments |

**Word shapes** (measured, this branch):

| word | `A` | strands | letters | generators used | multi-generator? |
|---|---|---|---|---|---|
| D `(1,1)` | 2 | 6 | 23 | `σ₀…σ₄` | **yes** |
| T `(1,2)` | 3 | 9 | 35 | `σ₀…σ₇` | **yes** |
| ³He `(2,1)` | 3 | 9 | 35 | `σ₀…σ₇` | **yes** |
| ⁴He `(2,2)` | 4 | 12 | 47 | `σ₀…σ₁₀` | **yes** |

> **Scoping note for #4848 (not a correction — a distinction).** #4848's scope-(b) is
> stated, correctly, for *single-generator* channels, and the deuteron `pn` **channel**
> word `σ₁³` is one. The **6-strand deuteron atom word** that the mass/binding compute
> actually consumes is a different corpus object and is multi-generator. So
> "the deuteron channel is order-2 sterile" is true of `σ₁³` and does **not** transfer
> to `atom_braid_word_3A(1,1)`. Both objects are legitimate; they must not be conflated.
> Posted to #4619 as a coordination note.

---

## 2. Construction — the determined transport, and one derived prune

**Representation.** The corpus canonical seminormal / Hoefsmit rep of `H_n(q)`
(`build_seminormal_matrices`: `a = h/(1−q^{−2ρ})`, `a′ = h/(1−q^{2ρ})`,
`b² = a a′ + 1`), rebuilt in the probe from the identical closed form with
**analytic** entry derivatives, and **certified before use** — braid, Hecke, and
far-commutation relations all hold to `≤ 3.6e-15`. Everything is done in
`H₁₂(q)` (`n = 12 = 3·4`) so the `A = 2, 3, 4` words live in **one** algebra and
their operators are directly comparable; sub-configurations never change the algebra.

**Transport.** Yekutieli ordered partial product before band `k`:
`U_k = ρ(ℓ₁)⋯ρ(ℓ_{k−1})`. Inverses are exact and matrix-free — from `σ² = hσ + 1`,
`(c σ + d)⁻¹ = (1/c)(α σ + β)` with `α = 1/(1 − e h − e²)`, `β = −α(h+e)`, `e = d/c`.
No matrix inversion occurs anywhere in the probe.

**Germ.** `δq_i = q (∂_q ρ(σ_i)) ρ(σ_i)⁻¹`, with `ρ(σ)⁻¹ = ρ(σ) − h`.

### 2.1 Derived prune — only *adjacent* germ observers carry curvature

`F_q = [δq_i, δq_j] = 0` **identically** for `|i − j| ≥ 2`: there `σ_i` and `σ_j`
commute and each germ lies in the subalgebra generated by its own generator.
Measured: `max‖F(i,j)‖ over |i−j| ≥ 2 = 0.000e+00` **exactly**, at every `λ`;
`min` over adjacent pairs `= 2.48…7.45` (λ-dependent). So the admissible observer
pairs are exactly the `n−2` adjacent ones — a genuine narrowing of the gauge, though
not to a point.

### 2.2 The germ is **`q`-dependent** for `A ≥ 3` — #4848's `q`-independence was a `|ρ| = 1` accident

Symbolically, in a seminormal block of axial distance `ρ`:

- `|ρ| = 1` (1×1 blocks): `δq = +1` (same row) or `−1` (same column) — **constant in `q`**.
- `|ρ| = 2`: `δq = [[2q²/(q²+1)², q³(q⁴+2q²+3)/(√(q⁴+q²+1)(q²+1)²)], [(3q⁴+2q²+1)/(q√(q⁴+q²+1)(q²+1)²), −2q²/(q²+1)²]]` — **manifestly `q`-dependent**.

#4848 worked in the 2-dimensional rep, where every axial distance is `±1` in the
relevant gauge, and found `δq₁ = H − 2E`, `δq₂ = −H` constant. That does **not**
generalise: as soon as a block with `|ρ| ≥ 2` appears — i.e. as soon as `n ≥ 4` —
the germ carries `q`. Measured drift `max_i ‖δq_i(q₀) − δq_i(1.25)‖` is reported in
§5. **Diagnostic answer: the multi-generator result is `q`-dependent, unlike #4848's.**

### 2.3 🛑 The germ is a *connection*, not a tensor — a gauge the corpus has never pinned

Under a change of representation basis `B`, `ρ ↦ BρB⁻¹`, the germ transforms as

$$
  \delta q \;\longmapsto\; B\,\delta q\,B^{-1} \;+\; \bigl(1 - \mathrm{Ad}(\rho(\sigma))\bigr)\bigl(q\,(\partial_q B)\,B^{-1}\bigr),
$$

i.e. **inhomogeneously**, whenever `B` depends on `q`. The seminormal basis *is*
`q`-dependent (through `b = √(1 − 1/[ρ]²)`), and the reduced-Burau basis used by
#4798/#4848 is a different `q`-dependent gauge. Hence `F_q = [δq_i, δq_j]` is
**basis-dependent**, and so is any number extracted from it.

This does **not** disturb #4848's conclusion — the answer there was `0` in every
gauge, which is exactly why the gauge did not have to be fixed. It does mean that
any **nonzero** multi-generator value inherits a freedom the corpus has never
addressed. Recorded here so a later agent does not read a germ-derived magnitude as
canonical. This audit therefore reports the **verdict's** robustness across gauges,
and explicitly declines to report a canonical value.

---

## 3. The Lean half — the pairing has no irreducible ≥3-body content of its own

[`QOU/MassTheory/TransversePairingClusterDecomposition.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransversePairingClusterDecomposition.lean)
— **sorry-free**, generic non-commutative `Ring R` (§7c: no `ℝ`, no ordering, no
`Real.*`); `scripts/lean-verify.sh` **exit 0**; `#print axioms` on **all 11**
declarations gives at most `[propext, Quot.sound]` — no `sorryAx`, no `axiom`, no
`native_decide`, no `: True`.

Formalize-first, this was written **before** the sweep, and it narrows what the
sweep can mean:

| Result | Statement |
|---|---|
| `rowPairing_eq_curvComm_sum` | `rowPairing c l = ⟦Σ l, c⟧` — a row depends on its block only through the **sum** |
| **`listPairing_append`** | `Ω(l₁ ++ l₂) = Ω(l₁) + Ω(l₂) + ⟦Σ l₂, Σ l₁⟧` — the block interaction is **one** commutator |
| `listPairing_append_eq_add_iff` | additive across a split **iff** the two block sums commute |
| `listPairing_append_add_of_collinear` | #4848's mechanism in cluster language: block sums collinear ⇒ additive |
| **`moebius3_eq_zero`** | `Ω(123) − Ω(12) − Ω(13) − Ω(23) + Ω(1) + Ω(2) + Ω(3) = 0` **identically** |
| **`moebius4_eq_zero`** | the 15-term four-block alternating sum `= 0` **identically** |
| `moebius3_eq_sub_of_context` | a measured residual equals exactly the change caused by the lists differing |

**Reading (this is the load-bearing point).** `listPairing` is *bilinear* in the
transported curvatures, so under **any** block partition it terminates at two-block
terms. A bilinear functional has no irreducible `k`-body content for `k ≥ 3`.
Therefore a nonzero measured three-body residual has **exactly one** possible source:
the per-block transported-curvature *lists* differ between sub-configurations.
Under the pinned Yekutieli ordering they do — the transport to a band is the ordered
product of everything earlier in the word, so deleting a nucleon changes the
transport of every later one.

So the measurement below is **not** a measurement of a three-body curvature. It is a
measurement of **holonomy context-dependence**, which is what non-abelian Stokes
*means*. That reframing is the honest content of this audit and it is what stops the
result being over-read.

> **`sorry-free ≠ derived`.** The Lean proves the algebra. It derives no magnitude,
> no `Δ_λ`, no binding energy, and it is not evidence that the transverse route
> closes anything.

---

## 4. The measurement

[`computations/probes/nastokes_multigen_cluster_additivity_probe.py`](../../computations/probes/nastokes_multigen_cluster_additivity_probe.py)
→ `nastokes-multigen-cluster-additivity.witness.json`.

**Sub-configuration.** For `S ⊆ {nucleons}`: keep nucleon `k`'s intra letters iff
`k ∈ S`, and link `k` iff **both** endpoints are in `S`; order preserved, generator
indices untouched. Möbius residual `R_S = Σ_{T ⊆ S} (−1)^{|S|−|T|} Ω(T)`.

**Readout — and why it is outside the trace-null theorem.** The verdict is stated on
the **operator**: `R₃ = 0` or `R₃ ≠ 0` as a matrix. That is readout-free. Frobenius
norms only give the operator a size, and `‖X‖_F² = tr(X Xᴴ)` is **quadratic**, not a
cyclic **linear** functional — `listPairing_trace_zero` kills `τ(X)` for linear cyclic
`τ` and says nothing about `tr(X Xᴴ)`. The scalar trace is reported as a **control**
and vanishes to round-off (`max |tr Ω| / ‖Ω‖ ≈ 1e-16`), exactly as that theorem
requires. Had the readout been secretly cyclic the answer would have been `0` by
theorem; it is not, and the control proves the arithmetic agrees with the theorem.

### 4.1 Result — nonzero, and super-pairwise

Representative rows (`λ = (10,1,1)`, dim 55; full tables in the witness):

| word | germ pair | `‖Ω‖` | `tr Ω` | `‖R₂‖` | `‖R₃‖` | `R₃/‖Ω‖` | `‖R₄‖` |
|---|---|---|---|---|---|---|---|
| T (A=3) | `(0,1)` | 8.637e3 | 1.1e-13 | 4.548e3 | **8.294e3** | 0.960 | — |
| T | `(3,4)` | 2.874e3 | −2.4e-13 | 1.397e3 | **6.510e3** | 2.265 | — |
| T | band-local | 2.082e3 | 3.7e-14 | 1.136e3 | **7.113e2** | 0.342 | — |
| ³He (A=3) | `(0,1)` | 8.978e3 | 8.0e-13 | 4.628e3 | **7.837e3** | 0.873 | — |
| ⁴He (A=4) | `(0,1)` | 1.485e4 | 4.5e-13 | 4.628e3 | **7.837e3** | 0.528 | **2.863e3** |
| ⁴He | `(3,4)` | 7.025e3 | −4.1e-13 | 1.479e3 | **7.699e3** | 1.096 | **1.069e4** |
| ⁴He | band-local | 3.216e3 | −5.0e-14 | 1.363e3 | **8.813e2** | 0.274 | 1.5e-11 |

**Aggregate over all 81 support-coupled readings:**

| quantity | min | max |
|---|---|---|
| `‖R₃‖` (curvature coupled to the cluster) | 8.347e0 | 1.978e4 |
| `‖R₄‖` (coupled, 30 readings) | 8.305e1 | 2.307e4 |
| `‖R₃‖` (curvature **central** for the cluster, 9 readings) | — | **8.79e-13** |

**Consistency check that the residual is real and not numerical noise.** `σ_a` and
`σ_b` commute iff `|a − b| ≥ 2`, so a germ curvature whose support sits at distance
`≥ 2` from every generator the cluster's word uses is **central** for that cluster —
all transported curvatures coincide and `R₃` must vanish identically. Measured:
`≤ 8.79e-13` on all 9 such readings, against `O(10¹…10⁴)` on every coupled one. The
residual switches on exactly where the curvature can see the cluster, and off exactly
where the algebra says it must.

**Trace control:** `max |tr Ω| / ‖Ω‖ = 2.21e-16` over all readings — the arithmetic
reproduces `listPairing_trace_zero` to machine epsilon, which is *why* a scalar
readout would have returned `0` by theorem and why the operator readout is necessary.

**Answer to the bean's question: SUPER-PAIRWISE.** The object is *not* additive over
links and therefore is *not* killed by #4818's pairwise cap.

### 4.2 Cluster budget — how much of `Ω` is irreducibly many-body

⁴He, `λ = (10,1,1)`, band-local curvature; `Ω(1234) = Σ_S R_S` exactly (Möbius
inversion), so the norms are a genuine budget:

| cluster level | `√(Σ_S ‖R_S‖²)` | as % of `‖Ω‖` |
|---|---|---|
| 1-body | 6.660e2 | 20.7 % |
| 2-body | 2.638e3 | 82.0 % |
| **3-body** | **1.584e3** | **49.2 %** |
| 4-body | 1.487e-11 | **0.0 %** |
| `‖Ω(1234)‖` | 3.216e3 | |

Roughly half the object is irreducibly three-body — far from a rounding effect. The
**four**-body level is empty for the band-local curvature (though not for a constant
curvature, where `‖R₄‖ = O(10³)`), which is itself a structural difference between
the two curvature assignments and one more sign that the assignment is not pinned.

### 4.3 Robustness across `λ` — near-invariant

`R₃/‖Ω‖` for T across five partitions of 12 spanning dim 11…165 and 2…6 rows:

| germ reading | `(11,1)` d11 | `(10,2)` d54 | `(10,1,1)` d55 | `(9,1,1,1)` d165 | `(2⁶)` d132 | spread |
|---|---|---|---|---|---|---|
| `(0,1)` | 0.9603 | 0.9287 | 0.9603 | 0.9603 | 0.9322 | 1.034× |
| `(3,4)` | 2.2653 | 2.0613 | 2.2653 | 2.2653 | 2.2356 | 1.099× |
| band-local | 0.3417 | 0.3476 | 0.3417 | 0.3417 | 0.3566 | 1.044× |

Spread `≤ 10 %`. The *relative* three-body content is close to a property of the
algebra element rather than of the representation — a genuine robustness, and the one
axis along which the answer *is* stable.

### 4.4 …and the value is **not** determined along the axes that matter

The same table shows a factor `≈ 6.6` between germ-observer readings (`0.342`
band-local, `0.960` at `(0,1)`, `2.265` at `(3,4)`); over all support-inside-cluster
readings the spread is **16.4×**, and including marginally-coupled ones **676×**.
`def:germ-commutator-q-curvature` fixes that the curvature is the commutator of **two
independent observations at a point**; for `n > 3` it does not say **which two**.
§2.3's connection-gauge freedom sits on top of that. The decisive control is §5.1.

---

## 5. Controls

### 5.1 🛑 Nucleon **ordering** — the object is not a function of the nucleus

A many-body binding term must be invariant under relabelling the nucleons; the
corpus's own scalar observable is (`tr_M(β) = tr_M(rep)` **exactly**,
`atom_orbit_reduction`). Same species multiset, permuted, `λ = (10,1,1)`, germ `(0,1)`:

| word | orderings | `R₃/‖Ω‖` | spread |
|---|---|---|---|
| T (1p2n) | `pnn` / `npn` / `nnp` | 0.9603 / 1.0072 / 1.0867 | **1.13×** |
| ⁴He (2p2n) | `ppnn` / `pnpn` / `pnnp` / `npnp` / `nppn` / `nnpp` | 0.5279 / 0.5717 / 0.5779 / 0.5643 / 0.5574 / 0.5956 | **1.13×** |

**Not invariant.** The violation is modest (13 %) but it is 10¹³ times round-off, and
nothing in the construction makes it zero — the Yekutieli ordering is a *linear word*
order with no nucleon-exchange symmetry, and §3 shows the entire super-pairwise
content *is* that ordering. So the object as constructed is a function of the braid
word, not of the nucleus. Any use of it as a binding term needs an explicit
symmetrisation principle; the corpus supplies none.

### 5.2 `q`-dependence — unlike #4848

| quantity | value |
|---|---|
| `max_i ‖δq_i(q₀) − δq_i(1.25)‖` | **1.516** (0 would mean `q`-independent germs) |
| ⁴He `R₃/‖Ω‖` at `q₀` (proton anchor) | 0.527932 |
| ⁴He `R₃/‖Ω‖` at the diagnostic ray `q = 1.25` | 0.184658 |

**The multi-generator result is `q`-dependent**, by a factor `≈ 2.9` between the two
rays — so the `q₀` pin is *material* here, unlike #4848 where every quantity was
`q`-free. §2.2 gives the reason: the germ is `q`-free only where every axial distance
is `±1`. (`q = 1.25` is exactly representable, so the f64 guard on
`atom_braid_word_3A` is a false positive there and is overridden with a comment; it is
a diagnostic ray, never an anchor.)

### 5.3 Precision control

`λ = (11,1)`, ⁴He, germ `(0,1)`: `‖R₃‖` float64 `= 2.6124381803e+03`, mpmath 40-dps
`= 2.6124381803e+03`, relative difference **1.76e-14**. The float64 sweep is faithful
for a `0`-vs-`O(10³)` verdict.

**Witness:** 16 assertions, all passing, including `R3_is_ordering_dependent = 1` —
recorded as the finding, not as a failed hope.

---

## 6. Scope classification

Per AGENTS.md §"Before declaring refuted / ruled out / dead end".

**scope-(a).** Two scope-(a) statements, one positive and one negative:

- **(a⁺)** On the canonical multi-generator atom words, with the conventions #4848
  pinned, the transverse pairing is **nonzero and super-pairwise** — it clears the
  pairwise cap that #4818 proved kills the Betti/diagonal reading. That is a
  *necessary* property of the missing ≥3-body term.
- **(a⁻)** It is **not** a determined observable: the value varies by **16.4×** with
  the germ observer pair (§4.4) and by **1.13×** with the nucleon **ordering** (§5.1),
  and the germ carries an unpinned connection gauge (§2.3). The ordering dependence is
  the sharp one — a many-body binding term is a function of the nucleus, and this is a
  function of the braid word. A magnitude read off it would be a *choice*, and a
  choice made to land near an AME number would be the forbidden seventh ansatz.

**No scope-(b) is claimed anywhere in this audit.** No invariant excludes the route;
what is shown is that it does not currently *determine* anything.

**What is NOT shown:**

- Not that the transverse pairing *is* the missing term. Super-pairwise is necessary,
  not sufficient; the magnitude and the sign are untouched.
- Not that #4848 or #4818 is wrong. Both are correct on their stated scopes; §1 only
  separates the `pn`-channel word from the `3A`-strand atom word, and §3 explains why
  the residual is a transport statement rather than a curvature one.
- Not a `Δ_λ`, not a binding energy, not a wiring. Nothing here enters production.

---

## 7. What a revival of this route now needs

Precisely two things, both principles rather than probes — #4798's lesson, restated
one level up:

1. **Which two germ observers.** A corpus rule selecting the observation pair at a
   surface point for `n > 3` (the adjacency prune of §2.1 narrows it to `n−2`
   candidates; it does not choose). Plus a rule fixing the representation gauge of
   §2.3, since the germ is connection-like.
2. **A nucleon-symmetric readout.** The corpus's scalar observables are
   ordering-invariant (`tr_M(β) = tr_M(rep)` exactly, `atom_orbit_reduction`). Any
   operator-valued many-body term built from an ordered holonomy needs an explicit
   symmetrisation principle, or it is not a function of the nucleus.

Until both exist, a number extracted from this object is a gauge choice. **Do not
run another discretization sweep** — the sweep is not what is missing.

---

## 8. Discipline record

- `free_parameters = 0`. **No AME quantity, and no `g₂`, appears anywhere in this
  audit's compute** — not even as a post-hoc comparison, because there is no
  determined value to compare.
- `q₀` = experimental proton anchor (`qou_substrate.constants`, owner directive
  2026-08-07); no muon-serving cache touched; layer-pure. Unlike #4848 the result is
  `q`-**dependent**, so the pin is material and is recorded in the witness.
- Arithmetic: float64 in the sweep, cast at a **visible** boundary from the exact
  `mpf` word, with an independent mpmath 40-dps re-run of `R₃` as the control (§5.3,
  rel diff 1.76e-14). The verdict is a `0`-vs-`O(10³)` question, not a 1-ppQ question.
- Run cost: 40 s wall, single process. No long-compute logging discipline needed.
- Lean sorry-free, `#print axioms` clean on all 11 declarations, generic `Ring`.
- Bean `qou-prjo` stays **OPEN**. This characterises a candidate; it does not close
  the magnitude.
