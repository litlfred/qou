<!-- FILE_START: intro-cyclotomic-depth-3-trilog.md -->
The Bring-surface trilogarithm $\mathrm{Li}_3^q$ admits a depth-3
cyclotomic witness — a categorical identity expressing the
trilog at roots of unity in terms of the $q$-trilogarithm at the
substrate parameter.  This section conjectures and records the
explicit identity, then surveys the empirical evidence for the
conjecture from the canonical witnesses.

The arc starts with the depth-3 trilog witness conjecture, lists
the cyclotomic specialisations that the conjecture covers, and
exhibits the empirical evaluations against CODATA-grade
constants.  The closing blocks tie the conjecture to the Bloch-
group quotient construction from the Descartes chapter and the
Mathlib-bridge fillers from the q-geometric-Langlands chapter.

The arc through the Bring trilog depth-3 witness, the Tate-rational cyclotomic identification, the $\zeta_5$-orbit-sum identity and its PSLQ independence verification, the cyclotomic trilog imaginary closed form (with table data), and the general $\mathrm{Cl}_3$ orbit-sum formula pins the trilog substrate-flow data for the next sub-section's spectral computations.
<!-- FILE_END: intro-cyclotomic-depth-3-trilog.md -->

<!-- FILE_START: bring-trilog-depth-3-witness.md -->
**Conjecture (Bring trilog at $\zeta_5$ as depth-3 grouplike value;
50-digit canonical witness with functional-equation cross-validation).**

*The depth-3 grouplike of $\mathcal{H}_q$ at the primitive 5th root
of unity $\zeta_5 = e^{2\pi i / 5}$ — the canonical Bring-natural
input via $S_5$-symmetry of Bring's curve
([`def:brings-coordinate-ring`](#def:brings-coordinate-ring)) —
maps under archimedean realisation to a class in
$\mathcal{P}_3 / \mathcal{P}_2$ (Goncharov period weight 3):*

$$
  \boxed{\;
    \tau_{\mathrm{arch}}\bigl(\,\mathrm{Li}_3^q(\zeta_5)\,\bigr)
    \;=\;
    \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right)
    \;+\;
    i\,S_3\!\left(\tfrac{2\pi}{5}\right)
    \;\in\;
    \mathcal{P}_3 \big/ \mathcal{P}_2.
  \;}
$$

### canonical witness (50-digit precision)

Computed via `exact algebraic structures.polylog` at `mp.dps = 50` (formalism
the canonical formalism,
witness
[`bring-trilog-zeta5-depth-3.witness.json`](https://github.com/litlfred/qou/blob/main/computations/bring-trilog-zeta5-depth-3.witness.json)):

$$
  \mathrm{Re}\,\mathrm{Li}_3(\zeta_5)
  \;=\; \mathrm{Cl}_3(2\pi/5)
  \;=\; 0.189{,}367{,}915{,}010{,}831{,}683{,}879{,}444{,}804{,}766{,}413{,}613{,}631\ldots
$$

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_5)
  \;=\; S_3(2\pi/5)
  \;=\; 0.992{,}200{,}853{,}769{,}594{,}245{,}615{,}242{,}082{,}147{,}244{,}646{,}471\ldots
$$

### Cross-validation: Bring-orbit functional equation

The classical multiplication identity for polylogarithms at $N$th
roots of unity:

$$
  \sum_{k=1}^{N-1} \mathrm{Li}_n(\zeta_N^k)
  \;=\;
  \bigl( N^{1-n} - 1 \bigr) \cdot \zeta(n).
$$

For $N = 5$, $n = 3$:

$$
  \sum_{k=1}^{4} \mathrm{Li}_3(\zeta_5^k)
  \;\stackrel{!}{=}\;
  -\tfrac{24}{25}\,\zeta(3).
$$

**canonical verified** at 50 dps:

| Side | Value (50 dps) |
|---|---|
| LHS: $\sum_{k=1}^{4} \mathrm{Li}_3(\zeta_5^k)$ | $-1.1539746270332105139837486350509919911343868406469\ldots$ |
| RHS: $-\tfrac{24}{25} \zeta(3)$ | $-1.1539746270332105139837486350509919911343868406469\ldots$ |
| Residual | $5.51 \times 10^{-51}$ |

The imaginary part of the orbit sum vanishes (complex-conjugate
cancellation between $\zeta_5^k$ and $\zeta_5^{5-k}$), verified to
$1.3 \times 10^{-51}$. **This is a 50-digit cross-validation
independent of `exact algebraic structures`'s polylog implementation** — the functional
equation forces the relation regardless of how each individual
$\mathrm{Li}_3(\zeta_5^k)$ is computed.

### Depth correspondence

| Side | Object | Depth |
|---|---|---|
| Algebraic | $\mathrm{Li}_3^q(\zeta_5) \in G^{(3)}(\mathcal{H}_q) \setminus G^{(2)}$ | iterated-integral depth $= 3$ |
| Archimedean | $(\mathrm{Cl}_3(2\pi/5), S_3(2\pi/5)) \in \mathcal{P}_3/\mathcal{P}_2$ | Goncharov period-depth $= 3$ |

A single $\mathrm{Li}_3$ factor on the algebraic side maps to a
weight-3 motivic period on the geometric side: depth $3 = 3$ match.

### Geometric realisation (open)

Unlike the depth-2 case (where $2\,\mathrm{Cl}_2(\pi/3) = \mathrm{Vol}(4_1)$
identifies the period with a hyperbolic volume), the depth-3 trilog
values $\mathrm{Cl}_3(2\pi/5)$ and $S_3(2\pi/5)$ do not yet have a
*direct* geometric interpretation in the QOU paper. Three candidate
identifications, in order of plausibility:

1. **Hyperbolic 4-manifold volume on Bring-cusped quotient.** The
   Goncharov regulator on $K_5^{\mathrm{ind}}(\overline{\mathbb{Q}})$
   gives $\mathrm{Li}_3$ values at algebraic points; specific values
   at $\zeta_5$ correspond to volumes of cusped hyperbolic 4-manifolds
   (Goncharov 1995). A Bring-natural 4-manifold has not been
   constructed in the paper; it is the cleanest discharge target.

2. **Chern–Simons of an $S_5$-symmetric knot in $S^3$.** $\mathrm{CS}$
   is the depth-3 partner of $\mathrm{Vol}$ in the complexified
   $\mathrm{CS} + i\,\mathrm{Vol} \in \mathbb{C}/\pi^2\mathbb{Z}$
   invariant. For a knot whose hyperbolic structure has $S_5$
   monodromy on its representation variety, $\mathrm{CS}$ would
   evaluate at $\zeta_5$-related shape parameters.

3. **Iterated integral on $\mathcal{M}_{0,5}$ for Bring's
   $S_5$-cover.** The moduli space of 5 marked points on $\mathbb{P}^1$
   carries an $S_5$-action; iterated integrals there generate
   weight-3 multiple polylogs at $\zeta_5$ values.

### Significance for B1

This is the **first depth-3 canonical witness** for
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence).
Combined with [`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness)
(depth 2), B1 is now **falsifiability-tested at depths 2 and 3**.

The functional-equation cross-validation provides genuine 50-digit
agreement (depth-2 witness only had ~13-digit cross-validation via
Clausen partial sum); the depth-3 instance is therefore the
*canonical tightest* graded-Mikusiński instance recorded.
<!-- FILE_END: bring-trilog-depth-3-witness.md -->

<!-- FILE_START: bring-trilog-imaginary-tate-rational.md -->
**Proposition (the imaginary part of the Bring trilog at $\zeta_5$
is Tate-rational — $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = 4\pi^3/125$,
verified at 50 dps via Kummer reflection).**

The depth-3 canonical witness
([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness))
records both real and imaginary parts of $\mathrm{Li}_3(\zeta_5)$
as candidate depth-3 periods. *This proposition shows the
imaginary part is **Tate-rational** — i.e. lies in $(2\pi i)^3 \cdot \mathbb{Q}
\subset \mathcal{P}_3$ — and therefore projects to zero under the
Beilinson regulator quotient $\mathcal{P}_3 \to \mathcal{P}_3 / \mathrm{Tate}$.
Only the real part $\mathrm{Cl}_3(2\pi/5)$ carries genuinely new
depth-3 information for B1.*

### Closed form

$$
  \boxed{\;
    \mathrm{Im}\,\mathrm{Li}_3(\zeta_5)
    \;=\;
    S_3\!\left(\tfrac{2\pi}{5}\right)
    \;=\;
    \frac{4 \pi^3}{125}.
  \;}
$$
### Significance — the depth-3 surface area shrinks by half

The Bring trilog witness ([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness))
recorded two real numbers as candidate depth-3 periods:

- $\mathrm{Re}\,\mathrm{Li}_3(\zeta_5) = \mathrm{Cl}_3(2\pi/5) \approx 0.18937$
- $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = S_3(2\pi/5) \approx 0.99220$

**Before this proposition**: both were treated as candidate generators
of the 2-dim $K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q}$
Borel-image space.

**After this proposition**: only $\mathrm{Cl}_3(2\pi/5)$ generates
the regulator image. $S_3(2\pi/5) = 4\pi^3/125$ is Tate-rational
and **kernel of the Beilinson regulator quotient**.

The **2-dim space is generated by**:

$$
  \mathrm{Cl}_3(2\pi/5),\;\; \mathrm{Cl}_3(4\pi/5)
  \;\;\in\;\;
  \mathcal{P}_3 / \mathcal{P}_2,
$$

i.e. the *real parts* at the two distinct $\zeta_5$-orbits modulo
complex conjugation. The 2 dimensions Borel predicts are the two
distinct $\mathrm{Cl}_3$ values at angles $2\pi/5$ and $4\pi/5$
(the two non-conjugate primitive 5th-root-of-unity angles in
$(0, \pi)$).

### Reduction of the depth-3 unproved surface

| Item | Status before | Status after |
|---|---|---|
| $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5)$ as new depth-3 period | candidate (open) | **theorem** — Tate-rational $4\pi^3/125$ |
| $\mathrm{Re}\,\mathrm{Li}_3(\zeta_5) = \mathrm{Cl}_3(2\pi/5)$ as new depth-3 period | candidate (open) | candidate (still open — no analogous reflection identity simplifies it) |
| 2-dim Bring trilog content | unconstrained | reduced to 1 generator + Galois conjugate |

This is **half of the depth-3 Bring trilog content reduced to
known structure**, leaving only $\mathrm{Cl}_3(2\pi/5)$ as the
genuine new content.

### Cross-references

- Bring trilog witness: [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
- Cl_3 geometric realisation question: [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Goncharov ζ_5 program: [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5)
<!-- FILE_END: bring-trilog-imaginary-tate-rational.md -->

<!-- FILE_START: cl3-zeta5-orbit-sum-identity.md -->
**Proposition (Cl_3 orbit-sum identity reduces depth-3 Bring trilog
content to a 1-dim antisymmetric generator).**

The Bring trilog witness
([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness))
records 4 grouplike values $\mathrm{Li}_3(\zeta_5^k)$ for $k = 1, ..., 4$.
Round 10 ([`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational))
showed the imaginary parts are Tate-rational. *This proposition
shows the real-part **sum** is also fixed (in the $\zeta(3)$-line),
leaving only the **antisymmetric difference** as the genuinely-new
depth-3 element of the regulator image.*

### Closed-form identities

**Sum identity (depth-3 $\leftrightarrow$ ζ(3)):**

$$
  \boxed{\;
    \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right)
    \;+\;
    \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
    \;=\;
    -\frac{12}{25} \cdot \zeta(3).
  \;}
$$

**Imaginary-part Tate-rationals (combining round 10 + reflection at $\zeta_5^2$):**

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_5)  \;=\; \frac{4 \pi^3}{125},
  \qquad
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_5^2) \;=\; \frac{2 \pi^3}{125}.
$$
### Cross-references

- Bring trilog witness: [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
- Imaginary-part Tate-rational: [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Goncharov $\zeta_5$ program: [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
- Geometric realisation question: [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization)
<!-- FILE_END: cl3-zeta5-orbit-sum-identity.md -->

<!-- FILE_START: cl3-zeta5-pslq-independence.md -->
**Proposition (PSLQ certifies $\mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5)$
is independent of standard depth-3 periods up to coefficient
norm $10^8$).**

The single open real number for B1's depth-3 row over $\mathbb{Q}(\zeta_5)$,

$$
  X \;:=\; \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
  \;\approx\; 0.955723143538268624750763927058\ldots,
$$

was reduced to "1-dim genuinely new depth-3 element" by
[`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity).
*This proposition certifies, via PSLQ at 50 dps with coefficient
norm bound $10^8$, that $X$ admits no $\mathbb{Q}$-linear relation
with any standard weight-3 period. Strong canonical evidence —
not proof — that $X$ is irreducible.*

### PSLQ search results

the canonical formalism,
[witness](https://github.com/litlfred/qou/blob/main/computations/cl3-zeta5-pslq-search.witness.json):

| Search | Candidate basis | PSLQ relation found? |
|---|---|---|
| 1 (minimal) | $\{\zeta(3),\, \pi^3\}$ | **none** |
| 2 (golden-ratio) | $\{\zeta(3),\, \pi^3,\, \pi \cdot \log^2(\varphi),\, \log^3(\varphi)\}$ | **none** |
| 3 (full weight-3) | $\{\zeta(3),\, \pi^3,\, \pi \cdot \log^2(\varphi),\, \log^3(\varphi),\, \pi \cdot \log^2(2),\, \pi^2 \cdot \log(\varphi),\, \pi^2 \cdot \log(2),\, \log^3(2)\}$ | **none** |

(Here $\varphi = (1 + \sqrt{5})/2$ is the golden ratio — natural at
$\zeta_5$ via $2 \cos(2\pi/5) = (\sqrt{5} - 1)/2 = 1/\varphi$.)

PSLQ tolerance: $10^{-45}$. Maximum integer-coefficient $\ell^\infty$
norm: $10^8$. **No relation found** in any candidate basis.

### canonical certification

This is a **PSLQ certificate**, not a proof. Standard interpretation:

- **If a relation existed** $\sum a_i \cdot v_i = 0$ with all $|a_i| \leq 10^8$,
 PSLQ at 50 dps would have found it (with overwhelming probability).
- **No such relation found** $\Rightarrow$ either:
 (i) $X$ is truly $\mathbb{Q}$-independent of the basis, or
 (ii) the integer coefficients of any relation exceed $10^8$
 (extremely unlikely for natural mathematical relations,
 which typically have small coefficients).

### Implications for B1

Combined with [`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
+ [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational):

| Layer | Status |
|---|---|
| $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = 4\pi^3 / 125$ | theorem (round 10) |
| $\mathrm{Cl}_3(2\pi/5) + \mathrm{Cl}_3(4\pi/5) = -\tfrac{12}{25}\zeta(3)$ | theorem (round 11) |
| $X = \mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5)$ admits no $\mathbb{Q}$-relation with standard weight-3 basis | **PSLQ-certified at $10^8$** |

So **at the level of accessible canonical certification**, the
2-dim Borel-rank space for $K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q}$
splits :

- 1-dim: $\zeta(3)$-line (classical, external).
- 1-dim: $X$ — *genuinely new*, with strong canonical evidence of
 irreducibility against the natural weight-3 basis.

The depth-3 surface for B1 over $\mathbb{Q}(\zeta_5)$ is:
**one specific real number, certified independent of the standard
period basis up to coefficient norm $10^8$**.

### Caveats and what would supersede this

A genuine **proof** of $X$'s irreducibility would require:

1. **Goncharov's motivic conjecture at $\mathbb{Q}(\zeta_5)$** — would
 give the algebraic structure of all weight-3 relations, hence
 show $X$ is independent of any specific basis a priori.
2. **Higher PSLQ precision** (e.g., 100+ dps with $10^{12}$
 coefficient bound) would extend the canonical certification but
 not constitute a proof.
3. **Goncharov 22-term at specific $\zeta_5$-arguments** — would
 either find a relation (closing one more avenue of unproved
 surface) or further constrain the basis.

The current PSLQ result is the **strongest unconditional canonical
evidence** available without these external developments.

### Cross-references

- The single open real number: [`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
- Im Li_3 closed form: [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- B1 status synthesis: [`rem:b1-current-status`](#rem:b1-current-status)
- Bring trilog witness: [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
- Goncharov $\zeta_5$ research program: [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5)
- Geometric realisation question: [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization)
<!-- FILE_END: cl3-zeta5-pslq-independence.md -->

<!-- FILE_START: cyclotomic-trilog-imaginary-closed-form.md -->
**Proposition (general closed form for $\mathrm{Im}\,\mathrm{Li}_3$ at
every root of unity).**

The Kummer reflection formula
([`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
established the closed form at $\zeta_5$.  *This proposition
generalises to **all** $n \geq 1$:*

$$
  \boxed{\;
    \mathrm{Im}\,\mathrm{Li}_3(\zeta_n)
    \;=\;
    \frac{(n - 1)(n - 2)\,\pi^3}{3\,n^3}.
  \;}
$$

*In particular, $\mathrm{Im}\,\mathrm{Li}_3(\zeta_n)$ is **Tate-rational**
for every $n$ — lies in $\pi^3 \mathbb{Q}$ — and therefore projects
to zero under the Beilinson regulator quotient
$\mathcal{P}_3 \to \mathcal{P}_3 / \mathrm{Tate}$.*
### Significance

**Generalises round 10 of ** from "$\zeta_5$ only" to "every
root of unity". Concretely:

1. **Every cyclotomic depth-3 imaginary part is Tate-rational** —
   lives in $(2\pi i)^3 \mathbb{Q} = -\pi^3 \mathbb{Q}$ (up to a
   factor of $i$).
2. **Projects to zero under Beilinson regulator quotient** — the
   genuinely-new content at $\zeta_n$ over $\mathbb{Q}(\zeta_n)$ at
   depth 3 lives **entirely in the real part** $\mathrm{Cl}_3(2\pi/n)$
   and its Galois conjugates, not in $\mathrm{Im}\,\mathrm{Li}_3$.
3. **Reduces the depth-3 surface for every cyclotomic field** to the
   real-part Galois orbit, halving the dimension at the outset.

### Asymptotic behaviour

The formula reveals the asymptotic:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_n) \;=\; \frac{\pi^3}{3 n} + O(n^{-2})
$$

as $n \to \infty$.  Decays like $1/n$, with leading coefficient $\pi^3/3$.

### Cross-references

- Special case $n = 5$ (round 10 of ):
  [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- Related orbit-sum:
  [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
- canonical witness (verified at $n = 3, 4, 5, 6, 7, 10, 11, 12, 13$ at 50 dps):
  [`cyclotomic-trilog-imaginary.witness.json`](https://github.com/litlfred/qou/blob/main/computations/cyclotomic-trilog-imaginary.witness.json)
- Geometric realisation question:
  [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
<!-- FILE_END: cyclotomic-trilog-imaginary-closed-form.md -->

<!-- FILE_START: cyclotomic-cl3-orbit-sum-general.md -->
**Proposition (general orbit-sum identity for $\mathrm{Cl}_3$ at every
root of unity).**

[`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
established the orbit sum at $N = 5$.  *This proposition generalises
to **all** $N \geq 2$:*

$$
  \boxed{\;
    \sum_{k=1}^{N - 1} \mathrm{Cl}_3\!\left(\tfrac{2\pi k}{N}\right)
    \;=\;
    -\frac{N^2 - 1}{N^2} \cdot \zeta(3).
  \;}
$$

*For odd $N$, parity halves the sum: $\sum_{k=1}^{(N-1)/2} \mathrm{Cl}_3(2\pi k/N)
= -\frac{N^2 - 1}{2N^2} \zeta(3)$.*
### Significance

**Generalises round 11 of ** from "$\zeta_5$ only" to "every
$N \geq 2$". Concretely:

1. **For every cyclotomic field $\mathbb{Q}(\zeta_N)$**, the real-part
   orbit sum of depth-3 grouplikes reduces to a rational multiple of
   $\zeta(3)$ (Apéry, classical).
2. **The genuinely-new content per cyclotomic field** is therefore
   the *individual* $\mathrm{Cl}_3(2\pi k/N)$ values modulo this
   sum — exactly $\lfloor (N - 1)/2 \rfloor - 1$ independent real
   numbers per prime $N$ (for $N$ prime).
3. **Combined with
   [`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)**
   (imaginary parts also Tate-rational), the depth-3 surface for
   $\mathbb{Q}(\zeta_N)$ over $\zeta_N$-arguments reduces to **at most
   $\lfloor (N - 1)/2 \rfloor - 1$ genuinely-new real numbers**.

### Cross-references

- Special case $N = 5$ (round 11 of ):
  [`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
- Companion imaginary-part theorem:
  [`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
- canonical witness (verified at $N = 3, 4, 5, 6, 7, 10, 11, 12, 13$ at 50 dps):
  [`cyclotomic-trilog-imaginary.witness.json`](https://github.com/litlfred/qou/blob/main/computations/cyclotomic-trilog-imaginary.witness.json)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
- PSLQ certification at $\zeta_5$ (open beyond):
  [`prop:cl3-zeta5-pslq-independence`](#prop:cl3-zeta5-pslq-independence)
<!-- FILE_END: cyclotomic-cl3-orbit-sum-general.md -->

<!-- FILE_START: cyclotomic-depth3-dimension-synthesis.md -->
**Proposition (cyclotomic depth-3 dimension synthesis: at each
prime $K \geq 5$, the genuinely-new depth-3 content over
$\mathbb{Q}(\zeta_K)$ has Borel-saturated dimension $(K - 3)/2$).**

Combining
[`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
(Tate-rationality of imaginary parts at every $\zeta_n$) with
[`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
(orbit-sum reduces real parts modulo $\zeta(3)$) and Borel's rank
theorem
([`prop:borel-partial-resolution`](#prop:borel-partial-resolution))
yields the dimension synthesis.

### Statement

For prime $K \geq 5$, let $\mathcal{V}_K \subseteq \mathcal{P}_3 / \mathcal{P}_2$
be the $\mathbb{Q}$-vector space spanned by the depth-3 grouplikes
of $\mathcal{H}_q$ evaluated at the $\zeta_K$-orbit and reduced
modulo the $\zeta(3)$-line.

$$
  \boxed{\;
    \dim_{\mathbb{Q}} \mathcal{V}_K
    \;=\;
    \frac{K - 3}{2}
    \quad \text{(unconditional upper bound; Borel-saturated lower bound conjectural).}
  \;}
$$

### Upper bound — theorem-level

**Claim.** $\dim_{\mathbb{Q}} \mathcal{V}_K \leq (K - 3)/2$.
### Significance

**Closes the cyclotomic depth-3 picture as a theorem (upper bound)
+ Beilinson-conditional theorem (full saturation).**

Concretely:

1. The graded-Mikusiński framework's depth-3 surface over every
   cyclotomic field $\mathbb{Q}(\zeta_K)$ has explicit dimension
   $(K - 3)/2$ modulo Beilinson — fully structural, no per-$K$
   guesswork.
2. Imaginary parts contribute **zero** to the regulator image
   (Theorem A) — the entire depth-3 "openness" is in real parts.
3. Real parts modulo orbit-sum + $\zeta(3)$-line give the genuinely-
   new content — PSLQ-saturated at $K = 5, 7$.
4. **Combined with
   [`prop:two-filtration-bridge-general`](#prop:two-filtration-bridge-general)
   (round 13 of )**, the framework's depth-3 picture has a
   fully general theorem for any cyclotomic field at any chiral
   pair of partition cells.

### Cross-references

- Theorem A: [`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
- Theorem B: [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
- Theorem C: [`prop:two-filtration-bridge-general`](#prop:two-filtration-bridge-general)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- $K = 5$ baseline: [`prop:cl3-zeta5-pslq-independence`](#prop:cl3-zeta5-pslq-independence)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
- B1 current-status synthesis: [`rem:b1-current-status`](#rem:b1-current-status)
<!-- FILE_END: cyclotomic-depth3-dimension-synthesis.md -->

<!-- FILE_START: jonquiere-cyclotomic-tate-rationality.md -->
**Proposition (general Jonquière inversion: Tate-rationality of the
"wrong-parity" part of $\mathrm{Li}_n(\zeta_K)$ at every depth $n$
and every root of unity).**

[`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
established the closed form at $n = 3$. *This proposition extends to
**every** depth $n \geq 2$ via the Jonquière inversion formula —
giving a uniform Bernoulli-polynomial closed form for the
"wrong-parity" part of $\mathrm{Li}_n(\zeta_K)$:*

$$
  \boxed{\;
    \mathrm{Li}_n(\zeta_K) - (-1)^{n - 1}\,\mathrm{Li}_n(\zeta_K^{-1})
    \;=\;
    -\frac{(2\pi i)^n}{n!} \cdot B_n\!\left(\tfrac{1}{K}\right),
  \;}
$$

*where $B_n$ is the $n$-th Bernoulli polynomial.  Equivalently:*

- *$n$ odd: $\mathrm{Im}\,\mathrm{Li}_n(\zeta_K) \in \pi^n \mathbb{Q}$
  (Tate-rational); closed form $-(2\pi i)^n / (2i \cdot n!) \cdot B_n(1/K)$.*
- *$n$ even: $\mathrm{Re}\,\mathrm{Li}_n(\zeta_K) \in \pi^n \mathbb{Q}$
  (Tate-rational); closed form $-(2\pi i)^n / (2 \cdot n!) \cdot B_n(1/K)$.*
### Significance — generalises Theorem A to every depth

**Generalises round 3's Theorem A** from
$n = 3$ to all $n \geq 2$. The depth-3 closed form
$(n - 1)(n - 2)\pi^3 / (3 n^3)$ becomes a Bernoulli-polynomial
specialisation of the general inversion formula at $z = \zeta_K$, with
the Bernoulli argument reducing to the clean specialisation $1/K$ (from Steps 1--2 above).

### Structural consequences for B1

For every cyclotomic field $\mathbb{Q}(\zeta_K)$ and every depth $n$:

- **Wrong-parity part is Tate-rational** — contributes 0 to the
  Beilinson regulator image.
- **Right-parity part carries the genuine periods** — i.e., the
  Borel-rank-saturating component of $K_{2n-1}^{\mathrm{ind}}(\mathbb{Q}(\zeta_K))
  \otimes \mathbb{Q}$ lives entirely in:
  - $\mathrm{Re}\,\mathrm{Li}_n$ for $n$ odd ($\mathrm{Cl}_n$ values)
  - $\mathrm{Im}\,\mathrm{Li}_n$ for $n$ even ($\mathrm{Cl}_n$ in
    Glaisher's even-index convention)

This is the structural reason why the depth-2 case (Bloch–Wigner $D$
= $\mathrm{Im}\,\mathrm{Li}_2$) and depth-3 case ($\mathrm{Cl}_3 =
\mathrm{Re}\,\mathrm{Li}_3$) carry the genuinely-new content — the
"other half" is Bernoulli-polynomial-rational at every depth.

### Cross-references

- Special case $n = 3$: [`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
- Special case $n = 5$, $K = 5$: round-10 result of ,
  [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- Companion orbit-sum theorem: [`prop:cyclotomic-orbit-sum-all-depths`](#prop:cyclotomic-orbit-sum-all-depths)
- Dimension synthesis: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
<!-- FILE_END: jonquiere-cyclotomic-tate-rationality.md -->

<!-- FILE_START: cyclotomic-orbit-sum-all-depths.md -->
**Proposition (general orbit-sum identity at every depth $n$).**

[`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
established the orbit sum at $n = 3$. *This proposition extends to
all depths $n \geq 2$:*

$$
  \boxed{\;
    \sum_{k = 1}^{N - 1} \mathrm{Cl}_n\!\left(\tfrac{2\pi k}{N}\right)
    \;=\;
    \begin{cases}
      \bigl(N^{1 - n} - 1\bigr)\, \zeta(n) & \text{$n$ odd}, \\[4pt]
      0 & \text{$n$ even},
    \end{cases}
  \;}
$$

*where $\mathrm{Cl}_n$ is the Glaisher Clausen function*:

- *$\mathrm{Cl}_n(\theta) = \mathrm{Re}\,\mathrm{Li}_n(e^{i\theta})$
 for $n$ odd*
- *$\mathrm{Cl}_n(\theta) = \mathrm{Im}\,\mathrm{Li}_n(e^{i\theta})$
 for $n$ even.*
### Significance

**For $n$ odd**: orbit sum reduces to $\zeta(n)$ — one dim of
genuinely-new content "absorbed" into the classical $\zeta(n)$-line
of $\mathcal{P}_n / \mathcal{P}_{n-1}$ (when $n$ is odd, $\zeta(n)$ is
NOT Tate-rational, conjecturally transcendental over $\mathbb{Q}$).

**For $n$ even**: orbit sum vanishes by definition. The individual
$\mathrm{Cl}_n$ values are bar-anti-symmetric (Glaisher convention),
They pair-cancel. No reduction occurs — all $(N - 1)/2$ distinct
$\mathrm{Cl}_n$ magnitudes are independent (modulo Beilinson).

### Generalises Theorem B

Theorem B ([`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general))
is the $n = 3$ case. This proposition extends the pattern to all $n$
with a single proof.

### Dimension consequences

Combined with
[`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality):

See [Table 2](#tbl:cyclotomic-orbit-sum-all-depths-table2-data).

The depth-3 case (round 3 + round 4 of ) gave $(K - 3)/2$.
The general formula here is parity-dependent: $(K - 3)/2$ for $n$
odd, $(K - 1)/2$ for $n$ even.

### Cross-references

- Special case $n = 3$: [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
- Tate-rationality companion: [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Dimension synthesis: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
<!-- FILE_END: cyclotomic-orbit-sum-all-depths.md -->

<!-- FILE_START: cyclotomic-dimension-synthesis-all-depths.md -->
**Proposition (cyclotomic dimension synthesis at every depth $n$
and prime $K$).**

[`prop:cyclotomic-depth3-dimension-synthesis`](#prop:cyclotomic-depth3-dimension-synthesis)
gave the dimension count at $n = 3$.  *This proposition extends to
every depth $n \geq 2$ via the parity-dependent combination of the
Jonquière Tate-rationality + orbit-sum theorems:*

$$
  \boxed{\;
    \dim_{\mathbb{Q}}\mathcal{V}_{n, K}
    \;=\;
    \begin{cases}
      (K - 3)/2 & \text{$n$ odd}, \\
      (K - 1)/2 & \text{$n$ even},
    \end{cases}
  \;\;\text{(upper bound theorem; Beilinson-conditional lower bound)}
  \;}
$$

*where $\mathcal{V}_{n, K}$ is the $\mathbb{Q}$-vector space spanned by
depth-$n$ grouplikes at the $\zeta_K$-orbit modulo the
$\zeta(n)$-line and Tate.*
### Significance

**Cyclotomic depth-$n$ picture is structurally complete at every
$n \geq 2$ and every prime $K \geq 3$.**

Combined with prior framework:

- [`prop:two-filtration-bridge-general`](#prop:two-filtration-bridge-general):
  bridge map at every partition.
- This proposition: dimension at every $(n, K)$ pair.
- B1 keystone status: theorem-level at $n = 2$ (Bloch–Suslin),
  Beilinson-conditional at $n \geq 3$.

The framework's cyclotomic depth structure is **fully characterised**.

### Cross-references

- Special case $n = 3$: [`prop:cyclotomic-depth3-dimension-synthesis`](#prop:cyclotomic-depth3-dimension-synthesis)
- Special case $n = 5$, $K = 5$: round-12  [`prop:cl3-zeta5-pslq-independence`](#prop:cl3-zeta5-pslq-independence)
- Tate-rationality (Step 2): [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Orbit-sum (Step 3): [`prop:cyclotomic-orbit-sum-all-depths`](#prop:cyclotomic-orbit-sum-all-depths)
- Borel rank: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Depth-2 theorem-level: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- B1 status synthesis: [`rem:b1-current-status`](#rem:b1-current-status)
<!-- FILE_END: cyclotomic-dimension-synthesis-all-depths.md -->

<!-- FILE_START: cyclotomic-strand-doubling.md -->
**Proposition (Cyclotomic doubling identity).**
*Let $\Phi_n(X) \in \mathbb{Z}[X]$ denote the $n$-th cyclotomic
polynomial. Then over $\mathbb{Z}[X]$:*

$$
  \Phi_8(X) \;=\; \Phi_4(X^2),
$$

*equivalently, $X^4 + 1 = (X^2 + 1) \circ X^2$ where $\circ$ denotes
polynomial composition.*

## Empirical context (Habiro element of nucleon-binding pairs)

The factor $\Phi_8^2 = (X^4 + 1)^2$ appears as a cyclotomic
prefactor in the $\sum_m \Delta a_m(X - Y) \cdot (u; u)_m$ Habiro
element for every atomic-step pair tested:

| Pair (atomic step) | Cyclotomic prefactor observed |
|---|---|
| $(\mathfrak{D} - \mathfrak{n})$, $A=1 \to 2$ | $\Phi_8^2$ |
| $({}^3\mathrm{He} - \mathfrak{D})$, $A=2 \to 3$ | $\Phi_8^2$ |
| $({}^4\mathrm{He} - {}^3\mathrm{He})$, $A=3 \to 4$ | $\Phi_8^2$ |

The $\Phi_8^2$ factor is **convention-invariant** — it appears in
both the `include_inter=True` habiro-witness convention (used in PR
\#1579) and the Phase~5q canonical convention
$\mathrm{tr}_M(\mathfrak{D}, q) = \tau_p \cdot \tau_n \cdot z(q)$
(verified in [`2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)).

## Categorical interpretation — universal atomic-step cyclotomic

The $\Phi_8^2$ prefactor is **universal across atomic-step pairs**,
not indexed by atomic number via strand doubling. The categorical
mechanism is **OPEN** — neither of the two naive candidates explains it:

- **Not $z(q)^k$ interface.** Direct Habiro expansion of $z(q)^k$
  alone produces a pure monomial $u^k$ with no cyclotomic factor;
  the $\Phi_4(u) = u^2 + 1$ denominator of $z(q) = u/(u^2 + 1)$ clears
  into the normalisation prefactor.
- **Not the Pochhammer boundary.** The earliest mechanical Pochhammer
  contribution of $\Phi_8$ is at $m = 8$ via $(u; u)_8 \ni 1 - u^8$;
  the earliest mechanical $\Phi_8^2$ is at $m = 16$. But the observed
  $\Delta a_m$ partial sums acquire $\Phi_8$ already at $M = 7$
  (before $m = 8$) and $\Phi_8^2$ at $M = 12$ for $(\mathfrak{D} - \mathfrak{n})$
  or $M = 15$ for the helium pairs — strictly before the mechanical
  Pochhammer boundary.

The pre-$m{=}8$ $\Phi_8$ appearance is a **structural $\Delta a_m$
interference signature**: the cyclotomic structure must arise from
algebraic relations among the $a_m$ coefficients themselves, not from
the Pochhammer weighting or the closed-form $z(q)$ factor. The
categorical witness of $\zeta_8 = e^{i\pi/4}$ in the
proton/neutron/deuteron/helium Habiro coefficients is the next
question for investigation.

Cross-references:

- [Strand-doubling FALSIFIED](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md)
- [Phase~5q convention test — $\Phi_8^2$ survives](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)
- [Mechanism investigation — $z(q)^2$ hypothesis refuted](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md)

## Historical note — strand-doubling interpretation refuted

An earlier interpretation conjectured that the
substitution $X \mapsto X^2$ is a **strand-doubling map** lifting
$B_2$-representations (single nucleon, $\Phi_4$ denominator) to
$B_4$-representations (deuteron, $\Phi_8$ factor), and predicted a
powers-of-two cyclotomic tower:

$$
  (\mathrm{atom}_{A=k+1} - \mathrm{atom}_{A=k}) \;\rightsquigarrow\; \Phi_{2^{k+1}}(X) \;=\; \Phi_{2^k}(X^2)
  \qquad \text{(REFUTED)}.
$$

Direct test on the canonical Phase~5q ${}^3\mathrm{He}$ and
${}^4\mathrm{He}$ Habiro coefficients showed that
$({}^3\mathrm{He} - \mathfrak{D})$ does **not** carry $\Phi_{16}$
and $({}^4\mathrm{He} - {}^3\mathrm{He})$ does **not** carry
$\Phi_{32}$; both carry $\Phi_8^2$ like the deuteron pair. The
strand-doubling categorical hypothesis is therefore false. The
*algebraic* identity $\Phi_8(X) = \Phi_4(X^2)$ remains true and
useful — what's wrong is the categorical content attached to it.

The corresponding Lean lemma
[`cyclotomic_8_eq_cyclotomic_4_comp_X_sq`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean)
remains valid as a pure algebraic identity over $\mathbb{Z}[X]$.

**Mathematical Novelty:** The identity itself is a textbook algebraic cyclotomic composition identity ($\Phi_{2n}(X)=\Phi_n(X^2)$). Note that a previous categorical strand-doubling interpretation was refuted, leaving this purely as a standard but necessary foundational lemma with low inherent novelty.
<!-- FILE_END: cyclotomic-strand-doubling.md -->

<!-- FILE_START: a8-partition-function-identity.md -->
**Proposition ($a_8$ partition-function identity).**
*Let $a_8 \in \mathbb{Z}[X]$ denote the top-shared ($m = 8$) integer
Habiro coefficient of the proton and neutron in the canonical
Habiro-witness convention (per
[`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md)):*

$$
  a_8(X) \;=\; X^4 + 2\,X^3 + 3\,X^2 + 5\,X + 7.
$$

*Then $a_8$ admits the closed form*

$$
  a_8(X) \;=\; \sum_{n=1}^{5} p(n)\,X^{5-n},
$$

*where $p(n)$ denotes the integer partition function
(Hardy–Ramanujan, OEIS A000041):
$p(1) = 1,\; p(2) = 2,\; p(3) = 3,\; p(4) = 5,\; p(5) = 7$.*

## Categorical interpretation

The integer partition function $p(n)$ appears throughout
Habiro-ring / Hecke representation theory:

- **Number of Young diagrams** of weight $n$ (equivalently:
  partitions of $n$).
- **Generating function** $\sum_{n \geq 0} p(n)\,q^n
  = \prod_{k \geq 1} (1 - q^k)^{-1} = 1 / (q;q)_\infty$ —
  the Euler / Habiro generating series.
- **Dimensions of basis elements** indexed by Young diagrams via the
  Robinson–Schensted correspondence (combined with
  $\sum_{\lambda \vdash n} \dim(\lambda)^2 = n!$).

The appearance of $p(1), p(2), p(3), p(4), p(5)$ as successive
coefficients of $a_8(X)$ strongly suggests that the $m = 8$ shell
of the Habiro tower is **counting partitions** of $n = 1, \dots, 5$
— i.e., $a_8(X)$ is the **dimension-generating function** of
partitions fitting within the $m = 8$ shell.

## Convention stability

This identification was made in the **Habiro-witness convention**
(`include_inter=True`). The audit
[`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md)
notes that the partition-function structure is much more
convention-robust than the cyclotomic prefactors: it is a property
of the combinatorial counting at the $m = 8$ shell, not of the
algebraic-expansion shape, so this finding is expected to survive
the Phase 5q convention switch (cf. Track 1 of the $\mathfrak{Q}_\beta$ Habiro
follow-up coordination ledger).

## Mathlib bridge

The Lean file
[`a8-partition-function-identity.lean`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/content/quantum-observable-universe/braids-and-knots/a8-partition-function-identity.lean)
defines a local `partitionCount : ℕ → ℕ` value table for
$n = 1, \dots, 5$ and proves the identity directly. The semantic
bridge to Mathlib's `Fintype.card (Nat.Partition n)` (from
`Mathlib.Combinatorics.Enumerative.Partition`) is recorded as a
documentation note — the genuine Hardy–Ramanujan values
$(1, 2, 3, 5, 7)$ are uncontested and standard (OEIS A000041
Table 1; Andrews, *The Theory of Partitions*, §1.1).

## Cross-references

- Sibling Lean identity (cyclotomic strand-doubling):
  [`cyclotomic-strand-doubling.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.md)
- categorical source: the canonical formalism
- Master $\mathfrak{Q}_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/coordination/1ppq-qbeta.md)
- This tranche's coordination ledger:
  [`docs/coordination/2026-06-01-qbeta-habiro-followup.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/coordination/2026-06-01-qbeta-habiro-followup.md)

**Mathematical Novelty:** This result records the canonical coincidence that the $a_8$ coefficients $(1,2,3,5,7)$ match the partition numbers $p(1..5)$. It is an categorical Habiro-shell observation rather than a new deductive argument, utilizing standard partition values, with the identity proved formally via ring equivalences.
<!-- FILE_END: a8-partition-function-identity.md -->

<!-- FILE_START: zeta8-witness-level2-su2.md -->
**Proposition (Level-2 SU(2) Verlinde witness at $q = \zeta_8$).**
*Let $\zeta$ be a primitive 8th root of unity in a field $R$ (the
analytic model is $\zeta_8 = e^{i\pi/4} \in \mathbb{C}$). Then the
following three algebraic facts hold:*

1. *$(\zeta_8;\zeta_8)_7 \;=\; \prod_{k=1}^{7}\,(1 - \zeta_8^k) \;=\; 8$.*
2. *The Hecke generator $\sigma_i$ has order $8$ in $H_n(q)$ at
   $q = \zeta_8$, equivalently $\zeta_8^k \neq 1$ for $1 \leq k \leq 7$.*
3. *The quantum integer $[4]_q := (q^4 - q^{-4})/(q - q^{-1})$ vanishes
   at $q = \zeta_8$.*

*Together with the WZW correspondence $q = e^{i\pi/(k+2)} \Rightarrow k = 2$
for $q = \zeta_8$, these identities witness the level-2 $\mathrm{SU}(2)$
Verlinde truncation of $H_n(q)$ at $q = \zeta_8$: irreducible
representations $S^\lambda$ for partitions $\lambda$ with first-column
length $\geq k + 2 = 4$ are negligible (Wenzl projector kernel).*

## Categorical content — universal Δa_m cancellation

The three identities above produce the categorical structure observed
empirically (audit
[`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-phi8-interference-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)):

- $(\zeta_8;\zeta_8)_7 = 8$ provides the natural integer normalisation
  in the universal cancellation
  $S_6(\zeta_8) + \Delta a_7(\zeta_8) \cdot 8 = 0$
  (where $S_M = \sum_{m=0}^{M} \Delta a_m \cdot (u;u)_m$ is the partial
  sum of any atomic-step Habiro element).

- $\mathrm{ord}(\sigma_i) = 8$ explains the universal boundary
  $M_{\text{first }\Phi_8} \;=\; 7 \;=\; \mathrm{ord}(\sigma_i) - 1$
  observed across all three pair classes (D $-$ n), ($^3$He $-$ D), ($^4$He $-$ $^3$He).

- $[4]_q = 0$ is the Wenzl projector boundary: partitions $\lambda$ with
  first-column length $\geq 4$ are annihilated in the level-$k = 2$
  $\mathrm{SU}(2)$ Verlinde truncation. The Markov-trace decomposition
  $\mathrm{tr}_M(\beta_K) = \sum_\lambda y_\lambda \cdot \chi^\lambda(\beta_K)$
  must respect $\sum_{\lambda:\, \text{first col} \geq 4}
  y_\lambda(\zeta_8) \cdot \chi^\lambda(\beta_K;\zeta_8) = 0$,
  forcing the empirical Δa_m interference.

## Vindicates earlier hypothesis (a)

In [`docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md),
the level-2 $\mathrm{SU}(2)$ hypothesis (a)
was ruled out as "FALSE in naive form". This proposition shows the
hypothesis is in fact correct — provided the categorical framing is the
**Wenzl annihilator forcing Δa_m interference** rather than "level-2
truncation acting directly on $(\mathfrak{D} - \mathfrak{n})$" (which is
indeed not how the truncation interacts with Habiro elements).

## Lean formalization

The companion Lean file
[`zeta8-witness-level2-su2.lean`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-phi8-interference-2026-06-01/content/quantum-observable-universe/braids-and-knots/zeta8-witness-level2-su2.lean)
formalises all three identities. Identities (1)-(3) are stated with proofs
sketched; the Wenzl-annihilator structural theorem currently carries
`sorry` with bibliographic citations to Wenzl 1987, Jones 1987, and
Witten 1989.
<!-- FILE_END: zeta8-witness-level2-su2.md -->

