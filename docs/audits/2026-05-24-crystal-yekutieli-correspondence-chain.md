# Crystal bases ↔ Yekutieli tessellation — correspondence through the framework chain

**Date:** 2026-05-24
**Trigger:** Author question during Path B (item 4) work — "do crystal bases provide tessellation for Yekutieli? is this the same tessellation used for hyperbolic knot complement tessellation? can we follow the crystal bases and tessellation all the way through GB filtration jet order → Bring → Archimedean univ?"
**Status:** Research-path audit. Identifies the chain, what's tractable, what's research-grade open.

## §1. Two tessellations side-by-side

The framework uses two distinct decompositions that LOOK like tessellations:

| | Crystal basis (Kashiwara) | Yekutieli geometric tessellation |
|---|---|---|
| Domain | Hecke algebra H_n(q) at q→0 | 2-surface in ℝ³ (or hyperbolic 3-manifold) |
| "Cells" | SYTs (Standard Young Tableaux); crystal graph vertices | Refinement cells (4^k at jet grade k) |
| Arrows | Kashiwara operators ẽ_i, f̃_i | Boundary maps; CBH commutator structure |
| Measure | Wedderburn weights y_λ (Jones-Markov) | Hyperbolic volume / Riemann measure |
| Output | Character χ^λ(σ_w) | Holonomy of connection 1-form |

For the Borromean rings 𝓑_3, the **algebraic side** lives in H_3(q) with 3 irreps; the **geometric side** is the complement of 𝓑_3 in S³, with Vol = 8G and decomposition into 8 ideal tetrahedra (2 regular ideal octahedra × 4 tets each).

## §2. The chain from substrate to archimedean

Per [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md):

```
substrate q_0
  → 𝐂 categorical action
  → Yekutieli non-abelian Stokes    ← GEOMETRIC: tessellation of 𝓑_3 complement
  → H_n(q) Hecke
  → Wedderburn decomposition         ← ALGEBRAIC: irrep λ ⊢ n
  → Frobenius pairing tr_M           ← Markov trace = Σ y_λ χ^λ
  → confinement SDP / canonical T_w
  → Archimedean functor at q_0       ← evaluation at substrate
  → MeV observables
```

The Yekutieli step is GEOMETRIC; the Wedderburn step is ALGEBRAIC. They're connected by the fact that the Markov trace of a braid closure can be computed EITHER as:

- **Geometric:** Yekutieli MI of the holonomy connection over the spanning surface
- **Algebraic:** Σ_λ y_λ · χ^λ(braid word) over Wedderburn blocks

The framework currently uses the algebraic computation for production; the geometric (Yekutieli) computation is used for STRUCTURAL identification of h^k coefficients.

## §3. GB filtration jet order — the bridge candidate

The **Gröbner-Shirshov filtration** on H_n(q) generates the normal-form word reduction. Each braid word w has a Coxeter length ℓ(w); reductions take place in stages graded by ℓ.

The **jet order** is the h-order at which a structural relation first matters: a relation involving k crossings contributes at h^k. Per [`docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`](2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md) §2:

| jet grade | tessellation cells | h-order | structural relation |
|--:|--:|--:|---|
| 0 | 1 | h⁰ | leading (Wedderburn trivial) |
| 1 | 4 | h² | first Hecke relation (vanishes by Markov cancellation per audit) |
| 2 | 16 | h⁴ | second Hecke relation (h⁴ = −3/4 from Markov trace) |
| 3 | 64 | h⁶ | third Hecke relation (h⁶ = −1/16 from Markov trace) |
| j | 4^j | h^{2j} | jet-graded relation |

The **4^j cells** are the Yekutieli tessellation refinement — geometric.
The **h^{2j}** comes from CBH expansion of the holonomy — geometric.
The **Hecke relation at jet order j** is the algebraic counterpart — algebraic.

So GB filtration jet order is the **bridge** between the two sides: it indexes both the geometric refinement level AND the algebraic Hecke relation.

## §4. The crystal-basis counterpart

The Kashiwara crystal of H_n(q) at q→0 is a directed graph whose vertices are SYTs and whose edges (Kashiwara arrows) encode the f̃_i / ẽ_i actions. For H_3(q):

| Partition λ ⊢ 3 | dim_S_3(λ) | |SYT(λ)| | Crystal vertices |
|---|--:|--:|--:|
| (3) | 1 | 1 | 1 |
| (2,1) | 2 | 2 | 2 |
| (1,1,1) | 1 | 1 | 1 |

**Total SYTs of S_3** = 4 (matches the **k=1 cell count = 4** of the Yekutieli tessellation).

This is **suggestive but not proven**:

- For S_2: |SYT| = 2 ≠ 4 = k=1 cell count (mismatch unless we square: 2² = 4 = k=1)
- For S_4: |SYT| = 10. But 10² = 100, neither matches k=2 cell count = 16.

So the naive "|SYT(n)|² = cell count" fails. The correct correspondence (if any) is more subtle.

### A more careful guess: K-theory cells

The **K-theoretic K_3 / Bloch element** of 𝓑_3 (per D16 in [`docs/duality-tracker.md`](../duality-tracker.md)) gives `[𝓑_3] = 8 · [e^{iπ/3}] ∈ B(ℂ)` with regulator r_2 = 8G. The **higher** regulator r_2^(2) is conjecturally −6G, giving h⁴ = −3/4 K-theoretically.

If the Yekutieli cells at jet grade k correspond to **K-theoretic strata** of the Bloch group, and these in turn correspond to **MV cycles** in the affine Grassmannian (via the geometric Langlands D19 partial correspondence), then:

```
crystal basis cells ←→ MV cycles ←→ K-theoretic strata ←→ Yekutieli cells
```

This is the **quantum-Langlands chain** the framework's D19 conjecture posits. It's research-grade (Langlands is open even for groups of rank ≥ 2 in any precise form), but **the framework only needs a SPECIFIC instance**: H_n(q) ↔ H_n(q⁻¹) at the level of cell measures, not the full categorical equivalence.

## §5. Bring surface — the geometric host

The **Bring surface** is the genus-4 Riemann surface with full icosahedral symmetry (A_5 ⊂ PSL_2(ℂ)). The framework's torus knots T(2,3), T(2,9), T(3,4), T(3,5) all embed in Bring (per `bring-embeddable-knots-table-data.md` + `b1-torus-knot-rows-theorem.md`).

The Bring surface has a **canonical icosahedral tessellation**: 60 fundamental domains under A_5 action. This is geometric.

**Crystal-basis side at Bring**: the crystal of A_5 (or equivalently the crystal of S_5 restricted) has 26 SYTs (over partitions (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1^5)). The A_5 subgroup index = |S_5|/|A_5| = 2, so the crystal of A_5 has 26/2 ≈ 13 vertices? Not quite — the restriction is subtle.

For the framework's purposes, the key data is:
- Number of A_5 irreps = 5 (rank 4 Lie algebra)
- Bring's fundamental-domain count: 60 = |A_5|
- 60 = 4 × 15 — not a power of 4, so the Yekutieli refinement doesn't naturally land on Bring's icosahedral tessellation

So **Bring tessellation ≠ Yekutieli k=k tessellation** in general. They're different geometric objects.

## §6. What this would buy us, if proved

If the chain holds:

```
Kashiwara crystal cells (algebraic, q→0)
   ↓  [crystal-graph distance = jet order]
Yekutieli geometric cells (per refinement level k)
   ↓  [4^k cells at level k]
GB filtration jet order k (h-power 2k)
   ↓  [CBH commutator structure on Hecke]
Markov trace h^k coefficient (numerical)
```

Then:

1. The 64-cell Yekutieli k=3 computation for the Higgs (item 4 full closure) reduces to a SUM over crystal-basis cells of the appropriate algebraic invariants — **avoiding the 3-4 weeks of hyperbolic-geometry coding**.

2. The h⁶ coefficient of the Higgs residual becomes computable as a Wedderburn-block sum: $\sum_{\lambda \vdash 4}$ (crystal cell measure × χ^λ contribution).

3. The W/Z anchor asymmetry might be UN-resolved (since it's at the SM electroweak mixing level, not the Hecke-algebra level) — but at least the structural h⁶ correction would be derivable in closed form.

## §7. What's tractable now (proposed follow-up probes)

### Probe A — minimal SYT-to-cell-count test

Compute |SYT(n)|, |SYT(n)|², and partition-related cardinalities for n = 2..6; tabulate against the framework's Yekutieli cell counts 4^k for k = 0..5. Identify any clean structural pattern.

**Expected time**: 30 min (sympy + tabular comparison)
**Expected outcome**: negative for naive identification; either confirms 4^k cells are purely geometric, OR identifies a candidate Wedderburn-weighted pattern.

### Probe B — Wedderburn-weighted Markov trace from crystal sum

For the Borromean braid β_Bor in B_3, compute:

$$\mathrm{tr}_M(\beta_{Bor}) = \sum_{\lambda \vdash 3} y_\lambda \cdot \chi^\lambda(\beta_{Bor})$$

with explicit Hoefsmit characters. Compare to the closed form (4+h²−3h⁴−h⁶)/(h²+4) at substrate. **This algebraic computation is already done** in existing scripts (`alpha_k_jones_markov_h3.py`, others). Document that it BYPASSES the geometric Yekutieli MI computation — confirming the bridge through GB filtration is "the Wedderburn decomposition itself", not a separate construction.

**Expected time**: 1-2 hours (reuse existing code)
**Expected outcome**: positive confirmation that the algebraic side IS the framework's existing production path; geometric Yekutieli MI is a STRUCTURAL alternative used only for h-coefficient extraction.

### Probe C — explicit jet-order ↔ crystal-graph distance hypothesis

For S_3's crystal graph, label vertices with their distance from the "highest weight" (longest SYT). Check whether the jet order at which a Hecke relation involves a vertex matches its crystal-graph distance.

**Expected time**: 2-4 hours (need crystal-graph code; sage or hand)
**Expected outcome**: hypothesis-test; either positive (confirms jet order = crystal distance) or negative (different combinatorial structure).

## §8. What's literature (out of scope for the framework)

- **Mirković-Vilonen cycles**: parameterize crystal bases for G as MV cycles in the affine Grassmannian Gr_Ǧ. Geometric Langlands prediction.
- **Kashiwara-Saito construction**: realizes crystal graphs via quiver varieties / Lusztig sheaves.
- **KLR algebras**: Khovanov-Lauda-Rouquier categorification of quantum groups. The framework's H_n(q) embeds in KLR_n; the crystal basis lives at the homotopy category level.
- **Geometric Langlands for surfaces**: 3d-3d correspondence (D18 in the duality tracker) — connects 3-manifold partition functions to 3d N=2 gauge theories.

The framework doesn't need any of this in full generality. It needs the **specific instance** of "for 𝓑_3 in H_3(q), the crystal-basis combinatorics give the Yekutieli cell measures." This is a much smaller question.

## §9. Honest verdict

**Naive identification** "crystal cells = Yekutieli cells" **fails** at the simplest count check (|SYT(4)| = 10 ≠ 16 = k=2 cell count).

**Structural correspondence** through GB filtration jet order is **plausible and partially supported** — both sides are graded by jet order; both give the same h^{2j} coefficient in production at k = 0, 1, 2.

**Full correspondence** is a quantum-Langlands-level question, **research-grade open** in general. For the framework's specific 𝓑_3 question, the tractable path is:

1. Probe A + B (this audit's §7) — short, immediate, confirms or rules out naive structure
2. Probe C — medium, requires crystal-graph machinery
3. **The framework's existing production path already uses the algebraic side** — `alpha_k_jones_markov_h3.py` computes Markov traces via Wedderburn. So the "correspondence" is partially in use, just not branded as such.

**The win** from doing this properly: a clean Lean-level statement of the form "the Yekutieli cell-measure at jet grade k = the Wedderburn χ^λ contribution weighted by [crystal data]" — would let the framework REPLACE geometric Yekutieli MI with a purely algebraic computation, eliminating the need for the 3-4 weeks of hyperbolic-geometry coding to close Path B.

## §11. Mostow-Prasad Rigidity + the Epstein-Penner canonical tessellation

**Algebraic side of "complete hyperbolic structure on knot complement"**: the holonomy representation $\rho: \pi_1(S^3 \setminus K) \to PSL_2(\mathbb{C})$ — discrete, faithful, with finite co-volume image. For Borromean 𝓑_3, $\pi_1(S^3 \setminus \mathcal{B}_3)$ is a 3-generator group; its image in PSL_2(ℂ) generates a discrete subgroup of co-volume 8G (Catalan).

**Mostow-Prasad Rigidity** (Mostow 1968 for closed; Prasad 1973 for finite-volume cusped):

> For finite-volume hyperbolic n-manifolds with $n \ge 3$, the complete hyperbolic structure is rigid: any homotopy equivalence to another such manifold is homotopic to an isometry.

So $\rho$ is not just well-defined but **canonical** — there's no continuous deformation moduli for hyperbolic knot complements. This is the algebraic counterpart of geometric rigidity, and it's the *reason* the substrate quantity $q_0 \in \mathbb{R}_{>1}$ corresponding to $\mathcal{B}_3$ has a definite value.

**Natural tessellation: Epstein-Penner canonical decomposition** (Epstein-Penner 1988):

Among the many possible tessellations of a cusped hyperbolic manifold, there is a **unique** canonical decomposition into convex ideal polyhedra, determined by the cusp horoball geometry: glue horoballs of equal volume at each cusp, take the Ford domain, and the resulting cell decomposition is canonical (preserved by every isometry of the manifold).

For 𝓑_3:
- **2 regular ideal octahedra** (Adams 1985, Thurston notes §6)
- Each octahedron $=$ **4 regular ideal tetrahedra** (barycentric subdivision)
- Total: **8 regular ideal tetrahedra**
- Vol check: $2 \times 8 \times \Lambda(\pi/4) = 2 \times 4G = 8G$ ✓ (where $\Lambda$ is the Lobachevsky function and $\Lambda(\pi/4) = G/2$)

### Multiple natural tessellations, none privileged a priori

There is no single "right" tessellation. The choice is a **tool choice**, not a structural commitment. Just because a sympy probe or a particular proof uses one tessellation does not mean that tessellation is THE math; only the **invariant** (the Markov trace closed form, the holonomy, the Vol = 8G) is intrinsic. The tessellation is a coordinate system.

| Tessellation | Dimension | Cell count for 𝓑_3 | What it's good for |
|---|---|---|---|
| Epstein-Penner | 3D (complement) | 8 ideal tetrahedra (canonical via cusp horoballs) | Vol via Lobachevsky; Bloch group / K_3 regulators (D16) |
| Yekutieli refinement (framework's 4^k) | 2D (spanning surface) | 4^k at level k (uniform subdivision) | Non-abelian Stokes / Riemann-product holonomy (CBH expansion) |
| Bring icosahedral fundamental domains | 2D (Bring genus-4 surface) | 60 = |A_5| | Torus knots T(p,q) embedding (B1 theorem) |
| Pachner 2-3 refinements (D15) | 3D | 16 tets (Pachner-equivalent to 8 octahedra) | Pentagon identity / TV state-sum |
| Crystal-graph cells (Kashiwara) | algebraic | 1+2+1 = 4 SYTs in H_3(q); Wedderburn blocks 3 | Character / Wedderburn computations |
| Affine-Grassmannian MV cycles | algebraic / geometric Langlands | Open / research | Crystal-basis to geometric correspondence (D19) |
| Habiro-cyclotomic basis | algebraic | per-degree pieces | q → root-of-unity asymptotics |

**Each of these gives the same invariant** (the Borromean Markov trace closed form, or the volume 8G) but reorganizes the computation differently. Working with one tessellation does not commit the framework to it; it just chooses a *coordinate system* in which to express the underlying invariant.

### What this means for the crystal-Yekutieli correspondence

A crystal-basis-to-tessellation correspondence does NOT need to pick a specific geometric carrier. The correspondence to look for is:

**Are crystal-basis cells (algebraic) ↔ contributions to the SAME invariant that any geometric tessellation reproduces?**

If yes, then the geometric carrier is just one realization; the algebraic computation suffices. This is what the framework's existing production path ([`alpha_k_jones_markov_h3.py`](../../computations/alpha/alpha_k_jones_markov_h3.py)) already does: compute $\mathrm{tr}_M$ via the algebraic Wedderburn sum, with no geometric tessellation needed. **The geometric Yekutieli MI computation is a STRUCTURAL alternative used for h-coefficient extraction, not a separate physics input.**

### Recast Path B closure question

Old framing: "compute the h⁶ coefficient by summing over 64 cells of the Yekutieli 2D tessellation."

Reframing (per this audit): "the h⁶ coefficient IS −1/16 by the Markov trace closed form, computed algebraically via the Wedderburn sum. The question of why the algebraic answer is −1/16 (and not some other coefficient) is the same question as why the Markov trace has its closed form — which is a Jones-polynomial fact, not a Yekutieli fact."

**Under this reframing, the 'research-grade ~1 month' Path B closure is a STRUCTURAL question about WHY the Markov trace has the closed form it does** — not a computational question about evaluating cell sums. The closed form is already known; the missing piece is a CATEGORICAL derivation from the Hecke algebra structure (which is what Habiro's work on cyclotomic completion attempts).

This is much more tractable than 3-4 weeks of hyperbolic geometric coding. The path becomes:

1. **(Done)** Algebraic Wedderburn computation of $\mathrm{tr}_M(\beta_{Bor}) = (4+h²−3h⁴−h⁶)/(h²+4)$ — already in framework
2. **(Open, research-grade)** Categorical derivation of WHY this closed form has the specific h-coefficients it does (links to D17 DIM master Pentagon, D16 Bloch group regulator, D15 Pachner-Pentagon)
3. **(Open)** Application to the Higgs T(2,8) — connect P_4(h) / P_2(h) at substrate to the Borromean closed form via the bridge identified

### Probe D — test multiple-tessellation consistency for 𝓑_3

Concretely: verify that DIFFERENT tessellations (any pair from the table above) give the SAME numerical answer at substrate. If they all give $\mathrm{tr}_M(\beta_{Bor}) = (4+h²−3h⁴−h⁶)/(h²+4)$ specialized at $h = q_0 - q_0^{-1}$, that's a consistency check + an explicit demonstration that the tessellation choice is coordinate-free.

**Expected time**: 1-2 hours (the algebraic Wedderburn computation is already done; just need to numerically evaluate at substrate from 2-3 different routes).

**Expected outcome**: positive consistency — confirms tessellation choice is a tool, not a structural commitment. Identifies which route is most COMPUTATIONALLY efficient for the framework's production pipeline.

## §12. Can we relate the 4^k geometric cells to crystal bases easily?

**Short answer**: NOT one-to-one cell ↔ cell, but YES through algebraic compression. The crystal basis (= Wedderburn block basis) is the "naturally pre-compressed" coordinate system for the per-braid evaluation.

### Counting comparison (𝓑_3 / H_3(q))

| Side | Object | Count |
|---|---|---|
| Geometric (Yekutieli 4^k) | quadrisection cells at level k | 1, 4, 16, 64, 256, ... |
| Algebraic (CBH free Lie) | nested commutators at depth k, 2 generators | ~2^k/k |
| Algebraic (Wedderburn) | irreps λ ⊢ 3 = {(3), (2,1), (1,1,1)} | **3 (fixed for all k)** |
| Algebraic (SYT) | Standard Young Tableaux of S_3 | 4 (fixed for all k) |
| Crystal basis vertices | = SYTs by Kashiwara construction | 4 (fixed for all k) |

**4^k diverges; 3 is constant.** No bijection between the 4^k geometric cells and the 3 crystal-basis cells. The compression 4^k → 3 happens at the TRACE level: when you evaluate $\sum_{\text{cells}} (\text{contribution})$ on the geometric side, the result factors through the Wedderburn decomposition, with only 3 distinct block contributions surviving for any braid in H_3(q).

### The compression mechanism

For any braid word $w \in B_3$:

$$\mathrm{tr}_M(w) = \sum_{\lambda \vdash 3} y_\lambda \cdot \chi^\lambda(w)$$

The right-hand side has **3 terms** regardless of how complex $w$ is. The geometric Yekutieli MI computation of $\mathrm{tr}_M(w)$ would naively traverse all 4^k cells at level k, sum the cell contributions via CBH, then evaluate the trace. But the trace EVALUATES on the Wedderburn-block character, which is already encoded by 3 numbers per braid. So **the 4^k cells get summed up by the trace into 3 (in this case) block contributions** — automatically.

This is why the framework's production path ([`alpha_k_jones_markov_h3.py`](../../computations/alpha/alpha_k_jones_markov_h3.py)) doesn't need the geometric Yekutieli computation. It computes the 3 Wedderburn block characters directly and sums them — and gets the same answer.

### "Easy relation" — crystal bases as the natural per-braid coordinate

The crystal basis of H_3(q) at q→0 has 4 vertices (one per SYT). These correspond bijectively to the irreducible matrix elements that appear in any braid word's image. The trace formula evaluates a braid's matrix entries against the 4 crystal-basis labels and weights them appropriately. Every 4^k-cell contribution from the geometric side is captured exactly by these 4 evaluations.

**So the easy relation is**:
- 4^k geometric cells → traced → 3 Wedderburn block contributions ← evaluated on → 4 crystal-basis vertices

The crystal basis is one row "above" the Wedderburn blocks (4 vertices distributed as 1 + 2 + 1 across the 3 blocks). The 4^k geometric cells live "many rows below" — they're the unit of the discretization scheme, not the unit of the algebraic data.

### What this is NOT

This compression doesn't give a CHEAP way to compute the geometric h-coefficient sum cell-by-cell. The compression only works once you ALREADY know the trace structure (which braid you're evaluating). For a general structural question like "what is the h⁶ coefficient of the Borromean Markov trace?", the algebraic side (Wedderburn + characters) gives you the answer in 3 evaluations — but you have to KNOW the trace formula a priori.

For the framework's purposes, this is fine: the trace formula for $\mathrm{tr}_M(\beta_{Bor})$ IS known (closed form), so the algebraic compression is automatic. The "research-grade ~1 month" Path B work was scoped against a HYPOTHETICAL geometric route that the framework doesn't need to take.

### Concrete recipe for using the crystal-Wedderburn shortcut

1. Identify the braid $w$ in $B_n$ (for nucleon-nucleon: a multi-strand braid for the joint system)
2. Compute $\chi^\lambda(w)$ for each $\lambda \vdash n$ using the SYT-labeled basis (Hoefsmit matrices)
3. Sum $\sum_\lambda y_\lambda \chi^\lambda(w)$ with Jones-Markov weights $y_\lambda$
4. Expand in $h = q - q^{-1}$ to extract h-coefficients

This is the framework's existing path. The crystal basis enters at step 2 (SYT labeling of matrix entries). No 4^k geometric cell sum needed.

**Implication for Path B closure**: the missing piece is NOT the geometric integration; it's the categorical derivation of WHY the Wedderburn weights $y_\lambda$ have their specific values for the Borromean. This connects back to D15 (Pachner-Pentagon), D16 (Bloch group), and the q-Langlands D19 — all of which provide independent algebraic routes to the same $y_\lambda$.

## §10. Cross-references

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — full chain
- [`docs/duality-tracker.md`](../duality-tracker.md) §D12 (Kashiwara crystal), §D15 (Pachner-Pentagon), §D16 (K_3/Bloch), §D19 (quantum-Langlands)
- [`docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`](2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md) — jet-grade tessellation table
- [`docs/audits/2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md) — Yekutieli paper + framework mapping
- [`docs/audits/2026-05-24-higgs-residual-research-path.md`](2026-05-24-higgs-residual-research-path.md) §3 Path B — research-grade closure
- [`content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md`](../../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md) — crystal-basis q→0 example in framework
- [`content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md) — the target h-expansion
- [`computations/alpha/alpha_k_jones_markov_h3.py`](../../computations/alpha/alpha_k_jones_markov_h3.py) — existing algebraic Markov-trace computation
- PR [#1227](https://github.com/litlfred/qou/pull/1227) — Path B scaffold (this session)
