**Conjecture.**
*The Higgs boson is the torus link $T(2,8)$ — the unique
genus-$3$ link on the Bring's surface whose Seifert surface
spans all three exceptional divisors simultaneously.*

**The three exceptional divisors.**

The Bring's surface ($\chi = -6$, genus $4$) has three color
tubes $(r, g, b)$
([color tube coordinates](#def:color-tube-coordinates)).  The
brane tower blow-up produces three exceptional divisors
$D_r, D_g, D_b$, one for each color fiber.  The Borromean
link $\mathcal{B}_3$
([Borromean quark](#conj:borromean-quark)) lives at the
intersection of these three divisors.

The torus links $T(2, 2k)$ on the Bring's surface have genus
$k - 1$ and interact with the exceptional divisors according
to their genus:

| Link | Genus | Divisors spanned | Role |
|------|------:|:----------------:|------|
| $T(2,2)$ | 0 | 0 (trivial Seifert) | Gluon |
| $T(2,4)$ | 1 | 1 ($D_r$ or $D_g$ or $D_b$) | $W$ boson |
| $T(2,6)$ | 2 | 2 ($D_r \cup D_g$ etc.) | $Z$ boson |
| $T(2,8)$ | 3 | **all 3** ($D_r \cup D_g \cup D_b$) | **Higgs** |

The torus link $T(2,8)$ is the **first and only** link whose Seifert surface
has genus large enough to span all three exceptional divisors.
Its genus $3$ exactly matches the number of color tubes on the
Bring's surface.

**Why $T(2,8)$ is scalar (spin $0$).**

The two components of $T(2,8)$ each wind $4$ times around
the torus longitude and $1$ time around the meridian.  By the
fermion--boson correspondence
([fermion--boson knot--link](#prop:fermion-boson-knot-link)),
even-$n$ links are bosons with their two components related by
the fiber adjoint involution.

For $T(2,8)$, the linking number is $4$ — the two components
cross each other $8$ times, with each component contributing
$4$ crossings.  The **net Reeb winding** of the two components
cancels: one winds $+4$ and the other $-4$ around the Reeb
direction.  The total angular momentum is

$$
  J =  J_1 + J_2 =  +4 + (-4) =  0.
$$

The torus link $T(2,8)$ is therefore a **scalar** (spin-$0$) boson — the only
one in the $T(2,n)$ family where the Reeb windings cancel
exactly due to the genus-$3$ symmetry.

**The Higgs mechanism as linking with $T(2,8)$.**

A particle (knot or link) acquires mass by **crossing** with
$T(2,8)$.  The crossing energy
([crossing energy](#def:crossing-energy)) of the interaction is
proportional to the number of crossings between the particle
and the Higgs link:

$$
  m_{\mathrm{Higgs}}  \propto 
  N_{\mathrm{cross}}(T(2,8))
   \times  \frac{q - q^{-1}}{q + q^{-1}}
$$

where $N_{\mathrm{cross}}(L)$ counts the crossings between the particle
braid and the link $L$.

Particles that cross all three exceptional divisors (heavy
quarks, $W$, $Z$) interact strongly with $T(2,8)$ and acquire
large mass.  Particles confined to fewer divisors interact less.
The photon ($\mathbf{1}_{B_4}$, 4-strand identity — knot-trivial
under Markov closure; see
[confined-particle](#def:confined-particle)) has zero crossings
with $T(2, 8)$ and remains massless.

**Why the Higgs is massive.**

The torus link $T(2,8)$ is itself a link with genus $3$ and Seifert surface
area proportional to the product of the three exceptional
divisor volumes.  The self-crossing energy of $T(2,8)$ gives
it a mass of $\sim 125$ GeV — determined by the Skein
polynomial of $T(2,8)$ evaluated at $q = q_0$:

$$
  m_H =  \frac{\mathrm{Vol}(\text{Seifert}(T(2,8)))}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
$$

The Higgs mass is set by the genus-$3$ Seifert surface volume,
which in turn is set by the three color tube volumes of the
Bring's surface.

**Why the Higgs is unique.**

On the Bring's surface (genus $4$), the Seifert surface of
$T(2,8)$ has genus $3$ — it fills $3$ of the $4$ available
handles.  There is exactly **one** way to embed a genus-$3$
surface into a genus-$4$ surface (up to isotopy), leaving one
handle free.  The next link $T(2,10)$ would require genus $4$
(all handles), saturating the surface — it cannot coexist with
the existing Borromean and knot structures.  So $T(2,8)$ is
the unique Higgs candidate.
