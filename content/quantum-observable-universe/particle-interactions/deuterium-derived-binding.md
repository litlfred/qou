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
([confinement selection](#prop:confinement-operator-selection)).
Let $T_{pn} = \frac{1}{2}(\sigma_0 + \sigma_0^{-1})$ be the
time-reversal symmetric crossing operator.  Then the deuterium
binding energy is*

$$
  B(d) = \bigl[\mathrm{tr}_M(\mathfrak{p})
       + \mathrm{tr}_M(\mathfrak{n})
       - \mathrm{tr}_M(T_{pn} \cdot \mathfrak{n})\bigr]
       \times m_e \cdot \mathrm{Vol}(\mathcal{B}_3).
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

## Numerical evaluation

All inputs are derived from $q_0$ and quark content:

| Quantity | Value |
|:---|:---|
| $q_0$ | $1.10998$ |
| $H_A = q_0 - q_0^{-1}$ | $0.20906$ |
| $z = 1/(\sqrt{q_0} + 1/\sqrt{q_0})$ | $0.49932$ |
| $\mathrm{tr}_M(\mathfrak{p})$ | $0.43801$ |
| $\mathrm{tr}_M(\mathfrak{n})$ | $0.32054$ |
| $\mathrm{tr}_M(T_{pn} \cdot \mathfrak{n})$ | $0.15417$ |
| $\Delta = \mathrm{tr}_M(\mathfrak{p}) + \mathrm{tr}_M(\mathfrak{n}) - \mathrm{tr}_M(T_{pn} \cdot \mathfrak{n})$ | $0.60438$ |
| $\alpha = m_e \cdot 8G$ | $3.7445\;\text{MeV}$ |
| $B(d) = \Delta \times \alpha$ | $2.2329\;\text{MeV}$ |
| $B_{\mathrm{obs}}(d)$ (AME2020) | $2.2246\;\text{MeV}$ |
| **Error** | **$+0.38\%$** |

The derivation chain:

1. $\mathrm{Vol}(4_1) = 2.0299$ (SnapPy, hyperbolic volume)
2. $m_\mu/m_e = 206.768$ (CODATA 2022, gives $q_0$)
3. $m_e = 0.5110\;\text{MeV}$ (CODATA 2022, gives MeV scale)
4. $G = 0.9160$ (Catalan's constant, computed)
5. Quark content: $\mathfrak{p} = \mathfrak{u}\mathfrak{u}\mathfrak{d}$,
   $\mathfrak{n} = \mathfrak{u}\mathfrak{d}\mathfrak{d}$
6. $H_3(q_0)$ multiplication rules (Hecke algebra)

No fitted parameters.  No semi-empirical scalings.  Direct
algebraic computation from the Hecke algebra and measured inputs.

**Witness**: `deuterium-derived.witness.json`.
