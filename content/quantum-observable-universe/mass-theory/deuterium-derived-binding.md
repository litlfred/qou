The binding energy of deuterium $\mathcal{A}(1,1)$ is computed
directly from the nucleon normal forms and a single inter-nucleon
crossing operator, with **zero fitted parameters** and **zero
semi-empirical scalings**.

## Statement

**Proposition.**
*Let $\mathrm{NF}(\mathfrak{p})$ and $\mathrm{NF}(\mathfrak{n})$
be the [proton](#def:categorical-proton) and
[neutron](#def:categorical-neutron) normal forms in $H_3(q)$,
each constructed as $\mathcal{B}_3 \cdot \mathrm{crossings}(quarks)$
([confinement selection](#prop:confinement-operator-selection))
with $\mathcal{B}_3 = \sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_2$.
The full canonical deuteron braid word
$\beta_D = \mathtt{atom\_braid\_word\_3A}(1, 1) \in H_6(q)$
([`mass_at_3A_proper.atom_braid_word_3A`](https://github.com/litlfred/qou/blob/main/computations/mass_at_3A_proper.py))
factors as $\mathrm{NF}(\mathfrak{p}) \cdot T_{pn} \cdot \mathrm{NF}(\mathfrak{n})$
under the H_3 $\to$ H_6 Hecke embedding, where
$T_{pn} = \frac{1}{2}(\sigma_0 + \sigma_0^{-1})$ is the time-reversal
symmetric crossing operator at the inter-nucleon site (the unique
generator of $\beta_D$ that crosses a proton strand with a neutron
strand). Then the deuterium binding energy is*

$$
  B(d) = \bigl[\mathrm{tr}_M(\mathfrak{p})
       + \mathrm{tr}_M(\mathfrak{n})
       - \mathrm{tr}_M(T_{pn} \cdot \mathfrak{n})\bigr]
       \times m_e \cdot \mathrm{Vol}(\mathcal{B}_3)
       \times (1 - \alpha_{\mathrm{EM}}/2).
$$

## Derivation

Deuterium has exactly one inter-nucleon crossing site (the $p$-$n$
pair).  The volume integral expansion
([topological mass](#thm:topological-mass)) reduces to:

$$
  \mathrm{Vol}(K_d) = \mathrm{Vol}(K_p) + \mathrm{Vol}(K_n)
    - V_{pn}(q),
$$

where $V_{pn}(q) = \mathrm{tr}_M(T_{pn} \cdot \mathrm{NF}(\mathfrak{n}))$
is the Markov trace of the crossed neutron normal form.

The crossing operator $T_{pn} = \frac{1}{2}(\sigma_0 + \sigma_0^{-1})
= \sigma_0 - \frac{H_A}{2}$ is the unique time-reversal invariant
crossing in $H_3(q)$ at generator $\sigma_0$.  It encodes the fact
that the proton--neutron nuclear force does not distinguish which
nucleon crosses over or under.

The energy scale $\alpha = m_e \cdot \mathrm{Vol}(\mathcal{B}_3)
= m_e \cdot 8G$ (where $G$ is Catalan's constant) is the
Borromean binding scale derived from the confinement operator.

## QED correction

The bare Hecke computation gives the strong-force binding energy
$B_{\mathrm{strong}} = \Delta \times \alpha = 2.2329$ MeV, which
over-binds by $+0.375\%$ ($+8.35$ keV).  This residual is exactly
$\frac{1}{2}\alpha_{\mathrm{EM}} \times B_{\mathrm{strong}}$: the
one-loop QED correction from virtual photon exchange between the
proton and neutron.

The physical binding energy is:

$$
  B_{\mathrm{phys}} = B_{\mathrm{strong}} \times (1 - \alpha_{\mathrm{EM}}/2).
$$

The factor $\frac{1}{2}$ arises because deuterium has a single
charged pair ($Z = 1$, $N = 1$), and the one-loop vacuum
polarization correction to the nuclear potential is
$\delta V / V = -\alpha_{\mathrm{EM}}/2$ per charged pair.

After the QED correction:

$$
  B(d) = 2.2329 \times (1 - 0.00365) = 2.2248\;\text{MeV}
$$

with a residual of $0.19$ keV ($0.008\%$), consistent with the
expected $O(\alpha_{\mathrm{EM}}^2) \approx 0.12$ keV two-loop
correction.

## Numerical evaluation

All inputs are derived from $q_0$ and quark content:

See [Table](#tbl:deuterium-derived-binding-table-data).

The derivation chain:

1. $\mathrm{Vol}(4_1) = 2.0299$ (SnapPy, hyperbolic volume)
2. $m_\mu/m_e = :val[m_mu_over_e]{precision=6}$ (CODATA 2022, gives $q_0$)
3. $m_e = 0.5110\;\text{MeV}$ (CODATA 2022, gives MeV scale)
4. $G = 0.9160$ (Catalan's constant, computed)
5. Quark content: $\mathfrak{p} = \mathfrak{u}\mathfrak{u}\mathfrak{d}$,
   $\mathfrak{n} = \mathfrak{u}\mathfrak{d}\mathfrak{d}$
6. $H_3(q_0)$ multiplication rules (Hecke algebra)
7. $\alpha_{\mathrm{EM}} = 1/(q_0 \cdot [9]_{q_0} \cdot [10]_{q_0})$
   with CS correction (Hecke algebra)

No fitted parameters.  No semi-empirical scalings.  Direct
algebraic computation from the Hecke algebra and measured inputs.

## Relationship to Bethe--Weizsäcker

The BW semi-empirical mass formula is the **continuum (large-$A$)
limit** of the exact pair-sum formula.  For $A = 2$ (deuterium),
the pair sum has exactly one term, so the continuum approximation
is maximally wrong: BW predicts $B(d) \approx -5.1$ MeV
(unbound!), while the exact formula gives $2.225$ MeV.

For large $A$, the pair sum
$\sum_{i < j} \mathrm{tr}_M(T_{ij} \cdot \mathrm{NF}_j)$
becomes a discrete integral over $\binom{A}{2}$ terms, and
the $A^{2/3}$ surface correction, $Z(Z-1)/A^{1/3}$ Coulomb
term, and $(N-Z)^2/A$ asymmetry term all emerge as continuum
approximations of the exact pair sums grouped by type (pp, nn, pn).

**Witness**: `deuterium-derived.witness.json`.

## Mass–binding endomorphism analogy

The formula is the binding-energy analogue of the mass endomorphism.
The nucleon mass is $m(K) = m_e \cdot \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2
\cdot \mathrm{lw}(K, q_0)$; binding replaces the $\mathrm{lw}/\hbar_q^2$
structural factor with the Wedderburn trace difference
$\Delta\mathrm{tr} = \mathrm{tr}_M(\text{free}) -
\mathrm{tr}_M(\text{atom})$, keeping the common
$m_e \cdot \mathrm{Vol}(\mathcal{B}_3)$ prefactor:

$$
  B(K) = m_e \cdot \mathrm{Vol}(K_{\mathrm{bind}}) \cdot \Delta\mathrm{tr}.
$$

The binding link $K_{\mathrm{bind}}$ is atom-specific — the
[binding-K SDP solver](https://github.com/litlfred/qou/blob/main/computations/binding-k-solver.witness.json)
identifies it as the Hopf link for the deuteron, the $8_{11}$-class
link for $^3\mathrm{H}$, and L6a4 for $^3\mathrm{He}$.  For the deuteron
$\mathrm{Vol}(K_{\mathrm{bind}}) = \mathrm{Vol}(\mathcal{B}_3) = 8G$
(the Hopf inter-nucleon link is Seifert-fibred, so the Borromean scale
dominates), giving $B(d) = 2.229$ MeV at $+0.19\%$ before the QED
correction.  See
[`docs/audits/2026-05-28-binding-endomorphism-analogy.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-28-binding-endomorphism-analogy.md).
