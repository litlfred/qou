**Proposition (the GB ↔ jet ↔ PL keystone).**

*Let $H_n(R, q)$ carry the Gröbner–Shirshov filtration
$\{J^p(q)\}_{p \geq 0}$ with associated graded
$E_0^p(q) = J^p(q)/J^{p+1}(q)$
([GB spectral sequence](#prop:gb-spectral-sequence)).  Let
$J^p(A) \in \mathbf{C}$ denote the categorical jet object at vertical
order $p$
([jet prolongation, $\mathbb{C}$-realisation](#cor:jet-prolongation-C)).
Let $\mathcal{S} \to \mathcal{E}_q$ be the state bundle and
$J^p\mathcal{S}$ its $p$-th geometric jet bundle
on the archimedean realisation of $\mathcal{E}_q$.  Let
$\lambda_{\mathrm{SW}}^{(p)}$ denote the $p$-th jet prolongation of
the Seiberg–Witten differential, and $\Pi^{(p)}$ the corresponding
Picard–Lefschetz thimble period
([Picard–Lefschetz thimble](#rem:picard-lefschetz-thimble),
 [SW-period thimble equivalence](#prop:sw-period-thimble-equivalence)).*

*The four-way correspondence holds:*

$$
  \boxed{\;
    \underbrace{E_0^p(q)}_{\text{algebraic, over } R}
    \;\xleftrightarrow{\ \text{symbol map }\sigma_p\ }\;
    \underbrace{J^p(A)}_{\text{categorical, in }\mathbf{C}}
    \;\xrightarrow{\;\;\tau\;\;}\;
    \underbrace{J^p\mathcal{S}}_{\text{geometric, on }\mathcal{E}_q(\mathbb{C})}
    \;\xleftrightarrow{\ \lambda^{(p)}_{\mathrm{SW}}\ }\;
    \underbrace{\Pi^{(p)}}_{\text{archimedean, in }\mathbb{C}}
  \;}
$$

*All four arrows are compatible with the Markov–Frobenius pairing
$\mathrm{tr}_M$ on the algebraic side and the contour pairing on the
analytic side:*

$$
  \tau\bigl\langle \mathrm{tr}_M, E_\infty^{p, *}(T_w)\bigr\rangle
  \;=\;
  n_p \cdot \Pi^{(p)}(T_w; q_0),
  \qquad n_p \in \mathbb{Z}_{>0},
$$

*where $n_p$ records the number of distinct conjugate-paired thimbles
contributing at order $p$ (and absorbs the intersection numbers
$n_\sigma^{(p)}$ from the Lefschetz decomposition, cf.
[SW-period thimble equivalence](#prop:sw-period-thimble-equivalence)).*

**The four columns of the correspondence.**

| stratum index $p$ | algebraic $E_0^p$ over $R$ | categorical $J^p(A)$ in $\mathbf{C}$ | geometric $J^p\mathcal{S}$ on $\mathcal{E}_q(\mathbb{C})$ | archimedean PL period |
|---|---|---|---|---|
| $0$ | $J^0/J^1$ (no GB rewrite) | $J^0(A) = A$ | base bundle $\mathcal{S}$ | $\Pi^{(0)} = \oint (c+z)\,dz$ — electron |
| $1$ | $J^1/J^2$ (one GB step) | $J^1(A)$ — first jet | $J^1\mathcal{S}$ — 1-jet bundle | $\Pi^{(1)} = \oint (dc/dz)\,dz$ — muon residue |
| $2$ | $J^2/J^3$ (pair-jet) | $J^2(A)$ — pair jet | $J^2\mathcal{S}$ — 2-jet bundle | $\Pi^{(2)}$ — pair residue at $z_c$ |
| $\geq 3$ | $J^p/J^{p+1}$ (high jets) | $J^p(A)$ | $J^p\mathcal{S}$ | $\Pi^{(p)}$ — higher PL corrections (jet prefix) |

**Strict archimedean split.**

*The four columns split sharply across $\tau$:*

- *The first two ($E_0^p$, $J^p(A)$) live entirely on the $R$-side.
  The symbol map $\sigma_p \colon J^p(A) \xrightarrow{\;\sim\;}
  E_0^p(q)$ is an isomorphism of $\mathbf{C}$-objects whose target is
  evaluated by the Markov trace to a quantity in $R$.*
- *The latter two ($J^p\mathcal{S}$, $\Pi^{(p)}$) live entirely on the
  $\mathbb{C}$-side.  $J^p\mathcal{S}$ is a holomorphic vector bundle
  on $\mathcal{E}_q(\mathbb{C})$; $\Pi^{(p)}$ is a contour integral
  in $\mathbb{C}$.*
- *The horizontal arrow $\tau \colon J^p(A) \to J^p\mathcal{S}$ is the
  archimedean fibre functor applied to the categorical jet object
  ([jet prolongation, $\mathbb{C}$-realisation](#cor:jet-prolongation-C)).
  This is **the only place** $R \hookrightarrow \mathbb{C}$ occurs in
  the diagram.*

*Stating the correspondence requires both sides; **using** it requires
declaring which side one is on at every step.  The proposition is
careful to keep the $R$-side and $\mathbb{C}$-side computations
formally distinct: equalities in $R$ are not automatically equalities
in $\mathbb{C}$, but become so after $\tau$.*

**Proof sketch.**

**Step 1 (GB symbol = categorical jet symbol, $R$-side).**
*The symbol map $\sigma_p$ is an isomorphism of associated-graded
modules by the GB construction
([GB spectral sequence](#prop:gb-spectral-sequence)); the categorical
jet object is defined as the same associated-graded data on the
Frobenius–Hopf algebra $A$ via the diagonal coproduct
([jet prolongation, $\mathbb{C}$-realisation](#cor:jet-prolongation-C)).
Both constructions yield the same $\mathbf{C}$-object $E_0^p$.*

**Step 2 (Fibre-functor compatibility, archimedean.)**
*By
([jet prolongation, $\mathbb{C}$-realisation](#cor:jet-prolongation-C)),
$\tau$ converts the categorical jet object $J^p(A)$ to the geometric
$p$-jet bundle $J^p\mathcal{S}$ on $\mathcal{E}_q(\mathbb{C})$ — and
the Frobenius–Hopf coalgebra structure on $A$ becomes the standard
linear connection on $J^p\mathcal{S}$.  This is one application of the
proposition above; no additional analytic input is required.*

**Step 3 (SW differential is the tautological section.)**
*On $J^p\mathcal{S}$, the Seiberg–Witten differential
$\lambda_{\mathrm{SW}}^{(p)}$ is the tautological section that
restricts to $\lambda_{\mathrm{SW}}^{(0)}$ on the base $\mathcal{S}$
and prolongs covariantly under the connection of Step 2.  This
identification is the geometric image of the GB filtration's
Frobenius pairing on $E_0^p$.*

**Step 4 (PL evaluation reads off the residues, archimedean.)**
*By
([SW-period thimble equivalence](#prop:sw-period-thimble-equivalence)),
the contour pairing $\Pi^{(p)}$ extracts the residues of
$\lambda_{\mathrm{SW}}^{(p)}$ at the discriminant locus
$\{z : \Delta(z) = 0\}$, weighted by the Picard–Lefschetz intersection
numbers.  Each residue is a $\mathbb{C}$-saddle-point integral; the
sum over $\sigma$ recovers the spectral-sequence pairing's
$\mathbb{C}$-realisation. $\square$*

**Term 6 of the mass tower.**

*Open Term 6 in
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications))
("higher jet prefix") is now identified geometrically: the
$p \geq 3$ stratum corresponds to the higher-jet bundles
$J^p\mathcal{S}$ on $\mathcal{E}_q(\mathbb{C})$, and its archimedean
realisation is the higher-order Picard–Lefschetz residue
$\Pi^{(p \geq 3)}$.  This collapses Term 6 from "conjectural" to a
straightforward PL computation with the same machinery used for
Terms 1–3.*

**Extension of the mass-endomorphism tower beyond $|S| = 2$.**

*In
([mass-endomorphism tower](#prop:mass-endomorphism-tower)), the
"tower" representation $\mathrm{Vol}_q^{\mathrm{tower}}(\beta)$ is
truncated at subset size $|S| \leq 2$.  The keystone correspondence
extends the truncation: the $|S| = 3$ contribution corresponds
exactly to the **simultaneous product of three colour-sheet
prolongations**, which is the baryon channel of
([baryon product from Alt](#prop:baryon-product-from-alt)) — i.e.
the $\mathrm{Alt}^3$ projector restricted to the size-$3$ stratum
$J^3/J^4$.  Under PL, this becomes the baryon period $\Pi^{(3)}$.
Higher $|S| \geq 4$ contributions are accessible by the same
correspondence at $J^p\mathcal{S}$ for $p \geq 4$.*

**Categorical / archimedean status.**

*This proposition is the **single bridge** that allows downstream
chapters to use PL results in arguments that began in the categorical
chapters.  Without it, the Markov–Frobenius pairing in
$\mathbf{C}$-side blocks and the SW periods in PL-side blocks are two
parallel formal systems with no inter-translation.  All cross-paragraph
edits in this PR (in
[GB spectral sequence](#prop:gb-spectral-sequence),
[GB residue spectral sum](#prop:gb-residue-spectral-sum),
[mass-endomorphism tower](#prop:mass-endomorphism-tower)) refer back
here for the formal license to switch sides of $\tau$.*
