## Proof

The chain has three steps.

**Step 1 (Mass integrand = identity).**
By definition ([mass](#def:mass-identity)), $\mathfrak{m}(\varrho) = \lVert \int_A \circ \Psi \circ \varrho \rVert$ with $\Psi = (\int_A \otimes \mathrm{id}) \circ \Delta$. The unit law and the Frobenius relation give $\Psi = L_u$, left multiplication by $u = \Psi \circ \eta$. When the Frobenius form is the counit, $\int_A = \varepsilon$, the counit law $(\varepsilon \otimes \mathrm{id}) \circ \Delta = \mathrm{id}_A$ gives $\Psi = \mathrm{id}_A$, hence

$$
  \mathfrak{m}(\varrho) = \Bigl\lVert \textstyle\int_A \varrho \Bigr\rVert .
$$

The reason is the counit law. It is not the Nakayama automorphism or $S^2 = \mathrm{id}$: $\Psi$ is a left multiplication, and it is the identity exactly when $u = \eta$.

**Step 2 (Frobenius form = Markov trace = quantum trace of the multiplicative integral).**
Take $\int_A$ to be the normalised Jones–Markov trace. It is realised on $V^{\otimes n}$, $V = R^2$, through Jimbo's R-matrix $\check R$. A braid word $\ell_1 \cdots \ell_k$ has transports $T(\sigma_a) = \check R_a$ and $T(\sigma_a^{-1}) = \check R_a - (q - q^{-1})$, acting at strands $a, a+1$. Its multiplicative integral is the ordered product $\mathrm{Hol}(\beta) = T(\ell_1) \cdots T(\ell_k)$, and

$$
  \textstyle\int_A \rho(\beta)
  \;=\; (1 + q^2)^{-n} \, \mathrm{Tr}\bigl( K^{\otimes n} \cdot \mathrm{Hol}(\beta) \bigr),
  \qquad K = \mathrm{diag}(1, q^2).
$$

This functional is cyclic. It satisfies the positive and negative Markov moves with scalars $q^3/(q^2+1)$ (convention D) and $q^{-1}/(q^2+1)$, and $\int_A 1 = 1$. The weight $K$ is not chosen: the Markov move exists only for $K = \mathrm{diag}(1, q^2)$ up to scale. This is Turaev's enhanced Yang–Baxter operator $(\check R, K, \alpha = q^2, \beta = q)$.

The categorical trace of $A$ acting on itself is not this functional. It is the regular trace, which fails the Markov property: on $H_3(q)$ the normalised regular trace gives $\mathrm{tr}(\sigma_1 \sigma_2) = h^2/6$ against $\mathrm{tr}(\sigma_1)^2 = h^2/4$, with $h = q - q^{-1}$.

**Step 3 (Mass = trace of cycle).**
Combining Steps 1 and 2:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \Bigl\lVert \textstyle\int_A \bigl(
    \underbrace{(\int_A \otimes \mathrm{id}) \circ \Delta}_{= \,\mathrm{id}_A}
    \circ\, \varrho \bigr) \Bigr\rVert
  \;=\; \Bigl|\!\int_A\! \rho(\beta_\mathcal{K})\Bigr|
  \;=\; (1 + q^2)^{-n} \, \bigl| \mathrm{Tr}\bigl( K^{\otimes n} \cdot \mathrm{Hol}(\beta_\mathcal{K}) \bigr) \bigr| .
$$

**Scope.** Steps 1 and 2 are proved sorry-free over a generic commutative ring: Step 1 in `QOU.Torsion.MassTraceIdentity` (`frobeniusForm_massIntegrand_of_frobeniusForm_eq_counit`), Step 2 in `QOU.Torsion.MassTraceMarkov` (`braidTrace_wordBraid`), on top of the Markov-trace arc `QOU.IwahoriHecke.{QTraceCyclic, MarkovPeel, NegativePeel, MarkovNormalized}`. Three points are not proved here.

1. *Which algebra carries the Frobenius structure.* Under convention D the Ocneanu weights vanish on every three-row shape (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`). So the pairing $(x, y) \mapsto \int_A xy$ is degenerate on $H_n(q)$ for $n \ge 3$, and $(H_n(q), \int_A)$ is not a Frobenius algebra. The Frobenius object is the quotient by the radical of this pairing, $H_n(q)/\mathrm{rad}$. On it the form is positive definite for $q > 1$, because the surviving two-row weights $y_{(n-k,k)} = [n-2k+1]_q/[2]_q^{\,n}$ are strictly positive (`QOU.QBeta.TemperleyLiebTower`, §T4). That this quotient is the Temperley–Lieb algebra $\mathrm{TL}_n(q)$ is not proved here.
2. *That the Frobenius form is the counit.* This is the hypothesis of Step 1. It holds when $\Delta$ is the coproduct induced by $\int_A$, and has to be checked for the Frobenius–Hopf data actually used.
3. *The continuous holonomy.* $\mathrm{Hol}$ is a finite ordered product. That the holonomy of the Knizhnik–Zamolodchikov connection along a braid equals such a product of R-matrices is the Drinfeld–Kohno theorem \cite{kohno1987, drinfeld1985}, cited, not proved. That theorem places $q$ on the unit circle for a real coupling, so the real substrate value $q_0 > 1$ needs a complex coupling.

## Explicit values

Evaluating at $q_0 \approx 1.110$ with Markov parameter $z = q^3/(q^2+1) \approx 0.613$ (**convention D**, SU(2)/Temperley–Lieb — see the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md)) and $h = q - q^{-1} \approx 0.209$:

| Particle | Braid $\beta_\mathcal{K}$ | $\int_A \rho(\beta_\mathcal{K})$ | Symbolic |
|:---:|:---:|:---:|:---:|
| $\gamma$ (photon) | $\mathbf{1}$ | $1$ | $1$ |
| $\sigma_0$ (pol.) | $\sigma_0$ | $z \approx 0.613$ | $z$ |
| $L_+$ (gluon) | $\sigma_0\sigma_1$ | $z^2 \approx 0.375$ | $z^2$ |
| $e^-$ (electron) | $\sigma_0\sigma_1\sigma_0$ | $\approx 0.691$ | $hz^2 + z$ |
| $4_1$ (figure-eight) | $(\sigma_0\sigma_1^{-1})^2$ | $\approx 0.280$ | $\dfrac{q^8-q^6+q^4-q^2+1}{q^6+2q^4+q^2}$ |

> **Convention change, 2026-08-09 (owner ruling; bean `qou-wgta` item 19).**
> This table published **convention C** ($z = 1/(q^{1/2}+q^{-1/2}) \approx 0.499$),
> which has been excised. Measured at the proton pin $q_0 =
> 1.1099785827513808\ldots$, 12 significant figures:
>
> <!-- literal-source: C column is preserved history, no producer (qou-ft3p) -->
> | quantity | convention C (was) | convention D (now) |
> |:---|---:|---:|
> | $z$ | $0.499320334184$ | $0.612688037146$ |
> | $z^2$ | $0.249320796129$ | $0.375386630862$ |
> | $hz^2+z$ | $0.551443414318$ | $0.691166478358$ |
> | $4_1$ | $0.182304485938$ | $0.280195642273$ |
>
> The **convention-C column has no producer by design**: C was excised by the
> owner ruling of 2026-08-09, so nothing in the repo computes it and no
> witness can carry it. The **convention-D column is witnessed** by
> `computations/markov/markov-trace-canonical.witness.json` (6 assertions at
> $10^{-40}$) — the script this note already names below as the reproducer,
> which until now emitted no witness at all (bean `qou-ft3p`).
>
> $h$ is convention-independent. The $4_1$ closed form is new here: it was
> "(see witness)", and the witness held the C value. Reproduce with
> `python3 computations/markov/markov_trace_canonical.py`, whose prop-table
> check now gates at $10^{-40}$ rather than $10^{-9}$.

These constitute **dimensionless ratios** relative to the photon ($\mathfrak{m}_{q,\gamma} = 1$). Physical masses in MeV require a calibration constant $E_0$, determined by anchoring to one experimental value (e.g., the free neutron $\beta$-decay $Q$-value).

## Role in the unified mass formula

This proposition supplies the $k = 0$ stratum of the curvature-rank decomposition ([unified mass formula](#prop:unified-curvature-rank-mass-formula)): $\mathfrak{m}^{(0)}_{q,\mathcal{K}}(1) = |\!\int_A\! \rho(\beta_\mathcal{K})|$ is the descended Frobenius integral, equal to $E_\infty^{0,*}$ of the GB spectral sequence.

The integral $\int_A \rho(\beta_\mathcal{K})$ is **vortex-specific**, distinguishing $\varrho_{\mathfrak{p}}$ from $\varrho_{\mathfrak{n}}$ and capturing fine isotope variations. The vortex-independent constant offset is the Frobenius co-Casimir $m_e \cdot \tau(C_{\dim_q})$ ([Frobenius universal](#thm:frobenius-codim-universal)). The full mass is:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{k \geq 0} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)
       \;+\; m_e \cdot \tau(C_{\dim_q}),
$$

with this proposition governing the $k = 0$ component.
