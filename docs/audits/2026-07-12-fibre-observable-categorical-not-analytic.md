# The fibre→observable passage is categorical / algebro-geometric, not analytic continuation

**Date:** 2026-07-12 · **Axis:** s5-so3 keystone geometric `W_λ`, continuation frontier ·
**Follow-up to** #3662 (gate de-opaqued) + #3677 (fibre residue) · **No fit; no physics claim.**

## Why this note exists

#3677 pinned the surviving residue of the de-opaqued gate `bwS0_eq_hecke` to a *passage*: the
geometric colored-WRT amplitude `bwS0Concrete = S_{0λ}·θ_λ^{f}` realizes the Verlinde measure
`W_λ = ‖S_{0λ}‖²` at the **fibre root of unity** `‖q‖=1` (where the ribbon twist `θ_λ=q^{c(λ)}` is a
phase and its framing cancels in the squared modulus), while at the **observable** substrate
`q₀>1` the framing does not cancel. The naive way to read that passage is *analytic continuation*
of a `q`-series from `‖q‖=1` to `q₀`. **That framing is wrong for this framework** — and, more to the
point, it is not how mathematics has learned to think about "continuation." This note records the
correct categorical / algebro-geometric framing and the three formalize-first carriers that state it.

The framework's own convention already refuses the analytic reading: AGENTS.md's *fibre-vs-observable
`q`* rule says the fibre object lives at formal / root-of-unity `q` (pre-`τ`, `Im q` unconstrained) and
the observable is its **archimedean functor** `τ_∞` evaluation at `q₀` (post-`τ`, `Im q₀=0`). `τ_∞` is
a **functor**, not a limit of paths.

## Analytic continuation *is* a categorical concept — the five reframings

"Reframe analytic continuation as a categorical question" is not speculative; it is one of the load-
bearing achievements of 20th–21st century geometry. Five reframings, ordered by relevance to QOU:

### 1. Riemann–Hilbert / Stokes — the one native to this framework

The analytic continuation of the solutions of a linear connection `∇` is its **monodromy**: continue a
solution around a loop, you return to a linear combination of solutions — the monodromy
representation `π_1 → GL(V)`. For a *regular-singular* connection the Riemann–Hilbert correspondence is
an equivalence of categories

  {regular-singular `𝒟`-modules on `X`}  ≃  {local systems on `X`}  =  {reps of `π_1(X)`},

so "continue this function" becomes "apply the monodromy operator" — a morphism in a category, with
no limits. For an **irregular** connection (which is the generic case for `q`-difference / `q`-KZ /
quantum-dilogarithm `Φ_q` equations) the resummation of the divergent formal solutions *across a
Stokes ray* is the extra datum, and Deligne–Malgrange–Mochizuki–Sabbah upgrade the correspondence to

  {`𝒟`-modules}  ≃  {**Stokes-filtered** local systems}.

The Stokes automorphisms — the discrete jumps of the Borel-resummed solution as one crosses a Stokes
line — are the categorified content of "analytic continuation of a divergent series." **This is the
non-abelian Stokes kernel the QOU framework is built on** (`nonabelian_stokes_surface_boundary_stokes`,
the na-Stokes period `a_D^{(n)}=S(n)/n` that opened this whole line of work). The fibre→observable
passage for `bwS0Concrete` is therefore not a continuation to be *performed*; it is the **Stokes /
monodromy datum of the underlying `q`-difference connection**, already a categorical object.

Concretely in the corpus: `BringWPlaneMonodromy` formalizes the **Gauss–Manin monodromy** `M` of the
elliptic curve `E = Bring/S₄` along the `S³/2I` Seifert fibration, with the depth-2 recurrence kernel
`x²−τx+1` proved to be its Cayley–Hamilton relation (`τ=tr M`, unimodularity forced by the symplectic
`H¹`). The `θ_λ^{f}` framing of `bwS0Concrete` is precisely a monodromy/twist eigenvalue of this
connection — the RH picture makes "how does the fibre value continue to `q₀`" into "what does the
Gauss–Manin monodromy do to the `λ`-graded piece", a categorical question about `M`, not an analytic
one.

### 2. Tannakian / differential Galois

The category of solutions of `∇` with its `⊗`-structure and a fibre functor `ω` (evaluate at a base
point) is Tannakian; its automorphism group `Aut^⊗(ω)` is the **differential Galois group**, and the
monodromy sits inside it (Schlesinger density). "Continue to another base point `x'`" is the natural
transformation `ω_x ⇒ ω_{x'}` — a *torsor* under the Galois group. QOU is Tannakian **by construction**
(`(𝐂, τ)`, the rigid monoidal category with fibre functor `τ`), so the fibre→observable passage is a
change of fibre functor `τ_{ζ} ⇒ τ_{q₀}` — an arrow in the framework's founding structure.

### 3. Motivic — periods and the motivic Galois group

Quantum knot invariants / WRT values are (conjecturally) **periods**; a root-of-unity value and the
`q₀` value are two **realizations of one motive** (Betti vs de Rham vs `ℓ`-adic vs archimedean),
intertwined by the motivic Galois group. There is no path to continue along — there is one motive with
several realization functors. Corpus threads: `MotivicSubstrate`, `AdelicSubstrate`,
`MotivesArchimedean`, and the cyclotomic-period files (`Cl3Zeta5*`, `BringTrilog*`,
`JonquiereCyclotomicTateRationality`). `RealisationVolumeCompatibility` is meant to be exactly the
statement that the **archimedean realization `τ_∞` and the topological/motivic realization `R_top`
agree** on QOU volume classes — the motivic incarnation of the passage.

### 4. Resurgence / alien calculus (Écalle)

Borel–Laplace resummation of a divergent series, and its jumps across Stokes lines, are governed by the
**alien derivations**, which form a (pro-)Lie algebra / the Stokes automorphisms form a group. "Continue
the divergent series past its singularity" becomes an *algebraic* action of that group. Corpus:
`BorelResummation`, `PhiQConvergence`.

### 5. Habiro ring / cyclotomic completion — the purely algebraic home

Habiro's ring `ℤ[q]^ = ⟵lim_n ℤ[q]/((q;q)_n)` is the completion in which WRT invariants of integer
homology spheres live. Its defining miracle (Habiro): the **evaluation map to the product over all
roots of unity is injective** — an element is *determined* by its root-of-unity values. So there is
**nothing to continue**: the algebraic element already carries a well-defined value at every root of
unity *and* a Taylor expansion at `q=1`, related by the cyclotomic structure, and "the value at `q₀`"
is an algebra homomorphism `ℤ[q]^ → ℝ`, not an analytic limit. Corpus: `ZHabiroCauchy`
(`ℤ[q^±1][z]/(P_n)`, the algebraic Cauchy-limit half of `conj:brane-tower-z-habiro`),
`PhiQConvergence`, `PhiQTowerAlgebraicStratification`, `HabiroNewtonLadder`.

## The correct statement of the residue (replacing "analytic continuation")

Assembling 1–5, the open object left by #3677 is stated **without any analytic continuation**:

> `W_λ(q₀)` is the **archimedean functor `τ_∞`** (equivalently: the `q₀`-evaluation algebra map on the
> `z`-Habiro ring) applied to a Habiro-ring element `𝔴_λ` whose **root-of-unity values are the
> colored-WRT amplitudes** `bwS0Concrete`. By **Habiro rigidity** (injectivity of root-of-unity
> evaluation) `𝔴_λ` — hence its `q₀` value — is *uniquely determined* by that fibre data. The
> `θ_λ^{f}` framing is the **Gauss–Manin/Stokes monodromy datum** of the `Φ_q`/`q`-KZ connection
> (`BringWPlaneMonodromy`), categorified by Riemann–Hilbert; it is not a phase one analytically
> continues.

This converts the frontier from an **analytic** question ("does the continuation exist / converge")
into an **algebro-geometric** one ("does the specific WRT Habiro element's `τ_∞`-evaluation at `q₀`
equal `W_λ(q₀)`") — with rigidity supplying *uniqueness for free*, so no fit is possible in principle:
the answer is forced by the fibre data, it cannot be tuned.

## The three formalize-first carriers (this tranche)

1. **`RealisationVolumeCompatibility` de-vacuified** — the placeholder `∃V, V=V` (`use 0,0,0`) is
   replaced with a content-bearing statement that the archimedean realization `τ_∞` and the
   topological/motivic realization `R_top` are two maps that must *agree* on a volume datum (the
   motivic reframing, §3 above), non-vacuous via an explicit model — never `∃V,V=V`.
2. **Habiro rigidity for the residue** — a §3b conjecture class carrying: *if* `bwS0Concrete`'s
   root-of-unity values extend to a `z`-Habiro element, *then* its `q₀` value is unique (the
   injectivity §5). Content-bearing (a parameter-quantified equality-of-evaluations claim, not an empty
   marker); a conditional uniqueness theorem is derived from it sorry-free.
3. **Riemann–Hilbert / Stokes framing** — a §3b class stating the fibre↔observable passage as the
   action of the Gauss–Manin/Stokes monodromy `M` (`BringWPlaneMonodromy`) on the `λ`-graded twist
   `θ_λ^{f}`, i.e. the categorical monodromy that *replaces* continuation (§1). The explication above is
   the substance; the class is its formal shadow.

## Scope (STRICT — anti-laundering)

These **reframe**; they do **not** close the gate. Per AGENTS.md §"Axiomatization is NOT a Proof": a
§3b class is not a proof, and none of these unlocks any physics or wires any constant. What they buy is
honest and real: they replace the wrong (analytic) framing with the framework-native categorical one,
de-vacuify a placeholder, and state the residue as an algebro-geometric rigidity question in which a
fit is *structurally impossible* (the fibre data determines the `q₀` value). The geometric `W_λ` index
— the identification of `𝔴_λ` with the actual `S³/2I` WRT element — remains owner-gated. No fit.
