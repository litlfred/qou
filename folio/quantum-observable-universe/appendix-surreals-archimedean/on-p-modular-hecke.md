This conjecture extends, to a primitive $p$-th root of unity, the
char-$0$ surreal picture of Hecke representation theory recalled
next.
[Hoefsmit-is-surreal-construction](#prop:hoefsmit-is-surreal-construction)
identifies the binary $\{L \mid R\}$ split at each Hecke
eigenchannel step with Conway's recursive surreal
construction. This works because the Hecke generator $\sigma$ has
exactly **two** eigenvalues at generic $q$.

At a primitive $p$-th root of unity $q = \zeta_p$, the
representation theory of $H_n(\zeta_p)$ acquires *p*-ary
structure: when $\geq p$ copies of the fundamental representation
$V$ are tensored, certain summands in the $q$-Schur--Weyl
decomposition become trivial (Lusztig's small quantum group
$\mathfrak{u}_q(\mathfrak{sl}_2)$ is finite-dimensional, with
truncation governed by $p$).

This conjecture asserts the natural extension of
[Hoefsmit-is-surreal-construction](#prop:hoefsmit-is-surreal-construction)
to the modular setting: the modular Hecke combinatorics at $q =
\zeta_p$ corresponds to **nimber surreals**
$\mathbf{On}_p$ in characteristic $p$ (Lenstra--Conway).

## Note on this paper

This conjecture is **not** load-bearing for QOU's main results; the substrate value $q_0$ is generic (not a root of unity). The binary Hoefsmit / char-$0$ surreal picture applies throughout this paper. The char-$p$ extension is included here as a conceptual companion. It records how the Hoefsmit machinery maps into the modular setting.

## Background: nimber surreals

The **nimber field** $\mathbf{On}_p$ is the field of all ordinals
under:

- **nim-addition**: $\alpha \oplus \beta$ is the unique ordinal
 $\gamma$ such that $\gamma \neq \alpha' \oplus \beta$ for all
 $\alpha' < \alpha$ and $\gamma \neq \alpha \oplus \beta'$ for
 all $\beta' < \beta$. For finite ordinals in base $p$, this is
 digit-wise XOR-mod-$p$.
- **nim-multiplication**: $\alpha \otimes \beta$ defined
 recursively via the mex (minimum-excluded-value) operator.

For each prime $p$:

- $\mathbf{On}_2$ is an algebraically closed field of
 characteristic $2$, equal to the union of $\mathbb{F}_{2^{2^k}}$
 for all $k$ (Conway, Lenstra).
- $\mathbf{On}_p$ for odd $p$ is constructed analogously by Pruss
 and others.

These fields are the **char-$p$ analogues** of $\mathbf{No}$:
they form the algebraic-geometric ambient for ordinal-valued
calculations in characteristic $p$, just as $\mathbf{No}$ does in
characteristic $0$.

## Conjecture

There is a $p$-ary analogue of the
[Hoefsmit-is-surreal-construction](#prop:hoefsmit-is-surreal-construction)
bijection:

$$
  \Phi_p :  \mathrm{KLcells}_n(\zeta_p)
   \xrightarrow{\sim} \mathbf{On}_p^{[n]},
$$

where:

- $\mathrm{KLcells}_n(\zeta_p)$ is the set of Kazhdan--Lusztig
 cells of $H_n(\zeta_p)$ (which replace the Hoefsmit tableaux
 in the modular setting), and
- $\mathbf{On}_p^{[n]}$ is the set of nimbers of *p-adic depth*
 $\leq n$ (analogous to dyadic surreals of birthday $\leq n$).

The bijection $\Phi_p$ is determined by the *p-ary fusion data*:
at each step, a vector decomposes into $p$ eigencomponents
(rather than $2$) according to the cyclic-group action of
$\mathbb{Z}/p$ on the truncated tensor power.

The smallest instance already makes this correspondence concrete:
at $p = 2$, $n = 3$ the three Kazhdan--Lusztig cells of $H_3(-1)$
are conjectured to match the first three nimbers $0$, $1$, $*2$ (worked out in the
proof strategy below).

## Surviving and broken structure

Compared to the char-0 surreal lift
([algebraic core survives](#rem:algebraic-core-survives)):

See [Table](#tbl:on-p-modular-hecke-table-data).

The crucial *break* is **Wedderburn semisimplicity**: at $q = \zeta_p$
the Hecke algebra is not semisimple, so the Hoefsmit-style
diagonalisation fails. The replacement is the **Kazhdan--Lusztig
cell decomposition**, which is *p*-ary rather than *binary*.

## Visibility in characteristic 0

The $p$-ary structure at $q = \zeta_p$ is *not* purely modular —
it is visible in characteristic $0$ as the limit behaviour of the
Hecke algebra near roots of unity. Specifically:

- **Dixmier--Lusztig truncation**: at generic $q$, every tensor
 power $V^{\otimes n}$ has $\lfloor n/2 \rfloor + 1$
 summands (binary Hoefsmit tree). At $q = \zeta_p$, summands
 with $\dim_q(\lambda) = 0$ disappear; the surviving summands
 are reorganised into $p$-cycles.

- **Quantum trivialisation**: when $p$ copies of
 $V$ are tensored at $q = \zeta_p$, the trivial representation acquires
 *multiplicity $p$* (or $0$, depending on parity), instead of
 $1$. This is the "$p$ braids coming together" — $p$ strands
 fuse into a single quantum-trivial channel.

- **Fusion ring**: the truncated tensor product
 $\otimes_{\zeta_p}$ on $\mathrm{Rep}(\mathfrak{u}_{\zeta_p}(\mathfrak{sl}_2))$
 has $p-1$ simple objects with $p$-ary fusion rules. The fusion
 graph is the **Dynkin diagram $A_{p-1}$**, generalising the
 binary $A_1$ of generic Hecke.

In QOU specifically, the **golden-ratio degeneration** at
$q_{\mathrm{gold}} = 1/\varphi^2$
([golden-ratio degeneration](#rem:golden-ratio-degeneration), if
present) is the $p = 5$ case: the Descartes elliptic curve nodes
at $\zeta_5$, and Hecke fusion becomes 5-ary.

## Implications for QOU

If the conjecture holds, QOU has a *parallel theory* in
characteristic $p$ for each prime $p$:

- **QOU**$_{\mathbf{No}}$: the surreal lift over $\mathbf{No}$
 (this appendix).
- **QOU**$_{\mathbf{On}_p}$: the modular lift over $\mathbf{On}_p$,
 one for each prime $p$.

The two lifts are related by:

- both reduce to the same archimedean QOU when "evaluated at
 $q = q_0$" (in the sense of the standard-part for char 0;
 in some analogous sense for char $p$);
- they record different *kinds* of fine structure
 (infinitesimal-corrections in char 0 vs. $p$-ary fusion data
 in char $p$);
- they are *both* valid algebraic ambients for the same
 underlying $\mathbb{Z}[q^{\pm 1}]$-form of QOU.

Speculative physical readings of the char-$p$
lifts are not pursued here. The mathematical content — that modular Hecke at
$\zeta_p$ corresponds to $\mathbf{On}_p$ surreals — is the actual
claim.

## Proof strategy

The conjecture's two halves: nimber existence (mathematically
established) and Hecke $\leftrightarrow$ nimber correspondence (open).

**Layer 1: nimber field existence (cited)**:

1. $\mathbf{On}_2$ is constructed by Conway–Lenstra
 \cite{conway1976} as the union of $\mathbb{F}_{2^{2^k}}$;
 algebraically closed, characteristic 2.

2. $\mathbf{On}_p$ for odd $p$: similar construction via
 nim-arithmetic. Established in the algebraic-geometry
 literature.

**Layer 2: Hecke-cell $\leftrightarrow$ nimber bijection (open)**:

3. **Smallest case** ($p = 2$, $n = 3$): compute the
 Kazhdan–Lusztig cells of $H_3(\zeta_2) = H_3(-1)$ explicitly.
 $H_3(-1)$ has 3 cells: $\{1\}$, $\{\sigma_1, \sigma_2, \sigma_1\sigma_2\sigma_1\}$,
 and $\{\sigma_1\sigma_2, \sigma_2\sigma_1\}$ (with appropriate $W$-graph
 structure).

4. **Match against** the first 3 elements of $\mathbf{On}_2$: the
 nim-numbers $0, 1, *2$ (where $*2$ is the third nimber, equal
 to the surreal $\{0,1 \mid \}$).

5. **Verify** that the bijection respects the $\mathbb{Z}/2$
 action (Frobenius / sign symmetry).

6. **Generalise** to larger $n$ and other primes $p$ by
 induction on KL-cell complexity.

**Falsification path**: produce a $H_n(\zeta_p)$-cell that does
not correspond to any nimber of depth $\leq n$ (i.e., a
"phantom" cell with no nimber witness). Such an example would
require $p$-ary fusion data not captured by nim-arithmetic,
suggesting a different combinatorial replacement is needed.

**Provability assessment**: Layer 1 already established. Layer 2
for $p = 2, n = 3$ is feasible by hand — a matter of weeks.
General Layer 2 requires Kazhdan–Lusztig cell theory, a
substantial multi-year project.
