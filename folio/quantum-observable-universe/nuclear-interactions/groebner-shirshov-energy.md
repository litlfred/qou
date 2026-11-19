The Gröbner--Shirshov basis theory establishes that the energy of a fixed nuclear braid word is path-independent.

**Theorem.**
For $q > 1$, $h = q - q^{-1} > 0$, and $\alpha > 0$, define the linear word-length energy and exponential fugacity functionals on $H_A(q)$ by

$$
  E_1(\xi) = \sum_{w \in B} |c_w(q)| \cdot \ell(w),
  \qquad
  \Phi_\alpha(\xi) = \sum_{w \in B} |c_w(q)| \cdot \alpha^{\ell(w)}.
$$

Then:

1. **Only Hecke reductions change energy.** The Yang--Baxter relation, the Bokut--Shiao braid family, and far commutativity preserve coefficients and word lengths; the Hecke quadratic relation is the unique energy-changing rule.
2. **Energy is path-independent.** Along any reduction path $\xi_0 \to \cdots \to \xi_m$, the step changes telescope to $E_1(\xi_m) - E_1(\xi_0)$ and $\Phi_\alpha(\xi_m) - \Phi_\alpha(\xi_0)$, which depend only on $\xi_0$ by confluence ([Hecke normal form](#def:hecke-normal-form)).
3. **Linear step change and length sign-flip bound.** On an isolated monomial $c\,w$ with $w = u\,\sigma_i^2\,v$ of length $\ell \geq 2$, replacing $\sigma_i^2$ by $h\,\sigma_i + 1$ changes $E_1$ by

$$
  \Delta E_1 = |c|\,\bigl(|h|\,(\ell - 1) - 2\bigr),
$$

which is negative for $\ell < 1 + 2/|h| \approx 10.57$ ($\Delta E_1 = -0.1185\,|c|$ at $\ell = 10$ for $q = q_0$) and positive for $\ell \geq 11$ ($\Delta E_1 = +0.0906\,|c|$ at $\ell = 11$).

4. **Critical exponential Lyapunov law ($\alpha_{\mathrm{crit}} = q$).** Under the same Hecke step at word length $\ell \geq 2$,

$$
  \Delta\Phi_\alpha
  = |c|\,\bigl(h\,\alpha^{\ell - 1} + \alpha^{\ell - 2} - \alpha^\ell\bigr)
  = -|c|\,\alpha^{\ell - 2}\,(\alpha - q)\,(\alpha + q^{-1}),
$$

so at every $\ell \geq 2$: $\Delta\Phi_\alpha < 0$ for $\alpha > q$ (strict Lyapunov descent), $\Delta\Phi_q = 0$ at the critical fugacity $\alpha_{\mathrm{crit}} = q = q_0$, and $\Delta\Phi_\alpha > 0$ for $0 < \alpha < q$.

Whereas Gröbner--Shirshov reduction quotients only by the skein ideal $I_{\mathrm{Hecke}} = \langle \sigma_i^2 - h\,\sigma_i - 1 \rangle$, Temperley--Lieb loop erasure on $E_i = q\,\mathbf{1} - \sigma_i$ carries trace weight $q - z_D = q/(q^2 + 1) = \delta^{-1} \neq z_D$ ($\delta\,z_D = q^2 > 1$) and kills all $\geq 3$-row diagrams. On $H_3(q)$, the resulting radical $\mathcal{N}_D = \langle y_{(1^3)} \rangle$ is the antisymmetric baryon and nuclear confinement sector completed by the Geer--Patureau-Mirand--Turaev (GPMT) modified trace with weight $|d_D(S^{(1^3)})| = \bigl([2]_q\,[3]_q\bigr)^{-1} > 0$ and eigenvalue $q^{-3} > 0$.
