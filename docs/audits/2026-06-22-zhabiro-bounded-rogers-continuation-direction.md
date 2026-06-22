# z-Habiro continuation — the bounded direction is the Rogers/real-q face

**Date:** 2026-06-22
**Branch:** `claude/adoring-meitner-aoufwb`
**Status:** direction-setting (formalize-first). Opens the replacement for the
**refuted** Φ_q-at-`|V̂_i|` production wire.
**Thesis (one line):** the bounded z-Habiro continuation is **not a new fitted
object** — it is the **Rogers `−Li₂^q` (real-q) archimedean saddle** of the
*same* quantum-dilogarithm whose root-of-unity saddle is the (unbounded)
Faddeev `Φ_q`. The open problem is therefore a **Faddeev → Rogers
saddle-identity at the brane-tower level**, to be *proved* (formalize-first),
not searched.

---

## 1. What is closed (do not reopen)

The "route per-generator `Φ_q(|V̂_i|)` through the canonical mass table" line is
**refuted**, recorded in
[`2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md`](2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md):

- physical `z_i = |V̂_i^full|` is pinned at **0.59–0.99** (not the
  representative `ℏ_q² ≈ 0.0098`);
- there `Φ_q` is convergent-but-**enormous** (`Φ_q(0.989) ≈ 6.7×10⁵`), giving
  the **−737 MeV** mirror-nucleus isospin pathology when summed into the tower
  (`zhabiro-physical-z-pin.witness.json`, `brane-tower-isospin-diagnosis`);
- the only finite-`Φ_q` rescue — an `n⋆` truncation level — is **refuted across
  all six probed families**
  ([`2026-06-17-refuted-ansatz-lemmas.md`](2026-06-17-refuted-ansatz-lemmas.md);
  `brane-tower-z-habiro.lean :: nStar_all_probed_forms_refuted`).

The merged Lean (`QOU.MassEndomorphism.ZHabiroCauchy`, PR #2447) and its
numeric bridge (PR #2460, certified again by
`zhabiro_phiq_production_crosscheck.py`) survive as the **algebraic
Cauchy-limit checkpoint only** — they correctly identify the `Φ_q` *utility*
with the Lean `eulerCoeff` series (Euler's identity), but that says nothing
about which archimedean evaluation belongs in the mass tower.

**Do not** propose a 7th `n⋆` ansatz, re-route `Φ_q`, or introduce a CAL-4
(the three-calibration discipline review will catch it).

## 2. The reframe — two saddles of one object; the substrate is real-q

The corpus already contains the structural key, in
[`phi-q-aj-machinery-identification.md`](../../content/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md)
(conditional proposition, §3b-cond):

> `Φ_q` (Faddeev) and `Li₂^q` (Rogers) are the **same algebraic object** — the
> AJ quantum A-polynomial `Â_K` (`[garoufalidis2004]`) — viewed through
> **different archimedean saddles**:
> - `Φ_q` = saddle at `q = e^{2πi/N}` (**root-of-unity** asymptotic, `[faddeev1994]`, `[kashaev1997]`);
> - `Li₂^q` = saddle at **real** `q ∈ (0,1)` (real asymptotic via Stokes),
>
> related by the modular S-transform `q ↔ q̃` (`conj:modular-s-transform-q-q-tilde`).

This collides directly with the substrate-layer constraint recorded in
`AGENTS.md` (*"Im(q) at fibre vs observable level"*): **at the observable /
archimedean level `Im(q₀) = 0`** — the MeV evaluation requires *real* `q₀`
(`lusztig_q_0_imaginary_part_zero`). The mass tower is an observable-level
evaluation at real `q₀ ≈ 1.11`.

> **Diagnosis.** Wiring `Φ_q` (the *root-of-unity* saddle) into a *real-q*
> observable evaluation was a **category error** — the wrong archimedean face.
> The production tower already uses the **Rogers `−Li₂^q`** form, which is
> precisely the **real-q saddle** of the same object, and is bounded
> (`O(1)` at the physical `z_i`; see the verdict-audit table). The bounded
> continuation is not missing — it is **already in production**; what is
> missing is the *proof* that `li2q` is the correct archimedean image of the
> merged `ZHabiroCauchy` limit.

This also explains the `Φ_q/Li₂^q` "context-sorting" the canonical cheat-sheet
currently does *pragmatically*: it is not a convention choice, it is a choice
of archimedean saddle, forced by `Im(q₀)=0` at the observable level.

## 3. Hypothesis class + the invariant (formalize-first)

Following the **formalize-first** discipline (narrow the class before any
scan):

1. **Hypothesis class.** Bounded z-Habiro corrections
   `C(z) = Σ_{n≥0} γ_n(q) · (z; q^{-1})_n`, the **cyclotomic / Habiro-ring**
   side (`[habiro2004cyclotomic]`, `def:habiro-ring`) — the q-Pochhammer
   building blocks `(z;q^{-1})_n = ∏_{k=0}^{n-1}(1 − z q^{-k})` are
   `≤ 1` in magnitude on `0<z<1<q`, the **opposite** behaviour to the
   reciprocal-Pochhammer `Φ_q` that blows up.
2. **The invariant the whole class must satisfy.**
   - **(I-bound)** bounded as `z → 1⁻` at real `q > 1` — this is the precise
     property that kills `Φ_q` and is *already a Lean lemma* on the Rogers
     side: `QRogersPentagonArchimedean.rogersAlpha_bounded_under_convergence`.
   - **(I-bar)** bar-symmetry `q ↔ q^{-1}` (the mass tower is bar-even); the
     Rogers `α/β` pair already carries this
     (`rogersAlpha_beta_symmetry`, `rogersLogCorrection_symmetric`).
   - **(I-Cauchy)** must reproduce the *algebraic* Cauchy data the merged
     `eulerCoeff` limit fixes (the part PR #2447/#2460 certified) — **in the
     regular-representation (`full`) channel**, which the open channel audit
     **#2481** argues is the *forced* mass-tower argument (trace of the
     left-mult endomorphism `L_{α_ϱ}`, hence the Wedderburn `w_λ`).

   **Channel caveat (do not skip).** (I-bound) holds for the `full` channel
   (`z_i < 1`). The *genuine* Jones–Markov per-generator arg is the `std`
   channel `Vol_q^({i})`, which is `> q₀` (proton σ₀ ≈ 1.146) — there **even
   `li2q` diverges** (#2481 finding 2). So the bounded-continuation programme is
   conditional on `full` (regular-rep) being the correct tower argument, and the
   `tr_M`-vs-`tr_reg` descended-term conflation (~10%) + the classical-vs-q
   weight convention (#2481 findings 3–4) are **part of the Cauchy data the
   Rogers-saddle lemma (§4) must reproduce — and must be reconciled first.**
3. **Let the invariant narrow the probe.** `−Li₂^q(−z)` satisfies
   (I-bound)+(I-bar) by the already-proved Rogers lemmas. So the *only* open
   numerical question is **(I-Cauchy): is `−Li₂^q(−z)` the exact real-q saddle
   of the `eulerCoeff` limit, or is there a residual?** — see the fork in §5.
   This is one decisive comparison, not a wide search.

## 4. The formalize-first Lean target

A single bridging lemma, conditional (§3b-cond) on the AJ + modular-S classes
that **already exist** in `phi-q-aj-machinery-identification.lean`:

```
-- conditional on [QuantumAPolynomial 𝓑_3] [Li2QRegulator 𝓑_3]
theorem zHabiro_realq_saddle_eq_rogers_li2q :
    archimedeanSaddle (ZHabiroCauchy.zHabiroLimit q⁻¹ eulerCoeff) realQ
      = QRogersPentagonArchimedean.rogers_li2q  := …
```

i.e. *the real-q archimedean saddle of the Lean-certified `eulerCoeff` limit
is the production `li2q` tower term.*

> **Update (2026-06-22): scaffolded.** The target is now a typed Lean object —
> `class QOU.BraidKnot.ZHabiroRogersSaddle` in `QuantumDilogarithm.lean`, whose
> `saddle_phi_q_eq_towerTerm : realQSaddle phi_q = towerTerm` field is the open
> conjectural input, with two non-vacuous conditional corollaries
> (`realQSaddle_phi_q_at_zero`, `…_ne_phi_q_at_zero`). It reuses the file's
> existing `phi_q` (Faddeev) and `towerTerm = -li2_q(-|·|)` (Rogers) so no new
> dilog objects were introduced. A full proof of the field remains research-grade
> (saddle-point / Stokes); the scaffold lets downstream depend on it conditionally.

Anchors that already exist (no scaffold from scratch):

| piece | where |
|---|---|
| root-of-unity face (`Φ_q`/`eulerCoeff`) | `QOU.MassEndomorphism.ZHabiroCauchy` (merged #2447) |
| real-q face (Rogers, bounded) | `QOU.BraidKnot.QRogersPentagonArchimedean` (`rogersAlpha`, `…_bounded_under_convergence`) |
| the two-saddle identification | `phi-q-aj-machinery-identification.{md,lean}` (`Â_K`, `[garoufalidis2004]`) |
| the `q ↔ q̃` bridge | `conj:modular-s-transform-q-q-tilde` |

Proving this lemma *retires* the brane-tower `Φ_q`-form proposition's
production claim cleanly: the tower's surviving evaluator is `li2q` **because**
it is the real-q face, not by fiat.

## 5. The fork — and the falsification

Compute one quantity: the real-q saddle `S(z)` of the `eulerCoeff` limit
(stationary-phase / Stokes of `log Φ_q` continued to real `q`, **not** the
divergent product itself) and compare to `−Li₂^q(−z)` at the physical `z_i`:

- **Fork A — they agree.** Then there is **nothing new to fit**: `li2q` *is*
  the bounded z-Habiro continuation, and the deliverable is the §4 *proof*. The
  honest, publishable statement is structural, not numerical.
- **Fork B — a residual `R(z) = S(z) − (−Li₂^q(−z))` remains.** Then `R` is the
  **genuinely new bounded object** — and it is *already constrained*: it must
  satisfy (I-bound)+(I-bar) and carry only the algebraic Cauchy data, a
  **finite-dimensional** target (per the PSLQ-entropy discipline), *not* the
  refuted `Φ_q`/`n⋆` family. Only Fork B warrants any numerical identification,
  and only on `R`.

Either way the refuted `Φ_q`-at-`|V̂_i|` direction is not revisited.

## 6. What NOT to do (guardrails)

- ✗ No 7th `n⋆` truncation ansatz (six refuted).
- ✗ No re-routing of the unbounded `Φ_q` product into the mass table.
- ✗ No CAL-4 / extra calibration input.
- ✗ No *wide* PSLQ/closed-form scan — only Fork B's residual `R`, only if it is
  nonzero, only after (I-bound)+(I-bar) prune it.

## Cross-references

- [`2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md`](2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md) (the refutation)
- [`2026-06-17-refuted-ansatz-lemmas.md`](2026-06-17-refuted-ansatz-lemmas.md) (six `n⋆` refutations)
- `content/.../stochastic-mechanics/phi-q-aj-machinery-identification.{md,lean}` (two-saddle identification)
- `content/.../lean/QOU/BraidKnot/QRogersPentagonArchimedean.lean` (bounded real-q Rogers lemmas)
- `content/.../mass-theory/brane-tower-z-habiro.md` (`conj:brane-tower-z-habiro`, the open `n⋆`)
- `content/.../mass-theory/mass-endomorphism-tower.md` (`prop:mass-endomorphism-tower`, the `li2q` production form)
- refs: `[garoufalidis2004]` (AJ), `[faddeev1994]`, `[kashaev1997]`, `[habiro2004cyclotomic]`
- `AGENTS.md` §"Im(q) at fibre vs observable level"; canonical-derivation cheat-sheet "Φ_q vs Li₂^q context-sorting"
- sibling PR **#2481** (channel-level `|V̂_i^full|` audit: `full`/regular-rep is the forced mass arg vs `std`/Jones–Markov which diverges; the `tr_M`-vs-`tr_reg` ~10% conflation + weight convention)
