*Let $\Delta = \mathrm{NF}(n) - \mathrm{NF}(p)$ be the single-wrap normal-form difference of the neutron and proton typed-crossing elements in $H_3(q)$, and write $h = q - q^{-1}$. Let $\varepsilon$ denote the coordinate-sum functional $\sigma \mapsto 1$ (see the scope section below — it is *not* a counit) and $\mathfrak{E}_0 = m_e/(q(q-1))$ the per-Hecke-step energy scale. Then:*
$$
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$

## Counit versus Markov trace

Two canonical functionals act on this difference:
$$
  \varepsilon(\Delta) = \frac{h^2}{2} - h,
  \qquad
  \mathrm{tr}_M(\Delta) = \frac{h^2}{2} - h\,z.
$$

On $\Delta$ the coordinate sum agrees with the Markov trace at the trivial loop value $z = 1$, and the trivial-loop value is never attained on the aether, so the two are genuinely distinct functionals there.

**That agreement is a property of $\Delta$ rather than an identity.** The Markov trace at $z = 1$ weights the standard basis as $[1,1,1,1,1,h+1]$, while the coordinate sum weights it as $[1,1,1,1,1,1]$, so
$$
  \mathrm{tr}_M\big|_{z=1} - \varepsilon \;=\; h \cdot (\text{the } e^- \text{ coordinate}).
$$
The two therefore coincide exactly on elements whose $e^-$ coordinate vanishes, which both nucleon models happen to satisfy. The identity must not be quoted in general.

## Scope: $\varepsilon$ is not a counit, and is inadmissible under convention D

**This statement is a construction in a non-canonical frame.** Three separate points, each measured; none of them moves a number above.

**It is not a counit.** A unital algebra map into a commutative ring is automatically cyclic, hence a class function. The functional here is the coordinate sum $\sigma \mapsto 1$, which is not multiplicative: pushing the Hecke relation $\sigma^2 = h\sigma + 1$ through such a map forces $h = 0$. The multiplicative functional the name suggests is the augmentation $\sigma \mapsto q$, which is a different map and gives a different value on the same vector.

**It does not descend to the algebra the canonical convention places the theory in.** Under convention D the trace ideal is the Temperley–Lieb radical, and the GNS space is $H_\infty(q)/\mathcal{N} \cong \mathrm{TL}_\infty(q)$ rather than $H_\infty(q)$. A functional descends to a quotient exactly when it annihilates the ideal. The augmentation annihilates $J_{(1^3)}$; the coordinate sum does not. Since $\Delta$ has a non-zero $(1^3)$ component, $\varepsilon$ assigns different values to two representatives of the same class.

**The admissible set is closed at two, and both miss.** The descent condition $y_{(1^3)}(z) = 0$ is quadratic with roots $z = q$ and $z = z_D = q^3/(q^2+1)$; at $z = q$ the Markov trace *is* the augmentation, so the two roots give two functionals rather than three. Evaluated on the same vector against the measured $Q$-value, the augmentation gives $+12.470\%$ and the Markov trace at $z_D$ gives $-43.157\%$, while the coordinate sum used here gives $+0.168\%$ at $z = 1$ — a loop value that is neither root. **The functional that reproduces the measurement is the one the canonical convention forbids.** The two admissible values bracket the target, so some convex combination reproduces it exactly; that is one parameter against one anchor, and any such weight must be derived from the representation rather than fitted.

None of this shows the $Q$-value wrong. It records which functional the construction evaluates, and that the canonical convention excludes it.

## Factorization of the energy scale

The per-Hecke-step energy factors through the information speed $c_q^2 = 1/(q-1)^2$ and the action-per-tick $\hbar_q^{E} = (q-1)/q$:
$$
  \mathfrak{E}_0
  =
  \frac{m_e}{q(q-1)}.
$$
The quantity $\hbar_q^{E}$ is the energy-scale action quantum, distinct from the Hecke parameter $h$.
