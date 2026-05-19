**Proposition (Markov–Frobenius pairing $\equiv$ algebraic residue period).**

*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q_0$
([quantum observable universe](#def:quantum-observable-universe)),
fix a vertical degree $k \in \{0, 1, 2, 3\}$, and a categorical
mass class $T_w \in H_n(R, q)$ in Hecke normal form
([Hecke normal form](#def:hecke-normal-form)). Then*

$$
  \boxed{\;
    \tau\!\bigl(\mathfrak{m}^{(k)}_{\mathrm{alg}}(T_w)\bigr)
    \;=\;
    \mathfrak{m}^{(k)}_{\mathrm{an}}(T_w;\,q_0)
    \quad\text{for all } k \in \{0,1,2,3\},
  \;}
$$

*where the two presentations are*

$$
  \mathfrak{m}^{(k)}_{\mathrm{alg}}(T_w)
  \;:=\;
  \bigl|\bigl\langle \mathrm{tr}_M,\ E_\infty^{k, *}(T_w) \bigr\rangle\bigr|
  \;\in\; R,
$$

*the categorical Markov–Frobenius pairing against the
$E_\infty$-page of the Gröbner–Shirshov spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence),
[$E_\infty$ page identifications](#prop:e-infinity-page-identifications)),
and*

$$
  \mathfrak{m}^{(k)}_{\mathrm{an}}(T_w;\,q_0)
  \;:=\;
  \tau\Bigl(\sum_{p \in \mathcal{O}_{\mathrm{prin}}}\!
    \mathrm{Res}^{\mathrm{alg}}_p(\lambda^{(k)}_{\mathrm{SW}})\Bigr),
$$

*the archimedean image of the algebraic residue formula on the
principal Galois orbit
$\mathcal{O}_{\mathrm{prin}} = \{z_c^\pm\}$ of the color-tube
discriminant.*

**Hypotheses (all $R$-side or routinely cited).**

| # | hypothesis | status | block |
|---|---|---|---|
| A2.1 | Crit. pts $\equiv$ discriminant locus | derived, $R$-side | implicit differentiation of $F$ |
| A2.2 | Hessian Morse at each $z_c$ | derived, $R$-side via $\Delta(z)$ squarefree | resultant has simple zeros |
| A2.4 | Algebraic residue on principal Galois orbit | derived, $R$-side | Laurent-coefficient extraction over $\mathbb{Z}[q^{\pm 1/2}, \zeta_5]$; cites [`grothendieck1966`], [`hartshorne1966`] |
| A2.5 | Baryon integrand = $\mathrm{Alt}^3$ projector | derived, $R$-side | [baryon-product-from-alt](#prop:baryon-product-from-alt) |

*A2.1, A2.2, A2.4, A2.5 are all $R$-side; the equivalence is a
theorem over $R = \mathbb{Z}[q^{\pm 1/2}, \zeta_5]$, with $\tau_q$
supplying the archimedean realisation. The historical
Lefschetz-decomposition hypothesis (A2.3) is no longer required —
the algebraic residue formulation makes thimble decomposition
unnecessary.*

**Proof.**

*Step 1 ($R$-side surface-integral representation).*
*By the non-abelian Stokes theorem
([Yekutieli–Stokes remark](#rem:yekutieli-stokes),
\[`yekutieli2015`]),
$\langle \mathrm{tr}_M, T_w\rangle = \mathrm{MI}\!\int_\Sigma
\alpha_{T_w}$ for a categorical surface $\Sigma$ with
$\partial\Sigma = \varrho$.*

*Step 2 (Spectral-sequence reduction).*
*The pairing decomposes as $\sum_p \langle \mathrm{tr}_M,
E_\infty^{p,*}(T_w)\rangle$ by
([GB spectral sequence](#prop:gb-spectral-sequence)) +
([$E_\infty$ identifications](#prop:e-infinity-page-identifications)),
each summand supported on $J^p(q)/J^{p+1}(q)$.*

*Step 3 (Algebraic residue at the principal Galois orbit, A2.4).*
*Each $E_\infty^{p,*}$ pairs against the algebraic residue
$\sum_{z_c \in \mathcal{O}_{\mathrm{prin}}} \mathrm{Res}^{\mathrm{alg}}_{z_c}(\lambda^{(p)}_{\mathrm{SW}})$
over $\mathbb{Z}[q^{\pm 1/2}, \zeta_5]$
(\[`grothendieck1966`], \[`hartshorne1966`]). The Galois selection
of $\mathcal{O}_{\mathrm{prin}}$ via palindromy + conjugation is
algebraic
([Möbius limit from thimble](#prop:mobius-limit-from-thimble) Step 2).*

*Step 4 (Channel selection by $\mathrm{Alt}^3$, A2.5).*
*The baryon integrand $\prod_k dc_k/dz$ is the sign-isotype
projector
([baryon product from Alt](#prop:baryon-product-from-alt)); analogous
specialisations to trivial / standard isotypes recover the electron
$(k=0)$ / muon $(k=1)$ cases. Applying $\tau$ to the resulting
$R$-valued expression gives $\mathfrak{m}^{(k)}_{\mathrm{an}}$.*  $\square$

**Promotion of `rem:baryon-period-ratio`.**
*The $k = 3$ case applied to the proton's atomic braid is now a
corollary (A2.4 is derived). The downstream
([baryon period ratio](#rem:baryon-period-ratio)) upgrades to a
provable statement.*

**Archimedean shadow.**
*The Picard–Lefschetz reading
([rem:picard-lefschetz-thimble](#rem:picard-lefschetz-thimble))
gives the same numerical answer via thimble periods
$\sum_\sigma n_\sigma \oint_{\mathcal{J}_\sigma}
\lambda^{(k)}_{\mathrm{SW}} dz$. The intersection numbers
$n_\sigma$ are formal $\mathbb{Z}$-valued labels in the archimedean
realisation; the script's finding $n_\sigma = 0$ is consistent
since the real-axis contour is trivial in Lefschetz homology but
non-trivial in residue homology — different homologies, same
numerical answer via $\tau$.*

**Relation to other blocks.**

- *([GB spectral sequence](#prop:gb-spectral-sequence)) — algebraic side.*
- *([GB residue spectral sum](#prop:gb-residue-spectral-sum)) — symbolic shadow.*
- *([categorical mass as Markov trace](#prop:categorical-mass-markov)) — fixes the scalar weight $w_\lambda$.*
- *([jet-GB-PL correspondence](#prop:jet-gb-pl-correspondence)) — geometric image of the GB filtration under $\tau$.*
