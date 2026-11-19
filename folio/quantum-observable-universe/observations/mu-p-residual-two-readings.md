The two admissible pins of the substrate modulus $q_0$ — the lepton relation and the proton ratio — do not meet. The discrepancy between them is small enough to be read as a prediction and large enough to be read as a gap, and the framework's own evidence does not say which. [The epistemic-status remark](#rem:epistemic-status-of-calibrations) records which calibration the computed values use and why; the discussion below records what the discrepancy is, what has been proved about any term that would close it, and which observations would settle its reading. Throughout, $\hbar_q = 1 - q^{-1}$ is the categorical Planck constant, evaluated at $q_0$ unless another argument is written; $m_\mu/m_e$ and $m_p/m_e$ are the CODATA-2022 mass ratios; and $\mathrm{Vol}(4_1) \approx {{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 5 }}$ is the hyperbolic volume of the figure-eight knot, a mathematical constant carrying no experimental input.

## The datum

[The calibration discipline](#def:three-calibration-discipline) pins $q_0$ through the lepton relation

$$
  \frac{m_\mu}{m_e} = \frac{\mathrm{Vol}(4_1)}{\hbar_q^2},
$$

and the Physical-Observations layer pins it instead through the proton relation $m_p/m_e = 2\,\mathrm{Vol}(4_1)\,F_{\mathrm{Bor}}(q)/\hbar_q^2 - 12$, in which $F_{\mathrm{Bor}}(q) = \lvert \mathrm{tr}_M(\beta_{\mathrm{Bor}}) \rvert\,[3]_q!/q^3$ dresses the same volume by the Markov trace $\mathrm{tr}_M$ of the Borromean braid $\beta_{\mathrm{Bor}} = (\sigma_1\sigma_2^{-1})^3$ in the three-strand Hecke algebra $H_3(q)$, with $[3]_q!$ the quantum factorial. The two solutions differ by $\approx 11.6$ ppb, the proton pin lying below the lepton pin. The lepton relation has logarithmic sensitivity $\mathrm{d}\ln(m_\mu/m_e)/\mathrm{d}\ln q = -2/(q\,\hbar_q) \approx -18$ at $q_0$, so that separation is the whole of the muon-side residual: evaluated at the proton-calibrated modulus, the lepton relation exceeds the CODATA-2022 value $m_\mu/m_e \approx {{ qou.computations.q-pinning-50-digit.calibration_inputs.m_mu_over_e_str | precision: 10 }}$ by $\approx 211$ ppb. Let $t$ denote the multiplicative correction the lepton relation would need, $(\mathrm{Vol}(4_1)/\hbar_q^2)(1 - t) = m_\mu/m_e$, so that to first order $t$ is the relative excess:

$$
  t \approx 2.1 \times 10^{-7}.
$$

The CODATA-2022 ratio carries a relative one-standard-deviation uncertainty $\sigma_{\mathrm{exp}} \approx 2.2 \times 10^{-8}$, so $t \approx 9.5\,\sigma_{\mathrm{exp}}$ and $\sigma_{\mathrm{exp}}/t \approx 10\%$. The reverse assignment — pinning on the lepton relation and predicting the proton ratio — leaves $m_p/m_e$ low by $\approx 2.4 \times 10^{-7}$; since that ratio is known to $\approx 1.7 \times 10^{-11}$, the miss there is $\approx 1.4 \times 10^{4}$ of its own standard deviations. The proton pin is the working one for the arithmetic reason [the epistemic-status remark](#rem:epistemic-status-of-calibrations) gives: a residual of fixed size costs least where the experimental resolution is coarsest.

## Independence from the trace convention

The Markov trace on $H_n(q)$ depends on a Markov parameter $z$, the trace of a single generator $\sigma_i$; the canonical choice is $z = q^3/(q^2+1)$, and an alternative convention sets $z = \sqrt{q}/(q+1)$. The residual is not an artefact of this choice, for two reasons that need no evaluation at the pin. The lepton relation contains no trace at all: $\mathrm{Vol}(4_1)$ is a hyperbolic volume and $\hbar_q$ is a rational function of $q$, so no Markov parameter reaches its arithmetic. The proton relation contains one, but the closed form it uses for $\lvert \mathrm{tr}_M(\beta_{\mathrm{Bor}}) \rvert$ — a rational function of $h = q - q^{-1}$ with integer exponents — is what the trace becomes under the canonical parameter and is not what it becomes under the alternative. The trace of any element of $H_3(q)$ is a polynomial of degree at most two in $z$ with coefficients in $\mathbb{Z}[q^{\pm 1}]$, because the Hecke relation and the Markov rule $\mathrm{tr}_M(x\,\sigma_2\,y) = z\,\mathrm{tr}_M(xy)$ for $x, y$ in the two-strand subalgebra $H_2(q)$ produce nothing else. Substituting $z = q^3/(q^2+1)$ therefore yields a rational function of $q$ with integer exponents, and its identity with the closed form holds for all $q$; substituting $z = \sqrt{q}/(q+1)$ leaves a remainder carrying half-integer powers of $q$, which no closed form in $h$ can absorb. Both pins already sit in the canonical convention, and a change of convention has nothing to act on.

## Constraints on a correction

Suppose the lepton relation is the leading term of a series in $\hbar_q$ whose first correction supplies the factor $1 - t$. Three constraints on that correction are established.

**Order window.** If the correction is a single monomial $\lvert c \rvert\,\hbar_q^{k}$ with a coefficient of small height, $\lvert c \rvert \in [1/5, 5]$, then $k \in \{6, 7\}$ (holding for every $\hbar_q \in [0.098, 0.1]$ and every $t$ between $1.8 \times 10^{-7}$ and $2.4 \times 10^{-7}$). At $q_0$, where $\hbar_q \approx 0.0991$, the two admissible coefficients are $c_6 = t/\hbar_q^6 \approx 0.22$ and $c_7 = t/\hbar_q^7 \approx 2.25$; orders $k \le 5$ overshoot $t$ by at least a factor of $7.5$ and orders $k \ge 8$ undershoot it by at least a factor of $3.6$. In particular the residual is not a one- or two-loop term of the asymptotic expansion of the figure-eight Kashaev invariant whose leading term is $\mathrm{Vol}(4_1)$: when the expansion parameter is identified with $\hbar_q$, those terms enter at $k = 1$ and $k = 2$ with coefficients of order one and overshoot $t$ by factors of $\approx 5 \times 10^{5}$ and $\approx 5 \times 10^{4}$.

**Bar parity.** The muon carrier $4_1$ is amphichiral and its invariants are fixed by the bar involution $q \mapsto q^{-1}$ ([the self-dual real-volume proposition](#prop:self-dual-higgs-real-volume)); the framework accordingly requires the correction to be bar-even. This requirement is an argument from the carrier's symmetry, not a theorem, and every exclusion drawn from it is conditional on it. Under the bar involution the substrate constant is not fixed: $\hbar_{q^{-1}} = -q\,\hbar_q$. A monomial $\hbar_q^{k} q^{\ell}$ is therefore carried to $(-1)^{k} q^{k-\ell}\,\hbar_q^{k}$, which coincides with $\hbar_q^{k} q^{\ell}$ for all $q$ exactly when $k$ is even and $\ell = k/2$ — and, since $n \mapsto q^{n}$ is injective for $q > 1$, for no other exponent pair. So the bar-even monomials are exactly the powers of

$$
  w := q\,\hbar_q^{2} = q + q^{-1} - 2,
$$

and the bar-even dressing of $\hbar_q^{6}$ is $\hbar_q^{6} q^{3} = w^{3}$. Measured at $q_0$, the residual over $w^{3}$ is $t/w^{3} \approx 0.163 < 1/5$ and over $w^{4}$ is $t/w^{4} \approx 15 > 5$: no single bar-even monomial with a coefficient of small height carries it, at any calibration point in the window $[1.1099, 1.11]$ and for every order. Together with the order window this says that the correction, if there is one, is not a monomial of small height in either $\hbar_q$ or $w$; it is a sum, or it carries a coefficient of genuinely non-unit height.

**Entropy.** The datum $t$ is known to $\sigma_{\mathrm{exp}}/t \approx 10\%$ — about one significant digit. The order-six coefficient window that experiment cannot distinguish from the central value is $\approx 21\%$ wide, and a dozen constants of small height — rationals, quantum integers at $q_0$, and simple functions of $\mathrm{Vol}(4_1)$ and $\pi$ — land inside it. Matching a closed form to $t$ therefore identifies nothing; only a coefficient fixed before the comparison can.

**Structural origin.** What is known about where such a correction would come from is this. The lepton relation evaluates a scalar knot invariant, the volume of $4_1$. The framework's working assignment places the muon in the five-dimensional icosahedral representation, carried by the $(3,2)$ block of the five-strand Hecke algebra $H_5(q)$, and the electron in the $(3,1,1)$ block, which splits under the icosahedral group into the two three-dimensional representations; the natural correction to the scalar relation is then operator-valued — a Wedderburn-trace factor attached to the muon's block. The assignment is a working hypothesis of the generation tower; the factor has not been constructed. The most direct realisation, a shift of the projector weight of the Markov trace between the two blocks, is excluded on magnitude: the shift it produces is of order one, more than six orders of magnitude larger than $t$, and it does not reproduce the generation ratio either.

## The two readings

The datum admits two readings.

**(R1) The bare relation is exact.** At the proton-pinned modulus the lepton relation holds as written, and the framework predicts a muon–electron mass ratio larger than the CODATA-2022 value by $\approx 2.1 \times 10^{-7}$ in relative terms, with a definite sign. This is a falsifiable prediction, decided by any determination of $m_\mu/m_e$ at the few-ppb level.

**(R2) The bare relation is a leading term.** The lepton relation is the first term of a series whose first correction is bar-even and is bounded, not determined, by the order window and the parity rule above; the framework's candidate for its coefficient is the operator-valued generation branching, which it has not constructed. The residual then measures an unclosed term: it is a derivation gap, not a prediction.

Nothing computed inside the framework separates R1 from R2, because the object that would — the a-priori coefficient — is what has not been constructed. On outside priors R2 is the conservative reading: the CODATA ratio rests on muonium spectroscopy and the muon magnetic-moment ratio, and an error of nine and a half standard deviations there is far less likely than an unclosed term here. R1 is what the bare relation asserts when it is taken as written.

## Discriminating observations

Three observations separate the readings, and one class of computation does not.

1. A coefficient derived before the comparison — bar-even and consistent with the constraints above — that reproduces $t$ establishes R2 and closes the gap. A derived coefficient that fails to reproduce $t$ falsifies the series it belongs to, which would then disagree with experiment at its first correction.
2. A determination of $m_\mu/m_e$ higher than the present value by $\approx 2 \times 10^{-7}$ — or, far less plausibly, of $m_p/m_e$ lower by $\approx 2.4 \times 10^{-7}$ — brings the two pins together and establishes R1.
3. Confirmation of the present central value of $m_\mu/m_e$ at a relative uncertainty $\lesssim 2 \times 10^{-9}$ excludes R1 outright and forces R2, or a revision of the second calibration relation itself.

What does not decide is any fit that drives the residual below the two-pin separation — a coefficient chosen against the datum, or an integer tower tuned to the CODATA value. Such a fit models the discrepancy as signal, and the entropy bound says it carries no evidence: a dozen constants of small height fit equally well.

## Scoring

The per-observable accuracy ledger scores $m_\mu$ as the proton-anchored prediction it is under both readings: the mass $m_\mu$ misses its target of one hundredth of its experimental uncertainty by a factor $\approx 970$. Nothing here changes that score. Under R1 the miss is the prediction; under R2 it is the size of the unclosed term. In neither reading is it compute imprecision: the separation of the pins exceeds the inversion floor of the hundred-digit recomputation of both pins by more than three orders of magnitude, and the internal agreement between independent evaluations of the same quantities is at the part-per-quadrillion level.
