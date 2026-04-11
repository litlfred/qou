The two-stage Garside construction
([two-stage Garside](#def:two-stage-garside)) is a single
algebraic object: the typed Garside element
$\mathcal{G}_{3A} \in H_{3A}(q)$.  Every physical concept that
appears in nuclear physics — nucleons, confinement, shells, magic
numbers, stability, decay — is **emergent** from this algebra.
Nothing is imposed from outside.

## What the algebra sees

The Iwahori--Hecke algebra $H_{3A}(q)$ sees $3A$ typed strands
with flavors $f_i \in \{u, d\}$ and one parameter $q$.  It does
not know about protons, neutrons, nuclei, or shells.  The typed
crossing operator $C(f_i, f_j; \sigma_m)$ applies the same Hecke
relation $\sigma^2 = (q - q^{-1})\sigma + 1$ at every crossing,
with the coefficient $d(f_i, f_j)$ determined solely by the two
quark flavors.  The Garside staircase processes all
$\binom{3A}{2}$ crossings in the canonical order determined by
the braiding-induced well-ordering
([braiding-induced ordering](#prop:braiding-induced-ordering)).
The result is a unique normal form — an element of $H_{3A}(q)$
with coefficients in $\mathbb{Z}[q, q^{-1}]$.

## What we label

We assign names to patterns that emerge from the normal form:

- **Quark**: a single typed strand ($u$ or $d$).  This is the
  input data — the flavor assignment.

- **Nucleon**: a group of three adjacent strands whose intra-group
  crossings produce a Gröbner--Shirshov normal form that is
  LP-optimal ([confinement LP](#prop:confinement-lp)).  The
  configurations $(u, u, d)$ and $(u, d, d)$ are the ones selected
  by the LP.  We call them proton and neutron.

- **Confinement**: the property that the LP optimum $\mathcal{B}_3$
  is the unique vertex of the feasible polytope.  The algebra
  forces the three quarks into this configuration — there is no
  other LP-feasible confined state.  We label this "confinement"
  but it is simply the LP having a unique solution.

- **Nuclear binding**: the inter-nucleon crossings in the Garside
  staircase.  The NF of the combined element has lower categorical
  action than the product of isolated nucleon NFs.  We label this
  difference "binding energy."

- **Shell structure**: the palindromic pattern in the word-length
  histogram of the NF at certain nucleon counts.  We label these
  counts "magic numbers" and the histogram pattern "shell closure."
  They are properties of the NF, not inputs.

- **Beta decay**: a change of one quark flavor $d \to u$ at a
  specific strand position.  This changes the typed crossings at
  that position and hence the NF.  The energy difference between
  the parent and daughter NFs is the $\mathcal{Q}_q$-value.

## The partition is cosmetic

The "two stages" (intra-nucleon, then inter-nucleon) are our
labeling of which crossings in the Garside staircase connect
quarks within the same group of three versus quarks in different
groups.  The algebra processes them identically — each crossing
is $C(f_i, f_j; \sigma_m) = \sigma_m + d(f_i, f_j)$, regardless
of whether $i$ and $j$ belong to the same nucleon.

If we permuted the quark ordering (interleaving quarks from
different nucleons), the Garside staircase would process the same
set of $\binom{3A}{2}$ crossings in a different order, producing
a different intermediate sequence but the same set of crossings.
The final normal form is unique (Gröbner--Shirshov confluence),
so the NF is independent of the ordering.

The grouping into nucleons is stable because the LP selects
$(u, u, d)$ and $(u, d, d)$ triples as optimal — other groupings
(e.g.\ $(u, u, u)$ or $(d, d, d)$) are not LP-feasible.  The
stability of these groupings is what we call "confinement."  It
is a theorem about the LP, not an assumption about quarks.
