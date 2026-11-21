**Conjecture (geometric realisation of the depth-3 Bring trilog
$\mathrm{Cl}_3(2\pi/5)$ — candidates list).**

The depth-3 canonical witness
[Bring trilog at $\zeta_5$ as depth-3 grouplike value (50-digit functional-equation cross-validated witness)](#conj:bring-trilog-depth-3-witness)
established that

$$
  \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) \;=\; \mathrm{Re}\,\mathrm{Li}_3(\zeta_5)
  \;=\; 0.18936791501083168387944480476641361363127422974423\ldots
$$

is a depth-3 grouplike value of $\mathcal{H}_q$ at the
$S_5$-Bring-natural input $\zeta_5$ — i.e. an element of
$\mathcal{P}_3 / \mathcal{P}_2$ in Goncharov's period filtration.
**Open question**: which geometric or topological invariant
realises this number on the archimedean side?

### Three candidate identifications, in order of plausibility

#### Candidate 1: hyperbolic 4-manifold volume on a Bring-natural cusped quotient

Goncharov (1995, 2002) and Beilinson–Levin connect $\mathrm{Li}_3$
values at algebraic points to volumes of hyperbolic 4-manifolds
via the regulator $K_5^{\mathrm{ind}}(\overline{\mathbb{Q}}) \otimes \mathbb{Q}
\to \mathbb{R}/\pi^4 \mathbb{Q}$. A specific 4-manifold is needed:

- **Cusped 4-mfd with $S_5$-cuspidal monodromy.** Compactified
  moduli space $\overline{\mathcal{M}}_{0,5}/S_5$ — a 2-dim
  complex, 4-dim real space — has cusps shaped on the $S_5$-orbit
  of $\zeta_5$. Its hyperbolic volume should be a
  $\mathbb{Q}$-linear combination of $\{\mathrm{Cl}_3(2\pi a/5) :
  \gcd(a, 5) = 1\}$ values.

**Discharge target**: identify the specific 4-manifold and its
$\mathbb{Q}$-coefficient in $\mathrm{Cl}_3(2\pi/5)$.

#### Candidate 2: Chern–Simons of an icosahedrally-symmetric knot in $S^3$

The icosahedral group $A_5 \subset S_5$ acts on $\mathbb{P}^1(\mathbb{C})$
with three orbits of size 12, 20, 30 (the icosahedral configuration).
Knots whose holonomy representation lands in this $A_5$-orbit have
Chern–Simons invariants whose archimedean evaluation involves
$\mathrm{Li}_3$ at $\zeta_5$ shape parameters.

Specifically, for a hyperbolic knot $K$ with shape parameters in
$\mathbb{Q}(\zeta_5)$, the complexified volume

$$
  \mathrm{CS}(K) + i\,\mathrm{Vol}(K) \;\in\; \mathbb{C} / \pi^2 \mathbb{Z}
$$

has imaginary part (volume) at depth 2 and real part (CS) at
depth 3. **For an $A_5$-symmetric knot**, the depth-3 part should
be expressible via $\mathrm{Cl}_3(2\pi/5)$ and its Galois conjugates.

**Discharge target**: identify a knot $K$ with
$\mathrm{CS}(K) \stackrel{?}{=} \alpha \cdot \mathrm{Cl}_3(2\pi/5) + \beta \cdot \zeta(3) + \cdots$
for explicit $\alpha, \beta \in \mathbb{Q}$.

> [!WARNING]
> **Update (canonical refutation)**: A PSLQ canonical experiment on the CS invariants of the seven Bring-natural torus-knot generators $\{T(2, 3), T(2, 5), T(2, 7), T(2, 9), T(3, 4), T(3, 5), T(5, 2)\}$ reveals that their Chern-Simons invariants are exactly rational (e.g., $\mathrm{CS}(T(2,5)) = 1/20, \mathrm{CS}(T(2,3)) = -1/12$). Therefore, their CS invariants cannot be expressed as non-trivial $\mathbb{Q}$-linear combinations of transcendental numbers like $\zeta(3)$ and $\mathrm{Cl}_3(2\pi/5)$. This strictly rules out torus knots as direct geometric realisations for this depth-3 period under Candidate 2.

#### Candidate 3: iterated integral on $\overline{\mathcal{M}}_{0, 5}$

Goncharov's motivic fundamental groupoid of $\mathbb{P}^1 \setminus \{0, 1, \infty\}$
generalises to $\overline{\mathcal{M}}_{0, 5}$, the moduli of 5
ordered marked points on $\mathbb{P}^1$. Iterated integrals there
generate weight-3 multiple polylogs at 5th-root-of-unity values;
specifically, at the $S_5$-orbit of base points, the integrals
realise

$$
  \mathrm{Li}_3(\zeta_5),\; \mathrm{Li}_3(\zeta_5^2),\;
  \mathrm{Li}_3(\zeta_5^3),\; \mathrm{Li}_3(\zeta_5^4) \;\in\; \mathcal{P}_3.
$$

These values lie in $\mathrm{MPV}(3,5)$, the $\mathbb{Q}$-span of the multiple
polylogarithm values of weight $3$ and level $5$. Its dimension $d(3,5)$ has an
upper bound (Deligne–Goncharov), but no unconditional lower bound is known, so a
$\mathbb{Q}$-linear identification of $\mathrm{Cl}_3(2\pi/5)$ inside this span
comes with no proved independence of the spanning values; for standard levels,
including $N = 5$, the standard relations are conjectured to generate all
$\mathbb{Q}$-linear relations \cite[\S1.1, \S6, \S7.4]{zhao2010-standard-relations}.

**Discharge target**: write down the explicit iterated integral
$\int_\gamma \omega$ on $\overline{\mathcal{M}}_{0, 5}$ whose
period evaluates to $\mathrm{Cl}_3(2\pi/5)$ for the right contour
$\gamma$ and form $\omega$.

### Comparison: all three candidates are conjecturally equivalent

The three candidates above are conjecturally **the same**
mathematical content viewed through three lenses:

- **Candidate 1** (hyperbolic 4-mfd volume) is the geometric image
  of the Beilinson regulator on $K_5^{\mathrm{ind}}$.
- **Candidate 2** (knot CS) is the dual / complementary image at
  the 3-mfd level — same regulator in a different basis.
- **Candidate 3** (iterated integral) is the motivic source — both
  Candidates 1 and 2 are special evaluations of it.

The geometric realisation question is then: *which is the canonical
representative for the QOU paper's purposes?* Candidate 2 is the
most directly compatible with the existing knot-theoretic framework;
Candidate 1 is the cleanest from the period-theoretic side;
Candidate 3 is most general.

### Consequences of an explicit identification

Identifying *any one* of the three candidates explicitly would:

1. **Close the depth-3 row of the depth correspondence.** The correspondence ([GS-depth $\leftrightarrow$ Goncharov period-depth correspondence](#conj:gb-depth-period-correspondence))
   currently has the figure-8 row at depth 2 verified and the trilog
   canonical witness at depth 3, but no geometric image for the
   trilog value. Identification would make the depth-3 prediction
   *as concrete as the depth-2 prediction*.
2. **Test joint-action commutativity at depth 3.** The Galois action
   on $\mathrm{Cl}_3(2\pi/5)$ via $\zeta_5 \mapsto \zeta_5^a$ should
   match the action on the geometric side (4-mfd cusps, knot CS,
   or marked-point permutations) — a sharp test of
   [Joint motivic-Galois $\times$ braid-group action on the bi-filtration $\mathcal{H}_q^{(n, K)}$](#conj:joint-galois-braid-action).
3. **Provide the Bring-natural depth-3 witness target.** The witness
   formalism
   (the canonical formalism)
   currently records the algebraic value; geometric identification
   would let it record a *measurement target* (e.g. SnapPy CS
   computation on a specific knot) and verify equality at 50 dps.
