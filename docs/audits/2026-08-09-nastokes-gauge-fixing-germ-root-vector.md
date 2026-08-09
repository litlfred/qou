# NA-Stokes transverse pairing: the gauge IS fixed, and the determined value is zero

**Date:** 2026-08-09
**Bean:** `qou-prjo` (deuteron Δ_λ magnitude) — stays **OPEN**
**Branch:** `claude/nastokes-gauge-fixing-2026-08-09` · **PR** [#4848](https://github.com/litlfred/qou/pull/4848)
**Predecessors:** [#4798](https://github.com/litlfred/qou/pull/4798) (discretization built, read as
gauge-underdetermined), [#4818](https://github.com/litlfred/qou/pull/4818) (Lean wall +
Betti-additivity scope-(b)), [#4619](https://github.com/litlfred/qou/pull/4619),
[#4817](https://github.com/litlfred/qou/pull/4817), [#4829](https://github.com/litlfred/qou/pull/4829)/[#4832](https://github.com/litlfred/qou/pull/4832)/[#4836](https://github.com/litlfred/qou/pull/4836).

---

## 0. The question, and the answer

PR #4798 built the discretization the bean had named as its wall — the Yekutieli
surface 2-form on the genus-1 trefoil Seifert surface — and reported

```
c₂ = ‖Ω₂^⊥‖ / h²  ∈  0 … 897   across six "natural" germ / handle choices,
```

never near the `g₂ ≈ 1.0087` that would close the deuteron. It concluded: *the
surface→scalar map carries O(100×) gauge freedom the corpus does not fix;
reviving the route needs a NEW PRINCIPLE fixing the germ + the two handle
holonomies.*

**This audit answers that question: yes, there is a derived principle; it is
already in the corpus; it fixes both gauges; and the determined value is `c₂ = 0`.**

The `0 … 897` spread is not a physical ambiguity. It is what you get by
averaging over choices the corpus already excludes. Restricted to the admissible
set, the pairing does not merely *have* a value — it has the **same** value for
every intersection form, every H₁ basis, and every handle assignment, and that
value is zero.

---

## 1. Phase 0 — corpus grep (mandatory, run before any derivation)

Per AGENTS.md §"Before declaring open math". Searched `content/`,
`computations/`, `docs/audits/`, `docs/coordination/` for Yekutieli
transport/ordering conventions, Seifert surface / Seifert form conventions,
handle holonomy, germ normalization, `P∮∮`, surface-ordered exponential.

**Result: the corpus already pins BOTH gauges. Neither needed to be invented.**

| Gauge | Pinned where | What it says |
|---|---|---|
| **Transport ordering** | [`QOU/MathlibExt/YekutieliIntegration.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/YekutieliIntegration.lean) | `holonomy segs = segs.prod` — the transport along a path is the **ordered product of its segments, in path order**; `holonomy_append` is the composition law. The continuum `P exp ∫` is explicitly *not* formalised, but the discrete ordering rule is, sorry-free. |
| **Seifert combinatorics** | [`QOU/MassTheory/TransverseSurfaceCurvature.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean) `seifertBettiOne` | `b₁ = c − s + 1` — Seifert's algorithm on a braid closure gives **discs ↔ strands, bands ↔ crossings**. Trefoil `σ₁³`: `b₁ = 3 − 2 + 1 = 2`. |
| **Germ normalization** | [`germ-commutator-q-curvature.md`](../../content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.md) | `[δq₁, δq₂] = F_q`, where `δq_i` are **germ-level increments of the substrate parameter `q`** in the germ algebra `A/𝔪_p²`. That is, `δq` is a derivative *in `q`* — the logarithmic `q`-derivative `q·(∂_q σ_i)·σ_i⁻¹`. |

**Negative Phase-0 findings** (recorded so a later agent does not re-search):
there is no corpus block assigning holonomies to Seifert-surface `H₁` handles;
no Seifert-matrix convention block beyond the standard `V = [[-1,1],[0,-1]]`
used in #4798; and `_deprecated/` holds several purged Yekutieli per-cell
probes, none of which touch surface transport. The prior agents' reading that
"the corpus lacks the data" was correct about the *handle→group-element
assignment* but missed that the two rules above **determine** it.

---

## 2. The derivation

### 2.1 The transport gauge is not free — and on `σ₁³` it is abelian

Seifert's algorithm on the closure of a braid word `w = σ_{i₁} ⋯ σ_{i_L}` gives
`n` discs (one per strand) joined by `L` bands (one per letter). The surface
deformation-retracts onto that band graph, so `H₁(Σ) ≅ H₁(G(w))`, of rank
`L − n + 1`; a spanning tree of `G(w)` gives the fundamental-cycle basis.

Yekutieli path-ordering then supplies the transport from the basepoint to band
`k`: it is the **ordered partial product** `U_k = ρ(σ_{i₁} ⋯ σ_{i_{k−1}})`.

For the deuteron `pn` channel the word is `σ₁³`. Hence:

> **Every admissible transport is a power of `ρ(σ₁)`.** The generator `σ₂` does
> not occur in the word, so any transport mentioning `ρ(σ₂)` is not a gauge
> choice — it is not a transport of this surface at all.

That alone deletes two of #4798's six rows (`s1,s2` → 897; `s2,s1s2` → 617 in the
log column). What remains is a ℤ-torsor of handle exponents — still, on its face,
a freedom. §2.3 removes it.

### 2.2 The germ gauge is not free — and the germ curvature is a root vector

`def:germ-commutator-q-curvature` fixes `δq_i = q·(∂_q σ_i)·σ_i⁻¹`. Evaluated in
the 2-dimensional Hecke representation (`ρ(σ₁) = [[q, −q⁻¹],[0, −q⁻¹]]`,
`ρ(σ₂) = [[−q⁻¹, 0],[−q, q]]`; eigenvalues `q, −q⁻¹`), this gives — **exactly, and
independently of `q`** —

$$
  \delta q_1 \;=\; \begin{pmatrix}1 & -2\\ 0 & -1\end{pmatrix} \;=\; H - 2E,
  \qquad
  \delta q_2 \;=\; \begin{pmatrix}-1 & 0\\ 0 & 1\end{pmatrix} \;=\; -H,
$$

with `H = diag(1,−1)`, `E = [[0,1],[0,0]]`. Their commutator is therefore

$$
  F_q \;=\; [\delta q_1,\, \delta q_2] \;=\; 2[E, H] \;=\; -4E
  \;=\; \begin{pmatrix}0 & -4\\ 0 & 0\end{pmatrix},
$$

a **pure root vector** of the `ρ(σ₁)` torus: traceless, nilpotent (`F_q² = 0`),
and carrying no Cartan component. Consequently

$$
  \mathrm{Ad}(\rho(\sigma_1))\,F_q \;=\; \rho(\sigma_1)\,F_q\,\rho(\sigma_1)^{-1}
  \;=\; (-q^2)\,F_q ,
$$

with eigenvalue `−q² = q / (−q⁻¹)` — exactly the ratio of `σ₁`'s two Hecke
eigenvalues, as root-space theory requires.

**The competing "`log σ`" germ of #4798 is not a `q`-germ at all.** `log ρ(σ_i)`
is the braid-direction connection 1-form `A`; its commutator is the
*inter-crossing Magnus* object, a different term of the same expansion — and one
already known to vanish identically on a single-generator word
(`eunit_magnus_order2_probe` N2). Numerically it is also *not* a root vector
(`‖Ad(σ₁)F_log − λF_log‖ = 14.48`), which is precisely why it fails to vanish and
produced the `294.57 / 616.92 / 251.50` column. Those rows measure the wrong
object.

### 2.3 The conclusion: the pairing vanishes, gauge-*independently*

Because `F_q` is an `Ad(ρ(σ₁))`-eigenvector, conjugating it by **any** power of
`ρ(σ₁)` returns a *scalar multiple of the same element*:

$$
  \mathcal{F}_k \;=\; \rho(\sigma_1)^{-k}\,F_q\,\rho(\sigma_1)^{k}
  \;=\; (-q^2)^{-k}\,F_q .
$$

All transported curvatures lie on **one line**. Hence `[𝓕_i, 𝓕_j] = 0` for every
pair, and

$$
  \Omega_2^{\perp} \;=\; \sum_{i,j} J_{ij}\,[\mathcal{F}_i, \mathcal{F}_j] \;=\; 0
$$

**for every intersection form `J`** (so every Seifert matrix, every `H₁` basis,
every spanning tree) **and every handle-exponent assignment**. The handle gauge
did not need to be fixed: the answer does not depend on it.

Robustness: the vanishing holds for any transport lying in the Borel subgroup
containing `ρ(σ₁)` — which is every element the word `σ₁³` can build. Only a
transport using `ρ(σ₂)` escapes, and `σ₂` is not in the word.

---

## 3. Verification

### 3.1 Lean — sorry-free

[`QOU/MassTheory/GermRootVectorGaugeFixing.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/GermRootVectorGaugeFixing.lean)

| Layer | Declarations |
|---|---|
| **Abstract** (generic `CommRing` scalars acting on a generic `Ring`, §7c) | `IsRootVector`, `transported`, `transported_eq_smul` (root-vector conjugation is scalar), `comm_smul_smul`, **`transversePairing_eq_zero`** (vanishing for every `J` and every exponent assignment), `transversePairing_genusOne_eq_zero` |
| **Concrete** (generic `Field`, 2-dim Hecke rep) | `heckeGen1_mul_inv`, `heckeGen1Inv_mul`, `heckeGen_braid`, `heckeGen1_hecke`, `heckeGen1_logDeriv`, `germCurvature_eq`, `germCurvature_sq`, **`germCurvature_conj_heckeGen1`**, `isRootVector_germCurvature`, `deuteron_transversePairing_eq_zero`, `trefoil_transversePairing_eq_zero` |

`scripts/lean-verify.sh` → **exit 0**. `#print axioms` on **all 16** declarations
→ `[propext, Classical.choice, Quot.sound]` only; **no `sorryAx`**, no `axiom`,
no `native_decide`, no `: True`. The braid and Hecke relations are proved (not
assumed) so the matrices are certified to be the Hecke generators, not arbitrary
data. Base ring per §7c: no `ℝ`, no ordering, no `Real.*`.

> **"sorry-free ≠ derived" seam — cite accordingly.** Lean proves the *algebra*.
> The single by-hand step is `∂_q ρ(σ_i) = dHeckeGen_i` (entrywise
> differentiation of a 2×2 matrix of rational functions in `q`). `sympy` performs
> that differentiation independently in the probe and agrees exactly. Cite as
> *"the germs are the constant matrices `H − 2E` and `−H`, and Lean proves their
> commutator is the root vector `−4E` with `Ad(σ₁)F = −q²F`"* — never *"Lean
> proves the germ is the `q`-derivative"*.

### 3.2 Probe + witness

[`computations/probes/nastokes_germ_root_vector_gauge_probe.py`](../../computations/probes/nastokes_germ_root_vector_gauge_probe.py)
→ `nastokes-germ-root-vector-gauge.witness.json`. Symbolic (`sympy`, exact over
`ℚ(q)`) + numeric (`mpmath` 50 dps, **experimental proton anchor**). 7/7
assertions pass.

```
  braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂            : True
  Hecke relation (σ₁−q)(σ₁+q⁻¹) = 0         : True
  δq₁ = [[1,-2],[0,-1]]   q-independent      : True
  δq₂ = [[-1,0],[0,1]]    q-independent      : True
  F_q = [[0,-4],[0,0]]    root vector        : True   traceless + nilpotent : True
  Ad(σ₁) F_q = (−q²)·F_q                     : True

  EXHAUSTIVE over all 49 handle-exponent pairs (a,b) ∈ {0..6}²:
      max ‖[𝓕_a, 𝓕_b]‖ = 1.17e-52          ⇒  determined c₂ = 2.7e-51  (i.e. 0)
      derived trefoil reading (J = V−Vᵀ, exponents 1,2): c₂ = 5.9e-52

  Attribution of the #4798 spread — every nonzero entry is inadmissible:
      qderiv; s1,s2      → 896.71   uses ρ(σ₂), absent from the word
      log germ; s1,s1²   → 294.57   log σ is the connection 1-form, not a q-germ
                                     (root-vector defect 14.48 ⇒ not a root vector)
```

Comparison to `g₂ ≈ 1.0087` is made **only after** the value is fixed by the
principle. `free_parameters = 0`; AME never inverted; nothing wired.

Note: every symbolic result is `q`-independent, so the `q₀` pin does not affect
the conclusion. The experimental proton anchor is used and recorded for
layer-purity bookkeeping.

---

## 4. Scope classification

Per AGENTS.md §"Before declaring refuted / ruled out / dead end".

**scope-(b) — STRUCTURAL EXCLUSION, restricted to single-generator `(2, L)`-torus
channels** (the deuteron `pn` channel `σ₁³`).

**Cited invariant:** the germ `q`-curvature `F_q` is an `Ad(ρ(σ₁))`-eigenvector
(a root vector) — Lean-proved sorry-free, `germCurvature_conj_heckeGen1` — and
every transport the word `σ₁³` can build is a power of `ρ(σ₁)`. Scalar multiples
of a common element commute, so the pairing is annihilated identically. This is
a proved algebraic obstruction, not a failed numerical search, which is what
licenses (b) rather than (a).

**What is NOT excluded** — state this whenever citing the result:

- **Multi-generator words (`A ≥ 3` nuclei) are untouched.** There the transports
  involve both `ρ(σ₁)` and `ρ(σ₂)`, the eigenvector property fails, and the
  transverse pairing is generically nonzero. That case remains **scope-(a) open**;
  #4798's `896.71` is in fact evidence that the object is large there.
- The transverse pairing as a *concept* is not refuted. It is refuted **as the
  source of the deuteron's order-`h²` coefficient**.
- Nothing here bears on the `Δ_λ` **value** (proved, `(−1)^{n(λ)}·dim V_λ`) or on
  the super-pairwise extensive term, which remains the open magnitude carrier.

---

## 5. What this does to the LEAD-2 geometric route

Read alongside the results already on `main`:

| Object on the `σ₁³` channel | Status |
|---|---|
| **Longitudinal** inter-crossing Magnus tower `Ω_k, k ≥ 2` | `= 0` identically (single generator, `[X,X] = 0`) — `eunit_magnus_order2_probe` N2 |
| **Transverse** surface-curvature pairing `½𝒫∮∮[𝓕,𝓕]` | `= 0` identically — **this audit**, Lean-proved |
| Scalar-trace visibility of any such term | `tr[A,B] = 0` — `listPairing_trace_zero` (#4818), #4619 |
| Diagonal / Betti-count reading | exactly linear in link count ⇒ pairwise-capped — `seifertBettiOne_link_additive` (#4818) |

> **The deuteron channel is order-2 STERILE in both directions.** The `−9.2 %`
> gap — equivalently the bar-even `g₂·h²` residual — is **not a second-order
> NA-Stokes effect at all**. The whole NA-Stokes organization contributes nothing
> at order 2 on a single-generator word, and the near-match `g₂ ≈ 1.0087` is not
> explained by it.

That closes the LEAD-2 geometric surface-curvature route **for the deuteron**,
honestly and with a named invariant, rather than leaving it parked behind an
unmeasurable gauge. The bean's magnitude question is unaffected and stays open.

**Do NOT redo:** any transverse-pairing / surface-curvature closure on a
single-generator channel, under any germ normalization or handle-holonomy
convention. The vanishing is gauge-independent.

**Still open (the honest next units):**

1. The transverse pairing on **multi-generator** words (`A ≥ 3`). The
   root-vector mechanism fails there; whether the resulting object is
   super-pairwise (the property the missing term needs) is untested. Note it is
   still killed by the scalar trace (`listPairing_trace_zero`), so any use of it
   must go through a non-trace functional — which is itself an open licence
   question.
2. The `g₂ ≈ 1.0087` near-match now has **no** NA-Stokes explanation. Either it
   comes from a different structure entirely, or it is a coincidence. It was
   never derived and must not be wired.
3. The super-pairwise extensive term (bean `qou-prjo`'s actual magnitude gate)
   is untouched by all of the above.

---

## 6. Discipline record

- `free_parameters = 0`. `g₂ ≈ 1.0087` appears **once**, in a post-hoc
  comparison after the value is fixed by the principle. Never an input, never
  inverted, never used to select among gauge choices — the failure mode the task
  brief flagged as the forbidden seventh ansatz.
- AME data not used anywhere in this audit's compute.
- `q₀` = experimental proton anchor (`qou_substrate.constants`); no muon-serving
  cache touched; layer-pure. Immaterial anyway — every result is `q`-independent.
- Lean: sorry-free, `#print axioms` clean on all 16 declarations, no
  `native_decide`, no `: True`, no axiom or class standing in for a proof.
- Bean `qou-prjo` stays **OPEN**. This closes a route; it does not close the
  magnitude.
