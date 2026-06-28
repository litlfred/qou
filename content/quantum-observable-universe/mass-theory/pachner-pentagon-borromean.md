**Conjecture (D15 Pachner-Pentagon closure).**
*The Pachner $2$–$3$ move on the ideal-tetrahedron decomposition of
the Borromean complement $\mathbf{S}^3 \setminus \mathcal{B}_3$
realises the Pentagon identity for the q-dilogarithm $\Phi_q$ at the
state-sum level (Turaev–Viro / Reshetikhin–Turaev), with the
$h^4 = -3/4$ coefficient of $\mathrm{tr}_M(\mathcal{B}_3)$ derivable
as the difference between the 8-octahedron and 16-tetrahedron
decompositions under the Pachner move.*

## The geometric Pentagon

The Borromean complement is hyperbolic with explicit ideal
decompositions:

- **8 ideal octahedra** (Thurston): $\mathbf{S}^3 \setminus
  \mathcal{B}_3 \cong 8 \cdot (\text{ideal octahedron of volume } G)$
  giving $\mathrm{Vol}(\mathcal{B}_3) = 8G$
  ([`prop:vol-through-tau`](#prop:vol-through-tau),
  [neumann-zagier1985]).
- **16 ideal tetrahedra**: each ideal octahedron splits into
  2 ideal tetrahedra via the Pachner $2$–$3$ move; total
  $8 \times 2 = 16$ ideal tetrahedra, each contributing
  $\Lambda(\theta)$ (Lobachevsky) such that $\sum \Lambda = 8G$.

The Pentagon identity for Lobachevsky / Rogers dilogarithm relates
these two decompositions: under Pachner, five ideal-tetrahedron
configurations map cyclically via a 5-term identity that IS the
Faddeev–Volkov–Kashaev Pentagon
([`prop:pentagon-uv-commutation`](#prop:pentagon-uv-commutation))
in its archimedean realisation
([`prop:q-rogers-pentagon-archimedean`](#prop:q-rogers-pentagon-archimedean)).

## Pachner $\leftrightarrow$ Pentagon at the state-sum level

For a Turaev–Viro / Reshetikhin–Turaev state sum $Z(M; q)$ on a
3-manifold $M$ with ideal-tetrahedron triangulation $T$:

$$
  Z(M; q)
  \;=\;
  \sum_{\text{coloring}}
    \prod_{\tau \in T} \Phi_q(\text{state}(\tau)),
$$

where $\Phi_q$ is the quantum dilogarithm
([`prop:quantum-dilogarithm-stratified`](#prop:quantum-dilogarithm-stratified)).

**Pachner invariance** means $Z(M)$ does not depend on the choice of
triangulation $T$.  The $2$–$3$ move (replace 2 tetrahedra with 3
tetrahedra sharing a common edge) preserves $Z(M)$ iff $\Phi_q$
satisfies the Pentagon identity — this is the **categorical content
of the Pachner-Pentagon link**.

## The conjectural content

Given:

- $\Phi_q$ obeys the Pentagon identity (proved per
  [`prop:pentagon-uv-commutation`](#prop:pentagon-uv-commutation))
- $\mathcal{B}_3 \setminus \mathbf{S}^3$ has both 8-octahedron and
  16-tetrahedron triangulations connected by Pachner moves
- $\mathrm{tr}_M(\mathcal{B}_3, q)$ has $h^4 = -3/4$ as the first
  non-trivial coefficient (proved in
  [`prop:borromean-markov-trace-closed-form`](#prop:borromean-markov-trace-closed-form))

**Conjecture**: the $h^4 = -3/4$ coefficient is the Pachner-invariant
$\Phi_q$ state-sum evaluation of the 16-tetrahedron decomposition,
expressible as

$$
  h^4 = -3/4
  \;\stackrel{?}{=}\;
  \frac{Z(\mathcal{B}_3; q)\big|_{h^4 \text{ coefficient}}}
       {\mathrm{tr}_M(\mathcal{B}_3, q)\big|_{h^0 \text{ coefficient}}}.
$$

If true, $h^4 = -3/4$ is **identified categorically** with the
8 octahedra $\times$ 5 Pentagon-vertices = 40 Pentagon-coherent state
contributions on the Borromean complement, of which 30 cancel by
trace cyclicity and 10 sum to $-3/4$.  (The "10" matches the
10-fold color-tube weighted averaging from
[`docs/canonical-derivation-cheat-sheet.md §"Bring color-tube weighted averaging"`](../../docs/canonical-derivation-cheat-sheet.md)
— possibly the same categorical structure viewed from two angles.)

## High-value $h^{4}$ cross-validation route

Per
[`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
§3, the Pentagon literature spans 8 disciplines.  Four candidate
routes for deriving $h^4 = -3/4$ categorically are flagged:

1. **Direct Borromean Markov trace** — already done
   ([`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form)).
2. **Pachner-Pentagon state-sum** (this conjecture).
3. **K-theoretic / Bloch group regulator** — see sibling
   [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md) (D16).
4. **DIM-master Pentagon** — research-grade, no QOU block yet.

Closing this conjecture provides an **independent cross-validation**
of the topological $h^4$ via the geometric Pentagon.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: state-sum is computed over the
  triangulation poset; the Pentagon identity sits at the 5-vertex
  cell level (= Coxeter length 5 in the corresponding braid-word
  encoding via [`prop:exterior-square-borromean`](#prop:exterior-square-borromean)).
- **Jet order**: $h^4$ — the load-bearing claim is that the
  Pachner-invariant $\Phi_q$ state-sum agrees with the Markov-trace
  closed form at $h^4$ order.
- **Bar-symmetry status**: bar-symmetric.  Pentagon identity is
  bar-symmetric (Pachner-invariance is symmetric under
  $q \mapsto q^{-1}$ because both decompositions transform
  identically under bar).

## Lean axiomatisation (sketch)

```lean
class PachnerPentagonBorromean
    (M : Type*) [BrCategory M] [QuantumDilogarithm M] where
  /-- The state-sum evaluation on a 3-manifold triangulation. -/
  z_state_sum : ∀ (M : Manifold3) (T : Triangulation M), Quantum
  /-- Pachner 2-3 invariance: ∀ T, T' related by 2-3 moves,
      z_state_sum M T = z_state_sum M T'. -/
  pachner_invariance :
    ∀ (M : Manifold3) (T T' : Triangulation M),
      pachner_related T T' → z_state_sum M T = z_state_sum M T'
  /-- Pentagon identity for Φ_q (already proved upstream). -/
  phi_q_pentagon : ∀ (a b c : Quantum), pentagon_identity a b c
  /-- The Borromean state-sum h^4 coefficient agrees with the
      Markov-trace closed form. -/
  borromean_h4_pachner_eq_markov_trace :
    z_state_sum_h4_coeff borromean_triangulation = -3/4
```

## Open R&D

1. **Compute prototype**: extend a Pachner-state-sum probe for
   $\mathcal{B}_3$ at $q = q_0$; cross-check $h^4$ coefficient via
   the Lobachevsky decomposition $8G = \sum \Lambda(\theta_i)$.
2. **D15 to closed** requires the Lean class + the
   `borromean_h4_pachner_eq_markov_trace` proof (which would
   likely import a Lobachevsky-Pentagon lemma).
3. **Connect to D16** (sibling): the Bloch-group element of
   $\mathcal{B}_3$ in $K_3(\mathbb{C})$ has regulator $r_2 = 8G$;
   the Pachner-Pentagon state-sum and the K-theoretic regulator
   should agree at $h^4$ — that would be a triple cross-validation.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D15
  + §2 Cluster C (Pentagon validation D15-D18)
- [`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
  — 8-literature Pentagon catalogue, 4 candidate routes
- Sibling Cluster C item:
  [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md) (D16)
- The Pentagon identity itself:
  [`prop:pentagon-uv-commutation`](#prop:pentagon-uv-commutation),
  [`prop:q-rogers-pentagon-archimedean`](#prop:q-rogers-pentagon-archimedean)
- The Borromean structure: [`def:borromean-baryon`](borromean-baryon.md),
  [`prop:exterior-square-borromean`](#prop:exterior-square-borromean)
- The volume route: [`prop:vol-through-tau`](#prop:vol-through-tau),
  [`prop:reeb-bundle-complement-equals-volume`](#prop:reeb-bundle-complement-equals-volume)
