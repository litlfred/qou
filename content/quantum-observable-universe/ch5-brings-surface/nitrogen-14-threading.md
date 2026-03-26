The isobar $A = 14$ provides a clean test of the nuclear threading
link ([nuclear threading link](#def:nuclear-threading-link)).  Two
nuclei compete: $\mathcal{N}(7,7)$ (nitrogen-14, stable) and
$\mathcal{N}(6,8)$ (carbon-14, $\beta^-$-unstable, $t_{1/2} =
5730$ yr).  Both have the same mass number $A = 14$, so their
threading links are the same torus link $T(2,14)$ with the same
braid word

$$
  \hat{\beta}_{14}
  \;=\;
  (\sigma_1 \, \sigma_2 \, \cdots \, \sigma_{13})^2
$$

and the same $26$ crossings.  The difference is entirely in **which
crossings are adjacent** — i.e., the assignment of nucleon species
to strands.

**Strand ordering and adjacent crossings.**

For $\mathcal{N}(7,7)$ ($p = n = 7$), the 14 strands can be
arranged in near-perfect alternation:

$$
  \mathfrak{p},\, \mathfrak{n},\, \mathfrak{p},\, \mathfrak{n},\,
  \mathfrak{p},\, \mathfrak{n},\, \mathfrak{p},\, \mathfrak{n},\,
  \mathfrak{p},\, \mathfrak{n},\, \mathfrak{p},\, \mathfrak{n},\,
  \mathfrak{p},\, \mathfrak{n}.
$$

Every $\sigma_i$ crosses a proton strand over a neutron strand (or
vice versa).  All 26 crossings are **mixed**, each carrying the
baseline Skein weight $\tfrac{1}{2}(q + q^{-1})$.  The Coulomb
excess from the threading link vanishes:

$$
  \mathcal{L}_{\mathrm{Coul}}^{\mathrm{thr}}\bigl(\mathcal{N}(7,7)\bigr)
  \;=\; 0.
$$

For $\mathcal{N}(6,8)$ ($p = 6$, $n = 8$), the neutron excess
$|n - p| = 2$ forces at least 2 same-species adjacencies per
winding.  The optimal ordering has 2 consecutive neutrons
somewhere in the sequence:

$$
  \mathfrak{p},\, \mathfrak{n},\, \mathfrak{p},\, \mathfrak{n},\,
  \ldots,\,
  \mathfrak{n},\, \mathfrak{n},\, \mathfrak{p},\, \mathfrak{n},\,
  \ldots,\,
  \mathfrak{n},\, \mathfrak{n}.
$$

Each $\mathfrak{n}$--$\mathfrak{n}$ adjacency contributes Skein
weight $q^{-1}$ instead of $\tfrac{1}{2}(q + q^{-1})$, an excess
of $-\tfrac{1}{2}(q - q^{-1})$.  Over two windings:

$$
  \mathcal{L}_{\mathrm{Coul}}^{\mathrm{thr}}\bigl(\mathcal{N}(6,8)\bigr)
  \;=\;
  -2 \cdot 2 \cdot \tfrac{1}{2}(q - q^{-1})
  \;=\;
  -2(q - q^{-1}).
$$

The sign is negative (attractive, since
$\mathfrak{n}$--$\mathfrak{n}$ crossings have weight $q^{-1}$ below
baseline), but this is misleading: the **total threading energy**
must be compared.

**Energy comparison.**

The Alexander polynomial of $T(2,14)$ is ($m = 7$):

$$
  \Delta_{T(2,14)}(q)
  \;=\;
  q^6 + q^4 + q^2 + 1 + q^{-2} + q^{-4} + q^{-6}.
$$

At $q = 1.110$: $\Delta \approx 7.18$.  This replaces the pairwise
Alexander weight of $\sim 14$ — a braid shortcut saving of
$\sim 6.8$ Alexander weight units.

The crossing energy of the threaded nucleus decomposes as:

$$
  E_{\mathrm{cross}}^{\mathrm{thr}}
  \;=\;
  \underbrace{\Delta_{T(2,14)}(q) \cdot \lambda_V}_{\text{threading baseline}}
  \;+\;
  \underbrace{\delta_{\mathrm{Coul}}^{\mathrm{thr}}}_{\text{strand-ordering correction}}.
$$

| Nucleus | $p$ | $n$ | Mixed crossings | Same-species | $\delta_{\mathrm{Coul}}^{\mathrm{thr}}$ |
|---------|----:|----:|:---:|:---:|---|
| $\mathcal{N}^{\mathrm{thr}}(7,7)$ | 7 | 7 | 26 | 0 | $0$ |
| $\mathcal{N}^{\mathrm{thr}}(6,8)$ | 6 | 8 | 22 | 4 | $-2(q - q^{-1})$ |

The $\mathfrak{n}$--$\mathfrak{n}$ crossings in $\mathcal{N}(6,8)$
are individually attractive, but this gain is smaller than the Pauli
asymmetry cost $\lambda_A \cdot (n-p)^2/(4A) = \lambda_A/14$ from
the matter sector ([Skein binding Lagrangian](#def:skein-binding-lagrangian)).
The net effect: $\mathcal{N}^{\mathrm{thr}}(7,7)$ is more stable
because it achieves the maximal braid shortcut — **all crossings
mixed, zero Coulomb penalty** — while $\mathcal{N}^{\mathrm{thr}}(6,8)$
pays the Pauli asymmetry cost without adequate compensation from its
attractive $\mathfrak{n}$--$\mathfrak{n}$ pairs.

**Why $\mathcal{N}(7,7)$ is the most stable $A = 14$ isobar.**

In the threading picture, the stability of $\mathcal{N}(7,7)$ has a
transparent geometric origin: $p = n$ is the unique configuration
that allows **perfect alternation** of the two nucleon species on
the braid strands.  Perfect alternation maximises the number of
mixed crossings, which carry no Coulomb excess and no Pauli penalty.
Any departure from $p = n$ (such as $p = 6$, $n = 8$) forces
same-species adjacencies in the braid word, raising the energy.

This is the nuclear analogue of the benzene ring's bond-order
equalisation: just as the braid word
$(\sigma_1 \cdots \sigma_5)^2$ treats all six $\sigma_i$
symmetrically in benzene, the braid word
$(\sigma_1 \cdots \sigma_{13})^2$ treats all 14 crossings
symmetrically in $\mathcal{N}(7,7)$ — but only when the strand
ordering is maximally alternating.

**$\alpha$-cluster substructure.**
Within the threaded nucleus, the $\alpha$-cluster decomposition
([shell correction](#conj:skein-shell-correction)) persists as a
**sub-threading**: $\mathcal{N}(7,7)$ contains
$k = \min(\lfloor 7/2 \rfloor, \lfloor 7/2 \rfloor) = 3$ complete
$\alpha$ clusters $\mathcal{N}(2,2)$, with one proton and one
neutron left over.  The threading link $T(2,14)$ threads through
these 3 $\alpha$ clusters and the 2 remaining nucleons, providing
the non-local correlation that locks them into a single bound state.

Carbon-14 ($\mathcal{N}(6,8)$) has the same $k = 3$ $\alpha$
clusters but with 2 extra neutrons instead of a balanced pair —
the threading through those extra neutrons carries same-species
crossings that break the alternation pattern.

**The braid shortcut principle for nuclei.**

The comparison generalises: for any mass number $A$, the threaded
nucleus $\mathcal{N}^{\mathrm{thr}}(p,n)$ achieves its lowest
energy when $p = n = A/2$ (the **threading ground state**),
because this is the unique strand assignment that permits maximal
alternation.  The beta-stability condition
([beta-stability](#prop:beta-stability)) is thus re-derived from a
purely topological criterion: *minimise the number of same-species
adjacencies in the braid word $(\sigma_1 \cdots \sigma_{A-1})^2$*.
