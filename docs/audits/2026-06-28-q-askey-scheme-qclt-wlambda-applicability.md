# q-Askey scheme applicability to GAP 3 (q-CLT) and GAP 5 (W_λ / WRT(Σ(2,3,5)))

**Date:** 2026-06-28
**Branch:** `claude/q-askey-scheme-gaps-wubsmv`
**Scope:** Assessment audit. Where can the q-Askey scheme of basic
hypergeometric orthogonal polynomials (Askey–Wilson at the top, descending
through q-Racah, big/little q-Jacobi, Al-Salam–Chihara, continuous/discrete
q-Hermite, Rogers–Szegő, q-Laguerre, Stieltjes–Wigert, Hahn–Exton/Jackson
q-Bessel) be used in QOU, and does it help close the q-CLT and W_λ gaps?
**Verdict in one line:** the scheme is a genuine **unifying lens** and supplies
one **named-theorem substitute** (Féray–Méliot q-Plancherel CLT) plus one
**confluent-limit identification** (Hahn–Exton q-Bessel for the WRT route), but
it **closes neither gap by itself**, and its most seductive member — the
Bożejko–Speicher q-Gaussian / continuous q-Hermite as a *real measure* — is
**already proved obstructed at the substrate** `q₀ > 1`.

---

> **Coordination (2026-06-28).** A sibling landed the same core placement on
> `main` (`10365a4362`, `feat(qaskey/frakV)`): `W_λ = d_q²/D²` is the
> Plancherel measure of the q-Hermite/Rogers–Szegő family, binding `= q-Hermite
> moments`, arena `= Hahn–Exton q-Bessel (E_q(2))`, bridge `=` three-term
> recurrence/orthogonality (not a product GF) — **fully consistent** with §1–§3
> here, plus a richer `𝔙 = Re(binding)+i·Im(Q_β)` cosh/sinh synthesis and a
> product-form refutation (a). This audit is the *assessment* complement: the
> **GAP-3 BS-obstruction + Féray–Méliot CLT framing** (§1), the **GAP-3 ≡ GAP-5
> measure identity** (§2), and the **compute lever** (§6) are the additive parts;
> the bare "W_λ = q-Plancherel measure / q-Bessel arena" placement is now also
> on `main`. The brings-surface Klein bridge (`conj:klein-bring-icosahedral-bridge`)
> is independent of both.

## 0. Why this audit (and a self-correction)

A chat assessment on this branch initially flagged "q-CLT ↔ continuous
q-Hermite" as the *cleanest* closure lever among the q-Askey applications. The
corpus-grep checklist (AGENTS.md §"Before declaring open") immediately
falsified the clean-win framing: QOU **already proves** that the
Bożejko–Speicher q-Gaussian does not exist as a probability measure at the
substrate value, with continuous q-Hermite as its orthogonal-polynomial system.
This audit records the corrected, corpus-grounded picture so the next agent
does not re-pitch the obstructed path.

Corpus-grep paths walked (all four, per the STRICT checklist):

- `docs/audits/`, `docs/coordination/` — keystone ledger
  [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md), CFS ledger
  [`cfs-q-clt.md`](../coordination/cfs-q-clt.md).
- `content/` — the q-Gaussian obstruction, q-Plancherel skeleton, non-commutative
  probability dictionary, Rogers–Szegő / q-Bessel / q-Lommel Lean (see §4).
- `computations/` — `lever1_*` formalize-first probes, q-Plancherel CLT typeclass.

---

## 1. GAP 3 (q-CLT) — the BS q-Gaussian is obstructed; the convergent limit is q-Plancherel

### 1.1 The obstruction (already in corpus, (b) structural exclusion with proved invariant)

[`prop:q-gaussian-obstruction-at-q0`](../../content/quantum-observable-universe/mass-theory/q-gaussian-obstruction-at-q0.md)
proves: at `q₀ ≈ 1.10998 > 1` the Bożejko–Speicher non-commutative q-Gaussian
**does not exist** as a probability measure. The would-be even moments
`T_n(q₀) = Σ_{π∈P₂(2n)} q₀^{cr(π)}` diverge super-exponentially
(`T_n ≥ q₀^{C(n,2)} = exp(Θ(n²))`), and by Bożejko–Speicher the q-deformed
commutation relations admit a positive Fock representation **iff** `−1 ≤ q ≤ 1`
— at `q₀ > 1` the Gram form fails PSD.

This is a legitimate **(b) structural exclusion** in the sense of the STRICT
"refuted" rule: the proved invariant is *Fock/Gram positive-semidefiniteness*,
which `|q| > 1` provably violates (Bożejko–Speicher `[bozejko-speicher1991]`).
The continuous q-Hermite polynomials are the orthogonal system of exactly this
(non-existent at q₀) measure. So:

> **The continuous q-Hermite / Al-Salam–Chihara family is a *fibre-level*
> object, not an archimedean attractor.** Its natural home is `|q| ≤ 1` (or
> formal q), reached from the substrate growth regime only via the bar
> involution `q ↦ q⁻¹` (`q₀ ↔ 1/q₀ ≈ 0.901`, inside the disk). This is the
> recurring fibre-vs-archimedean wall (AGENTS.md §"Im(q) at fibre vs observable
> level"), biting again.

This is consistent with — and explains — where the corpus *does* use continuous
q-Hermite successfully: at the fibre level. The binding period
`a_D^(n) = (1/n)Σ_{λ⊢n} dim_q(λ)` is identified as a **q-Hermite moment**
([`docs/audits/2026-06-26-binding-period-qinvolution-qhermite-identification.md`](2026-06-26-binding-period-qinvolution-qhermite-identification.md)),
and the Rogers–Szegő binding-kernel oscillator (`BindingQHermiteOscillator.lean`,
PR #2800) lives in the same formal-q world. None of these claim a real q-Gaussian
*probability law* at q₀ — and they must not.

### 1.2 The convergent substitute (also already in corpus)

The obstruction's own *Consequence* names the convergent replacements for braid
fluctuation statistics at q₀:

1. the **inner** Perron–Frobenius dominant eigenvalue (a deterministic
   law-of-large-numbers limit), and
2. the **outer Féray–Méliot q-Plancherel CLT** (a genuine Gaussian-fluctuation
   limit on the partition chain) — already carried as the Lean typeclass
   `HasQPlancherelCLT`
   ([`QPlancherel.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean)),
   with the variance bound `O(1/√(n−3))` established by Féray–Méliot
   `[feray2010]` (see
   [`prop:q-plancherel-asymptotic-skeleton`](../../content/quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md)).

**q-Askey contribution to GAP 3:** the scheme tells you *which* orthogonal
system governs the convergent limit — not continuous q-Hermite (the obstructed
braid-generator law) but the **q-Plancherel / Thoma-simplex** family on the
partition chain `λ ⊢ n`. The actionable, honest move is therefore **not** a new
probe but a framing fix: any content block or conjecture class that invokes "a
q-Gaussian limit" for braid observables *at q₀* is mis-applying `|q| ≤ 1`
Bożejko–Speicher theory and should cite the proved obstruction + the
q-Plancherel CLT instead.

---

## 2. GAP 3 ≡ GAP 5 through the q-Plancherel measure (the load-bearing finding)

The q-Plancherel skeleton's weight is

$$
  \tilde w_\lambda^{(n)} \;=\; \frac{\dim_q^2(\lambda)}{[n]_q!}.
$$

This is **literally the keystone target** `W_λ = d_q(λ)²/[n]_q!`
([`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)). Therefore:

> **The GAP-3 convergent limit law (the measure of the Féray–Méliot
> q-Plancherel CLT) and the GAP-5 index target `W_λ` are the *same* measure.**

This is the single most useful structural consequence of viewing the two gaps
through the q-Askey lens. Two corollaries:

- **The heat-kernel defect ladder is a Plancherel-moment expansion.** The
  keystone's falsifiable `q₀`-free targets — the defect cubic
  `144·C(n) = −n(n−1)(2n−13)`, the sub-leading `D(n)`, and the general
  `c_{2k}(n)` of degree `3k` with denominator `m_k·144^k` (keystone ledger
  2026-06-24, #2744) — are, in Askey-scheme language, the
  **moments / Kerov-polynomial expansion of the q-Plancherel measure**. The
  ledger already notes this is "expected from Plancherel-moment / Kerov-polynomial
  theory"; the q-Askey framing makes it the *organizing principle* rather than an
  observed coincidence.
- **Identity I is the second moment.** `M(n) = n(3n−1)/2` is the Plancherel
  content-square mean (the keystone's one carried representation-theoretic input,
  now Lean-proved unconditional for `n = 3..12`, #2760; (A)-half all-`n`, #2655).
  In the moment-problem framing it is the second moment of `W_λ` under the
  content statistic — the natural first nontrivial datum an orthogonal-polynomial
  treatment computes.

This linkage costs nothing to assert (both objects are already in the corpus)
and it is the right way to *unify* the q-CLT and W_λ workstreams: progress on the
q-Plancherel CLT's limit-measure identification (skeleton clauses 3a/3b) is
progress on the W_λ index, and vice versa.

---

## 3. GAP 5 (W_λ / WRT) — Hahn–Exton q-Bessel is the Askey-scheme confluent bottom

The keystone's *current* arena (2026-06-22 reframe, bean `s5bb`) is the
non-compact `SU_q(2) → E_q(2)` contraction, whose matrix coefficients are
**Hahn–Exton q-Bessel functions**, with the sharpened open object the colored
`Σ(2,3,5)` WRT / Lawrence–Zagier q-series reached via the bar involution.

In q-Askey terms this is precise and scheme-sanctioned:

- The **q-Bessel functions sit at the confluent bottom of the q-Askey scheme**
  (the q-analogue of the Bessel functions reached as confluent limits of
  Jacobi-type polynomials). The classical **İnönü–Wigner contraction**
  `SU(2) → E(2)` sends Jacobi polynomials (SU(2) matrix coefficients) to Bessel
  functions (E(2) matrix coefficients); its q-deformation
  `SU_q(2) → E_q(2)` sends the q-Krawtchouk/q-Jacobi level to **Hahn–Exton
  q-Bessel** — exactly the named arena. So the keystone's "non-compact arena" is
  not an ad-hoc move; it is the **standard Askey-scheme degeneration** of the
  compact `SU_q(2)` representation theory the framework already uses.
- Consequently the q-Askey scheme supplies three concrete services to the W_λ
  build, *without* re-opening the owner-gated geometric core:
  1. the **moment-problem framing** for Identity I and the defect ladder (§2);
  2. the **q-Bessel realization** of the WRT(Σ(2,3,5)) q-series as a
     scheme-recognized confluent limit (rather than a bespoke special function);
  3. the **orthogonality measure** (`W_λ` = q-Plancherel) that any candidate
     index must reproduce — i.e. the C1 normalization question (`Σ W_λ = 1` true
     Plancherel `d_q²/D²` vs the `[n]_q!`-normalized `0.98222`) is an
     orthogonal-measure normalization, which the Askey-scheme/Plancherel
     literature handles canonically.

### 3.1 What the q-Askey scheme does NOT supply (scope guards)

Two (b)-type guards, both already proved/recorded in the corpus — restated here
so the lens is not over-sold:

- **It does not supply the geometric index.** The hard core **G1** — the
  Beasley–Witten Seifert–Chern–Simons equivariant-index construction on `S³/2I`
  (live in #2524) — is research-level differential geometry. Identifying the
  arena as Askey-scheme q-Bessel constrains *what the index must equal*; it does
  not build the index. (G1 is owner-**authorized** per the 2026-06-19 narrow
  reversal, not owner-gated; the blocker is DG, not permission.)
- **It does not bridge the Schur–Weyl duality.** The 2026-06-22 capstone
  (`fe3a83d6b4`) records that `WRT ↔ W_λ` is a Schur–Weyl **duality, not an
  equality**: corpus `W_λ` is the `S_n`-side hook-content `d_q(λ)`, while
  WRT/Poincaré modular data is the `SU(2)`-side `[2j+1]_q`; they differ off the
  `(4,1)` coincidence. A direct `WRT = W_λ` identification is a category error.
  The q-Askey lens *respects* this — q-Bessel realizes the `E_q(2)` (geometric /
  `V_λ`) side; the q-Plancherel measure is the `S_n` side — and must not be used
  to paper the duality into an equality. The bare `Σ(2,3,5)` Lawrence–Zagier
  number `Ψ(1/q₀) = 2.32958` remains one scalar vs a λ-family (the numerology
  trap the discipline forbids).

---

## 4. Inventory — q-Askey members already load-bearing in QOU

For completeness (and to show the framework already lives in the scheme's
confluent rows):

| q-Askey node | QOU site | Level | Role |
|---|---|---|---|
| continuous q-Hermite / Rogers–Szegő | `BindingQHermiteOscillator.lean`, `RogersSzegoInhabited.lean`, `QStandardRogersSzego.lean` | fibre | binding-kernel basis; `a_D^(n)` = q-Hermite moment |
| Hahn–Exton / Jackson q-Bessel | `QBesselContiguityRecurrence.lean`, `BindingQBesselKernel.lean` (bean `z2bn`); `2026-06-13-reeb-phase-qbessel-identification.md` | fibre | Layer-2 binding kernel; **E_q(2) arena for W_λ** |
| q-Lommel | `QLommelOrderRecurrence.lean` | fibre | deterministic Δ_λ ladder from D,T seeds |
| q-Plancherel (Thoma simplex) | `QPlancherel.lean` (`HasQPlancherelCLT`); `q-plancherel-asymptotic-skeleton.md` | archimedean (partition chain) | **the convergent q-CLT = the W_λ measure** |
| q-Pochhammer `(q;q)_n` | `QPochhammer.lean` | both | building block |

Standard scheme references for citation when this lands in content blocks:
Koekoek–Lesky–Swarttouw (q-Askey scheme catalogue) and Gasper–Rahman (basic
hypergeometric series); the contraction `SU_q(2) → E_q(2)` → Hahn–Exton q-Bessel
is Vaksman–Korogodsky / Koornwinder. (No reference key is added in this audit;
add via the `ref()` builder in `content/schema/references.ts` if/when a content
block cites them.)

---

## 5. Recommendations (no new wide probe; consolidation + one framing fix)

Per the formalize-first discipline, the corpus-grep result *narrows* the work to
framing/consolidation, not a numerical search:

1. **Framing fix (cheap, high-value).** Anywhere a block or conjecture class
   invokes "a q-Gaussian limit" for braid observables at q₀, cite
   [`prop:q-gaussian-obstruction-at-q0`](../../content/quantum-observable-universe/mass-theory/q-gaussian-obstruction-at-q0.md)
   + the Féray–Méliot q-Plancherel CLT (`HasQPlancherelCLT`) instead. The
   continuous-q-Hermite usage stays, but explicitly tagged **fibre-level**
   (`|q| ≤ 1` / bar involution), never as an archimedean probability law.
2. **Record the GAP-3 ≡ GAP-5 measure identity (§2)** as a cross-link in both
   the CFS ledger and the keystone ledger: the q-Plancherel CLT measure *is*
   `W_λ`; the defect ladder is its Kerov/Plancherel-moment expansion; Identity I
   is its second moment. This unifies two workstreams that are currently tracked
   separately.
3. **Optional, owner-gated:** frame the WRT(Σ(2,3,5)) sharpened object explicitly
   as a q-Askey confluent (Hahn–Exton q-Bessel) limit in the geometric-W_λ
   tranche — a presentational upgrade to #2524's spec, not new mathematics.

**Net:** the q-Askey scheme helps by *organizing* and by *replacing a bespoke
conjecture with a named theorem* (Féray–Méliot), and it correctly *predicts* the
keystone's non-compact `E_q(2)`/q-Bessel arena as a standard scheme
degeneration. It does **not** close GAP 3 or GAP 5; the BS q-Gaussian form is
proved-obstructed at q₀, and the W_λ closure remains the (authorized, research-DG)
geometric index plus the Schur–Weyl duality guard.

## 6. Can any of this improve compute? (assessment — one real lever, one speculative)

Sober answer: the findings are mostly geometric/structural, but there is **one
genuine compute lever** and **one speculative** one. Neither is implemented here
(no compute env in this sandbox; route any implementation through
`local/compute-author`).

> **Done (2026-06-28):** the lever's first rung is realized — `C(n)` is now
> **derived analytically** from Identity I via the Plancherel-moment route
> (`scripts/keystone_wlambda_defect_kerov_derivation.py`, exact `n=2..12`),
> closing the keystone's deferred "C(n) derivation from the defect ... not yet
> symbolic" item. From `log W_λ = log(dim²/n!) + (η²/6)[Σ_k(k²−1) −
> 2Σ_c(h_c²−1)] + …` and `Σ_λ w_λ = 1`, the `h²` coefficient of `1−Z(n)` is
> `−(1/4)·(1/6)[Σ_k(k²−1) − 2(M(n)−n)]` with `M(n)=n(3n−1)/2` (Identity I),
> giving `C(n) = −n(n−1)(2n−13)/144` with no Taylor extraction or fit. Higher
> rungs `c_{2k}(n)` follow from the next log-sinh coefficients × higher
> Plancherel hook-power-sum moments.

- **Lever (real, modest): Kerov-polynomial / free-cumulant recursion for the
  `W_λ` defect ladder.** Since `W_λ = dim_q²/[n]_q!` is the q-Plancherel measure
  (§2), the defect coefficients `c_{2k}(n)` — the degree-`3k` polynomials the
  keystone currently obtains by per-order Richardson/Taylor extraction
  ([keystone ledger #2744](../coordination/s5-so3-keystone.md)) — *are* its
  Plancherel/Kerov moments. They can be generated from the **Kerov-polynomial /
  free-cumulant recursion** (one recursion → all orders + a closed form) instead
  of extracting each order numerically. The ledger already notes the ladder is
  "expected from Plancherel-moment / Kerov-polynomial theory"; this is
  *implementing* that observation. Producer to touch:
  `keystone_wlambda_defect_coeff_ladder.py`.

- **Speculative (needs checking): icosahedral `A₅`-orbit reduction.** The
  `A₅` symmetry constructed here lives at the **base / ℙ(V) (n=2)** level, with
  orbits `{12,20,30}`. A compute that genuinely carried this symmetry could fold
  ~`60×`. But the load-bearing `W_λ`/`tr_M` compute is over **partitions `λ`**,
  where the exploitable symmetry is `W_λ = W_{λ'}` (conjugation, already used) —
  **not** the base-level `A₅`. So the orbit reduction does **not** obviously
  apply to the partition compute; it would only help a base-level (`ℙ(V)`)
  computation if one exists. Flag, do not assume.

The exact Klein forms / syzygy (`klein_syzygy`) are symbolic identities — no
runtime relevance beyond replacing numerical icosahedral root-finding with exact
polynomial evaluation (negligible).
