One explicitly constructs the [vacuum state](#prop:vacuum-state) $\varphi$ for the [direct limit algebra](#def:direct-limit-algebra) of $\mathrm{SU}(2)$. One replaces the abstract direct-limit existence argument with a closed-form formula.

**Step 1: the Frobenius trace at finite level.** At level $n$ of the brane tower, the endomorphism algebra $\mathrm{End}(A_n)$ carries the Frobenius trace:
$$
  \mathrm{tr}_n(\alpha)
  = (\varepsilon \circ \alpha \circ \eta)(\mathbf{1}),
$$
where $\eta \colon \mathbb{C} \to A_n$ is the unit and $\varepsilon \colon A_n \to \mathbb{C}$ is the counit. For $A_n = \mathcal{O}(\mathrm{SU}(2))$ with its Peter–Weyl decomposition, this evaluates to:
$$
  \mathrm{tr}_n(f)
  = \sum_{j=0}^{n} (2j+1) \int_{\mathrm{SU}(2)}
    f(g)\,\overline{\chi_j(g)}\,dg
  \cdot \delta_{j,0}
  = \int_{\mathrm{SU}(2)} f(g)\,dg.
$$
The map $\mathrm{tr}_n$ is the Haar integral restricted to representations of spin $\leq n$.

**Step 2: the $q$-deformed Haar integral.** In the quantum group $\mathcal{O}_q(\mathrm{SU}(2))$, the Haar state $\varphi$ is the unique $\mathrm{SU}_q(2)$-invariant linear functional normalised by $\varphi(1) = 1$. Its action on the matrix coefficients $t^j_{m,m'}$ is:
$$
  \varphi(t^j_{m,m'}) = \delta_{j,0}\,\delta_{m,0}\,\delta_{m',0}.
$$
On products, one computes the Haar state via the Woronowicz--Peter--Weyl orthogonality:
$$
  \varphi\bigl((t^j_{m,n})^* \cdot t^{j'}_{m',n'}\bigr)
  = \frac{\delta_{jj'}\,\delta_{mm'}\,\delta_{nn'}}{[2j+1]_q},
$$
where $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ is the quantum integer.

**Step 3: uniqueness verification.** Any $G_q$-invariant functional $\psi$ satisfies $\psi \circ \mathrm{Ad}(g) = \psi$ for all $g \in G_q$. By the quantum Schur lemma, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ (the adjoint $V_1$ contains no trivial summand). The $G_q$-fixed subalgebra of $\mathcal{A}_\infty$ is $\mathbb{C}$. Normalising $\psi(1) = 1$ forces $\psi = \varphi$. $\square$

**Convergence rate.** The Frobenius traces $\mathrm{tr}_n$ converge to $\varphi$ exponentially. For $f \in A_n$ with spin content $\leq J$:
$$
  |\mathrm{tr}_n(f) - \varphi(f)| = 0
  \quad\text{for all } n \geq J.
$$
The convergence is exact after finitely many steps. The discrete Peter–Weyl decomposition eliminates the need for an $\epsilon$-$\delta$ argument.

**Bring's surface specialisation.** On Bring's QOU at the specific substrate parameter $q_0$ (recorded in the archimedean witness ledger), the Haar state evaluates to:
$$
  \varphi(t^j_{m,m'})
  = \frac{\delta_{j,0}\,\delta_{m,0}\,\delta_{m',0}}{1},
  \qquad
  [2j+1]_{q_0}
  = \frac{q_0^{2j+1} - q_0^{-(2j+1)}}{q_0 - q_0^{-1}}.
$$
For $j = \frac{1}{2}$, one has $[2]_{q_0} = q_0 + q_0^{-1} \approx 2.011$. For $j = 1$, one has $[3]_{q_0} = q_0^2 + 1 + q_0^{-2} \approx 3.044$. These quantum dimensions determine the normalisation of the vacuum state at each spin level.
