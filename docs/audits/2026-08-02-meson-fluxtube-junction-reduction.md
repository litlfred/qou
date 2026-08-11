# Meson flux-tube braid — Y-junction reduction / D-meson operator-selection: honest negative (2026-08-02)

**Branch:** `claude/meson-fluxtube-operation-2026-08-02` · **PR:** #4614
**Lean:** [`MesonFluxTubeReduction.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean) (sorry-free, `lean`-direct exit 0)
**Witness:** [`meson-fluxtube-topology.witness.json`](../../computations/meson-fluxtube-topology.witness.json)
**Serves:** bean `qou-qpj9` (meson-binding braid gate); the J/ψ attack [`2026-08-02-jpsi-boundstate-mass.md`](2026-08-02-jpsi-boundstate-mass.md) (PR #4608); owner bean `qou-jsx5` (lattice-QCD-from-QOU, PR #4600).

## The task

Derive the **canonical meson flux-tube braiding operation** — the operation that turns a `q̄q` colour singlet into a definite braid/tangle whose mass the framework can then predict. The J/ψ attack showed the charmonium mass is *in-range* for the hyperbolic mechanism (Vol ≈ 24 → 3097 MeV) but **no canonical c̄c braid exists** — J/ψ and η_c wanted different-topology braids (per-state-fit signature), so any braid choice was a fit.

Two routes were attempted:
1. **Topological (Y-junction → single-tube reduction).** Reduce the baryon's 3-tube Borromean vertex to the meson's single tube.
2. **Owner-redirected (symbolic gg→c̄c operator-selection on the D meson).** Target the D meson `c̄u` (1864.84 MeV) — the minimal dressing of a *stable* isolated `c̄` (no annihilating `c` partner, unlike charmonium) — and fix the asymmetric `c̄`(n=5) | light(n=3) tube via the Frobenius–Gram operator-selection rather than a numerical braid-volume search.

**Both routes fail to canonically fix a braid a priori.** The joint mass check was therefore **not** run (running it would be the per-state fit the discipline forbids). The negatives are sharp and name the precise missing structural data.

## Route 1 — the naive Y-junction → single-tube reduction is `Vol = 0` (scope (b))

The proton mass-knot is the Borromean link `6₂³ = (σ₁σ₂⁻¹)³`, a **3-strand** braid whose exterior is hyperbolic:

| object | strands | word | Vol (SnapPy) |
|---|---|---|---|
| Borromean (proton) | 3 | `(σ₁σ₂⁻¹)³` | **7.32772475342** = 2·V_oct ✓ |
| `(σ₁σ₂⁻¹)⁶` | 3 | — | 21.6315986792 |
| `(σ₁σ₂⁻¹)⁷` | 3 | — | 26.054401507 |
| `T(2,k)`, k=2..10 | 2 | `σ₁^k` | **0** (incl. gluon `T(2,9)`) |
| drop-σ₂ reduction | 2 | `σ₁³` (trefoil) | **0** |

QCD reading: three quarks, three colour flux tubes meeting at a string (Y-)junction. A meson `q̄q` has two endpoints and a single tube — no junction. The *literal* junction reduction (collapse the Y, drop one tube) takes the strand count **3 → 2**.

**The obstruction.** A 2-strand braid has no braiding freedom beyond one winding number: `B₂ ≅ ℤ` is abelian — the braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` needs a *third* strand. Hence every 2-strand braid is a torus braid `σ₁^k`, closure `T(2,k)`, hyperbolic volume `0` (Thurston; SnapPy-verified above). The reduction yields only a `Vol = 0` **carrier** (quantum numbers), never a hyperbolic mass-knot — strand *removal* cannot build the Brunnian (≥ 3-component) structure hyperbolicity requires.

This is a scope-**(b)** structural exclusion of *this specific operation*, cited invariant: `B₂` abelian (Lean-proved: `twoStrand_comm`, `twoStrand_commutator_trivial`, `twoStrand_winding_bijective`) + the torus-link `Vol = 0` theorem (SnapPy-witnessed). Every one of those Lean facts is **false** for `B₃` — whose nonabelian commutator structure *is* where the hyperbolic Borromean `(σ₁σ₂⁻¹)³` lives.

**The framework already knows this.** `lepton-meson-parallel.md` places the meson at **`H₃(q)` (3-strand)**, braid `(σ₀σ₁)²·σ₁σ₀` (Hopf-bound `q̄q` pair) — the Hopf-binding *supplies* the third strand. So the naive single-tube reduction is not the framework's meson; the "3rd strand" is the binding, not a quark. This route rules out the literal picture and points at the actual `H₃(q)` construction.

## Route 2 — the D-meson operator-selection is charm-degenerate (the load-bearing negative)

On the `H₃(q)` meson, the owner-redirected route fixes the braid via the symbolic **gg→c̄c operator-selection** (`operator-selection-lp.md`, `knot-operator-selection-proof.md`): the Frobenius–Gram LP selects the minimum-crossing-energy operator `Φ*` for a given `(n_strands, n_target)` and produces a dual certificate. The mechanism *is* canonical — a well-posed LP with a unique optimiser. **Its inputs for the D meson are not.**

### The generation-winding dictionary indexes generation, not up/down-type

`lepton-meson-torus-knot-dictionary.lean` fixes the meson crossing count as the **sum of the two quark generation windings** `n ∈ {3,5,7}` (`meson_crossing_is_sum`, Lean-proved):

| meson | quarks | windings | crossings |
|---|---|---|---|
| π | ū d | {3,3} | 6 |
| K | ū s | {3,5} | 8 |
| η/φ | s̄ s | {5,5} | 10 |

The dictionary is a **symmetric function of the unordered winding pair.** For the D meson `c̄u = {n_charm, 3}` this immediately collides:

- **charm = 5** ⇒ D `{5,3}` = kaon `{3,5}` — *identical multiset*, 8 crossings, same operator-selection target;
- **charm = 7** ⇒ D `{7,3}` shares its 10-crossing count with `η/φ` `{5,5}`.

But `m_D ≈ 1865 ≈ 3.8·m_K`. The winding dictionary **cannot separate D from K** (Lean-proved: `windingContent` is non-injective, `winding_content_not_injective`). The gg→c̄c operator-selection selects the *generation-2* (`n=5`) block — which is exactly the strange-selection; nothing in the `{γ,σ₀,σ₁,L₊,L₋,e⁻}` `H₃(q)` basis produces a charm-*specific* operator distinct from the strange operator.

### Corpus inconsistency (flag for canonical-watcher)

The prerequisite input — *which* torus knot is the charm quark — is itself ambiguous in the corpus:

- [`knot-formula-table-table2-data.md`](../../content/quantum-observable-universe/predicted-spectra/knot-formula-table-table2-data.md) row 11: **charm `𝔠` → T(2,5)** (m=2, n=5).
- [`knot-notation-convention-table1-data.md`](../../content/quantum-observable-universe/braids-and-knots/knot-notation-convention-table1-data.md) row 9: **charm `c` → (2,7)-torus knot `7₁`** (n=7).

These are incompatible (n=5 vs n=7). Neither resolves the degeneracy — both collide the D meson with a lighter meson (kaon at n=5, η/φ at n=7). Picking one value does not fix the braid; it just chooses which lighter meson D collapses onto.

### The precise missing datum

A canonical D-meson braid needs an invariant the `T(2,n)` winding number does **not** carry: a **weak-isospin / up-down-type grading `T₃`** orthogonal to the generation winding `n`. Charm (up-type gen-2) and strange (down-type gen-2) share `n`; what distinguishes them is weak isospin. Consistently, the framework itself places the up/down distinction in the *weak* sector — the cross-family generator `T(3,5)` (`force-knot-identification.md`), which transmutes up↔down — **not** in the `T(2,n)` winding dictionary. Until the meson-binding operation is refined to consume a `T₃` grading (so the c̄ block is selected distinctly from the s̄ block), the D-meson braid is not canonically fixed and its mass can only be fitted.

## What is canonical vs not (summary)

| ingredient | canonical? |
|---|---|
| operator-selection LP mechanism (unique `Φ*` per `(n, n_target)`) | ✅ yes (well-posed, dual-certified) |
| meson = `H₃(q)` Hopf-bound `q̄q` (3-strand) | ✅ yes (framework) |
| `m_K/m_π` mass *ratio* (down-type mesons) | ✅ yes (L2-MET observable) |
| charm's own winding `n` | ❌ **corpus-ambiguous** (T(2,5) vs T(2,7)) |
| D-vs-K separation from winding number | ❌ **degenerate** (same multiset at n=5) |
| up/down-type grading `T₃` on the meson tube | ❌ **absent** from `T(2,n)` dictionary |

Two independent `❌`s block a canonical D-meson braid. The reduction is **not** canonical; the honest step is not a mass check but the structural refinement named above.

## Anti-fit statement

No braid was hand-picked to reproduce 1864.84 / 1869.66 MeV. The joint `m_D` check was deliberately **not** run: with the braid under-determined at two independent points, a "closest hit" would be exactly the per-state fit the J/ψ attack already recorded as worthless. A negative that names the missing datum (`T₃` grading ⟂ `n`) is the valuable output.

## Next honest step (refines `qou-qpj9`)

Derive (or refute) a **weak-isospin `T₃` grading of the `H₃(q)` meson tube** that selects the charm (up-type) block distinctly from the strange (down-type) block — e.g. from the `T(3,5)` weak-generator's up↔down action, or a bar/mirror asymmetry on the `c̄` end. If such a grading is derived and canonically fixes the asymmetric `c̄`(5̄)|light(3) braid, *then* check once against `m_D`. Separately: resolve the charm T(2,5)-vs-T(2,7) corpus inconsistency (canonical-watcher).
