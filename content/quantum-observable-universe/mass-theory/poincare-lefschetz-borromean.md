**Conjecture (D21 Poincaré–Lefschetz closure).**
*The Borromean complement $\mathbf{S}^3 \setminus \mathcal{B}_3$
is a 3-manifold with cusps (boundary = 3 disjoint tori).
Poincaré–Lefschetz duality gives a canonical isomorphism:*

$$
  H^k(\mathbf{S}^3 \setminus \mathcal{B}_3, \partial) \;\cong\;
  H_{3-k}(\mathbf{S}^3 \setminus \mathcal{B}_3),
$$

*relating cohomology with boundary support to homology.  In
particular $H^2(\partial \mathcal{B}_3) \cong H_1(\mathbf{S}^3
\setminus \mathcal{B}_3) \cong \mathbb{Z}^3$ (the three meridian
classes around the three Borromean components).  The duality
pairs the volume form (top cohomology) with the fundamental
class (top homology), giving the natural categorical home for
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ as a Poincaré–Lefschetz
pairing.*

## Relationship to D16 Bloch group

The K-theoretic Bloch-group element
([`conj:borromean-bloch-group-element`](#conj:borromean-bloch-group-element), D16)
provides the **regulator** side of the Borromean structure
($r_2[\mathcal{B}_3] = 8G$).  D21 Poincaré–Lefschetz provides the
**topological** side: the volume form $\in$ $H^3$ pairs with the
fundamental class $\in$ $H_3$ to give the volume integral $8G$.

The two ARE the same number ($8G = \mathrm{Vol}(\mathcal{B}_3)$),
but expressed through distinct dualities. D21 IS the
topological-cohomological route; D16 IS the K-theoretic route.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A — manifold-with-boundary duality is at the
  topological level, not at the Hecke-element level.
- **Jet order**: $h^0$ — Poincaré–Lefschetz acts on the leading-
  order topological volume.
- **Bar-symmetry**: bar-symmetric (the duality is independent of
  q-parameter; both sides are classical-topology constructions).

## Open R&D

1. Verify that the Borromean volume $8G$ arises as a Poincaré–
   Lefschetz pairing in Lean — partial Mathlib infrastructure
   exists (Mathlib's `Topology.Manifold` library).
2. Connect to D16 Bloch group: show the regulator $r_2$ and the
   Poincaré–Lefschetz pairing both produce $8G$ via the
   `vol-as-motivic-period` framing.
3. D21 to closed requires Lean class for manifold-with-cusps Poincaré–
   Lefschetz (partial in Mathlib).

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D21
  + paired with D16
- D16 [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
  — K-theoretic regulator route to the same $8G$
- [`prop:reeb-bundle-complement-equals-volume`](#prop:reeb-bundle-complement-equals-volume)
  — Reeb-pairing volume route (third route to $8G$)
- [`rem:vol-as-motivic-period`](#rem:vol-as-motivic-period)
  — motivic framing tying all three routes together
- [Lefschetz 1926; Neumann–Zagier 1985 for cusped 3-manifolds]
