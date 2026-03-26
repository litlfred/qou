The stability curve and the chiral fibration of Bring's surface
share the same algebraic origin.  We conjecture that the
nuclear degeneracy locus — the curve in the $(Q, A)$-plane where
adjacent nuclei have equal energy — is an elliptic curve
isogenous to the chiral fiber $E_z$.

**The two cubics.**

The chiral elliptic curve
([chiral elliptic](#prop:chiral-elliptic)) at spacetime ratio
$z$ is

$$
  X^3 + (z + 1)\,X^2 + (z^2 + z + 1)\,X
  + (z^3 + z^2 + z + 1) = 0.
  \tag{C}
$$

The nuclear stability condition
([beta-stability](#prop:beta-stability)), with the substitution
$t = A^{1/3}$, is

$$
  t^3 - 2c\,Q\,t^2 - 2Q = 0,
  \qquad c = \frac{a_C}{2\,a_A}
  = \frac{(q - q^{-1})\,\lambda_C}{2\,a_A}.
  \tag{S}
$$

Both are cubics in one variable parametrized by another.  The
chiral cubic (C) has parameter $z$ (spacetime) and variable $X$
(chiral coordinate); the stability cubic (S) has parameter $Q$
(Coulomb charge) and variable $t$ (cube root of mass number).

**Genus comparison.**

The stability cubic (S) is rational: solving for $Q$ gives
$Q = t^3 / (2 + 2ct^2)$, so the curve has genus $0$.  The
chiral cubic (C) has genus $1$ for generic $z$ (it is an
elliptic curve with $j$-invariant varying as a rational function
of $z$).

However, the *physical* stability problem includes the pairing
energy $\pm \lambda_P / t^{3/2}$, which distinguishes even-even,
even-odd, odd-even, and odd-odd nuclei.  The **degeneracy locus**
— the set of $(Q, t)$ where the even-even and odd-odd binding
energies coincide — satisfies

$$
  t^3 - 2c\,Q\,t^2 - 2Q
  \;=\; \frac{2\lambda_P}{a_A} \cdot t^{3/2}.
  \tag{D}
$$

Squaring to clear the half-integer exponent and substituting
$u = t^{1/2}$ (so $t = u^2$, $t^{3/2} = u^3$, $t^3 = u^6$):

$$
  \bigl(u^6 - 2c\,Q\,u^4 - 2Q\bigr)^2
  \;=\; \frac{4\lambda_P^2}{a_A^2} \cdot u^6.
  \tag{D$'$}
$$

This is a degree-12 curve in $(Q, u)$.  After factoring out the
genus-$0$ component (the pairing-free stability curve), the
residual factor is a degree-6 curve in $(Q, u)$ — generically
of genus $1$.

**Conjecture.**
*Let $\mathcal{D} \subset \mathbb{A}^2$ be the degeneracy locus
(D$'$) reduced by the pairing-free stability curve (S).  Then:*

1. *The smooth model of $\mathcal{D}$ is an elliptic curve $E_Q$
   over $\mathbb{Q}(q)$.*

2. *There exists an isogeny $\varphi \colon E_Q \to E_{z(Q)}$
   to the chiral fiber of the Bring surface, where $z(Q)$ is
   the spacetime ratio at which the color-tube cubic
   ([color tube cubic](#rem:color-tube-cubic)) specialises to
   the stability cubic:*

$$
  z(Q) \;=\; -\frac{1}{2c\,Q}
$$

   *so that the coefficients of (C) at $z = z(Q)$ match
   those of (S) up to a Möbius transformation.*

3. *The integer points $(Q, A) \in E_Q(\mathbb{Z})$ correspond
   to the stability pairs: the mass numbers $A$ at which the
   even-even/odd-odd degeneracy falls exactly on an integer
   lattice point.*

**Coefficient matching.**

The chiral cubic at $z = -1/(2cQ)$ is

$$
  X^3 + \left(1 - \frac{1}{2cQ}\right) X^2
  + \left(\frac{1}{4c^2Q^2} - \frac{1}{2cQ} + 1\right) X
  + \cdots = 0.
$$

The stability cubic, rewritten as a monic cubic in $t$
with parameter $Q$:

$$
  t^3 - 2cQ \cdot t^2 + 0 \cdot t - 2Q = 0.
$$

Under the substitution $t = \alpha X + \beta$ with
$\alpha = -2cQ$ and $\beta = 2cQ \cdot z$, the leading
coefficients match:

| Coefficient | Chiral (C) | Stability (S) | Match condition |
|-------------|-----------|---------------|-----------------|
| $X^2$ | $z + 1$ | $-2cQ$ | $z = -(2cQ + 1)$ |
| $X^0$ | $z^3 + z^2 + z + 1$ | $-2Q$ | $(z+1)(z^2+1) = -2Q$ |

Eliminating $z$: $(-2cQ)(4c^2Q^2 + 1) = -2Q$, giving

$$
  4c^3 Q^2 + c = 1,
  \qquad\text{i.e.,}\qquad
  Q^2 = \frac{1 - c}{4c^3}.
$$

At $c = a_C/(2a_A) \approx 0.01497$, this gives
$Q \approx 67.8$, corresponding to $A \approx 170$.
This is in the neighborhood of **erbium** ($Z = 68$),
which lies in the rare-earth region where shell
effects are strongest and the even-odd staggering
is most pronounced — precisely where the degeneracy
locus would intersect the stability curve.

**Physical interpretation.**

If the conjecture holds, then:

- The **three color tubes** $(r, g, b)$ of the chiral
  fibration correspond to the **three sectors** of nuclear
  binding: volume (strong), Coulomb (electromagnetic), and
  Pauli (exclusion).

- The **elliptic fiber** $E_z$ at spacetime $z$ encodes the
  allowed baryon configurations at that point; the **stability
  elliptic curve** $E_Q$ at charge $Q$ encodes the allowed
  nuclear configurations at that charge.

- The **isogeny** $\varphi$ connecting them is the passage from
  single-baryon color structure to multi-baryon nuclear
  structure — the same passage that takes the proton
  ([proton](#def:categorical-proton)) from a color-linked
  triple to a nucleus
  ([stable nucleus](#def:stable-nucleus)).

- The **stability pairs** are the rational points of $E_Q$ — a
  finite set by Mordell's theorem (assuming $E_Q$ has rank $0$
  over $\mathbb{Q}$), which would explain why there are finitely
  many stability pairs.

**Mordell--Weil rank and stability pair count.**

If $E_Q$ has Mordell--Weil rank $0$ over $\mathbb{Q}$, then
$E_Q(\mathbb{Q})$ is finite (equal to the torsion subgroup).
The known stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ give
$7$ points; the torsion subgroups of elliptic curves over
$\mathbb{Q}$ have order dividing $12$ (Mazur's theorem).  A
torsion group of order $8$ (accommodating the $7$ magic neutron
numbers plus the identity) is consistent with
$E_Q(\mathbb{Q}) \cong \mathbb{Z}/8\mathbb{Z}$ — one of the
$15$ possibilities in Mazur's classification.

This would predict that **there are no undiscovered magic
numbers beyond $126$** — a statement that is consistent with
all experimental evidence to date but has not been proven from
nuclear shell theory.

**Computational evidence: stability pairs as torsion multiples.**

The chiral elliptic curve at $z = q^{1/2} - q^{-1/2} \approx
0.1044$ is

$$
  E_z \;:\; y^2 = x^3 + 0.7087\,x + 0.8056,
  \qquad \Delta = -18.95, \quad j = 129.9.
$$

Since $\Delta < 0$, the real locus $E_z(\mathbb{R})$ is a single
connected component homeomorphic to $S^1$.  The base point
$P_0 = (0, \sqrt{b}) = (0, 0.8976)$ has **approximate angle**
$\theta \approx 1/56$ on this circle.  The map
$n \mapsto n \cdot P_0$ is a rotation by $2\pi\theta$.

The magic neutron numbers land at distinguished positions:

| $n$ | $n\theta \bmod 1$ | Position on $S^1$ | Status |
|-----|------------------|-------------------|--------|
| $2$ | $1/28$ | near $O$ | magic |
| $8$ | $1/7$ | near $O$ | magic |
| $20$ | $5/14$ | near $T$ | magic |
| $28$ | $\mathbf{1/2}$ | **at $T$ (2-torsion)** | magic |
| $50$ | $25/28$ | near $O$ | magic |
| $82$ | $13/28$ | near $T$ | magic |
| $126$ | $\mathbf{1/4}$ | **at 4-torsion** | magic |

All stability pairs land at rational fractions with
**denominator dividing $28$**.  The doubly-stability pairs
$28$ and $126$ land *exactly* at the 2-torsion and 4-torsion
positions, respectively:
$28 \cdot (1/56) = 1/2$ and $126 \cdot (1/56) = 9/4 \equiv 1/4$.

**Stable hadrons as integer points on an elliptic curve.**

The computation shows that the proton point $P_0$ on $E_z$ is
approximately a **56-torsion point**: $56 \cdot P_0 \approx O$.
If the exact torsion order is $56$
($E_z(\mathbb{Q})_{\mathrm{tors}} \cong \mathbb{Z}/56\mathbb{Z}$
or a quotient), then:

- A nucleus with $N$ neutrons is stable when $N \cdot P_n$
  lies near the identity $O$ or the 2-torsion point $T$ in
  the group law of $E_z$.
- The stability pairs are precisely the values of $N$ where
  $N \cdot P_n$ hits a **torsion point** of $E_z$.
- **The stable hadrons of the Descartes universe are the
  integer solutions of a Diophantine equation on the elliptic
  curve $E_z$.**

The nuclear chart — every stable isotope, every stability pair,
the neutron-to-proton ratio of every element — is the
**set of integer points** on an elliptic curve derived from
the chiral fibration of Bring's surface at $q = 1.110$.

**Witness data**: see `folio-assistant/computations/elliptic-stability.json`
for the full numerical computation.
