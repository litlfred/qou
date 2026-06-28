The unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) has six
structural terms.  Earlier commentary suggested these emerge as
pages of a **spectral sequence** associated with the Gröbner–Shirshov
filtration $J^\bullet(q)$ on $H_n(R, q)$.  This proposition makes the
spectral-sequence structure precise and states the $E_\infty$
convergence target.

**Definition (filtered differential algebra).**
*The Hecke algebra $H_n(R, q)$ with the confinement filtration
$J^\bullet(q)$
([confinement level](#def:confinement-level)) carries a natural
differential $d$ induced by the three Gröbner–Shirshov rewriting
rules
([Hecke normal form](#def:hecke-normal-form)):*

1. *Hecke relation: $d_{\mathrm{H}}(\sigma_i^2) = (q - q^{-1})\sigma_i + \mathbf{1}$.*
2. *Far commutativity: $d_{\mathrm{F}}(\sigma_i \sigma_j) = \sigma_j \sigma_i$ for $|i - j| \geq 2$.*
3. *Yang–Baxter: $d_{\mathrm{YB}}(\sigma_i \sigma_{i+1} \sigma_i) = \sigma_{i+1} \sigma_i \sigma_{i+1}$.*

*Each rule lowers filtration degree (the RHS sits in the same or
lower stratum than the LHS).  The direct sum $d = d_H + d_F + d_{YB}$
satisfies $d \circ d = 0$ on the filtered complex (after
normalisation), making $(H_n(R, q), J^\bullet, d)$ a **filtered
differential algebra**.*

**Proposition (GB spectral sequence).**
*The filtered differential algebra $(H_n(R, q), J^\bullet, d)$ has an
associated spectral sequence $(E_r^{\ell, *}, d_r)$ with:*

$$
  E_0^{\ell, *} \;=\; J^\ell(q) / J^{\ell+1}(q)
  \qquad \text{(associated graded)},
$$

$$
  E_1^{\ell, *} \;=\; H^*\bigl(J^\ell / J^{\ell+1},\ d\bigr)
  \qquad \text{(Hochschild-type cohomology of each stratum)},
$$

*and higher pages $E_r^{\ell, *}$ obtained by successive
homology of the $d_r$ differential.*

*Convergence:*

$$
  E_\infty^{\ell, *}
  \;\Longrightarrow\;
  \mathrm{gr}^\ell\bigl(H_n(R, q)\bigr).
$$

*The Markov trace $\mathrm{tr}_M: H_n(R, q) \to \mathbb{C}$ is a
$d$-closed linear functional (by cyclicity) and therefore descends
to $E_\infty$.*

**Identification of the six mass terms with spectral-sequence pages.**

*Pairing $\mathrm{tr}_M$ against the braid word $T_w$ decomposes
over the spectral sequence pages as:*

See [Table](#tbl:gb-spectral-sequence-table-data).

**Derivation of $d \circ d = 0$ (via Hochschild complex).**

*The rewriting rules $d_H, d_F, d_{YB}$ define a reduction
procedure, not a genuine differential on a chain complex.  To
get $d \circ d = 0$ we pass to the **Hochschild cochain complex**
over the natural ground ring $R$ of the Hecke algebra:*

$$
  C^k(H_n(R, q), H_n(R, q))
  \;:=\;
  \mathrm{Hom}_R\bigl(H_n(R, q)^{\otimes k},\ H_n(R, q)\bigr),
$$

*where the ground ring is the paper's **categorical base ring $R$** —
the target of the fibre functor
$\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$
([Tannaka–Krein reconstruction](#prop:tannaka-krein-reconstruction)).
$R$ is the commutative ring in which Markov-trace values live
before the archimedean calibration $\tau \colon R \to \mathbb{R}$
([categorical mass, Markov](#prop:categorical-mass-markov)).*

*Under different realisations
([knot operator energy](#def:knot-operator-energy)):*

- *Archimedean: $R$ contains $\mathbb{R}[q, q^{-1}]$, evaluating
  at $q = q_0 \in \mathbb{R}$.*
- *$p$-adic: $R$ contains $\mathbb{Q}_p[q, q^{-1}]$.*
- *Finite-field: $R$ contains $\mathbb{F}_p[q, q^{-1}]$.*

*The spectral-sequence construction works over any such $R$; the
physics application uses the archimedean realisation $R$ containing
$\mathbb{R}[q, q^{-1}]$, but the **categorical** derivation is
ring-agnostic.  Complex numbers are **not required** for
$d \circ d = 0$ or for the spectral-sequence construction; they
appear only as a derived embedding
$R \hookrightarrow \mathbb{C}$ when residues at roots of unity
are extracted
([GB residue spectral sum](#prop:gb-residue-spectral-sum)).*

*equipped with the standard Hochschild differential*

$$
  (d\,f)(a_0 \otimes \cdots \otimes a_k)
  \;=\;
  a_0 \cdot f(a_1 \otimes \cdots \otimes a_k)
  + \sum_{i=0}^{k-1} (-1)^{i+1} f\bigl(a_0 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_k\bigr)
  + (-1)^{k+1} f(a_0 \otimes \cdots \otimes a_{k-1}) \cdot a_k.
$$

*$d \circ d = 0$ is a classical theorem
(Cartan–Eilenberg 1956) for any associative $R$-algebra over any
commutative ring $R$; it holds verbatim for $H_n(R, q)$ over the
paper's categorical base ring $R$ (fibre-functor value ring).  The Markov trace $\mathrm{tr}_M$ is a
**cyclic 0-cochain** (a map $H_n(R, q) \to \mathbb{C}$ satisfying
$\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$), hence is $d$-closed at
degree $0$.*

*The confinement filtration $J^\bullet(q)$ on $H_n(R, q)$ induces a
decreasing filtration on $C^\bullet$:*

$$
  F^p C^k
  \;:=\;
  \{f \in C^k \mid f\bigl(J^{p_1}(q)^{\otimes k}\bigr) \subset J^{p + p_1}(q)\},
$$

*compatible with the Hochschild differential in the sense
$d(F^p) \subset F^p$.  This is the **filtered Hochschild complex**.*

*Therefore:*

1. **$d \circ d = 0$ holds** *on the filtered complex — inherited
   from the classical Hochschild identity.*
2. **Filtration preservation** $d(F^p) \subset F^p$ *follows
   because $J^\bullet$ is an ideal-filtration compatible with
   multiplication.*

*Hence the filtered Hochschild complex $(C^\bullet(H_n(R, q)), d, F^\bullet)$
is a genuine filtered cochain complex with spectral sequence
pages $(E_r^{p, q}, d_r)$.*

**Convergence $E_\infty \Rightarrow \mathrm{gr}\,H_n(R, q)$.**

*The filtration $J^\bullet(q)$ is:*

1. *Bounded below: $J^0 = H_n(R, q)$ (the full algebra).*
2. *Exhaustive: $\bigcap_\ell J^\ell = 0$ for any fixed
   $q = q_0$ off the roots of unity, since partition energies
   $E_\ell(q_0)$ are distinct and positive
   ([confinement level, uniqueness](#prop:confinement-level-unique)).*
3. *Finite-dimensional at each degree
   $J^\ell(q)/J^{\ell+1}(q)$ (bounded by the Wedderburn block
   dimensions).*

*These are the classical convergence conditions for a filtered
spectral sequence (Weibel 1994, §5.5).  Therefore*

$$
  E_\infty^{p, q}
  \;\cong\;
  \mathrm{gr}^p\,H^{p+q}\bigl(H_n(R, q), H_n(R, q)\bigr),
$$

*and the total Hochschild cohomology equals the sum over pages.
When paired with the Markov-trace cocycle $\mathrm{tr}_M$, this
gives the six-term decomposition of the mass claimed in the
proposition statement.*
