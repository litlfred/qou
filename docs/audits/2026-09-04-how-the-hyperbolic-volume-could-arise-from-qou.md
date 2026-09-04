# How the hyperbolic volume could arise from QOU — the route, with a tier on every link

**Date:** 2026-09-04 · **Bean:** `qou-xlw1` · **Branch:**
`claude/lean-prove-assertions-2026-09-04` (PR #6584) · **Agent:** corpus-grepper
· **Tier:** corpus-status audit. Read-only: no Lean written, no content block
edited, nothing committed by this sweep.

**Prompted by a retraction.** An earlier claim of mine — *"the hyperbolic volume
form isn't a QOU structure, it's imported, Mostow-rigid"*, and *"standard
hyperbolic geometry, cited — Mathlib has no such API and `library/` holds nothing
on it"* — is **wrong in all three parts**, and the corpus disagreed with it
before I made it. This document is the measurement that replaces it.

---

## 0. The retraction, measured

| my claim | measured |
|---|---|
| "Mathlib has no such API" | Mathlib carries `Analysis/Complex/UpperHalfPlane/{Metric,Basic,Manifold,MoebiusAction,Topology}` — the hyperbolic metric on `ℍ²` and the Möbius action — plus all of `NumberTheory/ModularForms/`. What it lacks is a **dilogarithm** and a **3-dimensional** hyperbolic-manifold API. |
| "`library/` holds nothing on it" | `library/` is saturated. Re-measured this session (below). |
| "it's imported, not a QOU structure" | QOU has **~180 of its own `.lean` files** on this layer, including a from-scratch construction of the hyperbolic path-length metric on `H³`, and a **numerically confirmed** volume conjecture for `4₁`. |

**Why the error happened, since it is a repeat of a named class.** I searched the
**contact/CR** vocabulary (`Sasakian`, `CR manifold`, `7-manifold`) and read the
empty result as an absence. This layer is filed under the **knot-theory /
dilogarithm** vocabulary. Same shape as the `Sp(1)` vs `\mathrm{Sp}(1)` and
`sasaki` vs `Sasakian` traps already recorded in
`.claude/agent-memory/corpus-grepper/resolved-topics.md`.

**A spelling correction to the brief that sent me here.** The en-dash/hyphen pair
was quoted with the numbers swapped. Measured, case-insensitive, over
`library/*/sections/`:

| spelling | section files | section dirs |
|---|---:|---:|
| `Bloch-Wigner` (hyphen) | **135** | 13 |
| `Bloch–Wigner` (en-dash) | **19** | 10 |
| `Neumann-Zagier` (hyphen) | **96** | 29 |
| `Neumann–Zagier` (en-dash) | **65** | 14 |

The lesson stands and is if anything stronger — both spellings are live, in both
directions, and neither is a superset of the other.

---

## 1. Six-path sweep

**Path 0 — `corpus_search` (MCP): UNAVAILABLE.** `paper-assistant` failed to
connect this session (`ENOENT: /home/litlfred/folio-assistant/scripts/start-folio-assistant.sh`),
as it has for three sessions. **The blind spot it exists to cover is therefore
uncovered here**: every result below is lexical, so prior work phrased in
vocabulary I did not try is not excluded. Given that this audit exists *because
of* a change-of-vocabulary miss, that caveat is load-bearing. I mitigated it by
running 40+ spellings rather than by claiming coverage.

Counts are **files**, excluding `content/**/.lake/` (Mathlib vendored under
`content/` inflates every naive count by ~65 %; my first pass made that error).

### Paths 1–3, 6 — the knot-complement layer is saturated

| topic | `content/` | `docs/` | `computations/` | `.beans/` |
|---|---:|---:|---:|---:|
| hyperbolic volume | 277 | 170 | 186 | 47 |
| Kashaev | 222 | 268 | 236 | 102 |
| volume conjecture | 77 | 77 | 50 | 42 |
| ideal tetrahed* | 76 | 22 | 32 | 21 |
| Thurston | 75 | 54 | 57 | 22 |
| SnapPy | 80 | 155 | 273 | — |
| Bloch–Wigner (both spellings) | 50 / 48 | 50 / 53 | 28 / 78 | 20 / 16 |
| gluing equation | 30 | 18 | 28 | 16 |
| Neumann–Zagier (both) | 36 / 5 | 49 / 2 | 29 / 23 | 15 / 15 |

### Paths 1–3, 6 — the *Bring-surface-own-metric* layer is nearly empty

| topic | `content/` | `docs/` | `computations/` | `.beans/` |
|---|---:|---:|---:|---:|
| Fuchsian | 6 (all ODE homonym — see below) | 7 | 6 | 5 |
| uniformis/uniformiz | 1 | 2 | 0 | 0 |
| Gauss–Bonnet (both) | 11 / 10 | 17 / 2 | 7 / 26 | **0 / 0** |
| hyperbolic metric | 4 | 2 | 0 | 2 |
| hyperbolic area | 1 | 2 | 2 | 0 |
| constant negative curvature | 2 | 0 | 0 | 0 |
| triangle group | 1 | 2 | 3 | **0** |
| `(2,4,5)` / `(2, 4, 5)` | — | — | — | **0 / 0** |
| systole | **0** | **0** | **0** | **0** |
| Teichmüller | 5 | 11 | 34 | 12 |

**Homonym trap, recorded so it is not re-hit.** All six `content/` `Fuchsian`
hits are the **Fuchsian singular point of an ODE** (`C1ZeroSideExponents.lean`,
`C1FuchsianExponents.lean`, `BirkhoffAmplitudeE.lean` — the C1 indicial equation
`c₀² + (q−1)c₀ + (q−1) = 0`). **Not one is a Fuchsian *group*.** A count of
"Fuchsian" in this corpus measures the irregular-singularity work, not
hyperbolic uniformisation.

### Path 4 — coordination ledgers

`docs/coordination/` carries the `alpha-em*` and `s5-so3-keystone` threads that
touch Bring, and `1ppq-qbeta.md` for the `c₃`/`Vol(4₁)` leg. **No ledger on the
hyperbolic structure of Bring's surface.**

### Path 5 — the library (all four tiers)

Tier 1 is **current**: 576 directories, 552 `INDEX.md` rows, gap 24 against 23
directories carrying `duplicate_of` — i.e. the index is not in the stale state
recorded on 2026-09-03. Re-measured hit counts:

| topic | section files | section dirs | ocr files |
|---|---:|---:|---:|
| dilogarithm | 849 | 107 | 30 |
| Kashaev | 548 | 92 | 21 |
| volume conjecture | 381 | 72 | 12 |
| Thurston | 321 | 103 | 19 |
| gluing equation | 215 | 43 | 0 |
| ideal tetrahed* | 178 | 57 | 13 |
| uniformi* | 128 | 30 | 1 |
| Neumann-Zagier | 96 | 29 | 3 |
| Fuchsian | 63 | 25 | 0 |
| triangle group | 58 | 7 | 0 |
| Lobachevsky | 46 | 23 | 2 |
| Gauss-Bonnet | 21 | 12 | 0 |
| systole | 2 | 2 | 0 |

**The asymmetry is the finding.** The *library* holds the Fuchsian/uniformisation
material (63 / 58 / 128 section files). The *corpus* does not use it. So this is
**"cite it, not derive it"** — a held-source gap, not an open mathematical
problem.

---

## 2. The chain, link by link, with a tier on every link

Tiers used throughout:

- **T0 — proved.** Sorry-free Lean, unconditional.
- **T1 — proved-conditional.** Sorry-free modulo a *named* class that has **no
  instance** (§3b-cond). Honest; proves an implication, never its premise.
- **T2 — numerical.** A witness. No proof.
- **T3 — conjecture.** Block kind `conjecture`, class-carried, no instance.
- **T4 — prose.** Asserted in a `prose`/`remark` block. No Lean, no witness.
- **T5 — absent.**

### The route as the corpus actually has it

```
  q-Pochhammer denominator (x;q)_n
      │  L1  poles at x = q^{-k}                              T0
      ▼
  poles ←→ ideal-tetrahedron cusps of K_S
      │  L2  "pole-to-cusp bijection"                         T3  (+T2 bound)
      ▼
  shape parameters z_k on the Thurston gluing variety
      │  L3  cusp-completeness ⟺ denominator zero             T3
      ▼
  (1−q)·log Φ_n(x;q)  →  Li₂(x)                               T1 + T2
      │  L4  Faddeev scaling / Archimedean limit
      ▼
  D(z) = Vol_hyp(Δ_z),  Σ_S D(z_S) = Vol(S³∖K)                T3
      │  L5  volume conjecture (Kashaev–Murakami–Murakami)
      ▼
  Vol(4₁) = 2·Cl₂(π/3) → m_μ/m_e via CAL-2                    T2 (CONFIRMED)
```

### L1 — the pole side. **T0, and it is genuinely proved.**

`QOU.QPochhammer.denomPolyLocal_eq_zero_at_pole`
(`content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.lean:108`),
sorry-free, `q ≠ 0` only. Generic-field twin `QOU.QBeta.qPochDenom_eq_zero_at_pole`
in `lean/QOU/QBeta/QPochhammerPoles.lean`.

> **🛑 Claim-shape defect — the theorem is named for something it does not
> contain.** The wrapper is called **`pole_cusp_bijection_proved`**
> (`:124`). Its statement is
> `∃ z : Fin n → ℝ, (∀ k, z k = q^(-k)) ∧ (∀ k, denomPolyLocal q (z k) n = 0)`.
> **There is no cusp in it, and no bijection** — it exhibits `n` roots of a
> polynomial. The *file* is honest about this in prose (`:96-98`: "Only the
> *cusp correspondence* … remain the open volume conjecture"), so the defect is
> the **name**, which is what a downstream reader greps. Anyone citing
> `pole_cusp_bijection_proved` as evidence for L2 is citing a polynomial
> root-finding lemma.

**Arity, asked and answered.** L2/L3 are stated for the **`Φ_q`-piece `K_S`**
of a lifted transient crossing, *not* for general knots —
`algebraic-geometric-dilog-equivalence.md:18-23`,
`shared-denominator-cusp-holonomy.md:6-20`. A reader who takes it as a general
pole↔cusp statement is over-reading it.

### L2 — pole ↔ cusp. **T3, and the corpus has already bounded its strong form.**

`conj:shared-denominator-cusp-holonomy` (`.md:1-32`), carrier class
`SharedDenominatorCuspHolonomy`, **no instance by design** — the cusp shape
assignment `k ↦ z_k` is a *parameter*, which is what stops `z = i` discharging it
(`.md:147-155`).

**Measured negative, scope-(a), already in the corpus.**
`computations/snappy-cusp-seeding.witness.json` (engine **snappy 3.3.2**, real
run, proton pin) compares the algebraic seeds `q₀^{-k}` to SnapPy's shapes for
`m004`, `m003`, `L6a4`: pairing distance **0.400 … 0.915**, mean **0.615**. So
`q₀^{-k} = z_k` is **false**; the conjecture survives only as a bijection of
*labels*, with the shape a non-trivial function of the seed. That function is
unidentified. The block says so itself (`.md:173-188`).

Positive side, same file: `computations/q-pochhammer-seed.witness.json` — Newton
converges to residual ≲1e-13 in 9–11 iterations from the seeds (`+0.1i`) at
depths `n ≤ 3`, supporting the *O(1)-steps* claim only.

### L3 — cusp completeness. **T3.** Same class. Proof sketch at
`shared-denominator-cusp-holonomy.md:56-86` is explicitly "modulo the upstream
conjectures".

### L4 — the Archimedean limit `(1−q)log Φ_n → Li₂`. **T1 + T2.**

`conj:dilogarithm-archimedean-limit`, class `QOU.QPochhammer.ArchimedeanLimit`.
Part A numerically confirmed:
`computations/dilog-archimedean-limit-partA.witness.json`
(`all_within_bound_and_monotone: true`, `max_abs_error_over_predicted_bound
0.1668`, mpmath 70 dps). ~25 `QOU/Archimedean/DilogPart*.lean` files carry the
formalisation programme, including a landed **scope-(b) refutation**
(`DilogPartBWP1Refutation.lean`).

### L5 — the volume conjecture. **T3 in Lean; T2 CONFIRMED numerically for `4₁`.**

`conj:kashaev-volume-conjecture`, class `QOU.Kashaev.VolumeConjecture` with
universal field `kvc_holds : ∀ β, hypVolume β = kashaevLimit β`.

**The numerics are real and are the strongest single result on this route.**
`computations/figure-eight-kashaev-volume.witness.json`, 60 dps, `⟨4₁⟩_N =
Σ_{k<N} Π_{j≤k} (2 − 2cos(2πj/N))`:

| N | Richardson | error vs `2.029883212819307…` |
|---:|---|---|
| 100 | 2.03612378… | 6.24e-3 |
| 400 | 2.03086739… | 9.84e-4 |
| 1200 | **2.03017614…** | **2.93e-4** |

`exponential_growth: true`, `converging: true`, **`verdict: CONFIRMED`**. This is
the hyperbolic volume emerging from a purely categorical (Kashaev/coloured-Jones)
object the framework already computes — the owner's claim, realised numerically.

> **🛑 A 2026-07-11 audit statement about this file is now STALE — do not
> re-quote it.** `docs/audits/2026-07-11-algebraic-geometric-dilog-provability.md`
> reports *"the Kashaev conditional theorems are vacuous stubs … conclude
> `: True := trivial`"*. They no longer do:
> `figure_eight_volume_from_vc` / `borromean_volume_from_vc`
> (`kashaev-volume-conjecture.lean:144,154`) are now real conditional statements.
>
> **But read what they became before promoting them.** Each body is
> `inst.kvc_holds fourOneBraid` — a *one-line instantiation of a universal class
> field*. `hypVolume` and `kashaevLimit` are both undefined class fields, so the
> theorem says "an assumed function equals another assumed function at a point,
> because we assumed they agree everywhere." Tier **T1-trivial**: honest, and
> carrying no volume. The file states this itself (`:115-120`): the numeric
> values are *cited, not derived*. Two `sorry`s remain in the file
> (`pieceVolume`).

**The rest of the 2026-07-11 audit re-verified and still standing:** the three
classes are **unwired** — `AlgebraicGeometricEquivalence` does *not* take
`[VolumeConjecture]` or `[ArchimedeanLimit]` as instance hypotheses, so the
`.md`'s "downstream verifies modulo those two instances" is aspirational. And
`ArchimedeanLimit` targets `Li₂` while the alg-geom class targets `BlochWignerD`
— different functionals under different rescalings, so L5 is not a corollary of
L4.

---

## 3. The dilogarithm ladder, and the weakest link in the whole chain

`Vol(4₁) = 2·Cl₂(π/3) = 6Λ(π/3)` is a dilogarithm value, and the corpus has the
apparatus: `QOU/Infra/Clausen.lean` (sorry-free),
`Archimedean/ClausenFunctionMathlibFiller.lean`, `Archimedean/BlochWignerLobachevsky.lean`,
`Archimedean/{LobMonotonicity,LobachevskyDerivative,LobachevskyMaximum}.lean`,
`Archimedean/Orthoscheme*.lean`, `Knot/RivinConcavity.lean`,
`MathlibExt/ComplexDilogarithm*.lean`.

The `Li_2^q` vs `Φ_q` disambiguation is settled and is a **T4 definition block**
that records a *refutation*: `knots-particles-confinement/quantum-dilogarithm-disambiguation.md`
— the historical identity `Φ_q(z) = ∫₀^z ln_q(1+t)/t dt` is **false**; the
integral is the bounded `−Li₂^q(−z)`, and the two differ by ~10⁵ at `z = 0.989`.
Canonical amplitudes use `−Li₂^q(−|V|)`, never `Φ_q(|V|)`.

**Λ vs Cl₂ guard, checked and clean at the sites I read.** Every site I opened
carries the correct `Vol(4₁) = 2·Cl₂(π/3) = 6·Λ(π/3) ≈ 2.029883`. Per AGENTS.md
the *name* is wrong at ~54 sites corpus-wide while the *number* is right; I did
not sweep for it and I changed nothing.

### 🛑 THE WEAKEST LINK: the shape parameter is typed **real**, and the corpus's own theorem kills that

This is the sharpest structural finding of the sweep, and it is checkable in
three files.

1. `algebraic-geometric-dilog-equivalence.lean:44` declares
   **`opaque BlochWignerD : ℝ → ℝ`** — a black box, explicitly "until Mathlib
   provides a complete formalisation of the classical dilogarithm".
2. The class is `AlgebraicGeometricEquivalence (q x : ℝ)` with field
   `pole_cusp_matched : volume = BlochWignerD x`. The shape parameter `x` is
   **real**.
3. The genuine Bloch–Wigner function `D(z) = Im Li₂(z) + arg(1−z)·log|z|`
   **vanishes identically on ℝ** — and **the corpus proves this**, sorry-free, in
   `lean/QOU/MassTheory/BlochVolumeLegFlatVanishing.lean`:
   `eq_zero_of_conjAntisymm_ofReal` (`:111`) and
   `sum_eq_zero_of_real_shapes` (`:128`), on the mechanism `D(z̄) = −D(z)` with
   `x̄ = x`.

**So if `BlochWignerD` were ever instantiated by the real Bloch–Wigner function,
`pole_cusp_matched` would force `volume = 0` for every `x`, and the conjecture
would become the assertion that every hyperbolic volume on this route is zero.**

**Two honest caveats, because this is not yet a Lean contradiction.** (i)
`BlochWignerD` is `opaque`, so nothing is derivable from it today and no
inconsistency exists in the tree. (ii) `eq_zero_of_conjAntisymm_ofReal` is a
*generic* theorem about any conj-odd `D : ℂ → ℝ` taking antisymmetry as a
hypothesis — a different type (`ℂ → ℝ` vs `ℝ → ℝ`) in a different file, not
wired to the class. The two never meet, which is exactly why the defect survives.

**The corpus already knows the geometric half of this from both sides.**
`shared-denominator-cusp-holonomy.md:147-155` says a geometric shape requires
`Im z > 0`, "excludes real constants", and derives that `z_k` "is not real and in
particular is not the bare algebraic seed `q₀^{-k}`". The SnapPy witness reaches
it by measurement (distance 0.40–0.92). **What is missing is that the Lean class
was never re-typed to match.** `MathlibExt/IdealTriangulation.lean` already has
the right object — `IdealTetrahedron.param : Fin 3 → ℂ` with `param_im_pos`,
`param_prod = −1`, `shape_ne_zero` — sorry-free, 296 lines.

**Scope: (a).** This says the *current formalisation* cannot carry a nonzero
volume as typed. It is **not** a (b) exclusion of the route — the fix is to move
the class to `ℂ` with `Im z > 0`, which is a re-typing, not a new theorem.

---

## 4. Bring's surface — the owner's actual question

**The premise I was given ("if it does not, that is the gap worth naming") is
false: the corpus DOES use the hyperbolic structure on Bring's surface**, and it
is one of the better-proved things in the tree.

`lean/QOU/Archimedean/EmCouplingBringZeroMode.lean` (sorry-free) carries:

| declaration | line | content | tier |
|---|---:|---|---|
| `bringFundamentalTriangleArea` | 90 | `π − (π/2 + π/4 + π/5)` — the **(2,4,5) hyperbolic triangle** angle defect = `π/20` | def |
| `bringSurfaceArea` | 94 | `240 ×` that `= 12π` | def |
| `gaussBonnetArea g` | 123 | `4π(g−1)`; at `g=4` → `12π` | def |
| `bringSurfaceArea_eq_gaussBonnet` | 132 | tiling area = Gauss–Bonnet area | **T0** |
| `bringTilingEuler_eq` | 206 | `χ = 114 − 360 + 240 = −6` | **T0** |
| `bringTiling_genus_four` | 213 | `χ = 2 − 2g ⇒ g = 4` | **T0** |
| `bringTiling_b1` | 218 | `b₁ = 2 − χ = 8` | **T0** |
| `bringZeroMode_fully_tiling_derived` | 232 | `b₁ / Area = 2/(3π)`, numerator and denominator both from the tiling | **T0** |

Narrative twin: `predicted-spectra/em-coupling-bring-zero-mode.md:20` —
*"The area evaluates under constant negative curvature −1 as
`Area = −2πχ = 4π(g−1) = 12π`."* Block kind **`proposition`**.

**What tier this really is — and it is lower than it looks.** Every theorem above
is **arithmetic wearing geometric names**. `gaussBonnetArea` is a `def`, not
Gauss–Bonnet; `bringSurfaceArea_eq_gaussBonnet` is `240·(π − (π/2+π/4+π/5)) =
4π(4−1)` closed by `ring`. Three geometric facts are **assumed in docstrings and
proved nowhere**:

- **(B1)** that a hyperbolic triangle's area equals its angle defect (Gauss–Bonnet
  for `ℍ²`) — **T4**, docstring at `:88-89`;
- **(B2)** that Bring's curve is tiled by **240** such triangles — **T4**, `:195-199`;
- **(B3)** that Bring's curve carries a hyperbolic metric at all, i.e. **`B ≅ ℍ²/Γ`
  for a torsion-free Fuchsian `Γ`** — **T5, absent from the corpus entirely.**

There is **no `ℍ²`, no Möbius action, no Fuchsian group, no `Δ/Γ`** anywhere in
QOU. Confirmed: `Mathlib.Analysis.Complex.UpperHalfPlane.*` is **never imported**
by any QOU file (the only `Mathlib…Modular*` import in the tree is
`JacobiTheta.TwoVariable` in `MathlibExt/GaussianThetaSum.lean`, unrelated).
Mathlib's `ℍ²` metric is *named* in exactly two QOU files, both as prose about
what Mathlib has: `Archimedean/HyperbolicVolumeMeasure.lean:9` and
`Eightfold/HyperbolicVolumeFormType.lean:137`.

### 🛑 And the corpus HOLDS the source that proves B1–B3 — cited for a different section

`library/pjm-v154-n1-p09-s/` = **Riera & Rodríguez, "The period matrix of Bring's
curve", Pacific J. Math. 154 (1992)**, registered as `[riera-rodriguez-1992]`.
Its **§2, `sections/sec-001-2-the-universal-cover-of-brings-curve-if-b-b-is.md`,
pp. 2–8**, is exactly the missing construction, verbatim:

> "Consider the non-euclidean polygon of 20 sides in the unit disc Δ … the
> pattern of triangles with interior angles π/5, π/4, π/2. … `α⁵ = 1, β² = 1,
> (βα)⁴ = 1` as defining relations for a group `Γ* = ⟨α, β⟩`, that is, `Γ*` is a
> **(2,4,5) triangle group**, for which any pair of adjacent triangles … form a
> fundamental domain for `Γ*`, whence `Γ*` is discrete. Let `φ: Γ* → S₅` … `Γ =
> ker φ` … **`Γ` has no torsion** … the genus of **`B = Δ/Γ` is 4** and `S₅` acts
> on it as a group of automorphisms."

That paragraph supplies **B3** (`B = Δ/Γ`, Γ torsion-free Fuchsian — the
uniformisation), **B2** (index `[Γ*:Γ] = |S₅| = 120`, two triangles per Γ*
fundamental domain ⇒ **240** triangles — precisely the corpus's
`bringTilingFaces := 240`, currently an unsourced integer literal), and the
(2,4,5) datum the Lean uses without citation.

**The corpus cites this paper — for its period matrix.** `references.ts:9012-9037`
registers it for `Z = τ₀·C` and the `Jac ~ E⁴` isogeny; bean `qou-3q4q` cites its
Lemma 1 (p. 184) at `BringHauptmodulGate.lean`. **§2 is not cited anywhere.**
`EmCouplingBringZeroMode.lean` carries `-- Ref:` for `suslin1991`, `bloch2000`,
`thurston1978`, `manuscript` — **and none for the (2,4,5) triangle or the 240**.

**Duplicate warning (memory TRAP).** Riera–Rodríguez is held **twice**:
`library/pjm-v154-n1-p09-s/` and
`library/the-period-matrix-of-bring-s-curve-1hik02mwva/` (whose sections carry
`duplicate_of: "pjm-v154-n1-p09-s"`). **One work, not two sources** — and the
pair is **not listed in `docs/audits/library-duplicate-ledger.json`**, so the
ledger under-counts here.

### What is genuinely open on the Bring leg

**Nothing in the corpus connects Bring's `ℍ²` to the knot complements' `H³`.**
The 12π area is a *2-dimensional* hyperbolic quantity feeding `1/α_EM`; every
other hyperbolic object in the corpus is *3-dimensional* (knot complements). No
block, no Lean file and **no bean** relates them. `.beans/` returns **0** for
`Gauss-Bonnet`, `triangle group`, `(2,4,5)`, `systole`, `uniformis` — no agent has
ever worked this. **That is the genuinely-open item across all six paths.**

**Scope: (a) on the search, not (b).** Path 0 was down and my greps are lexical.
I measured `content/`, `docs/`, `computations/`, `.beans/`, and `library/` on 40+
spellings; I did not search PR bodies, `uploads/`, or sibling branches.

---

## 5. The held literature that would build this route

Cited by `library/<doc-id>`, all present on disk with greppable sections.

**Bring's surface (four documents; three distinct works + one duplicate):**

| doc-id | work | what it supplies |
|---|---|---|
| `pjm-v154-n1-p09-s` | Riera–Rodríguez 1992, *The period matrix of Bring's curve* | **§2 the uniformisation `B = Δ/Γ`, (2,4,5) triangle group, `Γ = ker(Γ*→S₅)` torsion-free.** The single most load-bearing uncited section in this audit. |
| `the-period-matrix-of-bring-s-curve-1hik02mwva` | *duplicate of the above* | — |
| `s40879-023-00706-0` | Braden–Disney-Hogg 2022, *Bring's curve: old and new* | §2.1–2.3 basic properties, period matrix, `Aut = S₅`; §3.1 Weierstrass points; §3.2 vertices and face centres; §4 quotients by subgroups |
| `sigma12-065` | Braden–Northover 2012, *Bring's Curve: its Period Matrix and the VRC* | Hulek–Craig sextic, real structure / anti-holomorphic involution |
| `arxiv-2402.08782v1` | *Hecke–Farey coordinates for Bring's surface* | Bring via the **Hecke group `H₃` = modular group Γ**; congruence subgroups; universal q-gonal maps. A second, independent Fuchsian route. |

**Volume conjecture / Kashaev:** `arxiv-q-alg-9601025v2` (Kashaev 1997, *The
hyperbolic volume of knots from the quantum dilogarithm* — the origin),
`arxiv-q-alg-9504020v1`, `0803219` (*Introduction to the volume conjecture*),
`arxiv-1002.0126v1`, `arxiv-1003.4808v2`, `arxiv-1203.2182v1`,
`arxiv-math-0603217v3`, `arxiv-math-0611181v2` (*proof for Whitehead chains* — a
**proved** family), `arxiv-2604.16077v1` (**figure-eight complement**, the
semi-classical limit — directly the `4₁` case QOU needs),
`104171-qt-83` + `ki6c` (Ohtsuki asymptotics, `5₂` and 6-crossing).

**Gluing equations / Neumann–Zagier / Bloch group:** `arxiv-1202.6268v2`
(*The quantum content of the gluing equations*), `arxiv-2109.00379v1` (*Twisted
Neumann–Zagier matrices*), `arxiv-2304.12545v1` (**Garoufalidis–Zagier,
*Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann*** — the
survey that ties the whole route together), `0307092v2` (*Extended Bloch group
and the Cheeger–Chern–Simons class*), `arxiv-1207.6711v1` (PGL(n,ℂ) gluing
equations), `arxiv-1507.03238v3` (Ptolemy varieties), `cspaper`,
`topologicalinvariance3dindex`, `arxiv-math-0604094v1` (*the NZ potential as a
classical limit of a quantum invariant*), `arxiv-math-0604057v2` (volume
conjecture via the Beilinson–Deligne **regulator**).

**Dilogarithm / hyperbolic geometry background:** `zagier-the-dilogarithm-function`
(has a section *"The Bloch–Wigner function D(z) and…"* — the canonical source for
the `D` this corpus needs), `thurston` (*The Geometry and Topology of
Three-Manifolds*, 22 sections), `angled-survey` (*From angled triangulations to
hyperbolic structures* — Casson–Rivin, i.e. the concavity machinery `qou-idvt`
wants), `milnor-1982-hyperbolic-geometry-the-first-150-years`, `ihpmay2025`,
`nrarith` (Neumann–Reid, arithmetic `M = H³/Γ`), `arxiv-1010.5321v3` (*Formulas on
hyperbolic volume*), `arxiv-hep-th-9408113v2` (*Dilogarithm identities*),
`arxiv-2506.10206v2` (*Analytic dilogarithm identities*).

**For the formalisation question specifically:** `poincare-proof-outline`,
*"Formalization of the Poincaré disc model of hyperbolic geometry"* — a
formalisation paper on exactly the `ℍ²` model the Bring leg needs. Not cited
anywhere in `content/`.

---

## 6. The smallest honest Lean statement on this route

Mathlib status, re-confirmed against bean `qou-mlbg`'s survey of 6,996 Mathlib
files at the pinned rev: `Bloch` **0**, `Borel regulator` **0**, `Polylog` **0**,
`Rogers` **0**, `Steinberg` **0**, no `KTheory` directory; `dilog` **1** and it is
a docstring aside; `Clausen`/`Lobachevsky` **3**, all false positives (the
surname *Claus Clausen*, and *Clausen–Scholze*). **Mathlib has `ℍ²` and the
modular machinery; it has no dilogarithm.**

Assessing the three candidates I was asked to weigh, plus one I would put ahead
of them:

**(i) Gauss–Bonnet area for a genus-`g` surface as arithmetic — ALREADY DONE, and
doing it again is the trap.** `bringSurfaceArea_eq_gaussBonnet`,
`bringTilingEuler_eq`, `bringZeroMode_fully_tiling_derived` are all sorry-free
today. Re-deriving them adds nothing. The *arithmetic* is closed; **B1/B2/B3 are
what is missing, and none of them is arithmetic.**

**(ii) The ideal-tetrahedron volume `D(z)` as a definition — reachable, and
largely built.** `MathlibExt/IdealTriangulation.lean` is sorry-free (296 lines)
with `IdealTetrahedron`, `angle_sum = π`, `volume_eq_lob_sum`, `volume_eq_dilog`,
`law_of_sines`, `param_im_pos`, `param_prod = −1`. `QOU/Infra/Clausen.lean` is
sorry-free. Remaining sorries are in the *analysis*: `LobMonotonicity` 1,
`IdealTetrahedronVolumeConcave` 1, `RivinConcavity` 1, `MultiTetVolumeConcave` 3,
`ClausenFunctionMathlibFiller` 2, `BlochWignerLobachevsky` 2. Bean `qou-idvt`
(in-progress, high) already scopes this as **T1** Lobachevsky Λ → **T2**
`Vol = Λ(α)+Λ(β)+Λ(γ)` → **T3 concavity** → **T4** regular triple maximises, and
correctly notes T3 "is a real-analysis statement, not a geometry one". **That
bean is live and roughly current — do not re-scope it.**

**(iii) The gluing-equation shape as a `Prop` — reachable and cheap.**
`SatisfiesEdgeEquations` / `SatisfiesAngleEquations` already exist in
`IdealTriangulation.lean:279,284`. Stating `∏ z_k^{a} (1−z_k)^{b} = 1` over `ℂˣ`
needs no manifold theory.

**(iv) — and this is the one I would actually recommend, because it is the
weakest link rather than the nearest lemma. Re-type the alg-geom class's shape
parameter from `ℝ` to `{z : ℂ // 0 < z.im}`.** Concretely: change
`class AlgebraicGeometricEquivalence (q x : ℝ)` and
`opaque BlochWignerD : ℝ → ℝ` so the matched shape is complex with positive
imaginary part, reusing `IdealTetrahedron.param`, which already carries exactly
that constraint sorry-free. This costs no new mathematics — it is a signature
change — and it is what makes the class capable of ever carrying a nonzero
volume. Until it is done, §3's defect stands: as typed, the honest instantiation
of `BlochWignerD` forces `volume = 0` by the corpus's own
`eq_zero_of_conjAntisymm_ofReal`.

**Not reachable without absent API:** anything requiring `ℍ²/Γ` as a *manifold*
(B3), Mostow rigidity, Thurston hyperbolisation, the Bloch group, or the Borel
regulator. `Archimedean/HyperbolicQuotient.lean` is explicit and correct about
this: it proves quotient-volume *well-definedness* for a rank-1 horizontal
translation group and states plainly that "Mostow rigidity and Thurston
hyperbolisation are untouched, and nothing here is a step toward either", and
that its lattice is rank 1 so "`H³/ℤ` is NOT a cusp".

---

## 7. Verdict

**Partially covered — and far more covered than my retracted claim allowed.**

- The **route exists in the corpus and is stated outright**, but its top-level
  statement (`brings-surface/thurston-relaxation.md:7-11`, *"the same algebraic-
  residue data feeds both the SDP and the gluing solver; they are different
  evaluations of one categorical object"*) is a **`prose` block — T4**. It cites
  `conj:algebraic-geometric-dilog-equivalence`(1) for its load-bearing claim. It
  is a research programme written down, not a result.
- **L1 is T0.** **L2, L3, L5 are T3**, class-carried with no instance — correctly
  and deliberately. **L4 is T1+T2.**
- **The volume conjecture for `4₁` is T2-CONFIRMED** at 2.93e-4 — the strongest
  evidence that this route is real.
- **Bring's surface already has its hyperbolic structure used**, at T0 for the
  arithmetic and **T4/T5 for the three geometric facts (B1, B2, B3)** underneath
  it, with **B3 absent from the corpus and present in a held, registered,
  differently-cited source.**
- **The `ℍ² ↔ H³` link is genuinely open on all six paths** (path 0 uncovered).

### What would close the weakest link

Two moves, in order, neither of which is research:

1. **Re-type the shape parameter to `ℂ` with `Im z > 0`** (§6(iv)). Without it,
   the alg-geom class cannot carry a nonzero volume, and the corpus already
   proves why in a file that is not wired to it. Also **rename
   `pole_cusp_bijection_proved`** to say what it proves (`qPochDenom_roots_explicit`
   or similar) — the current name is the sort of thing that gets cited as
   evidence for L2.
2. **Cite `library/pjm-v154-n1-p09-s` §2 at `EmCouplingBringZeroMode.lean`**, which
   converts B2 (the bare integer `240`) and B3 (`B = Δ/Γ`) from unsourced
   assumptions into cited literature — the honest tier for an imported classical
   fact, and the difference between *deriving* and *re-deriving*.

Neither is a proof of the volume conjecture, and neither should be described as
one.

## Cross-references

- Chain: [`algebraic-geometric-dilog-equivalence.md`](../../content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.md) ·
  [`shared-denominator-cusp-holonomy.md`](../../content/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md) ·
  [`kashaev-volume-conjecture.md`](../../content/quantum-observable-universe/mass-theory/kashaev-volume-conjecture.md) ·
  [`thurston-relaxation.md`](../../content/quantum-observable-universe/brings-surface/thurston-relaxation.md)
- Bring: [`em-coupling-bring-zero-mode.md`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md)
- Prior audits: [`2026-07-11-algebraic-geometric-dilog-provability.md`](2026-07-11-algebraic-geometric-dilog-provability.md) (one claim now stale, §2 above) ·
  [`2026-06-16-hyperbolic-hurdle-dialog-assessment.md`](2026-06-16-hyperbolic-hurdle-dialog-assessment.md)
- Beans: `qou-idvt` (ideal-tetrahedron Mathlib gap, in-progress) · `qou-mlbg`
  (Bloch/Borel Mathlib survey) · `qou-hq3m` (quotient volume) · `qou-3q4q`
  (Riera–Rodríguez locator) · `qou-xlw1` (this sweep)
