**Proposition (GB ↔ jet ↔ PL keystone).**

*Let $H_n(R, q)$ carry the Gröbner–Shirshov filtration
$\{J^p(q)\}_{p \geq 0}$
([GB spectral sequence](#prop:gb-spectral-sequence)), let $J^p(A)$ be
the categorical jet object at vertical order $p$
([jet prolongation, $\mathbb{C}$-realisation](#cor:jet-prolongation-C)),
let $J^p\mathcal{S}$ be the $p$-th geometric jet bundle on
$\mathcal{E}_q(\mathbb{C})$, and let $\Pi^{(p)}$ denote the
Picard–Lefschetz period at order $p$.  The four-way correspondence:*

$$
  \boxed{\;
    \underbrace{E_0^p(q)}_{R\text{-side}}
    \;\xleftrightarrow{\;\sigma_p\;}\;
    \underbrace{J^p(A)}_{\mathbf{C}\text{-side}}
    \;\xrightarrow{\;\tau\;}\;
    \underbrace{J^p\mathcal{S}}_{\mathcal{E}_q(\mathbb{C})}
    \;\xleftrightarrow{\;\lambda^{(p)}_{\mathrm{SW}}\;}\;
    \underbrace{\Pi^{(p)}}_{\text{archimedean shadow}}
  \;}
$$

*All arrows are compatible with the Markov–Frobenius pairing on the
$R$-side and the algebraic-residue formula
([sw-period thimble equivalence](#prop:sw-period-thimble-equivalence))
on the archimedean side.*

**Four columns of the correspondence.**

| $p$ | $E_0^p$ (R-side) | $J^p(A)$ ($\mathbf{C}$) | $J^p\mathcal{S}$ (geometric) | $\Pi^{(p)}$ (PL shadow) |
|---|---|---|---|---|
| $0$ | $J^0/J^1$ | $A$ | $\mathcal{S}$ | $\oint (c+z)\,dz$ (electron) |
| $1$ | $J^1/J^2$ | first jet | $J^1\mathcal{S}$ | $\oint (dc/dz)\,dz$ (muon) |
| $2$ | $J^2/J^3$ | pair jet | $J^2\mathcal{S}$ | pair residue at $z_c$ |
| $\geq 3$ | $J^p/J^{p+1}$ | $p$-jet | $J^p\mathcal{S}$ | higher PL corrections |

**Proof.**

*Step 1: $\sigma_p: J^p(A) \xrightarrow{\sim} E_0^p$ is the
associated-graded isomorphism from
([GB spectral sequence](#prop:gb-spectral-sequence)). Both
constructions give the same $\mathbf{C}$-object.*

*Step 2: $\tau$ converts $J^p(A) \mapsto J^p\mathcal{S}$ by
([jet prolongation, $\mathbb{C}$-realisation](#cor:jet-prolongation-C));
the Frobenius–Hopf coalgebra becomes the standard linear connection.*

*Step 3: $\lambda^{(p)}_{\mathrm{SW}}$ is the tautological section on
$J^p\mathcal{S}$. The PL period $\Pi^{(p)}$ is its archimedean
realisation; the underlying algebraic statement is the residue
formula of
([sw-period thimble equivalence](#prop:sw-period-thimble-equivalence)).
$\square$*

**Term 6 of the mass tower.**
*The $p \geq 3$ stratum corresponds to $J^p\mathcal{S}$ for $p \geq 3$;
its archimedean shadow is $\Pi^{(p)}$. Term 6 in
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications))
is recovered by the same residue machinery as Terms 1–3.*

**Mass-endomorphism tower extension.**
*The $|S| = 3$ contribution to
([mass-endomorphism tower](#prop:mass-endomorphism-tower)) is the
simultaneous product of three colour-sheet prolongations — the
$\mathrm{Alt}^3$ projector
([baryon product from Alt](#prop:baryon-product-from-alt)) restricted
to $J^3/J^4$, i.e. the baryon channel $\Pi^{(3)}$.*
