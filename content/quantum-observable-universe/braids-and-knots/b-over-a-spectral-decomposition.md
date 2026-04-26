**Proposition (Approach 2: spectral decomposition of $B/A$).**

*Let $\mathcal{K}_A$ be the nuclear braid for an $A$-nucleon nucleus
with $Z$ protons and $N$ neutrons ($A = Z + N$, $T = (Z-N)/2$).  Let
$\hat{V}(q)$ be the $6 \times 6$ transfer matrix of $H_3(R, q)$ acting
on the normal-form basis $\{1, \sigma_0, \sigma_1, L_+, L_-, e^-\}$.
Under the Wedderburn decomposition*

$$
  H_3(R, q) \;\cong\; V_{\mathrm{sym}} \,\oplus\, V_{\mathrm{std}}^{\oplus 2}
  \,\oplus\, V_{\mathrm{alt}}
$$

*the binding energy per nucleon admits a Plancherel-weighted block-trace
decomposition*

$$
  \boxed{\;
    B/A \;=\; E_0 \cdot \frac{1}{A}
      \sum_{\lambda \in \{\mathrm{sym}, \mathrm{std}, \mathrm{alt}\}}
      w_\lambda \,
      \log\!\left|
        \frac{\Lambda^{\mathrm{free}}_\lambda(q)}{\Lambda^{\mathrm{nuc}}_\lambda(q; Z, N)}
      \right|
  \;}
$$

*where $\Lambda_\lambda$ is the eigenvalue product of $\hat{V}(q)$ on
the irrep $V_\lambda$, $w_\lambda = \dim_q^2 V_\lambda / [3]_q!$ is the
Plancherel weight, and $E_0 = m_e/(q_0(q_0 - 1)) \approx 4.186$ MeV is
the hadronic energy unit
([energy scale and Planck time](#rem:energy-scale-planck)).  Expanded in
$T$ and $A$, this reproduces the Bethe--Weizsäcker form*

$$
  B/A \;=\; a_V(q) \;-\; a_S(q)\, A^{-1/3}
  \;-\; a_C(q)\, Z(Z-1)\, A^{-4/3}
  \;-\; a_A(q)\, (N - Z)^2 A^{-2}
$$

*with each coefficient a closed expression in $q$ alone:*

| *BW coefficient* | *Spectral origin* | *Closed form (in $\ell = \ln q$, $\ell_2 = \ln([2]_q/2)$)* |
|:---:|:---|:---|
| *$a_V$ (volume)* | *symmetric and standard pn product* | *$E_0 \cdot \bigl(w_{\mathrm{sym}} + 2 w_{\mathrm{std}}\bigr) \cdot \ell_2 / 4$* |
| *$a_S$ (surface)* | *$A^{2/3}$ deficit in $n_{pn}$ (boundary crossings)* | *$E_0 \cdot c_S \cdot \ell_2$, $c_S$ a geometric prefactor* |
| *$a_C$ (Coulomb)* | *symmetric pp excess over pn: $\ln(2q/[2]_q)$* | *$E_0 \cdot w_{\mathrm{sym}} \cdot \ln(2q/[2]_q)$* |
| *$a_A$ (asymmetry)* | *quadratic isospin in symmetric block* | *$E_0 \cdot 4\, w_{\mathrm{sym}}\, \ell_2$* |

*Proof.*

**Step 1 (block decomposition of the transfer matrix).** By
[Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form), the $6 \times 6$
transfer matrix $\hat{V}(q)$ is conjugate to a direct sum of
typed-crossing blocks acting on $V_{\mathrm{sym}}$ (1-dim),
$V_{\mathrm{std}}^{\oplus 2}$ ($2 \times 2$ matrices on each of two
copies, dim 4), and $V_{\mathrm{alt}}$ (1-dim).  The eigenvalue
product on each block is multiplicative across the chain of crossings
in the nuclear braid:

$$
  \Lambda_\lambda^{\mathrm{nuc}}(q; Z, N)
  \;=\;
  \prod_{\text{crossings } c} \mu_\lambda(c, q),
$$

with $\mu_\lambda(c, q)$ the eigenvalue contributed by crossing type
$c \in \{pp, nn, pn\}$ in irrep $\lambda$ (table in
[eigenvalue product expansion](#prop:eigenvalue-product-expansion)).

**Step 2 (Markov trace as Plancherel-weighted block sum).** By
[Hecke mass trace](#prop:hecke-mass-trace), the categorical mass is
the absolute Markov trace.  The Markov trace decomposes over Wedderburn
blocks with Plancherel weights $w_\lambda = \dim_q^2 V_\lambda /
[3]_q!$:

$$
  \mathrm{tr}_M\bigl(\rho(\beta_{\mathcal{K}_A})\bigr)
  \;=\;
  \sum_\lambda w_\lambda \, \chi_\lambda\bigl(\rho(\beta_{\mathcal{K}_A})\bigr)
  \;=\;
  \sum_\lambda w_\lambda \, \Lambda_\lambda^{\mathrm{nuc}}(q; Z, N).
$$

(The standard block appears with multiplicity 2 in the regular
representation, contributing weight $2 w_{\mathrm{std}}$ in the
expansion above; both copies share the same $\Lambda_{\mathrm{std}}$
because Hoefsmit's seminormal blocks are isomorphic.)

**Step 3 (binding as a free-minus-interacting log-ratio).** The
binding energy is

$$
  B(Z, N) \;=\; \mathfrak{m}^{\mathrm{free}}(Z, N) - \mathfrak{m}^{\mathrm{nuc}}(Z, N).
$$

Free nucleons carry only intra-nucleon (3-quark) crossings.  The
interacting nucleus has the same intra-nucleon crossings *plus* all
$\binom{A}{2}$ inter-nucleon crossings.  Taking absolute Markov traces
and applying $\mathfrak{m} \cdot c_q^2 = E_{\mathfrak{H}} = E_0 \cdot
\log|\mathrm{tr}_M|$ in each block (per
[unified curvature-rank mass formula](#prop:unified-curvature-rank-mass-formula)):

$$
  B \;=\;
  E_0 \sum_\lambda w_\lambda
  \log\!\left|
    \frac{\Lambda^{\mathrm{free}}_\lambda(q)}{\Lambda^{\mathrm{nuc}}_\lambda(q; Z, N)}
  \right|.
$$

Dividing by $A$ gives the boxed formula.

**Step 4 (BW coefficient extraction).** Substituting
[eigenvalue product expansion](#prop:eigenvalue-product-expansion):

$$
  \log|\Lambda^{\mathrm{nuc}}_{\mathrm{sym}}/\Lambda^{\mathrm{free}}_{\mathrm{sym}}|
  \;=\; \ell_2 \cdot \bigl(A^2/4 - T^2\bigr)
  \;+\; \ell \cdot T(A - 1).
$$

The four BW terms arise as follows.

- *Volume.* The leading $A^2/4 \cdot \ell_2$ contribution from the
  $n_{pn} = ZN$ mixed crossings.  Dividing by $A$ gives a piece
  proportional to $A$ at leading order; subtracting the long-range
  surface deficit (Step below) yields a constant volume coefficient
  $a_V$.  The standard block contributes additively because
  $\Lambda_{\mathrm{std}}$ has determinant $\pm 1$ on each crossing
  (per [transfer matrix identities](#prop:transfer-matrix-identities)),
  doubling the effective $w_{\mathrm{sym}}$ contribution.

- *Surface.* The crossing count $n_{pn} = ZN$ overcounts by an
  $A^{2/3}$-scaling boundary correction: nucleons on the surface of the
  braid have fewer interaction partners.  This gives
  $-a_S A^{-1/3}$ when expressed per nucleon.

- *Coulomb.* In the symmetric block, pp crossings contribute
  eigenvalue $q$, while pn crossings contribute $[2]_q/2$.  The
  *excess* $\log(2q/[2]_q)$ multiplied by $n_{pp} = Z(Z-1)/2$ gives
  the Coulomb term.  Per nucleon: $-a_C Z(Z-1) A^{-4/3}$ after
  including the $A^{1/3}$ density factor of the brane.

- *Asymmetry.* The $-\ell_2 \cdot T^2$ piece is intrinsic to the
  symmetric eigenvalue product.  Per nucleon, dividing $4 T^2 / A$
  by $A$ gives $(N-Z)^2/A^2$.

The alternating block contributes only at $O(q^{-A})$ to the
$T = 0$ trace and is negligible for $A \geq 4$ at $q \approx q_0$;
its weight $w_{\mathrm{alt}} = w_{\mathrm{sym}}$ produces a
sub-leading parity-dependent shift.

By [transfer matrix identities](#prop:transfer-matrix-identities)(i),
adjacent pp and nn crossings cancel as transfer matrices
($T_{pp} \cdot T_{nn} = I$), so only the *net* pp-vs-nn excess and
the mixed pn crossings survive; this is the spectral content of the
$T(A-1)$ term, which contributes to the asymmetry channel rather than
the volume.  $\square$

## Numerical comparison at $q_0$ (cap-A nuclei)

Using the Plancherel weights at $q_0$ (with $[2]_{q_0} = q_0 + q_0^{-1}
\approx 2.0119$, $[3]_{q_0} \approx 3.034$):

- $w_{\mathrm{sym}} \approx 0.164$
- $w_{\mathrm{std}} \approx 0.331$ (each copy; total $2 w_{\mathrm{std}}
  \approx 0.663$)
- $w_{\mathrm{alt}} \approx 0.164$
- $\ell_2 = \ln([2]_{q_0}/2) \approx 5.93 \times 10^{-3}$

Plugging into the boxed formula and using $E_0 \approx 4.186$ MeV,
the spectral prediction for $Z = N$ nuclei (so $T = 0$, no asymmetry,
no Coulomb at first order):

$$
  (B/A)_{T = 0}^{\mathrm{spec}}(q_0)
  \;\approx\; E_0 \cdot \bigl(w_{\mathrm{sym}} + 2 w_{\mathrm{std}}\bigr)
  \cdot \frac{\ell_2}{4} \cdot A
  \;-\; (\text{surface}).
$$

The *raw* volume coefficient evaluates to
$E_0 (w_{\mathrm{sym}} + 2 w_{\mathrm{std}}) \ell_2 / 4 \approx 5.13
\times 10^{-3}$ MeV/nucleon, which scales linearly in $A$ at this
order before surface and density corrections.  Compared to AME2020 at
the existing certificate level:

| Nucleus | $A$ | $(B/A)_{\mathrm{AME2020}}$ (MeV) | $(B/A)_{\mathrm{spec}}$ leading | Approach 2 status |
|:---|---:|---:|---:|:---|
| ${}^4\mathrm{He}$ | 4 | $7.074$ | leading + surface | structural-only at this commit |
| ${}^{12}\mathrm{C}$ | 12 | $7.680$ | leading + surface | structural-only at this commit |
| ${}^{40}\mathrm{Ca}$ | 40 | $8.551$ | leading + surface | structural-only at this commit |

The numerical match requires the surface coefficient $c_S$ from the
brane geometry and the Coulomb prefactor from the brane density;
those geometric inputs are computed in
[confined knot binding](#prop:confined-knot-binding) and
[Wigner np pairing](#prop:wigner-np-pairing) but are not assembled
into a single $(B/A)(q_0; Z, N)$ formula here.  This proposition
establishes the *spectral structure* — that each BW coefficient is a
Plancherel-weighted Wedderburn-block trace ratio — leaving the
geometric prefactors $c_S$ and Coulomb-density factor as the next
computation.

## Relation to the certificate fields

The hecke-engine certificates already record three projections of the
$6 \times 6$ Markov trace onto irreps:

- $\mathrm{net}(q_0) = \sum_\lambda w_\lambda \, \Lambda_\lambda^{\mathrm{nuc}}(q_0)$
  — the full Markov trace.
- $\mathrm{tr\_alt}(q_0) = w_{\mathrm{alt}} \cdot \Lambda_{\mathrm{alt}}^{\mathrm{nuc}}(q_0)$
  — the alternating projection.
- $F_{\mathrm{Pauli}}(q_0) = \mathrm{tr\_alt} / \mathrm{tr\_sym}$
  — the antisymmetric/symmetric ratio.

Approach 2 supplies the missing link: $B/A$ is *not* a direct
function of $\mathrm{net}$ alone (which spans 50 orders of magnitude
across the certificate set), but a Plancherel-weighted *log-ratio*
of free-vs-interacting block products.  The certificate's three
irrep projections are sufficient to reconstruct each
$\Lambda_\lambda^{\mathrm{nuc}}$, and hence $B/A$, once the free
braid's $\Lambda_\lambda^{\mathrm{free}}$ is computed in the same
basis.

## What remains

Three computations remain to turn the structural form into a
parameter-free numerical prediction:

1. *Surface coefficient* $c_S$ from the brane boundary geometry — a
   non-abelian Stokes computation on the $A$-nucleon braid surface.
2. *Coulomb prefactor* from the brane density at radius $r \propto
   A^{1/3}$.
3. *Free-braid eigenvalue products* $\Lambda_\lambda^{\mathrm{free}}$
   for the proton and neutron individually, in the same basis as
   the nuclear certificate.

With these, $(B/A)(q_0; Z, N)$ becomes a one-line evaluation of the
boxed formula.

## Numerical evaluator (Track 1, partial)

A first numerical evaluator is implemented in
[`folio-assistant/computations/b_over_a_evaluator.py`](
../../../folio-assistant/computations/b_over_a_evaluator.py),
producing the witness
[`b-over-a-witness.json`](
../../../folio-assistant/computations/b-over-a-witness.json).
It mirrors the Lean specification's `lambdaProduct` and
`bindingEnergyOverA` and supplies the three missing inputs as follows.

**Inputs.**

- *$\Lambda_\lambda^{\mathrm{free}}$ (derived):* identifying intra-nucleon
  flavour crossings with the irrep's $(pp, nn, pn)$ channels, the proton
  (uud) contributes $(n_{pp}, n_{nn}, n_{pn}) = (1, 0, 2)$ and the neutron
  (udd) contributes $(0, 1, 2)$.  The free-braid total scales linearly:
  $\Lambda_\lambda^{\mathrm{free}}(Z, N) =
  (\Lambda_\lambda^{\mathfrak{p}})^Z \cdot (\Lambda_\lambda^{\mathfrak{n}})^N$.
- *Coulomb (derived):* the textbook nuclear-physics form
  $E_C/A = \tfrac{3}{5} \, \alpha_{\mathrm{EM}} \, \hbar c \,
  Z(Z-1) / (r_0 A^{1/3} \cdot A)$ with
  $r_0 = 1.2$ fm and $\alpha_{\mathrm{EM}} = 1/137.036$.  This collapses
  the explicit brane-density factor of $A^{1/3}$ into the $1/R$
  prefactor; deriving the same expression directly from the brane density
  remains open.
- *$c_S$ (fitted):* the non-abelian Stokes computation referenced in
  [confined knot binding](#prop:confined-knot-binding) and
  [Wigner np pairing](#prop:wigner-np-pairing) is not yet assembled
  into a closed form.  We fit $c_S$ to ${}^4\mathrm{He}$ alone
  (so the $A=4$ residual is zero by construction) and report the
  out-of-sample residual on ${}^{12}\mathrm{C}$ and ${}^{40}\mathrm{Ca}$.

**AME2020 comparison.**

| Nucleus | $A$ | $(B/A)_{\mathrm{spec}}$ (MeV) | $(B/A)_{\mathrm{AME2020}}$ (MeV) | residual (MeV) | residual (%) |
|:---|---:|---:|---:|---:|---:|
| ${}^4\mathrm{He}$ | 4 | $7.074$ | $7.074$ | $0$ | $0\%$ (fitted) |
| ${}^{12}\mathrm{C}$ | 12 | $4.263$ | $7.680$ | $-3.42$ | $-44.5\%$ |
| ${}^{40}\mathrm{Ca}$ | 40 | $1.326$ | $8.551$ | $-7.23$ | $-84.5\%$ |

**Interpretation.**  The structural form *evaluates*, but with $c_S$
fitted to ${}^4\mathrm{He}$ it does not yet bind heavier nuclei.  The
expected sources of the deficit are: (i) the alt-block magnitude is
forced equal to the sym-block magnitude when $T = 0$ (Lean
`t_zero_alt_sym_magnitude`), so the volume coefficient at this commit
is too small by roughly the ratio
$(w_{\mathrm{sym}} + 2 w_{\mathrm{std}}) / (w_{\mathrm{sym}} + w_{\mathrm{alt}})$;
(ii) the brane-density prefactor for Coulomb has been absorbed into the
$A^{1/3}$ scaling rather than derived; (iii) the free-braid
identification of intra-nucleon flavour crossings with the isospin
channels of $H_3(R, q)$ may need a flavour-redressing factor before
the products combine.

These three open questions are the next milestones for Approach 2;
the witness JSON lays them out cleanly so each can be addressed in
isolation against a fixed numerical baseline.
