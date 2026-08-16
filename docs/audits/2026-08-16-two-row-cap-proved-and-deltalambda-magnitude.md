# The two-row cap is a theorem; the Δ_λ magnitude hits a named wall

**Branch** `claude/mass-tworow-lean-deltalambda-2026-08-16` · **PR** #5242
**Date** 2026-08-16

Two tranches. Tranche 1 lands. Tranche 2 prunes half the candidate, finds the
other half blocked upstream, and reports the wall rather than forcing a
closure.

---

## Tranche 1 — the mass channel's two-row cap, derived

### What was already proved, and where it actually lives

`QOU/QBeta/WenzlWeightVanishing.lean`, sorry-free:

* `wenzlLevel_conventionD` — convention D (`z = q³/(q²+1)`) **is** Wenzl level
  `r = 2`.
* `schurPrincipal_eq_zero_iff` — `s_λ(1,Q,…,Q^{r−1}) = 0 ⟺ ℓ(λ) > r`, for
  every `n`, every `λ`, every `r`.

**Correction to the brief that scoped this work.** It located both in
`QOU/MathlibExt/MarkovNormalisation.lean`. They are not there. That file
carries the `n = 2, 3` normalisation identities plus a bridge-side *mechanism*
sketch, and its own docstring says so: *"The lemmas below are not an
independent establishment of it and must not be read as one."*

### What this branch adds

[`QOU/MassTheory/TwoRowCapDerived.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TwoRowCapDerived.lean)
— sorry-free, generic `[Field R]`, `#print axioms` clean on all nine
declarations (`propext, Classical.choice, Quot.sound`).

| declaration | content |
|---|---|
| `massWeight_eq_zero_of_three_rows_of_wenzl` | the cap itself |
| `colLen_le_two_of_massWeight_ne_zero_of_wenzl` | contrapositive the sum lemmas consume |
| `traceSum_eq_twoRow_of_wenzl` | **restricting `∑ y_λ χ_λ` to `Λ²` is an identity** |
| `bindingSum_eq_twoRow_of_wenzl` | same for `∑ y_λ χ_λ Δ_λ`, at every `A` |
| `threeRowPart_eq_zero_of_wenzl` | the residual share is `0`, not "small" |
| `twoRow_share_eq_one_of_wenzl` | **the two-row share is exactly `1`** |
| `exists_three_row_diagram`, `two_one_survives_filter` | non-vacuity |
| `moment_and_schur_routes_agree_of_wenzl` | cross-route agreement |

The sum-level statements are the new content. The corpus had per-weight
vanishing; it did not have "the restriction the mass channel performs is
exact, for arbitrary observable `χ` and arbitrary `Δ`". `χ` and `Δ` are left
free deliberately — the dropped terms die through the *weight*, so nothing
depends on which observable is summed, and in particular `Δ_λ` cannot
reinstate a dropped block however large it is on many-row diagrams.

### Conditional on what

**Not** conditional in the Lean sense: no class hypothesis, no `sorry`, no
axiom beyond the standard three. But the `_of_wenzl` suffix is load-bearing
and every name carries it.

Everything is proved *about `schurPrincipal 2 Q μ / Z`*, a named explicit
rational expression. Reading those theorems as statements about **the mass
channel's Ocneanu weight** is Wenzl's theorem — cited, not proved. `#print
axioms` cannot see that dependency, because it is carried by the choice of
object rather than by an axiom. The file says this in a dedicated docstring
section so an axiom-clean report is never mistaken for unconditionality.

`IsOcneanuWeightSystem`, which the brief warned about, **does not exist
anywhere in this repo** — searched the whole working tree, zero hits. It is a
name from another branch or a proposal.

### What was deliberately *not* written

A corollary discharging `hTL : y₁₃ = 0` in
`markovWeights_eq_jones_of_threeRow_eq_zero`. That lemma **concludes**
`z·[2]_q = q²`, so feeding it a convention-D weight assumes what it proves —
the §3b-cond self-assuming-projection failure. The agreement theorem is safe
in a way that one is not: both sides there are *consequences* of convention D,
neither is a premise for it.

Also caught in passing: the first draft's `cap_agrees_with_moment_route_of_wenzl`
had a docstring claiming an agreement its proof never established — it never
invoked the moment route. Renamed to what it proves, and a genuine agreement
theorem written alongside.

### The two routes

| | premises | cost |
|---|---|---|
| **moment** `threeRow_eq_zero_of_jones_ocneanu` | three Markov moments + `z·[2]_q = q²` | none — no external citation |
| **Schur** this branch | `schurPrincipal_eq_zero_iff` at level 2 | Wenzl's weight formula |

Neither is derivable from the other as stated. Their agreeing is the one place
the Wenzl citation is independently corroborated inside the corpus.

---

## Tranche 1b — the sites that posit the cap

25 sites assert/posit rather than derive. Full inventory in the PR; the
load-bearing ones:

| site | what it says | should now cite |
|---|---|---|
| `mass-theory/markov-trace-frobenius-selection.{md,ts,lean}` | "(**row cap**) `w_λ = 0` whenever `ℓ(λ) ≥ 3`" as numbered *hypothesis* | `conventionD_weight_eq_zero_iff_rowLens` — hypothesis 1 is now a theorem |
| `mass-theory/convention-d-kills-antisymmetriser.md:81` | "**impose** the row cap … and `z` is forced" | `wenzlLevel_conventionD` — "impose" becomes "invoke" |
| `mass-theory/markov-trace-frobenius-selection-proof.md:190` | "**Adjoin** the row cap `y_{(1³)} = 0`" | same |
| `mass-theory/two-row-stratum.md:22,24` | "`y_λ = 0` exactly when `ℓ(λ)≥3`, **because** the fibre is 2-dimensional" — asserted, no proof pointer | `schurPrincipal_eq_zero_iff` |
| `mass-theory/hecke-radical-is-temperley-lieb.md:1` | "vanishes identically … as a rational function of `q`" — asserted from `dim V = 2` | same |
| `mass-theory/two-row-projection.md:12` | splits `tr_M` with a **live** complement `∑_{ℓ>2} y_λ χ^λ` | `traceSum_eq_twoRow_of_wenzl` — the complement is identically zero |
| `braids-and-knots/markov-axioms-primitive.md:26` and `mass-theory/h3-markov-wenzl-weights-context.md:24` | route the cap through `lem:feynman-eigenbasis-decomposition`, a *decomposition* lemma that never proves weight vanishing | the fibre premise is no longer load-bearing |
| `lean/QOU/BraidKnot/TwoRowStratum.lean:124` | `class HasTwoRowProjection`, "**axiomatised here as a class**" | `conventionD_weight_ne_zero_of_two_rows` + the iff |
| `lean/QOU/MassTheory/ThreeRowExtensiveCumulant.lean:49` | self-flagged: "`sRow3` is a *hand-entered table* … not proved in Lean" | derive the three-row entries |
| `lean/QOU/Eightfold/RowCapObstruction.lean`, `eightfold-way/eightfold-open-problems.md:19` | "the row cap `ℓ(λ) ≤ N` is **cited, not formalised**" | retired for the `r`-generic statement |
| `docs/coordination/trace-convention-registry.json:141,291` | "**The PREMISE is not established**" | the cap half now is |
| `docs/audits/2026-08-07-binding-is-three-row-dominated-hypothesis-refuted.md` | title asserts binding is **≥3-row dominated** | contradicted — needs a superseded banner |
| `docs/audits/2026-08-07-two-row-projection-is-the-pairwise-cap.md:38` | "**13.4 %** of the trace is projected to zero, measured, not estimated" | convention-C measurement |

**No content blocks were edited at all** — not even the two or three one-line
citation swaps the scope allowed. Reason: every one of these blocks carries a
`.qa.json` sidecar, and any `.md` edit drifts `source_hashes.md`, which needs
`qa-sweep` to refresh. `folio-assistant/` is not set up in this sandbox and
cloning it would spend most of the 1.3 GB of free disk. A stale sidecar I
cannot refresh is worse than a listed finding, so the whole inventory is left
as a list. Tracked as a bean.

### `prop:he4-two-row-dominance` — the withdrawn 86.6 % is worse than withdrawn

The brief asked whether the proved cap changes its status. It **moots** it.

The block asserts `|∑_{λ∈Λ²(12)} c_λ| / |tr_M| ≥ 0.80`, empirically `86.6 %`,
encoded per §3b-cond as `class HasHe4TwoRowDominance` with
`ratio_lower_bound : 4/5 ≤ ratio`, `ratio_upper_bound : ratio ≤ 1`, and an
`instance` pinning `ratio := 866/1000`.

Under convention D the share is **exactly 1** (`twoRow_share_eq_one_of_wenzl`),
for every braid word and every strand count. So:

1. `866/1000` is **not a weaker-but-valid bound**. A share below 1 records a
   nonzero `≥3`-row contribution, which is precisely what convention D
   forbids. The instance pins a convention-C measurement.
2. The witness is self-identifying as C-frame: the `.md` table reports the
   sign rep `(1¹²)` contributing `4.7 × 10⁻¹⁰`. Under D that is exactly `0`.
   A nonzero 12-row weight cannot occur at level 2.
3. The sibling `def:two-row-stratum` **already** withdrew the figure on
   2026-08-09 — *"Under the production convention D the restriction is not a
   dominance but an identity"* — and `he4-two-row-dominance.{md,ts,lean}` was
   never updated. The definition block and the proposition that consumes it
   have contradicted each other for a week.
4. `dominant_block_positive_share : (1:ℚ)/77 ≤ 866/1000` is a `norm_num`
   numeral tautology carrying no ⁴He content, dressed as a physics theorem.

**Recommended (not done here — beyond "one-line citation swap" scope):**
retire the class, restate the proposition as a corollary of the cap with
share `= 1`, and re-derive or retire the top-5 table, which is C-frame
throughout. Tracked as a bean.

---

## Tranche 2 — the Δ_λ binding magnitude via Neumann's extended Bloch group

Owner-directed focus. The missing object is an **additive, extensive,
super-pairwise** term; the extended Bloch group is the only named candidate
meeting all three, and it is parameter-free because the flattening is
determined by the gluing equations rather than chosen.

I did not close it. Here is precisely where it fails, and what survives.

### Three corrections to the brief, established before any work

1. **Bean `qou-wojw` does not exist** (`bean not found`; no "flatten" match in
   the store). The real bean is **`qou-985x`** — *"Extended Bloch group route:
   flattening supplies the canonical log-branch A1 lacked"*, status **todo**,
   parent `qou-kemt`, scoped 2026-08-07 and never executed. That is the slot.
2. **`docs/coordination/2026-08-08-main-review-workplan.md` does not exist**
   and never did on any branch. The doc meant is almost certainly
   `docs/coordination/2026-08-07-l2-volume-binding-cluster.md`.
3. **PR #4798's O(100×) log-branch gauge freedom is already closed** — and the
   answer is zero, not "needs a principle". PR #4848
   (`docs/audits/2026-08-09-nastokes-gauge-fixing-germ-root-vector.md`) shows
   `F_q` is an `Ad(ρ(σ₁))`-eigenvector, so all transported curvatures lie on
   one line and `Ω₂^⊥ = 0` for **every** intersection form, `H₁` basis and
   handle assignment — the handle gauge never needed fixing. Lean-proved
   sorry-free in `GermRootVectorGaugeFixing.lean`; probe exhausts all 49
   handle-exponent pairs at `max‖[𝓕_a,𝓕_b]‖ = 1.17e-52`. Every nonzero entry
   in #4798's spread is inadmissible (uses `ρ(σ₂)`, absent from `σ₁³`, or the
   log germ rather than the pinned q-germ). **This was offered as the concrete
   live hook. It is not live.**

### W1 — the volume leg is provably zero at the deuteron (scope-(b), proved)

The owner's cheap decisive question: *what is the deuteron's ideal
triangulation and its tetrahedron count, and does that count scale like the
deficit?*

Committed data —
`computations/deltalambda/deuteron-octahedral-gluing.witness.json`, SnapPy
3.3.2 at 70 dps: the `σ₁³` closure is the trefoil `T(2,3)`,

```
num_tetrahedra = 2      shapes = [0.5+0i, 2.0+0i]
volume         = 0.0    solution_type = "contains flat tetrahedra"
```

with the edge gluing equation forcing `z₀·z₁ = 1` identically. **Both shapes
are real.**

[`QOU/MassTheory/BlochVolumeLegFlatVanishing.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BlochVolumeLegFlatVanishing.lean)
— sorry-free, `#print axioms` clean:

* `eq_zero_of_conjAntisymm_ofReal` — Bloch–Wigner is odd under conjugation,
  `D(z̄) = −D(z)`; a real is its own conjugate; so `D` vanishes on `ℝ`.
* `sum_eq_zero_of_real_shapes` / `…_forall_card` — hence `∑ D(zᵢ) = 0` over
  real shapes **for every tetrahedron count**.
* `deuteron_volume_leg_eq_zero` — `Vol = D(1/2) + D(2) = 0`, from symmetry
  alone, no `Li₂`, no numerics.

Three things follow.

* SnapPy's `0.0` is **forced by the shapes being real**, not a numerical
  artefact of a degenerate solve.
* **Count-independence is the sharp part.** An extensive term grows with the
  number of constituents; this sum does not grow, because every summand is
  individually zero. No finer triangulation, no heavier still-flat nucleus,
  no different spanning choice rescues it.
* **Flattening cannot help.** A flattening `[z;p,q]` records branch data for
  `log z` and `−log(1−z)`; it shifts the *imaginary* part. `D` is the real
  part and is flattening-independent. So the very move that distinguishes
  this route from a fit is powerless on this leg.

Scope: **(b) structural exclusion**, invariant named (conjugation
antisymmetry). It excludes *the volume leg on a real-shape triangulation, at
any count*. It does **not** exclude the extended-Bloch route.

### W2 — the census-frame volumes are not extensive either (measured, pure geometry)

The other deuteron frame assigns the census knot `6₂`. Checking whether *those*
volumes scale like `A` — SnapPy census constants and Catalan's constant only,
**zero experimental input**:

| A | knot | Vol | Vol/A | Vol(A)/Vol(A−1) | A-ratio |
|---:|---|---:|---:|---:|---:|
| 2 | `6₂` | 4.400833 | 2.2004 | — | — |
| 3 | `8₁₁` | 8.286317 | 2.7621 | 1.8829 | 1.5000 |
| 4 | `L6a4` | 7.327725 | 1.8319 | **0.8843** | 1.3333 |

**`Vol(A=4) < Vol(A=3)`.** The assigned volumes are not monotone in `A`, let
alone linear. An extensive term must grow with `A`.

The tell: `binding_manybody_series.py` gets ⁴He extensivity from
`B_4 = 2·m_e·**A**·Vol(L6a4)` — an explicit `A` written into the formula, not
extracted from the geometry. The volume input itself is *decreasing*.

Self-test applied (*"if the experimental value were different, would these
numbers change?"*): no. Census volumes and Catalan's constant. Derivation, not
fit.

### W3 — the blocking wall: the corpus does not agree what knot the deuteron is

Three live, inconsistent assignments:

| reading | knot | volume | where |
|---|---|---|---|
| braid-closure (canonical for Δ_λ) | trefoil `T(2,3)` | **0**, 2 flat tetrahedra | `deuteron-octahedral-gluing.witness.json` |
| census-assigned | `6₂` | **4.40083** | `knot_volumes.py:139`, `binding_manybody_series.py:11`, 4 probes |
| linear-chain | Hopf `L2a1` | **0** | `volume-binding-four-point.witness.json:87` |

The candidate term differs by the *whole* of `Vol(6₂)` between frames. That
witness further flags that the deuteron's +0.2 % match was obtained by
**substituting `Vol(𝓑₃)` for `Vol(Hopf)`, an unjustified substitution**.

**You cannot derive a knot invariant while the knot is undetermined.** This is
upstream of every flattening question and it is where the route actually
stops. Resolving it is not a modelling preference — it decides whether the
`A = 2` anchor of the whole construction is `0` or `4.4`.

The owner ruling *"assume hyperbolicity is granted"* (recorded in `qou-985x`)
covers the hyperbolicity caveat. It does not resolve W3, which is a question
about **which manifold**, not whether it is hyperbolic — and the committed
SnapPy data for the canonical braid closure says flat, `Vol = 0`.

### W4 — what survives: the CS leg, determined only mod π²

`W1` kills the real part. The imaginary part is untouched, and it is exactly
where flattening is load-bearing (the ordinary Bloch group fixes `CS` only mod
`π²/6`). The corpus already knows the ordinary regulator is structurally blind
here: `qbeta-5two-route42-extended-bloch-anchor.witness.json` G4 records that
`∑ D` cancels **identically** over any Galois orbit in any number field, since
`D(z̄) = −D(z)` — the same invariant this branch proves, arrived at
independently.

But the corpus's own `admissible_correction` (`FiveTwoSaddleSumRule.lean` §7g,
reading Neumann `uploads/0307092v2.pdf`) shows `ν = 0` forces `(p,q) = (3k,−2k)`
with correction exactly `k·π²·ε`, so `R̂` is well-defined **in `ℂ/π²ℤ`**. An
additive binding term in MeV needs a definite real number, not a class mod
`π²`. Fixing that branch by whichever value matches AME is the forbidden fit
in hyperbolic-geometry costume.

So the honest statement of the surviving question: **can the `CS` leg be
pinned to a definite real value by the gluing and parity equations alone,
without a π²-fixing choice?** Not answered here.

### What exists already, for whoever picks this up

More infrastructure than `qou-985x`'s "'extended Bloch' in ONE file" suggests:

* `QBeta/FiveTwoFlattenedPentagon.lean` — **working flattening machinery**,
  no branch hypotheses; carries the expansion as the logarithm so the defect
  never appears as a hypothesis.
* `QBeta/FiveTwoSaddleSumRule.lean` §7g — Neumann's `R(z;p,q)`, `ℬ̂(ℂ) = ker ν`,
  and `admissible_correction`.
* `QBeta/BlochFiveTerm.lean` — 5-term relation, sorry-free; already records
  that Bloch–Wigner `D` is provably useless here (`∑ D(yⱼ) = 0` automatically).
* `MathlibExt/IdealTriangulation.lean` — `IdealTetrahedron`, volume in both
  Lobachevsky and dilogarithm form.
* Neumann's paper is local: `uploads/0307092v2.pdf`. Garoufalidis–Zagier survey
  `uploads/2304.12545v1.pdf`. Zagier dilogarithm
  `uploads/zagier-the-dilogarithm-function.pdf`. Neumann–Zagier 1985 present.
  **Several are not yet bib-registered** (`qou-xm0j` and siblings), and
  `bib-qa-verifications.json:10726` requires registration before any Lean
  statement leans on the lifted 5-term relation.

Cheapest real foothold that is *not* a per-λ ansatz and so escapes #5234's
scaling wall: **bean `qou-fl4t`**, restoring the DG flattening monomial
dropped in `whitehead_c_sigma_torsion.py`. That monomial is precisely what
makes the torsion expression triangulation-invariant, and
`one-loop-triangulation-invariance.witness.json:248` records that the `c = 1`
calibration used to justify dropping it **cannot detect its absence**.

### Not re-run, per PR #5234

The ≤2-row support restriction is a value no-op (dropped weights `< 1.5e-67`);
the ℓ¹ ceiling loosened 59 % → 69.2 % under D but stays `< 1`; and the
intensive-vs-extensive diagnosis is a *scaling* argument, indifferent to block
count, so no frame or support change touches it. **No per-block reweighting
can ever work** — any seventh per-λ ansatz is dead on arrival.

---

## Verification

CI is `workflow_dispatch`-only repo-wide (Actions billing) and Gemini review is
sunset, so per AGENTS.md §10 the agent's own verification is the gate.

* Both new Lean files: `lean`-direct **exit 0** against the real import cone
  (`LEAN_PATH` over the restored oleans), 1.7–1.9 s each. Never `lake build`
  (bean `qou-r13s`).
* `#print axioms` on all 15 new declarations: `[propext, Classical.choice,
  Quot.sound]`. Zero `sorry`, zero `native_decide`.
* Olean count unchanged at **7268** in `.lake/packages` (6990 mathlib); three
  QOU oleans compiled `lean`-direct into the package build dir, no cache
  eviction.
* No content blocks edited, so no `.qa.json` sidecar refresh is due.
* No witnesses regenerated (bean `qou-pgdw`).
