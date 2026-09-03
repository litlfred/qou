*Proof.*
The proton possesses quark content $\mathfrak{u}\mathfrak{u}\mathfrak{d}$;
the neutron possesses $\mathfrak{u}\mathfrak{d}\mathfrak{d}$. At the quark
level, the crossing types evaluate as:

- $\mathfrak{u}\mathfrak{u}$: same-type $\to \sigma$ (eigenvalue $q$).
- $\mathfrak{d}\mathfrak{d}$: same-type $\to \sigma^{-1}$ (eigenvalue $q^{-1}$).
- $\mathfrak{u}\mathfrak{d}$: mixed $\to \tfrac{1}{2}(\sigma + \sigma^{-1})$.

Replacing one $\mathfrak{u}\mathfrak{u}$ crossing with one
$\mathfrak{d}\mathfrak{d}$ crossing shifts the quantum dilogarithm by
$\Delta\Phi = \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d}) - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})$.

The ground-state configurations are $\mathfrak{u}\mathfrak{u}\mathfrak{d}$
(proton, $\Phi_{\mathfrak{p}} = -0.8785$) and
$\mathfrak{u}\mathfrak{d}\mathfrak{d}$ (neutron, $\Phi_{\mathfrak{n}} = -1.2261$).
This yields $|\Delta\Phi| = 0.3476$.

At the quark level, a more negative $\Phi$ implies greater confinement energy
(rather than reduced binding, as occurs at the nuclear level). The
$\mathfrak{d}\mathfrak{d}$ crossing ($\sigma^{-1}$) generates more
confinement than the $\mathfrak{u}\mathfrak{u}$ crossing ($\sigma$). This
excess makes the neutron heavier.

The scale $\alpha = m_e \times 8G$ governing nuclear binding also dictates
the quark-level confinement splitting:

$$
  \Delta m = 3.7445 \times 0.3476 \approx 1.302 \;\mathrm{MeV}.
$$

This prediction compares to the CODATA value $\Delta m = 1.2934$ MeV,
an error of $0.63\%$. $\square$

> **Provenance and scope (2026-08-25).** This proof cites no live witness
> and its stated agreement is not currently reproducible.
>
> The witness named here until now,
> `atom-mass-complete-wedderburn.witness.json`, is absent from
> `computations/`. It was **not**, however, never produced: it was added on
> 2026-04-10 in commit `1359fe23ac` under `folio-assistant/computations/` and
> left the tree with the platform code in the miga migration
> ([recovery and analysis](https://github.com/litlfred/qou/blob/main/docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md)).
> It is nonetheless the **wrong artifact** for this block: it is an
> *atomic*-mass witness of 20 atom rows, cited by a *quark*-level
> computation, and the recovered file contains no quark $\Phi$ values at
> all. So this block has no usable witness either way.
>
> Re-deriving the two $\Phi$ values from the crossing rules stated above
> ([`computations/pn_splitting_proof_provenance_probe.py`](https://github.com/litlfred/qou/blob/main/computations/pn_splitting_proof_provenance_probe.py))
> pins the reading and then fails to confirm the result. Convention C with
> the suffix-inclusive $\Phi_1$ reproduces
> $\Phi_{\mathfrak{p}} = -0.8785233$ against the $-0.8785$ quoted above —
> exact at the quoted precision, and the only one of eight readings that
> lands. The same reading gives $\Phi_{\mathfrak{n}} = -1.2677888$, not the
> $-1.2261$ quoted. Because the reading is pinned by the proton, this is not
> reading ambiguity.
>
> Consequently:
>
> | source | $\lvert\Delta\Phi\rvert$ | $\Delta m$ (MeV) | vs CODATA |
> |:---|:---|:---|:---|
> | as stated above | $0.3476$ | $1.3016$ | $+0.63\%$ |
> | re-derived, convention C | $0.3892655$ | $1.4576$ | $+12.7\%$ |
> | re-derived, convention D | $0.3354835$ | $1.2562$ | $-2.87\%$ |
>
> The derivation is also **convention C** throughout, which the owner ruling
> of 2026-08-15 excised in favour of convention D
> ($z = q^3/(q^2 + 1)$); under D the block's own construction gives
> $-2.87\%$, not $+0.63\%$.
>
> Scope (a): eight readings were tried, which is not an exhaustive
> exclusion, and no replacement value is proposed here. What is established
> is that the $+0.63\%$ figure **cannot currently be checked** and should
> not be cited as a confirmed prediction.
