*Resolve each averaged letter of the canonical word of the
[atomic braid](#def:atomic-braid) to a crossing sign (either branch) and
freely reduce. The result is a* **chain form**

$$
  W_A \;=\; \prod_{k=0}^{A-1} \sigma_{3k}^{\,a_k}\,\sigma_{3k+1}^{\,b_k}\,\sigma_{3k+2}^{\,\varepsilon_k}
  \qquad(\text{no } \varepsilon \text{ on the last block}),
$$

*each generator appearing exactly once, in order, as a single power, with
$a_k$ odd, $b_k$ even and non-zero, and $\varepsilon_k = \pm 1$. Consequently
its closure is the linear connected sum of the torus links $T(2, e_i)$ along
shared strands: $A$ knots $T(2, a_k)$ and one unknot, consecutive components
linked with $\mathrm{lk} = b_k/2$; the $A-1$ interface generators are
connected-sum bands with the unknot and drop out, leaving the $(2A+1)$-strand
chain $W'_A = \prod_k \sigma_{2k}^{a_k}\sigma_{2k+1}^{b_k}$ with the same
closure. Hence*

$$
  \mu = A+1,\qquad \#\{\text{knotted components}\} = A,\qquad b(L) = 2A+1,
  \qquad \inf_{\text{isotopy class}} \int \kappa\, ds \;=\; 2\pi\,(2A+1).
$$

## The exponents

Read off the [canonical interface composition](#def:canonical-braid-interface-composition)
block by block (verified for every isotope through $A = 12$ on both branches):

| | $a_k$ (generator $3k$) | $b_k$ (generator $3k+1$) | $\varepsilon_k$ (interface $3k+2$) |
|---|---|---|---|
| averaged $\to \sigma$ | $7$ for every nucleon | $-2$ (proton), $-4$ (neutron) | $+1$ ($pp$), $-1$ ($nn$), $+1$ ($pn$) |
| averaged $\to \sigma^{-1}$ | $5$ (proton), $3$ (neutron) | $-4$ for every nucleon | $+1$ ($pp$), $-1$ ($nn$), $-1$ ($pn$) |

So on the $\sigma$ branch every knotted component is $T(2,7)$; on the
$\sigma^{-1}$ branch protons give $T(2,5)$ and neutrons $T(2,3)$. The linking
graph is the path with $\mathrm{lk}(k, k+1) = b_k/2 \in \{-1, -2\}$, the
sublinks of consecutive pairs are *not* $(2, 2\,\mathrm{lk})$-torus links, and
the components are not unknots -- which is a second, independent reason the
Borromean (Brunnian) picture does not describe this closure.

## Proof

*Chain form.* Each nucleon block uses generator $3k$ seven times and generator
$3k+1$ four times, in that order, and the interface to the next block is the
single generator $3k+2$; resolving and freely reducing gives the table.

*Connected sum.* A closed braid whose word is a product of sub-words on strand
sets overlapping in exactly one strand is the connected sum of the closures of
the sub-words along that strand \cite{birman1974}; iterating gives the linear
chain of $T(2, e_i)$. Since $T(2, \pm 1)$ is the unknot and a connected sum
with the unknot is the identity, each $\sigma_{3k+2}^{\pm 1}$ can be deleted
and the indices closed up: $W'_A$ has the same closure.

*Bridge number.* A closed $n$-braid is an $n$-bridge presentation, so
$b(L) \le 2A+1$. Each $T(2, a_k)$ with $a_k \ge 3$ odd has bridge number $2$
and the unknot has $1$; bridge number is at least the sum over components, so
$b(L) \ge 2A + 1$.

*Curvature.* Milnor \cite{milnor1950}: the infimum of total curvature over an
isotopy class equals $2\pi$ times the bridge number. (Under Crofton, total
curvature is $\pi$ times the average number of critical points of the height
functions -- the oscillation count, integrated -- which is where the
serpenoid picture that prompted this result becomes exact.)

## What is formalised, what is checked, what is cited

`QOU.Mass.TorusKnotPages` carries the algebra: the Seifert form
of $T(2,n)$ is unimodular for every odd $n$; the continuant of $V - X V^{\mathsf T}$
satisfies $(X+1) D_{2g} = X^{2g+1} + 1$, so the Alexander polynomial is
$(X^n+1)/(X+1)$ and divides $X^{2n}-1$; the floor $2A+1 \le b \le 3A$ is
bookkeeping from $\mu = A+1$ and $A$ knotted components.
The chain form and its exponents are verified exactly for $A \le 12$, and the
symbolic predictions -- components, knot types, linking, and that $W'_A$ closes
to the same link (Jones polynomial and per-component Jones) -- for $A \le 4$,
by `the_canonical_closure_is_a_chain_of_torus_links_probe.py`; the
computational instance at $A \le 6$ via Reidemeister simplification and
Vogel's algorithm is `the_curvature_floor_is_sharp_probe.py`. Not formalised:
the two topological facts above, Milnor's theorem, and the identification of
the components from their Jones polynomials.

## Scope

Everything here is per classical branch: the canonical Hecke element is not a
link, its $2A+1$ averaged letters have no crossing sign, and a statement about
the un-resolved object does not exist. Nothing here connects curvature to
binding, and nothing supplies the twist: the osculating circle sees $\kappa$
and is blind to $\tau$, and the framing datum the binding gap needs lives in
the torsion.
