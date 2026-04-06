The Gröbner--Shirshov normal form coefficients are dimensionless Laurent
polynomials in $q$.  To connect them to observed energies we need
an **energy scale** $\mathbf{E}_0$ (in MeV) such that

$$
  \Delta(\mathrm{net}) \times \mathbf{E}_0
  \;=\;
  Q_{\beta}
  \;=\;
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} - \mathfrak{m}_{e}
  \;\approx\; 0.7823\;\text{MeV}.
$$

## Derivation

From the witness (`free-neutron-decay.witness.json`):

- $\mathrm{net}(\mathfrak{n}) = +1.5557$, $\mathrm{net}(\mathfrak{p}) = +1.3782$
- $\Delta(\mathrm{net}) = +0.17755$

From CODATA 2022:

- $\mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} = 1.29333\;\text{MeV}$
- $\mathfrak{m}_{e} = 0.51100\;\text{MeV}$
- $Q_{\beta} = 0.78233\;\text{MeV}$

Therefore:

$$
  \mathbf{E}_0
  \;=\;
  \frac{Q_{\beta}}{\Delta(\mathrm{net})}
  \;=\;
  \frac{0.78233}{0.17755}
  \;\approx\; 4.406\;\text{MeV}
  \;\approx\; 8.623 \times \mathfrak{m}_{e}.
$$

## Full energy budget

Each of the six NF terms contributes $\Delta_i \times \mathbf{E}_0$
to the total decay energy.  The budget is:

| Term | Basis | $\Delta_i$ | $\Delta_i \times \mathbf{E}_0$ (MeV) |
|:---:|:---:|---:|---:|
| $\nu$ | $\mathbf{1}$ | $-0.0757$ | $-0.333$ |
| $H^0$ | $\sigma_0$ | $+0.0091$ | $+0.040$ |
| $H^1$ | $\sigma_1$ | $+0.2933$ | $+1.292$ |
| $L_+$ | $\sigma_0\sigma_1$ | $-0.0378$ | $-0.166$ |
| $L_-$ | $\sigma_1\sigma_0$ | $+0.0019$ | $+0.009$ |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | $-0.0134$ | $-0.059$ |
|  |  | **Sum** | **$+0.782$ MeV** |

## The $\sigma_1$ dominance

The single largest contributor is $\Delta(H^1) = +0.2933$, which
gives $+1.292\;\text{MeV}$ — nearly equal to the full
neutron–proton mass difference $\mathfrak{m}_{\mathfrak{n}} -
\mathfrak{m}_{\mathfrak{p}} = 1.293\;\text{MeV}$.

The $\sigma_1$ generator acts within the color tube fiber
([observability](#rem:nucleon-nf-observability)).  Its
contribution of $+1.292\;\text{MeV}$ is **more** than the decay
energy $Q_\beta = 0.782\;\text{MeV}$.  The excess is absorbed by
the negative terms:

- **$\nu$ debt**: $-0.333\;\text{MeV}$ (42.6% of $Q_\beta$)
- **$L_+$ recoil**: $-0.166\;\text{MeV}$ (21.3% of $Q_\beta$)
- **$e^-$ debt**: $-0.059\;\text{MeV}$ (7.5% of $Q_\beta$)

The neutrino channel carries the largest negative correction.

## Physical interpretation

Beta decay pays down the neutron's leptonic debt:

$$
  \underbrace{+1.292}_{\sigma_1\text{ (color tube)}}
  \;\underbrace{-0.333}_{\nu\text{ debt}}
  \;\underbrace{-0.166}_{L_+\text{ recoil}}
  \;\underbrace{-0.059}_{e^-\text{ debt}}
  \;\underbrace{+0.049}_{\text{other}}
  \;=\;
  +0.782\;\text{MeV}.
$$

The process $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$
releases $Q_\beta = 0.782\;\text{MeV}$ because:

1. The neutron's $\sigma_1$ amplitude (color tube confinement
   energy) exceeds the proton's by $+1.292\;\text{MeV}$.

2. The neutron must pay larger $\nu$ and $e^-$ debts than the
   proton ($-0.333$ and $-0.059\;\text{MeV}$ respectively).

3. The Hopf link $L_+$ absorbs $-0.166\;\text{MeV}$ — the cost
   of restructuring the bound-state topology during the
   $d \to u$ quark transition.

4. The net surplus after all debts is $Q_\beta$.

Witness: `beta-decay-energy-scale.witness.json`.
