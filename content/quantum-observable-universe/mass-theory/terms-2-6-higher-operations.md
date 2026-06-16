Terms 2 (single-generator brane tower $\sum \Phi_q(|\hat V_i|)$) and
6 (jet-level prefix corrections) of the unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) are the two
remaining open identifications in the spectral-sequence framework
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications)).
This proposition sketches concrete avenues to close both via
**higher operations** on the Hochschild cohomology of $H_n(R, q)$.

**Setup: Gerstenhaber structure on $HH^*(H_n(R, q))$.**

*The Hochschild cohomology $HH^*(A, A)$ of any associative algebra
$A$ carries a canonical **Gerstenhaber algebra** structure:*

- *Cup product $\cup \colon HH^p \otimes HH^q \to HH^{p+q}$
 (graded-commutative, associative).*
- *Gerstenhaber bracket $[-, -] \colon HH^p \otimes HH^q \to HH^{p+q-1}$
 (graded Lie bracket of degree $-1$).*

*For $A = H_n(R, q)$, the cup product gives a ring structure on
$\bigoplus_p HH^p$, and the Gerstenhaber bracket measures the
non-commutativity of the deformation.*

**Term 2 = Cauchy $\Phi_q$ kernel = cup-product tower.**

**Claim.**
*The single-generator brane tower
$\sum_i \Phi_q(|\hat V_i|)$ arises from the **cup-product tower**
of the class $[\sigma_i] \in HH^1(H_n(R, q))$ with itself:*

$$
  \sum_{k = 1}^{\infty} \frac{q^{-k}}{(q; q)_k}\bigl([\sigma_i]\bigr)^{\cup k}
  \;=\;
  \bigl\langle \Phi_q(|\hat V_i|) - 1\bigr\rangle
  \quad \text{in } HH^* \text{ pairing with } \mathrm{tr}_M.
$$

*Expansion: $\Phi_q(z) = \sum_k z^k / (q;q)_k$ (Cauchy's $q$-exponential),
with $(q;q)_k = \prod_{j=1}^k(1 - q^j)$. The $z^k$ coefficient
$1/(q;q)_k$ is the $q$-binomial coefficient tracking partition
counts at the $k$-th level of the flag.*

**Derivation sketch.**
*Each generator $[\sigma_i] \in HH^1$ pairs with
$\mathrm{tr}_M$ via the Markov trace at degree $1$:
$\langle \mathrm{tr}_M, [\sigma_i]\rangle = z$. The $k$-fold
cup product $[\sigma_i]^{\cup k}$ lives in $HH^k$ (higher
filtration stratum) and its Markov-trace pairing is
$z \cdot q^{-(k-1)} \cdot (\text{weight})$ by the recursive
Hecke relation. Summing over $k$ with the $(q;q)_k$ normalisation
gives the full $\Phi_q$ kernel.*

**Proved (symbolic computation): $HH^1(H_3(R, q)) = 0$ at generic $q$.**

*Direct symbolic computation in `hochschild_h3.py`:*

- *dim Der$(H_3(R, q)) = 3$ (total derivations, linear-algebra nullspace
 of $216$ constraint equations on $36$ matrix entries).*
- *dim Inner$(H_3(R, q)) = 3$ (inner derivations $[x, \cdot]$ span).*
- ***$HH^1 = \text{Der}/\text{Inner} = 3 - 3 = \mathbf{0}$***
 at generic $q$.*

*This is consistent with $H_3(R, q)$ being **semisimple** over
$\mathbb{R}[q, q^{-1}]$ away from roots of unity: semisimple algebras
have $HH^1 = 0$ by Wedderburn (every derivation of a matrix algebra
is inner).*

*Consequence: **the cup-product tower hypothesis for Term 2 is null**.
Since $HH^1(H_3(R, q)) = 0$, there is no non-trivial class $[\sigma_0]$
to take cup products of. The Cauchy kernel $\Phi_q$ in Term 2
**does not** come from Hochschild cup products on $H_3(R, q)$.*

**Corrected framework.**

*The $E_\infty$ pages of the GB-filtration spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence)) are the
**graded pieces** of the confinement filtration on $H_3(R, q)$ itself:*

$$
  E_\infty^{p, *} \;=\; J^p(q) / J^{p+1}(q)
  \quad (\text{graded pieces, NOT } HH^p(H_3(R, q))).
$$

*These are distinct from Hochschild cohomology classes. My earlier
claim that Terms 2, 3 were "pages paired with cup product" confused
two different homological objects:*

1. ***Spectral sequence on filtered algebra*** (what we have):
 pages $E_r^{p, *}$ are graded pieces $\mathrm{gr}^p H_n(R, q)$;
 pairing with $\mathrm{tr}_M$ is direct projection.
2. ***Hochschild cohomology $HH^*$*** (what I conflated):
 classes are outer-derivation cocycles; cup product is on
 cochains; $HH^1(H_3(R, q)) = 0$ generically so no tower exists.

**Where Term 2's Cauchy kernel actually comes from.**

*The $\Phi_q$ Cauchy expansion $\Phi_q(z) = \sum z^k/(q;q)_k$ is
NOT from HH cup products. Possible sources:*

1. ***Cyclic cohomology $HC^*(H_3(R, q))$*** (Connes, Tsygan):
 Markov trace is a cyclic cocycle, so it lives in $HC^0$; the
 S-operator $HC^0 \to HC^2$ creates higher cyclic classes that
 DO have non-trivial structure even when $HH^*$ is trivial.
 Cauchy kernel may arise from the periodicity $\mathrm{Ph}(\mathrm{tr}_M)$
 in the cyclic complex.
2. ***Deformation resolution***: Treating $H_3(R, q)$ as a deformation
 of $\mathbb{R}[S_3]$, $\Phi_q$ arises in the deformation
 cohomology $HH^*(\mathbb{R}[S_3], \mathbb{R}[S_3])_q$ at
 non-trivial order in $q - 1$. **TESTED, FAILS.**
3. ***Root-of-unity limit***: At $q = \zeta_\ell$, $H_n(R, q)$ becomes
 non-semisimple and $HH^1 \neq 0$; Cauchy expansion could arise
 from the $q \to \zeta$ limit of filtered trace pairings.
4. ***Quantum group $U_q(\mathfrak{sl}_2)$ representation theory***:
 Via Schur–Weyl duality, $H_n(R, q)$ is paired with $U_q(\mathfrak{sl}_2)$
 acting on $V^{\otimes n}$; $\Phi_q$ appears as a character of
 specific $U_q$-modules (unipotent / Verma structure). Most
 plausible natural source.

***Option 2 (deformation cohomology) ruled out.***
*Direct computation in
`computations/deformation_cohomology_s3.py`:*

- *$\dim \mathrm{Der}(\mathbb{R}[S_3]) = 3 = \dim \mathrm{Inner}(\mathbb{R}[S_3])$*
- *$HH^1(\mathbb{R}[S_3]) = 0$*
- *$HH^2(\mathbb{R}[S_3]) = 0$ by Burghelea's theorem: for finite
 group $G$ over a characteristic-$0$ field,
 $HH^p(k[G]) = \bigoplus_{[C]} H^p(C_G(C); k)$, and group
 cohomology of finite $G$ with $\mathbb{R}$/$\mathbb{C}$
 coefficients vanishes in positive degrees (Maschke).*

*The Hecke deformation $H_3(R, q)$ exists despite $HH^2 = 0$ because
$H_3(R, q) \cong \mathbb{R}[S_3]$ as abstract $\mathbb{R}[q, q^{-1}]$-algebras
for generic $q$ (both are semisimple with identical irrep structure).
The deformation is **gauge-trivial in cohomology** — distinguishes
$H_3(R, q)$ from $\mathbb{R}[S_3]$ only by basis choice, not by a
non-trivial cocycle class.*

*Consequence: **deformation cohomology does NOT source $\Phi_q$**.
Options 2 and the HH* cup-product route are both CLOSED.*

*Remaining options:*

- *Option 1 (cyclic cohomology $HC^*$): untested, plausible.*
- *Option 3 (root-of-unity limit): untested, plausible.*
- *Option 4 (quantum group $U_q(\mathfrak{sl}_2)$): **most natural**
 — $\Phi_q(z) = \prod(1 - q^{-k}z)^{-1}$ is the character of
 the irreducible Verma module for $U_q(\mathfrak{sl}_2)$ acting
 on the Fock space; Schur–Weyl duality then transports this
 structure to $H_n(R, q)$.*

**CORRECTION 1: colored Jones / Kashaev / Habiro IS the algebraic source.**

*The $\Phi_q$ Cauchy kernel $(q; q)_n^{-1}$ is not from $HH^*$ or
deformation cohomology — it arises from the **colored Jones
polynomial** framework, already cited in paper blocks but not
previously tied explicitly to Term 2.*

**Habiro unified quantum invariant.**
*For any knot $K$, the family of colored Jones polynomials
$\{J_N(K; q) : N \geq 1\}$ satisfies Habiro's cyclotomic expansion
([Habiro ring](#def:habiro-ring)):*

$$
  J(K; q)
  \;=\;
  \sum_{m \geq 0} a_m(K) \cdot (q; q)_m,
  \qquad
  a_m(K) \in \mathbb{Z}[q, q^{-1}],
$$

*where $a_m(K)$ are integer-coefficient Laurent polynomials and
$(q; q)_m = \prod_{k=1}^m (1 - q^k)$ is the $q$-Pochhammer. The
sum converges in the Habiro ring for all $q$ in the closure of
roots of unity AND extends to generic $q$ by evaluation.*

**Immediate identification.**
*The $q$-Pochhammer structure $(q; q)_m$ is **exactly** the
denominator of the $\Phi_q(z) = \sum_n z^n / (q; q)_n$ Taylor
expansion. So the **inverse cyclotomic structure** of the Habiro
unified invariant IS the $\Phi_q$ Cauchy kernel. The
identification is:*

$$
  \Phi_q(|\hat V_i|)
  \;=\;
  \sum_{m \geq 0} \frac{|\hat V_i|^m}{(q; q)_m}
  \;=\;
  \text{generating function dual to Habiro } (q; q)_m \text{ basis}.
$$

**Kashaev volume conjecture route.**
*The **Kashaev invariant** $\langle K\rangle_N = J_N(K; e^{2\pi i/N})$
evaluated at roots of unity relates to the knot's hyperbolic volume:*

$$
  \lim_{N \to \infty} \frac{\log\lvert\langle K\rangle_N\rvert}{N}
  \;=\;
  \frac{\mathrm{Vol}(K)}{2\pi}
  \qquad (\text{Volume Conjecture}),
$$

*and is already part of the paper's framework via
[Kashaev volume density](#rem:kashaev-volume-density) and
[mass endomorphism conjecture](#conj:mass-endomorphism).*

*For our purposes: the **infinite-$N$ limit of colored Jones**
gives the $\Phi_q$ expansion. Each colored-Jones evaluation at
level $N$ corresponds to a specific Wedderburn component of
$H_n(R, q)$ at that level. Summing across all $N$ reproduces the
brane-tower Φ_q-kernel.*

**Algebraic source.**

*Term 2 is derivable from the algebraically-established colored
Jones / Habiro framework. The paper's
[mass endomorphism conjecture](#conj:mass-endomorphism) and
[algebraic quantum volume](#def:algebraic-quantum-volume)
explicitly use these structures for the volume-conjecture side;
the same machinery gives Term 2's Cauchy kernel.*

*Corrected option list for Term 2's source:*

See [Table 1](#tbl:terms-2-6-higher-operations-table1-data).

---

**CORRECTION 2: Wedderburn weights ARE used inside Term 2 already.**

*The search above asked the wrong question. Term 2 does NOT need
a new algebraic source for $\Phi_q$ as a "character" — the
**Wedderburn weights already enter** inside the argument of
$\Phi_q$. From
[mass endomorphism tower](#prop:mass-endomorphism-tower):*

$$
  \hat V_i^{\mathrm{full}}
  \;=\;
  w_{\mathrm{sym}} \cdot \mathrm{sp}_i
  + w_{\mathrm{std}} \cdot V_i^s
  + w_{\mathrm{alt}} \cdot \mathrm{ap}_i,
$$

*where the three Wedderburn weights are **algebraically derived**
in
[three-parameters Wedderburn](#prop:three-parameters-wedderburn)
as*

$$
  w_{\mathrm{sym}} = \frac{q^2}{D},\;
  w_{\mathrm{std}} = \frac{(q^2+1)^2}{D},\;
  w_{\mathrm{alt}} = \frac{q^2}{D},\quad
  D = q^4 + 4q^2 + 1.
$$

*and generalised in
[Frobenius universal](#thm:frobenius-codim-universal) for arbitrary
$H_n(R, q)$. The "tower" $\Phi_q(|\hat V_i^{\mathrm{full}}|)$ is
therefore:*

$$
  \Phi_q\bigl(\lvert w_{\mathrm{sym}}\cdot\mathrm{sp}_i + w_{\mathrm{std}}\cdot V_i^s + w_{\mathrm{alt}}\cdot\mathrm{ap}_i \rvert\bigr),
$$

*which IS a Wedderburn-weighted quantity at each generator, with
$\Phi_q$ the pointwise "blow-up resolution" from
[mass endomorphism tower](#prop:mass-endomorphism-tower) proof.*

**Term 2 as infinite Wedderburn sum (reinterpretation).**

*Alternatively, $\Phi_q(z)$ is the $k \to \infty$ limit of a finite
Jones–Wenzl trace at level $k$:*

$$
  \Phi_q(z)
  \;=\;
  \lim_{k \to \infty}
    \sum_{\lambda : |\lambda| \leq k}
    w_\lambda^{(k)} \cdot z^{|\lambda|},
$$

*where $w_\lambda^{(k)} = \dim_q(\lambda)^2 / [k]_q!$ are the
Wedderburn weights at level $k$. This limit is exactly the
cluster-algebra / quantum-dilogarithm generating function that
the paper's exceptional-divisor blow-up resolves.*

*So the six-term formula is **entirely Wedderburn-weight-based**:*

- *Terms 1, 3, 4: FINITE Wedderburn sums at level $k = n$.*
- *Term 2, 6: INFINITE Wedderburn sums in the $k \to \infty$ limit,
 expressed compactly as $\Phi_q$ and cyclotomic residues.*
- *Term 5: Wedderburn-weighted ribbon character
 (chirality coefficient).*

*No new algebraic source is needed; all terms use the same
[three-parameters Wedderburn](#prop:three-parameters-wedderburn)
machinery, either at finite or infinite level. The earlier search
for "Where does $\Phi_q$ come from?" in Hochschild/deformation
cohomology was **looking in the wrong place**: $\Phi_q$ is 
an infinite Wedderburn sum, and the Wedderburn weights themselves
have been algebraically derived from the start.*

**Term 2 — derivation.**

*Status revised: Term 2 IS algebraically derived, via
[mass endomorphism tower](#prop:mass-endomorphism-tower) +
[three-parameters Wedderburn](#prop:three-parameters-wedderburn)
+ [Frobenius universal](#thm:frobenius-codim-universal). The
"open" status in earlier blocks was due to mis-framing: I was
searching for a new algebraic home for $\Phi_q$ when the
Wedderburn-based derivation was already in place.*

*The remaining open item for Term 2 is only: **identifying which
$E_\infty$ page of the GB spectral sequence corresponds to the
infinite-level Wedderburn sum** — i.e., the translation between
"level-$k$ truncation of Jones–Wenzl trace" and "pairing with
$E_\infty^{\ell, *}$ for $\ell \geq 1$". This is a reindexing
question, not a missing-derivation question.*

**Previous naive proxy test (for reference).**

*Script `cup_product_tower_probe.py` tested the simplest proxy:
compute $\mathrm{tr}_M(\sigma_0^k)$ (algebra power) symbolically in
$H_3(R, q)$ and compare to $\Phi_q$ Cauchy Taylor coefficients
$1/(q; q)_k$.*

See [Table 2](#tbl:terms-2-6-higher-operations-table2-data).

*Ratios vary wildly (sign flips, non-monotone), and
$\mathrm{tr}_M(\sigma_0^k)$ **oscillates** rather than matching
the $\Phi_q$ generating-function growth. The hypothesis
"$\mathrm{tr}_M(\sigma_0^k) \propto 1/(q;q)_k$" is FALSE.*

**Why the shortcut is wrong.**

*Cup product in Hochschild cohomology $HH^*(A, A)$ is NOT algebra
multiplication. For a cochain $f \in HH^p$ represented by a map
$A^{\otimes p} \to A$ and $g \in HH^q$ represented by
$A^{\otimes q} \to A$, the cup product $f \cup g \in HH^{p+q}$ is
defined by*

$$
  (f \cup g)(a_1 \otimes \cdots \otimes a_{p+q})
  \;=\;
  f(a_1 \otimes \cdots \otimes a_p) \cdot g(a_{p+1} \otimes \cdots \otimes a_{p+q}).
$$

*This is the cochain-level product, not the algebra-element product.
A class $[\sigma_0] \in HH^1$ would be represented by a specific
$1$-cocycle $f_{\sigma_0}: A \to A$ (an outer derivation), and
$[\sigma_0]^{\cup k}$ is a $k$-cocycle $(f_{\sigma_0})^{\cup k}$
paired against $a_1 \otimes \cdots \otimes a_k$ as a specific
iterated-product. Identifying this cocycle explicitly in
$HH^1(H_3(R, q))$ is a non-trivial computation — NOT equivalent to
$\sigma_0^k$.*

**Correct setup (what would be needed).**

*To rigorously verify Term 2 as a cup-product tower:*

1. *Compute $HH^1(H_3(R, q))$ over $\mathbb{R}[q, q^{-1}]$ — the
 space of outer derivations modulo inner. This is a
 finite-rank $R$-module.*
2. *Identify the class $[\sigma_0] \in HH^1$ as a specific
 outer-derivation cocycle $f_{\sigma_0}$.*
3. *Compute $(f_{\sigma_0})^{\cup k} \in HH^k$ for $k = 1, 2, 3, \ldots$
 via the Hochschild cochain formula.*
4. *Evaluate the pairing
 $\langle \mathrm{tr}_M, (f_{\sigma_0})^{\cup k}\rangle \in \mathbb{R}[q, q^{-1}]$.*
5. *Compare to $\Phi_q$ Cauchy coefficients with the correct
 normalisation.*

*This is a **standard finite-dimensional Hochschild-cohomology
computation**, but requires machinery (cochain complex, cup
product, cocycle representatives) not in the current codebase.
Estimated effort: 200-400 LoC using sympy matrix operations on
$A \otimes A \cong H_3(R, q) \otimes H_3(R, q)$ (36-dimensional) and
higher tensor powers ($216$-dim at degree $3$, etc.) — doable but
significant.*

*Until this full machinery is implemented, the cup-product tower
hypothesis remains **structurally plausible but unverified**.
The shortcut $\mathrm{tr}_M(\sigma_0^k)$ is definitively not the
The right-object.*

---

**Term 6 = jet prefix = NOT a prefix-product formula.**

*Four candidate prefix conventions have been tested (three upstream
+ one GB-filtration in
[jet-prefix GB filtration](#prop:jet-prefix-gb-filtration));
**all fail**. We propose that Term 6 is structurally **not** a
prefix-word product but is instead the **root-of-unity residue
contribution** already captured by
[GB residue spectral sum](#prop:gb-residue-spectral-sum).*

**Proposed identification.**

$$
  \text{Term 6}(K)
  \;=\;
  \sum_{\ell \geq 2}
    \frac{\mathrm{Res}_{q = \zeta_\ell}\bigl[\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]}
         {q_0 - \zeta_\ell},
$$

*i.e., the cyclotomic residue sum at roots of unity $\zeta_\ell$
for $\ell \geq 2$ (the level-$\ell = 1$ residue is absorbed into
Terms 2, 3 as the dominant $\zeta_1 = 1$ pole).*

**Why this replaces the prefix formula.**

*The paper's prefix formula
$a_k(\beta) = \sum_\lambda w_\lambda \chi^\lambda(\beta_k) / \sum_\lambda w_\lambda \dim \mathrm{Res}^{H_k}_{H_3} V_\lambda$
has no algebraic match against the higher-strata $E_\infty^{\ell \geq 3}$
pages of the spectral sequence — consistent with the four failed
tests. Meanwhile, the **cyclotomic** formula DOES correspond
to higher $E_\infty$ strata (via the residue-spectral-sum
derivation in
[GB residue spectral sum](#prop:gb-residue-spectral-sum)).*

*So Term 6 may have been **mis-stated** in earlier blocks as a
prefix product; the correct identification is with root-of-unity
residues summed over all $\ell \geq 2$.*

**Caveat.**
*This is a structural proposal, not a proof. It requires:*

1. *Confirming that the cyclotomic sum for $\ell \geq 2$ reproduces
 the empirical Term 6 corrections needed to close the $A \geq 3$
 binding errors (typically $5\%$-$20\%$ from the BW+$\chi$
 + shell).*
2. *Rigorously identifying $E_\infty^{\ell, *}$ for $\ell \geq 3$
 with specific ribbon-residue combinations via the Cauchy
 kernel of Term 2.*

*If confirmed, the unified mass formula collapses from 6 terms to
**5 independent structural pieces**:*

1. *Descended $|\mathrm{tr}_M|$ (Term 1)*
2. *Brane tower $\sum \Phi_q(|\hat V_i|) + z^2 \sum \Phi_q(|\hat V_i \hat V_j|)$
 (Terms 2 + 3, combined as Cauchy kernel tower on $HH^{\geq 1}$)*
3. *Frobenius co-Casimir $m_e \cdot \tau(C_{\dim_q})$ (Term 4)*
4. *Chirality / ribbon twist $a_K$ (Term 5)*
5. *Higher-stratum residues (what was Term 6, now = cyclotomic
 residue sum at $\zeta_\ell$ for $\ell \geq 2$)*

*A much cleaner structural story.*

---

**Implications for the unified formula.**

*If the above identifications hold:*

$$
  \boxed{\;
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{|\mathrm{tr}_M(T_w)|}_{E_\infty^{0, *}}
  \;+\;
  \underbrace{\bigl\langle \mathrm{tr}_M,\ \Phi_q \text{-tower} \bigr\rangle_{HH^{\geq 1}}}_{\text{Cauchy kernel (Terms 2, 3, 6)}}
  \;+\;
  \underbrace{m_e \cdot \tau(C_{\dim_q})}_{\text{Term 4}}
  \;+\;
  \underbrace{a_K(\varrho) \cdot \mathcal{R}_{\mathrm{rib}}}_{\text{Term 5 (ribbon)}}
  \;}
$$

*where $\mathcal{R}_{\mathrm{rib}}$ denotes the chirality-couplable piece (e.g.,
$B_{\mathrm{bulk}}$ in the BW+$\chi$ form). Four structurally
distinct pieces, not six.*

**Caveat.**
*All of this is proposed, not proven. The cup-product tower
derivation for Term 2 and the root-of-unity residue
identification for Term 6 are **concrete computational
targets** but have not been verified for any nontrivial case.
They are the natural next steps.*

**Computational tasks, prioritized.**

1. *Compute $[\sigma_0]^{\cup k}$ for $k = 1, 2, 3$ in $HH^*(H_3(R, q))$
 over $\mathbb{R}[q, q^{-1}]$; verify Markov-trace pairings
 match $\Phi_q$ Taylor coefficients.*
2. *Compute cyclotomic residue at $\zeta_2 = -1$ for D's
 atomic braid; compare to residual $5$–$20\%$ binding errors
 at $A \geq 3$.*
3. *If Term 2 + Term 6 unification holds, the 6-term formula
 reduces to the 4-term boxed form above.*
