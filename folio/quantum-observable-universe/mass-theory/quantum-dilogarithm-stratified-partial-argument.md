**Partial argument for [the stratified quantum dilogarithm conjecture](#conj:quantum-dilogarithm-stratified).** Steps 1, 2 and 4 below are argued; Step 3 is not established, and as written it cannot be: $F_n(z)$ in (d) is a single power of $z$, so the product expansion $F_n(z) = \prod_k (1 - q^{-k}z)^{-c_k(n)}\, u_n(q)$ fails for it. What is proved is Step 1, the mutual orthogonality of the depth strata under the Frobenius pairing.

*Step 1 (Frobenius dual decomposition of $Z(A)$).* By
[curvature-rank stratification](#prop:curvature-rank-gb-stratification)
— **together with the partition-vs-word identification this proof itself
flags as unestablished at Step 3 below, and which is not supplied by that
proposition** —
the centre $Z(A) = \bigoplus_{\lambda \vdash n} R \cdot e_\lambda$
admits the GB-depth grading
$Z(A) = \bigoplus_{k \geq 0} Z^{(k)}(A)$. The Frobenius pairing
$\langle a, b \rangle = \int_A a \cdot b$ restricts to $Z(A)$ as a
non-degenerate bilinear form, and the depth strata $Z^{(k)}(A)$ are
mutually orthogonal under this pairing
([Frobenius duality of strata](#prf:spectral-sequence-collapse)
"§Frobenius duality of strata"):

$$
  \langle Z^{(k)}(A),\, Z^{(\ell)}(A) \rangle \;=\; 0
  \qquad \text{whenever } k \neq \ell .
$$

> **The pairing of strata is diagonal.** The strata are spans of central
> primitive idempotents, and distinct idempotents annihilate each other: for
> any linear functional $\varphi$,
> $\varphi(e_\lambda e_\mu) = \varphi(\delta_{\lambda\mu} e_\lambda)$.
> So the pairing on that basis is $\mathrm{diag}(\tau(e_\lambda))$, with every
> stratum self-dual and every distinct pair annihilating; at $n = 3$ this holds
> exactly in $\mathbb{Q}(q)$ (all six off-diagonal entries vanish, the diagonal
> is nonzero, and $\sum_\lambda \tau(e_\lambda) = 1$). This is the form Step 4
> needs: it uses $\langle Z^{(k)}, Z^{(\ell)}\rangle = 0$ for $k \neq \ell$, which
> an anti-diagonal (Poincaré-type) duality $Z^{(k)} \times Z^{(N-k)} \to R$ would
> not supply.
>
> **Open:** Step 4 pairs a central $\phi_q^{(k)}$ against a general
> $T_w \in A$, not against a central element, so "$T_w$ has zero projection
> on $Z^{(k)}$" has to be read as a statement about $T_w$'s Wedderburn
> blocks. That reading is plausible, since for a central idempotent
> $\tau(e_\lambda a) = \tau(e_\lambda a e_\lambda)$, but it is not stated in the
> block.

where $N$ is the maximal GB-depth in $Z(A)$, retained below only as the
top of the depth range. The pairing $Z^{(k)} \times Z^{(k)} \to R$ is
non-degenerate on each stratum separately — each stratum is **self**-dual,
and there is no Poincaré-type pairing across distinct strata.

*Step 2 (existence of $\phi_q^{(k)}(z_i)$).* By
[cor: quantum dilogarithm](#cor:quantum-dilogarithm), the level-$i$
torsion-volume contribution to the mass is
$\mathrm{tr}_{\mathrm{trans}}(\varrho, p_i) = \Phi_q(z_i)$. Since the
mass functional is centre-valued by
[categorical mass = Markov trace](#prop:categorical-mass-markov), the
$\Phi_q(z_i)$-action on $Z(A)$ via the Markov pairing factors through
$Z(A)$. Decomposing along the depth grading,

$$
  \Phi_q(z_i) \cdot \mathrm{id}_{Z(A)}
  \;=\;
  \sum_{k \geq 0} \Phi_q(z_i) \cdot \mathrm{proj}_{Z^{(k)}(A)}.
$$

Define $\phi_q^{(k)}(z_i) := \mathrm{proj}_{Z^{(k)}(A)}(\Phi_q(z_i))$
as the depth-$k$ projection of the Frobenius dual.

*Step 3 (cyclotomic factors $\leftrightarrow$ depth-$k$ partitions).*
The cyclotomic factor $(1 - q^{-k} z_i)^{-1}$ in $\Phi_q(z_i)$ has its
pole locus at $z_i = q^k$. We identify this locus with the
depth-$k$ centre stratum $Z^{(k)}(A)$ via the $q$-content / hook-length
structure:

(a) The q-deformed Wedderburn-block weight is
$w_\lambda(q) = \dim_q^2 V_\lambda / [n]_q!$ (distinct from the
classical Plancherel measure $w_\lambda(1) = (\dim V_\lambda)^2/n!$ —
the two coincide at $q = 1$; see
[Plancherel weights define a probability distribution](#prop:plancherel-weight-boundedness)),
where
$\dim_q V_\lambda = [n]_q! \,/\, \prod_{\square \in \lambda} [h(\square)]_q$
and $[h]_q = (q^h - q^{-h})/(q - q^{-1})$ is the symmetric quantum
integer
([Hoefsmit pipeline](#conj:hoefsmit-scattering-pipeline)).

(b) The hook lengths $h(\square)$ for $\square \in \lambda$ encode
the partition's depth in the GB filtration. Here
$\mathrm{depth}_{\mathrm{GB}}(\lambda) = \max_{\square \in \lambda} h(\square)$
(the partition's **maximum hook length**) is a *definition* — the
supremum of the hook length over the
cells of $\lambda$ — not a consequence of
[curvature-rank stratification](#prop:curvature-rank-gb-stratification),
which stratifies $J^{\,r}/J^{\,r+1}$ by the curvature rank $r(T_w)$ of
**words** and mentions no partition. The two are different indexings of
depth, and the reading of $\mathrm{depth}_{\mathrm{GB}}(\lambda)$ as
the minimal number of $R_H, R_{YB}$ rewrites needed to put any element
of the $\lambda$-isotypic component in NF is the identification of the
partition grading with the word filtration, which that proposition does
not supply.

(c) Therefore $\dim_q V_\lambda$ has a factor of $[k]_q$ in its
hook-length expansion exactly when $\lambda$ contains a box with
$h(\square) = k$, equivalently $\mathrm{depth}_{\mathrm{GB}}(\lambda) \geq k$.
Under the substitution $z_i \to q^k$, the factor $[k]_q$ vanishes —
$\dim_q V_\lambda(q)\big|_{z_i = q^k}$ has a zero, and the
corresponding $w_\lambda^{-1}$ specialisation has a pole.

(d) The Markov-trace generating function for the centre is the
formal series
$F_n(z) = \sum_{\lambda \vdash n} \dim_q^{-1}(V_\lambda) \cdot z^{|\lambda|}$,
and its expansion as an infinite product in $z$ is
$F_n(z) = \prod_{k \geq 1} (1 - q^{-k} z)^{-c_k(n)} \cdot u_n(q)$
where $c_k(n) = \#\{\lambda \vdash n : \max\text{-hook}(\lambda) = k\}$
and $u_n(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is a unit. The exponent
$c_k(n)$ counts depth-exactly-$k$ partitions; the factor
$(1 - q^{-k} z)^{-c_k(n)}$ contributes the depth-$k$ stratum of $Z(A)$.

> **Scope of (d): the multi-factor product expansion does not hold for a homogeneous monomial.** Every $\lambda \vdash n$ has $|\lambda| = n$, so $F_n(z) = \bigl(\sum_{\lambda \vdash n} \dim_q^{-1}(V_\lambda)\bigr)\, z^n$ is a single monomial in $z$. A product $\prod_{k \geq 1}(1-q^{-k}z)^{-c_k(n)}\, u_n(q)$ with some $c_k(n) > 0$ has the nonzero $z^1$ coefficient $u_n(q)\sum_k c_k(n)\, q^{-k}$ when $n \geq 2$, so the two sides cannot agree. Steps (e)–(f) inherit this. The proved truncation statement is [Cell-depth truncation of a trace](#prop:cell-depth-truncation).

(e) The single-stratum factor $(1 - q^{-k}z)^{-1}$ in $\Phi_q$ is
the $c_k = 1$ specialisation of (d) — applicable when each depth-$k$
stratum is one-dimensional or when factoring over irreducible
strata. For the brane-tower, each exceptional divisor $p_i$
contributes one $(1 - q^{-k} z_i)^{-1}$ per depth $k$, and the full
$\Phi_q(z_i) = \prod_k (1 - q^{-k} z_i)^{-1}$ is the universal
generating function over all depths.

(f) Combining (a)–(e): the partial product
$\Phi_q^{[\leq k]}(z_i) = \prod_{j=1}^{k}(1-q^{-j}z_i)^{-1}$ generates
exactly the contributions from depths $1, 2, \ldots, k$, and the
truncation increment
$\Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)$ is the
depth-exactly-$k$ generator. Identifying this with the Frobenius dual
$\phi_q^{(k)}(z_i)$ from Step 2 (modulo orthogonal strata) gives

$$
  \Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)
  \;\equiv\; \phi_q^{(k)}(z_i) \pmod{\bigoplus_{\ell \neq k} Z^{(\ell)}(A)}.
$$

*Step 4 (Frobenius truncation for $T_w$).* For $T_w \in H_n(R, q)$
with NF support depth
$k_\star(T_w) = \max_{\lambda \in \mathrm{supp}(T_w)} \mathrm{depth}_{\mathrm{GB}}(\lambda)$,
$T_w$ has zero projection on $Z^{(k)}(A)$ for every $k > k_\star(T_w)$
by definition of $k_\star$. By Step 3, $\phi_q^{(k)}(z_i) \in Z^{(k)}(A)$,
so

$$
  \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle \;=\; 0
  \qquad \text{for } k > k_\star(T_w).
$$

The Frobenius-paired sum truncates:

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr)
  \;=\;
  \sum_{k = 0}^{\infty} \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle
  \;=\;
  \sum_{k = 0}^{k_\star(T_w)} \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle
  \;=\;
  \mathrm{tr}_M\!\bigl(\Phi_q^{[\leq k_\star(T_w)]}(z_i) \cdot T_w\bigr).
$$

The second equality uses depth orthogonality (Step 1); the third uses
Step 3's identification of the partial product with the
$\bigoplus_{j \leq k_\star(T_w)} Z^{(j)}$-content. 

**Open: canonical bound.**
The proof above is a Frobenius-paired *equality*, not a canonical
identity. It says the Frobenius-pairing of $\Phi_q(z_i)$ with $T_w$
equals the Frobenius-pairing of $\Phi_q^{[\leq k_\star(T_w)]}(z_i)$
with $T_w$. To conclude that the *canonical* mass formula evaluated
with $\Phi_q$ replaced by $\Phi_q^{[\leq k_\star(T_w)]}$ gives the same
answer, one needs the projections $\mathrm{proj}_{Z^{(k)}}(\Phi_q(z_i))$
to be uniformly bounded as $|z_i| \to q$ — equivalently, no spurious
analytic mass leaks into $Z^{(k)}(A)$ from the divergent infinite
product. Establishing this uniform bound is the conjectural target of
[$z$-Habiro completion](#conj:brane-tower-z-habiro). It is no longer
needed for [$\Phi_q$ categorical truncation](#conj:phi-q-categorical-truncation):
the level-wise $\Phi_q$ identity that the bound was meant to regularise is
false algebraically, and the centre-projection truncation is proved without
it ([Cell-depth truncation of a trace](#prop:cell-depth-truncation)). Note also
that with $\Phi_q(z_i)$ a scalar the equality
$\mathrm{tr}_M(\Phi_q(z_i)T_w)=\mathrm{tr}_M(\Phi_q^{[\le k_\star]}(z_i)T_w)$
fails at $w=e$ unless $\prod_{j>k_\star}(1-q^{-j}z_i)^{-1}=1$, which is false
for $z_i\ne0$; the statement above needs $\Phi_q(z_i)$ read as a central
element, and that reading is not fixed here.

The argument above is solid as a **categorical (Frobenius-paired)
identity** but does not by itself rule out that the infinite analytic
product diverges at $|z_i| = q$ in a way that the finite Frobenius
truncation does not capture in real-valued terms. Step 3's
identification (a)–(f) reduces the cyclotomic-factor / depth-stratum
correspondence to the standard $q$-content / hook-length formula plus
[curvature-rank stratification §Step 3](#prop:curvature-rank-gb-stratification)
(GB-depth = max hook length), so the structural identification is now
explicit — **but "explicit" here means *written down*, not *established*.
The citation does not supply the identification; the passage above, at
"not a consequence of [curvature-rank stratification] ... which ... mentions no
partition", states the position of this proof.** The product expansion in **(d)** is false (see the status note under (d)); what this paragraph called the remaining open piece is the
expansion $F_n(z) = \prod_k (1 - q^{-k}z)^{-c_k(n)} \cdot u_n(q)$.
No such expansion exists for $n \geq 2$, because $F_n$ is a monomial in $z$. The earlier claim that unique factorisation in $\mathbb{Z}[q^{\pm 1/2}][z]$ supplies one is withdrawn.
